"""Tests for HTBW Core config, household options, discovery, and Room subentry flows."""

from __future__ import annotations

from pathlib import Path
from typing import Any
from unittest.mock import patch

import probatio
import pytest
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResultType
from homeassistant.helpers import area_registry as ar
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers import issue_registry as ir
from homeassistant.helpers import selector
from homeassistant.helpers.service_info.hassio import HassioServiceInfo
from homeassistant.helpers.translation import async_get_translations
from pytest_homeassistant.common import MockConfigEntry
from pytest_homeassistant.test_util.aiohttp import AiohttpClientMocker

from custom_components.htbw.const import (
    CONF_ASSIGNMENTS,
    CONF_EXTERNAL_STORAGE_PATH,
    CONF_RETAIN_ENROLLMENT_RECORDINGS,
    CONF_ROOM_ID,
    CONF_VOICE_EVIDENCE,
    DOMAIN,
    HOUSEHOLD_UNIQUE_ID,
    SUBENTRY_TYPE_ROOM,
    AssignmentResolution,
    InteractionFunction,
)
from custom_components.htbw.foundation import get_room_interaction_assignments

from .conftest import DEN_ROOM_ID, den, household_entry, set_den_assignments, start_den_reconfigure

REFERENCE_FIELDS = [
    ("voice_input", "entity_id", "voice_input", "assist_satellite.input"),
    ("spoken_response_output", "entity_id", "spoken_response_output", "media_player.output"),
    ("interface", "device_id", "interface", "native_interface"),
    ("physical_remote", "entity_id", "physical_remote", "remote.controller"),
    ("voice_input", "device_id", "voice_input_devices", "native_input"),
    ("spoken_response_output", "device_id", "spoken_response_output_devices", "native_output"),
    ("physical_remote", "device_id", "physical_remote_devices", "native_remote"),
]
SECRET = "A" * 43


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


async def _configure_room(hass: HomeAssistant, flow_id: str, data: dict[str, Any]) -> Any:
    return await hass.config_entries.subentries.async_configure(flow_id, data)


def _assert_reconfigured(result: Any) -> None:
    assert result["type"] is FlowResultType.ABORT
    assert result["reason"] == "reconfigure_successful"


async def _start_add_room(hass: HomeAssistant, entry: MockConfigEntry) -> Any:
    return await hass.config_entries.subentries.async_init(
        (entry.entry_id, SUBENTRY_TYPE_ROOM), context={"source": config_entries.SOURCE_USER}
    )


@pytest.fixture
def den_area_id(hass: HomeAssistant) -> str:
    """Create a neutral test Area ("Living Room") and return its native area_id."""
    return ar.async_get(hass).async_create("Living Room").id


# --- Household entry ---------------------------------------------------------


