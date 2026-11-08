"""Voiceprint lifecycle foundation (internal library functions, no public API).

* :meth:`VoiceprintLifecycle.create_voiceprint` - internal Voiceprint-creation proof.
* :meth:`VoiceprintLifecycle.apply_retention` - retention apply and YES->NO reconciliation.
* :meth:`VoiceprintLifecycle.delete_enrollment` - Contract D foundation.
* :meth:`VoiceprintLifecycle.migrate` - encoder-migration rebuild/remove, only under an
  HTBW-issued household ``migration_authorization`` for the active compatibility_id;
  without it, mismatched Voiceprints are only marked incompatible.

The Voiceprint artifact is the set of per-recording embeddings; no aggregation policy is
applied. Embeddings never leave the App.
"""

from __future__ import annotations

import logging
import threading
from collections.abc import Callable, Sequence
from dataclasses import dataclass

import numpy as np

from .const import ENROLLMENT_RECORDING_COUNT
from .encoder import Encoder, EncoderError, EncoderInputError, validate_embedding
from .features import AudioContractError, pcm_s16le_to_array
from .logs import get_logger, log_event
from .storage import (
    EvidenceStore,
    StorageError,
    VoiceprintAlreadyExistsError,
    VoiceprintRecord,
    VoiceprintState,
    utc_now,
    validate_person_id,
)

_LOGGER = get_logger("lifecycle")

__all__ = [
    "EncoderUnavailableError",
    "EnrollmentCardinalityError",
    "InvalidRecordingError",
    "MigrationOutcome",
    "RetentionResult",
    "VoiceprintAlreadyExistsError",
    "VoiceprintLifecycle",
]


MIGRATION_NOT_AUTHORIZED = "migration_not_authorized"


class EnrollmentCardinalityError(ValueError):
    """Enrollment did not supply exactly the governed number of recordings."""

    reason_code = "invalid_recording_count"


class InvalidRecordingError(ValueError):
    """A recording does not satisfy the audio contract."""

    reason_code = "unsupported_audio"


class EncoderUnavailableError(RuntimeError):
    """No validated encoder is active."""

    reason_code = "app_unavailable"


class MigrationError(Exception):
    """A replacement Voiceprint could not be built or validated."""

    def __init__(self, reason_code: str) -> None:
        super().__init__(reason_code)
        self.reason_code = reason_code


@dataclass(frozen=True)
class RetentionResult:
    applied_retain_enrollment_recordings: bool
    removed_recording_sets: int


@dataclass(frozen=True)
class MigrationOutcome:
    person_id: str
    outcome: str  # "regenerated" | "removed" | "failed" | "deferred"
    reason_code: str | None = None


EncoderProvider = Callable[[], Encoder | None]


