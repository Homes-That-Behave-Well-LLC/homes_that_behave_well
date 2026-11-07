"""Pytest fixtures for HTBW Core tests."""

from __future__ import annotations

import pytest
from homeassistant.core import HomeAssistant
from pytest_homeassistant.common import MockConfigEntry

from custom_components.htbw.const import CONF_ASSIGNMENTS, CONF_ROOM_ID, DOMAIN


@pytest.fixture
def mock_config_entry() -> MockConfigEntry:
    """Return a mock HTBW Core config entry for a single Room, unconfigured."""
    return MockConfigEntry(
        domain=DOMAIN,
        title="Den",
        unique_id="area_den",
        data={CONF_ROOM_ID: "area_den"},
        options={CONF_ASSIGNMENTS: []},
    )


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
