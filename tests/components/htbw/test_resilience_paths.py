"""Defensive and failure paths of the HTBW integration.

These close the Home Assistant Quality Scale `test-coverage` gap (more than 95%
of every module) by exercising the rejection, stale-listener, and recovery
branches directly. Every expectation is existing behavior; nothing here changes
what the integration does.
"""

from __future__ import annotations

import sys
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from homeassistant.config_entries import ConfigEntryState
from homeassistant.core import HomeAssistant
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers import issue_registry as ir
from pytest_homeassistant.common import MockConfigEntry
from pytest_homeassistant.test_util.aiohttp import AiohttpClientMocker

from custom_components.htbw import async_migrate_entry
from custom_components.htbw.const import (
    CONF_MIGRATED_INTO,
    CONF_ROOM_ID,
    DOMAIN,
    ISSUE_VOICE_EVIDENCE_PREFIX,
    VoiceEvidenceOutcome,
)
from custom_components.htbw.diagnostics import async_get_config_entry_diagnostics
from custom_components.htbw.foundation import get_room_assignments, reference_exists
from custom_components.htbw.models import HTBWRuntimeData
from custom_components.htbw.repairs_support import (
    async_check_assignment_health,
    async_project_voice_evidence_issue,
)
from custom_components.htbw.storage import legacy_room_payload
from custom_components.htbw.voice_evidence import (
    MalformedStatusError,
    VoiceEvidenceConnection,
    async_fetch_status,
    async_mirror_retention_to_app,
    parse_status,
)

from .conftest import DEN_ROOM_ID, household_entry, legacy_room_entry, room_subentry_data
from .test_voice_evidence import SECRET, URL, _provisioned, _status

TS = "2026-01-01T00:00:00+00:00"


def _record(reference_type: str, reference_id: str, room_id: str = DEN_ROOM_ID) -> dict[str, Any]:
    return {
        "room_id": room_id,
        "function": "voice_input",
        "reference_type": reference_type,
        "reference_id": reference_id,
        "participation_state": "participating",
        "assigned_at": TS,
        "updated_at": TS,
    }


def _connection() -> VoiceEvidenceConnection:
    return VoiceEvidenceConnection(
        "local-htbw-voice-evidence", 8099, SECRET, "local_htbw_voice_evidence"
    )


def _issues(hass: HomeAssistant) -> set[str]:
    return {issue_id for domain, issue_id in ir.async_get(hass).issues if domain == DOMAIN}


# --- Voice Evidence connection and Contract A validation -------------------


@pytest.mark.parametrize(
    "raw",
    [
        {"host": "h", "port": 8099},
        {"host": "", "port": 8099, "api_secret": SECRET},
        {"host": "h", "port": "not-a-port", "api_secret": SECRET},
        {"host": "h", "port": None, "api_secret": SECRET},
        {"host": "h", "port": 70000, "api_secret": SECRET},
    ],
    ids=["no_secret", "empty_host", "text_port", "missing_port", "port_out_of_range"],
)
def test_invalid_stored_connection_is_not_provisioned(raw: dict[str, Any]) -> None:
    entry = household_entry(data={"voice_evidence": raw})
    assert VoiceEvidenceConnection.from_entry(entry) is None


def test_connection_repr_never_renders_secret_or_host() -> None:
    rendered = repr(_connection())
    assert SECRET not in rendered
    assert "local-htbw-voice-evidence" not in rendered


@pytest.mark.parametrize(
    "payload",
    [
        ["not", "an", "object"],
        _status(app_version=1),
        _status(optional_capabilities="enrollment"),
        _status(retention={"applied_retain_enrollment_recordings": "yes"}),
        _status(voiceprints={"person.tom": True}),
        _status(voiceprints=["person.tom"]),
    ],
    ids=[
        "not_object",
        "non_string_field",
        "capabilities_not_list",
        "retention_not_bool",
        "voiceprints_not_list",
        "voiceprint_not_object",
    ],
)
def test_malformed_status_is_rejected_whole(payload: Any) -> None:
    with pytest.raises(MalformedStatusError):
        parse_status(payload)


