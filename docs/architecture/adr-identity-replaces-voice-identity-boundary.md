# ADR: Identity Replaces the Voice Identity Boundary

> **Document status: Canonical ADR.**
> Status: **Accepted**. Supersedes
> [adr-voice-identity-platform-service.md](adr-voice-identity-platform-service.md).
> Terminology: [../models/glossary.md](../models/glossary.md).

---

## Context

The repository asserted **Voice Identity** as a platform service and product boundary within HTBW.
Fifteen or more documents were built on that assertion, including an ADR declaring it a platform
service, a voice-recognition contract, a voice-profile model, and fourteen voice-enrollment documents.

Three problems followed.

1. **The boundary was named after a mechanism, not a responsibility.** Voice is a way of recognising
   someone. It is not the question being answered.
2. **Other identity evidence had no home.** BLE devices, assigned phones, watches, tablets, companion
   apps, presence trackers, Wi-Fi associations, room transitions, and vehicle associations all
   contribute to knowing who is present, and none of them are voice.
3. **Identity and presence were conflated.** A voice match in a room was frequently treated as the fact
   *this person is in this room*, which it is not.

---

## Decision

**The responsibility is Identity, answering *who do we believe this is?* Voice is one identity evidence
source among many.**

Voice Identity is superseded as a platform-service boundary inside HTBW Core.

### The three-way distinction is constitutional

| Concept | Owner | Example |
|---|---|---|
| **Identity Evidence** | Identity | A voice sample matched Tom's profile at 0.91 |
| **Identity Assertion** | Identity | Candidate Tom, identity_confidence_band: High, from voice + BLE + phone |
| **Contextual Person-Presence Fact** | **Truth** | Tom is present in the Den |

An identity assertion is an **input** to a presence fact. No responsibility may record an assertion as
a fact.

### Identity is advisory

**Identity is not authentication and not authorization.** Operational Trust consumes an identity
assertion, applies a threshold appropriate to the action-risk class, and decides what that assertion is
sufficient to authorize.

### Identity does not determine

Room occupancy, contextual presence, activity, what should happen, preferences, or permissions.

### An outcome that varies by person requires a sufficient Identity Assertion

> **This is a precondition. It is not a DL-41 dependency class.**

Where a capability produces a different outcome for different people — applying a person's
preferences, evaluating a person-scoped authority, addressing someone by name, disclosing something
person-specific — that outcome is a **person-scoped capability access**, evaluated against the
**current Identity Assertion** and against the band the capability requires.
[../scenarios/continuity-use-cases.md](../scenarios/continuity-use-cases.md) already states it in that
form: *"applying a person's preferences is a person-scoped capability access, evaluated against the
current Identity Assertion — not a consequence of the home having addressed someone by name."*

**No dependency class is created.** **DL-41**'s classes are a native Home Assistant capability, an
integration, a provider, Connected Storage, consent, and configuration. **Identity is not among them
and must not be added to them.** [failure-and-degradation.md](failure-and-degradation.md) requires
that a missing dependency is reported as the capability being **unavailable**, with the dependency
named, and is *"never rendered as a permission or identity failure"* — the two outcomes stay
distinguishable to the household because they are different kinds of thing, with different remedies.

**No new evaluation stage and no responsibility follow from this.** Identity remains advisory,
Operational Trust still owns every threshold, and an insufficient assertion produces an honest
degraded outcome rather than a silently misapplied one. **Voice Identity is not a governance
dependency**, and naming it as one would reinstate the boundary this ADR replaced.

### Forced artifact invalidation is an open household-event question

The **mechanism** by which a previously sufficient identity artifact becomes unusable — an encoder
change, an audio-contract change, or a comparability rule — is already settled and is **not reopened**:
it is a **DL-41** capability outcome, in which the capability is **unavailable** and the missing or
invalid dependency is **named**.

