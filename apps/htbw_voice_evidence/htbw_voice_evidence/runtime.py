"""App runtime orchestration: storage, auth, discovery, model, encoder, retention."""

from __future__ import annotations

import asyncio
import contextlib
import json
import logging
import sys
import threading
from collections.abc import Callable, Coroutine
from typing import Any

from aiohttp import web

from . import const
from .api import create_app
from .encoder import (
    Encoder,
    EncoderContractMismatchError,
    EncoderIdentity,
    OnnxSpeakerEncoder,
    governed_identity,
)
from .fsutil import read_json
from .lifecycle import VoiceprintLifecycle
from .logs import get_logger, log_event
from .model_artifact import (
    GOVERNED_MODEL_PIN,
    AiohttpDownloader,
    Downloader,
    ModelArtifactManager,
    ModelIntegrityError,
    ModelPin,
    ModelState,
)
from .secret_store import SecretStore
from .settings import Settings
from .storage import EvidenceStore, StorageUnavailableError, VoiceprintState
from .supervisor import SupervisorClient, SupervisorError

_LOGGER = get_logger("runtime")

RETENTION_OPTION = "retain_enrollment_recordings"
ROTATE_SECRET_COMMAND = "rotate-secret"

EncoderFactory = Callable[[bytes, EncoderIdentity], Encoder]


def default_encoder_factory(model_bytes: bytes, identity: EncoderIdentity) -> Encoder:
    return OnnxSpeakerEncoder(model_bytes, identity)


def parse_stdin_command(line: str) -> str | None:
    """Home Assistant JSON-encodes ``hassio.app_stdin`` input; accept string or object."""
    text = line.strip()
    if not text:
        return None
    try:
        value: Any = json.loads(text)
    except ValueError:
        value = text
    if isinstance(value, dict):
        value = value.get("command")
    return value.strip() if isinstance(value, str) else None


