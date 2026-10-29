# Assessment to Platform Traceability

> **Document status: Canonical.**
> Terminology: [../models/glossary.md](../models/glossary.md).
> Framework: [../architecture/framework.md](../architecture/framework.md).

---

## Purpose

A home does not become well-behaved because software was installed. It becomes well-behaved because
someone assessed what is there, what matters, what is missing, and what should be done — and then the
platform carried those conclusions faithfully into operation.

This document defines the **traceability model** that connects a household assessment to platform
behavior, and back again.

## Question answered

*How does an observation about a real home become configured, governed, operating behavior — and how do
we prove it did?*

---

## The traceability record

Every assessment item is traceable through the following elements. **No element may be silently
dropped.**

| Element | Meaning |
|---|---|
| **Assessment item** | What was observed or asked about the home |
| **Framework responsibility** | Which of the seven responsibilities owns it |
| **Object or relationship identified** | The Home, Room, Asset, Person, Pet, Service, or Relationship concerned |
| **Evidence source** | How it was established: inspection, interview, document, device, service record |
| **Current capability** | What the home can do about it today |
| **Gap** | What is missing, unconfigured, unknown, or unenforced |
| **Risk or significance** | Why it matters, and how much |
| **Recommendation** | What should be done |
| **Proposed policy** | The governance position that would follow |
| **Implementation status** | Not started, configured, partially configured, operating |
| **Operational validation** | Evidence that the platform actually behaves as intended |
| **Ongoing maturity assessment** | Whether the outcome is holding over time |

---

## Why each element exists

| Element | Failure it prevents |
|---|---|
| Framework responsibility | Findings landing in the wrong layer, recreating the ownership confusion this refoundation resolves |
| Object or relationship | Recommendations that cannot be attached to anything the platform knows |
| Evidence source | Unverifiable claims entering the household model |
| Gap | Conflating "we know about it" with "we handle it" |
| Risk or significance | Treating every finding as equally urgent |
| Proposed policy | Recommendations that never become governed behavior |
| Operational validation | Assuming that configuring something made it work |
| Ongoing maturity | Assuming that working once means working still |

---

## Worked example

```
Assessment item:        A 1918 A.B. Chase 6' grand piano is in the Music Room.
Framework responsibility: Foundation (description) and Stewardship (care)
Object identified:      Asset "1918 A.B. Chase 6' Grand Piano"; Room "Music Room"
Evidence source:        Inspection, owner interview, appraisal document
Current capability:     The Music Room has a temperature sensor; no humidity sensor
Gap:                    Humidity is unmeasured; no preservation obligation exists
Risk or significance:   High — irreplaceable, degraded by sustained low humidity
Recommendation:         Add a humidity sensor; record 40-60% RH as a preservation limit
Proposed policy:        Autonomous humidifier control permitted; caretaker notified when out of range
Implementation status:  Configured
Operational validation: Truth publishes Music Room RH as an Authority-Derived Fact (**DL-62**);
                        Stewardship reports the preservation obligation as met
Ongoing maturity:       Reviewed quarterly; obligation state history shows no sustained breach
```

Traced through the framework:

| Step | Responsibility |
|---|---|
| The piano exists, is in the Music Room, and requires 40–60% RH | Foundation |
| The humidity sensor is the configured Primary Authority for humidity (**DL-62**) | Room Configuration |
| The Music Room is at 31% RH | Truth |
| The preservation obligation is unmet | Stewardship |
| Humidifier control is permitted autonomously | Operational Trust |
| Raise humidity, notify the caretaker, explain | Concierge |

---

## Traceability rules

1. **Every assessment item maps to exactly one owning responsibility.** An item that appears to need
   two is really two items.
2. **A recommendation without a proposed policy is incomplete.** Advice that does not become governed
   behavior does not change how the home behaves.
3. **A proposed policy without operational validation is unproven.** Configuration is not evidence.
4. **A gap of `unknown` is a finding, not an omission.** "We cannot currently tell" is a legitimate and
   important assessment result.
