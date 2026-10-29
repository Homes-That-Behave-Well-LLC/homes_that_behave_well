# ADR — Product Disposition and Legacy Adoption

> **Document status: Accepted ADR.**
> Authority: rank 1 in [../governance/authority-order.md](../governance/authority-order.md).
> Establishes accepted decisions **DL-51** and **DL-52**, closes **OD-82**, and opens **OD-85**.
> Amends the non-negotiable constraint in [../governance/authority-order.md](../governance/authority-order.md).

---

## Status

Accepted, 2026-08-26.

This ADR resolves a **verified contradiction between canonical documents**. Under the *Conflict
procedure* in [../governance/authority-order.md](../governance/authority-order.md), two canonical
statements in conflict is a defect that must be recorded as an open decision and resolved by a new
ADR. **OD-82** was that decision. This is that ADR.

---

## Context

### The constraint flattened three products into one class

[../governance/authority-order.md](../governance/authority-order.md) recorded, under
**Non-negotiable constraints** — which bind *regardless of rank*:

> Asset Intelligence, Voice Identity, and Concierge remain **separate released products** with their
> own lifecycles.

### Two canonical constitutional documents already said something different

| Document | Asset Intelligence | Voice Identity | Concierge |
|---|---|---|---|
| `authority-order.md` — *Non-negotiable constraints* | separate released product | **separate released product** | **separate released product** |
| [greenfield-mandate.md](greenfield-mandate.md) — *Status of the reference repositories* | *"a separate, released product"* | **"exploratory project"** | **"exploratory project"** |
| [north-star.md](north-star.md) — *The Standalone Products Are Not Framework Layers* | separate released product, not a layer | **"Superseded as a product boundary inside HTBW Core"** | **no product disposition given** |
| [adr-htbw-core-refoundation.md](adr-htbw-core-refoundation.md) — *Consequences → Not changed* | separate released product | separate released product | separate released product |

**The asymmetry was already in the canonical tier.** The flattening was the error, and this ADR
corrects it rather than introducing a new position.

### The release footprint was verified

Checked 2026-08-26 against the GitHub release records of each repository.

| Repository | Releases | Latest | Finding |
|---|---|---|---|
| `tom-tagmdl/asset_intelligence` | **27** | v1.0.12, 2026-06-30 | A released product with a real installed footprint |
| `tom-tagmdl/voice_identity` | **1** | **v0.1.0, 2026-07-10** | **A published artifact exists**, installable as a HACS custom repository |
| `tom-tagmdl/concierge` | **0** | — | No released artifact |

> **The premise that Voice Identity has no released-user footprint is an assumption about installs,
> not a fact about artifacts.** It is recorded here as an assumption, and the artifact disposition is
> stated regardless of how many installs exist. **A published artifact that is silently abandoned
> leaves a household with no explanation, which is the outcome this architecture exists to prevent.**

### A resident's investment had no protection

A household that has described its rooms, sensors, assets, environmental limits, documents, custody
and service history in Asset Intelligence has done substantial work. **No repository document said
that work survives.** [home-assistant-boundary.md](home-assistant-boundary.md) and **DL-31** already
require that *"no resident may be required to maintain the same information twice"*, and a household
running both products was doing exactly that.

### The greenfield mandate appeared to forbid the remedy

[greenfield-mandate.md](greenfield-mandate.md) lists **migration adapters** among things that *"must
never be introduced **as a constraint on HTBW Core design**"*, and **DL-19**'s prohibited pattern is
recorded as *"implicit migration obligations."* Two readings were available, and the repository chose
between neither.

---

## Decision

### DL-51 — Product disposition is stated per product, never for the portfolio

| Product | Disposition |
|---|---|
| **Asset Intelligence** | Remains a **released standalone integration** with its own lifecycle. Existing installations continue to function. **It is not retired.** HTBW **absorbs equivalent functionality directly**, and **HTBW must never require Asset Intelligence to be installed** — it is never a prerequisite, never a mandatory **DL-41** dependency, and never a condition of any resident-facing outcome |
| **Voice Identity** | Functionality is **absorbed into HTBW**. **Identity** remains a first-class HTBW responsibility. **The standalone integration will sunset**, and its **v0.1.0 artifact carries a stated disposition** rather than being silently abandoned |
| **Concierge** | Functionality is **absorbed into HTBW**. **Concierge** remains a first-class HTBW responsibility. **The standalone integration will sunset** |

