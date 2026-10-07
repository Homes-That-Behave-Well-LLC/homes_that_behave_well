# Canonical Stewardship Use Cases

> **Document status: Canonical scenario.**
> Terminology: [../models/glossary.md](../models/glossary.md).
> Index: [README.md](README.md). Owning responsibility: **Stewardship**.
> Model: [../models/stewardship.md](../models/stewardship.md).
> Contract: [../contracts/stewardship-contract.md](../contracts/stewardship-contract.md).
> Companion scenario: [stewardship-obligations.md](stewardship-obligations.md).

---

## Purpose

[stewardship-obligations.md](stewardship-obligations.md) proves the **separation** — obligation versus
action, intent versus escalation, `unknown` versus `met`. This document proves the **lifecycle**: how
a household declaration becomes a care definition, how a care definition becomes an obligation, who
evaluates it, who performs anything, and how it closes.

These eight use cases arose as **architecture stress tests** during narrative development of *Season 1
Episode 6 — Stewardship: How Does a Home Know What Matters?* They are recorded here as canonical
Stewardship use cases and as **future acceptance scenarios**.

**The narrative is not architecture.** It was used to find questions the accepted architecture must
answer. Where it proposed something the accepted architecture does not support, the accepted
architecture prevailed and the narration is remediated. See
[../governance/decision-ledger.md](../governance/decision-ledger.md).

---

## The doctrine these use cases enforce

> **The household declares what matters. Stewardship represents that declaration as care
> expectations, evaluates authoritative observations against them, and creates governed care
> obligations when attention is required.**

Stated in the form the household hears:

> **The household determines what matters. Stewardship helps care for it.**

Behind that summary, precisely:

| Statement | Owner |
|---|---|
| *This matters to us, and here is what caring for it means* | **The household** |
| *That care expectation is represented, evaluated, and its obligation state maintained* | **Stewardship** |
| *What is actually true right now* | **Truth** |
| *Whether the proposed response is appropriate for this request, in this context* | **Operational Trust** |
| *What should happen now* | **Concierge** |
| *The action itself* | An **executor** — a Home Assistant automation, script, scene, service call, integration, or a person |

**Stewardship never decides that something matters on the household's behalf, and Stewardship never
performs the action.**

---

## Status legend

HTBW Core is **greenfield** ([../architecture/greenfield-mandate.md](../architecture/greenfield-mandate.md),
**DL-19**). Nothing in this document asserts an implemented HTBW Core capability.

| Code | Meaning |
|---|---|
| **A** | **Accepted architecture** — stated in a canonical HTBW document |
| **E** | **Architectural expectation** — follows from accepted architecture, not yet written into a canonical model or contract |
| **U** | **Unresolved decision** — held by a named open decision (OD) |
| **F** | **Future implementation requirement** — no HTBW Core implementation exists |
| **P** | **Partially present in a separate released product** — Asset Intelligence, Voice Identity, or Concierge. **This is not HTBW Core capability** and creates no compatibility requirement (**DL-19**) |

---

## The household used throughout

The household of [README.md](README.md), extended only where a use case requires it:

```
Home
├── Living Space            (Merged Room: Kitchen + Dining + Living)
├── Den
├── Office
├── Primary Bedroom
├── Music Room
├── Laundry                 (added for Use Case 4)
└── Garage

People:  Tom, David, Eleanor (David's mother, lives with the household — Use Case 3)
Pets:    Maisey
Assets:  Sonos speakers, Sonos Beam, LG television, Apple TV,
         7 shades (Kitchen 1, Dining 3, Living 3),
         1918 A.B. Chase 6' Grand Piano,
         a signed watercolour in the Den (Use Case 1),
         HVAC equipment (Use Case 6),
         washing machine (Use Case 4),
         irrigation controller and four zones (Use Case 7)
```

---

## How to read a use case

Each use case is presented as:

1. **Human purpose** — why a household would want this
2. **Household declaration** — the sentence the household is actually saying
3. **Subjects of care** — what is being cared for, and what kind of object it is
4. **Required setup** — the definition activities, with owner and status
5. **Ownership map** — the eighteen handoffs, each with exactly one owner
6. **Reference scenarios** — the walkthroughs, attributed step by step
7. **Acceptance scenarios** — what a conforming implementation must and must not do
8. **Known implementation gaps** — what is genuinely unresolved

**Every ownership map answers the same eighteen questions**, so the use cases can be compared without
re-reading them.

---

# Use Case 1 — Artwork Preservation

## Human purpose

The household owns a signed watercolour that is meaningful, financially valuable, and part of the
household's story. They want it to survive the way they keep their home.

## Household declaration

> "This watercolour matters. Help us care for it."

Expressed architecturally: the household **registers the Asset**, **declares its significance**, and
**declares its care expectations** — preservation limits, a cleaning cadence, a conservator, and who
is accountable.

## Subjects of care

| Subject | Object type | Owner of the object |
|---|---|---|
| The watercolour | **Asset** | Foundation asset model ([../models/asset.md](../models/asset.md)) |
| The Den | **Room** | Foundation / Room Configuration |

## Required setup

| Definition activity | Architectural owner | Source of truth | Persistence owner | Native HA representation | Status |
|---|---|---|---|---|---|
| Asset registration and authoritative identity | Foundation asset model | HTBW | Foundation | A native Device **may** be created for a non-device Asset (**DL-31**) | **A** |
| Description, acquisition and purchase information, provenance | Foundation asset model | HTBW | Foundation | None | **A** |
| Ownership and owner-of relationship | Foundation asset model | HTBW | Foundation | None | **A** |
| Custodian / conservator as a **Service** relationship | Foundation asset model | HTBW | Foundation | None | **A** |
| **Caretaker assignment** | **Stewardship** (recorded through the Foundation `caretaker-of` relationship type) | HTBW | Stewardship | None | **A** |
| Declared location and room placement | Foundation asset model, `located-in` | HTBW | Foundation | Area assignment where a native Device exists | **A** |
| **Where it is now** | **Truth**, as a Location Fact | Truth | Truth | Entity state where device-backed | **A** |
| Bills of sale, insurance rider, photographs, attached documentation | Foundation asset model, anchored in **Connected Storage** | HTBW | Foundation (the Asset is the governing parent, **DL-45**) | None. Sensitive artifacts are **not** exposed as resident media (**DL-44**) | **A** |
| Temperature, humidity, and light/UV limits **as properties of the thing** | Foundation asset model | HTBW | Foundation | None | **A** |
| **Significance declaration** — that it matters, and how much | **Stewardship**, recorded with **provenance** naming the household as the declarer | HTBW | Stewardship | None | **A** — representation is **DL-75** |
| Cleaning and conservation schedule | **Stewardship** | HTBW | Stewardship | Calendar projection is **OD-23** | **A / U** |
| Maintenance and conservation history | **Stewardship**, as Change Records (**DL-26**) | HTBW | Stewardship | Not Recorder. HTBW builds no second Recorder (**DL-42**) | **A** |
| Relevant room sensors, windows, window direction, sun exposure | Room Configuration participation set | Foundation | Foundation | Area, Entity, and Sun integration references (**DL-31**) | **A** |
| Escalation intent and accountability | **Stewardship** (the single ladder) | HTBW | Stewardship | None | **A** — semantics are **OD-22** |
| Reminder destination | **Not a Stewardship setting.** Delivery surface is Concierge; entitlement is Operational Trust (**DL-28**, **DL-29**) | — | — | — | **A** |
| Condition observations recorded by a person | **Stewardship** care record | HTBW | Stewardship | None | **E** |
| Loan / check-out / check-in state | **Stewardship** — a **Custody Period** (**DL-49**) | HTBW | Stewardship | None | **A** |

## Ownership map

