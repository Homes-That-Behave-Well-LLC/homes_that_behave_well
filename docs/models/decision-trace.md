# Decision Trace Model

> **Document status: Canonical model.**
> Terminology: [glossary.md](glossary.md). Produced by **Concierge**, composed from every
> responsibility that contributed.
> Architecture: [../architecture/explainability.md](../architecture/explainability.md)

---

## Purpose

The Decision Trace is the structural mechanism by which the home can answer *why did this happen?*
and *why did this not happen?*

**Explainability is a required output of the framework, not an optional feature.** A decision that
cannot be explained is a defect.

## Question answered

*What happened, why, on what basis, and what alternative was rejected?*

---

## Required structure

A Decision Trace must be able to record:

1. What was requested
2. Who requested it
3. How identity was determined
4. Identity confidence
5. Room context
6. Vocabulary resolution
7. Facts consulted
8. Fact confidence
9. Obligations considered
10. Preferences considered
11. Continuity intent
12. Policies evaluated
13. Restrictions applied
14. Autonomy level
15. Conflicts detected
16. Resolution applied
17. Action taken
18. Action suppressed
19. Reason for suppression
20. Alternative considered

A trace is produced for **actions, non-actions, and suppressions alike**.

---

## Field ownership

| Field group | Contributing responsibility |
|---|---|
| 1–2 request and requester | Concierge (interaction), Identity (candidate) |
| 3–4 identity determination and confidence | Identity — recorded as `identity_confidence_band` (**DL-39**), never conflated with field 8 |
| 5 room context | Room Configuration (Foundation) |
| 6 vocabulary resolution | Contextual Vocabulary (Foundation) |
| 7–8 facts and fact confidence | Truth — recorded as `truth_confidence_band` (**DL-58**), plus the Fact's validity state (`current`, `operationally_expired`, `unavailable`, `never_observed` — **DL-59**), never conflated with field 4 or with confidence. Where the Fact is sourced from a **Provider-Derived Environmental Indicator**, field 7 additionally names the provider and the indicator's provider-qualified name, and distinguishes it from a Direct Environmental Measurement or an HTBW Formula-Derived Fact (**DL-62**). **Where a genuine Truth conflict (DL-63) was qualified and resolved to produce this Fact**, field 7 additionally names the competing claims and their sources, the qualification outcome, the applicable Conflict Policy version, and the published outcome (reduced confidence, unresolved, or `unknown`) |
| 9 obligations | Stewardship |
| 10–11 preferences and continuity intent | Continuity |
| 12–14 policies, restrictions, autonomy level | Operational Trust |
| 15–20 conflicts, resolution, action, suppression, reason, alternative | Concierge — **a household-facing decision conflict** (for example two sessions meeting in one Room), distinct from and never conflated with a Truth-level evidence conflict (**DL-63**), which is recorded in fields 7–8 as part of the Fact itself |

Concierge composes the trace. **Concierge does not author fields it does not own.**

### Delegated Stewardship authority (DL-57)

Where an obligation-related decision involved self-authority, an authorized proxy, or a Delegated
Access Grant, field 9 (obligations, Stewardship-owned) and fields 3–4 (identity determination,
Identity-owned) together carry: whether the acting person was the subject, an authorized proxy, or a
grantee; the specific grant applied, its scope, and its operations; and, where a grant was later
revoked, that fact and its effect on the obligations it covered. **No new numbered field is
introduced** — this is carried within the existing obligation and identity-determination fields, kept
distinguishable so *"the subject agreed"* is never confused with *"a proxy configured this."*

### Room Context and how it was resolved

Field 5 is **not satisfied by naming a Room**. Foundation already guarantees to supply *"Room Context
**and how it was resolved**"* ([../contracts/foundation-contract.md](../contracts/foundation-contract.md),
[../contracts/room-configuration-contract.md](../contracts/room-configuration-contract.md)), and the
trace must carry both.

| Element | Requirement |
|---|---|
| `room_context.room` | The resolved Room or Merged Room, **or `unresolved`** |
| `room_context.resolved_from` | **The source of the resolution.** Mandatory whenever a Room was resolved |
| Constituent Room, where relevant | Which **Constituent Room** supplied a finer-grained Fact, per [room.md](room.md) |

