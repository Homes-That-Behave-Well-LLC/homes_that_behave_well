# Asset Model

> **Document status: Canonical model.**
> Terminology: [glossary.md](glossary.md). Owning responsibility: **Foundation** (descriptive
> knowledge). Significance and care belong to **Stewardship**: [stewardship.md](stewardship.md).

---

## Purpose

The HTBW asset model provides the **descriptive knowledge** the framework requires: what exists, what
it is, where it is, what it relates to, and what is known about it.

## Question answered

*What exists, and what do we authoritatively know about it?*

---

## Relationship to the standalone product

The standalone **Asset Intelligence** integration remains a separate released product with its own
lifecycle, and **it is not retired**. This refoundation does not merge, modify, deprecate, or create
compatibility requirements for it.

HTBW Core may learn from its concepts, contracts, and household outcomes. HTBW Core is **not** required
to depend on it or copy its implementation. See
[../architecture/greenfield-mandate.md](../architecture/greenfield-mandate.md).

> **HTBW must never require Asset Intelligence to be installed** (**DL-51**). It is never a
> prerequisite, never a mandatory **DL-41** dependency, and never a condition of any resident-facing
> outcome. **HTBW absorbs equivalent functionality directly.**

**A resident's investment survives the transition.** Where a household already holds asset knowledge
in the standalone product, HTBW offers a **one-time, authoritative, terminating adoption** of it
(**DL-52**) — never a runtime dependency, never continuous synchronisation, and never shared
authority. **Relationships and limits are adopted as declarations; service history is adopted as
Stewardship Care Evidence of kind `attested`; and observational history is never adopted as a Truth
Fact.** **Scope, artifact custody, and coexistence are settled by DL-110**: an adopted document
becomes a new, independently HTBW-governed artifact anchored to its HTBW Asset, surviving the source
product's own uninstall; coexistence resolves directly from DL-52's own authority-transfer language.
The generic acceptance-capture **surface** remains **OD-93**. See
[../architecture/adr-product-disposition-and-legacy-adoption.md](../architecture/adr-product-disposition-and-legacy-adoption.md).

---

## What an Asset is

A **thing** the household has declared matters, whether or not it is device-backed:

- Device-backed: televisions, speakers, networking equipment, appliances, HVAC equipment
- Non-device: artwork, instruments, furniture, collections, documents, vehicles, structures

An Asset is **not** a Home Assistant Device. One Asset may map to zero, one, or several Devices.

> **People are not Assets. Pets are not Assets.**
>
> A Person and a Pet are distinct object types with their own definitions, and both may carry
> Stewardship care obligations **without being modelled as property**. No record in this repository
> represents a household member — human or animal — as an Asset, an inventory item, or an equipment
> record, and none may.

**That an Asset exists does not establish that it matters.** Registration is descriptive knowledge
owned here; **significance is a separate, household-declared judgement owned by Stewardship**. An
unregistered thing may matter enormously, and a registered one may matter not at all.

---

## Descriptive knowledge the asset model provides

- What exists
- Authoritative asset identity
- Asset type and capabilities
- Location
- Relationships
- Documentation
- Manuals
- Photos
- Purchase and installation records
- Manufacturer and model
- Serial number
- Warranty
- Service provider
- Environmental or operating limits
- Maintenance-relevant metadata
- Physical and logical relationships
- Rooms served
- Person, pet, room, or home relationships
- Caretaker-of and owner-of relationships, as relationship *types*; the caretaker assignment itself is
  owned by [stewardship.md](stewardship.md). **`caretaker-of` is many-to-many** — one Asset may have
  multiple current caretakers, and one Person may be caretaker of multiple Assets; the Asset's own
  "Caretakers" view is a projection over Stewardship's single assignment record set, never an
  independently editable copy (**DL-71**)

---

## Object distinctions

**Do not automatically treat a Home Assistant Device, Home Assistant Entity, HTBW Asset, Person, Pet,
Room, or Service as the same object.**

| Object | Definition | Distinguishing property |
|---|---|---|
| Home Assistant Device | A platform registry object | Exists because an integration created it |
| Home Assistant Entity | A platform state-bearing object | Carries state; is not a household concept |
| HTBW Asset | A household thing that matters | May have no device at all; carries provenance, documentation, and lifecycle |
| Person | A human household member | Carries roles, consent, identity evidence, authority |
| Pet | A non-human household member | Carries obligations; is not a Person |
| Room | An interaction context | Is a place plus an interaction definition |
| Service | An external provider relationship | Is a relationship, not a thing in the home |

A single physical object may be an Asset **and** be represented by several Devices and many Entities.
The Asset is the household-meaningful object.

---

## Asset-scoped content

