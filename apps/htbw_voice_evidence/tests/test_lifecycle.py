"""Storage layout and Voiceprint lifecycle foundation (fake deterministic encoder)."""

from __future__ import annotations

import numpy as np
import pytest
from conftest import FakeEncoder, fake_identity, synthetic_recordings

from htbw_voice_evidence.lifecycle import (
    EncoderUnavailableError,
    EnrollmentCardinalityError,
    InvalidRecordingError,
    VoiceprintLifecycle,
)
from htbw_voice_evidence.storage import (
    EvidenceStore,
    InvalidPersonIdError,
    VoiceprintAlreadyExistsError,
    VoiceprintState,
    person_key,
)

PERSON = "person-0001"


class Holder:
    def __init__(self, encoder: FakeEncoder | None) -> None:
        self.encoder = encoder

    def __call__(self):
        return self.encoder


@pytest.fixture
def holder() -> Holder:
    return Holder(FakeEncoder())


@pytest.fixture
def lifecycle(store: EvidenceStore, holder: Holder) -> VoiceprintLifecycle:
    return VoiceprintLifecycle(store, holder)


def all_files(store: EvidenceStore) -> list[str]:
    return sorted(str(p.relative_to(store.root)) for p in store.root.rglob("*") if p.is_file())


# Storage -------------------------------------------------------------------------------
def test_storage_initializes_distinct_areas(store: EvidenceStore) -> None:
    for path in (
        store.voiceprints_dir,
        store.incoming_dir,
        store.retained_dir,
        store.models_dir,
        store.state_file.parent,
        store.secret_file.parent,
    ):
        assert path.is_dir()
    assert store.is_available()


def test_person_id_is_never_a_path_component(lifecycle, store) -> None:
    lifecycle.apply_retention(True)
    lifecycle.create_voiceprint(PERSON, synthetic_recordings())
    names = [p.name for p in store.root.rglob("*")]
    assert all(PERSON not in name for name in names)
    assert (store.voiceprints_dir / person_key(PERSON)).is_dir()
    assert (store.retained_dir / person_key(PERSON)).is_dir()


@pytest.mark.parametrize("bad", ["", "   ", None, "x" * 300, "bad\nid", 5])
def test_invalid_person_ids_rejected(lifecycle, bad) -> None:
    with pytest.raises(InvalidPersonIdError):
        lifecycle.create_voiceprint(bad, synthetic_recordings())


def test_voiceprint_metadata_and_artifact(lifecycle, store) -> None:
    record = lifecycle.create_voiceprint(PERSON, synthetic_recordings())
    identity = fake_identity()
    assert record.person_id == PERSON
    assert record.compatibility_id == identity.compatibility_id
    assert record.encoder_family == identity.encoder_family
    assert record.encoder_version == identity.encoder_version
    assert record.audio_contract_version == identity.audio_contract_version
    assert record.state is VoiceprintState.CURRENT
    assert record.created_at.endswith("Z")
    matrix = store.load_embeddings(record)
    assert matrix.shape == (10, 8)  # per-recording embeddings, no aggregation
    assert np.all(np.isfinite(matrix))
    assert store.get_voiceprint(PERSON) == record


def test_sweep_removes_crash_leftovers(store, lifecycle) -> None:
    lifecycle.create_voiceprint(PERSON, synthetic_recordings())
    vp_dir = store.voiceprints_dir / person_key(PERSON)
    (vp_dir / "embeddings-orphan.npy").write_bytes(b"x")
    (store.incoming_dir / "abandoned").mkdir()
    (store.retained_dir / "orphan").mkdir()
    removed = store.sweep()
    assert removed == {"incoming": 1, "orphan_artifacts": 1, "orphan_recordings": 1}
    assert store.get_voiceprint(PERSON) is not None


