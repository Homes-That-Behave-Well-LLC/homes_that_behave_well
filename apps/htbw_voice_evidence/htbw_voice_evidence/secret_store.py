"""App API secret: generation, private storage, verification and rotation."""

from __future__ import annotations

import contextlib
import hmac
import os
import secrets
import threading
from pathlib import Path

from .fsutil import PRIVATE_FILE_MODE, atomic_write_bytes, ensure_private_dir
from .logs import REDACTION_FILTER

SECRET_NBYTES = 32
_MIN_SECRET_LEN = 32


def generate_secret() -> str:
    return secrets.token_urlsafe(SECRET_NBYTES)


class SecretStore:
    """Holds the single valid API secret; persisted only in a 0600 file."""

    def __init__(self, path: Path) -> None:
        self._path = path
        self._lock = threading.Lock()
        self._secret: str | None = None

    @property
    def path(self) -> Path:
        return self._path

    def load_or_create(self) -> str:
        with self._lock:
            ensure_private_dir(self._path.parent)
            secret = self._read()
            if secret is None:
                secret = generate_secret()
                self._write(secret)
            else:
                with contextlib.suppress(OSError):
                    os.chmod(self._path, PRIVATE_FILE_MODE)
            self._activate(secret)
            return secret

    def use_ephemeral(self) -> str:
        """Fallback when private storage is unusable: an in-memory secret only."""
        with self._lock:
            secret = generate_secret()
            self._activate(secret)
            return secret

    def rotate(self) -> str:
        """Atomically replace the secret; the previous value is rejected immediately."""
        with self._lock:
            secret = generate_secret()
            self._write(secret)
            self._activate(secret)
            return secret

    def current(self) -> str:
        with self._lock:
            if self._secret is None:
                raise RuntimeError("secret not loaded")
            return self._secret

    def verify(self, presented: str | None) -> bool:
        with self._lock:
            expected = self._secret
        if expected is None or not presented:
            return False
        return hmac.compare_digest(presented.encode("utf-8"), expected.encode("utf-8"))

    def _activate(self, secret: str) -> None:
        REDACTION_FILTER.register(secret)
        self._secret = secret

    def _read(self) -> str | None:
        try:
            raw = self._path.read_bytes()
        except FileNotFoundError:
            return None
        try:
            value = raw.decode("utf-8").strip()
        except UnicodeDecodeError:
            return None
        if len(value) < _MIN_SECRET_LEN:
            return None
        return value

    def _write(self, secret: str) -> None:
        atomic_write_bytes(self._path, secret.encode("utf-8"), mode=PRIVATE_FILE_MODE)
