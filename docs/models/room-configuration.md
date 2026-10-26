# Room Configuration Model

> **Document status: Canonical model.**
> Terminology: [glossary.md](glossary.md). Owning responsibility: **Foundation**.
> Contract: [../contracts/room-configuration-contract.md](../contracts/room-configuration-contract.md)

---

## Purpose

**Room Configuration is an interaction-definition model. It is not an inventory screen and not merely
a location model.**

This is one of the most important architectural discoveries carried forward from the exploratory
Concierge work. The original Room Setup achieved a valid and essential household outcome. The
outcome is preserved; the ownership is corrected.

## Question answered

*In this Room, what participates, what is exposed, what do residents call it, what can they do here,
and which sensors feed the room's composite facts?*

---

## The canonical distinction

| Statement | Owner |
|---|---|
| The asset model defines **what exists** | Foundation (asset model) |
| Room Configuration defines **what participates** | Foundation (Room Configuration) |
| Room Configuration defines **what is exposed** | Foundation (Room Configuration) |
| Room Configuration defines **how residents refer to the participating resources** | Foundation (Room Configuration) |
| Truth defines **what is happening** | Truth |
| Operational Trust defines **what is allowed** | Operational Trust |
| Concierge determines **what should happen** | Concierge |

> Do not place canonical Room Configuration ownership inside Concierge merely because the exploratory
> Concierge integration contained the setup UI.
>
> **Concierge consumes Room Configuration.**
>
> The eventual unified HTBW UI may expose Room Configuration through a room-oriented experience, but
> **UI placement does not change architectural ownership.**

---

## The four states

These must never be conflated.

| # | State | Definition |
|---|---|---|
| 1 | **Existence** | The asset, device, entity, sensor, person, pet, service, or relationship is known. |
| 2 | **Participation** | The item has been explicitly selected to contribute to a Room capability, experience, composite fact, or interaction. |
| 3 | **Exposure** | The item or grouped capability is intentionally made available to residents through vocabulary, Room Help, UI, conversation, or another interaction surface. |
| 4 | **Authority** | A person or automated process is permitted to use, change, query, or act on the exposed capability. |

Principles P5–P7:

- Asset existence does not imply room participation.
- Room participation does not imply resident exposure.
- Resident exposure does not imply permission to act.

> **Exposure here is the HTBW constitutional state. It is not Home Assistant Assist entity
> exposure.** Assist exposure decides whether an assistant may target an entity; HTBW Exposure
> decides whether something may be perceptible to a resident. **Assist exposure is a platform safety
> boundary that HTBW may narrow and must never widen past or bypass** (**DL-66**), scoped to voice-
> and conversation-mediated interaction; a non-voice surface is independently governed. The canonical
> explanation and the precedence rule are in
> [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md).

Worked examples:

| Example | States |
|---|---|
| A Sonos Beam exists but does not participate as a music speaker | Exists, not participating (as a music speaker) |
| A temperature sensor exists, is not exposed conversationally, but participates as evidence for a Composite Fact about Room temperature | Exists, participates, not exposed |
| A piano exists, participates as a knowledge asset, and is exposed under the vocabulary term "Piano" | Exists, participates, exposed |
| Seven shades exist and are exposed collectively as "Shades" | Exist, participate, exposed as a group |
| A guest may see that lights are available but may not change security settings | Exposed, no authority |

---

## What Room Configuration owns or establishes