async def test_unexpected_http_status_is_unreachable(
    hass: HomeAssistant, aioclient_mock: AiohttpClientMocker
) -> None:
    aioclient_mock.get(URL, status=500)
    outcome, status, reason = await async_fetch_status(hass, _connection())
    assert (outcome, status, reason) == (VoiceEvidenceOutcome.UNREACHABLE, None, "http_500")


async def test_non_json_status_is_incompatible(
    hass: HomeAssistant, aioclient_mock: AiohttpClientMocker
) -> None:
    aioclient_mock.get(URL, text="<html>not contract a</html>")
    outcome, status, reason = await async_fetch_status(hass, _connection())
    assert (outcome, status, reason) == (
        VoiceEvidenceOutcome.INCOMPATIBLE,
        None,
        "malformed_status",
    )


async def test_unset_retention_choice_is_never_pushed(
    hass: HomeAssistant, aioclient_mock: AiohttpClientMocker
) -> None:
    aioclient_mock.get(URL, json=_status())
    entry = _provisioned()
    entry.add_to_hass(hass)
    hass.config_entries.async_update_entry(entry, options={})
    with patch(
        "custom_components.htbw.voice_evidence.async_mirror_retention_to_app", AsyncMock()
    ) as mirror:
        assert await hass.config_entries.async_setup(entry.entry_id)
        await hass.async_block_till_done()
    mirror.assert_not_awaited()
    assert entry.runtime_data.voice_evidence.retention_synchronized is None


async def test_retention_mirror_uses_official_app_options_helper(hass: HomeAssistant) -> None:
    class AddonError(Exception):
        """Stand-in for the hassio helper's error (aiohasupervisor is not a test dependency)."""

    manager = MagicMock()
    manager.async_set_addon_options = AsyncMock()
    hassio = MagicMock(AddonError=AddonError, AddonManager=MagicMock(return_value=manager))
    with (
        patch.object(hass.config, "components", {*hass.config.components, "hassio"}),
        patch.dict(sys.modules, {"homeassistant.components.hassio": hassio}),
    ):
        assert await async_mirror_retention_to_app(hass, _connection(), True) is True
        manager.async_set_addon_options.assert_awaited_once_with(
            {"retain_enrollment_recordings": True}
        )
        manager.async_set_addon_options.side_effect = AddonError("supervisor refused")
        assert await async_mirror_retention_to_app(hass, _connection(), False) is False


# --- Diagnostics -------------------------------------------------------------


async def test_diagnostics_report_contract_summary_with_person_ids_redacted(
    hass: HomeAssistant, aioclient_mock: AiohttpClientMocker
) -> None:
    aioclient_mock.get(URL, json=_status())
    entry = _provisioned()
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    result = await async_get_config_entry_diagnostics(hass, entry)
    voice = result["household"]["voice_evidence"]
    assert voice["outcome"] == "available"
    assert voice["contract"]["contract_version"] == "1.0"
    assert voice["contract"]["voiceprints"][0]["person_id"] == "**REDACTED**"
    rendered = repr(result)
    assert SECRET not in rendered
    assert "person.tom" not in rendered
    assert "local-htbw-voice-evidence" not in rendered


# --- Foundation and Repairs defensive paths ---------------------------------


async def test_unknown_reference_type_never_resolves(hass: HomeAssistant) -> None:
    assert reference_exists(hass, "area_id", "kitchen") is False  # type: ignore[arg-type]


async def test_unloaded_entries_contribute_no_assignments(hass: HomeAssistant) -> None:
    household_entry(
        rooms=[room_subentry_data(DEN_ROOM_ID, "Den", [_record("entity_id", "light.x")])]
    ).add_to_hass(hass)
    assert get_room_assignments(hass, DEN_ROOM_ID) == []


async def test_health_check_without_runtime_data_is_a_no_op(hass: HomeAssistant) -> None:
    entry = household_entry()
    entry.add_to_hass(hass)
    entry.runtime_data = None  # type: ignore[assignment]
    await async_check_assignment_health(hass, entry)
    assert _issues(hass) == set()


