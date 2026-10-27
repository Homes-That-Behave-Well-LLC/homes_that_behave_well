> **Document status: Operational — discovery artifact.** Not architecture-of-record.

# Article Series Recommendation — HTBW Reference Home

Opening sequence is fixed by instruction (articles 1–5). Remaining order derived from discovered capability categories and dependencies (network → platform → voice, the household's richest area → remaining capability domains by criticality → closing HTBW integration article). Full machine-readable form: `article-series.csv`.

## 1. Why Smart Homes Are Not Smart
- **Reader promise:** Understand why device-by-device "smart" gadgets don't add up to a smart *home*.
- **Household problem solved:** Framing, not a specific capability.
- **Technologies/integrations:** Referenced broadly (Insteon/X10 lineage as a 25+ year case study of fragmented, app-by-app control).
- **Representative automations:** None directly — scene-setting article.
- **Why this approach:** Establishes the series' thesis before any technology detail.
- **Alternatives to discuss:** Single-vendor "smart" ecosystems (Alexa-only, Google-only) vs. an orchestration-layer approach.
- **Constraints:** None evidence-based yet.
- **Lessons learned / what would be done differently:** OWNER INPUT REQUIRED.
- **New-construction / retrofit / grow-into-it guidance:** General framing only.
- **Supporting evidence:** OWNER PROVIDED (X10/Insteon lineage since 1997).
- **Architecture-image elements:** None (narrative article).
- **Instagram structure:** Carousel contrasting "gadget pile" vs. "orchestrated home" imagery.

## 2. The Home as an Operating System
- **Reader promise:** Understand Home Assistant's role as the home's operating system, not just an app.
- **Technologies/integrations:** `hassio` (Supervisor), HACS, Backup, Watchman, Analytics.
- **Representative automations:** `Backup Stale Automation`.
- **Why this approach:** Evidence-based — this household runs Supervisor + HACS + active self-diagnostics (Watchman), a textbook "operating system" posture.
- **Alternatives to discuss:** Container-only Home Assistant Core, cloud-hosted alternatives (explicitly contrasted with the household's local-first posture).
- **Lessons learned:** Watchman's own findings (missing doorbell entities, stale soil-moisture sensors) are honest, real "operating system needs maintenance too" material.
- **Supporting evidence:** DIRECTLY SUPPORTED BY REFERENCE HOME EVIDENCE.
- **Architecture-image elements:** Platform layer (layer 4 of the 12-layer model).

## 3. Begin With the End in Mind: The HTBW Reference Home Architecture
- **Reader promise:** See the whole picture before the detail articles.
- **Technologies/integrations:** All — this is the article the master architecture image illustrates.
- **Supporting evidence:** `reference-home-architecture.json`, all 12 layers.
- **Architecture-image elements:** The master image itself.

## 4. The Network Is the Backbone
- **Reader promise:** Understand why network design must come first in planning.
- **Technologies/integrations:** UniFi (network, access, protect) — topology largely `UNKNOWN`, see `07-network-and-infrastructure-inventory.md`.
- **Constraints:** Evidence gap — network topology not independently observable from Home Assistant.
- **Lessons learned:** OWNER INPUT REQUIRED before this article can be written in full.
- **Supporting evidence:** GENERAL RECOMMENDATION REQUIRING REVIEW for most of this article's planned content; only integration-level evidence (UniFi family presence) is DIRECTLY SUPPORTED.

## 5. Why Home Assistant Became the Home Operating System
- **Reader promise:** The decision rationale for Home Assistant specifically.
- **Supporting evidence:** OWNER PROVIDED ("Home Assistant is intentionally positioned as the controller, hub, and home operating platform of choice").
- **Lessons learned / alternatives discussed:** OWNER INPUT REQUIRED (what else was considered, why Home Assistant won).

## 6. Lighting (Insteon and Beyond)
- **Reader promise:** How whole-home lighting can be both automatic and always manually operable.
- **Technologies/integrations:** `insteon` (67 devices), `switch_as_x`, `group`.
- **Representative automations:** Sunset-offset, overnight, occupancy-driven, "Learn on Use" families (see `06-automation-script-scene-inventory.md`).
- **Why this approach chosen:** OWNER PROVIDED (Insteon/X10 lineage since 1997); Leviton preference noted but not realized due to wiring-plan constraints — OWNER PROVIDED.
- **Alternatives to discuss:** Leviton (preferred if wiring allowed), Zigbee/Z-Wave bulbs/switches, fully wireless retrofit lighting.
- **Constraints:** OWNER PROVIDED (construction/wiring constraints shaped the retrofit approach).
- **New-construction guidance:** DIRECTLY SUPPORTED — deep electrical boxes, neutral conductors at switch locations (see `10-building-and-renovation-guidance.md`).
- **Retrofit guidance:** DIRECTLY SUPPORTED BY REFERENCE HOME EVIDENCE (this home *is* the retrofit case study).
- **Supporting evidence:** Mixed — automation evidence is DIRECTLY SUPPORTED; vendor-preference narrative is OWNER PROVIDED.

## 7. Shades and Natural Light
- **Technologies/integrations:** `hunterdouglas_powerview` (20 devices, 8 directional automation pairs).
- **Lessons learned:** The `watchman_report.txt`-confirmed vanished PowerView scene is a genuine, honest case study.
- **New-construction guidance:** Window-header power, shade motor wiring (see `10-`).

## 8. Access, Security, and Alarm
- **Technologies/integrations:** `unifi_access`, `adtpulse`.
- **Representative automations:** Gate auto-close; 4-stage Primary Bedroom alarm escalation.
- **Why this approach:** Escalation-ladder pattern is a strong, evidence-based case study.

## 9. Cameras and Observation
- **Technologies/integrations:** `unifiprotect`, `reolink_discovery`, `go2rtc`, `llmvision`.
- **Lessons learned:** Confirmed front-gate doorbell gap (missing entities) is honest material — "what would be done differently today" territory, pending OWNER INPUT on the specific cause/fix.

## 10. Climate and Environmental Comfort
- **Technologies/integrations:** `nexia` (Trane), `baf` (fans).
- **Alternatives to discuss:** Local-only thermostat integrations vs. cloud-API-dependent Nexia — a direct local/cloud tradeoff case study.

## 11. Irrigation and Outdoor Systems
- **Technologies/integrations:** `bhyve`, moisture sensors, mister automations.
- **Lessons learned:** Confirmed stale soil-moisture sensors (Watchman) — an honest "sensors need maintenance" case study.
- **New-construction guidance:** Irrigation-controller wiring, moisture-sensor placement (see `10-`).

## 12. Voice Interaction and the Household's Own "Concierge"
- **Reader promise:** How this household built a sophisticated voice-command and learning layer entirely from native Home Assistant automations — and what that reveals about what a *formal* framework like HTBW would add.
- **Technologies/integrations:** `wyoming`, `openai_conversation`/`extended_openai_conversation`, `ai_automation_suggester`.
- **Representative automations:** The full "Concierge"/"VA:" family (14+ automations).
- **Why this approach:** This is the single richest, most production-mature capability area discovered.
- **Lessons learned:** The household independently arrived at voice-entry, follow-up-command, intentional-learning, and identity-self-query concepts — a strong natural bridge to the closing article.
- **What would be done differently today:** OWNER INPUT REQUIRED.
- **Supporting evidence:** DIRECTLY SUPPORTED BY REFERENCE HOME EVIDENCE.

## 13. Audio and Media
- **Technologies/integrations:** `sonos`, `mass`, room-audio-resolver scripts.
- **Representative automations/scripts:** `room_audio_resolver_keystone`, `resolve_speaker_profile`, `learn_music_volume_room`.

## 14. Presence and Occupancy
- **Technologies/integrations:** `bermuda`, `ibeacon`, `mobile_app`, `unifi` network-presence.

## 15. Safety (Leak and Flood Protection)
- **Technologies/integrations:** 6-location leak detection.
- **Why this is the strongest direct bridge to HTBW doctrine:** directly comparable to HTBW's own documented Washing-Machine Leak Protection use case (`homes_that_behave_well/docs/scenarios/stewardship-use-cases.md`) — a genuine production-evidence parallel, not an invented one.

## 16. Energy and Utilities
- **Technologies/integrations:** `energy`, `smart_meter_texas`, `ups`.

## 17. Asset Intelligence and Household Stewardship
- **Technologies/integrations:** `asset_intelligence` v1.0.12 — the one HTBW product genuinely deployed here.
- **Why this approach:** Direct, evidence-based bridge to HTBW's own Stewardship responsibility.

## 18. Dashboards and Household Interfaces
- **Technologies/integrations:** `fully_kiosk` (5 tablets), 15 Lovelace dashboards, `ui_lovelace_minimalist`.

## 19. Resilience, Backup, and Recovery
- **Technologies/integrations:** Backup, Watchman, UPS.
- **Lessons learned:** `Backup Stale Automation` is itself evidence the household actively guards against silent backup failure.

## 20. If You Are Building or Renovating
- Recurring/structural section — see `10-building-and-renovation-guidance.md` in full; appears once as its own article and is cross-referenced from every capability article above where relevant.

## Final article — The HTBW Integration for Home Assistant: Bringing the Framework Together
- **Reader promise:** See how the HTBW Framework's seven responsibilities (Foundation, Stewardship, Identity, Truth, Continuity, Operational Trust, Concierge) would formally govern the patterns this household already built informally (the "Concierge"/"VA:" automation family, the alarm escalation ladder, the "Learn on Use" patterns).
- **Household problem solved:** Moving from ad hoc, automation-by-automation logic to a governed, explainable framework — without discarding any of the proven patterns above.
- **Technologies/integrations:** Cross-references the entire catalog; explicitly distinguishes "what HTBW governs" from "what Home Assistant already does natively" (per `homes_that_behave_well/docs/architecture/home-assistant-boundary.md`'s own discipline).
- **Why the selected approach was chosen / alternatives / constraints / lessons learned / what would be done differently:** Primarily **OWNER INPUT REQUIRED** — this is the one article that most depends on narrative not yet captured anywhere in repository or production evidence.
- **New-construction / retrofit / grow-into-it guidance:** OWNER PROVIDED theme — "households can grow into the architecture while planning infrastructure ahead of installation" is the explicit intended closing message.
- **Supporting evidence:** Mixed — architectural cross-references are DIRECTLY SUPPORTED; the narrative framing is OWNER INPUT REQUIRED.
- **Architecture-image elements:** The full 12-layer master image, with an explicit "HTBW Framework responsibilities" overlay (layer 3) shown mapped onto the already-discovered capability domains (layer 5).
- **Instagram structure:** A closing carousel/reel summarizing the whole series — "what we built, what we learned, what a framework adds."

---

**Full machine-readable series:** `article-series.csv`.
