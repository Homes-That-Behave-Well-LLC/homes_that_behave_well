# ADR: Decoupled Voice Interaction Capability Architecture

> **Document status: Canonical ADR.**
> Status: **Accepted** 2026-10-26. Records **DL-90** and **DL-91** (issue **#198**, formal acceptance
> review PASS).
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Terminology: [../models/glossary.md](../models/glossary.md).

---

## Status

**Accepted 2026-10-26.** Formal acceptance review on Issue #198 recorded **PASS**, with no remediation
required.

Drafted by the 2026-10 Decoupled Voice Interaction Capability Architecture Review, prompted by the
Reference Home's intent to evaluate dedicated far-field microphone arrays as voice-input endpoints
while continuing to use the existing Concierge-managed Sonos room-audio path for spoken responses.
Consistent with this repository's established practice that a drafted decision is recorded first and
separately undergoes formal acceptance review before being treated as binding (see the DL-80–83/#188 and
DL-84–86/#191 precedents, and this ADR's own DL-90/DL-91/#198 precedent, in
[../governance/decision-ledger.md](../governance/decision-ledger.md)). **DL-87–89 (Issue #195, the
Stable Endpoint Identity ADR) remain separately pending and are unaffected by this acceptance.**

**This ADR does not redesign Home Assistant Assist, replace native device management, prescribe a
microphone vendor, prescribe Sonos, prescribe one STT or TTS engine, prescribe Ollama or one LLM,
implement unsupported automatic STT fallback, redesign Voice Identity, or duplicate Concierge audio
routing.** It authorizes no implementation. It creates **no new responsibility** — the seven
responsibilities recorded in **DL-01** are unchanged.

---

## Central decision

**HTBW models voice interaction as independently governed capture, recognition, interpretation, and
response-delivery capabilities. Foundation defines the configured room roles and relationships through
which those capabilities participate. Runtime truth, identity, continuity, operational authority, and
orchestration remain owned by their respective HTBW responsibilities. A physical device may fulfill one
or multiple interaction roles, and HTBW does not require the device that hears an interaction to
provide its response.**

**HTBW does not define a voice assistant. It defines how the Home listens, understands, decides, acts,
and responds. Those responsibilities may be fulfilled by one device or many, and Foundation governs how
their configured roles relate to the room.**

---

## Context

