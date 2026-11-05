# ADR: Deletion Versus Preservation Reconciliation

> **Document status: Canonical ADR.**
> Status: **Accepted** 2026-11-05. Records **DL-133** (issue **#82**, formal acceptance review PASS).
> Resolves **OD-36** in full.
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Terminology: [../models/glossary.md](../models/glossary.md), [../models/temporal-record.md](../models/temporal-record.md),
> [adr-preservation-hold-governance.md](adr-preservation-hold-governance.md).

---

## Status

**Accepted 2026-11-05.** Resolves every OD-36 Remaining Question. This ADR creates **no new
responsibility** and **no central deletion/preservation arbiter**. Operational Trust continues to own
the conflict-resolution *policy and authority*; each responsibility continues to own deletion,
minimization, and Hold-honouring over its own records; Concierge continues to orchestrate interaction
and communicate outcomes; Explainability continues to record why. **No Hold payload store, no second
Recorder, and no claim of legal or regulatory effect are introduced.**

---

## Context

Two accepted constitutional duties can address the same record and were never reconciled: a valid
deletion/erasure/consent-withdrawal obligation (**DL-43**, **DL-56**), and a retention floor or
**Preservation Hold** (**DL-24**, **DL-45**, **DL-47**, **DL-132**). **DL-45** already states cleanup
"never silently overrides" a Hold or floor; **DL-132** (Preservation Hold Governance, accepted
2026-11-05) supplies Hold authority, lifecycle, scope, and enforcement but explicitly, deliberately
left this precedence question to this decision.

---

## Decision

### 1. The conflict is itself governed — no blind universal winner (Remaining Question 1)

**Neither "preservation always prevails" nor "deletion always prevails" is adopted.** When a valid
deletion/erasure/consent-withdrawal obligation and a valid Preservation Hold (or retention floor)
cover the same record, the collision becomes a **governed conflict** with exactly one resulting
outcome — never two contradictory silent behaviours. Until resolved:

- deletion is never falsely reported as complete while payload remains;
- valid preserved evidence is never silently erased;
- material retained solely because of the conflict is never put to ordinary use (§4);
- the minimum required material is preserved fail-safe while resolution proceeds;
- the conflict itself is recorded;
- authorised affected Persons are told the truth, within their disclosure scope;
- the pending deletion obligation is never dropped.

### 2. Conflict-resolution authority (Remaining Question 2)

**A new, independently configured Operational Trust authorisation — Preservation/Deletion
Conflict-Resolution Authority — resolves the conflict.** It reuses, without inventing a parallel
system, the exact mechanism **DL-132** already established for Hold governance: **DL-71**'s Named
Person / Role-Authority-Class forms, configured per **DL-109**, evaluated as a Governance-class action
(**DL-76**: Very High / Strong, consistent with placement and release).

**The Person who placed the Hold does not automatically gain authority to decide that another
Person's deletion request loses.** Hold-placement authority, Hold-review authority, Hold-release
authority (each independently configured under **DL-132**), and Conflict-Resolution Authority are
**four separate, independently configured authorisations** — a household may name the same Person/Role
for all four, or different ones, but none is inferred from another.

### 3. Granularity (Remaining Question 3)

**The conflict is evaluated at the lowest practical governed level**: the record, the governed
Subject-record relationship, or the specific deletion obligation at issue — never globally for an
entire record class or identically for an entire Hold merely because one covered record conflicts. A
Hold supplies shared context (purpose, scope, authority) across the records it covers; each affected
record's own deletion and preservation duties remain distinct and may resolve differently within the
same Hold. No new conflict-record payload store is created; this reuses existing record-class
architecture and **DL-104** Governed References.

### 4. Minimization before full-payload preservation (Remaining Question 4, partial)

Before payload is preserved despite a deletion request, the following sequence is required, in order:

1. Can the preservation purpose be satisfied by deleting the payload while preserving only Tombstone,
   consent-lifecycle, Hold-lifecycle metadata, provenance, and record identity? If so, **delete the
   payload.**
2. Can identifying/private content be reduced while the legitimate preservation purpose survives? If
   so, **reduce it.**
3. Is a reduced governed record sufficient? If so, **that is the outcome.**
4. **Only if the actual payload is necessary to satisfy the valid Hold purpose does it remain.**

Minimization is never claimed where it would make the preserved evidence meaningless, and full payload
is never preserved merely because that is simpler. **DL-56** is the accepted worked pattern proving
this is sometimes valid (biometric/derived identity material deleted; the consent-lifecycle record
survives as a **DL-47** structural floor that cannot reconstruct what was deleted) — it is evidence
that the technique works, generalised here, **not** elevated into a rule that always applies regardless
of whether deletion would defeat a Hold's actual purpose.

### 5. Restricted use of payload preserved solely because of a conflict (Remaining Question 4, continued)

**A Preservation Hold is a temporary exception to ordinary forgetting. It is not new ownership or
general authority over the retained data.** This is not a new primitive: it restates the already-accepted
principle that authorization is purpose-bound, never blanket (**DL-93**: "configuring a provider does
not grant blanket access"; every Intended Audience Specification and Action-Risk evaluation is
per-purpose, never a standing grant). Where content remains **solely** because of an active Hold
conflicting with a deletion obligation, its continued existence does **not** authorise: ordinary use;
unrelated reasoning (including **Home Steward**, **DL-131**); personalization; generalised Historical
Retrieval; training; analytics; disclosure beyond §7; broader correlation; profile enrichment; unrelated
automation; or unrelated AI processing. **Use is limited to the stated preservation purpose and current
authorised governance** — evaluated by Operational Trust exactly as any other purpose-scoped access
already is, never through a second access-control model. Where the record is also queried for an
ordinary, unrelated purpose, the governing responsibility answers as though the restricted payload were
unavailable for that purpose, consistent with `failure-and-degradation.md`'s existing "report
unavailable" vocabulary.

### 6. Pending deletion (Remaining Question 1, 4, continued)

A deletion/erasure/consent-withdrawal obligation that cannot immediately be fulfilled because a valid
Hold conflicts is represented as a **governed pending-cleanup obligation**, reusing **DL-45**'s existing
pending-cleanup semantics (never a new construct): the request is never reported as "deleted" while
payload remains; it is never lost; it retains enough governed context (requester, subject, record,
applicable obligation, conflict record) that when the Hold ends it is automatically re-evaluated (§8).
**The Person is never required to repeat the deletion request.**

### 7. Person-facing disclosure (Remaining Question 4, continued)

The affected Person receives an honest, actionable answer, subject to existing disclosure/privacy
architecture (**DL-34**, **DL-36**) and to **DL-132**'s "Hold existence is itself governed information"
rule — distinguishing *that* a governed preservation requirement is active from the Hold's own
protected purpose/scope/placer details, which are disclosed only to the degree the requester's own
authorisation already permits. Four honest outcome shapes (wording not mandated, semantics preserved):

| Outcome | Semantic |
|---|---|
| **A — Deleted** | The requested information was deleted; a governance record proves it occurred |
| **B — Pending (preservation conflict)** | The deletion request is recorded; some information is currently preserved under an active household Preservation Hold, restricted to that purpose, and will be re-evaluated when the Hold ends |
| **C — Partial/minimized** | The requested content was removed; minimum governance information remains to document the deletion/preservation lifecycle |
| **D — Technically unavailable/pending reconciliation** | Honest statement of what HTBW can or cannot technically preserve or delete, including native-platform limits (§10) — never a claim of success that has not occurred |

**Silently doing nothing (a fifth, unreported outcome) is prohibited.**

### 8. Hold release reactivates pending deletion (Remaining Question 5, continued)

**DL-132 unchanged: Hold release is not deletion.** Where a deletion obligation was pending solely
because of the conflict, **release makes that obligation actionable again** — normal retention/deletion
processing then determines the actual outcome. The household is never required to re-request deletion
merely because time passed. If storage is unavailable at that point, deletion is not claimed; the
pending-cleanup state is retained and reconciled when storage returns (**DL-45** unchanged).

### 9. Late Hold — anti-abuse rule (Remaining Question 6)

**A Hold placed after a deletion/erasure request is received may affect that pending deletion only if
the independently configured Conflict-Resolution Authority (§2) explicitly validates it** — the Hold's
purpose, scope, the reason it must apply despite the earlier request, and the necessary preserved
content. **Ordinary Hold-placement authority alone is never sufficient** to retroactively defeat an
already-valid deletion obligation. Required record: deletion-request timestamp, Hold-placement
timestamp, conflict-approval timestamp (if any), conflict authority, rationale. **Without valid conflict
approval, the late Hold does not block the already-valid deletion obligation.** Where a valid Hold
already existed *before* the deletion request, the request is never silently rejected — it becomes
pending/conflicted under §1–§7 instead; **ordering is relevant evidence, not automatic precedence**
either way.

### 10. Tombstone behaviour (Remaining Question 5)

- **Preservation temporarily prevails (payload remains):** no Tombstone is created claiming deletion.
  Conflict/deletion-request lifecycle metadata is preserved instead, showing: deletion requested;
  deletion pending/conflicted; Hold still active; content remains because of the stated preservation
  purpose. **A Tombstone is created only when deletion actually occurs** (§8).
- **Deletion/minimization prevails (payload removed):** the existing canonical Tombstone/lifecycle
  evidence (**DL-45**, **DL-47**, glossary *Tombstone*) proves the record existed, when it was deleted,
  under what authority, and why; where a Hold applied, the Hold's own history and the conflict-
  resolution outcome remain part of the governed record (**DL-132** §7, unchanged) without the
  Tombstone recreating the deleted payload. **A Tombstone never reconstructs the deleted content**,
  restating the glossary's existing definition unchanged.

### 11. Native Home Assistant limitation (Remaining Question 7)

Restating **DL-132** §11, applied to deletion: Home Assistant Recorder offers no native per-record
purge or deletion exemption. **HTBW must not claim it can preserve, or individually delete, a native
Recorder row beyond what the platform actually provides.**

- Where a governed HTBW record exists independently in Connected Storage, this decision's conflict
  rule applies in full.
- Where only ephemeral native Recorder history exists with no corresponding governed record, per-row
  preservation or per-row deletion precision **may be technically unavailable**, stated honestly as
  Outcome D (§7) rather than claimed.
- Where material evidence was captured into a governed Decision Trace or other governed record before
  native expiry, the conflict rule applies to that governed record and its required source versions,
  never by pretending the original native Recorder row can be individually exempted or individually
  deleted. **No second Recorder is built.**

### 12. Connected Storage unavailable (Remaining Question — storage behaviour)

Restating **DL-45**/**DL-129** unchanged: if deletion must occur on Connected Storage while storage is
unavailable, **deletion is never claimed**; the pending-cleanup state is retained and reconciled when
storage returns. Likewise, Hold enforcement is never claimed over storage that cannot currently be
verified. Backup coverage of Connected Storage is deployment-specific and never assumed; where deleted
content may persist in a backup, this is reflected honestly against currently accepted backup
architecture rather than inventing a new backup-deletion system — a genuinely unresolved backup-deletion
question, if one exists, is routed to its own issue, not solved here.

### 13. Consent withdrawal (generalising DL-56, not replacing it)

Consent withdrawal may create an immediate deletion obligation for some content classes while
structural lifecycle records remain under accepted retention floors — **DL-56** resolves this
completely for the biometric/derived-identity case and is not reopened. Where consent withdrawal and an
active Preservation Hold genuinely collide for a *different* record class, this ADR's conflict model
(§1–§10) applies. **A Preservation Hold never reconstructs consent that has been withdrawn.**

### 14. Parent-object cleanup

Restating **DL-45** unchanged: parent removal cleans up dependent artifacts, but never silently
overrides a structural floor, an active Hold, or a pending-deletion obligation; cleanup does not create
orphaned payloads with no canonical Governing Parent, and uses **DL-104** Governed Reference semantics
where required.

### 15. Adopted Asset Intelligence artifacts — DL-110 (not reopened)

**DL-110** (Adoption Scope, Artifact Custody, and Coexistence Behaviour, accepted, #172) already
resolves the governing-parent ambiguity this issue's own history raised (Comments 1–2): a successfully
adopted document becomes an independently HTBW-governed artifact, with the equivalent HTBW Asset as its
own Governing Parent, from the moment of adoption — never re-parented from, or dependent on, the source
product. Consequently: retention-driven deletion is governed by **DL-47** on the artifact's own
declared retention (a Hold survives it exactly as for any other Asset document, per **DL-132**);
product retirement is already governed by **OD-82** (does not trigger **DL-45** cleanup); and
resident-initiated uninstall of the coexisting product has **zero effect** on an already-adopted HTBW
artifact. **This ADR does not reopen DL-110 or recreate the closed adoption problem** — the three
previously collapsed events remain distinguished exactly as DL-110 already states.

---

## Explainability and Decision Trace

Every conflict resolution produces Decision Trace evidence recording, at minimum: the deletion/erasure/
consent-withdrawal request (requester/subject, time); the affected record and applicable deletion
obligation; the active Hold (purpose/scope as authorised for disclosure); chronology of request versus
Hold placement; the minimization analysis performed (§4); the Conflict-Resolution Authority, identity,
and confirmation used; the conflict decision and its outcome class (§16); the resulting payload
handling and restricted-use status (§5); the Tombstone/lifecycle outcome (§10); the Person-facing
disclosure given (§7); the pending obligation, if any; and the eventual release/reconciliation event
(§8). **Protected payload is never copied merely to explain the conflict.**

## Conflict resolution outcomes (Remaining Question — normalized vocabulary)

Every conflict resolves to exactly one of:

- **A — Delete payload; retain minimum governance evidence** (§4.1–4.3, §10).
- **B — Preserve payload temporarily; restrict use; deletion remains pending** (§4.4, §5, §6).
- **C — Partial minimization; preserve only the necessary portion** (§4.2–4.3).
- **D — Technically unavailable; pending reconciliation** (§11, §12).

**Silently doing nothing is never a valid outcome.**

## Reevaluation

A resolved conflict is re-evaluated when a relevant governance event occurs: Hold release; Hold scope
narrowed; the preservation purpose ends; storage returns; conflict/placement authority changes; the
applicable deletion obligation changes; or a previously unavailable deletion capability becomes
available. Re-evaluation is event-driven, never a continuous poll, using existing lifecycle/event
architecture.

---

## Boundaries explicitly preserved

- **OD-40 (Evidence Package):** a conflict resolution, a Tombstone, and Hold/conflict metadata never
  automatically create an Evidence Package. This ADR supplies OD-40 with conflict outcome, restricted-
  use constraints, preserved/deleted status, Tombstone semantics, and disclosure constraints; it does
  not pre-decide OD-40's own assembly/transport/integrity/audience questions.
- **OD-09 (erasure/portability):** this ADR answers *what should happen when deletion and preservation
  collide*; OD-09 remains responsible for the operational mechanics of request, portability, actual
  erasure processing, and applicable interfaces.
- **OD-41 (Incident/Case model):** unaffected; this ADR's granularity model (§3) does not require an
  Incident construct, consistent with **DL-132**.

---

## Responsibility impact

| Responsibility/concept | Impact |
|---|---|
| Operational Trust | Extended, not altered: now owns the Preservation/Deletion Conflict-Resolution Authority (§2) alongside existing Hold authority (**DL-132**) |
| Each record-owning responsibility | Unchanged: continues to own deletion, minimization, and Hold-honouring over its own records |
| Identity | Unchanged: continues to own consent lifecycle and withdrawal effects (**DL-56**) |
| Concierge | Unchanged: orchestrates interaction, communicates outcomes; owns neither the conflict nor its resolution |
| Explainability/Decision Trace | Extended with conflict-outcome fields; **DL-82**'s provenance model unchanged |
| OD-39 (Preservation Hold) | Unaffected, not reopened; this ADR consumes **DL-132** by reference only |
| OD-85/DL-110 (Adoption) | Unaffected, not reopened; §15 restates, does not alter |
| OD-06/DL-56 (Consent) | Unaffected, not reopened; §13 generalises the pattern without altering it |

## Related documents

- [../governance/decision-ledger.md](../governance/decision-ledger.md) — **DL-133**, **DL-24**,
  **DL-43**, **DL-45**, **DL-47**, **DL-56**, **DL-71**, **DL-76**, **DL-104**, **DL-109**, **DL-110**,
  **DL-132**
- [adr-preservation-hold-governance.md](adr-preservation-hold-governance.md)
- [../models/temporal-record.md](../models/temporal-record.md) — *Preservation Hold*, *Tombstone*
- [../models/operational-trust.md](../models/operational-trust.md) — *Retention, history, and
  preservation authority*
- [privacy.md](privacy.md)
- [connected-storage.md](connected-storage.md)
- [failure-and-degradation.md](failure-and-degradation.md)
- [../models/decision-trace.md](../models/decision-trace.md)
