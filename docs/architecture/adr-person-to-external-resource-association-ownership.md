# ADR: Person-to-External-Resource Association Ownership

> **Document status: Canonical ADR.**
> Status: **Accepted** 2026-11-05. Records **DL-139** (issue **#148**, formal acceptance review PASS).
> Resolves **OD-77** in full.
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Terminology: [../models/glossary.md](../models/glossary.md),
> [../contracts/foundation-contract.md](../contracts/foundation-contract.md),
> [adr-home-identity-and-home-intelligence-governance.md](adr-home-identity-and-home-intelligence-governance.md).

---

## Status

**Accepted 2026-11-05.** Resolves every OD-77 acceptance criterion. This ADR creates **no new
responsibility**, **no provider abstraction**, **no credential/token/secret storage**, and does **not**
revive Household Memory. It does not reopen **DL-31**, **DL-32**, **DL-33**, **DL-41**, **DL-46**,
**DL-47**, **DL-56**, **DL-57**, **DL-69**, **DL-71**, **DL-85**, **DL-92**, **DL-93**, **DL-102**,
**DL-104**, **DL-112**, **DL-113**, **DL-115**, **DL-127**, **DL-128**, **DL-131**, or **DL-136** —
each is consumed unchanged.

---

## Context

`docs/models/person-and-identity.md`'s Person-extension table has, since its own creation, carried one
unassigned row:

> | Mailbox, calendar, and other external-service references | Referenced through the responsibility
> that governs their use; **the underlying configuration is never copied** |

**No responsibility is named.** `docs/contracts/foundation-contract.md` declares the relationship types
as `caretaker-of`, `owner-of`, `serves-room`, and `located-in` — none of which expresses that an
account belongs to a Person. Continuity's own ownership list explicitly excludes it. Every
personal-resource household outcome in `docs/scenarios/continuity-use-cases.md` depends on this gap:
Use Case 2 (the dental appointment reminder), Use Case 4 (audiobook resume), Use Case 5 (interaction
styles), Use Case 6 (the gap's own canonical statement), and Use Case 11 (music/book/television
recommendation candidates).

**The Home-scoped sibling of this exact question is already resolved.** **DL-115** (OD-90, #189,
accepted 2026-11-02) decided that Foundation owns the Home-scoped External-Resource Association
assignment, directly on the Home object, by the same Foundation-held-declarative-binding pattern
already used for `located-in`/`owner-of`. **DL-85** (#191) established, in advance, that OD-77 and
OD-90 share one Foundation-defined relationship-type shape (subject, external-resource reference,
fixed minimal lifecycle) while remaining two separately closeable assignment-ownership decisions,
because a Person's assignment sits inside the **DL-71** Person Extension's distributed-ownership model
while the Home carries no equivalent. This ADR is the second and final half of that reconciliation.

**Owner decision governing this closure:** **Option A — Foundation owns the Person-to-external-resource
association assignment**, as an instance of the broader principle that **Foundation owns the Home's
declarative structural relationships, including associations between a Person and resources assigned
to, belonging to, or representing that Person.**

---

## Decision

### 1. Foundation owns the Person-scoped External-Resource Association assignment

**Foundation owns the Person-scoped assignment of the External-Resource Association relationship type**
(**DL-85**) — the governed, declarative binding between a Person and an external calendar, mailbox,
media profile, audiobook account, reasoning-provider profile, or other supported external
service/resource. This mirrors **DL-115**'s Home-scoped assignment exactly in shape (subject, external
resource reference never its content or credentials, and the same fixed minimal lifecycle: creation,
disclosure, reassignment, revocation, stale-detection, retention under **DL-47**, Decision Trace
citation under **P30**) and differs from it only in subject (Person, not Home) and in sitting inside
the Person Extension's distributed-ownership model (**DL-71**) rather than `home.md`'s single flat
Foundation list.

**`docs/models/person-and-identity.md`'s Person-extension table row is updated**: "Mailbox, calendar,
and other external-service references" now names **Foundation**, consuming the identical
Foundation-defines-the-relationship/responsibility-owns-the-assignment split already used for
`caretaker-of` (where Foundation defines the relationship and Stewardship owns the caretaker
assignment) — here, Foundation both defines **and** holds the Person-scoped assignment, exactly as it
already both defines and holds the Home-scoped assignment under DL-115.

### 2. The broader Foundation principle, and a grounding correction to how it is supported

**The general principle**: Foundation owns declarative Person-resource topology — the bare fact of
*which resource is associated with which Person* — while the resource's own owning responsibility
retains every operational, content, and runtime authority. Foundation answers *which resource is
declaratively associated with this Person?* Foundation never answers *may this requester access that
resource?* (Operational Trust) or *what does that resource currently contain?* (the owning provider or
integration).

**A grounding correction, identified during this review and recorded transparently.** The issue's own
discussion (and early drafts of this reconciliation) suggested that currently-accepted **internal**
Person-device associations — a BLE identity device, a phone, a watch — already function as Foundation
ownership precedent for the external case. **Independent verification against currently accepted
architecture shows this is not accurate**, and this ADR does not carry it forward as a claim:

- `person-and-identity.md`'s own **What Identity owns** list names **"Assigned-device relationships
  used for identity"** explicitly as Identity's, not Foundation's — this is the **Identity Evidence
  Association** (**DL-32**): a Person-to-evidence-source binding carrying person-specific reliability,
  claim applicability, freshness, evidence family, and consent, feeding Identity Fusion.
  `home-assistant-boundary.md`'s own Person row confirms the same: a Person-associated tracker or
  evidence source's owner is **Identity**, never Foundation, and **"a duplicate person-to-tracker
  registry"** is explicitly listed as a forbidden construct.
- Where an internal device instead serves as a **delivery/notification surface** (a mobile
  notification target, a preferred read-later target), verified implementation evidence on this issue
  (Comment 1, Finding 5) classifies it as **Continuity**'s personal-surface-default record, consistent
  with `communication.md` and the Delivery Surface model — again, not Foundation's.

**Neither finding contradicts the Owner's Option A decision.** It corrects only the *supporting
argument*. The direct, in-kind, already-accepted precedent for Foundation ownership of the
Person-scoped External-Resource Association is **DL-115**'s structurally identical Home-scoped
assignment — not an analogy to internal device associations. The absence of any Foundation-owned
internal Person-device construct is itself informative, not contrary: **every existing internal
Person-resource construct carries purpose-specific semantics** (Identity's confidence-weighting,
Continuity's delivery preference) **that an External-Resource Association deliberately does not
carry** — it is bare topology, carrying no confidence weight and no delivery/presentation preference.
That is precisely Foundation's remit (a stable, declarative relationship with no runtime or evidentiary
content of its own) and precisely why it is not Identity's or Continuity's. **This correction does not
redesign, reopen, or relitigate DL-32, Continuity's ownership boundary, or any internal Person-device
relationship** — none is touched by this decision, consistent with the issue's own explicit
instruction not to expand OD-77 into a redesign of every Person-resource association.

### 3. Relationship-type definition versus relationship-assignment ownership

Restating, not inventing, the existing Foundation split (`foundation-contract.md`: "Foundation defines
the caretaker-of relationship; the caretaker assignment itself is owned by Stewardship"): **Foundation
owns both the shared External-Resource Association relationship-type shape (already accepted, DL-85)
and the Person-scoped assignment** (this decision). Earlier architecture left open the possibility that
another responsibility might hold the Person-scoped assignment while Foundation held only the type —
**the Owner resolves that choice here: Foundation holds both**, for the reasons in §1-2 above.
Foundation does **not** thereby acquire ownership of the referenced external resource itself.

### 4. Shared shape conformance — DL-85's floor is satisfied unchanged

This decision conforms to, and does not alter, **DL-85**'s fixed minimal lifecycle floor: a **subject**
(here, Person), an **external resource reference** (never its content or credentials, **DL-46**), and
creation, disclosure, reassignment, revocation, stale-detection, retention (**DL-47**), and Decision
Trace citation (**P30**). Per Maintenance Rule 1, **OD-77 and OD-90 remain two separately closed
decisions that select the identical assignment-owning responsibility** (Foundation) for structurally
different reasons — OD-90 because the Home carries no distributed-ownership model to contend with;
OD-77 because, per §2 above, no other Person-scoped construct fits a bare topological reference. Neither
decision imports the other's reasoning model onto its own subject.

### 5. Relationship to DL-115 — intentional structural symmetry, DL-115 not reopened

**DL-115** (OD-90) is not reopened, narrowed, or altered by this decision. DL-115's own closing text
already states "OD-77 (#148) is not decided, narrowed, or constrained beyond the existing DL-85
common-shape floor... the Home's structurally simpler, non-distributed ownership model is not
imported into Person's eventual answer." This decision keeps that promise: **DL-71's Person
distributed-ownership model is not imported onto the Home**, and this decision's own reasoning (§2) is
not imported backward into DL-115. The two decisions now read as a coherent pair:

| | DL-115 (OD-90) | DL-139 (OD-77) |
|---|---|---|
| Subject | Home | Person |
| Assignment owner | Foundation | Foundation |
| Grounding | `home.md`'s flat "Owns" list; no distributed-ownership model to reconcile | `person-and-identity.md`'s **DL-71** distributed Person Extension; Foundation selected because no other extension-owner's construct fits bare topology (§2) |
| Shared floor | DL-85, unchanged | DL-85, unchanged |

### 6. Person Extension — the row, named

`person-and-identity.md`'s extension table row is restated as:

> | Mailbox, calendar, and other external-service references | **Foundation** — the governed
> **External-Resource Association** assignment (**DL-85**, this decision); **the underlying provider
> configuration, content, and credentials are never copied** |

**"Person Extension" remains a collective name, not a new object (DL-71).** This decision adds one more
named owner to the already-distributed list; it creates no unified store, and Person Setup remains the
shared configuration *experience* across every distributed extension, presenting Foundation's
association alongside Identity's evidence associations, Continuity's preferences, and Operational
Trust's authority on one surface **without any of them becoming Concierge's** merely because they are
rendered together (verified implementation evidence, Comment 1/2, Findings 2 and 5).

### 7. Provider/resource authority boundary — restated, not newly invented

The External-Resource Association contains only enough information to **reference** the authoritative
external resource — a native Home Assistant `entity_id` where one exists, or an equivalent stable
provider-resource identifier otherwise — never its content or credentials. Foundation never holds, and
this decision never creates storage for: a provider Config Entry, an account object, an OAuth token, a
credential, a password, an access token, a refresh token, mailbox contents, calendar contents, a
media/audiobook library, listening history, a provider profile payload, or a reasoning-provider secret.
The provider or Home Assistant integration remains fully authoritative for all of these, restating
**P21**, **P22**, and **DL-46** unchanged.

**Cardinality is one-to-many per role**, consistent with verified implementation evidence (Comment 1,
Finding 1): a Person may hold several calendars, several mailboxes, and so on. **The role vocabulary is
extensible configuration data, not a fixed schema field** — calendar, mailbox, media profile, audiobook
account, reasoning-provider profile, and future roles are added without a schema change, following the
same stable-key-plus-household-display-name pattern ("what do you call this") already accepted for
Room device/asset groups. **Native Home Assistant labels may be used for discovery and filtering and
are never persisted into the governed association record** (verified evidence, Comment 1, Finding 2).

### 8. Association is not authorization

**Association ≠ authorization.** Foundation establishing that Tom is associated with Calendar Resource
X does not imply that Tom, or any capability, may access Calendar Resource X. **Operational Trust**
remains solely responsible for access, disclosure, audience, purpose, and authorization evaluation
(unchanged — `operational-trust.md`'s existing "who may access calendars, messages, email, or history"
holding). A denial of Operational Trust permission never deletes or suspends the Foundation association
— the topology continues to exist; only its use is withheld.

### 9. Rejected alternatives — recorded, not merely dismissed

**(B) Identity.** Rejected. Identity owns *who is this* — confidence, attribution, and evidence fusion
(**DL-32**, **DL-38**). A resource association is topology, not identity evidence. Reusing the pattern
DL-32 already established (one Person, one source, consent-scoped, revocable, no duplicate registry) is
appropriate; overloading the Identity Evidence Association construct itself with resource entitlement
is not, and is not done here.

**(C) Continuity.** Rejected. Continuity's existing exclusion list already states the association is
not Continuity's (`continuity.md`, `continuity-contract.md`). Continuity's genuinely broader than any
association — it is consumed by calendars, email, reasoning providers, media, and other capabilities,
not owned by the one responsibility that merely presents preferences about them. Continuity continues
to supply **preferred delivery and presentation only**, a materially different record that happens to
sit on the same Person Setup surface (verified evidence, Comment 1, Finding 5).

**(D) Operational Trust.** Rejected. Entitlement answers *may this be disclosed*, never *which resource
is this Person's*. Collapsing topology into permission would make the entitlement itself incoherent —
there would be nothing named for the entitlement to be about.

**(E) Concierge.** Rejected. Concierge may orchestrate: resolved Person → Foundation association lookup
→ Operational Trust authorization → owning provider/capability → response. It owns neither the
relationship nor the underlying resource. Verified implementation evidence (Comment 1, Finding 2;
Comment 2) shows the same Person/Room setup surface already carries Identity, Operational Trust,
Foundation, and Continuity records side by side — rendering confers no ownership, or Concierge would
own all of them.

### 10. Deterministic "my" resolution — requester-governed, never Room-governed

Personal-resource requests resolve from the **requester**, never from Room occupancy. *"What's on my
calendar tomorrow?"* resolves as: (1) Identity sufficiently resolves the requester; (2) Foundation
resolves that Person's applicable External-Resource Association; (3) Operational Trust authorizes the
specific request/context; (4) the authoritative provider/integration is queried; (5) Concierge
orchestrates and presents. **Room occupancy, most-recently-active Person, household Owner status,
nearest phone, nearby BLE device, speaker endpoint, shared kiosk identity, or any guessed identity never
substitutes for requester resolution.** An associated internal device may contribute **Identity
evidence** toward resolving who the requester is, exactly as DL-32 already governs — it never
independently decides whose external resource should be used.

### 11. Unknown Person and Guest

**Unknown Person** (**DL-33**, unchanged): references no Person, inherits nothing, resolves no
Person-scoped association, and receives no Person-owned external-resource binding. A request requiring
a Person association is simply unavailable when the requester cannot be sufficiently resolved. **Guest**
inherits no Owner association, no Room-occupant association, no household-default personal account, and
no "closest matching" resource. **If a Guest exists as a sufficiently resolved, deliberately configured
Person and the household has explicitly configured an External-Resource Association for that Person**,
that explicit association resolves under the normal rules above; otherwise, nothing is inherited.

### 12. Multi-person, shared resources, and conflicting exclusive claims

Where multiple Persons are present, "my calendar," "my audiobook," "my music profile," and "my mailbox"
each resolve from the requester's own association; Room occupancy supplies context only, never
ownership. **A household may deliberately configure the same external resource for more than one
Person** where the resource's own semantics permit sharing — this is not automatically a conflict. A
provider account shared between Persons **never collapses Person-scoped Continuity preference or
playback/reading progress** (**DL-112** confirms person-scoped media preference is derived only through
eligible, attributed evidence; this decision does not reopen it). Where a resource's semantics or the
household's own configured relationship rules mark it exclusive and two Persons claim it, **the
conflict is surfaced, never silently resolved by selecting first, newest, household Owner, Room
occupant, nearest device, or provider default**. No repository-wide exclusivity metadata is invented
here; where current architecture has none, the need is recorded as implementation/provider validation
work, not decided.

**DL-128's own cl.12 narrowing is confirmed, not reopened**: Follow-Me/resume lifecycle governance does
not require this decision; only the narrower per-person attribution question, where a household shares
one provider account, was ever OD-77's own (`continuity-use-cases.md` Use Case 4, scenario 4.4) — that
narrower question is resolved by this clause: shared-account attribution is evaluated the same way as
any other shared-resource claim above, through configured, explicit, per-Person records, never guessed
from usage pattern.

### 13. Reasoning-provider profile association

Consuming **DL-93** and **DL-131** unchanged: where current Reasoning Provider architecture supports a
Person-specific reasoning-provider profile/reference, **the Person-to-provider-profile association is
Foundation-owned under this decision**, exactly like any other external-resource role. This decides
only *which configured provider profile is referenced for this Person* — it does not reopen **which
providers are available** (established at Integration configuration time, never runtime-discovered,
per DL-93), **whether the Person may use General Reasoning or Home Steward at all** (Operational
Trust's "Allow General Questions"/"Allow Home Steward" gates, DL-93, unchanged), or **DL-93's existing
fallback order** (Person-specific provider → Integration default → unavailable, no Room step). Home
Steward (**DL-131**) remains distinct: it may optionally be configured as a DL-93 Reasoning Provider
entry, and is never auto-substituted into the General Reasoning fallback chain — this decision does not
alter that in any respect.

### 14. Creation — authored, never inferred

An association is established only through a governed configuration path: explicit household
configuration, a provider integration exposing an authoritative account/resource identity that the
household then binds or accepts, Home Assistant exposing an authoritative device/resource identity the
household assigns to a Person, or another currently approved configuration flow. **The Foundation
association must be governed/declared; it is never silently established from observed usage.**
*"Tom usually carries BLE device X"* never becomes Tom's governed association; *"David usually listens
through account Y"* never becomes David's governed association. Provider/Home Assistant metadata may
supply a candidate resource, an authoritative identifier, a capability/resource type, or a configuration
reference — it may not silently establish the Person assignment without passing through the household's
own accepted configuration path, and no competing configuration mechanism is created alongside it.

### 15. Disclosure

The existence of a Person-resource association may itself be private (a personal phone, mailbox, health
portal, financial resource, audiobook account, or AI provider profile). **Operational Trust governs
disclosure of the association's existence and detail, exactly as it governs disclosure of the
resource's content.** Foundation owning the association does not make it visible to everyone; an
unauthorized requester is not necessarily told that a protected association exists, under existing
protected-information refusal semantics.

### 16. Reassignment

Reassignment is explicit and governed: a new assignment is recorded, the prior assignment's lifecycle
is preserved under the existing Change Record/history model, reassignment authority is governed exactly
as creation is, no provider credential or content is silently migrated, and future resolution follows
the new assignment while **historical Explainability continues to reference the version in effect at
the time of each past decision** — never mutated retroactively.

### 17. Revocation and participant removal

Revocation ends the Foundation association's validity for future resolution. **Revoking the Foundation
association never inherently deletes the provider account, deletes credentials, deletes provider data,
revokes a provider's own OAuth authorization, or erases external history** — those remain the
provider's or the owning capability's own responsibility where supported. When a Person departs the
household: active associations stop resolving for any future personal-resource request; association
records follow accepted deletion/retention governance; provider accounts and resources remain untouched
unless a separate, explicit governed operation changes them; and erasure/portability consumes **DL-136**
unchanged. No active, resolvable personal-resource binding is ever left orphaned to a removed Person,
and the underlying device or provider resource is never deleted merely because the Person relationship
ended.

### 18. Stale, broken, and missing associations

Where an association references an integration/resource that no longer resolves, it is reported as
**broken/stale** using the existing lifecycle/reference semantics (**P30**, **DL-41**) — *"that calendar
association points to a resource that is no longer available."* HTBW never silently selects another
resource, falls back to another Person's, substitutes a household resource, approximates from local
history, or infers a replacement from observed usage. Where the resolved Person has **no** applicable
association, the dependent capability is simply unavailable — *"I can't answer that because no calendar
is associated with your Person configuration"* — with no silent creation, inference, or substitution.

### 19. Retention

The External-Resource Association is governed data under **DL-47**. **No arbitrary numeric duration is
invented here**, consistent with the corrected **DL-137** philosophy this decision explicitly adopts:
*architecture provides the governance mechanism; the household provides the retention value.* The
active/current assignment persists while configured; change, reassignment, and revocation history
follow the existing governed Change Record/historical-record lifecycle; Preservation Hold, deletion,
Tombstone, portability, and structural-record rules retain their separately accepted semantics
unchanged. No independent architectural floor or ceiling is created for this record class, exactly as
none exists for Explainability (DL-137, amended) or Communication (DL-138) retention.

### 20. Deletion and erasure

Consuming **DL-136** unchanged: erasure of the HTBW association record does not imply, assert, or cause
erasure of the underlying external resource. The operation distinguishes the **HTBW Person-resource
association** from the **internal device, Home Assistant resource, or external provider resource** it
references. Where association deletion occurs, lifecycle/Tombstone rules apply, the resource remains
authoritative and untouched in its owning system, and no false provider/device deletion claim is ever
made.

### 21. Explainability and versioning

A governed decision or action using an External-Resource Association records, through the existing
**Decision Trace → Explainability Record** model and the existing **DL-104** Governed Reference shape
(`{Subject Type: Person-scoped External-Resource Association assignment, Subject ID, Version
Identity}`): the association's exact Record Identity and version in effect at the time, the resolved
Person, the applicable provider/resource reference, and the authorization outcome where Explainability
rules require it. **Provider configuration is never copied into the Explainability Record.** Historical
Explainability remains able to state *"I used the calendar that was associated with Tom at that time"*
even after a later reassignment — no new versioning subsystem, provider snapshot, or credential history
is created; the existing Governed Reference mechanism is reused unchanged.

### 22. Use Case 6 — status change

`docs/scenarios/continuity-use-cases.md` Use Case 6 ("Person-to-Calendar and Person-to-Mailbox
Associations") changes status from **U** (unresolved) to **A** (accepted): **"A governed
person-to-external-resource association with a named owner"** is now **Foundation**, under this
decision. Use Cases 2, 4, 5, and 11 are updated to reflect the same resolved ownership where they cite
it; none of their own, separately-governed open items (interruption classification, audience
specification, delivery/acknowledgement semantics, and so on) is decided here.

---

## Explicit non-goals

- **No new responsibility is created.** Foundation's existing remit is extended to one more relationship
  type and one more Person-scoped assignment; no eighth responsibility, no "Association" responsibility,
  and no "Resource Governance" responsibility is introduced.
- **No provider abstraction is designed or presumed.** This decision does not define a universal
  provider interface, connector framework, or capability-negotiation protocol.
- **No credential, token, or secret storage is introduced anywhere in HTBW.**
- **Household Memory is not revived.** `household-memory-model.md` and `household-memory-contract.md`
  remain Historical — superseded; their former ownership boundaries are not reactivated by this
  decision.
- **Internal Person-device relationships (BLE, phone, watch, private interaction endpoints) are not
  redesigned, reassigned, or reopened.** They remain exactly as DL-32 (Identity) and the Delivery
  Surface model (Continuity) already hold them; §2 above records why they are not cited as literal
  Foundation precedent, without altering their ownership in any way.
- **`linked_area_id` / Person-to-Room-default is not absorbed into this decision.** That residual
  remains where **DL-113** (OD-73) left it: available for a future decision to pick up, not decided,
  required, or precluded here.
- **Stewardship's custody/Counterparty question is not resolved here, and `stewardship.md`'s own
  forward-reference to OD-77 is corrected, not extended.** `stewardship.md` speculatively cross-referenced
  OD-77 for "whether a role-bearing construct later supersedes" a custody record's free-text Counterparty
  designation. **This decision does not resolve that question** — the External-Resource Association
  (**DL-85**) is a structurally different construct (a Person-to-external-resource reference) from a
  custody record's accountable-party designation (which may reference a Foundation object **or** remain
  free text for a non-Foundation counterparty). No generic role-bearing-relationship construct is created
  by this decision. `stewardship.md`'s cross-reference is corrected to record this as a still-open,
  unassigned future question, not as something DL-139 answers.
- **DL-115/OD-90 is not reopened.** The Home-scoped assignment and its own reasoning stand unchanged.
- **DL-93's Reasoning Provider Strategy is not reopened.** Provider availability, authorization gates,
  and fallback order are unaffected; this decision resolves only which configured provider profile is
  referenced for a Person.
- **Continuity's, Identity's, and Operational Trust's existing ownership boundaries are not narrowed,
  widened, or reassigned.**

---

## Related documents

- [adr-home-identity-and-home-intelligence-governance.md](adr-home-identity-and-home-intelligence-governance.md) — DL-84/85/86, and the original OD-90/OD-77 reconciliation this decision completes
- [../contracts/foundation-contract.md](../contracts/foundation-contract.md)
- [../models/person-and-identity.md](../models/person-and-identity.md)
- [../models/continuity.md](../models/continuity.md)
- [../contracts/continuity-contract.md](../contracts/continuity-contract.md)
- [../scenarios/continuity-use-cases.md](../scenarios/continuity-use-cases.md)
- [../models/operational-trust.md](../models/operational-trust.md)
- [../models/glossary.md](../models/glossary.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
- [adr-reasoning-provider-strategy.md](adr-reasoning-provider-strategy.md)
- [adr-home-steward-product-boundary.md](adr-home-steward-product-boundary.md)
- [../models/stewardship.md](../models/stewardship.md) — corrected cross-reference only; custody/Counterparty question not resolved here
