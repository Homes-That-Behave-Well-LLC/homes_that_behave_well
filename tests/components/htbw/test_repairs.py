"""Tests for Repairs-compatible defect surfacing (spec SS16/SS17, DL-65)."""

from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers import issue_registry as ir
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.htbw.const import CONF_ASSIGNMENTS, DOMAIN, ISSUE_ID_TEMPLATE


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

    issue_id = ISSUE_ID_TEMPLATE.format(
        entry_id=setup_integration.entry_id, function="spoken_response_output"
    )
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
            CONF_ASSIGNMENTS: [
                _assignment(room_id, "spoken_response_output", entry.entity_id)
            ]
        },
    )
    await hass.async_block_till_done()

    issue_id = ISSUE_ID_TEMPLATE.format(
        entry_id=setup_integration.entry_id, function="spoken_response_output"
    )
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
            CONF_ASSIGNMENTS: [
                _assignment(room_id, "spoken_response_output", entry.entity_id)
            ]
        },
    )
    await hass.async_block_till_done()

    issue_id = ISSUE_ID_TEMPLATE.format(
        entry_id=setup_integration.entry_id, function="spoken_response_output"
    )
    assert ir.async_get(hass).async_get_issue(DOMAIN, issue_id) is None


async def test_issue_cleared_once_reference_is_corrected(
    hass: HomeAssistant, setup_integration: MockConfigEntry
) -> None:
    """Correcting a broken assignment through Options clears its Repairs issue."""
    room_id = setup_integration.data["room_id"]
    issue_id = ISSUE_ID_TEMPLATE.format(
        entry_id=setup_integration.entry_id, function="spoken_response_output"
    )

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
