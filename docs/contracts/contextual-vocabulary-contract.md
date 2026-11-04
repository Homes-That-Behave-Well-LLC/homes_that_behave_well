# Contextual Vocabulary Contract

> **Document status: Canonical contract.**
> Responsibility: **Foundation**, as part of Room Configuration. Model:
> [../models/contextual-vocabulary.md](../models/contextual-vocabulary.md).

---

## Owning responsibility

**Foundation — Room Configuration owns the mapping. Concierge consumes the resolved target.**

Do not define vocabulary as owned by Concierge. Any document doing so is superseded.

---

## What Contextual Vocabulary guarantees

- Deterministic resolution: the same term in the same Room resolves to the same target set every time
- Explicit configuration: a term exists because the household created it
- Persistence across restart, reconfiguration, and platform upgrade
- Room scoping: the same word may resolve differently in different Rooms
- Mapping provenance sufficient for explanation
- **Vocabulary is first-class (DL-69)**: it is contextual (Physical Room, Merged Room, Person,
  Household, Capability, Interaction), never globally unique, and resolved by the narrowest context
  that deterministically applies. A Household-wide inherited tier is not guaranteed here and remains
  **OD-13**'s own question
- **Cardinality is configuration, never grammar (DL-69)**: a collection term's target-set size and
  any separately configured member-level terms are household configuration; language-specific
  singular/plural morphology is never hard-coded as architecture
- **A failed match never silently authorizes a broader native action (DL-69)**: command resolution
  compiles to a governed target set before any native targeting, and native fallback is considered
  only afterward, only where safe, and only for an exact, permitted, exposed target
- **Home-scoped inheritance and shadowing (DL-70)**: a term may be defined once at Home scope and is
  inherited everywhere no narrower term exists; a Room or Merged Room may shadow it, never replace it
- **Vocabulary and Fulfillment are distinguished (DL-70)**: a word may stay Home-scoped and stable
  while its Fulfillment (provider, target, source) varies by Room, Merged Room, or Person
- **Person Vocabulary never redefines a Room- or Merged-Room-owned device term (DL-70)**: it is
  restricted to Person-owned capabilities and resources

---

## What residents must never need to know

- Home Assistant entity IDs
- Home Assistant device names
- Manufacturer names
- Model names
- Formal asset names
- Internal service names
- The individual members of a configured group

A resident says "Shades", and seven configured shades respond. The resident never learns that there
are seven.

---

## The platform domain must not dictate household vocabulary

Home Assistant may classify several devices as `media_player`; HTBW distinguishes **Speakers**, **TV**,
and **Media Player**. Home Assistant may classify ceiling fixtures and table lamps alike as `light`;
HTBW distinguishes **Lights** and **Lamps**.

**This household distinction is preserved. The device domain is an implementation detail, not a
household concept.**

---

## What consumers may rely upon

- A resolved target set for a term within a resolved Room Context
- The exposed-term list for Room Help
- The mapping source, for explanation

## What consumers must never assume

- That an unconfigured term can be resolved by searching devices
- That entity or device naming conventions imply meaning
- That a vocabulary term renames the authoritative asset
- That the same term means the same thing in another Room
- That resolving a term implies permission to act on the result
- That a plural form implies a group, or that a recognition form is a configurable vocabulary entry

---

## What Contextual Vocabulary will never guarantee

- That the resolved targets are currently available
- That the resident is permitted to act on them
- That the resolved action is appropriate now

---

## Prohibited resolution behavior

1. Runtime search of all devices in the Room
2. Guessing from entity names
3. Fuzzy matching across the whole home
4. Substituting a similar device when the configured target is missing
5. Renaming or overwriting the authoritative asset name
6. Deriving a recognition form from anything other than a configured term

---

## Knowledge assets

A term may resolve to a knowledge asset rather than a controllable capability.

```
Authoritative asset name:  1918 A.B. Chase 6' Grand Piano
Room vocabulary term:      Piano
Resident asks:             "Tell me about the piano"
Resolution:                Room Context -> term "Piano" -> that asset -> asset knowledge
```

---

## Uncertainty and unknown representation

| State | Meaning |
|---|---|
| `resolved` | The term maps to a valid target set |
| `not_configured_here` | The term has no mapping in this Room |
| `broken_mapping` | The mapping exists but a target no longer resolves |
| `ambiguous` | More than one configured mapping matches — **including a singular utterance matching more than one configured member-level term of a collection (DL-69)** |
| `partially_available` | Some members of the target group are unavailable |

