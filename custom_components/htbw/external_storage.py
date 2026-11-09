"""HTBW External Storage Foundation (Issue #211, DL-151).

The household connects External Storage exactly once, through Home
Assistant's own native external/network-storage mechanism (currently
Settings > System > Storage, a Share-usage target -- re-verify against
current official documentation before relying on this at a later date).
HTBW then owns only the governed root it creates beneath that connection,
and future capabilities (Voice Evidence under #212, Asset Documents,
Explainability) provision and deprovision their own exclusive branch
through this module rather than touching the filesystem directly.

Current official Home Assistant security guidance (retrieved 2026-11-09,
https://contributors.home-assistant.io/security/guides/integrations/,
"Check file paths") requires every integration that accepts a user-supplied
path to validate it against ``hass.config.is_allowed_path()`` before using
it. A Share-usage path is **not** in Home Assistant's default
``allowlist_external_dirs`` (only the ``www`` folder and configured
``media_dirs`` are default-allowed:
https://www.home-assistant.io/integrations/homeassistant/,
"allowlist_external_dirs", retrieved 2026-11-09) -- the household must add
it once, in their own ``configuration.yaml``. This module surfaces that
requirement as an actionable, named outcome (``path_not_allowed``) rather
than failing silently or working around the check.

Because ``media_dirs`` are themselves default-allowed, a household could
paste their Media-usage path into this same field and have it technically
succeed -- exactly the silent Media/Share substitution DL-151 and this
issue's own acceptance criteria forbid. ``is_media_path_sync`` rejects any
configured path that resolves under a configured Media folder as its own
distinct, actionable outcome (``media_path_not_supported``), independently
of the general allowlist check.

``discover_share_candidates_sync`` lets the household *pick* their path from
a dropdown instead of typing it. There is no supported way for a
non-``hassio`` integration to query Supervisor's Mounts API directly
(``aiohasupervisor``'s own documentation states its Supervisor-token access
is limited to Core's own ``hassio`` integration and Apps, each of which get
a token this Integration never receives), so this module does not attempt
it. Every Share-usage mount Home Assistant creates does, however, appear as
an ordinary subdirectory of Core's own fixed ``/share`` folder
(``HOME_ASSISTANT_SHARE_ROOT``) -- listing *that* needs no special role at
all. The household can still type a different path; this is a convenience,
never the only way in.

This module never implements a NAS/SMB/NFS client, never stores or asks for
storage credentials, and never scans, enumerates, or touches content outside
its own governed root (DL-151 SS2.6, legacy sibling coexistence).

Deprovisioning a capability's branch (DL-151 SS2.4) always requires an
explicit, already-disclosed confirmation (``async_deprovision_capability``'s
keyword-only, default-less ``confirmed`` argument) -- composing and
presenting the destructive-consequence disclosure itself (which artifact
classes are affected, whether re-enabling only recreates empty structures,
whether re-enrollment/re-capture is required) is each owning capability's
own responsibility, never this module's.
"""

from __future__ import annotations

import contextlib
import json
import logging
import os
import re
import secrets
import shutil
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.helpers.event import async_track_time_interval

from .const import (
    CONF_EXTERNAL_STORAGE_PATH,
    EXTERNAL_STORAGE_AUTHORIZATION_ISSUE_THRESHOLD,
    EXTERNAL_STORAGE_FAILURE_OUTCOMES,
    EXTERNAL_STORAGE_HEALTH_PROBE_PREFIX,
    EXTERNAL_STORAGE_REFRESH_INTERVAL_SECONDS,
    EXTERNAL_STORAGE_ROOT_MARKER,
    EXTERNAL_STORAGE_ROOT_MARKER_VERSION,
    EXTERNAL_STORAGE_ROOT_NAME,
    EXTERNAL_STORAGE_UNAVAILABLE_ISSUE_THRESHOLD,
    HOME_ASSISTANT_SHARE_ROOT,
    ExternalStorageOutcome,
)
from .models import HTBWConfigEntry
from .repairs_support import async_project_external_storage_issue

