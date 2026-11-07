"""Tests for the HTBW Core config and options flow."""

from __future__ import annotations

import probatio
import pytest
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResultType
from homeassistant.helpers import area_registry as ar
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.translation import async_get_translations
from pytest_homeassistant.common import MockConfigEntry

from custom_components.htbw.const import (
    CONF_ASSIGNMENTS,
    CONF_ROOM_ID,
    DOMAIN,
    AssignmentResolution,
    InteractionFunction,
)
from custom_components.htbw.foundation import get_room_interaction_assignments

REFERENCE_FIELDS = [
    ("voice_input", "entity_id", "voice_input", "assist_satellite.input"),
    ("spoken_response_output", "entity_id", "spoken_response_output", "media_player.output"),
    ("interface", "device_id", "interface", "native_interface"),
    ("physical_remote", "entity_id", "physical_remote", "remote.controller"),
    ("voice_input", "device_id", "voice_input_devices", "native_input"),
    ("spoken_response_output", "device_id", "spoken_response_output_devices", "native_output"),
    ("physical_remote", "device_id", "physical_remote_devices", "native_remote"),
]


def _prior_version_records(room_id: str) -> list[dict[str, str]]:
    """Literal record shape persisted by 2b1fd6b, independent of the current builder."""
    records = [
        {
            "room_id": room_id,
            "function": function,
            "reference_type": reference_type,
            "reference_id": f"{reference}_{index}",
            "participation_state": "participating",
            "assigned_at": "2026-01-01T00:00:00+00:00",
            "updated_at": "2026-01-02T00:00:00+00:00",
        }
        for function, reference_type, _, reference in REFERENCE_FIELDS
        for index in range(2)
    ]
    records.extend(
        {
            **records[0],
            "reference_id": f"assist_satellite.{state}",
            "participation_state": state,
        }
        for state in ("not_selected", "deliberately_excluded")
    )
    return records


def _suggested_options(schema: probatio.Schema) -> dict[str, dict[str, list[str]]]:
    return {
        group.schema: {
            key.schema: key.description["suggested_value"] for key in fields.schema.schema
        }
        for group, fields in schema.schema.items()
    }


