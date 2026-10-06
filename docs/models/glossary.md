# HTBW Canonical Glossary

> **Document status: Canonical (constitutional).**
> This is the single canonical terminology source for the HTBW repository.
> Where any other document uses a term differently, this glossary prevails.

Terms are grouped for readability. Every canonical responsibility document links here.

---

## Places

**Home**
The complete governed household. The outermost scope. Owns home-scoped policy such as security
posture, quiet hours, the global autonomy ceiling, and default privacy policy.
Model: [home.md](home.md)

**Physical Room**
An actual physical space, normally corresponding to a Home Assistant Area. Retained for asset
location, maintenance, environmental evidence, sensor provenance, diagnostics, and more precise
facts.

**Room**
The HTBW interaction context. A Room may be composed of exactly one Physical Room or of several.
A Room is the unit residents talk to and about.
Model: [room.md](room.md)

**Merged Room**
A Room configuration composed of more than one underlying Physical Room or Home Assistant Area.
Example: *Living Space* = Kitchen + Dining Room + Living Room.
**A Room and a Merged Room behave identically from the resident and runtime perspective.** No
separate orchestration logic exists for merged rooms.
**A Physical Room participates in at most one Merged Room at a time (DL-67)**: a Merged Room is a
curated conversational interaction context, not a general grouping mechanism, and Home Assistant's own
Floor/Area targeting meets the household's need for a broader or different grouping.
**A Merged Room has no native Home Assistant representation (DL-68)**: no proven consumer requires
one, and Assist/Conversation must never receive one.
This is the canonical public term. Do not rename it.

**Constituent Room**
A Physical Room that is a member of a Merged Room. Constituent membership is retained and remains
addressable for location, maintenance, evidence, and diagnostics.

**Room Configuration**
The interaction-definition model that declares which resources participate in a Room, which are
exposed, what residents call them, what Room Help says, and which sensors feed composite facts.
Owned by Foundation. **It is not an inventory screen and not merely a location model.**
Model: [room-configuration.md](room-configuration.md)

**Vocabulary**
The governed household-language layer mapping a natural word or phrase to a referenced Room, Merged
Room, device, target set, Asset, service, information source, capability, or another accepted HTBW
meaning within an applicable context (**DL-69**). Contextual, never globally unique. Scoped to Home
(Global), Room, Merged Room, or Person; a Home-scoped term is inherited everywhere no narrower term
exists, and a Room or Merged Room may shadow it (**DL-70**). Owned by Foundation as part of Room
Configuration; Person-scoped Vocabulary is coordinated through Person Setup under the same concept —
**no new responsibility is created**. Not a native identifier, a formal Asset name, a permission, an
exposure decision, or an execution authorization.
Model: [contextual-vocabulary.md](contextual-vocabulary.md)

**Fulfillment**
Which provider, target, script, Asset, capability, or source currently satisfies a Vocabulary term —
distinct from the word itself (**DL-70**). A term may stay Home-scoped and stable while its
Fulfillment varies by Room, Merged Room, or Person (for example "News" everywhere, with different
configured sources per Room). Not a new store or a new responsibility — Fulfillment is the existing
Room/Merged-Room/Person configuration fields Vocabulary resolves to.
Model: [contextual-vocabulary.md](contextual-vocabulary.md)

**Room Context**
The Room that a request is evaluated against. Normally established by the participating voice
assistant that received the request, or by an explicit resident statement, or by a UI surface.

> **Where the interaction arrives through a surface that is not bound to a Room** — a phone, a wearable, a
> Companion App action, or a browser session — **how Room Context is resolved is open decision OD-73**, and
> the governed interim outcome is `unresolved`: ask which Room, or refuse. **Room Context is never inferred
> from device naming.** Every Decision Trace must record Room Context **and how it was resolved**.
> Model: [room-configuration.md](room-configuration.md)

**Superseded terms**

| Old term | Canonical mapping |
|---|---|
| Composite Room | **Merged Room**. Historical contracts and models used "Composite Room" as the internal term and "Merged Room" as the user-facing term. HTBW now uses **Merged Room** for both. Not to be confused with **Composite Fact**, which is a Truth concept and remains canonical. |
| Operational Space | **Room** (and **Merged Room** where more than one Physical Room participates). |
| Interaction Space | **Room Context**. |
| Listening Area | The **Room** assigned to a participating voice assistant. |
| Space | Ambiguous. Use **Home**, **Physical Room**, **Room**, or **Merged Room**. |

---

## Things

**Asset**
An HTBW-known thing that matters, whether or not it is device-backed: appliances, equipment,
artwork, instruments, furniture, vehicles, collections, documents. Carries authoritative identity
and descriptive knowledge.
Model: [asset.md](asset.md)

**Home Assistant Device**
A Home Assistant registry object representing a physical or logical device. **Not** the same object
as an HTBW Asset. One Asset may map to zero, one, or several Devices.

**Home Assistant Entity**
A Home Assistant state-bearing object belonging to a Device or standing alone. **Not** the same
object as an Asset and **not** the same object as a resident-facing capability.

**Sensor**
An evidence-producing source. A Sensor may exist without being exposed and without participating in
any composite fact.

**Person**
A human known to the household. Distinct from a Home Assistant `person` entity, which is one
possible backing primitive. **A Person is never an Asset.** A Person may carry a Stewardship care
obligation without being modelled as property, inventory, or a tracked object.

**Pet**
A non-human household member that may carry Stewardship obligations (medication, food, walks,
veterinary appointments) and may be relevant to Truth and safety. **A Pet is not a Person and is not
an Asset**, and must never be reduced to an equipment record. A Pet is a Truth Fact **Subject** and is
never routed through Identity.

**Service**
An external provider relationship, such as a service company, technician, or subscription. Not a
Home Assistant service call.

**Asset Type**
The authoritative classification of what an Asset is, owned by **Foundation** as descriptive
knowledge. It is not a user-interface filter, and it is not owned by a Home Assistant Label.
Model: [asset.md](asset.md)

**Native Representation**
A Home Assistant object that makes an HTBW concept visible, targetable, or automatable natively — a
Device created for an Asset, an Entity publishing a determined value, a Label projecting a
classification. A native representation is a **projection**. It never becomes the authoritative HTBW
record, and its absence or deletion never changes what HTBW holds to be true. See **DL-31**.

**Managed Label**
A Home Assistant Label within a reserved set that HTBW creates and maintains as a derived projection
of an authoritative HTBW classification. Home Assistant owns the Label object. **Resident-created
labels are never removed or overwritten**, and removing a Managed Label changes no classification.

**Extension**
Additional governed HTBW information attached **to** a referenced Home Assistant object by its stable
identifier. An extension never absorbs the native object and never copies the properties that object
natively owns. See **DL-31**.

---

## Knowledge

**Evidence**
A raw or lightly processed observation. Evidence has a source, a timestamp, and a freshness. Evidence
is **not** Truth.

**Identity Evidence**
Evidence usable for deciding who a person is: voice match, BLE proximity, assigned phone/watch/tablet
signals, companion-app reports, presence trackers, Wi-Fi association, room transitions, vehicle
association.

**Identity Evidence Association**
The governed binding between **one Person and one evidence source**, holding the HTBW-specific
interpretation of that source for that Person: which claims it may support, its **configured
reliability** and provenance, freshness rule, evidence family, consent requirement, enabled state,
known limitations, and whether corroboration is required. Owned by **Identity**. It references native
objects and **copies no native property** (**DL-31**), and it is **not** a second Person record or a
duplicate person-to-tracker registry.
Model: [person-and-identity.md](person-and-identity.md)

**Assertion Purpose**
The question a given Identity Assertion answers — Speaker Attribution, Room Presence, Household
Presence, Interaction Initiator, Authenticated Session Identity, or Endpoint Context. **There is no
general-purpose identity score**, and an assertion for one purpose never answers another.

**Configured Association Reliability**
A governed household configuration expressing how strongly an evidence source should contribute **for
a specific Person and claim**. Stated as a band, optionally backed by a normalised contribution
weight. **It is not measured accuracy**, and must never be presented as such. A device type may supply
a default suggestion; the authoritative value belongs to the association.

**Evidence Family**
The correlation group an observation belongs to. Observations originating from **one physical device**
or one provider share a family and are **not counted as independent confirmations**. Independence is
never assumed merely because evidence arrived through different entities.

**Provider Match Value**
The candidate and match value reported by an evidence provider, such as a voice matcher. It is
**evidence**, retained as reported. **It is never rewritten as the fused identity confidence** and is
never presented as the home's own belief.

