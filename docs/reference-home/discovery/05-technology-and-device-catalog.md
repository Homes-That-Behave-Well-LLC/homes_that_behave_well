> **Document status: Operational — discovery artifact.** Not architecture-of-record.

# Technology and Device Catalog

Derived from `.storage/core.device_registry` (2,528 devices; 123 distinct manufacturer strings; 2,063 devices carry no manufacturer — expected for virtual/service devices such as automations, scripts, zones, persons, and helpers). Manufacturer strings are reported **exactly as stored** (including inconsistent casing/variants, e.g., "Sonos" / "Sonos, Inc." / "SONOS" are three distinct strings in the registry, not merged, to avoid presenting an inferred correction as observed fact).

| Manufacturer (as stored) | Device count | Household purpose | Connected integration | Local/cloud | Publication-logo candidate | Confidence |
|---|---|---|---|---|---|---|
| SmartLabs, Inc | 67 | Lighting/switch backbone | `insteon` | Local | Yes (Insteon) | HIGH |
| Ubiquiti Networks / Ubiquiti / Unifi (3 variants, 27+17+5) | 49 | Network, cameras, access | `unifi`, `unifiprotect`, `unifi_access` | Local | Yes (Ubiquiti/UniFi) | HIGH |
| Aqara | 26 | Zigbee sensors (door/window/motion — exact sensor types not individually itemized this pass) | Likely `zwave_js`/Zigbee path (not independently confirmed per-device) | Local | Yes (Aqara) | MEDIUM |
| esphome | 22 | Custom DIY sensors/controllers | `esphome` (22 node config entries) | Local | Optional (DIY, not a retail brand) | HIGH |
| Sonos, Inc. / Sonos / SONOS (3 variants) | 54 | Whole-home audio | `sonos`, `mass` | Local | Yes (Sonos) | HIGH |
| Hunter Douglas | 20 | Motorized shades | `hunterdouglas_powerview` | Local | Yes (Hunter Douglas / PowerView) | HIGH |
| Apple / Apple, Inc. (2 variants) | 21 | Apple TV, HomeKit ecosystem | `apple_tv`, `homekit_controller` | Local | Yes (Apple) | HIGH |
| Nabu Casa | 14 | Home Assistant Cloud virtual devices | `cloud` | Cloud | Optional | HIGH |
| ADT | 12 | Security/alarm panel | `adtpulse` | Cloud | Yes (ADT) | HIGH |
| Home Assistant | 10 | Core/virtual devices | multiple | Local | No (not a physical product) | HIGH |
| Microsoft / Microsoft Corporation (2 variants) | 12 | MS365 calendar/mail/todo | `ms365_calendar`, `ms365_mail`, `ms365_todo` | Cloud | Optional | HIGH |
| OpenAI | 8 | Conversation/TTS reasoning | `openai_conversation`, `openai_tts` | Cloud | Optional | HIGH |
| Orbit BHyve | 7 | Irrigation control | `bhyve` | Cloud (vendor app/API) | Yes (B-hyve) | HIGH |
| samsung | 5 | Samsung TV | `samsungtv` | Local | Yes (Samsung) | HIGH |
| Trane | 4 | Thermostat hardware (controlled via Nexia cloud API) | `nexia` | Cloud (API) / Local (hardware) | Yes (Trane) | HIGH |
| ESPresense (esp32) | 4 | BLE presence-detection nodes | `bermuda`/BLE path | Local | Optional (DIY) | MEDIUM |
| LG / LG Electronics (2 variants) | 5 | LG webOS TV | `webostv` | Local | Yes (LG) | HIGH |
| Ecowitt | 3 | Weather station | `ecowitt` | Local | Yes (Ecowitt) | HIGH |
| CorantGmbH | 3 | Air-quality sensor | `airq` | Local | Optional | MEDIUM |
| CyberPower Systems, Inc. | 3 | UPS/power protection | `ups` (custom) | Local | Yes (CyberPower) | HIGH |
| Sony Interactive Entertainment | 2 | PlayStation | `playstation_network` | Cloud | Optional | HIGH |
| Tesla | 1 | Vehicle | `tesla_custom` | Cloud | Yes (Tesla) | HIGH |
| Reolink | 1 | Camera | `reolink_discovery` | Local | Yes (Reolink) | MEDIUM |
| Oral-B | 1 | Smart toothbrush | `oralb` | Cloud | Optional (novelty/historical framing) | HIGH |

**Devices with no manufacturer recorded (2,063 of 2,528, 82%):** predominantly virtual/service devices (84 automation devices, 50 script devices, 40 zone devices, 7 person devices, helper/group devices, and `entry_type: service`-classified devices for integrations such as `hassio`, `cloud`, `backup`). This is **normal Home Assistant behavior**, not a data-quality defect, and must not be presented as "unknown hardware."

## Network infrastructure (INFERRED only — not independently observed)

No controller/switch/access-point model, count, or placement was directly observed. The presence of `unifi`, `unifi_access`, and `unifiprotect` config entries is strong **evidence that a Ubiquiti UniFi network exists**, but the specific hardware (Dream Machine vs. separate controller, switch models, AP models/count, PoE budget) is **UNKNOWN** pending owner input or a separately-approved network-discovery method.

## Controllers, hubs, gateways, and bridges (observed via integration presence)

- **PowerView Hub** (Hunter Douglas shades) — `zeroconf`-discovered, title "PowerView-Hub".
- **Insteon PLM/hub** — presence inferred from the `insteon` integration; exact hardware not verified.
- **Z-Wave JS** controller — 1 config entry.
- **Matter** controller — 1 config entry.
- **Thread** border router — 1 config entry.
- **MQTT broker** — 1 config entry (broker identity not verified; may be Home Assistant's add-on Mosquitto or external).
- **ESPHome** — 22 individually-paired nodes (each is both a "device family" entry point and, functionally, a micro-controller gateway for its own sensors).

## Protocol coordinators

Zigbee (via Aqara devices — exact coordinator not identified), Z-Wave (`zwave_js`), Matter, Thread, Bluetooth (passive + remote scanners), MQTT. **No single "coordinator count" claim is made** — each protocol's bridging hardware is evidence-inferred from the presence of its Home Assistant integration, not independently inspected.

---

**Full machine-readable catalog:** `device-family-catalog.csv`.
