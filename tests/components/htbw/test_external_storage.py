"""HTBW External Storage Foundation (Issue #211, DL-151).

The household connects External Storage exactly once; HTBW owns only the
governed ``HTBW`` root it creates beneath that connection. These tests prove,
above all, sibling-ownership safety (DL-151 SS2.6): HTBW never touches
content outside its own root, including Asset Intelligence's
``asset_documents`` sibling and any other unrelated household content on the
same share. A synthetic ``test_capability`` stands in for every real
capability (Voice Evidence under #212 is not implemented by this issue).
"""

from __future__ import annotations

import hashlib
import json
import os
import stat
from pathlib import Path

import pytest
from homeassistant.core import HomeAssistant
from homeassistant.helpers import issue_registry as ir
from pytest_homeassistant.common import MockConfigEntry

from custom_components.htbw.const import (
    CONF_EXTERNAL_STORAGE_PATH,
    DOMAIN,
    EXTERNAL_STORAGE_ROOT_MARKER,
    EXTERNAL_STORAGE_UNAVAILABLE_ISSUE_THRESHOLD,
    ExternalStorageOutcome,
)
from custom_components.htbw.external_storage import (
    CapabilityOwnershipError,
    ExternalStorageManager,
    ExternalStorageUnavailableError,
    check_root_sync,
    deprovision_capability_sync,
    probe_write_read_delete_sync,
    provision_capability_sync,
    resolve_root_sync,
)

from .conftest import household_entry

TEST_CAPABILITY = "test_capability"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _plant_siblings(base: Path) -> dict[Path, str]:
    """Plant legacy/unrelated content directly beside where HTBW's root will be.

    Mirrors DL-151 SS2.6 (legacy sibling coexistence): Asset Intelligence's own
    ``asset_documents`` folder, plus unrelated household content of mixed file
    types, all pre-dating and unrelated to HTBW's own root.
    """
    asset_documents = base / "asset_documents"
    asset_documents.mkdir()
    (asset_documents / "deed.pdf").write_bytes(b"%PDF-1.4 fake deed content")
    unrelated = base / "unrelated_household_data"
    unrelated.mkdir()
    (unrelated / "photo.jpg").write_bytes(bytes(range(256)))
    (unrelated / "notes.txt").write_bytes(b"shopping list")
    (base / "top_level_unrelated.bin").write_bytes(os.urandom(64))
    return {p: _sha256(p) for p in base.rglob("*") if p.is_file()}


def _assert_siblings_untouched(hashes: dict[Path, str]) -> None:
    for path, digest in hashes.items():
        assert path.exists(), f"sibling {path} was removed"
        assert _sha256(path) == digest, f"sibling {path} content changed"


# --- Synchronous helper unit tests (no event loop required) -----------------


def test_resolve_root_sync_never_touches_disk(tmp_path: Path) -> None:
    base, root = resolve_root_sync(str(tmp_path))
    assert base == tmp_path
    assert root == tmp_path / "HTBW"
    assert not root.exists()


def test_check_root_sync_reports_unavailable_when_base_missing(tmp_path: Path) -> None:
    missing = tmp_path / "not-mounted"
    outcome, reason = check_root_sync(missing, missing / "HTBW")
    assert outcome is ExternalStorageOutcome.UNAVAILABLE
    assert reason == "base_path_missing"
    # Never silently creates a stray local directory for an unmounted share.
    assert not missing.exists()


def test_check_root_sync_creates_root_and_marker_idempotently(tmp_path: Path) -> None:
    base, root = resolve_root_sync(str(tmp_path))
    outcome, reason = check_root_sync(base, root)
    assert outcome is ExternalStorageOutcome.AVAILABLE
    assert reason is None
    marker = root / EXTERNAL_STORAGE_ROOT_MARKER
    assert marker.exists()
    first_payload = json.loads(marker.read_bytes())

    # Second call (and a restart/reload) reuses the existing marker verbatim.
    outcome_again, reason_again = check_root_sync(base, root)
    assert outcome_again is ExternalStorageOutcome.AVAILABLE
    assert reason_again is None
    assert json.loads(marker.read_bytes()) == first_payload


def test_check_root_sync_rejects_corrupt_marker(tmp_path: Path) -> None:
    base, root = resolve_root_sync(str(tmp_path))
    root.mkdir()
    (root / EXTERNAL_STORAGE_ROOT_MARKER).write_bytes(b"not json")
    outcome, reason = check_root_sync(base, root)
    assert outcome is ExternalStorageOutcome.INVALID_ROOT
    assert reason == "root_marker_unreadable"


def test_check_root_sync_rejects_unsupported_marker_version(tmp_path: Path) -> None:
    base, root = resolve_root_sync(str(tmp_path))
    root.mkdir()
    (root / EXTERNAL_STORAGE_ROOT_MARKER).write_bytes(json.dumps({"version": 999}).encode())
    outcome, reason = check_root_sync(base, root)
    assert outcome is ExternalStorageOutcome.INVALID_ROOT
    assert reason == "root_marker_unsupported_version"


