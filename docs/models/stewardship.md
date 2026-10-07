# Stewardship Model

> **Document status: Canonical model.**
> Terminology: [glossary.md](glossary.md). Owning responsibility: **Stewardship**.
> Contract: [../contracts/stewardship-contract.md](../contracts/stewardship-contract.md)

---

## Purpose

**Stewardship must not be reduced to a synonym for inventory.**

Stewardship is the responsibility for significance, care, obligations, lifecycle accountability, and
ongoing responsibility.

## Question answered

*What matters, what must be cared for, what obligations exist, and who is accountable?*

---

## Household authority — who declares that something matters

> **The household declares what matters. Stewardship represents that declaration as care
> expectations, evaluates authoritative observations against them, and creates governed care
> obligations when attention is required.**

Stated in the form the household hears:

> **The household determines what matters. Stewardship helps care for it.**

**Stewardship does not decide, on the household's behalf, that something matters.** The question this
responsibility answers — *what matters, and what must be cared for?* — is answered **for** the
household, from what the household has declared. It is not answered **about** the household.

This mirrors the boundary already accepted for Operational Trust: *the framework provides governance;
the household provides the values* (**DL-36**, **P26**). It applies identically here.

| The household decides | Stewardship does |
|---|---|
| That a person, animal, possession, space, or system matters | Represents that declaration, with **provenance** naming who declared it |
| What caring for it means — limits, schedules, cadences, expectations | Holds those care expectations as the requirement an obligation is evaluated against |
| Who is accountable | Records the caretaker assignment and the escalation ladder |
| What may be waived, deferred, or not cared for at all | Represents the absence of an obligation as faithfully as its presence |

A declaration may be expressed through any accepted mechanism: explicit registration, configuration,
caretaker assignment, consent, household policy, an ownership or relationship record, a care profile,
a maintenance or preservation schedule, a declared environmental requirement, or a default the
household has **explicitly chosen**. A default the household never saw is not a declaration.

### There is no universal hierarchy of importance

**Different households declare different things significant, and the framework is unchanged by
either.** HTBW defines no ranking of people, animals, possessions, spaces, systems, or households, and
none may be introduced.

Specifically, none of the following confers significance:

- A higher price, appraisal, or insured value
- A greater number of associated sensors or devices
- Participation in Identity, or enrolment in any evidence source
- Residency, as against being a guest
- Being registered at all

Significance that was not declared is a **Learned Suggestion**, and a learned suggestion is never an
autonomous policy (**P26**, **DL-21**).

### People are not Assets. Pets are not Assets.

A Person may carry a Stewardship care obligation **without being modelled as property**, and a Pet is
a non-human household member rather than an equipment record. The distinction is held in
[asset.md](asset.md) and [glossary.md](glossary.md), and **no document in this repository models a
person or an animal as an Asset**.

**Stewardship assigns no human worth, ranks no household member, and produces no assessment of a
person beyond the care obligations that person or the household explicitly configured.**

### Stewardship does not begin with an alert

Stewardship begins with a household declaration and a care definition. A reminder, an advisory, a
maintenance task, a corrective action, or an escalation is a **later consequence** of that definition.
**The obligation exists before anything goes wrong, and it still exists afterwards.**

---

## Scope of care

Stewardship covers:

- Assets
- The home
- Rooms and environmental conditions
- People, where appropriate and consented
- Pets
- Vehicles
- Consumables
- Services
- Safety-related conditions (**DL-79**: a care obligation and a truthful, governed Safety
  Communication, never a life-safety responsibility, guaranteed detection, warning, delivery,
  protection, mitigation, or outcome — see [communication.md](communication.md)'s *Non-life-safety
  acknowledgement* section)

---

## Representative obligations

- Maintenance plans
- Service plans
- Service schedules
- Service history
- Maintenance history
- Warranty milestones
- Replacement planning
- Caretaker assignment
- Medication reminders
- Vet appointments
- Pet medication, food, and walk obligations
- Environmental limits that must be protected
- Filter replacement
- Inspection schedules
- Home-maintenance calendar
- Caretaker-calendar projection
- Overdue obligations
- Escalation of unmet obligations
- A garage door that should be secured after a defined time
- Windows that should not remain unlocked under defined conditions

---

## Obligation structure

| Element | Purpose |
|---|---|
| Subject | The asset, room, person, pet, vehicle, service, or home the obligation concerns |
| Statement | What care is required |
| Significance | Why it matters, and how much |
| Schedule or condition | When it becomes due, or the condition that makes it unmet |
| **Condition state** | `met`, `due`, `unmet`, `overdue`, `waived`, `unknown` — *what is true of the world relative to the care expectation* |
| **Lifecycle state** | `raised`, `active`, `deferred`, `closed`, `reopened` — *what has happened to the obligation record itself* |
| Accountability | The caretaker(s) or role accountable — **many-to-many** (**DL-71**; see below) |
| Escalation intent | What should happen if it remains unmet — as *intent*, not as an action |
| Provenance | Where the obligation came from: manufacturer guidance, household decision, regulation, learned suggestion |

### Accountability is many-to-many, and both views are projections (DL-71)

**One Person may be caretaker-of many subjects, and one subject may have many current caretakers.**
This clarifies, rather than adds to, the already-accepted Foundation `caretaker-of` relationship type
(**DL-49**): nothing previously stated a cardinality limit, and household examples such as a pet with
two caretakers or a Person who is caretaker of both a pet and an instrument require it.

**Stewardship owns the current assignment records; there is exactly one governed record set.** A
Person's own view ("Relationships: Caretaker of Maisey, Caretaker of Piano") and a subject's view
("Caretakers: Tom, David") are both **projections** over that same record set — never independently
editable copies. Editing one always means editing the single governed record; the other view reflects
it automatically.

### Completion Mode is explanatory vocabulary, not a new state (DL-71)

Two household patterns are both already expressible through the existing obligation model and
**DL-57**'s Delegated Access Grant, with no new Stewardship architecture:

| Completion Mode | Configuration | Example |
|---|---|---|
| **One Completion Satisfies All** | One obligation names multiple current caretakers, any of whom may hold the **complete** operation of a Delegated Access Grant over the same record | Maisey's monthly medication — Tom completes it; it is Complete for David too |
| **Each Recipient Must Complete** | Multiple independent obligations exist, one per accountable Person, each closed by its own Care Evidence Record | Each Person's flight check-in |

