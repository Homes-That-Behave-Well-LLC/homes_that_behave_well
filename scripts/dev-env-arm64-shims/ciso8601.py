"""Minimal pure-Python shim for the ``ciso8601`` C extension.

Installed only by scripts/setup-dev-env.ps1's ARM64 Windows compatibility
layer, into the repository-local .venv's site-packages -- never shipped as
part of the HTBW Core integration itself (manifest.json declares no
requirements) and never used by the actual Home Assistant deployment target.

No prebuilt ``ciso8601`` wheel is available for win_arm64 at any released
version, and this development machine has no C toolchain to build one from
source. Home Assistant calls only ``ciso8601.parse_datetime(date_string)``,
inside a try/except that falls back to its own regex-based parser on any
exception (homeassistant/util/dt.py), so a slower but correct pure-Python
implementation is fully sufficient for development, static validation, and
automated tests.
"""

from __future__ import annotations

from datetime import datetime


def parse_datetime(date_string: str) -> datetime:
    """Parse an ISO 8601 datetime string, mirroring ciso8601.parse_datetime."""
    normalized = date_string.strip()
    if normalized.endswith("Z"):
        normalized = normalized[:-1] + "+00:00"
    return datetime.fromisoformat(normalized)