| # | Question | Owner | Statement |
|---|---|---|---|
| 1 | Authoritative Truth inputs | **Truth** | Den temperature, relative humidity, illuminance, and sun elevation/azimuth — each with confidence, provenance, freshness, and validity |
| 2 | Identity requirements | **Identity** | **None for the assessment.** Identity is required only where a *person-directed* Communication or a person-scoped capability is involved |
| 3 | Consent or authority requirements | **Operational Trust** / household | Household declaration of significance and care. No personal consent is engaged by an Asset |
| 4 | Operational Trust evaluation | **Operational Trust** | Whether dehumidification may run autonomously; whether the caretaker Communication may be delivered, on which surface, before which audience (**DL-29**, **DL-34**) |
| 5 | Stewardship assessment | **Stewardship** | Compares the Truth Facts with the declared preservation limits and sets obligation state |
| 6 | Obligation or advisory | **Stewardship** | A **preservation obligation** (`met` / `due` / `unmet` / `overdue` / `waived` / `unknown`) or an **Advisory** where something could be improved but nothing is wrong |
| 7 | Notification path | **Stewardship originates; Concierge delivers** | Stewardship may originate a Communication. It never selects surface, moment, wording, or whether delivery happens |
| 8 | Corrective-action path | **Obligation → Operational Trust → executor** | Stewardship states the obligation is unmet. It does not start the dehumidifier |
| 9 | Execution owner | **Concierge decides; an executor performs** | A Home Assistant automation, script, or service call, or a person |
| 10 | Explainability | **Decision Trace** (**DL-15**, **DL-46**) | Which Fact, which declared limit, whose declaration, which policy, which executor, and the observed outcome — **by reference, never by copy** (**DL-27**) |
| 11 | Continuity interaction | **None** | Preservation care is not a preference, a session, or a resumable experience |
| 12 | Retention | **Per record class** (**DL-47**) | Documents live while the Asset lives (**DL-43**); Change Records follow the Asset lifecycle; the Decision Trace follows External History Retention |
| 13 | Closure criteria | **Stewardship** | The obligation returns to `met` **only when Truth reports the condition inside limits**, or when completed care is recorded. **A completed list item is not proof of care** |
| 14 | Failure / uncertainty | **Stewardship** | A failed humidity sensor makes the obligation `unknown`, never `met`. Absence of evidence is never compliance |
| 15 | HA native capabilities | Home Assistant | Area, Device, Entity, Sun, Recorder history, `todo`/Calendar as **projection** surfaces (**OD-23**), Repairs for configuration defects only (**DL-65**) |
| 16 | What must never happen | — | Stewardship must not publish, cache, or re-derive the environmental readings. **Truth owns them** (**DL-25**) |
| 17 | Household hierarchy | — | **No universal HTBW importance ranking exists.** Another household may declare the same object insignificant, and the framework is unchanged |
| 18 | Sensitivity | — | **Sensitivity is never inferred.** Value, insurability, and irreplaceability are household declarations recorded with provenance |

## Reference scenarios

### A — Conditions remain acceptable

| Step | Responsibility | Statement |
|---|---|---|
| 1 | **Truth** | The Den is at 47% relative humidity, Truth Confidence Band: High |
| 2 | **Stewardship** | The watercolour's preservation obligation is `met` |
| 3 | **Concierge** | Nothing happens, and the non-event is not announced |

**No obligation is created. Silence is the correct behaviour, and it is still explainable on request.**

### B — Humidity exceeds the accepted range

| Step | Responsibility | Statement |
|---|---|---|
| 1 | **Foundation asset model** | The watercolour requires 40–55% relative humidity — a declared property of the thing |
| 2 | **Truth** | The Den is at 68% relative humidity, Truth Confidence Band: High |
| 3 | **Stewardship** | The preservation obligation is `unmet`; significance is high — irreplaceable, household-declared |
| 4 | **Operational Trust** | Running the dehumidifier is permitted autonomously; the caretaker Communication is permitted on a personal surface |
| 5 | **Concierge** | Start dehumidification, convey to the caretaker, and explain |
| 6 | **Executor** | The Home Assistant automation switches the dehumidifier on |
| 7 | **Truth** | The Den returns to 52% |
| 8 | **Stewardship** | The obligation returns to `met`, and the transition is recorded |

> **The obligation existed before anything happened, and it still exists afterwards.** The automation
> changed the world; it did not change who owned the care responsibility.

### C — Periodic cleaning becomes due

| Step | Responsibility | Statement |
|---|---|---|
| 1 | **Stewardship** | The conservation-cleaning obligation is `due`; accountability is David |
| 2 | **Operational Trust** | The Communication is permitted; audience composition allows a shared surface |
| 3 | **Concierge** | Conveys it, and — where the household has chosen a projection (**OD-23**) — surfaces it on a `todo` list or calendar |
| 4 | **David** | Books the conservator and records the completed care |
| 5 | **Stewardship** | Records the conservation history and closes the obligation |

**The `todo` item is a projection. Ticking it is a list state, not evidence that the watercolour was
cleaned.**

### D — The artwork is loaned

| Step | Responsibility | Statement |
|---|---|---|
| 1 | **Foundation asset model** | The declared `located-in` relationship changes |
| 2 | **Truth** | The Location Fact for the Asset changes, or becomes `unknown` where no evidence exists |
| 3 | **Stewardship** | Environmental preservation obligations that depended on Den Facts become **`unknown`, not `met`** |
| 4 | **Stewardship** | Custody, return, and condition-check obligations are the **unresolved** part of this scenario — see gaps |

## Acceptance scenarios

| # | Given | Then | Must not |
|---|---|---|---|
| 1.1 | Conditions inside declared limits | Obligation `met`; no Communication originated | Announce a non-event |
| 1.2 | Humidity outside declared limits | Exactly one obligation `unmet`, carrying significance with **household provenance** | Stewardship calling a Home Assistant service |
| 1.3 | An authorised automation corrects the condition | The Decision Trace names the **executor** and the **authority**, and the obligation is re-evaluated from Truth | Report closure from the action rather than from the observed outcome |
| 1.4 | The humidity sensor is unavailable | Obligation `unknown`; the household is told the check is unverified | Retain the last reading as current, or report `met` |
| 1.5 | The household never declared the watercolour significant | No preservation obligation exists | Infer significance from price, appraisal, or asset type |
| 1.6 | A cleaning `todo` projection is ticked | The list state changes | Treat completion as proof that care occurred |
| 1.7 | Any explanation is requested | The Decision Trace resolves Fact, limit, declarer, policy, executor, and outcome **by reference** | Embed copies of the source records (**DL-27**) |

## Known implementation gaps

| Gap | Classification |
|---|---|
| **Loan, check-out, check-in, and custody transfer are resolved as DL-49.** A **Custody Period** is a time-bounded accountability record owned by **Stewardship**; `located-in` remains a declared relationship and is **not** a custody chain. **Physical return is evidence toward closure, never closure** — the period closes only on a recorded Check-In | **Resolved — DL-49** |
| Significance representation — band, score, or household vocabulary | **Resolved — DL-75** |
| Whether obligations project into calendars, `todo` entities, or connected storage | **OD-23** |
| Which Asset-derived values are published as Entities, and with which state vocabulary. **HTBW defines no "asset health" state model** | **OD-69** |
| Sun-exposure context as an input: no native Room-level or Area-level UV or direct-illumination capability has been verified, so the **DL-30** burden of proof is not discharged | **U / F** |

---

# Use Case 2 — Pet Stewardship

## Human purpose

The household considers Maisey part of the family and wants ongoing support for her care.

## Household declaration

> "Maisey matters. Help us care for her."

## Subjects of care

| Subject | Object type | Owner of the object |
|---|---|---|
| Maisey | **Pet** — *a non-human household member, and not a Person* | Foundation |

> **A Pet is not an Asset, and a Pet is not a Person.** The glossary and the asset model both keep it
> a distinct object type. **No document in this repository models a household animal as equipment, and
> none may.**

## Required setup

| Definition activity | Architectural owner | Source of truth | Persistence owner | Native HA representation | Status |
|---|---|---|---|---|---|
| Pet record and identity | Foundation | HTBW | Foundation | None verified | **A** |
| Associated wearable or tag, as an **evidence-source reference** | Foundation | HTBW | Foundation | Device Tracker / Device where one exists | **A** |
| Veterinarian as a **Service** relationship | Foundation | HTBW | Foundation | None | **A** |
| Caretaker assignment | **Stewardship** | HTBW | Stewardship | None | **A** |
| Medication schedule, feeding and walk routines, care schedule | **Stewardship** obligations | HTBW | Stewardship | Calendar/`todo` projection is **OD-23** | **A / U** |
| Veterinary appointments | **Stewardship** schedule obligation | HTBW | Stewardship | Calendar projection is **OD-23** | **A / U** |
| **Where Maisey is now** | **Truth**, as a Location Fact with Subject *Pet* | Truth | Truth | Device Tracker state | **A** |
| Activity observations | **Truth** | Truth | Truth | Entity state, Recorder history | **A** |
| Escalation path | **Stewardship** ladder + **Operational Trust** authority + **Concierge** execution | — | Stewardship | None | **A** — semantics are **OD-22** |
| Notification recipients | **Not a Stewardship setting** — audience specification is **OD-52** | — | — | — | **U** |
| Care records and history | **Stewardship** history | HTBW | Stewardship | Not Recorder | **A** |

## Ownership map