async def test_options_sections_use_native_serialization_and_translations(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """Each function has one translated section with adjacent native alternatives."""
    flow = await hass.config_entries.options.async_init(setup_integration.entry_id)
    fields = probatio.to_field_list(flow["data_schema"], custom_serializer=cv.custom_serializer)
    expected = [
        (
            "voice_input",
            "Voice input",
            [("voice_input", "entity", "Entities"), ("voice_input_devices", "device", "Devices")],
        ),
        (
            "spoken_response_output",
            "Spoken response output",
            [
                ("spoken_response_output", "entity", "Entities"),
                ("spoken_response_output_devices", "device", "Devices"),
            ],
        ),
        ("interface", "Interface", [("interface", "device", "Devices")]),
        (
            "physical_remote",
            "Physical remote",
            [
                ("physical_remote", "entity", "Entities"),
                ("physical_remote_devices", "device", "Devices"),
            ],
        ),
    ]
    assert [field["name"] for field in fields] == [name for name, _, _ in expected]
    translations = await async_get_translations(hass, "en", "options", {DOMAIN})
    visible_labels = []
    for group, (name, title, selectors) in zip(fields, expected, strict=True):
        assert group["type"] == "expandable"
        assert group["expanded"] is True
        prefix = f"component.htbw.options.step.init.sections.{name}"
        assert translations[f"{prefix}.name"] == title
        visible_labels.append(translations[f"{prefix}.name"])
        assert [field["name"] for field in group["schema"]] == [
            field_name for field_name, _, _ in selectors
        ]
        for field, (field_name, kind, label) in zip(group["schema"], selectors, strict=True):
            assert list(field["selector"]) == [kind]
            assert field["selector"][kind]["multiple"] is True
            assert field["description"]["suggested_value"] == []
            assert translations[f"{prefix}.data.{field_name}"] == label
            visible_labels.append(translations[f"{prefix}.data.{field_name}"])
    assert all("_" not in label for label in visible_labels)


@pytest.mark.parametrize(
    "reference_types",
    [("entity_id",), ("device_id",), ("entity_id", "device_id")],
    ids=["entities", "devices", "mixed"],
)
async def test_prior_version_records_populate_save_and_reload_without_loss(
    hass: HomeAssistant, mock_config_entry: MockConfigEntry, reference_types: tuple[str, ...]
) -> None:
    room_id = mock_config_entry.data[CONF_ROOM_ID]
    original = [
        record
        for record in _prior_version_records(room_id)
        if record["reference_type"] in reference_types
        or record["participation_state"] != "participating"
    ]
    mock_config_entry.add_to_hass(hass)
    hass.config_entries.async_update_entry(mock_config_entry, options={CONF_ASSIGNMENTS: original})
    assert await hass.config_entries.async_setup(mock_config_entry.entry_id)
    await hass.async_block_till_done()
    assert [a.to_dict() for a in mock_config_entry.runtime_data.assignments] == original

    flow = await hass.config_entries.options.async_init(mock_config_entry.entry_id)
    suggested = _suggested_options(flow["data_schema"])
    for function, reference_type, field, _ in REFERENCE_FIELDS:
        assert suggested[function][field] == [
            record["reference_id"]
            for record in original
            if record["function"] == function
            and record["reference_type"] == reference_type
            and record["participation_state"] == "participating"
        ]
    result = await hass.config_entries.options.async_configure(flow["flow_id"], suggested)
    assert result["type"] is FlowResultType.CREATE_ENTRY
    await hass.async_block_till_done()
    assert mock_config_entry.options[CONF_ASSIGNMENTS] == original
    assert mock_config_entry.data == {CONF_ROOM_ID: room_id}
    assert mock_config_entry.version == 1
    assert await hass.config_entries.async_reload(mock_config_entry.entry_id)
    await hass.async_block_till_done()
    assert [a.to_dict() for a in mock_config_entry.runtime_data.assignments] == original
    for function in InteractionFunction:
        results = get_room_interaction_assignments(hass, room_id, function)
        assert [result.assignment.to_dict() for result in results] == [
            record
            for record in original
            if record["function"] == function and record["participation_state"] == "participating"
        ]
        assert all(result.status is AssignmentResolution.MISSING for result in results)


@pytest.mark.parametrize(
    ("function", "reference_type", "field", "reference"),
    REFERENCE_FIELDS,
    ids=[field for _, _, field, _ in REFERENCE_FIELDS],
)
async def test_grouped_options_clear_references_without_changing_other_records(
    hass: HomeAssistant,
    setup_integration: MockConfigEntry,
    function: str,
    reference_type: str,
    field: str,
    reference: str,
) -> None:
    original = _prior_version_records(setup_integration.data[CONF_ROOM_ID])
    hass.config_entries.async_update_entry(setup_integration, options={CONF_ASSIGNMENTS: original})
    await hass.async_block_till_done()
    for retained in ([f"{reference}_0"], []):
        flow = await hass.config_entries.options.async_init(setup_integration.entry_id)
        selections = _suggested_options(flow["data_schema"])
        selections[function][field] = retained
        result = await hass.config_entries.options.async_configure(flow["flow_id"], selections)
        assert result["type"] is FlowResultType.CREATE_ENTRY
        await hass.async_block_till_done()
        assert setup_integration.options[CONF_ASSIGNMENTS] == [
            record
            for record in original
            if record["function"] != function
            or record["reference_type"] != reference_type
            or record["participation_state"] != "participating"
            or record["reference_id"] in retained
        ]
        reopened = await hass.config_entries.options.async_init(setup_integration.entry_id)
        assert _suggested_options(reopened["data_schema"])[function][field] == retained
        hass.config_entries.options.async_abort(reopened["flow_id"])


@pytest.fixture
def den_area_id(hass: HomeAssistant) -> str:
    """Create a neutral test Area ("Den") and return its native area_id."""
    area_registry = ar.async_get(hass)
    entry = area_registry.async_create("Den")
    return entry.id


async def test_config_flow_creates_entry_with_voice_input_and_response(
    hass: HomeAssistant, den_area_id: str
) -> None:
    """A room with independently-selected voice_input and spoken_response_output."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] is FlowResultType.FORM
    assert result["step_id"] == "user"
    assert isinstance(result["data_schema"], probatio.Schema)

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {
            "area_id": den_area_id,
            "voice_input": ["assist_satellite.den_satellite"],
            "spoken_response_output": ["media_player.den_speaker"],
        },
    )
    assert result["type"] is FlowResultType.CREATE_ENTRY
    assert result["title"] == "Den"
    assert result["data"][CONF_ROOM_ID] == den_area_id

    assignments = result["options"][CONF_ASSIGNMENTS]
    functions = {a["function"]: a["reference_id"] for a in assignments}
    assert functions["voice_input"] == "assist_satellite.den_satellite"
    assert functions["spoken_response_output"] == "media_player.den_speaker"


async def test_config_flow_room_only_is_valid(hass: HomeAssistant, den_area_id: str) -> None:
    """A Room with none of the four functions configured is a valid state (spec SS5)."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {"area_id": den_area_id}
    )
    assert result["type"] is FlowResultType.CREATE_ENTRY
    assert result["options"][CONF_ASSIGNMENTS] == []