# Creation ------------------------------------------------------------------------------
def test_one_voiceprint_per_person(lifecycle, store) -> None:
    first = lifecycle.create_voiceprint(PERSON, synthetic_recordings(1))
    with pytest.raises(VoiceprintAlreadyExistsError):
        lifecycle.create_voiceprint(PERSON, synthetic_recordings(2))
    assert store.get_voiceprint(PERSON) == first
    assert len(store.list_voiceprints()) == 1
    assert list(store.incoming_dir.iterdir()) == []
    lifecycle.delete_enrollment(PERSON)
    lifecycle.create_voiceprint(PERSON, synthetic_recordings(2))


@pytest.mark.parametrize("count", [0, 1, 9, 11, 20])
def test_exactly_ten_recordings_enforced(lifecycle, store, count) -> None:
    with pytest.raises(EnrollmentCardinalityError) as info:
        lifecycle.create_voiceprint(PERSON, synthetic_recordings(count=count))
    assert info.value.reason_code == "invalid_recording_count"
    assert store.get_voiceprint(PERSON) is None
    assert all_files(store) == []


def test_invalid_audio_rejected(lifecycle, store) -> None:
    recordings = synthetic_recordings()
    recordings[3] = b"\x01\x02\x03"  # odd length: not s16le
    with pytest.raises(InvalidRecordingError):
        lifecycle.create_voiceprint(PERSON, recordings)
    assert store.get_voiceprint(PERSON) is None


def test_creation_requires_validated_encoder(store) -> None:
    lifecycle = VoiceprintLifecycle(store, Holder(None))
    with pytest.raises(EncoderUnavailableError):
        lifecycle.create_voiceprint(PERSON, synthetic_recordings())


def test_encoder_failure_leaves_no_partial_state(store) -> None:
    lifecycle = VoiceprintLifecycle(store, Holder(FakeEncoder(fail_on_call=4)))
    lifecycle.apply_retention(True)
    with pytest.raises(Exception, match="injected"):
        lifecycle.create_voiceprint(PERSON, synthetic_recordings())
    assert store.get_voiceprint(PERSON) is None
    assert not store.has_retained(PERSON)
    assert list(store.incoming_dir.iterdir()) == []
    assert list(store.voiceprints_dir.iterdir()) == []


# Retention -----------------------------------------------------------------------------
def test_retention_no_deletes_recordings_keeps_voiceprint(lifecycle, store) -> None:
    lifecycle.apply_retention(False)
    lifecycle.create_voiceprint(PERSON, synthetic_recordings())
    assert store.get_voiceprint(PERSON) is not None
    assert not store.has_retained(PERSON)
    assert list(store.incoming_dir.iterdir()) == []
    assert not any(name.endswith(".pcm") for name in all_files(store))


def test_retention_unknown_behaves_as_no_for_new_enrollments(lifecycle, store) -> None:
    assert lifecycle.applied_retention is None
    lifecycle.create_voiceprint(PERSON, synthetic_recordings())
    assert not store.has_retained(PERSON)


def test_retention_yes_keeps_both(lifecycle, store) -> None:
    recordings = synthetic_recordings()
    lifecycle.apply_retention(True)
    lifecycle.create_voiceprint(PERSON, recordings)
    assert store.get_voiceprint(PERSON) is not None
    assert store.has_retained(PERSON)
    assert store.load_retained(PERSON) == recordings


def test_retention_yes_to_no_deletes_recordings_only(lifecycle, store) -> None:
    lifecycle.apply_retention(True)
    lifecycle.create_voiceprint("person-a", synthetic_recordings(1))
    lifecycle.create_voiceprint("person-b", synthetic_recordings(2))
    before = {r.person_id: r for r in store.list_voiceprints()}
    result = lifecycle.apply_retention(False)
    assert result.applied_retain_enrollment_recordings is False
    assert result.removed_recording_sets == 2
    assert not store.has_retained("person-a")
    assert not store.has_retained("person-b")
    after = {r.person_id: r for r in store.list_voiceprints()}
    assert after == before
    for record in after.values():
        store.load_embeddings(record)
    assert store.read_app_state()["applied_retain_enrollment_recordings"] is False
    assert VoiceprintLifecycle(store, Holder(None)).applied_retention is False