_LOGGER = logging.getLogger(__name__)

# A capability_id is a governed branch name, never a resident-supplied or
# display-derived path component (connected-storage.md's "no display-name
# keys" rule): lowercase ASCII, digits, and underscores only, non-empty, and
# never starting with a dot (which would otherwise collide with this module's
# own marker/probe file naming).
_CAPABILITY_ID_PATTERN = re.compile(r"^[a-z][a-z0-9_]*$")


class CapabilityOwnershipError(ValueError):
    """A capability_id is not a safe, governed branch name."""


class CapabilityDeprovisionNotConfirmedError(RuntimeError):
    """Raised when deprovisioning is requested without an explicit confirmation.

    DL-151 SS2.4 accepts capability deprovisioning as its own symmetric
    lifecycle, distinct from mere disable: a destructive-consequence
    disclosure (which artifact classes are affected, whether re-enabling
    recreates only empty structures, whether re-enrollment/re-capture is
    required) followed by explicit household confirmation, *before* any
    deletion. The Foundation does not know, and must never invent, what a
    future capability's own artifacts mean to the household -- composing
    that disclosure is the owning capability's responsibility (``#212`` and
    beyond). This exception makes the keyword-only ``confirmed`` argument on
    :meth:`ExternalStorageManager.async_deprovision_capability` impossible to
    satisfy by accident, so a caller cannot reach deletion without having
    made that explicit choice.
    """


class ExternalStorageUnavailableError(RuntimeError):
    """Raised when a capability requests provisioning while storage is unavailable."""

    def __init__(self, outcome: ExternalStorageOutcome, reason_code: str | None) -> None:
        super().__init__(f"External Storage is {outcome.value} ({reason_code})")
        self.outcome = outcome
        self.reason_code = reason_code


def _validate_capability_id(capability_id: str) -> str:
    if not _CAPABILITY_ID_PATTERN.fullmatch(capability_id):
        raise CapabilityOwnershipError(f"invalid capability_id: {capability_id!r}")
    return capability_id


@dataclass(frozen=True, slots=True)
class ExternalStorageCapabilityHandle:
    """A capability's own exclusive branch beneath the governed HTBW root.

    The capability never receives, and never needs, a path outside this
    branch. The Foundation created the branch, and the branch rule
    (DL-151: "a new branch exists only when an accepted capability
    introduces an artifact class with a complete lifecycle declaration")
    means nothing else is ever created inside it -- which is exactly what
    makes whole-branch deprovisioning safe.
    """

    capability_id: str
    path: Path


def _configured_path(entry: HTBWConfigEntry) -> str | None:
    value = entry.options.get(CONF_EXTERNAL_STORAGE_PATH)
    return value if isinstance(value, str) and value else None


def is_media_path_sync(path_str: str, media_dirs: dict[str, str]) -> bool:
    """Reject a configured path that is (or is beneath) a Home Assistant Media folder.

    A Media-usage path is, by default, already in ``allowlist_external_dirs``
    (unlike a Share-usage path -- the opposite of what DL-151 assumes), so
    ``is_allowed_path()`` alone cannot catch a household pasting their Media
    path here by mistake. Spec SS5/SS17/SS25: Media must never silently
    substitute for Share merely because Home Assistant would technically
    allow writing there.
    """
    try:
        resolved = Path(path_str).resolve()
    except OSError:
        return False
    for media_dir in media_dirs.values():
        try:
            resolved.relative_to(Path(media_dir).resolve())
        except OSError, ValueError:
            continue
        else:
            return True
    return False