---

## Failure and degradation behavior

| Condition | Behavior |
|---|---|
| Term not configured here | State that it is not configured in this Room; offer to show what is available; never runtime-search |
| Broken mapping | Report a configuration problem; never substitute |
| Ambiguous | Ask which was meant, offering only exposed options; record the ambiguity |
| Partially available group | Apply the configured partial-availability policy; report which members were unavailable |
| Room Context unresolved | Do not attempt resolution; resolve the Room first |

---

## Privacy constraints

Exposing a term makes a capability discoverable by anyone who can speak in the Room. Protection is an
Operational Trust authority decision, never obscurity of the term.

---

## Explainability contributions

Every resolution records the Room Context, the term, the resolved target set, and the mapping source.
Every failure records the reason and what the household could do about it.

Explanations use the household term, not the entity ID: *"I turned on the lamps"*, not
*"I turned on `light.den_table_2`"*.

---

## Native naming information

Home Assistant is authoritative for native Device and Entity names, for native Assist aliases on the
objects it documents — **entity, Area, and Floor** — and for native Assist exposure.

| Guarantee | Statement |
|---|---|
| Native values may seed a term | A term with no household value may be initialised from applicable native naming information, attributed to Home Assistant |
| A seed is not synchronisation | Accepting or editing a seed produces the governed HTBW term. Nothing is kept in step afterwards |
| A household-defined term is stable | **A later native rename or alias change never overwrites it automatically.** HTBW may report that the native value changed |
| Nothing is written back | **HTBW never automatically writes a term into a native Assist alias**, and never writes a group term onto its members |
| Exposure is not granted by vocabulary | Configuring a term exposes nothing to Assist and grants no authority |

Mapping source distinguishes `native_seed`, `accepted_native_seed`, and `household_defined`. This is
provenance on the existing mapping-source field, **not a second state model**.

See [../models/contextual-vocabulary.md](../models/contextual-vocabulary.md) for the full rule.

---

## Recognition forms

| Guarantee | Statement |
|---|---|
| One authoritative term | The household configures a single term per meaning, in the form they chose. **No second vocabulary field exists for any other form** |
| Forms may be derived | HTBW may derive additional forms of a configured term so ordinary speech is understood |
| Forms are subordinate | A derived form resolves to **exactly** the authoritative term's target set, and is never exposed, configured, or persisted as vocabulary |
| Forms never compete | A configured term always outranks a derived form. Two derived forms matching and no configured term is `ambiguous`, never a guess |
| Plurality is not grouping | A plural form never creates or expands a group. **A group is configured, or it does not exist** |
| Residents maintain one value | Residents are never asked to maintain a term and its variants separately |

Explanation records the form heard and the authoritative term it resolved to. Room Help advertises
**authoritative terms only**.

---

## Open decisions

| ID | Question |
|---|---|
| OD-02 | **Closed — DL-43, DL-44, DL-45.** Vocabulary definitions are located through a governed artifact reference; encoding remains capability-specific |
| OD-13 | **Closed — DL-70.** Home-scope inheritance and Room/Merged-Room shadowing are accepted; Vocabulary and Fulfillment are distinguished; Person Vocabulary stays restricted to Person-owned capabilities; collision behaviour is stated; Floor participation stays deferred to **OD-10** |
| OD-14 | **Resolved.** Native aliases are an input — a seed — and never an authority |
| OD-62 | **Closed — DL-69.** Vocabulary is first-class; command resolution, cardinality, and safe native fallback are accepted; historical reconstruction remains excluded from generic conversational retrieval, now fully resolved by **OD-35** as **DL-130** |
| OD-86 | **What the home owes the household when a term is changed, retargeted, or withdrawn.** Raised 2026-08-27. **Consumers must not assume any transitional alias, deprecation window, or grace period**, because none is guaranteed and none has been decided. See [../models/contextual-vocabulary.md](../models/contextual-vocabulary.md) |

## Related documents

- [../models/contextual-vocabulary.md](../models/contextual-vocabulary.md)
- [room-configuration-contract.md](room-configuration-contract.md)
- [../scenarios/room-vocabulary.md](../scenarios/room-vocabulary.md)