# Deletion ------------------------------------------------------------------------------
def test_delete_enrollment_cleans_everything_and_is_idempotent(lifecycle, store) -> None:
    lifecycle.apply_retention(True)
    lifecycle.create_voiceprint(PERSON, synthetic_recordings(1))
    lifecycle.create_voiceprint("other", synthetic_recordings(2))
    assert lifecycle.delete_enrollment(PERSON) is True
    assert lifecycle.voiceprint_exists(PERSON) is False
    assert not store.has_retained(PERSON)
    assert not (store.voiceprints_dir / person_key(PERSON)).exists()
    assert not (store.retained_dir / person_key(PERSON)).exists()
    assert lifecycle.delete_enrollment(PERSON) is False
    assert lifecycle.voiceprint_exists("other") is True
    assert store.has_retained("other")


# Encoder migration ---------------------------------------------------------------------
def _switch_encoder(holder: Holder, version: str, **kwargs) -> FakeEncoder:
    holder.encoder = FakeEncoder(fake_identity(version), **kwargs)
    return holder.encoder


def authorize(holder: Holder) -> str:
    """Stand-in for an HTBW household migration_authorization for the active encoder."""
    return holder.encoder.identity.compatibility_id


def _vp_files(store: EvidenceStore) -> list[str]:
    return sorted(p.name for p in (store.voiceprints_dir / person_key(PERSON)).iterdir())


@pytest.mark.parametrize("authorization", [None, "other"])
def test_unauthorized_migration_with_recordings_rebuilds_nothing(
    lifecycle, store, holder, authorization
) -> None:
    lifecycle.apply_retention(True)
    old = lifecycle.create_voiceprint(PERSON, synthetic_recordings())
    old_matrix = store.load_embeddings(old)
    new_encoder = _switch_encoder(holder, "fake-2")
    if authorization == "other":
        # Authorization issued for a different compatibility_id than the active one.
        authorization = fake_identity("fake-3").compatibility_id
        assert authorization != new_encoder.identity.compatibility_id
    outcomes = lifecycle.migrate(authorization)
    assert [(o.person_id, o.outcome, o.reason_code) for o in outcomes] == [
        (PERSON, "deferred", "migration_not_authorized")
    ]
    assert new_encoder.calls == 0
    record = store.get_voiceprint(PERSON)
    assert record.state is VoiceprintState.INCOMPATIBLE
    assert record.state_reason == "migration_not_authorized"
    assert record.compatibility_id == old.compatibility_id
    assert record.artifact_file == old.artifact_file
    np.testing.assert_array_equal(store.load_embeddings(record), old_matrix)
    assert _vp_files(store) == sorted(["record.json", old.artifact_file])
    assert store.load_retained(PERSON) == synthetic_recordings()


@pytest.mark.parametrize("authorization", [None, "other"])
def test_unauthorized_migration_without_recordings_removes_nothing(
    lifecycle, store, holder, authorization
) -> None:
    lifecycle.apply_retention(False)
    old = lifecycle.create_voiceprint(PERSON, synthetic_recordings())
    _switch_encoder(holder, "fake-2")
    if authorization == "other":
        authorization = old.compatibility_id  # authorizes a non-active identity
    outcomes = lifecycle.migrate(authorization)
    assert [(o.outcome, o.reason_code) for o in outcomes] == [
        ("deferred", "migration_not_authorized")
    ]
    assert lifecycle.voiceprint_exists(PERSON) is True
    record = store.get_voiceprint(PERSON)
    assert record.state is VoiceprintState.INCOMPATIBLE
    assert record.state_reason == "migration_not_authorized"
    assert record.artifact_file == old.artifact_file
    store.load_embeddings(record)
    # Repeating the unauthorized pass is stable and still destroys nothing.
    assert [o.outcome for o in lifecycle.migrate(None)] == ["deferred"]
    assert _vp_files(store) == sorted(["record.json", old.artifact_file])


def test_authorization_after_deferral_runs_migration(lifecycle, store, holder) -> None:
    lifecycle.apply_retention(False)
    lifecycle.create_voiceprint(PERSON, synthetic_recordings())
    _switch_encoder(holder, "fake-2")
    lifecycle.migrate(None)
    assert lifecycle.voiceprint_exists(PERSON) is True
    outcomes = lifecycle.migrate(authorize(holder))
    assert [o.outcome for o in outcomes] == ["removed"]
    assert lifecycle.voiceprint_exists(PERSON) is False