**"Completion Mode" is a label for which of these two shapes was configured — it is never a new stored
state**, and it must never be confused with **Acknowledgement** (**OD-45**, an identified person's
responsive act) or a Communication's own delivery lifecycle (**OD-44**). The existing
**Caretaker-calendar projection** already keeps every caretaker's open list clean under either mode:
it is a live, read-time projection over the governed obligation record(s), so a shared item's closure
is reflected for every caretaker without ever creating a stored per-recipient duplicate that would
need to be cleaned up.

### Condition and lifecycle are orthogonal

Governed by **DL-48**.

**These are two independent fields, and neither is a substitute for the other.** An obligation that is
`deferred` still has a condition — deferring a filter change does not make the filter clean. An
obligation that is `closed` had a condition at the moment it closed, and that condition is part of
what the closure means.

> **Deferral and closure are lifecycle transitions. They are not condition states, and they may never
> be added to the condition set.**

#### `met` means satisfied to date, not completed

**Clarified during the OD-75 formal acceptance review. This states the meaning the model already
carried; it introduces no new value.**

> **A condition state is a statement about the world *right now*, relative to the care expectation.
> It is not a completion flag.**

`met` therefore means **the care expectation is currently satisfied** — nothing is breached, and
nothing is presently required. A filter replaced last month with six months to run is `met`. A piano
tuned in spring is `met` until its cadence comes due. **This reading is forced by the model itself**:
if an obligation with a future due date could not be `met`, every scheduled obligation would sit
permanently `unmet` between completions, `unmet` would lose its meaning, and `overdue` could never be
reached as a distinct escalation.

**`met` is never asserted from absence.** Where a required fact is unknown, the condition is
`unknown`, not `met` — *absence of evidence is never compliance*.

#### Worked progression — a return obligation

The sculpture goes to a museum on 1 January, expected back 15 March.

| Point | Condition | Lifecycle | Why |
|---|---|---|---|
| Custody Period opened, obligation created | `met` | `raised` | The agreement is being honoured and nothing is breached |
| 1 February — running normally | `met` | `active` | Satisfied to date. **The obligation is not "complete"; it is "not breached"** |
| Due window opens, per household policy | `due` | `active` | Attention is now warranted |
| 16 March, no Check-In recorded | `overdue` | `active` | **Custody is unchanged.** The period is still open and the custodian is still the custodian |
| Return date amended to 1 April, with reason | `met` | `active` | A Change Record records the amendment; the old schedule is superseded |
| Check-In recorded with valid evidence | `met` | `closed` | Closed by a **Care Evidence Record** of kind `attested` |
| The custodian stops responding and nothing is known | `unknown` | `active` | Never `met` |
| The household stands the return down for a season | `met` or `unknown` | `deferred` | Deferral is a **lifecycle** transition; the condition is whatever is true |
| The household releases the obligation entirely | `waived` | `closed` | Closed **without asserting that care occurred** |
| The asset goes out again | as applicable | `reopened` | Identity retained, so the pattern stays reportable |

**Read the two columns together.** `met` appears both before the due window and after Check-In, and
the difference between them is carried entirely by the **lifecycle** state and the **Care Evidence
Record**. That is precisely why the two fields had to be separated.

**Every lifecycle transition is a Change Record written at the moment of the transition** — never
derived later by comparing stored payloads (**DL-26**) — carrying the actor, the recorded time, the
effective time where it differs, the reason where one was supplied, and **version-pinned references**
to the care expectation it was evaluated against (**P30**, **DL-27**).

A **reopened** obligation **retains its identity**, so a repeatedly unmet obligation stays reportable
as a pattern rather than appearing as a series of unrelated new obligations.

**Grouping simultaneous obligations is a projection concern** and is not part of this model
(**OD-23**).

### The Care Evidence Record — what closes an obligation

Governed by **DL-48**. It declares its own **Retention Classification** under **DL-47**.

| Evidence kind | Meaning |
|---|---|
| `observed` | **Truth** established that the condition resolved |
| `attested` | A person with accountability recorded that care occurred, **where Truth cannot observe it** |
| `performed` | An executor reported completion **and** Truth or an attestation confirms the outcome |
| `waived` | A household decision closing the obligation **without asserting that care occurred** |

**This answers the question the model previously asked and did not answer.** A *satisfied without
action* obligation carries `observed`; a *performed* one carries `performed`. They are now
distinguishable, and the difference is explainable years later.

**An executor reporting success is not closure** — nor is a dismissed reminder, a ticked projection,
or a requested action. **`unknown` is never `met`**, and **absence of evidence is never compliance**.

---

## The boundary that must not be crossed

> **Stewardship owns the obligation or care responsibility.**
>
> **Stewardship does not automatically own the resulting Communication or physical action.**

Worked separation:

| Responsibility | Statement |
|---|---|
| **Truth** | The garage door is open, and the current time is after 10 PM. |
| **Stewardship** | The home's security-care obligation is unmet. |
| **Operational Trust** | Automatic closing is permitted, prohibited, or requires confirmation. |
| **Concierge** | Close, ask, convey, defer, or escalate — and explain. |

Stewardship never closes the door. Stewardship states that the obligation is unmet.

### The corrective-action lifecycle

**An obligation does not always produce a reminder.** Where the household has authorised it, the
obligation may be resolved by an executor before anyone is told anything — and that is still not
Stewardship acting.

| Step | Owner |
|---|---|
| 1. Authoritative facts are published | **Truth** |
| 2. Those facts are evaluated against household-declared care requirements | **Stewardship** |
| 3. A governed obligation, advisory, or Domain Event is created | **Stewardship** |
| 4. Whether the proposed response is appropriate for this request, in this context | **Operational Trust** |
| 5. What should happen now | **Concierge** |
| 6. The action itself | An **executor** — a Home Assistant automation, script, scene, service call, integration, or a person |
| 7. Why the obligation and the response occurred | **Decision Trace** and Explainability |
| 8. Whether the care condition returned to an acceptable state | **Stewardship**, from Truth |
| 9. The obligation is met, deferred, escalated, or remains open | **Stewardship** |

**Corrective action and Communication are independent paths.** Either, both, or neither may occur, and
each is separately governed — acting is not announcing (**P32**).

**Stewardship never calls a Home Assistant service.** No accepted decision assigns service execution to
Stewardship, and none may be inferred from the fact that an automation resolved an obligation quietly.

### An obligation may be projected, but never surrendered

An obligation may be **projected** onto a native surface — a `todo` entity, a calendar — so that
residents can see and interact with it where they already work. The projection is an interaction
surface, not the obligation.

| Rule | Statement |
|---|---|
| The list does not own the obligation | Stewardship owns it. The projection is derived |
| **Completion is not proof of fulfilment** | Marking an item complete is a list state. It does not establish that the care occurred |
| Significance, accountability, and escalation intent do not transfer | A `todo` item carries none of them |
| **Repairs is not the household obligation model** | A Repairs issue is an administrator-facing configuration surface. See [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md) |