**What is not settled is the household event that follows**, in which every enrolled Person must enrol
again — how the household is told and by whom, what the home does in the interval, which fallback
applies, whether prior consent survives the artifact derived from it, and what completion means for a
bulk household act. That question is **OD-87**.

> **OD-87 reopens nothing.** It does not reopen **OD-16**, changes no compatibility mechanism, creates
> no dependency class, and restores no Voice Identity responsibility.

---

## Discoveries carried forward

From the Voice Identity exploratory work, preserved deliberately:

| Discovery | Where it now lives |
|---|---|
| Advisory, not authentication | [../contracts/identity-contract.md](../contracts/identity-contract.md) |
| Confidence bands rather than a single boolean | [../models/person-and-identity.md](../models/person-and-identity.md) |
| Reason codes `known`, `ambiguous`, `unknown`, `unavailable`, `not_required` | [../contracts/identity-contract.md](../contracts/identity-contract.md) |
| Short-lived attribution context that must not become a session | [../models/person-and-identity.md](../models/person-and-identity.md) |
| Safe metadata only — never vectors, embeddings, or storage paths | [../architecture/privacy.md](privacy.md) |
| Enrollment artifacts are temporary; derived profiles are durable | [../architecture/privacy.md](privacy.md) |
| Revocation removes the derived profile, not merely its use | [../contracts/identity-contract.md](../contracts/identity-contract.md) |

---

## Consequences

### Superseded

- `adr-voice-identity-platform-service.md`
- `voice-recognition-contract.md` and `person-identity-contract.md`, replaced by
  [../contracts/identity-contract.md](../contracts/identity-contract.md)
- `voice-profile-model.md` and `person-profile-model.md` as authority, replaced by
  [../models/person-and-identity.md](../models/person-and-identity.md)
- The fourteen voice-enrollment documents, retained as **architectural evidence** for the enrollment
  lifecycle, privacy handling, and retention design

### Retained

The voice-enrollment documents contain hard-won detail about enrollment state machines, artifact
lifecycle, retention, and data residency. They remain valuable evidence and are cited as the origin of
the preserved discoveries above.

### Not changed

The **Voice Identity integration remains a separate released product** with its own lifecycle. This ADR
creates no compatibility requirement for it, and no runtime code was modified.

> **Amended 2026-10-27 by DL-51, formal acceptance review of Issue #160 / OD-82.** This bullet recorded
> the state of the standalone product at the time this ADR replaced the Voice Identity platform-service
> boundary. **Disposition is now stated per product**: the standalone Voice Identity integration **will
> sunset**, while **Identity** — the responsibility this ADR establishes — remains unchanged and
> first-class. **The second half of the bullet is unchanged in force** — no compatibility requirement
> was created then, and none is created by sunset or by adoption (**DL-19**). This annotation records
> the amendment; **the original text is preserved as architectural evidence and is not rewritten.** See
> [adr-product-disposition-and-legacy-adoption.md](adr-product-disposition-and-legacy-adoption.md).

---

## Alternatives considered

| Alternative | Why rejected |
|---|---|
| Keep Voice Identity as a platform service and add other evidence sources beneath it | Names the boundary after a mechanism; other sources would remain second-class |
| Fold identity into Truth | Loses the distinction between an assertion and a fact, which is the source of the original confusion |
| Fold identity into Operational Trust | Conflates *who is this* with *what are they allowed to do*; identity must be usable when no authority question is being asked |

---

## Open decisions

**OD-07** local versus cloud voice; the rest resolved as
**DL-39**, **DL-64** assertion validity and applicability;
**OD-16** evidence weighting and fusion.

**OD-87** identity artifact invalidation as a governed household event — raised 2026-08-27 by the
Episode 10 governance narrative validation. It concerns the **household event**, never the
compatibility mechanism.

---

## Related documents

- [../models/person-and-identity.md](../models/person-and-identity.md)
- [../contracts/identity-contract.md](../contracts/identity-contract.md)
- [adr-truth-as-fact-engine.md](adr-truth-as-fact-engine.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
