> **Document status: Operational — discovery artifact.** Not architecture-of-record.

# Network and Infrastructure Inventory

**This category has the largest evidence gap in the entire discovery pass.** Home Assistant integration presence is strong indirect evidence of a Ubiquiti UniFi network, but no router, switch, access-point, or cabling detail is independently observable from `P:\`.

| Item | Status | Evidence |
|---|---|---|
| Internet-service dependency | INFERRED (present) | Household clearly has internet access (cloud integrations function); ISP identity `UNKNOWN` |
| Router/firewall platform | INFERRED: Ubiquiti UniFi family | `unifi` config entry; specific model `UNKNOWN` |
| Core switching | INFERRED: Ubiquiti UniFi | Same evidence; model/count `UNKNOWN` |
| Access points | INFERRED: Ubiquiti UniFi | Same evidence; count/placement `UNKNOWN` |
| Wired infrastructure | UNKNOWN | Not observable from Home Assistant |
| Wireless infrastructure | INFERRED: UniFi Wi-Fi | SSID/band/channel detail intentionally excluded even if present in source data |
| VLANs/segments | UNKNOWN | Not observable; would require UniFi controller access (out of scope — not a read-only HA-evidence method) |
| Server/compute infrastructure | PARTIALLY OBSERVED | A "Data Closet" area exists in `.storage/core.area_registry`, confirming a dedicated equipment location; specific hardware `UNKNOWN` |
| Storage infrastructure | UNKNOWN beyond the HA host itself | `home-assistant_v2.db` exists (Recorder SQLite); not opened this pass |
| PoE dependencies | INFERRED | ESPHome nodes, APs, and UniFi Protect cameras typically require PoE; not independently confirmed |
| UPS/power protection | **OBSERVED** | CyberPower UPS integration (3 devices) confirms at least one UPS is monitored |
| Home Assistant host connection | UNKNOWN | Hardware platform not observable from configuration data |
| Hubs and bridges | OBSERVED (by integration) | PowerView Hub, Insteon hub/PLM (inferred), Z-Wave JS controller, Matter controller, Thread border router, MQTT broker — each confirmed only by its Home Assistant integration's presence |
| Camera/NVR dependencies | OBSERVED | UniFi Protect (674 entities) is clearly the primary NVR platform; Reolink present as a secondary/legacy camera source |
| Local DNS dependencies | UNKNOWN | Not observable |
| Remote-access dependencies | OBSERVED (partial) | Home Assistant Cloud (`cloud` config entry) provides one documented remote-access path; whether it is the household's only remote-access method is `UNKNOWN` |
| Cloud dependencies | OBSERVED | Enumerated fully in `03-integration-catalog.md`'s per-category "Local/Cloud" columns |
| Single points of failure | INFERRED | Internet/network layer (everything cloud-dependent fails together); Insteon hub (if it fails, `Insteon Keep Alive Every 10 Minutes` existing as an automation suggests the household has already encountered reliability concerns here) |
| Observed resilience patterns | OBSERVED | UPS monitoring, Backup integration, Watchman self-diagnostic, `Backup Stale Automation` |

## What must not be published

No public IP, internal IP, MAC address, SSID, VLAN identifier, firewall rule, username, password, token, or external access endpoint was extracted by any analysis script in this discovery pass — none exists in any generated artifact to redact, because none was ever read into them.

## Recommendation

A dedicated, separately-scoped, owner-assisted network walkthrough (or an explicitly approved read-only UniFi-controller discovery method) is required before the "Network Is the Backbone" article can include real topology detail beyond "a Ubiquiti UniFi network with a Data Closet." This is marked **OWNER INPUT REQUIRED** in `11-owner-input-required.md`.
