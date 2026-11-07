"""Diagnostics support for HTBW Core.

Spec SS18.4: the minimum diagnostics information this workstream requires is,
for each RoomInteractionFunctionAssignment record, whether its reference
still resolves (existence, not current availability). Reuses Home
Assistant's native diagnostics platform; does not invent a new health model.

Redacts nothing sensitive is stored in the first place (only entity_id/
device_id native references and timestamps -- never credentials, tokens, or
network addresses), consistent with HTBW privacy architecture.
"""

from __future__ import annotations

from typing import Any

from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .foundation import reference_exists
from .models import HTBWConfigEntry


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: HTBWConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""
    assignments_diag: list[dict[str, Any]] = []
    runtime_data = entry.runtime_data

    for assignment in runtime_data.assignments if runtime_data else []:
        exists = reference_exists(hass, assignment.reference_type, assignment.reference_id)
        assignments_diag.append(
            {
                "function": assignment.function.value,
                "reference_type": assignment.reference_type.value,
                "participation_state": assignment.participation_state.value,
                "assigned_at": assignment.assigned_at,
                "updated_at": assignment.updated_at,
                "reference_exists": exists,
                "standing_defect": not exists,
            }
        )

    return {
        "domain": DOMAIN,
        "integration_version": "0.1.0",
        "config_entry_id": entry.entry_id,
        "room_id": entry.data.get("room_id"),
        "assignments": assignments_diag,
    }