def discover_share_candidates_sync(share_root: str = HOME_ASSISTANT_SHARE_ROOT) -> list[str]:
    """List subdirectories of Home Assistant's Supervisor share folder, as candidate paths.

    Every Share-usage network storage mount Home Assistant creates appears as
    a plain subdirectory of ``/share`` inside Core's own container -- this is
    an ordinary directory listing, never a Supervisor API call (see
    ``HOME_ASSISTANT_SHARE_ROOT``). Returns ``[]`` on any non-Supervisor
    install (``/share`` does not exist) or read failure; never raises, since
    the household can always type a path directly instead. Hidden entries
    (starting with ``.``) are excluded -- never a mount's own display name.
    """
    root = Path(share_root)
    try:
        if not root.is_dir():
            return []
        return sorted(
            str(root / entry.name)
            for entry in os.scandir(root)
            if entry.is_dir() and not entry.name.startswith(".")
        )
    except OSError:
        return []


# --- Synchronous filesystem helpers (invoked only through the executor) -----


def _fsync_dir(path: Path) -> None:
    try:
        fd = os.open(path, os.O_RDONLY)
    except OSError:
        return
    try:
        os.fsync(fd)
    except OSError:
        pass
    finally:
        os.close(fd)


def _atomic_write_bytes(path: Path, data: bytes) -> None:
    tmp = path.with_name(f".{path.name}.{secrets.token_hex(6)}.tmp")
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, path)
    except BaseException:
        with contextlib.suppress(OSError):
            os.unlink(tmp)
        raise
    _fsync_dir(path.parent)


def resolve_root_sync(path_str: str) -> tuple[Path, Path]:
    """Return (configured base path, governed HTBW root) without touching disk."""
    base = Path(path_str)
    return base, base / EXTERNAL_STORAGE_ROOT_NAME


def check_root_sync(base: Path, root: Path) -> tuple[ExternalStorageOutcome, str | None]:
    """Validate (or create) the governed root and its marker.

    Only ever creates the single ``HTBW`` child of an already-existing
    configured base path -- never the base path itself (``parents=True``
    would silently paper over an unmounted/missing share by creating an
    unrelated local directory tree with the same name).
    """
    if not base.is_dir():
        return ExternalStorageOutcome.UNAVAILABLE, "base_path_missing"

    marker = root / EXTERNAL_STORAGE_ROOT_MARKER
    try:
        root.mkdir(exist_ok=True)
    except PermissionError:
        return ExternalStorageOutcome.READ_ONLY, "root_not_writable"
    except OSError as err:
        return ExternalStorageOutcome.UNAVAILABLE, f"root_mkdir_failed:{err.errno}"

    if marker.exists():
        try:
            payload = json.loads(marker.read_bytes())
        except OSError, ValueError:
            return ExternalStorageOutcome.INVALID_ROOT, "root_marker_unreadable"
        if (
            not isinstance(payload, dict)
            or payload.get("version") != EXTERNAL_STORAGE_ROOT_MARKER_VERSION
        ):
            return ExternalStorageOutcome.INVALID_ROOT, "root_marker_unsupported_version"
        return ExternalStorageOutcome.AVAILABLE, None

    # First acceptance of a healthy connection: create only the base marker.
    # Never a capability structure here (DL-151 SS2.2: just-in-time only).
    payload = {
        "version": EXTERNAL_STORAGE_ROOT_MARKER_VERSION,
        "created_at": datetime.now(UTC).isoformat(),
    }
    try:
        _atomic_write_bytes(marker, json.dumps(payload, sort_keys=True).encode("utf-8"))
    except PermissionError:
        # The root directory itself already existed (mkdir above was a no-op)
        # but denies writes -- the same distinct outcome as a root that could
        # not be created at all, not the transient WRITE_FAILED outcome.
        return ExternalStorageOutcome.READ_ONLY, "root_not_writable"
    except OSError as err:
        return ExternalStorageOutcome.WRITE_FAILED, f"root_marker_write_failed:{err.errno}"
    return ExternalStorageOutcome.AVAILABLE, None


