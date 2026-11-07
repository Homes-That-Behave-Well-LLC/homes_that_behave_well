"""Tests for HTBW Core config-entry setup, unload, and reload."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntryState
from homeassistant.core import HomeAssistant
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.htbw.const import CONF_ASSIGNMENTS


async def test_setup_and_unload_entry(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """The entry loads cleanly and unloads cleanly, with no entities created."""
    assert setup_integration.state is ConfigEntryState.LOADED
    assert setup_integration.runtime_data is not None
    assert setup_integration.runtime_data.assignments == []

    assert await hass.config_entries.async_unload(setup_integration.entry_id)
    await hass.async_block_till_done()
    assert setup_integration.state is ConfigEntryState.NOT_LOADED


async def test_assignments_persist_across_reload(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """Configured assignments survive an options update / reload (spec SS20)."""
    room_id = setup_integration.data["room_id"]
    hass.config_entries.async_update_entry(
        setup_integration,
        options={
            CONF_ASSIGNMENTS: [
                {
                    "room_id": room_id,
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

    assert setup_integration.state is ConfigEntryState.LOADED
    assert len(setup_integration.runtime_data.assignments) == 1
    assert setup_integration.runtime_data.assignments[0].reference_id == (
        "assist_satellite.den_satellite"
    )
