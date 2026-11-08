"""Filesystem helpers: atomic writes and safe removal."""

from __future__ import annotations

import contextlib
import json
import os
import secrets
import shutil
from pathlib import Path
from typing import Any

PRIVATE_FILE_MODE = 0o600
PRIVATE_DIR_MODE = 0o700


def ensure_private_dir(path: Path) -> None:
    """Create a directory (and parents) readable only by the App user."""
    path.mkdir(parents=True, exist_ok=True, mode=PRIVATE_DIR_MODE)
    with contextlib.suppress(OSError):
        os.chmod(path, PRIVATE_DIR_MODE)


def fsync_dir(path: Path) -> None:
    """Flush directory metadata so a rename is durable (best effort on non-POSIX)."""
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


def temp_sibling(path: Path, suffix: str = ".tmp") -> Path:
    return path.with_name(f".{path.name}.{secrets.token_hex(6)}{suffix}")


def atomic_write_bytes(path: Path, data: bytes, mode: int = PRIVATE_FILE_MODE) -> None:
    """Write ``data`` to ``path`` atomically: temp file + fsync + os.replace."""
    ensure_private_dir(path.parent)
    tmp = temp_sibling(path)
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_EXCL, mode)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        with contextlib.suppress(OSError):
            os.chmod(tmp, mode)
        os.replace(tmp, path)
    except BaseException:
        with contextlib.suppress(OSError):
            os.unlink(tmp)
        raise
    fsync_dir(path.parent)


def atomic_write_json(path: Path, payload: Any) -> None:
    data = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    atomic_write_bytes(path, data)


def read_json(path: Path) -> Any:
    with open(path, "rb") as handle:
        return json.loads(handle.read().decode("utf-8"))


def remove_path(path: Path) -> bool:
    """Remove a file or directory tree. Returns True if something was removed."""
    if path.is_symlink() or path.is_file():
        path.unlink(missing_ok=True)
        fsync_dir(path.parent)
        return True
    if path.is_dir():
        shutil.rmtree(path)
        fsync_dir(path.parent)
        return True
    return False