| # | Question | Owner | Statement |
|---|---|---|---|
| 1 | Authoritative Truth inputs | **Truth** | Pet Location Fact, activity Facts, and Person-presence Facts for the caretaker |
| 2 | Identity requirements | **Identity** | **None for the Pet.** *"Where is Maisey?"* is a **Truth-only** question and must **not** be routed through Identity. Identity applies only to the *human* recipient of a Communication |
| 3 | Consent or authority | Household | The household declares the care. **No consent object attaches to a Pet**; consent attaches to the humans whose data or surfaces are involved |
| 4 | Operational Trust evaluation | **Operational Trust** | Whether the reminder may be delivered, to whom, on which surface, before which audience |
| 5 | Stewardship assessment | **Stewardship** | Whether each declared care obligation is `met`, `due`, `unmet`, `overdue`, `waived`, or `unknown` |
| 6 | Obligation or advisory | **Stewardship** | Health-significance care obligations |
| 7 | Notification path | Stewardship originates; Concierge delivers | — |
| 8 | Corrective-action path | Human care, in almost every case | A medication obligation is discharged by a person, not by an executor |
| 9 | Execution owner | **Concierge** decides; a **person** performs | — |
| 10 | Explainability | Decision Trace | Which schedule, which declaration, who was accountable, why it escalated |
| 11 | Continuity interaction | **None** | Care history is **Stewardship history**, not Continuity. Continuity is not a child of Stewardship |
| 12 | Retention | **DL-47** | Care and obligation history follow the governed-record model; wearable Facts follow Truth's Historical Fact retention |
| 13 | Closure criteria | **Stewardship** | Recorded administration, recorded feeding, a completed appointment. **The evidence accepted as completion is unresolved** — see gaps |
| 14 | Failure / uncertainty | **Truth**, then **Stewardship** | An absent tag signal is `unknown` location, never *"Maisey is gone"* and never *"Maisey is home"* |
| 15 | HA native capabilities | Home Assistant | Device Tracker, Calendar, `todo`, Recorder, Person state for the caretaker |
| 16 | What must never happen | — | **No medical diagnosis, and no health inference.** A wearable observation is evaluated **only** against explicitly configured care requirements |
| 17 | Tag versus wearer | **Truth** | A tag establishes where the **tag** is. That the tag is on Maisey is a **declared association**, and it can be wrong |
| 18 | Disclosure | **Operational Trust** | A pet-location answer can disclose a **person's** movements. It is audience-evaluated like any other disclosure (**DL-34**) |

## Reference scenarios

### A — A veterinary appointment approaches

| Step | Responsibility | Statement |
|---|---|---|
| 1 | **Stewardship** | The veterinary schedule obligation becomes `due`; accountability is Tom |
| 2 | **Operational Trust** | The Communication is permitted; a shared surface is appropriate |
| 3 | **Concierge** | Conveys it, and projects it to the household calendar where the household has chosen that projection (**OD-23**) |

### B — Medication becomes due

The path of [stewardship-obligations.md](stewardship-obligations.md) Scenario 5 exactly:
Stewardship states the obligation and supplies **escalation intent**; Operational Trust permits
escalation to another adult; **Concierge performs the escalation**.

> **Stewardship supplied the escalation intent. Concierge performed the escalation. Stewardship does
> not send notifications.**

### C — The wearable reports an observation

| Step | Responsibility | Statement |
|---|---|---|
| 1 | **Truth** | Publishes the available Fact — activity level, with confidence, provenance, and freshness |
| 2 | **Stewardship** | Evaluates it **only** against an explicitly configured care requirement, if one exists |
| 3 | **Stewardship** | Where no configured requirement exists, **nothing is produced.** No pattern is interpreted |

**No diagnosis. No health inference. No unrequested interpretation of an animal's body.**

### D — Location becomes uncertain

| Step | Responsibility | Statement |
|---|---|---|
| 1 | **Truth** | The tag has not reported inside its freshness window. The Location Fact is `unknown`, not the last known Room |
| 2 | **Stewardship** | Any care obligation depending on that Fact is `unknown`, never `met` |
| 3 | **Concierge** | Says what is actually known: *"The last place I saw her tag was the Den, forty minutes ago. I can't tell you where she is now."* |

## Acceptance scenarios

| # | Given | Then | Must not |
|---|---|---|---|
| 2.1 | A pet-location question | Answered from **Truth alone** | Route a Pet through Identity, or assign a **DL-39** confidence band to a Pet |
| 2.2 | A stale tag reading | `unknown` | Present the last known Room as current |
| 2.3 | A wearable observation with no configured care rule | No obligation, no advisory, no comment | Infer illness, distress, or a health trend |
| 2.4 | A medication obligation missed by the accountable person | Escalation **intent** from Stewardship; escalation **performed** by Concierge under Operational Trust authority | Stewardship delivering the escalation |
| 2.5 | A guest asks where Maisey is | Evaluated as a disclosure against audience composition | Answer because the requestor was authorised |
| 2.6 | Any pet care record | Held as **Stewardship** history | Store it in Continuity, or treat Continuity as a child of Stewardship |
| 2.7 | Anywhere in the model | The Pet remains a distinct object type | Represent the Pet as an Asset or as an equipment record |

## Known implementation gaps

| Gap | Classification |
|---|---|
| **What constitutes accepted evidence that care occurred** (medication given, fed, walked) | **REMEDIATION REQUIRED — OD-75** |
| No dedicated pet model document exists; the Pet is defined in the glossary, the asset model's object table, and [where-is-maisey.md](where-is-maisey.md) | **E** — sufficient today, and worth consolidating |
| Notification recipient specification | **OD-52** |
| Escalation ladder semantics and defaults | **OD-22** |

---

# Use Case 3 — Aging-Parent Support

## Human purpose

Eleanor lives with the household. They want to support her while respecting her independence,
consent, privacy, and dignity.

## Household declaration

> "Eleanor matters, and she has asked for help with some things."

**This declaration is materially different from the other seven**, because the subject of care can
speak for herself.

> **People are not Assets.** No document in this repository models a person as property, and none may.
> A Person may carry a Stewardship care obligation without becoming an Asset, an inventory item, or a
> tracked object. **Eleanor is a Person with declared care expectations, not a possession being
> maintained.**

## Subjects of care

| Subject | Object type | Owner of the object |
|---|---|---|
| Eleanor | **Person** | Foundation |
| The rooms she uses | **Room** | Foundation / Room Configuration |

## Required setup

| Definition activity | Architectural owner | Source of truth | Persistence owner | Consent | Status |
|---|---|---|---|---|---|
| Person record and roles | Foundation | HTBW | Foundation | — | **A** |
| Identity participation and enrolment | **Identity** | HTBW | Identity | **Required.** Participation is optional and consent-gated | **A** |
| Associated wearables as evidence-source references | Foundation; reliability per **Person-and-source** association (**DL-32**) | HTBW | Foundation / Identity | Required | **A** |
| Medication schedule | **Stewardship** obligation | HTBW | Stewardship | Required — see gaps | **A / U** |
| Physician appointments | **Stewardship** schedule obligation | HTBW | Stewardship | Required | **A / U** |
| Accessibility and environmental support requirements | **Resolved as DL-61.** Person Environmental Requirements, reusing the Asset environmental-limit pattern, held by Foundation through Person Setup, evaluated by Stewardship against current Room Environment Facts (**DL-60**) while a valid Contextual Person-Presence Fact applies | HTBW | Stewardship | Required | **A** |
| Preferred notification paths | **Continuity** owns the preference; **Operational Trust** decides when it may be applied | HTBW | Continuity | Required | **A** |
| Escalation contacts | **Stewardship** ladder; **Operational Trust** authority | HTBW | Stewardship | Required | **A** — **OD-22** |
| Disclosure and retention rules for care information | **Operational Trust** policy; retention per **DL-47** | HTBW | Operational Trust | Required | **A** |
| **Delegated care authority** — David acting for Eleanor | **Resolved as DL-57.** An explicit **Delegated Access Grant** (subject, grantee, operations, scope) | HTBW | Stewardship (grant), Operational Trust (proceed/disclosure) | Required | **A** |
| Caregiver relationship as a relationship *type* | **Resolved as DL-57.** No new relationship type is created; `caretaker-of` continues to record accountability for an obligation or Asset only. Access over a Person's Stewardship content is the **Delegated Access Grant**, never the relationship itself | HTBW | Foundation (grant type), Stewardship (grant record) | Required | **A** |

## Ownership map