Whether obligations project into calendars, `todo` entities, or a connected store is **OD-23**.

Stewardship may **originate** a Communication about an unmet obligation. It does not decide the
surface, the moment, the wording, or whether the delivery happens at all. **Significance is
referenced by the Communication, never copied into it** (**P30**). See
[communication.md](communication.md).

**Stewardship owns the single escalation ladder** — changing *who* is accountable when an obligation
remains unmet (**OD-22**). Repeating a delivery to the *same* audience is **retry**, is Concierge's,
and is never called escalation. **There is one escalation architecture.**

---

## Delegated Stewardship Authority (DL-57)

Resolves **OD-76**. Full acceptance record is **DL-57** in
[decision-ledger.md](../governance/decision-ledger.md); this section is the canonical model.

### One person may hold Stewardship authority delegated by another

**A care, asset, or pet obligation may be declared, viewed, received, or closed by a person other than
its subject or default accountable party, but only through an explicit, scoped grant — never through
role inference, relationship alone, or administrator status.** This applies uniformly across
Stewardship's existing scope: a Person's care (Eleanor/David), an Asset's conservation (a sculpture
conservator), a Pet's care (a dogsitter), or a household resource (a housekeeper's music ability,
governed by Continuity/Operational Trust rather than Stewardship but following the same grant shape).

> **A relationship or Role is not permission.** `caretaker-of` (Foundation) records **accountability**
> for an obligation or an Asset; it has never granted access over a **Person**, and it still does not.
> A Role such as *caretaker* or *service provider* (see `glossary.md`) names a **position**, consulted
> by Operational Trust; it is never itself the authority that permits an action. **Runtime always
> checks the configured grant, never the descriptive relationship or Role.**

### The Delegated Access Grant

One reusable, explicit construct — not a new responsibility — represents delegated Stewardship
authority:

| Field | Meaning |
|---|---|
| Subject | The Person, Asset, Pet, or obligation the grant concerns |
| Grantee | The Person receiving the authority |
| Operations | The explicit, separately-enumerable actions granted — at minimum: **view**, **receive** (notifications), **declare** (create an obligation), **update**, **schedule**, **complete/close**, **manage** (broader configuration). Reuses **DL-48**'s existing Care Evidence Record kinds (`observed`/`attested`/`performed`/`waived`) for how a grantee's completion is evidenced; invents no new evidence kind |
| Scope | The specific obligation, Asset, Asset group, Pet, or resource the operations apply to — never "everything belonging to this subject" by default |
| Grant basis | Self-declared by the subject, or established by an authorized proxy under the capacity model below |
| Effective and revocation time | When granted, and when (if) it ended |
| Disclosure constraints | Applicable audience/content-sensitivity rules the grant does not override (**DL-34**, **OD-52**, **OD-71**) |

**Operations are never collapsed.** A grantee permitted to *view* an obligation is not thereby
permitted to *close* it; permitted to *receive* a reminder is not thereby permitted to *edit* the
obligation; permitted to *complete* a maintenance obligation is not thereby permitted to change its
recurring schedule. This restates **DL-36**'s prohibition on collapsing distinct operations for the
Stewardship-authority case.

**Access to one grant never implies access to another.** A grant scoped to David's medication
obligations does not extend to David's mailbox, other obligations, or identity evidence. A grant
scoped to a named set of sculptures does not extend to paintings, antiques, or other collections.

**Ownership**: Foundation defines the Delegated Access Grant construct and, where the subject is an
Asset or Pet, continues to own `caretaker-of`/`owner-of` unchanged; **Stewardship owns the grant's
record, its lifecycle, and its application to obligations** (the same pattern **DL-49** already
established for Custody Periods — a time-bounded accountability record Foundation types and
Stewardship operates); **Operational Trust** decides whether a request under a grant may proceed and
governs disclosure; **Concierge** performs delivery and composes the Decision Trace. **No Care,
Caregiver, Guardianship, Delegation, or Authorized Abilities responsibility is created.**

### Non-resident authorized participants

A housekeeper, dogsitter, sculpture conservator, or collections administrator authorized to interact
with the system directly is a **Known Non-Resident Person** (`glossary.md`) — never a second Person
directory, and never an Unknown Person — carrying **only the Delegated Access Grants explicitly
configured for them**. Their own identity evidence (if any is configured — a phone, a BLE tag) remains
attached only to them, never to the resident who arranged their access. No occupational description
(*housekeeper*, *dogsitter*, *conservator*, *collections administrator*) grants anything by itself;
each grant is explicit, scoped, and independently revocable. A conservator authorized for named
sculptures gains no access to paintings, antiques, or unrelated collections without a separate grant; a
dogsitter gains only the explicitly configured pet-care resources, never resident medical information,
personal mailboxes, or unrelated Asset records; a housekeeper granted a music ability gains no
calendar, mailbox, or administrative access. Where a conservator, contractor, or service provider acts
only through a **Service** relationship on the Asset (Foundation) and never interacts with the system
directly, no Person record — resident or non-resident — is created for them at all.

### Capacity

- **A competent adult ordinarily holds self-authority** over their own Stewardship-authored grants.
- **A competent adult may explicitly delegate** a scoped grant to another person (Eleanor to David).
- **A minor, or a person unable to reasonably act independently, may be represented by an authenticated
  administrator acting as proxy** — see `person-and-identity.md`'s Consent (DL-56) section for the
  general self/proxy framework this extends.
- **Administrator status is never itself caregiver, care, or stewardship authority**, and never
  automatically grants disclosure of every person's or resource's Stewardship content. A proxy grant
  is recorded exactly as any other grant — subject, grantee (recorded as acting-as-proxy), scope, and
  basis — and is visible and auditable like any other.
- **Formal legal qualification (guardianship, power of attorney, conservatorship, or equivalent) is
  explicitly outside HTBW's scope.** HTBW records that a proxy grant was established and by whom; it
  makes no claim of legal authority, capacity determination, or legal sufficiency, consistent with the
  existing legal and regulatory non-claim. Where a household's use of proxy authority requires legal
  qualification, that determination is the household's and any applicable legal authority's, never
  HTBW's to verify or assert.

### Identity evidence never transfers with a grant

