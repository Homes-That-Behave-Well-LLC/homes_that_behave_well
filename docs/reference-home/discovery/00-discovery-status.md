> **Document status: Operational — discovery artifact.** Not architecture-of-record. Creates no authority. Does not amend `decision-ledger.md`, `authority-order.md`, or any canonical model/contract.

# Discovery Status — HTBW Reference Home

**Date:** 2026-10-07
**Repository reviewed:** `homes_that_behave_well` (identified as the active development repository — its `docs/` tree already contains `architecture/`, `contracts/`, `governance/`, `models/`, matching this task's vocabulary; its canonical `home-assistant-boundary.md`, `framework.md`, and `principles.md` were used as the HTBW Framework reference for categorization in this discovery pass).

## P: accessibility

**P: was accessible and read-only access was maintained throughout.** `P:\` resolved directly to a live Home Assistant configuration directory (not a nested subfolder) — confirmed by the simultaneous presence of `configuration.yaml`, `.storage/`, `home-assistant_v2.db`, `secrets.yaml`, `automations.yaml`, `scripts.yaml`, `scenes.yaml`, `custom_components/`, `blueprints/`, `www/`, and `.HA_VERSION`-equivalent version evidence at the drive root.

## Identified production root

`P:\` **is** the Home Assistant configuration root. Home Assistant Core version **2026.9.4** (read from `.storage/core.config`/environment; note this is one release behind the `homes_that_behave_well` repository's most recent reviewed release, 2026.10 — see Evidence Register item for this gap).

## Read-only boundary maintained

- **No file on P: was created, modified, renamed, moved, or deleted.** Every production read used the `read_file`/`list_dir` tools (no write calls) or a Python script invoked with `open(path, "r", ...)` (explicit read mode) executed from the local development venv — never from a process running against or writing to P:.
- All intermediate analysis (registry parsing, counting, redaction) was written to a **local scratch path** (`C:\ha_tmp\discovery\`), never to P: and never to the repository until reviewed.
- Final artifacts are written **only** under `docs/reference-home/discovery/` in this repository, per instruction.
- **No Home Assistant service, automation, script, add-on, container, API write endpoint, or administrative interface was invoked.** Only static files under `.storage/`, `automations.yaml`, `scripts.yaml`, `scenes.yaml`, `templates.yaml`, `configuration.yaml`, `watchman_report.txt`, and `custom_components/asset_intelligence/manifest.json` were read.
- **`secrets.yaml` was not opened.** Its existence is recorded; no value was read or reproduced.
- **`nexia_config_*.conf` and `trane_config_*.conf` files were not opened** (filenames alone indicate they hold account/cloud credentials for the Nexia/Trane thermostat integration); their existence and inferred purpose are recorded, not their content.
- **`home-assistant_v2.db` (Recorder SQLite database) was not opened.** No approved read-only discovery method for it exists yet in this repository, per the governing instruction ("databases must not be opened unless the repository already contains an explicitly approved read-only discovery method").
- **Camera images/recordings, audio recordings, household message content, and presence-history detail were not accessed or used to infer routines.** Device-tracker and presence-related counts are reported in aggregate only.
- Device **MAC addresses, connections arrays, unique_id strings containing network identifiers, IP addresses, and precise zone coordinates (latitude/longitude) were deliberately excluded** from every extraction script — they were never pulled into any intermediate file.
- Two resident first names appear in area names, mobile-device titles, and automation aliases (observed directly in `.storage/core.area_registry`, `.storage/core.config_entries`, and `automations.yaml`). They are **redacted to "Resident 1 (Primary)" / "Resident 2"** in every publication-facing artifact in this set. The evidence register notes where this redaction was applied.

## Evidence sources used

| Source | Method | Content read |
|---|---|---|
| `P:\.storage\core.config_entries` | Python, read-only JSON parse | 169 integration/config-entry records |
| `P:\.storage\core.device_registry` | Python, read-only JSON parse | 2,528 device records (manufacturer/model/area/disabled only — no connections/identifiers extracted) |
| `P:\.storage\core.entity_registry` | Python, read-only JSON parse | 8,548 entity records (domain/platform/disabled/hidden counts only) |
| `P:\.storage\core.area_registry` | Python, read-only JSON parse | 23 areas |
| `P:\.storage\core.floor_registry` | Python, read-only JSON parse | 3 floors |
| `P:\.storage\core.label_registry` | Python, read-only JSON parse | 39 labels |
| `P:\.storage\core.config` | Python, read-only JSON parse | Time zone, country, currency only (no coordinates) |
| `P:\.storage\person` | Python, read-only JSON parse | 7 person records — names redacted, only presence of device trackers recorded |
| `P:\.storage\zone` | Python, read-only JSON parse | 40 zone records — names and radius only, coordinates excluded |
| `P:\automations.yaml` | Python, read-only YAML parse | 84 automations — alias, mode, trigger-platform only |
| `P:\scripts.yaml` | Python, read-only YAML parse | 50 scripts — key/alias only |
| `P:\scenes.yaml` | Direct read | 3 bytes — effectively empty; HA-native scenes are not the household's scene mechanism |
| `P:\templates.yaml` | Direct read | 1 template helper (music-genre-to-URI map) |
| `P:\configuration.yaml` | Direct read | Top-level include structure only |
| `P:\watchman_report.txt` | Direct read (partial) | Self-diagnostic report the household already runs (Watchman integration) — used as evidence of known-missing/unavailable entities |
| `P:\custom_components\` (directory listing) | `list_dir` | Names of 27 custom integrations present |
| `P:\custom_components\asset_intelligence\manifest.json` | Direct read | Confirms Asset Intelligence v1.0.12 deployed in this production home |
| `P:\.HA_VERSION` equivalent | Derived from `core.config` | Core 2026.9.4 |

## Inaccessible or deliberately not accessed

- `secrets.yaml` — exists, not opened (per instruction).
- `nexia_config_*.conf`, `trane_config_*.conf` — exist, not opened (credential files).
- `home-assistant_v2.db` (+ `-shm`/`-wal`) — not opened (no approved read-only method).
- `.storage/auth*`, `.storage/http.auth` — not opened (authentication/session material).
- Router/firewall/switch administrative interfaces, UniFi controller administrative UI, ADT Pulse portal, physical network topology — **not observable from P: at all**; everything about physical network infrastructure in this discovery is **INFERRED** from Home Assistant integration evidence (UniFi/UniFi Protect/UniFi Access config entries and device counts), never OBSERVED directly. This is the single largest evidence gap in the set (see Phase F, Network and Infrastructure Inventory).
- Camera/doorbell image and video content — not accessed.
- Exact device MAC addresses, IP addresses, and precise person/zone coordinates — present in the raw registries but **deliberately never extracted** by the analysis scripts.

## Discovery limitations

- This is a **snapshot of configuration and registry metadata**, not a live state capture. No entity *state* (current sensor readings, lock status, etc.) was read; only registry/definition-level metadata (what exists, how it's named, how it's categorized).
- Automation/script **logic detail** (the exact conditions and actions inside each of the 84 automations and 50 scripts) was not individually transcribed into these artifacts — only alias, mode, and trigger-platform were extracted, plus pattern-level grouping. A full line-by-line automation transcription was judged out of proportion to this discovery pass and is recorded as **OWNER INPUT / FUTURE DISCOVERY** where relevant.
- Device registry **"manufacturer: UNKNOWN"** accounts for 2,063 of 2,528 devices (82%) — this is normal for Home Assistant: virtual/service devices (automations, scripts, scenes, zones, persons, groups, helpers, integrations without a declared physical manufacturer) are registered as devices without a manufacturer field. This is **not** a data-quality problem; it is correctly reported as such in the Integration/Device catalogs.
- Network topology, server/compute inventory, and physical cabling are **not derivable from Home Assistant alone** and are marked `UNKNOWN` or `INFERRED` throughout, never presented as observed.

## Completion status

**Phase 1–7 discovery completed** against the evidence available. All 19 required markdown files, the JSON architecture model, and the 4 CSV catalogs were produced. **No production change was made.** Narrative, historical, and preference-based content required for the article series (construction history, product-selection rationale, personal anecdotes) is **not determinable from production or repository evidence** and is isolated in `11-owner-input-required.md`.
