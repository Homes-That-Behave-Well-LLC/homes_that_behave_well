# Continuity Model

> **Document status: Canonical model.**
> Terminology: [glossary.md](glossary.md). Owning responsibility: **Continuity**.
> Contract: [../contracts/continuity-contract.md](../contracts/continuity-contract.md)
> Experience and Session structure: [experience-and-session.md](experience-and-session.md)

---

## Purpose

**Continuity is more than storage and more than a preference list.**

Any document that treats Continuity purely as persisted state is superseded.

## Question answered

*What should be remembered, restored, resumed, or allowed to follow a person or experience across
time and space?*

---

## Continuity is not a child of Stewardship

Continuity is a **first-class responsibility**, broader than the history of any other responsibility.
The two must not be folded together in either direction.

| Held by **Continuity** | Held by **Stewardship** |
|---|---|
| Person-scoped preferred artist, genre, album, playlist | Care obligations and their state |
| Preferred delivery, presentation, and re-presentation of a Communication | Significance, with provenance |
| Preferred interaction patterns, last lamp levels, last speaker volume | Caretaker assignment and the escalation ladder |
| Room-scoped music, duck, and TTS volume | Maintenance, service, and conservation history |
| Session, resume, and transfer state; Follow-Me behaviour | Obligation, significance, and caretaker-assignment history |
| Selected experience history and preference evolution | Care records that establish that care occurred |

**Stewardship history is Stewardship's**, under the shared temporal model
([temporal-record.md](temporal-record.md)) — *each responsibility owns the history of its own records*.
Continuity may **consume** it; Continuity does not become its owner, and Stewardship does not become
the owner of household preferences because a preference happens to concern something the household
cares about.

**No general preference, Follow-Me behaviour, resume behaviour, transfer behaviour, or experience
restoration moves into Stewardship**, and no care obligation moves into Continuity.

---

## Owns or governs

- Person-scoped preferences
- Room-scoped experience settings
- Active experience state
- Experience history
- Resume state
- Transfer state
- Follow-Me intent
- Follow-Me enabled or disabled state
- **Communication re-presentation preference** — whether an outstanding Communication should be
  re-presented as the person moves