async def test_user_flow_creates_household_with_explicit_retention_choice(
    hass: HomeAssistant,
) -> None:
    """The household entry records the DL-145 choice first, with no implicit default."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] is FlowResultType.FORM
    assert result["step_id"] == "user"
    key = next(iter(result["data_schema"].schema))
    assert key.schema == CONF_RETAIN_ENROLLMENT_RECORDINGS
    assert key.default is probatio.UNDEFINED

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {CONF_RETAIN_ENROLLMENT_RECORDINGS: "retain"}
    )
    assert result["type"] is FlowResultType.CREATE_ENTRY
    entry = result["result"]
    assert entry.unique_id == HOUSEHOLD_UNIQUE_ID
    assert entry.version == 2
    assert entry.options == {CONF_RETAIN_ENROLLMENT_RECORDINGS: "retain"}
    assert entry.data == {}
    assert entry.subentries == {}


async def test_second_household_entry_is_refused(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] is FlowResultType.ABORT
    assert result["reason"] == "already_configured"
    assert len(hass.config_entries.async_entries(DOMAIN)) == 1


async def test_household_options_change_retention_only(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """The Integration Options Flow holds household settings only, never Room settings."""
    before = den(setup_integration).data
    result = await hass.config_entries.options.async_init(setup_integration.entry_id)
    assert result["type"] is FlowResultType.FORM
    assert [k.schema for k in result["data_schema"].schema] == [
        CONF_RETAIN_ENROLLMENT_RECORDINGS,
        CONF_EXTERNAL_STORAGE_PATH,
    ]
    result = await hass.config_entries.options.async_configure(
        result["flow_id"], {CONF_RETAIN_ENROLLMENT_RECORDINGS: "retain"}
    )
    assert result["type"] is FlowResultType.CREATE_ENTRY
    await hass.async_block_till_done()
    assert setup_integration.options == {
        CONF_RETAIN_ENROLLMENT_RECORDINGS: "retain",
        CONF_EXTERNAL_STORAGE_PATH: "",
    }
    assert den(setup_integration).data == before
    assert CONF_RETAIN_ENROLLMENT_RECORDINGS not in den(setup_integration).data


async def test_household_options_offers_a_dropdown_of_attached_share_storage(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """Spec: pick already-attached Share-usage storage instead of typing it."""
    with patch(
        "custom_components.htbw.config_flow.discover_share_candidates_sync",
        return_value=["/share/nas-mount-1", "/share/nas-mount-2"],
    ):
        result = await hass.config_entries.options.async_init(setup_integration.entry_id)

    storage_field = next(
        key for key in result["data_schema"].schema if key.schema == CONF_EXTERNAL_STORAGE_PATH
    )
    field_selector = result["data_schema"].schema[storage_field]
    assert isinstance(field_selector, selector.SelectSelector)
    assert field_selector.config["custom_value"] is True
    assert field_selector.config["options"] == ["/share/nas-mount-1", "/share/nas-mount-2"]


async def test_household_options_dropdown_includes_a_currently_configured_custom_path(
    hass: HomeAssistant, tmp_path: Path
) -> None:
    """A previously typed path outside /share still appears as the selected option."""
    entry = household_entry(
        options={
            CONF_RETAIN_ENROLLMENT_RECORDINGS: "delete",
            CONF_EXTERNAL_STORAGE_PATH: str(tmp_path),
        }
    )
    entry.add_to_hass(hass)
    with patch(
        "custom_components.htbw.config_flow.discover_share_candidates_sync",
        return_value=["/share/nas-mount-1"],
    ):
        result = await hass.config_entries.options.async_init(entry.entry_id)

    storage_field = next(
        key for key in result["data_schema"].schema if key.schema == CONF_EXTERNAL_STORAGE_PATH
    )
    field_selector = result["data_schema"].schema[storage_field]
    assert isinstance(field_selector, selector.SelectSelector)
    assert str(tmp_path) in field_selector.config["options"]


async def test_household_options_saves_an_unauthorized_path_and_guides_authorization(
    hass: HomeAssistant, setup_integration: MockConfigEntry, tmp_path: Path
) -> None:
    """Spec (#211 remediation, Owner Decision 2026-11-09): the household's choice is

    always saved, even if Home Assistant has not yet allowlisted it -- HTBW explains
    the one-time step through a Repair instead of rejecting the form and making the
    household pick the storage again later.
    """
    result = await hass.config_entries.options.async_init(setup_integration.entry_id)
    result = await hass.config_entries.options.async_configure(
        result["flow_id"],
        {
            CONF_RETAIN_ENROLLMENT_RECORDINGS: "retain",
            CONF_EXTERNAL_STORAGE_PATH: str(tmp_path),
        },
    )
    assert result["type"] is FlowResultType.CREATE_ENTRY
    await hass.async_block_till_done()
    assert setup_integration.options[CONF_EXTERNAL_STORAGE_PATH] == str(tmp_path)

    issue = ir.async_get(hass).async_get_issue(DOMAIN, "external_storage_path_not_allowed")
    assert issue is not None
    assert issue.translation_placeholders is not None
    assert issue.translation_placeholders["path"] == str(tmp_path)
    assert issue.learn_more_url is not None
    assert "htbw-in-home-assistant.md" in issue.learn_more_url

    # The dropdown still shows the saved (not-yet-authorized) path as the current
    # selection -- the household never has to choose it again.
    result = await hass.config_entries.options.async_init(setup_integration.entry_id)
    storage_field = next(
        key for key in result["data_schema"].schema if key.schema == CONF_EXTERNAL_STORAGE_PATH
    )
    assert storage_field.default() == str(tmp_path)


async def test_household_options_rejects_a_media_usage_path(
    hass: HomeAssistant, setup_integration: MockConfigEntry, tmp_path: Path
) -> None:
    """A Media-usage path never silently substitutes for Share (spec SS5/SS17/SS25)."""
    hass.config.allowlist_external_dirs = {str(tmp_path)}
    hass.config.media_dirs = {"local": str(tmp_path)}
    result = await hass.config_entries.options.async_init(setup_integration.entry_id)
    result = await hass.config_entries.options.async_configure(
        result["flow_id"],
        {
            CONF_RETAIN_ENROLLMENT_RECORDINGS: "retain",
            CONF_EXTERNAL_STORAGE_PATH: str(tmp_path),
        },
    )
    assert result["type"] is FlowResultType.FORM
    assert result["errors"] == {CONF_EXTERNAL_STORAGE_PATH: "media_path_not_supported"}


def _discovery(**config: Any) -> HassioServiceInfo:
    return HassioServiceInfo(
        config={"host": "local-htbw-voice-evidence", "port": 8099, "api_secret": SECRET, **config},
        name="HTBW Voice Evidence",
        slug="local_htbw_voice_evidence",
        uuid="discovery-uuid",
    )


async def test_discovery_creates_household_after_retention_choice(
    hass: HomeAssistant, aioclient_mock: AiohttpClientMocker
) -> None:
    aioclient_mock.get(
        "http://local-htbw-voice-evidence:8099/v1/status", exc=ConnectionError("not running")
    )
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_HASSIO}, data=_discovery()
    )
    assert result["type"] is FlowResultType.FORM
    assert result["step_id"] == "hassio_confirm"
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {CONF_RETAIN_ENROLLMENT_RECORDINGS: "delete"}
    )
    assert result["type"] is FlowResultType.CREATE_ENTRY
    entry = result["result"]
    assert entry.data[CONF_VOICE_EVIDENCE] == {
        "host": "local-htbw-voice-evidence",
        "port": 8099,
        "api_secret": SECRET,
        "app_slug": "local_htbw_voice_evidence",
    }
    assert entry.options == {CONF_RETAIN_ENROLLMENT_RECORDINGS: "delete"}


async def test_repeated_discovery_reconciles_the_one_household_entry(
    hass: HomeAssistant, setup_integration: MockConfigEntry, aioclient_mock: AiohttpClientMocker
) -> None:
    """Discovery is idempotent: it updates the App connection, never adds an entry."""
    aioclient_mock.get(
        "http://local-htbw-voice-evidence:8099/v1/status", exc=ConnectionError("not running")
    )
    for secret in (SECRET, "B" * 43, "B" * 43):
        result = await hass.config_entries.flow.async_init(
            DOMAIN,
            context={"source": config_entries.SOURCE_HASSIO},
            data=_discovery(api_secret=secret),
        )
        assert result["type"] is FlowResultType.ABORT
        assert result["reason"] == "already_configured"
        await hass.async_block_till_done()
        assert setup_integration.data[CONF_VOICE_EVIDENCE]["api_secret"] == secret
    assert len(hass.config_entries.async_entries(DOMAIN)) == 1
    assert [s.unique_id for s in setup_integration.subentries.values()] == [DEN_ROOM_ID]
    assert CONF_VOICE_EVIDENCE not in den(setup_integration).data


@pytest.mark.parametrize(
    "config",
    [{"api_secret": "short"}, {"api_secret": None}, {"host": ""}, {"port": "x"}, {"port": 0}],
)
async def test_invalid_discovery_is_rejected(hass: HomeAssistant, config: dict[str, Any]) -> None:
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_HASSIO}, data=_discovery(**config)
    )
    assert result["type"] is FlowResultType.ABORT
    assert result["reason"] == "invalid_discovery_info"
    assert hass.config_entries.async_entries(DOMAIN) == []


# --- Room subentries (#201 behaviour, unchanged) ------------------------------


async def test_room_reconfigure_sections_use_native_serialization_and_translations(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """Each function has one translated section with adjacent native alternatives."""
    flow = await start_den_reconfigure(hass, setup_integration)
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
    translations = await async_get_translations(hass, "en", "config_subentries", {DOMAIN})
    visible_labels = []
    for group, (name, title, selectors) in zip(fields, expected, strict=True):
        assert group["type"] == "expandable"
        assert group["expanded"] is True
        prefix = f"component.htbw.config_subentries.room.step.reconfigure.sections.{name}"
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
    original = [
        record
        for record in _prior_version_records(DEN_ROOM_ID)
        if record["reference_type"] in reference_types
        or record["participation_state"] != "participating"
    ]
    mock_config_entry.add_to_hass(hass)
    set_den_assignments(hass, mock_config_entry, original)
    assert await hass.config_entries.async_setup(mock_config_entry.entry_id)
    await hass.async_block_till_done()
    assert [a.to_dict() for a in mock_config_entry.runtime_data.assignments] == original

    flow = await start_den_reconfigure(hass, mock_config_entry)
    suggested = _suggested_options(flow["data_schema"])
    for function, reference_type, field, _ in REFERENCE_FIELDS:
        assert suggested[function][field] == [
            record["reference_id"]
            for record in original
            if record["function"] == function
            and record["reference_type"] == reference_type
            and record["participation_state"] == "participating"
        ]
    _assert_reconfigured(await _configure_room(hass, flow["flow_id"], suggested))
    await hass.async_block_till_done()
    assert den(mock_config_entry).data[CONF_ASSIGNMENTS] == original
    assert den(mock_config_entry).data[CONF_ROOM_ID] == DEN_ROOM_ID
    assert mock_config_entry.version == 2
    assert await hass.config_entries.async_reload(mock_config_entry.entry_id)
    await hass.async_block_till_done()
    assert [a.to_dict() for a in mock_config_entry.runtime_data.assignments] == original
    for function in InteractionFunction:
        results = get_room_interaction_assignments(hass, DEN_ROOM_ID, function)
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
async def test_grouped_reconfigure_clears_references_without_changing_other_records(
    hass: HomeAssistant,
    setup_integration: MockConfigEntry,
    function: str,
    reference_type: str,
    field: str,
    reference: str,
) -> None:
    original = _prior_version_records(DEN_ROOM_ID)
    set_den_assignments(hass, setup_integration, original)
    await hass.async_block_till_done()
    for retained in ([f"{reference}_0"], []):
        flow = await start_den_reconfigure(hass, setup_integration)
        selections = _suggested_options(flow["data_schema"])
        selections[function][field] = retained
        _assert_reconfigured(await _configure_room(hass, flow["flow_id"], selections))
        await hass.async_block_till_done()
        assert den(setup_integration).data[CONF_ASSIGNMENTS] == [
            record
            for record in original
            if record["function"] != function
            or record["reference_type"] != reference_type
            or record["participation_state"] != "participating"
            or record["reference_id"] in retained
        ]
        reopened = await start_den_reconfigure(hass, setup_integration)
        assert _suggested_options(reopened["data_schema"])[function][field] == retained
        hass.config_entries.subentries.async_abort(reopened["flow_id"])


async def test_add_room_with_voice_input_and_response(
    hass: HomeAssistant, setup_integration: MockConfigEntry, den_area_id: str
) -> None:
    """A Room with independently-selected voice_input and spoken_response_output."""
    result = await _start_add_room(hass, setup_integration)
    assert result["type"] is FlowResultType.FORM
    assert result["step_id"] == "user"
    assert isinstance(result["data_schema"], probatio.Schema)

    result = await _configure_room(
        hass,
        result["flow_id"],
        {
            "area_id": den_area_id,
            "voice_input": ["assist_satellite.den_satellite"],
            "spoken_response_output": ["media_player.den_speaker"],
        },
    )
    assert result["type"] is FlowResultType.CREATE_ENTRY
    assert result["title"] == "Living Room"
    assert result["unique_id"] == den_area_id
    assert result["data"][CONF_ROOM_ID] == den_area_id
    functions = {a["function"]: a["reference_id"] for a in result["data"][CONF_ASSIGNMENTS]}
    assert functions["voice_input"] == "assist_satellite.den_satellite"
    assert functions["spoken_response_output"] == "media_player.den_speaker"
    await hass.async_block_till_done()
    assert {s.unique_id for s in setup_integration.subentries.values()} == {
        DEN_ROOM_ID,
        den_area_id,
    }
    assert len(hass.config_entries.async_entries(DOMAIN)) == 1


async def test_add_room_only_is_valid(
    hass: HomeAssistant, setup_integration: MockConfigEntry, den_area_id: str
) -> None:
    """A Room with none of the four functions configured is a valid state (spec SS5)."""
    result = await _start_add_room(hass, setup_integration)
    result = await _configure_room(hass, result["flow_id"], {"area_id": den_area_id})
    assert result["type"] is FlowResultType.CREATE_ENTRY
    assert result["data"][CONF_ASSIGNMENTS] == []


async def test_add_room_area_not_found_shows_error(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """An area_id that does not resolve in the registry is a form error, never a guess."""
    result = await _start_add_room(hass, setup_integration)
    result = await _configure_room(hass, result["flow_id"], {"area_id": "nonexistent_area"})
    assert result["type"] is FlowResultType.FORM
    assert result["errors"] == {"area_id": "area_not_found"}

    office = ar.async_get(hass).async_create("Office")
    result = await _configure_room(hass, result["flow_id"], {"area_id": office.id})
    assert result["type"] is FlowResultType.CREATE_ENTRY
    assert result["title"] == "Office"


async def test_add_room_duplicate_area_aborts(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """The same Area cannot be configured as a second Room."""
    result = await _start_add_room(hass, setup_integration)
    result = await _configure_room(hass, result["flow_id"], {"area_id": DEN_ROOM_ID})
    assert result["type"] is FlowResultType.ABORT
    assert result["reason"] == "already_configured"


async def test_reconfigure_adds_interface_and_physical_remote(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """The two optional functions are configured by reconfiguring the Room (spec SS5)."""
    result = await start_den_reconfigure(hass, setup_integration)
    assert result["type"] is FlowResultType.FORM
    assert result["step_id"] == "reconfigure"
    assert isinstance(result["data_schema"], probatio.Schema)

    result = await _configure_room(
        hass,
        result["flow_id"],
        {
            "interface": {"interface": ["device_kiosk_1"]},
            "physical_remote": {"physical_remote": ["remote.den_remote"]},
        },
    )
    _assert_reconfigured(result)
    await hass.async_block_till_done()
    functions = {
        a["function"]: a["reference_id"] for a in den(setup_integration).data[CONF_ASSIGNMENTS]
    }
    assert functions["interface"] == "device_kiosk_1"
    assert functions["physical_remote"] == "remote.den_remote"


async def test_reconfigure_clearing_a_field_removes_the_assignment(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """Omitting a previously-configured function removes that assignment."""
    set_den_assignments(
        hass,
        setup_integration,
        [
            {
                "room_id": DEN_ROOM_ID,
                "function": "voice_input",
                "reference_type": "entity_id",
                "reference_id": "assist_satellite.den_satellite",
                "participation_state": "participating",
                "assigned_at": "2026-01-01T00:00:00+00:00",
                "updated_at": "2026-01-01T00:00:00+00:00",
            }
        ],
    )
    await hass.async_block_till_done()

    result = await start_den_reconfigure(hass, setup_integration)
    _assert_reconfigured(await _configure_room(hass, result["flow_id"], {}))
    await hass.async_block_till_done()
    assert den(setup_integration).data[CONF_ASSIGNMENTS] == []


async def test_multiple_assignments_and_timestamps_survive_reconfigure_save(
    hass: HomeAssistant, setup_integration: MockConfigEntry, den_area_id: str
) -> None:
    flow = await _start_add_room(hass, setup_integration)
    result = await _configure_room(
        hass,
        flow["flow_id"],
        {
            "area_id": den_area_id,
            "spoken_response_output": ["media_player.first_output", "media_player.second_output"],
        },
    )
    assert result["type"] is FlowResultType.CREATE_ENTRY
    await hass.async_block_till_done()
    room = next(s for s in setup_integration.subentries.values() if s.unique_id == den_area_id)
    original = room.data[CONF_ASSIGNMENTS]
    assert len(original) == 2
    assert {a["reference_id"] for a in original} == {
        "media_player.first_output",
        "media_player.second_output",
    }
    assert all(isinstance(a["reference_id"], str) for a in original)

    flow = await hass.config_entries.subentries.async_init(
        (setup_integration.entry_id, SUBENTRY_TYPE_ROOM),
        context={"source": config_entries.SOURCE_RECONFIGURE, "subentry_id": room.subentry_id},
    )
    suggested = _suggested_options(flow["data_schema"])
    assert suggested["spoken_response_output"]["spoken_response_output"] == [
        "media_player.first_output",
        "media_player.second_output",
    ]
    _assert_reconfigured(
        await _configure_room(
            hass, flow["flow_id"], {"spoken_response_output": suggested["spoken_response_output"]}
        )
    )
    await hass.async_block_till_done()
    assert setup_integration.subentries[room.subentry_id].data[CONF_ASSIGNMENTS] == original
    assert await hass.config_entries.async_reload(setup_integration.entry_id)
    await hass.async_block_till_done()
    assert [a.to_dict() for a in setup_integration.runtime_data.rooms[room.subentry_id]] == original


async def test_reconfigure_preserves_excluded_records(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    record = {
        "room_id": DEN_ROOM_ID,
        "function": "spoken_response_output",
        "reference_type": "entity_id",
        "reference_id": "media_player.excluded",
        "participation_state": "deliberately_excluded",
        "assigned_at": "2026-01-01T00:00:00+00:00",
        "updated_at": "2026-01-02T00:00:00+00:00",
    }
    set_den_assignments(hass, setup_integration, [record])
    await hass.async_block_till_done()
    flow = await start_den_reconfigure(hass, setup_integration)
    _assert_reconfigured(await _configure_room(hass, flow["flow_id"], {}))
    await hass.async_block_till_done()
    assert den(setup_integration).data[CONF_ASSIGNMENTS] == [record]


async def test_reconfigure_does_not_discard_unsupported_native_reference(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    record = {
        "room_id": DEN_ROOM_ID,
        "function": "interface",
        "reference_type": "entity_id",
        "reference_id": "sensor.not_a_native_interface_device",
        "participation_state": "participating",
        "assigned_at": "2026-01-01T00:00:00+00:00",
        "updated_at": "2026-01-01T00:00:00+00:00",
    }
    set_den_assignments(hass, setup_integration, [record])
    await hass.async_block_till_done()
    flow = await start_den_reconfigure(hass, setup_integration)
    result = await _configure_room(hass, flow["flow_id"], {})
    assert result["type"] is FlowResultType.FORM
    assert result["errors"] == {"base": "unsupported_reference_type"}
    assert den(setup_integration).data[CONF_ASSIGNMENTS] == [record]


async def test_reconfigure_supports_native_devices_without_fabricated_entities(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    flow = await start_den_reconfigure(hass, setup_integration)
    selections = {
        "voice_input": {"voice_input_devices": ["native_input"]},
        "spoken_response_output": {
            "spoken_response_output": ["media_player.explicit_output"],
            "spoken_response_output_devices": ["native_output"],
        },
        "physical_remote": {"physical_remote_devices": ["native_remote_without_entity"]},
    }
    _assert_reconfigured(await _configure_room(hass, flow["flow_id"], selections))
    await hass.async_block_till_done()
    records = den(setup_integration).data[CONF_ASSIGNMENTS]
    assert {(a["function"], a["reference_type"], a["reference_id"]) for a in records} == {
        ("voice_input", "device_id", "native_input"),
        ("spoken_response_output", "entity_id", "media_player.explicit_output"),
        ("spoken_response_output", "device_id", "native_output"),
        ("physical_remote", "device_id", "native_remote_without_entity"),
    }
    reopened = await start_den_reconfigure(hass, setup_integration)
    suggested = _suggested_options(reopened["data_schema"])
    for function, fields in selections.items():
        for key, value in fields.items():
            assert suggested[function][key] == value
