> **Document status: Operational — discovery artifact.** Not architecture-of-record.

# Capability Catalog

Organized by household purpose (Phase 4 categories). Each category cross-references the Integration Catalog (`03-`) rather than repeating integration detail. Machine-readable form: `capability-catalog.csv`.

## 1. Network Foundation
- **Household need:** Reliable connectivity underlying every other capability.
- **Experience/outcome:** Invisible when working; everything else fails without it.
- **Integrations:** `unifi`, `unifi_access`, `unifi_play`, `upnp`.
- **Physical technology:** Ubiquiti UniFi switches/APs/gateway (inferred from integration presence; models not independently verified).
- **Key automations:** None directly — this layer is consumed by nearly every automation indirectly (presence, connectivity).
- **Dependencies:** Internet service (ISP) — not independently observable.
- **Manual fallback:** Not observable from Home Assistant; a network outage likely disables most of the home's automation.
- **Local/cloud posture:** Local.
- **Works well:** 4,861 `unifi`-platform entities suggest comprehensive client/device visibility.
- **Constraints:** Physical topology entirely `UNKNOWN`.
- **Evidence gaps:** Router/firewall model, AP placement, VLAN design, wiring — all `UNKNOWN`.
- **Likely article scope:** "The Network Is the Backbone" (article 4).

## 2. Home Assistant Platform
- **Household need:** The orchestration layer itself.
- **Integrations:** `hassio`, `cloud`, `hacs`, `backup`, `watchman`, `analytics`, `version`, `uptime`.
- **Key automations:** `Backup Stale Automation` (self-monitoring that backups are current).
- **Dependencies:** Supervisor host; Home Assistant Cloud for remote-access/voice convenience.
- **Manual fallback:** None observed; this is the controller itself.
- **Local/cloud posture:** Hybrid (core local, Cloud convenience optional).
- **Works well:** Self-diagnostic discipline (Watchman) is active and already catching real gaps.
- **Evidence gaps:** Backup destination/schedule/retention not read this pass.
- **Likely article scope:** "The Home as an Operating System" (article 2); "Why Home Assistant Became the Home Operating System" (article 5).

## 3. Lighting
- **Household need:** Automatic and manual light control throughout the home.
- **Integrations:** `insteon`, `switch_as_x`, `group`.
- **Physical technology:** Insteon switches/dimmers (SmartLabs, Inc., 67 devices).
- **Key automations:** `Turn On Daily 20 Minutes before Sunset`, `Turn-On/Off Overnight Lights`, `Turn on David's Lamp 39 minutes before sunset`, `Turn on Tom's Office when Occupied`, `Lighting Profile – Learn on Use`, `Den Lamps` occupancy+illuminance pair.
- **Dependencies:** Insteon PLM/hub (not independently verified); sun-position data.
- **Manual fallback:** Physical Insteon switches remain directly operable (a documented Insteon characteristic, not independently verified in this pass).
- **Local/cloud posture:** Local.
- **Works well:** A "learn on use" pattern is already running in production.
- **Constraints:** `Insteon Keep Alive Every 10 Minutes` automation suggests the household has needed to actively manage Insteon reliability.
- **Likely article scope:** A dedicated Lighting article, with the Insteon/X10 lineage as owner-provided history.

## 4. Shades and Natural-Light Management
- **Household need:** Automated shade position by time, sun, and presence.
- **Integrations:** `hunterdouglas_powerview`.
- **Physical technology:** Hunter Douglas PowerView (20 devices).
- **Key automations:** 8 directional automations (NE/NW/SE/SW × upstairs/downstairs, open/close pairs), `Close Guest Shade when David enters the Guest Bedroom between 9PM and 6AM`.
- **Manual fallback:** Physical remote/app control (PowerView native capability, not independently verified here).
- **Local/cloud posture:** Local (PowerView Hub, `zeroconf`-discovered).
- **Works well:** Systematic quadrant-based naming shows a deliberate, scalable automation design.
- **Evidence gaps:** `watchman_report.txt` shows one PowerView scene (`Close Downstairs Shades`) now resolves to `unknown` — a confirmed, real evidence gap worth using as a "lessons learned" case study.
- **Likely article scope:** Combined with Lighting, or its own "Shades and Natural Light" article.

## 5. Access
- **Household need:** Controlled entry (gate, doors).
- **Integrations:** `unifi_access`, `homekit_controller` (bridge only).
- **Key automations:** `Close Rolling Gate after 5 minutes of being open`.
- **Local/cloud posture:** Local.
- **Likely article scope:** Combined with Security.

