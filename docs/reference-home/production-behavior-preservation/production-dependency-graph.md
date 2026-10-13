# Production Dependency Graph — Concierge Automations, Scripts, and Helpers

> **Document status: Operational — discovery/evidence artifact.** Not architecture-of-record.
> Creates no authority.

Human-readable relationship chains for the 26 in-scope automations, 44 in-scope scripts, and the
helpers/scenes/templates they touch. Machine-readable equivalents are in
[production-automation-inventory.csv](production-automation-inventory.csv),
[production-script-inventory.csv](production-script-inventory.csv), and
[production-inventory-summary.json](production-inventory-summary.json).

---

## 1. The voice-entry layer → central controller fan-in

Nearly every voice-triggered automation ultimately funnels through one of two central scripts:

```
Dashboard / Voice command (conversation trigger)
  -> entry-point automation (room-matching conversation sentences)
    -> room_resolved = area_id(trigger.device_id)
      -> [branches per automation]
        -> script.sonos_speak_with_ducking_room   (confirmation speech + ducking + restore)
        -> script.room_audio_resolver_keystone     (capability-gated discovery + routing hub)
```

```
automation.concierge_voice_entry_ha_voice ("what can I do here")
  -> script.room_abilities_speak_unified
       -> script.ensure_main_living_area_sonos_group (Main Living Area only)
       -> script.sonos_speak_with_ducking_room
            -> script.voice_assistant_speak_fallback (if no Sonos in scope)

automation.concierge_room_monitoring_awareness_ha_voice ("what can this room monitor")
  -> script.room_audio_resolver_keystone (speak_awareness=true)
       -> script.room_monitoring_abilities_speak
            -> script.sonos_speak_with_ducking_room

automation.concierge_follow_up_sensor_queries_ha_voice ("what's the temperature" etc.)
  -> script.room_audio_resolver_keystone (speak_temperature/humidity/light_level/air_quality/noise)
       -> script.speak_room_temperature      -> script.sonos_speak_with_ducking_room
       -> script.speak_room_humidity         -> script.sonos_speak_with_ducking_room
       -> script.speak_room_light_level      -> script.sonos_speak_with_ducking_room
       -> script.speak_room_air_quality       -> [BROKEN gate -> manual readout] -> script.sonos_speak_with_ducking_room
            (intended but unreachable: -> script.speak_room_air_quality_ai_assessment -> ai_task.generate_data -> script.sonos_speak_with_ducking_room)
       -> script.speak_room_noise_level       -> script.sonos_speak_with_ducking_room
       -> [if nothing applicable] script.speak_capability_not_available -> script.sonos_speak_with_ducking_room
```

---

## 2. Lighting / shade / music / TV — bare-command follow-ups

```
automation.concierge_follow_up_commands_ha_voice ("lamps on", "lights off", "shades open",
                                                   "music pause", "tv on", ...)
  -> room_resolved = area_id(trigger.device_id)
  -> parallel:
       - script.sonos_speak_with_ducking_room (spoken confirmation)
       - [branch action]:
           lamps  -> light.turn_off | script.turn_on_lamps_usual_room
           lights -> light.turn_off | script.turn_on_lights_usual_room
           shades -> scene.turn_on (hardcoded 4-room scene map; silent no-op elsewhere)
           music  -> media_player.media_pause / media_stop / media_play
           tv     -> media_player.turn_off / turn_on

automation.concierge_shade_percentage_catcher_ha_voice ("set shades to 40%")
  -> script.sonos_speak_with_ducking_room (confirmation)
  -> cover.set_cover_position (live-discovered covers)

automation.concierge_lighting_percentage_catcher_ha_voice ("dim lights to 20%")
  -> script.sonos_speak_with_ducking_room (confirmation)
  -> light.turn_on/off (live-discovered lamps/lights)
```

---

## 3. Music chain (play / continue / genre / artist / album / surprise)

