# ADR: Room Configuration Ownership

> **Document status: Canonical ADR.**
> Status: **Accepted**.
> Terminology: [../models/glossary.md](../models/glossary.md).

---

## Context

Room Configuration emerged during the Concierge exploration and was, by default, treated as part of
Concierge. Contextual Vocabulary was likewise treated as a Concierge concern.

Three problems followed.

1. **The orchestrator owned the definition of its own context.** Concierge decided what a Room meant,
   then used that meaning to decide what to do — a circular authority.
2. **Room Configuration was described as an inventory screen.** Documentation drifted toward "which
   devices are in this area", losing the interaction semantics that made it valuable.
3. **Terminology forked.** Room, Composite Room, Merged Room, Interaction Space, Listening Area,
   Operational Space, and bare "Space" appeared across more than fifteen documents, sometimes in the
   same file.

---

## Decision

### 1. Room Configuration is owned by Foundation

**Room Configuration is an interaction-definition model. It is not an inventory screen and not merely a
location model.**

### 2. Contextual Vocabulary is part of Room Configuration

**Room Configuration owns the mapping. Concierge consumes the resolved target.** Vocabulary is not owned
by Concierge.

### 3. Four distinct states

| State | Meaning | Consequence |
|---|---|---|
| **Existence** | The thing is known to the Home | Nothing follows |
| **Participation** | It takes part in this Room's interaction model | It may be acted upon or contribute evidence |
| **Exposure** | Residents may address it here | It is discoverable and speakable |
| **Authority** | Someone may act upon it here, now | It may actually be operated |

Existence does not imply participation. Participation does not imply exposure. Exposure does not imply
authority.

### 4. The six questions are preserved

Room Configuration must always be able to answer:

1. What do you call this?
2. What can I do here?
3. Which devices participate?
4. Which devices are intentionally excluded?
5. Which sensors contribute to composite room truth?
6. Which vocabulary terms are available in this room?

**These questions must be preserved. This discovery must not be lost.**

### 5. "Merged Room" is the single canonical term

"Composite Room", "Operational Space", "Interaction Space", "Listening Area", and bare "Space" are
superseded. "Listening Area" becomes **the Room assigned to a participating voice assistant**.
"Interaction Space" becomes **Room Context**.

### 6. A Room and a Merged Room behave identically

There is **no separate orchestration path** for merged rooms. Movement between constituent Physical
Rooms inside one Merged Room is **neither a transfer nor a resume**, because no Room Context changed.

### 7. Voice assistant context resolves through the Room

A voice assistant is a **participating capability assigned to a Room**. The Room is the context; the
device is not. Two voice assistants assigned to the same Room resolve **identically**. Resolving context
from device names, from the Home Assistant Area alone when a Room definition exists, or by searching all
devices in the home, is prohibited.

### 8. Room Help comes from configuration, not inventory

**Room Help must be derived from the configured exposed capability set and vocabulary, never generated
from raw device inventory.** One configuration, many surfaces: voice, panel, and Room Help present the
same exposed set.

---

## Worked example — deliberate exclusion

```
Living Space (Merged Room: Kitchen + Dining + Living)
  Shades:      Kitchen 1 + Dining 3 + Living 3 = 7, addressed as one term
  Speakers:    the Sonos music speakers
  TV:          the LG television
  Media Player: the Apple TV
  Sonos Beam:  participates as TV audio, EXCLUDED from "Speakers"
```

"Play music on the speakers" must not reach the Beam. The exclusion is configuration, not an error, and
must be explainable as such.

---

## Consequences

### Superseded

- Room Configuration implicitly inside Concierge
- Vocabulary owned by Concierge
- `composite-room-contract.md`, replaced by
  [../contracts/room-configuration-contract.md](../contracts/room-configuration-contract.md)
- `room-vocabulary-registry-contract.md` and `room-vocabulary-registry-model.md`, replaced by
  [../contracts/contextual-vocabulary-contract.md](../contracts/contextual-vocabulary-contract.md)
- The composite-room section of `room-model.md`, replaced by [../models/room.md](../models/room.md)

### Established

- [../models/room.md](../models/room.md),
  [../models/room-configuration.md](../models/room-configuration.md),
  [../models/contextual-vocabulary.md](../models/contextual-vocabulary.md), and their contracts
- The prohibition on runtime device search for vocabulary resolution
- The prohibition on runtime sensor selection

### Not carried forward

> **Superseded authority is superseded, not inherited.** Recorded 2026-08-27 by the Episode 10
> governance narrative validation.

The superseded `adr-room-vocabulary-governance.md`,
`room-vocabulary-registry-contract.md`, and `room-vocabulary-registry-model.md` carried a **managed
vocabulary lifecycle** — *create, update, deprecate, retire vocabulary terms under governance*. **The
replacement set established above did not carry the deprecate-and-retire half forward**, and
**nothing in this ADR reactivates it.** A superseded document is evidence that a question once had an
owner; it is never authority for the answer.

The consequence is that **the household-facing effect of changing, retargeting, or withdrawing a term
is unowned**, which is now **OD-86**. **Recording this asserts no transitional alias, deprecation
window, grace period, or withdrawal behaviour**, and creates no lifecycle construct. The accepted
position is unchanged: **Room Configuration owns the mapping, Concierge consumes the resolved
target**, and vocabulary never renames or replaces the authoritative asset.

### Costs accepted

- Explicit configuration is more work for the household than inference. This is principle **P14 —
  explicit configuration over runtime discovery** — and it is accepted deliberately, because inference
  produces homes that behave unpredictably and cannot explain themselves.

---

## Alternatives considered

| Alternative | Why rejected |
|---|---|
| Leave Room Configuration in Concierge | The orchestrator would define its own context — circular authority |
| Derive room capability from Home Assistant Areas | Areas describe location, not participation, exposure, or authority |
| Infer vocabulary from entity names and aliases | Non-deterministic, unexplainable, and breaks the moment a device is renamed |
| Keep both "Composite Room" and "Merged Room" | Two names for one concept is the contradiction being removed |

---

## Open decisions

**OD-01** HA representation strategy; **OD-02** connected-storage format, **since closed as DL-43, DL-44, and DL-45**; **OD-10** Floors as a
first-class scope; **OD-11** a Physical Room in more than one Room; **OD-12** structured exclusion
reasons, **since closed as DL-103**; **OD-13** vocabulary inheritance; **OD-14** HA aliases; **OD-86** the household consequence of
changing or withdrawing a vocabulary term — distinct from **OD-13**, which is inheritance across scopes.

---

## Related documents

- [../models/room-configuration.md](../models/room-configuration.md)
- [../contracts/room-configuration-contract.md](../contracts/room-configuration-contract.md)
- [../contracts/contextual-vocabulary-contract.md](../contracts/contextual-vocabulary-contract.md)
- [../scenarios/room-vocabulary.md](../scenarios/room-vocabulary.md)
