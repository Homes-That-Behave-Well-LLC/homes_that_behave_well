# Greenfield and Compatibility Mandate

> **Document status: Canonical (constitutional).**
> Subordinate only to [north-star.md](north-star.md).
>
> **Annotated 2026-11-10 by DL-153 (Issue #214).** "HTBW Core" below is historical wording for what is
> now **BehavesWell Core** (current edition: **BehavesWell Core, Home Assistant Edition**). **This mandate
> concerns predecessor products** (Asset Intelligence, Voice Identity, Concierge): their boundaries,
> schemas, and APIs never constrain BehavesWell Core design. **It does not prohibit BehavesWell Core from
> protecting its own installed households' persisted technical identifiers** (`htbw`, `htbw_household`,
> `HTBW/`, Voice Evidence key derivation, and the others DL-153 lists), which a public rename must not
> break. See
> [adr-behaveswell-framework-foundation-core-edition-and-context-identity.md](adr-behaveswell-framework-foundation-core-edition-and-context-identity.md).

---

## Position

**HTBW Core is a greenfield platform.**

The following are **not required** and must never be introduced as a constraint on HTBW Core design:

- Backward compatibility
- Implementation compatibility
- API compatibility
- Schema compatibility
- Legacy data-model compatibility
- Code reuse
- Compatibility shims
- Migration adapters

> **Scope of the migration-adapter prohibition, settled by DL-52.** This list prohibits compatibility
> **as a constraint on HTBW Core design**, and **DL-19** prohibits **implicit** migration obligations.
> **An explicit, optional, one-way, terminating adoption that constrains no HTBW model is outside
> it.** The prohibition keeps its full force through the rule that **adoption maps into HTBW's own
> accepted models and reports unmappable content as *not adopted*** — the moment an HTBW model is
> shaped by what a legacy product happens to store, this mandate is violated. See
> [adr-product-disposition-and-legacy-adoption.md](adr-product-disposition-and-legacy-adoption.md).

---

## Status of the reference repositories

> **Disposition is now stated per product by DL-51.** This section is the origin of that asymmetry and
> is reaffirmed by it.

**Asset Intelligence** is a separate, released product with its own lifecycle. It is not merged into
HTBW Core, not deprecated by this refoundation, and not modified by it. **It is not retired**, and
**HTBW must never require it to be installed.** HTBW Core may learn from its concepts, contracts, and
household outcomes, but is not required to depend on it or copy its implementation. **HTBW absorbs
equivalent functionality directly**, and a household's existing Asset Intelligence data may be
**adopted once** under **DL-52**.

**Voice Identity** and **Concierge** were exploratory projects. They revealed important architectural
concepts and household outcomes. **They are not compatibility commitments.** Their functionality is
**absorbed into HTBW and the standalone integrations will sunset** (**DL-51**), while **Identity** and
**Concierge** remain first-class HTBW responsibilities. **Sunset creates no compatibility requirement,
and it is not permission to inherit a sunsetting product's defects.**

No HTBW Core document may cite an existing implementation as a reason to preserve a boundary, schema,
API, module name, or ownership assignment.

---

## What is preserved

| Preserved | Not preserved |
|---|---|
| Proven architectural ideas | Existing project boundaries |
| Valid contracts | Existing integration boundaries |
| Household-facing outcomes | Existing schemas |
| Important scenarios | Existing APIs |
| Accepted vocabulary | Existing module names |
| Explainability requirements | Existing folder structures |
| Behavioral intent | Existing ownership assignments |
| | Existing runtime implementation choices |

---

## Discoveries carried forward

These are preserved because they are architecturally correct, not because they already exist.

| Discovery | Origin | Canonical home |
|---|---|---|
| Room Setup is an interaction-definition screen, not an inventory screen | Concierge | [../models/room-configuration.md](../models/room-configuration.md) |
| "What do you call this?" — explicitly configured household vocabulary | Concierge | [../models/contextual-vocabulary.md](../models/contextual-vocabulary.md) |
| "What can I do here?" — Room Help from configured exposure | Concierge | [../models/room-configuration.md](../models/room-configuration.md) |
| Explicit inclusion **and explicit exclusion** of devices | Concierge | [../models/room-configuration.md](../models/room-configuration.md) |
| Merged Rooms behaving as one Room while retaining constituents | Concierge | [../models/room.md](../models/room.md) |
| Voice assistant assignment establishing default Room Context | Concierge | [../models/room-configuration.md](../models/room-configuration.md) |
| Follow-Me as a policy-governed handoff with explicit blocks, not motion-triggered movement | Concierge | [../models/continuity.md](../models/continuity.md) |
| Person-scoped media preferences that follow a person across rooms | Concierge | [../models/continuity.md](../models/continuity.md) |
| Room-scoped volume, duck volume, and TTS volume | Concierge | [../models/continuity.md](../models/continuity.md) |
| Machine-readable plus human-readable explanation pairing | Concierge | [../models/decision-trace.md](../models/decision-trace.md) |
| Identity as advisory context with confidence bands and reason codes — never authentication | Voice Identity | [../models/person-and-identity.md](../models/person-and-identity.md) |
| Short-lived identity attribution context; identity is not a long-lived session | Voice Identity | [../contracts/identity-contract.md](../contracts/identity-contract.md) |
| Safe metadata only; biometric internals never exposed | Voice Identity | [privacy.md](privacy.md) |
| Enrollment artifacts are temporary; derived profiles are durable | Voice Identity | [privacy.md](privacy.md) |
| Fail-closed behavior when identity dependencies are unavailable | Voice Identity | [failure-and-degradation.md](failure-and-degradation.md) |
| Assets include non-device things that matter | Asset Intelligence | [../models/asset.md](../models/asset.md) |
| Environmental requirements and operating limits attached to assets | Asset Intelligence | [../models/asset.md](../models/asset.md) |
| Documentation, manuals, warranty, custody, and service history as first-class asset knowledge | Asset Intelligence | [../models/asset.md](../models/asset.md) |
| Coverage and confidence drivers for room-level environmental conclusions | Asset Intelligence | [../models/truth.md](../models/truth.md) |
| Advisory that informs rather than interrupts | Asset Intelligence | [behavioral-governance.md](behavioral-governance.md) |
| Connected storage traceable to a system-of-record object | all three | [connected-storage.md](connected-storage.md) |

---

## Prohibitions during documentation work

- Do not copy code from the reference repositories into HTBW.
- Do not begin implementing HTBW Core code.
- Do not introduce a compatibility requirement in a contract, model, or ADR.
- Do not preserve an obsolete ownership statement for the sake of a smaller change.

---

## Related documents

- [north-star.md](north-star.md)
- [home-assistant-boundary.md](home-assistant-boundary.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
- [adr-htbw-core-refoundation.md](adr-htbw-core-refoundation.md)
