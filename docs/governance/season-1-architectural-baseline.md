# Season 1 Architectural Baseline

> **Document status: Operational.**
> A **point-in-time snapshot** taken 2026-08-25, before Episodes 9–11.
> **This document is not architecture-of-record and creates no authority.** Where it disagrees with
> [decision-ledger.md](decision-ledger.md), [authority-order.md](authority-order.md), or any canonical
> model or contract, **those prevail and this document is wrong**.
> Terminology: [../models/glossary.md](../models/glossary.md).

---

## Why this document exists, and what it deliberately is not

A baseline records **where the architecture actually stands**, so that the next episodes can be
written against evidence rather than optimism. It **restates** nothing as authority, **decides**
nothing, and **classifies** nothing that the repository has not already classified.

**It is a snapshot and it will go stale.** The ledger and the open-decision index are the living
records.

---

## 1. Framework status

| Element | State |
|---|---|
| Responsibilities | **Seven**, unchanged: Foundation, Truth, Identity, Operational Trust, Stewardship, Continuity, Concierge (**DL-01**) |
| Accepted decisions | **DL-01 through DL-50** |
| Open-decision identifiers | **OD-01 through OD-84** |
| Closed or resolved | **10** — OD-02, 03, 08, 14, 16, 33, 34, 50, 75, 80 |
| Open | **74** |
| Markdown documents | **194**, every one carrying a status banner |
| Relative link integrity | **194 files scanned, 0 broken links** |
| Open issues unreferenced by documentation | **0** |
| HTBW Core implementation | **None. The repository contains no code files** |

**No new responsibility, store, history mechanism, escalation ladder, or source of truth has been
created since the refoundation.** Every review in this cycle resolved to *consume a native
capability*, *record a distinction*, or *govern an existing capability more precisely*.

---

## 2. Accepted ADRs

**Nine.** All links verified.

| ADR | Status | Establishes |
|---|---|---|
| [../architecture/adr-htbw-core-refoundation.md](../architecture/adr-htbw-core-refoundation.md) | Canonical (constitutional) | The seven responsibilities; trust as an outcome; governance as cross-cutting |
| [../architecture/adr-truth-as-fact-engine.md](../architecture/adr-truth-as-fact-engine.md) | Canonical | Truth as a first-class authoritative fact engine |
| [../architecture/adr-identity-replaces-voice-identity-boundary.md](../architecture/adr-identity-replaces-voice-identity-boundary.md) | Canonical | Identity is the responsibility; voice is one evidence source |
| [../architecture/adr-room-configuration-ownership.md](../architecture/adr-room-configuration-ownership.md) | Canonical | Room Configuration owned by Foundation; the four states |
| [../architecture/adr-home-assistant-first-and-connected-storage.md](../architecture/adr-home-assistant-first-and-connected-storage.md) | Canonical | Home Assistant First; Connected Storage; Native Experience |
| [../architecture/adr-historical-explainability-and-historical-truth.md](../architecture/adr-historical-explainability-and-historical-truth.md) | Accepted | Explainability across time; retention as a floor as well as a ceiling |
| [../architecture/adr-temporal-record-model.md](../architecture/adr-temporal-record-model.md) | Accepted | Governed change rather than repeated full copies |
| [../architecture/adr-resident-communication-and-delivery-separation.md](../architecture/adr-resident-communication-and-delivery-separation.md) | Accepted | Communication separate from delivery; permission to act is not permission to announce |
| [../architecture/adr-wyoming-compatible-voice-evidence-runtime.md](../architecture/adr-wyoming-compatible-voice-evidence-runtime.md) | Canonical, **Accepted 2026-08-25** | **DL-50** — the capability execution host, the Wyoming boundary, the Voice Evidence Provider Principle |

---

## 3. Open decisions

**74 open.** Every one is traceable to a GitHub issue through
[open-decision-issue-index.md](open-decision-issue-index.md), and **every open issue is referenced by
at least one document**.

### Raised during this cycle