**A Delegated Access Grant conveys access and action authority; it never conveys identity.** Eleanor's
phone, watch, BLE device, and voiceprint remain identity evidence **only for Eleanor**, regardless of
any grant David holds. A caretaker's own device is never treated as evidence for the cared-for person,
and the cared-for person's evidence is never treated as evidence for the caretaker. Where the subject
cannot provide usable evidence for a class (a non-speaking adult and Voice Identity), that class is
**unavailable**, named under **DL-41** — never manufactured, never substituted from another person's
evidence, and never treated as a reason Stewardship is unavailable for that Person. **Voice Identity is
not required for Stewardship participation.**

### Incomplete obligations are notification, not automatic escalation

An obligation that remains unmet after being scheduled, attempted, or assigned to a grantee **stays
open and reportable** under Stewardship's existing condition/lifecycle model — this is **ordinary
continuing stewardship**, not escalation. **Escalation specifically means changing who is
accountable** (above); a household person being told that a scheduled obligation remains incomplete,
with accountability unchanged, is not escalation and requires no new construct. **OD-22 applies only
where the household has configured an actual change of accountable party**; where no such
configuration exists, the existing obligation-state, reminder, and notification architecture is
sufficient on its own.

### Revocation

A subject with self-authority may revoke a grant at any time; an authorized proxy may revoke where the
capacity model above permits. Revocation is **immediate and prospective**: future access, future
notifications, and future actions requiring the grant end at once; the runtime never infers a
replacement authority. **Existing obligations do not disappear.** They remain Stewardship-owned
governed records; the revoked person can no longer view, manage, receive, or close them absent another
grant; Stewardship reports the resulting accountability or assignment gap exactly as it already reports
an unassigned caretaker (see *Failure behavior*, below); the household may reassign. **Historical
actions remain attributed to the actor and grant valid at the time** — revocation never rewrites that
history, and a Care Evidence Record produced under a since-revoked grant is unaffected.

### Explainability

A Decision Trace produced under this section states, in addition to its existing required fields:
whether the acting person was the **subject**, an **authorized proxy**, or a **grantee**; the specific
grant or authority applied, including its scope and operations; whether the current identity assertion
met the applicable requirement; the audience present and what was disclosed or withheld; and, where
relevant, that a grant was later revoked and what happened to the obligations it covered. The trace
makes *"Eleanor agreed to this"* provably distinct from *"David configured this for Eleanor as proxy"*
and from *"a grant existed but did not cover this operation."*

---

## Significance

Significance is what makes Stewardship more than a task list. It expresses **why something matters**
and how strongly, so that Concierge can prioritise and Operational Trust can classify risk.

Significance is represented as a **Significance Declaration (DL-75)** — a structured combination of
four independently addressable fields, never a single combined text value, a numeric score, or a
probability:

| Field | Answers | Statement |
|---|---|---|
| **Derivation Source** | *Why does this matter?* | Mandatory. Value, Safety, Health, Security, Preservation, Cost of Deferral, or Household Declaration |
| **Base Significance** | *How much does this matter, under its accepted declaration?* | **Routine < Important < Significant < Critical** |
| **Provenance** | *Who declared it, and from what origin?* | Household decision, manufacturer guidance, regulation, or an accepted recommendation |
| **Effective Version** | *Which declaration was in force when?* | Versioned; prior declarations are never rewritten |

A household-facing explanation may use natural language — *"the piano matters more than the shades"* —
but the canonical model retains these four fields underneath it.

### Derivation Source is independent of Base Significance

The same Derivation Source may later coexist with a different Base Significance if the household
changes its declaration, or if another governed, accepted declaration replaces it. A routine-maintenance
obligation and a health obligation may each independently carry any Base Significance level; nothing
pairs a Derivation Source with a fixed Base Significance.

### Base Significance is importance language, never confidence language

`Routine`, `Important`, `Significant`, and `Critical` express **household-declared importance only**.
They never express confidence, probability, truth, identity, accuracy, evidence quality, risk, urgency,
issue severity, or confirmation strength. **No conversion is ever made** between Base Significance and
**DL-39** Identity Confidence, **DL-58** Truth Confidence, **DL-73** Behaviour Source Confidence,
**DL-74**'s Unknown Actor hypothesis vocabulary, Operational Trust's risk classification or confirmation
requirements, Home Assistant's `IssueSeverity`/Repairs severity, or **OD-22**'s escalation ladder.
Critical Significance never implies High Risk or Very High Truth Confidence; Routine Significance never
implies Low Urgency; Important Significance never auto-sets a confirmation requirement; High Identity
Confidence never raises Significance.

### Base Significance is comparable across every Stewardship subject

A Critical pet-health obligation, a Critical piano-preservation obligation, and a Critical safety
obligation all use the same household-wide Significance meaning — comparable across Person, Pet, Asset,
Device, Room, Home, Care Definition, and Obligation, so Concierge and Operational Trust can consume one
consistent ordered representation.

**Equal Base Significance does not mean equal action, equal risk, or a silently resolved conflict.**
Equal Base Significance never erases the Derivation Source, and never by itself authorises automatic
prioritisation without the applicable governing policy. Where the rare-book collection and the piano
want incompatible humidity, **both obligations are surfaced with their significance, and the conflict is
never silently resolved** (`stewardship-obligations.md` Scenario 6).

Significance is a Stewardship judgement **about a household declaration**, recorded with provenance.
It is **not** a Truth fact and **not** an Operational Trust policy, and it is **not an independent
Stewardship opinion about what the household ought to value**. Where the provenance is manufacturer
guidance, regulation, or a learned suggestion, that origin is recorded and remains visible; a learned
origin never becomes an autonomous policy without acceptance by a person with authority (**P26**,
**DL-21**).

### Recommendations never become policy automatically

A **Research-Based Recommendation** is informed by external knowledge relevant to a specific subject or
obligation — manufacturer guidance, veterinary or conservation guidance, professional standards, or
LLM-assisted research grounded in cited sources. An **Observed-Household Recommendation** is based on
governed observations of household behaviour. Both are non-authoritative **Suggestion**-stage proposals
under the existing learning promotion ladder (**P26**, **DL-21**,
[../architecture/behavioral-governance.md](../architecture/behavioral-governance.md)) — distinguished
from each other by the evidence they carry, not by a separate acceptance mechanism. Each may propose a
Derivation Source and/or a Base Significance. **LLM output alone is not household authority. Observed
behaviour alone is not household intent.** Neither recommendation type ever becomes policy
automatically.

Both recommendation types require an explicit household disposition — **Accept**, **Accept with
modification**, **Reject**, or **Defer** — recorded as a governed Change Record under the same
promotion-ladder discipline (**OD-28**). Only Accept or Accept-with-modification creates or modifies the
Significance Declaration. The acceptance record preserves the recommendation type, its provenance, the
proposed and accepted Derivation Source and Base Significance, the household decision maker, the
decision timestamp, and any modification rationale. **The research or reasoning provider is never
recorded as having made the household declaration.**

