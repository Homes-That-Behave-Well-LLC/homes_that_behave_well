# ADR — Historical Explainability and Historical Truth

> **Document status: Accepted ADR.**
> Authority: rank 1 in [../governance/authority-order.md](../governance/authority-order.md).
> Establishes **P27** and **P28**, and accepted decisions **DL-24** and **DL-25**.
> Mechanism ADR: [adr-temporal-record-model.md](adr-temporal-record-model.md).

---

## Status

Accepted.

This ADR establishes the **constitutional position**: that the home must be able to account for
itself across time, and that Truth is the system of record for what was true as well as for what is
true.

The **mechanism** by which that position is implemented — change records, snapshots, version
identity, references — is a separate concern with a separate lifetime, and is recorded in
[adr-temporal-record-model.md](adr-temporal-record-model.md). Neither ADR is complete without the
other.

---

## Context

### Explainability existed, but only in the present tense

The refoundation established explainability firmly. **P16** requires that the home explain both
actions and intentional non-actions. **DL-15** makes the Decision Trace a required output of every
decision, action, non-action, and suppression. [explainability.md](explainability.md) names six
questions the platform must always be able to answer.

**All six are single-decision questions.** Nothing in the canonical tier required the home to
reconstruct a time range, an incident, a Room, an Asset, or a Person's history. The word
*queryable* appeared once, in [../models/decision-trace.md](../models/decision-trace.md), naming no
retrieval dimensions.

### Retention was framed only as a ceiling

[privacy.md](privacy.md) required that traces be *"retained long enough to answer 'why did this
happen?' for a household-meaningful period, and no longer."* Retention appeared as a **limit** in
every canonical document and as a **requirement** in none. There was no counterweight — no statement
of how little may be retained.

### Fact history was unowned

Three histories had owners. Continuity owned experience history. Stewardship owned service and
maintenance history. Concierge owned decision history through the Decision Trace.

**Fact history had no owner at all.**

Under **P1** — *"if no responsibility owns a behavior, the behavior is undefined and will be invented
at runtime"* — this was a defect. Left unaddressed, each consumer would have built its own fact
history, or a revived "household memory" would have absorbed it.

### The architecture had already half-said it

Two canonical statements were reaching for this position without completing it.

[../models/truth.md](../models/truth.md) requires: *"All contributors unavailable → publish
`unknown`; do not retain the last value **as current**."* The qualifier *as current* presupposes a
distinction between operational and historical retention that no document defined.

The superseded `event-model.md` contained *"Event history remains authoritative"* and a history
retention policy. The refoundation correctly dismantled the event and memory layering — but
**dropped the underlying discovery without relocating it to an owner**. Under the greenfield mandate,
proven ideas are preserved even when obsolete boundaries are not.

**This ADR is therefore a restoration to the correct owner, not an invention.**

---

## Decision

### P27 — Historical explainability is an architectural requirement

HTBW retains enough governed information to reconstruct what the home observed, what it believed,
what it knew, what it decided, why it decided so, and why the alternatives were rejected.

This applies to a single decision, a time range, an incident retrieval scope, a Room, a Merged Room,
an Asset, a Person, an obligation, a session or experience, and a correlation or causation chain.

**Explainability has a temporal dimension.** Retention is a **floor as well as a ceiling**.

Where privacy requires removal or redaction, the resulting limitation must itself remain explainable,
so the home can state *"I no longer hold that record."* No record is silently discarded where the
architecture requires a governed deletion, purge, redaction, or truncation marker.

### P28 — Truth is the system of record for present and historical Facts

Operational expiration removes a Fact from *what is true now*. It does **not** automatically delete
*what was true then*.

Truth supports eight Fact lifecycle transitions — established, confirmed, confidence changed,
superseded, withdrawn, operationally expired, became unknown, became unresolved — and **each
transition is separately reconstructable**.

A Historical Fact is never presented as current, is never actionable, must not silently become
current again, and is not a retained raw evidence payload.

**Truth owns Fact history. No consumer may maintain a competing or re-derived Fact history.**

### Accepted decisions established

| ID | Decision |
|---|---|
| **DL-24** | Historical Explainability is a constitutional requirement |
| **DL-25** | Truth is the system of record for both present and historical Facts |

Full wording: [../governance/decision-ledger.md](../governance/decision-ledger.md).

---

## Responsibility impact

