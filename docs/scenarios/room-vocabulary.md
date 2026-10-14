# Scenario: Room Vocabulary

> **Document status: Canonical scenario.**
> Terminology: [../models/glossary.md](../models/glossary.md).
> Index: [README.md](README.md).

---

## The household

```
Living Space = Merged Room (Kitchen + Dining + Living)

Shades:        Kitchen 1 + Dining 3 + Living 3 = 7
Speakers:      Sonos music speakers
TV:            LG television
Media Player:  Apple TV
Sonos Beam:    participates as TV audio, EXCLUDED from "Speakers"
Lights:        overhead ceiling fixtures
Lamps:         table and floor lamps
```

Two voice assistants are assigned to the Living Space.

---

## Scenario 1 — One term, seven devices, two assistants

### What the household experiences

Tom stands in the Kitchen and says, "Close the shades." Seven shades close.

David stands in the Living area and says the same thing to the other assistant. The same seven shades
respond, identically.

Neither of them knows there are seven. Neither of them knows which assistant heard them.

### What each responsibility does

| Step | Responsibility | Action |
|---|---|---|
| 1 | Concierge | Receives the utterance from a voice assistant device |
| 2 | Room Configuration | Resolves the device → its assigned Room → **Living Space** |
| 3 | Contextual Vocabulary | Resolves "shades" in Living Space → the 7 configured shades |
| 4 | Truth | Reports the current state and availability of the resolved targets |
| 5 | Operational Trust | Confirms shade control is permitted here, now, at Autonomous level |
| 6 | Concierge | Closes them, and records the trace |

**The Kitchen and the Living area are constituent Physical Rooms of one Merged Room.** They resolve to
the same Room Context, so both assistants resolve identically. This is not two behaviors that happen to
agree; it is one configuration.

### What the home can say afterwards

> "I closed the shades in the Living Space."

Not: *"I closed `cover.kitchen_1`, `cover.dining_1` …"*

---

## Scenario 2 — A vocabulary term that is a knowledge asset

### What the household experiences

In the Music Room, Tom says, "Tell me about the piano." The home describes a 1918 A.B. Chase 6' grand
piano — its history, its service record, and its humidity requirements.

### What each responsibility does

| Step | Responsibility | Action |
|---|---|---|
| 1 | Room Configuration | Resolves Room Context → **Music Room** |
| 2 | Contextual Vocabulary | Resolves "piano" → the asset *1918 A.B. Chase 6' Grand Piano* |
| 3 | Foundation asset model | Supplies identity, documentation, and declared environmental limits |
| 4 | Stewardship | Supplies obligation state and service history |
| 5 | Truth | Supplies the current Music Room humidity |
| 6 | Operational Trust | Confirms Tom may see appraisal and value content |
| 7 | Concierge | Composes and speaks the answer |

**The vocabulary term did not rename the asset.** "Piano" is an interaction alias in this Room. The
authoritative name is unchanged.

---

## Scenario 3 — Lights are not Lamps

### What the household experiences

"Turn on the lights" turns on the overhead fixtures. "Turn on the lamps" turns on the table and floor
lamps. The household never has to say "turn on the light entities in the light domain".

### Why this matters architecturally

Home Assistant classifies both as `light`. **The platform domain must not dictate household
vocabulary.** The distinction is a household concept, held in Room Configuration, and it survives
regardless of how the platform classifies the devices.

| Term | Resolves to |
|---|---|
| Lights | explicitly selected overhead ceiling fixtures |
| Lamps | explicitly selected table and floor lamps |

---

## Scenario 4 — Speakers are not TV audio

### What the household experiences

Tom says, "Play music on the speakers." The Sonos music speakers play. **The Sonos Beam does not.**

### What each responsibility does

| Step | Responsibility | Action |
|---|---|---|
| 1 | Room Configuration | Resolves Room Context → Living Space |
| 2 | Contextual Vocabulary | Resolves "speakers" → the Sonos music speakers only |
| 3 | Room Configuration | Confirms the Beam **participates** as TV audio and is **excluded** from "Speakers" |
| 4 | Concierge | Plays on the resolved targets only |

The Beam **exists**. It **participates**. It is **not exposed** under this term. Those are three
different states, and the exclusion is configuration, not an error.

### If Tom asks why

> "The Beam is deliberately not part of *Speakers* in this room — it's set up for TV audio. Would you
> like me to use it anyway?"

Home Assistant classifies the Sonos speakers, the Beam, the LG television, and the Apple TV all as
`media_player`. HTBW distinguishes **Speakers**, **TV**, and **Media Player**. **This household
distinction is preserved.**

