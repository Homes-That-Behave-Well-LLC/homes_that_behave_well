# Performance-Aware Voice Processing — Implementation-Ready Specification

> **Document status: Active — subordinate to the HTBW canonical architecture.**
> Canonical authority: [adr-decoupled-voice-interaction-capability-architecture.md](adr-decoupled-voice-interaction-capability-architecture.md)
> (**DL-90**, **DL-91**, accepted), [foundation-room-interaction-roles-specification.md](foundation-room-interaction-roles-specification.md)
> (accepted), [framework.md](framework.md), and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> **Specification only. Authorizes no executable implementation.** Tracked at Issue #200. **Status:
> AWAITING OWNER ACCEPTANCE REVIEW — not yet accepted.**

---

## 1. Status and scope

This document operationalizes the accepted **DL-91** (Performance-Aware, Provider-Independent Voice
Processing Principle) into an implementation-ready specification for the **Performance-Aware Voice
Processing** workstream, remaining consistent with **DL-90** and the accepted
[Foundation Room Interaction Roles specification](foundation-room-interaction-roles-specification.md).
It does not reopen, narrow, or redecide DL-90 or DL-91, and it does not redesign the Foundation Room
Interaction Roles specification.

**This document authorizes no executable implementation.** The same pre-implementation grounding
recorded in the Foundation Room Interaction Roles specification applies unchanged: no HTBW Core
implementation repository exists, and [greenfield-mandate.md](greenfield-mandate.md) prohibits using
`concierge`, `voice_identity`, or `asset_intelligence` as a substitute implementation surface. **No
runtime code, STT/TTS installation, routing logic, or Concierge change is introduced by this document.**

**This issue is not closed by the implementing agent.** Per governing process, this specification
proposes a result and leaves Issue #200 open, status **AWAITING OWNER ACCEPTANCE REVIEW**, for the
repository owner's separate, formal acceptance review.

---

## 2. Governing decisions

