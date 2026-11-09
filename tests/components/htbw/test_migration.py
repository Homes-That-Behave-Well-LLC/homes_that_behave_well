"""#201 per-Room config entries migrate losslessly into Room subentries (Issue #162, decision B).

Old #201 representation -> migration -> one household HTBW entry -> Room
subentry -> assignments preserved -> restart -> migration does not repeat ->
assignments still preserved.
"""

from __future__ import annotations

from typing import Any

from homeassistant.config_entries import ConfigEntryState
from homeassistant.core import HomeAssistant
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers import issue_registry as ir
from homeassistant.setup import async_setup_component
from pytest_homeassistant.common import MockConfigEntry

from custom_components.htbw.const import (
    CONF_ASSIGNMENTS,
    CONF_EXTERNAL_STORAGE_PATH,
    CONF_RETAIN_ENROLLMENT_RECORDINGS,
    CONF_ROOM_ID,
    DOMAIN,
    HOUSEHOLD_UNIQUE_ID,
    SUBENTRY_TYPE_ROOM,
    AssignmentResolution,
    InteractionFunction,
)
from custom_components.htbw.foundation import get_room_interaction_assignments

from .conftest import household_entry, legacy_room_entry, room_subentry_data


def _record(room_id: str, function: str, reference_type: str, reference_id: str, **kw: str):
    return {
        "room_id": room_id,
        "function": function,
        "reference_type": reference_type,
        "reference_id": reference_id,
        "participation_state": kw.get("participation_state", "participating"),
        "assigned_at": kw.get("assigned_at", "2026-11-02T14:03:11.123456+00:00"),
        "updated_at": kw.get("updated_at", "2026-11-03T09:41:52.654321+00:00"),
    }


def _ha_dev_den(hass: HomeAssistant) -> tuple[str, list[dict[str, Any]]]:
    """The accepted HA-DEV Den shape: voice input, Sonos output, iPad interface, no remote."""
    satellite = er.async_get(hass).async_get_or_create(
        "assist_satellite", "test", "voice_assistant_dev", suggested_object_id="voice_assistant_dev"
    )
    sonos = er.async_get(hass).async_get_or_create(
        "media_player", "test", "toms_office_sonos", suggested_object_id="toms_office"
    )
    owner = MockConfigEntry(domain="test")
    owner.add_to_hass(hass)
    ipad = dr.async_get(hass).async_get_or_create(
        config_entry_id=owner.entry_id, identifiers={("test", "toms_ipad_air")}, name="iPad Air"
    )
    room_id = "den"
    return room_id, [
        _record(room_id, "voice_input", "entity_id", satellite.entity_id),
        _record(room_id, "spoken_response_output", "entity_id", sonos.entity_id),
        _record(room_id, "interface", "device_id", ipad.id),
        _record(
            room_id,
            "spoken_response_output",
            "entity_id",
            "media_player.previously_excluded",
            participation_state="deliberately_excluded",
        ),
    ]


def _rooms(entry: MockConfigEntry) -> dict[str, Any]:
    return {
        s.unique_id: s for s in entry.subentries.values() if s.subentry_type == SUBENTRY_TYPE_ROOM
    }


async def _start(hass: HomeAssistant) -> None:
    assert await async_setup_component(hass, DOMAIN, {})
    await hass.async_block_till_done()


async def test_ha_dev_den_migrates_losslessly_in_place(hass: HomeAssistant) -> None:
    room_id, records = _ha_dev_den(hass)
    legacy = legacy_room_entry(room_id, "Den", records)
    legacy.add_to_hass(hass)
    original_entry_id = legacy.entry_id

    await _start(hass)

    (entry,) = hass.config_entries.async_entries(DOMAIN)
    assert entry.entry_id == original_entry_id
    assert entry.state is ConfigEntryState.LOADED
    assert entry.version == 2
    assert entry.unique_id == HOUSEHOLD_UNIQUE_ID
    assert entry.title == "HTBW"
    assert entry.data == {}
    rooms = _rooms(entry)
    assert list(rooms) == [room_id]
    den = rooms[room_id]
    assert den.title == "Den"
    assert dict(den.data) == {CONF_ROOM_ID: room_id, CONF_ASSIGNMENTS: records}

    by_function = {
        function: get_room_interaction_assignments(hass, room_id, function)
        for function in InteractionFunction
    }
    assert [r.assignment.to_dict() for r in by_function[InteractionFunction.VOICE_INPUT]] == [
        records[0]
    ]
    assert [
        r.assignment.to_dict() for r in by_function[InteractionFunction.SPOKEN_RESPONSE_OUTPUT]
    ] == [records[1]]
    assert [r.assignment.to_dict() for r in by_function[InteractionFunction.INTERFACE]] == [
        records[2]
    ]
    assert by_function[InteractionFunction.PHYSICAL_REMOTE] == []
    assert all(
        r.status is AssignmentResolution.RESOLVED
        for results in by_function.values()
        for r in results
    )


async def test_migration_does_not_repeat_across_reload_and_restart(hass: HomeAssistant) -> None:
    room_id, records = _ha_dev_den(hass)
    legacy_room_entry(room_id, "Den", records).add_to_hass(hass)
    await _start(hass)
    (entry,) = hass.config_entries.async_entries(DOMAIN)
    snapshot = {sid: (s.unique_id, dict(s.data)) for sid, s in entry.subentries.items()}

    for _ in range(2):
        assert await hass.config_entries.async_reload(entry.entry_id)
        await hass.async_block_till_done()
    assert await hass.config_entries.async_unload(entry.entry_id)
    await hass.async_block_till_done()
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    assert hass.config_entries.async_entries(DOMAIN) == [entry]
    assert {sid: (s.unique_id, dict(s.data)) for sid, s in entry.subentries.items()} == snapshot
    assert len(entry.runtime_data.assignments) == len(records)


