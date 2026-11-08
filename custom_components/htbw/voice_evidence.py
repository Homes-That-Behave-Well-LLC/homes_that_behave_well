"""HTBW Integration side of the Voice Evidence App boundary (Issue #162).

The Voice Evidence App is an external runtime (DL-50 D1/D4). This module is
the Integration's only connection to it: a Contract A (handshake and
synchronization) client over the App's private, authenticated API, plus the
household configuration mirror for "Retain Enrollment Recordings".

Boundaries this module keeps (docs/contracts/identity-contract.md):
- It never loads a model, encodes audio, compares voices, or emulates the App
  when it is absent (DL-41, DL-50 D2). App absence is a named outcome only.
- It stores no biometric artifact. Contract A carries Voiceprint existence by
  person_id, never a Voiceprint, embedding, recording, or raw score.
- It never pushes a retention policy or disposition through Contracts A-D. The
  household setting is mirrored into the App's own official app options (Owner
  decision, #162); the App reads its options and owns every artifact decision.
- Every App call is bounded by a timeout; Home Assistant startup never waits on
  the App, and App failure never fails the household entry or any Room.
"""

from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass, field
from datetime import timedelta
from typing import Any

import aiohttp
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.event import async_track_time_interval

from .const import (
    CONF_API_SECRET,
    CONF_APP_SLUG,
    CONF_HOST,
    CONF_PORT,
    CONF_RETAIN_ENROLLMENT_RECORDINGS,
    CONF_VOICE_EVIDENCE,
    RETENTION_RETAIN,
    VOICE_EVIDENCE_CONTRACT_MAJOR,
    VOICE_EVIDENCE_REFRESH_INTERVAL_SECONDS,
    VOICE_EVIDENCE_REQUEST_TIMEOUT_SECONDS,
    VOICE_EVIDENCE_UNREACHABLE_ISSUE_THRESHOLD,
    VoiceEvidenceOutcome,
)
from .models import HTBWConfigEntry
from .repairs_support import (
    async_create_retention_sync_issue,
    async_delete_retention_sync_issue,
    async_project_voice_evidence_issue,
)

_LOGGER = logging.getLogger(__name__)

APP_OPTION_RETAIN = "retain_enrollment_recordings"
_STATUS_VALUES = {"available", "unavailable", "incompatible"}
_VOICEPRINT_STATES = {"current", "incompatible"}


@dataclass(frozen=True, slots=True)
class VoiceEvidenceConnection:
    """App endpoint and credential provisioned through Supervisor Discovery."""

    host: str
    port: int
    api_secret: str
    app_slug: str | None = None

    @classmethod
    def from_entry(cls, entry: HTBWConfigEntry) -> VoiceEvidenceConnection | None:
        """Return the stored connection, or None when the App was never provisioned."""
        raw = entry.data.get(CONF_VOICE_EVIDENCE)
        if not isinstance(raw, dict):
            return None
        host, port, secret = raw.get(CONF_HOST), raw.get(CONF_PORT), raw.get(CONF_API_SECRET)
        if not isinstance(host, str) or not host or not isinstance(secret, str) or not secret:
            return None
        try:
            port_number = int(port)  # type: ignore[arg-type]
        except TypeError, ValueError:
            return None
        if not 0 < port_number < 65536:
            return None
        slug = raw.get(CONF_APP_SLUG)
        return cls(host, port_number, secret, slug if isinstance(slug, str) else None)

    def __repr__(self) -> str:
        """Never render the secret."""
        return (
            f"VoiceEvidenceConnection(host=<redacted>, port={self.port}, app_slug={self.app_slug})"
        )


@dataclass(frozen=True, slots=True)
class VoiceprintState:
    """Contract A synchronization state for one person_id. No biometric content."""

    person_id: str
    voiceprint_exists: bool
    voiceprint_state: str
    retained_recordings: bool


@dataclass(frozen=True, slots=True)
class VoiceEvidenceStatus:
    """A validated Contract A status report."""

    contract_version: str
    app_version: str | None
    status: str
    reason_code: str | None
    compatibility_id: str | None
    encoder_family: str | None
    encoder_version: str | None
    audio_contract_version: str | None
    model_state: str | None
    optional_capabilities: tuple[str, ...]
    applied_retain_enrollment_recordings: bool | None
    voiceprints: tuple[VoiceprintState, ...]


class MalformedStatusError(ValueError):
    """The App returned a Contract A payload HTBW cannot accept (rejected, never partially used)."""