async def test_config_flow_area_not_found_shows_error(hass: HomeAssistant) -> None:
    """An area_id that does not resolve in the registry is a form error, never a guess."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {"area_id": "nonexistent_area"}
    )
    assert result["type"] is FlowResultType.FORM
    assert result["errors"] == {"area_id": "area_not_found"}


async def test_config_flow_duplicate_area_aborts(hass: HomeAssistant, den_area_id: str) -> None:
    """The same Area cannot be configured by a second HTBW Core entry."""
    MockConfigEntry(
        domain=DOMAIN,
        unique_id=den_area_id,
        title="Den",
        data={CONF_ROOM_ID: den_area_id},
        options={CONF_ASSIGNMENTS: []},
    ).add_to_hass(hass)

    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {"area_id": den_area_id}
    )
    assert result["type"] is FlowResultType.ABORT
    assert result["reason"] == "already_configured"


async def test_options_flow_adds_interface_and_physical_remote(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """The two optional functions are configured through Options (spec SS5)."""
    result = await hass.config_entries.options.async_init(setup_integration.entry_id)
    assert result["type"] is FlowResultType.FORM
    assert result["step_id"] == "init"
    assert isinstance(result["data_schema"], probatio.Schema)

    result = await hass.config_entries.options.async_configure(
        result["flow_id"],
        {
            "interface": {"interface": ["device_kiosk_1"]},
            "physical_remote": {"physical_remote": ["remote.den_remote"]},
        },
    )
    assert result["type"] is FlowResultType.CREATE_ENTRY
    functions = {a["function"]: a["reference_id"] for a in result["data"][CONF_ASSIGNMENTS]}
    assert functions["interface"] == "device_kiosk_1"
    assert functions["physical_remote"] == "remote.den_remote"


async def test_options_flow_clearing_a_field_removes_the_assignment(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """Omitting a previously-configured function in Options removes that assignment."""
    hass.config_entries.async_update_entry(
        setup_integration,
        options={
            CONF_ASSIGNMENTS: [
                {
                    "room_id": setup_integration.data[CONF_ROOM_ID],
                    "function": "voice_input",
                    "reference_type": "entity_id",
                    "reference_id": "assist_satellite.den_satellite",
                    "participation_state": "participating",
                    "assigned_at": "2026-01-01T00:00:00+00:00",
                    "updated_at": "2026-01-01T00:00:00+00:00",
                }
            ]
        },
    )
    await hass.async_block_till_done()

    result = await hass.config_entries.options.async_init(setup_integration.entry_id)
    result = await hass.config_entries.options.async_configure(result["flow_id"], {})
    assert result["type"] is FlowResultType.CREATE_ENTRY
    assert result["data"][CONF_ASSIGNMENTS] == []


async def test_multiple_assignments_and_timestamps_survive_options_save(
    hass: HomeAssistant, den_area_id: str
) -> None:
    flow = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    result = await hass.config_entries.flow.async_configure(
        flow["flow_id"],
        {
            "area_id": den_area_id,
            "spoken_response_output": ["media_player.first_output", "media_player.second_output"],
        },
    )
    assert result["type"] is FlowResultType.CREATE_ENTRY
    entry = result["result"]
    await hass.async_block_till_done()
    original = entry.options[CONF_ASSIGNMENTS]
    assert len(original) == 2
    assert {a["reference_id"] for a in original} == {
        "media_player.first_output",
        "media_player.second_output",
    }
    assert all(isinstance(a["reference_id"], str) for a in original)

    flow = await hass.config_entries.options.async_init(entry.entry_id)
    suggested = _suggested_options(flow["data_schema"])
    assert suggested["spoken_response_output"]["spoken_response_output"] == [
        "media_player.first_output",
        "media_player.second_output",
    ]
    result = await hass.config_entries.options.async_configure(
        flow["flow_id"], {"spoken_response_output": suggested["spoken_response_output"]}
    )
    assert result["type"] is FlowResultType.CREATE_ENTRY
    await hass.async_block_till_done()
    assert entry.options[CONF_ASSIGNMENTS] == original
    assert await hass.config_entries.async_reload(entry.entry_id)
    await hass.async_block_till_done()
    assert [a.to_dict() for a in entry.runtime_data.assignments] == original


async def test_options_preserve_excluded_records(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    record = {
        "room_id": setup_integration.data[CONF_ROOM_ID],
        "function": "spoken_response_output",
        "reference_type": "entity_id",
        "reference_id": "media_player.excluded",
        "participation_state": "deliberately_excluded",
        "assigned_at": "2026-01-01T00:00:00+00:00",
        "updated_at": "2026-01-02T00:00:00+00:00",
    }
    hass.config_entries.async_update_entry(setup_integration, options={CONF_ASSIGNMENTS: [record]})
    await hass.async_block_till_done()
    flow = await hass.config_entries.options.async_init(setup_integration.entry_id)
    result = await hass.config_entries.options.async_configure(flow["flow_id"], {})
    assert result["type"] is FlowResultType.CREATE_ENTRY
    assert result["data"][CONF_ASSIGNMENTS] == [record]


async def test_options_do_not_discard_unsupported_native_reference(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    record = {
        "room_id": setup_integration.data[CONF_ROOM_ID],
        "function": "interface",
        "reference_type": "entity_id",
        "reference_id": "sensor.not_a_native_interface_device",
        "participation_state": "participating",
        "assigned_at": "2026-01-01T00:00:00+00:00",
        "updated_at": "2026-01-01T00:00:00+00:00",
    }
    hass.config_entries.async_update_entry(setup_integration, options={CONF_ASSIGNMENTS: [record]})
    await hass.async_block_till_done()
    flow = await hass.config_entries.options.async_init(setup_integration.entry_id)
    result = await hass.config_entries.options.async_configure(flow["flow_id"], {})
    assert result["type"] is FlowResultType.FORM
    assert result["errors"] == {"base": "unsupported_reference_type"}
    assert setup_integration.options[CONF_ASSIGNMENTS] == [record]


async def test_options_support_native_devices_without_fabricated_entities(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    flow = await hass.config_entries.options.async_init(setup_integration.entry_id)
    selections = {
        "voice_input": {"voice_input_devices": ["native_input"]},
        "spoken_response_output": {
            "spoken_response_output": ["media_player.explicit_output"],
            "spoken_response_output_devices": ["native_output"],
        },
        "physical_remote": {"physical_remote_devices": ["native_remote_without_entity"]},
    }
    result = await hass.config_entries.options.async_configure(flow["flow_id"], selections)
    assert result["type"] is FlowResultType.CREATE_ENTRY
    await hass.async_block_till_done()
    records = setup_integration.options[CONF_ASSIGNMENTS]
    assert {(a["function"], a["reference_type"], a["reference_id"]) for a in records} == {
        ("voice_input", "device_id", "native_input"),
        ("spoken_response_output", "entity_id", "media_player.explicit_output"),
        ("spoken_response_output", "device_id", "native_output"),
        ("physical_remote", "device_id", "native_remote_without_entity"),
    }
    reopened = await hass.config_entries.options.async_init(setup_integration.entry_id)
    suggested = _suggested_options(reopened["data_schema"])
    for function, fields in selections.items():
        for key, value in fields.items():
            assert suggested[function][key] == value