| Decision | Status | What it supplies here |
|---|---|---|
| **DL-91** | Accepted | The simplest-authoritative-path principle; Home Intelligence as escalation-only; provider independence; Voice Identity/Continuity/Concierge-audio-reuse preservation; graceful degradation; privacy-stage distinctions; non-SLA performance-metrics vocabulary. Primary governing decision for this specification. |
| **DL-90** | Accepted | Capability/Participation/Interaction Function Assignment triad; `voice_input`/`spoken_response_output` as independent Room Configuration roles. |
| Foundation Room Interaction Roles specification | Accepted (Issue #199, owner PASS) | The atomic `RoomInteractionFunctionAssignment` model this specification's processing paths must consume, unchanged. |
| **DL-05**, **DL-06** | Accepted | Identity is the responsibility; voice is one evidence source; Identity Evidence/Identity Assertion/Contextual Person-Presence Fact separation. |
| **DL-50** | Accepted | Wyoming-compatible voice evidence runtime; Wyoming as the preferred, non-mandatory voice-pipeline boundary; STT/TTS engine selection explicitly out of scope there and here. |
| **DL-67**, **DL-68** | Accepted | Merged Room reconciliation — restated, not reopened. |
| **DL-86** | **Pending** (Issue #191, not yet accepted) | Home Intelligence's own product/deployment boundary. Cited only as forward-compatible, non-binding context; this specification does not depend on DL-86's acceptance and does not reopen it. |
| No-wake-word finding | Accepted (`decision-ledger.md`) | Wake-word detection remains a native satellite capability outside HTBW responsibility; restated, not reopened. |

---

## 3. Responsibility boundaries

Restating this specification's governing distinction (DL-91, Decoupled Voice Interaction Capability
Architecture ADR) — these are **processing responsibilities, not a generic "AI pipeline"**:

| Responsibility | What it does | Owner (existing, unchanged) |
|---|---|---|
| **Capture** | Microphone/microphone array, acoustic front end, wake-word evidence where applicable, voice stream | Native Home Assistant (`wake_word` stage, `assist_satellite` device); Foundation's `voice_input` Interaction Function Assignment names which configured capability captures |
| **Recognition** | Speech audio → recognized text/phrase/intent evidence | Native Home Assistant `stt` stage/entity — provider-independent |
| **Interpretation** | Deterministic Home Assistant intent processing; Concierge contextual interpretation; Home Intelligence/reasoning only where actually required | Native `conversation`/`intent` stage for deterministic matching; **Concierge** for contextual interpretation; **Home Intelligence** (escalation-only, DL-91) for reasoning-required cases |
| **Authorization/decision** | Permissions, consent, confirmation, autonomy, action authority | **Operational Trust** — unchanged. Recognition and interpretation never themselves grant execution authority |
| **Execution** | The governed action | Normal Home Assistant/HTBW governed action path — unchanged |
| **Response generation** | Content of a response, where one is needed | Concierge (what to say); Home Intelligence may contribute content where escalated, never authority |
| **Response delivery** | TTS where applicable, delivery to the configured `spoken_response_output`, existing Concierge delivery behavior | **Concierge**'s existing, reused response-delivery path (Response Delivery Space, [concierge-contract.md](../contracts/concierge-contract.md) §6) |

---

## 4. Voice processing model / stages

```
capture -> recognition -> interpretation -> authorization/decision -> execution -> response generation -> response delivery
```

Mapped to the native Home Assistant Assist pipeline stages (verified against current official Home
Assistant developer documentation, §20): `wake_word` → `stt` → `intent` (conversation agent) → `tts`.
**Capture** corresponds to `wake_word`/audio streaming; **Recognition** to `stt`; **Interpretation**,
**Authorization/decision**, and **Execution** occur within and around the `intent`/conversation stage
(the native conversation agent for deterministic matching, Concierge/Operational Trust/Home Assistant
action execution for everything requiring HTBW governance); **Response generation** and **Response
delivery** correspond to the content decision and the `tts` stage respectively, consumed through
Concierge's existing delivery path rather than the native pipeline's default device-local playback
where an HTBW-configured `spoken_response_output` differs from the capturing device (per the accepted
Foundation Room Interaction Roles specification).

**These seven responsibilities are never collapsed into a generic "AI pipeline."** Each remains owned
by its existing responsibility; this specification only states how an interaction moves between them.

---

## 5. Processing classes

Implementation-neutral classes, not a closed enumeration of products or engines:

| Class | Description | Architectural objective |
|---|---|---|
| **A. Deterministic Home control** | Ordinary commands resolvable through established Home Assistant/HTBW intent and capability mechanisms without general-purpose reasoning | `capture → fast authoritative recognition → deterministic intent → Operational Trust where applicable → Home action → optional response`. **An LLM or Home Intelligence must not be required merely because Home Intelligence exists.** |
| **B. Contextual Home interaction** | Recognized language alone is insufficient; Concierge context (room, person, household semantics, ambiguous references) is required | Concierge remains the contextual orchestration layer. **Not assumed to require an LLM.** |
| **C. Open-ended/conversational interaction** | Requires unrestricted language recognition or conversational interpretation | Permits open-ended STT and an appropriate conversation provider. **No specific STT engine is made constitutional.** |
| **D. Reasoning-required/Home Intelligence interaction** | Requires reasoning, synthesis, household knowledge, explanation, or other capability explicitly governed to Home Intelligence | Home Intelligence invoked only where appropriate; **never a prerequisite for deterministic Home control.** |
| **E. Context-dependent follow-up** | Interpretation depends on existing conversation/session context | Continuity is preserved (§10); a follow-up is never routed to a nominally faster path if doing so would discard context required to interpret it correctly. |

A single interaction may begin in one class and escalate to another (for example, A → D when a
deterministic match fails and reasoning is warranted); escalation mechanics are a routing question,
addressed in §8, not decided by this classification alone.

---

## 6. Simplest-authoritative-path principle (DL-91, restated)

> **"HTBW SHOULD use the simplest, lowest-latency authoritative capability capable of correctly
> satisfying the interaction."** — explicitly **not** "least expensive intelligence."

**Performance-aware does not mean "always fastest."** Correctness, Authority, Context, Privacy,
Continuity, and Safety take precedence over choosing a nominally faster processing path. **A fast but
contextually incorrect path is not acceptable performance.** Performance optimization means selecting
the simplest authoritative path capable of correctly satisfying the interaction — never a path that
produces a wrong or unauthorized outcome merely because it is faster.

---

## 7. Provider independence

**No engine, protocol, or vendor named in this section becomes a mandatory HTBW dependency.**
Distinguishing architectural requirement from current reference-implementation candidates:

| Processing role | Architectural requirement | Current reference-implementation candidate (not constitutional) |
|---|---|---|
| Fast, closed-domain recognition (Class A) | A provider-independent, Home-Assistant-native `stt` entity capable of fast, closed-domain recognition | Speech-to-Phrase — verified as closed-domain, local, generated from the household's own Home Assistant entities, with sub-second response on modest hardware (§20) |
| Open-ended recognition (Class C) | A provider-independent, Home-Assistant-native `stt` entity capable of open-ended recognition | Whisper (or another open-ended STT implementation) |
| Local speech synthesis | A provider-independent, Home-Assistant-native `tts` entity | Piper (or another local TTS provider) |
| Reasoning/Home Intelligence (Class D) | A **Reasoning Provider** (glossary; **OD-67**, open) consulted only where genuinely required; owns no facts, no authority | Ollama or another local inference provider (not selected, not prescribed, not installed by this specification) |

This restates, for the full processing model, **DL-50**'s existing rule that Wyoming is "a protocol and
never an HTBW component," and **DL-91**'s existing rule that "neither becomes constitutional."

---

## 8. Routing/escalation contract

### The routing problem, stated explicitly

**This specification does not pretend that HTBW already knows how to classify an utterance before
sufficient recognition has occurred.** The architectural question is: *how can the Home choose an
appropriate processing path without requiring the very expensive processing step the fast path exists
to avoid?*

**This specification does not invent an answer.** It documents the evidence available at each point and
what remains an open implementation question (§24).

### Evidence available before recognition

- The Room's configured `voice_input` assignment (Foundation, accepted Foundation Room Interaction
  Roles specification) — which capability is capturing.
