# ADR: Household Inbox Projection Semantics

> **Document status: Canonical ADR.**
> Status: **Accepted** 2026-11-05. Records **DL-141** (issue **#116**, formal acceptance review PASS).
> Resolves **OD-47** in full.
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Terminology: [../models/glossary.md](../models/glossary.md),
> [../models/communication.md](../models/communication.md),
> [adr-explainability-presentation-and-assist-interaction-path.md](adr-explainability-presentation-and-assist-interaction-path.md).

---

## Status

**Accepted 2026-11-05.** Resolves every OD-47 acceptance criterion. This ADR creates **no Inbox
store, cache, or owning responsibility**, **no second Delivery Surface model**, and **no merged
Communication/obligation record class**. It does not reopen **DL-34**, **DL-41**, **DL-53**, **DL-72**,
**DL-94**, **DL-95**, **DL-96**, **DL-104**, **DL-117**, **DL-138**, **DL-139**, or **DL-140** — each
is consumed unchanged.

---

## Context

`north-star.md` and `communication.md` already establish, as constitutional text: **"The Household
Inbox is not a cross-cutting area, not a layer, and not a store. It is a projection over outstanding
Communications, filtered by the viewer's authority at read time."** OD-47's own residual, per its own
"Already decided" list, was narrowly: projection scope, viewer/scoping granularity, refresh semantics,
whether viewing constitutes delivery/presentation/acknowledgement, filtered-item behavior, and whether
the Inbox is itself a Delivery Surface.

**Four of this issue's own cited dependencies are already closed** (OD-43/DL-53 Delivery Surface model,
OD-57/DL-94 Indication and Room-Delivery Authorization, OD-49/DL-138 Communication retention,
OD-23/DL-117 obligation projection surface), and **DL-140** (accepted today, resolving OD-30) now
separately establishes Assist as the canonical household-facing interaction path, with endpoints
contributing context never authority. This decision applies that already-accepted machinery directly
to the Household Inbox's own six remaining questions, consuming — not reopening — each of them.

**Owner direction governing this closure:** the Household Inbox is Communications-only, unowned,
unpersisted, request-centric, assembled fresh on every request, accessed through Assist, and filtered
by Operational Trust at read time.

---

## Decision

### 1. Projection scope — Communications only (Option A)