def probe_write_read_delete_sync(root: Path) -> tuple[bool, str | None]:
    """Bounded health probe confined to the governed root; never touches siblings.

    Each phase is its own distinct, non-suppressed failure (spec SS16:
    "do not collapse every failure into storage unavailable"; cleanup failure
    is reported, never silently swallowed, so it remains a provable outcome).
    """
    probe = root / f"{EXTERNAL_STORAGE_HEALTH_PROBE_PREFIX}{secrets.token_hex(8)}"
    token = secrets.token_hex(16).encode("ascii")
    try:
        _atomic_write_bytes(probe, token)
    except PermissionError:
        return False, "read_only"
    except OSError as err:
        return False, f"probe_write_failed:{err.errno}"

    try:
        read_back = probe.read_bytes()
    except OSError as err:
        with contextlib.suppress(OSError):
            probe.unlink(missing_ok=True)
        return False, f"probe_read_failed:{err.errno}"
    if read_back != token:
        with contextlib.suppress(OSError):
            probe.unlink(missing_ok=True)
        return False, "probe_mismatch"

    try:
        probe.unlink()
    except OSError as err:
        return False, f"probe_cleanup_failed:{err.errno}"
    return True, None


def provision_capability_sync(root: Path, capability_id: str) -> Path:
    """Create (or reuse) a capability's own exclusive branch. Idempotent."""
    branch = root / capability_id
    branch.mkdir(exist_ok=True)
    return branch


def deprovision_capability_sync(root: Path, capability_id: str) -> None:
    """Remove a capability's own branch in full. Idempotent; never touches siblings."""
    branch = root / capability_id
    resolved_root = root.resolve()
    resolved_branch = branch.resolve()
    # Ownership safety: only ever remove a direct child of the governed root,
    # never anything reached by walking or globbing the parent (DL-151 SS2.4;
    # sibling-ownership safety). A capability_id containing a path separator
    # is already rejected by _validate_capability_id before this is reached.
    if resolved_branch.parent != resolved_root:
        raise CapabilityOwnershipError(f"{branch} is not a direct child of {root}")
    if resolved_branch.exists():
        shutil.rmtree(resolved_branch)
        _fsync_dir(resolved_root)


# --- Async manager -----------------------------------------------------------


