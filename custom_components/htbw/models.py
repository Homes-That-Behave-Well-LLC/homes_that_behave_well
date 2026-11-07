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
            participation_state=ParticipationState(data["participation_state"]),
            assigned_at=data["assigned_at"],
            updated_at=data["updated_at"],
        )


@dataclass(frozen=True, slots=True)
class AssignmentLookupResult:
    """Existence outcome for one explicitly participating record (spec SS7/SS8)."""

    status: AssignmentResolution
    assignment: RoomInteractionFunctionAssignment


@dataclass
class HTBWRuntimeData:
    """Per-config-entry runtime state (current HA runtime-data convention).

    One config entry represents one Room, with zero or more atomic records per
    function. Multiple Rooms are supported by adding multiple config entries.
    """

    assignments: list[RoomInteractionFunctionAssignment]


# Typed alias for this integration's config entries, per current Home
# Assistant runtime-data typing conventions.
type HTBWConfigEntry = ConfigEntry[HTBWRuntimeData]