| ID | Issue | Question | Raised by |
|---|---|---|---|
| **OD-82** | **#160** | Product consolidation and retirement | A **verified contradiction** with `authority-order.md`. **Resolved 2026-08-26 as DL-51 and DL-52** |
| **OD-83** | **#168** | Voiceprint gallery structure under channel diversity | DL-50 acceptance, separated deliberately |
| **OD-84** | **#169** | Multi-speaker evidence and speaker plurality | Post-acceptance harvest |

**Three new decisions across four governance executions.** Two harvest reviews produced **none**,
which is the intended outcome — a review that manufactures decisions is not disciplined.

---

## 4. Capability maturity by responsibility

| Responsibility | Model | Contract | Scenario coverage | Implementation |
|---|---|---|---|---|
| **Foundation** | Canonical | Canonical | room-vocabulary | **None** |
| **Truth** | Canonical | Canonical | where-is-tom, where-is-maisey, where-is-my-phone | **None** |
| **Identity** | Canonical | Canonical | where-is-tom, multi-person-conflict | **None** |
| **Operational Trust** | Canonical | Canonical | multi-person-conflict, nighttime-suppression | **None** |
| **Stewardship** | Canonical | Canonical | stewardship-use-cases (8), stewardship-obligations | **None** |
| **Continuity** | Canonical | Canonical | continuity-use-cases (15), follow-me-media | **None** |
| **Concierge** | — *(no separate model; the contract is the model)* | Canonical | **concierge-use-cases (20)**, why-did-this-happen | **None** |

**Every responsibility has a canonical contract. None has code.** That asymmetry is the honest
headline of Season 1: **the architecture is materially ahead of the implementation, deliberately.**

---

## 5. Concierge maturity

From [../scenarios/concierge-use-cases.md](../scenarios/concierge-use-cases.md).

| Class | Count | Use cases |
|---|---|---|
| **A — Implemented** | **0** | — |
| **B — Architecturally supported** | 6 | C3, C4, C9, C12, C19, C20 |
| **C — Planned** | 0 | — |
| **D — North Star** | 1 | C1 |
| **E — Blocked** | 12 | C2, C6, C7, C8, C10, C11, C13, C14, C15, C16, C17, C18 |
| **F — Research required** | 1 | C5 |

**Facets: 14 of 24 already accepted, none missing, none requiring a new construct.**
**Cross-cutting questions: 11 of 20 answered by accepted architecture.**

---

## 6. Explainability dependencies

**Explainability is a required output, not a feature** — a non-negotiable constraint binding
regardless of rank.