5. **Significance is recorded, not implied.** It flows into Stewardship, and from there into
   prioritisation and risk classification.
6. **Maturity is reassessed.** A home changes; obligations lapse; sensors fail; residents change.

---

## Relationship to the framework

The assessment model does not introduce a new responsibility. It is a **method** that populates the
existing ones:

| Assessment output | Lands in |
|---|---|
| Objects and relationships | Foundation |
| Participation, exposure, vocabulary | Room Configuration |
| Significance, obligations, caretakers | Stewardship |
| People, consent, evidence sources | Identity |
| Required facts and missing sensors | Truth |
| Preferences and continuity expectations | Continuity |
| Proposed policies | Operational Trust |
| Expected behavior and explanations | Concierge |

---

## Vendor-agnosticism

> **The framework is vendor-agnostic.** Home Assistant is the first implementation environment, not a
> constraint on the architecture.

The assessment model describes homes, not products. An assessment performed against this model remains
valid if the implementation environment changes. Recommendations may reference specific technology, but
the traceability record must remain expressible without it.

See [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md) and
principle **P17 — architecture outlasts technology**.

---

## Failure behavior

| Condition | Behavior |
|---|---|
| An item cannot be assigned a responsibility | It is unresolved and must be escalated, not filed arbitrarily |
| Evidence is anecdotal | Record the evidence class honestly; do not upgrade it |
| A recommendation is declined by the household | Record the decline and its reason; the gap remains visible |
| Validation fails | Implementation status reverts to partially configured; the gap reopens |

## Privacy considerations

Assessment records may contain asset value, health obligations, occupancy patterns, and household
relationships. They are governed by the same visibility policy as the responsibilities they populate.
See [../architecture/privacy.md](../architecture/privacy.md).

## Explainability requirements

A household must be able to ask *why is the home configured this way?* and receive the assessment item,
the significance, and the accepted recommendation that produced the configuration.

---

## Materialized Assessment Artifact (DL-105)

**The canonical Assessment Record is the projection above — the live, cross-responsibility
traceability view reconstructed from what Foundation, Truth, Stewardship, Identity, Continuity,
Operational Trust, and Concierge already own.** It carries no independent payload; viewing it
requires no Connected Storage.

**On explicit household request only**, Concierge materializes the current projection into a durable
**Materialized Household Assessment** artifact. This is never automatic, and performing or viewing the
Assessment never depends on Connected Storage — only materializing and later retrieving a durable copy
does (**DL-41**).

The artifact is **Foundation-owned** (Foundation owns the Home, the artifact's anchor and Governing
Parent — the same anchor-ownership rule **DL-43** already applies to Asset documents), **Managed
Content**, anchored to and Governing-Parented by the **Home** (an Assessment is canonically
whole-household in scope; no narrower per-Room or per-Asset Assessment construct exists). Each
materialization produces its own immutable **Record Identity** (**DL-104**) — a new artifact, never a
revision of a prior one — carrying **Governed References** to the exact versions of the Facts,
obligations, and configuration consulted at that time, never a copy of the underlying payloads. A
Stewardship obligation produced by a finding survives independently of any materialized artifact's
existence, through the obligation's own required Provenance (`temporal-record.md`), never through
artifact retention. See [../architecture/connected-storage.md](../architecture/connected-storage.md),
"Accepted artifact retention strategies," for the full lifecycle declaration.

**#177 firewall preserved**: this section states storage/lifecycle only, against the current,
canonical 12-element traceability model above. It adds no element from #177's proposed
household-impact content, assigns no retention/access semantics to it, and does not depend on its
adoption.

---

## Reassessment Cadence and Triggers (DL-107)

