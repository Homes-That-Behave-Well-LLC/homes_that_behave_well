# HTBW Canonical Principles

> **Document status: Canonical (constitutional).**
> Subordinate only to [north-star.md](north-star.md).
> Terminology: [docs/models/glossary.md](../models/glossary.md).

These principles govern every HTBW document, contract, model, assessment, and future
implementation. A document that violates a principle is wrong, regardless of age.

---

## Responsibility principles

**P1. Every responsibility needs an owner.**
If no responsibility owns a behavior, the behavior is undefined and will be invented at runtime.

**P2. Framework layers define responsibility boundaries, not products.**
A layer is not a separate navigation entry, a separate installation, or a separately released
integration. It is a boundary of ownership.

**P3. Layers communicate through explicit contracts.**
See [../contracts/README.md](../contracts/README.md).

**P4. No layer may quietly assume a responsibility owned by another layer.**
Assuming another layer's responsibility is a defect even when the outcome looks correct.

---

## State-separation principles

**P5. Asset existence does not imply room participation.**

**P6. Room participation does not imply resident exposure.**

**P7. Resident exposure does not imply permission to act.**

**P32. Permission to act does not imply permission to announce.**

Authority to perform an action does not confer authority to speak about it, display it, or draw
attention to it in the presence of whoever happens to be there.

Outbound communication is governed by the same Existence → Participation → Exposure → Authority
chain as any other disclosure, evaluated against **who can perceive the delivery surface**, not
against who requested something.

Where context cannot be established with sufficient confidence to deliver safely, **the delivery
degrades — the governance does not.**

See [../models/communication.md](../models/communication.md) and [privacy.md](privacy.md).

These four states — Existence, Participation, Exposure, Authority — are defined in
[../models/room-configuration.md](../models/room-configuration.md) and must never be conflated.
P32 extends the same chain to the inverted case, in which the home speaks unprompted and the audience
is chosen by no requester.

---

## Knowledge principles

**P8. Evidence is not Truth.**
Evidence is an input. Truth is an authoritative, governed conclusion. See
[../models/truth.md](../models/truth.md).

**P9. Identity assertions are not automatically contextual Truth.**
"We believe this is Tom" is not the same fact as "Tom is present in the Den."

**P10. Preferences are not facts.**
A preference states what someone wants. A fact states what is.

**P11. Obligations are not actions.**
An unmet obligation is a condition, not an instruction to act.

**P12. Policies are not decisions.**
A policy defines what is permitted. A decision selects what happens.

---

## Orchestration principles

**P13. Concierge orchestrates. It does not become the system of record for everything it consumes.**

**P14. Important mappings are explicitly configured rather than guessed through hidden runtime discovery.**
Room participation, vocabulary targets, speaker sets, and composite-fact inputs are configured and
persisted. See [../models/contextual-vocabulary.md](../models/contextual-vocabulary.md).

**P15. Uncertainty must remain visible. It must not be converted into false certainty.**
See [failure-and-degradation.md](failure-and-degradation.md).

**P16. A well-behaved home must be able to explain both actions and intentional non-actions.**
See [explainability.md](explainability.md).

---

## Durability principles

**P17. Architecture lasts longer than technology.**
Contracts and models are written against household concepts, not vendor primitives.

**P18. Separate responsibilities must produce a unified household experience.**
Residents must never be asked to understand the framework in order to use the home.

---

## Trust principles

**P19. Operational Trust and Human Trust are different.**

| | Question | Nature |
|---|---|---|
| Operational Trust | What is allowed? | A governed responsibility with policies, roles, and authority |
| Human Trust | Can people rely on the environment? | An **outcome** of understandable, consistent, respectful, reliable behavior |

Human Trust is never implemented. It is earned. See [explainability.md](explainability.md).

**P20. Behavioral Governance is cross-cutting architecture and policy documentation.**
It is not automatically a new North-Star framework layer. See
[behavioral-governance.md](behavioral-governance.md).

---

## Platform principles

**P21. Home Assistant First.**

HTBW extends Home Assistant. HTBW does not compete with Home Assistant.

Before introducing any new model, storage mechanism, workflow, configuration system, UI concept,
registry, or architectural construct:

1. Review official Home Assistant documentation.
2. Review official Home Assistant developer documentation.
3. Review official Assist and Voice Assistant documentation.
4. Determine whether Home Assistant already provides a documented pattern.