def parse_status(payload: Any) -> VoiceEvidenceStatus:
    """Validate a Contract A status payload, rejecting anything malformed."""
    if not isinstance(payload, dict):
        raise MalformedStatusError("status payload is not an object")
    contract_version = payload.get("contract_version")
    status = payload.get("status")
    if not isinstance(contract_version, str) or status not in _STATUS_VALUES:
        raise MalformedStatusError("missing contract_version or status")

    def _opt_str(key: str) -> str | None:
        value = payload.get(key)
        if value is not None and not isinstance(value, str):
            raise MalformedStatusError(f"{key} is not a string")
        return value

    capabilities = payload.get("optional_capabilities", [])
    if not isinstance(capabilities, list) or not all(isinstance(c, str) for c in capabilities):
        raise MalformedStatusError("optional_capabilities is not a list of strings")

    retention = payload.get("retention") or {}
    applied = (
        retention.get("applied_retain_enrollment_recordings")
        if isinstance(retention, dict)
        else None
    )
    if applied is not None and not isinstance(applied, bool):
        raise MalformedStatusError("applied retention is not a boolean")

    model = payload.get("model_artifact")
    model_state = model.get("state") if isinstance(model, dict) else None

    voiceprints: list[VoiceprintState] = []
    raw_voiceprints = payload.get("voiceprints", [])
    if not isinstance(raw_voiceprints, list):
        raise MalformedStatusError("voiceprints is not a list")
    seen: set[str] = set()
    for item in raw_voiceprints:
        if not isinstance(item, dict):
            raise MalformedStatusError("voiceprint entry is not an object")
        person_id = item.get("person_id")
        exists = item.get("voiceprint_exists")
        state = item.get("voiceprint_state")
        retained = item.get("retained_recordings")
        if (
            not isinstance(person_id, str)
            or not person_id
            or person_id in seen
            or not isinstance(exists, bool)
            or state not in _VOICEPRINT_STATES
            or not isinstance(retained, bool)
        ):
            raise MalformedStatusError("invalid voiceprint entry")
        seen.add(person_id)
        voiceprints.append(VoiceprintState(person_id, exists, state, retained))

    return VoiceEvidenceStatus(
        contract_version=contract_version,
        app_version=_opt_str("app_version"),
        status=status,
        reason_code=_opt_str("reason_code"),
        compatibility_id=_opt_str("compatibility_id"),
        encoder_family=_opt_str("encoder_family"),
        encoder_version=_opt_str("encoder_version"),
        audio_contract_version=_opt_str("audio_contract_version"),
        model_state=model_state if isinstance(model_state, str) else None,
        optional_capabilities=tuple(capabilities),
        applied_retain_enrollment_recordings=applied,
        voiceprints=tuple(voiceprints),
    )


def contract_compatible(contract_version: str) -> bool:
    """Return whether the App speaks a compatible Contract A major version."""
    major, _, _ = contract_version.partition(".")
    return major.isdigit() and int(major) == VOICE_EVIDENCE_CONTRACT_MAJOR


async def async_fetch_status(
    hass: HomeAssistant, connection: VoiceEvidenceConnection
) -> tuple[VoiceEvidenceOutcome, VoiceEvidenceStatus | None, str | None]:
    """Run one bounded Contract A status request and classify the DL-41 outcome."""
    session = async_get_clientsession(hass)
    url = f"http://{connection.host}:{connection.port}/v1/status"
    try:
        async with asyncio.timeout(VOICE_EVIDENCE_REQUEST_TIMEOUT_SECONDS):
            async with session.get(
                url,
                headers={"Authorization": f"Bearer {connection.api_secret}"},
                allow_redirects=False,
            ) as response:
                if response.status in (401, 403):
                    return VoiceEvidenceOutcome.AUTHENTICATION_FAILED, None, "credential_rejected"
                if response.status != 200:
                    return VoiceEvidenceOutcome.UNREACHABLE, None, f"http_{response.status}"
                payload = await response.json(content_type=None)
    except TimeoutError:
        return VoiceEvidenceOutcome.UNREACHABLE, None, "timeout"
    except aiohttp.ClientError, OSError:
        return VoiceEvidenceOutcome.UNREACHABLE, None, "connection_failed"
    except ValueError:
        return VoiceEvidenceOutcome.INCOMPATIBLE, None, "malformed_status"

    try:
        status = parse_status(payload)
    except MalformedStatusError:
        return VoiceEvidenceOutcome.INCOMPATIBLE, None, "malformed_status"
    if not contract_compatible(status.contract_version):
        return VoiceEvidenceOutcome.INCOMPATIBLE, status, "contract_version_mismatch"
    if status.status == "incompatible":
        return VoiceEvidenceOutcome.INCOMPATIBLE, status, status.reason_code
    if status.status == "unavailable":
        return VoiceEvidenceOutcome.APP_UNAVAILABLE, status, status.reason_code
    return VoiceEvidenceOutcome.AVAILABLE, status, None


def configured_retention(entry: HTBWConfigEntry) -> bool | None:
    """Return the household retention choice, or None while it has not been made."""
    value = entry.options.get(CONF_RETAIN_ENROLLMENT_RECORDINGS)
    if value is None:
        return None
    return value == RETENTION_RETAIN


