# Concierge Contract

> **Document status: Canonical contract.**
> Responsibility: **Concierge**. Framework:
> [../architecture/framework.md](../architecture/framework.md).
> Terminology: [../models/glossary.md](../models/glossary.md).
>
> Sections **1 through 14** below are canonical. The **Historical appendix** that follows them is
> retained as architectural evidence from the pre-refoundation Concierge exploration. Where the
> appendix conflicts with the canonical sections or with
> [../architecture/framework.md](../architecture/framework.md), the canonical text prevails.

---

## 1. Owning responsibility

**Concierge — what should happen now?**

> **Concierge orchestrates. It does not own everything it consumes.**

Concierge is the last responsibility in the framework order because it depends on all the others.
Nothing depends on Concierge.

---

## 2. Consumes

| From | What |
|---|---|
| Foundation | Object definitions, relationships, capability descriptions |
| Room Configuration | Room Context, participation, exposure, experience endpoints |
| Contextual Vocabulary | Resolved target sets for household terms |
| Identity | The identity assertion, with confidence and reason code |
| Truth | Authoritative facts, with confidence, provenance, and freshness |
| Stewardship | Obligation state, significance, accountability, escalation intent |
| Continuity | Preferences, session state, transfer and resume intent and eligibility |
| Operational Trust | The authority decision and the effective autonomy level |

---

## 3. Owns

- Interpretation of intent
- Selection among permitted actions
- Conflict resolution between competing permitted outcomes
- Timing, modality, and phrasing of communication
- Whether to act, ask, defer, convey, escalate, or do nothing
- Resolution of a Communication **audience specification** to **Delivery Surfaces**
- The decision to deliver, suppress, defer, retry, or give up, and each **Delivery Attempt**
- The **record of every Communication state transition and Delivery Attempt outcome**
- Execution through governed interfaces
- Composition of the Decision Trace
- The resident-facing explanation

> **Concierge owns delivery, not communication significance.** See
> [../models/communication.md](../models/communication.md).

---

## 4. Does not own

- Object definitions or asset knowledge (Foundation)
- Room Configuration or vocabulary (Foundation)
- The definitions of Communication, Delivery, Delivery Attempt, Delivery Surface, and Urgency
  (Foundation)
- Who a person is (Identity)
- What is true (Truth)
- What matters and what care is owed (Stewardship)
- The **significance** a Communication references, and the **escalation ladder** (Stewardship)
- Preferences, sessions, and continuity intent (Continuity)
- Whether outstanding Communications are re-presented as a person moves — the **preference**
  (Continuity)
- Authority, permission, and autonomy level (Operational Trust)
- **Urgency entitlement, interruption authority, audience eligibility, visibility classification, and
  communication retention classification** (Operational Trust)

---

## 5. Hard prohibitions

1. **Concierge must not resolve competing Truths by inventing a fact.** If facts conflict, Truth
   preserves or resolves the conflict. Concierge decides what to do *given* the uncertainty.
2. **Concierge must not select sensors at runtime.** The Primary Authority (or Formula-Derived Fact
   inputs) is declared by Room Configuration (**DL-62**).
3. **Concierge must not runtime-search devices to satisfy a vocabulary term.** Resolution is explicit
   and configured.
4. **Concierge must not grant itself authority.** If Operational Trust returns `prohibited` or
   `undecidable`, Concierge must not act.
5. **Concierge must not treat an identity assertion as a presence fact.**
6. **Concierge must not treat a preference as an instruction.**
7. **Concierge must not treat an obligation as a Communication.** Stewardship states the obligation;
   Concierge decides whether, when, and how to surface it.
8. **Concierge must not promote a learned pattern into autonomous behavior.**
9. **Concierge must not act silently when it cannot explain the action.**
10. **Concierge must not write to another responsibility's system of record.** All state changes occur
    through the owning responsibility's governed interface.