| # | Question | Owner | Statement |
|---|---|---|---|
| 1 | Authoritative Truth inputs | **Truth** | Room environmental Facts, Contextual Person-Presence Facts, and wearable-derived Facts where consented |
| 2 | Identity requirements | **Identity** | Purpose-specific assertions only. **Participation is optional and requires consent**; withdrawn consent removes the evidence, not merely the display |
| 3 | Consent or authority | **Consent → Available Evidence → Identity → Operational Trust** | The accepted chain. Consent is an **eligibility** dependency (**DL-41**), never a platform dependency |
| 4 | Operational Trust evaluation | **Operational Trust** | Audience, disclosure, surface, urgency entitlement, and confirmation. **A medication reminder is health content and is audience-evaluated before it is spoken** |
| 5 | Stewardship assessment | **Stewardship** | Whether each **explicitly configured** care obligation is met, due, unmet, overdue, waived, or unknown |
| 6 | Obligation or advisory | **Stewardship** | Care obligations of health significance |
| 7 | Notification path | Stewardship originates; **Operational Trust** governs; **Concierge** delivers | — |
| 8 | Corrective-action path | Human, or environmental adjustment by an executor | — |
| 9 | Execution owner | **Concierge** decides; an **executor or a person** performs | — |
| 10 | Explainability | Decision Trace | Which configured rule, whose consent, which audience evaluation, which escalation, and **why nothing was said where nothing was said** |
| 11 | Continuity interaction | **Continuity** | Preferred delivery, preferred presentation, and re-presentation preference (**OD-48**). **Continuity is not a child of Stewardship** |
| 12 | Retention | **DL-47** + consent lifecycle | Consent-lifecycle records are a **structural retention floor** that survives any configured window |
| 13 | Closure criteria | **Stewardship** | Recorded acknowledgement or recorded administration, per the accepted **Care Evidence Record** (**DL-48**) |
| 14 | Failure / uncertainty | **Stewardship** and **Operational Trust** | Unknown facts produce `unknown` obligations; uncertain audience degrades the **delivery**, not the governance (**P32**, **OD-71**) |
| 15 | HA native capabilities | Home Assistant | Person, Calendar, `todo`, Companion App surfaces, Recorder |
| 16 | What must never happen | — | **No medical diagnosis, no clinical advice, no health inference, and no wellness scoring.** HTBW is **not a life-safety system** |
| 17 | Human override | **Operational Trust** | Eleanor may withdraw consent, decline participation, or refuse a care rule, and the home must degrade honestly rather than continue silently |
| 18 | Dignity | — | **Being cared for must never read as being monitored.** Care obligations exist because Eleanor agreed to them, and the home can say so |

## Reference scenarios

### A — A medication reminder becomes due

| Step | Responsibility | Statement |
|---|---|---|
| 1 | **Stewardship** | The medication care obligation is `due`; accountability is Eleanor; significance is health |
| 2 | **Identity** | Produces the purpose-specific assertion required for a person-directed delivery |
| 3 | **Operational Trust** | Evaluates audience, consent, disclosure, surface, and urgency entitlement. Guests are in the Living Space, so a shared audible surface is **not** permitted |
| 4 | **Concierge** | Delivers privately, records the suppressed shared delivery, and explains both |
| 5 | **Stewardship** | Awaits the recorded outcome; the obligation remains `due` until then |

### B — A physician appointment approaches

Identical in shape to Use Case 2 Scenario A, with an additional disclosure constraint: **the fact that
an appointment exists is itself health content.**

### C — A wearable reports an observation requiring attention

| Step | Responsibility | Statement |
|---|---|---|
| 1 | **Truth** | Publishes the observation as a Fact with confidence, provenance, and freshness |
| 2 | **Stewardship** | Evaluates it against an **explicitly configured** care rule the household and Eleanor agreed |
| 3 | **Stewardship** | Where a rule is breached, creates a care obligation and applies escalation **intent** |
| 4 | **Operational Trust** | Governs the escalation audience and the disclosure |
| 5 | **Concierge** | Escalates per accepted policy and explains |

**No diagnosis occurs at any step.** The home reports what was observed and which agreed rule it
crossed — never what it might mean clinically.

### D — A room falls outside the environment Eleanor needs

| Step | Responsibility | Statement |
|---|---|---|
| 1 | **Truth** | The Primary Bedroom is at 16°C |
| 2 | **Stewardship** | The declared comfort-care requirement is unmet |
| 3 | **Operational Trust** | Adjusting the room climate autonomously is permitted |
| 4 | **Concierge** | Requests the adjustment and explains |
| 5 | **Executor** | The climate entity is changed by the automation or service call |
| 6 | **Truth**, then **Stewardship** | The temperature returns to range; the obligation returns to `met` |

### E — Eleanor's declared humidity requirement, evaluated where she currently is (DL-61)

| Step | Responsibility | Statement |
|---|---|---|
| 1 | **Foundation**, through Person Setup | Eleanor's declared humidity requirement: 45–60% |
| 2 | **Identity**, then **Truth** | Eleanor's consented bracelet supports a current **Contextual Person-Presence Fact**: Eleanor is in the Den |
| 3 | **Truth** | The Den is at 38% relative humidity, Truth Confidence Band: High |
| 4 | **Stewardship** | Eleanor's humidity requirement is `unmet` — 38% is below her declared 45% minimum |
| 5 | **Operational Trust** | Evaluates disclosure and audience before any Communication |
| 6 | **Concierge** | Conveys only where authorized, and explains: current value, required range, Room, and time |

**No diagnosis is produced.** The result states that a declared range was not met by a current
reading — never that a condition exists or requires clinical attention.

### F — Eleanor's location becomes unknown (DL-61)

| Step | Responsibility | Statement |
|---|---|---|
| 1 | **Truth** | Eleanor's Contextual Person-Presence Fact becomes `unknown` — the bracelet's evidence no longer supports a current Room |
| 2 | **Stewardship** | Eleanor's environmental requirements are **not evaluated against the last known Room** |
| 3 | **Concierge** | States that current suitability cannot be evaluated because Eleanor's location is unknown — never that the prior Room remains suitable or unsuitable |

## Acceptance scenarios

| # | Given | Then | Must not |
|---|---|---|---|
| 3.1 | Anywhere in the model | Eleanor is a **Person** | Model a person as an Asset, an inventory item, or a tracked object |
| 3.2 | Consent is withheld or withdrawn | The evidence becomes **ineligible before weighting** (**DL-38**), and dependent capabilities become **unavailable and say so** (**DL-41**) | Down-weight the evidence and continue, or degrade silently |
| 3.3 | A medication reminder with guests present | Private delivery or content-free indication | Announce health content to a shared surface because the action was permitted (**P32**) |
| 3.4 | A wearable observation | Evaluated only against an explicitly agreed rule | Produce a diagnosis, a clinical interpretation, or a wellness score |
| 3.5 | An escalation to David | Performed by Concierge under Operational Trust authority, with a Decision Trace | Stewardship escalating directly |
| 3.9 | Eleanor's declared humidity requirement and a current Den Fact below it | The requirement is `unmet`, explainable to the current Fact, the requirement, and their provenance (**DL-61**) | Report a diagnosis, a health verdict, or a Room-wide health state |
| 3.10 | Eleanor's location is unknown | No current suitability claim; the prior Room is never substituted as current | Evaluate the last known Room as current |
| 3.11 | Eleanor and Tom share a Room with different declared requirements | Each is evaluated independently; a conflict between them is surfaced, never silently resolved | Average, rank, or merge their requirements into one Room verdict |
| 3.6 | David wants to manage Eleanor's care | **Supported through an explicit Delegated Access Grant** (**DL-57**) that Eleanor establishes, or an authorized proxy establishes under the capacity model, scoped to specific obligations and operations | Infer delegated authority from the `caretaker-of` relationship, a Role, or administrator status alone |
| 3.7 | Any care record | Retained under **DL-47** with consent-lifecycle floors | Retain health content beyond the consented lifecycle |
| 3.8 | Any emergency-shaped condition | Reported honestly within the accepted limits | Represent HTBW as a life-safety system |

## Known implementation gaps

| Gap | Classification |
|---|---|
| Consent user experience — capture, scope, review, withdrawal | **OD-06** |
| Safety-category scope, given the explicit life-safety non-claim | **OD-56** |
| Audience-uncertainty disclosure policy | **OD-71** |
| Completion evidence for a care obligation | **Resolved — DL-48**, as a **Care Evidence Record** |

---

# Use Case 4 — Washing-Machine Leak Protection

## Human purpose

The household wants to protect the home, the flooring, and the belongings around the Laundry from
water damage.

## Household declaration

> "Water where it shouldn't be matters. Stop it if you can, and tell us either way."

## Subjects of care

| Subject | Object type | Owner |
|---|---|---|
| The Laundry and adjacent flooring | **Room** / the **Home** | Foundation |
| The washing machine | **Asset** | Foundation asset model |

## Required setup

| Definition activity | Architectural owner | Native HA representation | Status |
|---|---|---|---|
| Leak sensor and its declared location | Room Configuration participation set | Binary sensor entity, Area assignment | **A** |
| Protected area declaration | Household declaration, held as a Stewardship care requirement | Area | **E** |
| Associated washing machine Asset | Foundation asset model | Device where device-backed | **A** |
| Available shutoff device | Foundation asset model + Room Configuration | Valve / switch entity | **A** |
| **Autonomous-action policy** — may the home shut the water off by itself | **Operational Trust** | None | **A** |
| Escalation path and accountability | **Stewardship** ladder | None | **A** — **OD-22** |
| Inspection / cleanup obligation after an event | **Stewardship** | — | **E** |
| Notification recipients | **OD-52** | — | **U** |