```
automation.voice_play_music ("play music")
  -> script.start_music_usual_room
       -> script.resolve_music_player_room       [response_variable: sonos_player, ma_player]
       -> media_player.volume_set / play_media / media_play
       -> script.update_last_media_room
            -> input_text.<room>_speaker_profile_last_media (write)

automation.voice_continue_playing ("continue playing")
  -> script.continue_playing_room
       -> media_player.media_play                        (if paused)
       -> script.start_music_usual_room                  (if idle)
       -> script.room_speak_sonos   ** BROKEN — no such script; dead end **

automation.voice_play_jazz ("Music Follow-Ups": genre/artist/surprise/what's-playing/why)
  -> media_player.media_pause                            (stop/pause/off branch)
  -> script.continue_playing_room                         (resume branch, see above)
  -> script.surprise_me_room  -> script.play_genre_room -> script.ensure_main_living_area_sonos_group
                                                         -> input_select.<key>_music_posture (write)
                                                         -> media_player.media_stop / play_media
  -> script.play_genre_room                               (named-genre branch, same as above)
  -> script.play_artist_room -> script.ensure_main_living_area_sonos_group
                              -> media_player.media_stop / play_media (on *_sonos_ma) / media_play
  -> script.whats_playing_room   ** BROKEN entity_id — real script is what_s_playing_room; dead end **
  -> script.why_did_you_play_this_room -> script.room_speak_sonos  ** BROKEN — dead end **

script.what_s_playing_room (only reachable by direct service-call today, not via the automation above)
  -> input_text.<room>_speaker_profile_last_media (read)
  -> script.room_speak_sonos  ** BROKEN — dead end; the computed answer is never spoken **

script.play_album_room_ma (no confirmed in-scope voice entry point)
  -> script.ensure_main_living_area_sonos_group
  -> music_assistant.get_library / music_assistant.search
  -> media_player.play_media (on *_sonos_ma) / media_play

automation.music_capture_last_media_on_playback (state-change observer, all 11 room Sonos players)
  -> script.update_last_media_room
  -> script.determine_music_genre_audit
       -> input_text.<room>_speaker_profile_last_media (local regex classification, then)
       -> ai_task.generate_data (ai_task.openai_ai_task)   [LLM fallback]

automation.music_genre_observe_playback_all_sources (state-change observer, last_media helpers)
  -> counter.music_genre_<genre> (counter.increment x19 possible targets)
       -> templates.yaml sensor.house_top_music_genre (reads all 19 counters)

automation.learn_music_volume_on_sonos_change (state-change observer, volume_level)
  -> script.learn_music_volume_room
       -> input_text.<room>_speaker_profile (read + write)
```

---

## 4. Learning chain

```
automation.lamp_profile_learn_on_use (state-change observer, brightness attribute, 49 lights)
  -> input_number.<light>_learned_brightness (write)
  -> input_datetime.lamp_brightness_profile_last_updated (write)

automation.concierge_intentional_learning_ha_voice ("remember this" / "remember lighting/volume")
  -> script.sonos_speak_with_ducking_room (confirmation)
  -> script.learn_lighting_usual_room  -> input_number.<light>_learned_brightness (write, all on lights)
  -> script.learn_music_volume_room    -> input_text.<room>_speaker_profile (write)
```

---

## 5. Bedroom routines (Bedtime / Goodnight / Good Morning / Alarm)

```
automation.bedtime_concierge ("Bedtime")
  -> [inline bedroom-context resolution, duplicated logic]
  -> script.bedroom_context_not_valid_speak (invalid room) -> script.sonos_speak_with_ducking_room
  -> script.concierge_bedtime (valid room)
       -> media_player.unjoin / volume_set (Sonos quieting)
       -> script.sonos_speak_with_ducking_room (confirmation, suppressed after 11pm)
       -> scene.turn_on (primary) | cover.close_cover (guest)   [shade_mode-gated]
       -> light.turn_on (hardcoded device_ids for primary; entity_ids for guest)

automation.goodnight_concierge ("Goodnight")
  -> [inline bedroom-context resolution, duplicated logic]
  -> script.concierge_goodnight
       -> script.set_room_posture (-> night)
       -> script.kiosk_set_overnight_mode -> rest_command.fk_command (REST)
       -> media_player.unjoin
       -> light.turn_off (area_id: bedroom + bathroom)
       -> scene.turn_on (primary) | cover.close_cover (guest)
       -> media_player.turn_off (AppleTV)
       -> media_player.volume_set / repeat_set / play_media (pink noise)

automation.good_morning_concierge ("Good Morning")
  -> [inline bedroom-context resolution, duplicated logic]
  -> script.concierge_good_morning
       -> script.set_room_posture (-> awake)
       -> script.kiosk_set_day_mode (called TWICE — duplicate)
       -> media_player.repeat_set / shuffle_set / media_stop / clear_playlist / volume_set
       -> weather.get_forecasts -> script.sonos_speak_with_ducking_room (weather report, unless pre-5am)
       -> cover.set_cover_position / light.turn_on / fan.turn_on / media_player.turn_off (AppleTV)

automation.primary_bedroom_alarm_started (input_boolean.alarm_primary_bedroom_ringing -> on)
  -> script.turn_on_lamps_usual   ** BROKEN entity_id — real script is turn_on_lamps_usual_room; dead end **
  -> script.primary_bedroom_play_alarm_chime -> script.sonos_speak_with_ducking_room
                                                 (message='' and an unsupported media_source param — no audio plays)

automation.primary_bedroom_alarm_repeat (restart mode, while ringing)
  -> script.primary_bedroom_play_alarm_chime  [repeats every 45s; same no-op audio issue]

automation.primary_bedroom_alarm_escalation (ringing for 2 minutes)
  -> script.room_audio_duck_and_play   ** BROKEN — script does not exist anywhere; dead end **

automation.primary_bedroom_alarm_stop (ringing -> off)
  -> script.room_audio_restore         ** BROKEN — script does not exist anywhere; dead end **
```

