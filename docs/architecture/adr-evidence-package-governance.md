# ADR: Evidence Package Governance

> **Document status: Canonical ADR.**
> Status: **Accepted** 2026-11-05. Records **DL-135** (issue **#86**, formal acceptance review PASS).
> Resolves **OD-40** in full.
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Terminology: [../models/glossary.md](../models/glossary.md), [../models/temporal-record.md](../models/temporal-record.md).

---

## Status

**Accepted 2026-11-05.** This ADR creates **no new responsibility, no Evidence Package store, no
Incident/Case store, no second Recorder, and no investigation store.** Concierge continues to own
assembly orchestration and its own Decision Trace; Operational Trust continues to own who may assemble,
materialize, and receive; each responsibility continues to own the records a package references; Truth
continues to own the Facts referenced. A materialized Evidence Package is **Managed Content** (**DL-44**)
with a full **DL-43** artifact declaration, never a second store.

---

## Context

**DL-130**, **DL-132**, **DL-133**, and **DL-134** are each consumed unchanged: ordinary retrieval,
Preservation Hold placement, a deletion/preservation conflict resolution, and Incident scope
construction each explicitly never automatically create an Evidence Package. What remained undecided
was assembly, boundary, integrity representation, authority, audience, transport, Governing Parent, and
lifecycle for the package itself.

---

## Decision

### 1. Projection by default, materialization by explicit request (Remaining Question 1)

**An Evidence Package begins as an on-demand, audience-governed projection.** Assembly occurs only
through a governed household request for a coherent representation of a bounded event or question
(*"show me what we know about the water-damage event"*). This creates a projection — it does **not**
automatically create a file, ZIP, PDF, archive, persistent package, package folder, Incident object,
Case, Preservation Hold, or any retention obligation beyond the underlying sources. **Assembly is never
triggered merely because** Historical Retrieval occurred, an Incident scope exists, an unknown actor
appears, a Preservation Hold exists, a deletion/preservation conflict exists, Concierge judges an event
important, a safety condition occurred, or an automation fired.

**A durable Evidence Package artifact is created only by an explicit, separately authorized
materialization request** (*"save this package," "prepare a copy for my insurer"*). Projection and
materialized artifact are distinct lifecycles, never blurred:

| | Projection | Materialized Evidence Package |
|---|---|---|
| Assembled | On demand | On explicit, separately authorized request |
| Retained | Not retained by default | Yes — new governed artifact |
| Interaction model | None (transient) | **Managed Content** (**DL-44**) |
| Declaration | None required | Full **DL-43** artifact declaration |
| Governing Parent | N/A | Required (**DL-45**, §6 below) |
| Lifecycle | None | Its own retention/deletion lifecycle (§7) |

Concierge may orchestrate assembly according to its existing responsibility boundaries; it does not
own the underlying records or gain a new ownership class by doing so.

### 2. Boundary (Remaining Question 2)

A package's boundary is a combination of, as needed — reusing **DL-130**'s historical-query dimensions
and **DL-134**'s Incident scope, inventing no new dimension: time/time range; Room/Merged Room/spatial
scope; Asset; Person/Pet where authorized; Decision/Decision Trace; Communication; Domain Event; Truth
Fact; Correlation Identity; Causation Identity; specific governed records; authorized external
references; explicit inclusion/exclusion criteria. **An Incident scope (DL-134) may provide a
convenient bounded-event representation for the boundary; Incident remains unpersisted and is never the
package's Governing Parent** (restating DL-134 unchanged).

### 3. Curated content, not a raw dump

A package is the **minimum coherent account required for the authorized purpose**, never an
indiscriminate copy of every record in range. Potential contents: scope definition; generation time;
requester; intended audience/recipient; relevant Truth Facts/provenance; relevant Decision Traces;
supported correlation/causation; conclusions; alternative interpretations/hypotheses; uncertainty;
missing/unavailable/purged evidence; withheld-by-policy markers; consulted/unconsulted-source status;
explicit exclusions; authorized external references; generation provenance. **Comprehensive raw-history
export remains OD-09's own** (data portability); an Evidence Package is never used as a substitute for
it.

### 4. Gaps and uncertainty are in the package itself

**A package containing an unreported material gap is defective.** It states, where applicable: known
gaps; missing/purged/unavailable/inaccessible/withheld-by-policy records; and next-evidence guidance
reusing **DL-134**'s six states unchanged (consulted/no result; exists/not consulted; unavailable; does
not exist, where known; existence cannot be disclosed; no further authorized source known — *"there is
nothing further to examine"* is a valid, complete answer). **Naming a source never asserts its
contents; identifying a source and retrieving it remain separately governed acts** (restating DL-134
unchanged). Additional private evidence is never automatically retrieved merely to make the package
look more complete.

### 5. Externally owned media and Unknown Actor References (DL-35 preserved)

Restating `temporal-record.md`'s *Externally owned video and camera evidence* unchanged: externally/
natively owned video is **referenced, never copied** merely because a package exists; a referenced clip
is never asserted to depict a Person/actor absent accepted supporting evidence; no identity, role,
intent, or criminality is inferred. An included Unknown Actor Reference remains package/reconstruction-
scoped, identifies nobody, is not a Person, and never becomes reusable across packages or a durable
Actor profile — materialization must not accidentally convert a reconstruction-scoped actor context into
a reusable identity.

### 6. Governing Parent (Remaining Question — reconciled against existing DL-43/DL-45 practice)

**The Governing Parent is the package's own declared primary Subject anchor — the single governed,
Foundation-owned Identity Subject (DL-84) the package's boundary is centered on (a Room/Merged Room,
Asset, Person, or Pet) — never Incident (DL-134), never Preservation Hold, never Connected Storage,
never an invented request/package object.** This reuses, without deviation, **DL-105**'s own
anchor-ownership rule: *"Foundation owns Asset documents because it owns the Asset; Identity owns
voiceprints because it owns the profile/consent lifecycle"* — the Governing Parent is always the
already-governed object the artifact's content is actually about, never a newly invented container.

