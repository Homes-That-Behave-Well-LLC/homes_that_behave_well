"""Structured logging with secret redaction.

Log lines are ``event=<name> key=value ...``. Callers must never pass the API secret,
audio, embeddings, or paths containing person identifiers. As defense in depth, a
filter redacts every registered secret value from formatted records.
"""

from __future__ import annotations

import logging
import threading
from typing import Any

LOGGER_NAME = "htbw_voice_evidence"
REDACTED = "[REDACTED]"


def get_logger(name: str | None = None) -> logging.Logger:
    return logging.getLogger(LOGGER_NAME if name is None else f"{LOGGER_NAME}.{name}")


def _format_value(value: Any) -> str:
    text = str(value)
    if not text or any(ch.isspace() for ch in text) or "=" in text or '"' in text:
        return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return text


def log_event(logger: logging.Logger, level: int, event: str, **fields: Any) -> None:
    parts = [f"event={event}"]
    parts.extend(f"{key}={_format_value(val)}" for key, val in sorted(fields.items()))
    logger.log(level, " ".join(parts))


class SecretRedactionFilter(logging.Filter):
    """Replace registered secret values in log records with a redaction marker."""

    def __init__(self) -> None:
        super().__init__()
        self._lock = threading.Lock()
        self._secrets: set[str] = set()

    def register(self, secret: str) -> None:
        if secret:
            with self._lock:
                self._secrets.add(secret)

    def filter(self, record: logging.LogRecord) -> bool:
        with self._lock:
            known = tuple(self._secrets)
        if not known:
            return True
        message = record.getMessage()
        redacted = message
        for secret in known:
            redacted = redacted.replace(secret, REDACTED)
        if redacted != message:
            record.msg = redacted
            record.args = None
        return True


REDACTION_FILTER = SecretRedactionFilter()


def configure_logging(level: int = logging.INFO) -> None:
    """Log to stderr (collected by the Supervisor) through the redaction filter."""
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s"))
    handler.addFilter(REDACTION_FILTER)
    root = logging.getLogger()
    root.handlers[:] = [handler]
    root.setLevel(level)
