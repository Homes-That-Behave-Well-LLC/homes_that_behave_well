"""Tests for the Foundation (room_id, function) retrieval boundary.

Covers docs/architecture/foundation-room-interaction-roles-specification.md
SS7 (Truth boundary), SS13 (retrieval boundary), SS15 (resolution
prohibitions), and SS16 (unavailable target behavior).
"""

from __future__ import annotations

import pytest
from homeassistant.core import HomeAssistant
from homeassistant.helpers import area_registry as ar
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers import entity_registry as er
from pytest_homeassistant.common import MockConfigEntry

from custom_components.htbw.const import (
    CONF_ASSIGNMENTS,
    AssignmentResolution,
    InteractionFunction,
    ParticipationState,
)
from custom_components.htbw.foundation import (
    get_room_assignments,
    get_room_interaction_assignments,
)

from .conftest import DEN_ROOM_ID, den, household_entry, room_subentry_data, set_den_assignments


def _set_assignments(hass: HomeAssistant, entry: MockConfigEntry, assignments: list[dict]) -> None:
    set_den_assignments(hass, entry, assignments)


def _assignment(room_id: str, function: str, reference_type: str, reference_id: str) -> dict:
    return {
        "room_id": room_id,
        "function": function,
        "reference_type": reference_type,
        "reference_id": reference_id,
        "participation_state": "participating",
        "assigned_at": "2026-01-01T00:00:00+00:00",
        "updated_at": "2026-01-01T00:00:00+00:00",
    }


