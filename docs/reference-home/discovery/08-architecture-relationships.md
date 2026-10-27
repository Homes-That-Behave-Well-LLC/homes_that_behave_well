> **Document status: Operational — discovery artifact.** Not architecture-of-record.

# Architecture Relationships

Full machine-readable relationship graph: `reference-home-architecture.json`. This document describes the model's structure and gives representative examples of each required relationship type; it does not reproduce every one of the hundreds of possible edges.

## The 12 layers (as specified)

1. **People and household context** — 7 persons (redacted), household composed of at least 2 named residents plus additional profiles (guests/other household members — not further itemized).
2. **Household experiences** — derived from the 24 capability categories in `04-capability-catalog.md`.
3. **HTBW Framework responsibilities** — Foundation, Stewardship, Identity, Truth, Continuity, Operational Trust, Concierge (per `homes_that_behave_well/docs/architecture/framework.md`) — used only as a **comparison lens** in this discovery; no production evidence claims to *implement* these responsibilities.
4. **Home Assistant as controller/hub/platform** — Core 2026.9.4, Supervisor-managed, the single convergence point for every layer below.
5. **Capability domains** — the 24 categories in `04-capability-catalog.md`.
6. **Home Assistant integrations** — the 78 domains in `03-integration-catalog.md`.
7. **Protocols and communication methods** — Zigbee (inferred, Aqara), Z-Wave, Matter, Thread, Bluetooth (passive+remote), MQTT, Wyoming (voice), HTTP/REST (`rest_command`), cloud vendor APIs (Nexia, ADT, Tesla, MS365, iCloud, OpenAI).
8. **Controllers, hubs, gateways, bridges** — PowerView Hub, Insteon hub/PLM (inferred), Z-Wave JS controller, Matter controller, Thread border router, MQTT broker, UniFi controller (inferred), 22 ESPHome nodes.
9. **Network and compute foundation** — UniFi network (inferred topology only), Data Closet area, Home Assistant host (platform unknown).
10. **Physical devices and equipment** — per `05-technology-and-device-catalog.md`.
11. **External or cloud services** — Home Assistant Cloud, Nexia, ADT Pulse, Tesla, MS365, iCloud, OpenAI, Xbox Live, PlayStation Network, AccuWeather, Smart Meter Texas, B-hyve, Miele, Oral-B, Meater, Google Assistant, Alexa.
12. **Resilience, governance, explainability** — Backup, Watchman, UPS, HACS/Analytics, and (as a comparison lens only) HTBW's Decision Trace/Explainability concepts.

## Representative relationships (full set in JSON)

| Source | Relationship | Destination | Direction | Posture | Criticality | Evidence |
|---|---|---|---|---|---|---|
| Home Assistant Core | CONTROLS | Insteon lighting devices | → | Local | CRITICAL | config_entries, device_registry |
| Home Assistant Core | INTEGRATES_WITH | UniFi Network | → | Local | FOUNDATIONAL | config_entries |
| UniFi Network | PROVIDES | device_tracker entities (presence) | → | Local | IMPORTANT | entity_registry (4,861 unifi-platform entities) |
| Wyoming (Whisper/Piper/openWakeWord) | COMMUNICATES_USING | local voice pipeline | ↔ | Local | CRITICAL | config_entries |
| "Concierge – Voice Entry (HA Voice)" automation | DEPENDS_ON | `conversation` trigger platform | → | Local/Hybrid | IMPORTANT | automations.yaml |
| OpenAI conversation agent | PROVIDES | reasoning for voice automations | → | Cloud | IMPORTANT | config_entries |
| Moisture sensors | SENSES | leak conditions (6 locations) | → | Local | CRITICAL | automations.yaml |
| Leak-detection automations | NOTIFIES | household (via mobile_app) | → | Hybrid | CRITICAL | automations.yaml (inferred action; notify service not individually transcribed) |
| Primary Bedroom Alarm Started | GOVERNS | Alarm Repeat → Escalation → Stop chain | → | Local | CRITICAL | automations.yaml |
| Hunter Douglas PowerView Hub | ACTUATES | 20 shade devices | → | Local | CRITICAL | device_registry |
| Nexia (cloud) | REQUIRES_CLOUD | Trane thermostat control | → | Cloud | CRITICAL | config_entries |
| Home Assistant Cloud | REQUIRES_CLOUD | remote access / optional voice convenience | → | Cloud | OPTIONAL (per Home Assistant's own documented design) | config_entries |
| Insteon lighting | FALLS_BACK_TO | physical switch (Insteon native capability) | — | Local | — | INFERRED, not independently verified |
| UPS (CyberPower) | PROTECTS | Home Assistant host power | → | Local | IMPORTANT | device_registry |
| Watchman | EXPLAINS | missing/unavailable entity references | → | Local | IMPORTANT | watchman_report.txt |
| Backup integration | STORES | configuration snapshots | → | Local/Hybrid | CRITICAL | config_entries (destination unverified) |
| Asset Intelligence | GOVERNS | asset records (HTBW-aligned, not core HA) | → | Local | IMPORTANT | manifest.json |

Every row above and the full remaining set carry a `publication_safety` field in the JSON (`PUBLIC`, `PUBLIC AFTER GENERALIZATION`, `INTERNAL ONLY`, or `DO NOT PUBLISH`) — no relationship involving a resident's name, device MAC, IP, or coordinate is marked `PUBLIC` as-is.