---

## Scenario 5 — Room Help

### What the household experiences

Tom says, "What can I do here?" The home answers with what is actually available in the Living Space,
in household language:

> "Here you can control the lights, the lamps, the shades, the speakers, the TV, and the media player.
> You can also ask about the artwork."

### What each responsibility does

| Step | Responsibility | Action |
|---|---|---|
| 1 | Room Configuration | Resolves Room Context → Living Space |
| 2 | Room Configuration | Returns the **configured exposed capability set** and the exposed-term list |
| 3 | Operational Trust | Filters by who is asking — a child or guest may see less |
| 4 | Concierge | Speaks the answer in household language |

> **Room Help must be derived from the configured exposed capability set and vocabulary, never generated
> from raw device inventory.**

The Beam is not offered. The individual seven shades are not enumerated. The Room Help answer, the panel,
and the voice surface all present **the same exposed set** — one configuration, many surfaces.

---

## Scenario 6 — An Authority-Derived Fact for room environment

### What the household experiences

Tom asks, "How warm is it in here?" The home says 72 degrees. It does not read out three sensors, and
it does not average them.

### What each responsibility does

| Step | Responsibility | Action |
|---|---|---|
| 1 | Room Configuration | Declares the **Primary Authority** for Living Space Temperature — one selected sensor (**DL-62**) |
| 2 | Truth | Reads that source's current state as an Authority-Derived Fact, with confidence, provenance, and freshness |
| 3 | Concierge | Reports the authoritative fact |

```
Truth: Living Space temperature = 72 degrees
       truth_confidence_band: High
       provenance: Sensor C
```

**Room Configuration does not calculate Truth. Truth does not own the sensor inventory. Concierge does
not choose sensors at runtime. No accepted household use case requires averaging the Living Space's
other capable sensors into this answer (DL-62).**

### If the Primary Authority fails

> "I can't tell how warm it is in here right now — the configured sensor for the Living Space isn't
> reporting."

Truth publishes `unknown`; it never silently switches to another capable sensor, and it never retains
the last reading as current.

---

## Scenario 7 — A term that is not configured here

### What the household experiences

In the Den, Tom says, "Close the shades." The Den has no configured shades.

### What the home does

> "There aren't any shades configured in the Den. In here you can control the lights, the speakers, and
> the TV."

**The home does not search the house for anything called a shade.** It does not guess. It does not close
the Living Space shades. It states what is configured, and offers what is available.

---

## Scenario 8 — Native names and aliases seed the configuration

The household has already named things in Home Assistant. **They are not asked to do it again.**

| # | Situation | What happens |
|---|---|---|
| 8a | An Entity becomes eligible, has a native name, and has no HTBW term | The native value is offered as the **seed**. Home Assistant stays authoritative for its own name. **HTBW creates no independently maintained duplicate merely to reproduce the same value**, and nothing is written back |
| 8b | The Entity also has an applicable native Assist alias | The alias may be presented as a selectable seed, attributed to Home Assistant. **Accepting or editing the term does not modify the native alias.** Where several aliases apply, none is chosen silently |
| 8c | Tom customizes *Desk Lamp* to **"Lamp"** in the Office | "Lamp" becomes Office contextual vocabulary. The native name and aliases are **unchanged**. Office Room Context resolves the target |
| 8d | The native Entity is later renamed | The new native name is read from Home Assistant. **The customized term stays "Lamp".** HTBW may say the native source changed and offer re-import. **Nothing is overwritten in either direction** |

---

## Scenario 9 — The same term in several Rooms

"Lamp" is configured in the Office, the Guest Room, and the Living Space.

| Room | "Lamp" resolves to |
|---|---|
| Office | the configured Office lamp target |
| Guest Room | the configured Guest Room lamp target |
| Living Space | a **configured group** of participating lamps |

Each Room resolves the term through its own configuration. **Reuse across Rooms is not an error** —
it is the point. **No native alias is written to any target**, and the Living Space group is
**not** projected as an alias onto each member. Explicit exclusions stay excluded.

This is exactly what a native alias cannot carry: one of these three targets is a group, and all
three depend on Room context that Home Assistant does not model.

---

## Scenario 10 — A Device with several Entities

The LG television is one native Device with many Entities — power, source, volume, and diagnostics.

**A Device-level term is not assumed to apply to every Entity.** The configuration identifies the
actual target or capability participating, native Device and Entity relationships remain
authoritative, and the mapping stays deterministic. **"TV" does not silently mean "everything this
Device offers".**

