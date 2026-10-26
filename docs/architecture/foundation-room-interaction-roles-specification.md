# Foundation Room Interaction Roles — Implementation-Ready Specification

> **Document status: Active — subordinate to the HTBW canonical architecture.**
> Canonical authority: [adr-decoupled-voice-interaction-capability-architecture.md](adr-decoupled-voice-interaction-capability-architecture.md)
> (**DL-90**, **DL-91**, accepted 2026-10-26, Issue #198), [framework.md](framework.md), and
> [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> **Specification only. Authorizes no executable implementation.** Tracked at Issue #199.

---

## 1. Status and scope

This document operationalizes the accepted **DL-90** (Decoupled Voice Interaction Capability Model) and
**DL-91** (Performance-Aware, Provider-Independent Voice Processing Principle) into an
implementation-ready schema/contract specification for the **Foundation Room Interaction Roles**
workstream only. It does not reopen, narrow, or redecide DL-90 or DL-91.

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
| [home-assistant-boundary.md](home-assistant-boundary.md) | Native device/entity/Area/`assist_satellite` discovery and registry ownership — reused, not duplicated |
| [../models/glossary.md](../models/glossary.md) | Capability, Participation, Interaction Function Assignment, `voice_input`, `spoken_response_output` term definitions |
| Existing setup/configuration implementation | **None found.** No Foundation Room Setup implementation exists in any repository available for inspection (see §1) |
| Existing tests covering Room Configuration | **None found**, for the same reason |

---

## 3. Core model

```
Room
  -> voice_input                  (Interaction Function Assignment)
  -> spoken_response_output       (Interaction Function Assignment)
```

Both are **Interaction Function Assignments** under **DL-90**'s triad, restated here for
implementation:

| Tier | Meaning |
|---|---|
| **Capability** | What a Home Assistant device/entity can technically provide (for example, a device exposing both a microphone and a speaker) — read from the native Home Assistant device/entity registry, never duplicated into an HTBW-owned registry |
| **Participation** | Whether that capability has been explicitly selected to take part in a Room's interaction model |
| **Interaction Function Assignment** | Which specific function — `voice_input`, `spoken_response_output`, or another existing experience-endpoint category (`music`, `video`, `announcement`, `conversation`) — a participating capability is assigned to fulfill in the Room |

**A capability's existence never implies participation, and participation never implies a specific
Interaction Function Assignment.** Each is independently, explicitly configured.

---

## 4. Schema / data contract

This is a **data-shape specification**, not a storage-engine or ORM design. Field names are
illustrative and MUST be reconciled with whatever persistence mechanism the eventual HTBW Core
implementation surface adopts (see **OD-01**, Room Configuration's own open persistence-shape
decision, unaffected by this specification).

### 4.1 `RoomInteractionFunctionAssignment` (conceptual record)

| Field | Type | Cardinality | Required | Description |
|---|---|---|---|---|
| `room_id` | Foundation Room reference | 1 | Yes | The Room (or Merged Room) this assignment belongs to |
| `function` | Enumeration | 1 | Yes | `voice_input` \| `spoken_response_output` \| other existing experience-endpoint category (extensible per **DL-55**) |
| `participating_capability_reference` | Native Home Assistant reference (entity_id/device_id or equivalent native identifier) | **0..N** | No | The native capability assigned this function. **Never a literal IP, MAC, or vendor-specific identifier** — the native Home Assistant reference only, consistent with the Stable Endpoint Identity resolution order (**DL-87**, pending #195, cited as forward-compatible guidance, not a dependency of this specification) |
| `participation_state` | Enumeration | 1 per reference | Yes | `participating` \| `not_selected` \| `deliberately_excluded` — reusing Room Configuration's existing three-state model unchanged |
| `assigned_at` / `updated_at` | Timestamp | 1 | Yes | Reuses Room Configuration's existing Change Record / configuration-history mechanism; no new history mechanism is created |

**Cardinality is explicitly list-valued (`0..N`), never a single scalar reference.** This satisfies the
no-cardinality-assumption requirement (multiple microphones, output groups, future redundancy) without
building multi-endpoint orchestration logic now — an empty, single-item, or multi-item list are all
valid today; only the schema shape, not the runtime fan-out behavior, is specified here.

### 4.2 Relationship to existing Room Configuration fields

This record is a **new, additional row shape within Room Configuration's existing "which experience
endpoints exist" and "which voice assistants are assigned" data**, not a parallel store. Where an
implementation surface already represents "participating voice assistants" as a list, `voice_input` and
`spoken_response_output` assignments are two further entries in that same list shape, distinguished by
`function`, not two new unrelated structures.

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
not replaced, to let a household answer **two independent questions** per Room:

1. **How should the Home hear voice interactions in this room?** (configures `voice_input`
   participation and assignment)
2. **Where should the Home deliver spoken responses in this room?** (configures
   `spoken_response_output` participation and assignment)

### Requirements

| Requirement | Statement |
|---|---|
| Independence | The two questions must be answerable independently. Answering one must never default-assign the other. |
| Discovery reuse | Candidate capabilities are discovered through existing Home Assistant-native device/entity/Area discovery and capability reporting. **No HTBW-owned physical-device discovery mechanism is created.** |
| No silent assignment | A device possessing both microphone and speaker capability must not be auto-assigned both functions merely because discovery found it. Discovery identifies **candidates**; the household's (or configuration flow's) explicit choice establishes the **assignment**. |
| No product-specific modes | The setup experience must not introduce separate "ReSpeaker mode," "Sonos mode," "microphone-array mode," or "Voice Assistant mode" constructs. The underlying governed model is capability/participation/assignment-based; a presentation-layer convenience (for example, a single setup screen offering "use this device for both" as a shortcut) may exist **only** as a UI convenience over the same underlying independent assignments — never as a distinct data model. |
| Both-absent is valid | A Room with neither `voice_input` nor `spoken_response_output` configured is a valid, ordinary configuration state, not an error or an incomplete-configuration warning. |

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

A single physical device capable of both functions (Configuration A) is represented by **one capability
participating in both Interaction Function Assignments** — two `RoomInteractionFunctionAssignment`
records sharing the same `participating_capability_reference`, each with its own `function` value — not
by a special-cased "dual-role" record type.

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

**Explicitly prohibited** (restating Concierge Contract Hard Prohibition #3, not creating a new rule):

- `microphone_entity_X -> speaker_entity_Y` hard-coded inside Concierge or any voice-routing component;
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
historically undifferentiated) must continue to behave as an integrated input/output device** — safe
default: a single existing "participating voice assistant" entry, on first migration to this model,
expands to **two** `RoomInteractionFunctionAssignment` records (`voice_input` and
`spoken_response_output`) **both referencing the same capability**, preserving Configuration A (§6)
exactly, with no household-visible behavior change.

**This default applies only to data migration, never to new configuration.** A household configuring a
Room for the first time under this specification answers the two Room Setup questions (§5) independently
and receives no automatic dual-assignment merely because a capability has both capabilities.

**If a future implementation surface's actual persisted data does not provide enough information to
distinguish "this was configured as integrated" from "this was never configured," the safe migration
is the integrated-default above** (preserving existing behavior) **and the gap must be documented in
that implementation's own migration notes — this specification does not fabricate a more specific rule
without that data.**

### Home Assistant boundary

Home Assistant's native devices, entities, media players, `assist_satellite` objects, integrations, and
discovery mechanisms remain Home Assistant's. **No duplicate HTBW-owned device registry is created.**
HTBW owns only the household semantics layered on top: Room Configuration, participation, Interaction
Function Assignment, and the governed relationships in §4.

---

## 14. Acceptance scenarios (implementation-neutral)

These restate the twelve testing requirements as scenarios a future implementation must satisfy. They
are **not executable tests** — no test framework, test file, or code is introduced by this
specification.

1. **Integrated device, both functions.** A Room configures one capability as both `voice_input` and
   `spoken_response_output`. Both assignments resolve to the same `participating_capability_reference`.
2. **Integrated device, input only; separate output device.** A Room configures Device A as
   `voice_input` only and Device B as `spoken_response_output`. Device A's speaker capability (if any)
   is never used for the response.
3. **Dedicated input + separate output.** A Room configures a microphone-array capability as
   `voice_input` and an independent speaker/media capability as `spoken_response_output`, with no shared
   device.
4. **Voice input, no spoken response.** A Room configures `voice_input` only; `spoken_response_output`
   has zero participating records — a valid, non-error state.
5. **Spoken response, no voice input.** A Room configures `spoken_response_output` only;
   `voice_input` has zero participating records — a valid, non-error state.
6. **Neither configured.** A Room has zero records for both functions — a valid, non-error state.
7. **Assignment is not inferred from capability.** A capability exposing both microphone and speaker
   capability, with only `voice_input` explicitly assigned, never resolves a `spoken_response_output`
   assignment for that Room.
8. **Configuration does not assert availability.** A configured `spoken_response_output` with its
   underlying Home Assistant entity in an unavailable/unknown state still reads as "configured"; the
   availability question is answered by Truth/runtime mechanisms, not by the configuration record.
9. **Merged Room validity.** A Merged Room (per **DL-67**/**DL-68**) carries `voice_input` and
   `spoken_response_output` assignments exactly as a Physical Room does, with no second,
   Merged-Room-specific schema.
10. **Backward-compatible integrated configuration.** An existing "integrated voice assistant"
    configuration, once represented under this model, continues to resolve both functions to the same
    device with no household-visible behavior change (§13).
11. **Concierge resolves without a hard-coded mapping.** Given a resolved Room Context, the configured
    `spoken_response_output` is obtainable through the existing Room Configuration/experience-endpoint
    lookup path, with no product-specific (for example, Sonos-specific) mapping logic inside Concierge.
12. **No vendor or Reference Home identifiers in the core model.** The schema in §4, the Room Setup
    requirements in §5, and the Concierge consumption contract in §8 contain no room names, vendor
    names (reSpeaker, Seeed Studio, Sonos, ESPHome, Home Assistant Voice), entity IDs, device IDs, or
    network addresses.

---

## 15. Deferred work

**Deferred to the Performance-Aware Voice Processing workstream** (not opened as an issue, not
implemented, per the governing execution instructions for this specification): STT-provider selection
and routing, automatic pipeline fallback, Home Intelligence/Ollama escalation routing, latency-based
processing-path selection, latency instrumentation, and the fast-deterministic-path mechanism.

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
| **DL-87** (pending, #195 — stable identity resolution order) | Cited as forward-compatible guidance for `participating_capability_reference` (§4.1); not a dependency of this specification, and not reopened |
| Concierge Contract Hard Prohibition #3 | Reused, restated for `spoken_response_output` specifically (§8) |
| [room-configuration-contract.md](../contracts/room-configuration-contract.md) "will never guarantee... currently available" | Reused unchanged (§7) |
| **OD-01** (Room Configuration persistence shape) | Unaffected; this specification's field list is illustrative and must reconcile with whatever OD-01 eventually resolves |
| [greenfield-mandate.md](greenfield-mandate.md) | Governs why no executable implementation is produced here (§1) |

---

## 17. Explicit non-goals

- Does not implement, or produce executable code for, any part of this specification.
- Does not create an HTBW Core implementation repository or surface.
- Does not touch the `concierge`, `voice_identity`, or `asset_intelligence` repositories.
- Does not implement Performance-Aware Voice Processing in any form.
- Does not select a persistence mechanism, storage engine, or API shape beyond the illustrative field
  list in §4.
- Does not reopen DL-90, DL-91, DL-55, DL-67, DL-68, DL-87, or Concierge Contract Hard Prohibition #3.
- Does not make any Reference Home vendor, device, or entity a dependency of the specification.

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
