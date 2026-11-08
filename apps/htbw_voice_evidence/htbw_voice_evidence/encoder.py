"""Encoder adapter interface, compatibility identity, and the WeSpeaker ONNX encoder.

Contracts depend only on :class:`Encoder` and :class:`EncoderIdentity`; nothing outside
this module knows WeSpeaker or ONNX specifics.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from typing import Any, Protocol, runtime_checkable

import numpy as np

from .const import (
    AUDIO_CONTRACT_VERSION,
    ENCODER_FAMILY,
    ENCODER_VERSION,
    MODEL_SHA256,
)
from .features import WESPEAKER_FBANK_PARAMS, FbankParams, extract_features

COMPATIBILITY_ID_PREFIX = "vecid1-"


class EncoderError(Exception):
    """Base class for encoder failures."""


class EncoderLoadError(EncoderError):
    """The encoder could not be constructed from its artifact."""


class EncoderContractMismatchError(EncoderLoadError):
    """The artifact does not match the governed feature/embedding contract."""


class EncoderInputError(EncoderError):
    """The audio could not be embedded (contract violation or too short)."""


@dataclass(frozen=True)
class EncoderIdentity:
    encoder_family: str
    encoder_version: str
    model_sha256: str
    audio_contract_version: str
    feature_params: dict[str, Any] = field(default_factory=dict)

    @property
    def compatibility_id(self) -> str:
        """Stable identity that changes whenever any compatibility-relevant field changes."""
        canonical = json.dumps(
            {
                "audio_contract_version": self.audio_contract_version,
                "encoder_family": self.encoder_family,
                "encoder_version": self.encoder_version,
                "feature_params": self.feature_params,
                "model_sha256": self.model_sha256,
            },
            sort_keys=True,
            separators=(",", ":"),
        )
        return COMPATIBILITY_ID_PREFIX + hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:32]


def governed_identity(
    model_sha256: str = MODEL_SHA256, params: FbankParams = WESPEAKER_FBANK_PARAMS
) -> EncoderIdentity:
    return EncoderIdentity(
        encoder_family=ENCODER_FAMILY,
        encoder_version=ENCODER_VERSION,
        model_sha256=model_sha256,
        audio_contract_version=AUDIO_CONTRACT_VERSION,
        feature_params=params.as_dict(),
    )


@runtime_checkable
class Encoder(Protocol):
    """Adapter: PCM (audio contract) -> 1-D speaker embedding."""

    @property
    def identity(self) -> EncoderIdentity: ...

    def embed(self, pcm: bytes) -> np.ndarray: ...


def validate_embedding(vector: Any, expected_dim: int | None = None) -> np.ndarray:
    array = np.asarray(vector, dtype=np.float32)
    if array.ndim != 1 or array.size == 0:
        raise EncoderError("embedding must be a non-empty 1-D vector")
    if expected_dim is not None and array.shape[0] != expected_dim:
        raise EncoderError("embedding has an unexpected dimension")
    if not np.all(np.isfinite(array)):
        raise EncoderError("embedding contains non-finite values")
    return array


class OnnxSpeakerEncoder:
    """WeSpeaker ONNX speaker encoder; I/O names and shapes are read from the session."""

    def __init__(
        self,
        model_bytes: bytes,
        identity: EncoderIdentity,
        params: FbankParams = WESPEAKER_FBANK_PARAMS,
        intra_op_threads: int = 1,
    ) -> None:
        try:
            import onnxruntime as ort
        except ImportError as err:  # pragma: no cover - dependency is pinned
            raise EncoderLoadError("onnxruntime is not available") from err
        self._identity = identity
        self._params = params
        try:
            options = ort.SessionOptions()
            options.intra_op_num_threads = intra_op_threads
            options.inter_op_num_threads = 1
            self._session = ort.InferenceSession(
                model_bytes, sess_options=options, providers=["CPUExecutionProvider"]
            )
        except Exception as err:
            raise EncoderLoadError("ONNX session could not be created") from err
        inputs = self._session.get_inputs()
        outputs = self._session.get_outputs()
        if len(inputs) != 1 or len(outputs) < 1:
            raise EncoderContractMismatchError("unexpected ONNX input/output arity")
        self._input_name = inputs[0].name
        self._output_name = outputs[0].name
        in_shape = list(inputs[0].shape)
        if len(in_shape) != 3:
            raise EncoderContractMismatchError("ONNX input must be [batch, frames, features]")
        feat_dim = in_shape[2]
        if isinstance(feat_dim, int) and feat_dim != params.num_mel_bins:
            raise EncoderContractMismatchError("ONNX feature dimension mismatch")
        out_shape = list(outputs[0].shape)
        self._embedding_dim = (
            out_shape[-1] if out_shape and isinstance(out_shape[-1], int) else None
        )

    @property
    def identity(self) -> EncoderIdentity:
        return self._identity

    @property
    def embedding_dim(self) -> int | None:
        return self._embedding_dim

    @property
    def input_name(self) -> str:
        return self._input_name

    @property
    def output_name(self) -> str:
        return self._output_name

    def embed(self, pcm: bytes) -> np.ndarray:
        try:
            feats = extract_features(pcm, self._params)
        except ValueError as err:
            raise EncoderInputError(str(err)) from err
        try:
            result = self._session.run([self._output_name], {self._input_name: feats[None, :, :]})
        except Exception as err:
            raise EncoderInputError("encoder inference failed") from err
        return validate_embedding(np.asarray(result[0]).reshape(-1), self._embedding_dim)