**The responsibility and the product are separable, and this decision depends on that separation.** A
responsibility may be first-class inside HTBW while its released product continues, and a product may
sunset while its responsibility is unchanged. **Absorbing functionality is not adopting a schema**,
and **DL-19** is unchanged: no compatibility requirement flows upward from any of the three into HTBW
Core, retired or retained.

### DL-52 — Adoption is one-time, authoritative, and terminating

**HTBW supports an Asset Intelligence Adoption experience, whose purpose is preserving resident
investment.**

| Property | Statement |
|---|---|
| **One-time** | Adoption is a bounded, resident-initiated act. It completes and does not recur |
| **Not a runtime dependency** | Adoption creates **no declared capability dependency**. After adoption, no **DL-41** dependency on Asset Intelligence remains, and **HTBW continues to function if the product is removed** |
| **Not synchronisation** | Adoption is **one-way and terminating**. There is no continuous synchronisation, no write-back, and **no synchronisation loop** |
| **Authoritative** | **HTBW becomes authoritative for adopted records.** Authority transfers at adoption and does not remain shared |
| **Lineage preserved** | Every adopted record carries **provenance naming the source product and its exact version** (**P30**) |
| **Investment preserved** | **A resident's investment in describing their household survives the transition.** HTBW does not require a resident to recreate information that already exists |

**The greenfield ambiguity is resolved in favour of the bounded reading.** The
[greenfield-mandate.md](greenfield-mandate.md) prohibition targets **compatibility as a constraint on
HTBW Core design** and **implicit** migration obligations. **An explicit, optional, one-way,
terminating adoption that constrains no HTBW model is outside it.** The constraint continues to do
its full work:

> **Adoption maps into HTBW's own accepted models and reports unmappable content as *not adopted*.**
> The moment an HTBW model is shaped by what Asset Intelligence happens to store, **DL-19 is
> violated.**

### What adoption may transfer, and what it may never transfer

**Adopted history is not HTBW history.** This distinction is constitutional, not stylistic.

| Content | Adopted as | Never |
|---|---|---|
| Asset-to-room, asset-to-tracker, asset-to-document relationships | **Declarations** | — |
| Environmental limits and thresholds | **Declarations** — limits as properties of the thing | — |
| Service, tuning, and maintenance records | **Care Evidence Record**, kind **`attested`** (**DL-48**) | Kind **`observed`** — HTBW did not observe it |
| Custody and loan history | **Custody Period** (**DL-49**) | — |
| Change and audit records | **Change Records** (**DL-26**), provenance naming the source | — |
| Environmental and observational history | An adopted external record with **foreign provenance** | **A Truth Historical Fact** |

**A Historical Fact carries confidence at the time, provenance, coverage, freshness, and a lifecycle
that HTBW never executed.** Adopting another product's conclusions as Truth's own would make HTBW
assert it knew things it never knew — prohibited by **P15**, **P27**, and **P28**.

**A default the household never saw is not a declaration.** Shipped care defaults and profile
constants originating in the source product are **not adopted as household declarations**.

### Adoption is a governed decision

Adoption is a **bulk authority transfer over household records**, not a configuration action.

- **Operational Trust authorises it.**
- It **produces a Decision Trace**, recording what was offered, what was adopted, what was **skipped**,
  what was **unmappable and therefore not adopted**, and the exact source version.
- **`Skip` and partial adoption are first-class outcomes**, and re-offering later is permitted.
- **Adoption is idempotent.** A second run creates no duplicates.

### Native objects are unaffected

Both products already **reference** the same native Home Assistant Areas, Devices, Entities, and
Persons. **Nothing in adoption copies a native object**, and **DL-31** is unchanged at that layer.

**Reference Over Copy does not apply to a coexisting product's private store, and applying it there
would cause the harm it exists to prevent.** A Governed Reference cannot survive removal of its
referent: a household that adopted by reference and then uninstalled Asset Intelligence would be left
with broken references where their data used to be. **Adoption therefore copies once, with lineage,
and that is the correct outcome.**

**The resulting artifact's identity, Governing Parent, and lifecycle are fully specified by DL-110**:
a successfully adopted document becomes a new, independently HTBW-governed artifact — never a revision
of the source's own file — anchored to the equivalent HTBW Asset and surviving the source product's
own uninstall, retirement, or cleanup unchanged. See
[../governance/decision-ledger.md](../governance/decision-ledger.md), **DL-110**.

