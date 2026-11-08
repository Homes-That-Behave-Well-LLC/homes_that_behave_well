"""Pinned model artifact acquisition, verification and atomic activation."""

from __future__ import annotations

import asyncio
import contextlib
import hashlib
import os
import secrets
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import BinaryIO, Protocol

import aiohttp

from . import const
from .fsutil import ensure_private_dir, fsync_dir, remove_path
from .logs import get_logger, log_event

_LOGGER = get_logger("model")
_CHUNK = 1 << 16


class ModelState(StrEnum):
    VALID = "valid"
    MISSING = "missing"
    INVALID = "invalid"
    DOWNLOADING = "downloading"
    DOWNLOAD_FAILED = "download_failed"


MODEL_STATE_REASON: dict[ModelState, str | None] = {
    ModelState.VALID: None,
    ModelState.MISSING: const.REASON_MODEL_MISSING,
    ModelState.INVALID: const.REASON_MODEL_DIGEST_MISMATCH,
    ModelState.DOWNLOADING: const.REASON_MODEL_DOWNLOADING,
    ModelState.DOWNLOAD_FAILED: const.REASON_MODEL_DOWNLOAD_FAILED,
}


class DownloadError(Exception):
    """The artifact could not be fetched within the configured bounds."""


class ModelIntegrityError(Exception):
    """The artifact on disk does not match the pinned digest."""


@dataclass(frozen=True)
class ModelPin:
    model_id: str
    filename: str
    revision: str
    sha256: str
    size_bytes: int | None
    url: str
    max_bytes: int


GOVERNED_MODEL_PIN = ModelPin(
    model_id=const.MODEL_ID,
    filename=const.MODEL_FILENAME,
    revision=const.MODEL_REVISION,
    sha256=const.MODEL_SHA256,
    size_bytes=const.MODEL_SIZE_BYTES,
    url=const.MODEL_URL,
    max_bytes=const.MODEL_MAX_DOWNLOAD_BYTES,
)


class Downloader(Protocol):
    async def download(self, url: str, dest: BinaryIO, *, max_bytes: int) -> None: ...


class AiohttpDownloader:
    """Streams a URL to a file with a total timeout and a hard size cap."""

    def __init__(
        self,
        total_timeout_s: float = const.MODEL_DOWNLOAD_TIMEOUT_S,
        connect_timeout_s: float = const.MODEL_DOWNLOAD_CONNECT_TIMEOUT_S,
        read_timeout_s: float = const.MODEL_DOWNLOAD_READ_TIMEOUT_S,
    ) -> None:
        self._timeout = aiohttp.ClientTimeout(
            total=total_timeout_s, connect=connect_timeout_s, sock_read=read_timeout_s
        )

    async def download(self, url: str, dest: BinaryIO, *, max_bytes: int) -> None:
        received = 0
        try:
            async with (
                aiohttp.ClientSession(timeout=self._timeout) as session,
                session.get(url, allow_redirects=True, max_redirects=5) as resp,
            ):
                if resp.status != 200:
                    raise DownloadError(f"unexpected HTTP status {resp.status}")
                if resp.content_length is not None and resp.content_length > max_bytes:
                    raise DownloadError("artifact exceeds the size cap")
                async for chunk in resp.content.iter_chunked(_CHUNK):
                    received += len(chunk)
                    if received > max_bytes:
                        raise DownloadError("artifact exceeds the size cap")
                    dest.write(chunk)
        except (aiohttp.ClientError, TimeoutError) as err:
            raise DownloadError(type(err).__name__) from err


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