## Ownership map

| # | Question | Owner | Statement |
|---|---|---|---|
| 1 | Authoritative Truth inputs | **Truth** | *The leak sensor in the Laundry reports wet.* That is the Fact — **and it is the whole Fact** |
| 2 | Identity requirements | **Identity** | None for the assessment; required only for person-directed delivery |
| 3 | Consent or authority | Household | The autonomy ceiling for water shutoff is a household configuration |
| 4 | Operational Trust evaluation | **Operational Trust** | Whether shutoff may occur autonomously, and whether the interruption is entitled to the urgency it wants |
| 5 | Stewardship assessment | **Stewardship** | The home's water-protection care obligation is `unmet` |
| 6 | Obligation or advisory | **Stewardship** | A water-protection obligation of safety significance |
| 7 | Notification path | Stewardship originates; Concierge delivers | **Notification and corrective action are independent.** Either, both, or neither may occur |
| 8 | Corrective-action path | Obligation → Operational Trust → executor | — |
| 9 | Execution owner | **Concierge** decides; a Home Assistant automation or service call performs the shutoff | **Stewardship does not close the valve, exactly as Stewardship does not close the garage door** |
| 10 | Explainability | Decision Trace | Which sensor, which policy, whether shutoff was available, whether it was authorised, what was done, and **what was not done and why** |
| 11 | Continuity interaction | **None** | — |
| 12 | Retention | **DL-47** | The Decision Trace and the obligation history; **the sensor's state history stays in Recorder** (**DL-42**) |
| 13 | Closure criteria | **Stewardship** | Truth reports the sensor dry **and** any declared inspection or cleanup obligation is discharged. **Dry is not the same as resolved** |
| 14 | Failure / uncertainty | **Stewardship** | No shutoff device, or shutoff unavailable → the capability is **unavailable and named** (**DL-41**), and the obligation stands |
| 15 | HA native capabilities | Home Assistant | Binary sensor, valve/switch, automations, Recorder. **A leak-response automation the household already owns must not be rewritten** (**OD-64**) |
| 16 | What must never happen | — | **The Fact must not be overstated.** *"The sensor is wet"* is not *"the house is flooding"* and is not *"your belongings are damaged"* |
| 17 | Independence of paths | **Concierge** | Acting is not announcing (**P32**). Announcing is not acting |
| 18 | Duplication | — | **No second copy of the sensor state is created** anywhere in HTBW (**DL-42**, **DL-46**) |

## Reference scenarios

### A–E — The full path

| Step | Responsibility | Statement |
|---|---|---|
| 1 | **Truth** | The Laundry leak sensor reports wet, Truth Confidence Band: High, fresh |
| 2 | **Stewardship** | The home's water-protection obligation is `unmet`; significance is safety, household-declared |
| 3 | **Operational Trust** | Autonomous shutoff is permitted; interruption at high urgency is entitled |
| 4 | **Concierge** | Requests shutoff, conveys to the household, explains |
| 5 | **Executor** | The Home Assistant automation closes the valve |
| 6 | **Truth** | The valve reports closed; the sensor still reports wet |
| 7 | **Stewardship** | The **shutoff** obligation is discharged; the **water-protection** obligation remains `unmet` |
| 8 | **Truth** | The sensor reports dry |
| 9 | **Stewardship** | Creates the declared **inspection** obligation, and closes the water-protection obligation only when it is discharged |

### D variant — Shutoff unavailable or unauthorised

| Step | Responsibility | Statement |
|---|---|---|
| 3a | **Operational Trust** | Autonomous shutoff is **not** permitted, or no shutoff capability is declared |
| 4a | **Concierge** | Conveys through the accepted path, and **names the missing capability in a sentence the household can act on** (**DL-41**) |

**A household told the home lacked permission when it actually lacked a valve has been told the wrong
thing.**

## Acceptance scenarios

| # | Given | Then | Must not |
|---|---|---|---|
| 4.1 | The sensor reports wet | Exactly one Truth Fact, stated at its actual scope | Escalate the Fact into a property-damage claim |
| 4.2 | Shutoff is authorised and available | The executor performs it and the Decision Trace names it | Attribute the shutoff to Stewardship |
| 4.3 | Shutoff is unavailable | The capability is reported **unavailable** with the missing dependency named | Report a permission failure, or silently do nothing |
| 4.4 | Shutoff succeeds | Notification is still evaluated independently | Assume that acting discharges the duty to tell |
| 4.5 | The sensor becomes dry | The obligation is re-evaluated, not auto-closed | Treat *dry* as *resolved* while an inspection obligation stands |
| 4.6 | An existing household leak automation exists | It is referenced as the executor | Require the household to rewrite it |
| 4.7 | Anywhere | Sensor history stays in Recorder | Create a second HTBW copy of the sensor state |
| 4.8 | Conflicting or insufficient leak evidence | **Investigation Needed** may be recommended, stating what is known, what is not, and why (**DL-79**) | Fabricate a conclusion, or silently pick a side |

## Known implementation gaps

| Gap | Classification |
|---|---|
| Native automation, script, and scene **awareness** as governed executor evidence | **OD-64** |
| Behaviour attribution — how *what changed the valve* is asserted | **OD-63** |
| Urgency entitlement model | **Resolved — DL-77** |
| Safety-category scope | **Resolved — DL-79** |
| Obligation closure and the inspection follow-on | **Resolved — DL-48**. Closure requires a Care Evidence Record; a follow-on inspection is a **reopened** obligation retaining its identity |

---

# Use Case 5 — Window-Shade Battery Maintenance

## Human purpose

The household wants their seven battery-powered shades to keep working, without discovering the
problem when a shade stops moving.

## Household declaration

> "The shades matter enough to maintain, not just to repair."

## Subjects of care

| Subject | Object type | Owner |
|---|---|---|
| Seven shades | **Assets**, exposed as a **group** in Room Configuration | Foundation |

## Required setup

| Definition activity | Architectural owner | Native HA representation | Status |
|---|---|---|---|
| Shade Assets and room association | Foundation asset model | Existing Devices — **referenced, never copied** (**DL-31**) | **A** |
| Battery entities | Home Assistant | Battery sensor entities | **A** |
| **Battery-maintenance threshold** | **Household declaration**, held as a Stewardship care requirement | None | **A** |
| Caretaker assignment | **Stewardship** | None | **A** |
| Replacement process and instructions | Foundation asset model documentation | None | **A** |
| Reminder destination | **Not a Stewardship setting** — Concierge and Operational Trust | — | **A** |
| Maintenance history | **Stewardship** history | Not Recorder | **A** |

## Ownership map

| # | Question | Owner | Statement |
|---|---|---|---|
| 1 | Authoritative Truth inputs | **Truth** | Battery level per shade, with freshness. **Home Assistant remains authoritative for the entity state** |
| 2 | Identity requirements | **Identity** | None for the assessment |
| 3 | Consent or authority | Household | The threshold is a household declaration, not a manufacturer default adopted silently |
| 4 | Operational Trust evaluation | **Operational Trust** | Delivery entitlement only. A maintenance reminder is low-urgency and must not interrupt as though it were safety |
| 5 | Stewardship assessment | **Stewardship** | Whether the preventative-maintenance obligation is `met`, `due`, `overdue`, or `unknown` |
| 6 | Obligation or advisory | **Stewardship** | Preventative maintenance — an **obligation** where the threshold is crossed, an **Advisory** where the household merely could do better |
| 7 | Notification path | Stewardship originates; Concierge delivers | — |
| 8 | Corrective-action path | **Human.** Nothing automates a battery change | — |
| 9 | Execution owner | A **person** | — |
| 10 | Explainability | Decision Trace | Which entity, which threshold, **whose threshold**, when it was crossed |
| 11 | Continuity interaction | **None** | — |
| 12 | Retention | **DL-47** | Replacement history is governed **Stewardship** history and survives the battery readings that produced it |
| 13 | Closure criteria | **Stewardship** | A recorded replacement. A **rising battery level is corroboration, not a record of care** |
| 14 | Failure / uncertainty | **Stewardship** | A stale or unavailable battery reading is `unknown`. **An unavailable battery entity is never a healthy battery** |
| 15 | HA native capabilities | Home Assistant | Battery sensors, Device registry, Area, `todo` projection (**OD-23**), Recorder |
| 16 | What must never happen | — | **No new confidence band is created.** Battery freshness is Truth freshness; it is not an Identity band (**DL-39**) and not an invented health score |
| 17 | Grouping | **Stewardship** | Whether seven near-simultaneous obligations are grouped, prioritised, or tracked separately is **unresolved** — see gaps |
| 18 | Duplication | — | The battery level is **not** copied into HTBW |

