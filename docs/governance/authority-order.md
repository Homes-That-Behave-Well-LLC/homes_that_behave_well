# Authority Order

> **Document status: Canonical governance.**
> Terminology: [../models/glossary.md](../models/glossary.md).

---

## Purpose

When two documents disagree, something must decide which one wins. This document records that order.

---

## The authority order

Applied top-down. A lower level never overrides a higher one.

| Rank | Source |
|---|---|
| **1** | The North-Star video-series framework |
| **2** | The constitutional decisions recorded in the refoundation execution prompt |
| **3** | Accepted ADRs, contracts, models, and governance documents that are not in conflict with 1 or 2 |
| **4** | Existing HTBW Markdown documentation |
| **5** | Lessons learned in Asset Intelligence, Voice Identity, and Concierge |
| **6** | Existing implementation |
| **7** | GitHub issues |

---

## What each rank means

### 1. The North-Star framework

The seven responsibilities, their order, and the questions they answer. Recorded in
[../architecture/north-star.md](../architecture/north-star.md). Nothing in this repository may
contradict it.

### 2. Constitutional decisions

The decisions made during the refoundation itself — the supersession of the four-service model, Truth
as a first-class fact engine, Room Configuration owned by Foundation, Home Assistant First, Connected
Storage, Native Experience, and the greenfield mandate. Recorded in
[decision-ledger.md](decision-ledger.md) and in the refoundation ADRs.

### 3. Accepted ADRs, contracts, models, and governance

Canonical documents created or retained under the refoundation. Where two canonical documents at this
rank disagree, the disagreement is a defect to be resolved by a new decision-ledger entry, not by
preference.

### 4. Existing HTBW Markdown

Pre-refoundation documentation. Valuable, frequently correct in detail, and **not authoritative where
it conflicts**. Each such document carries a status banner; see
[document-lifecycle.md](document-lifecycle.md).

### 5. Lessons learned in the reference implementations

Asset Intelligence, Voice Identity, and Concierge are **architectural evidence**. Their discoveries are
carried forward deliberately, and are recorded in
[../architecture/greenfield-mandate.md](../architecture/greenfield-mandate.md). Their implementations
are not binding.

### 6. Existing implementation

Code demonstrates that something *can* work. It does not establish that it *should* be so. **No
compatibility requirement flows upward from implementation to architecture.**

### 7. GitHub issues

Issues capture intent, work in progress, and history. They are the weakest authority and are frequently
superseded by the documents above.

**One distinction is deliberate and does not raise their rank.** **GitHub issues are the authoritative
source for the current *status* of an open decision** — its remaining questions, its dependencies, and
its closure evidence. **Repository architecture documents remain authoritative for accepted
architecture.** An issue never establishes architecture; it records what is still undecided and how far
the work has got. The identifier-to-issue mapping is
[open-decision-issue-index.md](open-decision-issue-index.md).

---

## Conflict procedure

1. Identify the ranks of the conflicting statements.
2. If the ranks differ, the higher rank prevails, and the lower-ranked document is annotated or
   superseded.
3. If the ranks are equal and both are canonical, the conflict is a **defect**. Record it in
   [decision-ledger.md](decision-ledger.md) as an open decision, and resolve it with a new ADR.
4. Never resolve a conflict by silently deleting evidence.

---

## Non-negotiable constraints

These bind regardless of rank:

- The framework is **vendor-agnostic**; Home Assistant is the first implementation environment, not a
  constraint on the architecture.
- **Product disposition is stated per product, never for the portfolio** (**DL-51**). **Asset
  Intelligence** remains a **separate released product** with its own lifecycle, and **HTBW must never
  require it to be installed**. The standalone **Voice Identity** and **Concierge** integrations will
  **sunset**, while **Identity** and **Concierge** remain first-class HTBW responsibilities. **No
  compatibility requirement is created for any of them by anything in this repository** (**DL-19**).
  A product may sunset while its responsibility is unchanged, and a responsibility may be first-class
  inside HTBW while its released product continues. See
  [../architecture/adr-product-disposition-and-legacy-adoption.md](../architecture/adr-product-disposition-and-legacy-adoption.md).
- **A resident's investment in describing their household survives the transition** (**DL-52**).
  Adoption of Asset Intelligence data is **one-time, authoritative, and terminating** — never a runtime
  dependency, never continuous synchronisation, and never a source of shared authority.
- HTBW Core is **greenfield**. See
  [../architecture/greenfield-mandate.md](../architecture/greenfield-mandate.md).
- Explainability is a **required output**, not a feature.
- **Explainability extends across time.** Retention is a **floor as well as a ceiling**, and a
  historical reconstruction containing an unreported gap is a defect. See **P27**.
- **Truth is the system of record for both present and historical Facts.** No consumer may maintain a
  competing or re-derived Fact history. See **P28**.
- **History is recorded as governed change, not as repeated full copies**, and governed records
  **reference exact versions** rather than copying payloads. See **P29** and **P30**.
- **No new responsibility is created by temporal architecture.** There is no History, Memory,
  Household Memory, Case Management, or Evidence responsibility; no central history owner; no central
  snapshot owner; and no central preservation-hold enforcer.
- **Preservation Hold and Evidence Package are HTBW architectural terms, not claims of legal effect.**
  Nothing in this repository asserts court admissibility, chain-of-custody sufficiency,
  tamper-evidence or forensic certification, or regulatory compliance.
- **Communication is separate from delivery.** A Communication exists independently of the mechanism
  used to convey it, and is never defined as a notification, push message, announcement, or
  indicator. See **P31**.
- **Permission to act does not imply permission to announce.** Outbound communication is governed by
  the Existence → Participation → Exposure → Authority chain, evaluated against who can perceive the
  delivery surface. Where context is insufficient, **the delivery degrades, not the governance.** See
  **P32**.
- **No new responsibility is created by communication architecture.** There is no Communication,
  Messaging, Inbox, Delivery, or Escalation responsibility; no central delivery owner; no central
  inbox owner; and **no second escalation ladder**.
- **HTBW is not a life-safety system.** No document may represent a safety-category Communication as
  smoke detection, carbon-monoxide detection, medical alerting, security monitoring, or emergency
  notification, or as a substitute for certified alarms or emergency services. **This is not in
  tension with Stewardship's accepted scope of safety-related care** (**DL-79**, resolving **OD-56**):
  Stewardship may recognise, evaluate, and care for safety-related conditions and obligations, and
  HTBW may originate truthful, governed Safety Communications — neither establishes life-safety
  responsibility, guaranteed detection, warning, delivery, protection, mitigation, or outcome, and a
  certified life-safety or protective device remains authoritative for its own domain throughout.
  Safety capabilities require a one-time, authenticated-Administrator acknowledgement of this
  boundary before they are enabled.
- **Every framework responsibility expresses conclusions in proportion to the evidence quality
  available to it, never inventing facts, overstating certainty, or hiding limitations** (**DL-79**,
  the framework-wide evidence chain — Truth contributes facts; Identity contributes assertions and
  confidence; Operational Trust evaluates appropriateness; Stewardship contributes obligations and
  significance; Continuity contributes retained context; Concierge assembles delivery; Explainability
  reconstructs what happened and why). This is the union of already-accepted **P15, P27, P28, DL-26,
  DL-27, DL-30, DL-38, DL-58**, named here for cross-reference, not a new responsibility.

---

## Related documents

- [document-lifecycle.md](document-lifecycle.md)
- [decision-ledger.md](decision-ledger.md)
- [document-register.md](document-register.md)
- [../architecture/north-star.md](../architecture/north-star.md)
- [../architecture/principles.md](../architecture/principles.md)