Prefer Home Assistant primitives whenever they appropriately represent the requirement: Areas,
Devices, Entities, People, Labels, Floors, Calendars, Assist, Config Flows.

An HTBW extension is justified only when Home Assistant cannot practically represent the required
information. See [home-assistant-boundary.md](home-assistant-boundary.md).

**The burden of proof is ordered.** Each layer must be evaluated, and shown insufficient, before the
next is considered:

| # | Layer | Question |
|---|---|---|
| 1 | **Native Home Assistant capability** | Does a documented native capability satisfy the requirement? |
| 2 | **An existing maintained integration or ecosystem capability** | Does a maintained integration or established ecosystem capability satisfy it? |
| 3 | **An HTBW extension that governs, explains, coordinates, or constrains a native capability** | Can the requirement be met by governing what already exists, rather than by building alongside it? |
| 4 | **A new HTBW capability** | Only when 1 through 3 have each been evaluated and recorded as insufficient. |

A step is passed only when the evaluation **records**:

1. the documented capability that was evaluated,
2. the source documentation used,
3. the HTBW constitutional requirement being tested,
4. the gap that remains after the native or existing capability is applied,
5. and why the lower architectural layer cannot practically satisfy that gap.

> **An undocumented evaluation does not discharge the burden of proof.**
>
> **If the relevant technical documentation cannot be verified, the burden is not discharged and the
> decision remains open.**

The durable record of these evaluations is the **Platform Capability Review** in
[home-assistant-boundary.md](home-assistant-boundary.md). The accepted statement of the burden of
proof is **DL-30** in [../governance/decision-ledger.md](../governance/decision-ledger.md).

**P22. Connected Storage.**

When information cannot be practically represented in Home Assistant-native storage models, HTBW
may use connected storage — and every connected-storage record must maintain traceability back to
its Home Assistant system-of-record object. See [connected-storage.md](connected-storage.md).

**P23. Native Experience.**

HTBW should feel like Home Assistant. Prefer HA navigation patterns, dialogs, selectors, forms,
configuration flows, and interaction conventions.

Residents should feel *"this is Home Assistant enhanced by HTBW,"* not *"this is a separate
application."*

**P24. Greenfield without compatibility debt.**

HTBW Core is greenfield. Backward, API, schema, data-model, and implementation compatibility are
not required. Proven ideas are preserved; obsolete boundaries are not. See
[greenfield-mandate.md](greenfield-mandate.md).

> **Annotated 2026-11-10 by DL-153.** "HTBW Core" is now **BehavesWell Core**. P24 concerns
> compatibility with **predecessor products**; it does not prohibit protecting BehavesWell Core's own
> installed persisted identifiers (`htbw` and the others listed in DL-153).

**P25. Vendor-agnostic framework, vendor-specific implementation.**

The framework must be able to assess homes built on platforms other than Home Assistant, even
though the reference implementation is Home Assistant-native.

---

## Configured versus learned behavior

**P26. An observed pattern must not silently become an autonomous policy.**

These are distinct and must be distinguishable in the model:

| Kind | Example |
|---|---|
| Explicitly configured fact source | "These three sensors contribute to Living Space temperature." |
| Explicitly configured preference | "Tom selected Jazz as his default music." |
| Explicitly configured policy | "Nighttime mode prevents incoming audio." |
| Explicit human instruction | "Have the music follow me." |
| Observed pattern | "The home observed that Tom often listens to Jazz." |
| Suggested preference | "Would you like Jazz to be your default?" |
| Approved learned preference | Tom accepted the suggestion. |
| Autonomous behavior | The home acts without asking, within an approved ceiling. |

Learning may support suggestions. Promotion of a learned behavior to an active preference or policy
must pass through Operational Trust, consent, and explainability requirements.

---

## Temporal principles

These four principles extend the framework across time. They are governed by
[adr-historical-explainability-and-historical-truth.md](adr-historical-explainability-and-historical-truth.md)
and [adr-temporal-record-model.md](adr-temporal-record-model.md).

**P27. Historical explainability is an architectural requirement.**

The home must retain enough governed information to reconstruct what it observed, what it believed,
what it knew, what it decided, why it decided so, and why the alternatives were rejected. This
applies to a single decision, a time range, an incident retrieval scope, a Room, a Merged Room, an
Asset, and a Person.

