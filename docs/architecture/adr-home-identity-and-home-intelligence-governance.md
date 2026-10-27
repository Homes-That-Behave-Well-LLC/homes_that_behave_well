# ADR: Home Identity and Home Intelligence Governance

> **Document status: Canonical ADR.**
> Status: **Accepted** 2026-10-14. Records **DL-84**, **DL-85**, and **DL-86** (issue **#191**, formal
> acceptance review PASS). This acceptance was not propagated into this banner until 2026-10-27, during
> the OD-67/#132 remediation — see *Notes on the 2026-10 Home Identity and Home Intelligence
> Architecture Review* in [../governance/decision-ledger.md](../governance/decision-ledger.md).
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Terminology: [../models/glossary.md](../models/glossary.md).

---

## Status

**Accepted 2026-10-14.** Formal acceptance review on Issue #191 recorded **PASS**. (Propagation into
this banner, the decision ledger, `document-register.md`, and `glossary.md` was delayed until
2026-10-27; no re-review occurred — the delay is a bookkeeping gap, not a substantive change.)

Drafted by the 2026-10 Home Identity and Home Intelligence Architecture Review, following an owner
discussion concerning HTBW Identity (Home, Individual, Guest), Home-owned email and calendar,
caretaker/personal calendars, Asset Intelligence source sharing, a Home Intelligence product boundary,
Concierge and Voice address semantics, and governed information sharing and provenance. Consistent
with this repository's established practice that a drafted decision is recorded first and separately
undergoes formal acceptance review before being treated as binding (see *Notes on the custody and
obligation-lifecycle decision* and *Notes on the 2026-10 AI, Natural Interaction, and Household
Knowledge Architecture Review (DL-80–DL-83)* in
[../governance/decision-ledger.md](../governance/decision-ledger.md)). **It does not authorize,
schedule, or require any implementation.** No discovery protocol, trust-establishment mechanism,
email/calendar provider, hardware, operating system, or on-premises server is built, selected, or
provisioned by this ADR.

