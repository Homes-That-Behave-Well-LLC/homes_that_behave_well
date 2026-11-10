# ADR: HTBW Core Constitutional Refoundation

> **Document status: Canonical (constitutional) ADR.**
> Status: **Accepted**. Supersedes the four-service platform model.
> Terminology: [../models/glossary.md](../models/glossary.md).
>
> **Annotated 2026-11-10 by DL-153 (Issue #214); the text below is historical and is not rewritten.**
> "HTBW Core" here named the architecture and the product together. Read the seven responsibilities as
> the **seven layers of the BehavesWell Core architectural stack** — **Layer 0 Foundation** plus the
> **six BehavesWell Framework stages** (Truth, Identity, Operational Trust, Stewardship, Continuity,
> Concierge, in that order). Foundation is not a Framework stage. Every ownership decision here stands;
> the table's numbering and order are the pre-DL-153 presentation. The product is now **BehavesWell
> Core, Home Assistant Edition**. See
> [adr-behaveswell-framework-foundation-core-edition-and-context-identity.md](adr-behaveswell-framework-foundation-core-edition-and-context-identity.md).

---

## Context

The HTBW documentation had grown from three reference implementations — Asset Intelligence, Voice
Identity, and Concierge — and from a video-series framework that continued to evolve. The result was a
repository that described a **four-service platform** in some places, a set of Concierge-centric
contracts in others, and a growing collection of exploratory documents that contradicted both.

Fifteen structural contradictions were identified, including:

- Voice Identity asserted as a platform service and product boundary
- "Foundation owns truth" asserted in five documents
- An explicit prohibition — "no fifth platform service is introduced" — that blocked Truth, Continuity,
  Operational Trust, and Stewardship from existing at all
- Asset Intelligence positioned as the platform layer answering *what matters*
- Stewardship and Operational Trust absent entirely
- A terminology fork across Room, Composite Room, Merged Room, Interaction Space, Listening Area,
  Operational Space, and Space
- Ambiguous ownership of Room Configuration and vocabulary
- No Decision Trace model, no glossary, no assessment traceability

A repository cannot govern implementation if it contradicts itself.

---

## Decision

**HTBW Core is defined by seven responsibilities.**

| # | Responsibility | Question |
|---|---|---|
| 1 | Foundation | What exists, and how do we describe it? |
| 2 | Stewardship | What matters, and what must be cared for? |
| 3 | Identity | Who do we believe this is? |
| 4 | Truth | What is actually true now? |
| 5 | Continuity | What should be remembered, resumed, or transferred? |
| 6 | Operational Trust | What is allowed? |
| 7 | Concierge | What should happen now? |

Additionally:

1. **Human Trust is an outcome, not a layer.** It emerges when the home behaves predictably and
   explains itself. It cannot be implemented directly.
2. **Behavioral Governance is cross-cutting, not a layer.**
3. **Layers are not products.** A responsibility may be implemented by one integration, several, or
   part of one.
4. **Concierge orchestrates. It does not own everything it consumes.**
5. **Explainability is a required output of the framework**, expressed as the Decision Trace.
6. **HTBW Core is greenfield.** No compatibility requirement exists with the reference
   implementations.
7. **The framework is vendor-agnostic.** Home Assistant is the first implementation environment, not a
   constraint on the architecture.
8. **A learned suggestion is not an autonomous policy.**
9. The **authority order** in [../governance/authority-order.md](../governance/authority-order.md)
   governs all future conflicts.

---

## Consequences

### Superseded

- The four-service platform model, and every statement of the form "HTBW is a four-service platform"
- The prohibition "no fifth platform service is introduced"
- Voice Identity as a platform-service boundary — see
  [adr-identity-replaces-voice-identity-boundary.md](adr-identity-replaces-voice-identity-boundary.md)
- "Foundation owns truth" — see [adr-truth-as-fact-engine.md](adr-truth-as-fact-engine.md)
- Asset Intelligence as the HTBW Core layer answering *what matters*
- "Composite Room", "Operational Space", "Interaction Space", "Listening Area", and bare "Space"

### Established

- Twelve canonical architecture documents, thirteen canonical models, nine canonical contracts, an
  assessment traceability model, four governance documents, and a canonical scenario set
- Principles **P1–P26** in [principles.md](principles.md)
- A glossary that every canonical document is bound to
- A decision ledger recording both what was decided and what remains open

### Not changed

- Asset Intelligence, Voice Identity, and Concierge remain **separate released products** with their
  own lifecycles. **No runtime code was modified, and no compatibility requirement was created.**
- The discoveries made in those products are carried forward deliberately and credited in
  [greenfield-mandate.md](greenfield-mandate.md).

> **Amended 2026-08-26 by DL-51.** The first bullet recorded the state of the portfolio at
> refoundation and stated one disposition for three products. **Disposition is now stated per
> product**: Asset Intelligence remains a released standalone integration and is never a required
> dependency of HTBW, while the standalone Voice Identity and Concierge integrations will **sunset**
> with their responsibilities unchanged. **The second half of the bullet is unchanged in force** — no
> compatibility requirement was created then, and none is created by sunset or by adoption
> (**DL-19**). This annotation records the amendment; **the original text is preserved as
> architectural evidence and is not rewritten.** See
> [adr-product-disposition-and-legacy-adoption.md](adr-product-disposition-and-legacy-adoption.md).

### Costs accepted

- A large documentation diff, including status banners on pre-refoundation files
- Thirty-two deliberately open decisions, recorded rather than invented
- Some pre-refoundation documents now read as evidence rather than as instruction

---

## Alternatives considered

| Alternative | Why rejected |
|---|---|
| Patch the contradictions in place | The contradictions were structural, not editorial. Patching would have preserved a model that cannot express Stewardship, Truth, or Operational Trust. |
| Extend the four-service model with a fifth service | The four-service model prohibits it explicitly, and the framework has seven responsibilities, not five. |
| Treat Concierge as the platform and everything else as plugins | This is the ownership confusion the refoundation exists to remove. |
| Delete superseded documents | Destroys architectural evidence. Supersession with banners preserves it. |

---

## Related documents

- [north-star.md](north-star.md)
- [framework.md](framework.md)
- [principles.md](principles.md)
- [greenfield-mandate.md](greenfield-mandate.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