- Room Context, where resolvable (Foundation/Room Configuration, existing).
- Wake-word identity, where the platform's wake-word engine is configurable per satellite (native
  Home Assistant capability, verified §20) — evidence only; **no wake-word decision is created or
  reopened** (`decision-ledger.md`).
- Whatever pipeline is currently selected for the capturing device, via Home Assistant's native
  `pipeline_entity_id` select-entity mechanism (verified §20) — a **configuration-time** or
  **automation-time** choice of which `stt`/`conversation`/`tts` providers a pipeline uses, **not** a
  per-utterance, content-based decision.

### Evidence available during recognition

- Partial/streaming recognition output, where a provider supplies it (provider-specific; not
  guaranteed by the Home Assistant `stt` entity abstraction in general).
- Provider-reported confidence or score, **where the provider supplies one** — never assumed to exist
  universally (restating **DL-50**'s "a provider value is meaningful only within its own provider").

### Evidence available after recognition

- The recognized text (native `stt` output).
- The conversation agent's response, including its `response_type` (`action_done`, `query_answer`, or
  `error`) and, for an error, its `data.code` (for example `no_intent_match`) — **verified, current,
  native Home Assistant evidence (§20) that a deterministic match did or did not occur.** This is the
  single most useful piece of native, already-existing evidence for a future routing implementation:
  whether the built-in/deterministic path succeeded is already an observable, documented outcome.
- `conversation_id`, continuing a native conversation across turns (§10).
- Identity evidence, where Voice Identity's evidence pipeline is engaged (§9).

### What Home Assistant-native pipeline-selection capabilities actually exist

Verified against current official Home Assistant developer documentation (§20):

- A household may configure **multiple pipelines**, each with its own `wake_word`/`stt`/`conversation`/
  `tts` provider combination.
- An `assist_satellite` entity may declare a `pipeline_entity_id` (a `select` entity) that **picks which
  configured pipeline that device uses**; absent that, "the preferred pipeline is used" (one global
  default).
- A client may also specify `pipeline` directly when invoking `assist_pipeline/run` over the WebSocket
  API.

**This is a configuration-time or explicit-invocation-time selection mechanism, not a native,
automatic, per-utterance, content-based routing mechanism.** Nothing in current official documentation
describes Home Assistant automatically selecting or switching pipelines based on recognized content,
confidence, or interaction class.

### What remains a routing/fallback implementation question

- Whether, and how, a future implementation changes which pipeline a device uses in response to
  observed evidence (for example, a deterministic `no_intent_match` outcome) — **not decided here**
  (§24).
- Whether a failed closed-domain recognition can safely trigger a second, open-ended recognition
  attempt on the same utterance — **not decided here** (§24); this would require re-processing audio
  already captured, which is a latency and privacy-relevant design question of its own.
- **"Speech-to-Phrase → automatic fallback to Whisper" is explicitly NOT asserted as a supported native
  capability.** No authoritative current Home Assistant evidence found during this specification's
  research (§20) describes such an automatic fallback. Any third-party or experimental mechanism
  achieving something like it is research evidence only, never an HTBW requirement.

### Minimal conceptual evidence shape (not a new store)

A future routing implementation needs the evidence below. **Nearly all of it already exists in a named,
existing contract; this specification creates no new store** — it only identifies where each piece of
evidence already lives, and names the one genuinely new element:

| Evidence | Existing source |
|---|---|
| Interaction origin (which Room, which `voice_input` capability) | Foundation / accepted Foundation Room Interaction Roles specification |
| Recognized result | Native Home Assistant `stt`/conversation API response |
| Recognition confidence, where provided | The provider itself (DL-50; not universal) |
| Conversation/session context | Continuity (existing) + native `conversation_id` |
| Room/context evidence | Truth (existing authoritative facts) |
| Identity evidence, where available | Identity (DL-05/DL-06, existing) |
| Whether a deterministic intent resolved | Native conversation API `response_type`/`data.code` (existing, verified §20) |
| Whether context is required | Concierge's own existing contextual-orchestration judgment |
| Whether reasoning is required | Concierge's own existing judgment, informed by **OD-67**'s (open) Reasoning Provider boundary |
| Operational Trust outcome | Operational Trust (existing) |
| **Which processing path was selected, and why (including any escalation)** | **Genuinely new**: recorded as an ordinary entry in the existing **Decision Trace** mechanism ([decision-trace.md](../models/decision-trace.md)) — no new record type, store, or telemetry subsystem is created (§18) |

**No priority, preferred-provider, automatic-fallback, or runtime orchestration behavior is specified,
implied, or required by this evidence shape.** It states what evidence exists and where; a future,
separately authorized implementation decides how to act on it.

---

## 9. Voice Identity interaction

**The choice of recognition provider must not architecturally eliminate Identity/Voice Identity.**
Existing ownership for speaker attribution, confidence, identity evidence, no-match behavior, and
privacy is unchanged (**DL-05**, **DL-06**; [identity-contract.md](../contracts/identity-contract.md)).

**What Voice Identity requires, and at what stage (from accepted architecture, DL-50):** a voice
evidence provider operates on the **audio stream itself**, at the capture/recognition stage, emitting an
unbound Voice Evidence Record (ordered candidates, provider-reported scores, separation data, quality
metadata, encoder identity) — **in parallel with recognition, never gated by it.** "Speaker evidence is
enrichment and never a gate": a non-match, unknown speaker, unavailable host, or incompatible gallery
never suppresses the transcript, and identity never travels inside transcript content (DL-50).

**This specification does not implement a new interception mechanism and does not assume every
recognition path routes through a specific STT proxy.** Research evidence (§20) indicates Speech-to-Phrase
and Whisper are each reachable as Home-Assistant-native `stt` entities through the same accepted Wyoming
audio/voice-service boundary (**DL-50**) HTBW already treats as the preferred interoperability seam —
suggesting, as **research evidence, not a proven guarantee**, that a Voice Identity evidence provider
tapping the Wyoming-level audio stream is not inherently gated by which `stt` entity a pipeline selects,
**provided the implementation taps audio at that boundary rather than after a specific STT engine's own
output.** This is recorded as an open implementation question (§24), not asserted as fact.

**If a future processing path cannot provide Voice Identity the evidence it requires, that is an
implementation constraint to be documented, not a reason to bypass or redesign Identity.**

---

## 10. Continuity behavior

**Continuity remains authoritative** for applicable conversation/session context
([continuity-contract.md](../contracts/continuity-contract.md)) — unchanged.

- **Follow-up utterances and conversational state**: Home Assistant's native `conversation_id` (verified
  §20) already provides a continuation mechanism at the platform level; this specification requires that
  whatever processing path handles a follow-up either honors that continuation or defers to Continuity's
  existing session/resume model — it does not invent a second continuity mechanism.
- **Escalation from deterministic to contextual/reasoning interaction**: escalating processing class
  (§5) must carry forward whatever conversational context Continuity or the native conversation turn
  already established; escalation is never a reason to discard context.
- **The fast path must not accidentally make the Home contextually less capable.** A follow-up whose
  correct interpretation depends on prior conversational context (Class E, §5) is **not eligible** for a
  faster path that would lose that context, regardless of that path's latency advantage — restating
  **DL-91** unchanged.

---

## 11. Operational Trust boundary

**All action paths preserve Operational Trust** ([operational-trust-contract.md](../contracts/operational-trust-contract.md))
— unchanged. Explicitly, for every processing class in §5:

> **Recognition ≠ authorization. Interpretation ≠ authorization. A Home Intelligence recommendation ≠
> authorization.**

A faster deterministic path is never a shortcut around permissions, consent, authority, confirmation,
autonomy, or privacy. This restates Concierge's existing hard prohibition ("must not grant itself
authority") and Operational Trust's existing authority model; it creates no new rule and no new
authorization path.

