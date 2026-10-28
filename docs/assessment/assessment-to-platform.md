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

## Open decisions

| ID | Question |
|---|---|
| OD-31 | **Resolved as DL-105.** Materialized Assessment Artifact — projection canonical, materialized only on explicit household request |
| OD-32 | The reassessment cadence, and whether it is per-item or per-home |

## Related documents

- [../architecture/framework.md](../architecture/framework.md)
- [../models/stewardship.md](../models/stewardship.md)
- [../models/room-configuration.md](../models/room-configuration.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