@pytest.mark.skipif(os.name == "nt", reason="POSIX permission bits; validated under WSL2")
def test_check_root_sync_reports_read_only(tmp_path: Path) -> None:
    base, root = resolve_root_sync(str(tmp_path))
    root.mkdir()
    root.chmod(stat.S_IRUSR | stat.S_IXUSR)
    try:
        outcome, reason = check_root_sync(base, root)
        assert outcome is ExternalStorageOutcome.READ_ONLY
        assert reason == "root_not_writable"
    finally:
        root.chmod(stat.S_IRWXU)


def test_probe_write_read_delete_sync_leaves_no_trace(tmp_path: Path) -> None:
    base, root = resolve_root_sync(str(tmp_path))
    check_root_sync(base, root)
    ok, reason = probe_write_read_delete_sync(root)
    assert ok is True
    assert reason is None
    assert list(root.iterdir()) == [root / EXTERNAL_STORAGE_ROOT_MARKER]


@pytest.mark.skipif(os.name == "nt", reason="POSIX permission bits; validated under WSL2")
def test_probe_write_read_delete_sync_reports_read_only(tmp_path: Path) -> None:
    base, root = resolve_root_sync(str(tmp_path))
    check_root_sync(base, root)
    root.chmod(stat.S_IRUSR | stat.S_IXUSR)
    try:
        ok, reason = probe_write_read_delete_sync(root)
        assert ok is False
        assert reason == "read_only"
    finally:
        root.chmod(stat.S_IRWXU)


def test_provision_and_deprovision_capability_are_idempotent(tmp_path: Path) -> None:
    base, root = resolve_root_sync(str(tmp_path))
    check_root_sync(base, root)

    branch = provision_capability_sync(root, TEST_CAPABILITY)
    assert branch == root / TEST_CAPABILITY
    assert branch.is_dir()
    # Calling again (restart, reload, repeated just-in-time provision) reuses it.
    branch_again = provision_capability_sync(root, TEST_CAPABILITY)
    assert branch_again == branch
    assert branch.is_dir()

    deprovision_capability_sync(root, TEST_CAPABILITY)
    assert not branch.exists()
    # Deprovisioning an already-absent capability is a no-op, not an error.
    deprovision_capability_sync(root, TEST_CAPABILITY)
    assert not branch.exists()


def test_deprovision_capability_rejects_escape_from_root(tmp_path: Path) -> None:
    base, root = resolve_root_sync(str(tmp_path))
    check_root_sync(base, root)
    sibling = tmp_path / "asset_documents"
    sibling.mkdir()
    (sibling / "deed.pdf").write_bytes(b"do not delete me")

    with pytest.raises(CapabilityOwnershipError):
        deprovision_capability_sync(root, "../asset_documents")

    assert (sibling / "deed.pdf").exists()


def test_capability_lifecycle_never_touches_siblings(tmp_path: Path) -> None:
    """DL-151 SS2.6: legacy sibling coexistence must survive the full lifecycle."""
    hashes = _plant_siblings(tmp_path)
    base, root = resolve_root_sync(str(tmp_path))

    check_root_sync(base, root)
    _assert_siblings_untouched(hashes)

    probe_write_read_delete_sync(root)
    _assert_siblings_untouched(hashes)

    branch = provision_capability_sync(root, TEST_CAPABILITY)
    (branch / "artifact.bin").write_bytes(b"governed capability content")
    _assert_siblings_untouched(hashes)

    # Repeated reconciliation passes (periodic health checks) are also inert.
    for _ in range(3):
        check_root_sync(base, root)
        probe_write_read_delete_sync(root)
    _assert_siblings_untouched(hashes)

    deprovision_capability_sync(root, TEST_CAPABILITY)
    assert not branch.exists()
    _assert_siblings_untouched(hashes)


# --- Async manager tests ------------------------------------------------------


def _entry(path: str | None) -> MockConfigEntry:
    options: dict[str, object] = {}
    if path is not None:
        options[CONF_EXTERNAL_STORAGE_PATH] = path
    return household_entry(options=options)


def _issues(hass: HomeAssistant) -> list[str]:
    return [
        issue_id
        for domain, issue_id in ir.async_get(hass).issues
        if domain == DOMAIN and issue_id.startswith("external_storage_")
    ]


async def test_not_configured_is_quiet(hass: HomeAssistant) -> None:
    entry = _entry(None)
    entry.add_to_hass(hass)
    manager = ExternalStorageManager(hass, entry)
    outcome = await manager.async_refresh()
    assert outcome is ExternalStorageOutcome.NOT_CONFIGURED
    assert manager.is_available() is False
    assert _issues(hass) == []


async def test_path_not_allowed_is_reported_only_after_it_persists(
    hass: HomeAssistant, tmp_path: Path
) -> None:
    entry = _entry(str(tmp_path))
    entry.add_to_hass(hass)
    # Deliberately not added to hass.config.allowlist_external_dirs.
    manager = ExternalStorageManager(hass, entry)
    outcome = await manager.async_refresh()
    assert outcome is ExternalStorageOutcome.PATH_NOT_ALLOWED
    assert manager.reason_code == "path_not_allowed"
    assert manager.is_available() is False
    assert _issues(hass) == []
    for _ in range(EXTERNAL_STORAGE_UNAVAILABLE_ISSUE_THRESHOLD - 1):
        await manager.async_refresh()
    assert _issues(hass) == ["external_storage_path_not_allowed"]