**Assertion**
A claim produced by a responsibility from evidence, carrying confidence and attribution.

**Identity Assertion**
Identity's output: a candidate person, **the purpose it answers**, a confidence value, and the evidence
that produced it. **Not** a contextual person-presence fact.

**Identity Fusion Function**
The deterministic, ordinal, purpose-scoped function by which Identity converts eligible evidence into
an Identity Assertion. Support is set by one **anchor family** and raised by bounded corroboration
steps; it is **never summed, averaged, or multiplied**. Owned by **Identity** alone — Truth,
Operational Trust, Concierge, Communication, and reasoning providers never fuse identity evidence, and
**confirmation is never an input**.
Model: [person-and-identity.md](person-and-identity.md)

**Fusion Policy**
The governed, versioned record holding purpose minimums, family ceilings, corroboration and reduction
rules, separation requirements, freshness rules, the band map, and the reason-code set. **Every
Identity Assertion references the version that produced it**, and a change never recalculates an
earlier assertion.

**Candidate Set**
The bounded set of Persons evaluated for one assertion purpose. Members enter from a nominating
provider, an Identity Evidence Association, an authenticated user, a consumed native association, or a
governed interaction. **Never from an unassociated source, a synthetic Guest, a reasoning provider's
suggestion, or household membership alone.**

**Evidence Eligibility**
The gate applied **before any weighting**. Evidence lacking consent, disabled, prohibited by policy,
inapplicable to the claim, beyond its freshness bound, or belonging to another Person or purpose is
**excluded with a reason** — never merely down-weighted.

**Candidate Separation**
The governed requirement that the leading candidate exceed the next by a stated margin before `known`
may be asserted. Where it is not met, the outcome is `ambiguous`. **The numerically highest candidate
is never silently selected.**

**Confidence Normalisation**
The mapping from an ordinal support level to a **confidence band** through a versioned band map. A
normalised numeric may accompany the band as a deterministic ordering value; **the band is
authoritative**, and the numeric is never a probability, a likelihood, or a measured accuracy. The band
enumeration and its meaning are **DL-39**.

**Unknown Person**
A **valid** Identity Assertion outcome: a human participant is supported for the stated purpose, but no
eligible known Person can be established. Momentary, expiring with the assertion. **Not** an error,
not `unavailable`, not an ambiguous choice among known candidates, **not a Home Assistant Person**,
not a profile, and not a permission.
Model: [person-and-identity.md](person-and-identity.md)

**Known Non-Resident Person**
A specific, intentionally configured Person who is not a resident — and who may therefore carry a
native Person reference, consent, permissions, and governed extensions. **Known**, and therefore never
an Unknown Person.

**Person Extension**
A household-facing, collective name for the totality of HTBW's governed configuration for a Person —
permissions, Vocabulary, preferences, relationships, and consent (**DL-71**). **Not a new store or a
new responsibility**: each piece remains owned by the responsibility that already owns it (**DL-31**
— "distributed, each extension keeps its own owner"). Person Setup is the shared configuration
experience across that distributed ownership.

**Guest fallback Person Extension**
Exactly one existing, deliberately configured Person a household may designate as the default
consulted when Identity yields **Unknown Person** (**DL-71**). Consulting its settings as interaction
defaults creates **no Identity Assertion** binding Unknown Person to it; Unknown Person remains
exactly what it already is (**DL-33**). May hold resources, Vocabulary, permissions, and relationships
if deliberately configured — none of that is prohibited by default.

**Copy Settings From Person**
A setup-time convenience that copies permissions/allowed interactions, Person Vocabulary, and
preferences/presentation defaults from one Person Extension into another, persisted independently at
the destination (**DL-71**). **Never copies** resources, relationships, consent records, identity
evidence, or other Person-bound state. Creates no runtime inheritance and no Role.

**Unknown Evidence Source**
An observed evidence source that is associated with no Person — an unassociated proximity source, an
unassociated device tracker, an unmatched voice sample, an unauthenticated interaction, or occupancy
without identity evidence. It may support an Unknown Person assertion. It **never** independently
establishes a Person, a role, a recurring individual, the same actor across time, permission, or
intent, and it creates no durable identity record.

**Unidentified-Person Policy**
The Operational-Trust-owned policy applied to a request attributed to an Unknown Person. **A policy
subject, never a profile and never a person**: it holds no preferences, no history, and no learning,
and it inherits nothing from any resident.
Model: [operational-trust.md](operational-trust.md)

**Fact**
An authoritative, governed statement about what is true now, owned by Truth, carrying provenance,
confidence, and validity.
Model: [truth.md](truth.md)

**Composite Fact**
A Fact that Truth derives by combining **more than one different Environmental Purpose's** current
Fact through a named, versioned formula — for example Dew Point, derived from Temperature and
Humidity. Also called a **Formula-Derived Fact**. It is never a same-purpose combination of equivalent
sensors: for an ordinary directly measured Environmental Purpose, Truth reads one selected **Primary
Authority**'s current state as an **Authority-Derived Fact** instead (**DL-62**, resolving OD-17).

> **Composite Fact is not related to the superseded term "Composite Room".** A Composite Fact is about
> combining *different-purpose evidence*. A Merged Room is about combining *Physical Rooms*. A
> Composite Fact may be scoped to a Room or to a Merged Room.

**Authority-Derived Fact**
The ordinary product of Room Configuration's Primary Authority selection: a Truth Fact read from one
selected source's current state, carrying Truth Confidence, provenance, freshness, and validity, but
**no contributor coverage** — it states that the household selected this source to represent the Room
purpose, never that every possible sensor agrees (**DL-62**).
Model: [truth.md](truth.md)

**Formula-Derived Fact**
A Composite Fact that combines more than one **different** Environmental Purpose's current Fact
through a named, versioned deterministic formula. Preserves its input Fact references, input validity
and confidence, derivation identity and version, formula or provider provenance, produced value, unit,
Truth Confidence, validity, and a named failure reason where not produced. A missing or invalid
mandatory input publishes it as `unknown` — never a partial calculation, never a retained last value
(**DL-62**).
Model: [truth.md](truth.md)

**Genuine Truth Conflict**
Two or more currently eligible, semantically comparable claims addressing the same Subject,
predicate/Fact purpose, context, and evaluation time, remaining independently eligible after Truth's
qualification order runs, and mutually incompatible, with no accepted authority-selection, validity,
availability, configuration, Identity, or Stewardship rule already explaining the difference. Truth
publishes a reduced-confidence Fact, an `unresolved` Fact, or `unknown` — never an average, a majority
vote, or a universal provenance-class precedence (**DL-63**).
Model: [truth.md](truth.md)

**Truth Conflict Policy**
The versioned, Fact-class-scoped configuration governing disagreement thresholds, semantic
comparability, publication minimums, confidence-reduction rules, range eligibility, and persistence
conditions for a **Genuine Truth Conflict**. Never contains Identity Fusion rules, person-ranking
rules, universal provenance precedence, or Stewardship significance. Every conflict outcome references
the policy version used; a later policy change never rewrites a Historical Fact (**DL-63**).
Model: [truth.md](truth.md)

**Environmental Purpose**
One of Room Configuration's extensible, household-oriented environmental meanings a source may be
mapped to in a Room — for example temperature, humidity, dew point, illuminance, UV, VOC, particulates,
CO2, mold index, leak, pressure, vibration, or noise. The set is never closed and never claims a
household has every sensor (**DL-60**).
Model: [room-configuration.md](room-configuration.md)

**Primary Authority**
For an Environmental Purpose in a Room, the single **required** source a direct Room-level question
resolves to — at most one per purpose, deterministic, and identical for a Physical Room and a Merged
Room. Distinct from **Secondary/Corroborating** participation, and never runtime-arbitrated among
equivalent sources (**DL-60**, **DL-62**).
Model: [room-configuration.md](room-configuration.md)

**Direct Environmental Measurement**
A value a device or integration reports as its own observation of an environmental property — for
example a thermostat's temperature reading. May be selected as a Room's Primary Authority for the
corresponding Environmental Purpose, producing an Authority-Derived Fact (**DL-62**).
Model: [truth.md](truth.md)

**Provider-Derived Environmental Indicator**
A value an external device, integration, or service **calculates** from one or more measurements,
historical trends, or a provider-owned algorithm, and exposes to Home Assistant as a native entity —
for example a device's Dew Point, Mold-Free Index, Health Index, Performance Index, or Virus Index
entity. May be selected as a Room's Primary Authority for a compatible Environmental Purpose, producing
an **Authority-Derived Fact that preserves the provider's identity and provider-qualified name — never
an HTBW Formula-Derived Fact merely because the provider's calculation used more than one measurement
internally.** HTBW makes no independent scientific claim about the provider's algorithm or cited limits;
it states only that the selected entity currently reports this value. Distinct from Foundation's
**Service** (an external provider *relationship*, `asset.md`) — this term describes an external
provider's calculated *environmental value* (**DL-62**).
Model: [truth.md](truth.md), [room-configuration.md](room-configuration.md)

