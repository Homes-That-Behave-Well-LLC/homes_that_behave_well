"""The HTBW Core integration.

Configuration hierarchy (Issue #162, Owner decision B): exactly one household
HTBW config entry is the Integration configuration authority, and each HTBW
Room is a native config subentry beneath it (Room Configuration authority).
Household/Integration-scoped settings (the Voice Evidence App connection and
"Retain Enrollment Recordings") live only on the household entry; Room-scoped
Interaction Function Assignments live only in Room subentries.

Room behaviour is the #201 vertical slice, unchanged: Foundation owns Room
Interaction Function Assignment relationships and proves the accepted
(room_id, function) retrieval boundary -- native Room/Area context, explicit
configuration, Foundation-owned persistence, and honest unavailable/missing
behaviour. The #201 per-Room config entries migrate losslessly into Room
subentries (async_migrate_entry).

The Voice Evidence App is an optional external dependency (DL-41, DL-50): its
absence, unreachability, or incompatibility is a named outcome and never fails
the household entry or any Room. This integration creates no entities.
"""

from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigSubentry
from homeassistant.core import Event, EventStateChangedData, HomeAssistant
from homeassistant.exceptions import ConfigEntryError
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers import issue_registry as ir
from homeassistant.helpers.event import async_track_state_change_event

from .const import (
    CONF_MIGRATED_INTO,
    CONF_ROOM_ID,
    DOMAIN,
    HOUSEHOLD_TITLE,
    HOUSEHOLD_UNIQUE_ID,
    ISSUE_MIGRATION_CONFLICT,
    SUBENTRY_TYPE_ROOM,
    ReferenceType,
)
from .models import HTBWConfigEntry, HTBWRuntimeData, RoomInteractionFunctionAssignment
from .repairs_support import async_check_assignment_health
from .storage import legacy_room_payload, load_assignments, room_subentries
from .voice_evidence import async_setup_voice_evidence

_LOGGER = logging.getLogger(__name__)

# This integration manages configuration relationships only; it creates no
# entities and therefore forwards to no platforms.
PLATFORMS: list[str] = []

CONFIG_ENTRY_VERSION = 2


def _household_entry(
    hass: HomeAssistant, exclude: HTBWConfigEntry | None = None
) -> HTBWConfigEntry | None:
    for candidate in hass.config_entries.async_entries(DOMAIN):
        if candidate is exclude:
            continue
        if candidate.version == CONFIG_ENTRY_VERSION and candidate.unique_id == HOUSEHOLD_UNIQUE_ID:
            return candidate
    return None


def _room_subentry(entry: HTBWConfigEntry, room_id: str) -> ConfigSubentry | None:
    return next((s for s in room_subentries(entry) if s.unique_id == room_id), None)


