"""Tests for the Foundation (room_id, function) retrieval boundary.

Covers docs/architecture/foundation-room-interaction-roles-specification.md
SS7 (Truth boundary), SS13 (retrieval boundary), SS15 (resolution
prohibitions), and SS16 (unavailable target behavior).
"""

from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers import entity_registry as er
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.htbw.const import (
    CONF_ASSIGNMENTS,
    AssignmentResolution,
    InteractionFunction,
)
from custom_components.htbw.foundation import (
    get_room_assignments,
    get_room_interaction_assignment,
)


def _set_assignments(hass: HomeAssistant, entry: MockConfigEntry, assignments: list[dict]) -> None:
    hass.config_entries.async_update_entry(entry, options={CONF_ASSIGNMENTS: assignments})


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
    """No assignment for (room_id, function) yields NOT_CONFIGURED, never a guess."""
    room_id = setup_integration.data["room_id"]
    result = get_room_interaction_assignment(hass, room_id, InteractionFunction.VOICE_INPUT)
    assert result.status is AssignmentResolution.NOT_CONFIGURED
    assert result.assignment is None


async def test_resolved_when_reference_exists(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """A configured entity_id that still exists in the registry resolves (existence only)."""
    entity_registry = er.async_get(hass)
    entry = entity_registry.async_get_or_create(
        "media_player", "test", "den_speaker_unique_id"
    )
    room_id = setup_integration.data["room_id"]
    _set_assignments(
        hass,
        setup_integration,
        [_assignment(room_id, "spoken_response_output", "entity_id", entry.entity_id)],
    )
    await hass.async_block_till_done()

    result = get_room_interaction_assignment(
        hass, room_id, InteractionFunction.SPOKEN_RESPONSE_OUTPUT
    )
    assert result.status is AssignmentResolution.RESOLVED
    assert result.assignment.reference_id == entry.entity_id


async def test_missing_when_reference_no_longer_exists(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """A configured reference that resolves to nothing is MISSING, never substituted."""
    room_id = setup_integration.data["room_id"]
    _set_assignments(
        hass,
        setup_integration,
        [
            _assignment(
                room_id, "spoken_response_output", "entity_id", "media_player.long_removed"
            )
        ],
    )
    await hass.async_block_till_done()

    result = get_room_interaction_assignment(
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

    room_id = setup_integration.data["room_id"]
    _set_assignments(
        hass,
        setup_integration,
        [_assignment(room_id, "spoken_response_output", "entity_id", entry.entity_id)],
    )
    await hass.async_block_till_done()

    result = get_room_interaction_assignment(
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
    room_id = setup_integration.data["room_id"]
    _set_assignments(
        hass,
        setup_integration,
        [
            _assignment(room_id, "voice_input", "entity_id", mic_entry.entity_id),
            _assignment(
                room_id, "spoken_response_output", "entity_id", speaker_entry.entity_id
            ),
        ],
    )
    await hass.async_block_till_done()

    voice_result = get_room_interaction_assignment(hass, room_id, InteractionFunction.VOICE_INPUT)
    response_result = get_room_interaction_assignment(
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
    room_id = setup_integration.data["room_id"]

    # Only spoken_response_output is explicitly configured.
    _set_assignments(
        hass,
        setup_integration,
        [
            _assignment(
                room_id, "spoken_response_output", "entity_id", combo_entry.entity_id
            )
        ],
    )
    await hass.async_block_till_done()

    voice_result = get_room_interaction_assignment(hass, room_id, InteractionFunction.VOICE_INPUT)
    assert voice_result.status is AssignmentResolution.NOT_CONFIGURED

    # Now explicitly add voice_input for the same device too.
    _set_assignments(
        hass,
        setup_integration,
        [
            _assignment(
                room_id, "spoken_response_output", "entity_id", combo_entry.entity_id
            ),
            _assignment(room_id, "voice_input", "entity_id", combo_entry.entity_id),
        ],
    )
    await hass.async_block_till_done()

    voice_result = get_room_interaction_assignment(hass, room_id, InteractionFunction.VOICE_INPUT)
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
    room_id = setup_integration.data["room_id"]
    _set_assignments(
        hass,
        setup_integration,
        [_assignment(room_id, "interface", "device_id", device.id)],
    )
    await hass.async_block_till_done()

    result = get_room_interaction_assignment(hass, room_id, InteractionFunction.INTERFACE)
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

    room_id = setup_integration.data["room_id"]
    result = get_room_interaction_assignment(
        hass, room_id, InteractionFunction.SPOKEN_RESPONSE_OUTPUT
    )
    assert result.status is AssignmentResolution.NOT_CONFIGURED
    assert result.assignment is None


async def test_get_room_assignments_returns_every_configured_function(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """get_room_assignments returns the full configured set for a Room."""
    room_id = setup_integration.data["room_id"]
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
