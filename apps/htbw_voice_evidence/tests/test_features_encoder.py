"""Feature extraction, encoder identity, and Match Level vocabulary."""

from __future__ import annotations

from dataclasses import replace

import numpy as np
import pytest
from conftest import synthetic_pcm

from htbw_voice_evidence.encoder import (
    Encoder,
    EncoderIdentity,
    governed_identity,
    validate_embedding,
)
from htbw_voice_evidence.features import (
    WESPEAKER_FBANK_PARAMS,
    AudioContractError,
    FbankParams,
    extract_features,
    kaldi_fbank,
    mel_banks,
    num_frames,
    pcm_s16le_to_array,
)
from htbw_voice_evidence.match_levels import (
    MatchLevel,
    MatchLevelUncalibratedError,
    UncalibratedMatchLevelMapper,
)


def test_wespeaker_inference_parameters() -> None:
    params = WESPEAKER_FBANK_PARAMS
    assert params.num_mel_bins == 80
    assert params.frame_length_samples == 400
    assert params.frame_shift_samples == 160
    assert params.padded_window_size == 512
    assert params.dither == 0.0
    assert params.window_type == "hamming"
    assert params.use_energy is False
    assert params.sample_rate_hz == 16000


def test_fbank_shape_and_cmn() -> None:
    pcm = synthetic_pcm(7, seconds=1.0)
    feats = extract_features(pcm)
    assert feats.dtype == np.float32
    assert feats.shape == (num_frames(16000), 80) == (98, 80)
    assert np.all(np.isfinite(feats))
    np.testing.assert_allclose(feats.mean(axis=0), 0.0, atol=1e-4)


def test_fbank_is_deterministic_and_uses_int16_scale() -> None:
    pcm = synthetic_pcm(3)
    raw = kaldi_fbank(pcm_s16le_to_array(pcm))
    np.testing.assert_array_equal(raw, kaldi_fbank(pcm_s16le_to_array(pcm)))
    # Scaling the waveform by 2 adds log(4) to every (non-floored) log-mel energy.
    doubled = kaldi_fbank(pcm_s16le_to_array(pcm) * 2.0)
    np.testing.assert_allclose(doubled - raw, np.log(4.0), atol=1e-3)


def test_silence_hits_energy_floor() -> None:
    feats = kaldi_fbank(np.zeros(1600))
    np.testing.assert_allclose(feats, np.log(np.finfo(np.float32).eps), rtol=1e-6)


def test_mel_banks_shape() -> None:
    banks = mel_banks(WESPEAKER_FBANK_PARAMS)
    assert banks.shape == (80, 257)
    assert np.all(banks >= 0)
    assert np.all(banks[:, -1] == 0)
    assert np.all(banks.sum(axis=1) > 0)
    assert np.all(banks.max(axis=1) <= 1.0)


def _naive_frame_logmel(frame: np.ndarray, params: FbankParams) -> np.ndarray:
    x = frame.astype(np.float64).copy()
    x -= x.mean()
    for i in range(len(x) - 1, 0, -1):
        x[i] -= params.preemphasis_coefficient * x[i - 1]
    x[0] -= params.preemphasis_coefficient * x[0]
    n = len(x)
    x *= np.array([0.54 - 0.46 * np.cos(2 * np.pi * i / (n - 1)) for i in range(n)])
    padded = np.zeros(params.padded_window_size)
    padded[:n] = x
    power = np.abs(np.fft.rfft(padded)) ** 2
    energies = mel_banks(params) @ power
    return np.log(np.maximum(energies, np.finfo(np.float32).eps))


def test_vectorized_fbank_matches_per_frame_reference() -> None:
    samples = pcm_s16le_to_array(synthetic_pcm(11, seconds=0.3))
    feats = kaldi_fbank(samples)
    p = WESPEAKER_FBANK_PARAMS
    for idx in (0, 5, feats.shape[0] - 1):
        start = idx * p.frame_shift_samples
        ref = _naive_frame_logmel(samples[start : start + p.frame_length_samples], p)
        np.testing.assert_allclose(feats[idx], ref, rtol=1e-5, atol=1e-4)


def test_fbank_matches_torchaudio_kaldi_when_available() -> None:
    torch = pytest.importorskip("torch")
    kaldi = pytest.importorskip("torchaudio.compliance.kaldi")
    pcm = synthetic_pcm(5, seconds=1.0)
    waveform = torch.from_numpy(pcm_s16le_to_array(pcm).astype(np.float32))[None, :]
    reference = kaldi.fbank(
        waveform,
        num_mel_bins=80,
        frame_length=25,
        frame_shift=10,
        dither=0.0,
        sample_frequency=16000,
        window_type="hamming",
        use_energy=False,
    ).numpy()
    ours = kaldi_fbank(pcm_s16le_to_array(pcm))
    assert ours.shape == reference.shape
    np.testing.assert_allclose(ours, reference, rtol=1e-3, atol=2e-3)


@pytest.mark.parametrize("pcm", [b"\x00", b"\x00\x00" * 100])
def test_audio_contract_violations(pcm: bytes) -> None:
    with pytest.raises(AudioContractError):
        extract_features(pcm)


def test_compatibility_id_changes_with_every_governed_field() -> None:
    base = governed_identity()
    assert base.compatibility_id == governed_identity().compatibility_id
    variants = [
        replace(base, encoder_family="other"),
        replace(base, encoder_version="other"),
        replace(base, model_sha256="0" * 64),
        replace(base, audio_contract_version="pcm_s16le_8000hz_mono.v1"),
        governed_identity(params=replace(WESPEAKER_FBANK_PARAMS, num_mel_bins=64)),
    ]
    ids = {base.compatibility_id, *(v.compatibility_id for v in variants)}
    assert len(ids) == len(variants) + 1


def test_governed_identity_fields() -> None:
    identity = governed_identity()
    assert isinstance(identity, EncoderIdentity)
    assert identity.encoder_family == "wespeaker_ecapa_tdnn512_lm"
    assert identity.audio_contract_version == "pcm_s16le_16000hz_mono.v1"
    assert identity.compatibility_id.startswith("vecid1-")


def test_fake_encoder_satisfies_protocol() -> None:
    from conftest import FakeEncoder

    assert isinstance(FakeEncoder(), Encoder)


def test_validate_embedding_rejects_bad_vectors() -> None:
    with pytest.raises(Exception, match="1-D"):
        validate_embedding(np.zeros((2, 2)))
    with pytest.raises(Exception, match="non-finite"):
        validate_embedding(np.array([1.0, np.nan]))
    with pytest.raises(Exception, match="dimension"):
        validate_embedding(np.ones(3), expected_dim=4)


def test_match_level_vocabulary_is_ordinal() -> None:
    assert [level.value for level in sorted(MatchLevel)] == [
        "no_match",
        "low",
        "moderate",
        "high",
        "very_high",
    ]
    assert MatchLevel.NO_MATCH < MatchLevel.LOW < MatchLevel.VERY_HIGH


@pytest.mark.parametrize("similarity", [-1.0, 0.0, 0.5, 0.99, 1.0])
def test_uncalibrated_mapper_never_guesses(similarity: float) -> None:
    mapper = UncalibratedMatchLevelMapper()
    assert mapper.calibrated is False
    with pytest.raises(MatchLevelUncalibratedError) as info:
        mapper.map(similarity)
    assert info.value.reason_code == "uncalibrated"
