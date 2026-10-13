# Dynamic Room Assembly Analysis

> **Document status: Operational — discovery/evidence artifact.** Not architecture-of-record.
> Creates no authority. Does not amend `decision-ledger.md`, `authority-order.md`, or any canonical
> model/contract. Produced under the HTBW Execution Grounding Standard
> ([../../governance/htbw-architecture-execution-grounding-standard.md](../../governance/htbw-architecture-execution-grounding-standard.md)).

**Scope of this pass:** the 18 automations and 44 scripts in the production `Concierge` category, plus
the 8 "ungrouped" automations named in the governing prompt. Full per-item evidence is in
[production-automation-inventory.csv](production-automation-inventory.csv) and
[production-script-inventory.csv](production-script-inventory.csv).

---

## 1. Why this analysis exists

[adr-room-configuration-ownership.md](../../architecture/adr-room-configuration-ownership.md) (**DL-09,
DL-10, DL-11, DL-13**) decides that Room Configuration — not Concierge — owns what a Room means: which
devices **participate**, which are **exposed** for address, which have **authority** to be acted on, and
which vocabulary terms resolve to them. The ADR explicitly prohibits two things production does
constantly:

> "Room Help must be derived from the configured exposed capability set and vocabulary, never generated
> from raw device inventory." (ADR, section 8)

> Concierge "must not runtime-search devices to satisfy a vocabulary term" and "must not select sensors
> at runtime." (`concierge-contract.md`, hard prohibitions #2–#3)

Production's Concierge implementation was built **before** this ADR and does both of these things, in
every room-aware script, every time it runs. This document inventories exactly what is dynamically
derived today, why it is there, what household outcome it produces, and what it must become at HTBW
setup time.

---

## 2. Entry-point scripts that perform dynamic room assembly

| Script | What it discovers at runtime |
|---|---|
| `script.room_audio_resolver_keystone` | Sonos/media-player membership, assist-satellite fallback target, "bathroomish" output-mode bias, presence/environment/air-quality/noise capability inference, self-healing speaker-profile seed |
| `script.sonos_speak_with_ducking_room` | Identical Sonos/assist-satellite/bathroomish discovery (duplicated independently) |
| `script.room_abilities_speak_unified` | Lamp vs. overhead-light classification, shade/cover membership, Sonos membership, AppleTV membership, wake-word lookup |
| `script.room_capabilities_snapshot_debug` | Identical lamp/light/shade/Sonos discovery, exposed as an owner debug notification |
| `script.concierge_follow_up_commands_ha_voice` (automation) | Identical lamp/light/Sonos/AppleTV discovery inline inside an automation, not even a script |
| `script.concierge_lighting_percentage_catcher_ha_voice` (automation) | Identical lamp/light discovery inline |
| `script.turn_on_lamps_usual_room` / `turn_on_lights_usual_room` / `learn_lighting_usual_room` | Lamp vs. light classification (repeated a fourth/fifth/sixth time) |
| `script.speak_room_temperature` / `_humidity` / `_light_level` / `_noise_level` / `_air_quality` / `_air_quality_ai_assessment` | Per-metric sensor selection via entity-id regex (Air-Q preferred, multi-sensor fallback) |
| `script.resolve_music_player_room` / `start_music_usual_room` / `play_genre_room` / `play_artist_room` / `play_album_room_ma` / `ensure_main_living_area_sonos_group` | Sonos membership plus an independently hardcoded "Main Living Area" (Kitchen+Dining Room+Living Room) zone, duplicated across **5 separate scripts** |

## 3. What each discovery mechanism does, and why it exists today

### 3.1 Lamp vs. overhead-light classification

**Discovers:** `area_entities(room) → light domain → label_devices('Lamps') / label_devices('Lights')
intersect`. Any light belonging to neither label falls through to "overhead."

**Why it is needed today:** Home Assistant has no native "lamp vs. ceiling light" distinction. The
household expresses this distinction through **device Labels** (`Lamps`, `Lights`, `AppleTV`), and every
lighting script re-derives the intersection with the current room's lights live, every single
invocation.

