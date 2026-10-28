# Room Configuration Contract

> **Document status: Canonical contract.**
> Responsibility: **Foundation**. Model:
> [../models/room-configuration.md](../models/room-configuration.md).

---

## Owning responsibility

**Foundation.** Room Configuration is **not** owned by Concierge. Any document placing Room
Configuration inside Concierge is superseded.

Room Configuration is an **interaction-definition model**. It is not an inventory screen and not
merely a location model.

---

## What Room Configuration guarantees

For each Room, an explicit and persisted definition of:

- The Room's household-facing name
- Which Physical Rooms constitute the Room, where it is a Merged Room
- Which assets and capabilities **participate**
- Which assets are **intentionally excluded**
- The **participation state** of each asset: `participating`, `not_selected`, or
  `deliberately_excluded`
- **Exclusion metadata (DL-103)** for every `deliberately_excluded` asset — a required structured
  reason (`privacy`, `designated_use`, or `other` with a mandatory note), scope inherited from the
  Participation record itself, and temporality following the same "in effect until changed" pattern as
  Consent (**DL-56**). See [../models/room-configuration.md](../models/room-configuration.md),
  *Exclusion Metadata (DL-103)*
- Which capabilities are **exposed** to residents
- Which vocabulary terms are available, and what they resolve to
- Which sensors are **eligible contributors** to Room-scoped Composite Facts
- Which Environmental Purpose (temperature, humidity, dew point, illuminance, UV, VOC, particulates,
  CO2, mold index, leak, pressure, vibration, noise, and other extensible purposes) each environmental
  source represents, and its disambiguation state — **Primary Authority** (required for the ordinary
  path), **Secondary/Corroborating**, or **Explicit Exclusion** (**DL-60**, narrowed to three states by
  **DL-62**)
- Which experience endpoints exist (music, video, announcement, conversation) — **this category set
  is extensible household vocabulary, never a closed enumeration** (**DL-55**); `voice_input` and
  `spoken_response_output` are further extensible members of this same set (**DL-90**, accepted)
- Which voice assistants are assigned to the Room
- **The Room's decorative presentation character (DL-100)** — persona (title/description) and
  configured TTS voice — a durable interaction-definition value distinct from, and never changed
  merely by, which device fulfils the Room's `voice_input`/`spoken_response_output` assignment above.
  See [../models/room-configuration.md](../models/room-configuration.md), *Room decorative
  presentation character (DL-100)*, and [../models/continuity.md](../models/continuity.md) for the
  full precedence rule against Continuity's Person-scoped preferences and requirements
- Room-scoped authority scoping inputs
- The exposed-term list used by Room Help

---

## The four states

Consumers must treat these as distinct.

| State | Meaning | Consequence |
|---|---|---|
| **Existence** | The thing is known to the Home | Nothing follows |
| **Participation** | It takes part in this Room's interaction model | It may be acted upon or contribute evidence |
| **Exposure** | Residents may address it here | It is discoverable and speakable |
| **Authority** | Someone may act upon it here, now | It may actually be operated |

Worked example — a Sonos Beam in the Living Space:

```
Exists:        yes (Foundation asset)
Participates:  yes, as a TV audio endpoint
Excluded from: the "Speakers" music vocabulary term
Exposed as:    not addressable as "Speakers"
Authority:     governed by Operational Trust
```

Saying "play music on the speakers" must not reach the Beam. It is excluded **deliberately**, and the
exclusion is configuration, not an error.

---

## The three participation states

Participation is not a boolean. Consumers must be able to distinguish these three states.

| State | Meaning | Consequence |
|---|---|---|
| `participating` | The asset or capability takes part in this Room's interaction model | It may be acted upon or contribute evidence |
| `not_selected` | The asset is known to the Home but was never considered for this Room | Nothing was intended; silence carries no meaning |
| `deliberately_excluded` | The asset was considered and intentionally kept out of this Room, or out of a specific vocabulary term | The exclusion is an intention and must be explainable |

**`not_selected` and `deliberately_excluded` must never be collapsed into a single "absent" state.**
Only `deliberately_excluded` supports the explanation *"the Beam is deliberately not part of Speakers
in this room."* A deliberate exclusion survives later re-configuration.

Whether a deliberate exclusion carries a structured reason, and whether that reason is
resident-visible, is **resolved as DL-103** — see [../models/room-configuration.md](../models/room-configuration.md), *Exclusion Metadata (DL-103)*: a required structured reason (`privacy` / `designated_use` / `other` with a mandatory note), rendered into household language, never surfaced to residents as a raw code or entity ID.

---

## The six questions Room Configuration answers

1. What do you call this?
2. What can I do here?
3. Which devices participate?
4. Which devices are intentionally excluded?
5. Which sensors contribute to composite room truth?
6. Which vocabulary terms are available in this room?

