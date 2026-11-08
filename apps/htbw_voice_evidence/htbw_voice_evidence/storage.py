"""App-owned private storage for Voice Evidence artifacts.

Layout below the storage root (the App's private ``/data`` in production):

* ``voiceprints/<person-key>/`` - (A) Voiceprint artifacts: ``record.json`` (metadata and
  commit point) and the per-recording embedding matrix it references.
* ``recordings/incoming/`` - (B) handed-off enrollment recordings awaiting processing.
* ``recordings/retained/<person-key>/`` - (B) retained enrollment recordings.
* ``models/`` - (C) model artifacts (managed by :mod:`model_artifact`).
* ``state/app_state.json`` - (D) minimal App lifecycle metadata.
* ``auth/`` - the API secret (managed by :mod:`secret_store`).

Person identifiers are never used as path components; they are hashed.
"""

from __future__ import annotations

import hashlib
import io
import os
import secrets
from collections.abc import Sequence
from dataclasses import asdict, dataclass, replace
from datetime import UTC, datetime
from enum import StrEnum
from pathlib import Path
from typing import Any

import numpy as np

from .fsutil import (
    atomic_write_bytes,
    atomic_write_json,
    ensure_private_dir,
    fsync_dir,
    read_json,
    remove_path,
)

_PERSON_KEY_DOMAIN = b"htbw-voice-evidence/person-id/v1\x00"
RECORD_FILE = "record.json"
MANIFEST_FILE = "manifest.json"
MAX_PERSON_ID_LENGTH = 256


class StorageError(Exception):
    """Base class for storage failures."""


class StorageUnavailableError(StorageError):
    """The storage root cannot be used."""


class VoiceprintAlreadyExistsError(StorageError):
    """A Voiceprint already exists for this person_id (re-enrollment requires delete)."""


class VoiceprintNotFoundError(StorageError):
    """No Voiceprint exists for this person_id."""


class ArtifactIntegrityError(StorageError):
    """A stored artifact does not match its recorded digest."""


class InvalidPersonIdError(ValueError):
    """The person_id is not an acceptable identifier."""


class VoiceprintState(StrEnum):
    CURRENT = "current"
    INCOMPATIBLE = "incompatible"


def utc_now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


def validate_person_id(person_id: Any) -> str:
    if not isinstance(person_id, str) or not person_id.strip():
        raise InvalidPersonIdError("person_id must be a non-empty string")
    if len(person_id) > MAX_PERSON_ID_LENGTH or not person_id.isprintable():
        raise InvalidPersonIdError("person_id is not an acceptable identifier")
    return person_id


