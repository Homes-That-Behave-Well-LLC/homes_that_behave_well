# Person and Identity Model

> **Document status: Canonical model.**
> Terminology: [glossary.md](glossary.md). Owning responsibility: **Identity** (Person definition is
> Foundation).
> Contract: [../contracts/identity-contract.md](../contracts/identity-contract.md)

---

## Purpose

Identity answers *who do we believe this is?* — with confidence, with attribution, and without
pretending to be certain.

**Voice Identity is superseded as a product boundary inside HTBW Core.** Voice is one
identity-evidence source among many.

---

## Person

A Person is a Foundation object. Person carries:

- Canonical identity within the Home
- Roles in the Home and in specific Rooms
- Relationships (caretaker of, owner of, assigned devices)
- Consent records
- Associations to identity-evidence sources
- References to person-scoped preferences held by Continuity
- References to person-scoped authority held by Operational Trust

A Person is **not** the same object as a Home Assistant `person` entity, which is one possible
backing primitive.

**Pet** is a separate Foundation object with its own obligations and relevance to Truth and safety.
A Pet is not a Person.

### Person extends the native Person; it never replaces it

Governed by **DL-31** and
[../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md).

Where a native Home Assistant Person exists, HTBW **references it** and extends it. **A second Person
record is never created.** Home Assistant remains authoritative for the native person's name, picture,
its associated `device_tracker` entities, and its optional association with a user account. A rename
or picture change therefore needs **no synchronisation**, because nothing was copied.

Whether, and how, HTBW helps a resident create a native Person when none yet exists — as distinct from
referencing one that already exists — is **OD-91**. Native Person creation by HTBW itself is verified
unsupported by current Home Assistant developer documentation; see
[../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md).

HTBW retains only what the native object does not hold, and **each extension keeps its own owner**:

| Extension | Owner |
|---|---|
| Roles, relationships, consent records | **Foundation** |
| Identity-evidence associations and assertions | **Identity** |
| Person-scoped preferences and continuity | **Continuity** |
| Person-scoped authority and disclosure policy | **Operational Trust** |
| Obligations and accountability | **Stewardship** |
| Delegated Access Grants held over another Person's, Asset's, or Pet's Stewardship content (**DL-57**) | **Stewardship** (grant record and lifecycle); Foundation types `caretaker-of`/`owner-of` unchanged |
| Person Environmental Requirements — minimum/maximum/range per **DL-60** Environmental Purpose (**DL-61**) | **Foundation** holds the declared requirement, coordinated through Person Setup; **Stewardship** evaluates it against current Room Environment Facts |
| Mailbox, calendar, and other external-service references | Referenced through the responsibility that governs their use; **the underlying configuration is never copied** |
| Person-scoped Vocabulary for a Person-owned capability (**DL-69**) — for example calling a configured mailbox "Mail" or "Inbox" | **Foundation** (Vocabulary's owning model), **coordinated through Person Setup**; no new responsibility. Never disclosed to another Person without authorization; an Unknown Person receives no Person-scoped mapping (**DL-33**) |

**No extension list is a single record**, and this rule decides nothing about how identity evidence is
weighted or how confidence thresholds are set — those are **DL-38** and **DL-39**.

### "Person Extension" is a collective name, not a new object (DL-71)

**Person Extension** is the household-facing, collective name for the totality of the distributed
extensions above — it changes no ownership and creates no unified store. Person Setup is the shared
configuration **experience** that lets a household configure roles/relationships/consent,
identity-evidence associations, preferences, authority, obligations, and Vocabulary in one place,
while each piece remains owned and persisted exactly as the table above states.

### Guest fallback Person Extension

**A household may designate exactly one existing, deliberately configured Person as the default
consulted when Identity yields Unknown Person.** This is ordinarily a **Known Non-Resident Person**
(a household-created placeholder such as "Guest"), but may be any configured Person the household
designates. When Identity's own state is `unknown`, Concierge and Operational Trust may read the
designated Person's own distributed extensions — permissions, Vocabulary, preferences — as
interaction defaults.

> **This never creates an Identity Assertion binding Unknown Person to the designated fallback.**
> Unknown Person remains exactly what **DL-33** already states — momentary, expiring with the
> assertion, carrying no Person reference — in every record, including the Decision Trace. Reading a
> configured default is not identifying anyone.

The designated fallback's Person Extension **may hold resources, Vocabulary, permissions, and
relationships if the household deliberately configures them** — none of that is prohibited merely
because it serves as the fallback. Where no fallback is designated, existing **DL-33**
household-neutral treatment applies unchanged.

**Recognition does not imply authority.** A Person who is fully identified and remembered (a
consented voiceprint, a known Identity Assertion) may still be configured with guest-level
permissions and interactions. This requires no new mechanism: **DL-36**/**DL-39** already hold access
and presentation independent of identity confidence — being recognized authorizes nothing beyond what
that Person's own Operational-Trust-owned authority is configured to permit.

### Copy Settings From Person is setup-only (DL-71)

A setup-time convenience **may** copy, from one Person's configuration into another's:

- Permissions and allowed interactions (Operational Trust)
- Person Vocabulary (Room Configuration/Person Setup, **DL-69**, **DL-70**)
- Preferences and presentation defaults (Continuity)

It **must never** copy: mail accounts, calendars, shopping lists, voiceprints, phones, presence
devices, email addresses, delivery devices, Person-specific services, relationships, caretaker
assignments, Asset ownership, consent records, historical activity, identity evidence, or any other
Person-bound resource.

The copied values are persisted **directly and independently** into the destination Person's own
distributed extensions. **No synchronization and no runtime inheritance exist**: runtime reads only
the destination Person's own configured values, never the source Person's. A later "Reset copied
settings from Person" performs a new explicit copy — it is not a resumed link.

**This creates no Role.** The existing **Role** concept (glossary.md) — a named position such as
resident, owner, child, guest, or service provider, used by Operational Trust to derive authority — is
unchanged and unextended by this convenience. Any informal household label for a copy-settings
pattern ("like David's settings") is setup metadata only, never a runtime authorization construct.

Identity may consume:

- Voice matching
- BLE devices
- Assigned phones
- Assigned watches
- Assigned tablets
- Home Assistant companion-app signals
- Presence trackers
- Wi-Fi associations
- Room-transition evidence
- Vehicle associations
- Future identity sources
- Explicit household enrollment

No single source is privileged by the architecture. A household may weight them by policy — **per
Person and per evidence source**, as *Identity Evidence Associations* below records.

**Tag scans, bounded.** A tag scan supplies a tag identifier, a tag name, and the scanning device. It
therefore identifies a **tagged object and an interaction with it**. It does not identify a person:
anyone may scan a tag.

| Rule | Statement |
|---|---|
| A scan alone is not identity evidence about a person | It is evidence that an object was scanned |
| Where a household governs it, a scan may contribute **low-confidence** evidence only | Subject to the Fusion Policy under **DL-38**, and the Operational Trust requirements under **DL-39** |
| **A tag scan is never independently an Identity Assertion** | Consistent with **DL-06**: a detection is not an identification |

---

## What Identity owns

- Person identity profile
- Associations between a person and identity-evidence sources
- Voice profile references
- Assigned-device relationships used for identity
- Candidate-person assertions
- Identity confidence
- Identity evidence attribution
- Enrollment, revocation, and identity diagnostics
- Privacy treatment of identity evidence

---

## Participation is optional, and participation requires consent

> **No person is required to participate in any identity-evidence source.**

Every evidence class Identity may consume is **opt-in**, and consent is the gate that decides whether
it exists as evidence at all.

| Participation class | Requires consent | Effect of declining |
|---|---|---|
| **Voice identity evidence** | **Yes.** Voice identity evidence is available **only for a consenting, enrolled participant** | No voice-derived candidate is nominated for that person, and their voice is not matched |
| **Wearable evidence** | **Yes** | The wearable family contributes nothing for that person |
| **Device or phone evidence** | **Yes** | The device family contributes nothing for that person |
| **Preference participation** — person-scoped preferences, history, and learning | **Yes** | The home behaves household-neutrally for that person |

**Declining is neutral, and the architecture is built to keep it neutral.** Fewer eligible families
produce a **lower ceiling** under **F1**, never a penalty and never a denominator effect under **F7**.
*Missing evidence is not contradicting evidence.* A person who has not consented **must still be able
to use the home in a guest-safe way**, and **enrollment is an explicit act, never a silent by-product
of ordinary use**.

Consent is **scoped** — consenting to voice identity is not consent to calendar access — and
**revocable at any time**, removing the derived profile and its associations rather than merely their
use.

### Consent governs the evidence that exists at all

```text
CONSENT             what the household and the person have permitted
    ↓
AVAILABLE EVIDENCE  the eligible evidence set — what may be used at all
    ↓
IDENTITY            fusion over that set, producing a purpose-specific assertion
    ↓
OPERATIONAL TRUST   sufficiency, audience, disclosure, and the outcome
```

**Consent gates eligibility, not weight.** Evidence lacking valid consent is **excluded before
weighting** at stage 1 of the qualification order — the assertion is produced as though the source did
not exist. **A withdrawn consent is not a reduced weight.**

**Consent determines what evidence may be used. Operational Trust ensures those choices are applied
consistently and respectfully.** See [operational-trust.md](operational-trust.md).

---

## Consent (DL-56)

Resolves **OD-06**. Full acceptance record is **DL-56** in
[decision-ledger.md](../governance/decision-ledger.md); this section is the canonical model.

### Observation is not Person Association

**Consent is required for person association and person-scoped participation, not for environmental
observation by itself.** The home may observe environmental facts according to applicable privacy,
camera, retention, and household policy without any person-association consent: a person visible in
camera video, an image containing a person, motion, occupancy, a BLE device's presence, a phone or
watch signal, an unknown device moving between Rooms, an interaction from an unidentified person, or
any other non-person-scoped event.

Consent is required only where the home seeks to **associate** an observation with a named Person —
binding a voiceprint, a BLE device, a phone, a watch, or a correlated observation to a Person; building
or using a person-scoped identity profile; performing person-scoped learning, personalization, or
Stewardship; or using a relationship to identify that Person in a future interaction.

> **Observation is not Person Association. Co-presence is not Person Association. Correlation
> capability is not authorization.** That the home *could* correlate a camera image, a BLE device, a
> phone, a watch, a voice, or an interaction into one identity does not mean it may — repeated
> co-presence is never itself sufficient to bypass consent.

### Consent scope: participation-based at the household surface, precise underneath

The household-facing experience is **participation-based and contextual** — a person consents by
**knowingly establishing a person-associated participation relationship**, not by reasoning about
evidence sources, assertion purposes, or Fusion Policy. The canonical record underneath is precise
enough for eligibility, explainability, withdrawal, and retention. **These are one model presented at
two levels of detail, never two inconsistent models.**

Participation-consent actions include, at minimum:

| Action | What is consented to |
|---|---|
| **Voice enrollment** | Creation of a voiceprint; its association with the person; its use as eligible identity evidence; use only for the disclosed identity purpose |
| **BLE / phone / watch association** | Association of the specified device with the person; use of that association as eligible presence or identity evidence; tracking the device per disclosed policy |
| **Authenticated application login** | Association between the authenticated session and the person; eligibility to attribute supported activity from that session to the person; use only within the disclosed application and capability scope |
| **Contextual continuity ("remember me")** | See *Contextual continuity consent*, below |

**Adding a data source is not identity-association consent by default.** Configuring a person-scoped
email account, calendar, news source, music preference, information source, or general-question/LLM
capability is **capability authorization**, **data-source authorization**, **preference
configuration**, or **access configuration** — never an unrestricted grant, and never assumed to imply
identity-evidence consent or the reverse. Each configuration action states what it authorizes; Person
Setup presents them coherently without collapsing their distinctions.

### The canonical consent record

Foundation holds one canonical consent record per granted or declined participation, capable of
representing:

- Person or participant reference
- Participation type (voice, BLE/phone/watch, authenticated app, contextual continuity, or a future
  class)
- Evidence source or association covered
- Capability or purpose enabled
- Data class involved, where required
- **Consent state**: not given, declined, granted, withdrawn (see *State distinctions*, below)
- Consent scope
- Granted or declined time, and effective time
- Withdrawal time, where applicable
- **Self-consent or proxy-consent**, and the recorded actor (see below)
- Authority basis for proxy consent, where applicable (owned by **DL-57**, referenced not duplicated)
- Interaction or surface used
- Deletion effects and retention-floor effects
- Current eligibility consequence
- Historical-explainability reference

This is the same record `person-and-identity.md`'s Person object already names under *Consent
records*; this section defines its required shape. **No second, inconsistent consent model is
created.**

### Self-consent and proxy consent

Both are supported. **A proxy action never masquerades as self-consent.** The interface and the record
state plainly that the signed-in person is acting **as a proxy** for another person's consent, and
capture: the person for whom consent is recorded; the signed-in actor who recorded it; the self/proxy
distinction; time; scope; the consent-bearing interaction; and any disclosed limitation. The signed-in
identity supplies the audit actor.

**OD-06 owns**: that self- and proxy-consent paths exist; that proxy consent must be explicit and
never silently assumed; that the acting person must be authenticated or otherwise authoritatively
recorded; that an audit trail is required; the consent scope granted; the consent lifecycle
consequences; and that a proxy action never masquerades as self-consent.

**OD-76 owned, now resolved as DL-57** (`stewardship.md`, *Delegated Stewardship Authority*): who
qualifies as an authorized proxy — a competent adult retains self-authority and may explicitly
delegate; a minor or a person unable to act independently may be represented by an authenticated
administrator acting as proxy; **a native Home Assistant administrator flag is never itself care,
guardianship, or proxy authority**; formal legal qualification (guardianship, power of attorney, or
equivalent) is explicitly outside HTBW's scope — HTBW records that a proxy grant was established and
by whom, and asserts no legal sufficiency. **Proxy-established identity participation never
manufactures evidence that does not exist**: an administrator may facilitate voice enrollment for a
subject, but if the subject cannot provide usable samples, no voiceprint is created and Voice Identity
remains unavailable for that person (**DL-41**) — other consented evidence remains usable, and Voice
Identity is never required for participation. A device (phone, watch, BLE tag) an administrator
associates with a proxy subject remains identity evidence **only for that subject**, never for the
administrator.

### Person Setup: the primary consent experience

**Person Setup (Person Management) is the primary experience for consent capture, review, and
withdrawal.** It coordinates with, and never duplicates, native Home Assistant Person maintenance:
Home Assistant remains authoritative for the native Person's name, picture, and `device_tracker`/user
association (**DL-31**); Person Setup extends it with governed HTBW participation configuration only.
Its present location inside the Concierge implementation is **rank-4 evidence, not final ownership** —
the architectural home is: **Foundation** holds the consent record; **Identity** owns the consent
lifecycle; **Operational Trust** decides whether a capability may proceed given consent state;
**Concierge** presents the interaction and facilitates capture; **Stewardship** owns delegated
authority (proxy qualification and the Delegated Access Grant) per **DL-57**. **No Consent
responsibility is created.**

**Person Setup is the coordination and management surface for every accepted person-scoped
configuration named in this document** — identity participation, consent records, Identity Evidence
Associations, Delegated Access Grants (**DL-57**), person-scoped preferences (Continuity),
person-scoped authority references (Operational Trust), and non-resident participant records (a
**Known Non-Resident Person**, `glossary.md`) — **coordinating, never owning**. Each remains governed
exactly where this document and `stewardship.md` already assign it; Person Setup introduces no new
responsibility, no new object type, and no new authority model by presenting them together.

Each consent-bearing control states **what association or participation it creates**, never a general
"I consent to Identity" statement. Conceptual examples (illustrative wording, not mandated strings):
*"Participate in Voice Identity"* discloses voiceprint creation, association, identification use, and
retention/deletion behaviour; a device-association action discloses which device, which person, what
the association is used for, and how to remove it; an authenticated-app login states its scope and
does not overstate unrelated data access.

#### Home Assistant First review (DL-18)

| Native mechanism | Verified capability | Limitation | DL-18 disposition |
|---|---|---|---|
| Config flow / options flow | Documented, general-purpose configuration surfaces already used throughout HTBW's Person Setup extensions | No native consent model exists on top of them | **Sufficient as the native-feeling extension surface** — carries required consent checkboxes, disclosures, and remove-association actions |
| Native Person entity, `user_id` linkage | Verified; supplies the authenticated actor for a proxy-consent audit trail | Administrator flag is binary; carries no household role or care-authority model | Sufficient for **recording the actor**; insufficient, and not used, for **authorizing** proxy scope (governed by **DL-57**) |
| Repairs | Verified administrator-correctable-defect surface | Not a consent surface — a Repairs issue has no audience, no consent semantics | **Not used for consent capture**; may report a broken consent-dependent configuration |
| Native conversational confirmation | Exists for other purposes (e.g. Assist confirmations) | No documented native consent-grant semantics | Used **only** for the contextual continuity pattern below, where the disclosed scope is spoken plainly, never for a silent or implicit grant |

**Burden of proof discharged**: no bespoke UI standard is proposed. Config/options-flow-based Person
Setup, extended with explicit per-action disclosure, is the native-feeling mechanism; DL-18 is
satisfied without inventing a parallel consent UI.

### Contextual continuity consent ("would you like me to remember you")

A secondary, contextual Person Setup path exists for an unidentified or guest participant who
interacts with the home without enrollment (asking about art, asking general questions, participating
in a Room interaction). The home may ask a disclosed equivalent of *"Would you like me to remember
you?"*. This remains **Person Setup** — contextual and conversational rather than the comprehensive
household-member flow — not a new experience or responsibility.

- **Declined or no consent**: no durable Person profile is created; no observation is attached to a
  named identity; no person-scoped learning occurs (**DL-33**); the unidentified-person policy
  continues to apply.
- **Consented**: only the minimum record the consent authorizes is created — typically a lightweight
  continuity record carrying the supplied name, recognised under existing **frequent-guest /
  continuity vocabulary**. A voice profile or device association is created **only** if separately
  disclosed and separately consented. **No automatic grant** of email, calendar, household
  administration, private data, or resident-level capability follows from this path. The record is
  reviewable and withdrawable exactly as full Person Setup's is, and may later be expanded into full
  Person Setup.
- **No durable synthetic "Guest Person" is ever created** merely because a guest was observed — this
  restates **DL-33** for the contextual path specifically.

### Withdrawal and deletion

Withdrawal is **explicit and capability-specific**.

**Voice Identity.** Unchecking or otherwise withdrawing Voice Identity participation makes voice
evidence **ineligible immediately**, excluded before weighting under **DL-38** stage 1 — never
down-weighted. Voiceprints, derived identity profiles, and temporary enrollment samples are **deleted**
under **DL-43**. Dependent capabilities become **unavailable** and name the missing dependency under
**DL-41**. The person is told what was deleted, what record survives, and which capabilities are now
unavailable.

**BLE / phone / watch.** Removing the device from the person withdraws consent for that association.
The home may continue observing the device as an **unidentified device** under applicable policy;
future observations are **never** attributed to the former person; dependent capabilities become
unavailable if no other eligible evidence satisfies them; no hidden association survives.

**Authenticated app.** Logging out or removing the association ends the eligibility it established for
attributing session activity to the person; it does not, by itself, alter separately configured
data-source or preference authorizations, which withdraw on their own terms.

### Consent duration and renewal

**Consent remains effective until explicitly withdrawn; it does not silently expire.** Optional
periodic reaffirmation may be offered during a suitable interaction, but: no response is not
withdrawal; failure to interact is not withdrawal; a missed renewal prompt is not withdrawal; inactivity
is not withdrawal. A documented reaffirmation is recorded as a **reaffirmation** event, distinct from
**initial consent**, a **scope change**, and a **withdrawal** — the four are never collapsed. Renewal
prompting follows existing indication and communication governance and never becomes indefinite
repeated prompting.

### DL-43 versus DL-47: what is deleted, what survives

The tension is resolved by keeping two records **separate in kind**, never merged:

| Deleted (DL-43) | Retained (DL-47 structural floor) |
|---|---|
| Voiceprints | That consent was granted, its scope, and when it became effective |
| Derived identity profiles | Whether it was self- or proxy-consent, and who recorded proxy consent |
| Temporary enrollment samples | When it was withdrawn |
| Other consent-dependent identity material named by canonical policy | What deletion was triggered, and that dependent eligibility ended |

**The retained lifecycle record is never sufficient to reconstruct deleted biometric or derived
identity material** — it proves that consent existed and ended, not what the evidence was. The
Decision Trace is never a replacement identity profile: it references the lifecycle record, and it
never stores a biometric embedding, raw payload, or reconstructable derivation.

### Historical explainability after a consent change

A consent change **never rewrites** a historical decision. A Decision Trace produced while consent was
active may explain that the person-associated evidence was eligible **at that time**, identifying the
person only to the extent the retention and deletion architecture permits, and must never imply that
consent remains active now. After withdrawal, new observations are **never** attributed to the person
through the withdrawn association: the honest explanation states that an unassociated device was
observed, an unidentified person interacted, or a person with observed devices issued a command — never
the withdrawn person's name via that evidence.

### State distinctions

Resident-facing explainability names the actual reason and never collapses these into a generic
"unavailable":

| State | Meaning |
|---|---|
| **Consent not given** | The applicable participation consent was never granted; the capability is unavailable because eligibility is absent |
| **Consent declined** | The person explicitly declined an offered participation |
| **Consent withdrawn** | Consent previously existed and was explicitly ended; deletion and eligibility consequences occurred |
| **Permission denied** | Consent may exist, but a distinct authorization or policy denies the requested action |
| **Dependency missing** | A required technical or architectural dependency is unavailable (**DL-41**) |
| **Unknown** | The consent state or required evidence cannot be resolved; **never** silently treated as granted or withdrawn |

Illustrative phrasing (not mandated strings): *"Voice personalization is unavailable because Voice
Identity consent was not granted."* / *"...because Voice Identity consent was withdrawn."* / *"Calendar
access is denied by the configured access policy."* / *"Voice Identity is unavailable because the
required integration is missing."*

### Retrospective Person Association is prohibited (DL-108)

Resolves **OD-89** in full. **An observation that was unassociated when it occurred may never later
be converted into a Person Association through retrospective correlation** — not through biometric
evidence, not through non-biometric evidence (device, BLE, platform-user, or another lawfully existing
identity signal), not through timing or location alone, and not through any future evidence class a
later accepted decision might introduce. The prohibition is **evidence-class agnostic** and
**permanent unless a future, separately accepted governance decision explicitly reopens it** — it is
never relaxed by Operational Trust policy, a provider's new capability, or an interpretation of this
section.

**An unassociated observation is a legitimate governed state, not incomplete identity awaiting later
resolution.** What the home knew at the time of observation remains what it knew at that time; later
evidence never grants retroactive permission to rewrite that historical state (**DL-35**'s own "no
retroactive permission" rule, applied here without qualification).

**This does not prohibit, and does not change, any of the following:**

- **Historical Reconstruction** of existing governed records under its own governance
  (`temporal-record.md`).
- **Bounded Unknown Actor Reference correlation** within one reconstruction (**DL-35**, **DL-74**) —
  it still **identifies nobody**, and this decision makes that boundary durable against retrospective
  fusion rather than narrowing it.
- **Disclosure of an already-existing, lawful Person Association** — an observation that already
  carried an association when it was recorded remains governed by its own existing rules; this
  decision concerns only an observation that carried **no** association at the time.
- An **Evidence Package** or other authorized export of records that already exist.

**Existing lawful, non-biometric evidence may not be retrospectively fused onto a historical Unknown
Actor Reference merely because it could be.** A resident's phone may already be lawfully associated
with them, and Truth may already hold a Location Fact placing that device near an event — but HTBW
must never assert that the device's owner was the actor in a separately recorded Unknown Actor
Reference by fusing those two already-existing records after the fact. **Technical capability never
creates retrospective authority** (restating **DL-56**'s "correlation capability is never itself
authorization" for the retrospective case specifically).

**A later voluntary statement is not an Identity Assertion, and must never be represented as one.**
Tested directly against **DL-64**: Identity Assertion production is bound to current-evidence
evaluation at the moment of production, and none of the six accepted Assertion Purposes (Speaker
Attribution, Room Presence, Household Presence, Interaction Initiator, Authenticated Session Identity,
Endpoint Context) contemplates a backdated result. Explicit Confirmation, as an evidence source, is
"the confirmed claim, on the confirmed channel, **for a bounded time**" — a live, current-interaction
mechanism, not one that can be invoked to retroactively date an assertion to a past moment. **No such
mechanism is created by this decision.** Where a Person later, voluntarily states that they were
involved in a past bounded event, the only accepted representation is an **ordinary Domain Event**
(`temporal-record.md`) — dated at its own actual occurrence, attributed to the speaking Person through
ordinary, current Identity/Behaviour Source Attribution evidence (**DL-73**) exactly as any other
present-moment statement is, and carrying a Governed Reference to the historical Unknown Actor
Reference it concerns. This Domain Event **never** associates the original observation, **never**
feeds Identity Fusion as though it were evidence available at the original time, and **never**
expands beyond what the statement actually claims — a confirmation of one bounded event never implies
the same Person across every other observation in a wider Unknown Actor Reference, and a confirmation
of device ownership never implies the Person was the actor in every observation involving that
device. A later correction or retraction is its own further Domain Event, under the existing
Change-Record correction discipline (**DL-26**, **DL-27**); conflicting statements from two different
people are each recorded as what they are — competing, unresolved claims — never adjudicated by HTBW
into a single winner.

**No new collection, no backfill, no retroactive retention, no resurrection of deleted records.** OD-89
authorizes no new retrospective observation and no prospective tracking; a request naming a deleted or
never-retained record is answered **unavailable**, never reconstructed, inferred, or treated as an
adverse inference; existing records follow their own governing retention class unchanged, and a
Preservation Hold, where validly placed under **OD-39**'s own governance, may protect only records
that still exist — it can never resurrect a deleted one or itself authorize retrospective Person
Association. **OD-35, OD-36, and OD-39 remain open and are not decided or pre-empted by this section.**

**Household incident review and an external legal request are both access/disclosure paths only, kept
symmetric, never a derivation path.** Each may be separately authorized to access, preserve, or
disclose records that already lawfully exist, exactly as each record's own governance already permits
— neither authorizes retrospective Person Association, and neither implies the other. **HTBW does not
determine legal sufficiency** and makes no claim of court admissibility, chain-of-custody sufficiency,
forensic certification, or regulatory-compliance (`authority-order.md`'s existing non-claim, now this
decision's own operative position, not merely an inherited disclaimer).

**No Legal, Investigation, or Forensic responsibility is created.** Operational Trust continues to
evaluate authority and disclosure appropriateness for operations it is permitted to evaluate; it has
no authority to convert a prohibited operation into a permitted one, through an exception flag,
elevated policy, or any other mechanism.

---

## The identity assertion

Identity's output is an assertion, not a fact about the world.

```
candidate_person: Tom
purpose:          current speaker in the Den
confidence:       high
evidence:         voice + BLE + assigned phone
families:         voice biometric + wearable proximity
freshness:        2.1s
reason_code:      known
```

Assertion states that must be representable:

| State | Meaning |
|---|---|
| known | A candidate person is asserted with sufficient confidence |
| ambiguous | Two or more candidates are plausible; all are reported |
| unknown | No candidate can be asserted |
| unavailable | Identity could not be evaluated; a dependency failed |
| not required | The interaction does not require identity |

**Identity is advisory context. Identity is not authentication and not authorization.**

### Every assertion states its purpose

**There is no general-purpose identity score.** An assertion answers **one** question about **one**
candidate, and the question is part of the assertion.

| Assertion purpose | The question | Typical primary evidence |
|---|---|---|
| Speaker Attribution | Who most likely spoke? | Voice match, within its capture context |
| Room Presence | Who is likely physically present in this Room? | Person-associated proximity, corroborated |
| Household Presence | Who is likely home, regardless of Room? | Native Person and device-tracker state |
| Interaction Initiator | Who initiated this digital action? | The interaction's own attribution |
| Authenticated Session Identity | Which authenticated account initiated the request? | The authenticated user, where the platform supplies one |
| Endpoint Context | Through which managed endpoint did this arrive? | The capture or request endpoint |

**These must not be collapsed into one number.** One Person may simultaneously be high confidence for
Household Presence, high for Room Presence, medium as the current speaker, confirmed as an
authenticated account, and **unknown** as the physical holder of the authenticated device. **The
architecture preserves those differences rather than averaging them away.**

Endpoint Context identifies a **thing**, not a person. It is recorded as context, and produces no
person assertion on its own.

> **"Current Engager" is a rejected term and must not be introduced.** *Who is engaging* is answered by
> whichever of the six purposes above applies — Speaker Attribution for a spoken request, Interaction
> Initiator for a digital action, Authenticated Session Identity where the platform supplies a user, and
> Endpoint Context for the surface itself. **A single fused "engager" result would be exactly the
> general-purpose identity score this section prohibits**, would break the **F1** purpose ceilings, and
> would make the kiosk safeguard unimplementable — because that safeguard *is* the purpose separation.
> The Truth-side counterpart is the **Engagement Fact**, which states that an interaction is occurring
> and **never who is engaging**. See [glossary.md](glossary.md) and [truth.md](truth.md).

### None of the six purposes requires a fixed validity window (DL-64)

Each purpose is re-evaluated identically — fresh, on demand, from current eligible evidence — and
carries no purpose-specific duration. Purpose-specific behavior lives entirely in **DL-38**'s existing
ceilings and freshness rules, never in a separate timer.

| Purpose | Historical relevance | Applicability requirement |
|---|---|---|
| Speaker Attribution | Permanently correct record of who most likely spoke for that one utterance | Re-evaluated per utterance; never reused for a later utterance, even by the same apparent speaker |
| Room Presence | Permanently correct record of who was likely present at that moment | Re-evaluated whenever a current Room-Presence determination is needed; bounded by the Room's own occupancy (**DL-64** cross-purpose eligibility, above) |
| Household Presence | Permanently correct record of who was likely home at that moment | Re-evaluated from current native Person/device-tracker state; no separate window |
| Interaction Initiator | Permanently correct record of who initiated that digital action | Bound to the specific action; never carried into a later, separate action |
| Authenticated Session Identity | Permanently correct record of which account initiated that request | Bound to the platform's own authenticated-session semantics, not an Identity-invented duration |
| Endpoint Context | Permanently correct record of which endpoint the request arrived through | Re-evaluated per interaction; identifies a thing, never a person, so applicability is not a person-eligibility question at all |

---

## Unknown Person

> **Unknown is a valid identity outcome, not a failure of one.**

Identity may establish with high confidence that **a human participant exists** while being unable to
associate that participant with any known Person. That outcome is the existing `unknown` state, and
it is a **valid assertion**, not a failure.

### Confidence is bounded by the evidence that supports it

> **The home should not be more confident than the evidence supports.**

This is not a tuning preference. It is the property every rule of the Identity Fusion Function exists
to guarantee, and it is what makes `unknown` a correct answer rather than a shortfall.

| Rule | How it bounds confidence |
|---|---|
| **F1 — purpose ceiling** | A family never contributes above the highest level it can reach **for that purpose**, and an assertion never exceeds the highest ceiling among the families actually supporting it |
| **F2 — one contribution per family** | Correlated observations from one device **never become a second confirmation** |
| **F3 — non-increasing qualification** | Every qualification stage may **lower or hold**, never raise |
| **F5 — corroboration requirement** | A source requiring corroboration **anchors only to a reduced ceiling** |
| **F6 — bounded reduction** | Contradiction reduces, forces `ambiguous`, or eliminates a candidate — and is **never averaged away** |
| **F7 — absence is neutral** | Fewer sources produce a **lower ceiling**, never a penalty |
| **F8 — separation** | `known` requires the leading candidate to **exceed the next by a governed margin**, or the result is `ambiguous` |
| Outcome order, row 6 | A leading candidate below the purpose minimum yields **`unknown`**. **A weak candidate is never forced** |

**Identity must not overstate confidence**, and four temptations are explicitly closed:

- **Never raise a result to be useful.** A consumer needing more confidence than the evidence supports
  is answered with the honest lower band, `ambiguous`, or `unknown` — and **Operational Trust decides
  what to do about it**, including offering confirmation.
- **Never present a provider match value as the home's own belief.** It is evidence, retained as
  reported.
- **Never present a governed belief as a calibrated probability**, a likelihood, or measured accuracy.
- **Never treat `Very High` as certainty.** It is the top of a belief scale, and a belief scale has a
  top.

> **A resident must be able to hear *"I was not confident enough that it was you"* as a correct,
> complete answer** — not an error, not a degraded mode, and not something to retry away.

```
purpose:            speaker attribution in the Den
assertion_state:    unknown
candidate_person:   none
human_participant:  supported
confidence:         high
families:           voice capture
reason_code:        no_eligible_match
```

`human_participant` is the one element this outcome required. Without it the model cannot distinguish
**"a person is here and I do not know who"** from **"I have no evidence that anyone is here"** — two
situations with opposite governance consequences. It is a property of the existing assertion.
**No parallel state enumeration is introduced, and `unknown` is not subdivided.**

Confidence on such an assertion is confidence **in the stated outcome for the stated purpose**, under
**DL-39** semantics. It is not a probability that the participant is someone in particular.

### Unknown Person is not

- An error, a defect, or a degraded mode
- An unavailable Identity service
- An ambiguous choice among known candidates
- A Home Assistant Person
- A permanent or reusable guest profile
- An owner of preferences, history, or learning
- A permission grant or a role assignment
- A claim that the same individual was observed anywhere else, at any other time

### The five states, kept distinct

| State | Meaning | The mistake it prevents |
|---|---|---|
| known | A known Person is supported **for the applicable purpose** | Treating a household-presence assertion as speaker attribution |
| ambiguous | Two or more **known** candidates or interpretations remain plausible and cannot be deterministically resolved | Silently selecting the highest-scoring candidate |
| unknown | A participant or presence is supported, but **no eligible known Person can be established** | Reporting a present stranger as an absence, or as a fault |
| unavailable | The required capability or evidence source **could not evaluate** | Reporting a working system's honest negative as a failure |
| not required | The interaction does not require identity resolution | Demanding identity for a benign, Room-scoped request |

> **A provider that evaluated successfully and returned no eligible match yields `unknown`, never
> `unavailable`.** The provider worked. Recording the result as `unavailable` would misreport a
> correct negative as a fault, and would invite a retry that cannot succeed.

Unknown proximity evidence is not evidence of a known Person. Occupancy is not identity.

### An unknown evidence source is not a person

An evidence source may be observed without establishing anyone: an unassociated proximity source, an
unassociated device tracker, an unmatched voice sample, an unauthenticated browser interaction, a
managed endpoint used without human attribution, or occupancy with no identity evidence at all.

| An unknown source may contribute to | It must never independently establish |
|---|---|
| Evidence that someone may be present | A known Person |
| Corroboration of interaction context | A role, an occupation, or a relationship |
| An Unknown Person assertion | A recurring or returning individual |
| Audience uncertainty | The same actor across time or place |
| Historical reconstruction | Permission, intent, or criminality |

**Observing an unknown source creates no identity record.** It produces evidence, retained as
evidence, not a durable profile that accumulates across visits. An unassociated proximity source and
an unmatched voice observed in the same minute are **two unassociated observations**, not one person,
until governed correlation supports the association.

### No synthetic Person is created

**HTBW must never create a Home Assistant Person named *Guest*, *Visitor*, *Unknown*, *Cleaner*, or
anything similar merely to have something to attach a default policy to.** A Person object asserts
that a specific human is known to the household. Manufacturing one to carry a policy inverts the
meaning of the object, writes into a registry HTBW does not own, and makes an unidentified stranger
indistinguishable from a household member. **Unidentified people require no Person object and no
enrollment.**

A household may of course intentionally create a Person for a *specific* known non-resident. That is
a governed household act, and the resulting Person is **known** — not unknown.

### Four concepts that must not be collapsed

| Concept | What it is | Lifetime | Owner |
|---|---|---|---|
| **Known non-resident Person** | A specific, intentionally configured Person who may carry a native Person reference, consent, permissions, and governed extensions | Durable, household-managed | Foundation; Identity for evidence |
| **Unknown Person** | A purpose-specific Identity Assertion carrying no known Person reference | Momentary; expires with the assertion | Identity |
| **Unidentified-person policy subject** | The policy subject against which an Unknown Person's request is evaluated | A policy, not an entity | Operational Trust |
| **Unknown Actor Reference** | A bounded historical correlation reference grouping supported observations | Scoped to one reconstruction | Concierge, as a projection |

**None of these is a profile.** None accumulates preferences, and none grants permission. See
[operational-trust.md](operational-trust.md) and [temporal-record.md](temporal-record.md).

---

## What each evidence source establishes

**Reliability is not a property of an evidence type.** What a source can *establish*, however, is
bounded by what the source actually observes.

| Evidence source | May support | Never establishes on its own |
|---|---|---|
| Wearable proximity | Person-associated proximity; Room Presence **only where Room-level detection is genuinely grounded** | The current speaker; account identity; permission |
| Phone, tablet, or laptop proximity | Person-associated proximity; Household or Room Presence | The current speaker; that the bound Person is holding it |
| Native device tracker and native Person state | Household Presence, at the granularity the platform supplies | Room Presence; the current speaker |
| Authenticated user | Interaction Initiator; Authenticated Session Identity | Physical presence; the physical holder; the current speaker |
| Managed endpoint, including a kiosk | Endpoint Context; probable Room context; a governed channel | **Any human identity** |
| Voice match | Speaker Attribution, within the capture context | Permission; account identity; presence beyond that context |
| Room occupancy or presence sensor | That the Room is occupied; corroboration of context | **Which** Person; who spoke; who initiated |
| Explicit confirmation | The confirmed claim, on the confirmed channel, for a bounded time | Unrelated claims; future interactions; permanent certainty |
| **Pet-worn tag, collar, or other non-person tracker** | **Nothing about a person.** It is evidence about a **tagged object**, consumed by **Truth** as a Location Fact source | **Any human identity**; Room Presence for a Person; occupancy; a candidate Person |

> **A non-person tracker is not identity evidence, and it must not be routed through fusion.** A pet
> tag, an asset tag, or an unassociated beacon has no Person to bind to; Identity's candidate set
> contains **known Persons only**. Such evidence belongs to **Truth**, which may publish a Pet, Asset, or
> Device Location Fact from it. Consistent with **DL-06** — a detection is not an identification — and
> with the treatment of tag scans above. See [truth.md](truth.md).

> **A managed endpoint account is not a Person.** A kiosk, tablet, or satellite account identifies the
> endpoint or channel. **It must never silently become the identity of the human using it**, however
> convenient that would be.

**Occupancy is not identity. Authentication is not physical presence. A match value is not
permission.** These follow **DL-06**: a detection is not an identification.

---

## Identity Evidence Associations

*What Identity owns* already includes **associations between a person and identity-evidence sources**.
This section names and governs that existing concept. **It is not a new model, not a second Person
record, and not a second registry.**

**An Identity Evidence Association binds one Person to one evidence source**, and holds the
**HTBW-specific interpretation** of that source for that Person. Governed by **DL-31**: the native
object is referenced by its stable identifier, and **no native Device, Entity, Person, or tracker
property is copied**. Where Home Assistant already holds the Person-to-tracker relationship, **HTBW
consumes it and does not maintain a competing one.**

| The association carries | Notes |
|---|---|
| Person | By reference. The native Person where one exists |
| Evidence source, and its native identifier where applicable | Native Device, Entity, device tracker, user, endpoint, or voice profile reference |
| Evidence type, and evidence family | The family governs correlation — see below |
| Claim types this source may support | Bounded by *What each evidence source establishes* above |
| Configured reliability, and its provenance | Explicit household configuration, a default suggestion, or an accepted proposal |
| Freshness rule | May differ by source and by claim type |
| Applicability context | Where and when this source is meaningful at all |
| Consent requirement, and current consent state | Governs eligibility before any weighting |
| Enabled or disabled state | A resident may disable a source without deleting its history |
| Whether the source may independently support a claim, or requires corroboration | A per-claim property, not a global one |
| Known limitations | Recorded, so an explanation can be honest |
| Configuration version and date | Versioned as a governed record |

**Historical change treatment follows the shared temporal model.** Changing a reliability value today
**never rewrites an Identity Assertion made yesterday**; a Decision Trace references the exact version
that applied at the time (**P30**, **DL-27**).

### Reliability belongs to the binding, not to the device type

**The same evidence type may carry different reliability for different people, and that is the point.**

| Association | Configured reliability | Why |
|---|---|---|
| Tom's watch | High, for Tom's proximity | He wears it almost always |
| Tom's phone | Strong, but below the watch for immediate proximity | He generally carries it |
| David's phone | Lower, and **corroboration required** for anything sensitive | He frequently leaves it behind |

> **Do not write a universal rule such as *all watches are highly reliable* or *all BLE evidence has
> one weight*.** A device type may supply a **default suggestion**. The authoritative value is scoped
> to the Person-to-source binding, because it describes **a person's habits**, not a product category.

### Configured reliability is not measured accuracy

| Concept | What it is | How it may be stated |
|---|---|---|
| **Configured association reliability** | A governed household configuration expressing how strongly this source should contribute for this Person and claim | A **band**, optionally backed by a normalised contribution weight |
| **Empirical accuracy** | A measured statistical performance supported by observed outcomes and calibration | **Only where such measurement exists** |

**The canonical resident-facing representation is a band**, which is already the privacy-safe form this
model requires. A numeric value may back it as a **normalised contribution weight**, and a household
that wants to say *"Tom's watch counts for more than David's phone"* may express exactly that.

> **A configured 90 must never be presented as 90 percent measured accuracy.** It is a configured
> contribution weight. Calling it accuracy would be a claim the home cannot support. Whether the
> configuration surface offers numbers, bands, or both is a configuration-experience question, not an
> architectural one.

---

## Freshness, correlation, contradiction, and absence

### Freshness

**Configured reliability alone is never sufficient.** A source's contribution also depends on how
recently it was observed, relative to the claim being evaluated.

A wearable seen in the Room moments before the interaction may contribute strongly to Room Presence. A
phone last seen there much earlier may contribute little or nothing. **A stale occupancy observation
must never be presented as current occupancy.**

Freshness rules may vary by evidence source, evidence type, claim type, detection technology, and
household configuration. **No universal duration is prescribed here**, because none is yet justified
by accepted architecture or verified platform behaviour. Defaults are implementation mapping, and
assertion validity windows remain **OD-15**.

### Evidence families and correlation

**Multiple observations are not automatically multiple independent signals.**

Phone proximity, a Wi-Fi tracker, native Person state derived from that phone, and companion-app
location may all originate from **one physical device**. **They must not be counted as four
confirmations.** Every observation therefore carries an **evidence family** — a correlation group —
and correlated evidence is evaluated as one contribution, not summed.

Voice biometric, wearable proximity, Room occupancy, and authenticated interaction are **potentially**
more independent families. **Independence is never assumed merely because evidence arrived through
different entities.** Where independence cannot be established, evidence is treated as correlated.

### Contradiction

Evidence may **contradict** a candidate, and contradiction is **claim-specific**.

Tom's strongly bound watch observed in the Kitchen contradicts *Tom is present in the Den*. It does
**not** disprove that Tom's authenticated account initiated a remote action. **The same observation
means different things for different claims.**

Contradiction is never discarded to reach a cleaner answer. The record retains supporting evidence,
contradicting evidence, unavailable evidence, ambiguous evidence, correlated evidence, and **the final
reason for promotion, reduction, or an unresolved outcome**.

### Missing evidence

> **Missing evidence is not contradicting evidence.**

A household may own no wearables. A person may not carry a phone. Detection may fail. A Room may have
no occupancy sensor. **None of that is evidence against anybody**, and no household is penalised for
declining an optional source.

| State | Meaning |
|---|---|
| Not configured | No association exists. Neutral |
| Configured but currently unavailable | The source could not be read. Neutral, and reported |
| Configured but not observed | The source is available and reports nothing here. Weakly informative at most |
| Observed somewhere contradictory | Genuine contradicting evidence, for the claims it bears on |
| Stale | Present but too old to carry its normal weight for this claim |
| Explicitly disabled | Excluded by resident choice |
| Consent absent or withdrawn | **Ineligible.** Excluded before weighting, not down-weighted |

Identity degrades gracefully: it may still return a candidate, a lower-confidence assertion, `unknown`,
or a request for confirmation.

---

## The fusion process

**Identity performs fusion. No other responsibility does.** Truth does not fuse identity evidence,
Concierge does not, and Operational Trust does not.

> **A naïve additive calculation is prohibited.** *Voice score plus watch weight plus occupancy* is
> not a governed result. A provider match of 0.82 and a configured reliability of 0.90 **do not**
> produce 0.86, 1.72, or any other arithmetic artefact.

| Step | Action | Owner |
|---|---|---|
| 1 | Identify the claim being evaluated | Identity |
| 2 | Identify candidate Persons | Identity |
| 3 | Gather eligible evidence | Identity |
| 4 | Exclude evidence prohibited by consent or policy | Identity |
| 5 | Evaluate freshness for this claim | Identity |
| 6 | Apply the Person-to-source configured reliability | Identity |
| 7 | Group correlated evidence into families | Identity |
| 8 | Evaluate supporting evidence | Identity |
| 9 | Evaluate contradicting evidence | Identity |
| 10 | Compare competing candidates | Identity |
| 11 | Produce a confidence result | Identity |
| 12 | Preserve the complete evidence rationale | Identity |
| 13 | Apply the confidence-band semantics of **DL-39** | Identity |
| 14 | Pass the assertion to Truth or the requesting consumer | Identity |
| 15 | Evaluate authorisation **separately** | **Operational Trust** |

**Steps 1 to 14 produce belief. Step 15 produces permission. They never merge.** No confidence value,
however high, is an authorisation.

### Candidate generation

**A bounded candidate set is established before any weighting.** Identity does not evaluate every
Person in the household by default.

| A candidate may enter from | It may never enter from |
|---|---|
| A provider that nominated it, such as a voice matcher | An **unassociated** proximity source or device tracker |
| The Person bound to an observed evidence source through an Identity Evidence Association | A synthetic *Guest*, *Visitor*, or *Unknown* Person |
| The authenticated platform user, where the platform supplies one | A reasoning provider's suggestion |
| A native Person or tracker association consumed by reference | Household membership alone, with no observation |
| A Person named explicitly in a governed interaction | Convenience, recency, or *the resident who is usually here* |

**A candidate is not excluded merely because one source failed to nominate it.** A candidate
nominated by any eligible source is evaluated against **all** eligible evidence, supporting and
contradicting alike. **Unknown Person remains available throughout**, and an empty candidate set is a
legitimate result rather than a reason to relax the rules.

A reasoning provider's suggestion is **not identity evidence**. General inference does not become
identity fusion, and no Person is selected from unsupported model output (**OD-67**).

---

## The Identity Fusion Function

The function that converts qualified evidence into a confidence result is **ordinal, purpose-scoped,
and stepped**. It is not arithmetic performed on percentages, and it produces **governed belief, never
measured probability**.

| # | Rule | Statement |
|---|---|---|
| **F1** | **Purpose ceiling** | For each assertion purpose, every evidence family carries the **highest support level it can reach for that purpose**, taken from *What each evidence source establishes*. A family never contributes above its own ceiling, and an assertion never exceeds the highest ceiling among the families actually supporting it |
| **F2** | **One contribution per family** | A correlation family yields **exactly one** contribution: its strongest qualified observation. Further observations in the same family may improve **observation quality**; they never add a second contribution and never raise the ceiling |
| **F3** | **Qualification is non-increasing** | Within a family, each qualification stage may **lower or hold** the level, never raise it. The stages run in a fixed order, and each records a reason code |
| **F4** | **Anchor and corroboration** | One **anchor family** sets the result: the strongest qualified family whose ceiling permits it to support the claim. Each **additional independent** family raises the result by **one bounded step** — never by summation, and never above the ceiling |
| **F5** | **Corroboration requirement** | A family marked *requires corroboration* for a claim may anchor only to a reduced ceiling. Reaching the top of the scale requires at least one independent corroborating family |
| **F6** | **Bounded reduction** | Contradiction applies **reduction steps** against the specific candidate and claim it bears on. It may reduce the result, force `ambiguous`, or eliminate a candidate. It is **never averaged into the supporting value** and never discarded to reach a cleaner answer |
| **F7** | **Absence is neutral** | Absence never subtracts and never enters a denominator. Fewer available sources produce a **lower ceiling**, never a penalty |
| **F8** | **Separation** | `known` requires the leading candidate to reach the purpose's minimum level **and** to exceed the next candidate by a governed **separation requirement**. Otherwise the outcome is `ambiguous` |
| **F9** | **Determinism and monotonicity** | The same inputs, at the same evaluation time, under the same Fusion Policy version, produce the same result. An eligible supporting observation never lowers a result; a contradicting one never raises it |

> **F6's contradiction handling is DL-38's alone, inside the fusion function, before Truth ever receives
> the resulting purpose-specific Assertion.** Truth's own genuine-conflict rules (**DL-63**) never reuse,
> duplicate, or reach past that Assertion to the evidence families behind it; DL-63 governs only how
> Truth resolves conflict among its own eligible current claims — which may include a consumed Identity
> Assertion as one input, never the fusion process itself.

### Why the result is stepped rather than calculated

| Rejected approach | Why it fails here |
|---|---|
| **Additive scoring** | Sums correlated observations into false corroboration, has no principled ceiling, and lets many weak signals impersonate one strong one |
| **Weighted average** | Puts absence in the denominator, so **a household with fewer sources is penalised** — directly contrary to *missing evidence is not contradicting evidence*. It also dilutes a decisive signal with irrelevant ones |
| **Bayesian or probabilistic fusion** | Requires priors and likelihood ratios no household can supply, assumes conditional independence this model explicitly denies, and would state a **calibrated probability the home cannot support** |
| **Belief-combination models** | Handle ignorance well, but combine conflicting evidence in ways that are not explainable to a resident, and can invert under high contradiction |
| **Unstructured rule accumulation** | Deterministic, but becomes an unauditable pile of special cases with no invariants to test |

The stepped form is chosen because it is the **minimum** architecture that is simultaneously
deterministic, explainable in household language, configurable, testable, purpose-specific,
correlation-aware, contradiction-aware, and honest about uncertainty. **Sophistication is not a
requirement. Explainability is.**

### Qualification order within a family

| Stage | Effect |
|---|---|
| 1 Eligibility gate | **Excluded entirely, before weighting.** Consent absent or withdrawn, disabled, prohibited by policy, unresolved native reference, or belonging to another Person or purpose |
| 2 Claim applicability | Excluded **for this purpose**, while remaining eligible for another |
| 3 Provider match value | Lowers or holds. Retained as reported |
| 4 Observation quality | Lowers or holds |
| 5 Freshness | Lowers or holds, and may render the observation ineligible |
| 6 Configured association reliability | Lowers or holds |
| 7 Family ceiling | Caps |

> **Four different kinds of statement are never multiplied into one product.** A provider match value,
> a configured contribution weight, an observation-quality judgement, and an elapsed time are not
> commensurable quantities. They are applied as **ordered qualifications**, each of which can only
> reduce, and each of which is separately explainable.

### Freshness treatment

Every eligible observation carries an observation time, and freshness is evaluated **at fusion time**,
against the claim being made. The architecture requires **all three mechanisms**, because no single
one is sufficient:

| Mechanism | Why it is required |
|---|---|
| **Source- and purpose-specific validity window** | A voice capture is meaningful for seconds; a household-presence tracker for far longer. One window cannot serve both |
| **Graduated reduction** | A slightly old observation is weaker, not worthless. A cliff edge would make results unstable across a single second |
| **Hard eligibility cutoff** | Beyond a bound, an observation stops being evidence about *now* at all, and must be excluded rather than reduced |

**Current absence and stale presence are different states**, and a stale observation is never
presented as a current one. **No duration is prescribed**; durations are Fusion Policy configuration
and implementation mapping. Freshness governs **each source observation**; how long the resulting
assertion remains a valid historical record, and whether it remains applicable to a new interaction,
are **Assertion Validity** and **Current-Interaction Applicability** (**DL-64**), and the three are
never conflated.

### Outcome selection is ordered

Evaluation stops at the first outcome that applies, so the states cannot blur into one another.

| Order | Outcome | Condition |
|---|---|---|
| 1 | `not required` | The consumer requires no identity resolution for this purpose. **No fusion is performed** |
| 2 | `unavailable` | A **required** input for this purpose could not be evaluated. Not *no match*, not low confidence |
| 3 | `unknown` | No eligible candidate could be generated. `human_participant` records whether a participant is nonetheless supported |
| 4 | `ambiguous` | Two or more **known** candidates remain plausible and the separation requirement is not met |
| 5 | `known` | One candidate reaches the minimum level and satisfies separation |
| 6 | `unknown` | The leading candidate is below the purpose's minimum level while human participation is supported. **A weak known candidate is never forced** |

Rows 3 and 6 are the same state reached by different routes, and both record why. **A close contest
between two known candidates is `ambiguous`, never `unknown`. An unmatched human participant is
`unknown`, never `ambiguous`.**

### The confidence result

Fusion produces an **ordinal support level on a purpose-scoped scale**, which maps to a **confidence
band** through a **versioned band map**.

| Requirement | Statement |
|---|---|
| The band is authoritative | It is the canonical resident-facing and privacy-safe form, consistent with [../architecture/privacy.md](../architecture/privacy.md) |
| A numeric may accompany it | A normalised value may be produced as a **deterministic ordering value**. It is not a probability, not a likelihood, and **never presented as accuracy** |
| One enumeration serves every purpose | Purpose-specificity lives in the **ceilings and rules**, not in a separate set of band names per purpose |
| The map is versioned | Band mapping is Fusion Policy, changed under governed change control |
| The enumeration is **DL-39** | Fusion defines the **output semantics**; **DL-39** enumerates the bands and fixes their meaning |

This is the deliberate handoff. **DL-38 defines what the output is; DL-39 defines what it is called,
and Operational Trust defines what it permits.** Neither reopens the other.

### The four Identity confidence bands

> **There are exactly four Identity confidence bands, and they describe one thing only: the strength
> of support for a known-Person Identity Assertion.**

The canonical labels are **Low**, **Moderate**, **High**, and **Very High**. They are **ordered**, and
the ordering is part of the decision:

```text
Low  <  Moderate  <  High  <  Very High
```

A higher band means stronger identity support **under the applicable assertion purpose**. It
authorises nothing additional by itself.

| Band | What Identity is stating |
|---|---|
| **Low** | A known-Person candidate has meaningful eligible support. Significant uncertainty remains, and alternative explanations may remain open. The candidate satisfies the **DL-38** requirements for this band and no more |
| **Moderate** | A known-Person candidate has stronger eligible support. Evidence quality, freshness, corroboration, and candidate separation reach a higher level. **Material uncertainty remains** |
| **High** | A known-Person candidate has strong purpose-relevant support. The leading candidate has meaningful separation under Fusion Policy, and contradicting evidence is absent, limited, or insufficient to reduce the result below this band. **Identity still claims neither certainty nor confirmation** |
| **Very High** | A known-Person candidate has the **strongest supported result** under the applicable Fusion Policy. The result remains evidence-based and purpose-specific |

**Very High is not certainty, not confirmation, not authentication, and not permission.** It is the top
of a governed belief scale, and a governed belief scale has a top.

**What a band never carries:**

| A band never describes |
|---|
| Permission, authorisation, or capability access |
| Presentation or personalization eligibility |
| Disclosure eligibility or audience eligibility |
| Confirmation, authentication, or session state |
| Consequence class or resource sensitivity |

A band is what Identity found. **The requirement it must meet belongs to what is being protected**,
and is Operational Trust's (**DL-36**). A band is therefore never *"enough"* on its own — only
*"enough for this requirement, evaluated by Operational Trust"*.

**The labels are words, deliberately.** They match how the household already speaks and how this
repository already writes, they read correctly in a resident-facing explanation — *"I was not
confident enough that it was you"* — and, unlike numbers, **they resist arithmetic**. Bands are never
added, averaged, subtracted, or treated as a distance (**DL-38**), and an ordinal numeral invites
exactly that misreading.

### `None` is not an Identity band

> **Identity never produces `None`.**

`None` is an **Operational Trust requirement value** meaning *this capability or protected operation
requires no known-Person Identity band.* It lives only in a requirement, never in an assertion, and
it is never the bottom of the band scale.

The two are read together but produced separately:

| Produced by Identity | Produced by Operational Trust |
|---|---|
| `known`, candidate Tom, **High** | Required Identity Band for this operation: **`None`** |

Both statements are true at once, and the honest account of the outcome is *"known-Person identity
was not required for this operation"* — **not** *"High exceeded `None`"*. See
[operational-trust.md](operational-trust.md).

### State and band are different dimensions

The four bands apply **only to a `known` assertion**. They are not an alternative encoding of the
assertion state, and the state enumeration is unchanged.

| State | Band |
|---|---|
| `known` | One of **Low**, **Moderate**, **High**, or **Very High** |
| `ambiguous` | **Not applicable.** `ambiguous` is not `Low` |
| `unknown` | **Not applicable.** An Unknown Person is never assigned a band, and never `None` |
| `unavailable` | **Not applicable.** `unavailable` is not a low band |
| `not required` | **Not applicable.** No fusion was performed |

**Nothing is gained by collapsing a state into a band, and correctness is lost.** `ambiguous` reports
competing candidates; a low band reports one weakly supported candidate. `unavailable` reports that
an input could not be evaluated; a low band reports that it could. Consumers must be able to
distinguish these, per [../contracts/identity-contract.md](../contracts/identity-contract.md).

### The Fusion Policy

A **Fusion Policy** is a governed, versioned record holding: purpose definitions and their minimum
levels, family ceilings per purpose, corroboration and reduction step rules, separation requirements,
freshness rules, the band map, and the reason-code set.

**Every Identity Assertion references the Fusion Policy version that produced it.** A change creates a
**Change Record** through the existing promotion ladder in
[../architecture/behavioral-governance.md](../architecture/behavioral-governance.md); **earlier
assertions are never recalculated**, a new policy never rewrites an earlier confidence, and an
explanation can state that a result was produced under an earlier policy. **This introduces no second
history mechanism** — it uses the shared temporal model.

### Reason codes

Every reduction, exclusion, cap, step, and outcome carries a reason code, drawn from these categories:
eligibility exclusion, applicability exclusion, freshness, observation quality, correlation reduction,
corroboration applied, ceiling applied, contradiction applied, separation not met, no eligible
candidate, human participation, evaluation failure, and not required. **The exact enumeration is
Fusion Policy and implementation mapping**; the categories are architecture.

### Calibration

**The function is deterministic and uncalibrated by construction.** It states configured belief, and
must never claim measured probability. Calibration may be added later and requires: deterministic
fixtures, replay against **retained governed evidence references and provider values**, resident
correction treated as new evidence, and false-positive and false-negative review.

**Calibration never requires retaining biometric material** — replay operates on references and
reported values, not raw samples. A calibration-derived change is a **proposal** and follows **P26**
and the promotion ladder. **Learning never changes a Fusion Policy silently.**

### The fusion output

The assertion carries or references: assertion identifier; assertion purpose; assertion state;
candidate Person by reference where applicable; confidence band; the normalised value where policy
governs it; supporting evidence; contradicting evidence; excluded evidence with its reason;
correlation treatment; freshness treatment; competing candidates; reason codes; **Fusion Policy
version**; produced time; validity reference; and consent status where required.

**Protected biometric internals are never included**, and evidence detail is omitted where privacy
policy prohibits it.

### Fusion is testable without hardware

A deterministic fixture specifies: assertion purpose, candidate set, Identity Evidence Associations,
evidence observations, provider values, freshness, evidence families, supporting and contradicting
evidence, consent state, and Fusion Policy version. It asserts: expected state, expected candidate,
expected band, expected reason codes, and expected excluded evidence.

**The same fixture under the same policy version must produce the same result**, and no live
biometric or proximity hardware is required to run it.

### Provider match and fused confidence are different values

A provider reports a **candidate** and a **match value**. That value is evidence. **It must never be
silently rewritten as the fused identity confidence**, and it must never be presented as the home's
own belief.

```
provider_match:   Tom, 0.82, voice, capture context Den satellite
                  (provider evidence — retained as reported)

assertion:        candidate Tom
                  purpose    current speaker in the Den
                  identity_confidence_band: High
                  supported  voice match; Tom's wearable observed in the Den;
                             capture endpoint is the Den satellite; Den occupancy active
                  families   voice biometric; wearable proximity; room occupancy
```

**Both values survive.** The assertion references the evidence that produced it, and an explanation can
state each honestly. An evidence observation is **not automatically a Fact**, and **an Identity
Assertion is not automatically a Fact** — Truth decides what becomes authoritative.

### Confirmation is not fusion

A governed confirmation — the household telling the home that a candidate is correct — is an
**evidence source with a bounded claim**, as recorded in *What each evidence source establishes*
above. It is not a recalculation.

> **A successful confirmation never rewrites the assertion it was raised against.**

The provider match value, the fused confidence, the supporting evidence, and the assertion itself are
all unchanged by it. An assertion made at a moderate band **remains** moderate, and remains the
correct historical record of what the evidence supported at that moment. Confirmation adds a separate
governed record; it does not add certainty to fusion, and **`Confirmed` is not the top of the
confidence scale.** Where a new assertion is emitted afterwards, it **references** the original,
names the confirmation method and scope, and never replaces it.

What confirmation is worth, which method a given operation requires, how long it lasts, and what it
covers are **Operational Trust's** decisions, not Identity's. See
[operational-trust.md](operational-trust.md). The **Identity Fusion Function** that produces the
confidence in the first place is **DL-38**, and **a confirmation outcome is never an input to it.**

### Evidence observations use existing records

Observations are recorded through the accepted **Domain Event** and shared temporal model. **No new
generic event store, and no identity history store, is created.** Which platform-supplied execution
evidence is captured is **resolved as OD-64 / DL-111** — native evidence (resulting state, Context,
`entity_id`) is cited as supporting evidence only, never admitted to Identity Fusion.

---

## Current-interaction applicability

> **HTBW does not create a long-lived Identity session.**

An Identity Assertion is purpose-specific, evidence-based, and produced at a point in time. It is
**not a login**, not a ticket, and not a standing claim about who is present from now on.

| An Identity Assertion is | An Identity Assertion is not |
|---|---|
| Produced for one assertion purpose | A general statement of who the household is dealing with |
| Produced from the eligible evidence available at that moment | Maintained because Room occupancy has not ended |
| A permanently correct historical record of what was supported (**DL-64**) | Automatically applicable to the next interaction merely because it has not "expired" |
| A durable historical record of what was supported then | Automatically applicable to a different speaker |

### Validity and applicability are two questions

**Assertion Validity** asks whether an assertion remains a correct historical record of what evidence
supported, for its stated purpose, at the moment it was produced. **This never changes.** An Identity
Assertion is never revoked, decayed, or invalidated by elapsed time alone; it is simply what the
evidence supported then (**DL-64**). **Current-Interaction Applicability** asks whether that assertion
— or a freshly produced one — is evidence-appropriate for *this* interaction, *this* assertion
purpose, and *this* participant.

> **An assertion may remain perfectly valid as a record while being inapplicable to a new
> interaction.**

A valid prior assertion is therefore **not** automatically the current-speaker assertion. Where a
consumer needs a current-speaker result, one is evaluated **fresh** from current eligible evidence —
validity alone never supplies it, and **no separate "assertion validity window" mechanism exists**:
applicability is answered by re-running **DL-38**'s Fusion Function against current eligible evidence,
which already carries its own per-source freshness windows, graduated reduction, and hard cutoff as
Fusion Policy configuration. **No Assertion Purpose requires a fixed validity duration** (**DL-64**).

### Presence does not preserve identity

Room occupancy is a **Truth** fact about the Room. It is not a statement about which Person is
speaking, and it can remain continuously true while the people in the Room change entirely.

| A Room may be | And therefore |
|---|---|
| Continuously occupied while its occupants change | Continuous occupancy is **not** continuous identity |
| Occupied by a different Person | The prior candidate is not the current candidate |
| Occupied by several people at once | No single candidate follows from occupancy |
| Occupied by an Unknown Person | Naming the prior candidate would be false |
| Occupied while identity evidence is unavailable | The correct result is `unavailable` or `unknown`, not the last known name |

**A prior Person assertion, band, or confirmation is never reused merely because presence remains
active.** This is a trust boundary, not a tuning preference, and it holds for presentation exactly as
it holds for access.

### Cross-purpose assertion eligibility (DL-64)

Resolves the one genuine residual question OD-15 originally left open: does a prior assertion for
**one** purpose ever bound the eligibility of an assertion for a **different** purpose — for example,
does a Speaker Attribution assertion remain eligible **evidence** for a later Room Presence fusion?

**Accepted answer**: a prior purpose-specific Assertion may contribute as eligible evidence to a
later, different-purpose fusion, but its contribution **ends** when either condition occurs — only one
break is required:

| Condition | Effect |
|---|---|
| The supporting Room's occupancy transitions to `unoccupied` | The prior Assertion no longer supports a current determination for that Room |
| The Person's configured primary evidence source no longer supports that Room | The prior Assertion no longer supports a current determination for that Room |

A **new** Speaker Attribution assertion is required where a **different** Person speaks in the same
occupied Room; the prior Assertion is never reused as the current-speaker Assertion for someone else —
this restates the existing *presence does not preserve identity* rule (**DL-39**), not a new one.

**This is evaluated entirely inside DL-38's fusion, before Truth ever receives an Assertion.** An
Assertion that fails this eligibility check is excluded as ineligible evidence within fusion (**F1**,
eligibility gating before weighting); it is never surfaced to Truth as a candidate claim requiring
**DL-63** conflict resolution. **Current-Interaction Applicability is therefore always evaluated before
any Truth-side conflict qualification runs.**

### Each interaction evaluates current evidence

```text
Current eligible evidence
        ↓
DL-38 Identity Fusion Function
        ↓
Current purpose-specific Identity Assertion
        ↓
Current confidence band
```

For a voice interaction, current evidence **may** include, where available and eligible: the current
voice observation and provider result, current wearable or phone proximity, current occupancy,
current endpoint context, current authenticated user context, current contradictions, current
freshness, the applicable Identity Evidence Associations, and the Fusion Policy version.

**No source is mandatory.** Absence remains neutral under **F7**, and an optional source never becomes
required by appearing in this list.

**Fusion is not re-run for activity that does not need identity.** Where the consumer's requirement is
`None` and no other consumer needs a candidate, `not required` is the correct and complete result. But
where a *presentation* decision is being considered — addressing someone by name — that decision needs
a **current applicable assertion** for its purpose, and cannot borrow an earlier one.

This is the same shape the platform already uses for governed environmental control: **current
sensors → current evaluation → current governed result**. The analogy is explanatory only. **It
creates no Identity Controller, no second fusion service, and no prescribed runtime component** — the
architectural requirement is current-state evaluation, not a class, a coordinator, or a name.

---

## Reliability may be proposed, never silently changed

Person-specific reliability may be **explicitly configured**, **suggested from observed behaviour**, or
**learned only under accepted Learning and Adaptive governance** — the promotion ladder in
[../architecture/behavioral-governance.md](../architecture/behavioral-governance.md). **Identity owns
the resulting configuration**, because the value determines how identity evidence is interpreted.
Continuity does not own it merely because habits influence it.

| Requirement | Statement |
|---|---|
| No silent change | **Learning never changes an identity weight on its own.** A proposal is a proposal |
| Explainable and evidenced | The proposal states its reasoning and references the observations behind it |
| Authorised acceptance | A resident with authority accepts it, and consent applies where behaviour profiling or biometric information is involved |
| Recorded | Acceptance creates a **Change Record**; prior versions stay historically reconstructable |
| Not retroactive | **A changed weight never rewrites an earlier Identity Assertion** |
| Explicit configuration wins | Household configuration outranks an unaccepted learned proposal |
| Reversible | A resident may revoke, reset, or disable an association, subject to preservation requirements |

**This adds no responsibility and no learning store.** Evidence eligibility remains **OD-65**, and the
proposal lifecycle remains **OD-28**.

---

## The three-way distinction

This distinction must be preserved everywhere in the platform.

| Concept | Owner | Example |
|---|---|---|
| **Identity Evidence** | Identity | A voice sample matched Tom's profile at 0.91; Tom's phone is on the Den Wi-Fi AP |
| **Identity Assertion** | Identity | Candidate person Tom, identity_confidence_band: High, from voice + BLE + phone |
| **Contextual Person-Presence Fact** | **Truth** | Tom is present in the Den, carrying its own **Truth Confidence Band** (**DL-58**), independently derived — never the Identity Assertion's band |

An identity assertion is an **input** to the presence fact. It is not the presence fact.

---

## Identity does not determine

- Authoritative room occupancy
- Authoritative presence in a contextual space
- What activity is occurring
- What should happen
- What a person prefers
- What a person is permitted to do
- **Whether its own confidence is sufficient for any purpose**

> **Identity states what it believes and how strongly. It never states that this is enough.**

Sufficiency is decided by the consumer, and it is not universal. The same assertion may be enough to
address someone by name, not enough to open their calendar, irrelevant to a household-neutral
request, and insufficient to authorise a permission change no matter how high it is. Presentation,
capability access, disclosure, and confirmation are **four distinct evaluations** owned by
Operational Trust, and satisfying one never satisfies another. See
[operational-trust.md](operational-trust.md).

---

## Consumes

- Foundation Person and Relationship definitions
- Identity-evidence sources
- Enrollment and consent records

## Provides

- Identity assertions with confidence, evidence attribution, and reason codes
- Enrollment state and quality summaries
- Identity diagnostics
- Revocation outcomes

---

## Identity assertions are short-lived

## Identity assertions are permanent records, never sessions (DL-64)

An identity assertion describes a moment, not a session, and it does not need to "expire" for the
architecture to behave correctly.

- **Assertion Validity is permanent.** An assertion remains a correct historical record of what
  evidence supported, for its stated purpose, at the moment it was produced — forever. It is never
  revoked or decayed by elapsed time alone.
- **Current-Interaction Applicability is re-evaluated fresh, on demand**, by re-running the **DL-38**
  Fusion Function against current eligible evidence — never by consulting a stored expiry timestamp.
  DL-38's own per-source freshness windows, graduated reduction, and hard cutoff already bound what
  counts as current eligible evidence; **no second, assertion-level validity-window mechanism is
  created**.
- **No Assertion Purpose requires a fixed validity duration.** `unknown` and `unavailable` carry no
  band and are never reused as though current.
- **A runtime attribution context must not become a long-lived identity session.**
- An implementation may **cache** a recently produced assertion as a performance optimisation —
  equivalent to asserting "fresh fusion would produce the same result" — keyed to a versioned,
  Fusion-Policy-configured duration. This is **implementation mapping** (the same status as OD-16's
  fusion coefficients), never a second governed architecture.

See *Current-interaction applicability*, above, and **DL-64** in
[../governance/decision-ledger.md](../governance/decision-ledger.md).

---

## Failure behavior

| Condition | Behavior |
|---|---|
| Identity unresolved | Report `unknown`. Apply guest-safe treatment. Never assume the most likely resident for an authority-bearing action. |
| A human participant is supported but no known Person is eligible | Report `unknown` with the participant supported. **This is a valid outcome, not a fault.** The unidentified-person policy applies. |
| A provider evaluated successfully and returned no eligible match | Report `unknown`, never `unavailable`. A correct negative must not be reported as a failure. |
| Two identities plausible | Report `ambiguous` with all candidates and confidences. Do not silently select the highest for authority-bearing actions. |
| Evidence sources disagree | Report the disagreement with attribution. Reduce confidence. |
| Evidence is stale | Reduce confidence or withdraw the assertion. |
| A dependency fails | Report `unavailable` and **fail closed**. Do not degrade to a guess. |

**None of the above is ever a Repairs issue by itself** (**DL-65**) — each is a self-resolving runtime
outcome, re-evaluated fresh on the next interaction. Only a **broken governed reference** an Identity
Evidence Association depends on (for example, an association pointing to a deleted device) is a
genuine Repairs candidate, under the same general broken-reference rule every responsibility follows —
never a special Identity-specific Repairs category.

See [../architecture/failure-and-degradation.md](../architecture/failure-and-degradation.md).

---

## Privacy considerations

- Consent is required, scoped, recorded, attributable, and revocable. **Identity owns the consent
  lifecycle** — capture, scope, renewal, expiry, and revocation. Foundation holds the consent record
  on the Person; Operational Trust owns consent policy and enforcement. See
  [operational-trust.md](operational-trust.md).
- Enrollment artifacts are temporary; derived profiles are durable and separately governed. **Raw
  enrollment samples never become historical identity evidence merely because they existed** — they
  are inputs to profile generation, not a record of who was present.
- **Deleting a Person cleans up every Person-governed voice profile and artifact**, so that no orphan
  profile remains. Consent records and historical governance records follow their own accepted
  lifecycle, and payloads are removed unless preservation or retention authority requires otherwise
  (**DL-45**).
- **Biometric internals — vectors, embeddings, fingerprint payloads, artifact internals, storage
  paths — are never exposed** through services, diagnostics, logs, telemetry, or explanations, and
  are never passed to another responsibility. Identity emits assertions; consumers, including Truth,
  receive assertions only.
- Safe metadata only: state, quality summary, confidence band, reason code.
- Presence history derived from identity evidence is among the most sensitive household data.
- Revocation removes the derived profile and its associations, not merely their use. **Removing a
  derived profile never rewrites an earlier Identity Assertion.** An assertion made while the profile
  was valid remains historically true and remains explainable (**P27**); later explanations report
  that the evidence source no longer exists, and never restate the past as though it did not happen.

See [../architecture/privacy.md](../architecture/privacy.md).

---

## Explainability requirements

A Decision Trace that used identity records: the candidate or candidates, the confidence, the
contributing evidence classes, the reason code, and the threshold that applied.

A resident must be able to hear "I was not certain it was you" as a valid explanation.

---

## Identity history

**Identity owns the history of its own records.** Foundation defines the shared temporal model; see
[temporal-record.md](temporal-record.md).

History is owned for:

- Identity Assertion history — candidates, confidence, evidence classes, reason codes, thresholds
  applied
- Identity-consent lifecycle history — granted, scoped, modified, revoked
- Enrollment and revocation lifecycle history

### The biometric boundary holds across time

**Identity history retains evidence classes and reason codes only. It never retains biometric
internals** — vectors, embeddings, fingerprint payloads, artifact internals, or storage paths. This
is unchanged by any retention floor: **P27** requires that the home be able to explain itself, and an
evidence class with a reason code and a confidence band is sufficient to do so.

Raw voice samples remain at **zero retention** by default. No Preservation Hold can preserve them,
because they were never stored.

### Explaining past identity decisions

A Decision Trace references the **exact version** of the Identity Assertion it used (**P30**), so an
explanation remains accurate after the assertion has expired, been superseded, or been revoked. Where
an identity record has been revoked or redacted, the trace reports the limitation rather than
implying the assertion never existed.

---

## Representative scenarios

- [../scenarios/follow-me-media.md](../scenarios/follow-me-media.md)
- [../scenarios/multi-person-conflict.md](../scenarios/multi-person-conflict.md)
- [../scenarios/why-did-this-happen.md](../scenarios/why-did-this-happen.md)

## Open decisions

| ID | Question |
|---|---|
| OD-07 | Local versus cloud voice implementation |
| OD-08 | **Resolved as DL-39 and DL-40.** Four bands — Low, Moderate, High, Very High; `None` is an Operational Trust requirement, not an Identity output; Operational Trust owns every threshold |
| OD-15 | **Resolved as DL-64.** "Assertion lifetime" was a conflation of Assertion Validity (a permanent historical record), Current-Interaction Applicability (re-evaluated per interaction via fresh DL-38 fusion, no fixed window), and Retention (DL-47's, unaffected). Cross-purpose assertion eligibility is accepted, bounded by Room occupancy and the Person's configured primary evidence source |
| OD-16 | **Resolved.** The evidence architecture is **DL-32**; the Identity Fusion Function is **DL-38**. Remaining coefficients are Fusion Policy configuration, not architecture |
| OD-33 | **Closed — DL-43, DL-46, DL-47.** A persisted Identity Assertion is retained with the Decision Trace or governed history it supports, never on a separate universal clock |
| OD-36 | Reconciliation of deletion and export obligations with retention floors and Preservation Holds |
| OD-91 | Whether and how HTBW orchestrates a resident's hand-off to Home Assistant's native Person creation surface when no native Person yet exists; native creation by HTBW itself is verified unsupported |

## Related documents

- [truth.md](truth.md)
- [operational-trust.md](operational-trust.md)
- [temporal-record.md](temporal-record.md)
- [../contracts/identity-contract.md](../contracts/identity-contract.md)
- [../architecture/privacy.md](../architecture/privacy.md)