async def test_voice_evidence_issue_is_replaced_not_accumulated(hass: HomeAssistant) -> None:
    entry = household_entry()
    entry.add_to_hass(hass)
    async_project_voice_evidence_issue(hass, entry, VoiceEvidenceOutcome.INCOMPATIBLE, "x")
    async_project_voice_evidence_issue(
        hass, entry, VoiceEvidenceOutcome.AUTHENTICATION_FAILED, None
    )
    assert _issues(hass) == {f"{ISSUE_VOICE_EVIDENCE_PREFIX}authentication_failed"}
    async_project_voice_evidence_issue(hass, entry, VoiceEvidenceOutcome.AVAILABLE, None)
    assert _issues(hass) == set()


# --- Lifecycle and migration defensive paths --------------------------------


async def test_device_removal_raises_and_restoration_clears_repair(hass: HomeAssistant) -> None:
    owner = MockConfigEntry(domain="test")
    owner.add_to_hass(hass)
    device = dr.async_get(hass).async_get_or_create(
        config_entry_id=owner.entry_id, identifiers={("test", "den-display")}
    )
    entry = household_entry(
        rooms=[room_subentry_data(DEN_ROOM_ID, "Den", [_record("device_id", device.id)])]
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()
    assert _issues(hass) == set()

    dr.async_get(hass).async_remove_device(device.id)
    await hass.async_block_till_done()
    assert len(_issues(hass)) == 1


async def test_listeners_ignore_events_after_runtime_data_is_replaced(
    hass: HomeAssistant,
) -> None:
    owner = MockConfigEntry(domain="test")
    owner.add_to_hass(hass)
    device = dr.async_get(hass).async_get_or_create(
        config_entry_id=owner.entry_id, identifiers={("test", "den-display")}
    )
    hass.states.async_set("media_player.den", "idle")
    entry = household_entry(
        rooms=[
            room_subentry_data(
                DEN_ROOM_ID,
                "Den",
                [_record("entity_id", "media_player.den"), _record("device_id", device.id)],
            )
        ]
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    entry.runtime_data = HTBWRuntimeData(assignments=[])
    with patch("custom_components.htbw.async_check_assignment_health") as check:
        hass.states.async_remove("media_player.den")
        hass.bus.async_fire(
            er.EVENT_ENTITY_REGISTRY_UPDATED,
            {"action": "remove", "entity_id": "media_player.den"},
        )
        dr.async_get(hass).async_remove_device(device.id)
        await hass.async_block_till_done()
    check.assert_not_called()


async def test_current_version_entry_needs_no_migration(hass: HomeAssistant) -> None:
    entry = household_entry()
    entry.add_to_hass(hass)
    assert await async_migrate_entry(hass, entry) is True
    assert entry.version == 2


async def test_failed_in_place_migration_verification_keeps_entry(hass: HomeAssistant) -> None:
    legacy = legacy_room_entry("den", "Den", [_record("entity_id", "light.x", room_id="den")])
    legacy.add_to_hass(hass)
    with patch("custom_components.htbw._room_subentry", return_value=None):
        await hass.config_entries.async_setup(legacy.entry_id)
        await hass.async_block_till_done()
    assert legacy.state is ConfigEntryState.MIGRATION_ERROR
    assert hass.config_entries.async_get_entry(legacy.entry_id) is not None


async def test_migrated_entry_is_kept_when_household_copy_cannot_be_verified(
    hass: HomeAssistant,
) -> None:
    orphan = MockConfigEntry(
        domain=DOMAIN,
        title="Den",
        unique_id="den",
        version=2,
        minor_version=1,
        data={CONF_ROOM_ID: "den", CONF_MIGRATED_INTO: "missing-household"},
    )
    orphan.add_to_hass(hass)
    assert await hass.config_entries.async_setup(orphan.entry_id)
    await hass.async_block_till_done()
    assert hass.config_entries.async_get_entry(orphan.entry_id) is not None
    assert orphan.state is ConfigEntryState.LOADED


@pytest.mark.parametrize(
    ("room_id", "records"),
    [
        ("", []),
        ("den", [_record("entity_id", "light.x", room_id="office")]),
    ],
    ids=["no_room_id", "record_for_other_room"],
)
def test_invalid_legacy_payload_is_rejected(room_id: str, records: list[dict[str, Any]]) -> None:
    with pytest.raises(ValueError):
        legacy_room_payload(legacy_room_entry(room_id, "Den", records))
