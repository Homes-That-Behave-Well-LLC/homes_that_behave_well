# ADR: Data Portability and Erasure Mechanics

> **Document status: Canonical ADR.**
> Status: **Accepted** 2026-11-05. Records **DL-136** (issue **#78**, formal acceptance review PASS).
> Resolves **OD-09** in full.
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Terminology: [../models/glossary.md](../models/glossary.md), [../models/temporal-record.md](../models/temporal-record.md),
> [adr-evidence-package-governance.md](adr-evidence-package-governance.md),
> [adr-deletion-versus-preservation-reconciliation.md](adr-deletion-versus-preservation-reconciliation.md),
> [adr-preservation-hold-governance.md](adr-preservation-hold-governance.md).

---

## Status

**Accepted 2026-11-05.** Resolves every OD-09 Remaining Question. This ADR creates **no Export,
Portability, or Erasure responsibility**, **no central erasure store or service**, **no permanent
Portability Store**, and **no second Recorder or duplicate native history**. Operational Trust
continues to own disclosure and conflict-resolution authority; each responsibility continues to own
its own records, their deletion, minimization, and Hold-honouring; Concierge continues to orchestrate
interaction; Explainability continues to record why. **No claim of legal or regulatory effect is
introduced.**

---

## Context

A household must be able to take its data out (**portability**) and have it removed (**erasure**).
Neither mechanism was decided. Two verified facts constrain the answer: Home Assistant's native
History export is **entity-scoped and ungoverned** (**DL-30**, Issue #146 item 15/16; restated
[home-assistant-boundary.md](home-assistant-boundary.md)); and **Connected Storage sits outside
Backup scope** unless the deployment deliberately places it there and that placement is verified
(**DL-44**, [connected-storage.md](connected-storage.md)). Every governed record and artifact class
already declares its own retention and deletion trigger (**DL-43**, **DL-45**, **DL-47**); consent
withdrawal already deletes voiceprints and derived profiles (**DL-56**); a collision between deletion
and preservation is already resolved as a governed conflict (**DL-133**); and an Evidence Package is
already distinguished from comprehensive export (**DL-135**). What remained unresolved was the
portability export's own shape, the erasure request's own shape, and a previously undecided residual:
**honest temporal representation of an exported timestamp**, surfaced as live Owner/Reference-Home
evidence (§7, below).

---

## Decision

### 1. Portability, Erasure, and Evidence Package are three distinct governed operations

**Consumed from DL-135 unchanged, restated precisely for this decision's own boundary:**

| Operation | Shape | Owner of the question |
|---|---|---|
| **Evidence Package** | A curated, bounded account about a stated question, event, Subject, or purpose | **DL-135** (closed; not reopened) |
| **Portability Export** | A comprehensive governed export of every applicable record/artifact class within an authorized scope | **This decision (DL-136)** |
| **Erasure** | Removal of governed content within an authorized scope, reconciled against retention floors and Preservation Holds | **This decision (DL-136)**, consuming **DL-133** unchanged for conflict precedence |

*"What happened during Tuesday's water leak?"* is an Evidence Package question. *"Give me everything
HTBW holds about me that I am authorized to receive"* is a Portability Export question. An Evidence
Package is never a substitute for a Portability Export, and a Portability Export is never assembled
as though it were a curated account — it must account for **every** applicable governed class, not a
stated subset.

---

### 2. Portability Export unit and scope

**A portability request carries a governed scope, not one hard-coded unit.** Supported scope
dimensions, singly or in authorized combination: **Person**, **Home**, **Asset**, **Room or Merged
Room**, **responsibility or capability**, **record or artifact class**, **time/date range**, and a
**correlation identifier** where one already exists (**DL-104**). This reuses the existing Subject/
reference/query architecture — the same scope dimensions **DL-130** (Historical Retrieval) and
**DL-135** (Evidence Package) already support — rather than inventing a parallel scope model.

**Authorization determines permitted scope, never the requester's own convenience.** A Person
requesting "everything you hold about me" receives their own authorized scope; this does not
automatically widen to another Person's unrelated private content, and a household-governance request
may legitimately receive a broader scope only where existing Operational Trust authority already
permits it (§8). **"Home" scope is not a privacy override** (§9).

---

### 3. Export shape — assembled on demand, no permanent Portability Store

**A Portability Export is, in its first state, an on-demand governed projection assembled from
authoritative sources at request time** — exactly the same shape **DL-135** already established for
Evidence Package assembly, generalized here to a comprehensive rather than curated boundary. Lifecycle:

> **Governed request → authorization/scope determination → query authoritative sources → assemble
> export → generate Completeness Manifest → materialize a Transient Export Artifact if a durable
> delivery copy is requested → deliver → expire/delete HTBW's own transient delivery copy.**

**No permanent Portability Store, periodic export snapshot, or export-ready duplicate directory is
created.** Maintaining an always-current duplicate dataset would create competing retention, stale
authority snapshots, and unnecessary privacy exposure — restating **DL-135**'s own "no second
explainability model" discipline (**DL-46**) applied to portability.

---

### 4. Transient Export Artifact — the materialized delivery copy

**Materializing a durable delivery copy is an explicit, separately authorized action distinct from
assembly** — exactly **DL-135**'s Assembly/Materialization split, reused unchanged. The existing
Asset Intelligence predecessor's `export_inventory` pattern (write to a temporary location, return a
retrieval handle, self-delete shortly after) is **rank-4 evidence of a reusable shape, not a canonical
duration** (its 60-second interval is implementation history, never canonized here).