**These questions must be preserved. This discovery must not be lost.**

> Question 5 is preserved verbatim. In canonical terminology, "composite room truth" means a
> **Composite Fact** scoped to the Room — a fact Truth derives from more than one eligible contributing
> sensor. It is unrelated to the superseded term "Composite Room". See
> [../models/glossary.md](../models/glossary.md).

---

## What Room Configuration will never guarantee

- That a participating capability is currently available
- That a composite fact is currently true
- That a resident is permitted to use an exposed capability
- That an exposed term is currently actionable
- That decorative presentation character (**DL-100**) grants disclosure authority, selects a
  Reasoning Provider, or overrides a Person-borne accessibility/accommodation or
  required-comprehension-language requirement — those remain Operational Trust's and Continuity's
- That a deliberately-excluded asset is unavailable, broken, or native-hidden/disabled, or that a
  native `hidden`/`disabled`/absent-Assist-exposure flag alone proves household exclusion intent —
  exclusion and availability are never conflated (**DL-103**)

---

## What consumers may rely upon

| Consumer | May rely upon |
|---|---|
| Truth | The eligible-contributor set for each Room-scoped Composite Fact |
| Continuity | The configured experience endpoints for the Room |
| Operational Trust | Room-scoped definitions used in policy evaluation |
| Concierge | Room Context, the exposed capability set, the exposed-term list, resolved targets |

---

## What consumers must never assume

- That every device in a Home Assistant Area participates in the Room
- That participation implies exposure
- That exposure implies authority
- That a non-participating device is an oversight — read the participation state; `not_selected` and
  `deliberately_excluded` are different answers
- That Room Help may be generated from device inventory

> **Room Help must be derived from the configured exposed capability set and vocabulary, never
> generated from raw device inventory.**

One configuration, many surfaces: voice, panel, and Room Help all present the **same** exposed set.

---

## Voice assistant context

A voice assistant is a **participating capability assigned to a Room**. The Room is the context. The
device is not the context. **"Voice assistant" denotes any participating capability assigned a
`voice_input` Interaction Function Assignment, whether an integrated device or a dedicated
microphone/array; the device that captures an utterance is never assumed to be the device that
delivers the spoken response** — see
[../architecture/adr-decoupled-voice-interaction-capability-architecture.md](../architecture/adr-decoupled-voice-interaction-capability-architecture.md)
(**DL-90**, accepted).

Resolution order:

1. The voice assistant device that received the utterance
2. Its assigned Room
3. The Room's configuration
4. The Room's vocabulary
5. The Room's exposed capabilities
6. The Room's authority scope

Prohibited:

- Resolving context from the device name
- Resolving context from the Home Assistant Area alone when a Room definition exists
- Searching all devices in the home for a matching name
- Treating two voice assistants in the same Room as two different contexts

Two voice assistants assigned to the same Room resolve **identically**.

---

## Sensors and Composite Facts

| Step | Owner |
|---|---|
| Declare each Environmental Purpose's **Primary Authority** (**DL-62**) | **Room Configuration** |
| Calculate the Authority-Derived Fact, or a Formula-Derived Fact where the purpose is derived | **Truth** |
| Choose sensors at runtime | **Nobody — this is prohibited** |

Concierge must not select sensors at runtime. Truth must not invent the inventory. Room Configuration
must not calculate the fact. **Same-purpose sensor aggregation is not the ordinary path** — see
[../models/room-configuration.md](../models/room-configuration.md), *Primary Authority is required for
the ordinary path (DL-62)*.

---

## Uncertainty and unknown representation

| State | Meaning |
|---|---|
| `configured` | The Room is fully defined |
| `partially_configured` | The Room exists but a required element is missing |
| `unconfigured` | No Room definition exists for this context |
| `unresolved_context` | The originating device is not assigned to any Room |

---

## Failure and degradation behavior

| Condition | Behavior |
|---|---|
| Room Context cannot be resolved | Do not guess a Room. State that the context is unknown and ask. |
| **The originating interaction surface is not bound to a Room** | Report `unresolved_context`. **Never infer a Room from the surface, its name, or its owner.** Record the reason in the Decision Trace. Resolution is open decision **OD-73** |
| A participating asset is unavailable | Report the capability as unavailable; do not remove it from configuration |
| A vocabulary target no longer exists | Report a broken mapping as a configuration problem; do not substitute |
| A Merged Room's constituent is unavailable | The Room remains the Room; report reduced capability and coverage |
| Configuration is unreadable | Fail closed. Consumers treat the Room as `unconfigured`, not as unrestricted. |

---

## Privacy constraints