How significance is expressed was **OD-21**, resolved as **DL-75**.

---

## Cooperation with the asset model

The asset model says *the piano requires 40–60% relative humidity*, because that is a property of the
thing.

Stewardship says *the piano's preservation obligation is unmet*, because that is a judgement about
care.

Truth says *the Music Room is at 31%*, because that is what is true now.

See [asset.md](asset.md).

### "Room health" is not an HTBW term

A Room's condition decomposes into two owned things and nothing else:

| Statement | Owner |
|---|---|
| The Music Room is at 31% relative humidity, Truth Confidence Band: High | **Truth** |
| The piano's preservation obligation is unmet | **Stewardship** |

**HTBW defines no "room health" state model and no "asset health" state model**, and neither may be
invented (**OD-69**). *Room health* appears only in pre-refoundation and historical illustration
documents and is **obsolete**. Where a household-facing summary is desired, it is a **projection** over
Truth Facts and Stewardship obligation states with those fields kept separate and separately
explainable — never a new determination, and never a second authority. **This prohibition names Room
Confidence and People Health explicitly as the same rejected shape** (**DL-60**, **DL-61**,
`glossary.md`); a conflict was found — not fixed — where current Concierge implementation evidence
offers both as selectable household-facing output labels, tracked as implementation-remediation
evidence on **OD-69**, resolved as **DL-61**.

**A provider-qualified Environmental Indicator is not "room health" (DL-62 clarification).** A
household may display a selected provider's own indicator — for example *"air-Q Health Index:
99.9%"* or *"air-Q Performance Index: 81.7%"* — as a **Provider-Derived Environmental Indicator**
(`truth.md`, `room-configuration.md`). This is a true statement about what the provider currently
reports, and it is displayed with its provider-qualified name intact. **It is never renamed "Room
Health," never presented as a Person's health or performance, and it never overrides a subject-specific
Environmental Requirement evaluation.** Abigail's declared humidity requirement is evaluated against
current Room Environment Facts independently of any provider index; a favorable provider index never
proves her requirement is met, and an unfavorable one never diagnoses her or proves the Room is
medically unsafe. Both statements may be shown together, separately attributed, never merged into one
Room score.

### Person Environmental Requirements (DL-61)

Resolves the remainder of **OD-69**. Full acceptance record is **DL-61** in
[decision-ledger.md](../governance/decision-ledger.md); this section is the canonical model.

**A Person may declare Environmental Requirements, reusing the Asset environmental-limit pattern
exactly — without becoming an Asset.** Stewardship's scope of care already includes *"people, where
appropriate and consented"* (above); this section formalizes the previously-flagged architectural
expectation in the Aging-Parent Support use case (`stewardship-use-cases.md`) into accepted
architecture, requiring no new responsibility and no new authority model.

| Question | Owner |
|---|---|
| What does this Person require, as a declared property? | **Foundation**, through Person Setup, exactly as an Asset's environmental limits are Foundation's |
| What is the current Room Environment? | **Truth**, as **DL-60** Environmental Purpose Facts |
| Where is the Person now? | **Truth**, as a Contextual Person-Presence Fact (**DL-38**, **DL-59**) |
| Does the current Room Environment satisfy the Person's requirement? | **Stewardship** |
| May this be disclosed, and to whom? | **Operational Trust** |
| What should be said, and how? | **Concierge** |

A Person Environmental Requirement carries: the applicable **Environmental Purpose** (**DL-60**); a
minimum, maximum, or acceptable range; **significance**, with provenance; **self- or proxy-declared
basis** (**DL-56**, **DL-57** — an authenticated administrator may facilitate a requirement for a minor
or a dependent Person exactly as any other proxy-established Stewardship content, asserting no legal or
medical sufficiency); consent state; effective period; and withdrawal history. **This is the smallest
shape that supports the accepted use cases — no field is added beyond what the Asset pattern already
required.**

#### Preference, Requirement, and medical threshold are three distinct kinds

| Kind | Effect | Owner |
|---|---|---|
| **Preference** | May guide Continuity personalization or produce an Advisory | Continuity, Stewardship |
| **Requirement** | Drives a Stewardship obligation evaluation | Stewardship |
| **Medical or clinical threshold** | **HTBW invents and validates none.** A requirement's value is a household or person declaration, never a clinical determination | — |

**A Requirement is never a diagnosis.** Stewardship states that a declared range was or was not met by
a current Fact — never that a condition exists, was caused, or requires clinical attention.

#### Location-bounded evaluation

**A Person's Environmental Requirement is evaluated against current Room Environment Facts only while
a valid Contextual Person-Presence Fact places that Person in the Room** (**DL-59**). Where the
Person's location is unknown, **no current suitability claim is made**, and the prior Room is never
substituted as current. Where a required Environmental Purpose has no valid current Fact for that
Room, the requirement evaluates to **`unknown`** — never assumed met, and never assumed unmet.

#### Every subject is evaluated independently

**A Room may contain People, Pets, and Assets simultaneously, each carrying its own applicable
requirements — Stewardship evaluates every subject independently.** One subject's requirement being met
has no bearing on another's; requirements are never averaged, never ranked, and a Room is never assigned
one universal verdict. Where two subjects' requirements conflict (one wants higher humidity than
another tolerates), **the conflict is surfaced, never silently resolved** — corrective-action choice
remains Operational Trust's and the household's, exactly as any other Stewardship conflict. **This is a
Stewardship conflict, never a Truth conflict** (`truth.md`, *Genuine Truth Conflict*, **DL-63**): Truth
publishes exactly one current Room Fact; Stewardship maintains the independent per-subject evaluations
against it.

### Environmental Coverage, Configuration Completeness, and Truth Confidence stay separate (DL-61)

Three measures answer three different questions and are **never collapsed, renamed into one another, or
averaged**:

| Measure | Question | Owner |
|---|---|---|
| **Configuration Completeness** | Of the Environmental Purposes the household selected as *applicable* to a Room, how many currently have a configured source? | **Room Configuration** |
| **Environmental Coverage** | Of the purposes that *are* configured, how many currently have a valid, available Fact? | A projection over Truth's per-Fact validity (**DL-59**) |
| **Truth Confidence** | How strongly is one particular Fact supported? | **Truth**, per Fact (**DL-58**) |

**An unconfigured but inapplicable purpose never counts against either measure.** A Room with no UV
requirement is not "incomplete" for lacking a UV sensor, and a Room with no configured Mold Index source
is not thereby unhealthy — **missing configuration is not an environmental failure, and unavailable
current data is not missing configuration.**

