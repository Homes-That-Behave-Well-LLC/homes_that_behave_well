"""Data models for the HTBW Core integration.

The RoomInteractionFunctionAssignment record implements the accepted schema
in docs/architecture/foundation-room-interaction-roles-specification.md SS4.1
exactly. Field names and cardinality (one Room, one function, one
participating capability per record) are preserved, not improvised.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any

from homeassistant.config_entries import ConfigEntry

from .const import AssignmentResolution, InteractionFunction, ParticipationState, ReferenceType


def _utc_now_iso() -> str:
    return datetime.now(UTC).isoformat()


@dataclass(frozen=True, slots=True)
class RoomInteractionFunctionAssignment:
    """One atomic Foundation-owned RoomInteractionFunctionAssignment record.

    Spec SS4.1: "Each RoomInteractionFunctionAssignment record is atomic: one
    Room, one interaction function, one participating capability."
    Multiplicity for a given (room, function) is expressed as zero, one, or
    many separate records -- never a list-valued field inside one record.
    """

    room_id: str
    function: InteractionFunction
    reference_type: ReferenceType
    reference_id: str
    participation_state: ParticipationState = ParticipationState.PARTICIPATING
    assigned_at: str = field(default_factory=_utc_now_iso)
    updated_at: str = field(default_factory=_utc_now_iso)

    def to_dict(self) -> dict[str, Any]:
        """Serialize to the config-entry-options-storable shape."""
        return {
            "room_id": self.room_id,
            "function": self.function.value,
            "reference_type": self.reference_type.value,
            "reference_id": self.reference_id,
            "participation_state": self.participation_state.value,
            "assigned_at": self.assigned_at,
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> RoomInteractionFunctionAssignment:
        """Deserialize from the config-entry-options-stored shape."""
        return cls(
            room_id=data["room_id"],
            function=InteractionFunction(data["function"]),
            reference_type=ReferenceType(data["reference_type"]),
            reference_id=data["reference_id"],
            participation_state=ParticipationState(
                data.get("participation_state", ParticipationState.PARTICIPATING)
            ),
            assigned_at=data.get("assigned_at") or _utc_now_iso(),
            updated_at=data.get("updated_at") or _utc_now_iso(),
        )


@dataclass(frozen=True, slots=True)
class AssignmentLookupResult:
    """Honest result of a Foundation (room_id, function) retrieval (spec SS13).

    status is one of AssignmentResolution.NOT_CONFIGURED / RESOLVED / MISSING.
    assignment is populated for RESOLVED and MISSING, and is None for
    NOT_CONFIGURED. There is no fourth outcome, and no guessed replacement is
    ever substituted (spec SS15, SS16).
    """

    status: AssignmentResolution
    assignment: RoomInteractionFunctionAssignment | None = None


@dataclass
class HTBWRuntimeData:
    """Per-config-entry runtime state (current HA runtime-data convention).

    One config entry represents one Room's full set of Interaction Function
    Assignments (a deliberate, documented v1 cardinality choice -- see
    SS21 of Issue #201 and the implementation report). Multiple Rooms are
    supported by adding multiple config entries, not by one entry holding
    several Rooms.
    """

    assignments: list[RoomInteractionFunctionAssignment]


# Typed alias for this integration's config entries, per current Home
# Assistant runtime-data typing conventions.
type HTBWConfigEntry = ConfigEntry[HTBWRuntimeData]
