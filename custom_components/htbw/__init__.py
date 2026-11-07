"""The HTBW Core integration.

Implements docs/architecture/foundation-room-interaction-roles-specification.md:
Foundation owns Room Interaction Function Assignment relationships. This
integration establishes the first authorized HTBW Core implementation
surface (Issue #201) and proves the accepted (room_id, function) retrieval
boundary end to end -- native Room/Area context, explicit configuration,
Foundation-owned persistence, and honest unavailable/missing behavior.

Out of scope here (see Issue #201 "Explicit non-goals" and
greenfield-mandate.md): Concierge, Voice Identity, response delivery, TTS,
Sonos behavior, network-endpoint resolution, and any other HTBW
responsibility. This integration creates no entities of its own -- it is a
configuration/relationship layer only, consumed by a future Concierge
implementation through `foundation.get_room_interaction_assignments`.
"""

from __future__ import annotations

from homeassistant.core import Event, EventStateChangedData, HomeAssistant
from homeassistant.exceptions import ConfigEntryError
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.event import async_track_state_change_event

from .const import ReferenceType
from .models import HTBWConfigEntry, HTBWRuntimeData
from .repairs_support import async_check_assignment_health
from .storage import load_assignments

# This integration manages configuration relationships only; it creates no
# entities and therefore forwards to no platforms.
PLATFORMS: list[str] = []


async def async_setup_entry(hass: HomeAssistant, entry: HTBWConfigEntry) -> bool:
    """Set up HTBW Core from a config entry (one Room's interaction-function assignments)."""
    try:
        runtime_data = HTBWRuntimeData(assignments=load_assignments(entry))
    except (KeyError, TypeError, ValueError) as err:
        raise ConfigEntryError("Invalid stored Room interaction assignment data") from err
    entry.runtime_data = runtime_data

    await async_check_assignment_health(hass, entry)

    async def _async_handle_entity_registry_event(
        event: Event[er.EventEntityRegistryUpdatedData],
    ) -> None:
        """Reconcile both disappearance and restoration, without remapping a reference."""
        if getattr(entry, "runtime_data", None) is not runtime_data:
            return
        affected = {event.data["entity_id"], event.data.get("old_entity_id")}
        if any(
            a.reference_type is ReferenceType.ENTITY_ID and a.reference_id in affected
            for a in entry.runtime_data.assignments
        ):
            await async_check_assignment_health(hass, entry)

    async def _async_handle_device_registry_event(
        event: Event[dr.EventDeviceRegistryUpdatedData],
    ) -> None:
        """Reconcile native device registry changes."""
        if getattr(entry, "runtime_data", None) is not runtime_data:
            return
        if any(
            a.reference_type is ReferenceType.DEVICE_ID
            and a.reference_id == event.data["device_id"]
            for a in entry.runtime_data.assignments
        ):
            await async_check_assignment_health(hass, entry)

    async def _async_handle_state_event(event: Event[EventStateChangedData]) -> None:
        if getattr(entry, "runtime_data", None) is not runtime_data:
            return
        if event.data["old_state"] is None or event.data["new_state"] is None:
            await async_check_assignment_health(hass, entry)

    entity_ids = {
        a.reference_id
        for a in entry.runtime_data.assignments
        if a.reference_type is ReferenceType.ENTITY_ID
    }
    if entity_ids:
        entry.async_on_unload(
            async_track_state_change_event(hass, entity_ids, _async_handle_state_event)
        )
    entry.async_on_unload(
        hass.bus.async_listen(er.EVENT_ENTITY_REGISTRY_UPDATED, _async_handle_entity_registry_event)
    )
    entry.async_on_unload(
        hass.bus.async_listen(dr.EVENT_DEVICE_REGISTRY_UPDATED, _async_handle_device_registry_event)
    )
    entry.async_on_unload(entry.add_update_listener(_async_update_listener))

    return True


async def async_unload_entry(hass: HomeAssistant, entry: HTBWConfigEntry) -> bool:
    """Unload a config entry.

    No platforms were forwarded (PLATFORMS is empty) and every listener was
    registered through entry.async_on_unload, so there is nothing further to
    tear down here.
    """
    return True


async def _async_update_listener(hass: HomeAssistant, entry: HTBWConfigEntry) -> None:
    """Reload the entry when its options (assignments) change."""
    await hass.config_entries.async_reload(entry.entry_id)
