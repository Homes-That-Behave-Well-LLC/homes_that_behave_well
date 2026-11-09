"""Repairs-compatible defect surfacing for Room Interaction Function Assignments.

Spec SS16/SS17 and DL-65: Repairs is a *projection* of an HTBW-owned,
authoritative defect state -- never a second authority, and never created
for a transient or self-healing condition. The only defect this integration
surfaces is a standing one: a configured native reference that no longer
resolves in its Home Assistant registry. A temporarily unavailable-but-still
-existing entity/device is never treated as a defect here (spec SS7 Truth
boundary; SS17 "do not create a Repairs issue for ... a currently offline
entity that still exists").

This uses Home Assistant's issue_registry directly (an informational,
non-fixable issue: is_fixable=False) rather than a repairs.py RepairsFlow
platform. A fix flow is not required for an informational Repairs issue, and
building one for a v1 vertical slice would be scope beyond what Issue #201
requires -- the issue text itself directs the administrator to this
integration's own configuration/options path.
"""

from __future__ import annotations

import logging
from hashlib import sha256

from homeassistant.core import HomeAssistant
from homeassistant.helpers import issue_registry as ir

from .const import (
    DOMAIN,
    EXTERNAL_STORAGE_AUTHORIZATION_LEARN_MORE_URL,
    EXTERNAL_STORAGE_FAILURE_OUTCOMES,
    ISSUE_EXTERNAL_STORAGE_PREFIX,
    ISSUE_ID_PREFIX,
    ISSUE_VOICE_EVIDENCE_PREFIX,
    ExternalStorageOutcome,
    ParticipationState,
    VoiceEvidenceOutcome,
)
from .foundation import reference_exists
from .models import HTBWConfigEntry, RoomInteractionFunctionAssignment

_LOGGER = logging.getLogger(__name__)


def assignment_issue_id(entry_id: str, assignment: RoomInteractionFunctionAssignment) -> str:
    """Identify a defect by entry, Room, function, and exact native reference."""
    reference_key = sha256(
        f"{assignment.room_id}:{assignment.reference_type.value}:{assignment.reference_id}".encode()
    ).hexdigest()
    return f"{ISSUE_ID_PREFIX.format(entry_id=entry_id)}{assignment.function.value}_{reference_key}"


async def async_check_assignment_health(hass: HomeAssistant, entry: HTBWConfigEntry) -> None:
    """Reconcile Repairs issues against every Room subentry's current assignments.

    For each configured assignment whose native reference no longer exists,
    ensure a standing Repairs issue exists. For each assignment whose
    reference resolves, ensure no stale issue remains. This follows the
    accepted "HTBW Defect State -> Repairs Projection" model (DL-65): HTBW's
    own state is authoritative, and the issue is created or deleted to match
    it, never the reverse. Issues raised under the #201 per-Room entry
    representation carry the same entry prefix and are removed here.
    """
    if entry.runtime_data is None:
        return

    registry = ir.async_get(hass)
    live_issue_ids: set[str] = set()

    for subentry_id, assignments in entry.runtime_data.rooms.items():
        subentry = entry.subentries.get(subentry_id)
        room_title = subentry.title if subentry is not None else entry.title
        for assignment in assignments:
            if assignment.participation_state is not ParticipationState.PARTICIPATING:
                continue
            issue_id = assignment_issue_id(entry.entry_id, assignment)
            if reference_exists(hass, assignment.reference_type, assignment.reference_id):
                continue

            live_issue_ids.add(issue_id)
            if registry.async_get_issue(DOMAIN, issue_id) is not None:
                continue
            ir.async_create_issue(
                hass,
                DOMAIN,
                issue_id,
                config_entry_id=entry.entry_id,
                is_fixable=False,
                is_persistent=True,
                severity=ir.IssueSeverity.ERROR,
                translation_key="missing_reference",
                translation_placeholders={
                    "function": assignment.function.value,
                    "entry_title": room_title,
                    "reference_id": assignment.reference_id,
                },
            )
            _LOGGER.warning(
                "HTBW Room Interaction Function Assignment for %s (%s) no longer "
                "resolves to a Home Assistant entity or device; reported through "
                "Repairs, not substituted",
                room_title,
                assignment.function.value,
            )

    prefix = ISSUE_ID_PREFIX.format(entry_id=entry.entry_id)
    for domain, issue_id in list(registry.issues):
        if domain == DOMAIN and issue_id.startswith(prefix) and issue_id not in live_issue_ids:
            ir.async_delete_issue(hass, DOMAIN, issue_id)