**External dependency not resolved in this scope:** nothing among the 26 in-scope automations or 44
in-scope scripts sets `input_boolean.alarm_primary_bedroom_ringing` to `on`. Its writer is outside this
pass's scope (a disabled automation, a blueprint, a dashboard button, or a third-party alarm app/skill)
and should be located before any HTBW replacement work begins on this behavior.

---

## 6. Voice-interaction ducking (cross-cutting)

```
automation.duck_sonos_when_any_assist_satellite_is_listening (mode: parallel — any of 13 satellites)
  -> script.duck_sonos_while_assist_is_listening_room
       -> input_text.<profile_key>_speaker_profile (read: duck volume)
       -> media_player.volume_set (duck all room Sonos, excl. *_beam)
       -> wait_template (satellite leaves 'listening', 12s timeout)
       -> media_player.volume_set (restore exact pre-duck volumes)
```

This runs **independently and concurrently** with every other chain above — any time a voice satellite
is listening, this automation ducks that room's Sonos regardless of what else is happening.

---

## 7. Kiosk provisioning and mode-switching (cross-cutting, device-facing)

```
script.living_room_fully_kiosk_provisioning  -> rest_command.fk_set_boolean/fk_set_int/fk_set_string/fk_command
script.bedroom_fully_kiosk_provisioning      -> rest_command.fk_set_boolean/fk_set_int/fk_set_string/fk_command
script.kiosk_set_overnight_mode  (called by concierge_goodnight)    -> rest_command.fk_command + switch/number entities
script.kiosk_set_day_mode        (called by concierge_good_morning) -> rest_command.fk_command + switch/number entities
```

All four share one plaintext credential pattern — see **Security Findings** in
[production-gaps-and-owner-review.md](production-gaps-and-owner-review.md).

---

## 8. Dashboard → script → household-outcome summary (per the task's requested chain shape)

```
Dashboard/Assist/Voice command
  -> Entry-point automation (conversation trigger)
  -> Room resolution (area_id(trigger.device_id) — live, not configured)
  -> Capability resolution (label_devices / area_entities / entity-id regex — live, not configured)
  -> Execution (light./cover./media_player./scene. service calls)
  -> Response routing (sonos_speak_with_ducking_room -> Sonos TTS, or voice_assistant_speak_fallback
     -> assist_satellite.announce / tts.cloud_say)
  -> State restoration (volume snapshot/restore inside sonos_speak_with_ducking_room and
     duck_sonos_while_assist_is_listening_room; NOT present for the broken alarm-escalation chain)
```

---

## 9. Orphan / broken-reference summary (also see production-gaps-and-owner-review.md)

| Caller | Broken target | Correct target (inferred) | Impact |
|---|---|---|---|
| `script.continue_playing_room` | `script.room_speak_sonos` | `script.sonos_speak_with_ducking_room` | "Nothing queued" fallback speech fails silently |
| `script.what_s_playing_room` | `script.room_speak_sonos` | `script.sonos_speak_with_ducking_room` | "What's playing" answer is computed but never spoken |
| `script.why_did_you_play_this_room` | `script.room_speak_sonos` | `script.sonos_speak_with_ducking_room` | "Why did you play this" answer is computed but never spoken |
| `automation.voice_play_jazz` | `script.whats_playing_room` | `script.what_s_playing_room` | "What's playing" voice follow-up never even reaches the (already-broken) script above |
| `script.speak_room_air_quality` | `script.speak_room_air_quality_assessment` | `script.speak_room_air_quality_ai_assessment` | AI-based air-quality assessment branch is permanently unreachable |
| `automation.primary_bedroom_alarm_started` | `script.turn_on_lamps_usual` | `script.turn_on_lamps_usual_room` | Bedside lamps do not turn on when the alarm starts |
| `automation.primary_bedroom_alarm_escalation` | `script.room_audio_duck_and_play` | *(no such script exists at all)* | 2-minute escalation audio never plays |
| `automation.primary_bedroom_alarm_stop` | `script.room_audio_restore` | *(no such script exists at all)* | Room audio is never restored after the alarm is silenced |
| `automation.concierge_identity_self_query_ha_voice` | service `concierge.execute` | *(no `concierge` integration/config_entry found in production)* | "Who am I" query target's existence is unconfirmed |

All nine were confirmed by direct `grep` against the full production `automations.yaml` and `scripts.yaml`
(not inferred), and the first six were independently re-confirmed by a second, separately-run analysis
pass over `scripts.yaml` alone.