**Person Environmental Requirement**
A Person-scoped declared minimum, maximum, or acceptable range for a **DL-60** Environmental Purpose,
reusing the Asset environmental-limit pattern without treating the Person as an Asset. Held by
Foundation, coordinated through Person Setup, self- or proxy-declared (**DL-56**, **DL-57**), and
evaluated by Stewardship against current Room Environment Facts only while a valid Contextual
Person-Presence Fact places the Person in that Room (**DL-61**). Never a diagnosis, a clinical
threshold, or a medical determination.
Model: [stewardship.md](stewardship.md)

**Configuration Completeness**
Of the Environmental Purposes a household has selected as *applicable* to a Room, the fraction that
currently have a configured source. A **Room Configuration** concern, distinct from Environmental
Coverage and Truth Confidence. An inapplicable, unconfigured purpose never counts against it (**DL-61**).
Model: [room-configuration.md](room-configuration.md)

**Environmental Coverage**
Of a Room's *configured* Environmental Purposes, the fraction currently available with a valid Fact — a
projection over Truth's per-Fact validity (**DL-59**), never itself a Truth Fact, never Truth Confidence,
and never Configuration Completeness (**DL-61**).
Model: [stewardship.md](stewardship.md)

**Room Environmental Status**
A non-authoritative household-facing projection over current per-subject Stewardship evaluations for a
Room's applicable Persons, Pets, and Assets. Never a Truth Fact, never a probability, never a medical or
clinical status, and never a replacement for an individual requirement evaluation; any presentation
color is presentation only, and every projected state drills through to its subject, Fact, requirement,
evaluation, significance, provenance, confidence, and validity (**DL-61**).
Model: [stewardship.md](stewardship.md)

**Presence**
A Truth fact that a specific person is in a specific Room.

**Occupancy**
A Truth fact that a Room contains one or more people, whether or not they are identified.

**Contextual Person-Presence Fact**
The authoritative combination: *this identified person is present in this Room now.* Produced by
Truth, not by Identity.

**Fact Subject**
The Foundation object a Fact is about, referenced by its stable identifier: **Home, Room, Merged Room,
Person, Pet, Asset, or Device**. The Fact is **one extensible model across every Subject**; no parallel
assertion type exists for any of them.
Model: [truth.md](truth.md)

**Location Fact**
A Truth Fact whose Statement places its Subject somewhere in the Home **now**, carrying confidence,
provenance, freshness, and validity. A **Person**-subject Location Fact is the **Contextual
Person-Presence Fact** and requires an Identity Assertion first. A **Pet**, **Asset**, or **Device**
subject requires **no Identity Assertion and must not be routed through Identity**. A Room-level Location
Fact is published only from evidence whose Room granularity is actually grounded. Where nothing can be
asserted, Truth publishes `unknown` and **never defaults to a Room**.
Model: [truth.md](truth.md)

**Declared Location**
The configured, durable statement of where something belongs or is kept, held by **Foundation** as the
`located-in` relationship. It carries no confidence, is not evidence-derived, and **is never the current
Location Fact**.
Contract: [../contracts/foundation-contract.md](../contracts/foundation-contract.md)

**Current Location**
Where something **is now** — a **Truth** Location Fact. Where declared and current location disagree,
**current location prevails as the Fact** and the declared relationship is unchanged.
Model: [truth.md](truth.md)

**Engagement Fact**
A Truth Fact stating that **an interaction is occurring**. It may carry the interaction channel, the
interaction surface, the Room Context or `unresolved`, freshness, and provenance. **It must never
identify the engaging Person.** It is not an Identity Assertion, never nominates a candidate Person, and
is **not** *Current Engager*.
Model: [truth.md](truth.md)

**Interaction Surface**
The device or endpoint through which an interaction arrived — a participating voice assistant, a kiosk,
a Companion App, a wearable, a browser session, or a physical control. A surface may be **room-bound**,
in which case Room Configuration supplies the Room Context, or **not room-bound**, in which case Room
Context resolution is **open decision OD-73**. A surface identifies a **thing, never a person**; who is
engaging is answered only by a purpose-specific Identity Assertion.

**Historical Fact**
A Fact that is no longer current — superseded, withdrawn, operationally expired, or otherwise past.
Owned by **Truth**, which is the system of record for both present and historical Facts. A Historical
Fact is never presented as current, is never actionable, must not silently become current again, and
is not a retained raw evidence payload.
Model: [truth.md](truth.md), [temporal-record.md](temporal-record.md)

**Provenance**
The recorded lineage of a piece of evidence, assertion, fact, decision, or record: where it came
from, who or what produced it, and when.

**Confidence**
A stated degree of belief attached to an assertion or fact. Confidence is never silently discarded.
**This is a general term, never itself a machine-form field.** The two governed, separately-typed
forms are **Truth Confidence Band** (Truth-owned, **DL-58**) and **Identity Confidence Band**
(Identity-owned, **DL-39**) — they share household-facing labels and nothing else, and are never
converted, averaged, or compared as though they measured the same thing.

**Truth Confidence Band**
One of exactly four ordered levels — **Low < Moderate < High < Very High** — expressing the strength
of qualified evidentiary support for a Truth Fact under the applicable Truth evaluation policy. Applies
identically across every Fact Subject (Home, Room, Merged Room, Person, Pet, Asset, Device) and Fact
class. **Never probability, measured accuracy, or certainty; never a DL-39 Identity Confidence Band;
never authorizes anything.** Independent of freshness, provenance, and contributor coverage. An
optional normalised numeric may accompany the band as a non-authoritative deterministic ordering value
only. `None`, `unknown`, `unresolved`, `stale`, and `withdrawn` remain first-class Fact states, never a
fifth band.
Model: [truth.md](truth.md)

**Freshness**
How recently the underlying evidence was observed, and whether it remains valid.

**Current-State Source**
A Fact source whose integration intends its state to represent Home Assistant's **current** state
(e.g. a presence sensor, a door, a valve, an environmental sensor, device availability, a current BLE
nearest-proxy state). Classified by documented integration semantics, never by domain or device class
alone. Remains a valid current Fact while available and while its documented semantics support a
current claim; never aged by an HTBW-imposed generic delay (**DL-59**).
Model: [truth.md](truth.md)

**Point-in-Time Observation Source**
A Fact source whose value names a **prior event or observation** (e.g. last motion detected, last
doorbell ring, last-seen timestamp). Carries an operational validity window and **never becomes a
current-state claim merely because its timestamp exists** (**DL-59**).
Model: [truth.md](truth.md)

**Fact Validity**
Whether a Fact remains current — a dimension **separate from Truth Confidence** (**DL-58**),
provenance, and coverage. Governed for a Current-State Source by availability and documented
integration semantics; governed for a Point-in-Time Observation Source by an operational validity
window. Operational expiration is a Truth lifecycle transition (**DL-25**) and never rewrites the
Fact's Historical confidence (**DL-59**).
Model: [truth.md](truth.md)

**Context**
The assembled set of resolved room context, identity assertions, facts, preferences, obligations,
and policies available when a decision is evaluated.

**Rejected terms**