async def test_not_configured_returns_honest_result(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """No assignment yields an empty configured set, never a guess."""
    room_id = DEN_ROOM_ID
    assert get_room_interaction_assignments(hass, room_id, InteractionFunction.VOICE_INPUT) == []


async def test_resolved_when_reference_exists(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """A configured entity_id that still exists in the registry resolves (existence only)."""
    entity_registry = er.async_get(hass)
    entry = entity_registry.async_get_or_create("media_player", "test", "den_speaker_unique_id")
    room_id = DEN_ROOM_ID
    _set_assignments(
        hass,
        setup_integration,
        [_assignment(room_id, "spoken_response_output", "entity_id", entry.entity_id)],
    )
    await hass.async_block_till_done()

    (result,) = get_room_interaction_assignments(
        hass, room_id, InteractionFunction.SPOKEN_RESPONSE_OUTPUT
    )
    assert result.status is AssignmentResolution.RESOLVED
    assert result.assignment.reference_id == entry.entity_id


async def test_missing_when_reference_no_longer_exists(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """A configured reference that resolves to nothing is MISSING, never substituted."""
    room_id = DEN_ROOM_ID
    _set_assignments(
        hass,
        setup_integration,
        [_assignment(room_id, "spoken_response_output", "entity_id", "media_player.long_removed")],
    )
    await hass.async_block_till_done()

    (result,) = get_room_interaction_assignments(
        hass, room_id, InteractionFunction.SPOKEN_RESPONSE_OUTPUT
    )
    assert result.status is AssignmentResolution.MISSING
    # The original stored reference is returned honestly -- never a different,
    # seemingly-similar entity (spec SS15/SS16).
    assert result.assignment.reference_id == "media_player.long_removed"


async def test_unavailable_state_is_not_treated_as_missing(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """A registry-existing entity that is currently 'unavailable' is still RESOLVED.

    Foundation reports configuration existence only (spec SS7 Truth
    boundary) -- it never asserts or depends on current runtime
    availability.
    """
    entity_registry = er.async_get(hass)
    entry = entity_registry.async_get_or_create("media_player", "test", "den_speaker_2")
    hass.states.async_set(entry.entity_id, "unavailable")

    room_id = DEN_ROOM_ID
    _set_assignments(
        hass,
        setup_integration,
        [_assignment(room_id, "spoken_response_output", "entity_id", entry.entity_id)],
    )
    await hass.async_block_till_done()

    (result,) = get_room_interaction_assignments(
        hass, room_id, InteractionFunction.SPOKEN_RESPONSE_OUTPUT
    )
    assert result.status is AssignmentResolution.RESOLVED


async def test_voice_input_and_spoken_response_output_are_independent(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """Different devices for voice_input and spoken_response_output resolve independently."""
    entity_registry = er.async_get(hass)
    mic_entry = entity_registry.async_get_or_create(
        "assist_satellite", "test", "den_satellite_unique"
    )
    speaker_entry = entity_registry.async_get_or_create(
        "media_player", "test", "den_speaker_unique"
    )
    room_id = DEN_ROOM_ID
    _set_assignments(
        hass,
        setup_integration,
        [
            _assignment(room_id, "voice_input", "entity_id", mic_entry.entity_id),
            _assignment(room_id, "spoken_response_output", "entity_id", speaker_entry.entity_id),
        ],
    )
    await hass.async_block_till_done()

    (voice_result,) = get_room_interaction_assignments(
        hass, room_id, InteractionFunction.VOICE_INPUT
    )
    (response_result,) = get_room_interaction_assignments(
        hass, room_id, InteractionFunction.SPOKEN_RESPONSE_OUTPUT
    )
    assert voice_result.assignment.reference_id == mic_entry.entity_id
    assert response_result.assignment.reference_id == speaker_entry.entity_id
    assert voice_result.assignment.reference_id != response_result.assignment.reference_id


async def test_same_device_multiple_roles_only_when_explicitly_configured(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """One device may fill two roles only via two explicit records -- never inferred."""
    entity_registry = er.async_get(hass)
    combo_entry = entity_registry.async_get_or_create(
        "media_player", "test", "integrated_combo_unique"
    )
    room_id = DEN_ROOM_ID

    # Only spoken_response_output is explicitly configured.
    _set_assignments(
        hass,
        setup_integration,
        [_assignment(room_id, "spoken_response_output", "entity_id", combo_entry.entity_id)],
    )
    await hass.async_block_till_done()

    assert get_room_interaction_assignments(hass, room_id, InteractionFunction.VOICE_INPUT) == []

    # Now explicitly add voice_input for the same device too.
    _set_assignments(
        hass,
        setup_integration,
        [
            _assignment(room_id, "spoken_response_output", "entity_id", combo_entry.entity_id),
            _assignment(room_id, "voice_input", "entity_id", combo_entry.entity_id),
        ],
    )
    await hass.async_block_till_done()

    (voice_result,) = get_room_interaction_assignments(
        hass, room_id, InteractionFunction.VOICE_INPUT
    )
    assert voice_result.status is AssignmentResolution.RESOLVED
    assert voice_result.assignment.reference_id == combo_entry.entity_id


async def test_device_id_reference_resolves_through_device_registry(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """An `interface` assignment using device_id resolves through the device registry."""
    owner_entry = MockConfigEntry(domain="test")
    owner_entry.add_to_hass(hass)
    device_registry = dr.async_get(hass)
    device = device_registry.async_get_or_create(
        config_entry_id=owner_entry.entry_id,
        identifiers={("test", "kiosk_1")},
        name="Den Kiosk",
    )
    room_id = DEN_ROOM_ID
    _set_assignments(
        hass,
        setup_integration,
        [_assignment(room_id, "interface", "device_id", device.id)],
    )
    await hass.async_block_till_done()

    (result,) = get_room_interaction_assignments(hass, room_id, InteractionFunction.INTERFACE)
    assert result.status is AssignmentResolution.RESOLVED
    assert result.assignment.reference_id == device.id


async def test_no_fallback_discovery_for_unrelated_entities_in_same_area(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """A device in the same Area is never silently selected (spec SS15)."""
    entity_registry = er.async_get(hass)
    # An unrelated media_player exists in Home Assistant, but was never
    # configured as this Room's spoken_response_output.
    entity_registry.async_get_or_create("media_player", "test", "unrelated_speaker")

    room_id = DEN_ROOM_ID
    results = get_room_interaction_assignments(
        hass, room_id, InteractionFunction.SPOKEN_RESPONSE_OUTPUT
    )
    assert results == []


async def test_explicit_cross_room_output_is_preserved(
    hass: HomeAssistant,
) -> None:
    """Explicit assignment wins over physical Area membership and apparent room naming."""
    areas = ar.async_get(hass)
    context = areas.async_create("Configured Room")
    equipment_area = areas.async_create("Equipment Room")
    entities = er.async_get(hass)
    selected = entities.async_get_or_create(
        "media_player", "test", "cross_room_output", suggested_object_id="equipment_output"
    )
    local_candidate = entities.async_get_or_create(
        "media_player", "test", "local_output", suggested_object_id="configured_room_output"
    )
    entities.async_update_entity(selected.entity_id, area_id=equipment_area.id)
    entities.async_update_entity(local_candidate.entity_id, area_id=context.id)
    entry = household_entry(
        rooms=[
            room_subentry_data(
                context.id,
                context.name,
                [
                    _assignment(
                        context.id, "spoken_response_output", "entity_id", selected.entity_id
                    )
                ],
            )
        ]
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    for state in ("idle", "unavailable"):
        hass.states.async_set(selected.entity_id, state)
        (result,) = get_room_interaction_assignments(
            hass, context.id, InteractionFunction.SPOKEN_RESPONSE_OUTPUT
        )
        assert result.status is AssignmentResolution.RESOLVED
        assert result.assignment is not None
        assert result.assignment.room_id == context.id
        assert result.assignment.reference_id == selected.entity_id
        assert result.assignment.reference_id != local_candidate.entity_id

    remote = get_room_interaction_assignments(hass, context.id, InteractionFunction.PHYSICAL_REMOTE)
    assert remote == []


async def test_get_room_assignments_returns_every_configured_function(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """get_room_assignments returns the full configured set for a Room."""
    room_id = DEN_ROOM_ID
    _set_assignments(
        hass,
        setup_integration,
        [
            _assignment(room_id, "voice_input", "entity_id", "assist_satellite.a"),
            _assignment(room_id, "spoken_response_output", "entity_id", "media_player.b"),
        ],
    )
    await hass.async_block_till_done()

    assignments = get_room_assignments(hass, room_id)
    assert {a.function for a in assignments} == {
        InteractionFunction.VOICE_INPUT,
        InteractionFunction.SPOKEN_RESPONSE_OUTPUT,
    }


@pytest.mark.parametrize("reverse", [False, True])
async def test_multiple_records_return_every_reference_without_selection(
    hass: HomeAssistant, setup_integration: MockConfigEntry, reverse: bool
) -> None:
    """A missing record never hides another record, and neither becomes a preferred target."""
    existing = er.async_get(hass).async_get_or_create("media_player", "test", "multi_existing")
    room_id = DEN_ROOM_ID
    records = [
        _assignment(room_id, "spoken_response_output", "entity_id", "media_player.missing"),
        _assignment(room_id, "spoken_response_output", "entity_id", existing.entity_id),
    ]
    _set_assignments(hass, setup_integration, records[::-1] if reverse else records)
    await hass.async_block_till_done()

    results = get_room_interaction_assignments(
        hass, room_id, InteractionFunction.SPOKEN_RESPONSE_OUTPUT
    )
    assert len(results) == 2
    assert {r.assignment.reference_id: r.status for r in results} == {
        "media_player.missing": AssignmentResolution.MISSING,
        existing.entity_id: AssignmentResolution.RESOLVED,
    }


@pytest.mark.parametrize(
    "participation_state",
    [ParticipationState.NOT_SELECTED, ParticipationState.DELIBERATELY_EXCLUDED],
)
async def test_nonparticipating_records_are_not_returned(
    hass: HomeAssistant,
    setup_integration: MockConfigEntry,
    participation_state: ParticipationState,
) -> None:
    room_id = DEN_ROOM_ID
    record = _assignment(room_id, "spoken_response_output", "entity_id", "media_player.excluded")
    record["participation_state"] = participation_state.value
    _set_assignments(hass, setup_integration, [record])
    await hass.async_block_till_done()

    assert (
        get_room_interaction_assignments(hass, room_id, InteractionFunction.SPOKEN_RESPONSE_OUTPUT)
        == []
    )
    assert get_room_assignments(hass, room_id) == []
    assert den(setup_integration).data[CONF_ASSIGNMENTS] == [record]


async def test_disabled_native_entity_still_exists(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    entity = er.async_get(hass).async_get_or_create(
        "media_player", "test", "disabled_output", disabled_by=er.RegistryEntryDisabler.USER
    )
    room_id = DEN_ROOM_ID
    _set_assignments(
        hass,
        setup_integration,
        [_assignment(room_id, "spoken_response_output", "entity_id", entity.entity_id)],
    )
    await hass.async_block_till_done()
    (result,) = get_room_interaction_assignments(
        hass, room_id, InteractionFunction.SPOKEN_RESPONSE_OUTPUT
    )
    assert result.status is AssignmentResolution.RESOLVED
    assert result.assignment.reference_id == entity.entity_id


async def test_disabled_native_device_still_exists(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    owner = MockConfigEntry(domain="test")
    owner.add_to_hass(hass)
    device = dr.async_get(hass).async_get_or_create(
        config_entry_id=owner.entry_id,
        identifiers={("test", "disabled_interface")},
        disabled_by=dr.DeviceEntryDisabler.USER,
    )
    room_id = DEN_ROOM_ID
    _set_assignments(
        hass,
        setup_integration,
        [_assignment(room_id, "interface", "device_id", device.id)],
    )
    await hass.async_block_till_done()
    (result,) = get_room_interaction_assignments(hass, room_id, InteractionFunction.INTERFACE)
    assert result.status is AssignmentResolution.RESOLVED
    assert result.assignment.reference_id == device.id