- **Preferred delivery and preferred presentation** — how a resident wants to be told, and in what
  form. Ownership was already stated in
  [../scenarios/stewardship-use-cases.md](../scenarios/stewardship-use-cases.md) and
  [communication.md](communication.md); it is named here so the list is complete. **The preference
  dimensions themselves — verbosity, explanation depth, citation, spoken versus visual delivery,
  accessibility, language and locale, and per-capability override — are not enumerated in any
  canonical document.** The only enumerations that exist are in
  [person-profile-model.md](person-profile-model.md) and
  [../contracts/service-contracts.md](../contracts/service-contracts.md), **both Historical and
  superseded**, and neither is authority. **Whether a person-scoped preference may name or steer a
  reasoning provider is resolved: it does not.** The explicit Person
  Reasoning-provider assignment, the **Allow General Questions** authorization, and the **Allow Home
  Steward** authorization (**OD-67**, accepted **DL-93**, Issue #132) are canonical for provider assignment and
  capability authorization, made through Person Configuration, never through a Continuity preference;
  Continuity's preferred delivery/presentation preference governs wording and delivery form only, and
  is never a second configuration authority for either capability gate. **The scope at which a
  presentation preference may exist, and what takes precedence when a Room persona and a person
  preference disagree, is OD-79**
- **Audience-Uncertainty Routing Preference (DL-72)** — distinct from the ordinary delivery
  preference above: where a Communication should route **when audience composition cannot be safely
  established** for that Person as intended recipient. Answers *"when HTBW cannot determine who else
  may hear or see a private message intended for you, where should it send it?"* **Not** an Audience
  Composition claim, not a statement that the selected destination is always private, not a bypass of
  Operational Trust, not a substitute for Delivery Surface capability evaluation, and not a request to
  identify everyone in the Room. Continuity holds the preference; Operational Trust determines whether
  it is currently permitted and safe; Concierge selects the Delivery Target. See
  [communication.md](communication.md) and [operational-trust.md](operational-trust.md)
- **Room-Delivery Audience Preference (DL-94, resolved OD-57)** — distinct from both preferences
  above: where the audience **is known**, not uncertain, which Urgency levels and which co-present
  audiences (Household, selected individual Household members, Guest — each independently permitted or
  not) make a Communication eligible for Room delivery at all, and whether a **known** mixed audience
  satisfies standing permission without a one-message Room-Delivery Authorization Challenge. **A
  Person present with another Person is not thereby an unauthorized audience**; the Preference, not
  mere co-presence, determines sufficiency. Continuity holds the preference; Operational Trust
  determines whether it is currently permitted and safe, exactly as for the Audience-Uncertainty
  Routing Preference; the Preference itself grants nothing. See [communication.md](communication.md)
- Ask-before-transfer preference
- Never-transfer preference
- Active personal media sessions
- Active room experiences
- Session ownership
- Session participants
- Origin room
- Current room
- Transfer eligibility
- Resume eligibility
- Blocking state supplied by other responsibilities
- Experience lifecycle

**Continuity owns person-scoped preferences. It does not decide when they may be applied.** Applying a
Person's preferences, history, or resumed session to a live interaction is a **person-scoped
capability access** evaluated by Operational Trust against the current Identity Assertion — not a
consequence of the home having addressed someone by name. See
[operational-trust.md](operational-trust.md).

### What Continuity does not hold, however personal it feels

| Not held by Continuity | Held by |
|---|---|
| An observation of what a person did | The responsibility that observed it, as a **Domain Event** |
| A pattern that has not been accepted | Nothing. *Nothing behavioural* until it is accepted (**P26**) |
| A Fact, current or historical | **Truth** (**P28**) |
| Care obligations and their history — medication, veterinary, maintenance, inspection, irrigation | **Stewardship** |
| Rainfall, forecast, soil-moisture, and every other environmental observation and its history | **Truth**, as Facts and Historical Facts |
| Calendar contents, mailbox contents, playback position, provider recommendations | **The source system.** HTBW *persists no second copy merely to explain later* (**DL-46**) |
| The association between a Person and an external service, account, mailbox, or calendar | **No responsibility is currently named.** [person-and-identity.md](person-and-identity.md) records the extension without an owner, and the accepted relationship types — `caretaker-of`, `owner-of`, `serves-room`, `located-in` — do not express it. **OD-77** |
| A recommendation, of any kind | Nobody, as truth. A **Reasoning Provider** *owns nothing*, and its recommendation *never silently becomes an authorised action* (**OD-67**) |

**A remembered value is not a Fact.** Which class of remembered value a restoration reproduces — last
observed, last successful, last person-selected, configured default, or approved preference — and
whether restoration reproduces a prior value or computes a currently appropriate one, is **OD-78**.

**There is no Journey, checkpoint, or progress-marker object.** The glossary defines **Experience** and
**Session**; resuming a book is a Session with a resume candidate, an eligibility window (**OD-25**),
and a **Governed Reference** to provider-owned position.

---

## Scope rules

### Person-scoped

- Preferred artist
- Preferred genre
- Preferred album
- Preferred playlist
- Preferred personal media defaults
- Personal Follow-Me setting
- Personal request to have music follow
- Current personal media session

### Room-scoped

- Last song played in the room
- Last genre played in the room
- Music volume
- Duck volume
- TTS volume
- Current room experience
- Room-specific resume state

### Room-scoped granularity follows Room Configuration's participating capabilities

**A Room-scoped value is recorded per participating capability, not collapsed into one room-wide
value, unless Room Configuration deliberately configures a single shared target.** Where a Room's
vocabulary term resolves to several configured fixtures (for example, "Lamps" resolving to more than
one lamp), "Room-specific resume state" means each participating fixture has its own remembered
value. This mirrors the granularity Room Configuration already uses for Primary Authority per
Environmental Purpose (**DL-60**, **DL-62**): the scope stays Room-scoped — ownership does not move to
the fixture, the Person, or a new third tier — but the stored value is per capability, read back at
the granularity Room Configuration declares.

### Guest and default experience are not a third Continuity scope

Continuity still has **exactly two scopes**. A household's guest or default experience — for example,
an appropriate genre or playlist when no identified Person's preference applies — does not create a
third scope and is never represented as a fabricated Person invented to hold a Room's taste. It is one
of:

- the already-accepted **Guest fallback Person Extension** (**DL-71**, see
  [glossary.md](glossary.md)): exactly one existing, deliberately configured Person the household
  designates as the default consulted under Unknown Person, consulted here as ordinary person-scoped
  Continuity for that Person Extension, never a new Identity state; or
- a **configured default** — Room Configuration's own baseline value for a capability, not a
  remembered or learned preference at all. "Configured default" is already named as one of the
  remembered-value classes **OD-78** must resolve; this model does not decide its provenance here.

**Which of these applies, and the full precedence among explicit request, Person-scoped Continuity,
Room/session Continuity, this guest/default context, and no fallback at all, remains OD-78.** What is
settled now is narrower and does not wait on OD-78: an **explicit resident request is never overridden
by remembered state of any scope.** Continuity supplies state Concierge may apply; a preference is
never treated as an instruction (see
[../contracts/concierge-contract.md](../contracts/concierge-contract.md) hard prohibitions). Remembered
state fills in what the resident did not say; it does not contradict what the resident did say.

### The preserved scoping rule

> **Preferred artist, genre, album, and playlist are person-scoped rather than person-plus-room
> scoped, so preferences may follow a person across rooms.**

This rule was discovered during the exploratory Concierge work and is preserved deliberately. A
person's taste is a property of the person. A room's volume is a property of the room.

**Learning respects this split rather than replacing it.** An approved learned preference is an
ordinary Continuity preference at one of these two scopes, versioned and revocable like any other. It
is **not** a separate learned-preference store. Continuity holds the approved preference; Operational
Trust holds the permission to act on it autonomously; the observation that produced the suggestion is
a **Domain Event** owned by the responsibility that observed it. The governing rules are in
[../architecture/behavioral-governance.md](../architecture/behavioral-governance.md) under **P26**;
the lifecycle is **OD-28** and evidence eligibility is **OD-65**.

### Habit continuity and vocabulary continuity are not Continuity scopes

**Continuity has exactly two scopes — person-scoped and room-scoped — and their silence on household
habits and household words must not be read as an invitation to add a third tier.**

*Habit continuity* and *vocabulary continuity* are useful **review lenses** for asking whether a
change breaks something the household relies on. **Neither is a Continuity storage scope, a remembered
value class, or an architectural construct**, and neither may be used to justify a household-scoped,
vocabulary-scoped, or habit-scoped tier alongside the two above.

The words the household uses are **Contextual Vocabulary**, owned by Room Configuration
([contextual-vocabulary.md](contextual-vocabulary.md)), and a vocabulary term is a **configured
mapping**, never a remembered value. **The consequence for the household when a term changes or is
withdrawn is not settled**, and is **OD-86** — it belongs to vocabulary governance, not to Continuity.
An established household routine is likewise not a Continuity object: what it rests on is either a
configured mapping, an approved preference already held at one of the two scopes, or a household
automation that HTBW references and never rewrites.

**No debt construct follows from this.** *Vocabulary debt* and *habit debt* are narrative language and
carry no architectural meaning here.

---

## Three modes of continuity

Continuity must support all three:

| Mode | Example |
|---|---|
| **Explicit** | "Have the music follow me." |
| **Assisted** | "You left a documentary in the Primary Bedroom. Move it here?" |
| **Autonomous** | The Jazz session moves with Tom without asking, because policy permits it |

Which mode applies is determined by Operational Trust, not by Continuity.

---

## Worked examples

- Tom says, "Have the music follow me."
- Tom moves from the Office to the Den.
- The active Jazz session **may** be transferred if policy and destination state permit.
- Tom moves to a room in Nighttime mode.
- The transfer **may be intentionally suppressed**.
- Tom leaves a documentary in the Primary Bedroom and moves to the Den.
- The system **may ask** whether to move or resume the documentary depending on policy.
- David enters a room where Tom's active experience already exists.
- The active experiences **may conflict** and require Concierge resolution.

In every case Continuity supplies the state and the intent. **Continuity does not choose the final
action.**

---

## Transfer versus resume

| | Transfer | Resume |
|---|---|---|
| Precondition | The session is active | The session is not active |
| Effect | Moves a running session between Rooms | Re-establishes a previous session |
| Typical trigger | A room transition with Follow-Me intent | A request, or an assisted offer on arrival |
| Blocked by | Destination mode, existing experience, authority, availability | Eligibility window, authority, availability |

**Movement between constituent Physical Rooms inside the same Merged Room is neither a transfer nor a
resume.** No Room Context changed. See [room.md](room.md).

---

## Follow-Me eligibility

Follow-Me is a **policy-governed handoff**, not motion-triggered movement.

All of the following must hold before a transfer is eligible:

- Follow-Me is enabled for the person or session
- Identity is resolved with sufficient confidence
- The room transition is unambiguous — origin and destination both known and different
- Manual-stop protection is not active
- Manual-stop cooldown is not active
- The destination Room has configured, valid, available playback targets

Representable blocks:

- Follow-Me disabled, or never-transfer preference set
- Identity unresolved, ambiguous, or below threshold
- Room transition ambiguous or missed
- Origin or destination Room unavailable
- Destination Room mode prohibits incoming media
- An existing experience in the destination Room has priority
- Another person's session would be displaced without authority

Each block is a **reason**, and each reason must reach the Decision Trace.

### Communication re-presentation is a preference, not a transfer

An outstanding **Communication** has no location and is never transferred, moved, or duplicated.
Where a person moves and a Communication remains outstanding, Concierge may make a **new Delivery
Attempt** on a newly appropriate surface.

| Question | Owner |
|---|---|
| Does the resident want this? | **Continuity** — a preference in the Follow-Me family |
| Is it permitted on the new surface? | **Operational Trust** (**P32**) |
| Is it attempted, and where? | **Concierge** |

**This preference is not coupled to media transfer eligibility.** The Follow-Me eligibility rules
above govern sessions, not Communications. Open decision **OD-48**. See
[communication.md](communication.md).

---

## Blocking state supplied by other responsibilities

Continuity records that a transfer or resume was blocked, and by which responsibility, without
claiming ownership of the blocking rule:

```
transfer_eligible: false
blocked_by:        operational_trust
reason:            destination_room_mode_prohibits_incoming_media
fact_reference:    primary_bedroom.mode = nighttime
```

---

## Consumes

- Foundation Person, Room, and Experience definitions
- Identity assertions (whose session is this?)
- Truth facts (room mode, existing experience, availability, room transitions)
- Explicit human instruction

## Provides

- Person-scoped and room-scoped preferences
- Active session state, ownership, participants, origin and current Room
- Transfer and resume intent and eligibility
- Experience history and resume candidates
- Blocking state with attribution

## Explicit non-responsibilities

Continuity does **not**:

- Decide whether a transfer happens (Concierge, under Operational Trust policy)
- Establish whether music is already playing (Truth)
- Grant authority to displace another person's session (Operational Trust)
- Own obligations (Stewardship)
- Perform playback (Concierge, through governed interfaces)
- Own Communications, delivery decisions, or delivery history (Concierge)
- **Formulate or present a recommendation.** *Continuity feeds Concierge; Continuity does not choose*
  ([../architecture/dependency-view.md](../architecture/dependency-view.md) rule 5)
- **Own the history of another responsibility's records**, however personal that history is

---

## Failure behavior

| Condition | Behavior |
|---|---|
| Home Assistant restarts during an active session | Do not fabricate a session. Re-establish only what can be verified; offer resume where eligible. |
| A room transition is missed | Do not retroactively transfer. Treat the newly observed Room as current and record the gap. |
| A configured speaker group is partially unavailable | Apply the configured partial-availability policy; record which members were unavailable. |
| Preferences unavailable | Do not substitute a platform default silently; state that the preference could not be read. |
| Two sessions claim the same Room | Surface the conflict to Concierge; do not merge or terminate unilaterally. |

## Privacy considerations

Preferences, session history, and room-to-room movement patterns are personal data. Visibility is
governed by Operational Trust policy; guests must not see residents' preferences or history.

## Explainability requirements

Every transfer, suppression, resume offer, and refusal records the intent, the eligibility outcome,
the blocking reason, and the responsibility that supplied it.

---

## Continuity history

**Continuity owns the history of its own records.** Foundation defines the shared temporal model; see
[temporal-record.md](temporal-record.md).

History is owned for:

- Preference history
- Session history
- Resume history
- Transfer history

Continuity's **experience history** was already owned before the temporal model existed. It is now
recorded as **Change Records** against a **Current Projection**, in common with every other
responsibility.

**Continuity owns experience history. Continuity does not own Fact history** — that is Truth's, under
**P28**. An experience is something a person had; a Fact is a governed conclusion about the world.
Keeping a private record of what Truth used to say would create a second fact engine, which **P8**
and **DL-04** prohibit.

A Decision Trace references the **exact version** of the preference or session it used (**P30**), so
a past explanation remains accurate after the preference has since changed.

Experience history is a governed record class under **DL-47**, following External History Retention
with its own Retention Classification. Whether it is retained per person, per room, or both, and for
how long, remains open decision **OD-26**.

---

## Representative scenarios

- [../scenarios/continuity-use-cases.md](../scenarios/continuity-use-cases.md)
- [../scenarios/follow-me-media.md](../scenarios/follow-me-media.md)
- [../scenarios/multi-person-conflict.md](../scenarios/multi-person-conflict.md)
- [../scenarios/nighttime-suppression.md](../scenarios/nighttime-suppression.md)
- [../scenarios/why-did-this-happen.md](../scenarios/why-did-this-happen.md)

## Open decisions

| ID | Question |
|---|---|
| OD-24 | Session-merging algorithm when two people's sessions meet in one Room |
| OD-25 | Resume eligibility window defaults per experience class |
| OD-26 | Whether experience history is retained per person, per room, or both, and for how long |
| OD-33 | **Closed — DL-43, DL-46, DL-47.** Retention is declared inside every governed record lifecycle; experience-history scope and duration remain **OD-26** |
| OD-48 | Re-presentation preference for outstanding Communications, and its relation to the Follow-Me preference family |
| OD-77 | Ownership of the association between a Person and an external service, account, calendar, mailbox, or media profile |
| OD-78 | Remembered-value classes and restoration semantics — reproduce a prior value, or compute a currently appropriate one |
| OD-79 | Presentation preference scope and precedence — which scopes may hold one, who owns each, and what wins when they disagree |

## Related documents

- [experience-and-session.md](experience-and-session.md)
- [operational-trust.md](operational-trust.md)
- [temporal-record.md](temporal-record.md)
- [../architecture/behavioral-governance.md](../architecture/behavioral-governance.md)
- [../contracts/continuity-contract.md](../contracts/continuity-contract.md)