| Content | Notes |
|---|---|
| Authoritative asset identity | The formal name, for example *1918 A.B. Chase 6' Grand Piano* |
| Documentation | Manuals, photos, receipts, appraisals, certificates |
| Service plan | Owned as an obligation by Stewardship; referenced here |
| Environmental limits | Operating and preservation limits the asset requires. **The same pattern — a declared requirement, a current Truth Fact, and a Stewardship evaluation — extends to Person Environmental Requirements without converting a Person into an Asset** (**DL-61**) |
| Warranty | Coverage window, provider, terms reference |
| Maintenance history | Record of what was done and when |
| Assigned caretaker | A reference to the Stewardship-owned caretaker assignment, expressed as a Foundation caretaker-of relationship |
| Rooms served | An asset may serve more than one Room |

An asset's **authoritative name is never replaced by a vocabulary term.** "Piano" is an interaction
alias in a Room; the asset remains *1918 A.B. Chase 6' Grand Piano*. See
[contextual-vocabulary.md](contextual-vocabulary.md).

---

## How the asset model and Stewardship cooperate

They must not be collapsed into one indistinguishable responsibility.

| Question | Owner |
|---|---|
| What is this thing, and what do we know about it? | Asset model (Foundation) |
| Where is it, and what does it relate to? — as **declared** knowledge | Asset model (Foundation), through the `located-in` relationship |
| **Where is it *now*?** | **Truth**, as a Location Fact with confidence, provenance, freshness, and validity |
| What are its environmental limits, as a property of the thing? | Asset model (Foundation) |
| Does it matter, and how much? | Stewardship |
| What care does it require, and when? | Stewardship |
| Is a care obligation currently met, due, or overdue? | Stewardship |
| Who is accountable for it? | Stewardship (owns the caretaker assignment), recorded through a Foundation caretaker-of relationship |
| Is its environment currently within limits? | **Truth** |
| Should we do something about it now? | **Concierge** |

Worked example:

```
Asset model:   The piano requires 40–60% relative humidity.
Truth:         The Music Room is at 31% relative humidity.
Stewardship:   The piano's preservation obligation is unmet.
Operational Trust: Humidifier control is permitted autonomously; notification requires no confirmation.
Concierge:     Raise humidity, notify the caretaker, and explain.
```

---

## Participation and exposure

Asset existence does **not** imply participation in any Room's interaction model, and participation
does not imply exposure. See [room-configuration.md](room-configuration.md).

An asset may be:

- known and not participating (a Sonos Beam excluded from music)
- participating and not exposed (a temperature sensor feeding a composite fact)
- exposed as an individual (the TV)
- exposed as part of a group (one of seven shades)
- exposed as a knowledge asset (the piano)

A deliberate exclusion (the Beam, above) carries its own governed metadata — a required structured
reason, scope inherited from the Participation record itself, and temporality — never a fifth
Existence/Participation/Exposure/Authority state. See
[room-configuration.md](room-configuration.md), *Exclusion Metadata (DL-103)*.

---

## Native representation

Governed by **DL-31** and
[../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md).

An Asset is **not** a Home Assistant Device. It may nonetheless **be represented by** one, and where a
native representation exists the household gains dashboards, automations, targeting, Area
relationships, and Assist without HTBW building a parallel hierarchy.

| Case | Required behaviour |
|---|---|
| The Asset is already backed by one or more existing Devices | **Reference them.** Do not create an additional Device, and do not copy manufacturer, model, serial number, versions, or Area assignment |
| The Asset has no native backing — artwork, an instrument, furniture, a collection | The integration **may create a native Device** for it through the supported registration pattern, so the Asset is natively visible |
| The Asset spans several Devices | The Asset remains the single household-meaningful object. It does not become several Assets |

**This is the accepted endpoint-identity anchor where more than one technical provider represents one
physical presentation endpoint** (for example a speaker visible through more than one integration) —
see **DL-55** and [room-configuration.md](room-configuration.md). No new identity construct is created
for that case; where the household has not declared the endpoint as an Asset at all, the Room
Configuration participation reference itself is a sufficient anchor.

Once a native Device exists, Home Assistant is authoritative for the registry entry and its native
fields. HTBW retains the device identifier and only the Asset knowledge Home Assistant does not hold:
identity, documentation references, provenance, appraisal and warranty references, environmental and
operating limits, relationships, and rooms served. **These need not all live in one record or one
responsibility** — significance and care remain **Stewardship's**, current conditions remain
**Truth's**, and documents remain anchored in connected storage rather than copied.

### Asset Type

**Asset Type is authoritative in HTBW and owned by Foundation**, as descriptive knowledge of *what
this thing is*. It is not a user-interface filter, and it is not owned by a Label.

| Layer | Owner | Status |
|---|---|---|
| Asset Type | **Foundation (asset model)** | **Authoritative.** Changed only through the governed HTBW mechanism |
| Native Label | Home Assistant owns the Label object | **A derived, HTBW-managed projection** of the authoritative type |
| Device class | Home Assistant | **Not available.** Device `entry_type` supports only `None` and `service`; device classes are entity classifications. **No custom "Asset" device class may be claimed** |

