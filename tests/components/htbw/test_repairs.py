"""Tests for Repairs-compatible defect surfacing (spec SS16/SS17, DL-65)."""

from __future__ import annotations

import pytest
from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers import issue_registry as ir
from pytest_homeassistant.common import MockConfigEntry

from custom_components.htbw.const import CONF_ASSIGNMENTS, DOMAIN
from custom_components.htbw.models import RoomInteractionFunctionAssignment
from custom_components.htbw.repairs_support import assignment_issue_id


def _assignment(room_id: str, function: str, reference_id: str) -> dict:
    return {
        "room_id": room_id,
        "function": function,
        "reference_type": "entity_id",
        "reference_id": reference_id,
        "participation_state": "participating",
        "assigned_at": "2026-01-01T00:00:00+00:00",
        "updated_at": "2026-01-01T00:00:00+00:00",
    }


def _issue_id(entry: MockConfigEntry, reference_id: str) -> str:
    return assignment_issue_id(
        entry.entry_id,
        RoomInteractionFunctionAssignment.from_dict(
            _assignment(entry.data["room_id"], "spoken_response_output", reference_id)
        ),
    )


async def test_missing_reference_creates_a_standing_repairs_issue(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """A configured reference that no longer exists becomes a Repairs issue."""
    room_id = setup_integration.data["room_id"]
    hass.config_entries.async_update_entry(
        setup_integration,
        options={
            CONF_ASSIGNMENTS: [
                _assignment(room_id, "spoken_response_output", "media_player.long_removed")
            ]
        },
    )
    await hass.async_block_till_done()

    issue_id = _issue_id(setup_integration, "media_player.long_removed")
    issue = ir.async_get(hass).async_get_issue(DOMAIN, issue_id)
    assert issue is not None
    assert issue.severity is ir.IssueSeverity.ERROR
    assert issue.is_fixable is False


async def test_resolved_reference_creates_no_issue(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """A configured reference that still exists never creates a Repairs issue."""
    entity_registry = er.async_get(hass)
    entry = entity_registry.async_get_or_create("media_player", "test", "ok_speaker")
    room_id = setup_integration.data["room_id"]

    hass.config_entries.async_update_entry(
        setup_integration,
        options={
            CONF_ASSIGNMENTS: [_assignment(room_id, "spoken_response_output", entry.entity_id)]
        },
    )
    await hass.async_block_till_done()

    issue_id = _issue_id(setup_integration, entry.entity_id)
    assert ir.async_get(hass).async_get_issue(DOMAIN, issue_id) is None


async def test_transient_offline_entity_creates_no_issue(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """An entity that still exists but is currently unavailable is not a defect (spec SS17)."""
    entity_registry = er.async_get(hass)
    entry = entity_registry.async_get_or_create("media_player", "test", "offline_speaker")
    hass.states.async_set(entry.entity_id, "unavailable")
    room_id = setup_integration.data["room_id"]

    hass.config_entries.async_update_entry(
        setup_integration,
        options={
            CONF_ASSIGNMENTS: [_assignment(room_id, "spoken_response_output", entry.entity_id)]
        },
    )
    await hass.async_block_till_done()

    issue_id = _issue_id(setup_integration, entry.entity_id)
    assert ir.async_get(hass).async_get_issue(DOMAIN, issue_id) is None


async def test_issue_cleared_once_reference_is_corrected(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """Correcting a broken assignment through Options clears its Repairs issue."""
    room_id = setup_integration.data["room_id"]
    issue_id = _issue_id(setup_integration, "media_player.long_removed")

    hass.config_entries.async_update_entry(
        setup_integration,
        options={
            CONF_ASSIGNMENTS: [
                _assignment(room_id, "spoken_response_output", "media_player.long_removed")
            ]
        },
    )
    await hass.async_block_till_done()
    assert ir.async_get(hass).async_get_issue(DOMAIN, issue_id) is not None

    entity_registry = er.async_get(hass)
    fixed_entry = entity_registry.async_get_or_create("media_player", "test", "fixed_speaker")
    hass.config_entries.async_update_entry(
        setup_integration,
        options={
            CONF_ASSIGNMENTS: [
                _assignment(room_id, "spoken_response_output", fixed_entry.entity_id)
            ]
        },
    )
    await hass.async_block_till_done()

    assert ir.async_get(hass).async_get_issue(DOMAIN, issue_id) is None


@pytest.mark.parametrize("reverse", [False, True])
async def test_multiple_missing_references_have_independent_repairs(
    hass: HomeAssistant, setup_integration: MockConfigEntry, reverse: bool
) -> None:
    entity = er.async_get(hass).async_get_or_create("media_player", "test", "existing_output")
    references = ["media_player.absent_one", entity.entity_id, "media_player.absent_two"]
    records = [
        _assignment(setup_integration.data["room_id"], "spoken_response_output", reference)
        for reference in references
    ]
    hass.config_entries.async_update_entry(
        setup_integration,
        options={CONF_ASSIGNMENTS: records[::-1] if reverse else records},
    )
    await hass.async_block_till_done()
    registry = ir.async_get(hass)
    for reference in ("media_player.absent_one", "media_player.absent_two"):
        issue = registry.async_get_issue(DOMAIN, _issue_id(setup_integration, reference))
        assert issue is not None
        assert issue.config_entry_id == setup_integration.entry_id
    assert registry.async_get_issue(DOMAIN, _issue_id(setup_integration, entity.entity_id)) is None
    assert len([key for key in registry.issues if key[0] == DOMAIN]) == 2


async def test_registry_restoration_clears_issue_without_reconfiguration(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    reference = "media_player.returning_output"
    records = [_assignment(setup_integration.data["room_id"], "spoken_response_output", reference)]
    hass.config_entries.async_update_entry(setup_integration, options={CONF_ASSIGNMENTS: records})
    await hass.async_block_till_done()
    registry = ir.async_get(hass)
    issue_id = _issue_id(setup_integration, reference)
    assert registry.async_get_issue(DOMAIN, issue_id) is not None

    entity = er.async_get(hass).async_get_or_create(
        "media_player", "test", "returning_unique", suggested_object_id="returning_output"
    )
    assert entity.entity_id == reference
    await hass.async_block_till_done()
    assert registry.async_get_issue(DOMAIN, issue_id) is None
    assert setup_integration.options[CONF_ASSIGNMENTS] == records

    er.async_get(hass).async_update_entity(
        entity.entity_id, new_entity_id="media_player.renamed_output"
    )
    await hass.async_block_till_done()
    assert registry.async_get_issue(DOMAIN, issue_id) is not None
    assert setup_integration.options[CONF_ASSIGNMENTS] == records


async def test_unregistered_entity_existence_is_reconciled_without_availability_noise(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    reference = "media_player.state_only_output"
    hass.states.async_set(reference, "idle")
    hass.config_entries.async_update_entry(
        setup_integration,
        options={
            CONF_ASSIGNMENTS: [
                _assignment(setup_integration.data["room_id"], "spoken_response_output", reference)
            ]
        },
    )
    await hass.async_block_till_done()
    registry = ir.async_get(hass)
    issue_id = _issue_id(setup_integration, reference)
    assert registry.async_get_issue(DOMAIN, issue_id) is None
    hass.states.async_set(reference, "unavailable")
    await hass.async_block_till_done()
    assert registry.async_get_issue(DOMAIN, issue_id) is None
    hass.states.async_remove(reference)
    await hass.async_block_till_done()
    assert registry.async_get_issue(DOMAIN, issue_id) is not None
    hass.states.async_set(reference, "unavailable")
    await hass.async_block_till_done()
    assert registry.async_get_issue(DOMAIN, issue_id) is None


async def test_excluded_missing_reference_and_disabled_entity_do_not_raise_repairs(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    entity = er.async_get(hass).async_get_or_create(
        "media_player", "test", "disabled", disabled_by=er.RegistryEntryDisabler.USER
    )
    room_id = setup_integration.data["room_id"]
    excluded = _assignment(room_id, "spoken_response_output", "media_player.excluded")
    excluded["participation_state"] = "deliberately_excluded"
    hass.config_entries.async_update_entry(
        setup_integration,
        options={
            CONF_ASSIGNMENTS: [
                excluded,
                _assignment(room_id, "spoken_response_output", entity.entity_id),
            ]
        },
    )
    await hass.async_block_till_done()
    assert not [key for key in ir.async_get(hass).issues if key[0] == DOMAIN]


async def test_legacy_issue_reconciled_and_entry_removal_cleans_linked_issues(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    legacy_id = f"missing_reference_{setup_integration.entry_id}_spoken_response_output"
    ir.async_create_issue(
        hass,
        DOMAIN,
        legacy_id,
        is_fixable=False,
        is_persistent=True,
        severity=ir.IssueSeverity.ERROR,
        translation_key="missing_reference",
    )
    hass.config_entries.async_update_entry(
        setup_integration,
        options={
            CONF_ASSIGNMENTS: [
                _assignment(
                    setup_integration.data["room_id"],
                    "spoken_response_output",
                    "media_player.still_missing",
                )
            ]
        },
    )
    await hass.async_block_till_done()
    registry = ir.async_get(hass)
    assert registry.async_get_issue(DOMAIN, legacy_id) is None
    assert (
        registry.async_get_issue(DOMAIN, _issue_id(setup_integration, "media_player.still_missing"))
        is not None
    )
    await hass.config_entries.async_remove(setup_integration.entry_id)
    await hass.async_block_till_done()
    assert not [key for key in registry.issues if key[0] == DOMAIN]