This ADR creates **no new responsibility**. The seven responsibilities recorded in **DL-01** —
Foundation, Stewardship, Identity, Truth, Continuity, Operational Trust, Concierge — are unchanged.
**OD-67** (Reasoning Provider Strategy) is unchanged; its own persistence/provider-strategy question is
drafted separately as **DL-93** (pending #132). **OD-77** (Person-to-External-
Resource Association Ownership), **OD-20** (Optional Asset Intelligence Product Integration), **OD-81**
(HTBW Capability Exposure and Self-Consumption), **OD-82** (HTBW Product Consolidation and
Retirement), **OD-85** (Adoption Scope, Artifact Custody, and Coexistence Behaviour), **OD-90**
(Home-to-External-Resource Association Ownership, #189), and the wake-word sub-question already
carried by **OD-86** [the vocabulary-supersession decision, not to be confused with this ADR's own
**DL-86**] are each referenced below and remain **open, unaffected** — none is narrowed, resolved, or
reopened by this ADR.

---

## Context

An owner discussion raised a cluster of related questions: should "the Home" be addressable and own
resources in its own right, distinct from any individual resident; how does a Home-owned mailbox and
calendar relate to a resident's personal mailbox and calendar; how should Asset Intelligence's existing
asset and document knowledge become available to a future AI-assisted household-knowledge capability
without duplicate configuration; and should such a capability be installable as a separate, optional
product.

Review against current authority found:

- **Guest and caretaker are already correctly modelled** as Roles/relationships, not identity classes
  (**DL-33**; `glossary.md`'s *Role* and *Caretaker* entries; the Foundation `caretaker-of`
  relationship type). This is restated below, not reopened.
- **The Person-to-external-resource association question is already open and unresolved as OD-77**
  (#148) — mailbox, calendar, and other external-service references are explicitly named in
  `person-and-identity.md`'s Person-extension table with **no responsibility assigned**. OD-77 is
  Person-scoped by its own title and source evidence.
- **No document describes the Home itself as capable of owning an external mailbox or calendar
  account**, despite `home.md` already naming a "home maintenance calendar" among Home-scoped state,
  and despite Stewardship already owning "caretaker-calendar projections" and "the home-maintenance
  calendar" among its representative obligations (`framework.md`).
- **A Household Knowledge Provider ingestion → retrieval → reasoning pipeline is already drafted as
  DL-81** (`adr-household-knowledge-provider-governance.md`, pending **#188**), consuming Asset
  Intelligence's asset-to-document relationships and existing Document Storage by reference. That ADR
  is explicit that it is architecture only, selects no hardware, and is not a product or deployment
  boundary — it describes a pipeline, not an installable, optional, separately-failing product.
- **No document distinguishes Home-owned resources from person-owned resources as a general
  principle**, though the distinction is already implicit throughout Foundation, Stewardship, and
  Continuity (for example, Continuity's person-scoped versus room-scoped preference split, and
  Foundation's `home.md` versus `person-and-identity.md` scope split).

This ADR closes those three narrow gaps and explicitly declines to re-litigate anything already
decided.

---

## Decision 1 — Home Identity (DL-84)

**The Home is a first-class, identity-adjacent Foundation object, distinct from Person (Individual)
and from Guest.** "Identity-adjacent" is deliberate: the Home is a **definitional Foundation subject**
— it already owns "Home identity and identification" per `home.md` — and it is **never** an outcome of
the **Identity** responsibility's confidence/attribution model. Identity answers *who do we believe
this human is*, with confidence, evidence, and purpose-scoped assertions (**DL-05**, **DL-32**,
**DL-38**); the Home is never evaluated for confidence, is never a candidate in an Identity Fusion
Function candidate set, and produces no Identity Assertion. A household addressing "the Home" (for
example, in conversation) is addressing a known, configured Foundation subject — not an attribution
outcome.

This is a **restatement and formalization** of what `home.md` already establishes (the Home as "the
outermost governed scope," owning Home-scoped identity, configuration, and policy), made explicit
because the owner discussion and `home.md` itself use the word "identity" for the Home without stating
how that relates to the **Identity** responsibility's Person-confidence model. **No change to `home.md`
itself is required by this decision** beyond the cross-reference below; Foundation's ownership of Home
identity and identification is unchanged. **The precise construct, ownership, resolution, and
Decision Trace treatment this implies are stated exhaustively in *Home identity semantics, resolved
precisely*, below** — this is not merely asserted.

### Home, Individual, and Guest are three distinct concepts, only two of which are identity classes

| Concept | What it is | Owning responsibility | Identity-responsibility participant? |
|---|---|---|---|
| **Home** | A Foundation definitional subject — the outermost governed scope and container | Foundation | **No.** Never attributed, never confidence-scored, never an Identity Assertion subject |
| **Individual (Person)** | A Foundation object representing a known human, extended by Identity, Continuity, Operational Trust, and Stewardship | Foundation (definition); Identity (evidence/confidence) | **Yes.** The subject of Identity Assertions, confidence bands, and evidence fusion |
| **Guest** | **Not a fourth identity class.** A Role (`glossary.md`'s Role examples: resident, owner, child, **guest**, caretaker, service provider), applied either to a **Known Non-Resident Person** a household deliberately configures, or to the **Unidentified-Person Policy** Operational Trust applies when Identity yields Unknown Person | Operational Trust (the policy); Foundation (the Role, when applied to a configured Person) | **No**, as a class. A Known Non-Resident Person carrying a guest Role *is* a Person and therefore an ordinary Identity participant; "Guest" itself names a trust-and-permissions construct, never an attribution state (**DL-33**) |

**Caretaker is likewise confirmed, not newly decided, as a Role/relationship rather than an identity
class** — `stewardship-contract.md` already defines caretaker assignment "through the Foundation
caretaker-of relationship type," and `glossary.md`'s Role entry already lists caretaker as an example.
An Individual carries a caretaker relationship to a Home, a Room, an Asset, a Person, or a Pet; the
Home never carries a caretaker relationship *to* an Individual in the reverse sense, and no new
relationship type is created by this decision.

### Home identity semantics, resolved precisely

The owner discovery was that **Home is a first-class identity.** This section states exactly what that
means, using only constructs this repository already has, so the placement is demonstrable rather than
asserted.

**Two Foundation terms are distinguished, neither of them new in substance — both previously implicit
and now named:**

| Term | Definition | Who currently qualifies |
|---|---|---|
| **Identity Subject** | Any Foundation object that carries a stable, canonical, governed identifier other records reference — Foundation's existing, general "Provides: Canonical identifiers for every household object" (`home.md`). Every Foundation object type is already an Identity Subject; this is not Home-specific | Home, Room, Person, Asset, Pet |
| **Identity Participant** | The narrower subset of Identity Subjects additionally evaluated by the **Identity** responsibility's confidence/attribution/evidence-fusion model (**DL-32**, **DL-38**) | **Person only** |

**Home is an Identity Subject. Home is never an Identity Participant.** This is the precise sense in
which Home is "a first-class identity": it has its own stable, governed, Foundation-assigned identity
— exactly as a Room or an Asset does — and that identity is never confidence-scored, never fused from
evidence, and never the subject of an Identity Assertion. "Identity-adjacent" in this ADR's banner
means exactly this: adjacent to the **Identity responsibility**, not absent from **Foundation's
identity concept**. No new identity class, and no third category alongside Identity Subject and
Identity Participant, is created.

Answering the seven questions precisely:

1. **What kind of construct is Home?** A Foundation object and Identity Subject (above) — not an
   identity class, not a Person, and not an Identity Participant.
2. **Which responsibility owns the authoritative Home record?** **Foundation**, unchanged. `home.md`
   already states this ("Foundation... owns the canonical definitions of... Home"); this decision adds
   no second owner and copies nothing out of Foundation.
3. **Which responsibility resolves Home as the addressed conversational subject?** **Concierge**,
   consuming a **Foundation**-owned resolution — exactly the existing division of labour in
   [contextual-vocabulary-contract.md](../contracts/contextual-vocabulary-contract.md): *"Foundation —
   Room Configuration owns the mapping. Concierge consumes the resolved target."* Addressing "Home" is
   a **Home-scope vocabulary resolution**: the same deterministic term-to-target mechanism Contextual
   Vocabulary already uses for a Room or an Asset, applied to a target at Home scope rather than
   confined to a Room Context. This decision extends the **target type** the existing mechanism may
   resolve to (adding the Home object itself); it creates no second resolution mechanism and does not
   move vocabulary ownership from Foundation to Concierge.
4. **How does Home own resources and participate in relationships and authorization without becoming a
   Person?** It already does, unchanged by this decision: `home.md`'s "Owns" list (Rooms, People,
   Pets, Assets, Services, Relationships) and Relationship scope ("Person has a Role in the Home")
   already make the Home a first-class relationship participant, and Operational Trust already governs
   authorization generically over Foundation objects and their roles/relationships — it does not
   require its subject to be a Person. An Asset already owns relationships and is scoped by
   participation/exposure/authority (**DL-11**) without being a Person; Home is simply the outermost
   such Foundation object. No Person-specific mechanism is extended to Home, and no Home-specific
   authorization mechanism is created.
5. **What governed identifier is resolved when someone addresses "Home"?** The Home's own existing
   Foundation-assigned canonical identifier — the same identifier `home.md`'s "Provides" section
   already names ("Canonical identifiers for every household object") and the same one every other
   Home-scoped record already references. No new identifier type is created.
6. **How does the addressed Home appear in the Decision Trace?** As a **resolved vocabulary target**,
   under Foundation's existing explainability contribution (`foundation-contract.md`: "Vocabulary
   resolution and its mapping source; Authoritative object names used in the human-readable
   explanation") — the same field that already records a resolved Room or Asset target. **It is not an
   Actor and not a Person Attribution outcome** (**DL-73**'s Known Person / Unknown Person / No Person)
   — the speaking resident remains the Actor; "Home" is the resolved *target* of the utterance, a
   different, already-existing Decision Trace dimension. No new Decision Trace field is created.
7. **How does this relate to the existing Home model and to installation-level identity?** The "Home
   construct" named by this decision **is** `home.md`'s existing Home object — not a parallel or
   second concept. This repository has no separate "installation identity" construct; the only
   adjacent open question is **OD-01** ("Whether a Home is represented as a Home Assistant config
   entry, subentry, or private record"), which concerns the Home's **platform-level backing
   representation** and remains entirely unresolved and unaffected by this decision. DL-84 states what
   the Home **is** architecturally; OD-01 states how it is **technically represented** in Home
   Assistant — the two are complementary, not competing, questions.

### What this decision does not do

- It does **not** create an eighth responsibility, an "Identity" participant status for the Home, or a
  confidence/attribution model for the Home.
- It does **not** reopen **DL-33**'s prohibition on a synthetic Guest Person, or `glossary.md`'s
  existing Role and Caretaker definitions.
- It does **not** change how Person, Unknown Person, or Known Non-Resident Person are defined.
- It does **not** create a third identity category alongside Identity Subject and Identity Participant.
- It does **not** create a new identifier type, a new vocabulary-resolution mechanism, a new
  authorization mechanism, or a new Decision Trace field.
- It does **not** decide **OD-01** (Home's Home-Assistant-level backing representation), which remains
  entirely open and unaffected.

---

## Decision 2 — Home-Owned Resources, Home Calendar, and Governed Sharing (DL-85)

### Home-owned resources, in principle

Resources and responsibilities that belong to the household as a whole — rather than to one
individual's caretaking of it — may be declared as **Home-owned**, consistent with `home.md`'s existing
"Owns" list (the set of Rooms, People, Pets, Assets, Services, Relationships) and Home-scoped state
(security posture, safety policy, quiet hours, the home maintenance calendar, global autonomy ceiling,
default privacy policy). This decision adds, as Home-scoped resource **categories** (not as a new
responsibility, and not deciding their association-ownership mechanics — see **OD-90**, #189):

- a **Home mailbox** — for service, vendor, warranty, invoice, and appointment correspondence directed
  at the household rather than at one resident
- a **Home calendar** — the authoritative schedule of what the Home is responsible for, and when
  (defined precisely below)

**Which responsibility owns the binding between the Home and the actual external mailbox/calendar
account is not decided here.** It is routed to **OD-90** (#189), reconciled with the already-open
**OD-77** (#148, Person-to-External-Resource Association Ownership) precisely below — not merely
"evaluated together," but governed by one shared relationship-type definition so the two cannot
diverge.

### Reconciling OD-90 with OD-77: one shared relationship type, two separate assignment decisions

Four options were evaluated for how a Home-scoped and a Person-scoped external-resource association
relate: (a) two specializations of one governed-subject-to-external-resource contract; (b) one fully
merged decision with Home- and Individual-specific policy; (c) separate ownership decisions sharing a
required common contract; (d) genuinely different architectures, reason documented. **The adopted
resolution combines (a) and (c), and rejects (b) and pure (d), for a reason grounded in existing
precedent:**

- **Foundation already separates relationship-TYPE definition from relationship-ASSIGNMENT ownership**
  for exactly this shape of problem: `foundation-contract.md` states "Foundation defines the
  **caretaker-of relationship**; the **caretaker assignment** itself is owned by Stewardship." The same
  split resolves this reconciliation without inventing a new pattern.
- **A new Foundation relationship type, External-Resource Association, is named** (not newly invented
  as a mechanism — formalizing what `person-and-identity.md`'s already-unassigned "Mailbox, calendar,
  and other external-service references" row and `home.md`'s Home-scoped resources both need): a
  **subject** (a Home or a Person — not limited to these two for the future, but **no other subject
  type is in scope of OD-77 or OD-90**), an **external resource reference** (never its content or
  credentials — **DL-46**), and a fixed minimal lifecycle shape: creation, disclosure, reassignment,
  revocation, stale-detection, retention (**DL-47**), and Decision Trace citation (**P30**). **Both
  OD-77 and OD-90 must adopt this shape as a floor on their own acceptance criteria.** This is where
  option (a) applies: OD-77 (subject = Person) and OD-90 (subject = Home) are two specializations of
  one relationship type, and cannot diverge in lifecycle, revocation, provenance, retention, or
  Decision Trace behaviour even though they are decided separately.
- **The assignment-owning responsibility is explicitly not forced to be the same for both subjects**,
  and is **not decided here** for either: this is where option (c) applies, and why full merge (option
  b) is rejected. A Person's external-resource assignment sits inside the Person Extension's
  **distributed-ownership model** (**DL-71**: "each extension keeps its own owner" — Foundation,
  Identity, Continuity, Operational Trust, and Stewardship each already own a different slice of a
  Person's configuration), which is exactly why OD-77 itself carries five live alternatives (A–E) under
  active discussion. The Home carries no equivalent distributed-ownership model — `home.md`'s "Owns"
  list is a single flat Foundation list — so a Home-scoped assignment is structurally simpler and does
  not inherit OD-77's distributed-ownership complexity. **Forcing one merged decision would either
  prematurely import Person's distributed-ownership complexity onto the Home, or prematurely simplify
  Person's genuinely harder question — both are rejected as outcomes, which is why option (b) is not
  adopted.** Pure option (d) — treating them as genuinely unrelated — is also rejected, because it is
  precisely what would permit the divergence in lifecycle/revocation/provenance/failure-behaviour this
  reconciliation exists to prevent.
- **Per Maintenance Rule 1** (`open-decision-issue-index.md`: "one open decision, one issue; never one
  issue for two separately closeable decisions"), **OD-77 and OD-90 remain two separate, independently
  closeable decisions.** Each may close with a different assignment-owning responsibility. Neither
  closure is valid, however, unless the closing text names the shared External-Resource Association
  relationship-type shape above and confirms conformance to it — this is added to both decisions'
  acceptance criteria (see **#189** and the follow-up comment on **#148**).

**This is not itself a final architectural decision**; it is this review's own drafted reconciliation
of how OD-77 and OD-90 relate, recorded here pending the same **#191** formal acceptance review, and
does not resolve either OD-77's or OD-90's own open question (which responsibility, for each subject,
owns the assignment).

### The Home Calendar is a distinct capability from a personal or caretaker calendar

Formalizing what `home.md` and `framework.md` already name but do not fully distinguish:

| | Home Calendar | Individual / Caretaker Calendar |
|---|---|---|
| **Question answered** | *What is the Home responsible for, and when?* | *What is relevant about the schedule of a person who may fulfill or participate in that responsibility?* |
| **Owner** | Stewardship owns the obligations it schedules (service, inspections, deliveries, housesitter periods); Foundation's Home scope is the definitional container `home.md` already names | Continuity (person-scoped preferences, reminders) and, where connected, the external provider that is the system of record (**DL-46**) |
| **Example** | "HVAC service appointment scheduled" | "Reminder: schedule HVAC service," on Tom's personal calendar |

**A personal reminder never marks a Home obligation as scheduled or completed, and creating one is not
a Stewardship action.** This restates, rather than changes, the existing boundary: Stewardship owns the
obligation and its condition/lifecycle state (`met`, `due`, `unmet`, `overdue`, `waived`, `unknown`;
`raised`, `active`, `deferred`, `closed`, `reopened`); only a **Care Evidence Record** closes an
obligation (`stewardship-contract.md`). A Home Calendar appointment is evidence Stewardship may
evaluate; it is never itself the obligation, and a personal reminder is weaker evidence still — it is
Continuity's own record of what one person intends to do, carrying no Stewardship authority at all.

### "Share with Home Intelligence: Yes/No" is governed disclosure, not bulk copying

Where a Home-owned or person-owned source is already configured within the HTBW capability that owns
its meaning (a Home mailbox, a Home calendar, an Individual's own permitted personal calendar, or Asset
Intelligence's asset/document relationships under **DL-81**), that capability may expose an explicit,
source-specific:

```
Share with Home Intelligence: Yes / No
```

**This is governed, revocable disclosure to the Household Knowledge Provider pipeline already drafted
in DL-81 — it is never a V1 requirement, and it never means every message, document, or event is
automatically and permanently copied into an AI/vector datastore.** Specifically:

- It reuses the **existing** consent/disclosure model rather than inventing a second one: Operational
  Trust remains the owner of "who may access calendars, messages, email, or history" and of disclosure
  evaluation (**DL-34**, **DL-36**); consent capture/revocation follows the existing consent record
  shape (**DL-56**) where applicable.
- It does not relax **DL-81**'s own constraints: no competing asset catalog or document repository is
  created, Asset Intelligence and Document Storage remain authoritative for asset identity, asset-to-
  document relationships, and original documents, and household knowledge ingestion remains architecture
  only pending **#188**.
- It does not relax **DL-82**'s provenance requirement (pending **#188**): an answer drawing on a
  shared source must identify its source class and must never blend classes without disclosure.
- Retention, indexing, retrieval, classification, and derived-data handling for any shared source
  follow whatever governed policy applies to that capability; this ADR does not invent a retention or
  indexing policy, consistent with **DL-81**'s own deferral of those mechanics to **#186**.
- An Individual's own personal calendar or mailbox participating in "Share with Home Intelligence" is a
  **person-scoped permission that must not be inferred from the Individual's relationship to the
  Home** — restating, not changing, the existing rule that an Individual's resources are never
  automatically available merely because the Individual is a caretaker or resident (`stewardship-
  contract.md`: "Accountability is not access").

### Asset Intelligence source sharing, specifically

Where Asset Intelligence is consumed at all (an **OD-20**, #110 question, unaffected and not decided
here), enabling `Share with Home Intelligence: Yes` for it makes available **both** the governed asset
model **and** its governed document relationships through the pipeline **DL-81** already defines — by
reference, never by copy, and never creating a second asset or document authority. The household is
never required to separately re-describe Asset Intelligence's database, filesystem path, or document
relationships to a Home Intelligence consumer; this restates **DL-81**'s "consumed by reference from
Asset Intelligence" clause and decides nothing new about it.

---

## Decision 3 — Home Intelligence as an Optional Product/Deployment Boundary (DL-86)

**Home Intelligence** is named as the optional, separately deployable product/deployment boundary that
may host and implement the **DL-81** Household Knowledge Provider pipeline and a **OD-67** (#132)
Reasoning Provider. This decision is analogous to, and reuses the pattern of, the standalone Asset
Intelligence product boundary already accepted in **DL-08** and narrowed in **OD-20** (#110): a
responsibility or capability may be first-class or architecturally defined inside HTBW while the
software that implements it ships and is installed separately.

### What this decision establishes

- **Home Intelligence is optional.** No HTBW Core capability may require it to be installed. Where a
  capability depends on it, that dependency is **declared** under **DL-41**: absence makes the
  dependent capability **unavailable**, reported and named — never silently degraded, approximated, or
  emulated.
- **Home Intelligence has its own deployment/failure domain.** It may have a separate repository,
  software lifecycle, compute/failure domain, independently installable software package, and versioned
  API boundary to Home Core (Home Assistant, HTBW, and Concierge). **This ADR selects none of those
  mechanics** — see **#190** for the residual discovery/trust-establishment/deployment-mechanics
  research this decision explicitly defers.
- **Home Intelligence does not require a separate normal household configuration experience.** HTBW
  remains the primary configuration and operating surface. The expected household-facing shape —
  install the package, the service starts its discovery capability, HTBW offers
  `Use Home Intelligence: Yes/No`, and setup/source-sharing/review/status/diagnostics are presented
  through HTBW — is captured here as the **required outcome**; the discovery and trust-establishment
  **mechanism** is explicitly not decided (routed to **#190**), per **P14** (important mappings are
  explicitly configured, not guessed through hidden runtime discovery) and the **DL-30** ordered burden
  of proof (a native Home Assistant discovery mechanism must be evaluated before any HTBW-specific one).
- **Home Core failure independence.** If Home Intelligence is unavailable, rebooting, upgrading, or has
  failed, deterministic room/device control, existing HTBW capabilities that do not depend on it, and
  Concierge's core orchestration must continue. Concierge degrades appropriately (per
  [failure-and-degradation.md](failure-and-degradation.md)) rather than failing Home Core. This restates
  **DL-41**'s existing "declared dependency, absence is unavailable not degraded" invariant for this
  specific optional product, and restates **OD-67**'s existing "deterministic behaviour continues where
  no provider is available" invariant; it creates neither.
- **No technology stack is selected.** Candidate technology discussion (Ubuntu/Linux, local model
  runtimes, local inference, structured storage, semantic retrieval) remains non-authoritative, exactly
  as **DL-81** already states for the pipeline it hosts.

### Action boundary (restated, not created)

Home Intelligence reasoning, contextual interpretation, and recommendation-origination never become
authorization. This restates **OD-67**'s existing invariant ("a reasoning provider owns nothing... a
recommendation never silently becomes an authorised action") and **DL-83**'s existing generated-
behaviour lifecycle (**Generate → Validate → Explain → Authorize → Persist → Observe → Review →
Revise-or-Retire**) and **DL-80**'s existing compound-intent decomposition under Concierge's ownership.
Where a resident request results in Home Intelligence interpretation, the resulting structured intent
or proposed action still passes through the same HTBW authoritative-capability validation, Identity
resolution, and Operational Trust authorization every other Concierge-orchestrated action does. No new
action-authorization model is created.

### Voice/Concierge address semantics (restated, not created)

Addressing the system as "Home" is household-facing vocabulary that now has an explicit semantic
referent: **DL-84**'s Home Identity, the Foundation subject — never Home Assistant, a specific vendor
assistant, a reasoning provider, or the Home Intelligence host as a device. **This creates no wake-word
decision.** `decision-ledger.md` already records "No wake-word decision is opened" (wake-word detection
occurs before any HTBW responsibility engages, is a native satellite capability evaluated under **DL-30**
at item 11 of **#146**, and its only household-facing consequence is already an **OD-86** sub-question
deferred behind #146). The existing architectural separation — wake word → intentional invocation →
speech/Concierge → speaker/room/identity context → interpretation → governed action — is unchanged, and
Concierge is not coupled to any particular wake word by this decision.

---

## Relationship to existing open decisions and reviews

| Open item | Relationship to this ADR |
|---|---|
| **OD-77** (#148) | **Reconciled, not merged.** Not reopened, narrowed, or resolved. Shares one Foundation-defined External-Resource Association relationship-type shape with the new **OD-90** (#189); remains an independently closeable decision that may select a different assignment-owning responsibility than OD-90 (see *Reconciling OD-90 with OD-77* above). |
| **OD-01** (`home.md`) | Unaffected. Home's platform-level backing representation (HA config entry, subentry, or private record) remains entirely open; DL-84 states what the Home is architecturally, never how it is technically represented. |
| **OD-20** (#110) | Unaffected. Whether/how HTBW Core consumes the standalone Asset Intelligence product remains undecided and is not narrowed here. |
| **OD-67** (#132) | Unaffected. No reasoning provider class, purpose, or disclosure rule is selected here. |
| **OD-81** (#159), **OD-82** (#160) | Unaffected. Home Intelligence's product-boundary treatment is analogous to, not a resolution of, the capability-exposure and product-consolidation questions those decisions hold open. |
| **OD-85** (#172) | Unaffected. Asset Intelligence adoption scope, custody, and coexistence remain governed entirely by OD-85; this ADR's "Share with Home Intelligence" is a disclosure question, not an adoption/custody question. |
| **DL-81**, **DL-82** (pending **#188**) | Extended, not altered. DL-85 and DL-86 build on DL-81's pipeline and DL-82's provenance model without changing either. |
| **OD-86** wake-word sub-question (#174) | Unaffected. Restated above without reopening. |
| **#186**, **#187** | Unaffected siblings. **#190** is this ADR's equivalent residual-mechanics issue for the Home Intelligence product boundary. |

---

## Explicit non-goals

- No new responsibility is created.
- No eighth framework layer, no Identity-responsibility status for the Home, and no confidence/
  attribution model for the Home. No third identity category alongside Identity Subject and Identity
  Participant.
- No new identifier type, vocabulary-resolution mechanism, authorization mechanism, or Decision Trace
  field.
- No email provider, calendar provider, discovery protocol, trust-establishment mechanism, hardware,
  operating system, model, vector database, or orchestration platform is selected, built, or required.
- No existing Open Decision is reopened, narrowed, or resolved — including **OD-01** and **OD-77**,
  each of which remains entirely open and independently closeable. The OD-77/OD-90 reconciliation
  above fixes a **shared relationship-type shape** only; it does not select either decision's
  assignment-owning responsibility.
- No superseded document (`asset-intelligence-contract.md`, `calendar-email-experience-contract.md`,
  `identity-governance-reference.md`) is reinstated as authority.
- **This entry is drafted content, not yet a closed decision; it must not be cited as equivalent to
  DL-01–DL-83 until #191's formal acceptance review records a result.**

## Related documents

- [../governance/decision-ledger.md](../governance/decision-ledger.md) — DL-84, DL-85, DL-86; OD-90
- [../governance/open-decision-issue-index.md](../governance/open-decision-issue-index.md)
- [adr-household-knowledge-provider-governance.md](adr-household-knowledge-provider-governance.md) — DL-81, extended by DL-85/DL-86
- [../models/decision-trace.md](../models/decision-trace.md) — DL-82
- [../models/home.md](../models/home.md), [../models/person-and-identity.md](../models/person-and-identity.md)
- [../contracts/stewardship-contract.md](../contracts/stewardship-contract.md), [../contracts/continuity-contract.md](../contracts/continuity-contract.md)
- [../models/glossary.md](../models/glossary.md)
