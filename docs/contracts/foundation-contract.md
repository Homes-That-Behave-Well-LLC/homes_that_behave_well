# Foundation Contract

> **Document status: Canonical contract.**
> Responsibility: **Foundation**. Models: [../models/home.md](../models/home.md),
> [../models/room.md](../models/room.md), [../models/asset.md](../models/asset.md),
> [../models/person-and-identity.md](../models/person-and-identity.md).

---

## Owning responsibility

**Foundation — what exists, and how do we describe it?**

Foundation is the descriptive substrate of the framework. Every other responsibility depends on it.
Foundation depends on no other responsibility.

---

## What Foundation guarantees

- A stable, authoritative definition of Homes, Physical Rooms, Rooms, Merged Rooms, Assets, People,
  Pets, Services, Relationships, Capabilities, Experiences, and Facts as *object types*
- Stable identity for every object, surviving restart, reconfiguration, and platform upgrade
- Explicit participation, exposure, and authority scoping via
  [room-configuration-contract.md](room-configuration-contract.md)
- Deterministic vocabulary resolution via
  [contextual-vocabulary-contract.md](contextual-vocabulary-contract.md)
- Descriptive asset knowledge with provenance
- Relationships between objects, including caretaker-of, owner-of, serves-room, and located-in
- The Communication **Category** axis: the closed, seven-value, content-domain enumeration
  (Stewardship, Security, Care, Environment, Experience, System, Safety), its canonical definitions,
  and assignment guidance (**DL-78**) — never the Category selected for an individual Communication,
  which the originating responsibility assigns. See [../models/communication.md](../models/communication.md).

---

## What Foundation will never guarantee

- That a described object currently exists in the physical world
- That a described capability is currently available
- That a described condition is currently met
- That a person described is currently present
- That an obligation is currently satisfied

> **Foundation defines what a Fact *is*. Foundation does not decide what is factual now.**
> That is [truth-contract.md](truth-contract.md).

Any document asserting that Foundation owns truth is superseded by this contract.

### Declared location is not current location

Foundation owns the **`located-in` relationship** — the configured, durable statement of where
something belongs or is kept. **It is a definition, not an observation.**

| | Declared Location | Current Location |
|---|---|---|
| Owner | **Foundation**, as `located-in` | **Truth**, as a Location Fact |
| Carries confidence, provenance, freshness | No | **Yes** |
| Answers | *Where does this belong?* | *Where is it now?* |
| When unrecorded | `unknown` — *"an asset with no known location"* | Truth publishes `unknown`; **never defaults to a Room** |

A declared location may be **evidence** toward a Location Fact where a household governs it that way.
**It is never itself the Fact**, and a contradicting observation never rewrites it. See
[truth-contract.md](truth-contract.md).

---

## What consumers may rely upon

| Consumer | May rely upon |
|---|---|
| Stewardship | Asset identity, environmental limits as declared properties, relationships, caretaker relationship definitions |
| Identity | Person definitions, roles, relationships, consent records |
| Truth | Object identity, the eligible-evidence set declared by Room Configuration, capability descriptions |
| Continuity | Person, Room, and Experience definitions; configured experience endpoints |
| Operational Trust | Person roles, Room definitions, relationships, asset risk classification inputs |
| Concierge | Room Context, resolved vocabulary, exposed capability sets |

Foundation holds the **consent record** as a Person attribute. It does not own the consent lifecycle
(Identity) or consent policy and enforcement (Operational Trust). Foundation defines the
**caretaker-of relationship**; the **caretaker assignment** itself is owned by Stewardship.

---

## What consumers must never assume

- That existence implies participation
- That participation implies exposure
- That exposure implies authority
- That a Home Assistant Device, Entity, Area, or `person` is the same object as an HTBW Asset, Room,
  or Person
- That a vocabulary term renames or replaces an authoritative asset name
- That an absent relationship means no relationship exists
- That Foundation can confirm current state

---

## Uncertainty and unknown representation

Foundation represents:

| State | Meaning |
|---|---|
| `defined` | The object exists in the household model |
| `undefined` | No such object is defined |
| `unknown` | A property is not recorded — for example, an asset with no known location |
| `unresolved_anchor` | A backing platform object referenced by this definition no longer resolves |

`unknown` is never rendered as a default value.

---

## Failure and degradation behavior

| Condition | Behavior |
|---|---|
| A backing Home Assistant object disappears | Report `unresolved_anchor`; retain the HTBW object and its knowledge |
| Connected storage is unreachable | Report documentation as unavailable; never report it as absent |
| Configuration is incomplete | Report the gap explicitly; never infer the missing configuration |
| Two definitions collide | Surface for household resolution; never auto-merge |
| Definitions cannot be loaded | Fail closed — downstream responsibilities must treat scope as unknown, not as unrestricted |

---

## Privacy constraints

Foundation holds identity-adjacent and value-revealing data: people, relationships, consent records,
asset value, and documentation. Visibility is governed by
[operational-trust-contract.md](operational-trust-contract.md), not by Foundation.

Foundation must never expose biometric internals. Identity evidence associations are references, not
payloads.

---

## Explainability contributions

Foundation supplies to every Decision Trace:

- Room Context and how it was resolved
- Vocabulary resolution and its mapping source
- Authoritative object names used in the human-readable explanation
- Configuration provenance for participation, exposure, and authority scoping

---

## Open decisions

| ID | Question |
|---|---|
| OD-01 | Home Assistant representation strategy for HTBW objects |
| OD-02 | **Closed — DL-43, DL-44, DL-45.** Configuration and documentation are located through a governed artifact reference; encoding remains capability-specific |
| OD-10 | Whether Floors are a first-class scope |
| OD-11 | Whether one Physical Room may participate in more than one Room |
| OD-20 | Whether the standalone Asset Intelligence product is consumed as an optional source |

## Related documents

- [../architecture/framework.md](../architecture/framework.md)
- [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md)
- [../models/glossary.md](../models/glossary.md)
