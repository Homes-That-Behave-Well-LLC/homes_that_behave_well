# Temporal Record Model

> **Document status: Active — Canonical model.**
> Terminology: [glossary.md](glossary.md). Owning responsibility: **Foundation**.
> Governed by **P29** and **P30** in [../architecture/principles.md](../architecture/principles.md).

---

## Purpose

Foundation defines the shared temporal, version, change-record, snapshot, correlation, and
provenance models that every other responsibility uses to record its own history.

**Foundation defines the shared temporal model. Foundation does not own the histories produced by
other responsibilities.** Truth owns Fact history. Stewardship owns obligation history. Concierge
owns decision history. Foundation owns none of them, in exactly the way Foundation defines what a
*Fact* is without deciding what is factual now.

This model creates **no new responsibility**. It defines shared object types, in the same way
[room-configuration.md](room-configuration.md) defines a Foundation-owned model without becoming a
responsibility of its own.

## Question answered

*How does the home record what changed, so that it can account for itself across time?*

---

## The record kinds

| Kind | Question it answers | Mutability | Owner |
|---|---|---|---|
| **Current Projection** | What is true or configured now? | Mutable; replaced | The owning responsibility |
| **Change Record** | What changed, when, why, by whom, from which version to which? | Immutable once recorded | The responsibility owning the changed record |
| **Domain Event** | What meaningful occurrence happened in the household? | Immutable once recorded | The responsibility that observed it |
| **Snapshot** | What was the governed state at a point in time? | Immutable; derivable | The owning responsibility |
| **Decision Trace** | Why did Concierge act, ask, defer, suppress, refuse, or take no action? | Immutable | Concierge |

Three connective constructs are **not** record kinds:

| Construct | What it is |
|---|---|
| **Governed Reference** | An immutable pointer to an exact version of a record |
| **Version Identity** | The identity by which an exact state of a governed record is addressed |
| **Preservation Hold** | A policy marker protecting records from normal removal |

Two constructs are **projections**, never stores and never a source of truth:

| Construct | What it is |
|---|---|
| **Historical Reconstruction** | A state or timeline assembled on demand from governed records |
| **Evidence Package** | A governed assembly of records for a stated scope, produced on demand |

---

## Current Projection

- Answers *what is true or configured now*.
- Is optimised for runtime consumption.
- Is owned by the relevant responsibility.
- **Must not require replay of complete history during normal operation.**

Every responsibility maintains or exposes a Current Projection. Representative projections:

| Responsibility | Current Projection |
|---|---|
| Room Configuration (Foundation) | Current Room and Merged Room membership, participation, exposure, vocabulary, voice-assistant assignment, Composite Fact contributors |
| Identity | Current Identity Assertions and current consent state |
| Truth | Current authoritative Facts |
| Stewardship | Current obligations and their state |
| Continuity | Current preferences and active sessions |
| Operational Trust | Current policies, thresholds, ceilings, retention classifications |

**Historical records must not become the normal runtime query path.** If runtime operation must
replay all history to determine current state, the implementation has failed its contract.

> **The Current Projection is authoritative for the present. The historical record is authoritative
> for the past. A mismatch between them is a defect, not a judgement call.**

---

## Change Record

A Change Record answers *what changed*.

- It is **immutable once recorded**, except for governed redaction or deletion treatment.
- It references the **prior version** and the **new version** of the changed record.
- It is owned by the responsibility that owns the changed record.

### Constitutionally required

| Element | Why it is required |
|---|---|
| Record ID | Without identity a change cannot be referenced, held, or tombstoned |
| Subject ID | Required for Room, Merged Room, Asset, Person, obligation, and session retrieval |
| Subject Type | The same identifier may exist in more than one subject space |
| Owning Responsibility | **P1.** Every record has exactly one owner |
| Change Type | Distinguishes creation, amendment, supersession, withdrawal, expiry, and removal |
| Effective Timestamp | When the change took effect in the household |
| Recorded Timestamp | When HTBW recorded it |
| Actor or Initiating Process | *Who or what changed it* is a required answer |
| Prior Version Reference | Without it, "what was the prior value" requires payload comparison |
| New Version Reference | Without it, a Decision Trace cannot cite the version it used |
| Changed Fields | The minimum that makes *what changed* answerable without comparison |
| Provenance | Already required of every Fact; extended to every governed change |
| Privacy Classification | Required for field-level redaction |
| Retention Classification | Carries the retention floor and ceiling onto the record itself |