class EvidenceRuntime:
    def __init__(
        self,
        settings: Settings,
        *,
        encoder_factory: EncoderFactory = default_encoder_factory,
        downloader: Downloader | None = None,
        supervisor: SupervisorClient | None = None,
        model_pin: ModelPin = GOVERNED_MODEL_PIN,
    ) -> None:
        self.settings = settings
        self.store = EvidenceStore(settings.data_dir)
        self.secrets = SecretStore(self.store.secret_file)
        self.model = ModelArtifactManager(
            self.store.models_dir, model_pin, downloader or AiohttpDownloader()
        )
        self._encoder_factory = encoder_factory
        self._encoder: Encoder | None = None
        self._encoder_reason: str | None = None
        self.lifecycle: VoiceprintLifecycle | None = None
        if supervisor is None and settings.supervisor_token:
            supervisor = SupervisorClient(
                settings.supervisor_url,
                settings.supervisor_token,
                timeout_s=settings.supervisor_timeout_s,
            )
        self.supervisor = supervisor
        self.storage_ok = False
        self.discovery_uuid: str | None = None
        self.bound_port: int | None = None
        self._runner: web.AppRunner | None = None
        self._tasks: set[asyncio.Task[Any]] = set()
        self._rotation_lock = asyncio.Lock()
        self._loop: asyncio.AbstractEventLoop | None = None
        self.model_ready = asyncio.Event()
        self.last_migration: list[Any] = []

    # Encoder access -----------------------------------------------------------------
    @property
    def encoder(self) -> Encoder | None:
        return self._encoder

    # Startup / shutdown -------------------------------------------------------------
    async def start(self) -> None:
        self._loop = asyncio.get_running_loop()
        await self._init_storage()
        await self._start_http()
        await self._reconcile_from_options_file()
        self._spawn(self._provision_discovery())
        self._spawn(self.bring_up_model())
        if self.supervisor is not None and self.settings.options_poll_interval_s:
            self._spawn(self._poll_options_loop(self.settings.options_poll_interval_s))
        if self.settings.read_stdin:
            self._start_stdin_reader()
        log_event(_LOGGER, logging.INFO, "app_started", version=const.APP_VERSION)

    async def stop(self) -> None:
        for task in list(self._tasks):
            task.cancel()
        for task in list(self._tasks):
            with contextlib.suppress(asyncio.CancelledError, Exception):
                await task
        if self._runner is not None:
            await self._runner.cleanup()
            self._runner = None
        if self.supervisor is not None:
            await self.supervisor.close()
        log_event(_LOGGER, logging.INFO, "app_stopped")

    def _spawn(self, coro: Coroutine[Any, Any, Any]) -> asyncio.Task[Any]:
        task = asyncio.create_task(coro)
        self._tasks.add(task)
        task.add_done_callback(self._tasks.discard)
        return task

    async def _init_storage(self) -> None:
        try:
            await asyncio.to_thread(self.store.initialize)
            await asyncio.to_thread(self.secrets.load_or_create)
            await asyncio.to_thread(self.store.sweep)
            self.storage_ok = True
        except (StorageUnavailableError, OSError):
            self.storage_ok = False
            self.secrets.use_ephemeral()
            log_event(_LOGGER, logging.ERROR, "storage_unavailable")
            return
        self.lifecycle = VoiceprintLifecycle(self.store, lambda: self._encoder)
        state = self.store.read_app_state()
        stored_uuid = state.get("discovery_uuid")
        self.discovery_uuid = stored_uuid if isinstance(stored_uuid, str) else None

    async def _start_http(self) -> None:
        self._runner = web.AppRunner(create_app(self), access_log=None)
        await self._runner.setup()
        site = web.TCPSite(self._runner, self.settings.listen_host, self.settings.port)
        await site.start()
        server = getattr(site, "_server", None)
        sockets = getattr(server, "sockets", None) or []
        self.bound_port = sockets[0].getsockname()[1] if sockets else self.settings.port
        log_event(_LOGGER, logging.INFO, "http_listening", port=self.bound_port)

    # Model and encoder --------------------------------------------------------------
    async def bring_up_model(self) -> None:
        """Acquire/verify the pinned model, load the encoder, then reconcile Voiceprints.

        Startup never holds a migration authorization (its transport is later-phase
        scope), so mismatched Voiceprints are only marked incompatible here.
        """
        allow = self.settings.model_auto_download
        state = await self.model.ensure(allow_download=allow)
        retry = self.settings.model_retry_interval_s
        while state is not ModelState.VALID and allow and retry:
            await asyncio.sleep(retry)
            state = await self.model.ensure(allow_download=True)
        if state is ModelState.VALID:
            await asyncio.to_thread(self.load_encoder)
            if self._encoder is not None and self.lifecycle is not None:
                outcomes = await asyncio.to_thread(self.lifecycle.migrate, None)
                self.last_migration = outcomes
                if outcomes:
                    counts: dict[str, int] = {}
                    for item in outcomes:
                        counts[item.outcome] = counts.get(item.outcome, 0) + 1
                    log_event(_LOGGER, logging.INFO, "migration_completed", **counts)
        self.model_ready.set()

    def load_encoder(self) -> Encoder | None:
        """Verify the artifact digest (every load) and construct the encoder."""
        try:
            model_bytes = self.model.read_verified()
        except ModelIntegrityError:
            self._encoder = None
            self._encoder_reason = None
            log_event(_LOGGER, logging.ERROR, "model_verification_failed")
            return None
        identity = governed_identity(self.model.pin.sha256)
        try:
            encoder = self._encoder_factory(model_bytes, identity)
        except EncoderContractMismatchError:
            self._encoder = None
            self._encoder_reason = const.REASON_ENCODER_CONTRACT_MISMATCH
            log_event(_LOGGER, logging.ERROR, "encoder_contract_mismatch")
            return None
        except Exception:  # any construction failure leaves the App unavailable
            self._encoder = None
            self._encoder_reason = const.REASON_ENCODER_LOAD_FAILED
            log_event(_LOGGER, logging.ERROR, "encoder_load_failed")
            return None
        self._encoder = encoder
        self._encoder_reason = None
        log_event(
            _LOGGER,
            logging.INFO,
            "encoder_loaded",
            compatibility_id=encoder.identity.compatibility_id,
        )
        return encoder

    # Discovery and secret rotation --------------------------------------------------
    def _discovery_config(self) -> dict[str, Any]:
        return {
            "host": self.settings.advertised_host,
            "port": self.settings.port,
            "api_secret": self.secrets.current(),
        }

    def _remember_uuid(self, uuid: str | None) -> None:
        self.discovery_uuid = uuid
        if self.storage_ok:
            with contextlib.suppress(OSError):
                self.store.update_app_state(discovery_uuid=uuid)

    async def _provision_discovery(self) -> bool:
        if self.supervisor is None:
            log_event(
                _LOGGER,
                logging.WARNING,
                "discovery_skipped",
                detail="no Supervisor token; manual provisioning required",
            )
            return False
        previous = self.discovery_uuid
        attempts = max(1, self.settings.discovery_attempts)
        for attempt in range(1, attempts + 1):
            try:
                uuid = await self.supervisor.post_discovery(
                    const.DISCOVERY_SERVICE, self._discovery_config()
                )
            except SupervisorError as err:
                log_event(
                    _LOGGER, logging.WARNING, "discovery_failed", attempt=attempt, error=str(err)
                )
                if attempt < attempts:
                    await asyncio.sleep(self.settings.discovery_retry_delay_s)
                continue
            if previous and previous != uuid:
                with contextlib.suppress(SupervisorError):
                    await self.supervisor.delete_discovery(previous)
            self._remember_uuid(uuid)
            log_event(_LOGGER, logging.INFO, "discovery_sent", uuid=uuid)
            return True
        return False

    async def rotate_secret(self) -> bool:
        async with self._rotation_lock:
            try:
                await asyncio.to_thread(self.secrets.rotate)
            except OSError:
                log_event(_LOGGER, logging.ERROR, "secret_rotation_failed")
                return False
            log_event(_LOGGER, logging.INFO, "secret_rotated")
            if self.supervisor is None:
                log_event(
                    _LOGGER,
                    logging.WARNING,
                    "discovery_skipped",
                    detail="no Supervisor token; manual provisioning required",
                )
                return True
            old_uuid = self.discovery_uuid
            if old_uuid:
                try:
                    await self.supervisor.delete_discovery(old_uuid)
                except SupervisorError as err:
                    log_event(_LOGGER, logging.WARNING, "discovery_delete_failed", error=str(err))
                self._remember_uuid(None)
            return await self._provision_discovery()

    async def handle_stdin_line(self, line: str) -> None:
        command = parse_stdin_command(line)
        if command is None:
            return
        if command == ROTATE_SECRET_COMMAND:
            await self.rotate_secret()
        else:
            log_event(_LOGGER, logging.WARNING, "stdin_command_unknown")

    def _start_stdin_reader(self) -> None:
        loop = self._loop
        assert loop is not None

        def reader() -> None:
            for raw in sys.stdin:
                asyncio.run_coroutine_threadsafe(self.handle_stdin_line(raw), loop)

        threading.Thread(target=reader, name="stdin-reader", daemon=True).start()

    # Retention options --------------------------------------------------------------
    async def _reconcile_from_options_file(self) -> None:
        try:
            options = await asyncio.to_thread(read_json, self.settings.options_file)
        except (OSError, ValueError):
            log_event(_LOGGER, logging.WARNING, "options_unavailable")
            return
        if isinstance(options, dict):
            await self.reconcile_options(options, force=True)

    async def reconcile_options(self, options: dict[str, Any], *, force: bool = False) -> bool:
        value = options.get(RETENTION_OPTION)
        if not isinstance(value, bool) or self.lifecycle is None:
            return False
        if not force and value == self.lifecycle.applied_retention:
            return False
        await asyncio.to_thread(self.lifecycle.apply_retention, value)
        return True

    async def poll_options_once(self) -> bool:
        if self.supervisor is None:
            return False
        try:
            options = await self.supervisor.get_own_options()
        except SupervisorError as err:
            log_event(_LOGGER, logging.WARNING, "options_poll_failed", error=str(err))
            return False
        return await self.reconcile_options(options)

    async def _poll_options_loop(self, interval: float) -> None:
        while True:
            await asyncio.sleep(interval)
            await self.poll_options_once()

    # Contract A ---------------------------------------------------------------------
    def _storage_available(self) -> bool:
        return self.storage_ok and self.store.is_available()

    def availability(self) -> tuple[str, str | None]:
        if not self._storage_available():
            return "unavailable", const.REASON_STORAGE_UNAVAILABLE
        if self.model.state is not ModelState.VALID:
            return "unavailable", self.model.reason_code
        if self._encoder is None:
            if self._encoder_reason == const.REASON_ENCODER_CONTRACT_MISMATCH:
                return "incompatible", self._encoder_reason
            return "unavailable", self._encoder_reason or const.REASON_STARTING
        return "available", None

    def _voiceprints_payload(self) -> list[dict[str, Any]]:
        if not self._storage_available():
            return []
        active = self._encoder.identity.compatibility_id if self._encoder else None
        entries = []
        for record in self.store.list_voiceprints():
            current = record.state is VoiceprintState.CURRENT and (
                active is None or record.compatibility_id == active
            )
            entries.append(
                {
                    "person_id": record.person_id,
                    "voiceprint_exists": True,
                    "voiceprint_state": "current" if current else "incompatible",
                    "retained_recordings": self.store.has_retained(record.person_id),
                }
            )
        return entries

    def status_payload(self) -> dict[str, Any]:
        status, reason = self.availability()
        identity = self._encoder.identity if self._encoder is not None else None
        pin = self.model.pin
        return {
            "contract_version": const.CONTRACT_VERSION,
            "app_version": const.APP_VERSION,
            "status": status,
            "reason_code": reason,
            "compatibility_id": identity.compatibility_id if identity else None,
            "encoder_family": identity.encoder_family if identity else None,
            "encoder_version": identity.encoder_version if identity else None,
            "audio_contract_version": identity.audio_contract_version if identity else None,
            "model_artifact": {
                "state": self.model.state.value,
                "model_id": pin.model_id,
                "revision": pin.revision,
                "sha256": pin.sha256,
            },
            "storage": {"state": "available" if self._storage_available() else "unavailable"},
            "optional_capabilities": [],
            "retention": {
                "applied_retain_enrollment_recordings": (
                    self.lifecycle.applied_retention if self.lifecycle else None
                )
            },
            "voiceprints": self._voiceprints_payload(),
        }

    def health_payload(self) -> dict[str, Any]:
        status, reason = self.availability()
        return {
            "status": status,
            "reason_code": reason,
            "checks": {
                "process": True,
                "model": self.model.state is ModelState.VALID,
                "encoder": self._encoder is not None,
                "storage": self._storage_available(),
            },
        }