**Explainability has a temporal dimension. Retention is a floor as well as a ceiling.** Privacy
minimization bounds how long information may be kept. Historical Explainability bounds how little
may be kept.

Where privacy requires removal or redaction, the resulting limitation must itself remain explainable,
so the home can state *"I no longer hold that record."* No record may be silently discarded where the
architecture requires a governed deletion, purge, redaction, or truncation marker.

Reconstruction is performed from governed temporal records, not from mandatory comparison of retained
full payloads. A home that must compare arbitrary complete archives to explain itself has recorded
the wrong thing.

See [explainability.md](explainability.md), [privacy.md](privacy.md), and
[../models/temporal-record.md](../models/temporal-record.md).

**P28. Truth is the system of record for both present and historical Facts.**

Operational expiration removes a Fact from *what is true now*. It does not automatically delete *what
was true then*. Historical Facts retain governed information sufficient for explainability, audit,
reconstruction, and accountability — and, where policy permits, the Subject, Statement, confidence at
the time, Provenance, evidence references or evidence classes, Coverage, Freshness, and lifecycle
transitions.

Eight Fact lifecycle transitions must each be separately reconstructable: **established**,
**confirmed**, **confidence changed**, **superseded**, **withdrawn**, **operationally expired**,
**became unknown**, **became unresolved**.

A Historical Fact is never presented as current, is never actionable, must not silently become
current again, and is not a retained raw evidence payload.

**Truth owns Fact history. No consumer may maintain a competing or re-derived Fact history.**

See [../models/truth.md](../models/truth.md) and
[../contracts/truth-contract.md](../contracts/truth-contract.md).

**P29. History is recorded as change, not as repeated copies.**

A governed record has a **Current Projection** answering what is true or configured now. Its history
consists of immutable **Change Records** and **Domain Events**, accelerated where useful by
**Snapshots**.

Normal operation reads Current Projections. Historical reconstruction uses the nearest valid Snapshot
and the subsequent Change Records. **HTBW must not require comparison of complete stored payloads to
discover what changed.**

At the moment of a governed change, the record must be able to answer: what changed, when it became
effective, when it was recorded, who or what changed it, why it changed, which prior version it
replaced, and which new version became effective.

A Snapshot is an accelerator, not an independent source of truth. A Snapshot must not rewrite
history, replace provenance, reinstate content removed through privacy policy, or hide historical
gaps.

This principle governs the **model**, never the **store**. It selects no storage technology, no
serialization format, no snapshot frequency, and no per-responsibility persistence choice.

See [../models/temporal-record.md](../models/temporal-record.md).

**P30. Governed records reference exact versions rather than copying payloads.**

A record depending on another responsibility's output references the exact version of that governed
record. Where durable human readability requires it, a minimal immutable explanation projection may
be retained beside the reference; it must not become a wholesale copy.

A Decision Trace references exact versions of Truth Facts, Identity Assertions, Operational Trust
policies and decisions, Stewardship obligations, Continuity preferences and sessions, Room
Configuration, Contextual Vocabulary mappings, and explicit human requests.

**An explanation must remain accurate after current configuration or policy changes.** A reference
transfers no ownership. A reference permits no re-derivation.

**A dangling or unresolved reference must be reported, never silently rendered as though the source
record never existed.**

See [../models/decision-trace.md](../models/decision-trace.md).

---

## Communication principles

These principles govern how the home conveys things to residents. They are governed by
[adr-resident-communication-and-delivery-separation.md](adr-resident-communication-and-delivery-separation.md).

**P31. Communication is separate from delivery.**

A **Communication** is a household interaction. It exists independently of the mechanism used to
convey it.

**The responsibility that originates a Communication does not select how it is delivered.**
Origination establishes that something must be conveyed, to whom, and about what. Delivery
establishes through which surface, at what moment, in what form, and whether at all.

A Communication must never be defined as a notification, a push message, an announcement, an
indicator, or any other transport artifact. Those are delivery outcomes.

This principle governs the **model**, never the **surface**. It selects no delivery technology, no
surface catalogue, no indicator scheme, and no escalation ladder.

See [../models/communication.md](../models/communication.md).

**P32** is stated with the state-separation principles above, because its placement is part of its
meaning.

---

## Related documents

- [north-star.md](north-star.md)
- [framework.md](framework.md)
- [../governance/authority-order.md](../governance/authority-order.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
