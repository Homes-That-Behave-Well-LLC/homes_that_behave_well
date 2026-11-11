"""Governed constants for the BehavesWell Voice Evidence App (formerly HTBW Voice Evidence)."""

from __future__ import annotations

from typing import Final

APP_VERSION: Final = "0.1.1"
CONTRACT_VERSION: Final = "1.0"

DEFAULT_PORT: Final = 8099
DEFAULT_DATA_DIR: Final = "/data"
SUPERVISOR_URL: Final = "http://supervisor"

# Discovery domain of the HTBW Home Assistant integration.
DISCOVERY_SERVICE: Final = "htbw"

# Governed enrollment workflow cardinality (not a quality threshold).
ENROLLMENT_RECORDING_COUNT: Final = 10

# Audio contract: signed 16-bit little-endian PCM, 16 kHz, mono.
AUDIO_CONTRACT_VERSION: Final = "pcm_s16le_16000hz_mono.v1"
AUDIO_SAMPLE_RATE_HZ: Final = 16000
AUDIO_SAMPLE_WIDTH_BYTES: Final = 2
AUDIO_CHANNELS: Final = 1

# Initial governed encoder: WeSpeaker ECAPA-TDNN512-LM (ONNX), pinned by revision and digest.
MODEL_ID: Final = "Wespeaker/wespeaker-ecapa-tdnn512-LM"
MODEL_FILENAME: Final = "voxceleb_ECAPA512_LM.onnx"
MODEL_REVISION: Final = "a2f3dcb1c8702caccc7a55ceb57f5e8d1842112b"
MODEL_SHA256: Final = "d71b85d9b48058ef68004f04f1b78acebefb9dfcf542e19b976a12a5ad1f10b0"
MODEL_SIZE_BYTES: Final = 24861931
MODEL_URL: Final = f"https://huggingface.co/{MODEL_ID}/resolve/{MODEL_REVISION}/{MODEL_FILENAME}"
# Hard cap for the download, comfortably above the pinned size.
MODEL_MAX_DOWNLOAD_BYTES: Final = 64 * 1024 * 1024
MODEL_LICENSE: Final = "CC-BY-4.0"

ENCODER_FAMILY: Final = "wespeaker_ecapa_tdnn512_lm"
ENCODER_VERSION: Final = f"voxceleb_ECAPA512_LM@{MODEL_REVISION[:12]}"
EMBEDDING_DIM: Final = 192

# Bounded timeouts (seconds) for every outbound call.
SUPERVISOR_TIMEOUT_S: Final = 10.0
MODEL_DOWNLOAD_TIMEOUT_S: Final = 300.0
MODEL_DOWNLOAD_CONNECT_TIMEOUT_S: Final = 15.0
MODEL_DOWNLOAD_READ_TIMEOUT_S: Final = 60.0
OPTIONS_POLL_INTERVAL_S: Final = 30.0

# Contract A reason codes.
REASON_STORAGE_UNAVAILABLE: Final = "storage_unavailable"
REASON_MODEL_MISSING: Final = "model_missing"
REASON_MODEL_DOWNLOADING: Final = "model_downloading"
REASON_MODEL_DOWNLOAD_FAILED: Final = "model_download_failed"
REASON_MODEL_DIGEST_MISMATCH: Final = "model_digest_mismatch"
REASON_ENCODER_LOAD_FAILED: Final = "encoder_load_failed"
REASON_ENCODER_CONTRACT_MISMATCH: Final = "encoder_contract_mismatch"
REASON_STARTING: Final = "starting"