> **A trace that names a Room without stating how it was resolved is incomplete.** Under the failure
> table below, a field that cannot be given is recorded as `unavailable` or `not_applicable` with its
> reason — **never omitted, and never silently filled with a plausible Room.**

**The enumeration of `resolved_from` is deliberately not fixed here.** Two of its values are already
governed — resolution from a **participating voice assistant's Room assignment**, and resolution from an
**explicit resident statement** ([room-configuration.md](room-configuration.md)). **A third case has no
governed value at all**: an interaction arriving through a surface that is **not bound to a Room** — a
phone, a wearable, a Companion App action, or a browser session. That case is **open decision OD-73**, and
this model does not pre-empt it.

Until OD-73 closes:

- The governed outcome for a non-room-bound surface is **`unresolved`**, and the trace says so.
- **Room Context is never inferred from device naming**, and a plausible Room is never substituted.
- **Adding a `resolved_from` value that OD-73 has not accepted is a defect**, not an implementation detail.

**Resolving Room Context never produces, alters, or substitutes for an Identity Assertion.** The two are
recorded in different fields, by different owners, for different questions.

#### Worked example — Room Context resolved from a voice assistant

```yaml
decision_id: 2026-08-16T18:22:07Z/kitchen/light.turn_on
requested: "turn on the lights"
room_context:
  room: Kitchen
  resolved_from: voice_assistant_room_assignment
  resolution_reference: <governed reference to the Room Configuration version>
vocabulary_resolution:
  term: Lights
  resolved_targets: [kitchen_ceiling, kitchen_under_cabinet]
  mapping_source: room_configuration
action_taken: light.turn_on(kitchen lights)
```

> "I turned on the Kitchen lights because you asked the Kitchen assistant, and *Lights* is configured
> there as the ceiling and under-cabinet lights."

#### Worked example — Room Context unresolved

```yaml
decision_id: 2026-08-16T18:24:41Z/unresolved/light.turn_on
requested: "turn on the lamps"
interaction_surface:
  kind: companion_app
  surface_reference: <native reference>
  room_bound: false
room_context:
  room: unresolved
  resolved_from: not_applicable
  reason: interaction_surface_not_room_bound
  open_decision: OD-73
vocabulary_resolution: not_attempted
reason: room_context_unresolved
capability_availability: available
access_decision: not_evaluated
action_taken: none
action_suppressed: light.turn_on
suppression_reason: room_context_unresolved
alternative_considered: ask_which_room
```

> "I did not turn on the lamps, because I could not tell which room you meant — you asked from your
> phone, and it is not tied to a room. Which room did you mean?"

**This trace is complete, and the outcome is correct.** A dependency was not missing, permission was not
denied, and identity did not fail — **the Room was genuinely unknown, and the home said so.**

### Threshold, confirmation, and disclosure detail

No new field group is introduced. Fields 3, 4, 12, 13, and 20 must be able to carry the following,
and a trace that cannot is incomplete:

| Detail | Contributing responsibility |
|---|---|
| The assertion purpose, and the confidence **band** | Identity |
| The numeric value, only where policy governs it and privacy permits | Identity |
| The presentation threshold applied, and whether it was met | Operational Trust |
| The capability access threshold applied, and whether it was met | Operational Trust |
| Whether confirmation was **offered** or **required** | Operational Trust |
| The confirmation method, outcome, scope, and expiry | Operational Trust |
| The audience composition considered, and its residual uncertainty | Operational Trust |
| The disclosure decision, recorded **separately** from the access decision | Operational Trust |
| The delivery surface selected, and any alternative offered | Concierge |

Fields 3 and 4 must additionally be able to carry the **fusion explanation**:

| Detail | Note |
|---|---|
| The **Fusion Policy version** that produced the assertion | Without it, an old result cannot be honestly explained |
| Provider match values, **as reported** | Never rewritten as the fused result |
| Supporting evidence, by family | Correlated observations shown as **one** contribution |
| The correlation treatment applied | Which observations were grouped, and why they were not counted separately |
| Contradicting evidence, and the reduction applied | Contradiction is claim-specific and is never averaged away |
| Excluded evidence and its exclusion reason | Ineligible, inapplicable, stale, or disabled |
| Competing candidates, and whether separation was met | The basis for `known` versus `ambiguous` |
| Reason codes | For every reduction, exclusion, ceiling, step, and outcome |

