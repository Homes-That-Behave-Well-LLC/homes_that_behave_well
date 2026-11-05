# ADR: Preservation Hold Governance

> **Document status: Canonical ADR.**
> Status: **Accepted** 2026-11-05. Records **DL-132** (issue **#85**, formal acceptance review PASS).
> Resolves **OD-39** in full, except the deletion-versus-preservation precedence question, which
> remains explicitly **OD-36**'s own.
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Terminology: [../models/glossary.md](../models/glossary.md), [../models/temporal-record.md](../models/temporal-record.md).

---

## Status

**Accepted 2026-11-05.** This ADR resolves every OD-39 Remaining Question except deletion-versus-
preservation precedence, which `#85`'s own text already assigns to **OD-36** and which this ADR does
not duplicate or decide.

This ADR creates **no new responsibility**. A Preservation Hold remains a **marker on governed
records, never an artifact class of its own** (**DL-43**, unchanged), enforced by each owning
responsibility over its own records, with **no central Preservation Hold enforcer** and **no Hold
payload store**. Operational Trust owns authorisation (who may place, review, and release); each
responsibility owns enforcement over its own records; Concierge may orchestrate the interaction and
participates in Decision Trace/Explainability, and owns none of the above.

---

## Context

A Preservation Hold already has real architectural force (**DL-43**, **DL-45**, **DL-47**): it survives
parent-object removal, is not defeated by ordinary purge, and constitutes a structural retention floor.
What was entirely undecided was **who may place one, for how long, under what review, and how it is
released** — and verified implementation evidence (a flat 30-day archive-retention setting; Asset
Intelligence's count-bounded ring buffers) showed that an unqualified Hold is not actually enforceable
against the storage/retention mechanisms a household already has.

---

## Decision

### 1. Placement, review, and release authority (Remaining Question 1, 5)

**A Preservation Hold may be placed only by a Person explicitly, household-configured-authorised for
Preservation Hold governance.** This reuses the **already-accepted** mechanism confirmed by **DL-109**
for exactly this situation ("where a household wants a more capable or trusted configuration role, the
already-accepted mechanism is **DL-71**'s Role/Authority Class... never a newly invented construct"):
authorisation is expressed using **DL-71**'s existing **Named Person** or **Role/Authority Class**
Intended Audience Specification forms, naming a specific Person or a household-configured Role (for
example an owner/administrator-equivalent Role, by direct analogy to **DL-97**'s reuse of the same
forms for escalation accountability). **No parallel Preservation Hold identity/role system is
invented.**

**Placement authority does not imply review authority, and neither implies release authority.** Each
is its own, independently household-configured authorisation, reusing the same DL-71 forms. A
household may name the same Person/Role for all three, or different ones. The following are
**explicitly not, by themselves, a sufficient basis** for any of the three: being a resident; being
Household; holding an Owner-role Person record; holding the native Home Assistant administrator flag
alone (**DL-109**: the native admin flag "confer[s] no care, guardianship, or proxy authority beyond"
itself); controlling the underlying device; being able to see the underlying data; managing the
affected Asset; being the Person the records describe; or holding Explainability/Historical-Retrieval
access. **Record access never implies Hold authority.**

### 2. Risk, identity, and confirmation (Remaining Question 2)

**Placement and release are each a Governance-class Action-Risk (DL-76)**: Required Identity Band
**Very High**, Required Confirmation Strength **Strong** — adopted as drafted; no new Identity Band or
Confirmation Strength is invented for Holds. Placement must not proceed from an uncertain or
insufficient identity result, a weak confirmation result, mere Room presence, or anonymous Assist use.
Where the required band/strength cannot be verified, **DL-40**'s existing `Unavailable` outcome governs
exactly as it already does elsewhere — the operation is refused, never silently downgraded to a weaker
class. **Review** that records continuation or narrowing is likewise a Governance-class action (it
alters an evidentiary/governance record, DL-76's own test), evaluated under the same defaults; a review
that itself releases the Hold is governed by release's own requirement, not a lesser one.

### 3. Explicit purpose (Remaining Question — stated purpose)

A Hold must carry a stated household purpose (for example: a missing delivery, a household accident, a
dispute, suspected equipment failure, an insurance matter, or another legitimate household reason), held
as Hold metadata and Decision Trace context. **The stated purpose is not permission to infer
criminality, guilt, intent, legal status, or wrongdoing** — it is a record of why the household chose
to stop forgetting, nothing more. An open-ended Hold with no stated purpose is not permitted.

### 4. Scope (Remaining Question 6)

A Hold must be able to exist **independently of an Incident object**. Supported canonical scopes:

- one or more specific governed records;
- a governed object/Subject, qualified by the applicable records (never "everything about this
  Subject" inferred from a narrower request);
- a bounded time range;
- a bounded Room-and-time context, where Room Configuration already makes that context canonical;
- a correlation/causation chain, reusing the existing **DL-104** Correlation Identity construct —
  no second correlation model is invented;
- an Incident/Case scope, **only if and when OD-41 accepts a usable Incident construct** — Incident
  scope is optional convenience, never a prerequisite. **OD-39 is not blocked by OD-41, and OD-41's own
  Incident/Case object model is not decided here.**

**Scope expansion must be explicit, never inferred.** "Preserve records from the Den between 2 PM and 6
PM related to this event" does not imply "hold everything about every Person who was in the Den."
Where a broader Hold is genuinely wanted, the broader scope itself must separately satisfy §1–§2's
authority/confirmation requirements. Privacy and minimisation remain first-class during preservation;
preserving more than the stated scope actually covers is not preservation, it is scope creep.

### 5. Duration and review (Remaining Question 3, 4)

**No Preservation Hold may become indefinite merely because nobody remembers to release it, and no
HTBW-wide numeric default duration or review interval is invented.** This follows the same reasoning
**DL-97** already applied to escalation timing ("no HTBW-wide default grace-period or elapsed-time
value exists... household-configured") and **DL-47**'s refusal to impose one retention rule across
classes: a Hold's own review-due time is **explicit, required Hold metadata**, set by the authorising
Person at placement and at every continuation, never defaulted by HTBW to an invented number of days.
Every active Hold carries: explicit start; explicit current status; explicit stated purpose; explicit
authorised placer; explicit review-due time; review history; release status.

**Review is a governed action** (§2), asking: is the stated purpose still active; is the current scope
still necessary; should the Hold continue, narrow, or be released; is the authorising household
authority still validly configured. Hold review reminders reuse the **existing** Stewardship pattern
for an obligation that remains open past its own schedule — **"notification, not automatic
escalation"** (`stewardship.md`, *Incomplete obligations are notification, not automatic escalation*):
an overdue review is reported and stays visible, exactly as an incomplete obligation already is, without
transferring Hold ownership to Stewardship or inventing a second reminder engine. **Operational Trust
remains the owner of Hold authority and policy; the record-owning responsibility remains the owner of
the marker; Stewardship, where the household has configured it, only helps the household not forget.**

### 6. Missed review (Remaining Question 4, continued)

A missed review **fails safe toward preservation**, restating this ADR's own §9/§10 principle for the
Hold's own lifecycle: the Hold does not silently release merely because a review date passed, and it
does not silently become permanent and unexamined either. Lifecycle: **ACTIVE → REVIEW DUE → OVERDUE**
(if missed) **→ RENEWED/CONTINUED** (after a governed review) **→ RELEASED**. An overdue Hold remains
preserving; the overdue state is itself reported through existing governed Communication/notification
mechanisms and remains visible and explainable for as long as it is outstanding — it is never resolved
by a silent timer-based release, and it is never allowed to disappear from view merely because nobody
has acted on it yet.

### 7. Release (Remaining Question 5, continued)

Release requires the household-configured release authority of §1 and the identity/confirmation of §2
(Governance, Very High, Strong). **Release does not erase Hold history**: who placed it, when, its
stated purpose and scope, review history, who released it, when, and why remain part of the governed
record, restating **DL-47**'s structural retention requirement unchanged. **Release is not immediate
deletion.** Release removes the Preservation Hold retention floor and hands the affected records back to
normal retention/deletion governance; what happens next — including any already-overdue ordinary
retention, and any conflict with a pending deletion/erasure obligation — is governed by the ordinary
rules and by **OD-36**, not by this ADR.

### 8. Deletion conflict — explicitly deferred (Remaining Question 7)

**This ADR does not decide, and explicitly defers to OD-36, the question of which prevails when a
Preservation Hold conflicts with a valid deletion or erasure obligation.** A Hold must not become an
unreviewable mechanism that automatically defeats a Person's deletion request, and a deletion request
must not automatically defeat an active Hold; **that precedence is OD-36's alone.** This ADR supplies
OD-36 with everything OD-36 needs to decide that conflict: who has authority to place/review/release,
lifecycle semantics, scope, audit/Decision Trace semantics, and enforcement behaviour — all above.

### 9. Disclosure of Hold existence (Remaining Question 8)

**The existence of a Preservation Hold is itself governed information**, evaluated through the
**existing** Operational Trust / Identity / audience / disclosure architecture (**DL-34**, **DL-36**),
never through a new, separate "who may see Holds" model. Access to the underlying data does not by
itself grant access to Hold metadata. At minimum, the following are distinguished: the Person(s)
authorised to manage/review/release the Hold (§1); the Subject(s) whose records are held, whose own
disclosure rights are evaluated exactly as for any other sensitive fact about them; ordinary household
Persons; and Guests/unauthorised Persons. Where a requester is not authorised, the existing protected-
information refusal vocabulary applies (`failure-and-degradation.md`'s honest-response vocabulary —
*"Not authorized,"* *"Cannot answer here"* — never a response that itself leaks the Hold's existence by
explaining why it cannot be shown). **This ADR does not invent a universal rule that a data subject must
always, or must never, be proactively notified that their records are held** — whether proactive
subject notification occurs is evaluated through the same existing disclosure/consent architecture
case by case, exactly as **#85**'s own text anticipated, and is not a new policy this ADR invents.

### 10. Storage-boundary enforcement and bounded collections

**Any retention, purge, truncation, or archival-deletion mechanism governing Hold-eligible governed
records must be able to discover and consult Hold status before discarding an applicable record.**
Where held records live in Connected Storage, Hold status must be discoverable at the storage/retention
boundary, and the retention routine must check it; ordinary expiry cannot silently override it.

**A fixed-size bound (a ring buffer discarding the oldest record as an unevaluated side effect of
appending a new one) is not an acceptable final retention mechanism for governed records to which a
Preservation Hold may apply, unless the bounding/eviction step itself can evaluate and honour the
Hold before discarding.** This directly addresses the verified implementation evidence on `#85`
(`events.append(event); events = events[-max_events:]`): an eviction with no evaluation step, no reason
code, and nothing recorded cannot honour a Hold and is not a conforming pattern for Hold-eligible
governed records. This does not categorically ban bounded collections — it requires that discard be an
**evaluable** step, not an unconditional side effect.

**Before discarding a governed record, the mechanism must evaluate preservation state. Where a Hold
prevents discard, the mechanism fails safe toward preservation**, never toward silent deletion, silent
oldest-record drop, or silent compaction of required evidence. The prevented discard itself is recorded
and explainable (§12). Where capacity or storage pressure results from records that cannot be
discarded, that pressure is surfaced as a dependency/capacity condition through the existing **DL-41**
/ `failure-and-degradation.md` vocabulary (*"Report unavailable,"* *"Record an unresolved state"*) —
never resolved by silently violating the Hold.

### 11. Native Home Assistant limitation

**Home Assistant Recorder offers no native per-record Preservation Hold exemption**
(`connected-storage.md` already states this: *"Preservation Hold enforcement | Recorder offers no
per-record purge exemption"*). This ADR states the consequence honestly rather than assuming it away:

- Where an HTBW-governed record exists independently in Connected Storage, a Hold applies according to
  the accepted persistence architecture above.
- Where only ephemeral native Recorder history exists with no corresponding governed HTBW record, a
  Hold **may be unimplementable** for that specific evidence, and this is stated honestly rather than
  claimed.
- Where material evidence was captured into a governed Decision Trace or other governed record before
  native expiry, the Hold applies to that governed record and its required source versions (§12), never
  by pretending the original native Recorder row itself can be exempted. **No second Recorder is
  built.**

### 12. Held Decision Trace and transitive source preservation

Restates `temporal-record.md`'s existing, unchanged *Transitive hold integrity* text: holding a
Decision Trace also preserves the exact governed source versions required to keep the trace
explainable (**DL-47**, **P30**), without duplicating referenced payloads and without unlimited,
unrelated transitive retention of everything loosely related to the trace — only what is actually
required to keep the held trace explainable. **No copied Hold archive is created to satisfy this.**

### 13. No payload store, no Evidence Package

Placing a Hold **never** copies scoped records into a Hold folder or archive, creates a ZIP, creates an
Evidence Package, duplicates native state, or creates a second record store. **Restates DL-43
unchanged.** A later household request for a deliberately materialised evidence artifact belongs to
**OD-40** (Evidence Package) and its own governed lifecycle; this ADR does not collapse the two.

### 14. No legal-effect claim

Restates the existing, unchanged constitutional boundary: *"Preservation Hold" is an HTBW architectural
term.* It asserts no legal hold status, litigation-hold sufficiency, court admissibility, evidentiary
sufficiency, forensic certification or integrity, chain-of-custody completeness, tamper evidence,
records-management compliance, or regulatory compliance. Its purpose is household-governed temporary
suspension of ordinary forgetting, nothing more.

---

## Explainability and Decision Trace requirements

Every consequential Hold lifecycle event is explainable per the existing Decision Trace structure
(`decision-trace.md`, *Preservation Hold lifecycle explainability*, below), at minimum: **Placement**
(requester, authorised Person, identity/confirmation used, stated purpose, scope, start time, review-due
time, applicable policy, affected record classes where known); **Review** (reviewer, date/time, outcome,
continuation/narrowing/release, reason, next review-due time if continuing); **Missed review** (overdue
state, notification/escalation if configured, continued preservation); **Release** (authorised releaser,
confirmation used, reason, release time, resulting preservation-state change); **Purge/truncation
skipped due to Hold** (affected record/reference, reason = Preservation Hold, resulting behaviour). Hold
metadata references governed records/subjects under existing canonical reference semantics; it does not
duplicate payload contents, copied communications, copied video/documents, or reconstructed actor
history merely to satisfy Explainability.

---

## Responsibility impact

| Responsibility/concept | Impact |
|---|---|
| Operational Trust | Unchanged, now fully specified: owns Hold authority (placement/review/release), policy, and is the sole owner of "who" |
| Each record-owning responsibility (Foundation, Truth, Stewardship, Continuity, Concierge, etc.) | Unchanged: each continues to own the marker on, and enforcement over, its own records |
| Stewardship | Unchanged; may help surface an overdue review via its existing obligation/notification pattern; does not gain Hold ownership |
| Connected Storage | Extended, not altered: Hold status must be discoverable at the storage/retention boundary (**DL-43**, **DL-45**, **DL-47** unchanged) |
| Decision Trace | Extended with Hold lifecycle explainability fields; **DL-82**'s provenance model and **DL-104**'s identity model are consumed unchanged |
| OD-36 (deletion-vs-preservation) | **Unblocked, not decided.** Now has placement/review/release authority, lifecycle, scope, and enforcement to build its precedence decision on |
| OD-40 (Evidence Package) | Unaffected; explicitly distinguished (§13) |
| OD-09 (erasure/portability) | Unaffected; a Hold's interaction with an erasure request is OD-36's, not decided here |
| OD-41 (Incident/Case model) | Unaffected; Incident scope remains optional convenience for this decision, never a dependency |
| OD-05 (Decision Trace retention floor/ceiling) | Unaffected; this ADR's Hold-related trace fields do not alter OD-05's own floor/ceiling question |

## Open decisions (not decided here)

- **OD-36** — deletion-versus-preservation precedence (this ADR's explicit boundary, §8).
- **OD-41** — Incident/Case object model (Incident scope remains optional per §4).
- **OD-40** — Evidence Package assembly/transport/integrity/audience (explicitly distinguished, §13).
- **OD-05** — Decision Trace retention floor/ceiling values (unaffected).
- Exact implementation of storage-boundary Hold discovery per connected-storage class (mechanics, not
  decided here; follows from §10's principle).

## Related documents

- [../governance/decision-ledger.md](../governance/decision-ledger.md) — **DL-132**, **DL-43**,
  **DL-45**, **DL-47**, **DL-71**, **DL-76**, **DL-97**, **DL-104**, **DL-109**
- [../models/temporal-record.md](../models/temporal-record.md) — *Preservation Hold*,
  *Transitive hold integrity*
- [../models/operational-trust.md](../models/operational-trust.md) — *Action-Risk Classes (DL-76)*,
  *Configuration Authority Composition (DL-109)*
- [../models/decision-trace.md](../models/decision-trace.md) — *Preservation Hold lifecycle
  explainability*
- [connected-storage.md](connected-storage.md)
- [failure-and-degradation.md](failure-and-degradation.md)
- [privacy.md](privacy.md)
- [../models/stewardship.md](../models/stewardship.md) — *Incomplete obligations are notification, not
  automatic escalation*