11. **Concierge must not announce merely because it was permitted to act.** Authority to act is not
    authority to announce (**P32**).
12. **Concierge must not infer `Presented` from `Delivered`.** Where a surface cannot attest
    presentation, the outcome is **unknown** and must be reported as such.
13. **Concierge must not fail to deliver silently.** A suppression is recorded with a Decision Trace;
    an undeliverable Communication is recorded and reported.
14. **Concierge must not embed delivery history inside a Communication.** Delivery history is Change
    Records referencing the Communication by Version Identity.
15. **Concierge must not escalate by changing the audience on its own authority.** Changing the
    audience is Stewardship's ladder and Operational Trust's authority. Repeating delivery to the
    same audience is **retry**, and is Concierge's.
16. **Concierge must not treat a category as an interruption entitlement.** Urgency is granted by
    Operational Trust.
17. **Concierge must not assign, approve, reject, or change a Communication's Category.** Category is
    assigned once, by the originating responsibility, from Foundation's closed seven-value enumeration
    (**DL-78**); Concierge consumes it for delivery decisions only.

---

## 6. The orchestration sequence

Concierge must honour the ordering rules in
[../architecture/runtime-sequence.md](../architecture/runtime-sequence.md):

- Context before intent
- Resolution before discovery
- Identity before authorization
- Truth before decision
- Trace always

---

## 7. Permitted outcomes

Concierge always produces exactly one governed outcome, and always produces a Decision Trace.

| Outcome | When |
|---|---|
| Act | Permitted at Autonomous level, with sufficient certainty |
| Propose, then act on confirmation | Permitted at Assisted level, or uncertainty warrants asking |
| Ask for disambiguation | Intent, target, or identity is ambiguous |
| Choose the benign action | Uncertainty is present but a safe subset is clearly permitted |
| Defer | The action is permitted but the moment is suppressed |
| Convey without acting | An obligation or condition warrants awareness only |
| Escalate | An unmet obligation or safety condition requires an authorised person |
| Do nothing, and be able to say why | Prohibited, undecidable, or suppressed |
| Refuse, and explain | Authority denied or consent missing |

**Doing nothing is a decision and is traced.**

### Delivery outcomes

Where the outcome is a Communication, Concierge additionally records the **two-level** outcome model
defined in [../models/communication.md](../models/communication.md):

| Level | States |
|---|---|
| Communication lifecycle | Created, Suppressed, Acknowledged, Expired, Superseded, Resolved by origin, Undeliverable |
| Delivery Attempt outcome | Attempted, Delivered, Presented, Failed |

The two levels are never flattened. A Communication has one current lifecycle state and may have many
Delivery Attempts.

---

## 8. Conflict resolution

Concierge resolves conflicts *among permitted outcomes*. It does not resolve conflicts by weakening
another responsibility's answer.

| Conflict | Concierge may | Concierge may not |
|---|---|---|
| Two facts disagree | Act on the reduced-confidence or unresolved state, or ask | Pick a preferred fact |
| Two people's sessions collide | Ask, defer, or apply a permitted priority rule | Displace a session without authority |
| Two obligations compete | Surface, prioritise by significance within policy | Waive an obligation |
| A preference conflicts with a policy | Follow the policy and explain | Follow the preference |
| Intent is ambiguous | Ask, offering only exposed options | Guess |

The priority hierarchy is recorded in
[../architecture/behavioral-governance.md](../architecture/behavioral-governance.md); its exact global
order is open decision **OD-04**.

---

## 9. What consumers may rely upon

Nothing in the framework depends on Concierge. Residents rely upon Concierge for one coherent
experience across surfaces, and for an explanation of every action and non-action.

---

## 10. Uncertainty and unknown representation

Uncertainty must survive the whole pipeline and reach the resident. Concierge must be able to say:

- "I was not certain it was you."
- "I could not tell whether the room was occupied."
- "I did not do that because the room is in Nighttime mode."
- "The Beam is deliberately not part of *Speakers* in this room."

