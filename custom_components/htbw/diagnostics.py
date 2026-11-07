"""Diagnostics support for HTBW Core.

Spec SS18.4: the minimum diagnostics information this workstream requires is,
for each RoomInteractionFunctionAssignment record, whether its reference
still resolves (existence, not current availability). Reuses Home
Assistant's native diagnostics platform; does not invent a new health model.

Native identifiers are redacted using Home Assistant's diagnostics helper.
Only explicitly selected diagnostic fields are exported.
"""

from __future__ import annotations

from typing import Any

from homeassistant.components.diagnostics import async_redact_data
from homeassistant.core import HomeAssistant

from .const import DOMAIN, ParticipationState
from .foundation import reference_exists
from .models import HTBWConfigEntry
from .storage import load_assignments


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: HTBWConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""
    assignments_diag: list[dict[str, Any]] = []
    for assignment in load_assignments(entry):
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

    return async_redact_data(
        {
            "domain": DOMAIN,
            "integration_version": "0.1.0",
            "config_entry_id": entry.entry_id,
            "room_id": entry.data.get("room_id"),
            "assignments": assignments_diag,
        },
        {"config_entry_id", "room_id", "reference_id"},
    )