---

## Scenario 11 — Native Assist exposure is turned off

Home Assistant exposure is removed from a participating Entity.

| State | Result |
|---|---|
| Native Assist exposure | Withdrawn. **The platform boundary moves** |
| HTBW participation | Unchanged |
| HTBW contextual exposure | Unchanged as configuration |
| Authority | Unchanged |

**The contextual term does not bypass the native restriction.** Room Help does not advertise a native
Assist capability the platform will not honour, or one the asking resident is not authorised to know
about. Four distinct states — **never one checkbox.**

---

## Scenario 12 — Merging, and a deleted target

| # | Situation | What happens |
|---|---|---|
| 12a | The Kitchen and Living Rooms are combined | Native names and aliases are **unchanged**. Merged vocabulary is **declared**, not inherited automatically. Where constituents used one term for different targets and the merged configuration is silent, the result is `ambiguous` and is surfaced. **No alias synchronisation occurs.** **OD-70 remains open** |
| 12b | The Merged Room is later unmerged | Constituent membership was retained, so constituent Room behaviour is restored. Native objects were never touched |
| 12c | A native target is deleted outside HTBW | The reference becomes **unresolved** and follows the Repairs and broken-reference boundary. **The customized term is never automatically reassigned to another object**, and historical references are not rewritten |

---

## Scenario 13 — One configured term, several recognised forms

Tom configures **Lamp** in the Office. He configures nothing else.

| # | Situation | What happens |
|---|---|---|
| 13a | "Turn on the lamp" | The configured term matches directly |
| 13b | "Turn on the **lamps**" | Recognised as a form of *Lamp*, resolving to **the same configured target** — not to more targets |
| 13c | Tom opens the Office configuration | He sees *Lamp*, and alongside it that *Lamps* will be understood. **Only *Lamp* is editable.** There is no plural field to fill in, and none to keep in step |
| 13d | The same configuration for **Shade** | *Shade* and *Shades* are both understood. **No separate plural entry exists** |

**The resident maintains one value. The home derives the rest.**

---

## Scenario 14 — The plural that is a group

In the Living Space the household configured **Lamps** deliberately, as the Corner Lamp, the Sofa
Lamp, and the Bookcase Lamp. The Office still has **Lamp**, meaning one desk lamp.

| Room | "Turn on the lamps" resolves to |
|---|---|
| Living Space | The **configured group** — three lamps. A configured term always outranks a derived form |
| Office | The **single configured target**, matched through a derived form. **Saying the plural did not add lamps to the Room** |

**These are different concepts and the repository keeps them apart.** *Lamps* as a grammatical form of
*Lamp* means the same thing said differently. *Lamps* as a group term means a larger, explicitly
configured target set. **Plurality alone never creates the group** — someone configured it.

If a word matched derived forms of two configured terms and no configured term, the result is
`ambiguous` and the home asks. It does not pick one.

---

## Scenario 15 — Explaining what was heard

Tom says *"Turn on the lamps"* in the Office.

| Recorded | Value |
|---|---|
| Recognition form heard | Lamps |
| Authoritative vocabulary | Lamp |
| Resolved target | The configured Office lamp target |
| Room Context | Office |

And the home simply says: *"I turned on the lamp in the Office."* **The explanation is available
without the resident needing to know anything about grammar, derivation, or entity IDs.** Where a
separate group configuration governs the word, that configuration is what is recorded and explained
instead.

---

## Scenario 16 — Lamps: collection versus member-level Vocabulary (DL-69)

Living Space configures the collection term **Lamps** → Sofa Lamp + Corner Lamp + Reading Lamp, and
separately configures member-level terms **Sofa Lamp**, **Corner Lamp**, and **Reading Lamp** for
those same three members.

| Utterance | Outcome |
|---|---|
| "Turn on the lamps" | Executes the full configured Lamps set |
| "Turn on the lamp" | `ambiguous` — more than one configured member-level term matches. The home asks: *"Which lamp: Sofa Lamp, Corner Lamp, or Reading Lamp?"* — never full native names, never unconfigured devices, never targets outside Living Space |

Had the household configured **only** the collection term "Lamps" with no member-level terms, "turn on
the lamp" would remain a recognition form of "Lamps" and would activate the full set, exactly as
Scenario 15 shows for a single-target case — **no new state is introduced; the existing `ambiguous`
outcome now also covers this case once member-level terms exist.**

---

