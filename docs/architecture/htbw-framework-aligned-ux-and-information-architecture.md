# HTBW Framework-Aligned User Experience and Information Architecture

> **Document status: Active — subordinate to the HTBW canonical architecture.**
> Canonical authority: [north-star.md](north-star.md), [framework.md](framework.md), and
> [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Where this document names **Asset Intelligence** or **Voice Identity** as an ownership domain, it
> refers to the separately released **repository**, not to an HTBW Core layer. See
> [../models/glossary.md](../models/glossary.md) section "Products versus responsibilities".

## 1. Purpose and non-authorization

This document establishes a governed user-experience and information-architecture (UX/IA) direction
for Homes That Behave Well (HTBW): the Behaves Well Framework (BWF) as the primary HTBW mental model
and navigation structure, organizing operational configuration, household knowledge, current-state
presentation, Stewardship and attention, meaningful history, conversational navigation, and
commissioning/validation.

This document is architecture and documentation only. It is:

- **not** authorization to build the UI;
- **not** authorization to redesign accepted BWF responsibility boundaries;
- **not** authorization to invent new business logic in frontend components;
- **not** a Decision Ledger entry and **not** a new ADR. No material architectural decision not
  already governed by the Decision Ledger is made here (§14).

Where the direction requested of this document conflicted with accepted architecture, the conflict is
surfaced rather than silently resolved (§4, §14).

## 2. Repository grounding performed

Before drafting direction, the following authority surfaces were reviewed:

- Authority: [authority-order.md](../governance/authority-order.md),
  [decision-ledger.md](../governance/decision-ledger.md),
  [document-register.md](../governance/document-register.md),
  [document-lifecycle.md](../governance/document-lifecycle.md),
  [open-decision-issue-index.md](../governance/open-decision-issue-index.md).
- Framework: [north-star.md](north-star.md), [framework.md](framework.md),
  [dependency-view.md](dependency-view.md), [runtime-sequence.md](runtime-sequence.md),
  [greenfield-mandate.md](greenfield-mandate.md), [home-assistant-boundary.md](home-assistant-boundary.md).
- Asset model and contracts: [../models/asset.md](../models/asset.md),
  [../contracts/foundation-contract.md](../contracts/foundation-contract.md),
  [../contracts/stewardship-contract.md](../contracts/stewardship-contract.md),
  [../contracts/truth-contract.md](../contracts/truth-contract.md),
  [../contracts/continuity-contract.md](../contracts/continuity-contract.md),
  [../contracts/asset-intelligence-contract.md](../contracts/asset-intelligence-contract.md) (Historical).
- Disposition and adoption: [adr-product-disposition-and-legacy-adoption.md](adr-product-disposition-and-legacy-adoption.md)
  (**DL-51**, **DL-52**).
- Experience, projection, and delivery: [../models/experience-and-session.md](../models/experience-and-session.md),
  [../models/communication.md](../models/communication.md),
  [../contracts/capability-projection-contract.md](../contracts/capability-projection-contract.md),
  [concierge-runtime-architecture.md](concierge-runtime-architecture.md),
  [context-before-intent.md](context-before-intent.md).
- UI: [../patterns/ui-patterns.md](../patterns/ui-patterns.md) (full document, this pass), **DL-104**
  (identifier/reference model), **DL-105** (Materialized Household Assessment artifact pattern).
- External storage: [connected-storage.md](connected-storage.md) (full document, this pass), and the
  standalone Asset Intelligence product's own `document_storage.py` source (inspected directly to
  verify its existing per-Asset, stable-identifier-keyed folder/file convention — §21).