### Room Environmental Status is a projection, never an authority (DL-61)

A household-facing **Room Environmental Status** may summarize current per-subject Stewardship
evaluations for a Room's applicable Persons, Pets, and Assets. It is **never a Truth Fact, never a
probability, never a medical or clinical status, and never a replacement for an individual requirement
evaluation.** Any presentation color is presentation only — the underlying projection state is defined
independently, and every projected state must drill through to its subject, Environmental Purpose,
current Fact, requirement, evaluation, significance, provenance, Truth Confidence, and validity. A
projection summarizing "no known unmet applicable requirements," "one or more requirements unmet,"
"evaluation inputs unavailable," "conflicting subject requirements," or "no applicable requirements
currently configured" is acceptable; a single green/amber/red health verdict that suppresses which
subject or requirement produced it is not.

**HTBW asserts no diagnosis, clinical advice, wellness score, medical claim, or life-safety guarantee at
any point in this model.** Stewardship may recognise, evaluate, and care for safety-related conditions
and obligations without that recognition ever becoming a life-safety responsibility — reconciled in
full as **DL-79**: Stewardship owns the obligation and its significance; **Operational Trust** grants
Urgency (**DL-77**) and determines appropriateness; **Concierge** coordinates delivery; a certified
life-safety or protective device remains authoritative for its own domain throughout.

---

## Consumes

- Foundation asset model, Person, Pet, Room, Service, and Relationship definitions
- Truth facts (environmental, device, room-state, time)
- Schedules, service records, warranty terms
- The Foundation caretaker-of relationship type, through which Stewardship records the caretaker
  assignments it owns
- Household-declared significance

## Provides

- Obligations and their current state
- Significance judgements with provenance
- Accountability (who is responsible)
- Escalation intent for unmet obligations
- Caretaker-calendar projections
- Maintenance and service history

## Explicit non-responsibilities

Stewardship does **not**:

- Decide, on the household's behalf, that something matters
- Establish current conditions (Truth)
- Decide what is permitted (Operational Trust)
- Send notifications (Concierge)
- Perform physical actions (Concierge)
- Store personal preferences or sessions (Continuity)
- Own the authoritative asset record (Foundation asset model)

---

## Failure behavior

| Condition | Behavior |
|---|---|
| A required fact is unknown | Obligation state is `unknown`, not `met`. Absence of evidence is never compliance. |
| A schedule source is unavailable | Report the source as unavailable; do not silently mark obligations met |
| A caretaker is unassigned | Report an accountability gap; escalate to household authority per policy |
| Conflicting obligations (two assets need incompatible conditions) | Surface the conflict; do not silently prefer one. Concierge and the household resolve it. |
| An obligation is repeatedly unmet | Escalation intent increases per policy; the pattern itself becomes reportable |

## Privacy considerations

Obligations may reveal health conditions, medication, absence patterns, pet care, and asset value.
Stewardship visibility is policy-gated by content class, not uniformly visible within the household.
See [../architecture/privacy.md](../architecture/privacy.md).

## Explainability requirements

Every obligation that influenced a decision appears in the Decision Trace with its state, its
significance, and the fact that made it unmet. An escalation must explain what is unmet, since when,
and who is accountable.

---

## Custody

Governed by **DL-49**.

> **Custody answers: who is accountable for this, for how long, and under what agreement?**

**Custody is not ownership, not caretaking, and not location.** A household may own a sculpture that a
museum has custody of; a household may have custody of a painting another collector owns.

### The Custody Period

A **Custody Period** is a **time-bounded accountability record**. Foundation defines the object type;
**Stewardship owns the record, its lifecycle, and its history** — because a custody period must
consume Truth and must produce obligations, and
[../architecture/dependency-view.md](../architecture/dependency-view.md) rule 6 forbids Foundation
from consuming anything.

| Element | Purpose |
|---|---|
| Subject | The Asset the period concerns |
| Custodian | Who is accountable. A **governed reference** to an existing Foundation object, **or free text**, preserved verbatim with the actor who recorded it |
| Declared custody location | Where it is expected to be during the period. **Not a Truth Fact** |
| Agreement reference | The loan agreement or contract, as a governed reference to an Asset document |
| Insurance responsibility | Who bears it **for this period** |
| Begin time | When accountability transferred |
| Expected end time | When it is expected back, where agreed |
| Actual end time | Recorded on closure, never before |
| Purpose, notes | Why, and anything else the household recorded |

**No new Foundation relationship type is created.** `owner-of` and `caretaker-of` are **durable**
relationships; custody is **episodic**, and episodic accountability belongs on a time-bounded record
rather than in a standing relationship set. Whether a role-bearing construct later supersedes this is
**OD-77**, which **DL-49** neither expands nor resolves.

### Opening and closing

**A Custody Period opens on a recorded Check-Out and closes only on a recorded Check-In.**

> **Physical return is evidence toward closure. It is not closure.**

Truth can establish **where something is**. Truth cannot establish that **an accountability period has
been accounted for** — that requires the household to record the return, its date, its condition, and
its evidence. The Check-In is a **Care Evidence Record** of kind `attested` (**DL-48**).

### What a custody transfer changes, and what it does not

| Changes | Does **not** change |
|---|---|
| The accountable party | Ownership |
| The declared custody location context | The Asset's declared `located-in` home |
| Insurance responsibility for the period | The Asset's **observed** current location (**Truth**) |
| — | The Asset's significance |

### HTBW does not adopt a fixed custody-status enumeration

**Corrected during the OD-75 formal acceptance review.** The earlier wording — *"there is no custody
state machine"* — was imprecise. A Custody Period **does** have a governed lifecycle. What HTBW
declines to adopt is the **legacy fixed custody-status enumeration** as canonical.

#### The governed Custody Period lifecycle

| Lifecycle state | Meaning |
|---|---|
| `opened` | A Check-Out was recorded; accountability transferred |
| `updated` | An amendment was recorded — expected end time, custodian, declared custody location, insurance responsibility, agreement reference, or notes |
| `closed` | A Check-In was recorded, with its Care Evidence Record |
| `corrected` | A recording error was fixed. **The prior value is never overwritten**; the correction is a new Change Record |
| `adversely_resolved` | The period ended without a return — loss, theft, or destruction — with a recorded disposition |

**Every transition is a Change Record written at the moment of the transition** (**DL-26**), and the
history is retained under **DL-47**.

#### Why the legacy enumeration was not adopted