Exposure is a privacy decision. A capability exposed in a Room is addressable by anyone who can speak
in that Room, including guests and children. Sensitive capabilities must be protected by Operational
Trust authority, never by obscurity.

---

## Explainability contributions

Room Configuration supplies: the resolved Room Context and how it was resolved; the vocabulary
resolution and its mapping source; whether a target was excluded deliberately; the configured Primary
Authority (or Formula-Derived Fact inputs) behind any Truth Fact used.

A resident asking why something did not respond must be able to hear "the Beam is deliberately not
part of *Speakers* in this room."

---

## Configuration history

Room Configuration owns the history of its own records and guarantees the following.

| Guarantee | Statement |
|---|---|
| Every governed change is recorded | A Change Record names the subject, change type, prior state, new state, Effective Time, Recorded Time, actor or initiating process, reason where supplied, and prior and new version references |
| The three participation states survive in history | **participating**, **not selected**, and **deliberately excluded** are never collapsed in a historical record, exactly as they are never collapsed in the present |
| Past decisions reference past configuration | A decision references the exact configuration version applied at the time, so changing configuration today never rewrites yesterday's explanation |
| Runtime reads the present | Resolution uses the Current Projection. Historical records are never the runtime query path |
| Gaps are reported | Where a historical configuration version cannot be resolved, the limitation is reported; today's configuration is never presented as though it applied then |

**Consumers must never assume** that the configuration they read now is the configuration that applied
to a past decision.

See [../models/temporal-record.md](../models/temporal-record.md).

---

## Open decisions

| ID | Question |
|---|---|
| OD-01 | Home Assistant representation strategy for Room Configuration, including the persistence shape of Change Records, Snapshots, and Current Projections |
| OD-02 | **Closed — DL-43, DL-44, DL-45.** Participation and vocabulary definitions are located through a governed artifact reference; encoding remains capability-specific |
| OD-10 | Whether Floors are a first-class scope |
| OD-11 | **Closed — DL-67.** A Merged Room is a curated conversational interaction context; a Physical Room participates in at most one Merged Room at a time |
| OD-37 | Snapshot triggers, cadence, and scope per responsibility |
| OD-38 | Version identity, correlation, and causation identifier strategy |
| OD-73 | **Interaction-Surface Room Context Resolution** — Room Context for a surface not bound to a Room, and the `room_context.resolved_from` enumeration |
| OD-61 | **Closed — DL-60.** Room Environment Standard, native Area environmental slot proposal behaviour (mirroring OD-14), Primary Authority/Secondary/Composite/Excluded disambiguation (later narrowed to three states by **DL-62**), Merged Room environmental candidates, and derived purposes accepted |
| OD-17 | **Closed — DL-62.** Primary Authority is required and deterministic for every directly measured Environmental Purpose, identically for a Physical Room and a Merged Room; Composite Contributor is removed from the ordinary path; Formula-Derived Fact governance is accepted. Conflict resolution remains **OD-19** |
| OD-70 | **Closed — DL-68.** Merged Room native representation: **accepted, no native representation.** No proven consumer requires a projection; Area/Floor/Group/Scene are rejected as representations; Label is not adopted; Assist/Conversation must never receive one |
| OD-79 | **Closed — DL-100** (Issue #152). Room decorative presentation character (persona, configured TTS voice) is Room Configuration's, distinct from equipment/interaction-function relationships; precedence against Continuity's Person-scoped preferences and requirements is [../models/continuity.md](../models/continuity.md)'s own |
| OD-12 | **Closed — DL-103** (Issue #137). Deliberate exclusion is metadata explaining the Deliberately Excluded Participation value, never a fifth **DL-11** state; closed reason taxonomy `privacy` / `designated_use` / `other` (mandatory note); scope already inherent in the Participation record; temporality reuses **DL-56**'s "in effect until changed"; native Home Assistant flags never copied or treated as proof of household rationale |

## Related documents

- [../models/room-configuration.md](../models/room-configuration.md)
- [../models/room.md](../models/room.md)
- [../models/temporal-record.md](../models/temporal-record.md)
- [contextual-vocabulary-contract.md](contextual-vocabulary-contract.md)
- [truth-contract.md](truth-contract.md)
- [../architecture/adr-stable-endpoint-identity-and-network-boundary-independence.md](../architecture/adr-stable-endpoint-identity-and-network-boundary-independence.md) — stable endpoint identity and network-boundary independence (**DL-87**–**DL-89**, accepted at **#195**)
- [../architecture/adr-decoupled-voice-interaction-capability-architecture.md](../architecture/adr-decoupled-voice-interaction-capability-architecture.md) — decoupled `voice_input`/`spoken_response_output` Interaction Function Assignments (**DL-90**/**DL-91**, accepted)