### Constitutionally required in existence; implementation format open

| Element | Open decision |
|---|---|
| Correlation linkage | **OD-38** |
| Causation linkage | **OD-38** |
| Preservation-hold discoverability | **OD-39** |
| Reason or source | Encoding open; reason codes already exist in the Decision Trace and should be reused rather than reinvented |

### Conditionally recordable, subject to privacy policy

| Element | Condition |
|---|---|
| Previous values | Recordable where the privacy classification of the field permits |
| New values | Recordable where the privacy classification of the field permits |

**This model does not specify** identifier encoding, database columns, JSON schema, database
technology, or storage technology. Those are implementation decisions — **OD-01**, **OD-38**.

### Compacting large collection changes

Where a change affects a large collection and a compact representation remains adequate for
explanation, a Change Record may record counts and deltas rather than copying the complete
collection. This preserves a useful pattern proven in the Asset Intelligence reference
implementation. It is a permitted representation, never a licence to omit the fact that a change
occurred.

---

## Domain Event

A Domain Event represents a **meaningful occurrence in the household**.

Representative Domain Events: a door opened; occupancy established; an Identity Assertion created;
an obligation became unmet; a session transfer requested; a room transition observed.

### Domain Event versus Change Record

> **A Domain Event is something that happened in the household.**
> **A Change Record is something that happened to a governed record.**

| Occurrence | Domain Event | Change Record |
|---|---|---|
| A door opened | Yes | No — no governed record changed |
| A vocabulary term was edited | No — nothing happened in the household | Yes |
| Occupancy became established | Yes — observed by Truth | Yes — against the Fact lifecycle |

A Domain Event may cause one or more Change Records. It is not itself a Change Record.

**Do not collapse Domain Events and Change Records into one generic event type.** Collapsing them is
what produced the sprawl in the superseded event model. The superseded
[event-model.md](event-model.md) and
[../architecture/adr-household-memory-governance.md](../architecture/adr-household-memory-governance.md)
remain Historical. **Their former ownership boundaries are not revived by this model.**

### Behaviour attribution

A Domain Event may record **what caused the occurrence**, where evidence supports it. This is the
HTBW record of *what happened in the household, and what is known to have brought it about*. It is
where behaviour attribution lives. **It does not require, and must not become, a separate Activity
model, Activity responsibility, or Activity store.**

> **Attribution is not reasoning.** Naming what brought an occurrence about is not the same as
> recording why a governed decision was reached. That remains the **Decision Trace**, and only
> Concierge produces it.

Distinguishable behaviour sources, where the evidence permits:

| Source | Established by |
|---|---|
| Direct resident interaction | An attributable platform user, or an Identity Assertion meeting the required confidence threshold |
| A native Home Assistant automation | Platform-supplied execution evidence |
| A native script | Platform-supplied execution evidence |
| A scene activation | Platform-supplied execution evidence |
| Manual physical interaction with a device | Device or integration reporting, where the integration documents it; otherwise graded **Probable Source** below |
| An external, non-autonomous integration | The source integration, where identifiable |
| **Unknown or unattributed** | Nothing — and this is recorded honestly |

> **Do not force attribution where evidence is absent.** *Unattributed* is a valid, first-class
> outcome. An invented cause is worse than an acknowledged gap.

### Decision Authority (DL-73)

**An HTBW-governed decision, an HTBW learned or adaptive policy, an external autonomous policy
engine, and a reasoning-provider recommendation are Decision Authorities, not Behaviour Sources.**
They answer *why* a decision was made, never *what initiated* the occurrence:

| Decision Authority | Established by |
|---|---|
| An HTBW-governed decision | The Decision Trace |
| An HTBW learned or adaptive policy | The approved policy version, and the Decision Trace |
| Asset Intelligence | Its own significance evaluation (representative example, not an exhaustive list) |
| Stewardship | Its own obligation determination |
| Continuity | A restored preference it supplied |
| Concierge | A household-decision evaluation it assembled |
| An external autonomous policy engine | A declared delegation boundary (**OD-66**) |
| A reasoning-provider recommendation | The consultation record, and the decision that accepted it |

**HTBW Attribution applies in both directions**: to activities HTBW merely observes within Home
Assistant, and to activities HTBW itself decides and executes through Home Assistant. In the second
case, the resulting Domain Event's Decision Authority attribution **references** the Decision Trace
that produced it — the two record kinds are never merged, and a Decision Trace still exists only
where HTBW decided.

### Source Confidence (DL-73)

Each attributed Behaviour Source carries exactly one of three tiers, structurally distinct from
**DL-39** Identity confidence and **DL-58** Truth confidence, and never reused by **OD-72**'s
unknown-actor correlation work:

| Tier | Established by |
|---|---|
| **Known Source** | Direct evidence — a same-context-id sibling execution event (a `call_service` or `automation_triggered` event sharing the occurrence's own context), or a `context_user_id` matching an authenticated platform user |
| **Probable Source** | Evidence-supported inference — a root-context occurrence with no competing source evidence, consistent with a documented, **per-integration-verified** (**DL-30**) device behaviour pattern — for example a physical wall-switch or dimmer interaction on an entity-backed device under a Local-Push integration independently verified to emit no distinct interaction event for that device class |
| **Unknown Source** | Insufficient evidence — the honest, sufficient, final answer wherever neither tier is met |

**Alternative-explanation handling (DL-73)**: where no candidate source meets the Known Source or
Probable Source threshold, the attribution is **Unknown Source**. HTBW **never presents competing
source theories as parallel explainability outputs** — it does not return "Candidate A / Candidate B
/ Candidate C" as alternatives; it returns the single best-supportable attribution, or Unknown Source
where none reaches threshold. **A recurring Unknown Source pattern is itself governance evidence**:
it may indicate missing telemetry, missing integration support, a new Behaviour Source category, a
new Decision Authority category, or an unsupported attribution pattern. Unknown Source is therefore
both a valid explainability result and a governance discovery mechanism.

**Decision Authority is a separate, formally distinct concept** (**DL-73**): Source answers *"what
initiated this"*; Decision Authority answers *"why was the decision made"* — which responsibility,
configured policy, or reasoning process determined the outcome; Execution remains a third, already-
distinct concept (what Home Assistant or another authorized environment actually did). **The three
are never collapsed.**

**Canonical Explainability Chain (DL-73)**: **Actor → Source → Decision Authority → Execution →
Outcome → Explanation** — a sequencing clarification over already-accepted architecture. The
preferred explainability hierarchy is **Decision Authority, else Source, else the originating
integration, else Unknown**, applied only where the Decision Trace's own evidence supports the richer
explanation; **Unknown remains fully valid wherever it does not.**

### Person Attribution (DL-73)

**Attributing an occurrence to a person is bounded by Identity.** It relies on Identity's assertion
and confidence, and **never establishes an identification of its own**. Person Attribution carries
exactly three states: **Known Person** (a `known` Identity Assertion exists); **Unknown Person** (a
person may have been involved but Identity cannot determine who — **DL-33**'s existing `unknown`
state, unchanged); **No Person** (no person participated in the decision at all — the attributed
Decision Authority or Source is itself non-person: Asset Intelligence, Stewardship, Continuity, a
schedule, or an automation may all result in No Person). **No Person is not a fourth Identity
state** — it is the attribution-layer statement that Identity was never invoked for this occurrence.
Where confidence is insufficient for a person, the occurrence is recorded without one. A source
classification also **does not mean HTBW owns that source**: naming an automation, an integration, or
an external policy engine identifies a participant, not a possession. **Guest remains a trust-and-
permissions construct, never an attribution state**; an Unknown Person may receive Guest-equivalent
permissions through Operational Trust without creating any Identity Assertion binding the two
(**DL-33**, **DL-71**).

**Revision is additive**: a later observation may improve an attribution's tier or supply a Decision
Authority where none was previously known, but the original record is never rewritten — inherited
from the existing Change Record immutability discipline (**DL-26**, **DL-27**) and **DL-35**'s
identical rule for the structurally analogous Unknown Actor Reference. No new revision mechanism is
created for attribution specifically.

Attribution **references** native objects; it does not copy them (**P30**). The enumeration, the
evidence thresholds, and the confidence representation are **resolved as OD-63 / DL-73**; the
platform-supplied evidence model is **OD-64**; correlation identifiers remain **OD-38**.

**A Domain Event is not a Decision Trace.** It records that something occurred. Only Concierge
records why HTBW decided. **A Domain Event and a Decision Trace are not interchangeable.**

---

## Snapshot

A Snapshot represents governed state at a point in time, for a bounded scope.

| Requirement | Statement |
|---|---|
| Identifies contents | A Snapshot identifies the exact record versions it includes |
| Identifies its boundary | A Snapshot identifies the last-applied Change Records |
| Preserves provenance | A Snapshot retains or references the required provenance |
| Never rewrites history | A Snapshot does not alter or supersede the Change Records it summarises |
| Never replaces Change Records | A Snapshot accelerates reconstruction; it does not stand in for the record of change |
| Honours later policy | A Snapshot must honour subsequent redaction and deletion |
| Never reinstates removed content | A Snapshot must not reintroduce content removed under privacy policy |
| Never hides a gap | A Snapshot that spans a period with missing records reports the gap |

> **A Snapshot is an accelerator. A Snapshot is not an independent source of truth.**

A Snapshot may be triggered by time interval, change threshold, lifecycle transition, Preservation
Hold, incident boundary, export request, or implementation policy.

**Snapshot triggers, cadence, and scope remain open — OD-37.** Snapshot **retention** is settled by
**DL-47**: a Snapshot is an accelerator and is retained no longer than the records it summarises.
Format and encoding are implementation mapping.

Each responsibility snapshots its own scope. **There is no central snapshot owner.**

---

## Decision Trace

The Decision Trace explains a Concierge evaluation. It covers action, non-action, suppression,
deferment, refusal, question, and suggestion alike.

- It **references exact source versions** rather than copying complete source payloads (**P30**).
- It may retain a **minimal immutable explanation projection** where durable human readability
  requires it.

The full structure is defined in [decision-trace.md](decision-trace.md).

---

## Governed Reference

A Governed Reference points to an **exact version** of a governed record.

| Rule | Statement |
|---|---|
| Points to a version | Not to the mutable object |
| Transfers no ownership | Referencing a Fact does not make the referrer a producer of Facts |
| Permits no re-derivation | A reference is not permission to recompute another responsibility's output |
| Must resolve, or say why not | A reference resolves, or is explicitly identified as unavailable |

> **A dangling or unresolved reference must be reported. It must never be silently rendered as
> though the source record never existed.**

Where a referenced native Home Assistant row has been purged, the Governed Reference resolves to an
explicit state such as *"no longer retained"* — never *"never existed."* See
[../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md).

---

## Version Identity

Every governed record carries a **Version Identity**. Every Change Record names the prior version
and the new version. Every dependent record references **versions, not objects**.

This is what makes historical explanation durable. Without Version Identity, a Decision Trace must
copy its inputs into itself, which is full-payload history under another name. With it, the trace
stays small **and** stays exact.

The identifier scheme — including whether Home Assistant context identifiers are adopted — is
**OD-38**.

---

## Bitemporality

Two timestamps are constitutional.

| Timestamp | Meaning | Why required |
|---|---|---|
| **Effective Time** | When the change took effect in the household | Late-arriving evidence; retrospective correction |
| **Recorded Time** | When HTBW recorded it | Audit integrity; separating *what we knew then* from *what we know now* |

**A correction must not overwrite prior history.** A correction is a **new Change Record** carrying:

- Its own Recorded Time
- The corrected Effective Time
- Provenance
- Reason
- Prior and new version references

This preserves what was believed at the time, what was learned later, and when the correction was
recorded. It is the mechanism by which
[../architecture/failure-and-degradation.md](../architecture/failure-and-degradation.md)'s rule
*"do not retroactively invent a transition — record the gap"* becomes enforceable rather than merely
stated.

---

## Historical Reconstruction

Historical Reconstruction is a **projection**. It is not a store, and it is not a source of truth.
It is assembled from existing governed records.

### Reconstruction rule

> **State at time T is reconstructed from the nearest valid Snapshot at or before T, plus the
> subsequent Change Records applied in Effective Time order.**

- Where no Snapshot exists, reconstruction begins from record creation.
- Where records have been purged, redacted, deleted, or are otherwise unavailable, reconstruction
  **reports the gap**, identifies the reason where known, does **not** fabricate the missing state,
  and does **not** silently close the gap.

**A reconstruction containing an unreported gap is a defect.**

Reconstruction reports only what the governed records support. It must not speculate, and it must
not convert missing history into certainty. This is
[../architecture/principles.md](../architecture/principles.md) **P15** applied across time.

### Unknown Actor Reference

A reconstruction may need to say *"these observations appear to belong to the same person"* without
saying *who*. That is an **Unknown Actor Reference**: a bounded, non-Person reference used to
associate observations that are sufficiently supported as belonging to one actor **within a defined
reconstruction scope**.

It is part of the reconstruction projection. **It is not a store.** It creates no actor registry, no
identity record, and no surveillance profile, and it exists only for the scope that produced it.

An Unknown Actor Reference is **not**:

- A Home Assistant Person, or any Person
- An Identity Assertion
- A permanent, reusable, or cross-scope identity
- A role, an occupation, or a relationship
- A criminal or behavioural classification
- A biometric profile
- A synthetic guest
- Proof that all correlated observations belong to one human
- A source of permission

It may reference an actor reference identifier, the reconstruction scope, start and end time, a
**Primary Hypothesis Label**, a **Criteria Satisfaction Record**, correlation reason codes, supporting
Domain Events, contradicting events, uncertain events, entry and exit hypotheses, Room-presence
intervals, a movement sequence, dwell-time estimates, related unknown evidence sources, related
known-Person assertions, related external video references, alternative actor hypotheses, later
associations, and preservation status (**DL-74**).

**Every one of those is a Governed Reference or a value derived from existing records** (**P30**).
Nothing is copied, and no payload is duplicated into an actor object.

#### Unknown Person is not Unknown Actor

| Aspect | Unknown Person | Unknown Actor Reference |
|---|---|---|
| What it is | An Identity Assertion outcome | A historical reconstruction reference |
| Tense | Current, bounded to one moment | Past, bounded to one reconstruction |
| Owner | Identity | Concierge, as part of the projection |
| Spans time | No | Only where governed correlation supports it |
| Grants anything | No | No |

An Unknown Person assertion may be **evidence contributing to** an Unknown Actor reconstruction.
**They are never interchangeable.**

> At 10:02 an Unknown Person is supported in the Kitchen. At 10:07 an Unknown Person is supported in
> the Den. **This does not establish that one person walked from the Kitchen to the Den.**

#### Correlation requires more than proximity in time

**Temporal proximity alone must never establish that two observations share an actor.**

A governed correlation defines the reconstruction window; gathers eligible Domain Events and Facts;
preserves native source references; identifies candidate observations involving known and unknown
people; evaluates freshness and time ordering, Room adjacency or other accepted topology, plausible
travel time without asserting certainty, continuity of eligible evidence sources, entry and exit
events, external video references, contradictions, and evidence that more than one actor may exist;
produces one or more actor hypotheses; assigns a **Primary Hypothesis Label** derived from a
**Criteria Satisfaction Record** over those same factors (**DL-74**); **preserves the alternatives**;
rewrites no original evidence; and yields an explainable result.

The same guard applies within a single moment: an unassociated proximity source and an unmatched
voice are **not** joined into one actor because they were observed together.

**No correlation mathematics is invented here.** How the evaluated factors combine into a hypothesis
is **DL-74**: a Criteria Satisfaction Record, never a numeric score, probability, percentage, or
weighted calculation.

#### Plurality is a first-class outcome

The reconstruction must be able to represent one possible actor, several possible actors, and
**Unresolved Plurality** as three separate, non-ordered **Primary Hypothesis Label** values —
**Probably One Actor**, **Probably Multiple Actors**, **Unresolved Plurality** (**DL-74**). Multiple
unassociated proximity sources, multiple unmatched voices, multiple occupancy transitions, and
multiple external detections must not be collapsed into one actor — and must not be assumed to be
several. **Unresolved Plurality is never a synonym for low confidence in a one-actor hypothesis** —
restating the lesson already recorded for speaker plurality (**OD-84**): two actors and low confidence
in one actor produce the identical observable shape from opposite causes.

A complete and correct answer may be:

```text
At least one unknown person was supported between 08:12 and 09:32.
Primary Hypothesis Label: Unresolved Plurality.
The available evidence cannot reliably determine whether one or several actors were present.
```

#### Movement path and dwell time

A reconstruction may produce an estimated path and dwell-time summary. **Every element must be
labelled for what it is.**

| Label | Meaning |
|---|---|
| Observed event | A Domain Event occurred and is recorded |
| Derived interval | An interval computed from observed events |
| Inferred transition | A movement that was not directly observed |
| Estimated dwell time | A duration estimate, carrying its uncertainty |
| Unknown gap | A period with no eligible evidence |
| Contradicting observation | Evidence inconsistent with the hypothesis, retained rather than discarded |
| Criteria Satisfaction Record entry | Supports Hypothesis / Contradicts Hypothesis / Unavailable / Not Applicable, per factor (**DL-74**) |

**An estimate must never be presented as a direct observation**, and a reconstruction must never
imply continuous surveillance where only intermittent sensor evidence exists.

Dwell time must account for a late first observation, an early last observation, sensor timeout,
gaps, more than one person, Merged Rooms, overlapping coverage, and unavailable sensors. **A dwell
time stated without its uncertainty is a false certainty**, and is prohibited by **P15**.

#### Externally owned video and camera evidence

Video and camera evidence is generally owned by another system. **HTBW references it and does not
copy it** (**P21**, **P22**, **DL-30**, **DL-31**).

A correlation may record the source system, the native clip or event identifier, the camera
identifier, start and end time, content availability, retention status, integrity metadata **where
the source supplies it**, the related Room or Area, the relationship to the actor hypothesis,
preservation status, and access restrictions. Where the owning system supplies no stable identifier
or no integrity metadata, **the reconstruction records that limitation rather than substituting one
of its own.**

> **A referenced clip must never be asserted to depict the actor** unless accepted evidence supports
> that association.

Whether an Evidence Package includes references, exports, or copies follows the package and
preservation rules below and **OD-40**. Referencing external media does not broaden Connected Storage.

#### Later identification is additive

An Unknown Actor may later be associated with a known Person, a known non-resident Person, another
governed identity reference, or with no one at all.

The association must be additive; must preserve the original evidence and the original uncertainty;
must record who or what established it, with what confidence, and from what Effective Time; and must
create a Change Record where one is required.

It must **not**:

- Rewrite or retroactively reinterpret the original observations
- Silently rewrite prior Identity Assertions
- Convert every correlated observation into a known-Person Fact
- Grant retroactive permission

**A reconstruction must remain able to show what was known at each point in time**, not only what is
known now. This is the correction mechanism above, applied to actors.

#### Role and intent are never inferred

An Unknown Actor is described in neutral terms. HTBW must not describe anyone as a guest, cleaner,
contractor, service provider, intruder, burglar, or robber unless accepted governed evidence
establishes that role. **Unexpected presence is not such evidence.**

A scheduled service visit overlapping an observation window is **context, not identification**. The
correct statement is that a visit was scheduled and that unknown-person evidence was observed during
part of that window, correlated only as far as governed evidence supports.

Where household policy classifies a presence as unexpected, the reconstruction may state the opening
event, the unknown-person evidence, the possible path, the related video references, the policy
classification, and the Communications or alarms produced. **It must not claim forced entry, theft,
criminal intent, a single actor, an identity, or legal proof.**

Access to actor reconstructions and movement histories is governed by **Operational Trust**. These
are among the most sensitive projections the home can produce, and they must not be reachable through
generic Room Help or a general-question capability. Retention follows the existing classification
rules, and **indefinite retention of unknown-person observation is not a default** (**DL-47**,
**OD-35**).

---

## Preservation Hold

A Preservation Hold protects applicable records from normal purge, truncation, archival deletion, or
retention-driven deletion.

| Aspect | Owner |
|---|---|
| Authorisation; who may create, review, and release; visibility; conflict with deletion; duration and review | **Operational Trust** |
| Enforcement over its own records; prevention of applicable purge or truncation; preservation of required references | **Each owning responsibility** |

**There is no central preservation-hold enforcer.**

A hold must be:

- **Discoverable** — hold status is visible on the record
- **Attributable** — who placed it, when, and under what authority
- **Bounded or periodically reviewed** — an indefinite unreviewed hold defeats minimisation
- **Independent of visibility** — a hold does **not** automatically increase visibility
- **Explainable** — the home can state that a record is held

A hold does not retain content that was never permitted to be retained. **A hold cannot preserve raw
biometric internals or raw voice samples, because those were never stored.**

Whether a hold may override an authorised deletion request is **OD-39**. It is not resolved here.

### Transitive hold integrity

Because Decision Traces use exact version references, **holding a Decision Trace must also preserve
the exact governed source versions required to keep the trace explainable**, subject to privacy and
legal constraints.

Potential dependencies include Facts, Identity Assertions, policies, obligations, preferences,
sessions, Room Configuration, vocabulary mappings, and explicit human requests.

> **A held trace whose required references have been silently purged is a preservation failure.**

**Do not duplicate referenced payloads merely to satisfy a hold.** Protect the referenced records
according to their canonical owners.

---

## Evidence Package

An Evidence Package is a **projection over governed records**, produced on demand.

It may assemble records by date and time range, incident retrieval scope, Room, Merged Room, Asset,
Person, obligation, session, responsibility, correlation identifier, or causation chain.

Every Evidence Package records:

- Assembly time
- Requesting authority
- Scope
- Applied filters
- Included record classes
- Excluded record classes
- Redactions
- Missing-record markers
- Purged-record markers
- Withheld-by-policy markers
- Known historical gaps
- Relevant provenance references

An Evidence Package:

- Creates **no** alternative historical source of truth
- Does **not** replace the underlying records
- Does **not** become authoritative over the records it summarises
- **May legitimately differ** when assembled at different times, because retention and redaction
  advance
- **Must never claim completeness when gaps exist**

Assembly, transport, integrity representation, and permitted audience are **OD-40**.

---

## Tombstone

When a governed record is deleted, purged, or truncated, a **Tombstone** remains where the
architecture requires one.

A Tombstone may retain: record identity, subject, record class, removal timestamp, removal
authority, removal reason classification, and correlation linkage where permitted.

These states must always be distinguishable:

| State | Meaning |
|---|---|
| No event occurred | Nothing happened |
| No record was created | Something happened but produced no governed record |
| A record existed but was purged | Removed by retention policy |
| A record existed but was deleted | Removed by an authorised deletion request |
| A record existed but was redacted | Retained, with values removed |
| A record is unavailable | Held somewhere that cannot currently be reached |
| A record is withheld by policy | Exists and is retained, but not disclosable to this audience |

> **Do not silently truncate history.** Silent truncation converts *"we discarded the record"* into
> *"nothing happened"*, which is a false statement about the household.

---

## Field-level redaction

**Change Record values are privacy-classified separately from Change Record metadata.**

Values may be redacted. Where policy requires redaction, the record retains at least:

- That a change occurred
- Subject
- Field class
- Actor or initiating process
- Effective Time
- Recorded Time
- Removal authority
- Record identity

> **A redacted record remains a record.** Redaction must not silently convert *"something changed
> but the value is no longer retained"* into *"no change occurred."*

---

## History ownership

Foundation defines this model. Foundation does **not** own the histories recorded with it.

| History | Owner |
|---|---|
| Fact history; Fact lifecycle transitions | **Truth** |
| Identity Assertion history; identity-consent lifecycle history — evidence classes and reason codes only, never biometric internals | **Identity** |
| Obligation, maintenance, service, significance, and caretaker-assignment history | **Stewardship** |
| Preference, session, resume, and transfer history | **Continuity** |
| Policy, authorization-decision, privacy-policy, retention-policy, and preservation-hold authority history | **Operational Trust** |
| Room and Merged Room membership, participation, not-selected, deliberately-excluded, exposure, vocabulary, voice-assistant assignment, Composite Fact contributor-selection, and capability-definition history | **Room Configuration** (Foundation) |
| Decision history, through Decision Traces | **Concierge** |
| The temporal, version, change-record, snapshot, correlation, and provenance **models** | **Foundation** |

**Historical Explainability assembles these records.** It owns no historical store, duplicates no
responsibility, and creates no new responsibility. See
[../architecture/explainability.md](../architecture/explainability.md).

**Communication delivery history is decision history, and is therefore already Concierge's.** It uses
the record kinds defined here unchanged and introduces no new kind. **No row is added for it.** See
[communication.md](communication.md).

**No consumer may maintain a competing or re-derived history of another responsibility's records.**

---

## Legal and regulatory non-claim

**This architecture does not claim to produce legal-grade evidence.**

HTBW does not assert court admissibility, legal chain-of-custody sufficiency, tamper-evidence
certification, forensic certification, regulatory compliance, or compliance with any legal retention
regime.

Any legal, regulatory, insurance, investigative, or court-admissibility requirement requires
separate professional and technical validation.

**Preservation Hold and Evidence Package are HTBW architectural terms. They are not claims of legal
effect.**

---

## Explicit non-responsibilities

This model does **not**:

- Create a History, Memory, Household Memory, Case Management, or Evidence responsibility
- Create a central history owner, a central snapshot owner, or a central preservation-hold enforcer
- Select a database, storage technology, serialization format, snapshot interval, or identifier
  encoding
- Require every responsibility to use the same persistence strategy
- Require pure event sourcing
- Require repeated full-payload versioning

---

## Failure behavior

| Condition | Behavior |
|---|---|
| A Snapshot is missing for the requested range | Reconstruct from record creation, or report that the range cannot be reconstructed |
| Change Records within the range were purged | Report the gap and its reason classification; never interpolate |
| A Governed Reference cannot be resolved | Report the reference as unavailable, with the reason where known |
| A referenced Home Assistant row has been purged | Resolve to *"no longer retained"*, never *"never existed"* |
| A Change Record cannot be written | The failure is itself reportable; a silently unrecorded governed change is a defect |
| Effective Time cannot be determined | Record it as unknown and state so; never substitute Recorded Time silently |
| A held record's references were removed | Report a preservation failure |

---

## Explainability requirements

Every element of this model exists to make [../architecture/explainability.md](../architecture/explainability.md)
answerable across time. A temporal record that cannot be turned into a household sentence has
recorded the wrong thing.

---

## Representative scenarios

- [../scenarios/why-did-this-happen.md](../scenarios/why-did-this-happen.md)

## Open decisions

| ID | Question |
|---|---|
| OD-01 | Home Assistant representation strategy, including the persistence shape of Change Records, Snapshots, and Current Projections |
| OD-35 | Historical query surface and access |
| OD-36 | Reconciliation of deletion and export obligations with retention floors and Preservation Holds |
| OD-37 | Snapshot triggers, cadence, and scope per responsibility |
| OD-38 | Version identity, correlation, and causation identifier strategy, including evaluation of Home Assistant Context IDs |
| OD-39 | Preservation Hold authority, duration, review, release, and conflict with deletion |
| OD-40 | Evidence Package assembly, transport, integrity representation, and audience |
| OD-41 | Incident and Case object model |

## Related documents

- [../architecture/principles.md](../architecture/principles.md)
- [../architecture/adr-temporal-record-model.md](../architecture/adr-temporal-record-model.md)
- [../architecture/adr-historical-explainability-and-historical-truth.md](../architecture/adr-historical-explainability-and-historical-truth.md)
- [../architecture/privacy.md](../architecture/privacy.md)
- [../architecture/connected-storage.md](../architecture/connected-storage.md)
- [truth.md](truth.md)
- [decision-trace.md](decision-trace.md)