def test_migration_rebuilds_from_retained_recordings(lifecycle, store, holder) -> None:
    lifecycle.apply_retention(True)
    old = lifecycle.create_voiceprint(PERSON, synthetic_recordings())
    new_encoder = _switch_encoder(holder, "fake-2")
    outcomes = lifecycle.migrate(authorize(holder))
    assert [(o.person_id, o.outcome) for o in outcomes] == [(PERSON, "regenerated")]
    record = store.get_voiceprint(PERSON)
    assert record.compatibility_id == new_encoder.identity.compatibility_id
    assert record.compatibility_id != old.compatibility_id
    assert record.state is VoiceprintState.CURRENT
    assert record.artifact_file != old.artifact_file
    assert not (store.voiceprints_dir / person_key(PERSON) / old.artifact_file).exists()
    assert store.load_embeddings(record).shape == (10, 8)
    assert store.has_retained(PERSON)
    assert lifecycle.migrate(authorize(holder)) == []


def test_migration_failure_keeps_old_voiceprint_marked_incompatible(
    lifecycle, store, holder
) -> None:
    lifecycle.apply_retention(True)
    old = lifecycle.create_voiceprint(PERSON, synthetic_recordings())
    old_matrix = store.load_embeddings(old)
    _switch_encoder(holder, "fake-2", fail_on_call=5)
    outcomes = lifecycle.migrate(authorize(holder))
    assert [(o.outcome, o.reason_code) for o in outcomes] == [("failed", "rebuild_failed")]
    record = store.get_voiceprint(PERSON)
    assert record.state is VoiceprintState.INCOMPATIBLE
    assert record.compatibility_id == old.compatibility_id
    assert record.artifact_file == old.artifact_file
    np.testing.assert_array_equal(store.load_embeddings(record), old_matrix)
    vp_files = sorted(p.name for p in (store.voiceprints_dir / person_key(PERSON)).iterdir())
    assert vp_files == sorted(["record.json", old.artifact_file])
    assert store.has_retained(PERSON)


def test_migration_failure_during_promotion_is_safe(lifecycle, store, holder, monkeypatch):
    lifecycle.apply_retention(True)
    old = lifecycle.create_voiceprint(PERSON, synthetic_recordings())
    _switch_encoder(holder, "fake-2")
    import htbw_voice_evidence.storage as storage_mod

    real = storage_mod.atomic_write_json

    def failing(path, payload):
        if path.name == "record.json":
            raise OSError("injected disk failure")
        return real(path, payload)

    monkeypatch.setattr(storage_mod, "atomic_write_json", failing)
    outcomes = lifecycle.migrate(authorize(holder))
    monkeypatch.setattr(storage_mod, "atomic_write_json", real)
    assert outcomes[0].outcome == "failed"
    assert outcomes[0].reason_code == "validation_failed"
    vp_files = sorted(p.name for p in (store.voiceprints_dir / person_key(PERSON)).iterdir())
    assert vp_files == sorted(["record.json", old.artifact_file])
    assert store.get_voiceprint(PERSON).compatibility_id == old.compatibility_id
    store.load_embeddings(store.get_voiceprint(PERSON))


def test_migration_without_recordings_removes_voiceprint(lifecycle, store, holder) -> None:
    lifecycle.apply_retention(False)
    lifecycle.create_voiceprint(PERSON, synthetic_recordings())
    _switch_encoder(holder, "fake-2")
    outcomes = lifecycle.migrate(authorize(holder))
    assert [(o.outcome, o.reason_code) for o in outcomes] == [("removed", "no_retained_recordings")]
    assert lifecycle.voiceprint_exists(PERSON) is False
    assert not (store.voiceprints_dir / person_key(PERSON)).exists()


def test_migration_requires_validated_encoder(store) -> None:
    assert VoiceprintLifecycle(store, Holder(None)).migrate() == []