| Rejected term | Canonical mapping |
|---|---|
| **Current Engager** | **Not an HTBW architectural term, and it must not be introduced.** Who is engaging is answered by the applicable **Assertion Purpose**, produced by **Identity**: **Speaker Attribution** (who most likely spoke), **Room Presence** (who is likely physically present in this Room), **Household Presence** (who is likely home), **Interaction Initiator** (who initiated this digital action), **Authenticated Session Identity** (which authenticated account initiated the request), or **Endpoint Context** (through which managed endpoint this arrived). **Use the existing purpose-specific assertions.** A single fused "engager" result would recreate the general-purpose identity score prohibited by **DL-32** and **DL-38**, break the **F1** purpose ceilings, break **DL-36**'s four independent consumers, and break **DL-34**'s separation of Requestor, Speaker, Present Person, Potential Listener, Authorized Recipient, and Delivery Target. **That one Person may be High for Household Presence, High for Room Presence, Moderate as the current speaker, confirmed as an authenticated account, and `unknown` as the physical holder of the device is the point — the architecture preserves those differences rather than averaging them away.** The Truth-side counterpart is the **Engagement Fact**, which states that an interaction is occurring and **never who is engaging** |
| **Room Health**, **Room Confidence**, **People Health** | **Not HTBW architectural terms; no synthetic authoritative state exists under any of these names** (`stewardship.md`, *"Room health" is not an HTBW term*; **OD-69**). A household-facing environmental summary must decompose into individual Truth Facts (each with its own Truth Confidence Band — **DL-58** — validity, and provenance) and separately owned Stewardship obligation states; it may summarize, but may never create a new determination or present one aggregate verdict as authoritative. **A conflict was found, not resolved**: current Concierge implementation evidence offers "People Health" and "Room Confidence" as selectable household-facing output labels, inconsistent with this prohibition — tracked as implementation-remediation evidence on **OD-69** |
| **Composite Contributor** (same-purpose sensor aggregation) | **Not an ordinary-path HTBW mechanism.** Room Configuration's earlier four-state disambiguation model (**DL-60**) included a same-purpose aggregation role; **no accepted household use case ever required combining multiple equivalent measurements of one Environmental Purpose into a single Room Fact**, and the role was removed from the ordinary path, narrowing Room Configuration to **Primary Authority** (required), **Secondary/Corroborating**, and **Explicit Exclusion** (**DL-62**, resolving OD-17). Use **Primary Authority** for the ordinary Room-level question, and a **Formula-Derived Fact** for a genuinely different-purpose derivation (for example Dew Point) |
| **HTBW Health Index**, **HTBW Performance Index**, **Aggregate Room Confidence** | **Not HTBW architectural terms; HTBW invents no such score.** A selected provider's own indicator (for example *"air-Q Health Index"* or *"air-Q Performance Index"*) may be displayed as a **Provider-Derived Environmental Indicator** with its provider-qualified name intact; **HTBW never adopts, recreates, or shortens it into an unqualified HTBW-owned health, wellness, or performance claim**, never presents it as a Person's health or performance, and never lets it override a subject-specific Environmental Requirement evaluation. **A provider's product name remains a valid label for the provider's own output; the unqualified HTBW terms above remain rejected regardless of what any provider names its indicator** (**DL-62**) |

> A **rejected** term differs from a **superseded** one. A superseded term named something real that has
> since been renamed. **A rejected term names a construct the architecture does not have, and adopting it
> would collapse distinctions that are deliberately kept apart.**

---

## Time and history

All terms in this section are defined by the Foundation-owned shared temporal model.
Model: [temporal-record.md](temporal-record.md)

**Current Projection**
The representation answering *what is true or configured now* for a governed record. Mutable,
optimised for runtime, owned by the responsibility that owns the record. Determining current state
must never require replaying complete history.

**Change Record**
An immutable record of *what changed* to a governed record: subject, change type, Effective Time,
Recorded Time, actor, prior and new version references, changed fields, provenance, and privacy and
retention classification. Owned by the responsibility owning the changed record.

**Domain Event**
A meaningful occurrence **in the household** — a door opening, occupancy becoming established, a
transfer being requested.

> **A Domain Event is something that happened in the household. A Change Record is something that
> happened to a governed record.** They are distinct object kinds and must never be collapsed into a
> single generic event type. Neither revives the superseded [event-model.md](event-model.md).

**Snapshot**
Governed state at a point in time for a bounded scope, identifying the exact record versions included
and the last-applied Change Records. **An accelerator for reconstruction, never an independent source
of truth.** A Snapshot never rewrites history, never replaces provenance, never reinstates content
removed under privacy policy, and never hides a gap.

**Governed Reference**
An immutable pointer to an **exact version** of a governed record. Transfers no ownership, permits no
re-derivation, and must resolve or be explicitly reported as unavailable. A dangling reference is
reported, never silently rendered as though the source record never existed.

**Version Identity**
The identity by which an exact state of a governed record is addressed, so that dependent records may
reference versions rather than mutable objects. The identifier scheme is open decision **OD-38**.

**Effective Time**
When a change took effect in the household.

**Recorded Time**
When HTBW recorded the change. Distinct from Effective Time; both are constitutional. A correction is
a **new** Change Record, never an overwrite.

**Historical Reconstruction**
A projection of governed state or activity for a past time or range, assembled from the nearest valid
Snapshot plus subsequent Change Records in Effective Time order. **A projection — never a store and
never a source of truth.** A reconstruction containing an unreported gap is a defect.

**Preservation Hold**
A policy marker protecting applicable records from normal purge, truncation, archival deletion, or
retention-driven deletion. Authorised by **Operational Trust**; enforced by each responsibility over
its own records. An HTBW architectural term, **not a claim of legal effect**.

**Unknown Actor Reference**
A bounded, non-Person reference within a **single** Historical Reconstruction, grouping observations
sufficiently supported as belonging to one actor. Part of the projection — **never a store, never an
identity, never a role, and never proof that the observations share one human**. Temporal proximity
alone never establishes one. Carries a **Primary Hypothesis Label**, a **Criteria Satisfaction
Record**, **Supporting Evidence**, and **Contradicting Evidence** (**DL-74**).
Model: [temporal-record.md](temporal-record.md)

**Primary Hypothesis Label (DL-74)**
The sole summarising output of an Unknown Actor Reference reconstruction: **Probably One Actor**,
**Probably Multiple Actors**, or **Unresolved Plurality**. Never a numeric score, probability,
percentage, or weighted calculation. Derived from the pattern of a **Criteria Satisfaction Record**,
never from a calculation. **Unresolved Plurality is a first-class, non-ordered outcome, never a
synonym for low confidence in a one-actor hypothesis.** ⚠️ **Name collision, not a reuse.** This is
**not** Audience Composition's existing *"Unresolved plurality"* state (**DL-34**): that state answers
*who could perceive* a delivery; this answers *was this the same actor*. The two are never
convertible, never compared, and never collapsed into one meaning. Structurally distinct from **DL-39**
Identity confidence, **DL-58** Truth confidence, **DL-73** Behaviour Source confidence, **DL-40**
Required Confirmation Strength, and **DL-34** Audience Composition — confirmed by a full repository
vocabulary review before this term was accepted.

**Criteria Satisfaction Record (DL-74)**
The combination mechanism for a Primary Hypothesis Label. Each of **DL-35**'s six accepted correlation
factors — adjacency, travel plausibility, evidence continuity, entry and exit, contradictions, and
competing-actor evidence — is individually recorded as exactly one of **Supports Hypothesis**,
**Contradicts Hypothesis**, **Unavailable**, or **Not Applicable**. **No weighting, ranking,
averaging, scoring, or probability is applied.** A contradiction is surfaced directly as its own entry
and is never averaged away; a material contradiction may force **Probably Multiple Actors** or
**Unresolved Plurality** instead of **Probably One Actor**.

**Evidence Package**
A governed assembly of records for a stated scope, produced on demand, recording its own scope,
filters, redactions, missing records, and known gaps. **Never an alternative source of truth** and
never authoritative over the records it summarises. An HTBW architectural term, **not a claim of
legal effect**.

**Tombstone**
The marker left when a governed record is deleted, purged, or truncated, so that *"a record existed
and was removed"* never becomes indistinguishable from *"nothing happened"*.

**Capability Dependency**
A stated precondition without which a capability cannot exist in this home — a native Home Assistant
capability, an integration, a provider, Connected Storage, consent, or configuration. Declared by the
responsibility that owns the capability. **Creates no Capability responsibility, registry, or
broker.**
Architecture: [../architecture/failure-and-degradation.md](../architecture/failure-and-degradation.md)

**Capability Unavailable**
The outcome when a declared dependency is missing. **A dependency failure — never a trust failure, an
identity failure, or a permission failure.** Identity and requirement are not evaluated, the missing
dependency is named, and the capability is never emulated, approximated, or silently reduced.
Architecture: [../architecture/failure-and-degradation.md](../architecture/failure-and-degradation.md)

**HTBW Defect State**
The authoritative, owning-responsibility-held record that a configuration or dependency condition is
wrong — a missing capability dependency, a broken governed reference, or a violated configuration
invariant. **Always held by the responsibility that detected it** (Room Configuration, Foundation,
Identity, Truth, or Operational Trust); never Repairs' own. A Repairs issue is a projection of this
state, never the reverse (**DL-65**).
Architecture: [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md)

**Repairs Issue**
The Home Assistant issue-registry entry an owning responsibility creates to surface an **HTBW Defect
State** to an administrator. **A projection, never a second authority**: the owning responsibility
creates and deletes it as its own Defect State changes; Home Assistant performs no independent defect
detection. Never an obligation store, a Communication, or an acknowledgement mechanism. Ignoring one
neither deletes nor resolves it, and never changes the underlying Defect State (**DL-65**).
Architecture: [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md)