async def async_mirror_retention_to_app(
    hass: HomeAssistant, connection: VoiceEvidenceConnection, retain: bool
) -> bool:
    """Mirror the household setting into the App's own options (official hassio helper).

    This is configuration synchronization only: it writes the App's single
    operational option and nothing else. It never names a recording, person, or
    Voiceprint, and it is never part of Contracts A-D.
    """
    if connection.app_slug is None or "hassio" not in hass.config.components:
        return False
    from homeassistant.components.hassio import AddonError, AddonManager

    manager = AddonManager(hass, _LOGGER, "HTBW Voice Evidence", connection.app_slug)
    try:
        async with asyncio.timeout(VOICE_EVIDENCE_REQUEST_TIMEOUT_SECONDS):
            await manager.async_set_addon_options({APP_OPTION_RETAIN: retain})
    except AddonError, TimeoutError:
        return False
    return True


@dataclass
class VoiceEvidenceManager:
    """Household-entry runtime state for the optional Voice Evidence dependency."""

    hass: HomeAssistant
    entry: HTBWConfigEntry
    outcome: VoiceEvidenceOutcome = VoiceEvidenceOutcome.NOT_CONFIGURED
    reason_code: str | None = None
    status: VoiceEvidenceStatus | None = None
    consecutive_unreachable: int = 0
    retention_synchronized: bool | None = None
    _lock: asyncio.Lock = field(default_factory=asyncio.Lock)

    def voiceprint_exists(self, person_id: str) -> bool | None:
        """Return App-authoritative existence; None means unknown (never "not enrolled")."""
        if self.outcome is not VoiceEvidenceOutcome.AVAILABLE or self.status is None:
            return None
        return any(
            v.person_id == person_id and v.voiceprint_exists for v in self.status.voiceprints
        )

    async def async_refresh(self) -> VoiceEvidenceOutcome:
        """Synchronize Contract A state once and reconcile the household retention mirror."""
        async with self._lock:
            connection = VoiceEvidenceConnection.from_entry(self.entry)
            if connection is None:
                self._set(VoiceEvidenceOutcome.NOT_CONFIGURED, None, None)
                return self.outcome
            outcome, status, reason = await async_fetch_status(self.hass, connection)
            self._set(outcome, status, reason)
            if outcome is not VoiceEvidenceOutcome.UNREACHABLE and status is not None:
                await self._async_reconcile_retention(connection, status)
            return self.outcome

    def _set(
        self,
        outcome: VoiceEvidenceOutcome,
        status: VoiceEvidenceStatus | None,
        reason: str | None,
    ) -> None:
        previous = self.outcome
        self.outcome, self.status, self.reason_code = outcome, status, reason
        if outcome is VoiceEvidenceOutcome.UNREACHABLE:
            self.consecutive_unreachable += 1
        else:
            self.consecutive_unreachable = 0
        projected: VoiceEvidenceOutcome | None = outcome
        if (
            outcome is VoiceEvidenceOutcome.UNREACHABLE
            and self.consecutive_unreachable < VOICE_EVIDENCE_UNREACHABLE_ISSUE_THRESHOLD
        ):
            projected = None
        async_project_voice_evidence_issue(self.hass, self.entry, projected, reason)
        if outcome is not previous:
            _LOGGER.info(
                "HTBW Voice Evidence capability is %s%s",
                outcome.value,
                f" ({reason})" if reason else "",
            )

    async def _async_reconcile_retention(
        self, connection: VoiceEvidenceConnection, status: VoiceEvidenceStatus
    ) -> None:
        retain = configured_retention(self.entry)
        if retain is None:
            return
        if status.applied_retain_enrollment_recordings is retain:
            self.retention_synchronized = True
            async_delete_retention_sync_issue(self.hass)
            return
        if await async_mirror_retention_to_app(self.hass, connection, retain):
            self.retention_synchronized = False  # written; confirmed on a later report
            async_delete_retention_sync_issue(self.hass)
        else:
            self.retention_synchronized = False
            async_create_retention_sync_issue(self.hass, self.entry)


async def async_setup_voice_evidence(
    hass: HomeAssistant, entry: HTBWConfigEntry
) -> VoiceEvidenceManager:
    """Create the manager and schedule non-blocking, periodic synchronization.

    With no provisioned App there is nothing to poll: the outcome is
    NOT_CONFIGURED, and Supervisor Discovery provisioning reloads the entry.
    """
    manager = VoiceEvidenceManager(hass, entry)
    if VoiceEvidenceConnection.from_entry(entry) is None:
        await manager.async_refresh()
        return manager

    async def _refresh(_now: Any = None) -> None:
        await manager.async_refresh()

    entry.async_create_background_task(hass, _refresh(), "htbw voice evidence initial sync")
    entry.async_on_unload(
        async_track_time_interval(
            hass, _refresh, timedelta(seconds=VOICE_EVIDENCE_REFRESH_INTERVAL_SECONDS)
        )
    )
    return manager