- GitHub (authoritative for status of open decisions only, per authority-order.md rank 7): Epic **#147**,
  **OD-85** (#172), **OD-81** (#159), **OD-20** (#110), **#171**, **#185**. A full open-issue title
  search for UI/frontend/navigation/UX/branding/commissioning-related work found none open beyond
  these already-tracked items (§27 cross-reference, final report item G).

## 3. Architecture Decision Test (per item)

| # | Topic | Disposition |
|---|---|---|
| 1 | BWF as primary HTBW navigation model | **A** — documentation only; already constitutional (north-star.md) |
| 2 | HA technical configuration vs. HTBW operational configuration | **A** — documentation only; the boundary already exists (home-assistant-boundary.md "HTBW Config Entry" row) |
| 3 | Asset Intelligence product lifecycle, HTBW capability, and Adoption | **A/C mixed** — the product/responsibility split is settled (**DL-51**, **DL-52**); the onboarding surface and live-coexistence behavior are **not** (**OD-85**, **OD-20**) — see §7 |
| 4 | One asset record, several perspectives | **A** — already established by asset.md's responsibility table |
| 5 | Foundation/Truth/Stewardship/Continuity asset responsibilities | **A** — already established by the four contracts |
| 6 | Continuity vs. raw telemetry | **A** — already established by continuity-contract.md and temporal-record.md |
| 7 | Subject + Perspective + Scope + Filter + Surface | **A** — new **presentation-layer vocabulary** mapped onto existing governed models; invents no new authority (§9) |
| 8 | Reusable parameterized views | **A** — documentation direction; implementation not authorized |
| 9 | UI must not own business logic | **A** — restates an existing ui-patterns.md principle |
| 10 | Conversation as navigation | **A/C mixed** — Concierge routing concepts are reused as-is; native Home Assistant capability publishing is **OD-81**, open, and not decided here |
| 11 | Multi-surface presentation | **A** — reuses the existing Delivery Surface abstraction (communication.md); no new surface catalogue is created |
| 12 | Subject-first primary navigation (People/Places/Assets); Framework within subject | **A** — clarifies, does not reopen, §5's framework-order rule; People/Places/Assets are already-established object-type ownership, never a new object model (§18) |
| 13 | Breadcrumbs; cross-Framework discoverability | **A** — restates `ui-patterns.md`'s existing, unchanged breadcrumb and cross-domain-navigation rules, extended to the subject-first model (§19) |
| 14 | Framework as education; ownership/location/custody worked example | **A** — restates §6's already-canonical asset-perspective split as a teaching example; no new responsibility ownership (§20) |
| 15 | External Storage Contract | **A** — `connected-storage.md` is confirmed, not newly created, as the canonical contract; the Asset Intelligence/Adoption keying principle is independently verified from the standalone product's own source, not invented (§21) |
| 16 | HTBW Settings | **A** — restates `ui-patterns.md`'s existing Global-Configuration/main-UI boundary; no new category invented (§22) |
| 17 | Native First, Native Extended | **A** — documentation principle; concrete conformance detail added to `ui-patterns.md`, which already owns that level of detail (§23) |
| 18 | Brand, visual system, Framework iconography | **B** — a genuine, currently-unsatisfied requirement (no Framework iconography exists today); recorded as follow-on design work, not decided or produced here (§24) |
| 19 | Household-aware language, progressive disclosure, readiness/health states | **A** — restates already-accepted `ui-patterns.md` and **DL-41** dependency-state rules; invents no new state model (§25, §26) |

No topic in this document required category **D** (new Architecture Decision). Where category **C**
applies, the open decision is named, not pre-empted (§7, §10). **Item 18 is category B** — a
genuinely missing deliverable, not a contradiction or an open decision — and is tracked as follow-on
work (final report, item H), never silently produced by this document.

## 4. Corrected premise: product lifecycle vs. adoption path

The direction that motivated this document initially described Asset Intelligence's "separate
application/sidebar experience" as being "retired through an already-governed migration into HTBW."
That phrasing is imprecise and was corrected during this review. The governed distinction is:

| Concern | Governed answer | Source |
|---|---|---|
| Standalone Asset Intelligence product lifecycle | **Continues indefinitely as a released, independent product.** A household may run it without HTBW. It is never required to be installed for any HTBW outcome | **DL-51** |
| HTBW's own asset capability | HTBW builds and owns a **native** asset capability distributed across Foundation/Truth/Stewardship/Continuity (§6). This is **not** a copy of Asset Intelligence's schema or UI; "absorbs equivalent functionality directly" means HTBW's own responsibility layers independently cover the same household outcomes | **DL-51**, greenfield-mandate.md |
| An existing household's Asset Intelligence data | May be carried into HTBW through **Adoption**: a bounded, resident-initiated, one-time, authoritative, terminating act with no synchronization and no write-back. HTBW becomes authoritative for what is adopted | **DL-52** |
| Standalone integration after Adoption | Removing it is a **per-installation recommendation**, never a requirement, and never an action this document authorizes or decides. HTBW continues to function whether or not that installation's standalone integration is subsequently removed | **DL-52** ("HTBW continues to function if the product is removed") |
| Effect on other households | **None.** Adoption and any subsequent removal are scoped to the one HTBW installation that performed them. The standalone product's availability to every other household is unaffected | **DL-51** |

**This document does not use the word "migration"** for the above, because the repository's own
governed term is **Adoption** (**DL-52**), and "migration" risks implying an ongoing or two-way process
that **DL-52** explicitly forbids. Recommended terminology, for use in all subsequent HTBW UX
documentation and copy:

| Avoid | Use instead | Why |
|---|---|---|
| "Migration" (as a sync or ongoing process) | **Adoption** | Adoption is the one-time, terminating, governed term (**DL-52**); "migration" is undefined in canonical architecture and is easily misread as continuous |
| "Retirement" / "deprecation" of Asset Intelligence | **Standalone Asset Intelligence is not retired** | **DL-51** is explicit and unconditional |
| "Legacy" (applied to the standalone product) | **Standalone Asset Intelligence** | "Legacy" implies the product is sunsetting; **DL-51** says it is not. ("Legacy" remains correct only for **adopted data**, which carries provenance back to a prior state — see **DL-52**) |
| "Coexistence" (undifferentiated) | **Coexistence period** (bounded: before Adoption is initiated, and optionally after, if the household keeps both installed) | Needed because Home Assistant publishing conflicts during this period are a distinct, open question (§7) |
| "Post-migration removal" | **Post-Adoption removal recommendation, scoped to one installation** | Matches **DL-52**'s installation-scoped framing exactly |

## 5. BWF as the primary HTBW navigation model

The seven responsibilities and the question each answers are already constitutional
([north-star.md](north-star.md) §"The Question Each Responsibility Answers"):

| # | Responsibility | Question |
|---|---|---|
| 1 | Foundation | What exists, and how do we describe it? |
| 2 | Stewardship | What matters, and what must be cared for? |
| 3 | Identity | Who do we believe this is? |
| 4 | Truth | What is actually true now? |
| 5 | Continuity | What should be remembered, resumed, or transferred? |
| 6 | Operational Trust | What is allowed? |
| 7 | Concierge | What should happen now? |

This is the **framework order** — "how the framework is taught, assessed, and presented"
(north-star.md). It is distinct from the dependency order ([dependency-view.md](dependency-view.md))
and the runtime sequence ([runtime-sequence.md](runtime-sequence.md)), and **must not be reordered**
to match either.

**Correction to the originally proposed landing-page stack.** A visual ordering of
`Concierge / Continuity / Stewardship / Operational Trust / Identity / Truth / Foundation` (Concierge
at the top, Foundation at the base) was proposed as the HTBW landing-page presentation. That sequence
is neither the framework order nor its reverse (the reverse of the canonical order is `Concierge,
Operational Trust, Continuity, Truth, Identity, Stewardship, Foundation`). A landing page **may**
present the seven responsibilities as a stack with Concierge visually uppermost and Foundation
visually foundational — a legitimate presentation metaphor — but it must use the canonical order or
its exact reverse, not a new sequence. Using the canonical order's reverse for the landing page is the
recommended direction here; it changes presentation only, never the taught/assessed framework order.

The HTBW landing page should function as framework navigation, an explanation of the architecture, and
access to layer-specific views and commissioning — not as a store of completion percentages without
governed meaning. No readiness criteria are established by this document; where a layer's readiness is
already governed (for example by a Repairs issue or a declared capability dependency, per
[home-assistant-boundary.md](home-assistant-boundary.md)), the landing page may reflect it, and
nowhere else.

Home Assistant Settings is preserved as the owner of platform mechanics (integrations, devices,
entities, Floors, Areas, Assist pipelines, scenes, scripts, automations). HTBW Operational
Configuration is already distinguished from it: [home-assistant-boundary.md](home-assistant-boundary.md)'s
comparison table records an **"HTBW Config Entry"** as "HTBW's own configuration," owned by
**Foundation**, distinct from a "Referenced provider or integration configuration," which is owned by
the responsibility governing its use and is subject to **OD-67** (not pre-empted here). This document
adds no new category; it directs that HTBW surfaces present *that* boundary, not reproduce Home
Assistant's integration-setup experience.

## 6. One authoritative asset record, several framework perspectives

**This direction is already canonical.** [../models/asset.md](../models/asset.md) states the
responsibility split exactly as proposed, and this document reconciles with it rather than inventing
anything new:

| Question | Owner |
|---|---|
| What is this thing, and what do we know about it? | **Foundation** asset model |
| Where is it, and what does it relate to — as *declared* knowledge? | **Foundation**, through the `located-in` relationship |
| What are its environmental limits, as a property of the thing? | **Foundation** asset model |
| Who is accountable for it? | **Stewardship** owns the caretaker assignment; **Foundation** defines the caretaker-of relationship |
| Is its environment currently within limits? | **Truth** |
| Does it matter, and how much? What care does it require, and when? Is the obligation met, due, or overdue? | **Stewardship** ([stewardship-contract.md](../contracts/stewardship-contract.md)) |
| What meaningful history persists? | **Continuity** consumes Domain Events and Stewardship/Truth history; it owns none of it as a duplicate store |

**Foundation** owns the durable descriptive record: identity, type, manufacturer, model, serial
number, documents (manuals, invoices, photographs, provenance), environmental limits, the
`located-in`/`serves-room`/caretaker-of relationships, and any Home Assistant device/entity
relationship. Foundation does not own changing observations, obligations, or history
([../models/asset.md](../models/asset.md)).

**Truth** owns current state: current observed location/presence, current environmental Facts
evaluated against Foundation's declared limits, and current status — never a second configuration
surface.

**Stewardship** owns care and obligation: maintenance, tuning, cleaning, service requirements,
environmental-condition attention, escalation, loan/check-out, expected return, custody, and the
completion/resolution of obligations. An intentional, governed absence (an asset on loan) is
represented as a Stewardship-governed state, not as an unexplained Truth anomaly.

**Continuity** presents meaningful history, consuming Domain Events that the owning responsibility
already recorded. [continuity-contract.md](../contracts/continuity-contract.md) already excludes
observations, Facts, and care-obligation history from Continuity's own ownership:

> "Care obligations and their history — medication, veterinary, maintenance, inspection, irrigation |
> **Stewardship**" and "Rainfall, forecast, soil-moisture, and every other environmental observation |
> **Truth**."

Continuity's role is to assemble the *story* — excursion began, obligation created, household
notified, condition recovered, obligation resolved — from records each responsibility already owns and
already records under the shared temporal model
([../models/temporal-record.md](../models/temporal-record.md): "A Domain Event represents a meaningful
occurrence in the household"). Continuity creates no second store and copies no raw observation. The
boundary between a meaningful Domain Event and Home Assistant's own raw history/statistics is not
separately named in `event-model.md` or `temporal-record.md` today; this document does not create that
naming, and flags it as a documentation gap worth a future small clarification to
[../models/temporal-record.md](../models/temporal-record.md) or
[continuity-contract.md](../contracts/continuity-contract.md) — not decided here, and not requiring an
ADR, since no governed outcome changes.

**No asset is copied into separate Foundation, Truth, Stewardship, and Continuity records.** The
household never re-declares a Room assignment in a second layer; Foundation's `located-in` and
`serves-room` relationships carry through into Truth's and Stewardship's presentations automatically.

## 7. Where this document does not decide: open items

Two matters relevant to Asset Intelligence coexistence remain genuinely open and are named, not
pre-empted:

1. **Commissioning/onboarding surface for Adoption — OD-85 (#172), question 4.** The open decision
   records: *"Where is adoption detected, offered, reviewed, and explained? HTBW has no onboarding or
   first-run experience architecture at all... Whether the onboarding gap is resolved here or in a
   separate decision is itself part of this question."* This document's commissioning direction (§13)
   is conceptual only; it does not design, and must not be read as deciding, the Adoption
   detect/offer/review/explain flow. That remains **OD-85**'s to resolve.
2. **Coexistence publishing conflicts and optional live consumption — OD-85 (#172) question 3, OD-81
   (#159), and OD-20 (#110).** If a household runs both products at once — whether before Adoption, or
   indefinitely by choice — both may publish overlapping conclusions to Home Assistant. **OD-85**
   explicitly states *"this decision must say which of the two [OD-69 or OD-81] holds each case, and
   must not create a third owner."* Separately, **OD-20** remains open on whether HTBW Core ever
   **consumes** the standalone product live as an optional evidence source, and through what interface.
   This document's framework-perspective direction (§6) describes where **HTBW's own, native** asset
   capability appears once governed; it makes no statement about simultaneous publishing precedence or
   live cross-product consumption, and **must not be cited as resolving OD-85, OD-81, or OD-20.**

No new Decision Ledger entry or ADR is allocated by this document for either item. If either is
resolved in the household's favor toward a UI treatment, this document should be revisited, not
silently extended.

## 8. HTBW Operational Configuration vs. Home Assistant Settings

Foundation may expose the operational status or configuration of HTBW-owned capabilities (an "HTBW
Config Entry," per [home-assistant-boundary.md](home-assistant-boundary.md)) without reproducing Home
Assistant's integration-setup experience for Floors, Areas, devices, entities, Assist pipelines,
scenes, scripts, or automations — those remain Home Assistant's. Candidate Foundation-surfaced items
(voice/Assist operational relationships, configured reasoning-provider relationships, household
knowledge sources, communication capabilities, HTBW-wide dependency health) require validation against
the owning responsibility's contract before being placed in a specific layer; this document does not
assign them and leaves that validation to implementation planning grounded in the existing contracts.

## 9. Subject + Perspective + Scope + Filter + Surface — a presentation-layer vocabulary

**This is new documentation vocabulary, not a new governed model.** The literal phrase does not appear
anywhere in `docs/` today. It is introduced here strictly as a naming convention over models that
already exist, and it must be read as mapping onto them, never duplicating or superseding them:

| UX term | Maps onto existing governed concept |
|---|---|
| **Subject** | The governed record a view is about — Home, Room, Merged Room, Person, Asset (Foundation), Stewardship obligation, Domain Event — already defined by Foundation's object-type ownership (framework.md §1) |
| **Perspective** | The BWF responsibility supplying the answer (Foundation/Truth/Identity/Operational Trust/Stewardship/Continuity/Concierge) — already the framework order (§5) |
| **Scope** | Room/Floor/Merged Room/whole-household context — already resolved by Concierge's existing local-first contextual resolution ([context-before-intent.md](context-before-intent.md)) and by [capability-projection-contract.md](../contracts/capability-projection-contract.md)'s room/area/floor/household-wide visibility tiers |
| **Filter** | Category/status/time-range/attention-state narrowing — already the kind of narrowing [capability-projection-contract.md](../contracts/capability-projection-contract.md) and the (historical, superseded-by-experience-and-session) experience-projection model perform for visibility/availability |
| **Presentation Surface** | Where the result is rendered — already the governed **Delivery Surface** abstraction ([../models/communication.md](../models/communication.md)): "a governed abstraction of a place through which delivery may occur," declaring supported modality, interactivity, and persistence, with **no surface catalogue** (by design, per **P31**) |

Because a Delivery Surface abstraction, a scope-resolution model, and a capability/experience
visibility model already exist and are canonical or in-force, this document does **not** define a new
parameter schema, new API field names, or a new routing syntax. It directs that any future
implementation reconcile with the models above rather than re-deriving them, and that
[../patterns/ui-patterns.md](../patterns/ui-patterns.md) — already registered with disposition
**Revise** in [document-register.md](../governance/document-register.md) — is the correct eventual home
for a concrete rewrite, not this document.

## 10. Reusable parameterized views over scenario-specific screens

Direction only; no component names or implementation are authorized. A limited set of reusable
presentation primitives — landing/framework view, collection/list, subject overview, current-state
view, status/attention view, timeline/history, explanation view, evidence/document collection,
related-subject view — should replace a one-screen-per-question approach. This reconciles with
existing [ui-patterns.md](../patterns/ui-patterns.md) principles already in force: information
hierarchy (status → context → explanation → actions → history), progressive disclosure, and
cross-domain navigation that "must remain independent" and "not force hierarchy." No new principle is
created; the existing ones are reaffirmed as the basis for a framework-aligned rewrite.

## 11. Frontend as a renderer of governed meaning

This document reaffirms, and does not alter, the existing rule already stated in
[ui-patterns.md](../patterns/ui-patterns.md):

> "The UI is a projection of configuration and runtime state. The UI must not execute system logic
> directly, act as a source of truth, or store independent state."

The required flow is unchanged: BWF responsibility → governed model/contract/evidence → view model →
reusable UI component. A frontend component must not independently decide truth, identity sufficiency,
permission, asset health, obligation existence, causal explanation, or what belongs in meaningful
history — those determinations remain with the owning responsibility.

## 12. Conversation as navigation

Concierge's existing runtime concepts — interaction-space resolution, conversation ownership, modality
and channel routing, and scoped execution
([concierge-runtime-architecture.md](concierge-runtime-architecture.md)) — are reused as the mechanism
by which a resident's question resolves to scope and channel. This document adds the **direction**
that the same resolution may additionally select a BWF perspective and a reusable view (§9, §10); it
does **not** introduce a new routing concept, and it does not decide **OD-81** (#159) — whether HTBW
publishes its own capabilities as native Home Assistant services/events/entities/objects for household
automations to call. That is a distinct, open, native-Home-Assistant-publishing question, scoped
differently from Concierge's own conversational routing of its application UI, and is not resolved,
narrowed, or assumed by this document.

Acceptance examples (illustrative, not an exhaustive utterance grammar):

| Resident question | Perspective | Scope | View |
|---|---|---|---|
| "What assets are in this room?" | Truth | Current Room | Collection |
| "What has happened with the Steinway?" | Continuity | Asset subject | Timeline |
| "Why does the piano need attention?" | Stewardship | Asset subject | Attention/explanation |
| "Where is the painting now?" | Truth | Asset subject | Current-state |
| "Why did this light turn on?" | Explainability/Continuity (per existing architecture) | Resolved entity, Room | Explanation with evidence |
| "What happened in the Kitchen?" | Continuity | Room | Scoped timeline |

The frontend must not independently infer the answer to "why did this light turn on" — that answer
comes from the applicable HTBW/Home Assistant evidence architecture, unchanged by this document.

## 13. Multi-surface presentation

Reuses the existing Delivery Surface abstraction ([../models/communication.md](../models/communication.md))
rather than introducing new delivery-surface classes. The delivery surface controls presentation
density (desktop: broader detail and drill-down; kiosk: Room/context-appropriate subset; mobile:
compact summary; voice: concise explanation); it does not redefine semantic meaning, authority, or
evidence. The literal phrase **"Experience Family"** appears in the repository only as Family 1
(target-Room/vocabulary resolution) and Family 2 (Continuity/restoration), used in
[concierge-contract.md](../contracts/concierge-contract.md) and several scenario documents, plus one
unlabelled "Family 4" reference to Communication and Delivery authority in
[nighttime-suppression.md](../scenarios/nighttime-suppression.md). **No canonical, numbered catalogue
of four Experience Families exists today.** This document does not invent one, and any future reference
to "Family #3" or "Family #4" media/delivery architecture should first confirm the citation against
the owning document rather than assume a numbering scheme this review could not verify.

## 14. Deep navigation targets

Conceptual destinations (Continuity → Asset → environmental history; Stewardship → Asset → active
obligation; Truth → Room → assets; Continuity → Room → meaningful events) should remain referable by
Concierge, notifications, kiosks, and desktop views without separately authored screens per
destination. No public URL format or routing syntax is defined here; no current frontend/routing
architecture document was found that already owns one (§2), so this is named as an implementation-level
gap for a later, narrower document — not decided in this one.

## 15. Assist and commissioning access

HTBW configuration and management surfaces should preserve convenient access to Home Assistant's
existing Assist/Concierge interaction path, rather than an embedded parallel tester. The commissioning
principle — configure where you are working; test through the real household interaction path;
validate the household outcome — is documentation direction only. It does not design a new testing
engine, and where it touches Adoption-specific commissioning (detecting, offering, and validating an
Asset Intelligence Adoption), it explicitly defers to **OD-85** (§7).

## 16. Workbook, framework, and platform alignment

The direction — Behaves Well Framework (methodology) → Household & Space Outcomes Workbook (household
outcomes) → HTBW UI (governed operational configuration organized by the framework) → Home Assistant
(platform mechanics) → the lived Home (outcome) — is affirmed as the organizing principle for HTBW's
UX. It does not change any responsibility's ownership; it states that the same seven-responsibility
language used to teach the methodology should organize the software, consistent with
[north-star.md](north-star.md)'s statement that "the framework is the constitution."

## 17. Josh.ai observations — disposition

Applying the stated test (does Home Assistant already provide it; does HTBW already provide it; is the
lesson commissioning methodology rather than runtime architecture; is there a genuine uncovered HTBW
requirement) to each reviewed observation:

| Observation | Disposition |
|---|---|
| Room photographs | Reuse Home Assistant Area imagery; no new HTBW capability |
| Floors/Areas hierarchy | Reuse Home Assistant topology |
| Device type | Reuse Home Assistant semantics where sufficient |
| Nicknames/alternate Room names | Evaluate Home Assistant aliases plus HTBW Contextual Vocabulary ([../models/contextual-vocabulary.md](../models/contextual-vocabulary.md)); do not duplicate canonical names |
| Scenes | Native Home Assistant Assist behavior remains available where HTBW does not claim the intent, subject to existing routing architecture |
| Conversational testing | Reuse Assist; do not build a parallel tester (§15) |

Josh.ai is not documented as a design authority for HTBW; only the durable principles above, already
reconciled against existing architecture, are retained.

## 18. Primary application navigation — subject-first, Framework within

**This document's §5 "BWF as the primary HTBW navigation model" is clarified, not reversed, by this
section.** Reconciling both: the HTBW landing page may present the seven responsibilities as a
framework overview and explainer, per §5, as one legitimate entry point. **The persistent application
navigation that the resident and integrator use for ordinary commissioning work is subject-first**:

```
[HTBW branding]
Home
People
Places
Assets
Review & Readiness
──────────
Settings
Help / About
[path back to Home Assistant]
```

The conceptual model is **Subject → Framework responsibility → specific configuration** — for
example `People > Tom > Identity > Voice Enrollment`, `Places > Den > Foundation > Voice Input`,
`Assets > A.B. Chase Piano > Stewardship > Environmental Care`. **The Framework provides the
architectural organization within a selected subject; it is not itself the primary navigation rail.**
This does not reopen or contradict §5's framework-order rule (Foundation → Stewardship → Identity →
Truth → Continuity → Operational Trust → Concierge must still never be reordered) — it states that
*where* that order is applied is within a subject, not as the top-level navigation structure.

**People, Places, and Assets are the three dominant commissioning subjects**, already grounded in
existing object-type ownership (framework.md §1; [../models/asset.md](../models/asset.md);
[room.md](../models/room.md)): People ("who does the Home serve?"), Places ("where does the Home
understand and act?" — broader than traditional Rooms, consistent with the already-accepted Room/
Merged Room/Physical Room model, [room-configuration.md](../models/room-configuration.md)), and Assets
("what does the Home understand, protect, and care for?"). **Assets carry a dedicated top-level
navigation entry even though an Asset also appears naturally within its Place** — `Places > Music Room
> [Asset reference] > A.B. Chase Piano` and `Assets > A.B. Chase Piano` resolve to the **same**
Foundation-owned Asset record (§6), never a duplicate or divergent representation. A Framework
responsibility is presented for a subject only where accepted architecture actually establishes
configuration or information at that scope (§6's own asset-perspective table is the worked
precedent) — settings are never invented merely for visual symmetry across subjects.

## 19. Breadcrumbs, context preservation, and cross-Framework discoverability

Persistent breadcrumbs are a standard part of the HTBW experience, reusing and extending
[ui-patterns.md](../patterns/ui-patterns.md)'s existing breadcrumb rule ("always visible, reflect the
user's entry path, fully clickable, not force hierarchy") to the subject-first model above —
`People > Tom > Identity > Voice Enrollment`, `Assets > A.B. Chase Piano > Truth > Environmental
Conditions`. At any point the user can answer: what am I working on; where am I in the Framework; what
responsibility am I configuring; how do I reach related configuration without losing this context.
**Where practical, changing Framework responsibility preserves the selected subject** — matching
`ui-patterns.md`'s already-accepted "Back navigation must restore selected tab, filters, scroll
position."

**One configuration element has one architectural owner, but may have multiple contextual paths by
which it is discovered.** Framework rigor must never make settings hard to find: while working
`People > Tom > Identity`, the UI makes the applicable Operational Trust elements discoverable through
Framework navigation, contextual links, section summaries, or cross-references — reusing
`ui-patterns.md`'s existing, unchanged "Cross-Domain Navigation... must remain independent... do not
force hierarchy, preserve original context" rule. **Settings are never duplicated across Framework
responsibilities for convenience**; cross-Framework navigation takes the user to the authoritative
owner, preserving the subject wherever possible.

## 20. Framework as education

The UI teaches Framework responsibility through use, reusing §6's own existing asset-perspective table
as the general pattern and extending it to People:

| Responsibility | Question, for a Person | Question, for an Asset |
|---|---|---|
| Foundation | Who is this Person to the Home? | What is this Asset, and what are its durable relationships? |
| Identity | How does the Home know who this Person is? | — |
| Truth | What does the Home know to be true about this Person in current context? | What is currently true about this Asset, and what does current evidence mean for it? |
| Operational Trust | What is the Home allowed to do for or with this Person? | What Asset-related actions/access are allowed, where architecture establishes Asset-scoped trust |
| Stewardship | — (Person-scoped obligations are a future extension, not decided here) | What care and obligations apply to this Asset? |
| Continuity | What should the Home remember for this Person? | — |
| Concierge | How should the Home interact with this Person? | — |

Other responsibilities appear only where architecturally applicable — a Framework layer with no
established configuration at that scope is simply absent for that subject, never populated with
invented settings for symmetry.

### Sensors are evidence; Truth determines meaning; Stewardship determines consequence

**This is already canonical** (§6; [truth-contract.md](../contracts/truth-contract.md);
[stewardship-contract.md](../contracts/stewardship-contract.md)) and is restated here only as a UI
teaching example, not a new decision. For the A.B. Chase Piano: Foundation identifies the Asset, its
type, manufacturer/model/serial, owner (a durable relationship), its Home/assigned Place, associated
Home Assistant entities/devices, and its documents; Truth evaluates environmental evidence against
Foundation's declared acceptable ranges and reports current condition, current location, current
custody, and current disposition/status; Stewardship answers what should happen as a result — care
obligations, maintenance, caretaker responsibility, escalation. A sensor reporting `44%` humidity is
evidence; Truth's contextual judgment ("44% is within the configured acceptable range for the piano")
is what the UI presents as currently true. **A Place may legitimately carry a different environmental
interpretation than an Asset within it** — the Music Room may be comfortable for residents while
approaching the piano's own narrower acceptable range — because Truth evaluates each Subject against
its own Foundation-declared criteria, never a single room-wide verdict silently applied to everything
inside it.

### Asset ownership, location, and custody — durable versus current

**Already established by §6 and `asset.md`'s existing responsibility split; restated here as a worked
example only.** Foundation owns durable relationships — owner, assigned/Home Place, durable Asset
identity relationships. Truth owns current state — current location, current custody, current
disposition/status. A temporary relocation never rewrites the Asset's durable Foundation-owned Home
Place:

```
Foundation (durable):  Owner: Tom.  Home Place: Music Room.
Truth (current):       Current Location: Museum.  Current Custodian: Museum.  Status: On Loan.
```

The UI presents both without conflating them: the Asset's home remains the Music Room even while
Truth reports it is presently on loan elsewhere. Stewardship may separately govern obligations
associated with the loan once/where that is architecturally established — not decided or assumed
here.

### Documents and images

Asset documents/images are information associated with the one authoritative Foundation-owned Asset
record (§6; `connected-storage.md`'s "Asset documents" artifact class) — presented at `Assets >
[Asset] > Foundation > Documents & Images`. Other Framework responsibilities may **reference** these
documents (Stewardship citing a service record when defining care; Operational Trust governing access
where document-level authorization is established) without ever duplicating them. **One document
remains one authoritative managed object**, never copied because multiple responsibilities use it —
directly reusing the already-accepted Governed Reference discipline (**DL-104**).

## 21. External Storage Contract

**`connected-storage.md` is the canonical External Storage Contract** — already covering, per its own
"Accepted artifact retention strategies" table and its "Governed namespace" section, every currently
established externally-persisted HTBW class (Asset documents, voice enrollment samples, voiceprints,
extended historical records, Evidence Package, Historical Reconstruction, and the Materialized
Household Assessment, **DL-105**). This document does not duplicate that contract; it directs that
future HTBW UI work consume it rather than inventing storage behavior independently.

**Principle: "Users select storage. HTBW selects paths."** The household selects the connected storage
resource through native Home Assistant mechanisms; HTBW owns taxonomy, naming, paths, and lifecycle
beneath that selection. The Storage settings UI (§22) must discover configured storage through
supported Home Assistant capabilities and present friendly, Home Assistant/household-recognizable
names — never require a resident to type a path.

**Asset Intelligence / Adoption file-structure continuity is now verified, not assumed.** The
standalone Asset Intelligence product's own `document_storage.py` was inspected directly: it already
keys every document folder by the Asset's stable `asset_id`, keys every file by its own opaque,
freshly generated identifier, and its own access layer "intentionally does NOT expose raw filesystem
paths." This already matches `connected-storage.md`'s governed-namespace rule (stable identifier,
never a display-name key, never an exposed raw path) — independently, not because HTBW requires it of
the standalone product. **HTBW's own Asset-anchored storage must replicate this same keying
principle** for Assets created natively in HTBW and for Assets carried in through Adoption alike, so
that **Adoption of existing Asset Intelligence documents/images is a reference-based act** — HTBW
takes governed ownership of files already present at their existing location using the Asset's own
stable identifier, without requiring re-upload or physical relocation, directly satisfying Adoption's
accepted "one-time, authoritative, no synchronization, no write-back" rule (**DL-52**). The
household-visible taxonomy ("Asset Intelligence > A.B. Chase Piano > Documents & Images") remains a
presentation label only; renaming the Asset never touches the physical structure and never orphans a
document, because resolution was never based on the display name in either product.

## 22. HTBW Settings

**"One configuration value, one authoritative source, multiple appropriate entry points."** Once HTBW
exists, HTBW-specific configuration is reachable through the HTBW application UI without leaving the
commissioning environment, reusing — never duplicating — `ui-patterns.md`'s existing System Boundary
distinction between **Global Configuration** (archive/storage destination wiring, provider/integration
credentials, authentication) and the main operational UI. Candidate Settings categories, derived from
already-established dependencies rather than invented, include **Storage** (§21), **Capabilities &
Providers** (reasoning providers, communication capabilities — each already a declared **DL-41**
dependency), **Identity Services** where applicable, **Privacy & Data** where applicable, **Diagnostics**,
and **About HTBW**. No category is added beyond what already-accepted architecture establishes a
configuration surface for. Settings must not reimplement Home Assistant administration: where an
underlying resource is Home-Assistant-owned, HTBW explains the relationship and links to the native HA
administration experience rather than recreating it (§8).

## 23. Native First, Native Extended; Home Assistant UI conformance

**Governing principle, reusing and extending `ui-patterns.md`'s existing "feel native to Home
Assistant" rule**: before any HTBW UI element is designed, the current Home Assistant-native
component, selector, form pattern, dialog, or established frontend pattern that could satisfy the
requirement is identified and used first. Where extension is required, the HTBW-specific requirement
driving it is documented; a wholly custom control is created only where no native pattern can be
reasonably extended, and even then follows Home Assistant's design conventions, theming, accessibility
conventions, and interaction patterns. **Detailed conformance criteria — the escalation order (use →
configure/constrain → compose → extend → create custom), concrete native selector/control categories,
and the UI Architecture Acceptance Gate — are added to [ui-patterns.md](../patterns/ui-patterns.md)
(§24 cross-reference), which already owns concrete UI pattern detail; this document states the
governing principle only.**

## 24. Brand, visual system, and Framework iconography

**Genuinely new requirement — not yet satisfied by any existing repository artifact.** No canonical
Framework iconography (one icon per responsibility: Foundation, Identity, Truth, Operational Trust,
Stewardship, Continuity, Concierge) and no documented HTBW semantic-icon system were found anywhere in
this repository. This is recorded as a **follow-on requirement** (§26, item H), not invented here —
producing the actual iconography is a design deliverable, not an architecture decision, and is out of
scope for this document. The governing principles, reusing `ui-patterns.md`'s existing Iconography
section (which already separates "Layer 1: Native" entity/sensor icons from "Layer 2: System"
signal/context/interaction icons) and extending it with a third, explicitly Framework-branded layer:

- **"Brand the concepts. Keep platform interactions native."** Framework iconography is reserved for
  the seven responsibility concepts and genuinely HTBW-specific semantics; standard Home Assistant
  interaction icons (edit, delete, settings, expand, navigation, device/entity concepts) are never
  redesigned for branding.
- **Color is punctuation, not the primary information model.** The seven Framework layers are not
  rendered as seven loud colors; `ui-patterns.md`'s existing status-color semantics (§25 cross-
  reference: context/normal/warning/critical/unknown) are a **different dimension** from any Framework-
  layer signature treatment and must not be confused with it.
- **Home Assistant theming is respected, never replaced** by an independent HTBW light/dark theme;
  official HTBW visual assets must work across supported HA themes.
- Intended reuse beyond HTBW itself (BehavesWell website, Framework diagrams, workbooks, education
  materials) is a brand-system property, not an architecture decision, and is not designed here.

## 25. Household-aware language, progressive disclosure, and state-aware help

**"Discover before asking. Explain before requiring. Show consequences before accepting."** HTBW never
asks the household to manually supply information it can reliably discover through supported Home
Assistant mechanisms. Household-facing language uses household terms ("Tom," "the Den," "A.B. Chase
Piano") rather than low-level identifiers — but **canonical HTBW architectural vocabulary and governed
architectural meaning are never personalized by household terminology**; help may personalize wording,
never meaning. This extends, without altering, the already-accepted Contextual Vocabulary boundary
([../models/contextual-vocabulary.md](../models/contextual-vocabulary.md)): household vocabulary
governs what residents may *say*, never what the architecture *means*.

Progressive disclosure — reusing `ui-patterns.md`'s existing, unchanged rule ("show high-level state
first, allow drill-down, never overwhelm") — begins with the household decision and exposes
implementation detail only when needed; a homeowner is never forced to understand platform
terminology to commission the Home, while an integrator can still reach deeper technical diagnostics
through the same progressively-disclosed path, never a separate application.

Help should be state-aware where appropriate (reflecting current configuration — for example, Identity
help explaining that detecting a BLE device alone does not establish that the device represents a
Person, per **DL-33**/**DL-38**, already accepted) and should answer, where accepted architecture
supports the answer: why am I seeing this; why can't I select this; where did this value come from
(**configuration provenance** — defined by household/HTBW, discovered from Home Assistant, derived by
HTBW, or supplied by a configured provider); what changes if I change this; what uses this setting.

## 26. Readiness, health, and dependency states

**Readiness** ("is this correctly commissioned?") and **Health** ("is this currently operating
correctly?") are distinct and never conflated — a correctly commissioned Voice endpoint may be
temporarily unavailable without that implying improper commissioning, directly reusing the existing
**DL-41** dependency-availability model (not configured / configured but invalid / configured but
unavailable / healthy / degraded-but-usable / removed are already distinguishable states). **No
arbitrary completion percentage is presented** absent a future governed mathematical definition for
one; meaningful states such as Ready, Needs Attention, Unavailable Dependency, Not Configured, and
Degraded are used instead. A Home can be intentionally and correctly commissioned without enabling
every optional HTBW capability — this is never presented as an error. Where architecture distinguishes
**Required** (HTBW cannot operate without it) from **Capability Requirement** (a specific capability
depends on it, per **DL-41**'s own mandatory/optional dependency distinction) from **Enhancement**
(the capability remains available; configuring this improves it), the UI presents that distinction
rather than a flat Required/Optional binary.

## 27. Required documentation outcome — cross-reference

| Required outcome item | Addressed in |
|---|---|
| 1. BWF as primary HTBW mental/navigation model | §5, §18 |
| 2. HA technical configuration vs. HTBW operational configuration | §8, §22 |
| 3. Asset Intelligence migration/Adoption | §4, §7, §21 |
| 4. One asset record, several perspectives | §6, §18, §20 |
| 5. Foundation/Truth/Stewardship/Continuity asset responsibilities | §6, §20 |
| 6. Continuity vs. raw telemetry | §6 |
| 7. Subject + Perspective + Scope + Filter + Surface | §9 |
| 8. Reusable parameterized views | §10 |
| 9. Frontend as renderer, not business-logic engine | §11 |
| 10. Conversation as navigation | §12 |
| 11. Cross-surface presentation | §13 |
| 12. Primary navigation (People/Places/Assets); breadcrumbs; cross-Framework discoverability | §18, §19 |
| 13. Framework as education; ownership/location/custody; documents | §20 |
| 14. External Storage Contract | §21 |
| 15. HTBW Settings | §22 |
| 16. Native First, Native Extended | §23 |
| 17. Brand, visual system, Framework iconography | §24 |
| 18. Household-aware language, progressive disclosure, state-aware help | §25 |
| 19. Readiness, health, dependency states, no arbitrary percentages | §26 |

## 28. Governing summary principles

> "HTBW should be as thoughtful to configure as the Home is thoughtful to live in."
> "Discover before asking. Explain before requiring. Show consequences before accepting."
> "Native First. Native Extended."
> "Brand the concepts. Keep platform interactions native."
> "One configuration value, one authoritative source, multiple appropriate entry points."
> "One configuration element has one architectural owner, but may have multiple contextual paths by
> which it can be discovered."
> "Users select storage. HTBW selects paths."
> "Sensors provide evidence. Truth determines what that evidence means in context."
> "The subject remains stable while the Framework changes around it."
> "People, Places, and Assets describe the Home. The Framework describes HTBW's responsibilities
> toward them."

The goal is not an independent high-end web application running inside Home Assistant. The goal is an
exceptionally thoughtful, premium, first-class Home Assistant integration whose commissioning
experience demonstrates the same calm, contextual, explainable, household-centered behavior HTBW is
intended to create in the Home.

## 29. Non-actions

This document does not: modify runtime code; implement Adoption; remove or deprecate the standalone
Asset Intelligence product or integration from any installation; close **OD-85**, **OD-81**, **OD-20**,
or any other open decision; allocate a new Decision Ledger entry; authorize any UI build; or design the
Framework iconography/brand-asset deliverable itself (§24, flagged as follow-on work). Concrete UI
pattern detail (native-component conformance order, accessibility, responsive design, motion,
configuration defaults/validation classification, destructive-action confirmation, search/filtering at
scale, and the formal UI Architecture Acceptance Gate) is added to
[ui-patterns.md](../patterns/ui-patterns.md), which already owns that level of detail — not duplicated
here. Register entry: [document-register.md](../governance/document-register.md).

