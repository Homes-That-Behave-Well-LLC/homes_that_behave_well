"""Runtime settings, from the container environment."""

from __future__ import annotations

import os
import socket
from dataclasses import dataclass
from pathlib import Path

from . import const


def _env_float(name: str, default: float | None) -> float | None:
    raw = os.environ.get(name)
    if raw is None or raw == "":
        return default
    value = float(raw)
    return value if value > 0 else None


@dataclass(frozen=True)
class Settings:
    data_dir: Path
    listen_host: str = "0.0.0.0"
    port: int = const.DEFAULT_PORT
    advertised_host: str = "localhost"
    supervisor_url: str = const.SUPERVISOR_URL
    supervisor_token: str | None = None
    supervisor_timeout_s: float = const.SUPERVISOR_TIMEOUT_S
    options_poll_interval_s: float | None = const.OPTIONS_POLL_INTERVAL_S
    model_auto_download: bool = True
    model_retry_interval_s: float | None = 600.0
    discovery_attempts: int = 5
    discovery_retry_delay_s: float = 5.0
    read_stdin: bool = False

    @property
    def options_file(self) -> Path:
        return self.data_dir / "options.json"

    @classmethod
    def from_env(cls) -> Settings:
        token = os.environ.get("SUPERVISOR_TOKEN") or None
        return cls(
            data_dir=Path(os.environ.get("HTBW_VE_DATA_DIR", const.DEFAULT_DATA_DIR)),
            port=int(os.environ.get("HTBW_VE_PORT", const.DEFAULT_PORT)),
            advertised_host=os.environ.get("HTBW_VE_ADVERTISED_HOST") or socket.gethostname(),
            supervisor_url=os.environ.get("HTBW_VE_SUPERVISOR_URL", const.SUPERVISOR_URL),
            supervisor_token=token,
            options_poll_interval_s=_env_float(
                "HTBW_VE_OPTIONS_POLL_INTERVAL_S", const.OPTIONS_POLL_INTERVAL_S
            ),
            model_retry_interval_s=_env_float("HTBW_VE_MODEL_RETRY_INTERVAL_S", 600.0),
            read_stdin=True,
        )
