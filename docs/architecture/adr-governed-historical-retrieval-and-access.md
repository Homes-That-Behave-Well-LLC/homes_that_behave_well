# ADR: Governed Historical Retrieval and Access

> **Document status: Canonical ADR.**
> Status: **Accepted** 2026-11-04. Records **DL-130** (issue **#81**, formal acceptance review PASS).
> Mechanism consumed unchanged: [adr-temporal-record-model.md](adr-temporal-record-model.md),
> [adr-historical-explainability-and-historical-truth.md](adr-historical-explainability-and-historical-truth.md).
> Canonical terminology: [../models/glossary.md](../models/glossary.md).

---

## Status

**Accepted 2026-11-04.** Formal acceptance review on Issue #81 returned **PASS**.

Resolves **OD-35** — the retrieval-surface, query-model, and authority residual left open by
[adr-historical-explainability-and-historical-truth.md](adr-historical-explainability-and-historical-truth.md)
(**P27**, **DL-24**) and [adr-temporal-record-model.md](adr-temporal-record-model.md) (**DL-26**,
**DL-27**, **DL-35**) after both settled *what* must be retained and *how it is represented*, without
deciding *how a household asks a historical question, and who may receive the answer*.

**This ADR creates no new mechanism.** Every clause below reuses an already-accepted construct: the
nine Explainability retrieval scopes, the Decision Trace (**DL-129**), the Historical Reconstruction
projection (**DL-35**, **DL-74**), Operational Trust's existing Access-then-Disclosure model (**DL-34**,
**DL-72**), its existing Person/Relationship scope table (**DL-126**), Foundation's `caretaker-of`
relationship (**DL-49**), and **DL-71**'s five Intended Audience Specification forms. The contribution
of this ADR is to classify a historical question against that existing architecture, before any
protected content is assembled, and to name precisely which existing mechanism answers each part of it.

---

## Context

### Historical Explainability was accepted; retrieval was not

**P27** requires the home to retain enough to reconstruct what it observed, believed, knew, and
decided. `explainability.md` already named nine retrieval scopes a reconstruction must answer
against. **Nothing decided how a resident actually asks**, what authority the answer requires, or how
an actor/movement reconstruction (**DL-35**) is kept out of reach of a generic conversational or
Room Help capability.

### Two canonical positions were in deliberate tension

**DL-24** ("retain enough to reconstruct") and **DL-35**/`privacy.md` ("do not build a surveillance
archive") were recorded as **deliberately** in tension, with OD-35 named as the decision that resolves
the retrieval side of it. This ADR is that resolution: retention and reconstruction remain exactly as
already accepted; what changes is that every retrieval path **must** pass through classification and
authorization before content is assembled, never after.

### Twenty tested question categories existed with no enumerated query model

An Episode 9 review tested twenty natural-language question categories against the nine accepted
retrieval scopes and found the categories were real but unmapped. Two residuals surfaced directly from
that review and from Issue #146's platform verification: a Decision Trace lacked a distinct
"observed outcome" element (remediated by **DL-129** before this ADR was drafted), and native
long-term statistics perform no gap detection of their own (**VERIFIED_SUPPORTED**, Issue #146) — a
fact this ADR consumes directly rather than re-verifying.

### A Caretaker authorization model was assumed to need inventing

Nothing in the issue's own text, nor in prior drafts, established what repository research would show:
that Foundation's `caretaker-of` relationship (**DL-49**) already carries exactly the shape this
decision needed — many-to-many, typed over **Person, Pet, and Asset subjects alike** — and that
**DL-71** had already formalized a reusable Intended Audience Specification vocabulary naming,
among other forms, Relationship-based resolution of exactly this relationship. No new authorization
construct was required once that reuse was confirmed.

---

## Decision

See **DL-130** in [../governance/decision-ledger.md](../governance/decision-ledger.md) for the full,
binding text. Summarized:

1. **One retrieval surface, internally tiered.** Assist/Conversation is the sole resident-facing
   interaction surface for every historical question. Every query is classified — before any content
   is assembled — into an ordinary retrieval (handled through Conversation's existing **DL-69**
   pre-answer-filtered discipline) or a Person/actor reconstruction (routed into the dedicated governed
   path, never answered inline by generic Room Help or a general-question capability).
2. **Nine scopes, no tenth.** `explainability.md`'s existing retrieval scopes remain the complete query
   model, expressed along Requester/Subject/Record-Class/Time/Correlation/Reconstruction-Required
   dimensions, with all twenty Episode 9 categories mapped onto them.
3. **Category 7 splits structurally** into "HTBW decided not to act" (Decision Trace, **DL-15**) versus
   "HTBW made no decision" (diagnostic reconstruction, **DL-73**/**DL-111**), stated explicitly in every
   answer.
4. **A twelve-step authorization sequence**, reusing the existing Access-then-Disclosure model
   unchanged, with Subject Authorization (step 5) evaluated through Operational Trust's existing
   Person/Relationship scope, expressed in **DL-71**'s existing specification-form vocabulary.
5. **Caretaker reconciliation reported in full** — see DL-130 clause 5 — confirming `caretaker-of`
   (**DL-49**) supplies candidates only, never access, for Person **and** Pet subjects alike, with no
   new relationship, vocabulary, or subject class.
6. **No new Required Identity Band/Confirmation Strength table** — Historical Retrieval and
   reconstruction classify under **DL-76**'s existing Disclosure default, separable only through
   **DL-109**'s existing object-specific-override mechanism.
7. **A structural gap model** reusing every source's own already-accepted vocabulary, adding exactly
   one new obligation: self-detected gap reporting when a historical answer consumes native long-term
   statistics.
8. **No new refusal taxonomy** — the existing six-outcome disclosure table states the
   authorized-to-ask-but-unauthorized-to-receive case unchanged.
9. **No historical store, no new responsibility**, and no pre-emption of **OD-40** or **OD-41**.

---

## Consequences

- Historical questions remain askable through the one surface a resident already uses for everything
  else; no second natural-language interface is built.
- A household configuring Person Setup already configures Historical Retrieval authorization, because
  it reuses the same Person-scope/Relationship-scope policy and the same `caretaker-of` relationship
  already used elsewhere.
- **OD-30** (Decision Trace visibility), **OD-40** (Evidence Package audience), and **OD-41** (Incident
  object model) each gain evidence from this ADR without being decided by it.
- Native long-term statistics consumers must implement the self-detected gap-reporting obligation
  (clause 7) before presenting a statistics-derived historical answer as complete.

## Related documents

- [../governance/decision-ledger.md](../governance/decision-ledger.md) — **DL-130**
- [../architecture/explainability.md](../architecture/explainability.md) — query model, Episode 9
  mapping, gap model
- [../models/operational-trust.md](../models/operational-trust.md) — authorization sequence, Subject
  Authorization
- [../models/temporal-record.md](../models/temporal-record.md) — Historical Reconstruction, unchanged
- [../architecture/privacy.md](../architecture/privacy.md) — retention floors/ceilings, unchanged
- [../models/person-and-identity.md](../models/person-and-identity.md),
  [../models/stewardship.md](../models/stewardship.md) — `caretaker-of` reuse
- [../scenarios/historical-retrieval-and-access.md](../scenarios/historical-retrieval-and-access.md) —
  worked scenarios