**Artifact Declaration**
The five properties every artifact stored outside Home Assistant must state before it is introduced:
**Artifact Type, Owner, Storage Location, Retention Strategy, Deletion Strategy**. An artifact with
an undeclared lifecycle **must not be created**.
Architecture: [../architecture/connected-storage.md](../architecture/connected-storage.md)

**Governed Namespace**
The single HTBW-owned branch of connected storage, separated by artifact-owning function or artifact
class. Requires collision-resistant references, traceability to a governing object, and no
cross-capability mixing. **Root and folder names, path depth, and file naming are implementation
mapping, not architecture.**
Architecture: [../architecture/connected-storage.md](../architecture/connected-storage.md)

**Artifact Reference**
The governed record by which HTBW locates and controls an externally stored artifact — identifier,
class, owner, creating capability, governing parent, native anchor, storage class, relative locator,
lifecycle, retention, deletion trigger, consent and preservation effects, availability, and
reconciliation state. **The reference, never a typed path or a display name, is the authoritative
way to reach an artifact.** No universal payload schema is implied.
Architecture: [../architecture/connected-storage.md](../architecture/connected-storage.md)

**Governing Parent Object**
The object whose existence justifies an artifact's existence — an Asset for its documents, a voice
profile for its voiceprint, a Person for that profile.
Architecture: [../architecture/connected-storage.md](../architecture/connected-storage.md)

**Parent Removal Behavior**
The declared rule for what happens to an artifact when its governing parent is removed. **The
ordinary default is cleanup; continued existence requires an accepted reason.** Never silently
overrides a Preservation Hold or a retention floor, and **distinct from retention** — a time window
and a governing object answer different questions.
Architecture: [../architecture/connected-storage.md](../architecture/connected-storage.md)

**Interaction Model**
The classification every artifact class declares alongside its lifecycle: **Managed Content**
(resident-facing, reached through the owning capability — an Asset document), **Internal Runtime
Artifact** (never browsed by residents — a voiceprint or enrollment sample), or **Queryable
Historical Record** (reached by asking a question, never by opening a file).
Architecture: [../architecture/connected-storage.md](../architecture/connected-storage.md)

**External History Retention**
The single configured period by which Connected Storage extends retention beyond the Home Assistant
window. **Both the retention window and the purge window** — anything older is removed
automatically, and no separate archive tier is introduced. A **ceiling**, never an authority: it
overrides no retention floor and no Preservation Hold. Disabled by default, in which case HTBW
follows Home Assistant retention.
Architecture: [../architecture/connected-storage.md](../architecture/connected-storage.md)

**Incident**
A **retrieval scope** over governed records — a bounded set of records relating to a single situation.
Whether an Incident or Case may become a persisted object is open decision **OD-41**, and is not
decided.

**Historical Explainability**
Cross-cutting architecture requiring that the home be able to reconstruct what it observed, believed,
knew, and decided, and why. It **assembles** governed records held by their canonical owners. It owns
no store and is **not** a responsibility.
Architecture: [../architecture/explainability.md](../architecture/explainability.md)

---

## Configuration and interaction

**Vocabulary Term**
A human word used in a Room, such as "Lights", "Lamps", "Shades", "Speakers", "TV", "Media Player",
"Piano". The configured term is **authoritative**, in whatever form the household chose, and is the
only value they maintain.

**Recognition Form**
A system-generated variation of an authoritative Vocabulary Term, used only for matching and
understanding. **It is not an independently maintained vocabulary entry**, resolves to exactly that
term's target set, and is always outranked by a configured term. A plural recognition form does not
imply a group.
Model: [contextual-vocabulary.md](contextual-vocabulary.md)

**Vocabulary Mapping**
The explicit, persisted, deterministic association between a Vocabulary Term in a Room and its
target set. Resolution must not require a runtime search of Room devices and must not guess from
entity names.
Model: [contextual-vocabulary.md](contextual-vocabulary.md)

**Home Assistant Native Name**
The name Home Assistant holds for a Device or Entity, including a registry name a resident set.
**Home Assistant is authoritative for it**, and HTBW reads it through the native object reference
rather than storing its own copy.

**Home Assistant Assist Alias**
An alternate term a resident configures in Home Assistant for an **entity, an Area, or a Floor**, used
by Assist alongside native names, and usable by other assistants where those are set up. **Home
Assistant is authoritative for it.** No native Device-level alias is documented.
See [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md).

**Vocabulary Seed**
A native name or Assist alias used to **initialise** a Vocabulary Term that has no household value
yet. A seed is a starting point attributed to Home Assistant. It is **not** a second authority, not
continuous synchronisation, and **never a write-back instruction**.
Model: [contextual-vocabulary.md](contextual-vocabulary.md)

**Customized Contextual Term**
A Vocabulary Term the household supplied or edited. It is **never automatically overwritten** when the
native name or alias later changes, and it is **never automatically written back** into Home
Assistant. Recorded as `household_defined` mapping source.

**Existence**
The asset, device, entity, sensor, person, pet, service, or relationship is known.

**Participation**
The item has been explicitly selected to contribute to a Room capability, experience, composite
fact, or interaction.

**Exposure**
The item or grouped capability is intentionally made available to residents through vocabulary, Room
Help, UI, conversation, or another interaction surface.

**Home Assistant Assist Exposure**
A **Home Assistant platform setting**, not an HTBW concept, controlling whether an assistant may
target or interact with an entity. It is configured per entity and per assistant, and exists so that
sensitive devices cannot be controlled inadvertently by voice — a **safety precondition**, not an
informational seed. **It is not HTBW Exposure**, which governs whether something may be perceptible to
a resident at all. For voice- and conversation-mediated interaction, HTBW Exposure may **narrow** this
platform boundary but must **never widen past it or bypass it**; a non-voice surface (a UI panel, a
dashboard) is independently governed and not bounded by it (**DL-66**).
See [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md).

**Authority**
A person or automated process is permitted to use, change, query, or act on the exposed capability.

**Capability**
Something that can be done or asked in a Room, expressed in household terms rather than platform
terms.

**Group**
An explicitly configured set of targets addressed as one. Residents need not know its members.

**Room Help**
The answer to *"What can I do here?"*, generated from configured exposure — never from inventory.

---

## Behavior

**Preference**
A person-scoped or room-scoped statement of what is wanted. A preference is not a fact and not a
policy.
Model: [continuity.md](continuity.md)

**Policy**
A governed rule stating what is permitted, required, prohibited, or prioritized. Owned by Operational
Trust.
Model: [operational-trust.md](operational-trust.md)

**Identity Confidence Band**
One of **exactly four** ordered levels — **Low < Moderate < High < Very High** — carried by a `known`
Identity Assertion to express **the strength of identity support for its assertion purpose**. Produced
by the Identity Fusion Function (**DL-38**), enumerated by **DL-39**. A band carries **no access,
presentation, personalization, disclosure, confirmation, or authentication meaning**. `ambiguous`,
`unknown`, `unavailable`, and `not required` carry **no band**, and `None` is not a band.
Model: [person-and-identity.md](person-and-identity.md)

**Required Identity Band**
The Operational Trust configuration value stating what a protected capability or protected operation
requires of identity. It takes one of **five** values — **`None`, Low, Moderate, High, Very High** —
and is owned by Operational Trust wherever it is surfaced in configuration.
Model: [operational-trust.md](operational-trust.md)

**No Identity Required**
The Required Identity Band value **`None`**, meaning *this operation does not require a known-Person
identity*. **It is a Trust requirement, never an Identity output**, and it is not the bottom of the
band scale. An operation permitted under `None` is explained as *identity was not required* — never as
a band exceeding `None`. It is **not** an absence of governance: every other applicable policy still
applies.
Model: [operational-trust.md](operational-trust.md)

**Address by Name Threshold**
The general HTBW Operational Trust setting governing whether the home may speak a Person's name, and
the minimum **current** Identity band required to do so. Owned by Operational Trust because speaking a
name is a disclosure; applied by Concierge. Below the threshold, or when disabled, the home speaks
**neutrally** — which never denies the requested action.
Model: [operational-trust.md](operational-trust.md)

**Assertion Validity**
Whether an Identity Assertion remains a correct historical record of what evidence supported, for its
stated purpose, at the moment it was produced. **Permanent** — never revoked, decayed, or invalidated
by elapsed time alone. Retention of the persisted record is a separate matter (**DL-47**), and neither
is a fixed duration by confidence band or Assertion Purpose (**DL-64**).
Model: [person-and-identity.md](person-and-identity.md)