class VoiceprintLifecycle:
    def __init__(self, store: EvidenceStore, encoder_provider: EncoderProvider) -> None:
        self._store = store
        self._encoder_provider = encoder_provider
        self._lock = threading.RLock()
        applied = store.read_app_state().get("applied_retain_enrollment_recordings")
        self._retain: bool | None = applied if isinstance(applied, bool) else None

    @property
    def applied_retention(self) -> bool | None:
        return self._retain

    # Internal helpers ---------------------------------------------------------------
    def _require_encoder(self) -> Encoder:
        encoder = self._encoder_provider()
        if encoder is None:
            raise EncoderUnavailableError("no validated encoder is active")
        return encoder

    @staticmethod
    def _validate_recordings(recordings: Sequence[bytes]) -> list[bytes]:
        if isinstance(recordings, (bytes, bytearray, str)) or not isinstance(recordings, Sequence):
            raise EnrollmentCardinalityError("recordings must be a sequence")
        if len(recordings) != ENROLLMENT_RECORDING_COUNT:
            raise EnrollmentCardinalityError(
                f"exactly {ENROLLMENT_RECORDING_COUNT} recordings are required"
            )
        validated: list[bytes] = []
        for pcm in recordings:
            if not isinstance(pcm, (bytes, bytearray, memoryview)) or len(pcm) == 0:
                raise InvalidRecordingError("recording must be non-empty PCM bytes")
            try:
                pcm_s16le_to_array(bytes(pcm))
            except AudioContractError as err:
                raise InvalidRecordingError(str(err)) from err
            validated.append(bytes(pcm))
        return validated

    @staticmethod
    def _embed_all(encoder: Encoder, recordings: Sequence[bytes]) -> np.ndarray:
        vectors = []
        for pcm in recordings:
            try:
                vectors.append(validate_embedding(encoder.embed(pcm)))
            except (AudioContractError, EncoderInputError) as err:
                raise InvalidRecordingError(str(err)) from err
        if len({vec.shape[0] for vec in vectors}) != 1:
            raise EncoderError("inconsistent embedding dimensions")
        return np.stack(vectors).astype(np.float32)

    @staticmethod
    def _new_record(person_id: str, encoder: Encoder, matrix: np.ndarray) -> VoiceprintRecord:
        identity = encoder.identity
        return VoiceprintRecord(
            person_id=person_id,
            compatibility_id=identity.compatibility_id,
            encoder_family=identity.encoder_family,
            encoder_version=identity.encoder_version,
            audio_contract_version=identity.audio_contract_version,
            created_at=utc_now(),
            state=VoiceprintState.CURRENT,
            artifact_file="",
            artifact_sha256="",
            embedding_count=int(matrix.shape[0]),
            embedding_dim=int(matrix.shape[1]),
        )

    # Creation (internal proof) ------------------------------------------------------
    def create_voiceprint(self, person_id: str, recordings: Sequence[bytes]) -> VoiceprintRecord:
        """Create the single Voiceprint for ``person_id`` from exactly ten recordings."""
        validate_person_id(person_id)
        validated = self._validate_recordings(recordings)
        encoder = self._require_encoder()
        with self._lock:
            if self._store.get_voiceprint(person_id) is not None:
                raise VoiceprintAlreadyExistsError("a Voiceprint already exists for this person")
            staged = self._store.stage_recordings(person_id, validated)
            try:
                matrix = self._embed_all(encoder, validated)
                record = self._store.write_voiceprint(
                    self._new_record(person_id, encoder, matrix),
                    matrix,
                    replace_existing=False,
                )
            except BaseException:
                self._store.discard_staged(staged)
                raise
            if self._retain is True:
                try:
                    self._store.retain_staged(staged, encoder.identity.audio_contract_version)
                except (OSError, StorageError, ValueError):
                    self._store.discard_staged(staged)
                    log_event(_LOGGER, logging.WARNING, "recording_retention_failed")
            else:
                self._store.discard_staged(staged)
            log_event(
                _LOGGER,
                logging.INFO,
                "voiceprint_created",
                retained_recordings=self._retain is True,
            )
            return record

    # Retention ----------------------------------------------------------------------
    def apply_retention(self, retain: bool) -> RetentionResult:
        """Apply the HTBW-managed retention setting; NO deletes recordings, never Voiceprints."""
        if not isinstance(retain, bool):
            raise TypeError("retain must be a bool")
        with self._lock:
            previous = self._retain
            removed = 0
            if not retain:
                removed = self._store.remove_all_retained()
                self._store.remove_all_incoming()
            self._store.update_app_state(applied_retain_enrollment_recordings=retain)
            self._retain = retain
            if previous != retain or removed:
                log_event(
                    _LOGGER,
                    logging.INFO,
                    "retention_applied",
                    retain=retain,
                    removed_recording_sets=removed,
                )
            return RetentionResult(retain, removed)

    # Deletion (Contract D foundation) -----------------------------------------------
    def delete_enrollment(self, person_id: str) -> bool:
        """Remove all enrollment state for ``person_id``; idempotent."""
        validate_person_id(person_id)
        with self._lock:
            removed_recordings = self._store.remove_retained(person_id)
            removed_incoming = self._store.remove_incoming_for(person_id) > 0
            removed_voiceprint = self._store.remove_voiceprint(person_id)
            removed = removed_recordings or removed_incoming or removed_voiceprint
            log_event(_LOGGER, logging.INFO, "enrollment_deleted", removed=removed)
            return removed

    def voiceprint_exists(self, person_id: str) -> bool:
        return self._store.get_voiceprint(person_id) is not None

    # Encoder migration --------------------------------------------------------------
    def _rebuild(self, record: VoiceprintRecord, encoder: Encoder) -> VoiceprintRecord:
        if self._store.retained_audio_contract(record.person_id) != (
            encoder.identity.audio_contract_version
        ):
            raise MigrationError("retained_recordings_incompatible")
        try:
            recordings = self._store.load_retained(record.person_id)
        except (OSError, StorageError, ValueError, KeyError) as err:
            raise MigrationError("retained_recordings_unreadable") from err
        if len(recordings) != ENROLLMENT_RECORDING_COUNT:
            raise MigrationError("retained_recordings_insufficient")
        try:
            matrix = self._embed_all(encoder, recordings)
        except (EncoderError, InvalidRecordingError) as err:
            raise MigrationError("rebuild_failed") from err
        replacement = self._new_record(record.person_id, encoder, matrix)
        try:
            return self._store.write_voiceprint(replacement, matrix, replace_existing=True)
        except (OSError, StorageError, ValueError) as err:
            raise MigrationError("validation_failed") from err

    def migrate(self, authorized_compatibility_id: str | None = None) -> list[MigrationOutcome]:
        """Bring every Voiceprint to the active compatibility identity (failure-safe).

        Rebuild/removal runs only when HTBW has issued a household-level migration
        authorization for the active ``compatibility_id``. Otherwise mismatched Voiceprints
        are only marked ``incompatible`` (``migration_not_authorized``); nothing is
        rebuilt or destroyed.
        """
        encoder = self._encoder_provider()
        if encoder is None:
            return []
        active = encoder.identity.compatibility_id
        authorized = authorized_compatibility_id is not None and (
            authorized_compatibility_id == active
        )
        outcomes: list[MigrationOutcome] = []
        with self._lock:
            for record in self._store.list_voiceprints():
                pid = record.person_id
                if record.compatibility_id == active:
                    if record.state is not VoiceprintState.CURRENT:
                        self._store.set_voiceprint_state(pid, VoiceprintState.CURRENT)
                    continue
                if not authorized:
                    if record.state_reason != MIGRATION_NOT_AUTHORIZED or (
                        record.state is not VoiceprintState.INCOMPATIBLE
                    ):
                        self._store.set_voiceprint_state(
                            pid, VoiceprintState.INCOMPATIBLE, MIGRATION_NOT_AUTHORIZED
                        )
                    outcomes.append(MigrationOutcome(pid, "deferred", MIGRATION_NOT_AUTHORIZED))
                    continue
                has_recordings = self._store.has_retained(pid)
                if has_recordings and self._retain is None:
                    self._store.set_voiceprint_state(
                        pid, VoiceprintState.INCOMPATIBLE, "retention_unknown"
                    )
                    outcomes.append(MigrationOutcome(pid, "deferred", "retention_unknown"))
                    continue
                if has_recordings and self._retain is True:
                    try:
                        self._rebuild(record, encoder)
                    except Exception as err:  # failure-safe: the old Voiceprint stays
                        reason = str(getattr(err, "reason_code", "rebuild_failed"))
                        try:
                            self._store.set_voiceprint_state(
                                pid, VoiceprintState.INCOMPATIBLE, reason
                            )
                        except (OSError, StorageError):
                            # Status still reports it incompatible via compatibility_id.
                            pass
                        outcomes.append(MigrationOutcome(pid, "failed", reason))
                        log_event(_LOGGER, logging.WARNING, "migration_failed", reason=reason)
                    else:
                        outcomes.append(MigrationOutcome(pid, "regenerated"))
                        log_event(_LOGGER, logging.INFO, "migration_regenerated")
                    continue
                self._store.remove_retained(pid)
                self._store.remove_voiceprint(pid)
                outcomes.append(MigrationOutcome(pid, "removed", "no_retained_recordings"))
                log_event(_LOGGER, logging.INFO, "migration_removed")
        return outcomes
