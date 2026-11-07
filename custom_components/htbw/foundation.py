"""Foundation-owned Room Interaction Function Assignment store and retrieval.

Implements docs/architecture/foundation-room-interaction-roles-specification.md
SS4, SS7, SS8, SS13, SS15, SS16, SS18. Foundation owns the
RoomInteractionFunctionAssignment relationships; this module is the only
authorized read/write seam for them. A future Concierge consumer (or the
minimal consumer seam in this integration) retrieves through
get_room_interaction_assignment(hass, room_id, function) only -- never a
name, vendor, IP, or runtime-search fallback.
"""

from __future__ import annotations

import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers import entity_registry as er

from .const import DOMAIN, AssignmentResolution, InteractionFunction, ReferenceType
from .models import AssignmentLookupResult, HTBWConfigEntry, RoomInteractionFunctionAssignment

_LOGGER = logging.getLogger(__name__)


def reference_exists(hass: HomeAssistant, reference_type: ReferenceType, reference_id: str) -> bool:
    """Return whether a configured native reference still exists in its registry.

    Existence only (spec SS7 Truth boundary): this never checks or asserts
    current runtime availability (on/off, reachable, powered, "unavailable"
    state). That remains a separate runtime concern for whatever eventually
    consumes the reference -- Foundation is not made responsible for polling
    or asserting runtime availability by this specification.
    """
    if reference_type is ReferenceType.ENTITY_ID:
        entity_entry = er.async_get(hass).async_get(reference_id)
        if entity_entry is not None:
            return entity_entry.disabled_by is None
        # Some natively-provided entities are not registry-backed. Fall back
        # to the state machine purely to check *existence*, never state.
        return hass.states.get(reference_id) is not None
    if reference_type is ReferenceType.DEVICE_ID:
        device_entry = dr.async_get(hass).async_get(reference_id)
        return device_entry is not None and not device_entry.disabled_by
    return False


def _iter_entries(hass: HomeAssistant) -> list[HTBWConfigEntry]:
    return hass.config_entries.async_entries(DOMAIN)


def get_room_interaction_assignment(
    hass: HomeAssistant,
    room_id: str,
    function: InteractionFunction,
) -> AssignmentLookupResult:
    """The accepted (room_id, function) retrieval boundary (spec SS13).

    Returns NOT_CONFIGURED when no assignment exists, RESOLVED when a
    configured assignment's native reference still exists, or MISSING when
    the configured reference no longer resolves. Never performs a name,
    vendor, IP, or runtime-search fallback, and never returns a guessed
    replacement (spec SS15, SS16).
    """
    for entry in _iter_entries(hass):
        runtime_data = getattr(entry, "runtime_data", None)
        if runtime_data is None:
            continue
        for assignment in runtime_data.assignments:
            if assignment.room_id != room_id or assignment.function != function:
                continue
            if reference_exists(hass, assignment.reference_type, assignment.reference_id):
                return AssignmentLookupResult(AssignmentResolution.RESOLVED, assignment)
            return AssignmentLookupResult(AssignmentResolution.MISSING, assignment)
    return AssignmentLookupResult(AssignmentResolution.NOT_CONFIGURED, None)


def get_room_assignments(
    hass: HomeAssistant, room_id: str
) -> list[RoomInteractionFunctionAssignment]:
    """Return every configured assignment for a Room, across all functions."""
    results: list[RoomInteractionFunctionAssignment] = []
    for entry in _iter_entries(hass):
        runtime_data = getattr(entry, "runtime_data", None)
        if runtime_data is None:
            continue
        results.extend(a for a in runtime_data.assignments if a.room_id == room_id)
    return results