- Room identity
- Constituent Physical Rooms or Areas
- Participating voice assistants, or decoupled `voice_input`/`spoken_response_output` participating
  capabilities (drafted, pending #198)
- Participating controllable assets
- Participating knowledge assets
- Participating music speakers
- Participating television or video assets
- Participating environmental sensors
- Participating occupancy or presence evidence sources
- **Explicitly excluded assets**
- Contextual vocabulary
- Vocabulary-to-target mappings
- Capability exposure
- Room Help definitions
- Composite-fact input selection
- Experience endpoints
- Relevant Room modes
- Human-friendly room configuration

Explicit exclusion is first-class. Participation is one of three distinct states, and the deliberate
exclusion must survive later re-configuration and be explainable.

| Participation state | Meaning |
|---|---|
| **Participating** | The asset or capability takes part in this Room's interaction model |
| **Not Selected** | The asset is known to the Home but was never considered for this Room |
| **Deliberately Excluded** | The asset was considered and intentionally kept out of this Room, or out of a specific vocabulary term |

**Not Selected** and **Deliberately Excluded** must never be collapsed. Only the latter is
explainable as an intention.

### Room Configuration extends an Area; it does not copy it

Governed by **DL-31** and
[../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md).

Home Assistant remains authoritative for the Area's **name, picture, `floor_id`, `aliases`, `labels`,
and its assigned temperature and humidity entities**. Room Configuration **references the Area by its
area ID** and stores only the interaction extensions listed above.

**None of those native values is copied into Room Configuration.** An Area rename, picture change, or
Floor move therefore requires **no synchronisation**, because there is nothing to keep in step. A
resident who has named and organised an Area in Home Assistant must **never be asked to do so again**
in HTBW.

A **Merged Room** likewise **references** its constituent Areas or Rooms. Constituent definitions are
never copied into the Merged Room; only the merged interaction semantics are HTBW-owned. **A Merged
Room has no native Home Assistant representation, and none is invented (DL-68, resolved OD-70)**: no
canonical consumer requires one, and Assist/Conversation must never receive one, since it would let
native intent matching bypass HTBW's own curated participation, exclusions, and exposure narrowing.

> **A Physical Room (Area) participates in at most one Merged Room at a time (DL-67).** A Merged Room
> is a curated conversational interaction context, not a general-purpose grouping mechanism; allowing
> overlapping membership would force Fact selection, session and transfer detection, policy scoping,
> and vocabulary resolution each to invent their own rule for which Merged Room currently applies,
> reintroducing the special-case orchestration **DL-13** rejects. A broader or capability-specific
> grouping ("Downstairs") is met by Home Assistant's own native Floor and Area targeting, never by an
> overlapping Merged Room.

### Selecting participating objects

The configuration experience distinguishes **available** native objects from **participating** ones.

**A Physical Room's available candidates are objects associated with its own native Area. A Merged
Room's available candidates are the union of objects associated with every constituent Physical
Room's Area (DL-70).** This is the *only* difference between configuring a Physical Room and a Merged
Room — once participation, exposure, and Vocabulary are configured, both behave identically in every
other respect (**DL-13**, **DL-67**).

*Available* objects are the Devices and Entities associated with, or otherwise eligible for, the
native Area the Room represents. Eligibility uses supported Home Assistant relationships and remains
subject to participation and exposure governance; it is never an unrestricted inventory.

Moving an object into participation **does not** rename it, change its native aliases, expose it to
Assist, grant authority to use it, make every one of its capabilities resident-visible, or include
every Entity belonging to a Device. **A Device-level term is never assumed to apply to all of that
Device's Entities**; the participating target or capability is identified explicitly.

#### Explicit participation already selects the execution provider (DL-55)

Where one physical endpoint is represented by more than one technical provider (for example a Sonos
speaker visible through the native Sonos integration, Music Assistant, and the Home Assistant device
registry simultaneously), **participation's existing rule that the target is identified explicitly
already resolves which provider executes** — the household's (or configuration flow's) explicit
native reference names one concrete entity, not an abstract capability class, so there is no runtime
choice left to make. **No separate provider-precedence mechanism is required for execution.** A
provider whose entity was not selected may still contribute identity, capability, or connectivity
**evidence** through Truth, but it never becomes a competing execution or attestation authority for
that participating target (**DL-41**, **DL-54**). Endpoint identity across multiple provider records
for one physical thing is the existing **Asset** model's concern where the household has declared an
Asset (`docs/models/asset.md`: one Asset may be represented by several Devices); where no Asset is
declared, the participating target's own native reference is a sufficient identity anchor for this
Room's purposes, and no name/room/IP/vendor matching is required or permitted. Residual runtime
questions this does not answer — room-level outcome aggregation across several participating
endpoints, and configuration evolution as capabilities change — are addressed in
[../architecture/failure-and-degradation.md](../architecture/failure-and-degradation.md) and this
model's existing failure-behavior table, respectively. See **OD-88**, resolved as **DL-55**.

For each participating target the configuration may present the native reference, the native display
name, applicable native Assist aliases, native Assist exposure status, the HTBW contextual term,
whether that term is seeded or household-defined, target scope, participation status, explicit
exclusions, ambiguity indicators, and Merged Room implications. **This is an architecture
description. It prescribes no frontend technology, layout, or component.**

Native naming information may **seed** a contextual term when a target first participates. The seed is
attributed to Home Assistant, never synchronised afterwards, and **never written back**. A
household-defined term survives a later native rename. The full rule is
[contextual-vocabulary.md](contextual-vocabulary.md).

### Four states that must not be collapsed

