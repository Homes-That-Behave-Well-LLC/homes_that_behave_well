"""Tests for the HTBW Core config and options flow."""

from __future__ import annotations

import pytest
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResultType
from homeassistant.helpers import area_registry as ar
from pytest_homeassistant_custom_component.common import MockConfigEntry

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

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {
            "area_id": den_area_id,
            "voice_input": "assist_satellite.den_satellite",
            "spoken_response_output": "media_player.den_speaker",
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
    """The two optional functions are configured only through Options (spec SS19/SS20)."""
    result = await hass.config_entries.options.async_init(setup_integration.entry_id)
    assert result["type"] is FlowResultType.FORM
    assert result["step_id"] == "init"

    result = await hass.config_entries.options.async_configure(
        result["flow_id"],
        {
            "interface": "device_kiosk_1",
            "physical_remote": "remote.den_remote",
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