**Concierge must never conceal uncertainty by acting confidently.**

---

## 11. Failure and degradation behavior

| Condition | Behavior |
|---|---|
| Room Context unresolved | Do not guess a Room; state the context is unknown and ask |
| Identity `unknown` or `ambiguous` | Apply guest-safe treatment; ask for authority-bearing actions |
| Truth `unknown` | Refuse, ask, or choose the benign action; never treat unknown as false |
| Operational Trust unavailable | Fail closed; do not act |
| Continuity unavailable | Do not substitute defaults silently; state what could not be read |
| A governed interface fails mid-action | Report the partial outcome precisely; do not claim success |
| The Decision Trace cannot be written | Treat as a defect and report it |
| No permitted Delivery Surface exists for the audience | Record **Undeliverable** and report it; never fail silently |
| A Delivery Attempt fails at the platform boundary | Record **Failed** with a diagnosable reason; never claim success |
| A surface cannot attest presentation | Record `Presented` as **unknown**; never infer it from `Delivered` |
| An acknowledgement never arrives | Remain **unknown**; never decay into *not acknowledged* |
| Occupancy is `unknown` and the surface is shared | Do not announce; reduce to content-free indication, choose a personal surface, or defer |

Where delivery must degrade, **the delivery degrades — the governance does not.**

See [../architecture/failure-and-degradation.md](../architecture/failure-and-degradation.md).

---

## 12. Privacy constraints

Concierge is the surface where privacy is most easily violated. It must:

- Apply Operational Trust visibility rules before speaking or displaying anything
- Never disclose another person's preferences, presence history, sessions, or obligations
- Never voice sensitive content in a Room where an unauthorised listener may be present
- Never include biometric internals in an explanation
- Evaluate outbound delivery against **who can perceive the surface**, not against the intended
  recipient (**P32**)
- Prefer **content-free indication** followed by identity-gated retrieval where content may not be
  disclosed on the available surface
- Never enumerate on a shared surface **whose** Communications are waiting
- Re-evaluate visibility at **each** Delivery Attempt; never rely on a stored resolved visibility
  value

See [../architecture/privacy.md](../architecture/privacy.md) and
[../models/communication.md](../models/communication.md).

---

## 13. Explainability contributions

Concierge **composes** the Decision Trace from every contributing responsibility and produces both the
machine form and the human form. It authors only the fields it owns: conflicts detected, resolution
applied, action taken, action suppressed, suppression reason, alternative considered.

Concierge additionally contributes the **communication record**: creation, suppression with its
Decision Trace, each Delivery Attempt and its outcome, acknowledgement, expiry, and supersession.
This is what makes *"why didn't you tell me?"* answerable under **P27**.

See [../models/decision-trace.md](../models/decision-trace.md) and
[../models/communication.md](../models/communication.md).

---

## 14. Open decisions

| ID | Question |
|---|---|
| OD-04 | Exact global priority order across policy scopes |
| OD-29 | Where Decision Traces are persisted |
| OD-30 | Which surfaces expose Decision Traces, and to whom |
| OD-43 | Delivery Surface capability model, including perceptibility and attestation |
| OD-44 | Delivery outcome semantics across the two levels |
| OD-45 | Acknowledgement semantics and acknowledger identification |
| OD-47 | Household Inbox projection scope and refresh semantics |
| OD-48 | Re-presentation preference and its relation to the Follow-Me preference family |
| OD-52 | Audience specification model |
| OD-54 | Delivery retry policy — attempts, intervals, surface progression, and give-up semantics |
| OD-55 | Presentation attestation per surface class |
| OD-57 | Indication versus content separation |

### Related documents