| Legacy status | Represented instead as |
|---|---|
| *In transit* | A Custody Period whose **custodian is the carrier** |
| *In storage* | A Custody Period whose **custodian is the storage provider** |
| *On loan out* | An open Custody Period where the household holds `owner-of` and another party is custodian |
| *Loaned in* | An open Custody Period where the household is custodian and another party owns |
| *Owned on site* | **See below — this is not a custody statement** |
| *Overdue* | **Not custody.** The return obligation's condition state |
| *Lost*, *Stolen* | **Not custody.** See *Loss and theft* below |

#### Absence of an open Custody Period is not a location claim

> **The absence of an open Custody Period means only that no non-default custodian is currently
> recorded.** It says nothing whatever about where the asset is.

**On-site status is never inferred from ownership, and never from the absence of a custody record.**
It requires either a **Truth** Location Fact, or Foundation's declared `located-in` — and those two
are themselves distinct: *"Declared location is not current location"*
([../contracts/foundation-contract.md](../contracts/foundation-contract.md)).

| Question | Answered by |
|---|---|
| Who owns it? | Foundation `owner-of` |
| Who is accountable for it right now? | The open Custody Period, or the household by default |
| Where does it belong? | Foundation `located-in` — a **declaration** |
| Where is it **now**? | **Truth**, as a Location Fact — or `unknown` |
| Where is it **expected** to be during this custody period? | The Custody Period's declared custody location — **a declaration, not a Fact** |

**Nothing in the custody model may be read as establishing current physical location.**

#### Household-chosen fidelity

A household may record **only the primary accountable custodian**, **every logistics handoff**, or any
practical level between. Recording every shipping leg means a Custody Period per leg; recording none
means the primary institution remains accountable throughout, **on the household's behalf**.

> **Missing intermediate legs are valid unrecorded detail, not an error. The home must never fabricate
> them.**

An unrecorded leg is simply absent from the chain. It is **never** inferred, interpolated, or
presented as though it had been recorded.

### Expected return creates an obligation

An expected end time causes Stewardship to raise a **care obligation whose subject is the Custody
Period**. Its condition state moves `met` → `due` → `overdue` on the ordinary rules. **Custody itself
is unchanged by the date passing**: the custodian is still the custodian and the period is still open.

**Reminder lead time and cadence are household policy, not architecture.** Stewardship originates the
Communication; **Operational Trust** governs entitlement, interruption, and audience; **Concierge**
decides whether, when, and how to deliver it. Acknowledgement, snooze, suppression, and
duplicate-prevention semantics remain **OD-45**, **OD-51**, and **OD-54**.

### The custodian designation

**Free text is accepted**, and no first-class Counterparty object is created.

| Rule | Statement |
|---|---|
| No new object | **No Counterparty, organisation, or institution object exists**, and none is created by recording a custody period |
| A known Person may be referenced | Where the custodian **is** an existing Foundation object — a Person, or a Service — the record may carry a **governed reference** to it instead of free text |
| Free text is preserved | The text the household recorded is **preserved verbatim in history**, with the actor who recorded it and the effective time |
| Corrections are Change Records | Correcting a custodian designation creates a `corrected` Change Record. **The prior text is never overwritten** |
| No inference | An unrecorded chain leg is **never** inferred from the presence of a later one |

Whether a role-bearing relationship construct later supersedes the free-text designation is **OD-77**,
which this model neither expands nor resolves.

### Insurance responsibility

**Clarified during the OD-75 formal acceptance review.** *Insurance responsibility* was carried as a
single field and is genuinely several distinct things, which claims and disputes depend on separating.

| Element | What it means | Owner |
|---|---|---|
| **Insurer** | The carrier or underwriter | **Not an HTBW object.** Recorded on the policy artifact, which is an Asset document |
| **Insured party** | Who the policy names as insured | The policy artifact |
| **Responsible for maintaining coverage** | Who must ensure a policy is in force **for this custody period** | **The Custody Period** |
| **Accountable for a claim** | Who files and pursues a claim if something happens | **The Custody Period**, defaulting to the party responsible for coverage where not separately stated |
| **Governing agreement** | The loan agreement or contract setting these terms | An **Asset document**, referenced by version-pinned governed reference |
| **Ownership** | Who owns the thing | Foundation `owner-of` — **independent of all of the above** |
| **Custody** | Who is accountable for it now | The Custody Period — **independent of who insures it** |

> **All four insurance elements are period-scoped.** They describe an arrangement for *this* custody
> period and are answered historically from that period's Change Records — not from the asset's
> current state.

**The Custody Period references the agreement; it never copies it.** Policy numbers, terms, schedules,
and correspondence live in the artifact under the Asset as governing parent (**DL-45**), reached by
**version-pinned governed reference** (**DL-27**, **P30**).

### Loss and theft

**Lost and stolen are neither custody states nor custodians, and neither collapses into `unknown`.**

> **Nothing is ever recorded as being "in the custody of" *lost* or *stolen*. There is no such
> custodian.**

| Element | Record type | Owner |
|---|---|---|
| *Where is it now?* → `unknown` | **Truth** Location Fact | **Truth** |
| The Custody Period ends `adversely_resolved`, with a recorded disposition of `lost`, `stolen`, or `destroyed` | Custody Period **Change Record** | **Stewardship** |
| **Last known custodian** | **Preserved unchanged** on the closed period — it is the whole point of the record | **Stewardship** |
| The resulting obligations — report, claim, recover | **Obligations** | **Stewardship** |
| Police report, claim correspondence, adjuster findings | **Asset documents** | Foundation / Connected Storage |
| **Preservation Hold** over the custody chain and its evidence | Hold | **Operational Trust** |
| *It was stolen* | A **household declaration recorded with provenance**. **Never inferred** from absence | The household |

**Effect on the return obligation.** An adverse resolution **does not satisfy** the expected-return
obligation. The obligation moves to lifecycle `closed` **only** with a Care Evidence Record — and its
kind is **`waived`**, because the household released the expectation, **never `observed` or
`performed`**, because the asset did not come back. Where recovery is still being pursued, the
household may instead leave it `active` with condition `unknown`.

**If the asset is later recovered**, the household records a **new Custody Period** returning
accountability, and a Check-In closes it with its condition evidence. **The adversely resolved period
is not reopened or rewritten** — the loss genuinely happened, and the history says so. A `reopened`
return obligation retains its identity.

**Retirement and deletion.** An adversely resolved asset may eventually be retired, but **retirement
never erases custody history, agreements, condition evidence, or claim artifacts that are under a
Preservation Hold or within a retention floor**. Parent removal follows **DL-45**; final deletion
eligibility follows **DL-47**, and the reconciliation of deletion against preservation remains
**OD-36**.

