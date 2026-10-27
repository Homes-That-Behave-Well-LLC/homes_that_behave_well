> **Document status: Operational — discovery artifact.** Not architecture-of-record.

# Executive Architecture Summary — HTBW Reference Home

## Architectural overview

The Reference Home is a mature, continuously-evolving Home Assistant installation (Core **2026.9.4**) with **169 integration config entries** across **78 integration domains**, **2,528 registered devices**, and **8,548 registered entities**, spread across **23 areas** on **3 floors** (First Floor, Second Floor, Outside). Home Assistant is observably the **controller, hub, and home operating platform** — it is the single point where lighting (Insteon), shades (Hunter Douglas PowerView), audio (Sonos, Music Assistant), climate (Trane via Nexia), irrigation (Orbit B-hyve), security (ADT Pulse), cameras (UniFi Protect), network (UniFi), voice (Wyoming: openWakeWord/Piper/Whisper, plus OpenAI conversation/TTS), and a custom-built native-automation "Concierge" voice layer all converge.

**HTBW's own Asset Intelligence product (v1.0.12) is deployed in this production home**, confirming it is not merely a standalone product but a lived-in reference deployment. Neither the Voice Identity nor Concierge HTBW *integrations* are present in `custom_components/` — the "Concierge" automations observed (`Concierge – Voice Entry (HA Voice)`, `Good Morning (Concierge)`, etc.) are a **household-native naming convention built from plain Home Assistant automations and scripts**, not the HTBW Concierge responsibility's own integration. This distinction must be preserved in all publication material.

## Major platforms

- **Home Assistant Core 2026.9.4**, Supervisor-managed (`hassio` config entry present), with Home Assistant Cloud (Nabu Casa) active.
- **HACS** installed, managing at least 27 custom integrations.
- **Network/security platform:** Ubiquiti UniFi (network), UniFi Protect (cameras/NVR), UniFi Access (door access) — observed as config entries, not yet corroborated by direct network-equipment inspection (INFERRED topology).
- **Lighting/whole-home control backbone:** Insteon (SmartLabs, Inc. — 67 devices), consistent with owner-provided lineage from the X10 era.
- **Voice platform:** Wyoming protocol apps (openWakeWord, Piper, Whisper) plus OpenAI (`openai_conversation`, `extended_openai_conversation`, `openai_tts`) and `assist_satellite` entities (13) — a hybrid local/cloud voice stack.

## Household capabilities observed (high level)

Lighting and shading, whole-home audio, voice interaction and a custom "Concierge" voice-command layer, climate control, irrigation (6+ moisture-gated zones), leak/flood detection (6 locations), security/alarm (ADT) with an escalating Primary-Bedroom alarm automation chain, camera/observation (UniFi Protect, Reolink discovery, AI-assisted `llmvision`), kiosk-tablet dashboards (5 `fully_kiosk` devices, 15 Lovelace dashboards), presence/occupancy (BLE via Bermuda/iBeacon/private BLE, plus UniFi network-presence at very large scale), calendar/mail/todo via Microsoft 365 and iCloud, media/entertainment (Xbox, PlayStation Network, Apple TV, LG/Samsung/WebOS TVs), energy/utility awareness (Smart Meter Texas, CyberPower UPS, Home Assistant Energy dashboard), asset stewardship (Asset Intelligence), and administrative self-monitoring (Watchman, HACS, Backup, Analytics, GitHub update tracking).

## Architectural posture

- **Local-first where it matters most, cloud-assisted by explicit choice elsewhere.** Core control (lighting, shades, locks, climate relay) runs through local integrations; voice processing is a documented local/cloud hybrid (Wyoming local STT/TTS alongside OpenAI cloud conversation); several conveniences (MS365, iCloud, Alexa Media, gaming platforms, Nexia/Trane cloud API) are explicitly cloud-dependent by the nature of the vendor's own service.
- **Household-native governance layer already exists, informally.** The "Concierge" and "VA:" (Voice Assistant) automation families show the household independently building toward several HTBW-Concierge-shaped concepts (voice entry, follow-up commands, intentional learning, identity self-query, room monitoring awareness) entirely in native Home Assistant automations, years before (or independent of) HTBW's own Concierge responsibility design. This is a **rich source of "patterns already proven in production"** evidence for the article series, but it is **not** evidence of the HTBW integration itself (none is installed).
- **Self-monitoring discipline is unusually strong for a household deployment.** Watchman, HACS, Backup, and Analytics are all active — the household already treats its smart home as infrastructure requiring observability, not merely a collection of conveniences.

## Strengths (evidence-based)

- Broad integration depth across almost every capability category the HTBW Framework recognizes.
- Demonstrable escalation-ladder pattern already in production (Primary Bedroom alarm: Started → Repeat → Escalation → Stop) — directly comparable to Operational Trust's accepted escalation concepts.
- Demonstrable "learn on use" pattern already in production (`Lighting Profile – Learn on Use`, `Learn Music Volume – On Sonos Change`) — directly comparable to Continuity's accepted room/person-scoped learned-value concepts.
- Demonstrable moisture/leak-safety pattern across 6 locations, independent of irrigation moisture-gating — a strong "Safety" category case study.
- Self-diagnostic discipline (Watchman) already surfaces real evidence gaps (missing doorbell entities, stale soil-moisture sensors, a vanished PowerView scene) — useful, honest "what currently doesn't work" material for the article series' "lessons learned" sections.

## Constraints and evidence gaps (evidence-based, not assumed)

- **Network/infrastructure physical layout is not observable from Home Assistant.** Router/firewall model, switch placement, access-point count/placement, VLAN design, and wiring are all `UNKNOWN` pending owner input or a separately-approved discovery method.
- **82% of registered "devices" carry no manufacturer** (virtual/service devices — automations, scripts, helpers, zones, persons) — expected, not a defect, but it means device-family counts in this report are drawn from the **18%** of devices that do carry manufacturer metadata plus the integration/domain evidence, not from the full 2,528.
- **Production is one Home Assistant release behind** the `homes_that_behave_well` repository's most recently reviewed release (production: 2026.9.4; repository's most recent HA review: 2026.10, per Issue #184). Any 2026.10-specific feature (new map, MCP server/client, trigger-ID UI, profile-page redesign) is **not yet observable in this production evidence** and must not be assumed present.
- **Household construction history, product-selection rationale, and personal narrative are not in any file on P: or in the repository** — isolated entirely to `11-owner-input-required.md`.

## Evidence confidence

High confidence for everything derived directly from `.storage` registries and YAML configuration (integration list, device/entity counts, areas/floors, automation/script names and trigger patterns, Asset Intelligence version). Low-to-unknown confidence for anything about physical network topology, exact device models inferred only from entity naming, and all narrative/historical material — each is labeled accordingly throughout this artifact set.
