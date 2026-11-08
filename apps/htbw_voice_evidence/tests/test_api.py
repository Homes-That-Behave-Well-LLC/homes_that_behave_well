"""Contract A API: authentication, health and status payloads."""

from __future__ import annotations

import json
import logging

import pytest
from conftest import FAKE_MODEL_PIN, FakeEncoder, api_get, synthetic_recordings

from htbw_voice_evidence.const import APP_VERSION, CONTRACT_VERSION

STATUS_KEYS = {
    "contract_version",
    "app_version",
    "status",
    "reason_code",
    "compatibility_id",
    "encoder_family",
    "encoder_version",
    "audio_contract_version",
    "model_artifact",
    "storage",
    "optional_capabilities",
    "retention",
    "voiceprints",
}


async def test_app_starts_in_test_mode_and_reports_health(runtime_factory) -> None:
    runtime = await runtime_factory()
    status, body, _ = await api_get(runtime, "/v1/health", runtime.secrets.current())
    assert status == 200
    assert body == {
        "status": "available",
        "reason_code": None,
        "checks": {"process": True, "model": True, "encoder": True, "storage": True},
    }


async def test_status_reports_contract_identity_and_capabilities(runtime_factory) -> None:
    runtime = await runtime_factory()
    status, body, _ = await api_get(runtime, "/v1/status", runtime.secrets.current())
    assert status == 200
    assert set(body) == STATUS_KEYS
    assert body["contract_version"] == CONTRACT_VERSION == "1.0"
    assert body["app_version"] == APP_VERSION == "0.1.0"
    assert body["status"] == "available"
    assert body["reason_code"] is None
    identity = FakeEncoder().identity
    assert body["compatibility_id"] == identity.compatibility_id
    assert body["encoder_family"] == identity.encoder_family
    assert body["encoder_version"] == identity.encoder_version
    assert body["audio_contract_version"] == identity.audio_contract_version
    assert body["model_artifact"] == {
        "state": "valid",
        "model_id": FAKE_MODEL_PIN.model_id,
        "revision": FAKE_MODEL_PIN.revision,
        "sha256": FAKE_MODEL_PIN.sha256,
    }
    assert body["storage"] == {"state": "available"}
    assert body["optional_capabilities"] == []
    assert body["retention"] == {"applied_retain_enrollment_recordings": None}
    assert body["voiceprints"] == []
    assert "enrollment_requirements" not in json.dumps(body)


async def test_status_lists_voiceprints_without_sensitive_fields(runtime_factory) -> None:
    runtime = await runtime_factory()
    await runtime.reconcile_options({"retain_enrollment_recordings": True}, force=True)
    runtime.lifecycle.create_voiceprint("person-a", synthetic_recordings(1))
    status, body, text = await api_get(runtime, "/v1/status", runtime.secrets.current())
    assert status == 200
    assert body["retention"] == {"applied_retain_enrollment_recordings": True}
    assert body["voiceprints"] == [
        {
            "person_id": "person-a",
            "voiceprint_exists": True,
            "voiceprint_state": "current",
            "retained_recordings": True,
        }
    ]
    for forbidden in ("embedding", "score", "consent", "count", "path", "secret", "/data"):
        assert forbidden not in text


@pytest.mark.parametrize("path", ["/v1/status", "/v1/health", "/", "/v1/unknown"])
async def test_missing_bearer_is_rejected(runtime_factory, path: str) -> None:
    runtime = await runtime_factory()
    status, body, _ = await api_get(runtime, path)
    assert status == 401
    assert body == {"error": "unauthorized"}


@pytest.mark.parametrize(
    ("token", "scheme"),
    [("wrong-secret", "Bearer"), ("", "Bearer"), (None, "Basic")],
)
async def test_invalid_bearer_is_rejected(runtime_factory, token, scheme) -> None:
    runtime = await runtime_factory()
    presented = runtime.secrets.current() if token is None else token
    status, body, _ = await api_get(runtime, "/v1/status", presented, scheme=scheme)
    assert status == 401
    assert body == {"error": "unauthorized"}


async def test_unknown_route_with_valid_bearer_is_404_without_detail(runtime_factory) -> None:
    runtime = await runtime_factory()
    status, body, _ = await api_get(runtime, "/v1/enroll", runtime.secrets.current())
    assert status == 404
    assert body == {"error": "not_found"}


async def test_rotated_secret_rejects_old_bearer(runtime_factory) -> None:
    runtime = await runtime_factory()
    old = runtime.secrets.current()
    assert (await api_get(runtime, "/v1/status", old))[0] == 200
    await runtime.handle_stdin_line('"rotate-secret"\n')
    new = runtime.secrets.current()
    assert new != old
    assert (await api_get(runtime, "/v1/status", old))[0] == 401
    assert (await api_get(runtime, "/v1/status", new))[0] == 200


async def test_secret_never_logged_or_returned(runtime_factory, caplog) -> None:
    caplog.set_level(logging.DEBUG)
    runtime = await runtime_factory()
    first = runtime.secrets.current()
    texts = []
    for path in ("/v1/status", "/v1/health", "/nope"):
        texts.append((await api_get(runtime, path, first))[2])
        texts.append((await api_get(runtime, path, "bad"))[2])
    await runtime.rotate_secret()
    second = runtime.secrets.current()
    texts.append((await api_get(runtime, "/v1/status", second))[2])
    log_text = "\n".join(record.getMessage() for record in caplog.records)
    assert "manual provisioning required" in log_text
    for secret in (first, second):
        assert secret not in log_text
        assert all(secret not in text for text in texts)