**The Assessment item is the reassessment unit.** Reassessment operates at the granularity of the
traceability record above — the same unit **rule 1** already requires ("every assessment item maps to
exactly one owning responsibility"). No narrower or coarser unit is invented. **Continuous
improvement** (`../architecture/north-star.md`, lifecycle stage 9) names the framework's terminal
lifecycle stage; it states that the lifecycle does not stop at operational validation, but it does not
itself mandate any numeric cadence or mechanism — the hybrid model below is one way architecture
operationalises it, accepted by Owner Policy Response (#111), never derived from the stage name alone.

### Hybrid model: two trigger paths, one reassessment mechanism

Reassessment has exactly two trigger paths, both producing the identical outcome — an Assessment item
re-evaluated through this document's own traceability record — never two separate reassessment models:

1. **Event-driven targeted reassessment (primary).** A **material-change trigger class** — a Room
   repurposed, a capability installed or removed, an Asset added or removed, an applicable requirement
   or policy change, or residents changing (trigger semantics only; **no household-impact content is
   added — #177 firewall**) — identifies the bounded set of Assessment items whose traceability is
   materially affected. "Targeted" names that bounded set, never exactly one item: a single change may
   affect several items, each still mapped to exactly one responsibility per **rule 1**. This is a
   semantic trigger **class**, not a closed enum; **DL-41** capability-unavailable detection is one
   already-accepted concrete source ("sensors fail" is event-driven-detectable there, not a gap this
   decision must separately close).
2. **Periodic whole-Home maturity-review backstop.** Required in addition to event-driven
   reassessment (Owner Policy Response, #111), because some household drift — habits, usage, and
   expectations changing without any capability failing, any Room being formally repurposed, or any
   other material-change event occurring — produces no discrete governed event sufficient to select
   affected items. The backstop exists so this category of drift is not structurally unreachable.

### Whole-Home review is discovery, never a blind rerun

A whole-Home maturity review is a **discovery pass**: for each Assessment item, it checks whether the
item's own **ongoing maturity assessment** element (rule 6, above) still appears to hold. It does
**not** mean every item is stale, every finding is invalid, or every recommendation is regenerated, and
it does not require rerunning unrelated items. Where an item's ongoing maturity assessment still holds,
the review reconfirms it — recorded as a non-action via the existing Decision Trace (**DL-15** requires
one for every decision, action, non-action, and suppression); no finding is fabricated merely to prove
the review ran. Where it no longer appears to hold, that item enters ordinary **event-driven targeted
reassessment** above, exactly as if a material-change event had flagged it. No new "Assessment Cycle"
Governing Parent is created (**DL-105** already forecloses one), and the review does not reset or
duplicate a targeted reassessment that already covered the same item.

### Household-configured interval; no HTBW-wide default

The review interval is **Home-scoped configuration** — the same category of whole-household scheduling
policy as the already-listed "Home maintenance calendar" in `../models/home.md`'s Home-scoped state and
policy table, where it is now also listed. **No HTBW-wide numeric interval is defined** — this is the
same "household configures; no invented default" pattern already accepted twice for other cadence
questions (**DL-97** escalation timing, **DL-98** retry count/interval), applied here for a third
cadence decision. Where no interval is configured, the backstop capability is **Configuration
Incomplete** for that household — reported honestly, never silently defaulted and never silently
disabled, under `home.md`'s own existing Failure behavior rule that an unconfigured state "must be
reported as such." **Event-driven targeted reassessment is unaffected by a missing interval** and
remains fully available regardless.

**Review-due state**: "a periodic whole-Home maturity review became due" is a Domain Event, a direct
instance of the shape `temporal-record.md` already lists ("an obligation became unmet"), owned by Truth
as a current home-level fact — the same shape already declared for "the home is in Away state." A new
Home-level tracking point, **last whole-Home maturity review performed**, is added to `home.md` so the
comparison against the configured interval is honestly derivable; this is the one new piece of
canonical content this decision adds, stated plainly rather than silently assumed. No new record class,
Reassessment Trace, or second store is created.

### Reassessment is never automatically a Stewardship obligation

A review becoming due, or a material-change trigger identifying an affected item, is a **fact**, not an
obligation. Where accountable completion work is independently warranted, the existing Stewardship
obligation model (Subject, Statement, Significance, Schedule or condition, Condition state, Lifecycle
state, Accountability, Escalation intent, Provenance — `../models/stewardship.md`) applies completely
unchanged; its Provenance cites the triggering Domain Event or material-change trigger by Governed
Reference, exactly as any other obligation's Provenance already works. No new obligation schema is
created.

**Accountability**: the whole-Home review capability itself has no accountable person — it is a
Concierge-orchestrated architectural capability, consistent with Concierge's existing role
materializing the **DL-105** artifact and composing every Decision Trace, not itself a care obligation.
This is the explicit residual where no accountability rule applies, stated rather than assumed. Where a
reassessment finding does become a Stewardship obligation, accountability resolves entirely through the
existing many-to-many caretaker/Role model (**DL-71**, **DL-97**) unchanged — no "Assessment accountable
role" is invented. **Nagging boundary**: review-due and any resulting obligation carry no communication
frequency, modality, or escalation cadence of their own; **DL-97**'s escalation ladder and stop
conditions govern any resulting notification entirely unchanged.

### Unactioned findings and declined recommendations

Every state in the Failure behavior table above, and every **DL-48** obligation condition/lifecycle
state, already answers how reassessment treats an unactioned finding: a gap without a recommendation
remains visible; a declined recommendation is recorded with its reason and the gap remains visible; an
open or overdue obligation is unaffected by reassessment except through its own governed lifecycle
(reassessment never deletes, duplicates, or resolves an obligation directly); where a condition
genuinely changed, a new current finding is produced under **DL-27**/**DL-104**'s historical-correctness
rule, which never rewrites the prior finding's historical truth.

**A previously declined recommendation, encountered under materially unchanged conditions, is never
re-raised as new** (Owner Policy Response, #111). "Materially unchanged" is established exclusively by
**DL-104** exact-version Governed-Reference identity — the declined recommendation's own governed
subject, scope, and version match the current one — never fuzzy text matching. Materially changed Room
usage, policy, requirement, or safety state may justify a new finding and recommendation; a materially
different recommendation is, by the same Governed-Reference identity, simply a different recommendation
rather than a re-raise of the declined one. A safety-state change takes the same precedence over a
prior decline that safety already holds over every other household preference elsewhere in accepted
architecture (`../contracts/stewardship-contract.md`, `../architecture/privacy.md`). **The prior decline
is retained as provenance in every case, never erased**, and remains explainable alongside any newly
justified recommendation.

### Boundaries preserved, nothing absorbed

**DL-22** traceability is preserved in full; the Decision Trace (**DL-15**) is the sole explainability
mechanism for every reassessment outcome, including a review's own non-action — no separate
Reassessment Trace exists. **DL-105**'s artifact boundary is unchanged: reassessment updates the live
projection only and never auto-materializes, deletes, or supersedes an existing Materialized Household
Assessment artifact. **The #177 firewall is preserved in full**: no household-impact element is added,
assigned retention/access semantics, or decided here; this decision governs cadence and triggering
only. **The human-worth boundary is preserved**: maturity applies to the Home, a decision, a capability,
or an implementation outcome — never to a person (`../contracts/stewardship-contract.md`). **OD-23 is
unaffected**: no scheduler mechanism, calendar/`todo` projection, or storage technology is chosen for
the interval or the review-due fact.

---

## Open decisions

| ID | Question |
|---|---|
| OD-31 | **Resolved as DL-105.** Materialized Assessment Artifact — projection canonical, materialized only on explicit household request |
| OD-32 | **Resolved as DL-107.** Assessment item is the reassessment unit; hybrid cadence — event-driven targeted reassessment (primary) plus a household-configured periodic whole-Home maturity-review backstop (no HTBW-wide default interval); review-due is never automatically a Stewardship obligation; declined recommendations are never re-raised under materially unchanged conditions (DL-104 exact-version matching) |

## Related documents

- [../architecture/framework.md](../architecture/framework.md)
- [../models/stewardship.md](../models/stewardship.md)
- [../models/room-configuration.md](../models/room-configuration.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