---

## Accepted decisions established

| ID | Decision |
|---|---|
| **DL-51** | Product disposition is stated per product, never for the portfolio |
| **DL-52** | Adoption is one-time, authoritative, and terminating |

Full wording: [../governance/decision-ledger.md](../governance/decision-ledger.md).

---

## Amendment to the non-negotiable constraint

The constraint in [../governance/authority-order.md](../governance/authority-order.md) is **amended,
not deleted**, and the amendment is recorded here so it is never left silently contradicted:

> **Before.** *"Asset Intelligence, Voice Identity, and Concierge remain separate released products
> with their own lifecycles. No compatibility requirement is created for them by anything in this
> repository."*
>
> **After.** *Product disposition is stated per product (**DL-51**). Asset Intelligence remains a
> separate released product with its own lifecycle and is never a required dependency of HTBW. The
> standalone Voice Identity and Concierge integrations will sunset, while Identity and Concierge
> remain first-class HTBW responsibilities. **No compatibility requirement is created for any of them
> by anything in this repository** (**DL-19**).*

**The second sentence is unchanged in force.** Sunsetting a product creates no compatibility
requirement, and neither does adoption.

---

## Responsibility impact

| Responsibility | Impact |
|---|---|
| **Foundation** | Owns the descriptive Asset and Room records that adoption writes into. **Owns no adoption history of its own** |
| **Stewardship** | Receives adopted care history as **`attested` Care Evidence Records** and adopted custody history as **Custody Periods** |
| **Truth** | **Receives nothing by adoption.** Adopted observations never become Facts or Historical Facts |
| **Identity** | Unaffected. **DL-05** stands; voice remains one evidence source |
| **Continuity** | **Does not depend on adopted historical data.** Continuity's two scopes are unchanged, and no adopted record becomes a preference or a session |
| **Operational Trust** | **Authorises adoption**, and governs disclosure of adopted records exactly as it governs any other |
| **Concierge** | Composes the adoption **Decision Trace**, and remains the responsibility regardless of the standalone product's disposition |

**No new responsibility is created.** The seven-responsibility framework is unchanged, and Adoption is
a **capability**, not an owner.

---

## Alternatives considered

| # | Alternative |
|---|---|
| A | Retain all three as separate released products; refuse adoption |
| B | Consolidate all three into one HTBW product with a full migration surface |
| C | Consolidate the responsibilities, retaining thin compatibility surfaces |
| D | **Retire selectively, product by product, each with its own record** |
| E | Adoption by runtime reference, with no copy |
| F | Adoption as an Asset Intelligence responsibility — the source product exports |

## Alternatives rejected

| # | Rejected because |
|---|---|
| A | Leaves the canonical contradiction standing, and leaves a resident's investment unprotected. **DL-31** double-maintenance would persist indefinitely |
| B | Asset Intelligence has 27 releases and a real installed footprint. Retiring it imposes a migration on households who asked for none |
| C | Two surfaces to maintain, and the compatibility surface becomes the schema constraint **DL-19** exists to prevent |
| D | **Accepted**, with the refinement that Asset Intelligence is not retired at all |
| E | **Fails outright.** A reference cannot survive removal of its referent, and it couples two independent release lifecycles — the coupling **DL-19** forbids |
| F | Places an HTBW obligation inside a product HTBW does not own, and would create the upward compatibility requirement **DL-19** prohibits |

---

## Consequences

**Positive**

- A canonical contradiction is closed rather than carried.
- A resident's investment acquires an architectural guarantee it did not have.
- **DL-31** double-maintenance is resolved rather than relocated.
- Product disposition and responsibility disposition are permanently separated.

**Costs and obligations**

- An adoption capability must eventually be built, tested, and explained.
- The Voice Identity v0.1.0 artifact requires a stated disposition.
- Four canonical documents required reconciliation.

**Risks**

| Risk | Mitigation |
|---|---|
| Adoption becomes a schema constraint on HTBW models | *"Absorbing functionality is not adopting a schema"*; unmappable content is reported as not adopted |
| Adopted history is presented as HTBW's own knowledge | The transfer table above, and the **`attested`** versus **`observed`** distinction |
| Sunset is read as permission to inherit the sunsetting product's defects | Recorded on the harvest registers; conformance drifts are corrected in absorption |
| Adoption is read as authority to retire Asset Intelligence | **DL-51** states the opposite explicitly |