**The Household Inbox projects outstanding Communications only.** Obligations (the `todo`/Calendar
surface governed by **DL-117**) are a separate, already-governed projection and are never merged into
the Inbox's own model. **Option B (Communications plus projected obligations) is rejected** — not
because composing them for a household is wrong, but because merging the two into one *projection
class* would blur Communication's and Stewardship's distinct record ownership (restating
`communication.md`'s existing "no Inbox responsibility" prohibition). A broad Assist question ("What's
outstanding?") may **compose** the Inbox projection and the obligation projection in one conversational
response (§8, below) without either model acquiring the other's fields, retention, or ownership.

### 2. Refresh semantics — request-centric, no store (Option A, rejecting Option C)

**The Inbox is assembled fresh on every request. There is no Inbox cache, store, or periodic refresh
of any kind.** **Option C (on-change refresh with a cached projection) is rejected outright** — a cache
is a store in all but name, and reintroduces exactly the hazard `communication.md` already names:
*"If authority to see a Communication is withdrawn, a stored inbox still contains it until something
remembers to rewrite it. A projection is correct by construction."* Every invocation re-evaluates the
authoritative Communication records and the current viewer's authority from scratch.

### 3. Access path — through Assist (consuming DL-140)

**The Household Inbox is accessed through Assist** — the canonical household-facing interaction path
(**DL-140**). A household question such as *"What's outstanding?"* or *"What's waiting for me?"*
enters through Assist, is classified as an Inbox-projection request, resolves the requester via
Identity, is filtered by Operational Trust at read time, and the resulting projection is delivered
back through Assist to whichever endpoint (Companion App, dashboard/kiosk, or voice) invoked it.
**Assist does not own, store, or become authoritative for the Inbox** — it is the orchestration/
interaction path; Concierge continues to assemble the projection; Operational Trust continues to own
the read-time authority filter; the originating responsibilities continue to own their own
Communications. Consuming **DL-139**'s identical pattern: the endpoint contributes requester, Room,
and audience context; it never grants access or disclosure authority merely by being invoked.

### 4. Scoping — per requester (per Person), never per Room or per household as a distinct Inbox scope

**"What's outstanding?" resolves per the resolved requester**, exactly as a personal-resource question
resolves under **DL-139**: Identity resolves the requester to the degree the request requires; the
projection reflects that Person's own authorized, outstanding Communications. **Room and household
composition remain disclosure inputs** (DL-34, DL-72), never a second, independent Inbox scope — there
is one Inbox construct, projected differently per viewer because each viewer's authorized Communication
set and current audience differ, not because "per-Room Inbox" or "per-household Inbox" are separate
constructs. **"Per surface"** (the issue's own wording) refers to this disclosure-constraint input (a
shared kiosk versus a private phone changes what may be disclosed), not to a surface-specific Inbox
variant — restating `decision-trace.md`'s and **DL-140**'s existing "endpoint contributes context,
never a separate authority" rule.

### 5. Viewing is not automatic acknowledgement; may constitute a presentation event

Consuming **DL-95**/**DL-96** unchanged: **opening or viewing the Inbox (or an item within it) does not
automatically constitute delivery, acknowledgement, or completion** — restating `communication.md`'s
existing "Opening or viewing a surface... is Not acknowledgement. Visibility alone establishes nothing"
rule, applied explicitly to Assist-mediated Inbox viewing. **Viewing an outstanding item may constitute
a current Presentation event** under the existing Communication lifecycle (Created, Suppressed,
Acknowledged, Expired, Superseded, Resolved by origin, Undeliverable; each Delivery Attempt's own
Attempted/Delivered/Presented/Failed outcome) where current Communication semantics already recognize
Presentation as distinct from Acknowledgement — reusing **DL-94**'s content/Indication distinction and
**DL-53**'s Presentation Attestation Capability. **A prior failed Delivery Attempt remains historically
failed**; a later Assist-mediated Inbox viewing is, where the originating Communication's own lifecycle
recognizes it, a **new, separate Presentation event** — the two are never merged or retroactively
rewritten into one another. If a capability's own Communication requires an explicit acknowledging
response (DL-96: an explicit, Communication-specific responsive act by an identified, in-audience
Person), that acknowledgement is processed through the owning Communication's own acknowledgement path,
never inferred from Inbox visibility alone.

### 6. Filtered-item behavior — content-free Indication, Challenge, or omission (consuming DL-94)

Where a Communication is excluded from the current viewer's projection because the current audience or
endpoint cannot receive it, reusing **DL-94**'s three already-accepted delivery forms unchanged:

- Where the Communication's own Room-Delivery Audience Preference makes it eligible and private
  delivery has not completed, a **Room-Delivery Authorization Challenge** may appear in its place
  (bounded disclosure: that a private Communication exists, its Urgency, and that current Room audience
  falls outside the intended Person's standing permission — nothing else).
- Where neither full content nor a Challenge is appropriate, a content-free **Indication** may appear
  (asserting only that something is outstanding, disclosing no recipient identity, subject, content, or
  sensitive classification).
- **Where the Communication's existence itself is protected, it is omitted entirely** — never rendered
  as a placeholder, a redaction marker, a count adjustment, or a "something is hidden" statement,
  restating the protected-existence-leakage prohibition already established for Explainability (**DL-140**
  §9, applied here to Inbox items identically).

### 7. The Inbox is not itself a Delivery Surface (consuming DL-53)

**The Household Inbox does not declare its own capability dimensions or Potential Perceptibility under
DL-53. It is not itself a Delivery Surface.** The invoking Assist endpoint (Companion App, dashboard/
kiosk, voice) supplies the presentation/surface context — modality, shared/private classification,
screen-persistence risk, spoken-disclosure risk — under its own already-accepted endpoint
classification (**DL-113**, **DL-88**, **DL-90**, consumed by **DL-140**). No new Inbox-specific surface
declaration, privacy classification, or perceptibility model is created; the existing Delivery Surface
model governs the *Communications themselves* when delivered through their own ordinary Delivery
Attempt path, unchanged by this decision.

### 8. Obligations remain separate; Assist may compose without merging

Consuming **DL-117** unchanged: an obligation/`todo`/Calendar question ("What do I need to do?") and a
Communication/Inbox question ("What messages are waiting?") remain two distinct models with two
distinct owners (Stewardship; Concierge/Operational Trust respectively). **A broad Assist question that
spans both ("What's outstanding?") may compose both projections into one conversational response**
(restating **DL-140**'s own "Assist questions may compose capabilities... this does not merge the
underlying domain models" principle) — Assist's composition is a presentation-layer convenience, never
a new combined data class, cache, or responsibility.

### 9. No store, no cache, confirmed

Restating the issue's own "Already decided" list, now fully discharged: the Inbox remains unowned (no
responsibility holds it as its own record), unpersisted (assembled fresh from the authoritative
Communication records on every request), and never a cross-cutting area, layer, or store. Any future
implementation detail that behaves like a cache — including one claimed to exist "only for
performance" — is non-conforming with this decision.

---

## Explicit non-goals

- **No Inbox store, cache, or owning responsibility is created.**
- **No second Delivery Surface model is created** — the Inbox is not itself a Delivery Surface; it
  reuses the existing model via the invoking Assist endpoint.
- **No merged Communication/obligation record class is created** — `todo`/Calendar and the Household
  Inbox remain two distinct, separately owned models.
- **No new acknowledgement/presentation vocabulary is created** — DL-94/DL-95/DL-96 are reused
  unchanged.
- **DL-34, DL-41, DL-53, DL-72, DL-94, DL-95, DL-96, DL-104, DL-117, DL-138, DL-139, and DL-140 are not
  reopened.**

---

## Related documents

- [../models/communication.md](../models/communication.md) — Household Inbox, Explaining communication,
  Multi-person communication
- [../models/glossary.md](../models/glossary.md) — Household Inbox
- [../contracts/concierge-contract.md](../contracts/concierge-contract.md)
- [north-star.md](north-star.md) — "The Household Inbox is not a cross-cutting area, not a layer, and
  not a store"
- [adr-explainability-presentation-and-assist-interaction-path.md](adr-explainability-presentation-and-assist-interaction-path.md)
  (**DL-140**)
- [adr-person-to-external-resource-association-ownership.md](adr-person-to-external-resource-association-ownership.md)
  (**DL-139**)
- [adr-communication-retention-governance.md](adr-communication-retention-governance.md) (**DL-138**)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