| State | Owner | Question it answers |
|---|---|---|
| **Native Assist exposure** | Home Assistant | May an assistant target this entity at all? |
| **HTBW participation** | Room Configuration | Does this object take part in this Room's interaction model? |
| **HTBW contextual exposure** | Room Configuration | Is it reachable by a term, and offered in Room Help? |
| **Authority** | Operational Trust | Is this resident permitted to act on it, or to know it exists? |

**These are four distinct states, never one checkbox and never one semantic concept.** Where the
configuration displays exposure, it must say which of the four it is showing. HTBW may narrow native
Assist exposure and must never widen past or bypass it (**DL-66**); the canonical explanation is in
[../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md).

### When the native object changes

| Native change | Required behaviour |
|---|---|
| Device or Entity renamed | The new name is read from Home Assistant. **A household-defined term is unchanged.** An unaccepted seed may be refreshed |
| Aliases added, removed, or changed | Same treatment. HTBW may report that the native source changed and offer re-import. **Nothing is imported automatically over a household-defined term** |
| Native Assist exposure changes | The platform boundary moves. Participation and vocabulary are unchanged; what may be voice-targeted follows the native setting |
| Object moves to another Area | Participation is **not** silently redefined. The condition is surfaced and resolved through this lifecycle |
| Object disabled or unavailable | Vocabulary is retained. Resolution reports the condition. **Unavailability never deletes a term** |
| Object deleted | The reference becomes unresolved and follows the Repairs and broken-reference boundary. **A term is never automatically reassigned to another object, and historical references are never rewritten** |
| The Room is inside a Merged Room | The same rules apply. The Merged Room is a Room |

Removing an object from participation **never renames or alters the native object.**

---

## The questions Room Configuration must keep answering

These were successful outcomes of the original Concierge Room Setup and must not be simplified away
into a generic room-grouping model:

- **What do you call this?**
- **What can I do here?**
- **Which devices participate?**
- **Which devices are intentionally excluded?**
- **Which sensors contribute to composite room truth?**
- **Which vocabulary terms are available in this Room?**

> These questions are preserved verbatim. In canonical terminology, "composite room truth" means a
> **Composite Fact** scoped to the Room — a fact Truth derives from more than one eligible contributing
> sensor. It is unrelated to the superseded term "Composite Room". See [glossary.md](glossary.md).

---

## Voice assistant context

Participating voice assistants are explicitly assigned to a Room configuration.

