# HTBW Canonical Scenarios

> **Document status: Canonical scenario index.**
> Terminology: [../models/glossary.md](../models/glossary.md).
> Framework: [../architecture/framework.md](../architecture/framework.md).

---

## Purpose

A framework is only as good as the household outcomes it produces. These scenarios are the acceptance
tests for the architecture: each one must be explainable, end to end, with **every step attributed to
the responsibility that owns it**.

If a scenario cannot be walked through without ambiguity about ownership, the architecture has a defect.

---

## The scenarios

| Scenario | Demonstrates |
|---|---|
| [room-vocabulary.md](room-vocabulary.md) | Room Configuration, Contextual Vocabulary, Merged Rooms, deliberate exclusion, Room Help, knowledge assets, composite environment |
| [follow-me-media.md](follow-me-media.md) | Continuity intent, transfer eligibility, Truth-driven blocking, Operational Trust authority |
| [multi-person-conflict.md](multi-person-conflict.md) | Identity ambiguity, session conflict, authority to displace, confidence thresholds, confirmation, audience and disclosure |
| [nighttime-suppression.md](nighttime-suppression.md) | Room mode, suppression as a deliberate outcome, explainable non-action |
| [stewardship-obligations.md](stewardship-obligations.md) | Obligation state versus action, escalation intent, the garage-door separation |
| [stewardship-use-cases.md](stewardship-use-cases.md) | **The eight canonical Stewardship use cases.** Household declaration of what matters, care definition before alert, the corrective-action lifecycle, the named executor, and obligation closure |
| [continuity-use-cases.md](continuity-use-cases.md) | **Sixteen canonical Continuity use cases.** What Continuity holds and what it only references, the memory-versus-observation-versus-preference separations, restoration, resume, personal-resource associations, recommendation boundaries, correction and deletion, and room-aware music continuity with guest/default fallback and Music Assistant resolution |
| [concierge-use-cases.md](concierge-use-cases.md) | **The twenty-one canonical Concierge human-outcome use cases.** What the most helpful appropriate next response is, and what governs it — interruption, audience-aware delivery, channel selection, guest consent and hospitality, capability discovery, outcome-based requests, knowledge-to-action, context-aware message delivery and response location, and no-action as a governed outcome. **Carries a maturity classification per use case and is not proof of implementation** |
| [why-did-this-happen.md](why-did-this-happen.md) | The Decision Trace, action and non-action explanation, source attribution |
| [where-is-tom.md](where-is-tom.md) | **Person location — the two-stage path.** Identity Assertion → Contextual Person-Presence Fact, evidence ceilings, correlated evidence, conflict preservation, `unknown` versus `unavailable`, access versus presentation versus disclosure |
| [where-is-maisey.md](where-is-maisey.md) | **Pet location — a Truth-only path.** Why a Pet is never routed through Identity, tag versus wearer, an undischarged **DL-30** burden stated honestly, consent and disclosure for pet-derived evidence, Pet record lifecycle |
| [where-is-my-phone.md](where-is-my-phone.md) | **Device location — a Truth-only path.** Zone versus Room granularity, **Home Assistant First** applied to a location answer, why a device answer is a person disclosure, Historical versus current, broken-reference lifecycle |

> **The three location scenarios are read together.** They exist to make one asymmetry unmistakable:
> *"Where is Tom?"* is a **two-stage** question requiring an Identity Assertion first; *"Where is
> Maisey?"* and *"Where is my phone?"* are **Truth-only** questions that must **not** be routed through
> Identity. All three use **one** Truth Fact model with different Subjects — there is no
> `PersonLocationAssertion`, `PetLocationAssertion`, or `DeviceLocationAssertion`.

> **The two Stewardship documents are read together.**
> [stewardship-obligations.md](stewardship-obligations.md) proves the **separation** — obligation
> versus action. [stewardship-use-cases.md](stewardship-use-cases.md) proves the **lifecycle** — how a
> household declaration becomes a care definition, an obligation, a governed response, and a closure.

> **The two Continuity documents are read together.**
> [follow-me-media.md](follow-me-media.md) proves the **handoff** — transfer versus resume,
> eligibility versus decision. [continuity-use-cases.md](continuity-use-cases.md) proves the
> **boundary of remembering** — what Continuity holds, what it only references, and what belongs to
> another responsibility that happens to have a history.

---

## The household used throughout

```
Home
├── Living Space            (Merged Room: Kitchen + Dining + Living)
├── Den
├── Office
├── Primary Bedroom
├── Music Room
└── Garage

People: Tom, David
Pets: Maisey
Assets: Sonos speakers, Sonos Beam, LG television, Apple TV,
        7 shades (Kitchen 1, Dining 3, Living 3),
        1918 A.B. Chase 6' Grand Piano
```

---

## How to read a scenario

Each scenario is presented three ways:

1. **What the household experiences** — plain language, no architecture
2. **What each responsibility does** — a step table with explicit ownership
3. **What the home can say afterwards** — the human form of the Decision Trace

---

## Rules these scenarios enforce

1. Every step has exactly one owning responsibility.
2. No responsibility performs another's work, even when it would be convenient.
3. Uncertainty survives the whole pipeline and reaches the resident.
4. Non-action is a decision, and is explained.
5. Household vocabulary is used in every explanation — never entity IDs.
6. A deliberate exclusion is explainable as deliberate.

---

## Relationship to the historical examples

The documents under `examples/scenarios/` predate the refoundation. They are retained as **historical
illustrations** and remain useful for household framing, but their terminology and ownership statements
are superseded by these canonical scenarios.

---

## Related documents

- [../architecture/framework.md](../architecture/framework.md)
- [../architecture/runtime-sequence.md](../architecture/runtime-sequence.md)
- [../models/decision-trace.md](../models/decision-trace.md)
- [../assessment/assessment-to-platform.md](../assessment/assessment-to-platform.md)