A trace must be able to say plainly *"a highly reliable wearable corroborated the candidate"* and
*"several phone-derived observations were treated as one"*. It must never expose voiceprint vectors,
embeddings, raw biometric payloads, storage paths, provider secrets, or unnecessary device
identifiers.

A trace must be able to state plainly that a threshold was met by confirmation rather than by
evidence, **without claiming that the original assertion became certain**. Biometric internals are
never included, and a confirmation artifact is retained only under its own classification and
retention policy.

A policy change never rewrites an earlier trace. A trace must remain explainable under **the
threshold and policy version that applied when the decision was made** (**P27**).

### Vocabulary and command resolution (DL-69)

No new field group is introduced; this extends fields 3, 4, 5, 12, 13, and 20 for a conversational
retrieval or command-resolution interaction. A trace must be able to carry:

| Detail | Note |
|---|---|
| Receiving endpoint | The voice assistant or surface that received the utterance |
| Recognized text | Exactly what the native pipeline returned — never a claimed confidence score, since none is documented as available |
| Vocabulary context and precedence applied | Which context (active clarification, Person, Merged Room, Physical Room, Home/Global) supplied the resolved term, per **DL-69**/**DL-70**'s precedence order |
| Winning scope and any shadowed (losing) scope | Whether a Room- or Merged-Room-scoped term shadowed a Home-scoped one, and what was shadowed (**DL-70**) |
| Inherited, explicit, or shadowed | Whether the resolved term was a Home-scoped inheritance, an explicit Room/Merged-Room/Person definition, or a shadow of a broader scope (**DL-70**) |
| Fulfillment source actually used | The provider, target, or source that satisfied the resolved word in this Room, Merged Room, or for this Person, distinguished from the word itself (**DL-70**) |
| Matched canonical Vocabulary term, and its mapping source | `native_seed`, `accepted_native_seed`, or `household_defined` |
| Singular or plural interpretation | Whether the utterance resolved as a collection term, a recognition form of one, or a distinct member-level term |
| Candidate and clarification sets | Bounded to authorized, exposed, contextual Vocabulary only |
| Suggested alternative, where offered | A "did you mean" suggestion, and that it required confirmation before any execution |
| Native-fallback candidate, where considered | Whether it was exact, permitted, exposed, and safe |
| Match classification | Deterministic, ambiguous, no-match-with-safe-native-candidate, no-match-unsafe-interpretation-rejected, or no-match-no-safe-candidate |
| No-match reason, where applicable | Never silently omitted |

A trace for this class of interaction must never record content that was withheld from the resident
alongside content that was spoken, in a form that could itself leak the withheld content.

### Intended Audience Specification (DL-71)

For a Communication or Stewardship obligation, a trace must be able to carry:

| Detail | Note |
|---|---|
| Originating responsibility | Which responsibility declared the Intended Audience |
| Original specification, and its form | Named Person, Role/Authority Class, Relationship-based, Anyone Present With Authority, or Household — verbatim, never rewritten |
| Resolution time | Origination, or each Delivery Attempt, per the form's re-resolution rule |
| Assertion Purpose used, where evidence-based | Household/Room Presence for Anyone Present With Authority; none for a configuration lookup |
| Relationship records consulted, where Relationship-based | Which `caretaker-of` assignment records were read |
| Resolved Persons, and Persons excluded | Never silently omitted |
| Unknown or uncertain candidates | Retained, never resolved away |
| Operational Trust result | Including any **DL-57** Delegated Access Grant checked |
| Audience Composition, separately | Never collapsed with the specification (**DL-34**) |
| Authorized Recipients, and Delivery Targets | Distinguished from each other and from the specification |
| No-recipient outcome, where applicable | The accountability gap or equivalent, never a silent discard |
| Too-broad outcome, where applicable | The degradation applied, never a broadened disclosure |
| Completion Mode, where applicable | One Completion Satisfies All or Each Recipient Must Complete, and by whom completed |
| Escalation change, where applicable | That a new specification was recorded, not a mutation of the original |

### Audience-uncertainty disposition (DL-72)

Extends the group above for a Communication delivered, or attempted, under audience uncertainty. A
trace must be able to carry:

| Detail | Note |
|---|---|
| System-Initiated or Person-Requested | Which origin classification applied |
| Requestor, where Person-Requested | The identified Person, or that requester authority could not be established |
| Audience Composition uncertainty state | Unresolved plurality, Audience unknown, Audience detection unavailable, or contradictory evidence (**DL-34**, **DL-63**) — never collapsed into one generic "uncertain" flag |
| Content classification | As declared by the originating responsibility (enumeration is **OD-51**'s) |
| Room or Merged Room, and Mode | Current values considered |
| Global uncertainty policy version, and Person-specific preference, if applied | Distinguished from the ordinary delivery preference |
| Ordinary delivery preference, for contrast | Recorded even where the uncertainty preference overrode it |
| Explicit delivery instruction, where given | For example "send that to my phone" |
| Private-surface qualification result, per candidate surface | Which criteria were met or failed, and why |
| Degradation path taken | Private redirect, content-free Indication, neutral challenge, or defer/refuse |
| Redirected Delivery Targets, per recipient | Independent per recipient (**DL-71**) |
| Content withheld | Never silently omitted |
| Retry or escalation references, where applicable | Owned by **OD-54**/**OD-22**, referenced not restated |