async def test_several_rooms_consolidate_into_one_household(hass: HomeAssistant) -> None:
    den_records = [_record("den", "voice_input", "entity_id", "assist_satellite.den")]
    office_records = [
        _record("office", "spoken_response_output", "entity_id", "media_player.office")
    ]
    legacy_room_entry("den", "Den", den_records).add_to_hass(hass)
    legacy_room_entry("office", "Office", office_records).add_to_hass(hass)

    await _start(hass)
    await hass.async_block_till_done()

    (entry,) = hass.config_entries.async_entries(DOMAIN)
    assert entry.unique_id == HOUSEHOLD_UNIQUE_ID
    rooms = _rooms(entry)
    assert set(rooms) == {"den", "office"}
    assert rooms["den"].data[CONF_ASSIGNMENTS] == den_records
    assert rooms["office"].data[CONF_ASSIGNMENTS] == office_records
    assert {s.title for s in rooms.values()} == {"Den", "Office"}
    (office,) = get_room_interaction_assignments(
        hass, "office", InteractionFunction.SPOKEN_RESPONSE_OUTPUT
    )
    assert office.assignment.to_dict() == office_records[0]

    assert await hass.config_entries.async_reload(entry.entry_id)
    await hass.async_block_till_done()
    assert set(_rooms(entry)) == {"den", "office"}
    assert len(hass.config_entries.async_entries(DOMAIN)) == 1


async def test_household_settings_exist_only_on_the_parent(hass: HomeAssistant) -> None:
    legacy_room_entry("den", "Den", []).add_to_hass(hass)
    legacy_room_entry("office", "Office", []).add_to_hass(hass)
    await _start(hass)
    (entry,) = hass.config_entries.async_entries(DOMAIN)

    result = await hass.config_entries.options.async_init(entry.entry_id)
    await hass.config_entries.options.async_configure(
        result["flow_id"], {CONF_RETAIN_ENROLLMENT_RECORDINGS: "retain"}
    )
    await hass.async_block_till_done()

    assert entry.options == {
        CONF_RETAIN_ENROLLMENT_RECORDINGS: "retain",
        CONF_EXTERNAL_STORAGE_PATH: "",
    }
    for room in _rooms(entry).values():
        assert set(room.data) == {CONF_ROOM_ID, CONF_ASSIGNMENTS}


async def test_invalid_legacy_data_is_preserved_not_migrated(hass: HomeAssistant) -> None:
    legacy = legacy_room_entry("den", "Den", [{"function": "voice_input"}])
    legacy.add_to_hass(hass)
    await _start(hass)

    assert legacy.state is ConfigEntryState.MIGRATION_ERROR
    assert legacy.version == 1
    assert legacy.options[CONF_ASSIGNMENTS] == [{"function": "voice_input"}]
    assert legacy.subentries == {}


async def test_conflicting_room_preserves_the_old_entry_and_reports_it(
    hass: HomeAssistant,
) -> None:
    existing = [_record("den", "voice_input", "entity_id", "assist_satellite.current")]
    household = household_entry(rooms=[room_subentry_data("den", "Den", existing)])
    household.add_to_hass(hass)
    legacy_records = [_record("den", "voice_input", "entity_id", "assist_satellite.other")]
    legacy = legacy_room_entry("den", "Den (old)", legacy_records)
    legacy.add_to_hass(hass)

    await _start(hass)

    assert legacy.state is ConfigEntryState.MIGRATION_ERROR
    assert legacy.options[CONF_ASSIGNMENTS] == legacy_records
    assert _rooms(household)["den"].data[CONF_ASSIGNMENTS] == existing
    assert ir.async_get(hass).async_get_issue(DOMAIN, "room_migration_conflict_den") is not None


async def test_already_copied_room_retires_the_old_entry(hass: HomeAssistant) -> None:
    """Re-running after a copy (e.g. interrupted before removal) only retires the duplicate."""
    records = [_record("den", "voice_input", "entity_id", "assist_satellite.den")]
    household = household_entry(rooms=[room_subentry_data("den", "Den", records)])
    household.add_to_hass(hass)
    legacy_room_entry("den", "Den", records).add_to_hass(hass)

    await _start(hass)
    await hass.async_block_till_done()

    assert hass.config_entries.async_entries(DOMAIN) == [household]
    assert list(_rooms(household)) == ["den"]
    assert _rooms(household)["den"].data[CONF_ASSIGNMENTS] == records


async def test_legacy_repairs_issues_are_reconciled_after_migration(hass: HomeAssistant) -> None:
    records = [_record("den", "spoken_response_output", "entity_id", "media_player.gone")]
    legacy = legacy_room_entry("den", "Den", records)
    legacy.add_to_hass(hass)
    stale_id = f"missing_reference_{legacy.entry_id}_spoken_response_output_legacyhash"
    ir.async_create_issue(
        hass,
        DOMAIN,
        stale_id,
        is_fixable=False,
        severity=ir.IssueSeverity.ERROR,
        translation_key="missing_reference",
    )
    await _start(hass)

    registry = ir.async_get(hass)
    assert registry.async_get_issue(DOMAIN, stale_id) is None
    live = [key for key in registry.issues if key[0] == DOMAIN]
    assert len(live) == 1