**Current-Interaction Applicability**
Whether an Identity Assertion is evidence-appropriate for **this** interaction, participant, and
assertion purpose. **Distinct from Assertion Validity:** an assertion may remain valid as a historical
record while being inapplicable to a new interaction. Answered by re-running the Identity Fusion
Function against current eligible evidence — never by consulting a stored expiry timestamp — so a
prior assertion is never revived because Room occupancy continued (**DL-64**).
Model: [person-and-identity.md](person-and-identity.md)

**Required Confirmation Strength**
The Operational Trust configuration value stating **what a confirmation must be worth** for a
protected operation, on the ordered class set **`None` < Verbal < Authenticated < Strong**. The
classes are distinguished by **independence from the evidence and channel that produced the
assertion**, not by friction. **A strength class is not a mechanism**: it is satisfied only by a
mechanism the deployment has verified as meeting it, and where none is available the outcome is
`Unavailable` — **never a silent downgrade**.
Model: [operational-trust.md](operational-trust.md)

**Operation-Scoped Confirmation**
A confirmation is **consumed by the protected operation for which it was requested**. It has no
occupancy grace period, establishes no authenticated session, does not carry into the next operation
by default, and **never changes the Identity band** (**DL-37**). A bounded multi-step task must state
its bound explicitly.
Model: [operational-trust.md](operational-trust.md)

**Identity Presentation Threshold**
The confidence at which the home may speak as though a candidate identity is likely — addressing a
Person by name, greeting them, or offering a person-scoped suggestion. Owned by **Operational Trust**
because speaking a name is a disclosure; applied by Concierge. **It grants no access, implies no
confirmation, and is never met by an Unknown Person.**
Model: [operational-trust.md](operational-trust.md)

**Capability Access Threshold**
The minimum identity confidence, or confirmation state, required before a capability, protected
resource, or protected operation may be exercised. It belongs to **what is being protected** — never
to the person, the evidence source, or Identity. **There is no universal threshold.**
Model: [operational-trust.md](operational-trust.md)

**Protected Resource**
Something an Operational Trust requirement attaches to — a person-scoped calendar or mailbox, an
asset record, household history. A person-scoped external resource is referenced through its **Person
anchor** (**DL-31**), and **ownership is never inferred from a connection's name**.

**Protected Operation**
A specific operation against a protected resource. Read, write, delete, and governance operations
**are never collapsed into one threshold**, and operation-specific requirements never force duplicate
resource definitions.

**Confirmation Opportunity**
A governed confirmation offered **instead of refusal** when identity confidence falls below what a
capability requires. Offering it is policy, not obligation, and declining it leaves the original
refusal standing.

**Confirmation Requirement**
A confirmation an operation demands **regardless of confidence**, because the act is consequential.
High probabilistic confidence never satisfies it.

**Confirmed Interaction**
The state produced by a successful governed confirmation, **bounded by its scope**. It is a scoped
interaction state, **not the top of the confidence scale**, not authentication, and not a session. It
**never rewrites the Identity Assertion it was raised against**, and is never rendered as a
percentage or as certainty.

**Confirmation Scope**
The bounds of a successful confirmation: purpose, capability and operation, interaction, channel,
Room, Person, and time — **and never audience**. Confirming identity or access confirms nothing about
disclosure (**DL-34**).

**Obligation**
A care responsibility owned by Stewardship, carrying **two orthogonal fields** (**DL-48**): a
**condition state** — `met`, `due`, `unmet`, `overdue`, `waived`, `unknown` — describing what is true
of the world relative to the care expectation, where **`met` means satisfied to date rather than
completed**; and a **lifecycle state** — `raised`, `active`, `deferred`, `closed`, `reopened` —
describing what has happened to the record itself. **An obligation
is not an action**, and its existence implies neither permission to act nor a Communication. It arises
from a **household declaration**, never from a framework judgement about what the household ought to
value. It is closed by a **Care Evidence Record**, never by a dismissed reminder, a ticked projection,
a requested action, or an executor reporting success.
Model: [stewardship.md](stewardship.md)

**Care Evidence Record**
What closes an obligation (**DL-48**). Carries exactly one evidence kind: `observed` — Truth
established that the condition resolved; `attested` — a person with accountability recorded that care
occurred where Truth cannot observe it; `performed` — an executor reported completion **and** Truth or
an attestation confirms it; or `waived` — a household decision closing the obligation **without
asserting that care occurred**. Declares its own Retention Classification (**DL-47**).
Model: [stewardship.md](stewardship.md)

**Completion Mode**
Explanatory vocabulary describing which of two already-accepted obligation configurations applies —
never a new stored state (**DL-71**). **One Completion Satisfies All**: one obligation names multiple
current caretakers, any of whom may produce the Care Evidence Record that closes it once for everyone.
**Each Recipient Must Complete**: multiple independent obligations exist, one per accountable Person,
each closed by its own Care Evidence Record. Both are ordinary applications of **DL-48**/**DL-57**.
Model: [stewardship.md](stewardship.md)

**Custody Period**
A **time-bounded accountability record** answering *who is accountable for this, for how long, and
under what agreement* (**DL-49**). Foundation defines the object type; **Stewardship owns the record,
its lifecycle, and its history**. **Custody is not ownership, not caretaking, and not location.** It
opens on a recorded Check-Out and closes only on a recorded Check-In — **physical return is evidence
toward closure, never closure**. **HTBW adopts no fixed custody-status enumeration**; the governed
lifecycle is `opened`, `updated`, `closed`, `corrected`, `adversely_resolved`. *In transit* and *in
storage* are Custody Periods with a carrier or storage provider as custodian; *overdue*, *lost*, and
*stolen* are not custody states, and **nothing is ever in the custody of "lost"**. **A custody record
declares accountability and expected location context; it never establishes current physical
location**, which requires a Truth Location Fact.
Model: [stewardship.md](stewardship.md)

**Significance**
A **Stewardship judgement about a household declaration** — why something matters, and how strongly —
represented as a **Significance Declaration** (**DL-75**). It is **not** a Truth fact and **not** an
Operational Trust policy. **Price, appraisal, sensor count, Identity participation, residency, and
registration confer no significance**, and **HTBW defines no ranking of people, animals, possessions,
spaces, or households**.
Model: [stewardship.md](stewardship.md)

**Significance Declaration (DL-75)**
The structured, machine-readable representation of Significance: **Derivation Source**, **Base
Significance**, **Provenance**, and **Effective Version** — four independently addressable fields,
never collapsed into one combined text value, a numeric score, or a probability. A household-facing
explanation may use natural language; the canonical model retains the structured fields underneath it.

**Derivation Source (DL-75)**
Answers *why does this obligation matter?* — Safety, Health, Security, Preservation, Value, Routine
Maintenance, Cost of Deferral, or Household Declaration. Mandatory for an accepted, declared
Significance. Independent of **Base Significance**: the same Derivation Source may later coexist with
a different Base Significance if the household's declaration changes.

**Base Significance (DL-75)**
Answers *how much does this matter, under its accepted declaration?* — exactly four canonical ordered
levels: **Routine < Important < Significant < Critical**. Importance language only — **never**
confidence, probability, truth, identity, accuracy, evidence quality, risk, urgency, issue severity, or
confirmation strength. Structurally typed and owned by Stewardship; never represented as an unqualified
`level`, `confidence`, `priority`, or `severity` field. **Comparable across every Stewardship subject in
a household** (Person, Pet, Asset, Device, Room, Home, Care Definition, Obligation) as one ordinal
meaning — but equal Base Significance never means equal action, equal risk, an erased Derivation
Source, or a silently resolved conflict between obligations. Structurally distinct from **DL-39**
Identity Confidence, **DL-58** Truth Confidence, **DL-73** Behaviour Source Confidence, **DL-74**
Unknown Actor hypothesis vocabulary, Operational Trust risk classification, and **OD-22**'s escalation
ladder — no conversion is ever made between Base Significance and any of these.

**Research-Based Recommendation (DL-75)**
A non-authoritative **Suggestion**-stage proposal (the existing **P26**/**DL-21** learning promotion
ladder) informed by external knowledge — manufacturer guidance, veterinary or conservation guidance,
professional standards, or cited LLM-assisted research — proposing a Derivation Source and/or Base
Significance. Preserves source citations, research date, scope, subject applicability, limitations,
and research provenance. **LLM output alone is not household authority** and never becomes policy
automatically.