class ModelArtifactManager:
    """Owns the model artifact: never falls back, never auto-updates beyond the pin."""

    def __init__(self, models_dir: Path, pin: ModelPin, downloader: Downloader) -> None:
        self._dir = models_dir
        self._pin = pin
        self._downloader = downloader
        self._state = ModelState.MISSING
        self._lock = asyncio.Lock()

    @property
    def pin(self) -> ModelPin:
        return self._pin

    @property
    def state(self) -> ModelState:
        return self._state

    @property
    def reason_code(self) -> str | None:
        return MODEL_STATE_REASON[self._state]

    @property
    def active_path(self) -> Path:
        return self._dir / self._pin.sha256 / self._pin.filename

    @property
    def staging_dir(self) -> Path:
        return self._dir / ".staging"

    def _active_is_valid(self) -> bool:
        path = self.active_path
        if not path.is_file():
            return False
        return sha256_file(path) == self._pin.sha256

    def _state_from_disk(self) -> ModelState:
        if not self.active_path.exists():
            return ModelState.MISSING
        return ModelState.VALID if self._active_is_valid() else ModelState.INVALID

    async def refresh_state(self) -> ModelState:
        self._state = await asyncio.to_thread(self._state_from_disk)
        return self._state

    async def ensure(self, allow_download: bool = True) -> ModelState:
        """Make the pinned artifact available; download only if no valid one exists."""
        async with self._lock:
            ensure_private_dir(self._dir)
            await asyncio.to_thread(remove_path, self.staging_dir)
            state = await asyncio.to_thread(self._state_from_disk)
            self._state = state
            if state is ModelState.VALID:
                log_event(_LOGGER, 20, "model_artifact_valid", sha256=self._pin.sha256)
                return state
            if state is ModelState.INVALID:
                log_event(_LOGGER, 30, "model_artifact_digest_mismatch")
            if not allow_download:
                return state
            return await self._download_and_promote()

    async def redownload(self) -> ModelState:
        """Fetch and validate a replacement; the current artifact stays until it validates."""
        async with self._lock:
            ensure_private_dir(self._dir)
            return await self._download_and_promote()

    async def _download_and_promote(self) -> ModelState:
        ensure_private_dir(self.staging_dir)
        staging = self.staging_dir / f"{self._pin.filename}.{secrets.token_hex(6)}.part"
        previous = self._state
        self._state = ModelState.DOWNLOADING
        log_event(_LOGGER, 20, "model_download_started", revision=self._pin.revision)
        outcome: ModelState
        try:
            fd = os.open(staging, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            with os.fdopen(fd, "wb") as handle:
                await self._downloader.download(
                    self._pin.url, handle, max_bytes=self._pin.max_bytes
                )
                handle.flush()
                os.fsync(handle.fileno())
            size = staging.stat().st_size
            digest = await asyncio.to_thread(sha256_file, staging)
            if digest != self._pin.sha256 or (
                self._pin.size_bytes is not None and size != self._pin.size_bytes
            ):
                log_event(_LOGGER, 40, "model_download_digest_mismatch", size=size)
                outcome = ModelState.INVALID
            else:
                ensure_private_dir(self.active_path.parent)
                os.replace(staging, self.active_path)
                fsync_dir(self.active_path.parent)
                log_event(_LOGGER, 20, "model_artifact_promoted", sha256=digest)
                outcome = ModelState.VALID
        except (DownloadError, OSError) as err:
            log_event(_LOGGER, 40, "model_download_failed", error=type(err).__name__)
            outcome = ModelState.DOWNLOAD_FAILED
        except asyncio.CancelledError:
            self._state = previous
            raise
        finally:
            with contextlib.suppress(OSError):
                staging.unlink(missing_ok=True)
        if outcome is not ModelState.VALID:
            # A previously validated artifact remains authoritative.
            on_disk = await asyncio.to_thread(self._state_from_disk)
            if on_disk is ModelState.VALID:
                outcome = ModelState.VALID
        self._state = outcome
        return outcome

    def read_verified(self) -> bytes:
        """Read the active artifact and verify its digest (every load)."""
        try:
            data = self.active_path.read_bytes()
        except FileNotFoundError as err:
            self._state = ModelState.MISSING
            raise ModelIntegrityError("model artifact missing") from err
        if hashlib.sha256(data).hexdigest() != self._pin.sha256:
            self._state = ModelState.INVALID
            raise ModelIntegrityError("model artifact digest mismatch")
        self._state = ModelState.VALID
        return data
