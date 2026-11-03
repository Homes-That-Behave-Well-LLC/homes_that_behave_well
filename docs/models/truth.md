# Truth Model

> **Document status: Canonical model.**
> Terminology: [glossary.md](glossary.md). Owning responsibility: **Truth**.
> Contract: [../contracts/truth-contract.md](../contracts/truth-contract.md)

---

## Purpose

**Truth is a first-class authoritative fact engine.**

Truth is not a section of Foundation. Foundation defines what a *Fact* is. **Truth decides what is
factual now.** Any document stating that Foundation owns truth is superseded.

## Question answered

*What is actually true now?*

---

## Consumes

Evidence and assertions from:

- Devices and sensors
- Assets
- Identity (identity assertions only — never biometric internals)
- Voice events
- BLE events
- Media systems
- Calendars, where authorized
- Environmental sources
- Room Configuration (which evidence is eligible for which composite fact)
- Other governed sources

---

## Owns

Authoritative facts, including:

- Presence facts
- Occupancy facts
- **Location facts**
- Environmental facts
- **Engagement facts**
- Device facts
- Contextual facts
- Room-state facts
- Active-room-mode facts
- Current-activity facts
- Composite facts (Formula-Derived Facts combining more than one Environmental Purpose's Fact, per **DL-62**); an ordinary same-purpose Environmental Fact is Authority-Derived, not composite
- Evidence freshness
- Fact confidence or certainty
- Provenance
- Fact validity and expiration

Examples:

- Tom is present in the Den.
- The Living Space is occupied.
- Maisey is in the Living Room.
- Tom's phone is in the Den.
- A conversation is active.
- An interaction is in progress through the Kitchen voice assistant.
- Music is already playing.
- The television is in use.
- The Primary Bedroom is in Nighttime mode.
- The room temperature is 72 degrees.
- The garage door is open.
- The room moved from occupied to unoccupied.

---

## Fact structure

Every fact carries at minimum:

| Element | Purpose |
|---|---|
| Subject | What the fact is about. See **Fact Subjects** below |
| Statement | What is asserted |
| Confidence | Degree of belief |
| Provenance | Contributing evidence and its sources |
| Freshness | When the underlying evidence was observed |
| Validity | When the fact expires or must be re-established |
| Coverage | For a **Formula-Derived Fact** (**DL-62**), which required inputs are currently available and valid; an **Authority-Derived Fact** carries no coverage |

A fact whose confidence, provenance, or freshness cannot be stated is not a fact.

### Fact Subjects

A Fact is **subject-typed**. The Subject is the Foundation object the Fact is about, referenced by its
stable identifier under **DL-31**.

| Subject | Notes |
|---|---|
| **Home** | The outermost governed scope |
| **Room** | The interaction context |
| **Merged Room** | A Room whose constituent set has more than one member. **A Room and a Merged Room behave identically** (**DL-13**); the finer-grained **Constituent Room** remains available where a more precise Fact is warranted |
| **Person** | See the two-stage rule below |
| **Pet** | A Foundation object with its own obligations. **A Pet is not a Person** |
| **Asset** | Device-backed or not |
| **Device** | A referenced Home Assistant Device or Entity. **Referenced, never duplicated** |

> **This enumeration extends the existing Fact. It creates no parallel assertion types.** There is no
> `PersonLocationAssertion`, `PetLocationAssertion`, `AssetLocationAssertion`, `DeviceLocationAssertion`,
> `CurrentEngagerAssertion`, or `EngagementContext` model, and none may be introduced. **Truth remains the
> single extensible model**, with one owner, one lifecycle, one provenance model, one conflict model, and
> one retention rule (**DL-47**).

**Confidence representation is DL-58 (resolved OD-74).** The four Identity confidence bands are
**DL-39** and describe *only* the strength of support for a `known` known-Person **Identity
Assertion**. **They are not Truth Fact confidence and must not be borrowed for one.**

### Truth Confidence (DL-58)

**Truth Confidence describes the strength of qualified evidentiary support for a Fact under the
applicable Truth evaluation policy.** It is never probability, measured accuracy, certainty, or
Identity Confidence, and it never authorizes anything — sufficiency for an operation remains
Operational Trust's (**DL-36**).

The canonical representation is one uniform ordinal band — **Truth Confidence Band** — applied
identically across every Fact Subject and Fact class:

| Band | Meaning |
|---|---|
| **Low** | A publishable Fact has meaningful qualified support, but substantial uncertainty remains |
| **Moderate** | A publishable Fact has credible qualified support, but material uncertainty remains |
| **High** | A publishable Fact has strong qualified support under the applicable Truth policy |
| **Very High** | A publishable Fact has the strongest qualified support available under the applicable Truth policy — **not certainty** |

**Ordering is authoritative** — Low < Moderate < High < Very High — and the bands are never added,
averaged, or treated as a distance. `None`, `unknown`, `unresolved`, `stale`, and `withdrawn` remain
**first-class Fact states, never a fifth band**, mirroring **DL-39**'s *state and band are different
dimensions*. Per-Fact-class derivation, evidence ceilings, and publication requirements may differ;
**the vocabulary does not** — no per-Subject or per-class confidence enumeration is created.

**Structurally separate from DL-39, permanently.** A **Truth Confidence Band** and a **DL-39 Identity
Confidence Band** share household-facing labels and nothing else: they are separately owned (Truth;
Identity), separately typed (`truth_confidence_band`; `identity_confidence_band`), never converted,
never averaged, and never compared as though they measured the same thing. **A Pet, Asset, or Device
Fact is structurally unable to carry an Identity Confidence Band** — Identity's candidate set contains
known Persons only. A Person-subject Truth Fact still carries a **Truth Confidence Band**, produced by
Truth from its own evaluation, never copied from the Identity Assertion that fed it.

**Comparability is ordinal and semantic only, never arithmetic.** High is above Moderate in every Fact
class, and Very High is the strongest supported band in every Fact class — but confidence values are
never added, averaged, multiplied, or subtracted, two High-confidence Facts are not equally accurate by
statistical claim, and a higher band never automatically outranks another Fact for an operational
consequence, which remains independently governed.

**Confidence is independent of freshness, provenance, and coverage** — four separate mandatory Fact
dimensions, never collapsed into one field. **OD-18** owns freshness and validity effects; **DL-62**
(resolving **OD-17**) owns Composite Fact derivation — Primary Authority is the ordinary path, carrying
no contributor coverage, and a Formula-Derived Fact carries input-availability semantics instead;
**OD-19** owns conflict-resolution effects. None of the three redefines this representation, and none
of them — nor **OD-72** — may borrow the Identity Fusion Function or DL-39 bands to answer a Truth-side
question.

**Floor is not a first-class Truth subject (resolved — DL-125, OD-10).** Foundation's accepted
object-type enumeration does not include Floor, and this decision does not add it. A Floor-scoped
question (*"what's the temperature upstairs"*) is answered as a Concierge-assembled projection over
each constituent Room's own already-existing Primary-Authority Fact — reusing the identical
"Concierge-assembled projection, not a decision HTBW made" discipline **DL-74** already established —
never a persisted Floor Fact, and never a same-purpose aggregation across Rooms (the identical
discipline **DL-60**/**DL-62** already apply within a single Room extends unchanged to Floor).

**An optional normalised numeric may accompany the band as a non-authoritative deterministic ordering
value only.** It is never resident-facing probability, likelihood, calibration, or accuracy; it never
merges Fact classes or merges Truth and Identity; it is never sufficient evidence and never authorizes
anything. No numeric is mandated by this decision, and none is introduced into the canonical model,
since no accepted consumer currently requires one.

**Every Historical Fact retains its Truth Confidence Band and the Truth evaluation-policy version that
produced it.** A later policy or band-map change never rewrites a prior Fact; a Historical Fact carrying
`High` remains interpretable as the accepted band under the version referenced at the time.

---

## Fact Validity and Current-State Evaluation (DL-59)

Resolves **OD-18**. Full acceptance record is **DL-59** in
[decision-ledger.md](../governance/decision-ledger.md); this section is the canonical model.

### Two Fact source shapes

Every Fact traces to one of two source shapes, **classified by documented integration semantics, never
by domain or device class alone**:

| Shape | Definition | Examples |
|---|---|---|
| **Current-State Source** | An entity whose state is intended by its integration to represent the current state Home Assistant exposes | Room presence/occupancy sensor, door state, valve state, an environmental sensor value, device availability, a current BLE nearest-proxy or room-assignment state |
| **Point-in-Time Observation Source** | An entity or attribute whose value names a prior event or observation | Last motion detected, last doorbell ring, last camera detection, last-seen timestamp, a schedule-derived value |

A **current-state source may still require a validity policy** where it becomes unavailable, becomes
unknown, stops updating abnormally, is documented as retained-rather-than-current, or whose update
mechanism cannot support a current claim. **A point-in-time observation never becomes a current-state
claim merely because its timestamp exists.**

| Statement | Kind |
|---|---|
| *"The Room is occupied."* | Current state |
| *"Motion was last detected at 2:14 PM."* | Historical observation |
| *"The tag was last observed in the Den at 2:14 PM."* | Last known |
| *"I cannot determine whether the Room is occupied now."* | Unknown current state |

### The dashboard principle

**For a current-state determination, Truth evaluates the most current authoritative Home Assistant
state available at evaluation time** — as though the household were looking at the current Home
Assistant dashboard — **and never prefers an older cached HTBW interpretation over healthier newer
native state.** No HTBW-imposed generic delay is applied to a healthy current-state source.

This does not mean every entity state is guaranteed physically current, and it does not mean every
device can be forcibly polled. It means: Home Assistant remains authoritative for the native state it
exposes; Truth evaluates that current exposed state, together with availability, documented integration
semantics, and applicable validity policy; and **HTBW does not create a second copy of native state
merely to claim freshness.**

A current-state Fact remains current **while its source is available and its documented semantics
support a current claim**, and ceases immediately — **never through elapsed HTBW time** — when the
source becomes unavailable, becomes unknown, or its documented semantics no longer support the claim.

### On-demand refresh is bounded, not universal

Home Assistant exposes `homeassistant.update_entity` — *"forces one or more entities to refresh their
data right away."* Per Home Assistant's own developer documentation, an entity either **polls** (Home
Assistant asks it for a value on an interval) or **pushes** (the integration calls
`schedule_update_ha_state()` when its own event occurs); `should_poll` determines which. A refresh
request therefore **asks the integration to refresh — it never manufactures a physical observation, and
request acceptance never proves a new device reading occurred.**

Before a current Fact is declared expired or unknown, Truth may request the freshest available
authoritative state **only where the selected integration's documented update mechanism has been
verified under DL-30's burden of proof** — the requirement is per-integration, never a universal
capability. Push-only, event-driven, and advertisement-based sources (BLE proximity, PIR motion) may
not support a meaningful forced refresh at all, and Truth must not block indefinitely waiting for one.

### Operational validity and expiration

A **current-state** Fact's validity is governed by availability and documented semantics, as above — no
separate elapsing window is imposed while the source remains healthy.

A **point-in-time observation**'s Fact carries an **operational validity window**. When it elapses, the
Fact **operationally expires** and is withdrawn from *what is true now*; the observation, its original
Truth Confidence Band, and its lifecycle remain available as a Historical Fact under **DL-25** and
**DL-47** — expiry is never deletion.

A Fact ceases being current when any of the following occurs — this is the **generic invalidation
interface** OD-18 defines; *which* triggers apply to a given Fact or derivation remains with whichever
responsibility owns that derivation (for example **DL-38** for the Identity Assertion feeding a
Room-Presence-purpose fusion, or Truth for the resulting Fact):

1. An operational validity window elapses.
2. The supporting source becomes unavailable or unknown.
3. A supporting condition changes (for example a Room's occupancy transitions to `unoccupied`).
4. The primary evidence moves to another context.
5. Contradictory current evidence emerges — resolution is **OD-19**'s own.
6. The source's documented integration semantics no longer support the current claim.

**`expired`, `unavailable`, and `never observed` remain three distinct, always-named outcomes** — never
collapsed into one generic `unknown`.

### Confidence and validity are separate dimensions

**Truth Confidence (DL-58) and Fact Validity are never merged.** The confidence originally established
for a Fact is **never decayed by elapsed time alone** — validity states whether the Fact remains
current; confidence states how strongly it was supported when established. A Fact may remain
historically strongly supported while no longer being current: Truth withdraws it and, where nothing
current can be asserted, publishes `unknown`. Historical confidence is never rewritten by a later
validity determination.

### Expiration is a Truth lifecycle transition

**Operational expiration is one of DL-25's eight Truth lifecycle transitions** — *operationally
expired* or *became unknown* — materialized through the existing Domain Event / Change Record mechanism
([temporal-record.md](temporal-record.md)). **No second event model is created.** Consumers reevaluate
on the resulting event or, where it has not yet materialized, at query time; **there is exactly one
authoritative validity result**, never independently computed per consumer.

### Presence, occupancy, and honest absence

**Expired or unavailable presence never decays into absence or solitude** (**DL-34**). Room Occupancy
(a Room-subject current-state Fact) and Contextual Person-Presence (a Person-subject Fact Truth derives
by consuming an Identity Assertion as one input, per the existing accepted fusion and consumption rules
below) remain the Facts already defined by this document — this section redefines neither, and does not
decide the multi-evidence combination behind a Contextual Person-Presence Fact, which is already
accepted under **DL-38** and *Identity assertions become presence facts*, below.

### Household configuration, not architecture

Freshness and validity windows are **household configuration values, not architecture**, mirroring
**DL-47**'s own established pattern: per-Fact-class and per-Subject differentiation is available where
a household chooses to declare it; **no universal duration is prescribed here**. Configuration must
never convert last-known into current, never treat unavailable as current, never bypass consent, and
never be silently learned — a learned duration proposal follows **P26** and **DL-21** exactly as any
other learned suggestion, and explicit configuration always outranks an unaccepted one.

---

## Location facts

A **Location Fact** is a Fact whose Statement places its Subject somewhere in the Home **now**.

> **Declared location and current location are different things with different owners, and collapsing
> them is a defect.**

| | Declared Location | Current Location |
|---|---|---|
| What it is | A configured, durable statement of where something belongs or is kept | An evidence-derived, confidence-bearing statement of where something **is now** |
| Owner | **Foundation** — the `located-in` relationship | **Truth** — a Location Fact |
| Authority | [../contracts/foundation-contract.md](../contracts/foundation-contract.md) | This model |
| Changes when | The household reconfigures it | Evidence changes |
| Carries confidence | No. It is a definition | **Yes**, with provenance, freshness, validity |
| When unrecorded | Foundation reports `unknown` — *"an asset with no known location"* | Truth publishes `unknown`. **Never default to a Room** |

**Foundation does not confirm current state** ([../contracts/foundation-contract.md](../contracts/foundation-contract.md)),
and **Truth does not own the object definition**. A declared location is *evidence* toward a Location
Fact where a household governs it that way; it is never itself the Fact.

### The Person asymmetry

| Subject | Requires an Identity Assertion first? | Why |
|---|---|---|
| **Person** | **Yes, always** | *Which human* is a fusion question over a bounded candidate set of known Persons. **DL-06**, **P9**. The result is the **Contextual Person-Presence Fact** |
| **Pet, Asset, Device** | **No — and must not** | There is no *which human* question. Identity's candidate set contains **known Persons only**, and **DL-39** bands describe identity support only. **Routing a pet tag or a device tracker through Identity is a category error** |

> *"Where is Maisey?"* and *"Where is my phone?"* are **Truth-only** questions.
> *"Where is Tom?"* is a **two-stage** question.

### What each source may establish about a non-Person Subject

**Reliability is not a property of an evidence type**, and what a source can *establish* is bounded by
what it actually observes. Under **P21** and **DL-30**, a Room-granularity claim requires evidence whose
Room granularity is **actually grounded**; where it is not, no Room-level Location Fact is asserted.

| Evidence source | May support | Never establishes on its own |
|---|---|---|
| Native `device_tracker` | Presence of the **device** at **zone** granularity — `Home`, `Not home`, a zone name | A Room or Area; **that the bound Person is with the device** |
| Connection-type tracker | The device is associated with a network, with its zone treated as a documented **assumption** | Physical location; a Room |
| Room-scoped proximity or beacon evidence | Device or tag proximity to a Room, **only where Room-level detection is genuinely grounded** | Which Person is holding it; which Person is in the Room |
| Pet-worn tag or collar | That a **tagged object** is where the tag is observed | That the Pet is wearing it; **any human identity**; Room Presence for a Person |
| Tag scan | That an object was scanned, by which device, at what time | Who scanned it; where the object is between scans |
| Declared `located-in` | Where the household **keeps** the thing | Where it is now |
| Room occupancy or presence sensor | That the Room is occupied; corroboration of context | **Which** Person, Pet, or Asset |

**The device-left-behind case is the governing example.** A phone observed in the Den supports *the phone
is in the Den*. It supports *Tom is in the Den* only through **Identity**, at that family's ceiling, and
it **never** establishes that Tom is holding it. **A tag removed from a pet, and a pet that has moved a
tag, are contradiction cases** handled under *Conflicting evidence* below and governed by **OD-19**.

### Disclosure warning

> **A device-location Fact is frequently a person-location disclosure, and a pet-location Fact is
> frequently a human-movement disclosure.** Truth publishes the Fact; **Operational Trust decides whether
> it may be conveyed, to whom, on which surface** (**DL-34**, **P32**). See
> [operational-trust.md](operational-trust.md) and [../architecture/privacy.md](../architecture/privacy.md).

---

## Engagement facts

An **Engagement Fact** is a Fact stating that **an interaction is occurring** — nothing more.

It may carry:

- The **interaction channel** — voice, kiosk, Companion App, browser session, physical control
- The **interaction surface** — the participating device or endpoint, referenced by its native identifier
- The **Room Context**, where one has been resolved, and **`unresolved` where it has not**
- **Freshness** — when the interaction was observed
- **Provenance** — which native event or governed source reported it
- **Whether a human participant is supported**, where an Identity Assertion has independently reported it

> **An Engagement Fact must never identify the engaging Person.**

| An Engagement Fact is | An Engagement Fact is not |
|---|---|
| A Truth Fact about the world | An Identity Assertion |
| A statement that an interaction is in progress | A statement of **who** is interacting |
| Channel, surface, Room, freshness, provenance | A candidate Person, a confidence band, or a fusion result |
| Consumable as **corroborating context** by Identity, at that family's ceiling | A source that may **nominate a candidate** |

**Two rejections are explicit and constitutional:**

- **Engagement Fact is not Identity.** Who is engaging is answered by a purpose-specific **Identity
  Assertion** — Speaker Attribution, Interaction Initiator, Authenticated Session Identity, or Endpoint
  Context — produced by **Identity alone** (**DL-32**, **DL-38**).
- **Engagement Fact is not "Current Engager".** *Current Engager* is **not an HTBW architectural term** and
  must not be introduced. A single fused engager result would recreate the general-purpose identity score
  that **DL-32** and **DL-38** prohibit. See [glossary.md](glossary.md).

**Endpoint Context remains Identity's**, and it identifies a **thing, not a person**
([person-and-identity.md](person-and-identity.md)). An Engagement Fact and an Endpoint Context assertion
may describe the same interaction from two sides; **they are not interchangeable and neither replaces the
other.**

Where the interaction arrived through a surface that is **not bound to a Room**, the Engagement Fact
records the Room Context as **`unresolved`**. **How such a Room Context may be resolved at all is open
decision OD-73**, and nothing in this section resolves it.

---

## Composite facts (DL-62)

Resolves **OD-17**. Full acceptance record is **DL-62** in
[decision-ledger.md](../governance/decision-ledger.md); this section is the canonical model.

For every directly measured Environmental Purpose, Room Configuration selects one **Primary
Authority**, and Truth reads that single source's current state (**DL-59**) as an **Authority-Derived
Fact** — never an average, median, or weighted combination of equivalent sensors, and identically for a
Physical Room and a Merged Room (**DL-13**).

```
Room Configuration:  Living Space Temperature Primary Authority = Sensor C
Truth:               Living Space temperature = 72.4 degrees
                     truth_confidence_band: High
                     provenance: Sensor C
```

> **No accepted household use case requires combining multiple equivalent measurements of the same
> Environmental Purpose into one authoritative Room Fact.** Several capable sensors existing, a Merged
> Room spanning several constituent Rooms, or a historical implementation having averaged readings are
> none of them evidence of such a requirement.

### Direct measurements and provider-derived indicators are both Authority-Derived (DL-62 clarification)

A selected Primary Authority's own native entity may be a **Direct Environmental Measurement** (the
device's own observation) or a **Provider-Derived Environmental Indicator** (a value the provider
calculates internally from measurements, trends, or a provider-owned algorithm — for example a Dew
Point, Mold-Free Index, Health Index, Performance Index, or Virus Index entity). **Both produce an
Authority-Derived Fact when selected; neither is a Composite Fact or a Formula-Derived Fact.** Truth
reads the provider entity's current published value exactly as any other Primary Authority; **the
provider's internal calculation is never re-derived, never independently validated, and its internal
inputs are never treated as separate Truth contributors or as evidence of a runtime conflict.**

An Authority-Derived Fact sourced from a Provider-Derived Environmental Indicator additionally carries:

- The indicator's **provider-qualified name** (for example *"air-Q Mold-Free Index"*), never shortened
  to an unqualified HTBW term
- The **provider's identity**
- Its **direct-versus-provider-derived classification**
- Any **provider-documented limitation** (for example that a value is trend-based rather than a
  point-in-time reading, or that its meaning is insufficiently documented)

**HTBW makes no independent scientific claim about a provider's algorithm, cited limit sources, or
trend window** — Truth is authoritative only for *the selected entity currently reports this value*,
never for validating the provider's interpretation. See [glossary.md](glossary.md), **Provider-Derived
Environmental Indicator**.

Truth may still combine **different** Environmental Purposes' current Facts into a single
**Formula-Derived Fact** — for example Dew Point, derived from a Room's Temperature and Humidity
Facts through a named, versioned formula. **This path exists only where HTBW itself performs the
derivation** — never merely because a provider's own indicator internally used multiple measurements. A
Formula-Derived Fact preserves its input Fact references,
input validity, input confidence, derivation identity and version, formula or provider provenance,
produced value, unit, Truth Confidence, validity, and a named failure reason where not produced. **A
missing or invalid mandatory input publishes the Formula-Derived Fact as `unknown`** — never a partial
calculation, and never the last derived value retained as current; the missing input is named. The
formula class and versioning discipline are canonical; the specific formula remains implementation
mapping, verified per **DL-30**. Dew Point's formula class and versioning are accepted on this basis;
**Mold Index and Condensation Risk remain unresolved** — no HTBW-endorsed formula exists for either.
**Home Assistant First applies before an HTBW derivation is used**: a direct native entity, then a
provider-derived native entity, then a verified integration-derived entity, then an accepted household
helper, and only then an HTBW Formula-Derived Fact.

> "Composite Fact" is unrelated to the superseded term "Composite Room" (now **Merged Room**), which
> concerns the combination of Physical Rooms. A Formula-Derived Fact may be scoped to a Room or to a
> Merged Room. See [glossary.md](glossary.md).

Boundaries:

- **Room Configuration does not calculate Truth.**
- **Truth does not own the sensor inventory.**
- **Concierge does not choose sensors at runtime.**

Residents ordinarily receive the authoritative Fact rather than a list of raw sensor readings. Raw
evidence remains available for diagnostics, provenance, calibration, and explainability where
authorized.

---

## Identity assertions become presence facts

```
Identity asserts:        candidate Tom, identity_confidence_band: High, evidence voice + BLE + phone
Room Configuration says: the Den's occupancy evidence sources are X and Y
Truth establishes:       Tom is present in the Den (truth_confidence_band, provenance, validity)
```

The identity assertion is evidence. The presence fact is Truth. They are different objects with
different owners, and **the Identity Confidence Band on the assertion is never copied onto, converted
into, or averaged with the Truth Confidence Band Truth independently derives for the presence Fact**
(**DL-58**).

**Truth receives the assertion only.** Biometric internals never cross this boundary, so Truth has
nothing to store or expose. See [person-and-identity.md](person-and-identity.md).

**Truth never fuses identity evidence.** It does not re-weight, re-combine, or recompute an assertion,
and it does not reach past the assertion to the evidence behind it in order to reach a different
conclusion about who someone is. Truth consumes the assertion as **one input** among the Room's
configured occupancy evidence, and produces a Fact about the world (**DL-06**, **DL-38**).

### The direction is one-way, and it is not a cycle

This boundary is frequently misread as circular. It is not, and the misreading is worth stating plainly
because it inverts two accepted decisions.

| Statement | Correct? |
|---|---|
| **Identity produces Identity Assertions** | ✅ Identity alone. *"Identity performs fusion. No other responsibility does."* |
| **Truth consumes Identity Assertions** | ✅ As **one input**, among the Room's configured occupancy evidence |
| **Truth produces Contextual Person-Presence Facts** | ✅ *Tom is present in the Den* is a **Truth** Fact |
| **Truth determines identity** | ❌ **Never.** *Which human* is Identity's question |
| **Truth re-runs identity fusion** | ❌ **Never.** Truth does not re-weight, re-combine, or recompute an assertion |
| **Identity consumes a Truth person-presence Fact to decide who is engaging** | ❌ **Never.** This inverts **DL-06** and **P9** |

> **Truth establishes *occupancy* — a Room-subject Fact — before fusion. Truth establishes *person
> presence* — a Person-subject Fact — only *after* fusion, from the assertion.** These are two different
> Fact Subjects at two different points, and reading them as one object is what creates the illusion of a
> loop.

Only one feedback path exists, and it is bounded on four sides:

```text
sensor / voice / BLE / tracker evidence
        ↓
Identity  →  purpose-specific Identity Assertion
        ↓
Truth     →  Contextual Person-Presence Fact          (Person subject)

Truth     →  Room occupancy Fact                      (Room subject)
        ↓
        └── may re-enter a LATER Identity fusion as ONE evidence family only
```

| Guarantee | Why the path cannot close into a cycle |
|---|---|
| **Subject separation** | Only the **Room-subject occupancy** Fact re-enters fusion. A **Person-subject** presence Fact never does, so no fusion consumes its own output |
| **Ceiling (F1)** | Room occupancy may support *"that the Room is occupied; corroboration of context"* and **never** *"which Person; who spoke; who initiated"* |
| **Candidate-set exclusion** | Occupancy is **not** an admissible source of a candidate Person. *"Occupancy is not identity"* |
| **Version referencing (P30, DL-27)** | Every stage references the **exact prior version** it used, so an evaluation cannot consume a result it has not yet produced |

**Continuous occupancy is not continuous identity.** A Room may remain occupied while its occupants
change entirely; a prior assertion, band, or confirmation is never revived because presence persisted
(**DL-39**). See [person-and-identity.md](person-and-identity.md) and
[../architecture/dependency-view.md](../architecture/dependency-view.md).

---

## Fact lifecycle and Historical Facts

**Truth is the system of record for both present and historical Facts** (**P28**).

Operational expiration removes a Fact from *what is true now*. It does **not** automatically delete
*what was true then*. This completes the qualifier already present in this model's failure table:
*"do not retain the last value **as current**"* — which has always presupposed that historical
retention is a different question from operational currency.

### The eight lifecycle transitions

Each must be **separately reconstructable**:

| Transition | Meaning |
|---|---|
| Established | The Fact came into being |
| Confirmed | Further evidence supported it without changing the statement |
| Confidence changed | The degree of belief moved |
| Superseded | A newer Fact replaced it |
| Withdrawn | Evidence was contradicted or invalidated |
| Operationally expired | Validity elapsed; the Fact left *what is true now* |
| Became unknown | Nothing could be asserted |
| Became unresolved | Candidates conflicted with no governed resolution |

A transition is recorded as a **Change Record** under the shared temporal model. See
[temporal-record.md](temporal-record.md).

### What a Historical Fact retains

Where policy permits: Subject, Statement, confidence **at the time**, Provenance, evidence references
or evidence classes, Coverage, Freshness, and lifecycle transitions.

A Historical Fact is **not** a retained raw evidence payload. Evidence is referenced, not copied
(**P30**).

### What a Historical Fact must never be

- Never presented as current
- Never actionable
- Never silently promoted back to current

Re-establishing a Fact requires new evidence and a new lifecycle transition. A Historical Fact does
not revive.

### Ownership

**Truth owns Fact history. No consumer may maintain a competing or re-derived Fact history.** A
consumer that keeps its own record of what Truth used to say has created a second fact engine, which
**P8** and **DL-04** prohibit.

Retention for Historical Facts is settled by **DL-47**: they are governed history following External
History Retention, carrying their own Retention Classification. **Per-Fact-class differentiation is
an Operational Trust policy matter, not architecture.**

### Governing parent, cleanup, and retention by Subject

**DL-43** required a declared lifecycle before an artifact could exist; **DL-47** extended that
obligation to every governed record class; **DL-45** requires every record to declare a **governing
parent** and a **Parent Removal Behavior**, whose ordinary default is **cleanup when the parent
disappears**. Location, Presence, and Engagement Facts are governed record classes and are therefore
bound by all three. **No new responsibility, artifact class, or store is created by this table.**

| Fact Subject | Governing parent | Retention | Parent Removal Behavior |
|---|---|---|---|
| **Person** | The **Person** (native Person by reference, **DL-31**) | Truth-owned governed history following External History Retention, own Retention Classification (**DL-47**) | Person deletion enumerates and removes dependent Facts and their history, subject to Preservation Holds, retention floors, and the versions required to keep a held Decision Trace explainable |
| **Pet** | The **Pet** (Foundation object) | As above | **Pet removal cleans up Pet-subject Facts and their history** on the same terms as a Person. A tag or collar is **evidence, not the parent** \u2014 removing the tag withdraws current Facts and never deletes history |
| **Asset** | The **Asset** \u2014 already the governing parent of its documentation (**DL-45**) | As above | Asset deletion removes Asset-subject Facts on the same terms already accepted for Asset documents |
| **Device** | The **Person, Asset, or Room** the Device is governed through | As above | **A referenced native Device is never deleted by HTBW** (**DL-31**). Its removal outside HTBW produces a **broken reference**, which is **reported**, withdraws current Facts, and **never rewrites history** |
| **Room, Merged Room, Home** | The Room, Merged Room, or Home | As above | A deleted constituent Area produces a broken constituent reference, **reported, never a silent shrink** |

Four rules bind every row:

- **Retention and parent cleanup are distinct mechanisms** (**DL-45**). Neither substitutes for the other,
  and a Fact class may be subject to both.
- **Cleanup never silently overrides** a Preservation Hold, a retention floor, an Evidence Package
  lifecycle, or historical explainability (**P27**).
- **Cleanup is not claimed while a required dependency is unavailable.** A governed pending-cleanup state
  is retained and reconciled when the dependency returns.
- **Native objects follow their own lifecycle** and are never removed because an HTBW record was cleaned.

**Withdrawing consent for an evidence source is not deletion of history.** Consent withdrawal renders the
source **ineligible** \u2014 excluded before weighting \u2014 and current Facts depending on it are withdrawn or
reduced. **An earlier Fact remains historically true and remains explainable**; later explanations report
that the evidence source no longer exists, and never restate the past as though it did not happen.

**Nothing here authorises a second store.** Location and Engagement Facts reference native state as
evidence; **HTBW builds no second Recorder and no second device tracker** (**DL-42**, **DL-46**).

---

## Truth must not

- Trigger actions
- Control devices
- Make resident-facing behavioral decisions
- Own preferences
- Own authority or permission
- Hide uncertainty
- Automatically convert weak evidence into a definitive fact

---

## Genuine Truth Conflict (DL-63)

Resolves **OD-19**. Full acceptance record is **DL-63** in
[decision-ledger.md](../governance/decision-ledger.md); this section is the canonical model.

### Definition

A **genuine Truth conflict** exists only when two or more currently eligible, semantically comparable
claims address the **same Subject, predicate/Fact purpose, context, and evaluation time**, remain
independently eligible after the qualification order below runs, and are **mutually incompatible** —
with **no accepted authority-selection, validity, availability, configuration, Identity, or Stewardship
rule already explaining the difference**.

**Different Subjects, different predicates, different time periods, current versus Historical, a
Truth Fact versus a Stewardship evaluation, and a native proposal versus an explicit selection are
never, by themselves, a Truth conflict** — they are different statements, not competing answers to one
question.

### Qualification order

Before any contradiction determination, Truth qualifies evidence in this fixed order:

1. Same Subject
2. Same predicate or Fact purpose
3. Same context
4. Same evaluation time or overlapping validity
5. Current availability (**DL-41**)
6. **DL-59** validity
7. Configuration eligibility (Room Configuration's designated Primary Authority / Secondary /
   Excluded participation)
8. Consent and policy eligibility, where applicable
9. Authority selection
10. Semantic comparability
11. Contradiction determination
12. Conflict outcome application

**Evidence excluded before step 11 is not conflicting evidence.** An expired value is invalid, not
contradictory. An unavailable source is unavailable, not contradictory. An unselected candidate is not
an authority and does not conflict with the selected Primary Authority. A Provider-Derived
Environmental Indicator has different semantics from a direct measurement or a Stewardship evaluation
and is never compared as competing evidence for the same purpose. Missing evidence is absence, not
contradiction. Every exclusion and qualification decision is explainable in the Decision Trace.

### What is no longer, or was never, a Truth conflict

- **Same-purpose environmental sensor disagreement is not an ordinary Truth conflict** (**DL-62**). Two
  thermostats ten degrees apart, or two disagreeing humidity sensors, are the pre-**DL-60** scenarios
  this decision originally used to illustrate the problem — they no longer apply. An unselected
  sensor's differing value is a source-specific diagnostic value, never a competing Room authority, and
  never reduces the selected Primary Authority's confidence.
- **A native Area environmental slot's proposal diverging from an explicit Room Configuration selection
  is a configuration condition, not a runtime conflict** (**DL-60**). HTBW never writes back, never
  silently switches, and the divergence remains visible and explainable — escalating to Repairs only
  where **DL-65**'s own administrator-correctable-defect criteria are independently met (for example
  two configuration records both claiming exclusive Primary Authority for one purpose).
- **A Provider-Derived Environmental Indicator does not conflict with a direct measurement or a
  Stewardship evaluation merely because the values differ in shape, scale, or outcome** — the
  statements have different predicates and owners (post-**DL-62** clarification). *"air-Q Health Index:
  99.9%"* and *"Abigail's humidity requirement: unmet"* may both be true.
- **Conflicting Person, Pet, or Asset Environmental Requirements against one current Room Fact remain
  Stewardship's own** (**DL-61**). Truth publishes one current Fact; Stewardship maintains independent
  per-subject evaluations; no average requirement, majority rule, or subject ranking is created.
- **Identity contradiction among evidence families remains DL-38's own**, resolved inside the Identity
  Fusion Function before Truth ever receives the resulting purpose-specific Assertion. This decision
  does not reuse, duplicate, or reach past that Assertion to its underlying evidence.
- **Assertion lifetime and cross-purpose assertion eligibility remain OD-15's own** and are not decided
  here. Whether a prior purpose-specific Assertion (for example Speaker Attribution) remains eligible
  evidence for a later, different-purpose determination (for example Room Presence) is OD-15's
  question; its own recorded boundary — the contribution ends when the supporting Room's occupancy
  transitions to `unoccupied`, or the Person's configured primary evidence source no longer supports
  that Room — is consumed without redefinition where OD-15 accepts it.

### Published outcome

Where a genuine Truth conflict remains after qualification, Truth publishes exactly one of:

| Outcome | When |
|---|---|
| A single Fact at a reduced Truth Confidence Band | A governed resolution rule or an accepted authority applies; recorded with the applicable reason and Conflict Policy version. Contradiction may **hold or reduce** confidence; it **never raises** confidence, and never produces Very High |
| An **unresolved** Fact | No resolution rule applies; every competing claim, its source, and its value are reported |
| `unknown` | Nothing can be honestly asserted. A successful, honest outcome — never conflated with `unavailable` (an evaluation that could not occur, **DL-41**) or with absence of evidence |
| Withdraw a fact | Prior evidence is stale or contradicted |

**Truth never averages contradictory evidence, never applies majority voting, and never adopts a
universal provenance-class precedence** — a native entity, an HTBW Fact, an external provider, and a
derived Fact are never ranked by class alone; only an accepted authority-selection rule (Room
Configuration's Primary Authority, Person Setup, or an Identity Evidence Association) establishes
precedence. The original observations remain unchanged; every competing claim remains visible in
provenance.

**A range-valued Fact is not adopted for any current Fact class.** No accepted Fact class canonically
requires one, and one is not invented merely to escape an unresolved contradiction — this is deferred,
not decided.

### Conflict Policy

Disagreement thresholds, where meaningful, are **Fact-class-scoped Conflict Policy configuration** —
named, versioned, unit-stated, and explainable — never a single universal numeric. Some Fact classes
(categorical location, occupancy, online/offline) have none. Every Truth conflict outcome references
the Conflict Policy version used; a later policy change never rewrites a Historical Fact. A Conflict
Policy may contain Fact-class qualification and comparability rules, disagreement thresholds,
publication minimums, confidence-reduction rules, range eligibility, persistence conditions, and a
reason-code set. It never contains Identity Fusion rules, person-ranking rules, universal provenance
precedence, automatic majority voting, arithmetic averaging, authorization, Stewardship significance,
or Communication delivery rules.

### Persistent conflict and Repairs

A conflict becomes **persistent** when the applicable Conflict Policy's configured recurrence or
continuity condition is satisfied. A conflict's appearance, continuation, and resolution are recorded
through the existing Domain Event / Change Record mechanism ([temporal-record.md](temporal-record.md))
— **no second conflict-history store is created**. When a conflict resolves, a new event and, where
current evidence now supports one, a new Fact are published; the prior `unknown` or reduced-confidence
outcome is never rewritten, and Stewardship reevaluates dependent obligations.

Persistent conflict may indicate a misconfigured authority, a sensor-placement concern, a failing
source, or another likely administrator-correctable defect. **A persistent Truth conflict does not, by
itself, become a Repairs issue** (**DL-65**, resolving OD-60): Truth's role ends at recording the
conflict's appearance, continuation, and resolution as Domain Events. A Repairs issue is raised only
where the responsibility owning the relevant configuration — typically Room Configuration — separately
and independently identifies that the persistence pattern reveals a genuine configuration defect (for
example, duplicate Primary Authority), never merely because two legitimately configured sources
disagree. Ordinary transient disagreement, a briefly unavailable source, or a native-proposal/HTBW
divergence are not automatically Repairs-eligible. See
[home-assistant-boundary.md](../architecture/home-assistant-boundary.md), *Repairs adoption scope
(DL-65)*.

### Location conflict cases

Location Facts generate a recurring family of conflicts. **All of them are preserved and explainable,
never hidden.**

| Case | Required treatment |
|---|---|
| **Device left behind** | The device-location Fact stands; it supports **no** Person-location claim. Identity applies the family ceiling. Do not promote *the phone is in the Den* into *Tom is in the Den* |
| **A Person's associated devices are in different Rooms** | Contradiction is **claim-specific** and is retained. Publish reduced confidence or `unresolved`; never average the Rooms |
| **A pet has moved, removed, or shed its tag** | The tag-location Fact stands for the **tag**; the Pet-location Fact is reduced, `unresolved`, or `unknown`. **A tag is not the Pet** |
| **A tag is worn by a different animal or carried by a person** | Same treatment. The Subject of the Fact is what the evidence actually observes |
| **Declared and current location disagree** | **Current location prevails as the Fact.** The declared `located-in` relationship is unchanged and is never rewritten by an observation |
| **Zone-level evidence conflicts with Room-level evidence** | The **zone** claim and the **Room** claim are different granularities, not two answers to one question. Publish at the granularity the evidence actually grounds |
| **Multiple people in one Room** | Occupancy remains true; **no single Person follows from it**. Person-presence requires its own assertion per Person |
| **All contributing sources become unavailable** | Publish `unknown`. **Never retain the last known location as current** |

---

## Provides

- Facts with confidence, provenance, freshness, validity, and coverage
- Fact-change notifications, including transitions such as occupied → unoccupied
- Unresolved and unknown states as first-class outputs
- Diagnostic access to contributing raw evidence, where authorized

---

## Explicit non-responsibilities

Truth does **not** own: identity (Identity), obligations (Stewardship), preferences and sessions
(Continuity), policy and authority (Operational Trust), decisions and actions (Concierge), the sensor
inventory (Foundation asset model), or which sensors are eligible (Room Configuration).

---

## Failure behavior

| Condition | Behavior |
|---|---|
| A contributor is unavailable | Recompute from remaining contributors, reduce confidence, record reduced coverage |
| All contributors unavailable | Publish `unknown`; do not retain the last value as current |
| Evidence stale | Mark stale, reduce confidence, or withdraw |
| Sources disagree | Preserve the disagreement; publish unresolved or reduced-confidence fact |
| A room transition is missed | Do not retroactively invent a transition; treat the newly observed Room as current and record the gap |

## Privacy considerations

Presence and occupancy facts, and their history, are highly sensitive. Visibility is governed by
Operational Trust policy. See [../architecture/privacy.md](../architecture/privacy.md).

Historical Facts are bounded from both directions: **P27** establishes a retention floor, and
[../architecture/privacy.md](../architecture/privacy.md) establishes the ceiling. Where they
conflict, privacy governs, and the resulting limitation is itself recorded rather than left silent.
Historical Facts may be redacted; a redacted Historical Fact **remains a record** that the Fact
existed and made the transitions it made.

## Explainability requirements

Every fact used in a decision appears in the Decision Trace with its confidence, provenance, and
freshness. A fact that was *unknown* and therefore blocked an action must appear as well.

A Decision Trace references the **exact version** of each Fact it used (**P30**), so an explanation
remains accurate after the Fact has since changed, expired, or been withdrawn.

---

## Representative scenarios

- [../scenarios/where-is-tom.md](../scenarios/where-is-tom.md) (person location — the two-stage path)
- [../scenarios/where-is-maisey.md](../scenarios/where-is-maisey.md) (pet location — Truth-only)
- [../scenarios/where-is-my-phone.md](../scenarios/where-is-my-phone.md) (device location — Truth-only)
- [../scenarios/nighttime-suppression.md](../scenarios/nighttime-suppression.md)
- [../scenarios/stewardship-obligations.md](../scenarios/stewardship-obligations.md)
- [../scenarios/why-did-this-happen.md](../scenarios/why-did-this-happen.md)

## Open decisions

| ID | Question |
|---|---|
| OD-17 | **Resolved as DL-62.** Primary Authority is required and deterministic for every directly measured Environmental Purpose, identically for a Physical Room and a Merged Room; Composite Contributor is removed from the ordinary path; Formula-Derived Fact governance (input availability, provenance, versioning) is accepted, with Dew Point ready and Mold Index/Condensation Risk unresolved |
| OD-18 | **Resolved as DL-59.** Truth distinguishes Current-State Sources from Point-in-Time Observation Sources; current-state Facts read the most current authoritative Home Assistant state at evaluation time; operational expiration is a DL-25 lifecycle transition; Truth Confidence (DL-58) is never decayed by elapsed time alone |
| OD-19 | **Resolved as DL-63.** A genuine Truth conflict requires the same Subject, predicate, context, and evaluation time, independent eligibility after Truth's qualification order, and mutual incompatibility with no accepted authority/validity/availability/configuration/Identity/Stewardship rule already explaining the difference; Truth publishes a reduced-confidence Fact, an unresolved Fact, or `unknown` under a versioned Conflict Policy |
| OD-73 | **Interaction-Surface Room Context Resolution.** How Room Context is resolved for a phone, wearable, Companion App, browser session, or other non-room-bound surface. An Engagement Fact records Room Context as `unresolved` until this closes |
| OD-74 | **Resolved as DL-58.** Truth Fact Confidence is a uniform ordinal band (Low < Moderate < High < Very High), structurally separate from DL-39 Identity Confidence, independent of freshness/provenance/coverage, and consumed without redefinition by OD-17, OD-18, and OD-19 |
| OD-33 | **Closed — DL-43, DL-46, DL-47.** Historical Facts follow External History Retention with their own Retention Classification; per-Fact-class differentiation is Operational Trust policy |
| OD-34 | **Closed — DL-42, DL-44, DL-46, DL-47.** The temporal-persistence model is complete; the representation mechanism is **OD-01** |

## Related documents

- [room-configuration.md](room-configuration.md)
- [person-and-identity.md](person-and-identity.md)
- [temporal-record.md](temporal-record.md)
- [../contracts/truth-contract.md](../contracts/truth-contract.md)
- [../architecture/adr-historical-explainability-and-historical-truth.md](../architecture/adr-historical-explainability-and-historical-truth.md)
- [../architecture/failure-and-degradation.md](../architecture/failure-and-degradation.md)