### Five separately recorded outcomes

A trace must keep these apart. Collapsing any two of them makes the home's account of itself wrong,
even when the behaviour was right.

| Recorded outcome | Must carry |
|---|---|
| **Identity result** | Candidate Person by reference; assertion purpose; assertion state; **the band, only where the state is `known`**; Fusion Policy version; supporting and contradicting evidence references |
| **Requirement** | The **Required Identity Band** — `None`, Low, Moderate, High, or Very High — the **Required Confirmation Strength**, and the applicable policy version |
| **Access decision** | Whether identity was required at all; whether the current band met the requirement; the other Operational Trust conditions applied; the final decision |
| **Presentation decision** | The Address by Name setting; the required current band; whether the current band qualified; the audience or disclosure constraint; whether the response was **named or neutral** |
| **Confirmation** | Whether it was offered or required; the method; the outcome; the protected operation it was consumed by; and that it was **not reused** |

Where a capability was **unavailable**, the trace records the **capability availability** outcome
instead: the capability, the declared dependency that was missing, and that identity and requirement
were **not evaluated**. **A dependency failure is never recorded as a denial, a refusal, or an
identity failure.** See [../architecture/failure-and-degradation.md](../architecture/failure-and-degradation.md).

Two rules follow:

- **Where the Required Identity Band is `None`, the trace states that known-Person identity was not
  required.** It must never state that a band satisfied, exceeded, or cleared `None` — that would
  invent an identity dependency the policy did not have.
- **The access and presentation outcomes are recorded separately even when both succeed**, because
  they can and often do differ.

The worked form of a complete trace reads:

> Lamp control required no known-Person identity. The current speaker was supported as Tom at **High**
> identity confidence.
> Operational Trust authorised lamp control independently of identity. The Address by Name setting
> required **High**; Operational Trust permitted use of Tom's name. Concierge responded *"Tom, I have
> turned on the lamps."*

A trace must also be able to record that an **earlier** assertion, band, or confirmation was **not**
carried into this interaction — that the current result was evaluated from current evidence. Silence
on that point is not sufficient where a resident could reasonably believe the home was still talking
to the previous person. **This is Current-Interaction Applicability (DL-64)**: the earlier assertion
remains a permanently valid historical record, and its exclusion here is an applicability outcome, not
a revocation — and where it was excluded as ineligible evidence inside Identity's own fusion, it never
reached Truth as a candidate claim requiring DL-63 conflict resolution at all.

---

## References, not copies

Under **P30**, a Decision Trace **references the exact version** of every governed record it used.
It does not copy complete source payloads.

Exact versions are referenced for:

- Truth Facts
- Identity Assertions
- Operational Trust policies and decisions
- Stewardship obligations
- Continuity preferences and sessions
- Room Configuration
- Contextual Vocabulary mappings
- Explicit human requests

Where durable human readability requires it, a **minimal immutable explanation projection** may be
retained beside the reference — for example the household-language name of the policy that
prevailed. It must not become a wholesale copy.

| Rule | Statement |
|---|---|
| Accuracy survives change | An explanation must remain accurate after the current configuration or policy has changed |
| Ownership does not transfer | Referencing a Fact does not make Concierge a producer of Facts |
| Re-derivation is not permitted | A reference is not permission to recompute another responsibility's output |
| Dangling references are reported | **A dangling or unresolved reference must be reported, never silently rendered as though the source record never existed** |

An explanation that silently re-reads today's policy to describe last month's decision is a defect.

The reference and version model is [temporal-record.md](temporal-record.md). The identifier strategy
is open decision **OD-38**.

---

## The Decision Trace across time

A Decision Trace is an **immutable temporal record**. It is one of the five record kinds defined in
[temporal-record.md](temporal-record.md), and it explains a Concierge evaluation covering action,
non-action, suppression, deferment, refusal, question, and suggestion alike.

Decision history is **owned by Concierge**. No other responsibility maintains a parallel decision
history.

Decision Traces participate in Historical Explainability retrieval by decision, time range, incident
retrieval scope, Room, Merged Room, Asset, Person, and correlation or causation chain. The query
surface is open decision **OD-35**.

### Preservation and transitive integrity

A Decision Trace may be placed within a **Preservation Hold**. Because the trace references exact
versions rather than copying payloads, **holding a trace must also preserve the governed source
versions required to keep it explainable**, subject to privacy and legal constraints.

**Do not duplicate referenced payloads merely to satisfy a hold.** A held trace whose required
references have been silently purged is a preservation failure. See
[../architecture/privacy.md](../architecture/privacy.md).

---

## Two paired forms

Every Decision Trace has both a machine form and a human form. Neither replaces the other.

### Machine form

```yaml
decision_id: 2026-07-21T21:14:03Z/den/media.play
requested: "play jazz"
requester:
  assertion_purpose: current_speaker
  candidate_person: Tom
  assertion_state: known
  identity_confidence_band: High
  fusion_policy_version: 4
  supporting_evidence_families: [voice, wearable_proximity]
  contradicting_evidence: none
  identity_assertion_ref: <governed reference>
native_references:
  - den_occupancy_event: <native reference>
  - voice_assistant_interaction: <native reference>
room_context:
  room: Den
  resolved_from: voice_assistant_room_assignment
vocabulary_resolution:
  term: Speakers
  resolved_targets: [den_sonos_left, den_sonos_right]
  mapping_source: room_configuration
capability_availability: available
facts_consulted:
  - statement: den.occupied = true
    truth_confidence_band: High
    provenance: [motion_a, presence_b]
    freshness_s: 4
    fact_ref: <governed reference>
  - statement: den.active_session = none
    truth_confidence_band: High
obligations_considered: []
preferences_considered:
  - person_scoped.preferred_genre = jazz
continuity_intent:
  follow_me: enabled
  transfer_requested: false
policies_evaluated:
  - home.quiet_hours: not_active
  - den.autonomy_ceiling: autonomous
  - media.play.required_identity_band: None
  - address_by_name.required_band: High
  - policy_version: 11
access_decision:
  identity_required: false
  basis: "media playback requires no known-Person identity"
  decision: permitted
presentation_decision:
  address_by_name_required_band: High
  current_band_qualified: true
  response: named
restrictions_applied: []
autonomy_level: autonomous
conflicts_detected: []
resolution_applied: none_required
action_taken: media.play(jazz -> den speakers)
action_suppressed: none
suppression_reason: null
alternative_considered: ask_before_playing (not required at autonomous level)
```

> **Read the access and presentation lines together.** Identity did not authorise the music — the
> operation required none, and it would have played for anyone. Identity qualified the home to use
> Tom's name. **A trace that collapses those two into "I recognised you, so I played it" is wrong
> about why the home acted**, even though the music was right.

