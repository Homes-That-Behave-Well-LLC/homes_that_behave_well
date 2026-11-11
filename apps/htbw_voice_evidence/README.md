# BehavesWell Voice Evidence (Home Assistant App)

> **Development runtime only.** Not ready for household enrollment or production biometric use. See
> [DOCS.md](DOCS.md).

**BehavesWell Voice Evidence** (formerly HTBW Voice Evidence; DL-154) is an independent,
environment-neutral, local voice-evidence runtime. It creates and manages Voiceprints and compares a
voice sample against every eligible Voiceprint, returning ordinal Match Levels. It never resolves who
is speaking; BehavesWell Core Identity does that. Packaged as the **BehavesWell Voice Evidence App**, it
runs as a Home Assistant App (formerly add-on) and currently serves one consumer: BehavesWell Core, Home
Assistant Edition (integration domain `htbw`). Technical identifiers are unchanged: slug, directory and
package `htbw_voice_evidence`, distribution `htbw-voice-evidence`, `HTBW_VE_*`, and the key-derivation
domain.

Version 0.1.0 is the Phase 2 runtime foundation (issue #162), and 0.1.1 changes only the displayed
name. The foundation covers: packaging, bearer authentication, Supervisor discovery provisioning,
Contract A status/health, pinned model acquisition and verification, the ONNX speaker encoder,
App-owned storage, and the Voiceprint lifecycle mechanics (retention, deletion, and encoder migration
gated on an HTBW-issued household migration authorization). There is no public enrollment or
comparison API yet, and no Match Level calibration.

Household documentation: [DOCS.md](DOCS.md). Model licence: [MODEL_LICENSE.md](MODEL_LICENSE.md).

## Layout

| Path | Purpose |
| --- | --- |
| `config.yaml`, `Dockerfile`, `rootfs/`, `translations/` | Home Assistant App packaging |
| `htbw_voice_evidence/` | Python runtime package |
| `tests/` | App test suite (synthetic audio only) |
| `requirements.txt` | Pinned runtime dependencies (Debian trixie, Python 3.13) |
| `requirements-test.txt` | Test and lint tooling |

## Contract A (v1.0)

`GET /v1/status` and `GET /v1/health` on port 8099, internal network only. Every route
requires `Authorization: Bearer <api_secret>`; anything else is `401`.

## Development

Run from this folder, with a virtual environment outside the repository using the same
Python minor version as the image (3.13):

```bash
python3.13 -m venv ~/.venvs/htbw-voice-evidence-tests
~/.venvs/htbw-voice-evidence-tests/bin/pip install -r requirements-test.txt
PYTHONDONTWRITEBYTECODE=1 ~/.venvs/htbw-voice-evidence-tests/bin/python -m pytest
~/.venvs/htbw-voice-evidence-tests/bin/ruff check --no-cache .
~/.venvs/htbw-voice-evidence-tests/bin/ruff format --no-cache --check .
```

The real-model smoke test downloads the pinned model into a cache outside the repository:

```bash
HTBW_VE_MODEL_CACHE=~/.cache/htbw-voice-evidence \
  ~/.venvs/htbw-voice-evidence-tests/bin/python -m pytest -m real_model
```

Running the App locally outside the Supervisor:

```bash
HTBW_VE_DATA_DIR=~/.cache/htbw-voice-evidence/data python -m htbw_voice_evidence
```

Environment variables: `HTBW_VE_DATA_DIR` (default `/data`), `HTBW_VE_PORT` (8099),
`HTBW_VE_ADVERTISED_HOST` (container host name), `HTBW_VE_OPTIONS_POLL_INTERVAL_S` (30),
`HTBW_VE_MODEL_RETRY_INTERVAL_S` (600), and `SUPERVISOR_TOKEN` (set by the Supervisor).
