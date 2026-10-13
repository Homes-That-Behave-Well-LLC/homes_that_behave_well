# Production Experience Regression Catalog

> **Document status: Operational — discovery/evidence artifact.** Not architecture-of-record.
> Creates no authority.

Existing production regression scenarios are listed first, derived strictly from the evidence in
[production-automation-inventory.csv](production-automation-inventory.csv) and
[production-script-inventory.csv](production-script-inventory.csv). Future scenarios (not evidenced in
production) are listed separately and labeled as such, per the governing instruction.

---

## Part 1 — Existing production regression scenarios

### 1. A room-local voice request resolves devices without naming the room
**Status: PASS (evidenced).** `area_id(trigger.device_id)` resolves the room from whichever Home
Assistant Voice satellite heard the request, in all 18 Concierge conversation automations. No automation
in scope requires the resident to name the room.

### 2. Room-local lamps/lights/shades resolve correctly
**Status: PASS, with two known gaps.**
- Lamps vs. overhead lights resolve correctly via device Labels (BHV-01, BHV-04).
- Shades resolve correctly for percentage-based control in any room (BHV-03).
- Shade open/close (verb-only, no percentage) only resolves in 4 hardcoded rooms (Den, Dining Room,
  Living Room, Primary Bedroom) and **silently does nothing** in any other room (BHV-02).

### 3. The correct room audio output is selected
**Status: PASS, with a fragile mechanism.** Sonos selection works via `select('search','sonos')` string
matching across every music/ducking/speech script. This works today because every Sonos entity_id
happens to contain the substring "sonos," but it is not a declared relationship and would silently
misbehave if that naming convention were ever violated (e.g., a renamed or newly-added media_player
entity).

### 4. Active audio ducks or pauses when conversation begins
**Status: PASS (evidenced).** `automation.duck_sonos_when_any_assist_satellite_is_listening` (mode:
parallel) ducks the relevant room's Sonos the instant any of 13 Home Assistant Voice satellites enters
`listening`, and restores the exact pre-duck volume afterward (12-second safety timeout).

### 5. The Home can hear the person over active room audio
**Status: PASS (evidenced, by the ducking mechanism in scenario 4).** No separate microphone-side
evidence (e.g., noise-cancellation configuration) was found or claimed; this scenario is evidenced only
at the "lower the competing audio" layer.

### 6. TTS/response is delivered through the correct room output
**Status: PASS, with one confirmed gap in scope.** `script.sonos_speak_with_ducking_room` routes to the
in-scope Sonos (ducking to the learned chat volume, speaking, restoring), or falls back to the local
voice assistant / Cloud TTS via `script.voice_assistant_speak_fallback` when no Sonos is in scope or the
room is bathroom-like. **Gap:** three leaf scripts (`continue_playing_room`, `what_s_playing_room`,
`why_did_you_play_this_room`) call a nonexistent `script.room_speak_sonos` instead of this controller, so
their responses are silently never delivered through any output at all.

### 7. Prior audio state and volume resume correctly
**Status: PASS for ducking and spoken-confirmation paths; NOT EVIDENCED for the alarm-escalation path.**
`sonos_speak_with_ducking_room` and `duck_sonos_while_assist_is_listening_room` both snapshot and
restore exact per-player volumes. The Primary Bedroom alarm's intended "restore room audio to pre-alarm
state" step (`script.room_audio_restore`) calls a script that does not exist anywhere in production —
this restoration **does not happen** for that specific flow.

### 8. Primary posture/routine commands behave consistently across equivalent rooms
**Status: PASS for the happy path; one confirmed implementation inconsistency.** Bedtime, Goodnight, and
Good Morning all work from both the Primary and Guest bedroom (and their paired bathrooms). However,
`concierge_bedtime`'s lamp-turn-on step targets 3 hardcoded Insteon `device_id`s for the Primary Bedroom
but targets generic `entity_id`s for the Guest Bedroom — the two "equivalent" rooms are not implemented
with the same mechanism, which is a latent maintenance risk even though the resident-facing outcome is
equivalent today.

### 9. Learning behaviors persist and are later honored
**Status: PASS (evidenced).** Both implicit (automatic, on every manual light adjustment) and explicit
("remember this") learning write to the same `input_number.*_learned_brightness` /
`input_text.*_speaker_profile` helpers that the "usual" scripts read back. Verified end-to-end via the
write-side automations/scripts and the read-side `turn_on_lamps_usual_room` / `turn_on_lights_usual_room`
/ `start_music_usual_room`.

### 10. Explainability queries ("what's playing," "why did you play this") are answered truthfully
**Status: BROKEN (evidenced).** Both queries compute a correct, evidence-based answer from the
structured last-media audit trail, but neither answer is ever actually spoken, due to the broken
`script.room_speak_sonos` reference documented in §9 of
[production-dependency-graph.md](production-dependency-graph.md). This is a confirmed regression
relative to the scripts' own documented intent, not a speculative gap.

### 11. A safety-relevant wake/alarm behavior performs as described
**Status: MAJOR REGRESSION (evidenced).** The Primary Bedroom alarm escalation ladder's Started,
Escalation, and Stop stages each call a script that either does not exist or has the wrong entity_id;
only the Repeat stage's script call resolves to a real script, and that script's own audio-playback
parameter is unused by its callee. See
[production-gaps-and-owner-review.md](production-gaps-and-owner-review.md) for the explicit
owner-verification request — this is the single highest-priority item in this entire inventory.

### 12. Household-specific music identity (genre tracking) persists over time
**Status: PASS (evidenced).** 19 lifetime per-genre counters are incremented by
`automation.music_genre_observe_playback_all_sources` and exposed via `sensor.house_top_music_genre`.

---

## Part 2 — Future scenarios (NOT evidenced in production; labeled explicitly as future)

The following are named in the governing prompt as scenarios to evaluate. **No production evidence was
found for any of them in the 26 in-scope automations or 44 in-scope scripts.** They are recorded here as
explicitly future/aspirational, not as production gaps, because nothing in the reviewed scope claims to
implement them today.

- **Compound commands** (e.g., "turn off the lights and lock the door") — no automation in scope parses
  or routes a multi-intent single utterance; each conversation trigger matches one semantic family.
- **Conversational referent continuity** (e.g., "turn it down" referring to something named two turns
  ago) — no state machine for pronoun/referent resolution across turns was found; each automation
  resolves intent from the current utterance alone.
- **Ephemeral delayed commands** (e.g., "turn off the lights in 10 minutes") — no `delay`-then-conditional
  pattern tied to a spoken duration was found in any in-scope automation; the `delay:` steps that do
  exist are all fixed, short, internal implementation delays (e.g., `00:00:01` before a service call),
  not resident-specified durations.
- **Condition/outcome statements** (e.g., "if it rains, close the windows") — no conditional-rule
  authoring mechanism triggered by voice was found; all conditions in scope are developer-authored inside
  automation/script YAML, not resident-authored at runtime.
- **Single-conversation arbitration across overlapping voice surfaces** (e.g., two satellites in the same
  Merged Room both hearing the same utterance) — the Duck Sonos automation's `mode: parallel` allows
  multiple satellites to duck independently and concurrently, but no evidence was found of explicit
  "which satellite owns this conversation" arbitration; HA's own Assist pipeline routing (outside this
  pass's scope) may already handle this at a layer not reviewed here.
