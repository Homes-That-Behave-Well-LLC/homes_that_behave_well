"""Config-subentry-backed persistence for Room Interaction Function Assignments.

Each HTBW Room is a native config subentry beneath the single household HTBW
config entry (Issue #162, Owner decision B). A Room subentry's data holds the
Room's native Area reference and its atomic assignment records, in exactly the
record shape #201 accepted. No arbitrary database, no second registry, and no
direct writes to Home Assistant's internal storage files. Display names are
never persisted as native identity -- only the native entity_id/device_id.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from homeassistant.config_entries import ConfigEntry, ConfigSubentry

from .const import CONF_ASSIGNMENTS, CONF_ROOM_ID, SUBENTRY_TYPE_ROOM
from .models import RoomInteractionFunctionAssignment


def parse_assignments(raw: Mapping[str, Any]) -> list[RoomInteractionFunctionAssignment]:
    """Parse a stored mapping's assignment list into records."""
    return [
        RoomInteractionFunctionAssignment.from_dict(item) for item in raw.get(CONF_ASSIGNMENTS, [])
    ]


def load_assignments(subentry: ConfigSubentry) -> list[RoomInteractionFunctionAssignment]:
    """Parse one Room subentry's stored data into assignment records."""
    return parse_assignments(subentry.data)


def room_subentries(entry: ConfigEntry) -> list[ConfigSubentry]:
    """Return the household entry's Room subentries."""
    return [s for s in entry.subentries.values() if s.subentry_type == SUBENTRY_TYPE_ROOM]


def room_subentry_data(
    room_id: str, assignments: list[RoomInteractionFunctionAssignment]
) -> dict[str, Any]:
    """Serialize a Room's configuration into the subentry data shape."""
    return {
        CONF_ROOM_ID: room_id,
        CONF_ASSIGNMENTS: [a.to_dict() for a in assignments],
    }


def legacy_room_payload(entry: ConfigEntry) -> dict[str, Any]:
    """Return a #201 Room config entry's Room configuration, validated and unchanged.

    The #201 representation stored the Area reference in entry data and the
    records in entry options. Parsing validates every record; the returned
    payload carries the original stored dictionaries verbatim, so timestamps,
    participation state, and native references survive migration exactly.
    """
    room_id = entry.data[CONF_ROOM_ID]
    if not isinstance(room_id, str) or not room_id:
        raise ValueError("Legacy Room entry has no room_id")
    raw = list(entry.options.get(CONF_ASSIGNMENTS, []))
    records = parse_assignments({CONF_ASSIGNMENTS: raw})
    if any(record.room_id != room_id for record in records):
        raise ValueError("Legacy Room entry contains a record for another Room")
    return {CONF_ROOM_ID: room_id, CONF_ASSIGNMENTS: [dict(item) for item in raw]}
