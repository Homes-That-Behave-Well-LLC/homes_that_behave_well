> **Document status: Operational — discovery artifact.** Not architecture-of-record.

# Integration Catalog

**78 integration domains across 169 config entries, observed in `.storage/core.config_entries` and cross-referenced against `.storage/core.device_registry` / `.storage/core.entity_registry`.** Grouped by household-purpose category (Phase 4 categories); machine-readable form in `integration-catalog.csv` and `reference-home-architecture.json`.

Production importance uses: **FOUNDATIONAL / CRITICAL / IMPORTANT / OPTIONAL / HISTORICAL / UNKNOWN.** A high entity count alone never raises a classification — see notes per row.

## Network Foundation

| Integration | Purpose | Local/Cloud | Entities (platform) | Importance | Evidence |
|---|---|---|---|---|---|
| `unifi` | Network controller — switches/APs/clients, powers the overwhelming majority of `device_tracker` entities | Local | 4,861 | **FOUNDATIONAL** — all household connectivity depends on it | config_entries, entity_registry |
| `unifi_access` | Door access control (gate/door hardware) | Local | 44 | **IMPORTANT** | config_entries |
| `unifi_play` | UniFi media-adjacent capability (exact household use not independently verified) | Local | 44 | UNKNOWN | config_entries only |
| `upnp` | UPnP/IGD network discovery | Local | 17 | OPTIONAL | config_entries |

## Home Assistant Platform

