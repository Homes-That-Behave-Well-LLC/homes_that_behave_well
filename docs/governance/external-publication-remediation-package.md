# External Publication Remediation Package

> **Document status: Operational.**
> **Exact, publication-ready replacement content** for external artifacts that this review could not
> edit directly. **This document creates no authority and decides nothing.** Where it disagrees with
> [decision-ledger.md](decision-ledger.md), [authority-order.md](authority-order.md), or any canonical
> model or contract, **those prevail and this document is wrong**.
> Compiled 2026-09-08. Findings register:
> [public-claim-register.md](public-claim-register.md).
>
> **Superseded in part, 2026-11-10, by DL-153 (Issue #214). Do not publish §1 or the W1 check as
> written.** The public six-stage BehavesWell Framework (Truth, Identity, Operational Trust,
> Stewardship, Continuity, Concierge) is **conceptually correct**. Foundation is **Layer 0** of a
> BehavesWell Core implementation, **not a seventh Framework stage**, so the replacement copy below that
> changes the public page to *"Seven connected responsibilities"*, adds Foundation as a *first
> responsibility card*, or says *"Foundation comes first"* in the Framework now contradicts accepted
> architecture. Any public mention of Foundation should present it as the substrate beneath the six
> stages. Replacement copy for that is public-copy work on **#180**, with stage wording on **#215**. The
> remaining sections are unaffected unless they repeat the same claim. See
> [../architecture/adr-behaveswell-framework-foundation-core-edition-and-context-identity.md](../architecture/adr-behaveswell-framework-foundation-core-edition-and-context-identity.md).

---

## Why nothing here was applied directly

**No external system was reachable from this execution.** Verified 2026-09-08:

- **No website source** exists in any workspace folder — searched for `www`, `web`, `site`, `website`, `cms`, `content`, `airo`, `next`, `astro`, `hugo` directories across `R:\HomesPlatformRepos`. **None found.**
- **No workbook file** exists — searched `N:\`, `H:\`, and `R:\HomesPlatformRepos` for `.pdf`, `.xlsx`, `.xlsm`, `.docx`, `.pptx` matching *workbook*, *assessment*, *htbw*, *behave*. **None found.**
- **No episode production artifact** exists — same search extended to `.srt`, `.vtt`, `.pptx`, `.key`. **None found.**
- **YouTube returned HTTP 401** to this review.

**Therefore nothing in this package may be reported as completed.** Each item is *publication-ready
but not applied*, and each carries an acceptance check to run **after** publication.

**Voice.** The replacement copy below is written in HTBW's plain-language, human-centred public voice.
**Architectural governance language has deliberately not been carried into public copy.**

---

## 1. Website — Framework page

**URL:** `https://www.homesthatbehavewell.com/framework`
**Governing source:** **DL-01**; `adr-htbw-core-refoundation.md`; `north-star.md`; `README.md`
**Related issue:** **#180** (F1, F2)
**Publication owner:** Tom Grounds

### 1.1 Section eyebrow and heading

| | |
|---|---|
| **Current** | `OVERVIEW` → *"Six connected responsibilities. One earned outcome."* |
| **Replacement** | `OVERVIEW` → *"Seven connected responsibilities. One earned outcome."* |

### 1.2 Responsibility card grid

**Current:** six cards — Truth, Identity, Operational Trust, Stewardship, Continuity, Concierge — plus an `OUTCOME` card for Human Trust.

**Replacement:** add a **seventh card, first in the grid**, and keep the remaining six in their existing order and styling.

| Field | Exact content |
|---|---|
| Eyebrow | `FOUNDATION` |
| Question | `What exists, and how do we describe it?` |
| Link | `/framework/foundation` |
| Card body (one sentence, matching the style of the existing cards) | `Before a home can decide anything, it has to know what it is made of — the rooms, the people, the things, and the words the household actually uses for them.` |

**Keep the `OUTCOME — Human Trust` card exactly as it is.** It is correctly presented as an outcome and matches accepted architecture.

### 1.3 Overview paragraph

| | |
|---|---|
| **Current** | *"The Behaves Well Framework helps a home understand reality, understand who it is serving, determine what is allowed, recognize what matters, preserve appropriate context, coordinate action, explain its behavior, and evolve responsibly."* |
| **Replacement** | *"The Behaves Well Framework helps a home describe what it is made of, understand reality, understand who it is serving, determine what is allowed, recognize what matters, preserve appropriate context, coordinate action, explain its behavior, and evolve responsibly."* |

*Only the opening clause is added. Everything else is unchanged.*

### 1.4 A note on ordering — recommended, not required

The site presents the responsibilities in the order Season 1 explores them. The framework's own order begins with Foundation. **Both can be true, and the cheapest honest fix is one sentence.** Add beneath the grid:

> *These are introduced in the order the series explores them. In the framework itself, Foundation comes first — everything else describes, decides about, or acts on what Foundation defines.*

### 1.5 Acceptance check

Load `/framework` on desktop and mobile. **PASS:** the page says *seven*, seven responsibility cards render, Foundation appears first, its link resolves, and the Human Trust outcome card is unchanged. **FAIL:** any count other than seven, or Foundation missing from navigation or grid.

---

## 2. Website — new Foundation responsibility page

**URL to create:** `https://www.homesthatbehavewell.com/framework/foundation`
**Governing source:** `foundation-contract.md`; **DL-01**
**Related issue:** **#180**

**Page eyebrow:** `FOUNDATION`
**Page title:** `What Does the Home Actually Contain?`

**Body copy:**

> Foundation is the part of the framework that describes the home.
>
> Before a home can tell you what is true, decide what is allowed, or work out what should happen next, it needs a shared description of what it is made of. The rooms. The people. The things that matter. The devices. And, just as importantly, the words the household actually uses for all of them.
>
> This sounds obvious until it is missing. When two systems disagree about what counts as the living room, or when the word everyone says out loud is not the word anything in the house recognises, nothing built on top of that can behave well. Every other responsibility is describing, deciding about, or acting on something Foundation defined.
>
> Foundation does not decide anything. It does not act. It does not judge what matters — that belongs to Stewardship. It holds the description the rest of the home relies on, and it keeps that description honest as the home changes.
>
> A home that behaves well starts by knowing what it contains, and by calling things what the people who live there call them.

**Cross-links, matching the pattern of the other responsibility pages:** Explore Truth · Explore Stewardship · Explore Human Trust · Return to the Framework · Watch Season 1

**Note:** *Season 1 has no Foundation episode.* Do not add a `RELATED EPISODE` block to this page. Tracked as **#181**.

**Acceptance check.** **PASS:** page loads, renders on mobile, is reachable from the framework grid and from navigation. **FAIL:** 404, or unreachable from `/framework`.

---

## 3. Website — Technical Debt framing

**URL:** `https://www.homesthatbehavewell.com/framework` and `https://www.homesthatbehavewell.com/framework/technical-debt`
**Governing source:** `decision-ledger.md` — *"No debt construct is created… the word appears normatively in this repository exactly once — **P24**"*; `stewardship.md`
**Related issue:** **#181**

**Disposition: retain the topic, change its status.** Technical debt is a real and useful thing to teach households about. What it must stop doing is standing beside Explainability as though it were a framework capability with an owner.

### 3.1 Cross-cutting group label

| | |
|---|---|
| **Current** | `CROSS-CUTTING CAPABILITIES` — Explainability, Governance, Technical Debt |
| **Replacement** | `CROSS-CUTTING CAPABILITIES` — Explainability, Governance · then a **separate** group below, labelled `WHAT THE FRAMEWORK HELPS YOU SEE` — Technical Debt |

### 3.2 Technical Debt card

| | |
|---|---|
| **Current** | `TECHNICAL DEBT — What does this choice cost later?` |
| **Replacement** | `TECHNICAL DEBT — What does this choice cost later?` **(unchanged)** with the sub-label `A condition the framework helps you see, not a responsibility it assigns.` |

### 3.3 Opening paragraph on `/framework/technical-debt`

Add as the first paragraph:

> Technical debt is not a part of the framework. It is a condition a home develops when choices are made without making their future obligations visible. The framework does not assign it an owner, because it does not need one: the obligations it creates are held by Stewardship, the dependencies it hides are described by Foundation, and the authority it quietly accumulates is governed by Operational Trust. What the framework gives you is a way to see it before it becomes expensive.

**Acceptance check.** **PASS:** Technical Debt is no longer presented as a peer of Explainability, and the opening paragraph names Stewardship, Foundation, and Operational Trust as where the work actually lands. **FAIL:** it still reads as a framework capability with an implied owner.

---

## 4. Website — Home Operating System framing

**URL:** homepage section *The Home Operating System*; blog category label
**Governing source:** zero repository occurrences; **P21**; **P25**
**Related issue:** **#181**

**Disposition: retain as an educational term, with one constraining sentence added.**

The existing homepage definition is already careful — *"A Home Operating System is not a product you buy"* — and needs only one addition. Append to that paragraph:

> It is not software, and it does not replace the platform your home already runs on. Homes That Behave Well extends Home Assistant rather than competing with it; a Home Operating System is the architecture and governance you put around whatever platform you have chosen.

**Acceptance check.** **PASS:** a reader cannot come away believing HTBW ships or plans an operating system, or competes with Home Assistant. **FAIL:** the term still reads as a product or a platform.

---

## 5. Website — Technology Stewardship category

**URL:** blog category label on `/ideas/blog/the-hidden-inventory` and the `/ideas` taxonomy
**Governing source:** `stewardship.md` — *"the responsibility for significance, care, obligations, **lifecycle accountability**, and ongoing responsibility"*
**Related issue:** **#181**

**Disposition: retain the category. No copy change is required.** The category sits inside the accepted Stewardship definition, and no reasonable reader would take a blog category as a framework element.

**One taxonomy note.** If category descriptions are supported by the CMS, set:

> `Technology Stewardship` — *Practical lifecycle, maintenance, accountability, obsolescence, and cost topics. These belong to the framework's Stewardship responsibility.*

**Do not rename the Stewardship responsibility.**

---

## 6. Blog — *What is Observability In A Home?*

**URL:** `https://www.homesthatbehavewell.com/ideas/blog/what-is-observability-in-a-home`
**Related issue:** **#180** (F5, F6)

### 6.1 The framework-order sentence — F6

| | |
|---|---|
| **Current** | *"This is one of the reasons Truth became the first responsibility in the Behaves Well Framework™."* |
| **Replacement** | *"This is one of the reasons Truth is the first responsibility the series explores. In the framework itself, Foundation comes first — it describes what the home is made of — and Truth is what the home then establishes about it."* |

**Do not simply substitute Foundation for Truth.** The author's point is about Truth, and it is a good point. The correction preserves it and adds the constitutional fact beside it.

### 6.2 Observability — F5

**No wording change is required.** The article's own definition is sound. **Optionally**, add one clarifying sentence after *"Monitoring tells us what happened. Observability helps us understand why."*:

> In the framework, that second question — *why did that happen?* — is called Explainability.

**Acceptance check.** **PASS:** the article no longer states that Truth is first in the framework, and Foundation is named. **FAIL:** unchanged, or Truth simply replaced by Foundation.

---

## 7. Store — Voice Identity Implementation & Integration Playbook

**URL:** `https://www.homesthatbehavewell.com/store`
**Governing source:** **DL-51** in `adr-product-disposition-and-legacy-adoption.md`; `adr-identity-replaces-voice-identity-boundary.md`
**Related issues:** **#180** (F7), **#171**, **#160**
**Publication owner:** Tom Grounds

### 7.1 Current listing, recorded for audit

| Field | Current value |
|---|---|
| Product name | `Voice Identity Implementation & Integration Playbook` |
| Price | `$49` |
| Status | `Coming soon` |
| Category | Implementation Playbooks |
| Description | *"A practical guide for creating voice experiences that use identity evidence, confidence, context, consent, and household boundaries appropriately."* |

### 7.2 Preferred disposition — rename and rescope to Identity

**DL-51** sunsets the Voice Identity standalone integration. **Identity remains a first-class responsibility**, and the described content is about Identity, not about a product.

| Field | Replacement value |
|---|---|
| Product name | `Identity & Voice Interaction Playbook` |
| Price | `$49` |
| Status | `Coming soon` |
| Category | Implementation Playbooks |
| Description | *"A practical guide to helping a home work out who it is speaking with — and what to do when it is not sure. Covers evidence, confidence, consent, household boundaries, and the difference between recognising a voice and trusting a request."* |
| Required note, displayed with the listing | *"This playbook covers the Identity responsibility in the framework. It is not a guide to any single product or integration."* |

### 7.3 Alternative disposition — unpublish

If the content is not ready to be rescoped, **unpublish the listing** rather than leave it advertised. Preserve the prior listing record for audit.

### 7.4 What the replacement copy must never imply

- That speech-to-text identifies the speaker.
- That a transcription-confidence value is identity evidence.
- That Home Assistant attributes a voice interaction to a person. **This is NOT VERIFIED** — see `home-assistant-boundary.md` **R3**.
- That HTBW can project a resolved actor into native Home Assistant Activity. **NOT VERIFIED.**
- That HTBW currently provides voice identity. **It does not — HTBW Core contains no code.**

### 7.5 Asset Intelligence playbook

**No change.** **DL-51** keeps Asset Intelligence a released standalone integration. The listing is consistent.

**Acceptance check.** **PASS:** no store listing offers implementation guidance for a sunsetting product, and no listing implies an unimplemented capability. **FAIL:** the original listing remains as-is.

---

## 8. Workbook v1.1 — remediation register

**Artifact:** `Homes That Behave Well™ Home Architecture Assessment Workbook v1.1` — PDF + Excel, $79, *Available now*
**Access:** **NOT AVAILABLE to this review.** No file located on `N:\`, `H:\`, or `R:\HomesPlatformRepos`.
**Related issue:** **#176**

**This review makes no claim about the workbook's content.** The register below states what must be checked and what each answer requires. **Locations cannot be given because the document was not available.**

| # | Check | Required content | Governing source | Severity | Publication consequence |
|---|---|---|---|---|---|
| **W1** | Does it present six or seven responsibilities? | **Seven**, including Foundation | **DL-01** | **Critical** | A paid instrument assessing homes against a framework the repository does not accept |
| **W2** | Is Foundation present and correctly defined? | Present; *"what exists, and how do we describe it"*; describes, never decides | `foundation-contract.md` | **Critical** | Assessment cannot cover rooms, vocabulary, or descriptive substrate |
| **W3** | How is Technical Debt framed? | As a **condition and assessment lens**, addressed through Stewardship, Foundation, and Operational Trust | `decision-ledger.md`; **P24** | **High** | A sellable artefact operationalising a construct the repository declined to create |
| **W4** | Are *Home Operating System* or *Technology Stewardship* presented as governed architecture? | **No** — educational terms only | zero repository occurrences | **Medium** | Public terminology promoted to architecture through a paid artefact |
| **W5** | Does it promise voice identity, explainability, Home Assistant behaviour, privacy, security, or local-first behaviour beyond repository authority? | No present-tense capability claims. **HTBW Core has no code; zero Season 1 behaviours are implemented** | `season-1-architectural-baseline.md` §5 | **Critical** | Paid product implying capability that does not exist |
| **W6** | Does it reflect later accepted decisions — historical explainability, historical truth, temporal records, communication vs delivery, permission vs announcement, identity confidence bands, occupancy vs identity, reference over copy? | Aligned, or explicitly marked as a v1.1 limitation | `adr-historical-explainability-and-historical-truth.md`; **DL-34**, **DL-39**, **DL-46** | **High** | Workbook predates accepted decisions and teaches superseded distinctions |
| **W7** | Do workbook instructions match the store description? | Consistent | `/store` | **Low** | Purchaser expectation mismatch |

**If W1, W2, or W5 fail, the workbook should not remain on sale unchanged.** A version increment to **v1.2** with preserved v1.1 history is the established route.

**Acceptance evidence required:** the workbook page or worksheet reference for each check, plus a screenshot of the responsibility list and of any Technical Debt section.

---

## 9. YouTube — Episode 11 clarification

**Artifact:** Season 1 Episode 11, *Can a Home Accumulate Technical Debt?*
**Access:** **NOT AVAILABLE** — HTTP 401.
**Related issue:** **#181**

**Do not re-edit or re-record the episode.** Add to the **video description**, as a final paragraph:

> A note on where this fits: technical debt is not one of the framework's responsibilities. It is a condition a home develops over time, and the framework addresses it through the responsibilities it already has — Stewardship for the obligations it creates, Foundation for the dependencies it hides, and Operational Trust for the authority it quietly accumulates.

**Also required, and cheap:** confirm from the authoritative episode source whether Episode 11 **intended** to introduce a Technical Debt construct or to **explain technical debt through existing responsibilities**. The second reading is consistent with the ledger. **This is not established** and is recorded as NOT VERIFIED until the episode is reviewed.

**Episodes 1, 2, 3, and 9** have no repository artefact. **No description change is proposed for them** — they need evidence capture first, tracked on **#173**.

**Acceptance check.** **PASS:** the Episode 11 description carries the note, and the episode's intent is recorded on #181. **FAIL:** technical debt still reads as a framework responsibility.

---

## 10. Taxonomy, categories, and tags

**Related issue:** **#181**

| Item | Current | Required |
|---|---|---|
| Blog category `HOME OPERATING SYSTEM` | Used on two posts | **Retain.** Educational term, now constrained by §4 |
| Blog category `TECHNOLOGY STEWARDSHIP` | Used on one post | **Retain.** Add the description in §5 |
| Tag `#technical-debt` | In use | **Retain.** A tag is not an architectural claim |
| Tag `#observability` | In use | **Retain.** Consider also tagging `#explainability`, which is already in use on the same post |
| Framework navigation | Six responsibilities | **Add Foundation**, first |

---

## 11. Where the mantra belongs — F8

**This one is a repository task first, and it is deliberately not drafted as public copy.**

The public site positions HTBW as *"Vendor-Neutral and Platform-Independent"*. The Building HTBW post
states *"HTBW extends Home Assistant. It does not compete with Home Assistant."* **Both may be
correct** — the *framework* is platform-neutral, while *HTBW Core, the software*, extends Home
Assistant — but **no repository document records that scope distinction**, and **P25** forbids binding
the architecture to one topology.

**Recommended sequence:** record the distinction in the repository through governance, **then** place
the mantra on the public framework pages. **Publishing the mantra first would state publicly a
boundary the repository has not yet drawn.** Tracked on **#180**.

---

## Related documents

- [public-claim-register.md](public-claim-register.md)
- [season-1-traceability-matrix.md](season-1-traceability-matrix.md)
- [decision-ledger.md](decision-ledger.md)
- [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md)
- [../models/glossary.md](../models/glossary.md)