The Reference Home intends to evaluate dedicated far-field microphone arrays (candidate locations:
Tom's Office, Den, Primary Bedroom) as voice-input endpoints, continuing to use the existing
Concierge-managed Sonos room-audio path for spoken responses. **These are Reference Home implementation
choices and are not core HTBW architectural requirements** — no HTBW installation is required to use a
dedicated microphone array, Sonos, Speech-to-Phrase, Whisper, Ollama, local inference, ESPHome, or any
other specific technology named here as evidence.

### Existing authority reused, not reopened

- **Identity is the responsibility; voice is one evidence source** (**DL-05**, **DL-06**,
  [adr-identity-replaces-voice-identity-boundary.md](adr-identity-replaces-voice-identity-boundary.md)).
  Voice Identity is not a platform-service boundary and is not redesigned here.
- **Wyoming is the preferred voice-pipeline interoperability boundary, never a mandatory component**
  (**DL-50**, [adr-wyoming-compatible-voice-evidence-runtime.md](adr-wyoming-compatible-voice-evidence-runtime.md)).
  Which STT/TTS engine a household uses is explicitly out of scope there, and remains out of scope here.
- **No wake-word decision is opened** (`decision-ledger.md`, "No wake-word decision is opened.").
  Wake-word detection occurs before any HTBW responsibility engages and is a native satellite
  capability evaluated under **DL-30**/item 11 of **#146**. This ADR creates no wake-word decision.
- **Room Configuration already models "a voice assistant" as a participating capability assigned to a
  Room**, with a device-naming-free resolution order
  ([../contracts/room-configuration-contract.md](../contracts/room-configuration-contract.md), "Voice
  assistant context"; [../models/room-configuration.md](../models/room-configuration.md), same
  heading). This ADR extends that model to decoupled capture/response; it does not replace it, and an
  integrated voice assistant resolves exactly as it does today.
- **Concierge's Interaction Space / Execution Target / Response Delivery Space model already exists**
  ([../contracts/concierge-contract.md](../contracts/concierge-contract.md) §6) and already states that
  the Response Delivery Space is, by default, the Interaction Space's configured surfaces — a Room-level
  question. This ADR adds the device-level question within that Room (which configured endpoint, among
  possibly several, delivers the response) and does not alter Room-level resolution.
- **Room Configuration already states it will never guarantee that a participating capability is
  currently available** ([room-configuration-contract.md](../contracts/room-configuration-contract.md),
  "What Room Configuration will never guarantee"). Foundation does not establish runtime availability
  by configuring a role; this ADR restates this for voice roles specifically rather than introducing a
  new rule — no inconsistency was found requiring correction.
- **Identity's failure-and-degradation contract already states a dependency failure is reported
  `unavailable`, never degraded to a guess**
  ([identity-contract.md](../contracts/identity-contract.md), "Failure and degradation behavior").
  Reused unchanged for Voice Identity's specific case below.
- **DL-55** already confirms Room Configuration's experience-endpoint category set
  (`music`/`video`/`announcement`/`conversation`) is **extensible household vocabulary, never a closed
  enumeration**. `voice_input` and `spoken_response_output`, below, are new members of that same
  extensible set — not a new mechanism.

### A terminology note, not a contradiction

[../models/glossary.md](../models/glossary.md) already defines **Role** as a person-authority class
(resident, owner, child, guest, caretaker, service provider). The three-tier device model this ADR
needs — what a device can do, whether it participates, and what function it is assigned in a Room —
deliberately does **not** reuse the word "Role" for its third tier, to avoid colliding with that
existing, unrelated meaning. See **Interaction Function Assignment**, below.

---

## Decision 1 — Decoupled Voice Interaction Capability Model (DL-90)

### Capability, Participation, and Interaction Function Assignment

Three concepts, building directly on the glossary's existing **Capability** and **Participation**
entries, with one new, deliberately-not-"Role" third tier:

| Tier | Meaning | Existing basis |
|---|---|---|
| **Capability** | What a Home Assistant device/entity is technically able to provide (for example, a device with both a microphone and a speaker) | Glossary: *"Something that can be done or asked in a Room, expressed in household terms."* Unchanged. |
| **Participation** | Whether that capability has been explicitly selected to take part in a Room's interaction model | Glossary: *"The item has been explicitly selected to contribute to a Room capability, experience, composite fact, or interaction."* Unchanged. |
| **Interaction Function Assignment** *(new term)* | Which specific experience-endpoint function a participating capability is assigned to fulfill in a Room — `voice_input`, `spoken_response_output`, `music`, `video`, `announcement`, `conversation`, or another extensible term | New, narrow addition. **Not** the glossary's **Role** (a person-authority class) — a device is never assigned a Role. |

**A device possessing a capability does not imply an assigned Interaction Function.** A voice-assistant
device may possess both microphone and speaker capabilities but be configured (participation +
assignment) to fulfill only `voice_input` in a given Room, exactly as the existing Sonos Beam worked
example in [room-configuration-contract.md](../contracts/room-configuration-contract.md) already shows
one device participating in one experience endpoint while being deliberately excluded from another.

### Room voice input (`voice_input`)

Foundation's Room Configuration must be able to represent the configured device or devices used to hear
voice interactions associated with a Room, using a `voice_input` Interaction Function Assignment —
extending the existing "participating voice assistants" concept to also cover a capture-only
participating capability (for example, a dedicated microphone array) that is never assigned a response
role.

### Spoken response output (`spoken_response_output`)

A generic `audio_output` term is **not** used, because it would conflict with existing music/media
experience-endpoint semantics (`music`, and the existing "Participating music speakers" / media
capability already owned by Room Configuration). **`spoken_response_output`** is established as the
precise Interaction Function Assignment representing the configured destination for Concierge's own
spoken responses (acknowledgements, answers), consumed within the Room's existing Response Delivery
Space exactly as [concierge-contract.md](../contracts/concierge-contract.md) §6 already defines it — this
ADR adds no new Response Delivery Space mechanism, only the device-level assignment within one.

**This refines, before formal acceptance, the still-pending DL-88 draft** (Issue #195), which named
"audio_output or media-player endpoint" generically among four separately-placeable room-interaction
relationships. Since DL-88 is not yet accepted, this ADR's more precise `spoken_response_output` term is
adopted in its place for the voice-interaction case; DL-88's remaining three relationships
(`voice_input`, `interface`, physical remote) are unaffected. See the cross-reference edit recorded in
`decision-ledger.md` and
[adr-stable-endpoint-identity-and-network-boundary-independence.md](adr-stable-endpoint-identity-and-network-boundary-independence.md).

### Device flexibility

The model supports, without architecturally distinguishing "microphone mode" from "voice assistant
mode" — both are ordinary Interaction Function Assignments on a participating capability:

- an integrated voice assistant assigned both `voice_input` and `spoken_response_output`;
- an integrated voice assistant assigned `voice_input` only, with `spoken_response_output` assigned to
  a separate room speaker/media system;
- a dedicated microphone/array assigned `voice_input` only;
- a room speaker/media player assigned `spoken_response_output` only;
- a Room with `voice_input` but no `spoken_response_output`;
- a Room with `spoken_response_output` but no `voice_input`;
- a Room with neither.

### Cardinality

**No architectural assumption of exactly one `voice_input` or exactly one `spoken_response_output`
device per Room is made.** The model remains capable of representing multiple microphones, output
groups, or future redundancy, exactly as Room Configuration already represents multiple participating
music speakers without assuming exactly one. **This ADR does not design that mechanism** — it states
only that the model must not architecturally foreclose it. Mechanics are routed to the Foundation Room
Interaction Roles workstream identified below.

### Merged Rooms

Reconciled explicitly, without reopening **DL-67**/**DL-68** (a Physical Room participates in at most
one Merged Room at a time; a Merged Room has no native Home Assistant representation):

**A microphone detecting an interaction provides originating-space evidence. It does not automatically
establish the final Interaction Space or semantic context.** Concierge retains the responsibility it
already has — under the existing resolution order in
[room-configuration.md](../models/room-configuration.md) ("Voice assistant context") — for resolving
effective Room Context using Foundation configuration (the capturing device's assigned Room, and its
Merged Room membership where applicable) and other available Truth evidence. This is a restatement of
the existing rule for a decoupled-capture device, not a new rule.

### Voice input as evidence, not authority

Restating the framework's existing "attention to people and spaces, not microphones as contextual
authorities" principle (**DL-06**'s Identity Evidence / Identity Assertion / Contextual Person-Presence
Fact separation, and the runtime sequence's existing "occupancy precedes fusion; person presence follows
it" rule in [runtime-sequence.md](runtime-sequence.md)): **a microphone or satellite provides evidence
about interaction origin. It does not by itself establish person identity, authority, intent, presence
truth, or final Room context.** Those remain Identity's, Operational Trust's, Truth's, and Concierge's
respectively, exactly as today.

---

## Decision 2 — Performance-Aware, Provider-Independent Voice Processing Principle (DL-91)

### Operational Trust remains in the authority path

Voice interaction creates **no alternate execution path** around Operational Trust. Determining an
intent does not itself authorize execution — Operational Trust's existing authority, autonomy,
confirmation, privacy, and consent boundaries
([../contracts/operational-trust-contract.md](../contracts/operational-trust-contract.md)) are
unchanged and are not bypassed by a decoupled capture/response configuration.

### Voice Identity reconciliation

**Voice Identity remains independently owned** by the **Identity** responsibility (**DL-05**, **DL-06**)
and is not redesigned by this ADR. Selecting Speech-to-Phrase, Whisper, or another STT/recognition
mechanism **must not architecturally eliminate Voice Identity** merely because a different recognition
path was selected — Voice Identity's existing governed outputs (identity evidence, identity assertion,
confidence) and its existing degradation contract
([identity-contract.md](../contracts/identity-contract.md): a dependency failure is reported
`unavailable`, never degraded to a guess) apply unchanged regardless of which STT engine captured the
utterance. **This ADR does not solve the integration mechanism** between a chosen STT path and Voice
Identity's evidence intake; that is implementation mechanics, left to governed follow-on work (the
Performance-Aware Voice Processing workstream, below), consistent with **DL-50**'s own established
practice of leaving the STT engine choice unselected.

### Continuity preserved

Session/resume/transfer state remains **Continuity's** unchanged responsibility
([../contracts/continuity-contract.md](../contracts/continuity-contract.md)). **Performance
optimization must not route a context-dependent follow-up into a fast deterministic path if doing so
loses conversational context required to interpret the request correctly.** A fast path is available
only where the interaction is genuinely self-contained; where Continuity's existing session/context
state is required to interpret a follow-up correctly, the interaction is not eligible for the fast
path regardless of its surface latency advantage.

### Speech-processing provider independence

**No single speech recognition engine is designated the universal HTBW implementation.** Home
Assistant-native pipeline/provider modularity is preserved wherever possible, consistent with **DL-50**.
The architectural model allows, without mandating any of them:

- a fast, deterministic/closed-domain recognition path for ordinary Home control;
- an open-ended speech recognition path for conversational interaction;
- Concierge interpretation and context resolution;
- Home Intelligence, or another reasoning provider, only when genuinely required;
- TTS for generated spoken responses, delivered to the Room's configured `spoken_response_output`.

Speech-to-Phrase may be documented as a **current Reference Home evaluation candidate** for the fast
Home-control path, and Whisper (or another open-ended STT implementation) may be documented as a
**current candidate** for the conversational/Home-Intelligence path. **Neither becomes constitutional.**
**No automatic routing or fallback between recognition systems is asserted to exist** — this ADR states
only the architectural shape, not an implemented capability, consistent with the requirement not to
present unsupported Home Assistant capability as fact.

### The simplest authoritative path principle

**HTBW SHOULD use the simplest, lowest-latency authoritative capability capable of correctly satisfying
the interaction** — explicitly **not** "least expensive intelligence." Routine deterministic Home
control must not require an LLM or Home Intelligence merely because Home Intelligence exists.

```
simple deterministic Home control  -> fast authoritative control path
contextual interaction              -> Concierge
reasoning-required interaction      -> Home Intelligence or appropriate reasoning provider
spoken response, when needed        -> TTS -> configured spoken_response_output
```

**Home Intelligence is an escalation capability, not a universal Home-control path.** Its existence must
not increase latency for ordinary deterministic Home control — restating, for the voice-interaction
case, **DL-86**'s existing "Home Core failure independence" and **DL-41**'s "declared dependency, absence
is unavailable, never silently degraded" invariants, neither of which is reopened here.

### Existing Concierge audio behavior is reused, not duplicated

**Room speaker selection, Sonos selection, duck/pause behavior, TTS delivery, and resume behavior are
not reimplemented** inside a microphone endpoint, an STT provider, or any new voice-routing component.
This ADR's `spoken_response_output` Interaction Function Assignment is **consumed by**, and extends, the
existing governed Concierge response-delivery path (Response Delivery Space,
[concierge-contract.md](../contracts/concierge-contract.md) §6); it is not a second, parallel delivery
mechanism.

### Optional spoken response

A successful interaction does not require spoken confirmation. Where the physical result sufficiently
communicates success, Concierge may remain silent — consistent with Concierge's existing "must not
announce merely because it was permitted to act" hard prohibition (§5, prohibition #11, **P32**) and
with the HTBW objective of a calm, purposeful Home. This is a restatement, not a new prohibition.

### Graceful degradation

| Condition | Required behavior |
|---|---|
| Home Intelligence unavailable | Deterministic Home control is **not** prevented. Restates **DL-86**/**DL-41**, not reopened. |
| Voice Identity unavailable | Follows its **existing** degradation contract — report `unavailable`, continue deterministic command processing without speaker attribution ([identity-contract.md](../contracts/identity-contract.md)). Not a new contract. |
| `spoken_response_output` unavailable | Does not automatically prevent an otherwise-permitted Home action. The action proceeds; the response is reported unavailable, never silently substituted for a different Room's output without configuration. |
| A failed microphone (`voice_input` unavailable) | Does not affect unrelated interaction surfaces — dashboards, remotes, physical controls — consistent with **Capability Unavailable**'s existing "never emulated, approximated, or silently reduced" rule ([glossary.md](../models/glossary.md)). |

**No fallback mechanism the platform cannot currently support is invented** by this table; each row
restates an existing degradation rule for the voice-interaction case.

### Privacy

Reconciling microphone participation with existing privacy, consent, Operational Trust, and Voice
Identity requirements, the following stages are explicitly distinguished (restating, not replacing, the
existing stage-relevant rules already recorded in
[privacy.md](privacy.md) and the Voice Identity privacy/retention documents):

| Stage | Governing rule (existing, restated) |
|---|---|
| Listening availability | A `voice_input` Interaction Function Assignment configures that a Room *may* capture; it is not itself capture. |
| Wake-word processing | Occurs before any HTBW responsibility engages (`decision-ledger.md`, "No wake-word decision is opened"); HTBW governs nothing here. |
| Active audio capture | Begins only after wake-word (or equivalent) activation; governed by the same participation/consent model as any other evidence source. |
| Speech recognition | Produces a transcript/intent; **speaker evidence never gates transcription and never appears in transcript text** (**DL-50**, D6). |
| Identity processing | Identity's existing evidence → assertion pipeline (**DL-05**, **DL-06**); optional, consent-gated, degrades to `unavailable` per [identity-contract.md](../contracts/identity-contract.md). |
| Storage/retention | **Raw voice audio must not become durable household data simply because an input device participates in voice interaction.** Raw samples default to zero retention beyond the processing window, per the existing rule in [privacy.md](privacy.md) ("Raw voice-sample retention") and the Voice Identity enrollment privacy documents. This ADR extends that existing default to ordinary (non-enrollment) voice-interaction capture; it creates no new retention floor or ceiling. |

### Performance

Performance is a first-class architectural and acceptance requirement. **No arbitrary SLA threshold is
established here** — none exists in governing repository material to draw from. The following metrics
are defined as **measurable concepts** for future implementation to instrument, not as accepted
thresholds:

- wake word → listening acknowledgment;
- end of utterance → recognition result;
- recognition result → action request;
- action request → observable Home state change;
- end of utterance → first audible response;
- complete interaction → useful outcome;
- wake-word success/missed-activation rate;
- recognition success rate;
- command success rate;
- escalation/fallback behavior (where it exists).

**Component benchmarks (model size, tokens/second) are not substitutes for end-to-end household
experience** and are not used as acceptance evidence by themselves.

---

## Follow-on implementation workstreams (identified, not created, not implemented)

Consistent with the governing execution prompt, this ADR identifies — and does **not** open issues for,
or begin implementation of — at least two separate workstreams:

**A. Foundation Room Interaction Roles** — device capability vs. assigned Interaction Function Assignment
mechanics; `voice_input`; `spoken_response_output`; integrated-device single/dual-role configuration;
Merged Room handling mechanics; Concierge's consumption mechanics; migration/backward compatibility for
existing "participating voice assistant" configurations.

**B. Performance-Aware Voice Processing** — the fast deterministic Home-control path; general/open-ended
recognition; Concierge routing; Home Intelligence escalation mechanics; Voice Identity integration
mechanics; continuity-preservation mechanics; the TTS response path; latency instrumentation;
degradation mechanics; routing/fallback investigation.

---

## Relationship to existing decisions, contracts, and reviews

| Item | Relationship to this ADR |
|---|---|
| **DL-05**, **DL-06** (Identity responsibility, voice as evidence) | **Reused, not reopened.** Voice Identity is not redesigned. |
| **DL-50** (Wyoming-compatible voice evidence runtime) | **Reused, not reopened.** STT/TTS engine selection remains out of scope. |
| No-wake-word finding (`decision-ledger.md`) | **Reused, not reopened.** No wake-word decision is created here either. |
| Room Configuration's existing "voice assistant context" ([room-configuration-contract.md](../contracts/room-configuration-contract.md), [room-configuration.md](../models/room-configuration.md)) | **Extended, not replaced.** An integrated voice assistant resolves identically to today. |
| Concierge's Interaction Space / Execution Target / Response Delivery Space ([concierge-contract.md](../contracts/concierge-contract.md) §6) | **Reused, not reopened.** This ADR adds a device-level question inside an existing Room-level mechanism. |
| **DL-67**, **DL-68** (Merged Room) | **Reused, not reopened.** Microphone evidence does not establish Interaction Space. |
| **DL-86**, **DL-41** (Home Intelligence optionality, declared-dependency unavailability) | **Reused, not reopened.** Home Intelligence remains escalation-only here too. |
| **DL-88** (pending, #195 — room-interaction-capability relationships) | **Refined before acceptance**, not reopened after it. The generic "audio_output" bullet is replaced by this ADR's precise `spoken_response_output` term for the voice-interaction case; DL-88's other three relationships are unaffected. |
| **#146** (Home Assistant native capability verification backlog) | **Unaffected.** No new item added by this ADR. |
| **#198** (this governance review) | Tracks this ADR's formal acceptance. |
| [foundation-room-interaction-roles-specification.md](foundation-room-interaction-roles-specification.md) (#199, accepted) | Operationalizes the Workstream A follow-on identified below. |
| [performance-aware-voice-processing-specification.md](performance-aware-voice-processing-specification.md) (#200) | Operationalizes the Workstream B follow-on identified below. |

---

## Explicit non-goals

- Does not redesign Home Assistant Assist or replace native device management.
- Does not prescribe a microphone vendor, Sonos, one STT engine, one TTS engine, Ollama, or one LLM.
- Does not implement unsupported automatic STT fallback or assert one already exists.
- Does not redesign Voice Identity or duplicate Concierge audio routing.
- Does not make the Reference Home's configuration (dedicated microphone arrays in specific rooms,
  Sonos, Speech-to-Phrase, Whisper, local inference) mandatory for any HTBW installation.
- Does not create a new responsibility, a new Decision Trace field, or a new authorization mechanism.
- Does not assume exactly one `voice_input` or `spoken_response_output` device per Room.
- **DL-05/DL-06, DL-50, DL-67/DL-68, DL-86/DL-41, the no-wake-word finding, Room Configuration's voice
  assistant model, and Concierge's Response Delivery Space are each referenced above and are each
  unaffected** — none is narrowed, resolved, or reopened by this ADR.
- **DL-90 and DL-91 are accepted, binding decisions (Issue #198, PASS, 2026-10-26), equivalent in
  standing to DL-01–DL-89.** They authorize no implementation; see the Foundation Room Interaction
  Roles and Performance-Aware Voice Processing workstreams above for implementation-readiness work.

---

## Related documents

- [adr-identity-replaces-voice-identity-boundary.md](adr-identity-replaces-voice-identity-boundary.md)
- [adr-wyoming-compatible-voice-evidence-runtime.md](adr-wyoming-compatible-voice-evidence-runtime.md)
- [adr-stable-endpoint-identity-and-network-boundary-independence.md](adr-stable-endpoint-identity-and-network-boundary-independence.md)
- [runtime-sequence.md](runtime-sequence.md)
- [failure-and-degradation.md](failure-and-degradation.md)
- [privacy.md](privacy.md)
- [../contracts/concierge-contract.md](../contracts/concierge-contract.md)
- [../contracts/identity-contract.md](../contracts/identity-contract.md)
- [../contracts/operational-trust-contract.md](../contracts/operational-trust-contract.md)
- [../contracts/continuity-contract.md](../contracts/continuity-contract.md)
- [../contracts/room-configuration-contract.md](../contracts/room-configuration-contract.md)
- [../models/room-configuration.md](../models/room-configuration.md)
- [../models/glossary.md](../models/glossary.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