**Where a package's boundary spans multiple Subjects with no single narrower Subject distinguished**
(a pure time-range, Room-only, or cross-Subject correlation scope), the Governing Parent is the **Home**
— exactly the fallback **DL-105** already established for Materialized Household Assessment, for the
identical reason: Home is itself an already-existing, Foundation-owned Identity Subject (**DL-84**),
never invented for this decision, and no narrower universal construct exists to serve that role.
**Creating capability**: Concierge, mirroring DL-105's own Concierge capability-ownership pattern.

### 7. Parent Removal Behavior and retention (Remaining Question 7)

A materialized Evidence Package is a **new artifact with its own DL-43/DL-47 lifecycle** — never
automatically the longest or shortest constituent retention, never Incident retention (none exists,
DL-134), never Hold duration, never "forever." Mirroring **DL-105**'s own precedent for a comparably
sensitive materialized artifact: retained while its Governing Parent exists, with **Parent Removal
Behavior** that deletes the package when its Governing Parent is removed, **unless an overriding
retention rule or an active Preservation Hold applies** (restating **DL-45** unchanged — parent removal
never silently overrides a Hold or floor). Deletion triggers: explicit household deletion of that
specific saved package, or Governing-Parent removal; **never** automatically triggered merely by a new
package being assembled over the same or overlapping scope (each materialization is its own artifact,
restating **DL-27**/**DL-104**'s historical-correctness rule — a new package never silently supersedes
or deletes a prior one). **Exact numeric retention values are not invented here**; where a package's
retention floor/ceiling requires a specific number, that number is **OD-05**/**OD-26**/**OD-49**'s own,
exactly as **DL-105** already deferred the equivalent question.

**Materialization is never a retention loophole.** Where a source record's own deletion obligation
(**DL-133**) was pending or restricted-use at the time of inclusion, that status is preserved and
carried into the package rather than laundered away by materialization (§9).

### 8. Artifact identity

Each materialization is a **one-shot immutable record** under **DL-104**'s Object+Version shape,
carrying its own Record Identity — never a revision of a prior package. Regenerating a package over the
same or a similar scope later produces a new artifact with its own generation provenance; the earlier
package's content never silently mutates to reflect current source state.

### 9. Restricted-use material is not laundered by materialization (DL-133 preserved)

Restating **DL-133** unchanged: where information remains **solely** because of an active Preservation
Hold or deletion/preservation conflict and is restricted to the stated preservation purpose, **that
restriction survives package assembly and materialization.** Before such content is included: the
package's own purpose must be compatible with the preservation purpose; disclosure authority must
separately permit the intended recipient; inclusion must be explicitly governed — never included by
default merely because the record is technically present. Otherwise, the package represents the
existence of withheld material only to the extent current disclosure rules permit (§13).

### 10. Integrity representation — technical, never forensic

A **Package Integrity Manifest** (logical, independent of rendering format) may include: Package Record
ID; generation timestamp; generator/version identity; request/operation provenance; scope/selection
manifest; included-item identities and governed Record/Version IDs (**DL-104**); referenced-but-not-
copied item list; generation Decision Trace reference; component digests and a manifest digest where
materialized. **This is never described as chain of custody, forensic integrity, forensic evidence,
tamper-proof, court-ready, certified, legally admissible, or regulatory proof.** A digest demonstrates
byte equality/difference only; it establishes nothing about truth, completeness, lawful collection,
legal sufficiency, source integrity, identity, or forensic provenance — restating the existing
constitutional non-claim (`temporal-record.md`, *Legal and regulatory non-claim*) unchanged.

### 11. Package discloses its own status

Every human-readable/materialized Evidence Package states plainly, in the package itself: it was
generated by HTBW from the authorized evidence available at generation time; it may contain gaps,
uncertainty, and externally referenced material; it makes no claim of forensic certification, legal
evidentiary status, or chain-of-custody sufficiency. No legal disclaimer beyond the architecture's own
competence is used.

### 12. Assembly, materialization, and export authority are distinct, reusing DL-76 (Remaining Question 5)

**Assemble ≠ Materialize ≠ Authorize-recipient ≠ Transport.** Each is evaluated independently by
Operational Trust, reusing **DL-76**'s existing Action-Risk Classes and the **DL-71**/**DL-109**
configured-authority mechanism already established for Preservation Hold and conflict-resolution
governance — no parallel role model is invented:

- **Assembly** (constructing and viewing a projection, no durable artifact) is a **Disclosure**-class
  action (DL-76's own test: *"information is revealed that should not have been"*) — Required Identity
  Band Moderate, Required Confirmation Strength Verbal, the existing Disclosure defaults, unaltered.
- **Materialization** (creating durable Managed Content) is **Disclosure**-class with a **capability-
  specific override** to **Authenticated** confirmation — reusing DL-76's own already-accepted
  Capability-Default → HTBW-Default → Household-Override tiering (the same mechanism DL-76 already uses
  for object-specific variation, e.g. "a Safe Lock versus a Closet Lock"), not a new risk class. A
  materialized artifact outlives the moment of disclosure and is retrievable later without re-asking, a
  materially different consequence than a transient projection, justifying the stronger confirmation
  tier within the same class.
- **External recipient/export** (the package leaves HTBW governance) is **Governance**-class — Required
  Identity Band Very High, Required Confirmation Strength Strong — matching DL-76's own Governance test
  most precisely among the six classes (*"a governance record, policy, identity, or evidentiary record
  is altered or destroyed"*; an evidentiary-adjacent artifact permanently leaving governed control is
  the clearest instance of that consequence this architecture has), and mirroring **DL-132**'s own
  Governance-class treatment of Hold placement/release for comparably irreversible governance-relevant
  acts.

Where a required band/strength cannot be verified, **DL-40**'s existing `Unavailable` outcome governs
unchanged — refused, never silently downgraded.

### 13. Recipient authority and audience evaluation (Remaining Question 5, continued)

**Assembly authorization never implies disclosure authorization to any particular recipient.**
Operational Trust evaluates the requester, the intended recipient, the Subject(s) represented,
information classes, disclosure policy, purpose, audience, delivery surface, restricted-use constraints
(§9), consent, and current configuration — **before** protected content enters a recipient-bound
package, never after. **Materialization creates no new disclosure authority**: information that cannot
be disclosed to a recipient in ordinary governed interaction does not become disclosable merely because
it was placed into a package (no laundering of restricted historical location, Identity information,
private Communications, restricted financial information, held restricted-use records, withheld-by-
policy evidence, or protected Person data). For an external recipient, **recipient-aware inclusion
precedes materialization/export** — a full household package is never assembled first on the assumption
the recipient will not view protected portions. External recipients are declared explicitly (a named
household Person, an authorized non-resident recipient reusing existing Communication/recipient models);
anonymous "share with anyone with a link" behavior is never generated merely because storage can
technically support it.

### 14. Transport model

Permitted categories, where currently supported and governed: **(A) Private view/render** — a private
Assist/Companion/dashboard surface, projection only, no durable artifact required; **(B) Download** —
deliberate authorized materialization delivered to an authorized private client surface; **(C) Managed
Content access** — a saved package reached through its owning HTBW capability, never through storage-
path navigation (**DL-44**); **(D) Governed share/export** — explicit recipient, explicit disclosure
authorization, supported transport, durable export event recorded. **Capability availability for each
category is stated honestly, not assumed implemented.**

**Prohibited unless an equivalent, separately accepted secure control exists**: anonymous public URLs;
"anyone with a link" sharing; unauthenticated media-browser access; exposed Connected Storage paths; a
raw NAS path or unrestricted network share as delivery; public web publishing; broadcast to a Room
audience without audience evaluation; silent email forwarding; automatic cloud or third-party upload.
**Media visibility is not authorization; storage reachability is not authorization** (restating **DL-44**
unchanged — media-browser exposure is a visibility boundary, never an authorisation control).

### 15. External-export boundary disclosed

When a package is exported/shared outside HTBW, HTBW can govern whether export occurs, its contents at
export time, the intended recipient, the selected transport, and its own Decision Trace/provenance up to
that point. **After transfer, HTBW cannot guarantee downstream deletion, forwarding controls, retention,
screenshots, copying, recipient storage, or later disclosure** — the household is told this before
consequential external sharing, using existing confirmation/Communication patterns. Source deletion
occurring after export does not retroactively alter an already-exported external copy's bytes; HTBW
states this honestly rather than overpromising erasure. The governed HTBW copy (if retained) remains
subject to its own privacy/deletion obligations (**DL-133**) unchanged.

### 16. Preservation Hold does not authorize package operations (restating DL-132)

**DL-132 Preservation Hold authority does not imply authority to assemble, materialize, export, share,
or disclose an Evidence Package.** A Hold may preserve source records a package later needs; it grants
no package authority. Likewise, **materializing a package never automatically places a Preservation
Hold** on its sources — a household that wants source records preserved must separately authorize a Hold
under **DL-132**.

### 17. Connected Storage and native Home Assistant limits

Materialization that requires Connected Storage, where storage is currently unavailable, is represented
honestly under existing **DL-41** semantics: materialization is reported unavailable/failed, never
falsely claimed as saved; a transient projection may still be shown if source retrieval allows. A
package represents only evidence actually available — it never implies native Recorder evidence exists
after Home Assistant purged it, and never implies a preserved native row existed where no per-row Hold
capability exists (restating **DL-132** §11 unchanged). **No second Recorder is built.**

---

## Responsibility impact

| Responsibility/concept | Impact |
|---|---|
| Concierge | Unchanged: owns assembly orchestration and its own Decision Trace; gains no ownership of referenced records or the package as a store |
| Operational Trust | Extended, not altered: evaluates Assembly/Materialization/Export as three distinct, DL-76-classified actions |
| Foundation (via Governing Parent) | Unchanged: owns the Room/Asset/Person/Pet/Home the package anchors to, exactly as it already owns documents/artifacts anchored to those objects |
| Truth, Identity, Stewardship, Continuity | Unchanged: continue to own the records a package references |
| Preservation Hold (DL-132) | Unaffected; grants no package authority |
| Deletion/preservation (DL-133) | Unaffected; restricted-use status survives materialization unchanged |
| Incident (DL-134) | Unaffected; may bound a package's scope, never its Governing Parent |
| OD-09 (erasure/portability) | Unaffected; comprehensive raw export remains OD-09's own, never replaced by Evidence Package |

## Related documents

- [../governance/decision-ledger.md](../governance/decision-ledger.md) — **DL-135**, **DL-24**,
  **DL-27**, **DL-34**, **DL-35**, **DL-36**, **DL-43**, **DL-44**, **DL-45**, **DL-47**, **DL-71**,
  **DL-76**, **DL-104**, **DL-105**, **DL-109**, **DL-130**, **DL-132**, **DL-133**, **DL-134**
- [../models/temporal-record.md](../models/temporal-record.md) — *Evidence Package*
- [adr-governed-historical-retrieval-and-access.md](adr-governed-historical-retrieval-and-access.md)
- [adr-preservation-hold-governance.md](adr-preservation-hold-governance.md)
- [adr-deletion-versus-preservation-reconciliation.md](adr-deletion-versus-preservation-reconciliation.md)
- [adr-incident-and-case-object-model.md](adr-incident-and-case-object-model.md)
- [connected-storage.md](connected-storage.md)
- [privacy.md](privacy.md)
