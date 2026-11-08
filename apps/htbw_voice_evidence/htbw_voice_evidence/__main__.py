"""Entry point: ``python -m htbw_voice_evidence``."""

from __future__ import annotations

import asyncio
import contextlib
import logging
import signal

from .logs import configure_logging, get_logger, log_event
from .runtime import EvidenceRuntime
from .settings import Settings


async def _run() -> None:
    runtime = EvidenceRuntime(Settings.from_env())
    stop = asyncio.Event()
    loop = asyncio.get_running_loop()
    for sig in (signal.SIGTERM, signal.SIGINT):
        with contextlib.suppress(NotImplementedError):
            loop.add_signal_handler(sig, stop.set)
    await runtime.start()
    try:
        await stop.wait()
    finally:
        await runtime.stop()


def main() -> None:
    configure_logging()
    log_event(get_logger(), logging.INFO, "app_starting")
    asyncio.run(_run())


if __name__ == "__main__":
    main()
