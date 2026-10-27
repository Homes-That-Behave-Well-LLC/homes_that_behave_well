> **Document status: Operational — discovery artifact.** Not architecture-of-record.

# Building and Renovation Guidance — "If You Are Building or Renovating"

Each recommendation is tagged: **DIRECTLY SUPPORTED BY REFERENCE HOME EVIDENCE** (something this production home's own configuration demonstrates), **SUPPORTED BY REPOSITORY GOVERNANCE** (grounded in `homes_that_behave_well` architecture docs), **OWNER EXPERIENCE TO BE DOCUMENTED** (the owner has relevant experience but it is not yet captured), or **GENERAL RECOMMENDATION REQUIRING REVIEW** (industry-general advice not yet verified against this home).

| Topic | Guidance | Classification |
|---|---|---|
| Structured cabling | Run home-run Ethernet to every AP, camera, and kiosk-tablet location rather than relying solely on Wi-Fi | GENERAL RECOMMENDATION REQUIRING REVIEW (network topology unverified this pass) |
| Wi-Fi AP placement | Plan AP density around whole-home coverage given a UniFi network of this device scale (2,528 registered devices) | GENERAL RECOMMENDATION REQUIRING REVIEW |
| PoE | Budget PoE capacity for cameras, APs, and any ESPHome nodes drawing power this way | GENERAL RECOMMENDATION REQUIRING REVIEW |
| Fiber | Not evidenced either way | GENERAL RECOMMENDATION REQUIRING REVIEW |
| Conduits / pull strings | Standard retrofit-friendliness advice | GENERAL RECOMMENDATION REQUIRING REVIEW |
| Accessible pathways | Same | GENERAL RECOMMENDATION REQUIRING REVIEW |
| Equipment racks / data closets | This home has a dedicated **Data Closet** area | DIRECTLY SUPPORTED BY REFERENCE HOME EVIDENCE (area exists; rack contents unverified) |
| Ventilation/cooling for equipment | Standard advice for a Data Closet of this home's evident scale | GENERAL RECOMMENDATION REQUIRING REVIEW |
| Dedicated circuits | Standard for a Data Closet / home-automation equipment | GENERAL RECOMMENDATION REQUIRING REVIEW |
| UPS support | This home demonstrably runs UPS monitoring (CyberPower, 3 devices) | DIRECTLY SUPPORTED BY REFERENCE HOME EVIDENCE |
| Generator/battery support | Not evidenced | GENERAL RECOMMENDATION REQUIRING REVIEW |
| Neutral conductors at switch locations | Required for most smart switches (Insteon included); directly relevant given this home's 67-device Insteon deployment | SUPPORTED BY REPOSITORY GOVERNANCE (P21/Home Assistant First doesn't speak to wiring, but general smart-lighting retrofit practice does) + OWNER EXPERIENCE TO BE DOCUMENTED (owner's actual retrofit constraints) |
| Deep electrical boxes | Needed to fit smart switches/dimmers behind existing plates | OWNER EXPERIENCE TO BE DOCUMENTED (owner-provided: "construction and wiring constraints contributed to the selected retrofit approach") |
| Shade power / window-header power | This home runs 20 motorized Hunter Douglas shades | DIRECTLY SUPPORTED BY REFERENCE HOME EVIDENCE (shades exist and are automated) + OWNER EXPERIENCE TO BE DOCUMENTED (how power was actually routed) |
| Door and lock wiring | This home has `unifi_access` | DIRECTLY SUPPORTED BY REFERENCE HOME EVIDENCE (capability exists); wiring detail `UNKNOWN` |
| Doorbell/intercom wiring | This home has (or had) a front-gate video doorbell, **currently showing missing entities** per Watchman | DIRECTLY SUPPORTED BY REFERENCE HOME EVIDENCE, including the honest "this is currently broken" finding |
| Alarm wiring | This home runs ADT Pulse | DIRECTLY SUPPORTED BY REFERENCE HOME EVIDENCE (capability exists); wiring detail `UNKNOWN` |
| Environmental sensors | This home runs Ecowitt weather + air-quality sensors + soil-moisture sensors (2 currently unavailable) | DIRECTLY SUPPORTED BY REFERENCE HOME EVIDENCE |
| Ceiling sensors | Big Ass Fans ceiling fans present; dedicated ceiling occupancy/motion sensors not separately itemized | GENERAL RECOMMENDATION REQUIRING REVIEW |
| Speakers | This home runs 21+ Sonos-family devices | DIRECTLY SUPPORTED BY REFERENCE HOME EVIDENCE |
| Displays | 5 kiosk tablets, multiple TVs (LG, Samsung, Apple TV) | DIRECTLY SUPPORTED BY REFERENCE HOME EVIDENCE |
| Exterior technology | Front gate, front door, carport, back yard, patio areas all exist as distinct Areas | DIRECTLY SUPPORTED BY REFERENCE HOME EVIDENCE (areas exist; exact exterior device placement `UNKNOWN`) |
| Detached structures | Not evidenced | GENERAL RECOMMENDATION REQUIRING REVIEW |
| Future serviceability | Reflected in the household's own Insteon-keep-alive and Watchman self-diagnostic practices | DIRECTLY SUPPORTED BY REFERENCE HOME EVIDENCE |
| Labeling | 39 labels exist in the label registry (not individually catalogued this pass) | DIRECTLY SUPPORTED BY REFERENCE HOME EVIDENCE (labels exist); scheme/usage `UNKNOWN` |
| Documentation | This discovery pass **is** a step toward that documentation | DIRECTLY SUPPORTED |
| Manual controls | Physical Insteon switches, PowerView remotes — both documented as retaining native manual control (Insteon/PowerView general product behavior) | GENERAL RECOMMENDATION REQUIRING REVIEW (not independently verified for this installation) |
| Privacy boundaries | Guest Bedroom/Bathroom exist as distinct areas with their own shade-automation logic (see `Close Guest Shade when [Resident] enters...`) | DIRECTLY SUPPORTED BY REFERENCE HOME EVIDENCE |

## "Grow Into It, But Plan Ahead" — owner-provided theme

Per explicit owner-provided context, the series should emphasize that households can **grow into** this architecture over time while **planning infrastructure ahead of installation** (conduit, neutral wires, deep boxes, data-closet space, labeled cabling) even if the smart-home capability itself is added later. This theme should recur in every capability article's "if you are building or renovating" subsection, cross-referencing this file rather than repeating it.