### Reminders are household policy

An expected end time causes Stewardship to raise a **care obligation whose subject is the Custody
Period**. **Stewardship originates the Communication; Operational Trust governs entitlement,
interruption, and audience; Concierge decides whether, when, and how to deliver it.**

> **Supported household-policy example, not a canonical cadence:** remind the accountable participant
> **one or two days before** the expected return, and **daily after** it passes, until either the
> expected return is updated or Check-In is recorded.

**Nothing in that example is a canonical constant.** Lead time, cadence, quiet hours, and the choice
of recipient are **household policy** held by Operational Trust.

**Updating the expected return supersedes the schedule.** Amending the date creates an `updated`
Change Record carrying the before value, the after value, the actor, the recorded time, and the reason
where supplied. **The previous reminder schedule is superseded, not silently abandoned**, and the
obligation's condition is re-evaluated against the new date. Acknowledgement, snooze, suppression, and
duplicate prevention remain **OD-45**, **OD-51**, and **OD-54**.

### What a dashboard may project

A household-facing surface may usefully distinguish **off site within the expected period** from **off
site beyond the expected return**.

> **Colour choices such as blue and purple are presentation examples. They are not Facts, not risk
> states, not custody states, and not universal colours.**

The governed inputs a projection may read:

| Input | Owner |
|---|---|
| Whether an open Custody Period exists, and who the custodian is | **Stewardship** |
| The expected end time, and whether it has passed | **Stewardship** |
| The return obligation's **condition** and **lifecycle** states | **Stewardship** |
| Whether environmental observation is **available** for the asset at all | **Truth** / **DL-41** |
| Current Facts, where Truth can establish them | **Truth** |
| What this audience may be shown, and in what form | **Operational Trust** |
| Accessibility and presentation requirements | Presentation policy |

**The projection presents these fields separately and never merges them into a single verdict**, and
the projection surface itself remains **OD-23**.

### Evidence belongs to the Asset

**Condition photographs, appraisals, conservator and repair reports, contracts, and insurance material
are Asset documents under the Asset as governing parent** (**DL-45**). The custody record **references
them by version-pinned governed reference and never copies them** (**DL-27**, **P30**).

**Custody supplies the reason and the relationship. The Asset document model owns the artifact.**

Repair does not close custody: a custodian who arranges and pays for a repair **retains custody until
the asset is returned and checked in**.

---

## Stewardship history

**Stewardship owns the history of its own records.** Foundation defines the shared temporal model;
see [temporal-record.md](temporal-record.md).

History is owned for:

- Obligation history — condition changes, and the lifecycle transitions `raised`, `active`,
  `deferred`, `closed`, `reopened` (**DL-48**)
- **Custody history** — Custody Periods, their amendments, and their closures (**DL-49**)
- Care Evidence Records
- Maintenance history
- Service history
- Significance history
- Caretaker-assignment history

> **Resolved by DL-48.** *Deferred* and *closed* are **lifecycle** transitions, not condition states.
> The condition states remain `met`, `due`, `unmet`, `overdue`, `waived`, and `unknown`; the lifecycle
> states are `raised`, `active`, `deferred`, `closed`, and `reopened`; and **what constitutes accepted
> evidence that care occurred is the Care Evidence Record**. **An obligation is still never closed by a
> dismissed reminder, a ticked projection, a requested action, or an executor reporting success.**

These are the histories longest-lived in the household, and the ones most often asked about years
later: *when was this last serviced, who was accountable, and what changed?*

### Change Records, not embedded audit trails

Stewardship history is recorded as **independently addressable, independently retainable,
version-anchored Change Records** — not as an audit array embedded inside the mutable Asset or
obligation record.

This is the direct lesson of the Asset Intelligence reference implementation. Where history lives as
a field on the live object, it cannot be retained, redacted, exported, or placed on hold
independently, and it is destroyed with the object. See
[../architecture/adr-temporal-record-model.md](../architecture/adr-temporal-record-model.md).

**Silent truncation is prohibited.** Where history is truncated or purged, a **Tombstone** remains, so
that *"records were removed"* never becomes indistinguishable from *"nothing happened"*.

### Compacting large collection changes

Where a change affects a large collection and a compact representation remains adequate for
explanation, a Change Record may record counts and deltas rather than copying the complete
collection. This preserves a useful pattern proven in the reference implementation.

---

## Representative scenarios

- [../scenarios/stewardship-obligations.md](../scenarios/stewardship-obligations.md)
- [../scenarios/stewardship-use-cases.md](../scenarios/stewardship-use-cases.md) — the eight canonical
  Stewardship use cases and their acceptance scenarios

## Open decisions

| ID | Question |
|---|---|
| OD-21 | **Resolved as DL-75.** Significance is a structured Significance Declaration — Derivation Source, Base Significance (Routine < Important < Significant < Critical), Provenance, Effective Version. Research-Based and Observed-Household Recommendations are separately defined, non-authoritative Suggestion-stage proposals under the existing P26/DL-21 promotion ladder |
| OD-22 | Escalation ladder semantics and defaults |
| OD-23 | Whether obligations project into Home Assistant calendars, `todo` entities, or a connected store |
| OD-75 | **Resolved as DL-48 and DL-49.** Condition and lifecycle are orthogonal; deferral and closure are lifecycle transitions carried by Change Records; the **Care Evidence Record** defines accepted evidence that care occurred; custody is a Stewardship-owned **Custody Period**. Grouping remains a projection concern (**OD-23**) |
| OD-76 | **Resolved as DL-57.** Delegated Stewardship authority — the Delegated Access Grant, self/proxy/capacity model, non-resident authorized participants, revocation, and the OD-22 escalation boundary are accepted |
| OD-69 | **Resolved as DL-61.** Asset-derived Entity projection reuses existing owned vocabularies; Person Environmental Requirements reuse the Asset environmental-limit pattern; Environmental Coverage, Configuration Completeness, and Truth Confidence are kept separate; Room Environmental Status is a non-authoritative projection; Room Health, Room Confidence, and People Health are formally rejected |
| OD-33 | **Closed — DL-43, DL-46, DL-47.** Retention is declared inside every governed record and artifact lifecycle |
| OD-34 | **Closed — DL-42, DL-44, DL-46, DL-47.** The temporal-persistence model is complete; the representation mechanism is **OD-01** |

## Related documents

- [asset.md](asset.md)
- [truth.md](truth.md)
- [operational-trust.md](operational-trust.md)
- [temporal-record.md](temporal-record.md)
- [../contracts/stewardship-contract.md](../contracts/stewardship-contract.md)