### Human form

> "I started jazz on the Den speakers because you asked for it, the Den was free, and you have jazz
> as your preferred genre. Quiet hours were not active, so I did not need to ask. I used your name
> because I recognised you — the music itself did not require that."

---

## Non-action traces

A non-action trace is as important as an action trace.

```yaml
decision_id: 2026-07-21T23:41:52Z/primary_bedroom/media.transfer
requested: follow_me_transfer(session: tom.jazz, origin: office, destination: primary_bedroom)
requester:
  candidate_person: Tom
  identity_confidence_band: High
facts_consulted:
  - statement: primary_bedroom.mode = nighttime
    truth_confidence_band: High
policies_evaluated:
  - primary_bedroom.nighttime: no_incoming_media
restrictions_applied: [primary_bedroom.nighttime.no_incoming_media]
autonomy_level: explicit
action_taken: none
action_suppressed: media.transfer
suppression_reason: destination_room_mode_prohibits_incoming_media
alternative_considered: ask_before_transfer (blocked by nighttime interruption policy)
```

> "I did not move the music into the Primary Bedroom because the room is in Nighttime mode, and
> Nighttime mode does not allow music to arrive on its own. I also did not ask, because Nighttime mode
> does not allow me to interrupt."

### A suppressed Communication always produces a trace

**Withholding a Communication is an Intentional Non-Action**, and is traced under **P16** and
**DL-15** exactly as any other non-action. A home that decided to stay quiet and cannot say so is in
the condition **P27** was written to prevent.

The trace must record the audience considered, the surfaces considered and why each was rejected, the
visibility or interruption rule that prevailed, and whether a **content-free indication** was
available as a degradation.

```yaml
decision_id: 2026-07-21T23:41:52Z/den/communication.deliver
communication_reference: communication/9f2c@v1
audience: role(caretaker)
facts_consulted:
  - statement: den.contextual_persons includes an unidentified guest
    confidence: medium
policies_evaluated:
  - den.shared_surface: no_sensitive_content_with_unauthorised_listener
restrictions_applied: [privacy.visibility.health_class]
action_taken: delivery_attempt(surface_class: personal)
action_suppressed: announcement(surface_class: shared_audible)
suppression_reason: unauthorised_listener_may_perceive_surface
alternative_considered: content_free_indication (available, not required here)
```

> "I did not say it aloud in the Den, because someone I could not identify was present and the
> reminder is private. I sent it to your phone instead."

See [communication.md](communication.md).

---

## Quality rules

1. Explanations use **household vocabulary**, not entity IDs or internal service names.
2. Explanations name the **deciding factor**, not every evaluated input.
3. Explanations state **uncertainty honestly**: "I was not certain it was you."
4. Explanations never fabricate a rationale after the fact.
5. Explanations for refusals state **what would change the outcome**, where safe to do so.
6. Explanations respect privacy: a trace shown to one person must not disclose another person's
   protected content.
7. **A Decision Trace exists only where HTBW decided.** Where a resident, a native automation, a
   script, a scene, or an external integration caused a change, there is no HTBW decision and
   therefore no trace. **A trace is never fabricated for a decision HTBW did not make.** What
   occurred is recorded as a **Domain Event** with behaviour attribution instead. See
   [temporal-record.md](temporal-record.md).

---

## Consumes

Contributions from Identity, Room Configuration, Contextual Vocabulary, Truth, Stewardship,
Continuity, and Operational Trust.

## Provides

- A queryable record supporting "why did this happen?" and "why did this not happen?"
- Diagnostic evidence for misbehaviour
- Audit evidence for authority and consent decisions

## Explicit non-responsibilities

The Decision Trace does **not** grant authority, establish facts, or alter behavior. It records.

**A Decision Trace is not a record of what occurred.** It answers *why HTBW decided*, never *what
happened in the household*. That is a **Domain Event**, and the two are not interchangeable.

---

## Failure behavior

