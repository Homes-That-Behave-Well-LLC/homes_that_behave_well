"""Tests for HTBW Core diagnostics (spec SS18.4)."""

from __future__ import annotations

from pathlib import Path

from homeassistant.components.diagnostics import REDACTED
from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry as er
from pytest_homeassistant.common import MockConfigEntry

from custom_components.htbw.const import (
    CONF_EXTERNAL_STORAGE_PATH,
    CONF_RETAIN_ENROLLMENT_RECORDINGS,
)
from custom_components.htbw.diagnostics import async_get_config_entry_diagnostics

from .conftest import DEN_ROOM_ID, den, household_entry, set_den_assignments


async def test_diagnostics_reports_assignment_status(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """Diagnostics reports existence per assignment, and nothing sensitive."""
    entity_registry = er.async_get(hass)
    ok_entry = entity_registry.async_get_or_create("media_player", "test", "diag_ok_speaker")
    room_id = DEN_ROOM_ID

    set_den_assignments(
        hass,
        setup_integration,
        [
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
        ],
    )
    await hass.async_block_till_done()

    diagnostics = await async_get_config_entry_diagnostics(hass, setup_integration)

    assert diagnostics["domain"] == "htbw"
    assert diagnostics["config_entry_id"] == REDACTED
    assert diagnostics["household"]["retain_enrollment_recordings"] == "delete"
    assert diagnostics["household"]["voice_evidence"]["outcome"] == "not_configured"
    assert diagnostics["household"]["external_storage"] == {
        "configured": False,
        "outcome": "not_configured",
        "reason_code": None,
        "root_initialized": False,
    }
    (room,) = diagnostics["rooms"]
    assert room["room_id"] == REDACTED
    assert room["subentry_id"] == REDACTED
    assert room["title"] == den(setup_integration).title
    assert all(a["reference_id"] == REDACTED for a in room["assignments"])
    by_function = {a["function"]: a for a in room["assignments"]}
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
    unloaded = await async_get_config_entry_diagnostics(hass, setup_integration)
    assert unloaded["rooms"] == diagnostics["rooms"]
    assert "outcome" not in unloaded["household"]["voice_evidence"]
    assert unloaded["household"]["external_storage"] == {"configured": False}


async def test_diagnostics_never_export_app_secret_or_host(hass: HomeAssistant) -> None:
    """A provisioned App connection is reported only as provisioned, never its secret or host."""
    secret = "S" * 43
    entry = household_entry(
        data={
            "voice_evidence": {
                "host": "private-voice-evidence-host",
                "port": 8099,
                "api_secret": secret,
                "app_slug": "local_htbw_voice_evidence",
            }
        }
    )
    entry.add_to_hass(hass)
    diagnostics = await async_get_config_entry_diagnostics(hass, entry)
    serialized = str(diagnostics)
    assert secret not in serialized
    assert "private-voice-evidence-host" not in serialized
    assert diagnostics["household"]["voice_evidence"]["connection_provisioned"] is True


async def test_diagnostics_never_export_the_configured_external_storage_path(
    hass: HomeAssistant, tmp_path: Path
) -> None:
    """Spec SS18: configured/outcome/root-initialized only -- never the path itself."""
    entry = household_entry(
        options={
            CONF_RETAIN_ENROLLMENT_RECORDINGS: "delete",
            CONF_EXTERNAL_STORAGE_PATH: str(tmp_path),
        }
    )
    entry.add_to_hass(hass)
    hass.config.allowlist_external_dirs = {str(tmp_path)}
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    diagnostics = await async_get_config_entry_diagnostics(hass, entry)
    assert diagnostics["household"]["external_storage"] == {
        "configured": True,
        "outcome": "available",
        "reason_code": None,
        "root_initialized": True,
    }
    assert str(tmp_path) not in str(diagnostics)
