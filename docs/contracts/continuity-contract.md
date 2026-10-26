# Continuity Contract

> **Document status: Canonical contract.**
> Responsibility: **Continuity**. Models: [../models/continuity.md](../models/continuity.md),
> [../models/experience-and-session.md](../models/experience-and-session.md).

---

## Owning responsibility

**Continuity — what should be remembered, resumed, or transferred?**

**Continuity is more than storage and more than a preference list.** Any document treating Continuity
as persisted state alone is superseded.

**Continuity is not a child of Stewardship.** Stewardship owns the history of its own records \u2014
obligations, significance, maintenance, service, and caretaker assignment \u2014 under the shared temporal
model. Continuity may consume that history; it never becomes its owner. Conversely, **no general
preference, Follow-Me behaviour, resume behaviour, transfer behaviour, or experience restoration moves
into Stewardship**. See [../models/continuity.md](../models/continuity.md).

---

## What Continuity guarantees

- Person-scoped preferences and room-scoped experience settings, explicitly distinguished
- **Preferred delivery and preferred presentation**, and the re-presentation preference (**OD-48**).
  **The preference dimensions are not enumerated in any canonical document**; the only enumerations
  that exist are Historical and superseded, and neither is authority
- Active session state: identity, experience class, owner, participants, origin Room, current Room,
  state, and lifecycle
- Transfer intent: Follow-Me enabled or disabled, ask-before-transfer, never-transfer
- Transfer and resume **eligibility**, with blocking attribution
- Experience history and resume candidates

---

## Scope rules

| Person-scoped | Room-scoped |
|---|---|
| Preferred artist | Last song played in the room |
| Preferred genre | Last genre played in the room |
| Preferred album | Music volume |
| Preferred playlist | Duck volume |
| Personal media defaults | TTS volume |
| Personal Follow-Me setting | Current room experience |
| Current personal media session | Room-specific resume state |

> **Preferred artist, genre, album, and playlist are person-scoped rather than person-plus-room
> scoped, so preferences may follow a person across rooms.**

This rule is preserved deliberately.

**Room-scoped granularity follows Room Configuration's participating capabilities.** Where a Room's
vocabulary term resolves to several configured fixtures, "Room-specific resume state" is recorded and
restored per participating fixture, not collapsed into one room-wide value — mirroring the Primary
Authority granularity Room Configuration already uses per Environmental Purpose (**DL-60**, **DL-62**).

