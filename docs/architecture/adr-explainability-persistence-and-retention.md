# ADR: Explainability Persistence, Origins, and Retention

> **Document status: Canonical ADR.**
> Status: **Accepted** 2026-11-05. Records **DL-137** (issue **#77**, formal acceptance review PASS).
> Resolves **OD-05** in full.
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Terminology: [../models/glossary.md](../models/glossary.md), [../models/decision-trace.md](../models/decision-trace.md),
> [adr-governed-record-persistence-mechanism.md](adr-governed-record-persistence-mechanism.md).

---

## Status

**Accepted 2026-11-05.** Resolves every OD-05 Remaining Question, plus an Owner clarification of the
canonical relationship between **Decision Trace** and **Explainability Record**. This ADR creates **no
new responsibility**, **no second Home Assistant Recorder**, **no duplicate durable Decision-Trace-plus-
Explainability store**, and **no numeric retention default invented for its own convenience**. It does
not reopen **DL-15**, **DL-24**, **DL-27**, **DL-46**, **DL-47**, **DL-56**, **DL-76**, **DL-92**,
**DL-104**, **DL-114**, **DL-122**, **DL-129**, **DL-130**, **DL-132**, **DL-133**, or **DL-136** — each
is consumed unchanged.

---

## Context

**DL-47 already settled the rule**: a Decision Trace is governed explainability history following
External History Retention unless an accepted floor or a Preservation Hold applies, and holding a
trace preserves the governed source versions required to keep it explainable. **DL-47 also already
classified the exact numeric values as household configuration, not architecture** — "the trace floor
(**OD-05**)... and no universal retention matrix is required." What remained open was the floor itself
(how long a trace *must* be kept to satisfy **P27**/**DL-24**), the ceiling (how long it *may* be kept
under privacy minimization), and a terminology clarification the Owner has now supplied: the repository
must distinguish the governed *process* that produces an explanation (**Decision Trace**) from the
*persisted record* of its result (**Explainability Record**), and must formally recognize that an
explainability question answered on demand — even one that resolves to an identical answer asked
twice — is itself a new governed interaction producing its own new record, never a backdated or
deduplicated one.

---

## Decision

### 1. Decision Trace and Explainability Record — the canonical relationship

**Decision Trace** names the governed reasoning process: the evaluation that consumes Identity,
Truth, Stewardship, Continuity, and Operational Trust state and produces a decision, action,
non-action, suppression, refusal, disclosure, or escalation (`decision-trace.md`'s 21-field content
model, unchanged). **Explainability Record** names the persisted, durable governed record of that
process's result — the thing `decision-trace.md`'s "Persistence (resolved — DL-129)" section already
describes being written to Connected Storage. **These are not two stores.** There is exactly one
durable Explainability repository; a Decision Trace's governed content, once produced, becomes an
Explainability Record the moment it is persisted. **"Decision Trace" is not globally renamed** — it
remains the correct term for the reasoning/evidence/decision content itself, exactly as **DL-15**,
**DL-24**, **DL-27**, **DL-46**, and **DL-129** already use it, and none of those accepted decisions is
reopened or reworded. The clarification is narrow and additive: where those decisions say "the Decision
Trace is persisted," the precise meaning is "the Decision Trace's content is persisted as an
Explainability Record" — a distinction of **persistence ownership**, not of reasoning terminology.

### 2. Two canonical Explainability origins

Every Explainability Record identifies how it originated, using exactly two canonical values — no
third is invented:

| Origin | Produced when | Reuses |
|---|---|---|
| **`outcome_generated`** | HTBW performs a governed evaluation and produces an outcome (action, non-action, suppression, refusal, disclosure, escalation) | The ordinary write-time-assembled trace `decision-trace.md`'s Persistence section already describes |
| **`on_demand_decision_trace`** | A Person asks an Explainability question requiring research or reconstruction, and HTBW evaluates and answers it | `decision-trace.md`'s existing clause-10 "diagnostic explanation... persisted as an ordinary new record of a *current* diagnostic activity" (**DL-129**), formalized as a first-class origin rather than an optional byproduct |

**Answering an Explainability question is itself a governed evaluation.** **DL-15** already establishes
that a Decision Trace exists wherever, and only wherever, HTBW participates in a governed evaluation —
Concierge resolving authority, evaluating disclosure (**DL-34**, **DL-72**), assembling evidence, and
composing an answer is exactly such an evaluation, regardless of whether the answer cites a retained
`outcome_generated` record or reconstructs via **Category 7**'s diagnostic branch
(`explainability.md`). This is not a new architectural mechanism — it is **DL-15** applied,
consistently, to the act of answering rather than only to the act of acting.

### 3. Every on-demand invocation produces a new Explainability Record — never deduplicated

**Each time an on-demand Decision Trace is invoked, a new Explainability Record is created**, even
where: the historical question was asked before; the resolved historical scope is identical; the
resulting explanation is identical. Two such records are two legitimate governed interactions, each
with its own Record Identity (**DL-104**), Creation Time, request parameters, evidence basis, and
gaps — **never the same evaluation merely repeated in presentation.** **An earlier Explainability
Record is never overwritten, mutated into a later one, or silently returned as though no new
interaction occurred.** An existing retained record **may** be consulted as evidence/input to a new
on-demand request where current architecture permits (for example, citing a retained
`outcome_generated` record by Governed Reference), but **the request itself always produces its own
new record** — extending **DL-129** clause 10's "may be persisted" to "is persisted" for this origin
specifically, because an on-demand research interaction is now a first-class governed evaluation under
**DL-15** (§2), not an optional byproduct.

### 4. Request parameters are recorded

An on-demand Explainability Record preserves the governed parameters of the request, where available
and where current privacy architecture permits: requester; request timestamp; a governed-normalized
question representation (never a raw-conversation archive created merely to preserve exact wording —
reusing existing governed request/provenance mechanisms, **DL-113**'s Declaration/Request-Parameter
distinction, before inventing another record class); question class (`explainability.md`'s Episode 9
category mapping); resolved Subject; Room/Merged Room context; Asset; Person/Pet where authorized;
requested historical date/time; resolved historical interval; applicable correlation/causation scope
(**DL-104**); and the applicable Decision/automation/capability.

### 5. Record Creation Time and Historical/Effective Scope are distinct

**Record Creation Time** is when HTBW performed the on-demand Decision Trace and wrote the
Explainability Record. **Historical/Effective Scope** is the earlier event, interval, decision, or
non-action being examined — reusing `temporal-record.md`'s existing **Effective Time**/**Recorded
Time** bitemporal pair unchanged (§Bitemporality), never a third competing timestamp taxonomy. **An
on-demand Explainability Record is never backdated to make it appear created at the historical
event's own time** — restated directly from **DL-129** clause 10, generalized from the diagnostic case
to every on-demand record.

### 6. Timestamp convention — Home Assistant technical precedent, reconciled with DL-136

Canonical persisted creation time for a newly created Explainability Record follows Home Assistant's
own verified UTC convention (**DL-30**, Issue #146 item 16: Recorder/`.storage` timestamps are UTC).
Ambiguous locale-only timestamps are never persisted as canonical time. Presentation converts the
canonical UTC instant to the household's configured IANA timezone (Foundation's Home-level "temporal
conventions," `home.md`), and **DL-136**'s Temporal Portability Contract applies unchanged whenever an
Explainability Record is exported: canonical UTC instant, event-time-rule local civil representation,
and the IANA identifier together — never a fixed offset applied retroactively, and never increased
precision beyond what the source/provenance supports. No competing timestamp convention is invented.

### 7. SQLite is the default persistence technology for the Explainability repository

**Home Assistant's own Recorder uses SQLite as its default, verified embedded persistence engine**
(`home-assistant_v2.db`, confirmed in this repository's own Reference-Home evidence register). Following
this already-verified Home Assistant technical precedent (**DL-30**'s reuse-before-invention
discipline), **HTBW's own structured, growing Explainability repository uses SQLite as its default
persistence technology.**

**This is a distinct, separately owned database — never Home Assistant's Recorder database, and never
a second Recorder:**

| | Home Assistant Recorder Database | HTBW Explainability Database |
|---|---|---|
| Owner | Home Assistant | HTBW (Concierge-produced, Operational-Trust-governed) |
| Schema | Home Assistant's own, Home Assistant's own migrations | HTBW's own schema, HTBW's own migrations |
| Content | Native state/event/statistics history | Explainability Records (Decision Trace content, both origins) |
| Lifecycle | Recorder's own `purge_keep_days`, no per-record exemption | HTBW's own retention classification (§11), Preservation Hold (§13), erasure (§14) |
| Location | Home Assistant's own database file | Within the Explainability repository's own authoritative location (§8) |

**HTBW never writes HTBW-owned schema or tables into the Home Assistant Recorder database, and never
queries or writes the Explainability repository as though it were Recorder.** Native Home Assistant
history remains Recorder's own; Explainability references native evidence where appropriate (**DL-27**,
§10) and never duplicates it merely for convenience.

**This reconciles, and narrowly supersedes, one descriptive detail of DL-129 without reopening DL-129's
own holdings.** DL-129 described the Decision Trace as persisted as "one governed **JSON-backed**
record class per DL-92's already-accepted Storage-helper-based mechanism" — a description of what
DL-92's Storage helper naturally produces, not an independent constitutional commitment to JSON
encoding: **DL-92 itself explicitly states its own non-goals include "does not select database
technology, serialization format, or physical file layout... implementation mapping"** for every
record class it governs. Read in that light, DL-129's "JSON-backed" detail was illustrative, not a
foreclosure of SQLite. **DL-129's actual holdings are unchanged and not reopened**: Connected Storage
remains the authoritative durable location; the External History Retention (**DL-42**) extension
mechanism is unchanged; write-time assembly, Room normalization, and storage-outage independence all
apply identically regardless of whether the underlying file is a Storage-helper JSON blob or a SQLite
database. **This decision narrows only the physical encoding** for the Explainability repository
specifically, from the Storage helper's native JSON shape to SQLite, consistent with Home Assistant's
own technical precedent for exactly this kind of structured, growing, queryable record set.

### 8. Connected Storage location, Home Assistant Backup, and growth

The HTBW Explainability database resides within the Connected Storage governed namespace, reusing
**DL-129**'s already-accepted authoritative-location decision (Connected Storage, as the **DL-42**
External History Retention extension) — this decision does not relocate it. **Explainability is an
append-heavy, continuously growing governed record set, and this growth must never silently inflate
Home Assistant Backup without explicit architectural intent.** Restated, not newly invented,
from `connected-storage.md`'s existing Backup-scope section: **Connected Storage sits outside Home
Assistant's Backup boundary unless the deployment deliberately places it there, and that placement has
been verified** — this applies to the Explainability database precisely as it applies to every other
Connected Storage record. **Connected Storage backup coverage for the Explainability database must be
deliberately configured and verified by the household/deployment; it is never assumed included in an
ordinary Home Assistant Backup merely because the database happens to be reachable from the Home
Assistant host.** A multi-year Explainability history is therefore never a silent driver of Home
Assistant Backup size — restating the existing "a gap must be explainable" rule (`connected-storage.md`)
applied to this specific, newly significant growth vector. Database consistency, recovery, and restore
behaviour for the Explainability database follow the same unavailable/lost-after-creation rules already
established for every Connected Storage artifact (`connected-storage.md`, "When Connected Storage is
lost after artifacts exist") — no competing recovery model is introduced.

**This ADR does not over-design the SQLite schema.** It establishes required logical record semantics
only — Record Identity, Explainability Origin, Creation Time, request/historical-scope provenance,
explanation content, evidence references, gaps, retention classification, and Hold/erasure state (all
already stated in this document) — never specific tables, indexes, or migrations, which remain
implementation design following later, consistent with **DL-92**'s own "exact keys and schemas are
implementation mapping" discipline.

### 9. Source evidence is referenced, not duplicated

Restated from **DL-27**/**P30**, unchanged: an Explainability Record references exact governed
evidence/source versions, never copying full Recorder history, complete documents, full
Communications, raw sensor history, or external video merely because the reasoning consulted them. A
Preservation Hold may preserve the source versions required to keep a held Explainability Record
meaningful (**DL-47**, **DL-132**) — it never duplicates those payloads into the Explainability
repository itself. **No second history store is created by this decision.**

### 10. Published entity state and Recorder are not the Explainability source of truth

Restated from **DL-114**, unchanged: where HTBW publishes entity state or events into Home Assistant,
Recorder's retention of that published projection is a separate, native retention consequence —
**it does not become the Explainability source of truth**, and the governed Explainability Record
remains independently explainable from its own accepted evidence references regardless of what Recorder
does with the published projection. Where Recorder has purged the corresponding published-state
history, that native projection is reported as unavailable where relevant; **the Explainability Record
is never treated as invalid merely because Recorder's own, independently governed projection has since
expired.**

### 11. Retention — proportionate, not a single invented number

**DL-76's existing six Action-Risk Classes (Convenience, Disclosure, Financial, Safety, Security,
Governance) are reused to make retention proportionate, inventing no second, Explainability-only
classification system** (restating `decision-ledger.md` DL-76's own comment-2 evidence on this issue).
**Proportionality is expressed as an ordering constraint, never as an invented absolute duration**: a
decision class's configured Explainability retention floor must be no shorter than a lower-consequence
class's configured floor (Governance ≥ Security/Safety/Financial ≥ Disclosure ≥ Convenience, consistent
with **DL-76**'s own consequence ordering) — **HTBW assigns no specific day, month, or year value to
any class.** This generalizes **DL-76**'s already-accepted Capability-Default → HTBW-Default →
Household-Override tiering: the Capability-Default is the governed outcome's own Action-Risk Class
(already recorded, field 12–14 of the Decision Trace content model); the HTBW-Default is the
**ordering constraint** above (a relative rule, not a number); the Household-Override is the household's
own configured value per class, reusing **DL-122**'s already-accepted retention-duration-choice shape
(a hybrid of enumerated, human-understandable presets plus a custom numeric override), configured at
Integration-default/Room-override scope exactly as **DL-129** (comment 4 on this issue) already
anticipated.

**No numeric floor or ceiling value is invented by this decision.** **DL-47 already classified the
exact values as a household configuration matter, not architecture** ("the trace floor (OD-05)...
household configuration value, not architecture"); this decision does not relitigate that
classification, and does not choose 30, 90, or 365 days, or any other specific number, "merely because
they are common."

**The floor is a configuration requirement, not a configuration default.** Reusing **DL-47**'s own
"undeclared retention must not be accepted... undecided is not a retention strategy" discipline,
applied here to the floor specifically: **a configured Explainability retention floor of zero,
disabled, or unset is invalid and must be rejected by configuration validation**, because **P27**/
**DL-24** already establish that *some* retained explainability window is a constitutional
requirement — the household determines what counts as a sufficient floor for its own home, but it
may not configure "no floor" at all. This is the same **existence-requirement-without-an-invented-
value** pattern already accepted for Preservation Hold duration (**DL-97**, **DL-132**) — generalized
here to a case where the existence of a non-zero value is itself constitutionally required, which Hold
duration never was.

**The ceiling is household-configurable, Integration-default/Room-override** (**DL-122**'s pattern,
unchanged), bounded only by the floor relationship below; no HTBW-invented ceiling value is assigned
either.

**Floor/ceiling relationship**: a configured retention value must satisfy `configured retention >=
applicable floor` and `configured retention <= configured ceiling`. **A configuration attempting to
violate the floor is rejected by existing configuration-validation convention, never silently
accepted.**

### 12. Consent-lifecycle interaction does not become the whole record's ceiling

**Restated from DL-47's already-accepted structural-floor separation, not reinvented.** Where an
Explainability Record's Subject was a Person under consent, the record does **not** automatically
inherit that Person's full consent-lifecycle duration as the whole record's retention ceiling.
**DL-47**'s four structural floors already separate, in kind, the **consent-lifecycle proof** (that
consent existed, its scope, when it ended — a structural floor that survives any configured window)
from the **ordinary Explainability content** governed by this decision's own floor/ceiling — exactly
the separation **DL-56**, **DL-133**, and **DL-136** already apply elsewhere. **Consent withdrawal
reuses DL-56 unchanged**: it does not retroactively shorten an already-configured Explainability
ceiling; it governs only the person-association evidence within the record, per **DL-56**'s existing
rule.

### 13. Expiry and Tombstone

**When ordinary Explainability retention expires, the record is removed; no bounded "summary" that
effectively reproduces the expired explanation is retained unless another accepted structural floor
requires it** (restating §12's structural-floor exception, not widening it). **A Tombstone is required**
(`privacy.md`'s existing Tombstone model, **DL-136** unchanged): the Home must remain able to
distinguish *"an Explainability Record existed and expired/was deleted under retention"* from *"no
Explainability Record was ever created for this question/outcome."* **No indefinite shadow explanation
is created merely to soften an honest expiry.**

### 14. Preservation Hold

Restated from **DL-132**, unchanged: a Preservation Hold may suspend ordinary Explainability
expiration. Holding an Explainability Record preserves the governed source versions **DL-47** requires
to keep it explainable, without duplicating those payloads into the Explainability repository itself
(§9).

### 15. Deletion, consent withdrawal, and erasure

Restated from **DL-133** and **DL-56**, unchanged — no new conflict precedence is invented. Where an
Explainability Record becomes subject to erasure, this decision applies **DL-133**'s existing
minimization sequence, pending-deletion semantics, restricted-use preservation, Tombstone, and
Hold-conflict behaviour exactly as already accepted, and **DL-136**'s Erasure model (orchestrated
Governance-class authority, each responsibility's own existing deletion authority unchanged) applies to
Explainability Records precisely as to any other governed record class.

### 16. Both origins share one retention policy

**`outcome_generated` and `on_demand_decision_trace` records share the identical retention
architecture** (§11–§13). Origin is provenance, recorded on the record, never a retention
classification of its own. Neither origin is treated as inherently temporary or inherently permanent
unless a later, separately accepted governance decision explicitly establishes such a difference — none
does here.

### 17. New follow-on issue — HTBW Structured Data Persistence Placement Review

**This decision creates exactly one new governed issue, not executed here**: a repository-wide
classification of HTBW data by canonical persistence mechanism (Home Assistant native storage, Config
Entry/options, YAML, SQLite, Connected Storage Managed Content, or transient-only), inventorying at
least Integration/Person/Room/Merged-Room/Asset configuration, Stewardship obligations, Identity
configuration/Assertions, Truth Facts, Continuity state/preferences, Operational Trust policy,
Explainability records, Communications, Portability metadata, Tombstones, Preservation Hold metadata,
Home Steward/Household Knowledge Provider configuration, and document/Connected-Storage metadata. The
new issue is required because this question extends materially beyond Explainability and must not be
decided ad hoc per capability. **This decision's own SQLite choice (§7) is the first worked instance
that new issue's matrix will formalize, not a substitute for performing that review.**

---

## Responsibility impact

| Responsibility | Change |
|---|---|
| **Concierge** | Produces the Decision Trace for both origins; composes and persists the resulting Explainability Record |
| **Operational Trust** | Authorizes on-demand Explainability requests as Disclosure-class (**DL-76**, unchanged, per `operational-trust.md`'s existing Historical Retrieval authorization); owns the proportionality ordering constraint (§11); no new authority mechanism |
| **Foundation** | Owns the Home's temporal conventions (IANA timezone, unchanged) |
| **Each responsibility (Truth, Stewardship, Continuity, Identity)** | Continues to supply the content an Explainability Record references by Governed Reference, never copied |
| **Explainability repository (SQLite, Connected Storage)** | New default persistence technology for both Explainability origins; no new responsibility created |

---

## What this decision does not do

- Does not rename "Decision Trace" globally or reopen DL-15, DL-24, DL-27, DL-46, or DL-129.
- Does not create a second Home Assistant Recorder or write HTBW schema into the Recorder database.
- Does not create a duplicate durable Decision-Trace-plus-Explainability store.
- Does not invent a numeric retention floor or ceiling value.
- Does not reopen DL-76's Action-Risk Class enumeration, DL-122's retention-duration-choice shape,
  DL-132's Preservation Hold model, DL-133's deletion/preservation conflict model, DL-136's Portability/
  Erasure model, or DL-114's publishing/Recorder-consequence model.
- Does not design the Explainability SQLite schema in implementation detail.
- Does not execute the new persistence-placement issue it creates.

---

## Related documents

- [../governance/decision-ledger.md](../governance/decision-ledger.md) — DL-137
- [../governance/open-decision-issue-index.md](../governance/open-decision-issue-index.md) — OD-05
- [../models/decision-trace.md](../models/decision-trace.md) — Explainability Record, origins, retention
- [explainability.md](explainability.md) — Historical Explainability, Category 7
- [../models/temporal-record.md](../models/temporal-record.md) — Bitemporality
- [../models/operational-trust.md](../models/operational-trust.md) — Historical Retrieval authorization
- [privacy.md](privacy.md) — Tombstone model
- [connected-storage.md](connected-storage.md) — Explainability database, Backup-growth boundary
- [home-assistant-boundary.md](home-assistant-boundary.md) — DL-30 UTC evidence, DL-114
- [adr-governed-record-persistence-mechanism.md](adr-governed-record-persistence-mechanism.md) — DL-92
- [adr-data-portability-and-erasure-mechanics.md](adr-data-portability-and-erasure-mechanics.md) — DL-136
- [../models/glossary.md](../models/glossary.md) — Explainability Record, Explainability Origin