| Integration | Purpose | Local/Cloud | Entities | Importance | Evidence |
|---|---|---|---|---|---|
| `hassio` | Supervisor | Local | 130 | **FOUNDATIONAL** | config_entries |
| `cloud` | Home Assistant Cloud (Nabu Casa) — remote access, convenience services | Cloud | 3 | IMPORTANT (voice/remote-access convenience; household functions without it per HA's own "optional" design) | config_entries; cross-referenced against the HTBW repo's own Oct-2026 Cloud→Link finding |
| `hacs` | Community integration/update manager | Local | 100 | **CRITICAL** — 27 custom components depend on it being present to update | config_entries |
| `backup` | Backup | Local | 5 | CRITICAL (resilience) | config_entries |
| `analytics`, `version`, `uptime`, `time_date`, `worldclock` | Platform self-reporting/utility | Local | 1 each | OPTIONAL | config_entries |
| `watchman` | Self-diagnostic: reports missing/unavailable entities referenced in automations | Local | 13 | **IMPORTANT** — the household's own quality-control mechanism | config_entries; `watchman_report.txt` |

## Lighting

| Integration | Purpose | Local/Cloud | Entities | Importance | Evidence |
|---|---|---|---|---|---|
| `insteon` | Whole-home lighting/switch backbone (also some non-lighting loads) | Local | 81 | **FOUNDATIONAL** — 67 Insteon devices, owner-provided lineage since the X10 era | config_entries, device_registry (SmartLabs, Inc.) |
| `switch_as_x` | Re-expose switches as lights/other domains | Local | 10 | OPTIONAL | config_entries |
| `group` | Light/entity groups | Local | 15 | IMPORTANT (used for "turn on daily" family of automations) | config_entries |

## Shades and Natural-Light Management

| Integration | Purpose | Local/Cloud | Entities | Importance | Evidence |
|---|---|---|---|---|---|
| `hunterdouglas_powerview` | Motorized shade control, 8 direction/floor-named automation pairs observed (NE/NW/SE/SW × upstairs/downstairs) | Local | 139 | **CRITICAL** | config_entries, device_registry (20 Hunter Douglas devices), automations.yaml |

## Access

| Integration | Purpose | Local/Cloud | Entities | Importance | Evidence |
|---|---|---|---|---|---|
| `unifi_access` | Gate/door access (see Network Foundation) | Local | 44 | IMPORTANT | config_entries |
| `homekit_controller` | Bridges third-party HomeKit accessories (e.g., a PowerView HomeKit bridge was observed, ignored as a duplicate path) | Local | 128 | OPTIONAL (one accessory explicitly `source: ignore`) | config_entries |

## Security and Alarm

| Integration | Purpose | Local/Cloud | Entities | Importance | Evidence |
|---|---|---|---|---|---|
| `adtpulse` | ADT Pulse alarm panel integration | Cloud (ADT's own portal/API) | 26 | **CRITICAL** | config_entries, device_registry (ADT, 12 devices) |

## Cameras and Observation

| Integration | Purpose | Local/Cloud | Entities | Importance | Evidence |
|---|---|---|---|---|---|
| `unifiprotect` | NVR/camera platform | Local | 674 | **CRITICAL** | config_entries |
| `reolink_discovery` | Discovers Reolink cameras | Local | UNKNOWN (not separately broken out) | OPTIONAL/UNKNOWN | config_entries, device_registry (1 Reolink device) |
| `go2rtc` | Local streaming relay for cameras | Local | 1 config entry | IMPORTANT (supports Protect/other camera streaming) | config_entries |
| `llmvision` | AI-assisted analysis of camera imagery (custom component) | Hybrid (local capture, likely a cloud or local model for analysis — not independently verified) | n/a | OPTIONAL — observational convenience, not alarm-authoritative | custom_components listing |

## Climate and Environmental Comfort

| Integration | Purpose | Local/Cloud | Entities | Importance | Evidence |
|---|---|---|---|---|---|
| `nexia` | Cloud API for Trane/American Standard thermostats (title observed: "TAGMDL Home") | Cloud | 28 | **CRITICAL** | config_entries, device_registry (Trane, 4 devices); `trane_config_*.conf` files corroborate (not opened) |
| `baf` | Big Ass Fans ceiling fan control | Local | 14 | IMPORTANT | config_entries |

## Environmental Awareness

| Integration | Purpose | Local/Cloud | Entities | Importance | Evidence |
|---|---|---|---|---|---|
| `ecowitt` | Weather-station sensor platform | Local | 282 | **IMPORTANT** | config_entries, device_registry |
| `airq` | Indoor air-quality sensors | Local | 60 | IMPORTANT | config_entries, device_registry (CorantGmbH) |
| `accuweather`, `nws`, `met` (disabled) | Outdoor forecast data | Cloud | 132 / 13 / — | OPTIONAL (redundant pair; `met` explicitly disabled by the household) | config_entries |
| `smart_meter_texas` | Utility (electric) usage data | Cloud | 1 | IMPORTANT (Energy dashboard input) | config_entries |

## Presence and Occupancy

| Integration | Purpose | Local/Cloud | Entities | Importance | Evidence |
|---|---|---|---|---|---|
| `bermuda` | BLE presence/triangulation | Local | 62 | **IMPORTANT** | config_entries, device_registry (4 ESPresense nodes) |
| `ibeacon`, `private_ble_device` | BLE beacon presence sources | Local | 10 / 5 | OPTIONAL/IMPORTANT | config_entries |
| `mqtt_room` | Room-level presence via MQTT | Local | 3 | OPTIONAL | config_entries |
| `mobile_app` | Phone/tablet presence + notification target (7 titled devices observed) | Hybrid | 142 | **CRITICAL** | config_entries |
| `person`, `zone` | Household presence model | Local | 7 / 40 | **FOUNDATIONAL** | `.storage/person`, `.storage/zone` |

## Voice Interaction

| Integration | Purpose | Local/Cloud | Entities | Importance | Evidence |
|---|---|---|---|---|---|
| `wyoming` | openWakeWord, Piper (TTS), Whisper (STT) — local voice pipeline | Local | 3 config entries | **CRITICAL** | config_entries |
| `openai_conversation`, `extended_openai_conversation` | Cloud conversation-agent / reasoning layer | Cloud | 5 / 1 | **IMPORTANT** (drives the household's voice-reasoning and the custom "Concierge"-named automations) | config_entries |
| `openai_tts` | Cloud TTS voice | Cloud | 2 | OPTIONAL (alternative to local Piper) | config_entries |
| `wakeword_installer` | Wake-word model management helper | Local | n/a | OPTIONAL | custom_components listing |
| `ai_automation_suggester` | Suggests new automations using an AI model (custom component) | Hybrid | n/a | OPTIONAL — a suggestion mechanism, never an autonomous policy (consistent with HTBW P26) | custom_components listing |

## Audio and Media

| Integration | Purpose | Local/Cloud | Entities | Importance | Evidence |
|---|---|---|---|---|---|
| `sonos` | Whole-home audio | Local | 248 | **CRITICAL** | config_entries, device_registry (54 Sonos-family devices) |
| `mass` (Music Assistant) | Media library/queue orchestration layered over Sonos and other players | Local | 44 | **CRITICAL** | config_entries |
| `cast`, `dlna_dmr`, `webostv`, `samsungtv`, `apple_tv`, `xbox`, `playstation_network`, `radio_browser`, `media_index` | Additional media endpoints/sources | Hybrid | varies (see CSV) | IMPORTANT/OPTIONAL per device | config_entries |

## Notifications and Household Communication

| Integration | Purpose | Local/Cloud | Entities | Importance | Evidence |
|---|---|---|---|---|---|
| `mobile_app` (notify platform) | Push notifications to 7 registered devices | Hybrid | (counted under Presence) | **CRITICAL** | config_entries |

## Safety

| Integration | Purpose | Local/Cloud | Entities | Importance | Evidence |
|---|---|---|---|---|---|
| (moisture/leak sensors — exact integration platform not separately isolated; several referenced in `automations.yaml` as `sensor.weatherhub_*` / `sensor.soil_moisture_*`) | Leak detection (6 named automations: toilets ×4, laundry, kitchen dishwasher) and irrigation moisture-gating | Local | — | **CRITICAL** for leak detection | automations.yaml; `watchman_report.txt` shows 2 of these sensors currently `unavail` — a confirmed evidence gap, not a publication claim of full coverage |

## Energy and Utilities

| Integration | Purpose | Local/Cloud | Entities | Importance | Evidence |
|---|---|---|---|---|---|
| `energy` | Home Assistant Energy dashboard | Local | 3 | IMPORTANT | config_entries |
| `smart_meter_texas` | Utility usage import | Cloud | 1 | IMPORTANT | config_entries |
| `ups` (custom component, CyberPower) | Power-protection monitoring | Local | — | IMPORTANT (resilience) | custom_components listing, device_registry (CyberPower Systems, 3 devices) |

## Asset Intelligence and Stewardship

| Integration | Purpose | Local/Cloud | Entities | Importance | Evidence |
|---|---|---|---|---|---|
| `asset_intelligence` | **HTBW's own product**, v1.0.12 | Local | 23 | IMPORTANT (lived-in reference deployment) | manifest.json, config_entries |
| `battery_notes` | Tracks battery types/levels across the household's battery-powered devices | Local | 5 | OPTIONAL (maintenance convenience) | config_entries |

## Dashboards and Household Interfaces

| Integration | Purpose | Local/Cloud | Entities | Importance | Evidence |
|---|---|---|---|---|---|
| `fully_kiosk` | Wall-mounted tablet kiosk control (screen on/off, 5 devices) | Local | 165 | **IMPORTANT** | config_entries, automations.yaml (kiosk on/off scheduling) |
| `ui_lovelace_minimalist` (custom component) | Dashboard card/template framework | Local | n/a | OPTIONAL (presentation layer) | custom_components listing |
| 15 Lovelace dashboards (`.storage/lovelace.*`) | Room- and function-specific dashboards (Den, Echo, Home, Irrigation, Kitchen, Digital Twin, Guest Bedroom, Living Room, Location & Devices, Map, Primary Bedroom, Security Cameras, Air Quality, Battery Levels, Bedroom Clock) | Local | n/a | **IMPORTANT** | `.storage` directory listing |

## Identity and Authority

| Integration | Purpose | Local/Cloud | Entities | Importance | Evidence |
|---|---|---|---|---|---|
| `person` | 7 household members/profiles registered | Local | 7 | **FOUNDATIONAL** | `.storage/person` |
| `auth`, `auth_provider.homeassistant`, `auth.session`, `auth_module.totp` | Native user authentication | Local | n/a | **FOUNDATIONAL** | `.storage` directory listing (contents not opened) |

## Privacy and Operational Trust

No dedicated integration exists for this category — in Home Assistant terms it is expressed through `homeassistant.exposed_entities` (the entity-exposure list consumed by Assist/voice and any future MCP server) and the household's authentication model. Direct equivalence to HTBW's own Operational Trust responsibility must not be assumed; Home Assistant's exposure/auth model is evidence, not HTBW governance.

## Resilience, Backup, and Recovery

Covered by `backup`, `watchman`, `ups` (custom), and `hassio` above.

## Governance and Explainability

| Integration | Purpose | Local/Cloud | Entities | Importance | Evidence |
|---|---|---|---|---|---|
| `nodered` (custom component) | Visual/flow-based automation engine, running alongside native `automation:` | Local | n/a | UNKNOWN — household's split of logic between Node-RED and native automations is **not independently verified** in this pass | custom_components listing |
| `openclaw` (custom component) | Purpose **UNKNOWN** from directory listing alone | — | n/a | UNKNOWN | custom_components listing |
| `github` | Tracks repository/update information (likely HACS-adjacent) | Cloud | 17 | OPTIONAL | config_entries |

## Administration and Maintenance

Covered by `watchman`, `hacs`, `backup`, `analytics`, `version`, `uptime` above.

## External Services

| Integration | Purpose | Local/Cloud | Entities | Importance | Evidence |
|---|---|---|---|---|---|
| `ms365_calendar`, `ms365_mail`, `ms365_todo` | Microsoft 365 calendar/mail/to-do | Cloud | 3 / 2 / 2 | IMPORTANT | config_entries, device_registry (Microsoft, 12 devices) |
| `icloud` | Apple iCloud (device/location and likely calendar) | Cloud | n/a (directory present) | IMPORTANT | `.storage` directory listing |
| `google_assistant`, `alexa_media` (custom), `feedreader` | Third-party voice-ecosystem bridge, RSS | Cloud | — / — / 4 | OPTIONAL | config_entries |
| `tesla_custom` | Vehicle integration | Cloud | 57 | IMPORTANT (household uses a Tesla-charge-reminder automation) | config_entries, device_registry (Tesla), automations.yaml |
| `xbox`, `playstation_network` | Gaming-platform cloud accounts | Cloud | 150 / 18 | OPTIONAL | config_entries |
| `miele`, `oralb`, `meater` | Appliance/personal-care cloud integrations | Cloud | 14 / 9 / — | OPTIONAL/HISTORICAL | config_entries |

## Historical or Transitional Technology

| Integration | Purpose | Local/Cloud | Entities | Importance | Evidence |
|---|---|---|---|---|---|
| `insteon` | Explicitly **not** historical in this home — still FOUNDATIONAL (see Lighting). Listed here only to note the owner-provided X10-lineage narrative belongs in the article series' history, not as a deprecation signal | Local | 81 | **FOUNDATIONAL** (re-asserted) | owner-provided context, `11-owner-input-required.md` |
| `met` (National forecast, disabled by household) | Superseded by AccuWeather/NWS | Cloud | — (disabled) | HISTORICAL | config_entries (`disabled_by: user`) |
| `google_translate`, `shopping_list` (disabled by household) | Onboarding defaults the household turned off | Cloud/Local | — (disabled) | HISTORICAL | config_entries |

---

**Full machine-readable catalog:** `integration-catalog.csv` and `reference-home-architecture.json`.
