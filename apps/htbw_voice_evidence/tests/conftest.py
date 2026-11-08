"""Shared fixtures. All audio is synthetic (numpy-generated); no human voice data."""

from __future__ import annotations

import hashlib
import uuid as uuid_mod
from collections.abc import AsyncIterator, Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, BinaryIO

import aiohttp
import numpy as np
import pytest
from aiohttp import web
from aiohttp.test_utils import TestServer

from htbw_voice_evidence.const import ENROLLMENT_RECORDING_COUNT
from htbw_voice_evidence.encoder import EncoderError, EncoderIdentity
from htbw_voice_evidence.model_artifact import DownloadError, ModelPin
from htbw_voice_evidence.runtime import EvidenceRuntime
from htbw_voice_evidence.settings import Settings
from htbw_voice_evidence.storage import EvidenceStore
from htbw_voice_evidence.supervisor import SupervisorClient

FAKE_MODEL_BYTES = b"fake-onnx-model-for-tests-only" * 64
FAKE_MODEL_PIN = ModelPin(
    model_id="test/fake-model",
    filename="fake.onnx",
    revision="0" * 40,
    sha256=hashlib.sha256(FAKE_MODEL_BYTES).hexdigest(),
    size_bytes=len(FAKE_MODEL_BYTES),
    url="https://example.invalid/fake.onnx",
    max_bytes=1 << 20,
)


def synthetic_pcm(seed: int, seconds: float = 1.0, sample_rate: int = 16000) -> bytes:
    """Deterministic synthetic tone+noise as s16le PCM (never real voice)."""
    rng = np.random.default_rng(seed)
    t = np.arange(int(seconds * sample_rate)) / sample_rate
    freq = 120.0 + 10.0 * (seed % 17)
    signal = 0.3 * np.sin(2 * np.pi * freq * t) + 0.05 * rng.standard_normal(t.shape[0])
    return (np.clip(signal, -1.0, 1.0) * 32767).astype("<i2").tobytes()


def synthetic_recordings(seed: int = 0, count: int = ENROLLMENT_RECORDING_COUNT) -> list[bytes]:
    return [synthetic_pcm(seed * 100 + i, seconds=0.5) for i in range(count)]


def fake_identity(version: str = "fake-1") -> EncoderIdentity:
    return EncoderIdentity(
        encoder_family="fake_encoder",
        encoder_version=version,
        model_sha256=FAKE_MODEL_PIN.sha256,
        audio_contract_version="pcm_s16le_16000hz_mono.v1",
        feature_params={"kind": "fake"},
    )


class FakeEncoder:
    """Deterministic encoder: an 8-dim vector derived from the PCM digest."""

    def __init__(self, identity: EncoderIdentity | None = None, fail_on_call: int | None = None):
        self._identity = identity or fake_identity()
        self.calls = 0
        self.fail_on_call = fail_on_call

    @property
    def identity(self) -> EncoderIdentity:
        return self._identity

    def embed(self, pcm: bytes) -> np.ndarray:
        self.calls += 1
        if self.fail_on_call is not None and self.calls >= self.fail_on_call:
            raise EncoderError("injected encoder failure")
        digest = hashlib.sha256(self._identity.encoder_version.encode() + pcm).digest()
        return (np.frombuffer(digest[:32], dtype=np.uint8)[:8].astype(np.float32) / 255.0) + 0.1


