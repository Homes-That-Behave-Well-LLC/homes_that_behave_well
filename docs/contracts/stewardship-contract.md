# Stewardship Contract

> **Document status: Canonical contract.**
> Responsibility: **Stewardship**. Model: [../models/stewardship.md](../models/stewardship.md).

---

## Owning responsibility

**Stewardship — what matters, and what must be cared for?**

**Stewardship must not be reduced to a synonym for inventory.** It is the responsibility for
significance, care, obligations, lifecycle accountability, and ongoing responsibility.

Asset Intelligence as a platform layer answering *what matters* is superseded: the descriptive asset
record belongs to Foundation, and significance and care belong here.

---

## Household authority

> **The household declares what matters. Stewardship represents that declaration as care
> expectations, evaluates authoritative observations against them, and creates governed care
> obligations when attention is required.**

Stewardship answers *what matters* **for** the household, from what the household has declared. It
does not answer it **about** the household. This is the same boundary already accepted for Operational
Trust — *the framework provides governance; the household provides the values* (**DL-36**, **P26**).

A declaration may be expressed through explicit registration, configuration, caretaker assignment,
consent, household policy, an ownership or relationship record, a care profile, a maintenance or
preservation schedule, a declared environmental requirement, or a default the household **explicitly
chose**.

**No universal HTBW hierarchy of importance exists.** Price, appraisal, sensor count, Identity
participation, residency, and registration confer no significance. Significance that was not declared
is a **Learned Suggestion**, never an autonomous policy (**P26**, **DL-21**).

**People are not Assets. Pets are not Assets.** A Person may carry a care obligation without being
modelled as property. **Stewardship assigns no human worth and ranks no household member.**

**Stewardship does not begin with an alert.** It begins with a declaration and a care definition; a
reminder, advisory, maintenance task, corrective action, or escalation is a later consequence.

---

## What Stewardship guarantees

- Obligations with subject, statement, significance, schedule or condition, state, accountability,
  escalation intent, and provenance
- Obligation **condition** states: `met`, `due`, `unmet`, `overdue`, `waived`, `unknown`
- Obligation **lifecycle** states: `raised`, `active`, `deferred`, `closed`, `reopened` (**DL-48**)
- **Condition and lifecycle are orthogonal.** Deferral and closure are lifecycle transitions and are
  **never** condition states
- A **Care Evidence Record** is what closes an obligation, carrying exactly one evidence kind —
  `observed`, `attested`, `performed`, or `waived` — and declaring its own Retention Classification
  (**DL-47**)
- **Custody Periods** — who is accountable for a subject, for a bounded time, under what agreement,
  with whose insurance responsibility (**DL-49**)
- A Custody Period lifecycle of `opened`, `updated`, `closed`, `corrected`, `adversely_resolved`
- **`met` means satisfied to date, not completed.** A condition state describes the world now, not a
  completion; `met` is never asserted from absence
- A **Significance Declaration (DL-75)** — Derivation Source, Base Significance (`Routine` < `Important`
  < `Significant` < `Critical`), Provenance, and Effective Version, each independently addressable, with
  provenance
- Accountability — who is responsible
- **Caretaker assignment**, recorded through the Foundation caretaker-of relationship type. Foundation
  defines the relationship; Stewardship owns the assignment. **The relationship records
  accountability; it is never itself access authority** — access to a Person, Asset, or Pet's
  Stewardship content requires an explicit **Delegated Access Grant** (**DL-57**)
- **`caretaker-of` is many-to-many** (**DL-71**): one Person may be caretaker of many subjects, and
  one subject may have many current caretakers. The Person view and the subject view are both
  **projections** over Stewardship's single assignment record set, never independently editable
  copies
- **Completion Mode** — One Completion Satisfies All (one obligation, multiple caretakers, any may
  close it) or Each Recipient Must Complete (multiple independent obligations, one per Person) — is
  explanatory vocabulary for an existing configuration, never a new stored state (**DL-71**)
- Caretaker-calendar projections
- Maintenance and service history

Scope of care: assets, the home, rooms and environmental conditions, people where consented, pets,
vehicles, consumables, services, and safety-related conditions.

---

## The boundary that must not be crossed

> **Stewardship owns the obligation or care responsibility.**
> **Stewardship does not automatically own the resulting Communication or physical action.**

| Responsibility | Statement |
|---|---|
| Truth | The garage door is open, and the time is after 10 PM |
| **Stewardship** | The home's security-care obligation is unmet |
| Operational Trust | Automatic closing is permitted, prohibited, or requires confirmation |
| Concierge | Close, ask, convey, defer, or escalate — and explain |

Stewardship never closes the door.

### The corrective-action lifecycle

**An obligation does not always produce a reminder.** Where the household has authorised it, an
executor may resolve the condition before anyone is told anything — and that is still not Stewardship
acting.

| Step | Owner |
|---|---|
| Authoritative facts | **Truth** |
| Evaluation against household-declared care requirements | **Stewardship** |
| Governed obligation, advisory, or Domain Event | **Stewardship** |
| Whether the proposed response is appropriate for this request, in this context | **Operational Trust** |
| What should happen now | **Concierge** |
| The action itself | An **executor** — a Home Assistant automation, script, scene, service call, integration, or a person |
| Why it happened | **Decision Trace** and Explainability |
| Whether the condition returned to an acceptable state | **Stewardship**, from Truth |
| Met, deferred, escalated, or still open | **Stewardship** |

**Corrective action and Communication are independent paths.** Either, both, or neither may occur
(**P32**).

**Stewardship never calls a Home Assistant service.** No accepted decision assigns service execution
to Stewardship.

