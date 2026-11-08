"""Pinned model acquisition, digest verification, and failure safety."""

from __future__ import annotations

import hashlib
from dataclasses import replace

from conftest import FAKE_MODEL_BYTES, FAKE_MODEL_PIN, FakeDownloader, FakeEncoder, api_get

from htbw_voice_evidence import const
from htbw_voice_evidence.model_artifact import (
    GOVERNED_MODEL_PIN,
    DownloadError,
    ModelArtifactManager,
    ModelState,
)


def test_governed_pin_is_revision_pinned() -> None:
    pin = GOVERNED_MODEL_PIN
    assert pin.model_id == "Wespeaker/wespeaker-ecapa-tdnn512-LM"
    assert pin.revision == "a2f3dcb1c8702caccc7a55ceb57f5e8d1842112b"
    assert pin.sha256 == "d71b85d9b48058ef68004f04f1b78acebefb9dfcf542e19b976a12a5ad1f10b0"
    assert pin.size_bytes == 24861931
    assert pin.url == (
        "https://huggingface.co/Wespeaker/wespeaker-ecapa-tdnn512-LM/resolve/"
        "a2f3dcb1c8702caccc7a55ceb57f5e8d1842112b/voxceleb_ECAPA512_LM.onnx"
    )
    assert "/main/" not in pin.url


async def test_valid_digest_downloads_promotes_and_loads(runtime_factory) -> None:
    loaded: list[bytes] = []

    def factory(model_bytes, identity):
        loaded.append(model_bytes)
        return FakeEncoder()

    downloader = FakeDownloader()
    runtime = await runtime_factory(encoder_factory=factory, downloader=downloader)
    assert runtime.model.state is ModelState.VALID
    assert runtime.model.active_path.read_bytes() == FAKE_MODEL_BYTES
    assert loaded == [FAKE_MODEL_BYTES]
    assert downloader.urls == [FAKE_MODEL_PIN.url]
    assert list(runtime.model.staging_dir.iterdir()) == []
    assert runtime.availability() == ("available", None)


async def test_existing_valid_artifact_is_not_redownloaded(runtime_factory, data_dir) -> None:
    first = await runtime_factory()
    await first.stop()
    downloader = FakeDownloader()
    second = await runtime_factory(downloader=downloader)
    assert downloader.calls == 0
    assert second.model.state is ModelState.VALID


async def test_invalid_digest_is_unavailable_without_fallback(runtime_factory) -> None:
    built: list[bytes] = []
    downloader = FakeDownloader(payload=b"tampered" * 100)
    runtime = await runtime_factory(
        encoder_factory=lambda b, i: built.append(b) or FakeEncoder(), downloader=downloader
    )
    assert runtime.model.state is ModelState.INVALID
    assert runtime.availability() == ("unavailable", const.REASON_MODEL_DIGEST_MISMATCH)
    assert built == []  # no encoder constructed, no alternative model tried
    assert downloader.urls == [FAKE_MODEL_PIN.url]
    assert not runtime.model.active_path.exists()
    assert list(runtime.model.staging_dir.iterdir()) == []
    status, body, _ = await api_get(runtime, "/v1/status", runtime.secrets.current())
    assert status == 200
    assert body["status"] == "unavailable"
    assert body["reason_code"] == "model_digest_mismatch"
    assert body["model_artifact"]["state"] == "invalid"
    assert body["compatibility_id"] is None
    _, health, _ = await api_get(runtime, "/v1/health", runtime.secrets.current())
    assert health["checks"] == {"process": True, "model": False, "encoder": False, "storage": True}


async def test_download_failure_is_distinct_and_safe(runtime_factory) -> None:
    downloader = FakeDownloader(error=DownloadError("TimeoutError"))
    runtime = await runtime_factory(downloader=downloader)
    assert runtime.model.state is ModelState.DOWNLOAD_FAILED
    assert runtime.availability() == ("unavailable", const.REASON_MODEL_DOWNLOAD_FAILED)
    assert not runtime.model.active_path.exists()
    assert list(runtime.model.staging_dir.iterdir()) == []


async def test_failed_replacement_keeps_known_good_artifact(tmp_path) -> None:
    manager = ModelArtifactManager(tmp_path / "models", FAKE_MODEL_PIN, FakeDownloader())
    assert await manager.ensure() is ModelState.VALID
    good = manager.active_path.read_bytes()

    manager._downloader = FakeDownloader(error=DownloadError("ClientError"))
    assert await manager.redownload() is ModelState.VALID
    assert manager.active_path.read_bytes() == good

    manager._downloader = FakeDownloader(payload=b"wrong" * 50)
    assert await manager.redownload() is ModelState.VALID
    assert manager.active_path.read_bytes() == good
    assert list(manager.staging_dir.iterdir()) == []


async def test_size_cap_enforced(tmp_path) -> None:
    pin = replace(FAKE_MODEL_PIN, max_bytes=16)
    manager = ModelArtifactManager(tmp_path / "models", pin, FakeDownloader())
    assert await manager.ensure() is ModelState.DOWNLOAD_FAILED
    assert not manager.active_path.exists()


async def test_downloads_disabled_reports_missing(tmp_path) -> None:
    downloader = FakeDownloader()
    manager = ModelArtifactManager(tmp_path / "models", FAKE_MODEL_PIN, downloader)
    assert await manager.ensure(allow_download=False) is ModelState.MISSING
    assert manager.reason_code == const.REASON_MODEL_MISSING
    assert downloader.calls == 0


async def test_digest_verified_again_on_every_load(runtime_factory) -> None:
    runtime = await runtime_factory()
    assert runtime.encoder is not None
    runtime.model.active_path.write_bytes(b"corrupted after activation")
    assert runtime.load_encoder() is None
    assert runtime.model.state is ModelState.INVALID
    assert runtime.availability() == ("unavailable", const.REASON_MODEL_DIGEST_MISMATCH)


async def test_corrupt_artifact_on_disk_is_replaced_only_by_validated_download(
    runtime_factory, data_dir
) -> None:
    first = await runtime_factory()
    await first.stop()
    first.model.active_path.write_bytes(b"bit rot")
    second = await runtime_factory(downloader=FakeDownloader())
    assert second.model.state is ModelState.VALID
    digest = hashlib.sha256(second.model.active_path.read_bytes()).hexdigest()
    assert digest == FAKE_MODEL_PIN.sha256


async def test_encoder_contract_mismatch_reports_incompatible(runtime_factory) -> None:
    from htbw_voice_evidence.encoder import EncoderContractMismatchError

    def factory(_bytes, _identity):
        raise EncoderContractMismatchError("feature dimension mismatch")

    runtime = await runtime_factory(encoder_factory=factory)
    assert runtime.availability() == ("incompatible", const.REASON_ENCODER_CONTRACT_MISMATCH)


async def test_encoder_load_failure_reports_unavailable(runtime_factory) -> None:
    def factory(_bytes, _identity):
        raise RuntimeError("boom")

    runtime = await runtime_factory(encoder_factory=factory)
    assert runtime.availability() == ("unavailable", const.REASON_ENCODER_LOAD_FAILED)