---

## 12. Truth boundary

**Truth remains authoritative for current operational facts** ([truth-contract.md](../contracts/truth-contract.md),
"Truth is a first-class authoritative fact engine") — unchanged. No processing provider independently
becomes an authority for current Home state. For example, a Home-Intelligence-generated assertion about
device state must never replace or compete with Truth's authoritative current-state determination; it
is, at most, Reasoning Provider output — which "owns nothing" (glossary) and never silently becomes a
Fact.

---

## 13. Concierge boundary

Concierge remains the contextual orchestrator ([concierge-contract.md](../contracts/concierge-contract.md))
— unchanged. This specification does **not** turn Concierge into a speech-recognition engine, an STT
multiplexer, a TTS engine, a microphone manager, a Home Intelligence runtime, or a hard-coded device
router. It defines only the processing/orchestration contract needed for Concierge to participate: which
processing class an interaction falls into (§5), and that Concierge's existing contextual-interpretation
role (Class B) and its existing orchestration sequence
([runtime-sequence.md](runtime-sequence.md)) are unchanged by the existence of faster or escalated
paths.

**Existing Concierge spoken-response delivery is reused, not duplicated**: room speaker selection,
Sonos selection/mapping, pause, duck, TTS delivery orchestration, and resume behavior are not
reimplemented by any processing path, STT provider, or routing mechanism this specification describes.

---

## 14. Response / TTS behavior

**A successful interaction does not require speech.** Where observable Home behavior is adequate
confirmation (lights visibly turn off, shades visibly move, media stops), Concierge may remain silent —
restating Concierge's existing "must not announce merely because permitted to act" prohibition (**P32**),
not a new rule. TTS is never forced into every deterministic path.

Where speech is appropriate:

```
response content -> TTS -> configured spoken_response_output -> existing Concierge delivery behavior
```

This is the same path the accepted Foundation Room Interaction Roles specification already defines
(§8 there); this specification adds no new delivery mechanism.

---

## 15. Privacy

Distinguishing processing stages explicitly, restating existing rules rather than creating new ones:

| Stage | Governing rule (existing, restated) |
|---|---|
| Listening availability | A configured `voice_input` Interaction Function Assignment means a Room *may* capture; it is not itself capture (Foundation Room Interaction Roles specification). |
| Wake-word processing | Occurs before any HTBW responsibility engages (`decision-ledger.md`, "No wake-word decision is opened"). |
| Active voice capture | Begins only after wake-word (or equivalent) activation; governed by the same participation/consent model as any other evidence source ([privacy.md](privacy.md)). |
| Recognition | Produces a transcript/intent; speaker evidence never gates it and never appears in transcript text (**DL-50**, D6). |
| Speaker attribution | Identity's existing evidence → assertion pipeline (**DL-05**, **DL-06**); optional, consent-gated, degrades to `unavailable` ([identity-contract.md](../contracts/identity-contract.md)). |
| Interpretation | Concierge's existing contextual-interpretation behavior; no new data collection. |
| Reasoning (Home Intelligence, where engaged) | A Reasoning Provider "owns nothing" (glossary); no new persistent store is created by this specification. |
| Response generation | No new data collection. |
| Retention | **Raw audio must not become durable household data merely because it entered a processing pipeline.** Raw samples default to zero retention beyond the processing window, per the existing rule in [privacy.md](privacy.md) ("Raw voice-sample retention") and the Voice Identity enrollment privacy documents — extended, not newly created, to every processing class in this specification. **No new retention behavior is introduced.** |

**Local-first is preserved where accepted architecture requires it** ([voice-identity-trust-and-data-residency-policy.md](voice-identity-trust-and-data-residency-policy.md)); this specification does not redefine "local-first" to mean "local-only." Where local and remote providers may both exist for a given processing role (§7), provider selection and its trust/privacy implications are a future, separately governed configuration choice — **this specification does not invent a selection policy that has not been accepted.**

---

## 16. Graceful degradation

