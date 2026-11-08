"""Voice Evidence App boundary on the Integration side (Issue #162).

The App is an optional DL-41 dependency. Absent, unreachable, rejected,
incompatible, and not-ready are distinct outcomes; none fails the household
entry or any Room, none is emulated, and every call is time-bounded.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any
from unittest.mock import AsyncMock, patch

import pytest
from homeassistant.config_entries import ConfigEntryState
from homeassistant.core import HomeAssistant
from homeassistant.helpers import issue_registry as ir
from pytest_homeassistant.common import MockConfigEntry
from pytest_homeassistant.test_util.aiohttp import AiohttpClientMocker

from custom_components.htbw.const import (
    CONF_RETAIN_ENROLLMENT_RECORDINGS,
    DOMAIN,
    VOICE_EVIDENCE_UNREACHABLE_ISSUE_THRESHOLD,
    InteractionFunction,
    VoiceEvidenceOutcome,
)
from custom_components.htbw.foundation import get_room_interaction_assignments

from .conftest import DEN_ROOM_ID, household_entry, room_subentry_data

SECRET = "Z" * 43
URL = "http://local-htbw-voice-evidence:8099/v1/status"
INTEGRATION_DIR = Path(__file__).parents[3] / "custom_components" / "htbw"


def _status(**overrides: Any) -> dict[str, Any]:
    payload = {
        "contract_version": "1.0",
        "app_version": "0.1.0",
        "status": "available",
        "reason_code": None,
        "compatibility_id": "cmp-1",
        "encoder_family": "wespeaker_ecapa_tdnn",
        "encoder_version": "ecapa512_lm",
        "audio_contract_version": "pcm_s16le_16k_mono_v1",
        "model_artifact": {"state": "valid", "model_id": "m", "revision": "r", "sha256": "0" * 64},
        "storage": {"state": "available"},
        "optional_capabilities": [],
        "retention": {"applied_retain_enrollment_recordings": False},
        "voiceprints": [
            {
                "person_id": "person.tom",
                "voiceprint_exists": True,
                "voiceprint_state": "current",
                "retained_recordings": False,
            }
        ],
    }
    payload.update(overrides)
    return payload


def _provisioned(retain: str = "delete") -> MockConfigEntry:
    room = room_subentry_data(
        DEN_ROOM_ID,
        "Den",
        [
            {
                "room_id": DEN_ROOM_ID,
                "function": "voice_input",
                "reference_type": "entity_id",
                "reference_id": "assist_satellite.den",
                "participation_state": "participating",
                "assigned_at": "2026-01-01T00:00:00+00:00",
                "updated_at": "2026-01-01T00:00:00+00:00",
            }
        ],
    )
    return household_entry(
        rooms=[room],
        data={
            "voice_evidence": {
                "host": "local-htbw-voice-evidence",
                "port": 8099,
                "api_secret": SECRET,
                "app_slug": "local_htbw_voice_evidence",
            }
        },
        options={CONF_RETAIN_ENROLLMENT_RECORDINGS: retain},
    )


async def _setup(hass: HomeAssistant, entry: MockConfigEntry) -> Any:
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()
    assert entry.state is ConfigEntryState.LOADED
    return entry.runtime_data.voice_evidence


def _rooms_still_work(hass: HomeAssistant) -> None:
    (result,) = get_room_interaction_assignments(hass, DEN_ROOM_ID, InteractionFunction.VOICE_INPUT)
    assert result.assignment.reference_id == "assist_satellite.den"


def _voice_issues(hass: HomeAssistant) -> list[str]:
    return [
        issue_id
        for domain, issue_id in ir.async_get(hass).issues
        if domain == DOMAIN and issue_id.startswith("voice_evidence_")
    ]


async def test_app_absent_is_not_configured_and_quiet(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    manager = setup_integration.runtime_data.voice_evidence
    assert manager.outcome is VoiceEvidenceOutcome.NOT_CONFIGURED
    assert manager.voiceprint_exists("person.tom") is None
    assert _voice_issues(hass) == []


async def test_app_unreachable_loads_and_reports_after_it_persists(
    hass: HomeAssistant, aioclient_mock: AiohttpClientMocker
) -> None:
    aioclient_mock.get(URL, exc=ConnectionError("refused"))
    manager = await _setup(hass, _provisioned())
    assert manager.outcome is VoiceEvidenceOutcome.UNREACHABLE
    assert manager.reason_code == "connection_failed"
    assert manager.voiceprint_exists("person.tom") is None
    _rooms_still_work(hass)
    assert _voice_issues(hass) == []
    for _ in range(VOICE_EVIDENCE_UNREACHABLE_ISSUE_THRESHOLD - 1):
        await manager.async_refresh()
    assert _voice_issues(hass) == ["voice_evidence_unreachable"]


async def test_app_timeout_is_bounded_and_unreachable(
    hass: HomeAssistant, aioclient_mock: AiohttpClientMocker
) -> None:
    aioclient_mock.get(URL, exc=TimeoutError())
    manager = await _setup(hass, _provisioned())
    assert manager.outcome is VoiceEvidenceOutcome.UNREACHABLE
    assert manager.reason_code == "timeout"
    _rooms_still_work(hass)


async def test_rejected_credential_is_authentication_failed(
    hass: HomeAssistant, aioclient_mock: AiohttpClientMocker
) -> None:
    aioclient_mock.get(URL, status=401, json={"error": "unauthorized"})
    manager = await _setup(hass, _provisioned())
    assert manager.outcome is VoiceEvidenceOutcome.AUTHENTICATION_FAILED
    assert _voice_issues(hass) == ["voice_evidence_authentication_failed"]
    _rooms_still_work(hass)


@pytest.mark.parametrize(
    ("payload", "reason"),
    [
        (_status(contract_version="2.0"), "contract_version_mismatch"),
        (_status(status="incompatible", reason_code="model_incompatible"), "model_incompatible"),
        ({"contract_version": "1.0"}, "malformed_status"),
        (_status(voiceprints=[{"person_id": "p", "voiceprint_exists": "yes"}]), "malformed_status"),
    ],
    ids=["major_mismatch", "app_incompatible", "missing_status", "bad_voiceprint"],
)
async def test_incompatible_app_is_distinct_and_rejected_whole(
    hass: HomeAssistant, aioclient_mock: AiohttpClientMocker, payload: Any, reason: str
) -> None:
    aioclient_mock.get(URL, json=payload)
    manager = await _setup(hass, _provisioned())
    assert manager.outcome is VoiceEvidenceOutcome.INCOMPATIBLE
    assert manager.reason_code == reason
    assert manager.voiceprint_exists("person.tom") is None
    assert _voice_issues(hass) == ["voice_evidence_incompatible"]
    _rooms_still_work(hass)


async def test_app_not_ready_is_app_unavailable(
    hass: HomeAssistant, aioclient_mock: AiohttpClientMocker
) -> None:
    aioclient_mock.get(URL, json=_status(status="unavailable", reason_code="model_digest_mismatch"))
    manager = await _setup(hass, _provisioned())
    assert manager.outcome is VoiceEvidenceOutcome.APP_UNAVAILABLE
    assert manager.reason_code == "model_digest_mismatch"
    assert manager.voiceprint_exists("person.tom") is None
    assert _voice_issues(hass) == ["voice_evidence_app_unavailable"]


async def test_available_app_synchronizes_existence_without_storing_biometrics(
    hass: HomeAssistant, aioclient_mock: AiohttpClientMocker, caplog: pytest.LogCaptureFixture
) -> None:
    caplog.set_level(logging.DEBUG)
    aioclient_mock.get(URL, json=_status())
    entry = _provisioned()
    manager = await _setup(hass, entry)

    assert manager.outcome is VoiceEvidenceOutcome.AVAILABLE
    assert manager.voiceprint_exists("person.tom") is True
    assert manager.voiceprint_exists("person.unknown") is False
    assert _voice_issues(hass) == []

    (_, _, _, headers) = aioclient_mock.mock_calls[0]
    assert headers["Authorization"] == f"Bearer {SECRET}"
    assert SECRET not in caplog.text
    assert SECRET not in repr(manager)

    persisted = json.dumps(
        {"data": dict(entry.data), "options": dict(entry.options)}
        | {"subentries": [dict(s.data) for s in entry.subentries.values()]},
        default=str,
    )
    for forbidden in ("voiceprint", "embedding", "person.tom", "match_level"):
        assert forbidden not in persisted


async def test_retention_is_mirrored_into_app_options_when_it_differs(
    hass: HomeAssistant, aioclient_mock: AiohttpClientMocker
) -> None:
    aioclient_mock.get(URL, json=_status(retention={"applied_retain_enrollment_recordings": False}))
    with patch(
        "custom_components.htbw.voice_evidence.async_mirror_retention_to_app",
        AsyncMock(return_value=True),
    ) as mirror:
        manager = await _setup(hass, _provisioned(retain="retain"))
    mirror.assert_awaited_once()
    assert mirror.await_args.args[2] is True
    assert manager.retention_synchronized is False
    assert _voice_issues(hass) == []


async def test_retention_already_applied_is_not_rewritten(
    hass: HomeAssistant, aioclient_mock: AiohttpClientMocker
) -> None:
    aioclient_mock.get(URL, json=_status(retention={"applied_retain_enrollment_recordings": True}))
    with patch(
        "custom_components.htbw.voice_evidence.async_mirror_retention_to_app", AsyncMock()
    ) as mirror:
        manager = await _setup(hass, _provisioned(retain="retain"))
    mirror.assert_not_awaited()
    assert manager.retention_synchronized is True


async def test_retention_mirror_failure_is_reported(
    hass: HomeAssistant, aioclient_mock: AiohttpClientMocker
) -> None:
    """Without Supervisor the official app-options helper is unavailable; this is reported."""
    aioclient_mock.get(URL, json=_status())
    await _setup(hass, _provisioned(retain="retain"))
    assert _voice_issues(hass) == ["voice_evidence_retention_sync_failed"]


def test_manifest_carries_no_optional_heavy_requirement() -> None:
    manifest = json.loads((INTEGRATION_DIR / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["requirements"] == []
    assert manifest["dependencies"] == []


def test_integration_never_imports_or_embeds_the_app() -> None:
    """Source co-location never becomes runtime coupling or a local encoder fallback."""
    for path in INTEGRATION_DIR.rglob("*.py"):
        source = path.read_text(encoding="utf-8")
        for forbidden in ("htbw_voice_evidence", "onnxruntime", "numpy", "wespeaker", "apps."):
            assert forbidden not in source, f"{path.name} references {forbidden}"