| Condition | Behavior |
|---|---|
| A contributing responsibility is unavailable | Record the field as `unavailable` with the reason; never omit it silently |
| The trace cannot be written | The failure itself is reportable; a silently untraced decision is a defect |
| A field is not applicable | Record `not_applicable`, not empty |
| A referenced version cannot be resolved | Report the reference as unavailable with the reason where known; never render it as though the source record never existed |
| A referenced record was purged or redacted | Report *"no longer retained"* or *"redacted"*; never *"never existed"* and never *"nothing happened"* |
| A held trace's required references were removed | Report a preservation failure |

## Privacy considerations

Decision Traces contain identity, presence, preference, and obligation data. Visibility is governed by
Operational Trust policy. Biometric internals are never included; only reason codes, confidence bands,
and evidence classes.

Retention is bounded from **both** directions: **P27** establishes a floor, and
[../architecture/privacy.md](../architecture/privacy.md) establishes the ceiling. **DL-47 settles the
rule**: a Decision Trace is governed explainability history following **External History Retention**
unless an accepted floor or a Preservation Hold applies, and **holding a trace preserves the governed
source versions required to keep it explainable** rather than duplicating their payloads. The exact
floor and ceiling values remain open decision **OD-05**.

**Referencing instead of copying is itself a privacy mechanism.** Sensitive content stays in one
governed place, where it can be redacted once, rather than in every trace that consumed it. A trace
whose referenced content has been redacted remains a record that the decision was made.

## Explainability requirements

This model *is* the explainability requirement. Every other canonical document references it.

---

## Representative scenarios

- [../scenarios/why-did-this-happen.md](../scenarios/why-did-this-happen.md)
- [../scenarios/nighttime-suppression.md](../scenarios/nighttime-suppression.md)

## Open decisions

| ID | Question |
|---|---|
| OD-05 | Decision Trace retention floor and ceiling |
| OD-29 | Where Decision Traces are persisted — Home Assistant logbook, connected storage, or both, including purge exemption and Governed Reference resolvability |
| OD-30 | Which surfaces expose Decision Traces, and to whom |
| OD-35 | Historical query surface and access |
| OD-38 | Version identity, correlation, and causation identifier strategy |
| OD-39 | Preservation Hold authority, duration, review, release, and conflict with deletion |
| OD-44 | Delivery outcome semantics across the two levels |
| OD-57 | Indication versus content separation |
| OD-63 | **Closed — DL-73.** Behaviour attribution — which evidence a Domain Event's attribution may carry where no Decision Trace exists, because no HTBW decision was made. The Source Confidence tier (Known/Probable/Unknown Source), the Decision Authority / Source / Execution distinction, the narrowed Behaviour Source enumeration, Person Attribution (Known/Unknown/No Person), and alternative-explanation handling (no competing candidates presented) are all accepted. Where HTBW itself decided and executed through Home Assistant, the resulting Domain Event's Decision Authority attribution references the Decision Trace that produced it |
| OD-64 | Native behaviour observation — which platform-supplied execution evidence is referenced and retained |
| OD-72 | **Closed — DL-74.** Unknown Actor correlation confidence — a Historical Reconstruction's Unknown Actor Reference carries a Primary Hypothesis Label, a Criteria Satisfaction Record, and Supporting/Contradicting Evidence, never a Decision Trace field — a reconstruction is a Concierge-assembled projection, not a decision HTBW made, and is never recorded as one |
| OD-73 | **Interaction-Surface Room Context Resolution**, which owns the `room_context.resolved_from` enumeration. **Until it closes, a non-room-bound surface yields `unresolved`** |

## Related documents

- [../architecture/explainability.md](../architecture/explainability.md) — see also its *Explainability
  Evidence Record* hypothesis, which bounds what this model's quality rule 7 already states: where no
  HTBW decision was made, the evidence belongs to the Domain Event's behaviour attribution, never to a
  fabricated trace
- [temporal-record.md](temporal-record.md)
- [communication.md](communication.md)
- [../architecture/adr-temporal-record-model.md](../architecture/adr-temporal-record-model.md)
- [../architecture/adr-resident-communication-and-delivery-separation.md](../architecture/adr-resident-communication-and-delivery-separation.md)
- [operational-trust.md](operational-trust.md)
- [../architecture/connected-storage.md](../architecture/connected-storage.md)