## 6. Security and Alarm
- **Household need:** Intrusion detection and alerting.
- **Integrations:** `adtpulse`.
- **Key automations:** `Primary Bedroom – Alarm Started/Repeat/Escalation/Stop` — a complete escalation ladder.
- **Local/cloud posture:** Cloud (ADT's own portal).
- **Works well:** The escalation-ladder pattern is a strong, production-proven case study directly relevant to HTBW's Operational Trust escalation concepts (as a household pattern worth studying, not as HTBW architecture already implemented here).
- **Likely article scope:** "Security and Alarm."

## 7. Cameras and Observation
- **Household need:** Visual awareness of the property.
- **Integrations:** `unifiprotect`, `reolink_discovery`, `go2rtc`, `llmvision` (AI-assisted analysis).
- **Key automations:** Front gate video doorbell automations exist in `automations.yaml`, but `watchman_report.txt` shows the underlying `camera.front_gate_doorbell` and `event.front_gate_video_doorbell_ding` entities are currently **missing** — a confirmed, real hardware/integration gap.
- **Local/cloud posture:** Local (Protect/Reolink), with `llmvision`'s analysis posture unverified (hybrid/unknown).
- **Likely article scope:** "Cameras and Observation," explicitly including the doorbell gap as an honest "what's currently broken" case study.

## 8. Climate and Environmental Comfort
- **Household need:** Comfortable, efficient temperature control; fan comfort.
- **Integrations:** `nexia` (Trane/American Standard cloud API), `baf` (Big Ass Fans).
- **Local/cloud posture:** Hybrid (Nexia is cloud-dependent for thermostat control).
- **Likely article scope:** "Climate and Environmental Comfort."

## 9. Environmental Awareness
- **Household need:** Understanding outdoor and indoor conditions (weather, air quality, soil moisture).
- **Integrations:** `ecowitt`, `airq`, `accuweather`, `nws`, `smart_meter_texas`.
- **Key automations:** `AccuWeather Update every 5 Minutes`, `VA: Weather Announcement`, multiple moisture-gated irrigation automations.
- **Evidence gaps:** `watchman_report.txt` shows 2 soil-moisture sensors (`Bamboo 05/06 Moisture`) currently `unavail`.
- **Likely article scope:** Folded into Irrigation/Energy articles rather than standalone.

## 10. Presence and Occupancy
- **Household need:** Knowing who/what is home and where.
- **Integrations:** `bermuda`, `ibeacon`, `private_ble_device`, `mqtt_room`, `mobile_app`, `unifi` (network presence), `person`/`zone`.
- **Key automations:** `Turn on Tom's Office when Occupied`, `Turn on Den Lamps when Presence is detected`, `Concierge – Room Monitoring Awareness (HA Voice)`.
- **Local/cloud posture:** Local.
- **Works well:** Multiple independent presence-evidence sources (BLE, network, device-tracker) — directly comparable to HTBW's own multi-source Identity/Truth evidence philosophy, as a household pattern worth studying.
- **Likely article scope:** "Presence and Occupancy."

## 11. Voice Interaction
- **Household need:** Hands-free control and query.
- **Integrations:** `wyoming` (local STT/TTS/wake-word), `openai_conversation`/`extended_openai_conversation` (cloud reasoning), `openai_tts`, `ai_automation_suggester`.
- **Key automations:** The entire "Concierge – … (HA Voice)" and "VA: …" automation families (Voice Entry, Follow-Up Commands, Intentional Learning, Identity Self Query, Bedtime, Goodnight, Good Morning, Weather Announcement).
- **Local/cloud posture:** Hybrid by design (local STT/TTS, cloud reasoning).
- **Works well:** This is the richest, most architecturally mature capability area observed — a household-built, production-proven voice-command and learning layer, independent of any HTBW integration.
- **Likely article scope:** A dedicated Voice Interaction article, and the primary evidence base for the closing "HTBW Integration for Home Assistant" article (as a *contrast* — what the household built natively versus what HTBW's Concierge responsibility would formally govern).

## 12. Audio and Media
- **Household need:** Whole-home music and entertainment.
- **Integrations:** `sonos`, `mass` (Music Assistant), `cast`, `dlna_dmr`, `webostv`, `samsungtv`, `apple_tv`, `xbox`, `playstation_network`, `radio_browser`.
- **Key automations:** `Voice – Play Music`, `Voice – Continue Playing`, `Learn Music Volume – On Sonos Change`, `Music – Capture Last Media (Robust)`, `Music Genre – Observe Playback (All Sources)`, `Duck Sonos When Any Assist Satellite Is Listening`.
- **Scripts:** `resolve_speaker_profile`, `room_audio_resolver_keystone`, `sonos_speak_with_ducking_room`, `resolve_music_player_room`.
- **Local/cloud posture:** Local (Sonos/Music Assistant), hybrid for some sources.
- **Works well:** A sophisticated room-aware audio-resolution and learned-preference system is already in production.
- **Likely article scope:** "Audio and Media."

## 13. Notifications and Household Communication
- **Household need:** Timely, relevant alerts.
- **Integrations:** `mobile_app` (notify platform, 7 devices).
- **Key automations:** `Send Notification when B-Hyve Battery Low`, `Reminder to Charge the Tesla`, `Tesla below 100 Mile Range - Please Charge`.
- **Local/cloud posture:** Hybrid (push delivery depends on each platform's cloud notification service).
- **Likely article scope:** Folded into Notifications or the closing HTBW article (Communication/Delivery Surface comparison).

## 14. Safety
- **Household need:** Leak/flood prevention and early warning.
- **Integrations:** moisture/leak sensors referenced in automations (platform not separately isolated this pass).
- **Key automations:** `Toilet Leak - Downstairs/Primary/Guest Bathroom/Powder Room`, `Leak Detected - Laundry Room`, `Leak Detected - Kitchen Dishwasher`.
- **Local/cloud posture:** Local.
- **Works well:** 6 independent leak-detection points is strong coverage.
- **Likely article scope:** "Safety," directly reusable as the real-world counterpart to HTBW's own Washing-Machine Leak Protection use case.

## 15. Energy and Utilities
- **Household need:** Usage visibility and resilience.
- **Integrations:** `energy`, `smart_meter_texas`, `ups` (CyberPower).
- **Local/cloud posture:** Hybrid.
- **Likely article scope:** "Energy and Utilities."

## 16. Asset Intelligence and Stewardship
- **Household need:** Tracking and caring for physical household assets.
- **Integrations:** `asset_intelligence` (HTBW product, v1.0.12), `battery_notes`.
- **Local/cloud posture:** Local.
- **Likely article scope:** Directly useful evidence for the closing HTBW article — this is the one HTBW product genuinely deployed here.

## 17. Dashboards and Household Interfaces
- **Household need:** Visual control surfaces throughout the home.
- **Integrations:** `fully_kiosk` (5 wall tablets), `ui_lovelace_minimalist`, 15 named Lovelace dashboards.
- **Key automations:** `All Kiosk Screen Off 11 PM` / `All Kiosk Screens On 7AM`.
- **Likely article scope:** "Dashboards and Household Interfaces."

## 18. Identity and Authority
- **Household need:** Knowing who is asking, and what they're allowed to do.
- **Integrations:** `person` (7 profiles), native `auth`.
- **Key automations:** `Concierge - Identity Self Query (HA Voice)`.
- **Likely article scope:** Closing HTBW article (Identity responsibility comparison).

## 19. Privacy and Operational Trust
- **Household need:** Appropriate, consistent permission behavior.
- **Evidence:** `homeassistant.exposed_entities` exists; no dedicated integration. See Integration Catalog note.
- **Likely article scope:** Closing HTBW article only — not enough standalone production evidence for its own article.

## 20. Resilience, Backup, and Recovery
- **Integrations:** `backup`, `watchman`, `ups`, `hassio`.
- **Likely article scope:** Folded into the Platform article.

## 21. Governance and Explainability
- **Household need:** Understanding why something happened; improving automations safely.
- **Integrations:** `ai_automation_suggester`, `nodered` (purpose split vs. native automations UNKNOWN), `openclaw` (UNKNOWN).
- **Likely article scope:** Closing HTBW article (Explainability/Decision Trace comparison) — strongest conceptual bridge to HTBW Framework content.

## 22. Administration and Maintenance
- **Integrations:** `watchman`, `hacs`, `backup`, `analytics`.
- **Likely article scope:** Folded into the Platform article.

## 23. External Services
- **Household need:** Calendar, mail, gaming, vehicle, appliance cloud integration.
- **Integrations:** `ms365_calendar/mail/todo`, `icloud`, `tesla_custom`, `xbox`, `playstation_network`, `miele`, `oralb`, `meater`, `alexa_media`, `feedreader`.
- **Likely article scope:** Folded into relevant capability articles (media, climate-adjacent, etc.), not a standalone article.

## 24. Historical or Transitional Technology
- **Household need:** N/A — retained for continuity/narrative.
- **Integrations:** `insteon` (active, not historical — the *lineage* is historical); `met`, `google_translate`, `shopping_list` (disabled by household).
- **Likely article scope:** Owner-provided history embedded in the Lighting article and "Why Smart Homes Are Not Smart" (article 1).

---

**Full machine-readable catalog:** `capability-catalog.csv`.
