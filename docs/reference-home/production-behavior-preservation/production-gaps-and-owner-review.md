# Production Gaps and Owner Review

> **Document status: Operational — discovery/evidence artifact.** Not architecture-of-record.
> Creates no authority. Does not decide any of the questions below — they are recorded for Tom and/or
> future architecture review, per the governing instruction.

---

## 1. SAFETY-RELEVANT — Primary Bedroom alarm-clock escalation ladder (highest priority)

**What was found:** three of the four stages of the Primary Bedroom alarm escalation automation chain
call a script entity that either does not exist in production at all, or does not match the real
script's entity_id:

| Stage | Automation | Calls | Status |
|---|---|---|---|
| Started | `automation.primary_bedroom_alarm_started` | `script.turn_on_lamps_usual` | **Does not exist** (real script: `turn_on_lamps_usual_room`) |
| Repeat | `automation.primary_bedroom_alarm_repeat` | `script.primary_bedroom_play_alarm_chime` | Exists, but its only callee (`sonos_speak_with_ducking_room`) ignores the `media_source` parameter it is passed, so the chime audio file is never actually played |
| Escalation | `automation.primary_bedroom_alarm_escalation` | `script.room_audio_duck_and_play` | **Does not exist anywhere in production** |
| Stop | `automation.primary_bedroom_alarm_stop` | `script.room_audio_restore` | **Does not exist anywhere in production** |

All four findings were confirmed by direct `grep` against the live production `automations.yaml` and
`scripts.yaml` (line numbers recorded in
[production-dependency-graph.md](production-dependency-graph.md) §9). This was not inferred, assumed, or
estimated.

**Why this is being escalated above every other finding:** this is the one behavior in the entire
inventory where the gap between "what the automation's own alias/description says it does" and "what the
evidence shows it can actually do" is large enough to plausibly affect whether a resident is woken up as
intended.

