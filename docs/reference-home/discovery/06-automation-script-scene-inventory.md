> **Document status: Operational — discovery artifact.** Not architecture-of-record.

# Automation, Script, and Scene Inventory

**84 automations, 50 scripts, and an effectively empty `scenes.yaml` (3 bytes)** — native Home Assistant scenes are **not** this household's scene mechanism; shade/lighting "scenes" are achieved through PowerView's own scene objects and through scripts (`turn_on_home_tour`, `turn_on_dinner_party`, etc.) instead.

## Automation trigger-platform distribution (84 automations)

| Trigger platform | Count | Notes |
|---|---|---|
| `state` | 56 | Dominant pattern — state-change-driven automation is this household's primary style |
| `conversation` | 27 | Voice-intent-driven — a large share of total automations are voice-triggered |
| `time` | 15 | Fixed clock-time schedules |
| `numeric_state` | 15 | Threshold-crossing (e.g., moisture below 20%) |
| `time_pattern` | 7 | Recurring interval checks |
| `sun` | 6 | Solar-position-driven (sunset offsets) |
| `moisture.detected` | 6 | Leak-sensor events |
| `device`, `zone` | 2 each | Device-trigger and geofence-based |
| `occupancy.detected` / `.cleared` | 2 each | Room-occupancy sensor events |
| `illuminance.crossed_threshold` | 1 | Light-level threshold |

A single automation may register more than one trigger; counts are per trigger, not per automation.

## Automation modes

80 `single`, 3 `restart` (the two "Learn …" automations plus `Primary Bedroom – Alarm Repeat` — all three are patterns that must cancel and restart themselves on repeated triggering), 1 `parallel` (`Duck Sonos When Any Assist Satellite Is Listening` — must be able to duck multiple concurrent speakers).

## Representative automation families (redacted of resident names → "Resident 1 (Primary)" / "Resident 2")

**Lighting (sun/time/occupancy-driven):** *Turn On Daily 20 Minutes before Sunset*, *Turn-On/Off Overnight Lights*, *Turn Off Daily at 10PM*, *Turn on Daily 40 Minutes before Sunset if it is Cloudy*, *Turn on Resident 2's Lamp 39 minutes before sunset*, *Turn on Tom's Office when Occupied* → generalized: *Turn on Resident 1's Office when Occupied*, *Turn off [Resident]'s Light when Office not occupied after 5PM and before 8AM*, *Turn on Den Lamps when Presence is detected and it's dark between 7AM and 11PM*, *Turn off Den Lamps when there is No Occupancy and it has gotten brighter*, *Den - It gets bright and no longer need lamps on*, *Turn off den corner lamp at 8:00 AM*, *Lighting Profile – Learn on Use* (restart mode).

**Shades (8 directional pairs):** *NE/NW/SE/SW Upstairs/Downstairs Shades – Open/Close*, *Close Guest Shade when [Resident] enters the Guest Bedroom between 9PM and 6AM*, *Open Guest Shade at 6AM if it is closed*, *VA - Close/Open Den Shades*.

**Irrigation (moisture-gated):** *Water Bamboo at 8:00 AM if Moisture below 20%*, *Water Front Door Bushes at 7 AM when moisture falls below 20%*, *Water Front Bed and Patio Grass at 5AM when Moisture is below 20%*, *Water Walkway Grass at 9AM when moisture falls below 20%*, *Water Front Bed Drip at 6AM when moisture is below 20%*, *9AM 4PM 9PM - Yard Misters On (Mosquitos)*, *Send Notification when B-Hyve Battery Low*.

**Leak/Safety (6 locations):** *Toilet Leak - Downstairs Bathroom*, *Toilet Leak - Primary Bathroom*, *Toilet Leak - Guest Bathroom*, *Toilet Leak - Powder Room*, *Leak Detected - Laundry Room*, *Leak Detected - Kitchen Dishwasher*.

**Security/Alarm (escalation ladder):** *Primary Bedroom – Alarm Started* → *Alarm Repeat* (restart mode) → *Alarm Escalation* → *Alarm Stop*.

**Presence/arrival:** *[Resident 1] or [Resident 2] Arrives Home after 10PM*, *Turn on Resident 1's Office when Occupied*.