| Dependency | State |
|---|---|
| Decision Trace as the explainability spine | **Accepted** — **DL-15**, **DL-46**; [../models/decision-trace.md](../models/decision-trace.md) |
| A trace for every decision, action, **non-action**, and suppression | **Accepted** — **DL-15** |
| References rather than copies, version-pinned | **Accepted** — **DL-27** |
| Uncertainty survives to the resident | **Accepted** — concierge-contract §10 |
| *"I can't tell you what caused it"* as a valid answer | **Accepted** — [../scenarios/why-did-this-happen.md](../scenarios/why-did-this-happen.md) |
| **Where traces are persisted** | **Open — OD-29 (#79), blocked on OD-01** |
| **Which surfaces expose traces, and to whom** | **Open — OD-30 (#80)** |
| Retention floor and ceiling | **Open — OD-05 (#77)** |

**The explainability model is accepted; its persistence and visibility are not.** A home cannot
explain itself from a trace it has nowhere to keep — **OD-29 is on the critical path for the Season 1
promise**, and it is currently blocked on **OD-01**.

---

## 7. Governance dependencies

| Dependency | State |
|---|---|
| Authority order | **Canonical** |
| Document lifecycle and status banners | **Canonical**; every one of 194 files classified |
| Decision ledger | **Canonical**; DL-01–DL-50, OD-01–OD-84 |
| Open-decision issue index | **Canonical**; ledger and index verified consistent |
| Document register | **Canonical**; every new file registered |
| Episode narrative validation pattern | Established — Episodes 4/5, 6 (#75), 7 (#151), 8 (**#170**) |
| **Version control of the constitutional set** | **Committed locally only — NOT resolved.** See the correction below and **#145** |

> **Corrected 2026-09-08 against direct `git` evidence.** This row previously read *"Resolved by this
> baseline"*. **That was true of the local commit and false of the governed remote.** Verified:
> `origin/main` is at `b1e02b3` and contains **137 files**, and **none** of
> `decision-ledger.md`, `authority-order.md`, `north-star.md`, `truth.md`, this file, or
> `docs/scenarios/` is present in it. The baseline commit `e39c0936` exists **only in the local
> repository**, the branches have **diverged**, and **#145 remains open**.

---

## 8. Technical-debt dependencies

**All documentation debt. No code debt exists, because no code exists.**

| Item | Issue | Severity |
|---|---|---|
| Nine canonical documents illustrate Identity confidence as **floats**, contradicting **DL-39** | **#154** | **High** — it is the pattern most likely to be built |
| Pet model consolidation | **#144** | Medium |
| HTBW visual canon not under repository governance | **#150** | Medium |
| Home Assistant native capability verification backlog (**DL-30**) | **#146** | **High** — several decisions cannot close without it |
| Constitutional set not under version control | **#145** | **NOT addressed.** Committed locally at `e39c0936`; **absent from `origin/main`**, which holds 137 files and none of the constitutional set. **High** |

---

## 9. Day-1 capability set

**Organising principle, derived from the constitutional non-negotiables rather than invented here:**

> **Day-1 is what makes the home explainable, safe, and honest.**
> **Post-launch is what makes it helpful.**
> **North Star is what makes it anticipatory.**

A home that is helpful but cannot explain itself has not behaved well. A home that is explainable and
does little has.

### Identity

| Capability | Class |
|---|---|
| Purpose-scoped Identity Assertion with the four bands (**DL-39**) | **Day-1** |
| `known` / `ambiguous` / `unknown` / `unavailable` / `not required` all expressible (**DL-33**) | **Day-1** |
| At least one evidence family, person-scoped reliability (**DL-32**) | **Day-1** |
| Consent as an eligibility gate, excluded before weighting | **Day-1** |
| Voice as an evidence family | **Post-launch** — DL-50 accepted, unimplemented |
| Multi-speaker plurality | **North Star** — OD-84 |

### Truth

| Capability | Class |
|---|---|
| Facts with provenance, confidence, and **freshness** | **Day-1** |
| `unknown` distinguishable from `false` | **Day-1** |
| Contextual Person-Presence Fact, distinct from an assertion (**DL-06**) | **Day-1** |
| Historical Facts and the eight lifecycle transitions (**DL-25**) | **Post-launch** |
| Conversation-active state | **North Star** |

### Operational Trust

| Capability | Class |
|---|---|
| Required Identity Band per protected operation (**DL-39**) | **Day-1** |
| Audience composition and disclosure evaluation (**DL-34**) | **Day-1** |
| The unidentified-person policy (**DL-33**) | **Day-1** |
| Confirmation outcomes, including `Unavailable` (**DL-37**) | **Day-1** |
| Required Confirmation Strength classes (**DL-40**) | **Post-launch** |
| Learned-policy promotion | **North Star** — OD-28 |

### Stewardship

| Capability | Class |
|---|---|
| Household **declaration** of what matters — *a default the household never saw is not a declaration* | **Day-1** |
| Obligation condition and lifecycle as orthogonal fields (**DL-48**) | **Day-1** |
| Care Evidence Record closing an obligation (**DL-48**) | **Day-1** |
| The escalation ladder | **Post-launch** — OD-22 |
| Custody Periods (**DL-49**) | **Post-launch** |

### Continuity

| Capability | Class |
|---|---|
| Person-scoped and room-scoped preference, and nothing else | **Day-1** |
| Current experience context for resume | **Post-launch** |
| Restoration semantics | **Post-launch** — OD-78 |
| Guest relationship memory | **North Star** — OD-06, OD-28 |

### Concierge

| Capability | Class |
|---|---|
| The nine permitted outcomes, including **do nothing and be able to say why** | **Day-1** |
| Audience-evaluated delivery — **permission to act is not permission to announce** | **Day-1** |
| Capability-unavailable that **names the dependency** (**DL-41**) | **Day-1** |
| Guest-safe treatment when Identity is `unknown` | **Day-1** |
| Room capability discovery in household vocabulary (**C9**) | **Day-1** |
| Channel selection across surfaces | **Post-launch** — OD-43 |
| Deferral, re-presentation, acknowledgement | **Post-launch** — OD-45, OD-48 |
| Opportunity recognition (**C6**, **C7**) | **Post-launch** — OD-77 |
| Conversation-aware interruption (**C1**) | **North Star** |

### Explainability

| Capability | Class |
|---|---|
| A Decision Trace for **every** decision, non-action, and suppression | **Day-1, non-negotiable** |
| Resident-facing explanation that retains uncertainty | **Day-1** |
| Trace persistence | **Day-1 blocker** — OD-29 |
| Historical reconstruction across time | **Post-launch** |
| Evidence Packages | **North Star** — OD-40 |

### Governance

| Capability | Class |
|---|---|
| Every capability declares its dependencies (**DL-41**) | **Day-1** |
| Every artifact and record class declares its retention (**DL-43**, **DL-47**) | **Day-1** |
| Consent recorded, scoped, attributable, revocable | **Day-1** |
| Preservation Hold | **Post-launch** — OD-39 |

---

## 10. North Star capability set

**None is implemented, and none may be presented as implemented.**

Passive speech-activity monitoring · real-time conversation-active state · multi-speaker
identification · unknown-speaker audience use · conversation-break detection · passive guest-device
observation · voice-based returning-guest recognition · cross-calendar travel-demand estimation ·
automatic battery-load optimisation · speaker-conditioned extraction · ambient participant
identification · guest relationship learning · learned-policy promotion · Evidence Packages.

---

## 11. Blockers — highest-leverage decisions

Ranked by **total downstream unlock**: use cases, issues, roadmap phases, and dependent decisions.

| Rank | Decision | Issue | Use cases | Dependent decisions | Roadmap | Why it leads |
|---|---|---|---|---|---|---|
| **1** | **OD-43** Delivery Surface Capability Model | **#113** | C17 fully; C1, C2, C16 partially | OD-44, OD-45, OD-54, OD-55, OD-57, OD-71 | — | **Nothing Concierge does reaches a person without it.** C1 alone needs five surface behaviours in one interaction |
| **2** | **OD-06** Consent Capture and Revocation | **#94** | C13, C14, C15 | OD-15, OD-28, OD-65, OD-77 | #163 | Gates **every** guest experience, and a guest has no household surface on which to consent or revoke |
| **3** | **OD-84** Multi-Speaker Plurality | **#169** | C1, C2, C16 | — | #164, #166 | Blocks two roadmap phases, and segmentation ships into a model with nowhere to put the finding |
| **4** | **OD-77** Person-to-External-Resource Association | **#148** | C6, C7, C11 | OD-20 | — | Every task, list, and calendar experience contract is Historical; there is no canonical owner |
| **5** | **OD-29** Decision Trace Persistence | **#79** | All | OD-05, OD-30, OD-35 | — | **Explainability is a Day-1 non-negotiable and it currently has nowhere to live.** Blocked on OD-01 |
| **6** | **OD-52** Audience Specification | **#100** | C10, C16 | OD-71 | — | Two-valued Guest/Owner cannot express a mixed audience, which is the common case |
| **7** | **OD-83** Gallery Structure | **#168** | — | — | #163 | Narrow, but must not be settled by implementation choice |
| **8** | **OD-82** Product Consolidation | **#160** | — | OD-20 | — | **Different leverage**: it blocks no use case but no portfolio decision can be made without it |

**Deciding ranks 1–4 and 6 would unblock ten of the twelve blocked Concierge use cases.**
**Deciding rank 5 is required before the home can honestly claim to explain itself.**

---

## 12. Season 1 promise audit

### Scope caveat, stated rather than glossed

**The repository contains material for Episodes 4 through 8 only.** Episodes 1–3 have **no repository
artefacts**, so no behaviour from them can be classified on evidence. **They are excluded rather than
guessed at.**

| Behaviour demonstrated or implied | Class | Evidence |
|---|---|---|
| The home explains why it did something | **A — Day-1 requirement** | **DL-15**; why-did-this-happen; concierge-contract §13 |
| The home explains why it did **nothing** | **A — Day-1 requirement** | concierge-contract §7 — *doing nothing is a decision and is traced* |
| The home says *"I was not certain it was you"* | **A — Day-1 requirement** | identity-contract; concierge-contract §10 |
| The home declines to announce in front of a guest | **A — Day-1 requirement** | **DL-29**, **DL-34**; nighttime-suppression |
| The home says a capability is unavailable and **names why** | **A — Day-1 requirement** | **DL-41** |
| The home answers *"where is Tom?"* through two stages | **B — Architecturally supported** | where-is-tom |
| The home answers *"where is Maisey?"* without routing a pet through Identity | **B — Architecturally supported** | where-is-maisey |
| The home tells a guest what they can do in this Room | **B — Architecturally supported** | C9; room-vocabulary |
| The home makes a Room comfortable from an outcome request | **B — Architecturally supported** | C12; concierge-contract §3 |
| The home uses connected cloud information but decides locally | **B — Architecturally supported** | C4; **DL-31**, **DL-42** |
| The home lets a transient fact expire | **B — Architecturally supported** | C3; **DL-25**, **DL-47** |
| The home maintains shade batteries without being asked | **B — Architecturally supported** | stewardship-use-cases 5 |
| The home recognises a voice | **C — Planned** | **DL-50**; #161–#167 |
| The home reminds you at the shop | **E — Blocked** | C6; **OD-77** |
| The home recommends charging the car tonight | **E — Blocked** | C7; **OD-77**, no travel governance |
| The home suggests shedding load during an outage | **E — Blocked** | C8; **OD-51**, **OD-67** |
| The home tells a guest about the artwork | **E — Blocked** | C10; **OD-52** |
| A question becomes a task | **E — Blocked** | C11; **OD-77**, **OD-23** |
| The home asks a guest whether to remember them | **E — Blocked** | C13; **OD-06** |
| The home welcomes a returning guest by name | **E — Blocked** | C14; **OD-06** |
| The home chooses the right channel | **E — Blocked** | C17; **OD-43** |
| The home waits for a break in conversation | **D — North Star** | C1 |
| The home knows someone unidentified is in the conversation | **E — Blocked** | C2; **OD-84** |

### The three groups the audit asked for

**Must exist before HTBW can honestly claim to *Behave Well*** — the five **A** rows above.
**Every one is about honesty rather than helpfulness**, which is the point: a home that explains
itself, admits uncertainty, respects an audience, and names what it cannot do has behaved well even if
it does very little.

**May evolve later** — the **B** and **C** rows. Nothing depends on them for the claim.

**Should not appear in Season 1 as current** — every **D** and **E** row. **Thirteen behaviours.**
They may appear as *intent*, clearly framed. They may not appear as *what the home does*.

---

## 13. Contradictions found

**Three found. One resolved 2026-08-25; two documented and not repaired.** None is architectural.

### C-1 — Four dangling issue references

| Reference | Document | Status of document |
|---|---|---|
| **#176** | `standard-implementation-prompt-header.md` | Active — subordinate |
| **#177** | `issue-execution-review-checklist.md` | Operational |
| **#178** | `cross-repo-ownership-drift-checklist.md` | Active — subordinate |
| **#186** | `concierge-v2-roadmap-coverage-review.md`, `final-roadmap-closure-review.md` | Historical |

**When this snapshot was taken, no issue with these numbers had ever existed** — the repository's
highest issue number was 170. They are pre-refoundation artefacts, and the source documents show they
are **Concierge** issue numbers. **No canonical document is affected.**

> **Corrected 2026-09-08.** HTBW issues **#176**, **#177**, **#178**, and **#179** now exist, so the
> bare references above **silently resolve to unrelated HTBW issues**. The references are still
> dangling in the sense that matters — they do not point at the Concierge issues they meant — but they
> are no longer *non-existent*, and the sentence *"no issue with these numbers has ever existed"* is
> now false. **The remediation is unchanged: qualify each reference with its repository.**

### C-2 — A stale issue-state assertion in two canonical governance documents — **RESOLVED 2026-08-25**

[decision-ledger.md](decision-ledger.md) and
[open-decision-issue-index.md](open-decision-issue-index.md) both stated that **"Issue #105 remains
open pending formal acceptance review"**, while **#105 had been closed on 2026-08-20**.

The baseline audit deliberately did **not** repair this, because repairing it meant asserting that the
formal acceptance review of **DL-48** and **DL-49** had occurred, and that could not be established
from repository evidence alone.

**It has since been established from the issue record.** The closing comment on #105, authored
2026-08-20T23:17:14Z and posted at the moment of closure, states *"PASS: OD-75 Formal Acceptance
Review Complete"*, *"Acceptance result: PASS"*, and *"Issue #105 may close as the completed governance
record for OD-75"*. The issue is closed with state reason **COMPLETED**.

**Every accepted outcome the review named was verified present in canon before the wording was
changed** — `met` means satisfied to date, the Custody Period lifecycle, and the preservation of the
last known custodian on an adversely resolved period are all held in
[../models/stewardship.md](../models/stewardship.md),
[../contracts/stewardship-contract.md](../contracts/stewardship-contract.md), and
[../models/glossary.md](../models/glossary.md).

**Both statements now record the completed review.** **#105 was not reopened, no issue was created,
and no decision was made.**

### C-3 — Closed pre-refoundation issues cited by non-historical documents

`architecture-guardrails.md` (Active — subordinate) and several Operational governance checklists cite
V2-era issues that are now closed. **Correct for a Historical document; stale for an Active one.**
Low severity, and no canonical document is affected.

### Not a contradiction, and recorded so it is not mistaken for one

**OD-82 was itself an unresolved contradiction** — between the premise that the standalone products are
being retired and `authority-order.md`'s non-negotiable that they remain separate released products.
At the time of this snapshot it was **raised, tracked, and deliberately unresolved**, which was the
correct state and not a defect in this baseline.

> **Resolved 2026-08-26 as DL-51 and DL-52**, after a review found a **second and deeper
> contradiction**: `greenfield-mandate.md` and `north-star.md` already described Voice Identity and
> Concierge differently from the flattened non-negotiable. **The asymmetry was already in the
> canonical tier, and the flattening was the defect.** Disposition is now stated **per product**, the
> non-negotiable is **amended rather than deleted**, and the adoption residual is separated as
> **OD-85**. See
> [../architecture/adr-product-disposition-and-legacy-adoption.md](../architecture/adr-product-disposition-and-legacy-adoption.md).
> **This snapshot is not rewritten; the resolution is recorded against it.**

---

## 14. Readiness assessment

### Ready for Episodes 9–11 — with two conditions

**Condition 1 — narrative discipline.** **Thirteen behaviours are blocked or North Star.** They may be
shown as intent and must not be shown as current capability. The maturity column in
[../scenarios/concierge-use-cases.md](../scenarios/concierge-use-cases.md) is the reference, and it is
maintained rather than one-off.

**Condition 2 — decision sequencing.** What Season 2 can honestly show is decided by **OD-43**,
**OD-06**, **OD-84**, **OD-77**, and **OD-52**. **Deciding those five converts ten blocked use cases
into architecturally supported ones.** Writing episodes that depend on them before they are decided
will produce narrative that the architecture then has to chase.

### What is genuinely strong

The seven responsibilities have held through five consecutive adversarial reviews without a boundary
moving. Every canonical contract exists. Every document is classified. **Every link resolves. Every
open issue is traceable. No review manufactured a decision it did not need.**

### What is genuinely weak

**There is no implementation, and explainability — the one thing declared non-negotiable — has nowhere
to be persisted** until **OD-29** closes, which is itself blocked on **OD-01**. **That is the single
most important gap in this baseline**, and it is not a Concierge problem.

---

## Related documents

- [decision-ledger.md](decision-ledger.md)
- [open-decision-issue-index.md](open-decision-issue-index.md)
- [authority-order.md](authority-order.md)
- [document-register.md](document-register.md)
- [../scenarios/README.md](../scenarios/README.md)
- [../scenarios/concierge-use-cases.md](../scenarios/concierge-use-cases.md)
- [../architecture/adr-wyoming-compatible-voice-evidence-runtime.md](../architecture/adr-wyoming-compatible-voice-evidence-runtime.md)
- [../architecture/north-star.md](../architecture/north-star.md)
