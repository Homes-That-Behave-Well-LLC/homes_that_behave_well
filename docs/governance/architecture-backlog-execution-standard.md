# Architecture Backlog Execution Standard

> **Document status: Operational.**
> A **repeatable process standard**. It defines *how* the next open HTBW architecture-backlog issue is
> selected and *how* readiness for greenfield implementation is assessed.
> **This document is not architecture-of-record and creates no authority.** It decides nothing,
> reprioritizes nothing, and closes nothing. Where it disagrees with
> [decision-ledger.md](decision-ledger.md), [authority-order.md](authority-order.md),
> [open-decision-issue-index.md](open-decision-issue-index.md), or any canonical model or contract,
> **those prevail and this document is wrong**.
> Terminology: [../models/glossary.md](../models/glossary.md).

---

## Why this document exists

Epic **#147** governs dozens of open architecture decisions and non-decision work items. Without a
recorded method, every future review would have to rediscover how to choose what to work on next, and
would risk treating a point-in-time plan as if it were permanent authority. This standard records the
durable *method* — Priority, Dependency, Readiness, and Dependency leverage — so future selection is
repeatable without re-deriving it, and so no specific backlog order is ever mistaken for architecture.

This standard governs **sequencing and readiness assessment only**. It does not touch, reopen, or
reprioritize any accepted decision, Priority label, or open issue.

---

## 1. Governing objective

The HTBW architecture backlog exists to **systematically retire architectural uncertainty** so that
implementation proceeds from accepted authority rather than allowing implementation choices to
silently become architecture.

**HTBW is deliberately greenfield.** Greenfield means the program should exploit the absence of
installed-base compatibility obligations, legacy HTBW Core persistence, established Core schemas,
public Core APIs, and customer migration obligations to establish foundational architecture correctly
**before** those implementation choices become expensive to change.

**Greenfield does not mean every conceivable future capability must be fully designed before any code
is written.** It means foundational choices — the ones expensive to change later — are resolved before
they are silently fixed by whatever gets implemented first.

---

## 2. The sequencing rule

**PRIORITY** establishes architectural importance.
**DEPENDENCY** establishes executable sequence.
**CURRENT READINESS** determines what can be worked now.
**DEPENDENCY LEVERAGE** breaks ties among otherwise-actionable work.

Default progression: **Priority 1 before Priority 2 before Priority 3.**

**This is not a rigid waterfall.** A lower-priority issue moves ahead of a higher-priority one only
when it is an explicit or demonstrably necessary prerequisite for that higher-priority work.

**A newly created implementation issue does not supersede older, intentionally prioritized
architectural work merely because implementation has become possible.** Priority labels were assigned
deliberately when the backlog was created and remain first-class governance evidence until a governed
decision changes them.

---

## 3. Issue work-class model

For sequencing purposes only, an open issue may be understood as one of:

| Class | Meaning |
|---|---|
| **A — Open Architecture / Product Decision** | A governed decision that must eventually receive formal acceptance, supersession, deferral, or another governed disposition |
| **B — Implementation-Shaping Research / Mapping** | Non-decision work supplying evidence needed to resolve architecture or safely implement accepted architecture |
| **C — Governance / Documentation / Remediation** | Work required to make repository authority, documentation, public contract, or governance state internally consistent |
| **D — Implementation** | Executable product/runtime work grounded in sufficiently accepted architecture |
| **E — Standing Governance Process** | Non-terminating or recurring work, such as the monthly Home Assistant release review ([home-assistant-release-review-standard.md](home-assistant-release-review-standard.md)) |
| **F — Acceptance / Closure Candidate** | Work whose substantive requirements appear already satisfied and which should receive formal review rather than another execution cycle |

**These work classes assist sequencing. They do not replace existing labels, decision identifiers,
Priority labels, or repository governance, and issues are never retroactively relabeled merely to fit
this model.**

---

## 4. Execution lifecycle

```
SELECT → GROUND → RESEARCH → DECIDE / REMEDIATE → UPDATE AUTHORITATIVE REPOSITORY
       → VALIDATE → OWNER ACCEPTANCE REVIEW → CLOSE → UPDATE EPIC / DEPENDENCIES → RECALCULATE
```

**No static, complete backlog order is ever treated as permanent authority.** After every accepted
closure, the next actionable issue is recalculated from current GitHub state — dependencies and
readiness change with each closure.

---

## 5. Selection rules

1. Begin with actionable Priority 1 work.
2. Among same-priority actionable issues, prefer the one with greater explicit dependency leverage
   (the issue whose completion unblocks the largest or most foundational dependency chain).
3. If the selected high-priority issue is blocked, work the minimum prerequisite necessary to unblock
   it, regardless of the prerequisite's own, possibly lower, Priority.