async def async_migrate_entry(hass: HomeAssistant, entry: HTBWConfigEntry) -> bool:
    """Migrate a #201 per-Room config entry into the household entry's Room subentries.

    Lossless and idempotent. The decision and every write below are synchronous
    (no await), so concurrent migrations of several #201 entries cannot
    interleave. The first #201 entry is converted in place -- it keeps its
    entry_id, gains its Room as a subentry carrying the original stored records
    verbatim, and becomes the household entry. Each further #201 entry copies
    its Room into the household entry, is verified, and is only then marked for
    removal (performed outside its own setup lock). Any doubt preserves the old
    entry and surfaces a Repairs issue; nothing is discarded.
    """
    if entry.version >= CONFIG_ENTRY_VERSION:
        return True

    try:
        payload = legacy_room_payload(entry)
    except KeyError, TypeError, ValueError:
        _LOGGER.error(
            "HTBW could not migrate Room entry %s: its stored assignments are invalid; "
            "the entry is preserved unchanged",
            entry.title,
        )
        return False
    room_id = payload[CONF_ROOM_ID]

    household = _household_entry(hass, exclude=entry)
    if household is None:
        hass.config_entries.async_add_subentry(
            entry,
            ConfigSubentry(
                data=payload,  # type: ignore[arg-type]
                subentry_type=SUBENTRY_TYPE_ROOM,
                title=entry.title,
                unique_id=room_id,
            ),
        )
        migrated = _room_subentry(entry, room_id)
        if migrated is None or dict(migrated.data) != payload:
            _LOGGER.error("HTBW Room migration verification failed for %s", entry.title)
            return False
        hass.config_entries.async_update_entry(
            entry,
            data={},
            options={},
            title=HOUSEHOLD_TITLE,
            unique_id=HOUSEHOLD_UNIQUE_ID,
            version=CONFIG_ENTRY_VERSION,
            minor_version=1,
        )
        _LOGGER.info("HTBW migrated Room %s into the household configuration entry", entry.title)
        return True

    existing = _room_subentry(household, room_id)
    if existing is None:
        hass.config_entries.async_add_subentry(
            household,
            ConfigSubentry(
                data=payload,  # type: ignore[arg-type]
                subentry_type=SUBENTRY_TYPE_ROOM,
                title=entry.title,
                unique_id=room_id,
            ),
        )
        existing = _room_subentry(household, room_id)
    if existing is None or dict(existing.data) != payload:
        ir.async_create_issue(
            hass,
            DOMAIN,
            ISSUE_MIGRATION_CONFLICT.format(room_id=room_id),
            is_fixable=False,
            is_persistent=True,
            severity=ir.IssueSeverity.ERROR,
            translation_key="room_migration_conflict",
            translation_placeholders={"entry_title": entry.title},
        )
        _LOGGER.error(
            "HTBW Room %s already exists in the household entry with different "
            "configuration; the original entry is preserved for recovery",
            entry.title,
        )
        return False

    hass.config_entries.async_update_entry(
        entry,
        data={**entry.data, CONF_MIGRATED_INTO: household.entry_id},
        version=CONFIG_ENTRY_VERSION,
        minor_version=1,
    )
    return True


async def async_setup_entry(hass: HomeAssistant, entry: HTBWConfigEntry) -> bool:
    """Set up the household HTBW entry and its Room subentries."""
    if CONF_MIGRATED_INTO in entry.data:
        return await _async_retire_migrated_entry(hass, entry)

    rooms: dict[str, list[RoomInteractionFunctionAssignment]] = {}
    try:
        for subentry in room_subentries(entry):
            rooms[subentry.subentry_id] = load_assignments(subentry)
    except (KeyError, TypeError, ValueError) as err:
        raise ConfigEntryError("Invalid stored Room interaction assignment data") from err

    runtime_data = HTBWRuntimeData(
        assignments=[a for records in rooms.values() for a in records],
        rooms=rooms,
    )
    entry.runtime_data = runtime_data
    runtime_data.voice_evidence = await async_setup_voice_evidence(hass, entry)

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
            for a in runtime_data.assignments
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
            for a in runtime_data.assignments
        ):
            await async_check_assignment_health(hass, entry)

    async def _async_handle_state_event(event: Event[EventStateChangedData]) -> None:
        if getattr(entry, "runtime_data", None) is not runtime_data:
            return
        if event.data["old_state"] is None or event.data["new_state"] is None:
            await async_check_assignment_health(hass, entry)

    entity_ids = {
        a.reference_id
        for a in runtime_data.assignments
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


async def _async_retire_migrated_entry(hass: HomeAssistant, entry: HTBWConfigEntry) -> bool:
    """Remove a #201 entry whose Room is verified present in the household entry."""
    entry.runtime_data = HTBWRuntimeData(assignments=[])
    household = hass.config_entries.async_get_entry(entry.data[CONF_MIGRATED_INTO])
    room_id = entry.data.get(CONF_ROOM_ID)
    if (
        household is None
        or not isinstance(room_id, str)
        or _room_subentry(household, room_id) is None
    ):
        _LOGGER.error(
            "HTBW kept migrated Room entry %s because its household copy could not be verified",
            entry.title,
        )
        return True

    hass.async_create_task(
        hass.config_entries.async_remove(entry.entry_id), f"htbw retire {entry.entry_id}"
    )
    return True


async def async_unload_entry(hass: HomeAssistant, entry: HTBWConfigEntry) -> bool:
    """Unload a config entry.

    No platforms were forwarded (PLATFORMS is empty) and every listener and the
    Voice Evidence background synchronization were registered through
    entry.async_on_unload, so there is nothing further to tear down here.
    """
    return True


async def _async_update_listener(hass: HomeAssistant, entry: HTBWConfigEntry) -> None:
    """Reload when household options or Room subentries change."""
    await hass.config_entries.async_reload(entry.entry_id)