**Guest and default experience are not a third scope.** A guest or default experience (for example, a
default music genre when no identified Person's preference applies) is either the already-accepted
**Guest fallback Person Extension** (**DL-71**) consulted as ordinary person-scoped Continuity, or a
Room Configuration **configured default** — never a remembered preference and never a fabricated
Person invented to hold a Room's taste. Which applies, and the complete precedence among explicit
request, Person-scoped, Room/session-scoped, and guest/default context, remains **OD-78**. Settled now,
independent of OD-78: an explicit resident request is never overridden by remembered state of any
scope — see the Concierge Contract hard prohibition that a preference is never treated as an
instruction.

### What is *not* in either column

A record does not become Continuity's because it is personal, remembered, or emotionally significant.

| Not Continuity's | Owner |
|---|---|
| An observation of what someone did | The responsibility that observed it, as a **Domain Event** |
| A pattern that has not been accepted | Nothing. *Nothing behavioural* until accepted (**P26**, **DL-21**) |
| Any Fact, current or historical | **Truth** (**P28**) |
| Care obligations and their history — medication, veterinary, maintenance, inspection, irrigation | **Stewardship** |
| Rainfall, forecast, soil-moisture, and every other environmental observation | **Truth** |
| Calendar contents, mailbox contents, playback position, provider recommendations | **The source system** (**DL-46**, **P21**) |
| The Person-to-external-service association | **Currently unowned — OD-77** |
| A recommendation | Nobody, as truth. A Reasoning Provider *owns nothing* (**OD-67**) |

**A remembered value is not a Fact.** Whether a restoration reproduces a prior value or computes a
currently appropriate one, and which value class it draws from, is **OD-78**.

**There is no Journey, checkpoint, or progress-marker construct.** Resuming a book is a Session with a
resume candidate, an eligibility window (**OD-25**), and a **Governed Reference** to provider-owned
state.

---

## Three modes

| Mode | Example |
|---|---|
| Explicit | "Have the music follow me." |
| Assisted | "You left a documentary in the Primary Bedroom. Move it here?" |
| Autonomous | The Jazz session moves with Tom without asking, because policy permits it |

**Which mode applies is determined by Operational Trust, not by Continuity.**

---

## The decisive boundary

> **Continuity does not choose the final action.**

Continuity supplies state, intent, and eligibility. Concierge decides. Operational Trust authorizes.

---

## Transfer versus resume

| | Transfer | Resume |
|---|---|---|
| Precondition | The session is active | The session is not active |
| Effect | Moves a running session between Rooms | Re-establishes a previous session |
| Blocked by | Destination mode, existing experience, authority, availability | Eligibility window, authority, availability |

**Movement between constituent Physical Rooms inside the same Merged Room is neither a transfer nor a
resume.** No Room Context changed.

---

## Follow-Me eligibility

Follow-Me is a **policy-governed handoff**, not motion-triggered movement. All must hold:

- Follow-Me is enabled for the person or session
- Identity is resolved with sufficient confidence
- The room transition is unambiguous — origin and destination known and different
- Manual-stop protection is not active
- Manual-stop cooldown is not active
- The destination Room has configured, valid, available playback targets

Representable blocks:

- Follow-Me disabled or never-transfer set
- Identity unresolved, ambiguous, or below threshold
- Room transition ambiguous or missed
- Origin or destination Room unavailable
- Destination Room mode prohibits incoming media
- An existing experience in the destination Room has priority
- Another person's session would be displaced without authority

Each block is a **reason** and must reach the Decision Trace.

---

## What consumers may rely upon

| Consumer | May rely upon |
|---|---|
| Operational Trust | Session ownership and participants, to evaluate displacement authority |
| Concierge | Preferences, session state, intent, eligibility, and blocking attribution |
| Concierge | The resident's **Communication re-presentation preference**, within the Follow-Me preference family |

## What consumers must never assume

- That eligibility means the transfer will happen
- That a preference is a fact
- That a preference is an instruction
- That a resumed session retains authority granted at its start
- That a missing preference may be replaced by a silent platform default
- That a re-presentation preference is permission to deliver — permission is Operational Trust's
  (**P32**)
- That Follow-Me media eligibility governs Communication re-presentation — they are separate

---

## What Continuity will never do

- Decide whether a transfer happens
- Establish whether music is already playing (Truth)
- Grant authority to displace another person's session (Operational Trust)
- Own obligations (Stewardship)
- Perform playback
- Own Communications, delivery decisions, delivery surfaces, or delivery history (Concierge)
- **Formulate or present a recommendation** — *Continuity feeds Concierge; Continuity does not choose*
- **Own another responsibility's history**, however personal that history is
- **Hold a second copy of source-owned content** in order to explain it later (**DL-46**)

---

## Uncertainty and unknown representation

Blocking is expressed with attribution rather than as a bare boolean:

```
transfer_eligible: false
blocked_by:        operational_trust
reason:            destination_room_mode_prohibits_incoming_media
fact_reference:    primary_bedroom.mode = nighttime
```

---

## Failure and degradation behavior

| Condition | Behavior |
|---|---|
| Platform restart during an active session | Do not fabricate a session; re-establish only what is verifiable; offer resume where eligible |
| A room transition is missed | Do not retroactively transfer; treat the newly observed Room as current and record the gap |
| A configured speaker group is partially unavailable | Apply the configured partial-availability policy; record which members were unavailable |
| Preferences unavailable | State that the preference could not be read; never substitute a platform default silently |
| Two sessions claim one Room | Surface the conflict to Concierge; never merge or terminate unilaterally |

---

## Privacy constraints

Preferences, session history, and room-to-room movement patterns are personal data. Visibility is
governed by Operational Trust policy. Guests must not see residents' preferences or history.

---

## Explainability contributions

Every transfer, suppression, resume offer, and refusal records the intent, the eligibility outcome, the
blocking reason, and the responsibility that supplied it.

A suppressed transfer must be explainable as a deliberate outcome, not as a failure.

---

## Open decisions

| ID | Question |
|---|---|
| OD-24 | Session-merging algorithm when two people's sessions meet in one Room |
| OD-25 | Resume eligibility window defaults per experience class |
| OD-26 | Whether experience history is retained per person, per room, or both, and for how long |
| OD-27 | Whether concurrent same-class sessions in one Room are permitted by default |
| OD-48 | Re-presentation preference for outstanding Communications, and its relation to the Follow-Me preference family |
| OD-77 | Ownership of the association between a Person and an external service, account, calendar, mailbox, or media profile |
| OD-78 | Remembered-value classes and restoration semantics |
| OD-79 | Presentation preference scope and precedence |

## Related documents

- [../models/continuity.md](../models/continuity.md)
- [../models/experience-and-session.md](../models/experience-and-session.md)
- [operational-trust-contract.md](operational-trust-contract.md)
- [../scenarios/continuity-use-cases.md](../scenarios/continuity-use-cases.md)
- [../scenarios/follow-me-media.md](../scenarios/follow-me-media.md)
- [../architecture/adr-decoupled-voice-interaction-capability-architecture.md](../architecture/adr-decoupled-voice-interaction-capability-architecture.md) — a context-dependent voice follow-up must not be routed to a fast path that loses required Continuity state (drafted, pending #198)
