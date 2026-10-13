# ADR: Generated Behavior Authoring Governance

> **Document status: Active — subordinate to the HTBW canonical architecture.**
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Drafts decision **DL-83**, recorded pending formal acceptance review at **Issue #188**.
> **Not yet authoritative.** Creates no new responsibility.
> Terminology: [../models/glossary.md](../models/glossary.md).

---

## Status

**Recorded, pending formal acceptance review (Issue #188). Not yet authoritative.**

Drafted by the 2026-10 AI, Natural Interaction, and Household Knowledge Architecture Review, which
found no current or historical document governing what happens when a natural-language request asks
the Home to change its own future behavior (*"do that every evening at sunset when I'm here"*), as
distinct from an ordinary one-time action. This ADR proposes the **governance lifecycle boundary**
that would prevent silent, ungoverned persistent change. Consistent with this repository's
established practice that a drafted decision is recorded first and separately undergoes formal
acceptance review before being treated as binding (see *Notes on the custody and obligation-lifecycle
decision* in [../governance/decision-ledger.md](../governance/decision-ledger.md)), this ADR is
**not yet authoritative** and must not be cited as equivalent to an accepted ADR until #188 records a
result. **It does not decide implementation mechanics** — versioning, conflict detection with existing
native automations, or a storage shape — which remain open regardless of this ADR's eventual
acceptance status (see below).

This ADR creates **no new responsibility**. Concierge continues to decide what should happen now,
including what should happen in the future; Operational Trust continues to own authorization;
Home Assistant continues to own the native automation, script, scene, and blueprint execution
substrate ([home-assistant-boundary.md](home-assistant-boundary.md), *Native automations, scripts, and
scenes*). **OD-66** (Delegation Boundary for External Adaptive Behaviour) is unchanged and governs a
different question — a *third party's* autonomous policy engine, not HTBW- or resident-directed
authoring of HTBW's or Home Assistant's own behavior. **OD-67** is unchanged and governs the reasoning
provider used, where one is consulted, to help generate a candidate.

---

## Context

A request may ask for one of three materially different things, and current architecture does not
distinguish them explicitly:

1. **A one-time desired outcome** — "turn the lights down now." Already fully governed by Concierge's
   existing orchestration, permitted-outcomes, and conflict-resolution rules
   ([concierge-contract.md](../contracts/concierge-contract.md) §6–§8). Nothing new is required.
2. **A reusable scene proposal** — a candidate grouping of settings Concierge or a Reasoning Provider
   proposes, that is **not** yet persisted and has no effect until separately invoked or confirmed.
3. **A persistent behavioral change** — a request that creates, modifies, or retires a standing rule
   governing *future* Home behavior (a native automation, script, scene, or an HTBW-equivalent
   persistent rule). **This is the case with no existing governance**, and the one this ADR addresses.

Generative authoring is capable of producing (2) or (3) from natural language. Executing (3) without
explicit governance would let an ungoverned process silently rewrite the Home's own future behavior —
exactly what **OD-67**'s invariants ("a recommendation never silently becomes an authorised action")
and the Representation Strategy's "Deletion is directional" discipline
([home-assistant-boundary.md](home-assistant-boundary.md)) already exist to prevent in adjacent cases.

---

## Decision

**A persistent behavioral change must follow this lifecycle, and no stage may be skipped or silently
collapsed into another:**

```
Generate -> Validate -> Explain -> Authorize -> Persist -> Observe -> Review -> Revise or Retire
```

| Stage | Requirement |
|---|---|
| **Generate** | A candidate persistent behavior is proposed, bounded strictly to capabilities, entities, Rooms, and vocabulary already known to HTBW and Home Assistant. **No fabricated device, capability, or entity is ever proposed** — restating the existing **OD-67** invariant unchanged |
| **Validate** | The candidate is checked against currently available capabilities and entities, applicable Operational Trust policy, and detectable conflicts with existing behavior. An invalid candidate is rejected before it reaches the resident, with an honest reason |
| **Explain** | Before anything persists, the resident receives a plain explanation of **what will change** — the trigger, the condition, and the action — sufficient to decide whether to authorize it. An unexplained persistent change is never authorized |
| **Authorize** | Operational Trust evaluates the request exactly as it evaluates any other action-risk class ([operational-trust-contract.md](../contracts/operational-trust-contract.md)), and the resident's explicit authorization is captured. **A proposal is never silently promoted to persistent** |
| **Persist** | The authorized behavior is written through the owning responsibility's governed interface, preferring a native Home Assistant representation (automation, script, scene, or blueprint) under the existing Representation Strategy (**DL-31**) rather than a parallel HTBW store. The authoring act itself produces a Decision Trace, because it is a decision HTBW and the resident made together |
| **Observe** | Each subsequent native execution of the persisted behavior is an ordinary Domain Event under *Native automations, scripts, and scenes* ([home-assistant-boundary.md](home-assistant-boundary.md)) — **not** a fabricated Decision Trace for a decision HTBW did not make at execution time. The authoring decision and its ongoing executions are distinct records, exactly as existing doctrine already requires |
| **Review** | The household may revisit an authored behavior at any time; periodic or resident-triggered re-confirmation is a candidate pattern, not decided here |
| **Revise or Retire** | A change or withdrawal follows the same Generate→Authorize sequence as creation, and withdrawal follows the existing "deletion is directional" discipline — a retired behavior's history is preserved, never silently erased ([home-assistant-boundary.md](home-assistant-boundary.md), *Representation strategy*) |

**No stage of this lifecycle may be bypassed by a Reasoning Provider's confidence, by phrasing that
sounds authoritative, or by repetition of a request.** A reasoning-provider suggestion at the Generate
stage remains a suggestion — per **OD-67** and [decision-trace.md](../models/decision-trace.md)'s
*Source-class provenance* (**DL-82**) — until it has passed Validate, Explain, and Authorize.

---

## Responsibility impact

| Responsibility | Impact |
|---|---|
| Concierge | Gains the lifecycle above as the governing sequence for any persistent-behavior request; one-time outcomes are unaffected |
| Operational Trust | Authorizes persistent behavioral change using its existing action-risk and authorization model; no new authorization mechanism is created |
| Home Assistant | Remains the preferred execution and storage substrate for the persisted behavior (native automation/script/scene/blueprint); not duplicated |
| Explainability / Decision Trace | The authoring act is traced; routine subsequent executions remain Domain Events, not traces, per existing doctrine |

---

## Open decisions

Not decided by this ADR, and routed to a new non-decision research item rather than answered here:

- Versioning and rollback mechanics for a persisted, authored behavior.
- Conflict detection between an authored behavior and a household's own pre-existing native
  automations, beyond the Validate stage's existence requirement.
- The Review stage's cadence and surface (periodic prompt, dashboard list, or otherwise).
- Whether a declined or superseded proposal is retained, and for how long.

---

## Consequences

- If formally accepted, natural-language requests that change future Home behavior gain an explicit,
  bounded governance lifecycle, closing a gap the original architecture review identified as a
  genuine absence.
- No implementation is required or authorized by this ADR, whether drafted or later formally
  accepted. A V1 release may ship with this ADR in either state while implementing none of its
  stages, provided no natural-language persistent-behavior authoring ships ahead of formal
  acceptance.
- Any future implementation of this lifecycle must preserve **OD-66** and **OD-67**'s invariants
  unchanged, regardless of this ADR's acceptance status at that time.

---

## Related documents

- [../governance/decision-ledger.md](../governance/decision-ledger.md) — **DL-83**
- [home-assistant-boundary.md](home-assistant-boundary.md) — *Native automations, scripts, and scenes*;
  *Representation strategy*
- [../contracts/concierge-contract.md](../contracts/concierge-contract.md)
- [../contracts/operational-trust-contract.md](../contracts/operational-trust-contract.md)
- [../models/decision-trace.md](../models/decision-trace.md) — *Source-class provenance*, **DL-82**
- [adr-household-knowledge-provider-governance.md](adr-household-knowledge-provider-governance.md)
