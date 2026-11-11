# Changelog

## 0.1.1

- Public product name changed to **BehavesWell Voice Evidence** (formerly HTBW Voice Evidence;
  DL-154, issue #216). The App name and description are updated.
- Metadata only. No runtime, storage, slug, key-derivation, Voiceprint, retention, comparison, or
  discovery change. Existing Voiceprints and retained recordings remain in place.

## 0.1.0

- Initial Phase 2 runtime foundation (issue #162).
- Home Assistant App packaging on the official Debian base image (glibc, for onnxruntime).
- Bearer authentication with an App-generated secret, provisioned to HTBW via Supervisor
  discovery; rotation through `hassio.app_stdin` (`rotate-secret`).
- Contract A v1.0: `GET /v1/status` and `GET /v1/health`.
- Pinned WeSpeaker ECAPA-TDNN512-LM ONNX model: revision-pinned download, SHA-256
  verification before activation and on every load, no fallback, no auto-update.
- NumPy Kaldi-compatible 80-bin log-mel filterbank with per-utterance mean normalization.
- App-owned storage, retention reconciliation, enrollment deletion and encoder migration
  mechanics (no public enrollment or comparison API).
- Encoder migration (rebuild/remove) runs only under an HTBW-issued household
  `migration_authorization` for the active `compatibility_id`; without it, mismatched
  Voiceprints are kept and marked incompatible (`migration_not_authorized`). Startup never
  migrates; the authorization transport is later-phase scope.
