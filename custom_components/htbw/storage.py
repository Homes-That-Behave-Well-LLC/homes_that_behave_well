"""Config-entry-backed persistence for Room Interaction Function Assignments.

Spec SS12 (Persistence): uses ordinary Home Assistant config-entry options
storage. No arbitrary database, no second registry, no direct writes to
Home Assistant's own internal storage files. Display names are never
persisted as native identity -- only the native entity_id/device_id itself.
"""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry

from .const import CONF_ASSIGNMENTS
from .models import RoomInteractionFunctionAssignment


def load_assignments(entry: ConfigEntry) -> list[RoomInteractionFunctionAssignment]:
    """Parse the config entry's stored options into assignment records."""
    raw_assignments = entry.options.get(CONF_ASSIGNMENTS, [])
    return [RoomInteractionFunctionAssignment.from_dict(item) for item in raw_assignments]


def dump_assignments(assignments: list[RoomInteractionFunctionAssignment]) -> dict:
    """Serialize assignment records into the options dict shape to persist."""
    return {CONF_ASSIGNMENTS: [a.to_dict() for a in assignments]}