## Reference scenarios

### A — The battery is healthy

Obligation `met`. No Communication. Nothing is said.

### B — The threshold is approached

| Step | Responsibility | Statement |
|---|---|---|
| 1 | **Truth** | Dining Shade 2 battery is at 18%, fresh |
| 2 | **Stewardship** | The declared threshold is 20%. The preventative-maintenance obligation is `due` |
| 3 | **Operational Trust** | Delivery permitted at ordinary urgency |
| 4 | **Concierge** | Conveys it once, to the caretaker, in household vocabulary — *"the middle dining shade"*, never `cover.dining_shade_2` |
| 5 | **Tom** | Replaces the battery and records it |
| 6 | **Stewardship** | Closes the obligation and records the replacement |

### C — Several shades approach together

**Unresolved.** Grouping, prioritisation, and separate tracking are all defensible, and the accepted
architecture does not choose. What it **does** require: whatever is chosen, each shade's obligation
remains individually explainable, and a grouped Communication is still one Communication with one
audience evaluation.

### D — The reading is stale or unavailable

| Step | Responsibility | Statement |
|---|---|---|
| 1 | **Truth** | The battery Fact is `unknown` — outside its freshness window, or the entity is unavailable |
| 2 | **Stewardship** | The obligation is `unknown`, **not** `met` |
| 3 | **Concierge** | Says so: *"I can't tell you the battery state of the middle dining shade."* |

## Acceptance scenarios

| # | Given | Then | Must not |
|---|---|---|---|
| 5.1 | Battery above threshold | No obligation, no Communication | Report healthy status unprompted |
| 5.2 | Battery below the **declared** threshold | Obligation `due`, with the threshold's source named | Adopt a manufacturer or integration default as though the household chose it |
| 5.3 | Battery entity unavailable | Obligation `unknown` | Treat unavailable as healthy, or carry the last reading forward |
| 5.4 | A replacement occurs | The obligation closes on the **recorded replacement** | Close on a rising battery reading alone |
| 5.5 | Anywhere | Home Assistant remains authoritative for battery state | Create an HTBW battery store or an invented health band |
| 5.6 | Any explanation | Uses household vocabulary | Use entity IDs |
| 5.7 | Several obligations at once | Each remains individually explainable | Collapse them into an unattributable summary |

## Known implementation gaps

| Gap | Classification |
|---|---|
| Grouping and prioritisation of simultaneous obligations | **OD-23** — **DL-48** records that grouping is a projection concern and not part of the obligation model |
| Fact validity and expiration defaults per Fact class — *how stale is stale* | **Resolved — DL-59** |
| Obligation projection surface | **OD-23** |
| Significance representation for a low-significance maintenance obligation | **Resolved — DL-75** |

---

# Use Case 6 — HVAC Filter Maintenance

## Human purpose

The household wants the HVAC system to keep working properly and the home environment to stay
maintained.

## Household declaration

> "The HVAC system matters. Remind us before it degrades, not after."

## Subjects of care

| Subject | Object type | Owner |
|---|---|---|
| HVAC equipment | **Asset** | Foundation asset model |
| The Home's environment | **Home** | Foundation |

## Required setup

| Definition activity | Architectural owner | Native HA representation | Status |
|---|---|---|---|
| HVAC equipment Asset, filter type, filter location | Foundation asset model | Device where device-backed | **A** |
| Replacement interval, last replacement, next expected replacement | **Stewardship** obligation schedule | Calendar/`todo` projection is **OD-23** | **A / U** |
| **Usage-based or date-based rule** | **Household declaration**, held as a Stewardship care requirement | None | **A** |
| Runtime or usage input where available | **Truth** | Entity state, Recorder statistics | **A** |
| Caretaker assignment and replacement instructions | **Stewardship** / Foundation documentation | None | **A** |
| Maintenance history | **Stewardship** history | Not Recorder | **A** |

## Ownership map

| # | Question | Owner | Statement |
|---|---|---|---|
| 1 | Authoritative Truth inputs | **Truth** | Runtime, usage, or differential-pressure Facts where the household has them. **Where none exist, the schedule alone governs** |
| 2 | Identity requirements | **Identity** | None for the assessment |
| 3 | Consent or authority | Household | The interval is a household declaration, informed by manufacturer guidance recorded as **provenance** |
| 4 | Operational Trust evaluation | **Operational Trust** | Delivery entitlement only |
| 5 | Stewardship assessment | **Stewardship** | Whether the maintenance obligation is `met`, `due`, `overdue`, `waived`, or `unknown` |
| 6 | Obligation or advisory | **Stewardship** | A maintenance obligation |
| 7 | Notification path | Stewardship originates; Concierge delivers | — |
| 8 | Corrective-action path | **Human** | — |
| 9 | Execution owner | A **person**, or a **Service** provider relationship | **No service action is attributed to Stewardship** |
| 10 | Explainability | Decision Trace | Which schedule, its **provenance** — manufacturer guidance, household decision, or learned suggestion — and when it became due |
| 11 | Continuity interaction | **None** | — |
| 12 | Retention | **DL-47** | Maintenance history is long-lived **Stewardship** history. *When was this last serviced?* must remain answerable years later |
| 13 | Closure criteria | **Stewardship** | A recorded replacement. **The accepted completion evidence is unresolved** (**OD-75**) |
| 14 | Failure / uncertainty | **Stewardship** | No usage data → fall back to the declared schedule and **say that is what happened**. Never silently assert an inferred usage figure |
| 15 | HA native capabilities | Home Assistant | Climate entities, Recorder long-term statistics, Calendar, `todo` |
| 16 | What must never happen | — | **`overdue` is not failure.** An overdue filter obligation is not a claim that the HVAC system is broken or that air quality is poor |
| 17 | Deferral | **Stewardship** | A deliberately deferred obligation must remain distinguishable from an ignored one — **unresolved** (**OD-75**) |
| 18 | Repeated non-completion | **Stewardship** | **The pattern itself becomes reportable**, and Concierge must not send a fifth identical reminder |

## Reference scenarios

### A — Replacement becomes due

Stewardship sets the obligation `due`. Operational Trust permits ordinary delivery. Concierge conveys
it once.

### B — Replacement is completed

The obligation closes, the maintenance history updates, and the next expected replacement is derived
from the recorded event rather than from the original schedule origin.

### C — Replacement is deferred

The household says *"not this month."* The obligation must be representable as **deliberately
deferred** — neither `met`, nor silently `overdue`, nor forgotten. **The accepted architecture does not
yet provide this state.**

### D — Usage information is unavailable

| Step | Responsibility | Statement |
|---|---|---|
| 1 | **Truth** | Runtime statistics are unavailable |
| 2 | **Stewardship** | Falls back to the declared date-based schedule |
| 3 | **Concierge** | Explains that the reminder is date-based because runtime data is unavailable |

## Acceptance scenarios

| # | Given | Then | Must not |
|---|---|---|---|
| 6.1 | The interval elapses | Obligation `due`, with the schedule's provenance named | Present a manufacturer default as a household decision |
| 6.2 | Replacement recorded | Obligation closes; history updates; next due date derives from the record | Close from a reminder being dismissed |
| 6.3 | Deferral requested | Deliberate deferral is distinguishable from neglect | Silently roll the obligation forward, or mark it `met` |
| 6.4 | Usage data unavailable | Schedule fallback, stated plainly | Infer runtime, or claim usage-based evaluation |
| 6.5 | Four reminders ignored | The **pattern** is reported, and Concierge changes approach | Send a fifth identical reminder |
| 6.6 | The obligation is `overdue` | Reported as an unmet care obligation | Report equipment failure or degraded air quality |

## Known implementation gaps

| Gap | Classification |
|---|---|
| **`deferred` and `closed` are resolved as DL-48.** They are **lifecycle** transitions, not condition states. The condition states remain `met`, `due`, `unmet`, `overdue`, `waived`, `unknown`; the lifecycle states are `raised`, `active`, `deferred`, `closed`, `reopened` | **Resolved — DL-48** |
| Accepted completion evidence | **Resolved — DL-48**, as a **Care Evidence Record** |
| Escalation ladder semantics for a repeatedly unmet obligation | **OD-22** |
| Obligation projection surface | **OD-23** |

---

# Use Case 7 — Irrigation Stewardship

## Human purpose

The household values the landscape and wants it watered responsibly — not on a timer that ignores the
weather.

## Household declaration

> "The landscape matters, and so does not wasting water."

## Subjects of care

| Subject | Object type | Owner |
|---|---|---|
| Four irrigation zones and their landscape areas | **Assets** | Foundation asset model |
| The irrigation controller | **Asset** | Foundation asset model |

## Required setup