**Observed-Household Recommendation (DL-75)**
A non-authoritative **Suggestion**-stage proposal based on governed observations of household behaviour
(the same **P26**/**DL-21** ladder), proposing a Derivation Source and/or Base Significance change.
Preserves supporting observations, observation period or scope, provenance, limits, and consent/privacy
constraints. **Observed behaviour alone is not household intent** and never becomes policy
automatically.

**Role**
A named position a person holds in the Home or in a Room, used by Operational Trust to derive
authority. Examples: resident, owner, child, guest, caretaker, service provider. **A bare Role is
unscoped to any subject** — distinct from a Relationship-based Audience Specification, below
(**DL-71**).

**Caretaker**
A person accountable for a specific Stewardship obligation or asset. **Accountability is not access**:
what a Caretaker or any other person may view, receive, declare, update, or close requires an explicit
**Delegated Access Grant** (**DL-57**), never inferred from the relationship or a Role alone. **The
`caretaker-of` relationship is many-to-many**: one Person may be caretaker-of multiple subjects, and
one subject may have multiple current caretakers (**DL-71**). Stewardship owns the current assignment
records; the Person view and the subject view are both projections over the same records, never
independently editable copies.

**Delegated Access Grant**
A Foundation-typed, Stewardship-operated record of explicit, scoped authority one Person holds over
another Person's, Asset's, or Pet's Stewardship content — subject, grantee, the specific operations
granted (view / receive / declare / update / schedule / complete / manage), scope, grant basis
(self or proxy), and effective/revocation time. Never conveys identity evidence, never implies access
beyond its stated scope, and is revocable at any time by the subject or an authorized proxy (**DL-57**).

**Owner**
The person or household entity with primary accountability for an asset.

**Experience**
A coherent household-facing activity that can be started, transferred, resumed, suppressed, or
ended — for example a music session, a video session, a briefing, or a Good Night routine.
Model: [experience-and-session.md](experience-and-session.md)

**Session**
A specific running instance of an Experience, with an owner, participants, an origin Room, a current
Room, and a lifecycle.

**Activity**
What is currently happening, expressed as a Truth fact — for example "a conversation is active".

> ⚠️ **Name collision.** *Activity* is also the name of the Home Assistant integration that records
> state changes and events, formerly called the Logbook. **The HTBW record of a meaningful occurrence
> in the household is a Domain Event**, owned by the responsibility that observed it. There is no
> HTBW Activity model, no Activity responsibility, and no Activity store.
> See [temporal-record.md](temporal-record.md).

**Behaviour Source**
What initiated an observed change — direct resident interaction (voice or dashboard/app), a native
Home Assistant automation, a native script, a scene activation, manual physical interaction with a
device, an external non-autonomous integration, or **unknown**. Recorded as attribution on a Domain
Event. **Never inferred from timing alone.** Carries a **Source Confidence** tier (**DL-73**):
**Known Source** (direct evidence — a same-context sibling execution event, or a `context_user_id`
match), **Probable Source** (evidence-supported inference — no competing source evidence, consistent
with a per-integration-verified device pattern), or **Unknown Source** (insufficient evidence — a
valid, sufficient, final answer, never a guess). **An HTBW-governed decision, an HTBW learned or
adaptive policy, an external autonomous policy engine, and a reasoning-provider recommendation are
not Behaviour Sources** — they are **Decision Authorities** (**DL-73**).

**Alternative-explanation handling (DL-73)**: HTBW never presents competing candidate sources as
parallel explainability outputs. It returns the single best-supportable attribution, or **Unknown
Source** where no candidate reaches the Known or Probable threshold. A recurring Unknown Source is
itself governance evidence — a signal of missing telemetry, missing integration support, or an
uncovered category — never a defect to conceal.

**Decision Authority**
*Why was the decision made* — which responsibility, configured policy, or reasoning process
determined an outcome. Representative examples: **Asset Intelligence** (a significance evaluation),
**Stewardship** (an obligation determination), **Continuity** (a restored preference), **Concierge**
(a household-decision evaluation), the **resident** (a direct request), an **Occupancy Automation**
(its own configured rule), an **HTBW-governed decision**, an **HTBW learned or adaptive policy**, an
**external autonomous policy engine**, or a **reasoning-provider recommendation**. Formally distinct
from **Behaviour Source** (*what initiated this*) and from **Execution** (*what Home Assistant or
another authorized environment actually did*) (**DL-73**). The explainability preference order is
Decision Authority, else Source, else the originating integration, else **unknown** — applied only
where the Decision Trace's own evidence supports the richer explanation; **unknown** remains fully
valid and sufficient. **HTBW Attribution applies in both directions**: to activities HTBW merely
observes within Home Assistant, and to activities HTBW itself decides and executes through Home
Assistant — in the latter case the resulting Domain Event's Decision Authority attribution references
the Decision Trace that produced it, without merging the two record kinds.

**Canonical Explainability Chain (DL-73)**
**Actor → Source → Decision Authority → Execution → Outcome → Explanation.** A sequencing
clarification layered over already-accepted architecture, never a replacement: Actor is Identity's
existing assertion-purpose model; Source is the Behaviour Source enumeration carrying its Source
Confidence tier; the triggering occurrence is the existing **Trigger**/**Domain Event** concept,
folded into Source rather than a separate stage; Execution, Outcome, and Explanation are the existing,
already-owned concepts this chain names in sequence.

**Person Attribution (DL-73)**
The person-dimension of Behaviour Attribution, carrying exactly three states: **Known Person** (a
`known` Identity Assertion exists), **Unknown Person** (a person may have been involved but Identity
cannot determine who — the existing **Unknown Person** state above, unchanged), or **No Person** (no
person participated in the decision at all — the attributed Decision Authority or Source is itself
non-person, for example Asset Intelligence, Stewardship, Continuity, a schedule, or an automation).
**No Person is not a fourth Identity state**; it is the attribution-layer statement that Identity was
never invoked for this occurrence. **Guest remains a trust-and-permissions construct, never an
attribution state**; an Unknown Person may receive Guest-equivalent permissions through Operational
Trust without creating any Identity Assertion binding the two (**DL-33**, **DL-71**).

**Learned Suggestion**
An observed pattern offered for approval. It is not a preference and not a policy until a person with
authority accepts it (**P26**).

**Adaptive Policy**
An approved learned behaviour the home may act on within an authorised ceiling. It is governed,
revocable, versioned, and explainable.

**Delegated Adaptive Behaviour**
Behaviour decided and executed by an external policy engine within a declared boundary. HTBW may
observe it and must disclose that it does not hold the external engine's reasoning.

**Mode**
A governed Room or Home state that changes what is permitted or appropriate — for example Nighttime
mode, Privacy mode, Quiet hours.

**Trigger**
The event that begins a decision evaluation: an utterance, a state change, a schedule, an obligation
becoming due, a room transition, or a UI action.

**Decision**
The evaluated conclusion about what should happen now. Owned by Concierge.

**Action**
The execution requested as a result of a Decision.

**Intentional Non-Action**
A Decision to do nothing, for a stated reason. It is a first-class outcome and must be as explainable
as an Action.

**Decision Trace**
The structured record of a decision evaluation, sufficient to answer why something happened and why
something did not.
Model: [decision-trace.md](decision-trace.md)

---

## Communication

**Communication**
A household interaction that must be conveyed — what must be conveyed, to whom, and about what. It
exists independently of the mechanism used to convey it, and is **never** defined as a notification,
push message, announcement, or indicator. Governed by **P31**.
Model: [communication.md](communication.md)

**System-Initiated Communication**
A Communication HTBW originates without a current explicit request — a medication reminder, new
private Mail, a Calendar reminder, a Stewardship warning (**DL-72**). Under audience uncertainty, the
accepted default prefers authorized private delivery. Distinct from a **Person-Requested Response**.

**Person-Requested Response**
A response to a Person's current explicit request — *"What is on my Calendar?"*, *"Read my Mail"*
(**DL-72**). The request is evidence of willingness to receive an authorized response through the
current interaction context — **never unrestricted consent**, and never authorization for another
Person's information.

**Audience-Uncertainty Routing Preference**
A Continuity-owned Person Setup preference, distinct from the ordinary delivery preference, answering
where a Communication should route when audience composition cannot be safely established for that
Person (**DL-72**). Supplies a desired degradation path only; Operational Trust determines whether it
is currently permitted and safe.

**Delivery**
The act of conveying a Communication through a surface. Distinct from the Communication itself.

**Delivery Attempt**
One bounded act of delivery to one surface, with its own outcome. A Communication may have many.

**Delivery Surface**
A governed capability abstraction of a place through which delivery may occur, declaring its
**capability dimensions**, its **Potential Perceptibility**, and whether it can attest presentation.
Never a device list, and **never declares itself private** (**DL-53**).

**Potential Perceptibility**
Which people could potentially perceive a delivery through a proposed Delivery Surface, given its
declared capability and current Truth evidence. Distinct from **Audience Composition** (Operational
Trust's disclosure-time evaluation) and from **Potential Listener** (a specific Person or Unknown
Person within a composition). Never sufficient on its own to declare a surface private (**DL-53**).

**Presentation Attestation Capability**
A Delivery Surface's declared capacity to attest that content was presented. Defaults to
**Unsupported**. Where unsupported, or where attestation evidence is absent, `Presented` is recorded
as **unknown**, never inferred as *not presented* (**DL-53**, **OD-55**).

**Presentation Outcome**
The technical determination of whether a Delivery Attempt's artifact was rendered, displayed, shown,
spoken, played, or otherwise made available through the selected surface. Exactly one of **Presented**,
**Failed**, **Unknown**, or **Attestation Unavailable** (**DL-54**). A technical claim only — it never
asserts perception, acknowledgement, correctness, or that the household's request was satisfied.

**Acknowledgement**
An explicit responsive act by an **identified person** — closing, dismissing, confirming, denying, or
answering. Distinct from **Presentation Outcome**: a surface attesting that content was technically
presented is never acknowledgement, and acknowledgement never rewrites a historical Presentation
Outcome (**DL-54**, **OD-45**).

**Recipient Attribution Capability**
A Delivery Surface's declared capacity to supply evidence about who received, perceived,
acknowledged, or interacted with a delivery. A capability declaration only — it is never itself an
assurance level, a confirmation, or an Identity Assertion; evidence it supplies is consumed through
the existing **Required Confirmation Strength** (**DL-40**) and Identity confidence machinery
(**DL-38**, **DL-39**), never through a second scale (**DL-53**).

**Intended Audience**
The specification of who a Communication or Stewardship obligation is *for* — one of five accepted
forms: **Named Person**, **Role / Authority Class**, **Relationship-based**, **Anyone Present With
Authority**, or **Household** (**DL-71**). Distinct from **Audience Composition** (who may perceive
it) and from **Delivery Target** (which surface was selected). Never a device or surface list.
Model: [communication.md](communication.md)

**Relationship-based Audience Specification**
An Intended Audience form scoped to a specific Subject — a Person, Pet, or Asset — resolved through a
governed relationship record (for example `caretaker-of`), never through presence or identity
evidence (**DL-71**). Distinct from a bare **Role**, which is unscoped to any subject.
Model: [communication.md](communication.md)

**Audience Composition**
Who may be able to **perceive** content through a proposed Delivery Surface. A governed input to
disclosure, evaluated by Operational Trust. Distinct from **Intended Audience**, which is who the
Communication is *for*. It consumes accepted identity assertions and presence Facts, **identifies
nobody, and is never a second identity fusion**. It must retain its uncertainty.
Model: [communication.md](communication.md)

**Potential Listener**
A Person or Unknown Person who may perceive a proposed delivery. **Not** the requestor, **not**
necessarily an Authorized Recipient, and never established by an occupancy count.

**Authorized Recipient**
A subject Operational Trust permits to receive specific content on a specific surface. Being the
requestor does not make everyone present an Authorized Recipient (**P32**).

**Delivery Target**
The surface, device, application, Room, or endpoint selected for a Delivery Attempt. **A surface is
not private merely because it is a phone.**

**Announcement**
A Delivery made **audibly to a shared surface**. It is a delivery outcome, never an object, and is
the primary target of **P32**.

**Indication**
A content-free Delivery asserting only that something is outstanding. It discloses nothing, and is
the required degradation where content may not be delivered.

**Urgency**
What a Communication is entitled to interrupt. An **entitlement granted by Operational Trust**, never
a category and never a property the originator asserts.

**Category**
What a Communication is about. Proposed by the originator. Orthogonal to Urgency; the two axes must
never be merged.

**Household Inbox**
A **projection** over outstanding Communications, assembled on demand and filtered by the viewer's
authority at read time. It is not a persisted object and no responsibility owns it.

**Delivery retry**
Repeating delivery to the **same** audience. A Concierge concern. It is never called escalation.

**Escalation**
Changing the **audience** to a more authoritative or accountable person. Stewardship owns the ladder
(**OD-22**); Operational Trust owns the authority; Concierge executes. **There is one escalation
ladder.**

**Advisory**
A **Stewardship judgement** about what could be improved, distinct from an Alert, which indicates
that something is wrong. See [../patterns/advisory-patterns.md](../patterns/advisory-patterns.md).
Advisory is **not** a Communication category; a Communication conveying an advisory carries the
**stewardship** category.

**Superseded terms**

| Old term | Canonical mapping |
|---|---|
| Notification | **Communication**, where the household interaction is meant; **Delivery** or **Delivery Attempt**, where the act of conveying is meant. *Notification* is retained only as Home Assistant platform vocabulary and must not be used as an HTBW domain term. |
| Message | **Communication**. *Message* is retained only for external provider content where the provider is the system of record. |
| Push, Toast, Banner, Ring, Indicator | Not domain terms. They are Home Assistant or device presentation concerns. See [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md). |
| Completed (as a Communication state) | Ambiguous. Use **Resolved by origin** where the underlying condition cleared, or **Acknowledged** where an identified person acknowledged it. |
| Follow-Me Communication | Not a kind of Communication. A Communication has no location. Use a **new Delivery Attempt** on a newly appropriate surface. |

Scope of the *Notification* and *Message* supersessions in the **DL-12** sense is open decision
**OD-58**.

---

## Autonomy

**Explicit**
The home acts only after direct human instruction.

**Assisted**
The home may suggest or ask for confirmation.

**Autonomous**
The home may act without asking when all required facts, permissions, confidence thresholds, and
policies are satisfied.

**Reasoning Provider**
An external or local model consulted to improve wording, summarisation, or presentation. **A
reasoning provider owns nothing**: not facts, not authority, not the reasoning of record. Its output
never silently becomes a Fact, and its recommendation never silently becomes an authorised action.
Strategy is **OD-67**.

---

## Trust

**Operational Trust**
The responsibility that answers *what is allowed?*
Contract: [../contracts/operational-trust-contract.md](../contracts/operational-trust-contract.md)

**Human Trust**
The **outcome** of understandable, consistent, respectful, and reliable behavior. Human Trust is not
a layer and is never implemented directly.

**Stewardship**
The responsibility that answers *what matters, and what must be cared for?*

**Continuity**
The responsibility that answers *what should be remembered, restored, resumed, or transferred?*

**Concierge**
The responsibility that answers *what should happen now?*

**Identity**
The responsibility that answers *who do we believe this is?*

**Truth**
The responsibility that answers *what is actually true now?*

**Foundation**
The responsibility that answers *what exists, and how do we describe it?*

---

## Products versus responsibilities

Several names in this repository refer to **repositories and released products**, not to HTBW Core
responsibilities. The distinction matters, because the same word appears in both senses.

| Name | As a product/repository | As an HTBW Core boundary |
|---|---|---|
| **Voice Identity** | A real, separately released Home Assistant integration. It remains a valid repository, deployment unit, and governance subject for cross-repo work. | **Superseded.** There is no "Voice Identity" layer in HTBW Core. The responsibility is **Identity**, and voice is one evidence source among many. |
| **Asset Intelligence** | A real, separately released Home Assistant integration. | **Not a layer.** Foundation owns the descriptive asset model; Stewardship owns obligations. Asset Intelligence may act as an optional evidence source (OD-20). |
| **Concierge** | A real, separately released Home Assistant integration. | Also a genuine HTBW Core responsibility — *what should happen now?* |

Where an operational, cross-repo, or release-governance document names Voice Identity or Asset
Intelligence as an ownership domain, it is referring to the **repository**, not to an HTBW Core layer.
That usage is legitimate and is not a contradiction.

See [../architecture/framework.md](../architecture/framework.md) and
[../architecture/greenfield-mandate.md](../architecture/greenfield-mandate.md).

---

## Document status

**Superseded**
A document or section that is retained as architectural evidence but is no longer authority. It must
name its canonical replacement. See
[../governance/document-lifecycle.md](../governance/document-lifecycle.md).

---

## Related documents

- [../architecture/north-star.md](../architecture/north-star.md)
- [../architecture/framework.md](../architecture/framework.md)
- [../architecture/principles.md](../architecture/principles.md)
- [../governance/document-register.md](../governance/document-register.md)