**What this document does NOT do:** it does not claim the alarm "doesn't work" in the sense of failing to
ring at all — `input_boolean.alarm_primary_bedroom_ringing` and its state-change triggers are correctly
wired, and the chime script **is** called repeatedly. It does not claim any resident has actually been
affected. It does not identify what, if anything, externally compensates (a phone alarm, a smart-watch
alarm, etc., which are entirely plausible and outside this review's static-file evidence).

**Owner-review questions for Tom:**
1. Is there an external/legacy alarm mechanism (a phone app, a different smart-speaker routine, etc.)
   that already compensates for these gaps today, independent of this automation chain?
2. What sets `input_boolean.alarm_primary_bedroom_ringing` to `on` in the first place? It was not found
   among the 26 in-scope automations or 44 in-scope scripts reviewed in this pass — locating that writer
   is a prerequisite to understanding the full chain.
3. Would you like this fixed as a same-behavior production bug-fix (within the read-only constraints of
   this task, this review cannot make that change itself), or would you prefer to hold it entirely for
   the eventual HTBW replacement?

---

## 2. Six confirmed broken/orphaned script references (beyond the alarm chain above)

| # | Caller | Broken target | Likely correct target | Effect |
|---|---|---|---|---|
| 1 | `script.continue_playing_room` | `script.room_speak_sonos` | `script.sonos_speak_with_ducking_room` | "Nothing queued" fallback speech silently fails |
| 2 | `script.what_s_playing_room` | `script.room_speak_sonos` | `script.sonos_speak_with_ducking_room` | "What's playing" answer computed but never spoken |
| 3 | `script.why_did_you_play_this_room` | `script.room_speak_sonos` | `script.sonos_speak_with_ducking_room` | "Why did you play this" answer computed but never spoken |
| 4 | `automation.voice_play_jazz` ("Voice – Music Follow-Ups") | `script.whats_playing_room` | `script.what_s_playing_room` | The "what's playing" voice phrase never even reaches script #2 above |
| 5 | `script.speak_room_air_quality` | `script.speak_room_air_quality_assessment` | `script.speak_room_air_quality_ai_assessment` | The fully-implemented AI air-quality assessment is permanently unreachable from normal voice use |
| 6 | `automation.concierge_identity_self_query_ha_voice` | service `concierge.execute` | *(unknown — no `concierge` integration found installed)* | "Who am I" query's target existence is unconfirmed |

**Pattern observed:** findings 1–3 and 4 strongly suggest a script was once named `room_speak_sonos` (or
similar), was later renamed to `sonos_speak_with_ducking_room` and `what_s_playing_room` respectively,
and the rename was not propagated to every call site. Finding 5 is a simple naming typo
(`_assessment` vs. `_ai_assessment`). Finding 6 is categorically different — it is not a typo, but a call
to an entire integration that does not appear to be installed.

**Owner-review questions for Tom:**
1. Do you recall renaming a "speak via Sonos" script at some point? If so, when, and were these four
   call sites (continue_playing_room, what_s_playing_room, why_did_you_play_this_room, and the
   Music Follow-Ups automation) known to still reference the old name?
2. Was `script.speak_room_air_quality_assessment` vs. `_ai_assessment` ever caught before? Has anyone
   ever actually heard the AI-generated air-quality assessment spoken aloud?
3. Is `concierge.execute` a real, currently-working service call in this production instance under an
   integration this static-file review did not identify (e.g., a pyscript/AppDaemon script registering a
   custom service, rather than a conventional `custom_components` folder)? A live test (saying "who am
   I" and observing what happens) would resolve this definitively; this review could not safely do that
   under its read-only/no-service-call constraint.

---

## 3. Additional confirmed implementation defects (lower severity, still evidence-based)

1. **`script.surprise_me_room` debug-notification Jinja bug:** the notification message ends with the
   literal text `selected_genre` instead of `{{ selected_genre }}` — the actual randomly-chosen genre
   name is never substituted into the debug notification (the real `play_genre_room` call that follows
   it is unaffected and receives the correctly-evaluated variable).
2. **`speak_room_noise_level` regex-grouping risk:** the sensor-matching pattern
   `'^sensor\.airq_.*noise|sound|decibel|db'` lacks grouping parentheses around the alternation, so only
   the first branch is anchored to the `airq_` prefix — in a room with a non-Air-Q sensor whose entity_id
   happens to contain "sound," "decibel," or "db," it could match a sensor the script's own description
   says is explicitly out of scope ("noise... Air-Q only"). Not confirmed to have actually misfired in
   this production instance (would require a matching non-Air-Q sensor name to exist in some room), but
   recorded as a risk.
3. **Volume-clamp drift between `room_audio_resolver_keystone` and `sonos_speak_with_ducking_room`:** the
   two scripts duplicate near-identical speaker-profile parsing logic, but clamp `chat_volume`'s maximum
   differently (0.60 in Keystone vs. 0.70 in the ducking-speak script). Low household impact, but a clear
   example of the duplication risk documented throughout
   [production-dynamic-room-assembly-analysis.md](production-dynamic-room-assembly-analysis.md).
4. **Speaker-profile schema drift risk:** `start_music_usual_room` writes extra `last_source` /
   `last_media_type` keys into a room's `input_text.*_speaker_profile` JSON that `learn_music_volume_room`
   does not know about and would silently drop on its next write to the same helper.
5. **`concierge_good_morning` calls `script.kiosk_set_day_mode` twice in direct succession** — harmless
   (idempotent REST calls) but apparently an unintentional duplicate step.
6. **Three bedroom/bathroom-pairing mappings are hand-duplicated** in `bedtime_concierge`,
   `goodnight_concierge`, and `good_morning_concierge`, **despite a dedicated
   `script.resolve_bedroom_context` existing that performs exactly this mapping and is never called by
   any of the three.** A future maintenance change to the mapping (e.g., adding a third bedroom) would
   need to be made in 3 places and could easily miss one.
7. **Inconsistent Primary vs. Guest bedroom lamp-targeting strategy** in `concierge_bedtime`: Primary
   targets 3 hardcoded Insteon `device_id`s; Guest targets generic `light.*` `entity_id`s. Functionally
   equivalent today, structurally inconsistent.

---

## 4. Security finding — hardcoded plaintext credential

**What was found:** the Fully Kiosk Browser admin password appears as a **plaintext script variable**
(not a `!secret` reference into `secrets.yaml`) in all four kiosk-related scripts
(`living_room_fully_kiosk_provisioning`, `bedroom_fully_kiosk_provisioning`, `kiosk_set_overnight_mode`,
`kiosk_set_day_mode`). The same literal value is repeated across all four. The value itself is **redacted
in every artifact produced by this inventory**, consistent with this task's "do not reproduce secrets"
instruction; only its existence and pattern are recorded here.

**Why this matters regardless of any HTBW decision:** this is a production hygiene issue independent of
migration — the credential is both committed into the automation configuration (and therefore present in
any backup, export, or future repository capture of this production instance) and transmitted as a
plaintext HTTP GET query parameter on the local network.

**Owner-review questions for Tom:**
1. Would you like this moved to `secrets.yaml` (referenced via `!secret`) as a standard Home Assistant
   hygiene improvement, independent of any HTBW migration timeline? This review is not authorized to make
   that change itself (production is read-only for this task), but flags it as a low-risk, high-value fix
   whenever you choose to apply it.
2. Should the device IP addresses (also hardcoded alongside the password) be reviewed for the same
   treatment, or are they considered non-sensitive in your household's threat model?

**This question is tracked, not duplicated, in [Hard-Coded Topology Audit and Remediation (#197)](https://github.com/Homes-That-Behave-Well-LLC/homes_that_behave_well/issues/197)**, which applies the
DL-89 technical-debt recording convention drafted by
[adr-stable-endpoint-identity-and-network-boundary-independence.md](../../architecture/adr-stable-endpoint-identity-and-network-boundary-independence.md)
(pending #195) to this and other hard-coded endpoint references.

---

## 5. Unknown-purpose items — DO NOT REMOVE

| Item | Why it is flagged |
|---|---|
| `input_boolean.daily_lights` | Not read or written by any of the 26 in-scope automations or 44 in-scope scripts |
| `input_boolean.bedtime_toggle` | Same |
| `input_boolean.good_morning_toggle` | Same |
| `input_boolean.good_night_toggle` | Same |
| `input_boolean.{primary_bedroom,guest_bedroom,kitchen,den}_alarm_enabled` (4 helpers) | No in-scope reader or writer found; only the `*_ringing` counterpart for Primary Bedroom is wired into an automation chain |
| `input_boolean.{guest_bedroom,kitchen,den}_alarm_ringing` (3 helpers) | No in-scope automation chain wired to these, unlike the Primary Bedroom one |
| `input_text.music_genre_determination` | Not read or written in scope; `determine_music_genre_audit` writes directly to the per-room last-media helper instead |
| `input_datetime.speaker_profile_last_media_last_updated` | Not read or written in scope, despite its name implying a counterpart to `update_last_media_room` |
| `input_number.dining_room_art_learned_brightness_2` | Apparent duplicate of `input_number.dining_room_art_learned_brightness`; purpose of the `_2` suffix not confirmed |
| `input_number.laundry_room_lights` | Does not follow the household's own `<light>_learned_brightness` naming convention; purpose not confirmed |
| `automation.test_automation` | Enabled, no trigger, appears to be a development/test artifact (also independently flagged by the 2026-10-07 prior Reference Home discovery pass) |

**Per the governing instruction, none of the above are recommended for removal, disabling, or renaming by
this review.** They are recorded so a future owner/architecture review has the evidence needed to decide
their disposition.

---

## 6. Items with no identified HTBW responsibility owner

See [production-to-htbw-reconciliation-matrix.csv](production-to-htbw-reconciliation-matrix.csv) rows
classified `Production behavior has no identified HTBW owner`: TV/AppleTV control (BHV-06), album
playback via Music Assistant (BHV-10), kiosk dashboard switching and provisioning (BHV-21, BHV-22), and
music-genre popularity tracking (BHV-23). None of these require urgent owner attention — they are
recorded as architecture-scope gaps for later roadmap/epic triage, not as defects.

---

## 7. Open-Issue Impact Review (lightweight, per this pass's narrowed scope)

Epic **#147** tracks 68 genuinely open architecture decisions (OD-01 through OD-76, less 8 already
resolved/closed) via one child issue per decision. This pass did not perform an exhaustive per-issue
cross-check against all 68 (out of proportion to this pass's narrowed automations/scripts/helpers scope,
per direction received during this task), but the following direct correspondences were identified and
are recorded for a future, dedicated Open-Issue Impact Review:

- **OD-10 (Floors as a first-class scope), OD-11 (a Physical Room in more than one Room), OD-13
  (vocabulary inheritance)** — directly relevant to the "Main Living Area" Merged Room finding (BHV-27)
  and the bedroom/bathroom pairing finding (BHV-17/18/19). A future Open-Issue Impact Review should check
  whether either open decision's acceptance criteria already anticipate this production evidence.
- **OD-86 (household consequence of changing/withdrawing a vocabulary term)** — directly relevant to any
  future change to the device-Label-based lamp/light/AppleTV vocabulary this review found production
  depends on in 6+ places.
- **DL-62 (Primary Authority sensor declared by Room Configuration)** — already-accepted decision in
  direct, documented conflict with production's runtime sensor-selection pattern (BHV-15, BHV-28); this
  is not an open decision requiring a new issue, but an acceptance-criteria question for whatever issue
  eventually implements Room Configuration's sensor-authority field, since production evidence now exists
  to ground acceptance scenarios.

**No new GitHub issues were created, no existing issue was commented on, and no label/milestone/state was
changed by this review, per the governing instruction.**