---

## Open decisions

**This ADR closes OD-82. OD-85 was opened here and is now closed as DL-110 (Issue #172); DL-110 opened one follow-on, OD-93.**

> **DL-52 governs the transfer of authority, not the whole household transition experience.**
> Recorded 2026-08-27 by the Episode 10 governance narrative validation. What **DL-52** settles is that
> adoption is one-time, authoritative, terminating, non-synchronising, lineage-preserving,
> Operational-Trust-authorised, traced, and idempotent, with `Skip` and partial adoption as first-class
> outcomes. **What it does not settle is what the household lives through while the transition
> happens** — where it is detected, offered, reviewed, and explained, and what the home says while both
> products remain installed. **That residual was OD-85 (#172) question 4, now resolved by DL-110**:
> OD-85 supplies the semantic requirements only, and routes the generic onboarding/acceptance-capture
> surface itself to a new, narrowly-scoped follow-on, **OD-93**, shared with **DL-109**'s commissioning
> acceptance and **OD-87**'s identity-artifact-invalidation acknowledgement. **No transition-governance
> responsibility, construct, or migration-debt class is created by this** — the residual has a named
> owner, and this clarification adds no decision beyond DL-110 and OD-93 themselves.

| ID | Question |
|---|---|
| **OD-82** | **Closed — DL-51, DL-52** |
| **OD-85** | **Closed — DL-110.** Adoption unit, artifact custody (a successfully adopted document becomes a new, independently HTBW-governed artifact under its own DL-104 Record Identity, anchored to the equivalent HTBW Asset, surviving source-product uninstall), coexistence (resolved directly from DL-52's own authority-transfer language), and surface requirements (capture surface routed to **OD-93**) |
| **OD-93** | **HTBW Onboarding and Household Acceptance Interaction Surface.** Raised by DL-110. Interaction-surface placement only, for DL-109, DL-110, and OD-87's acceptance events |
| **OD-20** | **Narrowed, not closed.** Runtime consumption of the standalone product remains open and is now bounded: whatever is decided, **HTBW must never require Asset Intelligence to be installed** |
| **OD-36** | **Extended, now informed.** DL-110 supplies the fact that an adopted artifact's governing parent is the HTBW Asset from the moment of adoption, never the source product's — the "artifact whose governing parent is removed by a different product" scenario this extension anticipated does not arise for an adopted artifact |
| **OD-01** | Unaffected in question, newly consequential in scope — adopted records need somewhere to live |
| **OD-69** | **Closed — DL-61**, independently re-verified narrower in scope than assumed here: it governs only HTBW's own internal asset-derived Room/health-status projection, never a coexisting source product's own publishing. The coexistence case is resolved instead by DL-110 directly from DL-52 |
| **OD-81** | **Unaffected, not expanded.** Its own broader public-capability-exposure question remains entirely its own; it was never required to resolve DL-110's narrower coexistence case |
| **OD-87** | **Adjacent, and deliberately separate.** Identity artifact invalidation is a second **bulk household act** of the same shape as adoption. It shares the missing-surface root, now routed to **OD-93** alongside DL-109 and DL-110 — whether OD-87's own acceptance criterion treats this as resolved remains OD-87's own determination |

---

## Home Assistant First review

Conducted under **P21**. **No new HTBW platform capability is created by this ADR.** Adoption reads a
custom integration's private store, which Home Assistant neither owns nor exposes, so no native
capability is displaced and **DL-30**'s ladder is not engaged. Native Areas, Devices, Entities, and
Persons continue to be referenced and never copied (**DL-31**), and **no second Recorder and no
parallel history is created** (**DL-42**, **DL-46**).

---

## Related documents

- [../governance/decision-ledger.md](../governance/decision-ledger.md)
- [../governance/authority-order.md](../governance/authority-order.md)
- [greenfield-mandate.md](greenfield-mandate.md)
- [north-star.md](north-star.md)
- [adr-htbw-core-refoundation.md](adr-htbw-core-refoundation.md)
- [../models/asset.md](../models/asset.md)
- [../models/stewardship.md](../models/stewardship.md)
- [../models/temporal-record.md](../models/temporal-record.md)