- [../scenarios/concierge-use-cases.md](../scenarios/concierge-use-cases.md) — **the twenty canonical Concierge human-outcome use cases**, each with a maturity classification. Architecture and outcome guidance, **not proof of implementation**
- [../architecture/framework.md](../architecture/framework.md)
- [../architecture/runtime-sequence.md](../architecture/runtime-sequence.md)
- [../architecture/privacy.md](../architecture/privacy.md)
- [../architecture/adr-resident-communication-and-delivery-separation.md](../architecture/adr-resident-communication-and-delivery-separation.md)
- [operational-trust-contract.md](operational-trust-contract.md)
- [../models/decision-trace.md](../models/decision-trace.md)
- [../models/communication.md](../models/communication.md)

---
---

# Historical appendix

> **Status: Historical — subordinate to the canonical sections above.**
> This appendix records the pre-refoundation Concierge exploration. It is retained as architectural
> evidence and as a source of preserved discoveries. It is **not** current authority, and it uses
> superseded terminology in places.
>
> Known supersessions in this appendix:
> - "Asset Intelligence exposes asset and environment capabilities" describes a **separate released
>   product**, not an HTBW Core layer. See [../models/asset.md](../models/asset.md).
> - "Interaction space" is superseded by **Room Context**, and "composite room" by **Merged Room**.
>   See [../models/glossary.md](../models/glossary.md).
> - "person-identity-contract.md" is superseded by [identity-contract.md](identity-contract.md).
> - Room posture, quiet-hours, and protected-action authorization are now owned by **Operational
>   Trust**. See [operational-trust-contract.md](operational-trust-contract.md).
> - Auditability and trace stitching are now expressed as the **Decision Trace**. See
>   [../models/decision-trace.md](../models/decision-trace.md).
> - The "Communication Model" section below describes **delivery levels**, not communications. Its
>   Info / Attention / Urgent levels are superseded by the separate **Category** and **Urgency** axes,
>   and its Night Mode and Quiet-Hours rules are now owned by **Operational Trust**. See
>   [../models/communication.md](../models/communication.md) and
>   [operational-trust-contract.md](operational-trust-contract.md).

## Service Interaction Rules

Concierge interacts with other integrations only through services.

Examples:

- Request asset data from Asset Intelligence
- Request environment recommendations
- Trigger updates via service calls

Concierge must:

- Never bypass service boundaries
- Never manipulate internal store structures
- Never assume data formats outside contract definitions

---

## Orchestration Model

Concierge is responsible for:

- Determining what capability is relevant
- Calling the appropriate service
- Combining results if needed
- Presenting the outcome to the user

Concierge must not:

- Reimplement logic already owned by another integration
- Duplicate evaluation rules
- Create conflicting interpretations of system state

---

## Communication Model

> **Superseded.** This section merged *what a communication is about* with *what it may interrupt*,
> and treated delivery levels as communication kinds. The canonical treatment separates **Category**
> (owned by the originator) from **Urgency** (an entitlement granted by Operational Trust), and
> separates the Communication from the Delivery. Night Mode, quiet hours, and room posture are owned
> by **Operational Trust**. See [../models/communication.md](../models/communication.md).

Concierge controls all communication using defined levels:

### Info
- Visual only
- No interruption

### Attention
- Visual plus optional voice
- Non-urgent

### Urgent
- Immediate voice
- Interruptive if required

### Night Mode
- Night behavior is determined by effective room posture
- In night posture, suppress all except urgent
- Global configuration may define the default night behavior, but rooms control the effective mode

### Quiet-Hours and Room Posture
- Quiet-hours is configured concierge-wide and defines the default suppression window
- Room posture remains room-wide and may increase suppression for that room at any time (for example: naps or early bedtime)
- Room posture overrides floor and concierge defaults for that room only
- Urgent delivery follows explicit global urgent bypass policy

---

## Scope Model

Concierge configuration is layered:

1. concierge-wide
2. floor-wide
3. room-wide

Effective resolution uses most-specific valid scope:

- room override
- else floor default
- else concierge default

