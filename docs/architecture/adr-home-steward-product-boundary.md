# ADR: Home Steward Product/Domain Definition and Boundary

> **Document status: Canonical ADR.**
> Status: **Accepted** 2026-11-05. Records **DL-131** (issue **#206**, Governance Review, formal
> acceptance review PASS, following one bounded Owner clarification confirming **DL-93**'s Person-only
> General Reasoning authorization is unchanged).
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Terminology: [../models/glossary.md](../models/glossary.md).

---

## Status

**Accepted 2026-11-05.** This ADR fills a gap three other accepted documents explicitly and
repeatedly left open:

- **DL-93** (`adr-reasoning-provider-strategy.md`, Accepted, Issue #132) already names "Home Steward,"
  already creates an independent Person-scoped **Allow Home Steward: YES/NO** capability gate, already
  states Home Steward is never inserted into the General Reasoning fallback chain, and its own closing
  comment states: *"Home Steward remains proposed/unaccepted as a complete product boundary; its
  ownership is currently unassigned to any existing issue."*
- **DL-86** (`adr-home-identity-and-home-intelligence-governance.md`, Accepted, Issue #191) names
  "Home Intelligence" as an optional deployment/hosting boundary that may host a Household Knowledge
  Provider pipeline and a Reasoning Provider, explicitly without asserting any relationship to a
  prospective "Home Steward" product.
- `glossary.md`'s own "Home Steward" entry states plainly that *"no existing issue has been identified
  as the owner of Home Steward's product naming, commercial packaging, or information-category
  authorization taxonomy; that governance remains explicitly unassigned pending a future decision."*

This ADR is that decision. It does not authorize, schedule, or require any implementation. No model,
inference engine, vector store, embedding technology, hardware appliance, or on-premises server is
selected or provisioned here.

This ADR creates **no new responsibility**. The seven responsibilities recorded in **DL-01** —
Foundation, Stewardship, Identity, Truth, Continuity, Operational Trust, Concierge — are unchanged.

---

## Decision

**Home Steward is HTBW's locally governed AI knowledge assistant.** It reasons over:

- HTBW/Home Intelligence context supplied through governed boundaries; and
- additional household knowledge the household has explicitly authorized it to consume.

Home Steward exists so that Concierge and other responsible HTBW capabilities may obtain an answer
from authorized household knowledge the Home would otherwise need to ask a Person to provide. **Home
Steward is an AI extension to HTBW. It does not replace HTBW. It does not assume ownership of any HTBW
responsibility merely because AI/LLM reasoning enhances that responsibility.**

### 1. Foundational relationship — Assist, Concierge, Home Steward

Home Assistant Assist remains the household-facing interaction surface. Home Steward does not create a
separate chatbot or competing conversational surface.

```
PERSON -> HOME ASSISTANT ASSIST -> CONCIERGE -> RESPONSIBLE HTBW CAPABILITY / FRAMEWORK RESPONSIBILITY

RESPONSIBLE HTBW CAPABILITY / CONCIERGE
  -> HOME STEWARD
  -> REASONED / KNOWLEDGE RESULT
  -> RESPONSIBLE HTBW CAPABILITY
  -> NORMAL HTBW GOVERNANCE
  -> CONCIERGE / ASSIST RESPONSE OR GOVERNED ACTION
```

Home Steward sits behind Assist rather than replacing it. **Concierge orchestrates across the
Framework. Home Steward reasons across authorized knowledge.** Neither replaces HTBW Framework
responsibilities. Concierge manages household interaction, understands the request/context,
orchestrates appropriate HTBW responsibilities, and asks the Person when human input is genuinely
required. Home Steward supplies AI reasoning and answers from authorized household knowledge to
Concierge or another responsible HTBW capability; it does not own the workflow merely because it
supplied reasoning, and it is never described as HTBW's ultimate decision authority.

### 2. Knowledge versus human intent

**Home Steward may substitute for asking a Person for authorized knowledge.** It may **not**
automatically substitute for asking a Person for: current intent, consent, confirmation, authorization,
approval, disclosure permission, safety confirmation, financial authority, access authorization, or
another human decision — unless current accepted HTBW governance has separately, explicitly delegated
that decision.

| If Concierge/a responsible capability needs... | Then... |
|---|---|
| **Knowledge** (e.g. "when was this Asset purchased," "what does the warranty cover") | Home Steward may answer when within authorized scope |
| **Human intent** (e.g. "should I spend $900," "do you consent," "should I schedule it") | Ask the Person, unless governance has separately delegated the decision |

### 3. Non-regression — existing HTBW ownership does not move

**The introduction of Home Steward does not transfer, narrow, supersede, or reassign any currently
accepted HTBW responsibility.** This explicitly includes Stewardship, calendar functionality, Asset
functionality, Asset document management, email functionality, Room configuration, Person
configuration, Identity, Operational Trust, Concierge, Continuity, Truth, Explainability,
Environment/Exposure, device control, automations/scripts, Communication, Home Assistant integration,
and persistence/retention. **Adding AI does not transfer ownership of an HTBW function to Home
Steward.** A capability may be **HTBW-owned + Home-Steward-enhanced**; that does not make it
Home-Steward-owned.

**Worked example — Asset documents.** HTBW owns Asset identity, Asset relationship, document
association, document management, document storage, document lifecycle, document access governance,
retention, and configuration — all unchanged. Home Steward may extend that capability with semantic
document ingestion, RAG-or-successor retrieval, question answering over document contents,
cross-document reasoning, and knowledge extraction. *"Show me the refrigerator warranty document"* is
ordinary HTBW Asset/document capability; Home Steward is not required. *"Does the refrigerator warranty
cover compressor failure after four years?"* is HTBW Asset context plus Home Steward reasoning over the
authorized document. Asset document management is not moved to Home Steward.

**Worked example — Stewardship and calendar.** Stewardship remains an HTBW function. Calendar
functionality/actions remain HTBW functions. HTBW Stewardship determines that HVAC maintenance is due;
Home Steward may inspect an authorized invoice/service record and report what the manufacturer or
contractor recommended; that knowledge returns to HTBW; HTBW Stewardship determines the obligation;
HTBW governs authorization to create a calendar entry; the existing HTBW capability performs the
calendar action. Home Steward does not become Stewardship and does not become the calendar capability.

**Worked example — email.** Current HTBW ownership of email integration/action semantics is unchanged.
Home Steward may reason over explicitly authorized household correspondence (service-provider,
utility, insurance, maintenance, mortgage, other authorized household mail). Understanding email
content does not grant authority to send, delete, disclose, change permissions on, or act upon it —
those remain governed through existing HTBW/Operational Trust architecture.

### 4. Home Intelligence remains distinct (DL-86 unchanged)

**Home Intelligence** (accepted **DL-86**) remains exactly what it already is: an optional, separately
deployable product/deployment boundary — a "where," not a "what" — that may host the **DL-81**
Household Knowledge Provider pipeline and/or a **DL-93** Reasoning Provider. This ADR does not rename
Home Intelligence, does not redefine its deployment-boundary meaning, and does not reopen its discovery/
trust-establishment mechanics (**#190**). Ordinary questions about the governed operational Home —
*"why are the Den shades closed,"* *"which Rooms are outside their configured environmental
requirements,"* *"when did the Kitchen lights last turn off,"* *"are any Assets exposed to
inappropriate conditions"* — are answered by existing Truth, Stewardship, Environment/Exposure, and
Explainability capability directly, whether or not a Home Intelligence hosting boundary is installed,
and are not routed to Home Steward merely because Home Steward exists. Home Intelligence does **not**
automatically mean household financial records, correspondence, a general document corpus, bank/
credit-card statements, private insurance documents, or other external household knowledge sources —
those are Home Steward's broader, separately-authorized domain.

### 5. General Reasoning remains independent — DL-93 unchanged

**DL-93 is not reopened by this ADR, and its substance is unchanged.** General Reasoning provider
resolution remains exactly **Person → Integration-default → unavailable**. **There is no Room-configured
provider and no Room authorization step for General Reasoning or for Home Steward** — this restates,
and does not narrow, DL-93's own deliberate removal of an earlier draft's Room-level provision, for
exactly DL-93's own stated reason: a Room is spatial/interaction context, never an authorization owner.

**Allow General Questions: YES/NO** and **Allow Home Steward: YES/NO** remain the two independent,
Person-scoped capability gates DL-93 already created; this ADR does not combine them into one "Allow
AI" setting, and a Person may hold any of the four combinations exactly as DL-93 already states.
**Home Steward is not inserted into the General Reasoning fallback chain, and is not made the
mandatory Reasoning provider.** Where DL-93's existing provider-contract and configuration-time
(never runtime-discovered) rules permit it, a household **may** explicitly configure a local Home
Steward AI stack as a Person-specific or Integration-default Reasoning-provider entry — an explicit
configuration choice, evaluated through the same unchanged resolution order as any other configured
provider, never an automatic substitution. A household may therefore legitimately run one configured
provider for General Reasoning (local or cloud) while separately using Home Steward for its
household-knowledge role, or configure the same local stack to serve both roles.

**Reasoning**, **Home Intelligence**, and **Home Steward** remain three distinct concepts, restating
DL-93 unchanged:

- **General Reasoning** (DL-93) — general knowledge questions, conversational wording, summarisation,
  natural-language interpretation, reasoning over explicitly authorized supplied context.
- **Reasoning Provider** (DL-93) — the configured inference provider serving General Reasoning (and,
  optionally, Home Steward).
- **Home Intelligence** (DL-86) — the optional deployment/hosting boundary (a "where").
- **Home Steward** (this ADR) — the governed AI/household-knowledge product/domain extending HTBW (a
  "what," for a specific, authorized-knowledge purpose).

### 6. Home Steward is not the local LLM

Home Steward is the governed product/capability layer around AI reasoning and authorized household
knowledge — potentially including authorized source connections, ingestion, semantic indexing,
retrieval, reasoning, provenance, authorization boundaries, privacy/retention governance, and governed
interaction with HTBW. **The underlying model, inference engine, vector store, embedding model,
hardware appliance, or local AI distribution is replaceable; Home Steward's product/governance identity
survives that replacement.**

### 7. Locality and privacy

**Local** means household-controlled processing inside the governed Home network boundary. Home
Steward does not have to run on the Home Assistant host; a separate private AI appliance inside the
governed Home network boundary satisfies locality. Possible future, independently governed source
connections (NAS/document source, HTBW/Home Assistant, authorized email, authorized financial source,
authorized calendar source) are each independent: **authorization to one source does not imply
authorization to another.** Having access to information for reasoning does **not** imply authority to
disclose it, correlate it with every other source, retain it indefinitely, change it, act upon it, send
it elsewhere, use cloud inference, control the Home, spend money, or communicate externally — each
remains separately governed, restating **DL-34** (disclosure), **DL-41** (capability dependency), and
DL-81's own disclosure clause, unchanged. Operational Trust remains authoritative; privacy/minimization
remain first-class.

### 8. Explicit non-authority list

Home Steward does **not** automatically gain: Home control authority; Stewardship ownership; calendar
ownership; email ownership; Asset ownership; document-management ownership; Identity authority;
Operational Trust authority; consent authority; permission to spend money or initiate financial
transactions; permission to send external communication; permission to disclose private information;
permission to correlate every authorized source with every other; permission to ingest every source;
unlimited retention; cloud-processing permission; or automatic General-Questions authorization for
every Person. None of these is implied merely because AI can technically perform it.

### 9. Home Assistant First preserved

Home Assistant Assist remains the interaction surface. This ADR does not create a parallel voice
stack, a competing conversational UI, duplicate Home Assistant Person/Room/Area models, duplicate HA
operational state, or duplicate service/action mechanisms. Where Home Steward supplies knowledge to an
HTBW capability, HTBW continues to use the appropriate native Home Assistant mechanisms for actual Home
operations.

### 10. Home Steward as an HTBW extension domain, not a dumping ground

A feature belongs in Home Steward when its distinctive responsibility is **AI reasoning over
authorized knowledge**, especially where that knowledge extends beyond the operational Home model or
uses AI to enrich an existing HTBW capability. A feature does **not** belong in Home Steward merely
because it does not fit cleanly elsewhere, uses an LLM, feels "smart," or has unresolved architecture.
When a future requirement does not fit an existing HTBW responsibility: if its core responsibility is
AI reasoning/knowledge, Home Steward may be appropriate; if AI merely assists an existing HTBW
responsibility, ownership stays in HTBW, classified as HTBW-capability-with-Home-Steward-extension; if
neither, it may expose a missing Framework responsibility rather than a Home Steward feature.

### 11. Directional capability families (non-committal)

Potential future capability families: (1) local AI reasoning; (2) household document semantic
ingestion; (3) Asset-document intelligence; (4) household correspondence/email intelligence;
(5) calendar-context reasoning; (6) financial-document and transaction intelligence;
(7) insurance/property-document intelligence; (8) cross-source household questions; (9) HTBW/Home
Intelligence context consumption; (10) AI enhancement of existing HTBW responsibilities. These
establish directional product scope only — not an implementation roadmap, not committed connectors,
not permission to access any source, not permission to act, not permission to use cloud processing.
Each future capability requires normal HTBW governance.

---

## Relationship to DL-81 (Household Knowledge Provider)

**DL-81** (`adr-household-knowledge-provider-governance.md`, Accepted 2026-11-05) defines a
provider-agnostic architectural pipeline: authoritative household sources → governed ingestion/query
connector → extraction and classification → asset/document association (by reference) → indexes and
embeddings → retrieval → a replaceable Reasoning Provider → a **DL-82** provenance-aware answer →
Identity/Operational-Trust-governed disclosure. **Home Steward consumes this pipeline as one capability
it is built on.** This ADR does not alter DL-81's architecture, and DL-81 remains an architectural
boundary/role name, never itself a product name — the same pipeline could, in principle, be consumed
by another product if one were ever accepted; this ADR only accepts that Home Steward is, today, its
household-facing consumer.

---

## Responsibility impact

| Responsibility/concept | Impact |
|---|---|
| Foundation, Stewardship, Identity, Truth, Continuity, Operational Trust, Concierge (DL-01) | Unchanged |
| Home Intelligence (DL-86) | Unchanged; remains an optional deployment/hosting boundary |
| General Reasoning / Reasoning Provider (DL-93) | Unchanged; Home Steward is an optional, explicitly-configured additional provider choice, never an automatic substitute |
| Household Knowledge Provider (DL-81) | Unchanged architecture; now has an accepted household-facing product consumer, Home Steward |
| Decision Trace / provenance (DL-82) | Unchanged; governs every Home Steward answer |
| Asset Intelligence migration (DL-121, DL-52, DL-110) | Unchanged; not reopened |

## Open decisions (not decided here)

- Ingestion/query connector mechanics, indexing/embedding technology, freshness policy (**#186**).
- Home Intelligence discovery/trust-establishment/deployment mechanics (**#190**).
- Finer-grained Home Steward information-category authorization taxonomy (e.g. distinguishing
  maintenance/manual information, Asset records, financial/banking information, insurance/legal
  information, and administrative household information for a specific request) — explicitly **not**
  designed here; remains a future governed decision in combination with Operational Trust's existing
  disclosure-evaluation authority (**DL-34**).
- Household mail, invoice, and financial-record ingestion as an actual connector — a future candidate
  source only, not authorized here.
- MCP transport-preference research (**#185**) — unrelated and untouched.

## Related documents

- [../governance/decision-ledger.md](../governance/decision-ledger.md) — **DL-131**, **DL-81**, **DL-82**, **DL-93**, **DL-86**
- [adr-household-knowledge-provider-governance.md](adr-household-knowledge-provider-governance.md)
- [adr-reasoning-provider-strategy.md](adr-reasoning-provider-strategy.md)
- [adr-home-identity-and-home-intelligence-governance.md](adr-home-identity-and-home-intelligence-governance.md)
- [../models/decision-trace.md](../models/decision-trace.md) — Source-class provenance, **DL-82**
- [../models/glossary.md](../models/glossary.md)
- [concierge-philosophy.md](concierge-philosophy.md)
- [../patterns/ai-assisted-actions.md](../patterns/ai-assisted-actions.md)
