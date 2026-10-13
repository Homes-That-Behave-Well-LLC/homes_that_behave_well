# ADR: Household Knowledge Provider Governance

> **Document status: Active — subordinate to the HTBW canonical architecture.**
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Drafts decision **DL-81**, recorded pending formal acceptance review at **Issue #188**.
> **Not yet authoritative.** Creates no new responsibility.
> Terminology: [../models/glossary.md](../models/glossary.md).

---

## Status

**Recorded, pending formal acceptance review (Issue #188). Not yet authoritative.**

Drafted by the 2026-10 AI, Natural Interaction, and Household Knowledge Architecture Review, which
found no current-authority document governing household document and knowledge retrieval for AI-
assisted answers. This ADR proposes to close that gap at the architecture level, consistent with this
repository's established practice that a drafted decision is recorded first and separately undergoes
formal acceptance review before being treated as binding (see *Notes on the custody and obligation-
lifecycle decision* in [../governance/decision-ledger.md](../governance/decision-ledger.md) for the
precedent). **It does not authorize, schedule, or require any implementation**, whether or not it is
later formally accepted. No ingestion connector, index, embedding technology, vector store, or
on-premises server is built, selected, or provisioned by this ADR.

This ADR creates **no new responsibility**. The seven responsibilities recorded in **DL-01** —
Foundation, Stewardship, Identity, Truth, Continuity, Operational Trust, Concierge — are unchanged.
Explainability and the Decision Trace are unchanged. **OD-67** (Reasoning Provider Strategy) is
unchanged and remains open.

---

## Context

Residents should eventually be able to ask natural-language questions whose answer depends on
household documents and records — *"what's the warranty on the water heater?"*, *"when was the
furnace last serviced?"* — not only on live device state. No current-authority document described how
such a question is answered without either (a) treating a reasoning provider as though it were
household memory, or (b) building a second, competing document or asset catalog.

The historical Household Memory ADR, Household Memory Contract, and Household Memory Model
(`adr-household-memory-governance.md`, `../contracts/household-memory-contract.md`,
`../models/household-memory-model.md`) define a governed artifact and explanation boundary, but predate
the refoundation, are superseded, and do not define an ingestion → indexing → retrieval pipeline. The
Knowledge Briefing Status Synthesis Contract and Briefing Composition Model cover household briefings,
not general document retrieval. Asset Intelligence (`foundation-contract.md`, `../contracts/
stewardship-contract.md`) already owns asset identity and asset-to-document relationships in its
current, shipped implementation (`document_models.py`, `document_resolver.py`), and
[connected-storage.md](connected-storage.md) already owns original-document persistence. Neither of
those boundaries is reopened here.

---

## Decision

**A Household Knowledge Provider boundary is proposed as future architecture, bounded by the
following pipeline:**

```
authoritative household sources (Asset Intelligence, Document Storage, Truth, Stewardship)
  -> governed ingestion or query connector
  -> extraction and classification
  -> asset/document association (consumed from Asset Intelligence, never duplicated)
  -> structured indexes and embeddings
  -> retrieval
  -> replaceable Reasoning Provider (OD-67)
  -> provenance-aware answer (see decision-trace.md, Source-class provenance, DL-82)
  -> Identity- and Operational-Trust-governed disclosure or action
```

### 1. Household knowledge is durable; the reasoning provider is replaceable

Restating the existing **OD-67** invariant without narrowing it: *"a model is replaceable. No
architecture may depend on one provider's behaviour."* The Household Knowledge Provider's indexes,
embeddings, and extracted associations are household-owned artifacts that must survive a reasoning-
provider replacement. **A future change of reasoning provider must never require re-deriving household
knowledge from nothing**, though re-embedding against a new provider's embedding space is an
implementation detail, not an architectural dependency.

### 2. No competing asset catalog or document repository

The Household Knowledge Provider **consumes** Asset Intelligence's asset-to-document relationships and
**consumes** existing Document Storage (the household NAS and any other authoritative original-
document location) by reference. It never becomes a second authority for an asset's identity, for an
asset-to-document relationship, or for a document's original content. **A document's original-source
system remains authoritative for that document.** Extraction, classification, and indexing produce
*derived* artifacts (text, embeddings, structured metadata) that reference their source; they are not
a second original.

### 3. Local and cloud reasoning providers both remain possible

Per **OD-67**, the Household Knowledge Provider's reasoning step is provider-agnostic. The same
household functions must be able to use a local provider, an authorized external cloud provider, or a
hybrid routing between them, without redesigning the pipeline above. **No step in this pipeline
requires cloud AI, and no step prohibits it** — the choice is **OD-67**'s, not this ADR's.

### 4. Deterministic behavior continues without a reasoning provider

Where no reasoning provider is configured or available, retrieval may still answer a bounded,
structured question directly from the indexed metadata (for example, "which documents are associated
with this asset?") exactly as Concierge already degrades gracefully elsewhere (see
[failure-and-degradation.md](failure-and-degradation.md)). **The Household Knowledge Provider is not a
dependency a deterministic HTBW capability may silently require.**

### 5. A future on-premises AI server is a candidate host, not a mandate

The future household data-closet server referenced in household planning discussion may conceptually
host local inference, ingestion, extraction, embeddings, and indexes for this pipeline. **This ADR
selects no hardware, no operating system, no model, no vector database, and no orchestration platform,
and it does not require V1 to deploy one.** Any such server is one possible execution host for the
pipeline above (see **DL-50**'s existing execution-host declaration pattern); it is never a second
architectural authority.

### 6. Provenance is mandatory, not optional

Every answer this pipeline produces is subject to [decision-trace.md](../models/decision-trace.md)'s
*Source-class provenance for AI-assisted and document-grounded explanations* (**DL-82**). An answer
that cannot be attributed to a source class, or that cannot honestly state insufficient evidence, is
not a conforming answer.

### 7. Disclosure is Identity- and Operational-Trust-governed, not retrieval-governed

Retrieval answers **what can be found**; it never answers **who may be told**. Every retrieved answer
passes through the same Identity and Operational Trust disclosure rules as any other sensitive
content before it reaches a resident — explicitly including household invoices, financial records, and
any other content a household would not consider disclosable to every audience. Household mail,
invoices, and financial records are **future candidate sources only**; no mailbox or financial
connector is implemented, scheduled, or authorized by this ADR.

---

## Responsibility impact

| Responsibility | Impact |
|---|---|
| Foundation | Unchanged. Continues to own descriptive asset and household knowledge |
| Asset Intelligence (product) | Unchanged. Remains the authoritative owner of asset identity and asset-to-document relationships, consumed by reference (**OD-20**) |
| Truth | Unchanged. A retrieved document is not a Truth Fact; where retrieval corroborates a Fact, Truth's own provenance rules apply unchanged |
| Concierge | Gains an additional consulted capability (retrieval) under the same orchestration, conflict-resolution, and Decision Trace rules already in [concierge-contract.md](../contracts/concierge-contract.md) |
| Operational Trust | Unchanged. Continues to gate disclosure and action; retrieval never bypasses it |
| Identity | Unchanged. Continues to determine who is asking and who may be told |
| Explainability / Decision Trace | Extended by **DL-82**, not replaced |

---

## Open decisions

The following implementation-shaping questions are genuinely unresolved and are **not** decided by
this ADR. They are routed to a new non-decision research item (see the Open-Issue Impact Review in the
governing review report) rather than answered here:

- The governed ingestion/query connector mechanism and its ownership boundary with Asset Intelligence
  and Document Storage.
- Indexing and embedding technology selection.
- Document freshness, change-detection, and re-indexing policy.
- Retention and custody of derived artifacts (extracted text, embeddings) relative to the original
  document's own retention — see **OD-85** for the adjacent adoption/custody question.
- Whether URL-sourced (externally hosted) documents are locally cached, and the associated vendor-
  disappearance and copyright questions raised in the governing review.
- Household mail, invoice, and financial-record ingestion as a future source — explicitly **not**
  decided or authorized here.

---

## Consequences

- If formally accepted, HTBW gains an architecturally sound, non-duplicative place to put future
  document- and knowledge-retrieval capability, without inventing a second asset catalog, a second
  document store, or a reasoning-provider dependency.
- No implementation obligation is created either way. V1 may ship with this ADR drafted but not yet
  formally accepted, or accepted, and zero lines of retrieval code in either case.
- Future closure of the open decisions below must preserve every invariant in **OD-67** and this ADR's
  Decision section, regardless of this ADR's own acceptance status at that time.

---

## Related documents

- [../governance/decision-ledger.md](../governance/decision-ledger.md) — **DL-81**
- [home-assistant-boundary.md](home-assistant-boundary.md)
- [connected-storage.md](connected-storage.md)
- [failure-and-degradation.md](failure-and-degradation.md)
- [../models/decision-trace.md](../models/decision-trace.md) — *Source-class provenance*, **DL-82**
- [../models/truth.md](../models/truth.md)
- [adr-generated-behavior-authoring-governance.md](adr-generated-behavior-authoring-governance.md)
- [../contracts/foundation-contract.md](../contracts/foundation-contract.md)
- [../contracts/stewardship-contract.md](../contracts/stewardship-contract.md)