@dataclass
class ExternalStorageManager:
    """Household-entry runtime state for the optional External Storage Foundation.

    Generic and capability-agnostic: #212 (Voice Evidence) and any future
    Connected-Storage capability provision/deprovision their own branch
    through this manager rather than touching the filesystem directly.
    """

    hass: HomeAssistant
    entry: HTBWConfigEntry
    outcome: ExternalStorageOutcome = ExternalStorageOutcome.NOT_CONFIGURED
    reason_code: str | None = None
    root: Path | None = None
    consecutive_unavailable: int = 0

    def is_available(self) -> bool:
        return self.outcome is ExternalStorageOutcome.AVAILABLE and self.root is not None

    async def async_refresh(self) -> ExternalStorageOutcome:
        """Re-validate configuration, path permission, root, and read/write health."""
        path_str = _configured_path(self.entry)
        if path_str is None:
            self.root = None
            self._set(ExternalStorageOutcome.NOT_CONFIGURED, None)
            return self.outcome

        allowed = await self.hass.async_add_executor_job(self.hass.config.is_allowed_path, path_str)
        if not allowed:
            self.root = None
            self._set(ExternalStorageOutcome.PATH_NOT_ALLOWED, "path_not_allowed")
            return self.outcome

        is_media = await self.hass.async_add_executor_job(
            is_media_path_sync, path_str, dict(self.hass.config.media_dirs)
        )
        if is_media:
            self.root = None
            self._set(ExternalStorageOutcome.MEDIA_PATH_NOT_SUPPORTED, "configured_path_is_media")
            return self.outcome

        base, root = await self.hass.async_add_executor_job(resolve_root_sync, path_str)
        outcome, reason = await self.hass.async_add_executor_job(check_root_sync, base, root)
        if outcome is ExternalStorageOutcome.AVAILABLE:
            ok, probe_reason = await self.hass.async_add_executor_job(
                probe_write_read_delete_sync, root
            )
            if not ok:
                outcome = (
                    ExternalStorageOutcome.READ_ONLY
                    if probe_reason == "read_only"
                    else ExternalStorageOutcome.WRITE_FAILED
                )
                reason = probe_reason

        self.root = root if outcome is ExternalStorageOutcome.AVAILABLE else None
        self._set(outcome, reason)
        return self.outcome

    def _set(self, outcome: ExternalStorageOutcome, reason: str | None) -> None:
        previous = self.outcome
        self.outcome, self.reason_code = outcome, reason
        if outcome in EXTERNAL_STORAGE_FAILURE_OUTCOMES:
            self.consecutive_unavailable += 1
        else:
            self.consecutive_unavailable = 0
        threshold = (
            EXTERNAL_STORAGE_AUTHORIZATION_ISSUE_THRESHOLD
            if outcome is ExternalStorageOutcome.PATH_NOT_ALLOWED
            else EXTERNAL_STORAGE_UNAVAILABLE_ISSUE_THRESHOLD
        )
        projected: ExternalStorageOutcome | None = outcome
        if (
            outcome not in (ExternalStorageOutcome.AVAILABLE, ExternalStorageOutcome.NOT_CONFIGURED)
            and self.consecutive_unavailable < threshold
        ):
            projected = None
        async_project_external_storage_issue(
            self.hass, self.entry, projected, reason, configured_path=_configured_path(self.entry)
        )
        if outcome is not previous:
            _LOGGER.info(
                "HTBW External Storage capability is %s%s",
                outcome.value,
                f" ({reason})" if reason else "",
            )

    async def async_provision_capability(
        self, capability_id: str
    ) -> ExternalStorageCapabilityHandle:
        """Create (or reuse) a capability's own exclusive branch, just in time."""
        _validate_capability_id(capability_id)
        if not self.is_available() or self.root is None:
            raise ExternalStorageUnavailableError(self.outcome, self.reason_code)
        branch = await self.hass.async_add_executor_job(
            provision_capability_sync, self.root, capability_id
        )
        return ExternalStorageCapabilityHandle(capability_id, branch)

    async def async_deprovision_capability(self, capability_id: str, *, confirmed: bool) -> None:
        """Remove a capability's own branch in full. Idempotent.

        ``confirmed`` is keyword-only and has no default: DL-151 SS2.4 accepts
        deprovisioning as its own symmetric lifecycle -- destructive-consequence
        disclosure, then explicit household confirmation, *before* deletion.
        Composing and presenting that disclosure (which artifact classes are
        affected, whether re-enabling only recreates empty structures, whether
        re-enrollment/re-capture is required) is the calling capability's own
        responsibility; the Foundation never invents it. Passing ``False``
        (or skipping the disclosure/confirmation step entirely) raises
        :class:`CapabilityDeprovisionNotConfirmedError` instead of deleting
        anything.
        """
        _validate_capability_id(capability_id)
        if not confirmed:
            raise CapabilityDeprovisionNotConfirmedError(
                f"deprovisioning {capability_id!r} requires an explicit, "
                "already-disclosed household confirmation"
            )
        if self.root is None:
            raise ExternalStorageUnavailableError(self.outcome, self.reason_code)
        await self.hass.async_add_executor_job(
            deprovision_capability_sync, self.root, capability_id
        )


async def async_setup_external_storage(
    hass: HomeAssistant, entry: HTBWConfigEntry
) -> ExternalStorageManager:
    """Create the manager and schedule non-blocking, periodic reconciliation.

    With no configured path there is nothing to probe: the outcome is
    NOT_CONFIGURED, and no Repairs issue is ever raised for that state alone
    (DL-148: an optional capability's absence is never nagged about).
    """
    manager = ExternalStorageManager(hass, entry)
    await manager.async_refresh()

    async def _refresh(_now: Any = None) -> None:
        await manager.async_refresh()

    entry.async_on_unload(
        async_track_time_interval(
            hass, _refresh, timedelta(seconds=EXTERNAL_STORAGE_REFRESH_INTERVAL_SECONDS)
        )
    )
    return manager
