# ADR: Incident and Case Object Model — Scope, Not Object

> **Document status: Canonical ADR.**
> Status: **Accepted** 2026-11-05. Records **DL-134** (issue **#87**, formal acceptance review PASS).
> Resolves **OD-41** in full.
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Terminology: [../models/glossary.md](../models/glossary.md), [../models/temporal-record.md](../models/temporal-record.md).

---

## Status

**Accepted 2026-11-05.** This ADR creates **no new responsibility, no Incident record class, no
Incident store, no Case store, no Incident owner, no Case Management responsibility, and no Incident
lifecycle.** Foundation, Truth, Identity, Operational Trust, Concierge, Historical Reconstruction
(**DL-130**), Preservation Hold (**DL-132**), and Evidence Package (**OD-40**) retain exactly the
ownership they already have.

---

## Context

Several accepted constructs are bounded to *"one reconstruction"* or *"a bounded event"* — Unknown
Actor References (**DL-35**), Preservation Holds (**DL-132**), Evidence Packages (prospective **OD-40**)
— without naming the thing they are bounded **by**. **DL-130** already lets an Incident participate in
Historical Retrieval as a query Subject scope ("Person, Pet, Asset, Room/Merged Room, Communication,
Decision, or Incident scope") without deciding whether an Incident is itself persisted. This ADR settles
that ambiguity.

A persisted Case object — with a lifecycle, an owner, and attachments — is functionally a new
responsibility, and the architecture already prohibits a Case Management responsibility (**DL-24**).
Any resolution must show why it is not recreating that prohibited construct by another name.

---

## Decision

### 1. Scope, not object (Remaining Question 1)

**An Incident is a bounded, governed event scope — not a persisted Home object, not a Case, not an
artifact, not a governing parent, not a durable actor profile, and not a store.** It is a bounded
correlation/retrieval/reconstruction scope used to describe the set of relevant records, Facts,
observations, decisions, correlations, and other authorized evidence associated with a household
question or event. The scope is assembled from existing authoritative records; **it does not become a
durable Case file merely because a household asks about an event.**

### 2. No owner (Remaining Question 2)

**No responsibility owns an Incident record, because no Incident record exists.** The HTBW operation
that constructs and consumes an Incident scope (a Historical Reconstruction, a Preservation Hold
placement, an Evidence Package assembly, or an Explainability answer) retains ownership of its own
durable output exactly as it already does:

| Responsibility | Owns |
|---|---|
| Foundation | Object definitions and relationship types |
| Truth | The Facts an Incident scope may reference |
| Identity | Identity Assertions an Incident scope may reference |
| Operational Trust | Access, disclosure, and Hold/conflict authority |
| Concierge | Orchestration and the Decision Trace of its own decisions |
| Historical Reconstruction | The projection assembled on demand (**DL-130**) |
| Preservation Hold | Its own lifecycle (**DL-132**) |
| Evidence Package | Its own artifact/projection lifecycle (prospective **OD-40**) |

None of these becomes "the Incident's owner." **Incident is a cross-record bounded scope consumed by
these mechanisms where useful, never a record they jointly or separately own.**

### 3. Construction, not creation (Remaining Question 3)

**Nothing creates a durable Incident.** A governed operation **constructs** (establishes, uses) an
Incident scope when a bounded event context is required — in response to a household question, a
Preservation Hold placement, an Evidence Package request, or an Explainability answer. No Incident is
created as a side effect of: a Person asking a historical question; a Hold being placed; a
reconstruction being performed; an unknown actor appearing; an Evidence Package being requested; an
automation firing; or a safety condition occurring. When the operation ends, **there is no separately
retained Incident object** unless some other canonical artifact/record (a Decision Trace, a Hold, an
Evidence Package) independently persists information produced by that operation, under its own
already-accepted lifecycle.

### 4. No lifecycle (Remaining Question 4)

Because Incident is a scope, not a persisted object, **there is no canonical Incident lifecycle** —
no OPEN, UNDER REVIEW, CLOSED, or ARCHIVED state, and nothing "closes" an Incident. Individual durable
constructs that may have used an Incident scope continue to have their own, already-accepted lifecycle
unchanged: Preservation Hold (**DL-132**), Decision Trace (Explainability), Evidence Package (prospective
**OD-40**), Communications, Truth Facts, Identity Assertions, and deletion/preservation conflicts
(**DL-133**).

### 5. Not a Governing Parent (Remaining Question 5)

**Incident is not, and cannot be, a DL-45 Governing Parent.** Preservation Holds and Evidence Packages
use their own canonical governing-parent/reference semantics — unchanged by this ADR. A Preservation
Hold may *reference* the same Incident scope definition or correlation boundary another operation used
for the same event; it is never *owned by* that scope (restating **DL-132** §4 unchanged). An Evidence
Package may be *assembled using* an Incident scope; the Incident never becomes its governing parent
(prospective **OD-40** remains free to determine its own governing-parent answer independently).

### 6. No retention declaration (consequence of §1, §4)

Because Incident is not a persisted record or artifact class, **it has no independent DL-47 retention
duration**, and none is assigned ("Incident retention days" is not a construct this ADR creates).
Records used in or produced from an Incident-scoped operation retain their own existing retention
classification: a Decision Trace keeps Decision Trace retention; a Historical Fact keeps Fact retention;
a Communication keeps Communication retention; an Evidence Package keeps its own prospective OD-40
lifecycle; Hold metadata keeps its **DL-132** structural floor.

### 7. Shared scope, not shared container

A Historical Reconstruction, a Preservation Hold, and an Evidence Package may need to describe the
**same** bounded household event. The architecture supports this by letting them **reuse a coherent
scope definition** — time bounds, **DL-104** Correlation/Causation Identity, record references, Subject
references, Room/spatial scope, explicit inclusions/exclusions — **never** by inventing a shared
persisted container that all three attach to. Where a reusable scope expression benefits from a
canonical shape, it remains a **value/projection/reference structure**, never an independently governed
persisted Incident record.

### 8. Canonical scope dimensions

An Incident scope may be described through any combination of, as needed — none is mandatory, and only
what is necessary to define the bounded event is included:

- bounded time/interval;
- Room/Merged Room/spatial scope;
- governed Subject(s) (restating **DL-130**'s existing Subject-scope list: Person, Pet, Asset, Room/
  Merged Room, Communication, Decision — Incident is itself one more Subject-scope form, not a new
  dimension layered on top);
- Decision Trace(s); Communication(s); Domain Event(s); Truth Facts;
- **DL-104** Correlation Identity and Causation Identity;
- record classes; explicit inclusion/exclusion;
- authorized external evidence references; known gaps/unavailable evidence.

### 9. Dossier prevention (Remaining Question 6) — the central privacy guardrail

Using an Incident scope must **not**: create a persistent Person dossier; create a durable actor
profile; collect all available information merely because it might relate; extend retention
automatically; make intermittent observation look continuous; join unrelated events into one narrative
without evidence; transform temporal proximity into causation; infer occupation, role, intent, or
criminality; or maintain a reusable Unknown Actor identity. **Only authorized evidence necessary for
the bounded operation is used. DL-35 is preserved completely:**

- An Unknown Actor Reference remains within one reconstruction/projection, non-identifying, non-
  reusable across scopes, not stored as a durable actor profile, not silently promoted to Person, and
  not linked across Incident scopes merely because observations look similar.
- **DL-104** Correlation Identity / Causation Identity may connect records as a scope boundary input;
  this never manufactures same-Person, same-unknown-actor, same-intent, or same-narrative claims.
  Temporal proximity (e.g. a scheduled service visit overlapping an observation window) remains
  **context, not identification**.

### 10. Next-evidence guidance (Episode 9 finding, routed here and to OD-40)

**"What should be examined next?" has a governed answer without a new Evidence responsibility.**
Responsibilities already in place supply it:

- **Historical Reconstruction** identifies the unresolved question/evidence gap (`temporal-record.md`'s
  existing gap-reporting requirement, unchanged).
- **Concierge** may offer a permitted next action (`concierge-contract.md`'s existing **Ask** outcome).
- **Operational Trust** determines whether the existence of, and access to, a proposed evidence source
  may be disclosed or used (**DL-34**, `privacy.md`).
- The **existing source responsibility** owns and retrieves the source where authorized (externally
  owned video/camera evidence remains referenced, never copied, per `temporal-record.md` unchanged).

**Six distinguishable states are preserved** (existing canonical vocabulary reused, not replaced):
source consulted, no responsive evidence found; source exists, not consulted; source unavailable/
retrieval failed; source does not exist/is not configured, where known; source existence cannot be
disclosed; no further authorized source is known. **"There is nothing further to examine" is a valid,
complete answer** when supported.

**Naming a source does not assert its contents.** *"The front-door camera exists and was not
consulted"* means only that the source may be relevant and has not been examined — never that footage
exists for the interval, contains the actor, proves identity, proves intent, or will resolve the gap
(restating `temporal-record.md`'s existing *"a referenced clip must never be asserted to depict the
actor unless accepted evidence supports that association"* unchanged). **Identifying a source and
retrieving it are separate, separately authorized acts** — naming a potential source never itself
triggers retrieval of sensitive evidence.

---

## Terminology (glossary addition)

**Incident** — a bounded, governed event scope used for historical reconstruction, retrieval,
preservation scope, Evidence Package projection, or related explainability where several authoritative
records must be considered together. Constructed from existing authoritative records and scope
constraints. Not a persisted Home object, a Case, an artifact, a governing parent, a durable actor
profile, a store, or a new responsibility.

---

## Home Assistant First review

Home Assistant has no native Incident/Case concept. This is not a native gap being duplicated — it is
an HTBW-only construct, and the burden of proof (**DL-30**) is that bounded-scope semantics are
genuinely required (households think in bounded events) while a **persisted** Incident object is not
(the bounded-scope semantics are fully satisfiable by reusing existing query/reference architecture).
Native Areas, Persons, entities, Recorder history, Activity, automations, traces, and media/source
references remain the authoritative inputs an Incident scope may reference; none is duplicated into an
Incident record.

## Validation against DL-130, DL-132, DL-133

- **DL-130** already lets Incident participate in Historical Retrieval as a Subject-scope form without
  deciding persistence; this ADR completes exactly that decision, consuming DL-130 unchanged.
- **DL-132** already supports Preservation Hold scope through specific records, a governed Subject, a
  bounded time range, a bounded Room/time context, and a correlation/causation chain, with Incident
  scope explicitly optional; this ADR confirms a persisted Incident was never required for Hold scope
  and does not reopen DL-132.
- **DL-133** resolves deletion-versus-preservation conflict at the lowest practical record/obligation
  level and never required a persistent Incident/Case container; this ADR does not reopen DL-133 and
  does not retrofit one.

---

## Responsibility impact

| Responsibility/concept | Impact |
|---|---|
| Foundation, Truth, Identity, Operational Trust, Concierge (DL-01) | Unchanged |
| Historical Reconstruction (DL-130) | Unchanged; Incident confirmed as one Subject-scope form, not persisted |
| Preservation Hold (DL-132) | Unchanged; Incident scope remains optional convenience, never required, never a governing parent |
| Deletion-versus-preservation (DL-133) | Unchanged; not reopened |
| Unknown Actor Reference (DL-35) | Unchanged; fully preserved, not weakened |
| Evidence Package (OD-40, prospective) | Unaffected; may use an Incident scope for assembly without Incident becoming its governing parent; OD-40 retains its own governing-parent question |

## Open decisions (not decided here)

- **OD-40** (Evidence Package assembly/transport/integrity/audience/governing-parent) — unaffected;
  this ADR removes Incident as a candidate persisted governing parent, narrowing but not deciding
  OD-40's own question.
- **OD-09** (erasure/portability mechanics) — unaffected.

## Related documents

- [../governance/decision-ledger.md](../governance/decision-ledger.md) — **DL-134**, **DL-24**,
  **DL-35**, **DL-43**, **DL-45**, **DL-104**, **DL-130**, **DL-132**, **DL-133**
- [../models/temporal-record.md](../models/temporal-record.md) — *Unknown Actor Reference*, *Evidence
  Package*, *Externally owned video and camera evidence*
- [adr-governed-historical-retrieval-and-access.md](adr-governed-historical-retrieval-and-access.md)
- [adr-preservation-hold-governance.md](adr-preservation-hold-governance.md)
- [adr-deletion-versus-preservation-reconciliation.md](adr-deletion-versus-preservation-reconciliation.md)
- [explainability.md](explainability.md) — Episode 9 category mapping, rows 15 and 17
- [../models/glossary.md](../models/glossary.md) — **Incident**