| Definition activity | Architectural owner | Native HA representation | Status |
|---|---|---|---|
| Zones and associated landscape areas | Foundation asset model | Existing Devices/Entities — referenced | **A** |
| Irrigation schedule | **Stewardship** care requirement, or an existing native schedule referenced as the executor | Schedule helper, automation | **A / E** |
| Household objectives and water restrictions | **Household declaration** + **Operational Trust** policy | None | **A** |
| Rainfall and forecast inputs | **Truth** | Weather integration entities | **A** |
| Soil or moisture inputs where they exist | **Truth** | Sensor entities | **A** |
| Autonomous-action policy | **Operational Trust** | None | **A** |
| Caretaker assignment | **Stewardship** | None | **A** |

## Ownership map

| # | Question | Owner | Statement |
|---|---|---|---|
| 1 | Authoritative Truth inputs | **Truth** | Rainfall, forecast, and soil-moisture Facts. **Stewardship does not own weather truth, and does not fetch a forecast** |
| 2 | Identity requirements | **Identity** | None |
| 3 | Consent or authority | Household + **Operational Trust** | Restrictions and autonomy ceilings are household policy |
| 4 | Operational Trust evaluation | **Operational Trust** | Whether the schedule may be skipped or altered autonomously, and whether a restriction prohibits watering outright |
| 5 | Stewardship assessment | **Stewardship** | Whether the landscape-care requirement is currently satisfied by rainfall, or requires irrigation |
| 6 | Obligation or advisory | **Stewardship** | A landscape-care obligation, or an **Advisory** where watering is merely suboptimal |
| 7 | Notification path | Stewardship originates; Concierge delivers | Routine skips are usually **not** worth conveying, and silence is a legitimate outcome |
| 8 | Corrective-action path | Obligation → Operational Trust → executor | — |
| 9 | Execution owner | The **irrigation controller integration, automation, or schedule** | **Stewardship never opens a valve** |
| 10 | Explainability | Decision Trace | **Why watering occurred, and why it did not.** A skipped cycle is an **Intentional Non-Action** and must be as explainable as a run |
| 11 | Continuity interaction | **None** | — |
| 12 | Retention | **DL-47** | Obligation and decision history; **weather Facts are Truth's Historical Facts** |
| 13 | Closure criteria | **Stewardship** | The cycle ran, or the requirement was satisfied without it |
| 14 | Failure / uncertainty | **Stewardship** | Unavailable rainfall data → the declared default applies, and the fallback is stated. **No soil condition is inferred from weather** |
| 15 | HA native capabilities | Home Assistant | Weather integration, Schedule helper, valve/switch entities, automations |
| 16 | What must never happen | — | **No unsupported soil inference.** Absent a moisture sensor, the home does not know whether the ground is wet |
| 17 | Restrictions | **Operational Trust** | A municipal or household restriction is a **prohibition**, not a preference to be weighed |
| 18 | Existing automations | — | An existing irrigation automation is referenced as the executor and **is not rewritten** (**OD-64**) |

## Reference scenarios

### A — Scheduled watering remains appropriate

Stewardship's care requirement is unsatisfied, Operational Trust permits, and the accepted executor
runs the schedule.

### B — Rainfall makes watering inappropriate

| Step | Responsibility | Statement |
|---|---|---|
| 1 | **Truth** | 22 mm of rainfall in the last 24 hours; forecast rain tomorrow |
| 2 | **Stewardship** | The landscape-care requirement is currently satisfied. The irrigation obligation is `met` without action |
| 3 | **Operational Trust** | Skipping the scheduled cycle autonomously is permitted |
| 4 | **Concierge** | Skips the cycle and records an **Intentional Non-Action** with its reason |

> *"I skipped the front zones this morning — 22 millimetres of rain since yesterday, and more forecast."*

### C — A zone requires maintenance

Stewardship creates a maintenance obligation exactly as in Use Case 6. The path is identical; only the
subject differs.

## Acceptance scenarios

| # | Given | Then | Must not |
|---|---|---|---|
| 7.1 | Rainfall data available | Consumed as **Truth** Facts | Stewardship owning, fetching, or caching weather |
| 7.2 | No soil-moisture sensor | The declared rule applies, and its basis is stated | Infer soil moisture from rainfall |
| 7.3 | A restriction is in force | Watering is prohibited | Weigh a restriction against a landscape preference |
| 7.4 | A cycle is skipped | Recorded as an explainable **Intentional Non-Action** | Skip silently and unrecorded |
| 7.5 | A cycle runs | The executor is named in the Decision Trace | Attribute the valve operation to Stewardship |
| 7.6 | An existing irrigation automation exists | Referenced as the executor | Require the household to rebuild it in HTBW |
| 7.7 | Weather data unavailable | The declared fallback applies and is stated | Present a fallback decision as a weather-informed one |

## Known implementation gaps

| Gap | Classification |
|---|---|
| Native automation and schedule awareness as governed executor evidence | **OD-64** |
| Behaviour attribution for the resulting change | **OD-63** |
| Whether a *satisfied without action* obligation is distinguishable from a *performed* one | **Resolved — DL-48**. `observed` versus `performed` evidence kinds |

---

# Use Case 8 — Antique Piano Stewardship

## Human purpose

The 1918 A.B. Chase grand piano is part of the household's history. They want to preserve both its
condition and its use.

## Household declaration

> "The piano matters. Help us keep it playable."

## Subjects of care

| Subject | Object type | Owner |
|---|---|---|
| The piano | **Asset** | Foundation asset model |
| The Music Room | **Room** | Foundation / Room Configuration |

## Required setup

| Definition activity | Architectural owner | Native HA representation | Status |
|---|---|---|---|
| Asset registration, authoritative identity, images, historical information | Foundation asset model | A native Device may be created for a non-device Asset (**DL-31**) | **A** |
| Accompanying documents and insurance documentation | Foundation asset model, anchored in **Connected Storage** | None — reached through the Asset, never a file browser (**DL-44**) | **A** |
| Room placement, declared and current | Foundation `located-in`; **Truth** Location Fact | Area | **A** |
| Tuner as a **Service** relationship | Foundation asset model | None | **A** |
| Tuning schedule | **Stewardship** obligation | **OD-23** | **A / U** |
| Acceptable environmental conditions, as properties of the instrument | Foundation asset model | None | **A** |
| Significance declaration | **Stewardship**, with household provenance | None | **A** — **DL-75** |
| Maintenance history | **Stewardship** history | Not Recorder | **A** |

## Ownership map

| # | Question | Owner | Statement |
|---|---|---|---|
| 1 | Authoritative Truth inputs | **Truth** | Music Room humidity and temperature, with confidence, provenance, and freshness |
| 2 | Identity requirements | **Identity** | None for the assessment |
| 3 | Consent or authority | Household | Significance is declared, never derived from the instrument's appraised value |
| 4 | Operational Trust evaluation | **Operational Trust** | Whether humidification may run autonomously; whether the caretaker Communication is permitted |
| 5 | Stewardship assessment | **Stewardship** | Compares Truth against the declared limits; sets the preservation obligation state |
| 6 | Obligation or advisory | **Stewardship** | Preservation obligation and tuning maintenance obligation — **two obligations, one Asset** |
| 7 | Notification path | Stewardship originates; Concierge delivers | — |
| 8 | Corrective-action path | Obligation → Operational Trust → executor | — |
| 9 | Execution owner | **Concierge** decides; an automation or the tuner performs | — |
| 10 | Explainability | Decision Trace | The canonical worked example: asset limit, Truth Fact, obligation, authority, action |
| 11 | Continuity interaction | **None** | Playing the piano is not an HTBW Experience |
| 12 | Retention | **DL-47** | Tuning and conservation history is long-lived **Stewardship** history |
| 13 | Closure criteria | **Stewardship** | Truth reports the environment back in range; the tuning obligation closes on recorded service |
| 14 | Failure / uncertainty | **Stewardship** | Scenario 4 of [stewardship-obligations.md](stewardship-obligations.md) applies unchanged: a failed sensor produces `unknown`, never `met` |
| 15 | HA native capabilities | Home Assistant | Area, humidity sensors, humidifier entity, Calendar, `todo`, Recorder |
| 16 | Conflicts | **Stewardship** | Where the rare-book collection and the piano want incompatible humidity, **both obligations are surfaced with their significance and the conflict is not silently resolved** |
| 17 | Movement | **Stewardship** | Moving the piano to another Room changes which Truth Facts govern it and may change the caretaker. **Care requirements are re-evaluated, not carried over** |
| 18 | Vocabulary | — | *"the piano"* is a Room-scoped interaction alias. The Asset remains *1918 A.B. Chase 6' Grand Piano* |

## Reference scenarios

### A — Annual tuning approaches

Stewardship creates the maintenance obligation; the caretaker is conveyed to; the tuner is a Service
relationship, not an executor inside HTBW.

### B — Room humidity remains outside the preferred range

