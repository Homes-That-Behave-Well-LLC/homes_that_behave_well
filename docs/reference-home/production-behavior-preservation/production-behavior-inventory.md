# HTBW Production Behavior Preservation Inventory

> **Document status: Operational — discovery/evidence artifact.** Not architecture-of-record. Creates no
> authority. Does not amend `decision-ledger.md`, `authority-order.md`, or any canonical model/contract.
> Produced under
> [../../governance/htbw-architecture-execution-grounding-standard.md](../../governance/htbw-architecture-execution-grounding-standard.md)
> and [../../governance/standard-implementation-prompt-header.md](../../governance/standard-implementation-prompt-header.md).

**Date:** 2026-10-13.
**Production source:** `P:\` — a live Home Assistant configuration directory, Home Assistant Core
(version per `.storage/core.config`, not re-verified in this pass; the 2026-10-07 prior discovery pass
recorded 2026.9.4).
**Repository reviewed:** `homes_that_behave_well` (this repository).

---

## Scope of this pass

The governing prompt originally requested a comprehensive, full-environment inventory. **That scope was
explicitly narrowed during execution**, directed to focus on `automations.yaml` and `scripts.yaml`
filtered by the three production groups the prompt itself names:

- the automation category **Concierge** (18 automations), plus the **8 ungrouped (uncategorized)**
  automations;
- the script category **Concierge** (44 scripts);
- the helper category **Concierge Automation Helpers** (116 helpers across 6 domains).

This is **26 of 84 total production automations** and **44 of 50 total production scripts**. The
remaining 58 automations and 6 scripts were not individually inspected in this pass. This narrowing is
recorded transparently here and in every output artifact's scope note, consistent with this task's own
Count Discipline requirement ("if access limitations prevent an exact count, report count observed, scope
observed, scope not accessible").

A broader, differently-purposed discovery pass already exists at
[docs/reference-home/discovery/](../discovery/) (dated 2026-10-07, not yet committed to git at the time
of this pass). That pass covered the full entity registry (8,548 entities then, 8,680 now), all 84
automations and 50 scripts at a trigger/alias level, and produced household-narrative/article-series
content. This pass is narrower in automation/script/helper scope but **substantially deeper** for the
items it does cover — full trigger/condition/action/script-call/helper-read/write detail for every one of
the 26 + 44 + 116 items in scope, which the prior pass did not attempt.

---

## 1. Executive Verdict

A complete inventory of the **directed scope** (Concierge + ungrouped automations, Concierge scripts,
Concierge Automation Helpers) was achieved: all 26 automations and all 44 scripts were read in full
(not sampled), all 116 helpers were enumerated and classified, and the single native-scene file and
single template-entity file were read in full. A complete inventory of the **full production
environment** (84 automations, 50 scripts, 8,680 entities, 9 dashboards, 27 custom integrations, etc.)
was **not** attempted in this pass — see "Scope not accessible or not reviewed this pass" in
[production-inventory-summary.json](production-inventory-summary.json).

Within the directed scope, this review found the production implementation to be **substantially more
complex, more duplicated, and more fragile than its own descriptions suggest** — including a
**safety-relevant finding**: the Primary Bedroom alarm-clock escalation ladder has three of its four
stages silently broken (confirmed by direct evidence, not inference). See §6 and
[production-gaps-and-owner-review.md](production-gaps-and-owner-review.md) §1.

## 2. Production Safety Confirmation

**Production was not modified.** No automation, script, scene, or helper was saved, enabled, disabled,
renamed, deleted, reloaded, or triggered. `P:\automations.yaml` and `P:\scripts.yaml` were copied
read-only to local scratch space (`%TEMP%\ha_automations.yaml`, `%TEMP%\ha_scripts.yaml`) for inspection;
every other production file was read in place, never written. `secrets.yaml`, the Nexia/Trane thermostat
credential files, and the Recorder database were not opened. No Home Assistant service, automation,
script, or administrative interface was invoked. Full detail in
[production-evidence-register.md](production-evidence-register.md).

## 3. Exact Inventory Counts

| Artifact type | Count observed (in scope) | Count in full production | Notes |
|---|---|---|---|
| Automations | **26** | 84 | 18 Concierge category + 8 ungrouped |
| Scripts | **44** | 50 | 6 ungrouped scripts out of scope |
| Helpers (Concierge Automation Helpers category) | **116** | n/a (3 other helper categories exist, out of scope) | 54 input_number, 26 input_text, 19 counter, 12 input_boolean, 3 input_datetime, 2 input_select |
| Native HA scenes (`scenes.yaml`) | **0** | 0 | File is a literal `[]` |
| PowerView-vendor scenes referenced by in-scope items | **8** | n/a (not independently countable — vendor-supplied) | |
| Template entities (`templates.yaml`) | **1** | 1 | `sensor.house_top_music_genre` |
| REST command action collections | **2 files, 12 actions** | n/a | Fully Kiosk wrapper (4 actions); Music Assistant direct-API wrapper (8 actions) |
| Reconstructed household behaviors | **29** | n/a | See [production-behavior-catalog.csv](production-behavior-catalog.csv) |
| Confirmed broken script/service references | **6 distinct, 9 call sites** | n/a | See §6 |
| Blueprints used by in-scope automations | **0** | 6 blueprint files exist in production, none referenced by the 26 in-scope automations | |

Full counts, including the scope-not-accessible disclosures, are in
[production-inventory-summary.json](production-inventory-summary.json).

## 4. Major Existing Household Experiences

- **Room-aware voice control** of lamps, overhead lights, shades, music, and TV — without naming the
  room — across every Home Assistant Voice satellite in the house.
- **A central, reused voice-output controller** (`sonos_speak_with_ducking_room`) that ducks active
  music, speaks via TTS, and restores volume — used by nearly every spoken response in the house.
- **Automatic ducking** of room music whenever that room's voice satellite starts listening.
- **Learning**, both implicit (silent, on every manual adjustment) and explicit (opt-in, voice-confirmed),
  of per-light brightness and per-room music volume.
- **A full Bedtime / Goodnight / Good Morning routine family**, each working identically from a bedroom or
  its paired bathroom, coordinating Sonos, shades, lights, AppleTV, kiosk tablets, and a spoken weather
  briefing.
- **A room-capability discovery experience** ("what can I do here") that speaks back only what is
  actually present in that room.
- **A music explainability layer** ("what's playing," "why did you play this") built on a structured,
  per-room last-media audit trail — though currently non-functional end-to-end (see §6).
- **A Primary Bedroom alarm-clock escalation ladder** — intended to turn on lamps, chime, repeat, escalate
  to ambient audio, and restore state — currently substantially broken (see §6).
- **Household music-genre popularity tracking**, exposed as a dashboard sensor.
- **Wall-tablet kiosk provisioning and day/night mode switching**, driven by the same bedroom
  routines above.

## 5. Concierge Inventory

| Category | Count | Detail |
|---|---|---|
| Concierge automations | 18 | Voice entry, follow-up commands, intentional learning, music capture/genre observation, play/continue/follow-up music, learning, shade/lighting percentage catchers, Bedtime/Goodnight/Good Morning, Sonos ducking, room monitoring/sensor follow-ups |
| Ungrouped automations (in this pass's scope) | 8 | 2 disabled legacy Den shade commands, 1 dormant test automation, 4 Primary Bedroom alarm-chain automations (3 of which call broken scripts), 1 Identity self-query (orphaned service call) |
| Concierge scripts | 44 | See [production-script-inventory.csv](production-script-inventory.csv) for full detail |
| Concierge Automation Helpers | 116 | See [production-helper-inventory.csv](production-helper-inventory.csv) |
| Scenes | 0 native + 8 referenced vendor scenes | See [production-scene-inventory.csv](production-scene-inventory.csv) and the template-and-group inventory |
| Templates | 1 | `sensor.house_top_music_genre` |
| Dashboards | not inventoried in this pass (9 lovelace dashboard storage files exist in production; out of this pass's directed scope) | |
| Dependencies | Sonos integration; Music Assistant integration (both native service calls AND a parallel direct-REST API path); Home Assistant Cloud (TTS); OpenAI (`extended_openai_conversation`, `openai_conversation`, AI Task); AccuWeather; Fully Kiosk Browser (REST, with a hardcoded plaintext credential); PowerView/Insteon (vendor scenes) | |

## 6. Dynamic Room Assembly

Production derives, at runtime, every single time a behavior executes: lamp-vs-light membership, shade
membership, Sonos/media-player membership and active-player selection, voice-assistant fallback bias,
and presence/environment/air-quality/noise capability flags — all via live `area_entities()` /
`label_devices()` / entity-id regex matching, duplicated independently across 6–12 scripts and
automations for each category. The one exception is a hardcoded "Main Living Area" (Kitchen+Dining
Room+Living Room) zone concept, duplicated as a **literal list** in 5–7 places rather than derived live.

This directly and explicitly conflicts with already-accepted HTBW architecture: **ADR Room Configuration
Ownership** (DL-09/DL-10/DL-11/DL-13) states Room Help "must never be generated from raw device
inventory," and the **Concierge Contract**'s hard prohibitions state Concierge "must not select sensors
at runtime" and "must not runtime-search devices to satisfy a vocabulary term." Production's current
implementation does precisely what both documents already say must not happen — not because it
disregards the architecture, but because it predates it.

What HTBW must configure at setup instead, and what must be preserved: full detail, mechanism-by-mechanism,
is in [production-dynamic-room-assembly-analysis.md](production-dynamic-room-assembly-analysis.md). In
summary, six runtime-derived concepts (lamp/light classification, shade/cover membership, media-player
membership, voice-assistant fallback bias, sensing-capability inference, and the Main Living Area zone)
each need one setup-time Room Configuration relationship to replace between 2 and 12 duplicated,
hand-maintained Jinja blocks.

## 7. Production-to-Repository Reconciliation

Of the 29 reconstructed behaviors (full detail in
[production-to-htbw-reconciliation-matrix.csv](production-to-htbw-reconciliation-matrix.csv)):

- **3** are in direct, documented conflict with already-accepted architecture (room capability discovery,
  room monitoring/sensor-value queries, and the Main Living Area/Merged Room concept) — classified
  **HTBW REPLACEMENT REQUIRED**.
- **17** have repository implementation evidence (a Concierge custom_component exists in the sibling
  repository) that is **not deployed to this production instance** — production runs an entirely
  independent, pre-HTBW YAML/UI implementation of these experiences.
- **1** (the identity self-query) has a plausible HTBW-equivalent owner (Identity) but the production call
  target's very existence could not be confirmed — classified **HTBW EQUIVALENT EXISTS — VALIDATION
  REQUIRED**.
- **4**, including the alarm escalation ladder, require direct owner verification before any
  classification beyond **OWNER REVIEW REQUIRED** is responsible.
- **1** is already recognized by the household itself as legacy (disabled, not deleted) — **LEGACY —
  RETIREMENT CANDIDATE**.
- **1** has no in-scope reader/writer/caller found at all and must not be assumed safe to remove —
  **UNKNOWN PURPOSE — DO NOT REMOVE**.
- **2** (both intentional/opt-in learning flows) are directionally aligned with existing HTBW governance
  principles (DL-21/P26) and are candidates to **PRESERVE AS-IS**.

No production behavior in this pass's scope was found to be already fully aligned end-to-end with an
accepted, deployed HTBW implementation — the sibling `concierge` custom_component is not active in
production, so every in-scope Concierge experience today is running on its pre-refoundation,
household-built implementation.

## 8. Dynamic Room Assembly (summary)

See §6 above and the dedicated
[production-dynamic-room-assembly-analysis.md](production-dynamic-room-assembly-analysis.md) for the
full mechanism-by-mechanism breakdown and mapping table.

## 9. Preservation Classification Summary

| Classification | Count | Examples |
|---|---|---|
| PRESERVE AS-IS | 2 | Intentional/opt-in learning (BHV-12); voice-interaction ducking (BHV-16) |
| PRESERVE EXPERIENCE / REPLACE IMPLEMENTATION | 17 | Lamp/light/shade/music/TV voice control; Bedtime/Goodnight/Good Morning; last-media explainability |
| HTBW EQUIVALENT EXISTS — VALIDATION REQUIRED | 1 | Identity self-query |
| HTBW REPLACEMENT REQUIRED | 3 | Room capability discovery; room monitoring/sensor queries; Main Living Area/Merged Room |
| LEGACY — RETIREMENT CANDIDATE | 1 | Disabled Den-only shade commands |
| UNKNOWN PURPOSE — DO NOT REMOVE | 1 | `automation.test_automation` (plus 10 individual helpers flagged separately — see Gaps and Owner Review §5) |
| OWNER REVIEW REQUIRED | 4 | Primary Bedroom alarm escalation ladder (elevated priority); implicit lighting learning (DL-21 tension); air-quality AI assessment (unreachable); `automation.test_automation` |

Full per-behavior detail, including the Retirement Gate and acceptance scenarios for every row, is in
[production-migration-protection-matrix.csv](production-migration-protection-matrix.csv).

## 10. Orphan, Duplication, and Legacy Findings

**Six confirmed broken script/service references** (nine call sites), independently corroborated by two
separate analysis passes over the same production evidence:

1. `script.room_speak_sonos` — called by 3 scripts, does not exist anywhere in production.
2. `script.whats_playing_room` — called by 1 automation, real entity is `script.what_s_playing_room`.
3. `script.speak_room_air_quality_assessment` — checked by 1 script, real entity is
   `script.speak_room_air_quality_ai_assessment`.
4. `script.turn_on_lamps_usual` — called by 1 automation, real entity is `script.turn_on_lamps_usual_room`.
5. `script.room_audio_duck_and_play` — called by 1 automation, does not exist anywhere in production.
6. `script.room_audio_restore` — called by 1 automation, does not exist anywhere in production.

Plus one unconfirmed service target (`concierge.execute`, no matching integration found installed), one
hardcoded plaintext credential pattern (Security Finding), and 10 helpers/1 automation with no in-scope
reader/writer/caller found (Unknown Purpose — Do Not Remove). Full detail in
[production-gaps-and-owner-review.md](production-gaps-and-owner-review.md).

**No duplicate media-player entity-ID handling defects were found** beyond the already-noted string-match
fragility; **no disabled automation with architecturally valuable, otherwise-lost behavior** was found
beyond the two Den-shade automations, which are already fully superseded by newer, more general
behaviors still active in production.

## 11. Open-Issue Impact Review

A lightweight (not exhaustive) correspondence check against Epic #147's open-decision index identified
direct relevance to **OD-10, OD-11, OD-13, OD-86**, and the already-accepted **DL-62**. No new issues
were created, no existing issue was modified, and no acceptance was declared. Full detail in
[production-gaps-and-owner-review.md](production-gaps-and-owner-review.md) §7.

## 12. Limitations of This Pass

- Scope was narrowed, by explicit direction during execution, from the full production environment to
  the three named groups (Concierge automations + ungrouped, Concierge scripts, Concierge Automation
  Helpers). This is recorded transparently, not as a silent reduction.
- The writer of `input_boolean.alarm_primary_bedroom_ringing` (the trigger for the entire alarm chain)
  was not located within this pass's scope.
- `decision-ledger.md` Part 2's 68 individually open decisions were not each individually cross-checked
  against every finding (a lightweight, not exhaustive, correspondence list is provided instead).
- Dashboards, devices, areas/floors/labels beyond category resolution, and the Recorder database were not
  inspected.
- Live/dynamic behavior (actually triggering the alarm, actually speaking "who am I" to observe the real
  response) was **not** performed, consistent with the read-only/no-service-call production-safety
  constraint; several findings in this document are therefore "evidence of a broken reference" rather than
  "confirmed observed failure," and are worded accordingly throughout.

---

## Related artifacts in this set

1. [production-automation-inventory.csv](production-automation-inventory.csv)
2. [production-script-inventory.csv](production-script-inventory.csv)
3. [production-helper-inventory.csv](production-helper-inventory.csv)
4. [production-scene-inventory.csv](production-scene-inventory.csv)
5. [production-template-and-group-inventory.csv](production-template-and-group-inventory.csv)
6. [production-behavior-catalog.csv](production-behavior-catalog.csv)
7. [production-dependency-graph.md](production-dependency-graph.md)
8. [production-dynamic-room-assembly-analysis.md](production-dynamic-room-assembly-analysis.md)
9. [production-to-htbw-reconciliation-matrix.csv](production-to-htbw-reconciliation-matrix.csv)
10. [production-migration-protection-matrix.csv](production-migration-protection-matrix.csv)
11. [production-experience-regression-catalog.md](production-experience-regression-catalog.md)
12. [production-gaps-and-owner-review.md](production-gaps-and-owner-review.md)
13. [production-evidence-register.md](production-evidence-register.md)
14. [production-inventory-summary.json](production-inventory-summary.json)
