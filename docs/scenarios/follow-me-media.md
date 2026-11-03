# Scenario: Follow-Me Media

> **Document status: Canonical scenario.**
> Terminology: [../models/glossary.md](../models/glossary.md).
> Index: [README.md](README.md).

---

## Scenario 1 — The transfer happens

### What the household experiences

Tom is in the Office listening to jazz. He says, "Have the music follow me," and walks to the Den. The
jazz is playing in the Den when he arrives.

### What each responsibility does

| Step | Responsibility | Action |
|---|---|---|
| 1 | Room Configuration | Resolves Room Context → Office |
| 2 | Identity | Asserts candidate Tom, identity_confidence_band: High, from voice + BLE + assigned phone |
| 3 | Continuity | Records Follow-Me intent on Tom's active jazz session; origin Room = Office |
| 4 | Truth | Later establishes: Tom is present in the Den; the Office is now unoccupied; the Den has no active session |
| 5 | Continuity | Evaluates transfer eligibility → eligible; destination endpoints configured and available |
| 6 | Operational Trust | Permits media transfer to the Den at Autonomous level |
| 7 | Concierge | Transfers playback and records the trace |

### What made it eligible

- Follow-Me enabled for the session
- Identity resolved above threshold
- The room transition was unambiguous — Office and Den both known, and different
- Manual-stop protection not active, cooldown not active
- The Den has configured, valid, available playback targets

**Follow-Me is a policy-governed handoff, not motion-triggered movement.**

### What the home can say afterwards

> "I moved the jazz to the Den because you asked the music to follow you, I recognised you here, and
> the Den was free."

---

## Scenario 2 — The transfer is suppressed

### What the household experiences

Later that night, Tom walks from the Office into the Primary Bedroom. The music does not follow. The
home says nothing.

### What each responsibility does

| Step | Responsibility | Action |
|---|---|---|
| 1 | Truth | Tom is present in the Primary Bedroom; the Primary Bedroom is in Nighttime mode |
| 2 | Continuity | Transfer intent is present; evaluates eligibility |
| 3 | Operational Trust | Nighttime mode prohibits incoming media; it also prohibits interruption |
| 4 | Continuity | Records `transfer_eligible: false`, `blocked_by: operational_trust` |
| 5 | Concierge | Takes no action, and records a non-action trace |

**The session remains active in the Office. A suppressed transfer is not a failure.**

### What the home can say if asked

> "I did not move the music into the Primary Bedroom because the room is in Nighttime mode, and
> Nighttime mode does not allow music to arrive on its own. I also did not ask, because Nighttime mode
> does not allow me to interrupt."

See [nighttime-suppression.md](nighttime-suppression.md).

---

## Scenario 3 — Assisted settlement of a pending Follow-Me intent

### What the household experiences

Tom said "follow me with the documentary" this morning in the Primary Bedroom, without naming a
destination. This evening he walks into the Den and says, "Resume it here." The home asks: "Move your
documentary here?"

### What each responsibility does

| Step | Responsibility | Action |
|---|---|---|
| 1 | Identity | Asserts Tom, identity_confidence_band: High |
| 2 | Truth | Tom is present in the Den; the Den has no active session |
| 3 | Continuity | A Pending Follow-Me intent exists for Tom's documentary (resolved — **DL-128**); Tom's explicit "resume it here" supplies the destination |
| 4 | Operational Trust | Media in the Den is permitted at **Assisted** level for this class |
| 5 | Concierge | Proposes; acts only on confirmation |

The mode was Assisted, not Autonomous. **Which mode applies is determined by Operational Trust, not by
Continuity.** **Concierge never proposes this unprompted — the Pending intent existed only because Tom
explicitly established it this morning (resolved — DL-128, OD-25); mere elapsed time since he left the
Primary Bedroom is never, by itself, a reason to offer anything.**

---

## Scenario 4 — Movement inside a Merged Room

### What the household experiences

Music is playing in the Living Space. Tom walks from the Kitchen to the Dining area. Nothing happens.
Nothing needs to.

### Why

The Kitchen and the Dining area are constituent Physical Rooms of the **Living Space** Merged Room.

> **Movement between constituent Physical Rooms inside the same Merged Room is neither a transfer nor a
> resume, because no Room Context changed.**

There is no special orchestration path for merged rooms. A Room and a Merged Room behave identically.

---

## Scenario 5 — A missed room transition

### What the household experiences

Tom moves from the Office to the Den, but the Office presence sensor never reported him leaving.

### What each responsibility does

| Step | Responsibility | Action |
|---|---|---|
| 1 | Truth | Observes Tom present in the Den; records that the Office transition was not observed; records the gap |
| 2 | Continuity | Treats the Den as the current Room; **does not retroactively transfer** |
| 3 | Concierge | Acts on the current state, and the gap is available in the trace |

**Do not invent a retroactive transition.** Treat the newly observed Room as current and record the gap.

---

## Scenario 6 — Partial availability at the destination

### What the household experiences

The music follows Tom into the Living Space, but one of the three configured Living speakers is offline.
The music plays on the other two, and the home mentions it.

### What each responsibility does

| Step | Responsibility | Action |
|---|---|---|
| 1 | Room Configuration | Declares the configured speaker group |
| 2 | Truth | Reports one member unavailable |
| 3 | Continuity | Applies the configured partial-availability policy; records which members were unavailable |
| 4 | Concierge | Plays on the available members and reports the shortfall |

> "The music followed you here, though one of the Living Space speakers isn't responding."

---

## Blocking reasons that must be representable

| Reason | Supplied by |
|---|---|
| Follow-Me disabled, or never-transfer set | Continuity |
| Identity unresolved, ambiguous, or below threshold | Identity |
| Room transition ambiguous or missed | Truth |
| Origin or destination Room unavailable | Truth |
| Destination Room mode prohibits incoming media | Operational Trust |
| An existing experience in the destination has priority | Operational Trust |
| Another person's session would be displaced without authority | Operational Trust |

**Every block is a reason, and every reason reaches the Decision Trace.**

---

## Related documents

- [../models/continuity.md](../models/continuity.md)
- [../models/experience-and-session.md](../models/experience-and-session.md)
- [../contracts/continuity-contract.md](../contracts/continuity-contract.md)
- [multi-person-conflict.md](multi-person-conflict.md)