Identical to [stewardship-obligations.md](stewardship-obligations.md) Scenario 3, which remains the
canonical worked example.

### C — The piano moves to another Room

| Step | Responsibility | Statement |
|---|---|---|
| 1 | **Foundation asset model** | The declared `located-in` relationship changes to the Den |
| 2 | **Room Configuration** | The Den's configured Primary Authority for humidity becomes the relevant source |
| 3 | **Truth** | Den humidity Facts now govern |
| 4 | **Stewardship** | Re-evaluates the preservation obligation against Den Facts. **Music Room Facts no longer satisfy it** |
| 5 | **Stewardship** | The caretaker assignment is re-examined where it was room-derived |

### D — Service is completed

The maintenance history updates and the obligation closes on the recorded service — **not** on the
calendar entry passing.

## Acceptance scenarios

| # | Given | Then | Must not |
|---|---|---|---|
| 8.1 | Significance | Explicitly household-declared with provenance | Derive significance from appraised value or age |
| 8.2 | Environmental facts | Owned by **Truth** | Stewardship publishing, caching, or re-deriving humidity |
| 8.3 | A maintenance obligation | Explainable to schedule, provenance, and accountability | Present it without its origin |
| 8.4 | The Asset moves | Care requirements are re-evaluated against the new Room | Continue evaluating against the previous Room's Facts |
| 8.5 | Service completed | History recorded as an independently retainable Change Record | Embed the history as a mutable field on the Asset record |
| 8.6 | Conflicting obligations | Both surfaced with significance | Silently prefer one |
| 8.7 | Any explanation | Uses the household alias in speech and the authoritative identity in the record | Replace the authoritative name with the alias |

## Known implementation gaps

| Gap | Classification |
|---|---|
| Whether a caretaker assignment is Room-derived, Asset-derived, or both, when an Asset moves | **E — REMEDIATION REQUIRED, folded into OD-75** |
| Obligation projection into calendars | **OD-23** |
| Significance representation | **Resolved — DL-75** |
| Governed-record persistence shape | **OD-01** |

---

# Cross-use-case responsibility map

**This table does not collapse responsibilities. It makes the handoffs explicit.**
Where a cell reads **none**, that is a deliberate architectural statement, not an omission.

| Use case | Household declaration | Truth inputs | Identity | Consent / authority | Operational Trust | Stewardship | Continuity | Executor | Explainability | Retention | Closure | Implementation status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Artwork Preservation** | *This artwork matters; here are its limits, its cleaning cadence, and its caretaker* | Room temperature, humidity, illuminance, sun position; Asset Location Fact | **None** for assessment; required for person-directed delivery | Household declaration; no personal consent engaged | Autonomy for dehumidification; delivery entitlement; audience | Preservation + conservation obligations; significance with provenance | **None** | HA automation / service call, or a person | Fact, limit, declarer, policy, executor, outcome — by reference | Documents while the Asset lives; Change Records per Asset lifecycle; trace per External History Retention | Truth reports in-range, **or** completed care recorded | **A** for ownership; **U** for loan/custody (**OD-75**), projection (**OD-23**), significance form (**DL-75**) |
| **Pet Stewardship** | *Maisey matters; here is her care* | Pet Location Fact; activity Facts; caretaker presence | **None for the Pet** — Truth-only. Required for the human recipient | Household declaration; consent attaches to humans, not the Pet | Delivery, audience, disclosure, escalation authority | Medication, feeding, appointment, walk obligations | **None** — care history is Stewardship history | A **person** | Schedule, declaration, accountability, escalation reason | Care history per **DL-47**; wearable Facts as Historical Facts | Recorded administration or completed appointment | **A** for ownership; **U** for completion evidence (**OD-75**), recipients (**OD-52**) |
| **Aging-Parent Support** | *Eleanor matters, and she agreed to this help* | Room environment; Contextual Person-Presence; consented wearable Facts | **Required** — purpose-specific, consent-gated | **Consent is mandatory. Delegated authority is a Delegated Access Grant (DL-57)** | Audience, disclosure, surface, urgency, confirmation | Explicitly configured care obligations only | **Preferred delivery and presentation** | A **person**, or an environmental executor | Configured rule, consent, audience evaluation, escalation, and **why nothing was said** | **DL-47** + consent-lifecycle floors | Recorded acknowledgement or administration | **A** for ownership, including delegated care authority (**DL-57**) |
| **Washing-Machine Leak Protection** | *Water where it shouldn't be matters; stop it if you can* | Leak sensor Fact; valve state | **None** for assessment | Household autonomy ceiling for shutoff | Autonomous shutoff; urgency entitlement | Water-protection obligation; inspection follow-on | **None** | **HA automation or service call** | Sensor, policy, availability, action, and **non-action** | Trace + obligation history; sensor state stays in Recorder | Sensor dry **and** inspection discharged | **A** for ownership; **U** for executor evidence (**OD-64**), urgency (**resolved — DL-77**) |
| **Window-Shade Battery Maintenance** | *The shades matter enough to maintain* | Battery level Facts with freshness | **None** | Household-declared threshold | Delivery entitlement only | Preventative maintenance obligation or Advisory | **None** | A **person** | Entity, threshold, **whose threshold**, when crossed | Replacement history survives the readings | **Recorded replacement**, never a rising reading | **A** for ownership; **U** for grouping (**OD-75**); staleness resolved (**DL-59**) |
| **HVAC Filter Maintenance** | *The HVAC system matters; remind us before it degrades* | Runtime or usage Facts where available | **None** | Household-declared interval, manufacturer guidance as provenance | Delivery entitlement only | Maintenance obligation | **None** | A **person** or a **Service** provider | Schedule, provenance, due date, deferral | Long-lived Stewardship history | **Recorded replacement** | **A** for ownership; **REMEDIATION REQUIRED** for `deferred`/`closed` states (**OD-75**) |
| **Irrigation Stewardship** | *The landscape matters, and so does not wasting water* | Rainfall, forecast, soil moisture where present | **None** | Household objectives; restrictions as Operational Trust prohibitions | Autonomy to skip or alter; restriction enforcement | Landscape-care obligation; zone maintenance obligation | **None** | **Irrigation controller, automation, or schedule** | **Why it watered and why it did not** — non-action is first class | Obligation and decision history; weather is Truth's | Cycle ran, or requirement satisfied without it | **A** for ownership; **U** for executor evidence (**OD-64**), attribution (**OD-63**) |
| **Antique Piano Stewardship** | *The piano matters; keep it playable* | Music Room humidity and temperature | **None** | Household declaration of significance | Autonomy for humidification; delivery entitlement | Preservation obligation **and** tuning obligation | **None** | HA automation, or the tuner as a Service | The canonical worked example, end to end | Long-lived tuning and conservation history | In-range Truth, or recorded service | **A** for ownership; **U** for projection (**OD-23**), caretaker re-derivation on move (**OD-75**) |

---

## Rules these use cases enforce

1. **The household declares what matters.** Stewardship represents that declaration; it never
   substitutes its own.
2. **Stewardship begins with a declaration, not with an alert.** The obligation existed before
   anything went wrong.
3. **Significance is recorded with provenance**, and a significance judgement with no household or
   accepted origin is a **learned suggestion**, never an autonomous policy (**P26**, **DL-21**).
4. **There is no universal HTBW hierarchy of importance.** Price, sensor count, participation,
   residency, and registration confer no inherent worth.
5. **People are not Assets. Pets are not Assets.** Both may carry care obligations without becoming
   property.
6. **Stewardship never performs the action** and never calls a Home Assistant service. It states that
   an obligation is unmet.
7. **Corrective action and notification are independent paths.** Either, both, or neither may occur,
   and each is separately governed.
8. **The executor is always named.** An action with no attributable executor is an explainability
   defect.
9. **Truth owns current conditions.** Stewardship consumes them and never republishes, caches, or
   re-derives them.
10. **`unknown` is never `met`.** Absence of evidence is never compliance, and an unavailable entity is
    never a healthy one.
11. **Non-action is explainable.** A skipped irrigation cycle, a suppressed announcement, and a silent
    healthy asset are all decisions.
12. **Closure comes from the observed outcome or from recorded care** — never from a dismissed
    reminder or a ticked list item.
13. **No second Recorder, and no second copy of native state.**
14. **No diagnosis, no clinical interpretation, and no health inference** — for a person or an animal.

---

## Related documents

- [stewardship-obligations.md](stewardship-obligations.md) — the separation these use cases assume
- [../models/stewardship.md](../models/stewardship.md)
- [../contracts/stewardship-contract.md](../contracts/stewardship-contract.md)
- [../models/asset.md](../models/asset.md)
- [../models/truth.md](../models/truth.md)
- [../models/operational-trust.md](../models/operational-trust.md)
- [../models/continuity.md](../models/continuity.md)
- [../architecture/explainability.md](../architecture/explainability.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
