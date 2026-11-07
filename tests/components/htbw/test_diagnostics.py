"""Tests for HTBW Core diagnostics (spec SS18.4)."""

from __future__ import annotations

from homeassistant.components.diagnostics import REDACTED
from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry as er
from pytest_homeassistant.common import MockConfigEntry

from custom_components.htbw.const import CONF_ASSIGNMENTS
from custom_components.htbw.diagnostics import async_get_config_entry_diagnostics


async def test_diagnostics_reports_assignment_status(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """Diagnostics reports existence per assignment, and nothing sensitive."""
    entity_registry = er.async_get(hass)
    ok_entry = entity_registry.async_get_or_create("media_player", "test", "diag_ok_speaker")
    room_id = setup_integration.data["room_id"]

    hass.config_entries.async_update_entry(
        setup_integration,
        options={
            CONF_ASSIGNMENTS: [
                {
                    "room_id": room_id,
                    "function": "spoken_response_output",
                    "reference_type": "entity_id",
                    "reference_id": ok_entry.entity_id,
                    "participation_state": "participating",
                    "assigned_at": "2026-01-01T00:00:00+00:00",
                    "updated_at": "2026-01-01T00:00:00+00:00",
                },
                {
                    "room_id": room_id,
                    "function": "voice_input",
                    "reference_type": "entity_id",
                    "reference_id": "assist_satellite.long_removed",
                    "participation_state": "participating",
                    "assigned_at": "2026-01-01T00:00:00+00:00",
                    "updated_at": "2026-01-01T00:00:00+00:00",
                },
            ]
        },
    )
    await hass.async_block_till_done()

    diagnostics = await async_get_config_entry_diagnostics(hass, setup_integration)

    assert diagnostics["domain"] == "htbw"
    assert diagnostics["room_id"] == REDACTED
    assert diagnostics["config_entry_id"] == REDACTED
    assert all(a["reference_id"] == REDACTED for a in diagnostics["assignments"])
    by_function = {a["function"]: a for a in diagnostics["assignments"]}
    assert by_function["spoken_response_output"]["reference_exists"] is True
    assert by_function["spoken_response_output"]["standing_defect"] is False
    assert by_function["voice_input"]["reference_exists"] is False
    assert by_function["voice_input"]["standing_defect"] is True
    assert ok_entry.entity_id not in str(diagnostics)
    assert "assist_satellite.long_removed" not in str(diagnostics)

    # No credentials, tokens, or network information of any kind.
    serialized = str(diagnostics)
    for forbidden in ("token", "password", "secret", "ip_address", "192.168", "10.0.0"):
        assert forbidden not in serialized.lower()

    assert await hass.config_entries.async_unload(setup_integration.entry_id)
    await hass.async_block_till_done()
    assert not hasattr(setup_integration, "runtime_data")
    assert await async_get_config_entry_diagnostics(hass, setup_integration) == diagnostics