# Outcomes that are standing, administrator-correctable conditions. NOT_CONFIGURED
# is a legitimate optional state (no nagging, DL-148) and AVAILABLE is healthy;
# UNREACHABLE is raised only after it persists (see VoiceEvidenceManager).
_VOICE_EVIDENCE_ISSUE_OUTCOMES = {
    VoiceEvidenceOutcome.UNREACHABLE,
    VoiceEvidenceOutcome.AUTHENTICATION_FAILED,
    VoiceEvidenceOutcome.INCOMPATIBLE,
    VoiceEvidenceOutcome.APP_UNAVAILABLE,
}


def async_project_voice_evidence_issue(
    hass: HomeAssistant,
    entry: HTBWConfigEntry,
    outcome: VoiceEvidenceOutcome | None,
    reason_code: str | None = None,
) -> None:
    """Project the current Voice Evidence DL-41 outcome as at most one Repairs issue."""
    wanted = (
        f"{ISSUE_VOICE_EVIDENCE_PREFIX}{outcome.value}"
        if outcome in _VOICE_EVIDENCE_ISSUE_OUTCOMES
        else None
    )
    registry = ir.async_get(hass)
    for domain, issue_id in list(registry.issues):
        if domain == DOMAIN and issue_id.startswith(ISSUE_VOICE_EVIDENCE_PREFIX):
            if issue_id != wanted:
                ir.async_delete_issue(hass, DOMAIN, issue_id)
    if wanted is None or outcome is None:
        return
    ir.async_create_issue(
        hass,
        DOMAIN,
        wanted,
        config_entry_id=entry.entry_id,
        is_fixable=False,
        is_persistent=False,
        severity=ir.IssueSeverity.WARNING,
        translation_key=wanted,
        translation_placeholders={"reason_code": reason_code or "none"},
    )


def async_create_retention_sync_issue(hass: HomeAssistant, entry: HTBWConfigEntry) -> None:
    """Report that the household retention setting could not reach the App."""
    ir.async_create_issue(
        hass,
        DOMAIN,
        f"{ISSUE_VOICE_EVIDENCE_PREFIX}retention_sync_failed",
        config_entry_id=entry.entry_id,
        is_fixable=False,
        is_persistent=False,
        severity=ir.IssueSeverity.WARNING,
        translation_key="voice_evidence_retention_sync_failed",
    )


def async_delete_retention_sync_issue(hass: HomeAssistant) -> None:
    """Remove the retention-sync issue once the App applies the household setting."""
    ir.async_delete_issue(hass, DOMAIN, f"{ISSUE_VOICE_EVIDENCE_PREFIX}retention_sync_failed")


# NOT_CONFIGURED is a legitimate optional state (no nagging, DL-148) and
# AVAILABLE is healthy; every failure outcome is raised only after it
# persists (see ExternalStorageManager.consecutive_unavailable, which reads
# the same EXTERNAL_STORAGE_FAILURE_OUTCOMES set as this module).


def async_project_external_storage_issue(
    hass: HomeAssistant,
    entry: HTBWConfigEntry,
    outcome: ExternalStorageOutcome | None,
    reason_code: str | None = None,
    *,
    configured_path: str | None = None,
) -> None:
    """Project the current External Storage DL-41 outcome as at most one Repairs issue.

    ``configured_path`` is the household's own already-selected path, shown
    back to them so they can recognize/copy it in the guided-authorization
    text (Issue #211 remediation, Owner Decision 2026-11-09) -- unlike
    diagnostics, a Repairs issue is only ever shown to the administrator
    configuring this exact entry, never attached to a public bug report, so
    this is not a privacy exposure.
    """
    wanted = (
        f"{ISSUE_EXTERNAL_STORAGE_PREFIX}{outcome.value}"
        if outcome in EXTERNAL_STORAGE_FAILURE_OUTCOMES
        else None
    )
    registry = ir.async_get(hass)
    for domain, issue_id in list(registry.issues):
        if domain == DOMAIN and issue_id.startswith(ISSUE_EXTERNAL_STORAGE_PREFIX):
            if issue_id != wanted:
                ir.async_delete_issue(hass, DOMAIN, issue_id)
    if wanted is None or outcome is None:
        return
    ir.async_create_issue(
        hass,
        DOMAIN,
        wanted,
        config_entry_id=entry.entry_id,
        is_fixable=False,
        is_persistent=False,
        severity=ir.IssueSeverity.WARNING,
        translation_key=wanted,
        translation_placeholders={
            "reason_code": reason_code or "none",
            "path": configured_path or "the selected storage",
        },
        learn_more_url=(
            EXTERNAL_STORAGE_AUTHORIZATION_LEARN_MORE_URL
            if outcome is ExternalStorageOutcome.PATH_NOT_ALLOWED
            else None
        ),
    )