**Voice / "Concierge" and "VA:" family (household-native, not the HTBW integration):** *Concierge – Voice Entry (HA Voice)*, *Concierge – Follow-Up Commands (HA Voice)*, *Concierge — Intentional Learning (HA Voice)*, *Concierge – Shade Percentage Catcher (HA Voice)*, *Concierge – Lighting Percentage Catcher (HA Voice)*, *Concierge – Room Monitoring Awareness (HA Voice)*, *Concierge – Follow-Up Sensor Queries (HA Voice)*, *Concierge - Identity Self Query (HA Voice)*, *Bedtime (Concierge)*, *Goodnight (Concierge)*, *Good Morning (Concierge)*, *VA: Bedtime*, *VA: Goodnight*, *VA: Good Morning*, *VA: Weather Announcement*.

**Media/audio:** *Voice – Play Music*, *Voice – Continue Playing*, *Voice – Music Follow-Ups*, *Learn Music Volume – On Sonos Change* (restart), *Music Genre – Observe Playback (All Sources)*, *Music – Capture Last Media (Robust)*, *Duck Sonos When Any Assist Satellite Is Listening* (parallel), *Turn On Apple TV Den*.

**Vehicle:** *Reminder to Charge the Tesla*, *Tesla below 100 Mile Range - Please Charge*.

**Seasonal/novelty:** *Turn on/off Christmas Tree / Sculpture*, *Turn on/off Home Tour*.

**Dashboards/kiosk:** *All Kiosk Screen Off 11 PM*, *All Kiosk Screens On 7AM*.

**Platform/maintenance:** *Backup Stale Automation*, *Insteon Keep Alive Every 10 Minutes*, *AccuWeather Update every 5 Minutes*, *Refresh Shade Battery Level*, *Test Automation* (explicitly a test artifact left in production — flagged as an evidence note, not a defect to correct here).

## Scripts (50 total — representative set)

`turn_on_daily` / `turn_off_daily`, `turn_on_home_tour` / `turn_off_home_tour`, `turn_on_dinner_party` / `turn_off_dinner_party`, `resolve_speaker_profile`, `room_audio_resolver_keystone`, `sonos_speak_with_ducking_room`, `room_capabilities_snapshot_debug`, `learn_lighting_usual_room`, `learn_music_volume_room`, `resolve_music_player_room`, `update_last_media_room` (remaining ~36 not individually itemized in this pass — see `automation-catalog.csv` for the full key/alias list captured).

## Architectural patterns observed (cross-cutting)

- **Occupancy-driven behavior:** lighting on/off tied to room occupancy (Den, Office).
- **Presence-driven behavior:** arrival-time-conditioned lighting; shade behavior tied to a resident entering a room.
- **Time-driven behavior:** fixed schedules (10PM off, 8AM lamp-off, kiosk on/off).
- **Solar-position behavior:** sunset-offset lighting, cloudy-day sunset adjustment.
- **Environmental behavior:** moisture-gated irrigation, illuminance-threshold lamp control.
- **Safety-related behavior:** 6-location leak detection.
- **Security-related behavior:** 4-stage alarm escalation ladder.
- **Access behavior:** gate auto-close after 5 minutes.
- **Lighting behavior / Shade behavior:** see families above.
- **Media behavior:** room-aware audio resolution, "last media" capture, genre observation.
- **Voice behavior:** the full "Concierge"/"VA:" family.
- **Notification behavior:** battery-low and vehicle-charge reminders.
- **Asset-protection behavior:** Tesla range reminder, B-hyve battery notification.
- **Recovery behavior:** `Backup Stale Automation`, `Insteon Keep Alive`.
- **Administrative behavior:** `AccuWeather Update every 5 Minutes`, `Refresh Shade Battery Level`.
- **Governance behavior:** none formally separated from the automations above — this is itself a finding (see `01-executive-architecture-summary.md`): the household has no separate "governance" layer; voice/learning/identity concerns are interleaved directly into the "Concierge"/"VA:" automation family.

## Evidence gaps (from Watchman self-diagnostic)

`watchman_report.txt` independently confirms (household's own tool, not HTBW-generated): a missing front-gate doorbell camera/event pair, two `unavail` soil-moisture sensors, and one `unknown`-state PowerView scene referenced by automations — all genuine, currently-open issues in the production automation set, useful "lessons learned" material rather than claims of perfect operation.
