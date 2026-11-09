# HTBW Voice Evidence

> **Development runtime only.** The Voice Evidence App is currently being used to validate the HTBW
> Voice Evidence architecture and is not ready for household enrollment or production biometric use.

The HTBW Voice Evidence App is the local voice-evidence runtime of Homes That Behave Well
(HTBW). It runs next to Home Assistant, managed by the Supervisor, and is used only by the
HTBW integration.

## What it does

The App has two biometric responsibilities:

1. creating and managing **Voiceprints** (one per household person), and
2. comparing voice against every enrolled Voiceprint, producing ordinal Match Levels.

Version 0.1.0 is the **runtime foundation** only. It installs, secures itself, connects to
HTBW, acquires and verifies its speaker-embedding model, and manages its own storage.
Enrollment, comparison and Match Levels are **not** available to the household yet; the
App reports its health to HTBW and nothing more.

The App does not resolve who a person is, does not compute identity confidence, and does
not make trust decisions. Those stay in HTBW.

## Installation

1. Add this repository to Home Assistant: **Settings** > **Apps** > **Install app** >
   menu > **Repositories**, then enter the repository URL.
2. Install **HTBW Voice Evidence** and start it.
3. Home Assistant discovers the App for the HTBW integration. Confirm it under
   **Settings** > **Devices & services**.

On first start the App downloads its model (about 25 MB) once. Until the download has
been verified, HTBW shows the App as unavailable.

## Settings are managed by HTBW

The App has one option, **Retain enrollment recordings**. It is **managed by HTBW**: set it
in the HTBW Household configuration. HTBW copies the value into the App, and any change
made directly on the App's Configuration tab is overwritten.

- **No** (default): after a Voiceprint is created, the ten enrollment recordings are
  deleted. The Voiceprint is kept.
- **Yes**: the ten recordings are kept with the Voiceprint, so the Voiceprint can be
  rebuilt when the speaker model is upgraded and the household has authorized the
  migration.
- Changing **Yes** to **No** deletes all kept recordings. Voiceprints are kept.

The setting never deletes a Voiceprint.

## Speaker model changes

When a new speaker model makes existing Voiceprints incompatible, the App does **not**
rebuild or remove anything on its own. Each affected Voiceprint is kept but reported to
HTBW as incompatible (`migration_not_authorized`) and is never used. Only after the
household administrator acknowledges the change in HTBW, and HTBW authorizes the migration
for the new model, does the App rebuild Voiceprints from kept recordings. A person without
kept recordings then has their old Voiceprint removed and needs to enroll again. If a
rebuild fails, the old Voiceprint stays (marked incompatible) and the failure is reported.
Version 0.1.0 has no way to receive that authorization yet, so incompatible Voiceprints
simply stay incompatible.

## Security

- The App's API is reachable only on Home Assistant's internal network; it publishes no
  port on the host.
- The App creates a random API secret on first start, keeps it in its private storage,
  and hands it to HTBW through Home Assistant discovery. Every request must present it.
- To rotate the secret, call the `hassio.app_stdin` action with `input: "rotate-secret"`
  for this App. The old secret stops working immediately and HTBW receives the new one
  through discovery.
- The App asks for no Home Assistant or Supervisor API permissions beyond its own
  information and discovery, no host network, no privileged access, and does not map the
  Home Assistant configuration folder.

Outside the Supervisor (for development) discovery is skipped; HTBW must then be given the
host, port and secret manually.

## Privacy (local only, DL-120)

All voice processing happens on this Home Assistant host. Recordings, Voiceprints and
embeddings are stored only in the App's private data folder and never leave the App. The
App contacts the internet only to download its pinned model file from Hugging Face; it
never uploads anything. Logs never contain the API secret, audio, embeddings, or person
identifiers in file paths.

Home Assistant backups include the App's private data folder, so they contain Voiceprints
(and kept recordings, if retention is on). Treat backups accordingly.

## Model licence and attribution

The App uses the speaker-embedding model `voxceleb_ECAPA512_LM.onnx` from the
[WeSpeaker](https://github.com/wenet-e2e/wespeaker) project
([`Wespeaker/wespeaker-ecapa-tdnn512-LM`](https://huggingface.co/Wespeaker/wespeaker-ecapa-tdnn512-LM),
revision `a2f3dcb1c8702caccc7a55ceb57f5e8d1842112b`), licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). It is used unmodified and is
downloaded at runtime, not shipped with the App. Details are in `MODEL_LICENSE.md`.

## Status reasons

When HTBW shows the App as unavailable, the reason is one of:

| Reason | Meaning |
| --- | --- |
| `model_downloading` | The model is being downloaded. |
| `model_download_failed` | The download failed; the App retries periodically. |
| `model_digest_mismatch` | The model file does not match the pinned digest; it is not used. |
| `model_missing` | No model file is present. |
| `encoder_load_failed` | The verified model could not be loaded. |
| `encoder_contract_mismatch` | The model does not fit the governed feature contract (reported as incompatible). |
| `storage_unavailable` | The App's private storage cannot be used. |
| `starting` | The App is still starting. |
