> **Document status: Operational — discovery artifact.** Not architecture-of-record.

# Home Assistant Platform Inventory

## Installation

| Attribute | Value | Evidence status |
|---|---|---|
| Core version | **2026.9.4** | OBSERVED (`.storage/core.config`) |
| Installation type | Home Assistant OS/Supervised (Supervisor present: `hassio` config entry, title "Supervisor") | OBSERVED |
| Time zone | America/Chicago | OBSERVED |
| Country / currency | US / USD | OBSERVED |
| Host/hardware platform | Not determinable from configuration data alone | UNKNOWN |
| Backup | `backup` integration config entry present (5 related entities) | OBSERVED (presence only; schedule/destination not read) |
| Update mechanism | `update` entity domain present (110 entities); HACS (`hacs` domain, 100 entities) manages custom-component updates; `version`/`analytics`/`uptime` domains present | OBSERVED |
| Add-ons (Wyoming apps) | openWakeWord, Piper, Whisper present as `wyoming` config entries via `hassio` source | OBSERVED |
| Recovery mechanism | Not independently verified (Recorder database not opened; backup destination not read) | UNKNOWN |

## Configuration structure

`configuration.yaml` uses Home Assistant's standard include pattern:

```yaml
default_config:
frontend:
  themes: !include_dir_merge_named themes
automation: !include automations.yaml
script: !include scripts.yaml
scene: !include scenes.yaml
template: !include templates.yaml
rest_command: !include_dir_merge_named rest_commands
```

No `packages:` directory reference was observed at the top level; automations, scripts, scenes, and templates are each a single flat file (`automations.yaml`, `scripts.yaml`, `scenes.yaml`, `templates.yaml`), not package-split. One logger override is configured (`custom_components.extended_openai_conversation: info`).

## Package / include structure

- `rest_commands/` — directory of REST command definitions, merged by name (content not individually catalogued in this pass).
- `themes/` — custom frontend themes directory (presence only).
- `blueprints/` — present at the config root (automation/script blueprints; content not individually catalogued).
- `www/` — present (custom frontend static assets, e.g., for dashboards).

## Custom components (27 observed)

`adtpulse`, `ai_automation_suggester`, `alexa_media`, **`asset_intelligence`** (HTBW product, v1.0.12), `battery_notes`, `bermuda`, `bhyve`, `hacs`, `llmvision`, `mass` (Music Assistant), `media_index`, `ms365_calendar`, `ms365_mail`, `ms365_todo`, `network_scanner`, `nodered`, `openai_tts`, `openclaw`, `reolink_discovery`, `tesla_custom`, `ui_lovelace_minimalist`, `unifi_access`, `unifi_play`, `ups`, `vaca`, `wakeword_installer`, `watchman`.

**Not present:** `concierge`, `voice_identity` — confirms these HTBW integrations are not installed in this production home; any "Concierge"-named automation observed later in this discovery is a household-native naming convention only (see `06-automation-script-scene-inventory.md`).

**`openclaw` and `vaca` and `network_scanner` purposes are UNKNOWN** from directory listing alone — not independently verified in this pass; flagged for owner input or a follow-on, narrower discovery pass.

## Backup configuration

`backup` config entry present; 5 backup-domain entities registered. Destination, schedule, and retention were **not read** (would require opening configuration this pass judged out of scope for a registry-level discovery; add-on/Supervisor backup settings are typically in Supervisor storage, not `.storage/core.*`).

## Development-to-production relationship

No evidence in production of a staging/test Home Assistant instance. The `homes_that_behave_well`, `asset_intelligence`, `voice_identity`, and `concierge` **repositories** are the development side; `P:\` is the sole observed production instance. **No documented environment-separation mechanism exists** (consistent with the same finding already recorded for a hypothetical future MCP pilot in Issue #185 — Home Assistant itself provides no native dev/prod separation concept beyond running a second instance).

## Major platform dependencies (observed)

Supervisor (`hassio`), Home Assistant Cloud (`cloud`), HACS, MQTT broker (`mqtt` domain, 1 config entry + 44 entities), Z-Wave JS (`zwave_js`), Matter (`matter`), Thread (`thread`), Bluetooth (passive + remote scanners), ESPHome (22 node config entries). Each is a **documented Home Assistant native or well-known community integration**, not an HTBW-built mechanism.