| Condition | Required behavior |
|---|---|
| Home Intelligence unavailable | Does not unnecessarily prevent deterministic Home control (Class A). Restates **DL-86**/**DL-41**'s existing "declared dependency, absence is unavailable" invariant, not reopened. |
| Open-ended STT unavailable | Does not unnecessarily prevent supported deterministic control (Class A) — only Class C/D interactions depending on it are affected. |
| Voice Identity unavailable | Follows its **existing** degradation contract — report `unavailable`, continue deterministic command processing without speaker attribution ([identity-contract.md](../contracts/identity-contract.md)). Not a new contract. |
| `spoken_response_output` unavailable | Does not necessarily prevent an otherwise valid Home action — restates the accepted Foundation Room Interaction Roles specification §12, not reopened. |
| `voice_input` unavailable | Does not impair dashboards, remotes, physical controls, automations, or unrelated interaction surfaces — restates **Capability Unavailable**'s existing "never silently reduced" rule (glossary). |
| An optional reasoning provider fails | Must not falsely report successful execution — restates Concierge's existing "must not act silently when it cannot explain the action" and "must not infer `Presented` from `Delivered`" prohibitions. |

**No unsupported automatic fallback behavior is invented by this table.**

---

## 17. Performance metrics

Performance is a first-class acceptance concern. **No arbitrary SLA threshold is established here** —
none exists in governing repository material to draw from, consistent with **DL-91**. The following are
defined as **measurable concepts** for future implementation to instrument, not accepted thresholds:

| Phase | Metric |
|---|---|
| Voice acquisition | Wake-word/activation to listening acknowledgment; missed activation rate; false activation rate, where observable |
| Recognition | End of utterance to recognition result; recognition success/correctness |
| Interpretation | Recognition result to intent/interpretation result |
| Authorization | Interpretation to authorization/decision result, where applicable |
| Execution | Authorized action request to observable Home state change |
| Response | End of utterance to first audible response, where a spoken response is appropriate; time to useful outcome |
| Intelligence (where Home Intelligence participates) | Inference start latency; time to first useful generated response; generation performance, where meaningful; total end-to-end interaction latency |

**Component benchmarks (model size, tokens/second) are not substitutes for end-to-end household
experience and must not satisfy performance acceptance by themselves.**

### Reference Home performance context

The Reference Home's performance concern is real household responsiveness: current experience
indicates poor voice-assistant responsiveness materially reduces willingness to use voice. A future
implementation should permit controlled comparison of processing paths using the same room,
microphone/input, Home Assistant instance, requested action, and output configuration where possible.
**Reference Home technologies (dedicated microphone arrays, room Sonos output) are evidence, not core
dependencies** — restating the same Reference-Home-independence principle already established
throughout this voice-interaction work.

---

## 18. Observability

A future implementation should be able to distinguish: which processing class/path handled the
interaction; whether escalation occurred; which major stages contributed latency; whether the
interaction succeeded; whether a response was intentionally silent; and whether degradation occurred.

**No new telemetry subsystem is created.** This information is recorded as event/timing metadata
consistent with the existing Decision Trace mechanism ([decision-trace.md](../models/decision-trace.md)),
which already carries machine-readable reason codes, source lineage, confidence, and timestamps
(restated from the historical Coordinator V2 evidence's explainability requirements, carried forward as
architectural evidence, not as a second mechanism). **Raw voice content is never required for
observability.**

---

## 19. Home Intelligence escalation

Home Intelligence is established as an **escalation target** for Class D interactions (§5) —
**restating, not deciding, DL-91**. This specification does not decide the Home Intelligence
implementation, does not prescribe Ollama, does not prescribe a model, and does not prescribe hardware.
**DL-86** (Home Intelligence's own product/deployment boundary) remains separately pending at Issue
#191; this specification is consistent with it where it already exists as evidence, and does not depend
on its acceptance.

**Disambiguation**: "escalation" here means routing an interaction to a higher-capability processing
class (§5). It is a distinct concept from Stewardship's existing **Escalation Ladder** (**OD-22**,
obligation/Communication urgency escalation) — the two are unrelated and neither is redefined by the
other.

This specification preserves the future ability to measure Home Intelligence processing latency, time
to first useful result, and end-to-end Home interaction latency (§17), without implementing any of it.

---

## 20. Home Assistant compatibility / research findings

Verified against current official Home Assistant developer and user documentation during this
specification's preparation (in addition to the already-accepted repository evidence in
[home-assistant-boundary.md](home-assistant-boundary.md)'s native-capability evaluation table, which
this section extends, not replaces):

| Finding | Source | Verified |
|---|---|---|
| The Assist pipeline runs `wake_word → stt → intent → tts` in order, over `assist_pipeline/run`, with each stage a separate entity type (`wake_word`, `stt`, `conversation`, `tts`) | `https://developers.home-assistant.io/docs/voice/pipelines/` (current, fetched during this specification's preparation) | Yes |
| A household may configure multiple pipelines; an `assist_satellite` entity may declare `pipeline_entity_id` (a `select` entity) to choose which pipeline it uses; absent that, the single global "preferred pipeline" is used | `https://contributors.home-assistant.io/core/entities/assist-satellite/` (current) | Yes |
| The conversation API (`conversation/process`) accepts an `agent_id` (defaulting to the built-in `conversation.home_assistant` agent) and returns a `response_type` of `action_done`, `query_answer`, or `error` (with `data.code` such as `no_intent_match`); `conversation_id` continues a conversation across turns | `https://contributors.home-assistant.io/core/internals/conversation-api/` (current) | Yes |
| Speech-to-Phrase is a closed-domain, local, fast (sub-second on modest hardware) STT model generated from the household's own Home Assistant entities; a household selects it instead of an open-ended engine such as Whisper — **a user/configuration choice, not an automatic runtime fallback** | Official Home Assistant voice-setup documentation and community technical documentation (no official dedicated integration reference page was reachable during this research pass; findings corroborated across multiple independent sources) | Partially — primary claim (closed-domain, entity-generated, local, fast) corroborated across independent sources; **no official page directly confirming an automatic-fallback mechanism was found, consistent with this specification's position that none is asserted to exist** |
| Wyoming is a lightweight protocol connecting voice services (wake word, STT, TTS) to Home Assistant without the cloud; already accepted in this repository (**DL-50**) as the preferred, non-mandatory voice-pipeline interoperability boundary, with no speaker/biometric service type | `home-assistant-boundary.md`'s existing, already-verified capability table (citing `https://www.home-assistant.io/integrations/wyoming/`, `https://github.com/OHF-Voice/wyoming`) | Yes (already accepted repository evidence, reused here) |
| `assist_satellite` entities do not perform recognition or synthesis themselves; they move audio and events between the device and the pipeline, whose actual STT/conversation/TTS entities do the work | `https://contributors.home-assistant.io/core/entities/assist-satellite/` (current) | Yes |

**No authoritative current Home Assistant source was found describing an automatic, native,
content-based fallback between STT engines or pipelines.** This specification's position in §8 — that
such routing is a configuration-time or explicit-invocation-time choice, not an automatic per-utterance
mechanism — is consistent with every source reviewed.

---

## 21. Reference Home applicability

The Reference Home's candidate technologies (Speech-to-Phrase for fast Home control, Whisper for
open-ended recognition, Piper for local TTS, local inference for Home Intelligence, dedicated microphone
arrays, room Sonos output) are **evidence and comparative-testing context, not HTBW architectural
requirements.** No HTBW installation is required to use any of them. This restates, for the processing
workstream specifically, the same Reference-Home-independence principle already established in the
Decoupled Voice Interaction Capability Architecture ADR and the Stable Endpoint Identity ADR.

---

## 22. Acceptance scenarios (implementation-neutral)

Not executable tests — no test framework, test file, or code is introduced by this specification.

1. A deterministic Home-control interaction (Class A) can complete without Home Intelligence.
2. Ordinary Home control does not require an LLM.
3. A contextual interaction (Class B) can invoke Concierge without automatically invoking Home
   Intelligence.
4. An open-ended interaction (Class C) may use open-ended recognition without that engine becoming
   constitutional.
5. A reasoning-required interaction (Class D) may escalate to Home Intelligence without Home
   Intelligence being required for any other class.
6. A context-dependent conversational follow-up (Class E) preserves Continuity's existing session
   state rather than being routed to a context-losing fast path.
7. A faster processing path never bypasses Operational Trust — recognition and interpretation alone
   never authorize an action.
8. Recognition or interpretation output never becomes an authoritative Truth fact about current Home
   state.
9. Voice Identity remains architecturally available (its evidence pipeline engageable) across every
   supported recognition path, or the specific path's inability to supply evidence is documented as an
   implementation constraint rather than worked around by bypassing Identity.
10. A spoken response, where one occurs, uses the Room's Foundation-configured `spoken_response_output`
    through Concierge's existing delivery path.
11. A successful deterministic-control interaction may intentionally remain silent.
12. Home Intelligence unavailability does not unnecessarily prevent deterministic Home control.
13. Open-ended recognition unavailability does not unnecessarily prevent supported deterministic Home
    control.
14. `spoken_response_output` unavailability does not necessarily prevent an otherwise valid action from
    completing.
15. Processing-provider choice (which STT/TTS/reasoning provider) is never encoded into a
    `RoomInteractionFunctionAssignment` record — Room setup and processing-path concerns remain
    separable.
16. Routing/fallback behavior not proven to exist (for example, automatic STT engine fallback) is never
    presented as implemented.
17. End-to-end performance can be measured by stage (§17), independent of any single component's
    throughput.
18. Tokens-per-second alone cannot satisfy performance acceptance.
19. Raw audio is not required to become durable telemetry or observability data.
20. No specific voice, STT, TTS, inference, microphone, or speaker vendor is required by the core
    specification.

---

## 23. Deferred implementation work

All executable work: the actual routing/escalation implementation; any pipeline-selection automation;
the actual Voice Identity audio-tap integration; the actual Decision Trace fields for processing-path
recording; performance instrumentation; and any Home Intelligence integration. **Deferred pending an
authorized HTBW Core implementation surface**, per the same finding recorded in the Foundation Room
Interaction Roles specification (§1 there).

---

## 24. Open questions

Resolved only where accepted architecture or authoritative platform evidence supports the answer;
otherwise explicitly deferred, not guessed:

- **The automatic processing-path routing mechanism itself** — how (or whether) a future
  implementation changes pipeline/provider selection in response to observed evidence (§8). Not
  resolved here.
- **Fast-path-to-open-ended-path escalation mechanics** — whether a failed closed-domain recognition can
  safely trigger a second, open-ended recognition attempt on the same captured audio, and the privacy
  and latency implications of doing so. Not resolved here.
- **Voice Identity evidence availability across recognition paths** — whether tapping audio at the
  Wyoming boundary (§9) is sufficient and safe in practice regardless of which `stt` entity is selected;
  recorded as favorable research evidence, not a proven guarantee. Not resolved here.
- **How conversation continuity crosses processing-path changes** in practice (beyond the native
  `conversation_id` mechanism already verified, §10) — the precise mechanics of carrying Continuity
  state across a Class A→D escalation. Not resolved here.
- **Instrumentation points** — the exact Decision Trace field additions (if any) needed for §18's
  observability goals. Not resolved here; existing Decision Trace structure is reused, not extended, by
  this specification itself.
- **The future Home Intelligence boundary/interface** — mechanics remain with the separately pending
  **DL-86**/Issue #191, not this specification.