def person_key(person_id: str) -> str:
    validate_person_id(person_id)
    return hashlib.sha256(_PERSON_KEY_DOMAIN + person_id.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class VoiceprintRecord:
    person_id: str
    compatibility_id: str
    encoder_family: str
    encoder_version: str
    audio_contract_version: str
    created_at: str
    state: VoiceprintState
    artifact_file: str
    artifact_sha256: str
    embedding_count: int
    embedding_dim: int
    state_reason: str | None = None

    def to_json(self) -> dict[str, Any]:
        data = asdict(self)
        data["state"] = self.state.value
        return data

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> VoiceprintRecord:
        return cls(
            person_id=str(data["person_id"]),
            compatibility_id=str(data["compatibility_id"]),
            encoder_family=str(data["encoder_family"]),
            encoder_version=str(data["encoder_version"]),
            audio_contract_version=str(data["audio_contract_version"]),
            created_at=str(data["created_at"]),
            state=VoiceprintState(data["state"]),
            artifact_file=str(data["artifact_file"]),
            artifact_sha256=str(data["artifact_sha256"]),
            embedding_count=int(data["embedding_count"]),
            embedding_dim=int(data["embedding_dim"]),
            state_reason=data.get("state_reason"),
        )


@dataclass(frozen=True)
class StagedRecordings:
    person_id: str
    path: Path


def _encode_matrix(matrix: np.ndarray) -> bytes:
    buffer = io.BytesIO()
    np.save(buffer, np.ascontiguousarray(matrix, dtype=np.float32), allow_pickle=False)
    return buffer.getvalue()


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class EvidenceStore:
    """Private, atomic storage for Voiceprints, recordings and App metadata."""

    def __init__(self, root: Path) -> None:
        self._root = root

    # Layout -------------------------------------------------------------------------
    @property
    def root(self) -> Path:
        return self._root

    @property
    def voiceprints_dir(self) -> Path:
        return self._root / "voiceprints"

    @property
    def incoming_dir(self) -> Path:
        return self._root / "recordings" / "incoming"

    @property
    def retained_dir(self) -> Path:
        return self._root / "recordings" / "retained"

    @property
    def models_dir(self) -> Path:
        return self._root / "models"

    @property
    def state_file(self) -> Path:
        return self._root / "state" / "app_state.json"

    @property
    def secret_file(self) -> Path:
        return self._root / "auth" / "api_secret"

    def _voiceprint_dir(self, person_id: str) -> Path:
        return self.voiceprints_dir / person_key(person_id)

    def _retained_path(self, person_id: str) -> Path:
        return self.retained_dir / person_key(person_id)

    # Lifecycle ----------------------------------------------------------------------
    def initialize(self) -> None:
        """Create the layout and prove the root is writable."""
        try:
            for directory in (
                self._root,
                self.voiceprints_dir,
                self.incoming_dir,
                self.retained_dir,
                self.models_dir,
                self.state_file.parent,
                self.secret_file.parent,
            ):
                ensure_private_dir(directory)
            probe = self.state_file.parent / f".probe-{secrets.token_hex(4)}"
            atomic_write_bytes(probe, b"ok")
            probe.unlink()
        except OSError as err:
            raise StorageUnavailableError("storage root is not usable") from err

    def is_available(self) -> bool:
        try:
            return self._root.is_dir() and os.access(self._root, os.W_OK)
        except OSError:
            return False

    def sweep(self) -> dict[str, int]:
        """Remove crash leftovers: handed-off recordings, orphans and temp files."""
        removed = {"incoming": 0, "orphan_artifacts": 0, "orphan_recordings": 0}
        for entry in list(self.incoming_dir.iterdir()):
            remove_path(entry)
            removed["incoming"] += 1
        live_keys: set[str] = set()
        for vp_dir in list(self.voiceprints_dir.iterdir()):
            record = self._read_record_file(vp_dir / RECORD_FILE)
            if record is None:
                remove_path(vp_dir)
                removed["orphan_artifacts"] += 1
                continue
            live_keys.add(vp_dir.name)
            for child in list(vp_dir.iterdir()):
                if child.name not in (RECORD_FILE, record.artifact_file):
                    remove_path(child)
                    removed["orphan_artifacts"] += 1
        for retained in list(self.retained_dir.iterdir()):
            if retained.name not in live_keys:
                remove_path(retained)
                removed["orphan_recordings"] += 1
        return removed

    # Voiceprints --------------------------------------------------------------------
    @staticmethod
    def _read_record_file(path: Path) -> VoiceprintRecord | None:
        try:
            return VoiceprintRecord.from_json(read_json(path))
        except (OSError, ValueError, KeyError, TypeError):
            return None

    def get_voiceprint(self, person_id: str) -> VoiceprintRecord | None:
        return self._read_record_file(self._voiceprint_dir(person_id) / RECORD_FILE)

    def list_voiceprints(self) -> list[VoiceprintRecord]:
        records: list[VoiceprintRecord] = []
        if not self.voiceprints_dir.is_dir():
            return records
        for vp_dir in sorted(self.voiceprints_dir.iterdir()):
            record = self._read_record_file(vp_dir / RECORD_FILE)
            if record is not None:
                records.append(record)
        return sorted(records, key=lambda rec: rec.person_id)

    def write_voiceprint(
        self,
        record: VoiceprintRecord,
        embeddings: np.ndarray,
        *,
        replace_existing: bool,
    ) -> VoiceprintRecord:
        """Persist and validate a Voiceprint, then commit it via its record file.

        With ``replace_existing`` the previous artifact is removed only after the new
        record has been committed.
        """
        vp_dir = self._voiceprint_dir(record.person_id)
        previous = self.get_voiceprint(record.person_id)
        if previous is not None and not replace_existing:
            raise VoiceprintAlreadyExistsError("a Voiceprint already exists for this person")
        if previous is None and replace_existing:
            raise VoiceprintNotFoundError("no Voiceprint to replace")
        matrix = np.asarray(embeddings, dtype=np.float32)
        if matrix.ndim != 2 or matrix.shape[0] == 0 or not np.all(np.isfinite(matrix)):
            raise StorageError("embedding matrix is not valid")
        payload = _encode_matrix(matrix)
        artifact_file = f"embeddings-{secrets.token_hex(8)}.npy"
        committed = replace(
            record,
            artifact_file=artifact_file,
            artifact_sha256=_sha256(payload),
            embedding_count=int(matrix.shape[0]),
            embedding_dim=int(matrix.shape[1]),
        )
        artifact_path = vp_dir / artifact_file
        try:
            atomic_write_bytes(artifact_path, payload)
            # Validate what is on disk before it can become authoritative.
            self._load_matrix(artifact_path, committed.artifact_sha256)
            atomic_write_json(vp_dir / RECORD_FILE, committed.to_json())
        except BaseException:
            remove_path(artifact_path)
            if previous is None and not any(vp_dir.glob(RECORD_FILE)):
                remove_path(vp_dir)
            raise
        if previous is not None and previous.artifact_file != artifact_file:
            remove_path(vp_dir / previous.artifact_file)
        return committed

    @staticmethod
    def _load_matrix(path: Path, expected_sha256: str) -> np.ndarray:
        data = path.read_bytes()
        if _sha256(data) != expected_sha256:
            raise ArtifactIntegrityError("Voiceprint artifact digest mismatch")
        return np.load(io.BytesIO(data), allow_pickle=False)

    def load_embeddings(self, record: VoiceprintRecord) -> np.ndarray:
        path = self._voiceprint_dir(record.person_id) / record.artifact_file
        return self._load_matrix(path, record.artifact_sha256)

    def set_voiceprint_state(
        self, person_id: str, state: VoiceprintState, reason: str | None = None
    ) -> VoiceprintRecord:
        record = self.get_voiceprint(person_id)
        if record is None:
            raise VoiceprintNotFoundError("no Voiceprint for this person")
        updated = replace(record, state=state, state_reason=reason)
        atomic_write_json(self._voiceprint_dir(person_id) / RECORD_FILE, updated.to_json())
        return updated

    def remove_voiceprint(self, person_id: str) -> bool:
        """Remove the record (commit point) first, then the artifacts and directory."""
        vp_dir = self._voiceprint_dir(person_id)
        existed = (vp_dir / RECORD_FILE).exists()
        record_path = vp_dir / RECORD_FILE
        if record_path.exists():
            record_path.unlink()
            fsync_dir(vp_dir)
        remove_path(vp_dir)
        return existed

    # Enrollment recordings ----------------------------------------------------------
    def stage_recordings(self, person_id: str, recordings: Sequence[bytes]) -> StagedRecordings:
        """Persist handed-off recordings for processing (swept at startup if abandoned)."""
        staged = self.incoming_dir / f"{person_key(person_id)}.{secrets.token_hex(6)}"
        ensure_private_dir(staged)
        files = []
        try:
            for index, pcm in enumerate(recordings):
                name = f"rec-{index:02d}.pcm"
                atomic_write_bytes(staged / name, bytes(pcm))
                files.append({"name": name, "sha256": _sha256(bytes(pcm)), "bytes": len(pcm)})
            atomic_write_json(
                staged / MANIFEST_FILE,
                {"person_id": person_id, "created_at": utc_now(), "files": files},
            )
        except BaseException:
            remove_path(staged)
            raise
        return StagedRecordings(person_id=person_id, path=staged)

    def discard_staged(self, staged: StagedRecordings) -> None:
        remove_path(staged.path)

    def retain_staged(self, staged: StagedRecordings, audio_contract_version: str) -> None:
        target = self._retained_path(staged.person_id)
        manifest = read_json(staged.path / MANIFEST_FILE)
        manifest["audio_contract_version"] = audio_contract_version
        atomic_write_json(staged.path / MANIFEST_FILE, manifest)
        if target.exists():
            remove_path(target)
        ensure_private_dir(target.parent)
        os.replace(staged.path, target)
        fsync_dir(target.parent)

    def has_retained(self, person_id: str) -> bool:
        return (self._retained_path(person_id) / MANIFEST_FILE).is_file()

    def retained_audio_contract(self, person_id: str) -> str | None:
        try:
            manifest = read_json(self._retained_path(person_id) / MANIFEST_FILE)
        except (OSError, ValueError):
            return None
        value = manifest.get("audio_contract_version")
        return str(value) if value is not None else None

    def load_retained(self, person_id: str) -> list[bytes]:
        path = self._retained_path(person_id)
        manifest = read_json(path / MANIFEST_FILE)
        recordings: list[bytes] = []
        for entry in manifest["files"]:
            data = (path / entry["name"]).read_bytes()
            if _sha256(data) != entry["sha256"]:
                raise ArtifactIntegrityError("retained recording digest mismatch")
            recordings.append(data)
        return recordings

    def remove_retained(self, person_id: str) -> bool:
        return remove_path(self._retained_path(person_id))

    def remove_all_retained(self) -> int:
        count = 0
        if not self.retained_dir.is_dir():
            return count
        for entry in list(self.retained_dir.iterdir()):
            if remove_path(entry):
                count += 1
        return count

    def remove_incoming_for(self, person_id: str) -> int:
        prefix = person_key(person_id) + "."
        count = 0
        if not self.incoming_dir.is_dir():
            return count
        for entry in list(self.incoming_dir.iterdir()):
            if entry.name.startswith(prefix) and remove_path(entry):
                count += 1
        return count

    def remove_all_incoming(self) -> int:
        count = 0
        if not self.incoming_dir.is_dir():
            return count
        for entry in list(self.incoming_dir.iterdir()):
            if remove_path(entry):
                count += 1
        return count

    # App lifecycle metadata ---------------------------------------------------------
    def read_app_state(self) -> dict[str, Any]:
        try:
            data = read_json(self.state_file)
        except (OSError, ValueError):
            return {}
        return data if isinstance(data, dict) else {}

    def update_app_state(self, **changes: Any) -> dict[str, Any]:
        state = self.read_app_state()
        state.update(changes)
        atomic_write_json(self.state_file, state)
        return state