| Responsibility | Impact |
|---|---|
| **Foundation** | Defines the shared temporal, version, change-record, snapshot, correlation, and provenance models. See [../models/temporal-record.md](../models/temporal-record.md). Owns no other responsibility's history |
| **Stewardship** | Owns obligation, maintenance, service, significance, and caretaker-assignment history |
| **Identity** | Owns Identity Assertion history and identity-consent lifecycle history — evidence classes and reason codes only, never biometric internals |
| **Truth** | **Scope extended across time.** Owns Fact history and Fact lifecycle transitions |
| **Continuity** | Owns preference, session, resume, and transfer history |
| **Operational Trust** | Owns policy, authorization-decision, privacy-policy, retention-policy, and preservation-hold authority history. Owns retention classification and historical-query visibility |
| **Concierge** | Owns decision history through Decision Traces, and assembles Historical Reconstruction and Evidence Packages as projections |
| **Room Configuration** (Foundation) | Owns membership, participation, exclusion, exposure, vocabulary, voice-assistant assignment, contributor-selection, and capability-definition history |

---

## No new responsibility

**The seven-responsibility framework is unchanged:** Foundation, Stewardship, Identity, Truth,
Continuity, Operational Trust, Concierge. Human Trust remains an outcome.

- **Historical Explainability is cross-cutting**, exactly as Explainability already is. Every
  responsibility contributes to it; none owns it exclusively. It **assembles** governed records and
  owns no store.
- **Historical Truth is Truth extended across time.** Extending an existing owner's scope along the
  time axis is not a new boundary.

This ADR does **not** create a History responsibility, a Memory responsibility, a Household Memory
responsibility, a Case Management responsibility, an Evidence responsibility, a central history
owner, a central snapshot owner, or a central preservation-hold enforcer.

### No Household Memory revival

[../models/household-memory-model.md](../models/household-memory-model.md),
[adr-household-memory-governance.md](adr-household-memory-governance.md), and
[../models/event-model.md](../models/event-model.md) **remain Historical or Superseded**. Their
former ownership boundaries are **not** reactivated.

Historical Facts are Truth's records in a different lifecycle state. They are not a separate memory
subsystem, and no eighth responsibility follows from them. Useful discoveries in those documents are
preserved only where relocated into the approved canonical owner.

---

## Alternatives considered

| # | Alternative |
|---|---|
| A | Leave explainability single-decision; treat any temporal need as a later product feature |
| B | Adopt Historical Explainability but leave Fact history unowned, to be settled per implementation |
| C | Assign Fact history to Continuity, alongside experience history |
| D | Assign all histories to a new cross-cutting owner |
| E | Revive the household-memory boundary as the historical owner |
| F | Adopt P27 and P28 as stated |

---

## Alternatives rejected

| # | Rejected because |
|---|---|
| A | Retention decisions made in the absence of a stated floor are irreversible. A record not kept in the first month cannot be recovered in the sixth. The constitution would have been silent at exactly the point where the outcome is determined |
| B | **P1 violation.** Unowned behavior is invented at runtime, and the invention would differ per consumer, making cross-subject reconstruction impossible |
| C | Conflates two different objects. An experience is something a person had; a Fact is a governed conclusion about the world. Continuity would have become a second fact engine, violating **P8** and **DL-04** |
| D | Creates an eighth responsibility by another name, violating **P2** and **DL-01**, and would absorb four histories that already have correct owners |
| E | Reactivates a boundary the refoundation deliberately dismantled, and would place governed conclusions under a store rather than under their producer |
| F | **Accepted** |

---

## Privacy consequences

P27 establishes retention **floors**. [privacy.md](privacy.md) establishes retention **ceilings**.
**Both bind.**

- What is retained historically is the **governed conclusion and its attribution**, not the raw
  payload.
- Raw voice samples remain at zero retention by default. Biometric vectors, embeddings, fingerprint
  payloads, artifact internals, and biometric storage paths are **never** retained through this
  architecture and never cross the Identity → Truth boundary.
- Complete raw sensor streams are not retained. Evidence **references** and **classes** are.
- Where a retention floor and a privacy ceiling conflict, **privacy governs the outcome**, and the
  resulting limitation on explainability is itself recorded.
- Redaction, tombstones, and the distinction between *"nothing happened"* and *"the record is no
  longer held"* are required. Their mechanics are in
  [adr-temporal-record-model.md](adr-temporal-record-model.md) and
  [../models/temporal-record.md](../models/temporal-record.md).

**P30 is itself a privacy mechanism.** Referencing instead of copying means sensitive content exists
in one governed place, where it can be redacted once, rather than in every record that consumed it.

---

## Home Assistant First review

Conducted under **P21** against official documentation. The full capability review, including
documentation links, is recorded in
[adr-temporal-record-model.md](adr-temporal-record-model.md) and
[home-assistant-boundary.md](home-assistant-boundary.md).

Summary as it bears on this ADR:

- Home Assistant natively supplies the **evidence** layer — recorder state history, events, context
  identifiers, and long-term statistics. HTBW does not duplicate it.