**Beneficial behavior enabled:** "lamps on," "lights usual," and "what can I do here" all correctly
distinguish lamps from overhead lighting without the household ever naming individual fixtures.

**Household outcome:** a resident can say "turn on the lamps" or "turn on the lights" in any room and
get exactly the fixtures they mean, even though HA's own light domain makes no such distinction.

**Maps to HTBW setup-time configuration as:** a per-light-entity **Participation + Exposure** record
inside Room Configuration, carrying an explicit "lamp" vs. "overhead light" exposure classification —
replacing the Label lookup with a configured fact. (`adr-room-configuration-ownership.md`, DL-11.)

### 3.2 Shade/cover membership

**Discovers:** `area_entities(room) → cover domain`, optionally narrowed to `device_class` in
`{shade, blind, curtain, awning}`.

**Beneficial behavior enabled:** percentage-based shade/blind control (BHV-03) works in any room with
covers, with no per-room configuration today.

**Household outcome:** "set the shades to 40 percent" works correctly regardless of how many covers
exist in the room.

**Maps to HTBW setup-time configuration as:** Room Configuration cover-group **Participation**,
replacing live `cover` domain discovery.

### 3.3 Sonos/media-player membership and "active player" selection

**Discovers:** `area_entities(room) → media_player domain → string search for "sonos"` (fragile —
depends on every Sonos entity_id literally containing the substring "sonos"), then prefers whichever is
currently `playing`, else the first found (or alphabetically first, depending on the script).

**Beneficial behavior enabled:** every voice-driven music behavior (BHV-05, 07–10, 16, 23–24, 27)
depends on this resolution.

**Household outcome:** music commands "just work" in any room with a Sonos speaker, without ever naming
the speaker.

**Maps to HTBW setup-time configuration as:** Room Configuration media-player **Participation**, with an
explicit "preferred output" designation per room/Merged Room — replacing string-matching with a
configured relationship. (See also §5, Main Living Area.)

### 3.4 Assist-satellite fallback / "bathroomish" output-mode bias

**Discovers:** `area_entities(room) → assist_satellite domain`, and a **hardcoded regex**
(`room_resolved | regex_search('bath|powder', ignorecase=True)`) that biases speech toward the local
voice assistant instead of Sonos for any room whose slug contains "bath" or "powder."

**Beneficial behavior enabled:** bathrooms (which may have a Sonos Beam used for TV audio rather than a
freestanding speaker) still get spoken confirmations through the room's voice assistant instead of a
TV-audio device.

**Household outcome:** announcements are audible in every room, including rooms whose best speaker is
unsuitable for incidental chat.

**Maps to HTBW setup-time configuration as:** an explicit **preferred response surface** per room
(Room Configuration), replacing a string-matched heuristic that would misclassify, for example, a future
room named "Bath House Studio" that is not actually a bathroom.

### 3.5 Presence/environment/air-quality/noise capability inference

**Discovers:** `area_entities(room) → binary_sensor/sensor domain`, matched against entity-id regex
patterns for `_occupancy_sensor|_presence_sensor` (→ `has_presence`) and `^sensor\.airq_` (→
`has_airq`/`air_quality_level`/`has_noise`).

**Beneficial behavior enabled:** BHV-14 and BHV-15 (room monitoring-awareness and sensor-value queries)
capability-gate their answers so the Home never claims a sensing ability it does not have.

**Household outcome:** asking "what can this room monitor" or "how loud is it" gets a truthful,
room-specific answer.