**"Voice assistant" here denotes any participating capability assigned a `voice_input` Interaction
Function Assignment** — whether fulfilled by an integrated voice-assistant device or a dedicated
microphone/microphone-array endpoint — and the device that captured the utterance is never assumed to
be the device that delivers the spoken response; the response destination is the Room's separately
assigned `spoken_response_output`, which may be the same device or a different one. See
[../architecture/adr-decoupled-voice-interaction-capability-architecture.md](../architecture/adr-decoupled-voice-interaction-capability-architecture.md)
(drafted, pending #198). The resolution order below is unchanged by this clarification.

When a participating voice assistant receives a request, **its Room assignment provides the default
Room Context.** The resident should not need to state the Room name.

Resolution order for a spoken request:

1. Voice assistant identity
2. Assigned HTBW Room Context
3. The exclusive Merged Room (**DL-67**), if the Physical Room participates in one
4. Persisted Vocabulary mapping, resolved by context precedence — active clarification, current
   Person (for a Person-owned capability), current Merged Room, current Physical Room, Home (Global)
   scope (**DL-69**, **DL-70**; see [contextual-vocabulary.md](contextual-vocabulary.md))
5. Explicit target set
6. Applicable Identity, Truth, Continuity, Stewardship, and Operational Trust context
7. Concierge evaluation and orchestration; native fallback considered only where no governed match
   exists and only where safe (**DL-69**)

Two voice assistants participating in the same Room produce the **same** target resolution.

Prohibited:

- Runtime discovery of nearby devices
- A query across every device in the Room
- Requiring the resident to name the Room
- Requiring the resident to know individual target names
- Automatic inclusion of every matching device in every constituent Room

Separation to preserve:

- **Identity** may determine who spoke.
- **The voice assistant assignment** determines the default Room Context.
- **Truth** may confirm or refine current person presence where required.

Do not collapse these separate responsibilities.

### Interaction surfaces that are not bound to a Room

The resolution order above is defined for a **room-bound** surface — a participating voice assistant, a
participating kiosk, or another endpoint the household has assigned to a Room.

**It is not defined for a surface that is not bound to a Room**: a phone, a wearable, a Companion App
action, or a browser session. Such a surface may carry very strong **person** binding while carrying no
**room** binding at all, and the two must not be confused.

| Rule | Statement |
|---|---|
| The governed outcome today is `unresolved` | Ask which Room, or refuse, per policy. **This is correct behaviour, not a failure** |
| **Never infer from device naming** | Unchanged from the failure table below, and it applies to surfaces exactly as it applies to targets |
| Never substitute a plausible Room | A wrongly resolved Room resolves the wrong vocabulary, targets the wrong assets, consults the wrong Room's facts and modes, and produces a trace that is internally consistent and externally wrong |
| A person binding is not a room binding | An authenticated surface may establish **Authenticated Session Identity** or **Interaction Initiator** — and establishes **no Room Context** |
| The trace must say so | Every Decision Trace records Room Context **and how it was resolved**; where it was not resolved, it records `unresolved` and the reason. See [decision-trace.md](decision-trace.md) |

> **How Room Context may be resolved for such a surface is open decision OD-73.** The obvious input — the
> device's current location — is a **Truth** Fact, and [../architecture/dependency-view.md](../architecture/dependency-view.md)
> rule 6 states that **Foundation consumes nothing**. That is an ownership and directional question, not an
> implementation detail, and it is recorded rather than resolved here.

---

## Room Help and capability exposure

When a resident asks **"What can I do here?"**, the answer is generated from the deliberately
configured Room interaction model.

**Room Help must not be generated from:**

- Every Home Assistant entity
- Every device in the Physical Room
- Every asset known to the asset model
- Every sensor
- Every internal diagnostic
- A live runtime inventory search

Room Help describes only intentionally exposed vocabulary and capabilities. Example content:

- Control the lights
- Control the lamps
- Open or close the shades
- Play music
- Control the TV
- Use the media player
- Ask about the piano

**Room Help is a projection of configured participation, vocabulary, capabilities, and exposure. It
is not an inventory report.**

Native Home Assistant names and aliases may **seed** the configuration, but they **never independently
determine Room Help content**. Room Help must not advertise an excluded target, a non-participating
target, a capability not exposed through this configuration, or anything the asking resident is not
authorised to use or to know exists.

**Room Help lists authoritative vocabulary terms only.** Derived recognition forms improve
understanding; they are not separately advertised capabilities, and Room Help does not enumerate them.

### One configuration, many surfaces

The same canonical Room configuration must drive:

- Voice target resolution
- Room Help
- Resident-facing controls
- Capability exposure
- Explainability
- Diagnostics

This is what prevents drift between what the home says is available and what commands actually do.

### Presentation-purpose vocabulary is vocabulary, not a new concept

A household term such as "Speaker" resolving to a Room's music endpoints, or "Display" resolving to
its visual endpoint, is an ordinary application of the existing **vocabulary-to-target mapping** above
— it requires no new capability. Room Configuration continues to own only **which target set a term
resolves to**; it does not own, and must not be asked to resolve, **which currently available
technical provider or evidence path** delivers through that target at a given moment, nor how a
Room-defined outcome spanning several endpoints is aggregated. Those runtime questions are **OD-88**.

---

## Sensors and Composite Facts

Many sensors may exist in a Room without being exposed to residents or used individually by
Concierge.

| Step | Owner |
|---|---|
| Retain all sensors and their authoritative records | Asset model (Foundation) |
| Select the **Primary Authority** for each Environmental Purpose (**DL-62**) | Room Configuration |
| Establish the Authority-Derived Fact, or a Formula-Derived Fact where the purpose is derived | **Truth** |
| Consume the Fact | Concierge and residents |

Example:

```
Asset model knows:        Temperature Sensor A, B, C
Room Configuration says:  Sensor C is the Living Space Temperature Primary Authority
Truth establishes:        Living Space temperature is 72 degrees (Truth Confidence Band, provenance)
Resident hears:           "It's 72 degrees in the Living Space."
```

Raw evidence remains available for diagnostics, provenance, calibration, and explainability where
authorized.

Boundaries:

- **Room Configuration does not calculate Truth.**
- **Truth does not own the sensor inventory.**
- **Concierge does not choose sensors at runtime.**

### The Room Environment Standard (DL-60)

Resolves **OD-61**. Full acceptance record is **DL-60** in
[decision-ledger.md](../governance/decision-ledger.md); this section is the canonical model.

**Room Configuration defines an extensible household-oriented Environmental Purpose set** — the
available meanings a source may be mapped to in a Room. Representative purposes include: temperature,
humidity, dew point, illuminance, UV, VOC, particulates (PM2.5, PM10), CO2, mold index, leak, pressure,
vibration, noise, and window/orientation/exposure characteristics.

**The set is extensible, never closed, and never claims universal availability.** New integrations and
sensor classes may be mapped to it without redesigning Room Configuration. A household need not have a
sensor for every purpose; an unconfigured purpose is simply **unavailable**, never invented, and never
converted into a normal, healthy, or safe default value merely because no sensor exists.

**One configuration serves every consumer.** The same Environmental Purpose participation and
authority selection is used for direct Room-level questions, Composite Facts, Asset environmental
requirement evaluation, Stewardship obligation evaluation, and household-facing explanation. No
separate environmental mapping exists per consumer.

#### Disambiguating multiple same-purpose sources

More than one eligible source may exist for one Environmental Purpose in a Room — for example an
air-quality sensor's temperature reading, a presence sensor's temperature reading, and a thermostat's
temperature reading, all in the same Room. **Existence does not make all of them participants, and
participation does not make all of them equally authoritative.** Room Configuration represents three
distinct, non-collapsible states per purpose (**DL-62** narrows this from the four states originally
accepted under **DL-60**; see *Primary Authority is required for the ordinary path*, below):

| State | Meaning | At most one per purpose? |
|---|---|---|
| **Primary Authority** | The source every direct Room-level question resolves to — **required** for every directly measured Environmental Purpose the Room has configured | Yes |
| **Secondary / Corroborating** | Contributes supporting or contradicting context; never itself the direct answer; may inform **DL-63** conflict diagnostics | No |
| **Explicit Exclusion** | Deliberately kept out, exactly as the existing three-state participation model already requires | No |

**Runtime never arbitrates among equivalent same-purpose sources** — never by query order, entity
order, alphabetical order, integration load order, most recent value, vendor preference, or "whichever
responds first." Only the household's Room Configuration selection determines which source is primary
or secondary for a given purpose.

*"What is the current temperature in the Den?"* resolves to the Truth Fact produced from the Den's
configured **Primary Authority** for Temperature. **Where no Primary Authority is configured for a
directly measured purpose, the purpose is unconfigured or unavailable** — never invented, and never
silently satisfied by an implicit combination of whatever sources happen to exist.

#### Primary Authority is required for the ordinary path (DL-62)

Resolves **OD-17**. Full acceptance record is **DL-62** in
[decision-ledger.md](../governance/decision-ledger.md); this section is the canonical model.

**No accepted household use case requires averaging, median-combining, weighting, or otherwise
aggregating multiple equivalent same-purpose sensors into one ordinary Room Environment Fact.** A
Room's having several capable sensors, a Merged Room spanning several constituent Rooms, a dashboard
displaying more than one source, or a historical implementation having averaged readings are none of
them evidence of such a requirement. Accordingly:

- **Composite Contributor is removed from the ordinary Room Environment path.** The state Room
  Configuration previously represented under this name (**DL-60**) had no accepted consumer, no tested
  household outcome, and no reason Primary Authority could not satisfy it; **DL-30**'s burden of proof
  was never discharged for inventing a bespoke aggregation algorithm.
- **If a genuinely narrow future need for same-purpose aggregation is ever accepted**, Home Assistant's
  native **Min/Max helper** already computes `mean`, `median`, `min`, `max`, `range`, or `sum` across
  configured entities and discharges **DL-30** directly — no new HTBW aggregation engine is invented in
  advance of that need.
- **An Authority-Derived Fact** — the ordinary product of this path — carries no contributor coverage.
  It does not claim that every possible Room sensor agrees; it states that the household selected this
  one source to represent the Room purpose. The source remains authoritative for its own native state;
  Room Configuration remains authoritative for the Room purpose; Truth remains authoritative for the
  published Fact.
- **A source-specific question is distinct from a Room-purpose question.** *"What temperature does the
  Den presence sensor report?"* may read that sensor's own current native value where authorized; it
  never redefines the Den's Temperature Fact, and a difference between the two does not trigger runtime
  arbitration — **DL-63** owns any conflict-detection use this evidence.

This applies **identically to a Physical Room and a Merged Room** (**DL-13**); see *Merged Room
environmental candidates*, below.

**A missing Primary Authority is unavailability, not a Repairs defect.** Where a household has not
configured one, the purpose is simply unconfigured (Scenario B). **A genuine Repairs candidate exists
only where the configuration itself is invalid** — for example two configuration records
simultaneously claiming exclusive Primary Authority for one Environmental Purpose (Scenario C) — a
state ordinary runtime evaluation cannot resolve on its own, since Room Configuration guarantees at
most one Primary Authority per purpose and this violates that invariant. See
[home-assistant-boundary.md](../architecture/home-assistant-boundary.md), *Repairs adoption scope
(DL-65)*.

#### A Primary Authority may be a Direct Environmental Measurement or a Provider-Derived Environmental Indicator (DL-62 clarification)

A source eligible for Primary Authority selection is one of two kinds, and Room Configuration records
which kind applies without changing the selection mechanism:

| Kind | Definition | Example |
|---|---|---|
| **Direct Environmental Measurement** | A value a device or integration reports as its own observation of an environmental property | A thermostat's temperature reading, a sensor's relative humidity reading |
| **Provider-Derived Environmental Indicator** | A value an external device, integration, or service **calculates** from one or more measurements, historical trends, or a provider-owned algorithm, and exposes as a native Home Assistant entity | A device's Dew Point entity, Mold-Free Index, Health Index, Performance Index, or Virus Index, where the provider — not HTBW — performs the calculation |

**Either kind may be selected as a Room's Primary Authority for a compatible DL-60 Environmental
Purpose.** Selecting a Provider-Derived Environmental Indicator does not make Truth's resulting
Fact an HTBW Formula-Derived Fact — **the provider's internal calculation remains the provider's
internal calculation**, never re-derived, never validated, and never treated as multiple competing
HTBW contributors. Truth reads the provider entity's current published value exactly as it would any
other selected Primary Authority (**DL-59**), producing an **Authority-Derived Fact** that preserves the
provider's identity, the indicator's provider-qualified name, its native entity reference, its unit or
scale, and any provider-documented limitation, in addition to the ordinary Truth Confidence, freshness,
validity, and provenance.

**A Provider-Derived Environmental Indicator must retain its provider-qualified name wherever
presented** — for example *"air-Q Mold-Free Index"*, never shortened to *"Mold Index"* or presented as
an HTBW-owned determination. HTBW makes no independent claim that a provider's cited algorithm, limit
source, or trend window is scientifically validated; it states only that the household's selected
entity currently reports this value. See [glossary.md](glossary.md), **Provider-Derived Environmental
Indicator**.

**An HTBW Formula-Derived Fact remains reserved for the case where HTBW itself performs the
derivation** — no acceptable direct or provider-derived Primary Authority satisfies the purpose, or the
household explicitly selects the HTBW derivation, and the derivation is named, versioned, and
DL-30-verified. Home Assistant First applies in order: a direct native entity, then a provider-derived
native entity, then a verified integration-derived entity, then an accepted household helper, and only
then an HTBW Formula-Derived Fact — HTBW does not recreate a provider's Dew Point, Mold-Free Index,
Health Index, Performance Index, or Virus Index merely to obtain an HTBW-owned value.

#### Native Area environmental slots seed a proposal, never automatic participation

A native Home Assistant Area environmental slot (`temperature_entity_id`, `humidity_entity_id`, and any
future documented slot whose semantics correspond to an accepted Environmental Purpose, each verified
individually under **DL-30**) **seeds a default proposal for that purpose — exactly as OD-14 already
established for native naming.** It is never automatic silent participation (**DL-11**): existence in
an Area does not by itself make a source a contributor. It **is** presented so the household is never
asked to reconfigure information Home Assistant already holds (**DL-31**): a resident who has already
told Home Assistant which sensor represents a Room's temperature is never asked to say so again.

- **An explicit HTBW selection or exclusion, once made, is never silently overridden** by a later
  native (re)assignment. The later native change becomes a **new proposal** presented alongside the
  existing configuration, not a silent replacement of it.
- **The resulting divergence is a Room Configuration condition** — explainable and reviewable through
  this model's own lifecycle, not automatically a Repairs issue (**DL-65**) and never a silently
  changed Fact.
- **HTBW never writes the selection back to the native Area assignment.**
- Accepting a proposal creates a governed configuration Change Record, exactly as any other
  participation change does.

#### Merged Room environmental candidates

For a Merged Room, eligible environmental sources are surfaced from **every constituent Room**, with
the source Room visible for each candidate — never hidden, never presented as though it belonged to
the Merged Room itself. **No constituent entity is copied.** Room Configuration selects, per
Environmental Purpose, **one constituent-Room source as the Merged Room's own Primary Authority** —
identically to a Physical Room (**DL-13**, **DL-62**) — plus any Secondary/Corroborating sources and
Explicit Exclusions. Truth reads the current state of that one selected Primary Authority; **no
constituent Room composite is averaged, and no same-purpose aggregation occurs merely because the
Merged Room spans several constituent Rooms.** **DL-63** governs disagreement among constituent-Room
sources. Direct questions about a constituent Room continue to use that Room's own definition,
unaffected by the Merged Room's.

#### Derived Environmental Purposes

A purpose may be **derived** from other established Facts rather than directly measured — for example
dew point, derived from a Room's configured Temperature and Humidity purposes. Room Configuration
declares that a purpose is derived and from which inputs; **Truth computes the derived Fact as a
Formula-Derived Fact (DL-62)** — combining more than one **different** Environmental Purpose's Fact
through a named, versioned deterministic formula, never a same-purpose aggregation choice. A
Formula-Derived Fact preserves its input Fact references, input validity and confidence, derivation
identity and version, formula or provider provenance, produced value, unit, Truth Confidence, validity,
and a named failure reason where not produced. **A missing or invalid mandatory input Fact makes the
derived Fact `unknown`, never invented, never a partial calculation, and never a retained last value**
— the missing input is named. **The formula class and versioning discipline are canonical; the specific
formula remains implementation mapping, verified per DL-30.** Dew point's formula class and versioning
are accepted on this basis; **mold index and condensation risk remain unresolved** — no HTBW-endorsed
formula exists for either, and HTBW invents no clinical, medical, or safety-threshold formula.

**A derived purpose is only a Formula-Derived Fact when HTBW itself performs the derivation.** Where a
device or integration already reports dew point, a mold-risk indicator, or another derived value as its
own native entity, that entity is a candidate **Provider-Derived Environmental Indicator** — see
*A Primary Authority may be a Direct Environmental Measurement or a Provider-Derived Environmental
Indicator (DL-62 clarification)*, above — and Room Configuration selects it as the Primary Authority for
that purpose in preference to inventing an HTBW derivation (**DL-30**).

#### Room Health, Room Confidence, and People Health remain uninvented

**HTBW defines no synthetic Room Health, Room Confidence, or People Health authority.** This restates
the existing prohibition in [stewardship.md](stewardship.md) (*"Room health" is not an HTBW term*,
**OD-69**) as it applies to Room Configuration: a household-facing environmental summary may exist as a
**projection**, but must decompose into individual Truth Facts (each with its own Truth Confidence Band,
provenance, validity, and coverage) and separately owned Stewardship obligation states. **A projection
may summarize; it may never create a new determination, and it may never present one aggregate state as
authoritative.**

**A provider-qualified indicator name is not an HTBW health, confidence, or performance claim** (DL-62
clarification). *"air-Q Health Index"* or *"air-Q Performance Index"* may be displayed as a
provider-attributed Environmental Indicator; **HTBW never shortens it to "Room Health" or "People
Health," never presents it as a Person's health or performance, and never lets it override a
subject-specific Environmental Requirement evaluation** (`stewardship.md`, *Person Environmental
Requirements*). The provider's product name remains a valid label for its own output; the unqualified
HTBW terms remain rejected regardless of what any provider names its indicator.

---

## Consumes

- Foundation object identifiers and the asset model
- Home Assistant Area, Device, and Entity references
- Household intent expressed through configuration

## Provides

- Resolved Room Context for a given voice assistant or surface
- Resolved target set for a given vocabulary term in a given Room
- The exposure set used to answer Room Help
- The eligible-evidence set used by Truth for composite facts
- Explicit exclusions, with reasons where supplied

---

## Explicit non-responsibilities

Room Configuration does **not**:

- Calculate composite facts (Truth)
- Determine occupancy or presence (Truth)
- Grant authority (Operational Trust)
- Store preferences or sessions (Continuity)
- Decide what should happen (Concierge)
- Own the authoritative asset record (Foundation asset model)

---

## Failure behavior

| Condition | Behavior |
|---|---|
| Voice assistant not assigned to a Room | Ask which Room, or refuse. Surface as a configuration problem. Never infer from device naming. |
| **The interaction surface is not bound to a Room** | **Room Context is `unresolved`.** Ask which Room, or refuse. **Never infer a Room from the surface, its name, or its owner.** Recorded in the trace with the reason. Resolution is **OD-73** |
| Vocabulary term not configured in this Room | State that the term is not configured here. Do not fall back to runtime search. |
| Vocabulary term maps ambiguously | Ask which target was meant, offering only exposed options. |
| A participating target no longer exists | Report a broken participation reference; do not silently drop it. |
| A composite-fact contributor is unavailable | Truth reduces confidence and records reduced coverage; configuration is unchanged. |
| A historical configuration version cannot be resolved | Report the reference as unavailable with the reason where known; never present today's configuration as though it applied then. |
| A configuration Change Record cannot be written | The failure is itself reportable; a silently unrecorded configuration change is a defect. |
| Room Help requested for an unconfigured Room | Say the Room is not configured yet; do not enumerate inventory. |

## Privacy considerations

Exposure decisions are privacy decisions. A capability that is exposed becomes discoverable by anyone
present. Sensitive capabilities must rely on Operational Trust authority, not on obscurity.
See [../architecture/privacy.md](../architecture/privacy.md).

## Explainability requirements

Every Decision Trace that resolved a target must record: the Room Context, the vocabulary term, the
resolved target set, and the configuration source. Every refusal caused by missing configuration must
say so plainly.

---

## Configuration history

**Room Configuration owns the history of its own records.** Foundation defines the shared temporal
model; Room Configuration records its changes with it. See
[temporal-record.md](temporal-record.md).

History is owned for:

- Room and Merged Room membership
- Participation
- Not-selected state
- Deliberately-excluded state
- Exposure
- Vocabulary terms and mappings
- Voice-assistant assignment
- Composite Fact contributor selection
- Capability definitions

### Current Projection

The **Current Projection** answers what is configured now, and is what runtime resolution reads.
Room Help, vocabulary resolution, and eligible-contributor lookup use the Current Projection.
**Historical records are never the runtime query path.**

### Change Records

Every governed configuration change produces a **Change Record** naming the subject, the change type,
the prior state, the new state, the Effective Time, the Recorded Time, the actor or initiating
process, the reason where supplied, and the prior and new version references.

The three participation states — **participating**, **not selected**, **deliberately excluded** —
must never be collapsed. **This holds in history exactly as it holds in the present.** A Change
Record that reduces *"moved from not selected to deliberately excluded"* to *"changed"* has destroyed
the distinction the model exists to protect.

### Explaining past decisions

A past decision references the **exact configuration version** applied at the time (**P30**). Changing
configuration today must never silently rewrite the explanation of a decision made yesterday.

---

## Representative scenarios

- [../scenarios/room-vocabulary.md](../scenarios/room-vocabulary.md)
- [../scenarios/why-did-this-happen.md](../scenarios/why-did-this-happen.md)

## Open decisions

| ID | Question |
|---|---|
| OD-01 | Home Assistant representation strategy for Room Configuration — the Area reference-and-extension rule is accepted as **DL-31**; the residual is the persistence shape of Change Records, Snapshots, and Current Projections |
| OD-02 | **Closed — DL-43, DL-44, DL-45.** Vocabulary and participation definitions are located through a governed artifact reference; encoding remains capability-specific |
| OD-12 | Whether exclusions carry a structured reason and whether reasons are resident-visible |
| OD-37 | Snapshot triggers, cadence, and scope per responsibility |
| OD-38 | Version identity, correlation, and causation identifier strategy |
| OD-70 | Whether a Merged Room warrants a native Home Assistant projection |
| OD-73 | **Interaction-Surface Room Context Resolution** — how Room Context is resolved for a phone, wearable, Companion App, browser session, or other surface not bound to a Room, without Foundation consuming Truth and without introducing a cycle |
| OD-61 | **Resolved as DL-60.** Room Environment Standard (extensible Environmental Purpose set), native Area environmental slot proposal behaviour, Primary Authority/Secondary/Composite/Excluded disambiguation (later narrowed to three states by **DL-62**), Merged Room environmental candidates, and derived purposes are accepted |
| OD-17 | **Resolved as DL-62.** Primary Authority is required and deterministic for every directly measured Environmental Purpose, identically for a Physical Room and a Merged Room; Composite Contributor is removed from the ordinary path; Formula-Derived Fact governance (input availability, provenance, versioning) is accepted, with Dew Point ready and Mold Index/Condensation Risk unresolved |
| OD-19 | **Resolved as DL-63.** Same-purpose environmental sensor disagreement, native Area proposal divergence, and Provider-Derived Environmental Indicator differences are confirmed as not Truth conflicts; a genuine Truth conflict is qualified and resolved per DL-63's fixed procedure |

## Related documents

- [room.md](room.md)
- [contextual-vocabulary.md](contextual-vocabulary.md)
- [truth.md](truth.md)
- [temporal-record.md](temporal-record.md)
- [../contracts/room-configuration-contract.md](../contracts/room-configuration-contract.md)
- [../contracts/contextual-vocabulary-contract.md](../contracts/contextual-vocabulary-contract.md)
- [../architecture/adr-stable-endpoint-identity-and-network-boundary-independence.md](../architecture/adr-stable-endpoint-identity-and-network-boundary-independence.md) — separately placeable room-interaction-capability relationships (drafted, pending #195)
