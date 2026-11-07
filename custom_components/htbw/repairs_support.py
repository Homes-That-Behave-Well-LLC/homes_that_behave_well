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

from .const import DOMAIN, ISSUE_ID_PREFIX, ParticipationState
from .foundation import reference_exists
from .models import HTBWConfigEntry, RoomInteractionFunctionAssignment

_LOGGER = logging.getLogger(__name__)


def assignment_issue_id(entry_id: str, assignment: RoomInteractionFunctionAssignment) -> str:
    """Identify a defect by entry, function, and exact native reference."""
    reference_key = sha256(
        f"{assignment.reference_type.value}:{assignment.reference_id}".encode()
    ).hexdigest()
    return f"{ISSUE_ID_PREFIX.format(entry_id=entry_id)}{assignment.function.value}_{reference_key}"


async def async_check_assignment_health(hass: HomeAssistant, entry: HTBWConfigEntry) -> None:
    """Reconcile Repairs issues against this entry's current assignment set.

    For each configured assignment whose native reference no longer exists,
    ensure a standing Repairs issue exists. For each assignment whose
    reference resolves, ensure no stale issue remains. This follows the
    accepted "HTBW Defect State -> Repairs Projection" model (DL-65): HTBW's
    own state is authoritative, and the issue is created or deleted to match
    it, never the reverse.
    """
    if entry.runtime_data is None:
        return

    registry = ir.async_get(hass)
    live_issue_ids: set[str] = set()

    for assignment in entry.runtime_data.assignments:
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
                "entry_title": entry.title,
                "reference_id": assignment.reference_id,
            },
        )
        _LOGGER.warning(
            "HTBW Room Interaction Function Assignment for %s (%s) no longer "
            "resolves to a Home Assistant entity or device; reported through "
            "Repairs, not substituted",
            entry.title,
            assignment.function.value,
        )

    prefix = ISSUE_ID_PREFIX.format(entry_id=entry.entry_id)
    for domain, issue_id in list(registry.issues):
        if domain == DOMAIN and issue_id.startswith(prefix) and issue_id not in live_issue_ids:
            ir.async_delete_issue(hass, DOMAIN, issue_id)
