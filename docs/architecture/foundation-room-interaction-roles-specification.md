# Foundation Room Interaction Roles — Implementation-Ready Specification

> **Document status: Active — subordinate to the HTBW canonical architecture.**
> Canonical authority: [adr-decoupled-voice-interaction-capability-architecture.md](adr-decoupled-voice-interaction-capability-architecture.md)
> (**DL-90**, **DL-91**, accepted 2026-10-26, Issue #198),
> [adr-stable-endpoint-identity-and-network-boundary-independence.md](adr-stable-endpoint-identity-and-network-boundary-independence.md)
> (**DL-87**, **DL-88**, accepted 2026-10-27, Issue #195), [framework.md](framework.md), and
> [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> **Specification only. Authorizes no executable implementation.** Owner Acceptance Review:
> **PASS** (2026-10-26, Issue #199, closed), after remediating one data-model issue in commit
> `7096a38`. **Extended by Issue #196** to generalize the Interaction Function Assignment model to the
> remaining DL-88 room-interaction-capability roles (`interface`, `physical_remote`) and to resolve
> DL-87's implementation mechanics for this workstream (§18). **The #196 extension's own Owner
> Acceptance Review: PASS (2026-10-27, Issue #196, closed), no remediation required. It does not
> reopen the #199 PASS result for the original voice_input/spoken_response_output material, and does
> not reopen DL-87 or DL-88.**

---

## 1. Status and scope

This document operationalizes the accepted **DL-90** (Decoupled Voice Interaction Capability Model) and
**DL-91** (Performance-Aware, Provider-Independent Voice Processing Principle) into an
implementation-ready schema/contract specification for the **Foundation Room Interaction Roles**
workstream only. It does not reopen, narrow, or redecide DL-90 or DL-91. **Owner Acceptance Review
recorded PASS on Issue #199 (2026-10-26)**, confirming this specification correctly preserves Foundation,
Truth, Concierge, Operational Trust, Identity/Voice Identity, and Continuity boundaries.

**Issue #196 extension — Owner Acceptance Review PASS (2026-10-27, no remediation required).** Issue
#195 accepted **DL-87** (Stable Identity Hierarchy and Network-Boundary Independence) and **DL-88**
(Foundation and Concierge Responsibility Split for Endpoint and Room-Interaction-Capability
Relationships), which require Room Configuration to represent `interface` (kiosk/visual-manual) and
`physical_remote` as two further room-interaction-capability relationships alongside `voice_input` and
`spoken_response_output`, and require the DL-87 resolution-order mechanics to be resolved for this
workstream. This document is the existing specification that already owns the adjacent
`voice_input`/`spoken_response_output` material (per repository governance precedent against creating
a parallel document for closely related material); Issue #196 extended it rather than creating a new
one. **Issue #196 is closed.** The extension is confined to: (1) generalizing §3/§4's Interaction
Function Assignment model to the two additional DL-88 roles, and (2) §18, which resolves DL-87's
implementation mechanics for this workstream. **It does not reopen DL-90, DL-91, or the #199 acceptance
result for the original material, and does not reopen DL-87 or DL-88.**

**This document authorizes no executable implementation.** Pre-implementation grounding found:


- `homes_that_behave_well` is a documentation-only repository.
- The three available sibling repositories (`concierge`, `voice_identity`, `asset_intelligence`) are
  governed by [greenfield-mandate.md](greenfield-mandate.md) as sunsetting, non-authoritative
  "exploratory projects," which states: *"Do not copy code from the reference repositories into HTBW.
  Do not begin implementing HTBW Core code."*
- No HTBW Core implementation repository exists for this specification to target.

**Executable implementation of this specification remains deferred until an authorized HTBW Core
implementation surface exists. Creating that surface is explicitly out of scope for this document.**
This document is written so that, once such a surface exists, implementation can proceed directly from
it without further architectural research.

**Performance-Aware Voice Processing (DL-91's implementation workstream) is explicitly out of scope
here** — Speech-to-Phrase, Whisper, STT-provider selection, automatic pipeline fallback, Home
Intelligence/Ollama routing, latency-based processing selection, ESPHome/reSpeaker firmware,
microphone-array DSP configuration, wake-word tuning, Voice Identity redesign, new TTS engines, and new
Sonos ducking logic are not specified, implemented, or begun by this document.

---

## 2. Grounding summary

Inspected and reconciled before writing this specification:

| Authority | Relevant finding |
|---|---|
| [adr-decoupled-voice-interaction-capability-architecture.md](adr-decoupled-voice-interaction-capability-architecture.md) (DL-90/DL-91) | Source decision for everything in this document |
| [../contracts/foundation-contract.md](../contracts/foundation-contract.md) | Foundation owns object definitions, relationships, capability descriptions — unchanged |
| [../contracts/room-configuration-contract.md](../contracts/room-configuration-contract.md) | Existing "voice assistant context," experience-endpoint vocabulary, three participation states, four-state model (Existence/Participation/Exposure/Authority), "will never guarantee current availability" — all reused |
| [../models/room-configuration.md](../models/room-configuration.md) | Existing "Voice assistant context" resolution order, Merged Room reconciliation already stated there — extended, not replaced |
| [../contracts/concierge-contract.md](../contracts/concierge-contract.md) §6 | Interaction Space / Execution Target / Response Delivery Space model — consumed, not altered |
| [../contracts/identity-contract.md](../contracts/identity-contract.md) | Dependency-failure degradation contract (`unavailable`, never a guess) — reused unchanged |
| [../contracts/continuity-contract.md](../contracts/continuity-contract.md) | Session/resume/transfer boundaries — unaffected |
| [../contracts/operational-trust-contract.md](../contracts/operational-trust-contract.md) | Authority/autonomy/confirmation boundaries — unaffected |
| [home-assistant-boundary.md](home-assistant-boundary.md) | Native device/entity/Area/`assist_satellite` discovery and registry ownership — reused, not duplicated; verified native Area/Device/Entity registry behavior (§18.1) and the "prefer HA navigation patterns, dialogs, selectors" principle (§18.3) |
| [../models/glossary.md](../models/glossary.md) | Capability, Participation, Interaction Function Assignment, `voice_input`, `spoken_response_output` term definitions |
| Existing setup/configuration implementation | **None found.** No Foundation Room Setup implementation exists in any repository available for inspection (see §1) |
| Existing tests covering Room Configuration | **None found**, for the same reason |
| [adr-stable-endpoint-identity-and-network-boundary-independence.md](adr-stable-endpoint-identity-and-network-boundary-independence.md) (DL-87/DL-88, accepted #195) | **Issue #196 addition.** DL-88's `interface`/`physical_remote` roles generalized into §3/§4; DL-87's resolution-order mechanics resolved for this workstream in §18 — this workstream needs no HTBW-owned network-endpoint resolution (§18.2) |

---

## 3. Core model

```
Room
  -> voice_input                  (Interaction Function Assignment)
  -> spoken_response_output       (Interaction Function Assignment)
  -> interface                    (Interaction Function Assignment — Issue #196 addition, DL-88)
  -> physical_remote              (Interaction Function Assignment — Issue #196 addition, DL-88)
```

All four are **Interaction Function Assignments** under **DL-90**'s triad (restated here for
implementation) and **DL-88**'s room-interaction-capability relationships (`interface` and
`physical_remote` added by Issue #196, completing DL-88's four-relationship set alongside the
already-specified `voice_input`/`spoken_response_output`):

| Tier | Meaning |
|---|---|
| **Capability** | What a Home Assistant device/entity can technically provide (for example, a device exposing both a microphone and a speaker) — read from the native Home Assistant device/entity registry, never duplicated into an HTBW-owned registry |
| **Participation** | Whether that capability has been explicitly selected to take part in a Room's interaction model |
| **Interaction Function Assignment** | Which specific function — `voice_input`, `spoken_response_output`, `interface`, `physical_remote` (Issue #196 addition), or another existing experience-endpoint category (`music`, `video`, `announcement`, `conversation`) — a participating capability is assigned to fulfill in the Room |

**A capability's existence never implies participation, and participation never implies a specific
Interaction Function Assignment.** Each is independently, explicitly configured.

---

## 4. Schema / data contract

This is a **data-shape specification**, not a storage-engine or ORM design. Field names are
illustrative and MUST be reconciled with whatever persistence mechanism the eventual HTBW Core
implementation surface adopts (see **OD-01**, Room Configuration's own open persistence-shape
decision, unaffected by this specification).

### 4.1 `RoomInteractionFunctionAssignment` (conceptual record)

**Each `RoomInteractionFunctionAssignment` record is atomic: one Room, one interaction function, one
participating capability.** Multiplicity (zero, one, or many endpoints fulfilling a function in a
Room) is expressed as **zero, one, or many separate records**, never as a list-valued field inside one
record.

| Field | Type | Cardinality (within one record) | Required | Description |
|---|---|---|---|---|
| `room_id` | Foundation Room reference | 1 | Yes | The Room (or Merged Room) this assignment belongs to |
| `function` | Enumeration | 1 | Yes | `voice_input` \| `spoken_response_output` \| `interface` \| `physical_remote` (Issue #196 addition, **DL-88**) \| other existing experience-endpoint category (extensible per **DL-55**) |
| `participating_capability_reference` | Native Home Assistant reference (entity_id/device_id or equivalent native identifier) | **1** | Yes | The single native capability this record assigns to this function. **Never a literal IP, MAC, or vendor-specific identifier** — the native Home Assistant reference only, consistent with the Stable Endpoint Identity resolution order (**DL-87**, accepted at **#195**). Per-function reference-type guidance, including the `interface`/`physical_remote` cases, is resolved in §18.1 |
| `participation_state` | Enumeration | 1 | Yes | `participating` \| `not_selected` \| `deliberately_excluded` — reusing Room Configuration's existing three-state model unchanged |
| `assigned_at` / `updated_at` | Timestamp | 1 | Yes | Reuses Room Configuration's existing Change Record / configuration-history mechanism; no new history mechanism is created |

**Room-and-function cardinality is explicitly record-level, not field-level: a Room may have zero, one,
or many `RoomInteractionFunctionAssignment` records for a given interaction function.** This satisfies
the no-cardinality-assumption requirement (multiple microphones, output groups, future redundancy)
without building multi-endpoint orchestration logic now — zero, one, or many records for one
Room+function pair are all valid today; only the schema shape, not the runtime fan-out behavior, is
specified here. **No priority, preferred-endpoint, fallback, failover, or runtime endpoint-selection
semantics are introduced by this cardinality** — selecting among multiple records for the same
Room+function, where it ever matters, is runtime behavior left entirely to future, separately
authorized implementation and governance work, not decided here.

### 4.2 Relationship to existing Room Configuration fields

This record is a **new, additional row shape within Room Configuration's existing "which experience
endpoints exist" and "which voice assistants are assigned" data**, not a parallel store. Where an
implementation surface already represents "participating voice assistants" as a list, `voice_input`,
`spoken_response_output`, `interface`, and `physical_remote` assignments are further entries in that
same list shape — one atomic record per participating capability per function — distinguished by
`function`, not separate unrelated structures. `interface` (kiosk/visual-manual) is additionally a
candidate Response Delivery Space surface alongside `spoken_response_output` (§8); `physical_remote`,
like `voice_input`, is an interaction-input surface only and is never itself a delivery target.

### 4.3 What this schema does not do

- It does not store Home Assistant's own device/entity capability data (name, model, integration) — that
  remains Home Assistant's native registry, read by reference.
- It does not store or assert current runtime availability (see §7, Truth boundary).
- It does not store raw audio, voice samples, or any durable voice/audio artifact (see §10, Privacy).
- It does not define a Merged Room-specific record shape (see §9).

---

## 5. Foundation Room Setup requirements

The existing Room Setup experience (an interaction-definition flow, not an inventory screen, per
[greenfield-mandate.md](greenfield-mandate.md)'s "Discoveries carried forward" table) must be extended,
not replaced, to let a household answer **four independent questions** per Room (the first two
specified originally; the latter two added by Issue #196 to complete DL-88's four-relationship set):

1. **How should the Home hear voice interactions in this room?** (configures `voice_input`
   participation and assignment)
2. **Where should the Home deliver spoken responses in this room?** (configures
   `spoken_response_output` participation and assignment)
3. **What visual/manual interface, if any, serves this room?** (configures `interface` participation
   and assignment)
4. **What physical remote, if any, serves this room?** (configures `physical_remote` participation and
   assignment)

### Requirements

| Requirement | Statement |
|---|---|
| Independence | All four questions must be answerable independently. Answering one must never default-assign another. |
| Discovery reuse | Candidate capabilities are discovered through existing Home Assistant-native device/entity/Area discovery and capability reporting. **No HTBW-owned physical-device discovery mechanism is created.** |
| No silent assignment | A device possessing more than one function's capability (for example, microphone and speaker) must not be auto-assigned more than one function merely because discovery found it. Discovery identifies **candidates**; the household's (or configuration flow's) explicit choice establishes the **assignment**. |
| No product-specific modes | The setup experience must not introduce separate "ReSpeaker mode," "Sonos mode," "microphone-array mode," "kiosk mode," or "Voice Assistant mode" constructs. The underlying governed model is capability/participation/assignment-based; a presentation-layer convenience (for example, a single setup screen offering "use this device for both" as a shortcut) may exist **only** as a UI convenience over the same underlying independent assignments — never as a distinct data model. |
| All-absent is valid | A Room with none of the four functions configured is a valid, ordinary configuration state, not an error or an incomplete-configuration warning. |

---

## 6. Supported configurations

All of the following are valid, independently representable `(voice_input, spoken_response_output)`
configurations for one Room, with no configuration requiring a different data model than any other:

| Configuration | `voice_input` | `spoken_response_output` |
|---|---|---|
| A. Integrated voice assistant | Device A | Device A |
| B. Integrated voice assistant, input only | Device A | Device B (separate) |
| C. Dedicated microphone + independent speaker | Microphone Array A | Speaker B |
| D. Voice input, no spoken response | Microphone A | *(none)* |
| E. Spoken response, no voice input | *(none)* | Speaker B |
| F. No voice participation | *(none)* | *(none)* |

A single physical device capable of both functions (Configuration A) is represented by **two atomic
`RoomInteractionFunctionAssignment` records, one per function** — each referencing the native
capability appropriate to its own function. Where Home Assistant represents the device's microphone and
speaker as one combined native reference, both records reference that same `participating_capability_reference`;
where Home Assistant instead exposes separate native entities for the device's microphone and speaker
capabilities, each record references its own corresponding entity. **This specification does not assume
or require Home Assistant to expose one combined reference** — it requires only that each record name
the capability appropriate to its own function, never a special-cased "dual-role" record type, and
never a fabricated capability identity where the native representation does not provide one.

**Issue #196 addition — `interface` and `physical_remote` follow the identical pattern.** Each is an
independent column in the same shape: a Room may have zero, one, or more `interface` records and zero,
one, or more `physical_remote` records, combined with any of the Configurations A–F above with no
additional data model. For example, a Room with Configuration C (dedicated microphone + independent
speaker) may additionally carry an `interface` record (a wall kiosk) and a `physical_remote` record (an
integrated remote), each independently participating or absent — the four functions are orthogonal, and
no combination requires special-case schema.

---

## 7. Truth boundary (Foundation vs. Truth)

**Configuration is not runtime truth.** A `RoomInteractionFunctionAssignment` record stating "Speaker B
is the configured `spoken_response_output` for the Den" means exactly that — a configured relationship
— and **never** means "Speaker B is currently available, powered on, or reachable."

This restates, for `voice_input`/`spoken_response_output` specifically, Room Configuration's existing,
unchanged guarantee: *"What Room Configuration will never guarantee: that a participating capability is
currently available"* ([room-configuration-contract.md](../contracts/room-configuration-contract.md)).

**Foundation is not made responsible for polling or asserting runtime availability by this
specification.** Where a configured endpoint is unavailable at runtime, existing governed
failure-and-degradation mechanisms ([failure-and-degradation.md](failure-and-degradation.md)) apply
unchanged — this specification introduces no new runtime-availability mechanism.

---

## 8. Concierge consumption contract

Concierge consumes the configured relationship; it does not own, cache, or hard-code a mapping.

**Required consumption shape:** given a resolved Room Context (Interaction Space), Concierge (or the
existing governed response-delivery mechanism it uses) obtains the Room's configured
`spoken_response_output` assignment(s) from Foundation/Room Configuration **at the time a response is
being delivered**, through the same configured-relationship lookup it already uses for other experience
endpoints (`music`, `video`, `announcement`, `conversation`). **No new lookup mechanism, cache, or
mapping table is created** — this is the existing Response Delivery Space mechanism
([concierge-contract.md](../contracts/concierge-contract.md) §6), consuming one more configured
endpoint category.

**Issue #196 addition — the general query shape Concierge needs, generalized across all four
functions.** Concierge's existing resolution path already answers these by configured-relationship
lookup, keyed by `(room_id, function)`, with no new mechanism per function:

| Concierge question | Answered by |
|---|---|
| What voice input produced this request? | The originating `voice_input` record's `participating_capability_reference`, supplying originating-space evidence only (§9; never identity/authority) |
| Which Place does that input belong to? | Existing Room Context resolution (unchanged; `room_id` on the matched `voice_input` record) |
| Which configured audio output should receive a response? | The Room's `spoken_response_output` record(s), via the existing Response Delivery Space lookup (unchanged from the paragraph above) |
| Which visual/manual interface is associated with the Place? | The Room's `interface` record(s), via the identical configured-relationship lookup, keyed by `function = interface` |
| Which physical remote is associated with the Place? | The Room's `physical_remote` record(s), via the identical configured-relationship lookup, keyed by `function = physical_remote` |
| Which capability relationships are valid here? | The full set of the Room's `RoomInteractionFunctionAssignment` records with `participation_state = participating`, read directly — never inferred from device capability alone (§5, "no silent assignment") |

No per-function lookup table, cache, or mapping is created beyond the one generalized
`(room_id, function)` query already required for `voice_input`/`spoken_response_output` — `interface`
and `physical_remote` are two further values of the same `function` key, not a new mechanism.

**Explicitly prohibited** (restating Concierge Contract Hard Prohibition #3, not creating a new rule):

- `microphone_entity_X -> speaker_entity_Y` hard-coded inside Concierge or any voice-routing component;
- `room -> kiosk_entity` or `room -> remote_entity` hard-coded inside Concierge (Issue #196 addition,
  same prohibition applied to `interface`/`physical_remote`);
- any runtime search across Room devices to find "a reasonable speaker" when no `spoken_response_output`
  is configured — the correct behavior is to report none configured, not to guess.

**Existing Concierge audio-delivery responsibilities are reused unchanged**: room speaker selection,
Sonos selection, pause, duck, TTS delivery, and resume behavior are not reimplemented, forked, or
duplicated by this specification or by whatever eventually implements it. **A successful interaction
does not require a spoken response** — where the physical result sufficiently communicates success (or
no `spoken_response_output` is configured), Concierge may remain silent, per its existing "must not
announce merely because permitted to act" prohibition.

---

## 9. Merged Rooms

A microphone detecting an interaction provides **originating-space evidence only**. It never
independently establishes the final Interaction Space, person identity, presence truth, authority, or
intent — those remain Identity's, Truth's, Operational Trust's, and Concierge's respectively, exactly as
today.

**Merged Room representation**: no separate `RoomInteractionFunctionAssignment` record shape is created
for a Merged Room. A `room_id` may reference a Merged Room exactly as it already can for any other
experience-endpoint assignment, consistent with **DL-67**/**DL-68** (a Physical Room participates in at
most one Merged Room at a time; a Merged Room has no native Home Assistant representation and is never
a second physical-topology authority). Concierge's existing Room Context resolution order (the
capturing device's assigned Room, then its exclusive Merged Room membership where applicable) is
unchanged by this specification.

---

## 10. Privacy

This specification **introduces no recording, retention, or new durable voice/audio artifact.** A
`RoomInteractionFunctionAssignment` record describes a **permitted, configured relationship** — it does
not cause raw microphone audio to become durable household data, and it carries no audio payload of any
kind. Existing microphone/voice/privacy/identity handling requirements
([privacy.md](privacy.md), [identity-contract.md](../contracts/identity-contract.md)) are unchanged and
fully preserved.

---

## 11. Operational Trust, Identity, and Continuity preservation

**Configuring `voice_input` or `spoken_response_output` grants no action authority.** A recognized
command continues through the existing authorization/trust path appropriate to the requested action,
unchanged. This specification creates no voice-specific bypass around permissions, consent, privacy,
authority, confirmation, or autonomy rules.

**A `voice_input` endpoint supplies interaction-origin evidence only; it does not by itself establish
who spoke.** Existing speaker-attribution ownership and contracts (Identity, Voice Identity's governed
outputs) are unchanged. This specification adds only the minimum metadata needed to associate an
originating capability with a Room Configuration assignment (§4.1's `participating_capability_reference`
and `room_id`) — it does not implement speaker-recognition algorithms or STT interception logic.

**Continuity's session/interaction-state boundaries are unchanged.** The assignments introduced here
may later be consumed by performance-aware voice-processing work (explicitly out of scope here, §1);
this specification implements no speech routing of any kind.

---

## 12. Graceful degradation (restated, not newly designed)

| Condition | Required behavior |
|---|---|
| `voice_input` unavailable | Dashboard, remote, and physical controls remain usable — unaffected, per **Capability Unavailable**'s existing "never silently reduced" rule |
| `spoken_response_output` unavailable | An otherwise-permitted Home action still completes; only the response is affected |
| No `spoken_response_output` configured | Valid state (§6, Configuration D, F); not an error |
| No `voice_input` configured | Valid state (§6, Configuration E, F); not an error |
| `interface` unavailable (Issue #196 addition) | Voice, remote, and other configured interaction surfaces remain usable; only the visual/manual surface is affected |
| `physical_remote` unavailable (Issue #196 addition) | Voice, interface, and other configured interaction surfaces remain usable; only the remote-triggered surface is affected |
| No `interface` or no `physical_remote` configured (Issue #196 addition) | Valid state, identical in kind to the voice_input/spoken_response_output absent-states above; not an error |

**No new runtime-failover behavior is invented.** This specification describes configuration
representation only; existing governed runtime behavior consumes it unchanged.

---

## 13. Backward compatibility and migration

### Inspection finding

No Foundation Room Setup implementation currently exists (§1, §2). There is therefore **no existing
runtime data to migrate** in any repository available for this specification. The "existing
representation" available for inspection is the **documented model**
([room-configuration.md](../models/room-configuration.md), [room-configuration-contract.md](../contracts/room-configuration-contract.md)),
which describes "participating voice assistants" as a single undifferentiated concept (capture and
response together), not existing persisted records.

### Migration semantics (for when an implementation surface exists)

**A currently configured, integrated "participating voice assistant" (one device, both functions
historically undifferentiated) must continue to behave as an integrated input/output device.** Safe
default: a single existing "participating voice assistant" entry, on first migration to this model,
expands to **two** atomic `RoomInteractionFunctionAssignment` records — one `voice_input` record and
one `spoken_response_output` record — preserving Configuration A (§6) exactly, with no household-visible
behavior change.

- **Both assignments may belong to the same physical/native Home Assistant device.** Where that device
  exposes its microphone and speaker capability through Home Assistant as a single combined native
  reference, both migrated records reference that same `participating_capability_reference`.
- **Each assignment references the native capability/entity appropriate to its own interaction
  function, where Home Assistant exposes those capabilities independently.** Where the device's
  microphone and speaker are instead separate native entities, the `voice_input` record references the
  microphone entity and the `spoken_response_output` record references the speaker entity — both still
  describing one integrated device, with no household-visible behavior change.
- **The migration must not fabricate separate capability identities where the underlying Home Assistant
  representation does not provide them.** If the existing data cannot distinguish the device's
  microphone-capable reference from its speaker-capable reference, the same single native reference is
  used for both migrated records rather than inventing a synthetic split.
- **Any actual representational limitation discovered during executable implementation must be
  documented rather than guessed around in this specification** — this document states the rule above
  as the safe default; it does not anticipate every native Home Assistant device/entity shape in
  advance.

**This default applies only to data migration, never to new configuration.** A household configuring a
Room for the first time under this specification answers the four Room Setup questions (§5)
independently and receives no automatic multi-assignment merely because a capability has more than one
capability.

**If a future implementation surface's actual persisted data does not provide enough information to
distinguish "this was configured as integrated" from "this was never configured," the safe migration
is the integrated-default above** (preserving existing behavior) **and the gap must be documented in
that implementation's own migration notes — this specification does not fabricate a more specific rule
without that data.**

**Issue #196 addition — `interface` and `physical_remote` have no pre-existing undifferentiated
concept to migrate.** Unlike `voice_input`/`spoken_response_output` (which migrate from the existing
"participating voice assistant" concept, above), no equivalent existing Room Configuration field
conflates an interface or physical-remote capability with anything else. There is therefore no
migration default to define for these two functions: a household configures them for the first time
directly under §5's independent-question model, with no pre-existing data and no behavior-preservation
default required.

### Home Assistant boundary

Home Assistant's native devices, entities, media players, `assist_satellite` objects, integrations, and
discovery mechanisms remain Home Assistant's. **No duplicate HTBW-owned device registry is created.**
HTBW owns only the household semantics layered on top: Room Configuration, participation, Interaction
Function Assignment, and the governed relationships in §4.

---

## 14. Acceptance scenarios (implementation-neutral)

These restate the twelve testing requirements as scenarios a future implementation must satisfy, plus
one additional scenario (13) added by this specification's cardinality/capability remediation to
demonstrate record-level multiplicity explicitly. They are **not executable tests** — no test
framework, test file, or code is introduced by this specification.

1. **Integrated device, both functions.** A Room configures one physical device as both `voice_input`
   and `spoken_response_output`, via two atomic assignment records. Each record references the native
   capability appropriate to its own function — the same combined reference where Home Assistant
   exposes one, or the device's separate microphone/speaker entities where it exposes two — never a
   fabricated capability identity.
2. **Integrated device, input only; separate output device.** A Room configures Device A as
   `voice_input` only and Device B as `spoken_response_output`. Device A's speaker capability (if any)
   is never used for the response.
3. **Dedicated input + separate output.** A Room configures a microphone-array capability as
   `voice_input` and an independent speaker/media capability as `spoken_response_output`, with no shared
   device.
4. **Voice input, no spoken response.** A Room has zero `spoken_response_output` records and one or
   more `voice_input` records — a valid, non-error state.
5. **Spoken response, no voice input.** A Room has zero `voice_input` records and one or more
   `spoken_response_output` records — a valid, non-error state.
6. **Neither configured.** A Room has zero records for both functions — a valid, non-error state.
7. **Assignment is not inferred from capability, and each record is unambiguous.** A capability exposing
   both microphone and speaker capability, with only a `voice_input` record created for it, never
   resolves a `spoken_response_output` assignment for that Room. Each `RoomInteractionFunctionAssignment`
   record names exactly one Room, one function, and one capability — never a list or a dual-function
   record.
8. **Configuration does not assert availability.** A configured `spoken_response_output` record with its
   underlying Home Assistant entity in an unavailable/unknown state still reads as "configured"; the
   availability question is answered by Truth/runtime mechanisms, not by the configuration record.
9. **Merged Room validity.** A Merged Room (per **DL-67**/**DL-68**) carries `voice_input` and
   `spoken_response_output` records exactly as a Physical Room does, with no second,
   Merged-Room-specific schema.
10. **Backward-compatible integrated configuration.** An existing "integrated voice assistant"
    configuration, once represented under this model, continues to resolve both functions with no
    household-visible behavior change (§13).
11. **Concierge resolves without a hard-coded mapping.** Given a resolved Room Context, the configured
    `spoken_response_output` record(s) are obtainable through the existing Room Configuration/experience-
    endpoint lookup path, with no product-specific (for example, Sonos-specific) mapping logic inside
    Concierge.
12. **No vendor or Reference Home identifiers in the core model.** The schema in §4, the Room Setup
    requirements in §5, and the Concierge consumption contract in §8 contain no room names, vendor
    names (reSpeaker, Seeed Studio, Sonos, ESPHome, Home Assistant Voice), entity IDs, device IDs, or
    network addresses.
13. **Multiple assignments for one function are schema-valid.** A Room has two or more `voice_input`
    records (for example, two microphones in a large room) or two or more `spoken_response_output`
    records (for example, an output group). This is a valid, ordinary schema state. **No priority,
    preferred-endpoint, fallback, or runtime fan-out behavior among the multiple records is specified,
    implied, or required by this scenario** — only that the schema permits more than one record for the
    same Room+function without alteration.

**Scenarios 14–16 added by Issue #196:**

14. **`interface` and `physical_remote` are independently configurable, like the first two functions.**
    A Room configures an `interface` record (a wall kiosk) and/or a `physical_remote` record (an
    integrated remote) independently of `voice_input`/`spoken_response_output` and of each other; no
    function's presence or absence implies any other function's assignment.
15. **No network-endpoint resolution mechanism is required for the first vertical slice.** Every
    `participating_capability_reference` in §4.1 (for all four functions) is satisfiable by a native
    Home Assistant entity/device reference alone (DL-87 rank 1); no stable-DNS, DHCP-reservation, or
    literal-IP mechanism is exercised, configured, or required by this specification (§18.2).
16. **Configuration-time enforcement rejects a non-native reference structurally, not by runtime
    warning.** Because Room Setup's selection surfaces for all four functions are native Home
    Assistant selectors (§18.3), a literal IP address or vendor-specific identifier is never an
    available choice in the configuration flow — enforcement occurs by construction, not by a
    separate validation step reacting to an already-entered invalid value.

---

## 15. Deferred work

**Deferred to the Performance-Aware Voice Processing workstream** (now specified, not implemented, in
[performance-aware-voice-processing-specification.md](performance-aware-voice-processing-specification.md),
Issue #200, pending owner acceptance): STT-provider selection and routing, automatic pipeline fallback,
Home Intelligence/Ollama escalation routing, latency-based processing-path selection, latency
instrumentation, and the fast-deterministic-path mechanism.

**Deferred pending an authorized HTBW Core implementation surface**: all executable code — the actual
Foundation Room Setup UI/flow changes, the actual Room Configuration persistence changes, and the actual
Concierge consumption code. This specification is written to make that future implementation direct,
but does not perform it.

---

## 16. Relationship to existing decisions and contracts

| Item | Relationship |
|---|---|
| **DL-90**, **DL-91** (accepted, #198) | Operationalized by this specification; not reopened |
| **DL-55** | Reused — experience-endpoint category set remains extensible household vocabulary |
| **DL-67**, **DL-68** (Merged Room) | Reused, not reopened (§9) |
| **DL-87**, **DL-88** (accepted, #195) | **Issue #196 addition.** Operationalized, not merely cited: DL-88's `interface`/`physical_remote` relationships are specified in §3–§6/§8; DL-87's resolution-order mechanics are resolved for this workstream in §18. Neither decision is reopened or narrowed. |
| Concierge Contract Hard Prohibition #3 | Reused, restated for `spoken_response_output` specifically (§8), and for `interface`/`physical_remote` (Issue #196 addition, §8) |
| [room-configuration-contract.md](../contracts/room-configuration-contract.md) "will never guarantee... currently available" | Reused unchanged (§7) |
| **OD-01** (Room Configuration persistence shape) | Unaffected; this specification's field list is illustrative and must reconcile with whatever OD-01 eventually resolves |
| [greenfield-mandate.md](greenfield-mandate.md) | Governs why no executable implementation is produced here (§1) |
| [home-assistant-boundary.md](home-assistant-boundary.md) (Issue #196 addition) | Verified native Area/Device/Entity registry behavior and the "prefer HA selectors" principle, grounding §18 |

---

## 17. Explicit non-goals

- Does not implement, or produce executable code for, any part of this specification.
- Does not create an HTBW Core implementation repository or surface.
- Does not touch the `concierge`, `voice_identity`, or `asset_intelligence` repositories.
- Does not implement Performance-Aware Voice Processing in any form.
- Does not select a persistence mechanism, storage engine, or API shape beyond the illustrative field
  list in §4.
- Does not reopen DL-90, DL-91, DL-55, DL-67, DL-68, DL-87, DL-88, or Concierge Contract Hard
  Prohibition #3.
- Does not make any Reference Home vendor, device, or entity a dependency of the specification.
- **(Issue #196 addition)** Does not create a new Home Assistant entity domain, integration, or
  kiosk/remote-management platform.
- **(Issue #196 addition)** Does not create an HTBW-owned DNS, DHCP, or any other network-infrastructure
  mechanism (§18.2).
- **(Issue #196 addition)** Does not fabricate a native-reference type for an `interface` or
  `physical_remote` capability that has no native Home Assistant representation (§18.1) — that gap is
  recorded, not resolved, by this specification.

---

## 18. Issue #196 extension — DL-87 implementation mechanics for this workstream

This section resolves the four "Remaining questions" in Issue #196's body for the Foundation Room
Interaction Roles workstream specifically. It does not decide DL-87/DL-88 mechanics for any other
workstream, and it does not reopen DL-87 or DL-88.

### 18.1 Native reference type per function

Consistent with §4.1's `participating_capability_reference` and DL-87 rank 1 (a Home Assistant native
entity/device/area/config-entry identity):

| Function | Native reference | Basis |
|---|---|---|
| `voice_input` | Home Assistant `entity_id` (typically an `assist_satellite` or microphone-capable entity) or `device_id` | Already established by the existing specification (§4.1); unchanged |
| `spoken_response_output` | Home Assistant `entity_id` (typically a `media_player` entity) or `device_id` | Already established; unchanged |
| `interface` | Home Assistant `device_id` of the kiosk/display hardware **where Home Assistant has a native device representation for it** (for example, a kiosk-management integration that registers the device) | Home Assistant's device registry is the native pattern for physical hardware ([home-assistant-boundary.md](home-assistant-boundary.md)'s verified Device/Area registry findings); no HTBW-owned device identity is invented |
| `physical_remote` | Home Assistant `entity_id` in a native domain that represents the remote (for example, `remote`, `event`, or `button`) or `device_id` where the remote has no distinct entity | Mirrors `voice_input`/`spoken_response_output`'s existing entity-or-device pattern; no new reference type is introduced |

**Known, recorded limitation — not resolved by this specification.** Where a candidate `interface` or
`physical_remote` endpoint has **no** native Home Assistant device or entity representation at all (for
example, a dashboard shown on a tablet with no corresponding Home Assistant integration/device), this
specification does not fabricate a substitute identity (a URL, a device name, or a generated ID) to make
it referenceable. That endpoint is **not yet eligible** for an `interface`/`physical_remote`
assignment under this specification until Home Assistant represents it natively (for example, through an
appropriate kiosk-management or remote integration) — consistent with §4.1's "never a literal IP, MAC,
or vendor-specific identifier" rule and with not inventing an identity substrate HA does not provide.
This is recorded as a known gap, not silently worked around.

### 18.2 Network-endpoint resolution mechanics (DL-87 ranks 3–5)

**Finding: this workstream needs no HTBW-owned network-endpoint resolution at all.** Every
`participating_capability_reference` for all four functions (§18.1) is a Home Assistant native
`entity_id`/`device_id` — DL-87 rank 1. Home Assistant itself owns the underlying device/integration
connection (IP address, hostname, Bluetooth/Zigbee/Z-Wave pairing, cloud-relay session, or whatever
transport the integration uses); HTBW never stores, resolves, or reasons about that connection.

This directly answers Issue #196's remaining questions 2 and 4:

- **No stable-local-DNS mechanism is needed for this workstream** (question 2). DL-87 rank 3 is reached
  only where rank 1 and rank 2 are both unavailable, which does not occur here — every function's
  reference is a native HA object. **No HTBW DNS mechanism is created.** If a future, different
  workstream genuinely requires rank 3, that is a separate question for that workstream, not decided
  here.
- **No centrally reserved DHCP representation is needed for this workstream** (question 4), for the
  same reason. If a future workstream's native reference is ever insufficient and a literal endpoint
  address becomes necessary, **DL-89's existing, accepted technical-debt recording convention**
  (applied by **#197**) is the correct recording mechanism — this specification does not create a
  second one.

**This is a finding scoped to the Foundation Room Interaction Roles workstream, not a general claim
that HTBW never needs DL-87 ranks 3–5 anywhere.** Other workstreams (for example, a future security-
camera or recorder integration without a native Home Assistant object) may still require them; this
specification neither authorizes nor forecloses that separately.

### 18.3 Resolution-order enforcement (question 3)

**Enforcement occurs at Room Setup's configuration-time selection surface, using native Home Assistant
selectors, not a separate post-entry validation step.** This follows [home-assistant-boundary.md](home-assistant-boundary.md)'s
established principle that "HTBW surfaces should feel like Home Assistant. Prefer HA navigation
patterns, dialogs, selectors" — Room Setup's config/options-flow screens for all four functions present
an **entity/device selector** (Home Assistant's native `EntitySelector`/`DeviceSelector` pattern) rather
than a free-text field. Because the selection surface only offers native HA objects as choices, a
literal IP address, MAC address, or vendor-specific identifier is **never an enterable value** —
enforcement is structural (by construction), not a warning reacting to an already-entered value (restates
Issue #196's own example "enforcement" question with a stronger answer than a warning).

This distinguishes the three enforcement layers Issue #196 asked to separate:

| Layer | Role here |
|---|---|
| **Configuration-time validation** | The selector itself restricts input to native HA references (§18.1); this is where DL-87's resolution order is enforced for this workstream |
| **Runtime availability validation** | Unchanged — existing failure-and-degradation mechanisms (§7, §12) determine whether a configured, valid reference is currently reachable; this is never conflated with configuration-time validity |
| **Discovery** | Unchanged — discovery (§5, "Discovery reuse") only identifies **candidates** for the selector; it never silently assigns, substitutes, or validates on HTBW's behalf ("validation is not discovery," restated unchanged) |

No new Foundation-side or Concierge-side enforcement mechanism is created; the native selector is
sufficient for this workstream, and no literal-IP-entry case therefore needs further foundation
validation. If a future field other than `participating_capability_reference` is ever introduced that
can hold a literal endpoint (not current for this workstream, §18.2), schema validation at that field's
own config/options-flow step would be the analogous enforcement point — not decided further here since
no such field exists in this specification.

### 18.4 Diagnostics implications

Home Assistant's native diagnostics/repairs mechanisms ([home-assistant-boundary.md](home-assistant-boundary.md)'s
verified Repairs-platform findings) are reused, not duplicated. The minimum diagnostics information this
workstream requires: for each `RoomInteractionFunctionAssignment` record, whether its
`participating_capability_reference` still resolves to a known Home Assistant entity/device
(**existence**, not current availability — §7 remains unchanged). A reference that no longer resolves
(for example, after the referenced device is removed from Home Assistant) is a candidate for an existing
native Repairs-style issue, surfaced through Home Assistant's own mechanism; this specification does not
create a new diagnostics framework or HTBW-owned health model.

---

## Related documents

- [adr-decoupled-voice-interaction-capability-architecture.md](adr-decoupled-voice-interaction-capability-architecture.md)
- [adr-stable-endpoint-identity-and-network-boundary-independence.md](adr-stable-endpoint-identity-and-network-boundary-independence.md)
- [greenfield-mandate.md](greenfield-mandate.md)
- [failure-and-degradation.md](failure-and-degradation.md)
- [privacy.md](privacy.md)
- [../contracts/foundation-contract.md](../contracts/foundation-contract.md)
- [../contracts/room-configuration-contract.md](../contracts/room-configuration-contract.md)
- [../contracts/concierge-contract.md](../contracts/concierge-contract.md)
- [../contracts/identity-contract.md](../contracts/identity-contract.md)
- [../contracts/continuity-contract.md](../contracts/continuity-contract.md)
- [../contracts/operational-trust-contract.md](../contracts/operational-trust-contract.md)
- [../models/room-configuration.md](../models/room-configuration.md)
- [../models/glossary.md](../models/glossary.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
- [performance-aware-voice-processing-specification.md](performance-aware-voice-processing-specification.md) — the sibling Performance-Aware Voice Processing workstream (Issue #200, pending owner acceptance)
- [home-assistant-boundary.md](home-assistant-boundary.md) — verified native Area/Device/Entity/Repairs registry behavior grounding §18 (Issue #196 addition)
