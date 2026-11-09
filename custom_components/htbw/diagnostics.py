"""Diagnostics support for HTBW Core.

Spec SS18.4: for each RoomInteractionFunctionAssignment record, whether its
reference still resolves (existence, not current availability). Issue #162
adds the household's Integration-scoped state: the retention choice and the
Voice Evidence App's DL-41 outcome and Contract A summary. Reuses Home
Assistant's native diagnostics platform; does not invent a new health model.

Only explicitly selected fields are exported. Native identifiers, the App host,
and person identifiers are redacted; the App secret is never read here at all.
No biometric material exists in this integration to export.
"""

from __future__ import annotations

from typing import Any

from homeassistant.components.diagnostics import async_redact_data
from homeassistant.core import HomeAssistant

from .const import CONF_RETAIN_ENROLLMENT_RECORDINGS, DOMAIN, ParticipationState
from .external_storage import ExternalStorageManager
from .foundation import reference_exists
from .models import HTBWConfigEntry
from .storage import load_assignments, room_subentries
from .voice_evidence import VoiceEvidenceConnection, VoiceEvidenceManager

TO_REDACT = {"config_entry_id", "room_id", "reference_id", "subentry_id", "person_id"}


def _external_storage_diagnostics(entry: HTBWConfigEntry) -> dict[str, Any]:
    """Report health only. The configured path is never included (connected-storage.md:

    "physical storage paths are not exposed... where a governed identifier suffices").
    """
    manager = getattr(getattr(entry, "runtime_data", None), "external_storage", None)
    if not isinstance(manager, ExternalStorageManager):
        return {"configured": False}
    return {
        "configured": manager.outcome.value != "not_configured",
        "outcome": manager.outcome.value,
        "reason_code": manager.reason_code,
        "root_initialized": manager.is_available(),
    }


def _voice_evidence_diagnostics(entry: HTBWConfigEntry) -> dict[str, Any]:
    connection = VoiceEvidenceConnection.from_entry(entry)
    manager = getattr(getattr(entry, "runtime_data", None), "voice_evidence", None)
    result: dict[str, Any] = {
        "connection_provisioned": connection is not None,
        "provisioned_by_supervisor_discovery": bool(connection and connection.app_slug),
    }
    if not isinstance(manager, VoiceEvidenceManager):
        return result
    result["outcome"] = manager.outcome.value
    result["reason_code"] = manager.reason_code
    result["retention_synchronized"] = manager.retention_synchronized
    status = manager.status
    if status is not None:
        result["contract"] = {
            "contract_version": status.contract_version,
            "app_version": status.app_version,
            "status": status.status,
            "reason_code": status.reason_code,
            "compatibility_id": status.compatibility_id,
            "encoder_family": status.encoder_family,
            "encoder_version": status.encoder_version,
            "audio_contract_version": status.audio_contract_version,
            "model_state": status.model_state,
            "optional_capabilities": list(status.optional_capabilities),
            "applied_retain_enrollment_recordings": status.applied_retain_enrollment_recordings,
            "voiceprints": [
                {
                    "person_id": v.person_id,
                    "voiceprint_exists": v.voiceprint_exists,
                    "voiceprint_state": v.voiceprint_state,
                    "retained_recordings": v.retained_recordings,
                }
                for v in status.voiceprints
            ],
        }
    return result


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: HTBWConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for the household entry and its Room subentries."""
    rooms_diag: list[dict[str, Any]] = []
    for subentry in room_subentries(entry):
        assignments_diag: list[dict[str, Any]] = []
        for assignment in load_assignments(subentry):
            exists = reference_exists(hass, assignment.reference_type, assignment.reference_id)
            assignments_diag.append(
                {
                    "function": assignment.function.value,
                    "reference_type": assignment.reference_type.value,
                    "reference_id": assignment.reference_id,
                    "participation_state": assignment.participation_state.value,
                    "assigned_at": assignment.assigned_at,
                    "updated_at": assignment.updated_at,
                    "reference_exists": exists,
                    "standing_defect": (
                        not exists
                        and assignment.participation_state is ParticipationState.PARTICIPATING
                    ),
                }
            )
        rooms_diag.append(
            {
                "subentry_id": subentry.subentry_id,
                "title": subentry.title,
                "room_id": subentry.data.get("room_id"),
                "assignments": assignments_diag,
            }
        )

    return async_redact_data(
        {
            "domain": DOMAIN,
            "integration_version": "0.2.0",
            "config_entry_id": entry.entry_id,
            "config_entry_version": entry.version,
            "household": {
                CONF_RETAIN_ENROLLMENT_RECORDINGS: entry.options.get(
                    CONF_RETAIN_ENROLLMENT_RECORDINGS, "not_set"
                ),
                "voice_evidence": _voice_evidence_diagnostics(entry),
                "external_storage": _external_storage_diagnostics(entry),
            },
            "rooms": rooms_diag,
        },
        TO_REDACT,
    )