async def test_available_initializes_root(hass: HomeAssistant, tmp_path: Path) -> None:
    entry = _entry(str(tmp_path))
    entry.add_to_hass(hass)
    hass.config.allowlist_external_dirs = {str(tmp_path)}
    manager = ExternalStorageManager(hass, entry)
    outcome = await manager.async_refresh()
    assert outcome is ExternalStorageOutcome.AVAILABLE
    assert manager.is_available() is True
    assert (tmp_path / "HTBW" / EXTERNAL_STORAGE_ROOT_MARKER).exists()
    assert _issues(hass) == []


async def test_recovery_clears_a_previously_projected_issue(
    hass: HomeAssistant, tmp_path: Path
) -> None:
    """Once the household adds the path to allowlist_external_dirs, the issue clears."""
    entry = _entry(str(tmp_path))
    entry.add_to_hass(hass)
    manager = ExternalStorageManager(hass, entry)
    for _ in range(EXTERNAL_STORAGE_UNAVAILABLE_ISSUE_THRESHOLD):
        await manager.async_refresh()
    assert _issues(hass) == ["external_storage_path_not_allowed"]

    hass.config.allowlist_external_dirs = {str(tmp_path)}
    outcome = await manager.async_refresh()
    assert outcome is ExternalStorageOutcome.AVAILABLE
    assert _issues(hass) == []


async def test_refresh_is_idempotent_across_repeated_calls(
    hass: HomeAssistant, tmp_path: Path
) -> None:
    entry = _entry(str(tmp_path))
    entry.add_to_hass(hass)
    hass.config.allowlist_external_dirs = {str(tmp_path)}
    manager = ExternalStorageManager(hass, entry)
    for _ in range(3):
        outcome = await manager.async_refresh()
        assert outcome is ExternalStorageOutcome.AVAILABLE
    assert manager.is_available() is True


async def test_provision_capability_requires_availability(
    hass: HomeAssistant, tmp_path: Path
) -> None:
    entry = _entry(None)
    entry.add_to_hass(hass)
    manager = ExternalStorageManager(hass, entry)
    await manager.async_refresh()
    with pytest.raises(ExternalStorageUnavailableError):
        await manager.async_provision_capability(TEST_CAPABILITY)


async def test_deprovision_capability_requires_a_root(hass: HomeAssistant) -> None:
    entry = _entry(None)
    entry.add_to_hass(hass)
    manager = ExternalStorageManager(hass, entry)
    await manager.async_refresh()
    with pytest.raises(ExternalStorageUnavailableError):
        await manager.async_deprovision_capability(TEST_CAPABILITY)


async def test_invalid_capability_id_is_rejected(hass: HomeAssistant, tmp_path: Path) -> None:
    entry = _entry(str(tmp_path))
    entry.add_to_hass(hass)
    hass.config.allowlist_external_dirs = {str(tmp_path)}
    manager = ExternalStorageManager(hass, entry)
    await manager.async_refresh()
    for bad_id in ("../escape", "Has-Caps", "", ".hidden", "with/slash"):
        with pytest.raises(CapabilityOwnershipError):
            await manager.async_provision_capability(bad_id)


async def test_async_provision_and_deprovision_capability_round_trip(
    hass: HomeAssistant, tmp_path: Path
) -> None:
    entry = _entry(str(tmp_path))
    entry.add_to_hass(hass)
    hass.config.allowlist_external_dirs = {str(tmp_path)}
    manager = ExternalStorageManager(hass, entry)
    await manager.async_refresh()

    handle = await manager.async_provision_capability(TEST_CAPABILITY)
    assert handle.capability_id == TEST_CAPABILITY
    assert handle.path.is_dir()

    # Idempotent: a second just-in-time provision reuses the same branch.
    handle_again = await manager.async_provision_capability(TEST_CAPABILITY)
    assert handle_again.path == handle.path

    await manager.async_deprovision_capability(TEST_CAPABILITY)
    assert not handle.path.exists()
    # Idempotent: deprovisioning an already-removed capability is a no-op.
    await manager.async_deprovision_capability(TEST_CAPABILITY)


async def test_async_lifecycle_never_touches_siblings(hass: HomeAssistant, tmp_path: Path) -> None:
    hashes = _plant_siblings(tmp_path)
    entry = _entry(str(tmp_path))
    entry.add_to_hass(hass)
    hass.config.allowlist_external_dirs = {str(tmp_path)}
    manager = ExternalStorageManager(hass, entry)

    await manager.async_refresh()
    _assert_siblings_untouched(hashes)
    handle = await manager.async_provision_capability(TEST_CAPABILITY)
    _assert_siblings_untouched(hashes)
    await manager.async_refresh()
    _assert_siblings_untouched(hashes)
    await manager.async_deprovision_capability(TEST_CAPABILITY)
    assert not handle.path.exists()
    _assert_siblings_untouched(hashes)