## Scenario 17 — Person-scoped Vocabulary (DL-69)

Tom's configured mailbox is called **Mail** by Tom. The same mailbox capability, if configured for
another Person, could be called **Inbox** by them instead.

Tom says, in the Kitchen: *"Do I have any mail?"*

| Step | Responsibility | Action |
|---|---|---|
| 1 | Identity | Evaluates current eligible evidence for Tom |
| 2 | Room Configuration | Resolves Room Context (Kitchen); no Room-scoped "Mail" term exists |
| 3 | Vocabulary (Person context, DL-69) | Resolves "Mail" against Tom's current Person-scoped Vocabulary |
| 4 | Operational Trust | Confirms Tom's authority to hear this content in this audience |
| 5 | Concierge | Answers using Tom's configured mailbox capability |

**No Person-scoped Vocabulary, or the existence of the underlying capability, is disclosed to another
Person present without authorization**, and an Unknown Person receives no Person-scoped mapping.

---

## Scenario 18 — "Bedtime": no HTBW match, safe native boundary (DL-69)

No Room or Merged Room has configured a "Bedtime" Vocabulary term.

Tom says, in the Primary Bedroom: *"Bedtime."*

**Forbidden outcome:** the request silently falls through to a native interpretation that turns on
every light in the Room, because no configured HTBW match exists.

**Accepted outcomes**, in order of preference given available evidence:

| Condition | Outcome |
|---|---|
| An exact, permitted, exposed, and safe native automation or intent matches "Bedtime" | Native handoff may proceed |
| Recognized text is uncertain and a bounded candidate exists (for example, the household has a Vocabulary term or safe native automation named similarly) | Replay what was heard, or offer a bounded "did you mean" suggestion — **execute only after confirmation** |
| No safe candidate exists at all | *"I didn't understand that."* — a safe, honest no-match response |

**Never accepted**: executing a materially broader native action (turning on every Room light) merely
because some native interpretation of the misheard or unmatched text happened to be executable. The
event is traceable under [decision-trace.md](../models/decision-trace.md)'s Vocabulary and
command-resolution fields.

---

## Production provenance

The desired household outcome demonstrated throughout this document — residents use natural household
vocabulary to address a Room or Merged Room's participating, exposed, authorized capabilities, without
knowing device names, entity IDs, or Home Assistant domains, and without Concierge searching Home
Assistant inventory at runtime — is already established architecture, not a new finding of this or any
single production-behavior review:

| Outcome element | Established by |
|---|---|
| Resident vocabulary addresses a Room/Merged Room without device names, entity IDs, or domains | [framework.md](../architecture/framework.md) §7 Concierge: *"runtime discovery of which assets a household meant when an explicit room mapping exists"* is listed under what Concierge **does not own** |
| Setup declares participation, exclusion, exposure, vocabulary, vocabulary-to-target mapping | [room-configuration-contract.md](../contracts/room-configuration-contract.md), "What Room Configuration guarantees"; **DL-09**, **DL-10**, **DL-11** |
| Setup declares applicable (room-scoped) authority | [room-configuration-contract.md](../contracts/room-configuration-contract.md): *"Room-scoped authority scoping inputs"*; authority itself is decided by Operational Trust, never Room Configuration or Concierge |
| Setup declares authoritative sources for informational capabilities | [room-configuration-contract.md](../contracts/room-configuration-contract.md): Primary Authority declaration (**DL-60**, **DL-62**); Scenario 2 (piano), Scenario 6 (temperature) above |
| No runtime device search to resolve vocabulary | [adr-room-configuration-ownership.md](../architecture/adr-room-configuration-ownership.md) §7; [concierge-contract.md](../contracts/concierge-contract.md) hard prohibition #3 |

[production-behavior-inventory.md](../reference-home/production-behavior-preservation/production-behavior-inventory.md)
records that the current production implementation derives this same class of outcome — lamp/light,
shade, media-player, and room-capability-discovery membership alike — **"at runtime, every single time a
behavior executes," "duplicated independently across 6–12 scripts and automations"** (for example
**BHV-01**, **BHV-02**, **BHV-04**, **BHV-06**, **BHV-13**). This corroborates that the desired outcome
is genuine, recurring household value — it is **not** a reason to carry the runtime-discovery mechanism
forward, and it does **not** by itself accept, migrate, or retire any individual production behavior.
**Each production behavior still requires its own disposition review** before its production mechanism
may be considered superseded; the entries below record that review for behaviors already examined.

---

### BHV-01 — Room-local lamp/light on-off control

