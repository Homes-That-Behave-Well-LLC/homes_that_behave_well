"""Real-model smoke test (opt-in): pinned download, digest check, fbank + ONNX inference.

Run with ``HTBW_VE_MODEL_CACHE=/some/cache/dir pytest -m real_model``. The cache directory
must be outside the repository. Input is 1 s of synthetic noise.
"""

from __future__ import annotations

import os
from pathlib import Path

import numpy as np
import pytest

from htbw_voice_evidence.const import EMBEDDING_DIM
from htbw_voice_evidence.encoder import OnnxSpeakerEncoder, governed_identity
from htbw_voice_evidence.model_artifact import (
    GOVERNED_MODEL_PIN,
    AiohttpDownloader,
    ModelArtifactManager,
    ModelState,
)

CACHE_ENV = "HTBW_VE_MODEL_CACHE"

pytestmark = [
    pytest.mark.real_model,
    pytest.mark.skipif(not os.environ.get(CACHE_ENV), reason=f"{CACHE_ENV} not set"),
]


async def test_pinned_model_downloads_verifies_and_embeds() -> None:
    cache = Path(os.environ[CACHE_ENV]) / "models"
    manager = ModelArtifactManager(cache, GOVERNED_MODEL_PIN, AiohttpDownloader())
    assert await manager.ensure() is ModelState.VALID
    model_bytes = manager.read_verified()
    assert len(model_bytes) == GOVERNED_MODEL_PIN.size_bytes

    encoder = OnnxSpeakerEncoder(model_bytes, governed_identity())
    rng = np.random.default_rng(1234)
    noise = (rng.standard_normal(16000) * 0.1 * 32767).clip(-32768, 32767).astype("<i2")
    embedding = encoder.embed(noise.tobytes())

    assert embedding.ndim == 1
    assert embedding.shape == (EMBEDDING_DIM,)
    assert np.all(np.isfinite(embedding))
    assert float(np.linalg.norm(embedding)) > 0.0
    print(
        f"real_model ok: input={encoder.input_name} output={encoder.output_name} "
        f"dim={embedding.shape[0]} compatibility_id={encoder.identity.compatibility_id}"
    )
