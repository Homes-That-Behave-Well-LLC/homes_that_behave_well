"""Pytest fixtures for HTBW Core tests.

Issue #162 (Owner decision B): one household HTBW config entry with each Room as
a native config subentry. `mock_config_entry` is that household entry with one
Den Room subentry; Room-level helpers read and write the Den subentry exactly
where #201's tests read and wrote the per-Room entry.
"""

from __future__ import annotations

from typing import Any

import pytest
from homeassistant import config_entries
from homeassistant.config_entries import ConfigSubentry
from homeassistant.core import HomeAssistant
from pytest_homeassistant.common import MockConfigEntry

from custom_components.htbw.const import (
    CONF_ASSIGNMENTS,
    CONF_RETAIN_ENROLLMENT_RECORDINGS,
    CONF_ROOM_ID,
    DOMAIN,
    HOUSEHOLD_TITLE,
    HOUSEHOLD_UNIQUE_ID,
    RETENTION_DELETE,
    SUBENTRY_TYPE_ROOM,
)

DEN_ROOM_ID = "area_den"
DEN_SUBENTRY_ID = "den_room_subentry"


def household_entry(
    *,
    rooms: list[dict[str, Any]] | None = None,
    data: dict[str, Any] | None = None,
    options: dict[str, Any] | None = None,
) -> MockConfigEntry:
    """Build a household HTBW entry (version 2) with the given Room subentries."""
    return MockConfigEntry(
        domain=DOMAIN,
        title=HOUSEHOLD_TITLE,
        unique_id=HOUSEHOLD_UNIQUE_ID,
        version=2,
        minor_version=1,
        data=data or {},
        options=options
        if options is not None
        else {CONF_RETAIN_ENROLLMENT_RECORDINGS: RETENTION_DELETE},
        subentries_data=rooms
        if rooms is not None
        else [room_subentry_data(DEN_ROOM_ID, "Den", [], subentry_id=DEN_SUBENTRY_ID)],
    )


def room_subentry_data(
    room_id: str,
    title: str,
    assignments: list[dict[str, Any]],
    *,
    subentry_id: str | None = None,
) -> dict[str, Any]:
    """Return subentries_data for one Room."""
    data: dict[str, Any] = {
        "data": {CONF_ROOM_ID: room_id, CONF_ASSIGNMENTS: assignments},
        "subentry_type": SUBENTRY_TYPE_ROOM,
        "title": title,
        "unique_id": room_id,
    }
    if subentry_id is not None:
        data["subentry_id"] = subentry_id
    return data


def den(entry: MockConfigEntry) -> ConfigSubentry:
    """Return the Den Room subentry."""
    return next(s for s in entry.subentries.values() if s.unique_id == DEN_ROOM_ID)


def set_den_assignments(
    hass: HomeAssistant, entry: MockConfigEntry, assignments: list[dict[str, Any]]
) -> None:
    """Write the Den Room subentry's records (fires the entry's update listener)."""
    subentry = den(entry)
    hass.config_entries.async_update_subentry(
        entry,
        subentry,
        data={CONF_ROOM_ID: subentry.data[CONF_ROOM_ID], CONF_ASSIGNMENTS: assignments},
    )


async def start_den_reconfigure(hass: HomeAssistant, entry: MockConfigEntry) -> dict[str, Any]:
    """Open the Den Room reconfigure flow (the #201 Room options form)."""
    return await hass.config_entries.subentries.async_init(
        (entry.entry_id, SUBENTRY_TYPE_ROOM),
        context={
            "source": config_entries.SOURCE_RECONFIGURE,
            "subentry_id": den(entry).subentry_id,
        },
    )


def legacy_room_entry(
    room_id: str, title: str, assignments: list[dict[str, Any]]
) -> MockConfigEntry:
    """A #201 (version 1) per-Room config entry, exactly as #201 stored it."""
    return MockConfigEntry(
        domain=DOMAIN,
        title=title,
        unique_id=room_id,
        version=1,
        data={CONF_ROOM_ID: room_id},
        options={CONF_ASSIGNMENTS: assignments},
    )


@pytest.fixture
def mock_config_entry() -> MockConfigEntry:
    """Return the household HTBW entry with one unconfigured Den Room subentry."""
    return household_entry()


@pytest.fixture
async def setup_integration(
    hass: HomeAssistant,
    mock_config_entry: MockConfigEntry,
) -> MockConfigEntry:
    """Set up the HTBW Core integration for tests."""
    mock_config_entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(mock_config_entry.entry_id)
    await hass.async_block_till_done()
    return mock_config_entry