Fine Art, Sculpture, Collection, Antique, Furniture, and Instrument are **examples, not a closed
taxonomy**.

Required behaviour for the managed projection:

- Residents maintain **the type only**. They must never be asked to maintain type and labels separately
- HTBW maintains its **reserved** labels; resident-created labels are **never removed or overwritten**
- **A failed or missing label projection never silently changes the Asset Type**
- Reconciliation, where reported, uses the existing Repairs boundary (**DL-65**)

The reserved taxonomy's naming, seeding, collision handling, versioning, retirement, and reconciliation
mechanism are **OD-68**. No punctuation, casing, namespacing, or label identifiers are prescribed here.

### Asset-derived Entities

Where an Asset-related value is useful natively, it may be **published as an Entity**. The Entity is a
**projection**: it never becomes a second authority for a value another responsibility determines.
Obligation state remains **Stewardship's**, current conditions remain **Truth's**, and the projected
value stays explainable back to its inputs. Which values are projected, on which entity platform, and
with which state vocabulary is **OD-69** — HTBW defines no "asset health" state model, and none is
invented here.

---

## Consumes

- Home Assistant Device, Entity, and Area references where applicable
- Connected-storage documents anchored to the asset

## Provides

- Authoritative asset identity and descriptive knowledge
- Capability descriptions consumed by Room Configuration and Concierge
- Environmental and operating limits consumed by Stewardship and Truth
- Relationships consumed across the framework

## Explicit non-responsibilities

The asset model does **not** decide significance, own obligations, evaluate current conditions, grant
authority, or orchestrate.

---

## Failure behavior

| Condition | Behavior |
|---|---|
| Backing Device removed | Report a broken anchor; retain the asset and its knowledge |
| Documentation unreachable in connected storage | Report unavailable; do not claim absence |
| Asset location unknown | Represent as unknown; do not default to a Room |
| Duplicate assets suspected | Surface for household resolution; do not auto-merge |

## Deletion and cleanup

**The Asset is the governing parent of its documentation** (**DL-45**). Foundation owns the Asset and
its documentation anchor; Stewardship owns significance and care, not the document artifact.

| Event | Required behavior |
|---|---|
| **A single document is deleted** | The artifact is removed, its governed reference is removed or tombstoned, empty dependent structures may be removed, and **the Asset remains** |
| **The Asset is deleted** | All associated artifact references are enumerated; every document without an overriding retention or preservation rule is deleted; Asset-specific structures are removed once empty; **cleanup failure is surfaced**; and deletion is **not reported complete while mandatory cleanup remains unresolved**, unless the accepted lifecycle supports a pending-cleanup state |
| **Storage is unavailable during cleanup** | **Deletion is not claimed.** A governed pending-cleanup state is retained, the reference is not discarded, and reconciliation follows once storage returns |
| **A hold or retention floor applies** | The artifact remains, governed and explained. **Cleanup never silently overrides a Preservation Hold or a retention floor** |

Historical governance records may remain where required, **but they must not retain the document
payload without authority**. The backing Home Assistant Device follows its own lifecycle and is
**never removed because an artifact structure was cleaned**.

Documents are reached through the Asset and its document list — **never through a storage hierarchy**
(**DL-44**).

## Privacy considerations

Asset records may reveal value, ownership, and household absence patterns. Visibility of asset value,
documentation, and location history is governed by Operational Trust policy.

## Explainability requirements

Any decision that relied on an asset's limits, warranty, service relationship, or caretaker records
that fact and its source in the Decision Trace.

---

## Representative scenarios

- [../scenarios/room-vocabulary.md](../scenarios/room-vocabulary.md) (piano knowledge)
- [../scenarios/stewardship-obligations.md](../scenarios/stewardship-obligations.md)

## Open decisions

| ID | Question |
|---|---|
| OD-01 | Home Assistant representation strategy for HTBW Assets — the representation rule is accepted as **DL-31**; the residual is the persistence shape of governed records |
| OD-02 | **Closed — DL-43, DL-44, DL-45.** Documentation, manuals, photos, and records are located through a governed artifact reference; file formats remain capability-specific |
| OD-68 | Reserved Asset Type label taxonomy and its projection mechanism |
| OD-69 | Which Asset-related values are projected as Entities, on which platform, and with which state vocabulary |
| OD-20 | Whether HTBW Core consumes the standalone Asset Intelligence product as an optional evidence source, and through what interface |

## Related documents

- [stewardship.md](stewardship.md)
- [room-configuration.md](room-configuration.md)
- [../architecture/connected-storage.md](../architecture/connected-storage.md)
- [../contracts/foundation-contract.md](../contracts/foundation-contract.md)