- Home Assistant records **entity states**, which are evidence. It does not record **governed
  Facts**, which carry confidence, provenance, coverage, validity, and lifecycle. The existing
  object distinction *"a state is evidence; a Fact is governed"* holds unchanged across time.
- Home Assistant has **no per-record purge exemption**, no governed-record versioning, no
  field-level historical redaction, and no tombstone distinction. These gaps, and only these, justify
  extension.

---

## Connected-storage implications

The connected-storage justification arising from this ADR is **narrow** and is stated in full in
[connected-storage.md](connected-storage.md) and
[adr-temporal-record-model.md](adr-temporal-record-model.md).

This ADR does **not** grant permission to build a parallel history system. Connected records remain
anchored to Home Assistant objects, and evidence references point at native Home Assistant records
rather than copying their payloads.

---

## Legal and regulatory non-claim

**This architecture does not claim to produce legal-grade evidence.**

HTBW does not assert court admissibility, legal chain-of-custody sufficiency, tamper-evidence
certification, forensic certification, regulatory compliance, or compliance with any legal retention
regime.

Any legal, regulatory, insurance, investigative, or court-admissibility requirement requires separate
professional and technical validation.

**Preservation Hold and Evidence Package are HTBW architectural terms. They are not claims of legal
effect.**

---

## Open decisions

None is closed by this ADR.

| ID | Question |
|---|---|
| **OD-33** | **Closed — DL-43, DL-46, DL-47.** Retention is declared inside every governed record and artifact lifecycle; the remaining values are **OD-05**, **OD-26**, **OD-49** |
| **OD-34** | **Closed — DL-42, DL-44, DL-46, DL-47.** The temporal-persistence model is complete; the representation mechanism is the residual of **OD-01** |
| **OD-35** | **Closed — DL-130.** Governed Historical Retrieval and Access — one surface, classified before assembly; nine existing Explainability scopes remain the complete query model; `caretaker-of`/**DL-71** reused unchanged for Subject Authorization |
| **OD-36** | Reconciliation of deletion and export obligations with retention floors and Preservation Holds |
| **OD-05** *(amended)* | Decision Trace retention **floor and ceiling** |
| **OD-18** *(resolved as DL-59)* | Governs **operational** Fact validity, not Historical Fact retention |
| **OD-26** | Whether experience history is retained per person, per room, or both, and for how long |

---

## Consequences

**Positive**

- Fact history acquires an owner, closing a P1 defect.
- Explainability gains a temporal dimension without a new responsibility.
- Retention becomes a two-sided constraint rather than a one-sided limit.
- A discovery from the superseded event model is preserved under the correct owner.

**Costs and obligations**

- Every responsibility now owes a history, and must state what it retains and for how long.
- Privacy reconciliation must be applied before any document asserts a retention floor.
- Truth's contract grows: historical guarantees, lifecycle transitions, and a prohibition on
  consumer-held fact history.

**Risks**

| Risk | Mitigation |
|---|---|
| P28 is read as licence to build a general event or logging store | The Domain Event versus Change Record distinction, and the explicit non-revival of the superseded event model |
| Historical Explainability drifts into an eighth responsibility | It assembles and owns no store; stated in this ADR, in [explainability.md](explainability.md), and in [../models/temporal-record.md](../models/temporal-record.md) |
| Retention floors are read as overriding privacy | Privacy governs conflicts; the limitation is recorded rather than silently applied |
| Preservation Hold and Evidence Package are read as legal instruments | The explicit non-claim, repeated in four documents |

---

## Validation requirements

1. **Terminology consistency** for every new term across the canonical tier.
2. **No Household Memory revival** — no canonical document reactivates the superseded boundaries.
3. **Ownership uniqueness** — every history has exactly one owner; no document claims a history it
   does not own; no eighth responsibility is implied.
4. **Domain Event versus Change Record** distinction is stated and never collapsed.
5. **Retention floor-and-ceiling consistency** — no document states a floor without its ceiling.
6. **Snapshot-redaction protection** is present wherever snapshots are described.
7. **Tombstone requirement** is present and referenced from failure behaviour.
8. **Legal and regulatory non-claim** is present verbatim in this ADR,
   [adr-temporal-record-model.md](adr-temporal-record-model.md),
   [privacy.md](privacy.md), and [../models/temporal-record.md](../models/temporal-record.md), and
   no document anywhere asserts legal or regulatory sufficiency.

---

## Related documents

- [adr-temporal-record-model.md](adr-temporal-record-model.md)
- [principles.md](principles.md)
- [explainability.md](explainability.md)
- [privacy.md](privacy.md)
- [../models/temporal-record.md](../models/temporal-record.md)
- [../models/truth.md](../models/truth.md)
- [../contracts/truth-contract.md](../contracts/truth-contract.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