Stewardship may **originate** a Communication about an unmet obligation. It does not select the
surface, the moment, the wording, or whether delivery happens at all. **Significance is referenced by
the Communication, never copied into it.** See [../models/communication.md](../models/communication.md).

**Stewardship owns the single escalation ladder** — changing *who* is accountable (**OD-22**).
Repeating a delivery to the *same* audience is **retry**, is Concierge's, and is never called
escalation.

---

## Cooperation with the asset model

They are not collapsed.

| Question | Owner |
|---|---|
| What is this thing, and what do we know about it? | Foundation asset model |
| What are its environmental limits, as a declared property? | Foundation asset model |
| Does it matter, and how much? | **Stewardship** |
| What care does it require, and when? | **Stewardship** |
| Is the obligation met, due, or overdue? | **Stewardship** |
| Who is the assigned caretaker? | **Stewardship** (Foundation defines the caretaker-of relationship) |
| Is its environment currently within limits? | Truth |
| Should we do something now? | Concierge |

---

## What consumers may rely upon

| Consumer | May rely upon |
|---|---|
| Operational Trust | Significance, to classify risk and set confirmation requirements. **Significance is never itself the risk classification or the confirmation requirement (DL-75)** |
| Concierge | Obligation state, significance, accountability, and escalation intent |
| Continuity | Care experiences that may be resumed or deferred |

## What consumers must never assume

- That an obligation implies permission to act
- That an obligation implies a Communication
- That originating a Communication implies it will be delivered
- That `unknown` obligation state means compliance
- That significance is a Truth fact
- That significance was assigned by the framework rather than declared by the household
- That Base Significance converts to or implies Identity Confidence, Truth Confidence, Behaviour Source
  Confidence, an Operational Trust risk class, a confirmation requirement, or an escalation rung
  (**DL-75**)
- That equal Base Significance across two obligations means equal action, equal risk, or a silently
  resolved conflict (**DL-75**)
- That Stewardship has established the current condition — Truth did
- That a completed list item, a dismissed reminder, or a requested action is evidence that care occurred

---

## What Stewardship will never do

- Decide, on the household's behalf, that something matters
- Establish current conditions
- Decide what is permitted
- Deliver a Communication, choose its surface, or decide its Urgency
- Perform physical actions
- Call a Home Assistant service
- Store personal preferences or sessions
- Own the authoritative asset record
- Rank people, animals, possessions, or households against one another

---

## Uncertainty and unknown representation

`unknown` is a first-class obligation state. **Absence of evidence is never compliance.** An
obligation whose governing fact is unknown is `unknown`, never `met`.

---

## Failure and degradation behavior

| Condition | Behavior |
|---|---|
| A required fact is unknown | Obligation state is `unknown`, not `met` |
| A supporting fact operationally expires or its source becomes unavailable (**DL-59**) | Stewardship reevaluates the dependent obligation to `unknown`; it never remains `met` by inertia |
| A schedule source is unavailable | Report the source as unavailable; never silently mark obligations met |
| A caretaker is unassigned | Report an accountability gap; escalate to household authority per policy |
| A Delegated Access Grant is revoked and no other grant covers the obligation | Report the resulting access/assignment gap exactly as an unassigned caretaker; the household may reassign (**DL-57**) |
| Conflicting obligations | Surface the conflict; never silently prefer one |
| An obligation is repeatedly unmet with accountability unchanged | Continuing notification, **not automatic escalation** — escalation requires a configured change of accountable party (**OD-22**, **DL-57**) |

---

## Privacy constraints

Obligations may reveal health conditions, medication, absence patterns, pet care, and asset value.
Visibility is policy-gated by content class, not uniformly visible within the household. Guests must
not see care obligations. See [../architecture/privacy.md](../architecture/privacy.md).

---

## Explainability contributions

Every obligation that influenced a decision appears in the Decision Trace with its state, its
significance, and the fact that made it unmet. An escalation must explain what is unmet, since when,
and who is accountable.

---

## Open decisions

| ID | Question |
|---|---|
| OD-21 | **Resolved as DL-75.** Significance is a structured Significance Declaration — Derivation Source, Base Significance, Provenance, Effective Version — structurally separate from DL-39, DL-58, DL-73, DL-74, Operational Trust risk classification, and OD-22's escalation ladder |
| OD-22 | Escalation ladder semantics and defaults |
| OD-23 | Whether obligations project into Home Assistant calendars, `todo` entities, or a connected store |
| OD-75 | **Resolved as DL-48 and DL-49.** Condition and lifecycle are orthogonal; deferral and closure are lifecycle transitions carried by Change Records; the **Care Evidence Record** defines accepted completion evidence; custody is a Stewardship-owned **Custody Period**. Grouping remains a projection concern (**OD-23**) |
| OD-76 | **Resolved as DL-57.** Delegated Stewardship authority — one person may hold Stewardship access delegated by another, self/proxy/capacity model, the Delegated Access Grant construct, non-resident authorized participants, revocation, and the OD-22 escalation boundary are accepted |
| OD-69 | **Resolved as DL-61.** Asset-derived Entity projection reuses existing owned vocabularies, never an invented health scale; Person Environmental Requirements reuse the Asset environmental-limit pattern through Person Setup; Environmental Coverage, Configuration Completeness, and Truth Confidence remain three separate measures; Room Environmental Status is a non-authoritative projection; Room Health, Room Confidence, and People Health are formally rejected as authoritative terms |

## Related documents

- [../models/stewardship.md](../models/stewardship.md)
- [../models/asset.md](../models/asset.md)
- [truth-contract.md](truth-contract.md)
- [../scenarios/stewardship-obligations.md](../scenarios/stewardship-obligations.md)
- [../scenarios/stewardship-use-cases.md](../scenarios/stewardship-use-cases.md)