[docs/reference-home/production-behavior-preservation/production-behavior-catalog.csv](../reference-home/production-behavior-preservation/production-behavior-catalog.csv)
(**BHV-01**) and
[production-to-htbw-reconciliation-matrix.csv](../reference-home/production-behavior-preservation/production-to-htbw-reconciliation-matrix.csv)
record a live household behavior: a resident says "lamps on", "lights off", or "lights usual" in any
Room without naming it, and only that Room's lamps (or only its overhead/architectural lights) respond,
at a remembered brightness where applicable. This is preserved **household experience**, cited here as
corroborating evidence for scenarios already accepted above — it creates no new architecture.

| BHV-01 production fact | Already-accepted scenario/authority here |
|---|---|
| "Lamps" and "Lights" are distinct household terms though both are HA `light`-domain | Scenario 3 — *Lights are not Lamps* |
| A fixture can participate in a Room yet be excluded from a vocabulary term | Scenario 4 — *Speakers are not TV audio* (deliberate exclusion) |
| A Room with no configured lamps/lights must not search elsewhere or broaden the request | Scenario 7 — *A term that is not configured here*; Scenario 18 |
| The same word ("Lamps") can resolve to different configured participants in different Rooms | Scenario 9 — *The same term in several Rooms* |
| Room context is supplied by the speaking device without the resident naming the Room | Scenario 1 |

**Production mechanism not carried forward.** Production resolves lamp-vs-light membership at every
invocation via `label_devices('Lamps')`/`label_devices('Lights')` and `area_entities()`. This is the
runtime device search [adr-room-configuration-ownership.md](../architecture/adr-room-configuration-ownership.md)
§7 and [../contracts/concierge-contract.md](../contracts/concierge-contract.md)'s hard prohibition
("Concierge must not runtime-search devices to satisfy a vocabulary term. Resolution is explicit and
configured.") already prohibit. Home Assistant Labels carry no HTBW meaning
([home-assistant-boundary.md](../architecture/home-assistant-boundary.md), native-concept consumer
table: "Labels … Nothing … Labels are flat, global, and ungoverned"); they are, at most, setup-time
candidate evidence under the same **DL-11**/**DL-60** "seeds a proposal, never automatic participation"
pattern already established for Areas — never runtime vocabulary authority.

**Deferred, not decided here.** Two genuinely open decisions already own the remaining questions and
are not reopened or duplicated by this note:

- **OD-73** — *Interaction-Surface Room Context Resolution* (Open — Research Required, issue **#134**)
  owns exactly how room context physically reaches Concierge from the speaking device. BHV-01's
  `area_id(trigger.device_id)` production pattern is additional evidence for that research, not a
  resolution of it.
- **OD-78** — *Remembered-Value Classes and Restoration Semantics* (Open — Blocked, issue **#149**)
  owns the provenance of the brightness value "usual" restores. BHV-01 only requires that an already-
  authorized value can be consumed; [continuity-contract.md](../contracts/continuity-contract.md)
  already governs safe consumption ("Preferences unavailable | State that the preference could not be
  read; never substitute a platform default silently").

---

## Responsibilities exercised

| Responsibility | Exercised by |
|---|---|
| Foundation | Asset identity, Room and Merged Room object definitions |
| Room Configuration | Merged Room composition, participation, exclusion, exposure, eligible contributors, Room Help |
| Contextual Vocabulary | Term → target resolution in every scenario |
| Truth | Authority-Derived temperature, availability, current state |
| Stewardship | Piano service history and obligations |
| Operational Trust | Room Help filtering, permission to act |
| Concierge | Interpretation, execution, explanation |

## Related documents

- [../models/room-configuration.md](../models/room-configuration.md)
- [../models/contextual-vocabulary.md](../models/contextual-vocabulary.md)
- [../contracts/room-configuration-contract.md](../contracts/room-configuration-contract.md)
- [../contracts/concierge-contract.md](../contracts/concierge-contract.md)
- [../contracts/continuity-contract.md](../contracts/continuity-contract.md)
- [../architecture/framework.md](../architecture/framework.md)
- [../architecture/adr-room-configuration-ownership.md](../architecture/adr-room-configuration-ownership.md)
- [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md)
- [../reference-home/production-behavior-preservation/production-behavior-catalog.csv](../reference-home/production-behavior-preservation/production-behavior-catalog.csv)
- [../reference-home/production-behavior-preservation/production-behavior-inventory.md](../reference-home/production-behavior-preservation/production-behavior-inventory.md)