4. Do not execute downstream issues before their explicit prerequisites.
5. Do not send acceptance-ready work through unnecessary new execution — identify and route it to
   formal review instead (work class F).
6. Do not treat implementation *availability* as implementation *readiness*. An issue being executable
   does not mean the broader architecture is ready for it.
7. Do not optimize sequencing around a newly created implementation issue merely because it exists.
8. Do not require unrelated future-capability decisions to close merely because they exist; only
   decisions that materially determine the surface actually being implemented gate it.
9. Recalculate after every closure. Dependencies and readiness are current-state facts, not fixed plans.

---

## 6. Home Assistant First and implementation-mapping evidence (e.g., Issue #146)

This section records how **P21 / DL-30** evidence-gathering issues interact with backlog sequencing;
it does not reopen DL-30 or the Home Assistant First principle itself.

- Consume already-recorded, verified evidence first.
- Perform only the missing research required by the **currently selected** decision — do not require
  an evidence backlog to close globally merely because it still carries unresolved items for unrelated,
  not-yet-selected decisions.
- Use official Home Assistant developer documentation as the first external authority.
- Inspect upstream Home Assistant source/tests only where documentation is insufficient and repository
  governance permits.
- Treat unverifiable capability as **unverifiable**, never as verified absence.
- Do not invent an HTBW capability merely because native behavior has not yet been verified.

---

## 7. Greenfield implementation readiness states

| State | Meaning |
|---|---|
| **NOT READY** | Unresolved architectural decisions still materially determine the foundational implementation surface being considered |
| **PARTIALLY READY FOR ISOLATED IMPLEMENTATION** | Some independently governed implementation can safely proceed without prejudicing unresolved foundational decisions |
| **FOUNDATIONALLY READY** | No unresolved architectural decision materially determines the foundational surface about to be implemented |

**These are planning/governance assessments, not permanent architecture decisions.** They are
reevaluated every time decisions close or implementation scope changes.

### Foundational vs. capability-specific impact

| Classification | Meaning |
|---|---|
| **FOUNDATIONAL IMPLEMENTATION IMPACT** | The decision may materially alter canonical ownership, package/product boundary, persistence, stable identifiers, foundational relationships, configuration/provisioning, authority boundaries, public interfaces/contracts, or lifecycle/migration structure |
| **CAPABILITY-SPECIFIC IMPLEMENTATION IMPACT** | The decision affects a bounded capability that can be implemented later without restructuring unrelated Core foundation |
| **NO CURRENT IMPLEMENTATION IMPACT IDENTIFIED** | No implementation consequence is currently evidenced |

**These classifications support analysis only. They do not override Priority labels.**

---

## 8. PAYGO discipline for backlog governance

- Reuse prior accepted research and existing issue/dependency state.
- Avoid complete backlog re-analysis when only one branch of the dependency graph changed.
- Research only the selected issue and its necessary prerequisites.
- Avoid rereading unrelated ADRs/contracts/models already settled.
- Avoid repeating accepted architecture reviews.
- Use implementation-mapping evidence (e.g., #146) selectively — see §6.
- Avoid broad external research where repository or official evidence already answers the question.
- Update stale dependency/status metadata **encountered in the active branch of work** rather than
  launching an unrelated repository-cleanup exercise.

---

## 9. Point-in-time backlog reviews are non-normative evidence

A full backlog sequencing review may be performed and recorded (for example, as an Epic #147 comment)
at any time. Such a review is a **dated planning artifact**, not canonical governance. In particular:

- the exact issue order produced by any single review is **never** copied into this document or any
  other canonical document as permanent authority;
- the review's **implementation readiness** conclusion (§7) is recorded as a point-in-time assessment,
  expected to change as decisions close;
- a specific implementation issue's scope (for example, **Issue #201**) is never encoded here as
  architecture. An implementation issue may be valid and ready relative to its own immediate
  dependencies while the broader greenfield architecture remains **not ready** for that foundational
  implementation — the backlog's priorities, dependencies, and current readiness govern that question,
  not the existence of the implementation issue itself.

---

## Related documents

- [decision-ledger.md](decision-ledger.md)
- [authority-order.md](authority-order.md)
- [open-decision-issue-index.md](open-decision-issue-index.md)
- [document-register.md](document-register.md)
- [document-lifecycle.md](document-lifecycle.md)
- [htbw-architecture-execution-grounding-standard.md](htbw-architecture-execution-grounding-standard.md) — per-issue authority-order grounding and conflict handling; this document governs backlog-wide *selection and readiness*, not per-issue authority validation
- [home-assistant-release-review-standard.md](home-assistant-release-review-standard.md) — the standing (work-class E) monthly Home Assistant review process referenced in §3
- [../architecture/greenfield-mandate.md](../architecture/greenfield-mandate.md)