This scope model must be used for communication behavior, execution target routing, and media/climate defaults.

Merged rooms (composites) are valid room-context targets and must route deterministically from any member area.

---

## Floor-Level Infrastructure Boundaries

Some capabilities are shared at floor scope and should not default to room scope.

Examples:

- thermostats and HVAC zone entities
- floor speaker groups
- floor media routing defaults

Room-level overrides remain allowed for explicit exceptions.

---

## Context Awareness

Concierge must be aware of:

- Room context (area)
- Available integrations and capabilities
- Active modes and posture (guest mode, room night posture, sleep posture, etc.)
- User intent (explicit or inferred)

Context must be:

- deterministic
- derived from system state
- not inferred unpredictably

For mobile endpoints, context resolution should fuse person-linked mobile device identity with room presence signals (for example BLE and supporting room presence devices).

---

## Person-Aware Interaction Boundaries

Concierge may apply person context to communication style.

Examples:

- concise responses for direct-style users
- richer detail for conversational-style users

Person-aware behavior must follow these rules:

- identity context may change delivery style
- identity context must not change foundational truth
- identity context must not bypass safety confirmation rules
- low-confidence identity must degrade to neutral style

Person-aware behavior must remain explainable and reversible.

Enrollment and consent rules are defined in person-identity-contract.md.

---

## Mobile Interaction Plane

Mobile voice and mobile typed requests are one interaction plane with different input modality.

Rules:

- both modalities must use the same intent and service path
- person resolution may use mobile endpoint identity when configured
- room resolution may use BLE and supporting room presence context with explicit confidence
- low-confidence room resolution must trigger concise clarification instead of hidden guessing

Informational room-context intents (for example "what art is in this room") are allowed with medium confidence and must return explainable room attribution.

---

## Protected Action Authorization Boundary

Concierge may orchestrate protected actions, such as alarm control, only when authorization policy is satisfied.

Rules:

- global policy defines alarm connection and allowed control modes
- person profile grants define who may control alarm actions
- voice attribution may contribute to authorization context but must not be the sole disarm authority
- disarm actions should require step-up confirmation when enabled by policy
- preferred step-up for disarm is a Home Assistant mobile push confirmation to the authorized person
- PIN (or equivalent secure unlock) should be required for mobile disarm confirmation when policy requires it
- all protected-action allow and deny decisions must be auditable

---

## Multi-Assistant Responder Responsibility

When multiple voice assistants hear the same request, Concierge must coordinate a single responder outcome.

Concierge must:

- evaluate room context and interaction space
- evaluate person-aware context when available
- elect one primary responder
- suppress duplicate responses
- preserve active conversation ownership where possible

This behavior must remain deterministic and explainable.

---

## AI Usage Rules

Concierge may use AI to assist with:

- natural language understanding
- summarization
- recommendation requests (delegated to integrations)

Concierge must not:

- allow AI to directly mutate system state
- make decisions that bypass contracts
- produce outputs that cannot be explained

All AI usage must:

- be bounded
- reference system data
- produce explainable results

---

## Capability Model

Concierge operates on capabilities exposed by integrations.

Examples:

- Asset Intelligence exposes asset and environment capabilities
- Future integrations may expose additional capabilities

Concierge must:

- discover available capabilities at startup or configuration time
- adapt behavior based on what is available
- avoid hard dependencies where possible

Discovery is allowed at startup or configuration time. Runtime must use precomputed results only.

---

## Global Context and Signal Integration

Concierge may orchestrate capabilities that represent whole-home context and household signals.

These include:

- Informational context (weather, time, news)
- Stateful signals (calendar, shopping list, appliance states, reminders)

These capabilities:

- Are owned and exposed by other integrations
- Must be accessed only via defined service interfaces
- Must not be stored or evaluated by Concierge

Concierge is responsible for:

- Determining when these signals are relevant to the user
- Routing requests to the appropriate integration
- Combining signal data into meaningful responses
- Delivering responses in a context-aware manner (room, time, mode)

Concierge must not:

- Directly interpret raw sensor or entity data
- Maintain independent copies of signal state
- Create conflicting representations of household state

---

## Failure Handling

Concierge must degrade gracefully when:

- required integrations are unavailable
- data is incomplete
- services fail

In these cases, Concierge should:

- provide a clear response
- avoid partial or misleading outputs
- never fabricate data

---

## Auditability And Trace Stitching

Concierge must provide an auditable orchestration trail without duplicating full logs already owned by other systems.

Rules:

- Concierge audit records are orchestration metadata, not full copies of provider logs
- each activity must include correlation identifiers that link to source logs (voice, service calls, automations, notifications)
- each activity must include outcome (success, partial, denied, failed, canceled)
- each activity must include explainable decision summary and policy gates used
- protected-action decisions must include allow or deny reason codes

Guest audit minimization policy:

- unknown interactions must be labeled as guest-unlinked
- guest audit records should store intent_class and outcome with timestamp as the primary retained fields
- guest records should avoid stable identity linkage unless required by safety or legal policy
- guest mobile push/device targeting is unsupported unless the device is explicitly linked to a known person profile

Minor audit minimization policy:

- when a matched profile is marked as minor, audit records should retain intent_class, outcome, and timestamp as primary fields
- request_summary and stitched reference excerpts should be minimized by default for minor records
- minor records should follow stricter retention policy than default household retention when configured

Offline archive rule:

- when exporting to offline storage (for example NAS), Concierge must generate a self-contained readable activity archive
- the archive may include normalized excerpts and references needed for human-readable reconstruction
- the archive must avoid storing full duplicated raw logs when references and concise excerpts are sufficient
- archive exports must be immutable, timestamped, and retention-policy governed
- archive destination connection settings must be configured in global integration options, not room/person operational UI

---

## System Behavior Rules

Concierge must:

- prioritize clarity over complexity
- prioritize usefulness over completeness
- only speak when necessary
- avoid repetition and noise

Concierge must never:

- overwhelm the user
- act without explanation
- assume data it does not have
- bypass validation in other integrations

---

## V2 Governance Consumption

This contract is consumed under E0 governance authority and must align with:

- ADR-004 Coordinator V2 Governance Boundaries
- ADR-005 Room Vocabulary Governance Boundaries
- ADR-006 Capability Projection Governance Boundaries
- ADR-007 Experience Model Governance Boundaries
- ADR-008 Personalization Governance Boundaries
- ADR-009 Household Memory Governance Boundaries
- ADR-010 Household Productivity Experience Governance Boundaries
- ADR-011 Provenance Governance Boundaries
- ADR-012 Occupancy and Presence Governance Boundaries
- ADR-013 Concierge V1 Household-Facing Outcome Preservation Governance
- HACS and Platinum Governance Standard

This contract consumes governance.

This contract does not redefine governance.

---

## Ownership Boundary Validation

Ownership constraints for this contract:

- Foundation remains authoritative for room, area, device, occupancy, and environmental truth
- Voice Identity remains authoritative for attribution and confidence outputs
- Asset Intelligence remains authoritative for significance and environmental interpretation outcomes
- Concierge Coordinator V2 remains orchestration-only and does not become a system of record

---

## Terminology Alignment

Canonical terms used by this contract:

- Room
- Area
- Floor
- Composite Room
- Capability
- Experience
- Personalization
- Household Memory
- Provenance
- Occupancy
- Presence
- Attribution
- Confidence
- Context
- Scope

Obsolete V1-only ownership assumptions are out of scope for this contract.

---

## Final Principle

Concierge orchestrates understanding.

If a feature involves:

- communication
- interaction
- coordination across integrations

It belongs in Concierge.

If it involves:

- data ownership
- evaluation logic
- persistence

It does not belong in Concierge.