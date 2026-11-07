"""Tests for the HTBW Core config and options flow."""

from __future__ import annotations

import probatio
import pytest
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResultType
from homeassistant.helpers import area_registry as ar
from pytest_homeassistant.common import MockConfigEntry

from custom_components.htbw.const import CONF_ASSIGNMENTS, CONF_ROOM_ID, DOMAIN


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
            "interface": ["device_kiosk_1"],
            "physical_remote": ["remote.den_remote"],
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
    suggested = {
        key.schema: key.description["suggested_value"] for key in flow["data_schema"].schema
    }
    assert suggested["spoken_response_output"] == [
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
        "voice_input_devices": ["native_input"],
        "spoken_response_output": ["media_player.explicit_output"],
        "spoken_response_output_devices": ["native_output"],
        "physical_remote_devices": ["native_remote_without_entity"],
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
    suggested = {
        key.schema: key.description["suggested_value"] for key in reopened["data_schema"].schema
    }
    for key, value in selections.items():
        assert suggested[key] == value