**Maps to HTBW setup-time configuration as:** a per-room declared **sensing capability set** plus, per
metric, a declared **Primary Authority** sensor (`concierge-contract.md` hard prohibition #2; **DL-62**)
— replacing regex-based sensor selection entirely. This is also where the documented conflict is
sharpest: the ADR and Contract already say runtime sensor selection must not happen, and production does
exactly that in every `speak_room_*` script.

### 3.6 "Main Living Area" (Merged Room) zone

**Discovers:** nothing at runtime — this one is a **hardcoded literal list**
(`['kitchen', 'dining_room', 'living_room']`) duplicated independently inside **5 separate scripts**
(`resolve_music_player_room`, `start_music_usual_room`, `play_genre_room`, `play_artist_room`,
`play_album_room_ma`, `room_abilities_speak_unified`, `ensure_main_living_area_sonos_group` — 7 call
sites across the file).

**Beneficial behavior enabled:** Kitchen, Dining Room, and Living Room share one Sonos group and one
"usual music" profile, so playing music in any one of the three plays in all three.

**Household outcome:** an open-plan living area behaves like one room for music purposes.

**Maps to HTBW setup-time configuration as:** this is **exactly** the canonical **Merged Room** concept
HTBW already defines (**DL-12, DL-13**: "A Room and a Merged Room behave identically... there is no
separate orchestration path for merged rooms"). Production has independently hardcoded the Merged Room
concept 5–7 times instead of declaring it once. This is the single most directly actionable finding in
this entire review: replace 5–7 duplicated literal lists with **one** Merged Room configuration record.

### 3.7 Wake-word lookup for example phrases

**Discovers:** `states('select.voice_assistant_<room>_wake_word')`, falling back to "Jarvis" if
undefined.

**Beneficial behavior enabled:** the "what can I do here" response uses the resident's actually
configured wake word in its example phrases rather than a hardcoded generic one.

**Household outcome:** spoken example commands sound natural and match what the resident would actually
say.

**Maps to HTBW setup-time configuration as:** this one is already close to correct — it reads a
configured `select` entity rather than inferring anything, and is the one piece of "room vocabulary"
already externalized from script logic. It should migrate as-is into Room Configuration's vocabulary
model.

---

## 4. How ambiguity, exclusion, and missing capability are handled today

| Situation | Current production behavior |
|---|---|
| Room has no lamps/lights matching a requested category | Silent no-op (no refusal spoken) — BHV-01/04 |
| Room has no scene mapping for shade open/close | Silent no-op (no refusal spoken) — BHV-02 |
| Room has no matching sensor for a value query | Graceful spoken refusal via `speak_capability_not_available` — BHV-15 |
| Room has no Sonos and no assist satellite | `output_mode = 'none'`, no speech attempted — all `sonos_speak_with_ducking_room` callers |
| Duplicate/ambiguous Sonos entities in scope | Prefers the currently `playing` one; else first found (order is not deterministic across all call sites — some use `| sort | first`, others do not) |
| Device explicitly excluded (e.g., Sonos Beam) | Hardcoded `reject('search','_beam$')` in the music/ducking scripts — **this is production's only real instance of the "deliberate exclusion" concept** the Room Configuration ADR names explicitly (see the ADR's "Sonos Beam... EXCLUDED from Speakers" worked example) |
| Merged-space/adjacent-room handling | Only the Main Living Area case exists, and only for music; no other room is ever treated as merged for any other capability |

**Finding:** capability-value queries (temperature/humidity/etc.) degrade gracefully with a spoken
refusal; capability-control commands (lamps/lights/shades) frequently degrade **silently**. This
inconsistency should be resolved — one way or another — when these behaviors move to a governed
implementation.

---

## 5. Runtime cost and complexity observed

- The lamp/light label-classification Jinja block (`label_devices('Lamps') | map('device_entities') |
  sum(start=[]) | intersect(room_lights) | ...`) is copied, **character-for-character identical**, into
  at least 6 different scripts/automations (§3.1).
- The Sonos string-search discovery pattern (`area_entities(room) | ... | select('search','sonos')`) is
  copied into at least 12 different scripts/automations.
- The "Main Living Area" hardcoded room list is copied into 7 call sites across 6 scripts.
- The bedroom/bathroom pairing lookup (`Primary Bedroom`/`Primary Bathroom` → `primary`;
  `Guest Bedroom`/`Guest Bathroom` → `guest`) is duplicated inline in 3 automations
  (`bedtime_concierge`, `goodnight_concierge`, `good_morning_concierge`) **despite a dedicated
  `script.resolve_bedroom_context` existing that does exactly this and is never called by any of them.**
- The 19-entry genre-to-spoken-phrase map (`genre_speak_map`) is duplicated verbatim in at least 2
  scripts (`what_s_playing_room`, `why_did_you_play_this_room`).
- The `room_phrase` friendly-name lookup (`tom_s_office` → "Tom's Office", `david_s_office` → "David's
  Office") is duplicated verbatim in at least 7 scripts.

This is the direct, measurable cost of runtime discovery without a shared configuration layer: every
behavior that needs "what belongs to this room" re-derives it, and every mapping that needs updating
(e.g., adding a lamp, renaming a room, changing the Main Living Area boundary) must be changed in
5–12 places by hand, with no mechanism to detect a missed location.

---

## 6. Summary mapping table

| Current runtime-derived value | Evidence source | Household outcome enabled | Future HTBW setup-time field/relationship | Migration requirement | Validation scenario |
|---|---|---|---|---|---|
| Lamp vs. overhead-light membership | `label_devices('Lamps'/'Lights')` in 6+ places | Correct fixture class responds to "lamps"/"lights" | Room Configuration per-light Participation+Exposure classification | Capture every light's lamp/overhead classification at setup | Say "lamps on" / "lights on" in every room, confirm correct class responds |
| Shade/cover membership | `area_entities → cover domain` | "set shades to N%" works in any covered room | Room Configuration cover-group Participation | Capture every room's cover membership | Set a percentage in every shaded room |
| Shade open/close scene mapping | hardcoded 4-room dict in 1 automation | "open/close shades" works in 4 rooms today (silently fails elsewhere) | Room Configuration shade-scene/cover-group binding, for **every** shaded room | Extend coverage beyond today's 4 rooms during replacement | "open/close shades" in every shaded room, confirm no silent failures |
| Sonos/media-player membership + active-player selection | `select('search','sonos')` in 12+ places | Music commands resolve to the right speaker without naming it | Room Configuration media-player Participation + preferred-output designation | Capture every room's media-player participation | Trigger music commands in every music-equipped room |
| Assist-satellite fallback / "bathroomish" bias | hardcoded regex on room slug | Announcements audible even where Sonos is unsuitable | Room Configuration declared preferred response surface | Capture explicit preferred-surface per room instead of inferring from name | Trigger an announcement in a bathroom-like room and a falsely-matching room name |
| Presence/environment/air-quality/noise capability flags | entity-id regex matching | Truthful "what can this room monitor" / gated sensor answers | Room Configuration declared sensing-capability set + per-metric Primary Authority (DL-62) | Capture every room's sensing capability and authoritative sensor | Query every metric in rooms with 0, 1, and 2+ candidate sensors |
| "Main Living Area" zone (Kitchen+Dining+Living) | hardcoded literal list, 7 call sites | Open-plan area behaves as one room for music | A single Merged Room configuration record (DL-12, DL-13) | Replace 7 duplicated hardcodes with 1 configuration relationship | Trigger music/ability-discovery from each of the 3 constituent rooms |
| Bedroom↔bathroom pairing | hardcoded dict, duplicated in 3 automations (despite an unused dedicated script existing) | "Bedtime"/"Goodnight"/"Good Morning" work from either the bedroom or its bathroom | Room Configuration room-pairing relationship | Replace 3 duplicated inline dicts with 1 relationship; retire the now-genuinely-used `resolve_bedroom_context` | Say each bedtime phrase from both the bedroom and its bathroom |
| Wake word per room | `select.voice_assistant_<room>_wake_word` (already configured, not inferred) | Natural-sounding example phrases | Carry forward as-is into Room Configuration vocabulary | Direct migration, no behavior change needed | Confirm "what can I do here" uses the correct wake word per room |

---

## 7. What must NOT be inferred as implemented

This document describes **current production implementation evidence only**. It is explicitly **not**
the HTBW target design. Per the governing instruction:

- Do not read this document as proposing exact HTBW field names — none beyond those already defined in
  `room.md` / `room-configuration.md` / `contextual-vocabulary.md` are implied here.
- Do not read any "Maps to HTBW setup-time configuration as" line as authorization to design or build
  that configuration now. These are migration-requirement observations for later architecture reasoning.
- Where a gap has no accepted HTBW owner today (e.g., "preferred response surface," "duck-while-listening
  policy"), this document says so plainly rather than inventing one.
