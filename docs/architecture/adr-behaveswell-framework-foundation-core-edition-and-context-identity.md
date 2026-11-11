# ADR: BehavesWell Framework, Foundation, Core, Edition, and Context Identity

> **Document status: Canonical ADR (constitutional).**
> Status: **Accepted** 2026-11-10. Records **DL-153** (issue **#214**; Owner decisions supplied directly
> by the Owner as the governing outcome, following the repository-grounded Phase 1 governance finding
> **C** recorded on #214).
> Canonical authority: [north-star.md](north-star.md), [framework.md](framework.md), and
> [../models/glossary.md](../models/glossary.md).
> Terminology: [../models/glossary.md](../models/glossary.md).

---

## Status

**Accepted 2026-11-10.** This ADR makes six Owner decisions authoritative:

1. the **BehavesWell Framework** consists of **six stages**;
2. **Foundation** is **Layer 0**, the platform substrate, and not a Framework stage;
3. **BehavesWell Core** is the product that applies the Framework over a Layer 0 Foundation;
4. an **Edition** identifies the Layer 0 Foundation platform — the current and only edition is
   **BehavesWell Core, Home Assistant Edition**;
5. **Homes That Behave Well** remains the residential research, education, evidence, and lived-outcome
   ecosystem;
6. **BehavesWell Extended Intelligence** is the successor product name for the existing Home Steward
   product (**DL-131**) — a rename of one product, not a new one.

It also governs the **backward-compatible public rename** from *HTBW Core* to *BehavesWell Core*.

**No responsibility is created, removed, merged, or reassigned. No runtime behavior changes. No stable
technical identifier changes. No installed data is migrated.**

---

## Context

The Phase 1 grounding review on **#214** found this to be a material architecture decision (finding
**C**), not a terminology clarification:

| # | Evidence |
|---|---|
| 1 | **DL-01** and [adr-htbw-core-refoundation.md](adr-htbw-core-refoundation.md) used *HTBW Core* for the seven-responsibility architecture itself, while `manifest.json` and `hacs.json` used *HTBW Core* as the Home Assistant integration's display name. One name had two referents. |
| 2 | [north-star.md](north-star.md) described *HTBW* as both the framework and the platform. |
| 3 | [../governance/public-claim-register.md](../governance/public-claim-register.md) **F8** recorded that no repository document stated the distinction between the platform-neutral Framework and the platform-specific software, and routed it *"repository first"*. **F1** and **F6** recorded that public material presents a six-responsibility Framework with Truth first, while the repository presented seven with Foundation first. |
| 4 | Product identity is a ledger decision in this repository (**DL-86**, **DL-131**). |
| 5 | Three different responsibility orders were in use in repository documents (DL-01; issue #202 and the UX/IA document §24; the UX/IA document §9 and the Season 1 baseline). |

The public **BehavesWell Framework Specification v1.0** (September 2026) already defines a
platform-neutral Framework for *intelligent environments* with six responsibilities, in the order
Truth, Identity, Operational Trust, Stewardship, Continuity, Concierge, and names Homes That Behave
Well, Buildings That Behave Well, and Spaces That Behave Well as founding contextual research
programs.

---

## Decision

### 1. The BehavesWell Framework has six stages

> **"The BehavesWell Framework consists of six stages: Truth, Identity, Operational Trust,
> Stewardship, Continuity, and Concierge. BehavesWell Core applies those six stages over a Layer 0
> Foundation supplied by the implementation platform. Foundation is part of the complete BehavesWell
> Core architectural stack, but it is not a seventh stage of the BehavesWell Framework."**

| # | Framework stage | Question answered |
|---|---|---|
| 1 | **Truth** | What is actually true now? |
| 2 | **Identity** | Who do we believe this is? |
| 3 | **Operational Trust** | What is allowed? |
| 4 | **Stewardship** | What matters, and what must be cared for? |
| 5 | **Continuity** | What should be remembered, resumed, or transferred? |
| 6 | **Concierge** | What should happen now? |

This is the **Framework stage order**: how the Framework is taught, assessed, and presented. It is
**not** the dependency order ([dependency-view.md](dependency-view.md)) and **not** the runtime
sequence ([runtime-sequence.md](runtime-sequence.md)), and it must not be reordered to match either.

**Each Framework stage is also an architectural responsibility** with an owner, a contract, and models.
"Stage" names a stage's place in the Framework; "responsibility" names its ownership boundary. Every
stage's accepted repository meaning, ownership, contract, and model are **unchanged** by this
decision. In particular, Operational Trust still answers *"What is allowed?"* and Continuity still
does not own a central history. Where the public v1.0 wording differs, see §12.

**Human Trust remains an outcome, not a stage, layer, or responsibility (P19, DL-02).** Behavioral
Governance, Explainability, and the other cross-cutting areas remain cross-cutting (DL-03, DL-15).

### 2. Foundation is Layer 0

**Foundation is Layer 0: the platform substrate on which the six-stage BehavesWell Framework is
applied.** It is **not** a seventh Framework stage and must never be described as the first of seven
Framework responsibilities.

The complete **BehavesWell Core architectural stack** has **seven layers**:

```text
Top
  6  Concierge
  5  Continuity
  4  Stewardship
  3  Operational Trust
  2  Identity
  1  Truth
  0  Foundation
Bottom
```

Shown vertically, Foundation is at the bottom and Concierge is at the top. The canonical counts are
always stated as **six Framework stages**, **Layer 0 Foundation**, and **a seven-layer BehavesWell Core
stack**.

**Foundation answers the implementation-level question:**

> *What platform model and native capabilities provide the substrate on which BehavesWell Core applies
> the Framework?*

The descriptive guarantee in [../contracts/foundation-contract.md](../contracts/foundation-contract.md)
— *what exists, and how do we describe it* — is what Layer 0 provides to the six stages.

**Foundation's accepted ownership is unchanged and is restated as Layer 0.** Every definition and model
already accepted as Foundation's remains Foundation's:

- the canonical object-type definitions (Home, Physical Room, Room, Merged Room, Person, Pet, Asset
  reference, Fact, Policy, Obligation, and the rest listed in [framework.md](framework.md));
- **Room Configuration** and **Contextual Vocabulary** (**DL-09**, **DL-10**);
- the descriptive asset model (**DL-08**);
- the shared temporal model and the communication model;
- the definitional relationship in which Foundation defines what a Fact is and Truth decides what is
  factual now (**DL-04**).

**In the current edition, Home Assistant supplies Layer 0**: its registries, Areas, Floors, People,
Devices, Entities, Labels, Assist, config entries, and platform mechanics. **BehavesWell Core extends
that substrate natively** ("Native First. Native Extended."). The Foundation-owned models above are
BehavesWell Core's governed Layer 0 extensions. They reference native objects and never copy them
(**DL-31**), and they never replace Home Assistant authority over native concepts.

Dependency rule 6 in [dependency-view.md](dependency-view.md) is unchanged: Foundation feeds everything
and consumes nothing.

### 3. BehavesWell Core extends Home Assistant

For the current implementation:

- **Home Assistant supplies Layer 0 Foundation.**
- **BehavesWell Core extends Home Assistant.** It does not replace or compete with Home Assistant
  (**P21**, **DL-16**, **DL-30**).
- **Home Assistant remains authoritative** for its native platform concepts, registries, interaction
  patterns, and platform mechanics (**DL-31**, **DL-42**).
- **Native Experience** is unchanged (**DL-18**, **P23**).

This records, in the repository, the scope distinction **F8** said was missing:

- the **BehavesWell Framework is platform-neutral** (**DL-20**, **P25**);
- **BehavesWell Core, Home Assistant Edition is Home Assistant-first**.

### 4. Foundation portability

The BehavesWell Framework is not inherently limited to Home Assistant. Another platform may
potentially supply Layer 0 through a **separately governed edition**. Josh.ai, Control4, and Homey are
**illustrative examples only**.

This decision:

- does **not** claim that any named platform currently satisfies the BehavesWell Foundation contract;
- does **not** claim that current Home Assistant code runs on another platform;
- does **not** authorize, schedule, or commit to any other edition.

**Each Foundation platform requires its own governed implementation, mapping, compatibility review,
and acceptance.** **No edition may weaken or redefine the six Framework stages to fit its platform.**

### 5. BehavesWell Core is the product

**BehavesWell Core** is the governed software implementation of the BehavesWell Framework over an
eligible Layer 0 Foundation:

- one product identity shared across editions;
- **not** the Framework itself;
- **not** a Framework stage or a layer;
- not permanently tied to one environment type;
- does **not** own every BehavesWell-related product.

Products and capabilities that remain distinct from BehavesWell Core:

| Name | Classification | Governing record |
|---|---|---|
| **HTBW Voice Evidence** App | Independent, separately installed product; a voice-evidence provider. **Voice Evidence is not Identity** — Identity alone resolves who a person is | **DL-50**, **DL-90**, [../contracts/identity-contract.md](../contracts/identity-contract.md) |
| **BehavesWell Extended Intelligence** (formerly **Home Steward**) | Independent, separately installed private/local reasoning product over explicitly authorized sources; an extension of authorized *reasoning context*, never of operational authority | **DL-131** (product boundary, recorded under its former name); successor name by **DL-153** |
| **Home Intelligence** | Optional deployment/hosting boundary capability concerning intelligence about the Home; never required by Core | **DL-86** |
| **General Reasoning** | A configured Reasoning capability that may reason but never govern | **DL-93** |
| **Asset Intelligence** | Separately released predecessor product; optional one-time adoption source only | **DL-51**, **DL-52**, **DL-121** |

The App keeps the name **HTBW Voice Evidence**.

> **Annotated 2026-11-10 by DL-154 (Issue #216).** The Owner subsequently renamed the App's public
> identity to **BehavesWell Voice Evidence** (the **BehavesWell Voice Evidence App**). It is the same
> product, and every technical identifier is unchanged. The sentence above records DL-153 as accepted.
> See [adr-behaveswell-voice-evidence-product-identity.md](adr-behaveswell-voice-evidence-product-identity.md).

**BehavesWell Extended Intelligence is the Owner-directed successor product name for the existing,
governed Home Steward product (DL-131).** It is a **rename of one product identity, not a second
product**: *Home Steward* is the former/working name, and *BehavesWell Extended Intelligence* is the
public-facing name. DL-131's accepted boundary applies unchanged under the new name:

- it is an independent product, **not** a Framework stage, **not** Layer 0 Foundation, **not** part of
  BehavesWell Core, and **not** a BehavesWell Core Edition;
- it is **not Stewardship** — the rename deliberately removes the *Home Steward* / *Stewardship*
  semantic collision — and it is **not** Concierge, **not** Home Intelligence, and **not** General
  Reasoning;
- **"Extended" describes extension of authorized reasoning context, not of operational authority.**
  Connecting more sources grants it no additional authority. Operational Trust and every other
  governed authorization boundary continue to apply (DL-131's explicit non-authorities stand);
- it may serve as a configured provider or source for a capability only where separately authorized
  and architecturally permitted (for example as a **DL-93** Reasoning Provider entry, under DL-93's
  unchanged resolution order). It is never collapsed into the Home Intelligence capability, and it
  may optionally be hosted within the DL-86 boundary as DL-131 already states.

**Formal branded notation:** **BehavesWell © Extended Intelligence**, under the same © rules as §10.

**Historical text that says "Home Steward" is retained and annotated**, not rewritten — including the
DL-131 row, [adr-home-steward-product-boundary.md](adr-home-steward-product-boundary.md) and its
filename, and DL-85's annotated disclosure toggle. **This decision does not rename the Home Steward
repository** or any of its technical identifiers, filenames, paths, namespaces, APIs, or persisted
identifiers. That rename is separate follow-on implementation work in that repository.

This decision renames the Core product and records the Extended Intelligence successor name. No other
product is renamed.

### 6. The Edition model

An **Edition** identifies the Layer 0 Foundation platform on which BehavesWell Core runs:

- all editions share the BehavesWell Core product identity;
- edition-specific behavior and integration are governed separately per edition;
- editions do **not** receive unrelated product logos merely because the Foundation changes.

**The current and only edition is BehavesWell Core, Home Assistant Edition.**

- *"BehavesWell Core"* is the product; *"Home Assistant Edition"* identifies the Foundation
  implementation.
- Public product language spells out **"Home Assistant"** in full. **"HA Edition" is never the primary
  public name.**
- *"BehavesWell Core, Josh.ai Edition"*, *"… Control4 Edition"*, and *"… Homey Edition"* are
  architecture-explanation examples only. They must not be created, announced, documented as
  available, or implied as delivery commitments.

**Scope of the current edition.** BehavesWell Core, Home Assistant Edition is the initial governed
implementation that extends Home Assistant by applying the Framework to the Home Assistant environment
and to the People, Places, Assets, relationships, evidence, permissions, obligations, continuity, and
interactions understood within it. The table below states its **product direction**. Each row must be
read with the accepted / implemented / open distinction:

| Direction | Status today |
|---|---|
| Extending Home Assistant People through governed Identity, Truth, Operational Trust, Continuity, and Concierge relationships | **Accepted architecture**; Voice Evidence runtime foundation only implemented (#162); enrollment and matching open (#163–#167, #212) |
| Extending Home Assistant spatial concepts into Places, including Rooms and Merged Rooms | **Accepted** (DL-09, DL-67, DL-68); household entry with Room subentries **implemented** (v0.2.0) |
| Extending the device-centric model into Assets, including non-device things that matter | **Accepted** (DL-08, `asset.md`); **not implemented** |
| Stewardship over care, obligation, preservation, custody, and accountability | **Accepted**; **not implemented** |
| Continuity over memory, preference, meaningful history, resumption, and transfer | **Accepted**; **not implemented** |
| Concierge over contextual, governed interaction and orchestration, including *"What can I do here?"* | **Accepted** (Room Help, `room-configuration.md`); **not implemented** |
| External Storage Foundation | **Implemented** (DL-151, DL-152) |

This ADR **does not invent runtime functionality**.

### 7. Homes That Behave Well is the residential ecosystem

**Homes That Behave Well** remains the residential problem, research, education, evidence,
storytelling, and lived-outcome ecosystem. This includes the Reference Home, residential scenarios and
questions, public articles, YouTube, Substack, workbooks, research journals, residential
implementation guidance, lived household evidence, residential commissioning and stewardship
learning, and architectural pressure-testing through real household use.

- It is **not** the new name of BehavesWell Core.
- It is **not** reduced to a software integration.

The relationship:

1. **Homes That Behave Well** discovers, teaches, tests, and socializes residential questions and
   outcomes.
2. **The BehavesWell Framework** supplies the six-stage behavioral architecture.
3. **BehavesWell Core** operationalizes governed, accepted capabilities over a Foundation.
4. **BehavesWell Core, Home Assistant Edition** is the current implementation used in the residential
   Reference Home context.

**Homes That Behave Well LLC** remains the legal entity and the GitHub organization. **HTBW LLC** is the
founding steward and publisher of the Framework (public specification v1.0).

### 8. How existing repository terminology is read

**No mechanical replacement is performed.** Existing documents are read as follows.

| Term as found | Reading from DL-153 onward |
|---|---|
| **"HTBW Core"** in an accepted ADR, ledger row, or historical document | **Historical.** It names the earlier combined usage — architecture and product together. Read the *architecture* sense as the seven-layer BehavesWell Core stack (six stages plus Layer 0 Foundation) and the *product* sense as BehavesWell Core, Home Assistant Edition. Historical text is **annotated, never rewritten** |
| **"HTBW Core"** as a current public display name | **Replaced** by **BehavesWell Core** (§9) |
| **"HTBW"** in current architecture documents | The repository's established shorthand, which predates DL-153. Where it names software behavior, read it as BehavesWell Core (Home Assistant Edition) applying the Framework. Where it names the residential context, read it as Homes That Behave Well. It is **not** a product name. Remaining usage is recorded vocabulary debt, reduced document-by-document when each is next revised, never by global replacement |
| **"seven responsibilities"** / **"framework order"** (Foundation, Stewardship, Identity, Truth, Continuity, Operational Trust, Concierge) | **Historical presentation.** The seven responsibilities are the **seven layers of the BehavesWell Core stack**, and every ownership statement made about them stands. Their *presentation order* is superseded by the six-stage order over Layer 0 |
| **"BWF"**, **"Behaves Well Framework"**, **"Behaves Well Framework™"** | Variants of **BehavesWell Framework**, the canonical written form in repository documents. Public brand notation (™, ©) is a publication concern (§10) |
| **"layer"** in the public v1.0 specification ("six progressive layers") | The six stages occupy **layers 1–6** of the Core stack; Layer 0 is Foundation. The two uses are consistent |

### 9. Backward-compatible public rename

The public display name changes; **stable technical identifiers do not**.

| Surface | Name |
|---|---|
| `manifest.json` `name`, `hacs.json` `name` (Home Assistant-native, searchable) | **BehavesWell Core** |
| Current README, user guide, and installation guidance, where space allows | **BehavesWell Core, Home Assistant Edition**, then **BehavesWell Core**. The former public name *HTBW Core* may be stated for transition clarity |
| Config-flow, Repairs, options, and diagnostics strings | Unchanged in this decision. They say **"HTBW"**, which names the household's configuration entry and the external-storage folder (`HTBW/`). Revising them is a later, separately validated copy change |

**Protected identifiers (unchanged, never renamed for branding):**

- integration domain `htbw`, `custom_components/htbw`, `DOMAIN`, and Supervisor discovery `htbw`;
- `HOUSEHOLD_UNIQUE_ID = "htbw_household"`, Room subentry type `room`, Room subentry unique IDs, every
  `CONF_*` key, `migrated_into`, and every Repairs issue ID prefix;
- storage root `HTBW/`, `.htbw-root.json`, `.htbw-health-*`;
- `htbw_voice_evidence` and `htbw-voice-evidence`, the Voice Evidence package and logger names, and
  `HTBW_VE_*` environment variables;
- `_PERSON_KEY_DOMAIN` and every Voice Evidence cryptographic domain separator, Voiceprint,
  derived Person identifier, storage-key derivation, and enrollment-recording address;
- the repository name `homes_that_behave_well` and the organization `Homes-That-Behave-Well-LLC`;
- every ADR filename, DL/OD identifier, and historical issue name;
- released documentation anchors, including `#authorizing-external-storage-for-htbw`, which runtime
  code references.

**`HOUSEHOLD_TITLE = "HTBW"` is unchanged.** It is the title of the household config entry. Changing it
would affect new installs only (existing titles are stored and may be user-renamed), so it is not
needed for the rename.

**Relationship to the greenfield mandate (P24, DL-19).** The greenfield mandate prohibits compatibility
with **predecessor products** (Asset Intelligence, Voice Identity, Concierge) as a constraint on design.
It does **not** prohibit BehavesWell Core from protecting **its own installed households' persisted
identifiers**. Preserving them is not a compatibility requirement imported from a predecessor; it
protects existing BehavesWell Core installations from a rename that changes no behavior.

Distribution repository naming remains with **#210**.

### 10. The © notation

- The product name is **BehavesWell Core**.
- **BehavesWell © Core** is the Owner's formal branded notation. It is reserved for visual lockups,
  website branding, About/Help copy, the first formal reference in appropriate current
  documentation, and brand-system documentation.
- **©** never appears in an integration domain, repository name, package or module name, filename,
  path, storage namespace, service, event, API identifier, entity or device identifier, config key,
  persisted identifier, environment variable, cryptographic domain separator, documentation anchor,
  or URL.
- **©** is not used in Home Assistant-native, platform-searchable name fields.
- The product notation is **not** the legal copyright notice. Where a notice is needed it is
  **© 2026 Homes That Behave Well LLC**.
- **No trademark registration or legal status is inferred** from either notation.

### 11. Visual identity disposition

No visual asset is created or approved by this decision.

| Asset | Disposition |
|---|---|
| **Homes That Behave Well** architectural-house mark | Residential **context** identity. Not redesigned, and **not** assigned to BehavesWell Core |
| **BehavesWell Core** product mark | **Pending #202** design and Owner acceptance. Environment- and platform-neutral across editions. Not the house mark, not an Interlock stage block, not a seventh stage |
| Current integration icon (`custom_components/htbw/brand/*`) | **Legacy/transitional artifact** pending #202. Retained unchanged so the rename does not wait for, or prematurely approve, a mark |
| **Voice Evidence** mark | Environment-neutral product identity **pending #202** |
| Framework stage icons (Interlock system) | Six stage icons, plus a **distinguishable Layer 0 Foundation** treatment (#202) |

### 12. Public Framework reconciliation

**The stage set and order are reconciled:**

- the public six-stage model is conceptually correct;
- Foundation is Layer 0 of a Core implementation, not a seventh stage;
- public findings **F1**, **F6**, and **F8** are resolved at the repository level. Remaining public-copy
  work stays with **#180**.

**Stage definitions were compared, not silently changed.** The public v1.0 wording differs from
accepted repository meaning in three allocations:

| Public v1.0 requirement | Satisfied in BehavesWell Core by |
|---|---|
| Identity 02.01 — who is authorized to be present, and in what capacity | Foundation (Person, Role) and Operational Trust (roles, authority) — Identity supplies assertions only (DL-06) |
| Operational Trust 03.02 / 03.03 — account for actions; disclose behavior changes | Explainability and the Decision Trace (cross-cutting; DL-15), Behavioral Governance, and Operational Trust policy |
| Continuity 05.01 — durable record of operational history | Distributed history ownership with Historical Explainability (P27–P30); no central history owner |

Truth, Stewardship, and Concierge are compatible. **Every v1.0 requirement is satisfied by accepted
BehavesWell Core architecture**, so *"BehavesWell Core implements the BehavesWell Framework"* is not
materially false and the rename is not blocked. How the public specification should word those three
stages requires Owner judgment and is tracked in **#215**. **Repository meaning is unchanged** until a
new Decision Ledger entry says otherwise.

---

## What is not changed

- No responsibility is created, removed, merged, or reassigned. Every ownership statement in
  [framework.md](framework.md), every contract, and every model stands.
- The dependency view and the runtime sequence are unchanged.
- **DL-01**'s ownership content stands; its *presentation order* is superseded (§8).
- **DL-16**, **DL-18**, **DL-19**, **DL-20**, **DL-30**, **DL-31**, **DL-51**, **DL-86**, and **DL-93**
  are consumed unchanged. **DL-131** is consumed unchanged in substance; only its product's public
  name changes (Home Steward → BehavesWell Extended Intelligence).
- No runtime behavior, persisted identifier, storage location, or data changes.

---

## Consequences

**Annotated, not rewritten** (each carries a note pointing to DL-153 and this ADR):

- DL-01 in [../governance/decision-ledger.md](../governance/decision-ledger.md);
- [adr-htbw-core-refoundation.md](adr-htbw-core-refoundation.md);
- [north-star.md](north-star.md);
- [../governance/authority-order.md](../governance/authority-order.md);
- [greenfield-mandate.md](greenfield-mandate.md);
- [principles.md](principles.md) (P24);
- the DL-131 row and [adr-home-steward-product-boundary.md](adr-home-steward-product-boundary.md)
  (successor product name).

**Reconciled:**

- [framework.md](framework.md), [dependency-view.md](dependency-view.md), and
  [runtime-sequence.md](runtime-sequence.md);
- [home-assistant-boundary.md](home-assistant-boundary.md);
- [htbw-framework-aligned-ux-and-information-architecture.md](htbw-framework-aligned-ux-and-information-architecture.md)
  and [../patterns/ui-patterns.md](../patterns/ui-patterns.md);
- [../models/glossary.md](../models/glossary.md);
- the governance register documents;
- the README, the user guide, and the Voice Evidence App's documentation prose.

**Accepted cost:** documents not revised in this pass still use *"HTBW"* as shorthand (§8). This is
recorded vocabulary debt, reduced as each document is next revised.

---

## Alternatives considered

| Alternative | Why rejected |
|---|---|
| Keep "HTBW Core" as the product name | Leaves one name with two referents (F8), and binds an environment-neutral product to a residential context name |
| Make Foundation a seventh Framework stage | Contradicts the published six-stage Framework and the Owner decision; Foundation is the substrate, not a household-facing stage |
| Remove Foundation from the architecture | Would orphan every accepted Foundation ownership (DL-04, DL-08, DL-09, DL-10) and break dependency rule 6 |
| Rename `htbw` identifiers to match the brand | Breaks installed households' config entries, storage, Repairs, discovery, and Voiceprint key derivation for no behavioral gain |
| Rename Homes That Behave Well to BehavesWell | Erases the residential research and evidence ecosystem, which is a distinct thing (Owner decision 3) |
| Rewrite DL-01 and the refoundation ADR in the new terms | Falsifies historical record; annotation preserves it |

---

## Related documents

- [north-star.md](north-star.md)
- [framework.md](framework.md)
- [adr-htbw-core-refoundation.md](adr-htbw-core-refoundation.md)
- [home-assistant-boundary.md](home-assistant-boundary.md)
- [../models/glossary.md](../models/glossary.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
- [../governance/public-claim-register.md](../governance/public-claim-register.md)