**No new artifact interaction model is required.** The existing `connected-storage.md` artifact
declaration (19-point checklist) already supplies everything a Transient Export Artifact needs; this
decision declares it as a **named artifact class** rather than inventing a parallel construct:

| # | Declaration | Transient Export Artifact |
|---|---|---|
| 1 | Artifact Type | Transient Export Artifact (a materialized Portability Export delivery copy) |
| 2 | Owning responsibility | The responsibility that owns the exported scope's Governing Parent (§14); **Operational Trust** authorises materialization itself |
| 3 | Creating capability | The Portability Export capability, orchestrated by **Concierge** |
| 4 | Required dependency | Connected Storage (**DL-41**); unavailable storage blocks materialization, never claims it |
| 5 | Storage class | Managed Content once materialized (below) |
| 6 | Anchor | The export's own authorized scope (Person, Home, Asset, Room, responsibility, record class, time range, or combination) |
| 7 | Governing parent object | The scope's own declared primary Subject anchor, falling back to the **Home** — reusing **DL-105**'s anchor-ownership rule exactly as **DL-135** already applies it (§14) |
| 8 | Parent Removal Behavior | Deleted when the Governing Parent is removed, subject to Preservation Hold/retention floor (**DL-45**, unchanged) |
| 9 | Interaction model | **Managed Content** while it exists (reachable only through the owning capability, never through storage browsing — **DL-44**) |
| 10 | Retention strategy | **Short-lived by design.** Household-configured duration, reusing **DL-122**'s already-accepted retention-duration-choice shape (a hybrid of enumerated, human-understandable presets plus a custom numeric override) rather than a hard-coded interval; a **Capability-Default → HTBW-Default → Household-Override** tier (**DL-76**, **DL-109**) supplies the default where unconfigured. **No specific numeric default is invented by this decision** — exact preset values are implementation/configuration-design detail, restating **DL-47**'s "job timing and cadence are implementation choices" discipline |
| 11 | Deletion trigger | Automatic expiry under its declared short retention, explicit household deletion, or Governing Parent removal |
| 12 | Consent effect | None directly; consent governs the underlying records it was assembled from, unchanged |
| 13 | Preservation Hold effect | A Hold on an **underlying source record** does not itself hold the Transient Export Artifact; **a separate decision to preserve the artifact itself requires its own explicit materialization under the ordinary artifact rules** — Hold authority over sources never automatically extends to a derived export copy (restating **DL-135**'s "materializing a package never places a Hold on its sources," applied in reverse) |
| 14 | Behaviour when Connected Storage unavailable before creation | Materialization does not proceed; the household is told plainly that a durable delivery copy could not be created, never that the export itself failed if assembly/manifest generation otherwise succeeded |
| 15 | Behaviour when storage is lost after creation | Reported as an ordinary **DL-41** dependency outage; the artifact's retrieval is `unavailable`, never silently vanished without report |
| 16 | Historical/explainability requirements | The Completeness Manifest (§5) and the Portability Decision Trace (§15) remain reconstructable independent of the artifact's own short lifetime |
| 17 | Access restrictions | Retrievable once, by the authorized requester only, never a public or anonymous link absent a separately accepted equivalent control (restating **DL-135**'s transport discipline) |
| 18 | Integrity/version requirements | Carries the same Completeness Manifest (§5) that accompanied assembly; **never regenerated silently on retrieval** — a later request produces a new artifact, never a mutated one |
| 19 | Recovery/reconciliation | None required; an expired or lost Transient Export Artifact is simply re-requested — it was never the sole record of anything |

**This is not a Portability responsibility.** The artifact's governance lives with the responsibility
that owns its Governing Parent, exactly as every other artifact class already works.

---

### 5. Completeness Manifest — mandatory, honest, never silently partial

**"Comprehensive" means every applicable governed record/artifact class resolves to a stated outcome
— not that every class produces a payload.** Every portability export carries a canonical
**Completeness Manifest** recording, at minimum: export identity; generation timestamp (§7); requester;
authorized scope; schema/version; HTBW version where applicable; Home/timezone context where
applicable; every record/artifact class evaluated, each resolved to exactly one of:

| Outcome | Meaning |
|---|---|
| **Included** | The class's payload is present in the export |
| **Included by reference** | The class is represented by Governed Reference/provenance, not copied payload (reuses **DL-27**/**DL-46**'s "references, not copies" discipline for any class this decision would otherwise have to duplicate, such as Decision Trace-cited Truth Facts) |
| **Excluded by requested scope** | The class exists but was not within the authorized/requested scope |
| **Withheld by policy** | The class exists but is not disclosable to this requester/audience (§8–9) |
| **Unavailable** | The class's source (commonly Connected Storage) could not currently be reached |
| **No longer retained** | The class's content was purged under its own accepted retention |
| **Deleted / Tombstoned** | The class's content was removed under an erasure request; a Tombstone remains (§14) |
| **Unsupported by native source** | The native platform does not expose the requested class in governed form (for example, raw native History rows — §11) |
| **No responsive records** | The class applies in principle but no record currently exists for this scope |

**No class is silently omitted.** An export whose manifest demonstrates a gap is preferred over a
false claim of completeness — restating **DL-97**'s "an honest partial answer over an invented
complete one" discipline, generalized here from a numeric default to export completeness.

---

### 6. Machine-readable representation is required; human-readable rendering is optional and supplementary

**Portability must not depend solely on a human-readable rendering.** The logical export model —
records, relationships, provenance, Tombstones, Decision Trace references, artifact references, and
temporal metadata (§7) — is defined at the **semantic** level first; physical file format is a later,
evolvable choice. **No single physical format is locked in by this decision**: CSV may remain a useful
optional representation for tabular subsets; a structured format (whatever current implementation
mapping selects) may carry richer relational/provenance content; a human-readable index/summary
rendering may additionally be offered, but **must never substitute for, or degrade, the machine-
readable canonical representation and its provenance**. The schema itself carries its own identity/
version, so future evolution is possible without this decision promising round-trip import, backup
equivalence, or system restoration (**Export ≠ Backup ≠ Clone ≠ Restore Image** — restated explicitly
so the distinction is never assumed away, §16).

---

### 7. Temporal Portability Contract

**This is the one residual this decision adds beyond assembling existing mechanisms**, prompted by
live Owner/Reference-Home evidence (below) that was not previously reconciled anywhere in canonical
architecture.

#### 7.1 The evidence

In the Reference Home, Home Assistant's own Recorder and `.storage` timestamps are **verified UTC**,
and the household's configured time zone is an **independently stored, verified IANA identifier**
(`core.config`, `"time_zone": "America/Chicago"`) — already recorded as **DL-30** platform evidence
(`home-assistant-boundary.md`, "UTC and household-local timestamp normalisation," item 16) and already
the direct cause of a real investigative defect once, when a resident-reported local time was compared
against raw UTC evidence without conversion. **That finding already states a resident-facing
explanation requirement** (`explainability.md`); **it was never previously extended to the export/
portability surface**, where the identical hazard reappears: *the time a person saw in the Home
Assistant UI and the time present in a raw export may represent the same instant while appearing
different.* This decision extends that already-accepted principle to portability, and completes the
explainability cross-reference the DL-130 Notes narrative already anticipated (§22). **This is
Reference-Home production evidence for one deployment, not a universal guarantee that every Home
Assistant installation's clock, NTP synchronization, or timezone configuration is correct** — the
contract below states what HTBW must do with whatever temporal information its sources actually
supply, honestly, never what every possible source is assumed to supply.

#### 7.2 The contract — reusing, not duplicating, the existing bitemporal model

**temporal-record.md's existing Effective Time / Recorded Time pair is reused unchanged as the
semantic backbone** (§Bitemporality); this decision adds no competing timestamp taxonomy. One further,
narrow, export-specific concept is introduced because it describes the export *operation* rather than
a record field: **Export Generation Time** — when the portability artifact itself was assembled,
**always distinct from, and never confused with, the Effective Time or Recorded Time of any record it
contains.**

For every exported timestamp that is materially relevant, the export preserves — **where the source
genuinely supplies it** —:

| Element | Content | Rule |
|---|---|---|
| **Canonical instant** | The UTC instant (reusing Effective Time/Recorded Time's own value, expressed in UTC) | Preserved wherever the source value is known, for reliable machine correlation |
| **Local civil-time representation** | The same instant rendered in the **timezone rules applicable at that event's own time** | **Never** the export-generation day's offset applied retroactively; a historical event uses the Daylight-Saving/standard-time rule in force *when it occurred*, not when it was exported |
| **IANA timezone identifier** | The specific zone (for example `America/Chicago`), reused directly from the already-verified Foundation-owned Home configuration (`home.md`'s "temporal conventions... time zone handling") where that zone governs the event, or the record's own documented source zone where different | **Never** reduced to a fixed numeric UTC offset, because the same zone's offset varies by date (Daylight Saving Time) |

**Precision is never fabricated or increased.** If a source supplies a date only, minute resolution,
second resolution, millisecond resolution, an estimated time, or a derived interval, the export states
exactly that — reusing the already-accepted **observed / derived / inferred / estimated / unknown**
distinction (**DL-129**'s Historical Reconstruction precedent, applied here to export fidelity rather
than invented anew).

**Unknown or unavailable temporal context is reported honestly, never fabricated:**

| Scenario | Required behaviour |
|---|---|
| **UTC-known, source timezone unknown** | Preserve the UTC instant; do **not** fabricate a source timezone; a household/Home-timezone rendering may be offered only if clearly labelled as a *derived presentation*, not the source's own context |
| **Local-time-known, no trustworthy UTC conversion available** | Preserve the raw local representation and its provenance; do **not** invent a canonical UTC instant; mark canonical conversion as unavailable/uncertain |
| **Imported historical record from a different source/timezone** | The original local time is **never reinterpreted using the current Home's timezone** unless architecture explicitly identifies a derived Home-local view as such — restating **DL-129**'s "never retroactively invent a transition" discipline applied to time-zone reinterpretation |
| **Differing source precision across classes in one export** | Each class's own precision is preserved as-is; precision is never harmonized upward across the export |

**Source temporal inconsistency is surfaced, never silently smoothed.** Where sources disagree or
supply incompatible precision, the Completeness Manifest records the original/source representation,
the normalized/canonical interpretation applied (if any), whether timezone context was known, the
precision, and any assumption that interpretation required — or states that no assumption was made and
the value is reported as unknown.

**The export's own generation time is never confused with a contained record's own timestamp.** The
Completeness Manifest states the Export Generation Time in canonical form plus the Home's applicable
local representation, separately from every record-level timestamp.

#### 7.3 Ownership

**Foundation** already owns "temporal conventions (timestamps, validity windows, time zone handling)"
at the Home level (`home.md`); this decision adds no new owner. **Truth** (or the owning responsibility
of the specific exported record class) owns the record's own Effective Time/Recorded Time/precision/
provenance, unchanged. **Concierge** assembles the export and states the Export Generation Time.
**No Temporal/Timestamp responsibility is created.**

---

### 8. Portability authority — export is disclosure

**Export is itself a disclosure, evaluated exactly as any other disclosure (DL-34), never merely
authenticated.** Authority is evaluated at request/assembly time, reusing **DL-71**'s existing
Intended-Audience-Specification forms (Named Person, Role/Authority Class, Relationship-based, Anyone
Present With Authority, Household) to determine **who may request**, and **DL-76**'s Action-Risk
Classification plus its Capability-Default → HTBW-Default → Household-Override tiering (identical to
**DL-135**'s own mechanism, reused verbatim rather than reinvented) to determine **how strongly gated**
each operation is:

| Operation | Risk Class | Default Required Identity Band / Confirmation Strength (DL-76) |
|---|---|---|
| **Assembly** (constructing the projection, no durable artifact) | **Disclosure** (default) | Moderate / Verbal |
| **Materialization** (creating the Transient Export Artifact) | **Disclosure**, with the same capability-specific **Authenticated**-confirmation override **DL-135** already established for materializing any durable artifact from a projection | Moderate / Authenticated |
| **External recipient / transport** (the export leaves HTBW governance) | **Governance** | Very High / Strong |

**Requester authority ≠ recipient authority ≠ transport authority** — restated verbatim from **DL-135**
for the export case. A household member's own right to obtain a copy of their authorized scope does
not itself authorize handing another Person's private content, or content outside the requester's own
scope, to an arbitrary external recipient. **No native Home Assistant administrator flag, by itself,
grants portability authority over another Person's data** (restating **DL-56**/**DL-57**'s "an
administrator flag confers no care, guardianship, or proxy authority" unchanged).

---

### 9. Self-data and shared records

**A Person-scoped export encountering another Person's private content never silently discloses it,
and never strips context until the record becomes meaningless.** Existing privacy/minimization rules
govern exactly as they already do elsewhere: where authorized, include the requester's own authorized
portion; where not, apply **field-level redaction** (`privacy.md`) rather than removing the whole
record, and state a **withheld-by-policy** marker with the reason class (never a silent omission).
**"Home" scope is not a privacy override** (§2): a whole-Home export, where current Operational Trust
authority permits one at all, applies the identical per-Person disclosure restrictions a narrower
export would — breadth of scope never substitutes for authorization.

**Redaction never fabricates a false historical narrative.** Removing a value must never convert
*"something changed but the value is withheld"* into *"no change occurred"* — restated directly from
`privacy.md`'s field-level-redaction rule, applied here to export content specifically.

---

### 10. Decision Traces within a Person-scoped export

**A Person's own contribution to another Person's Decision Trace is handled exactly as DL-133 already
requires, never reinterpreted.** Minimization is attempted first; full payload is retained only where
an accepted structural floor genuinely requires it (`decision-trace.md`'s existing floors: Tombstones,
consent-lifecycle records, Preservation Hold, governed versions required to keep a held trace
explainable); any content preserved solely because of a conflict remains **restricted to that
purpose** (**DL-133**). **A Person's export is never used to rewrite history**: a trace correctly
recording that the Person participated remains correct, subject only to the same minimization/
Tombstone rules that would apply regardless of whether an export was ever requested. "History" is
never used as justification for disclosing another Person's protected content beyond what this
Person's own authorized scope already permits.

---

### 11. Native History export, Backup, and Connected Storage boundaries

**Restated from already-verified DL-30 evidence, not rediscovered:**

- **Native Home Assistant History export is entity-scoped and ungoverned** — it exports state rows,
  not governed HTBW meaning, and applies no HTBW authority filtering. It is consulted as native
  evidence where applicable (reported **unsupported by native source** or **included by reference**
  in the Completeness Manifest, §5) but is **never treated as the complete HTBW portability
  mechanism**, and HTBW **never duplicates native history merely to claim ownership of the export**
  (restating **DL-46** unchanged).
- **Home Assistant Backup is not portability.** Backup exists for system recovery; it may not include
  Connected Storage depending on deployment; it is not authority-filtered Person portability; and it
  is never presented as the household's portability mechanism, nor as a substitute for erasure
  (restated from `connected-storage.md`'s Backup-scope section, unchanged).
- **Connected Storage in-scope content must be accounted for.** Where Connected Storage is
  unreachable at assembly or materialization time, the affected class(es) are reported **unavailable**
  in the Completeness Manifest — never silently omitted, and the export is never claimed complete.
  Where materialization itself requires Connected Storage and storage is unavailable, the artifact is
  **not** claimed created (§4, item 14).

---

### 12. Erasure is distributed — no central Erasure responsibility, store, or service

**Restated and generalized from DL-45/DL-56/DL-133, never replaced.** Operational Trust authorizes
and governs the erasure request as a whole; Concierge or existing orchestration coordinates it across
responsibilities; **each responsibility owns its own records, performs its own deletion, redaction, or
minimization, writes its own Tombstone/lifecycle evidence, applies DL-133's conflict behaviour where
applicable, and reports its own result** — no central erasure store, erasure database, or global
delete-everything bypassing responsibility ownership is created. **Identity** continues to own its own
consent-specific material and lifecycle (**DL-56**, unchanged).

**The overall orchestrated erasure request — the household-facing act of asking "remove me" or "remove
this Asset" across every applicable responsibility — is itself a Governance-class action (DL-76):
Very High identity band, Strong confirmation**, by direct analogy to **DL-132**'s Hold placement/
release and **DL-133**'s Conflict-Resolution Authority (both already Governance-class for the
identical reason — an irreversible, high-consequence governed action). This governs the **orchestrated
request itself**, never each responsibility's own already-accepted internal authority for ordinary,
unconflicted deletion within its own domain (for example, **DL-56**'s existing consent-withdrawal
authority), which continues to apply unchanged and is never additionally gated by this new Governance-
class requirement.

---

### 13. Erasure unit and scope

**An erasure request carries a governed Subject/scope**, matching the same dimensions already
supported for portability (§2): Person, Asset, Room, governing parent, record class, artifact class, a
specific record, a responsibility/capability, or an authorized combination. **A Person erasure request
never automatically deletes another Person's records, shared household records, records structurally
required for Explainability, or records under an unresolved valid conflict** — reusing **DL-133**'s
record/obligation-level resolution model, never a blanket cascade.

---

### 14. Delete, Redact/Minimize, Tombstone, Pending Cleanup, and Preserve-Restricted are distinct

**No new taxonomy is invented; the existing vocabulary across DL-45, DL-56, DL-133, and `privacy.md`
is consolidated here into one erasure-result vocabulary, never collapsed:**

| Term | Meaning | Source |
|---|---|---|
| **Delete** | Payload/record removed according to its own declared lifecycle | DL-43, DL-45, DL-47 |
| **Redact / Minimize** | Protected fields or content removed while a surviving governed record remains where architecture permits | `privacy.md` field-level redaction |
| **Tombstone** | Governance evidence that something existed and was removed; never reconstructs the deleted payload | `privacy.md`, `temporal-record.md` |
| **Pending Cleanup** | A deletion obligation exists but cannot yet complete (storage unavailable, or a conflict is active) | DL-45 |
| **Preserve-Restricted** | A DL-133 conflict outcome where payload is retained solely under an active Preservation Hold's own stated purpose | DL-133 |

**These compose into DL-133's own four household-facing outcome shapes** (restated verbatim, never
reopened): **A — Deleted**; **B — Pending (preservation conflict)**; **C — Partial/minimized**; **D —
Technically unavailable/pending reconciliation**. **Silently doing nothing is prohibited** in every
case. The **Erasure Result Manifest** (§21) records, per class/item, exactly one of: deleted; redacted/
minimized; tombstoned; preserve-restricted; pending cleanup; technically unsupported; excluded by
scope; no responsive records — **never a parallel, incompatible status set**.

---

### 15. DL-133 governs every retention-floor/Preservation-Hold collision — not reopened

**OD-09 invents no new precedence.** Every collision between an erasure obligation and a retention
floor or Preservation Hold is resolved exactly as **DL-133** already requires: the collision becomes a
governed conflict (never a blind universal winner); minimization is attempted first; any payload
retained is restricted to the Hold's stated purpose; the deletion obligation remains **pending, never
lost**, until the conflict resolves; Hold release **reactivates** the pending obligation automatically,
so **the Person never has to ask again**; a late-placed Hold is subject to **DL-133**'s existing
anti-abuse rule; and the resulting Tombstone/Person-facing disclosure follows **DL-133** and
**DL-132**'s existing rules ("Hold existence is itself governed information," disclosed only to the
degree the requester's own authorization permits).

---

### 16. Consent withdrawal and Parent Removal are consumed unchanged

**DL-56 is not relitigated.** Where a consent-specific deletion rule already exists (voiceprints,
derived identity profiles, temporary enrollment samples deleted on withdrawal; the surviving consent-
lifecycle record never sufficient to reconstruct deleted material), this decision reuses it directly
and generalizes only the **separation-in-kind principle** (deleted material versus surviving lifecycle
proof) to erasure broadly — the specific consent example is not reopened.

**DL-45 is not relitigated.** Parent-object cleanup remains distributed by owning responsibility and
artifact class; **this decision does not become a global cascade-delete engine**; preservation floors
and conflicts are evaluated before final deletion exactly as **DL-45** already requires, with
reconciliation against floors/Holds owned by **DL-133**.

---

### 17. Export-then-erasure sequencing

**Portability is not a mandatory precondition of every erasure request.** But where a household asks
for both — "give me a copy, then remove it" — the two governed operations are sequenced coherently:
(1) the authorized portability export completes to the extent technically possible; (2) the export's
own completeness result is stated honestly (§5); (3) erasure then proceeds under its own governance
(§12–§16). **Erasure is never performed first, discovering afterward that the requested copy can no
longer be assembled.** Where current authority prohibits exporting certain content to this requester,
erasure is **not delayed** merely to produce an export that was never authorized in the first place.

**A Transient Export Artifact must never become an erasure loophole.** Its own short declared
lifecycle (§4) continues to apply regardless of a subsequent erasure request; where current retention
rules require earlier removal, the artifact is removed accordingly; **no permanent export archive
survives an erasure merely because an export was previously generated.** HTBW cannot guarantee deletion
of copies already delivered outside its own governance (§18) — the household is told this honestly,
never promised an impossible remote erasure.

**Export does not imply a Hold, and erasure does not imply a Hold release.** These remain entirely
separate governed operations; neither is auto-created nor auto-triggered by the other.

---

### 18. External delivery boundary

Restated directly from **DL-135**'s own external-export boundary, applied identically here: **HTBW
can govern** the request, contents, authority, delivery mechanism, recipient (where applicable), and
the Transient Export Artifact's own lifecycle. **Once an export has transferred outside HTBW's own
governance, HTBW cannot guarantee downstream deletion, forwarding restrictions, copies, screenshots,
recipient retention, or redistribution.** This limitation is disclosed honestly to the household,
never minimized or implied away.

---

### 19. Home Steward and external-source boundary

**Access to an external knowledge source through Home Steward never becomes HTBW ownership of that
entire source.** Portability and erasure concern information HTBW/Home Steward actually governs and
retains under this architecture — not an arbitrary copy of every external system Home Steward can
query. HTBW does not assume authority to export or erase a connector's or provider's own source system
merely because Home Steward can reason over authorized content from it; source ownership and connector
boundaries are preserved unchanged (consistent with **DL-131**'s Home Steward product boundary and the
existing Communications-source discipline below).

**Communications and other externally sourced references are handled identically.** Where HTBW holds
governed Communication records or references, those records are exported/erased according to their own
scope and authority; HTBW does not assume ownership of, or export authority over, an external mailbox
or source system merely because HTBW references correspondence from it.

---

### 20. Backup is not portability (restated)

**Home Assistant Backup answers "give me my backup," never "give me my export."** Where a household
requests portability and is offered Backup instead, that substitution is incorrect: Backup is for
system recovery, may omit Connected Storage, is not authority-filtered Person portability, and is not
a substitute for erasure (§11, restated for emphasis because Remaining Question 7 names it explicitly).

---

### 21. Result manifests — Completeness Manifest (export) and Erasure Result Manifest

Both manifests answer the household's own question honestly and are never a format the household must
interpret technically:

- **Portability**: *"What did I actually receive?"* — answered by the **Completeness Manifest** (§5).
- **Erasure**: *"What did you actually remove?"* — answered by the **Erasure Result Manifest** (§14),
  per responsibility/class/item: deleted; redacted/minimized; tombstoned; preserve-restricted; pending
  cleanup; technically unsupported; excluded by scope; no responsive records.

**No parallel status taxonomy is invented for either manifest** beyond what §5 and §14 already state.

---

### 22. Explainability and Decision Trace

**Portability** produces governance evidence capturing, at minimum: requester; authorized scope;
authority/Risk-Class applied (§8); requested classes; included/excluded/withheld/unavailable items
(§5); temporal representation applied (§7); generation result; delivery result; and any external-
boundary warning given (§18). **Erasure** produces governance evidence capturing, at minimum:
requester/subject; scope; authority/Risk-Class applied (§12); each responsibility/class contacted and
its own result (§14); conflicts encountered and their **DL-133** resolution; storage outages
encountered; and the final household-facing result. **Neither trace copies the exported or deleted
payload itself** — restating `decision-trace.md`'s "references, not copies" discipline unchanged.

**This decision completes a cross-reference the DL-130 Notes narrative already anticipated but never
finished stating**: `explainability.md`'s existing "Relevant timestamps or validity periods"
requirement is now explicit that a resident-facing or exported timestamp must carry household-local
context derived from the Home's own verified configuration (§7), never raw UTC alone and never a
newly-invented universal guarantee about every deployment's clock accuracy.

---

### 23. Dependency reconciliation — mechanics are separable from numeric retention values

**Consumed and reconciled against current state, not assumed stale:**

- **OD-36** (deletion versus preservation) is **closed as DL-133** and consumed unchanged (§15).
- **OD-40** (Evidence Package) is **closed as DL-135** and consumed unchanged (§1).
- **OD-26** (Experience History retention) is **closed as DL-122**; its retention-duration-choice shape
  is reused for the Transient Export Artifact (§4).
- **OD-01** (governed-record persistence shape) is **closed as DL-31/DL-92**; this decision invents no
  competing persistence mechanism.
- **OD-05** (Decision Trace retention floor/ceiling) and **OD-49** (Communication retention floor/
  ceiling, content-versus-metadata classification) **remain open, and this decision does not wait on
  them.** **DL-47** already established the controlling precedent this decision applies directly:
  retention **mechanics** (that a class declares retention, has a floor, has a ceiling, honours
  structural floors) are architecture; the **numeric values** themselves are household configuration,
  decided independently. A portability export or erasure request against a Decision Trace or
  Communication record applies **whatever retention mechanics DL-47/DL-122/DL-129 already establish**
  for that class, using its currently configured values (or reporting them as unconfigured, where
  applicable) — it does not require OD-05/OD-49's own numeric values to be fixed first, and does not
  fix them here.

**The issue's own prior "Blocked by OD-05, OD-36, OD-49" status is corrected**: OD-36 is resolved;
OD-05/OD-49 block only the numeric values those specific classes will eventually use, never OD-09's own
mechanics.

---

### 24. Governing Parent for a materialized Transient Export Artifact

Reusing **DL-105**'s anchor-ownership rule exactly as **DL-135** already applies it: the Governing
Parent is the export's own declared primary Subject anchor (Person, Asset, Room/Merged Room, or Pet)
where the requested scope is sufficiently narrow to distinguish one, falling back to the **Home** where
the scope spans multiple Subjects or is itself whole-Home. **The scope's own Incident context, if any,
is never the Governing Parent** (**DL-134**, unchanged).

---

## Responsibility impact

| Responsibility | Change |
|---|---|
| **Operational Trust** | Gains the Portability authority mapping (§8) and the Governance-class orchestrated-erasure-request authority (§12); no new authority mechanism |
| **Foundation** | Confirmed owner of the Home's temporal conventions (§7.3) and of the Transient Export Artifact's Governing Parent anchor rule (§24); no change |
| **Concierge** | Orchestrates portability assembly/materialization/delivery and erasure-request coordination across responsibilities; no new responsibility created |
| **Each responsibility (Truth, Stewardship, Continuity, Identity, Foundation, Operational Trust)** | Continues to own its own records' export representation and deletion/redaction/Tombstone behaviour under its own already-accepted rules |
| **Identity** | Continues to own consent-specific material/lifecycle (**DL-56**) unchanged |
| **Explainability** | Gains two new governed trace shapes (§22); no new persistence mechanism |

---

## What this decision does not do

- Does not create an Export, Portability, or Erasure responsibility.
- Does not create a central erasure store, erasure database, or global cascade-delete mechanism.
- Does not create a permanent Portability Store or export-ready duplicate dataset.
- Does not reopen DL-43, DL-45, DL-47, DL-56, DL-76, DL-92, DL-104, DL-122, DL-129, DL-130, DL-132,
  DL-133, DL-134, or DL-135.
- Does not decide OD-05's or OD-49's own numeric retention values.
- Does not claim legal, regulatory, or forensic effect for any export or erasure record.
- Does not promise import/restore compatibility for any export format.
- Does not expand Home Steward's or any connector's export/erasure authority beyond what HTBW itself
  governs and retains.

---

## Related documents

- [../governance/decision-ledger.md](../governance/decision-ledger.md) — DL-136
- [../governance/open-decision-issue-index.md](../governance/open-decision-issue-index.md) — OD-09
- [../models/temporal-record.md](../models/temporal-record.md) — Bitemporality, Portability Export, Erasure
- [../models/operational-trust.md](../models/operational-trust.md) — Portability and Erasure authority
- [../models/decision-trace.md](../models/decision-trace.md) — Portability and Erasure explainability
- [privacy.md](privacy.md) — Deletion and export
- [connected-storage.md](connected-storage.md) — Transient Export Artifact, Backup scope
- [home-assistant-boundary.md](home-assistant-boundary.md) — Native History export, Recorder, Backup, UTC/timezone evidence (DL-30)
- [explainability.md](explainability.md) — Resident-facing temporal representation
- [adr-evidence-package-governance.md](adr-evidence-package-governance.md) — DL-135
- [adr-deletion-versus-preservation-reconciliation.md](adr-deletion-versus-preservation-reconciliation.md) — DL-133
- [adr-preservation-hold-governance.md](adr-preservation-hold-governance.md) — DL-132
- [../models/glossary.md](../models/glossary.md) — Portability Export, Erasure Request, Transient Export Artifact
