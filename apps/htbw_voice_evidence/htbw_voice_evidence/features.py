"""Kaldi-compatible log-mel filterbank features in NumPy.

Parameters follow what WeSpeaker uses at inference time for its fbank front end
(``wespeaker/cli/speaker.py`` ``compute_features`` and ``wespeaker/bin/infer_onnx.py``):
80 mel bins, 25 ms frames, 10 ms shift, dither 0, Hamming window, energy not used,
waveform in int16 range, then per-utterance cepstral mean normalization (no variance
normalization). The remaining values are the Kaldi ``fbank`` defaults that WeSpeaker
leaves untouched.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

import numpy as np

from .const import AUDIO_SAMPLE_RATE_HZ


class AudioContractError(ValueError):
    """Audio does not satisfy the App audio contract."""


@dataclass(frozen=True)
class FbankParams:
    sample_rate_hz: int = AUDIO_SAMPLE_RATE_HZ
    num_mel_bins: int = 80
    frame_length_ms: float = 25.0
    frame_shift_ms: float = 10.0
    dither: float = 0.0
    preemphasis_coefficient: float = 0.97
    remove_dc_offset: bool = True
    window_type: str = "hamming"
    round_to_power_of_two: bool = True
    snip_edges: bool = True
    low_freq_hz: float = 20.0
    high_freq_hz: float = 0.0
    use_power: bool = True
    use_log_fbank: bool = True
    use_energy: bool = False
    input_scale: str = "int16"
    normalization: str = "utterance_mean"

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)

    @property
    def frame_length_samples(self) -> int:
        return int(self.sample_rate_hz * self.frame_length_ms * 0.001)

    @property
    def frame_shift_samples(self) -> int:
        return int(self.sample_rate_hz * self.frame_shift_ms * 0.001)

    @property
    def padded_window_size(self) -> int:
        size = self.frame_length_samples
        if not self.round_to_power_of_two:
            return size
        return 1 << (size - 1).bit_length()


WESPEAKER_FBANK_PARAMS = FbankParams()

_FLOAT32_EPS = float(np.finfo(np.float32).eps)


def pcm_s16le_to_array(pcm: bytes) -> np.ndarray:
    """Decode signed 16-bit little-endian mono PCM to float64 samples in int16 range."""
    if not isinstance(pcm, (bytes, bytearray, memoryview)):
        raise AudioContractError("audio must be raw PCM bytes")
    if len(pcm) % 2:
        raise AudioContractError("PCM length must be a whole number of 16-bit samples")
    return np.frombuffer(bytes(pcm), dtype="<i2").astype(np.float64)


def _mel(freq: np.ndarray | float) -> np.ndarray | float:
    return 1127.0 * np.log(1.0 + np.asarray(freq) / 700.0)


def mel_banks(params: FbankParams) -> np.ndarray:
    """Triangular mel filters, shape (num_mel_bins, padded_window_size // 2 + 1)."""
    padded = params.padded_window_size
    num_fft_bins = padded // 2
    nyquist = 0.5 * params.sample_rate_hz
    high = params.high_freq_hz if params.high_freq_hz > 0 else nyquist + params.high_freq_hz
    low = params.low_freq_hz
    if not 0.0 <= low < high <= nyquist:
        raise ValueError("invalid mel frequency range")
    fft_bin_width = params.sample_rate_hz / padded
    mel_low = _mel(low)
    mel_high = _mel(high)
    delta = (mel_high - mel_low) / (params.num_mel_bins + 1)
    index = np.arange(params.num_mel_bins, dtype=np.float64)[:, None]
    left = mel_low + index * delta
    center = mel_low + (index + 1.0) * delta
    right = mel_low + (index + 2.0) * delta
    mel = np.asarray(_mel(fft_bin_width * np.arange(num_fft_bins, dtype=np.float64)))[None, :]
    up = (mel - left) / (center - left)
    down = (right - mel) / (right - center)
    banks = np.maximum(0.0, np.minimum(up, down))
    # The Nyquist bin never contributes to a Kaldi mel filter.
    return np.pad(banks, ((0, 0), (0, 1)))


def _window(params: FbankParams) -> np.ndarray:
    n = params.frame_length_samples
    if params.window_type == "hamming":
        return 0.54 - 0.46 * np.cos(2.0 * np.pi * np.arange(n) / (n - 1))
    raise ValueError(f"unsupported window type: {params.window_type}")


def num_frames(num_samples: int, params: FbankParams = WESPEAKER_FBANK_PARAMS) -> int:
    length = params.frame_length_samples
    if not params.snip_edges:
        raise ValueError("only snip_edges=True is supported")
    if num_samples < length:
        return 0
    return 1 + (num_samples - length) // params.frame_shift_samples


def kaldi_fbank(samples: np.ndarray, params: FbankParams = WESPEAKER_FBANK_PARAMS) -> np.ndarray:
    """Compute log-mel filterbank features, shape (frames, num_mel_bins), float32."""
    if params.dither != 0.0:
        raise ValueError("dither must be 0 for deterministic inference")
    if params.use_energy:
        raise ValueError("energy feature is not part of the governed front end")
    waveform = np.asarray(samples, dtype=np.float64).reshape(-1)
    frames_count = num_frames(waveform.shape[0], params)
    if frames_count == 0:
        raise AudioContractError("audio is shorter than one analysis frame")
    length = params.frame_length_samples
    shift = params.frame_shift_samples
    frames = np.lib.stride_tricks.sliding_window_view(waveform, length)[::shift][:frames_count]
    frames = np.array(frames, dtype=np.float64)
    if params.remove_dc_offset:
        frames -= frames.mean(axis=1, keepdims=True)
    if params.preemphasis_coefficient != 0.0:
        previous = np.concatenate([frames[:, :1], frames[:, :-1]], axis=1)
        frames = frames - params.preemphasis_coefficient * previous
    frames *= _window(params)[None, :]
    spectrum = np.fft.rfft(frames, n=params.padded_window_size, axis=1)
    power = np.abs(spectrum) ** 2
    if not params.use_power:
        power = np.sqrt(power)
    energies = power @ mel_banks(params).T
    if params.use_log_fbank:
        energies = np.log(np.maximum(energies, _FLOAT32_EPS))
    return energies.astype(np.float32)


def apply_cmn(features: np.ndarray) -> np.ndarray:
    """Per-utterance mean normalization without variance normalization."""
    return (features - features.mean(axis=0, keepdims=True)).astype(np.float32)


def extract_features(pcm: bytes, params: FbankParams = WESPEAKER_FBANK_PARAMS) -> np.ndarray:
    """PCM (audio contract) -> normalized fbank features, shape (frames, num_mel_bins)."""
    return apply_cmn(kaldi_fbank(pcm_s16le_to_array(pcm), params))