---

## 25. Explicit non-goals

- Does not implement, or produce executable code for, any part of this specification.
- Does not create an HTBW Core implementation repository or surface.
- Does not touch the `concierge`, `voice_identity`, or `asset_intelligence` repositories.
- Does not implement Speech-to-Phrase, Whisper, Wyoming services, STT fallback, an STT proxy, Home
  Intelligence, or Ollama; does not install any of them; does not select an LLM or Home Intelligence
  hardware.
- Does not modify ESPHome or reSpeaker firmware.
- Does not change Concierge audio runtime code or Sonos scripts.
- Does not create arbitrary latency SLAs.
- Does not redesign Voice Identity or the Foundation Room Interaction Roles specification.
- Does not reopen DL-90, DL-91, DL-05, DL-06, DL-50, DL-67, DL-68, or DL-86 (the last remaining
  separately pending, unaffected).
- Does not make any vendor, engine, or Reference Home configuration choice constitutional.

---

## Related documents

- [adr-decoupled-voice-interaction-capability-architecture.md](adr-decoupled-voice-interaction-capability-architecture.md)
- [foundation-room-interaction-roles-specification.md](foundation-room-interaction-roles-specification.md)
- [adr-wyoming-compatible-voice-evidence-runtime.md](adr-wyoming-compatible-voice-evidence-runtime.md)
- [adr-identity-replaces-voice-identity-boundary.md](adr-identity-replaces-voice-identity-boundary.md)
- [adr-home-identity-and-home-intelligence-governance.md](adr-home-identity-and-home-intelligence-governance.md)
- [home-assistant-boundary.md](home-assistant-boundary.md)
- [runtime-sequence.md](runtime-sequence.md)
- [failure-and-degradation.md](failure-and-degradation.md)
- [privacy.md](privacy.md)
- [greenfield-mandate.md](greenfield-mandate.md)
- [../contracts/concierge-contract.md](../contracts/concierge-contract.md)
- [../contracts/identity-contract.md](../contracts/identity-contract.md)
- [../contracts/continuity-contract.md](../contracts/continuity-contract.md)
- [../contracts/operational-trust-contract.md](../contracts/operational-trust-contract.md)
- [../contracts/truth-contract.md](../contracts/truth-contract.md)
- [../models/decision-trace.md](../models/decision-trace.md)
- [../models/glossary.md](../models/glossary.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