@dataclass
class FakeDownloader:
    payload: bytes = FAKE_MODEL_BYTES
    error: Exception | None = None
    calls: int = 0
    urls: list[str] = field(default_factory=list)

    async def download(self, url: str, dest: BinaryIO, *, max_bytes: int) -> None:
        self.calls += 1
        self.urls.append(url)
        if self.error is not None:
            dest.write(self.payload[: len(self.payload) // 2])
            raise self.error
        if len(self.payload) > max_bytes:
            raise DownloadError("artifact exceeds the size cap")
        dest.write(self.payload)


def make_settings(data_dir: Path, **overrides: Any) -> Settings:
    base: dict[str, Any] = {
        "data_dir": data_dir,
        "listen_host": "127.0.0.1",
        "port": 0,
        "advertised_host": "test-htbw-voice-evidence",
        "supervisor_token": None,
        "options_poll_interval_s": None,
        "model_retry_interval_s": None,
        "discovery_attempts": 1,
        "discovery_retry_delay_s": 0.0,
        "read_stdin": False,
    }
    base.update(overrides)
    return Settings(**base)


@pytest.fixture
def data_dir(tmp_path: Path) -> Path:
    path = tmp_path / "data"
    path.mkdir()
    return path


@pytest.fixture
def store(data_dir: Path) -> EvidenceStore:
    evidence_store = EvidenceStore(data_dir)
    evidence_store.initialize()
    return evidence_store


@dataclass
class MockSupervisor:
    """In-process stand-in for the Supervisor API."""

    options: dict[str, Any] = field(default_factory=lambda: {"retain_enrollment_recordings": False})
    discovery: dict[str, dict[str, Any]] = field(default_factory=dict)
    posts: list[dict[str, Any]] = field(default_factory=list)
    deletes: list[str] = field(default_factory=list)
    auth_headers: list[str] = field(default_factory=list)
    fail_posts: int = 0

    def app(self) -> web.Application:
        app = web.Application()
        app.router.add_post("/discovery", self._post_discovery)
        app.router.add_delete("/discovery/{uuid}", self._delete_discovery)
        app.router.add_get("/addons/self/info", self._self_info)
        return app

    async def _post_discovery(self, request: web.Request) -> web.Response:
        self.auth_headers.append(request.headers.get("Authorization", ""))
        body = await request.json()
        self.posts.append(body)
        if self.fail_posts > 0:
            self.fail_posts -= 1
            return web.json_response({"result": "error", "message": "boom"}, status=500)
        new_uuid = uuid_mod.uuid4().hex
        self.discovery[new_uuid] = body
        return web.json_response({"result": "ok", "data": {"uuid": new_uuid}})

    async def _delete_discovery(self, request: web.Request) -> web.Response:
        self.auth_headers.append(request.headers.get("Authorization", ""))
        uuid = request.match_info["uuid"]
        self.deletes.append(uuid)
        self.discovery.pop(uuid, None)
        return web.json_response({"result": "ok", "data": {}})

    async def _self_info(self, request: web.Request) -> web.Response:
        self.auth_headers.append(request.headers.get("Authorization", ""))
        return web.json_response(
            {"result": "ok", "data": {"slug": "htbw_voice_evidence", "options": self.options}}
        )


SUPERVISOR_TOKEN = "test-supervisor-token"


@pytest.fixture
async def mock_supervisor() -> AsyncIterator[tuple[MockSupervisor, SupervisorClient]]:
    mock = MockSupervisor()
    server = TestServer(mock.app())
    await server.start_server()
    client = SupervisorClient(str(server.make_url("")), SUPERVISOR_TOKEN, timeout_s=5.0)
    try:
        yield mock, client
    finally:
        await client.close()
        await server.close()


RuntimeFactory = Callable[..., EvidenceRuntime]


@pytest.fixture
async def runtime_factory(data_dir: Path) -> AsyncIterator[Callable[..., Any]]:
    """Builds runtimes in test mode (fake encoder/downloader, ephemeral port)."""
    started: list[EvidenceRuntime] = []

    async def factory(
        *,
        encoder_factory: Callable[[bytes, EncoderIdentity], Any] | None = None,
        downloader: FakeDownloader | None = None,
        supervisor: SupervisorClient | None = None,
        model_pin: ModelPin = FAKE_MODEL_PIN,
        wait_model: bool = True,
        **settings_overrides: Any,
    ) -> EvidenceRuntime:
        runtime = EvidenceRuntime(
            make_settings(data_dir, **settings_overrides),
            encoder_factory=encoder_factory or (lambda _b, _i: FakeEncoder()),
            downloader=downloader or FakeDownloader(),
            supervisor=supervisor,
            model_pin=model_pin,
        )
        await runtime.start()
        started.append(runtime)
        if wait_model:
            await runtime.model_ready.wait()
        return runtime

    yield factory
    for runtime in started:
        await runtime.stop()


async def api_get(
    runtime: EvidenceRuntime, path: str, token: str | None = None, scheme: str = "Bearer"
) -> tuple[int, Any, str]:
    headers = {}
    if token is not None:
        headers["Authorization"] = f"{scheme} {token}"
    async with (
        aiohttp.ClientSession() as session,
        session.get(f"http://127.0.0.1:{runtime.bound_port}{path}", headers=headers) as resp,
    ):
        text = await resp.text()
        try:
            body = await resp.json(content_type=None)
        except ValueError:
            body = None
        return resp.status, body, text
