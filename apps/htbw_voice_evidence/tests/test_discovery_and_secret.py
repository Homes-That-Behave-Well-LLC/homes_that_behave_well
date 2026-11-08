"""Secret storage, Supervisor discovery provisioning and rotation."""

from __future__ import annotations

import logging
import os
import stat

import pytest
from conftest import SUPERVISOR_TOKEN, api_get

from htbw_voice_evidence.runtime import parse_stdin_command
from htbw_voice_evidence.secret_store import SecretStore


def test_secret_created_private_and_persistent(tmp_path) -> None:
    path = tmp_path / "auth" / "api_secret"
    first = SecretStore(path).load_or_create()
    assert len(first) >= 43  # token_urlsafe(32)
    if os.name == "posix":
        assert stat.S_IMODE(path.stat().st_mode) == 0o600
    assert SecretStore(path).load_or_create() == first


def test_rotation_replaces_file_and_rejects_old(tmp_path) -> None:
    path = tmp_path / "auth" / "api_secret"
    store = SecretStore(path)
    old = store.load_or_create()
    new = store.rotate()
    assert new != old
    assert path.read_text() == new
    assert store.verify(new)
    assert not store.verify(old)
    assert not store.verify(None)
    assert not store.verify("")
    assert [p.name for p in path.parent.iterdir()] == ["api_secret"]


@pytest.mark.parametrize(
    ("line", "expected"),
    [
        ('"rotate-secret"\n', "rotate-secret"),
        ("rotate-secret\n", "rotate-secret"),
        ('{"command": "rotate-secret"}', "rotate-secret"),
        ("\n", None),
        ("42", None),
    ],
)
def test_stdin_command_parsing(line, expected) -> None:
    assert parse_stdin_command(line) == expected


async def test_discovery_payload_shape(runtime_factory, mock_supervisor) -> None:
    mock, client = mock_supervisor
    runtime = await runtime_factory(supervisor=client)
    await _wait_for(lambda: runtime.discovery_uuid is not None)
    assert mock.posts == [
        {
            "service": "htbw",
            "config": {
                "host": "test-htbw-voice-evidence",
                "port": runtime.settings.port,
                "api_secret": runtime.secrets.current(),
            },
        }
    ]
    assert set(mock.auth_headers) == {f"Bearer {SUPERVISOR_TOKEN}"}
    assert runtime.discovery_uuid in mock.discovery
    assert runtime.store.read_app_state()["discovery_uuid"] == runtime.discovery_uuid


async def test_rotation_deletes_old_discovery_and_posts_new(runtime_factory, mock_supervisor):
    mock, client = mock_supervisor
    runtime = await runtime_factory(supervisor=client)
    await _wait_for(lambda: runtime.discovery_uuid is not None)
    old_secret = runtime.secrets.current()
    old_uuid = runtime.discovery_uuid
    await runtime.handle_stdin_line('"rotate-secret"')
    new_secret = runtime.secrets.current()
    assert new_secret != old_secret
    assert mock.deletes == [old_uuid]
    assert len(mock.posts) == 2
    assert mock.posts[1]["config"]["api_secret"] == new_secret
    assert runtime.discovery_uuid not in (None, old_uuid)
    assert list(mock.discovery) == [runtime.discovery_uuid]
    assert (await api_get(runtime, "/v1/health", old_secret))[0] == 401
    assert (await api_get(runtime, "/v1/health", new_secret))[0] == 200


async def test_restart_replaces_stale_discovery_message(runtime_factory, mock_supervisor):
    mock, client = mock_supervisor
    runtime = await runtime_factory(supervisor=client)
    await _wait_for(lambda: runtime.discovery_uuid is not None)
    first_uuid = runtime.discovery_uuid
    await runtime.stop()
    second = await runtime_factory(supervisor=client)
    await _wait_for(lambda: second.discovery_uuid not in (None, first_uuid))
    assert first_uuid in mock.deletes
    assert mock.posts[0]["config"]["api_secret"] == mock.posts[1]["config"]["api_secret"]


async def test_discovery_failure_is_retried_and_secret_not_logged(
    runtime_factory, mock_supervisor, caplog
) -> None:
    caplog.set_level(logging.DEBUG)
    mock, client = mock_supervisor
    mock.fail_posts = 1
    runtime = await runtime_factory(supervisor=client, discovery_attempts=3)
    await _wait_for(lambda: runtime.discovery_uuid is not None)
    assert len(mock.posts) == 2
    log_text = "\n".join(r.getMessage() for r in caplog.records)
    assert "discovery_failed" in log_text
    assert runtime.secrets.current() not in log_text
    assert SUPERVISOR_TOKEN not in log_text


async def test_no_supervisor_skips_discovery_with_manual_notice(runtime_factory, caplog):
    caplog.set_level(logging.INFO)
    runtime = await runtime_factory()
    await _wait_for(lambda: "manual provisioning required" in caplog.text)
    assert runtime.discovery_uuid is None
    assert runtime.secrets.current() not in caplog.text


async def _wait_for(predicate, timeout: float = 5.0) -> None:
    import asyncio

    loop = asyncio.get_running_loop()
    deadline = loop.time() + timeout
    while not predicate():
        if loop.time() > deadline:
            raise AssertionError("condition not reached")
        await asyncio.sleep(0.01)
