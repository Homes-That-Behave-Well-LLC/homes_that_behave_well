"""Runtime-level retention option reconciliation and startup migration."""

from __future__ import annotations

import json

from conftest import FakeEncoder, api_get, fake_identity, synthetic_recordings

PERSON = "person-0001"


def write_options(data_dir, retain: bool) -> None:
    (data_dir / "options.json").write_text(json.dumps({"retain_enrollment_recordings": retain}))


async def test_options_file_applied_at_start(runtime_factory, data_dir) -> None:
    write_options(data_dir, True)
    runtime = await runtime_factory()
    assert runtime.lifecycle.applied_retention is True
    _, body, _ = await api_get(runtime, "/v1/status", runtime.secrets.current())
    assert body["retention"] == {"applied_retain_enrollment_recordings": True}


async def test_options_polling_reconciles_yes_to_no(
    runtime_factory, data_dir, mock_supervisor
) -> None:
    mock, client = mock_supervisor
    write_options(data_dir, True)
    mock.options = {"retain_enrollment_recordings": True}
    runtime = await runtime_factory(supervisor=client)
    runtime.lifecycle.create_voiceprint(PERSON, synthetic_recordings())
    assert runtime.store.has_retained(PERSON)

    assert await runtime.poll_options_once() is False  # unchanged
    mock.options = {"retain_enrollment_recordings": False}
    assert await runtime.poll_options_once() is True
    assert runtime.lifecycle.applied_retention is False
    assert not runtime.store.has_retained(PERSON)
    assert runtime.lifecycle.voiceprint_exists(PERSON)
    _, body, _ = await api_get(runtime, "/v1/status", runtime.secrets.current())
    assert body["retention"] == {"applied_retain_enrollment_recordings": False}
    assert body["voiceprints"] == [
        {
            "person_id": PERSON,
            "voiceprint_exists": True,
            "voiceprint_state": "current",
            "retained_recordings": False,
        }
    ]


async def test_options_poll_loop_runs_periodically(
    runtime_factory, data_dir, mock_supervisor
) -> None:
    import asyncio

    mock, client = mock_supervisor
    write_options(data_dir, False)
    mock.options = {"retain_enrollment_recordings": True}
    runtime = await runtime_factory(supervisor=client, options_poll_interval_s=0.05)
    for _ in range(200):
        if runtime.lifecycle.applied_retention is True:
            break
        await asyncio.sleep(0.01)
    assert runtime.lifecycle.applied_retention is True


INCOMPATIBLE_ENTRY = {
    "person_id": PERSON,
    "voiceprint_exists": True,
    "voiceprint_state": "incompatible",
}


async def _restart_with_new_encoder(runtime_factory, data_dir, retain: bool, **encoder_kwargs):
    write_options(data_dir, retain)
    first = await runtime_factory()
    old = first.lifecycle.create_voiceprint(PERSON, synthetic_recordings())
    await first.stop()
    encoder = FakeEncoder(fake_identity("fake-2"), **encoder_kwargs)
    second = await runtime_factory(encoder_factory=lambda _b, _i: encoder)
    return old, second, encoder


async def test_startup_without_authorization_keeps_voiceprint_without_recordings(
    runtime_factory, data_dir
) -> None:
    old, runtime, encoder = await _restart_with_new_encoder(runtime_factory, data_dir, False)
    assert [(o.outcome, o.reason_code) for o in runtime.last_migration] == [
        ("deferred", "migration_not_authorized")
    ]
    record = runtime.store.get_voiceprint(PERSON)
    assert record is not None
    assert record.artifact_file == old.artifact_file
    assert record.state_reason == "migration_not_authorized"
    _, body, _ = await api_get(runtime, "/v1/status", runtime.secrets.current())
    assert body["voiceprints"] == [{**INCOMPATIBLE_ENTRY, "retained_recordings": False}]
    assert body["compatibility_id"] == encoder.identity.compatibility_id


async def test_startup_without_authorization_rebuilds_nothing(runtime_factory, data_dir) -> None:
    old, runtime, encoder = await _restart_with_new_encoder(runtime_factory, data_dir, True)
    assert [o.outcome for o in runtime.last_migration] == ["deferred"]
    assert encoder.calls == 0
    assert runtime.store.get_voiceprint(PERSON).compatibility_id == old.compatibility_id
    _, body, _ = await api_get(runtime, "/v1/status", runtime.secrets.current())
    assert body["status"] == "available"
    assert body["voiceprints"] == [{**INCOMPATIBLE_ENTRY, "retained_recordings": True}]


async def test_authorized_migration_regenerates(runtime_factory, data_dir) -> None:
    _, runtime, encoder = await _restart_with_new_encoder(runtime_factory, data_dir, True)
    outcomes = runtime.lifecycle.migrate(encoder.identity.compatibility_id)
    assert [o.outcome for o in outcomes] == ["regenerated"]
    _, body, _ = await api_get(runtime, "/v1/status", runtime.secrets.current())
    assert body["voiceprints"] == [
        {
            "person_id": PERSON,
            "voiceprint_exists": True,
            "voiceprint_state": "current",
            "retained_recordings": True,
        }
    ]


async def test_authorized_migration_without_recordings_reports_absence(
    runtime_factory, data_dir
) -> None:
    _, runtime, encoder = await _restart_with_new_encoder(runtime_factory, data_dir, False)
    outcomes = runtime.lifecycle.migrate(encoder.identity.compatibility_id)
    assert [o.outcome for o in outcomes] == ["removed"]
    _, body, _ = await api_get(runtime, "/v1/status", runtime.secrets.current())
    assert body["voiceprints"] == []


async def test_authorized_migration_failure_reports_incompatible(runtime_factory, data_dir):
    _, runtime, encoder = await _restart_with_new_encoder(
        runtime_factory, data_dir, True, fail_on_call=1
    )
    outcomes = runtime.lifecycle.migrate(encoder.identity.compatibility_id)
    assert [(o.outcome, o.reason_code) for o in outcomes] == [("failed", "rebuild_failed")]
    _, body, _ = await api_get(runtime, "/v1/status", runtime.secrets.current())
    assert body["status"] == "available"
    assert body["voiceprints"] == [{**INCOMPATIBLE_ENTRY, "retained_recordings": True}]
