# Scenario: Nighttime Suppression

> **Document status: Canonical scenario.**
> Terminology: [../models/glossary.md](../models/glossary.md).
> Index: [README.md](README.md).

---

## Scenario 1 — Good Night in the Primary Bedroom

### What the household experiences

David says, "Good night," in the Primary Bedroom. The lights fade, the shades close, the doors lock, and
the house goes quiet.

For the rest of the night, the Primary Bedroom behaves differently.

### What each responsibility does

| Step | Responsibility | Action |
|---|---|---|
| 1 | Room Configuration | Resolves Room Context → Primary Bedroom |
| 2 | Identity | Asserts David, identity_confidence_band: Very High |
| 3 | Operational Trust | Confirms David may set Nighttime mode for this Room |
| 4 | Concierge | Executes the routine through governed interfaces |
| 5 | Truth | Establishes the fact: **the Primary Bedroom is in Nighttime mode** |
| 6 | Operational Trust | Nighttime restrictions now apply to this Room |

**Note the separation.** Concierge ran the routine. Truth holds the resulting mode as a fact. Operational
Trust interprets that fact as a restriction. The mode is not a Concierge variable.

---

## Scenario 2 — Music does not arrive

Tom walks into the Primary Bedroom with Follow-Me active. The music does not follow, and the home does
not ask.

| Step | Responsibility | Action |
|---|---|---|
| 1 | Truth | The Primary Bedroom is in Nighttime mode |
| 2 | Continuity | Transfer intent present; eligibility evaluated |
| 3 | Operational Trust | Nighttime prohibits incoming media **and** prohibits interruption |
| 4 | Concierge | Takes no action, and records a non-action trace |

```yaml
action_taken: none
action_suppressed: media.transfer
suppression_reason: destination_room_mode_prohibits_incoming_media
alternative_considered: ask_before_transfer (blocked by nighttime interruption policy)
```

> "I did not move the music into the Primary Bedroom because the room is in Nighttime mode, and
> Nighttime mode does not allow music to arrive on its own. I also did not ask, because Nighttime mode
> does not allow me to interrupt."

**Suppression is a deliberate outcome, not a failure.** The session remains active where it was.

---

## Scenario 3 — A reminder waits

Stewardship reports that a filter-replacement obligation became due at 11 PM.

| Step | Responsibility | Action |
|---|---|---|
| 1 | Stewardship | The obligation is `due`; significance is routine |
| 2 | Truth | The Primary Bedroom is in Nighttime mode; the Home is in quiet hours |
| 3 | Operational Trust | Routine notifications are suppressed during quiet hours |
| 4 | Concierge | **Defers** the notification to the morning, and records the deferral |

**Stewardship owns the obligation. It does not own the notification.** Stewardship did not decide to
wait; Concierge did, under Operational Trust policy.

---

## Scenario 4 — A safety condition does not wait

At 2 AM, a water-leak sensor reports.

| Step | Responsibility | Action |
|---|---|---|
| 1 | Truth | A leak is detected in the Utility area |
| 2 | Stewardship | The safety obligation is unmet; significance is high |
| 3 | Operational Trust | Nighttime suppression **does not apply** to safety-critical escalation |
| 4 | Concierge | Wakes the household, escalating through the permitted channel |

**Suppression policy is scoped by experience class.** Media may be suppressed while care escalations are
not. The ceiling rule restricts what is permitted; it does not silence what must be heard.

---

## Scenario 5 — The rest of the home is unaffected

David is asleep in the Primary Bedroom. Tom is awake in the Den, listening to music at normal volume.

Nothing about Nighttime mode in the Primary Bedroom restricts the Den.

**Room-scoped policy applies to the Room.** A Room mode is not a Home mode, and the two must not be
conflated. If the household wants a whole-home quiet period, that is a Home-scoped policy — and where
both apply, the most restrictive sets the ceiling.

---

## Scenario 6 — The mode cannot be established

The Primary Bedroom's presence and mode evidence is unavailable after a restart.

| Step | Responsibility | Action |
|---|---|---|
| 1 | Truth | Publishes the Room mode as `unknown`; does not retain the last value as current |
| 2 | Operational Trust | `unknown` is **not** permission; returns `undecidable` for incoming media |
| 3 | Concierge | Does not transfer; does not interrupt; records the reason |

> "I couldn't tell what mode the Primary Bedroom is in, so I left the music where it was."

**Unknown is never treated as false, and never treated as permission.** Both Truth and Operational Trust
fail closed.

---

## Rules demonstrated

1. A Room mode is a **Truth fact**, not a Concierge variable.
2. Restriction is interpreted by **Operational Trust**, not by whoever set the mode.
3. Suppression is a decision, and is traced.
4. Non-action is explainable.
5. Suppression scope depends on experience class — safety is not silenced.
6. Room-scoped policy does not leak into other Rooms.
7. Unknown fails closed everywhere.

---

## Production provenance — Household Automation Integration and Room Posture

**"Room Posture" is not a new concept.** It is the already-accepted **Room mode** demonstrated in every
scenario above: a Truth fact, scoped to a Room or Merged Room, declared as a "relevant mode" by Room
Configuration, established by Truth once Concierge orchestrates an authorized transition through
governed interfaces (Scenario 1), and interpreted — never implemented — by Operational Trust.
**Concierge orchestrates the transition; it does not own the mode, which remains Truth's fact exactly as
Scenario 1 states ("the mode is not a Concierge variable").** "Normal," "Quiet," "Nap," "Bedtime,"
"Movie," and "Entertaining" are
household vocabulary for Room mode values, exactly as "Nighttime" is in Scenario 1. None of them is a
canonical enumeration; Room Configuration's "relevant Room modes" are household-configured, not a fixed
HTBW list.

[production-behavior-catalog.csv](../reference-home/production-behavior-preservation/production-behavior-catalog.csv)
corroborates this independently: production's own Goodnight and Good Morning routines (**BHV-18**,
**BHV-19**) set an explicit `posture=night` / `posture=awake` value, separately from the household-
specific device actions (lights, shades, Sonos, AppleTV, kiosk dashboard) those routines also perform.
This is prior art for the household's own vocabulary, not a reason to adopt production's mechanism —
the device actions in BHV-17/18/19 remain exactly the kind of household-specific automation mechanics
this scenario already keeps outside Truth and outside Operational Trust.

### The Nursery Nap scenario, walked through existing authority

A caregiver says "It's nap time" (or triggers the equivalent kiosk action). **Nothing new is required**:

| Step | Responsibility | Action |
|---|---|---|
| 1 | Room Configuration / Contextual Vocabulary | Resolves Room Context → Nursery; resolves the household's "Nap" vocabulary to the governed mode-transition action, exactly as "Good night" resolves in Scenario 1 |
| 2 | Operational Trust | Confirms the speaker may set Nursery mode |
| 3 | Concierge | Executes the transition through governed interfaces |
| 4 | Truth | Establishes the fact: **the Nursery is in Nap mode** |
| 5 | *(household-owned, outside HTBW)* | The household's own Home Assistant automation, triggered by whatever representation of that fact the household's automation observes, closes shades, dims lights, and starts white noise |

**HTBW does not own step 5.** [home-assistant-boundary.md](../architecture/home-assistant-boundary.md),
*Native automations, scripts, and scenes*, already states this generally: *"HTBW does not own, absorb,
replace, or require the rewriting of any native automation, script, scene, or blueprint"* — what HTBW
observes of step 5 is a **Domain Event**, never a fabricated Decision Trace, because HTBW did not decide
the shade, light, or white-noise actions.

**Voice, kiosk, and a household automation's own request converge on the same governed transition** at
step 3, regardless of which interaction surface or source supplied it — Concierge orchestrates the
identical Room-mode-setting action, and **DL-73**'s Behaviour Source enumeration already classifies
*direct resident interaction*, *native automation*, and *manual physical interaction* as distinct,
equally legitimate sources without special-casing any of them.

### Time is not mode

Scenario 3 and Scenario 5 already establish this: quiet hours are a temporal, Home-scoped policy input;
a Room's mode is a Truth fact the household (or a governed automation request) sets explicitly. A
Nursery entering Nap mode in the afternoon, or a Den remaining in an Entertaining-equivalent mode late at
night, follows without exception or special case — **time informs policy interpretation; it does not
silently become the mode.**

### Interruption/DND is not a second concept

No standalone "Do Not Disturb" object is introduced, and none is required. Scenario 2 and Scenario 3
already show the accepted mechanism: Operational Trust interprets a Room mode (Nighttime) as an
interruption restriction, on the same **Risk-versus-Interruption** axis
([operational-trust-contract.md](../contracts/operational-trust-contract.md), **DL-76**) that governs
every other interruption decision. A household that configures a Nap mode to restrict interruption in
the Nursery uses this identical mechanism — **a new mode value, not a new policy concept.** Experience
Family 4's Communication and Delivery authority already consumes exactly this kind of governed context
without modification; Room mode is additional contextual evidence to that existing pipeline, never a
parallel notification path.

### Household Posture is an ordinary Home-scoped Truth Fact

**No distinct "Household Posture" model is required.** Scenario 5 already anticipates this: *"If the
household wants a whole-home quiet period, that is a Home-scoped policy."* [truth.md](../models/truth.md)
already establishes **Home** as a Fact Subject — *"the outermost governed scope"* — using the identical
Fact model, lifecycle, and confidence/provenance rules as a Room-scoped Fact. A household concept such as
Away, Vacation, or Guest is represented the same way a Room mode is: as a Home-scoped Truth Fact, set
through a governed routine and interpreted by Operational Trust, not as a second model invented for
symmetry with Room mode.

### Household automation read/write integration remains OD-81, not decided here

Whether, and how, Room mode (or any other HTBW-governed semantic state) is **published** as a native Home
Assistant service, event, or entity a household automation may read, and whether a household automation
may **request** a governed mode transition through a public surface, is the exact, already-identified,
still-open question: **OD-81 — HTBW Capability Exposure and Self-Consumption** (#159). OD-81's own
recorded reasoning already anticipates this case precisely: *"where an HTBW concept benefits from native
visibility, state, targeting, or automation, a native representation is created or used in preference to
a parallel hierarchy — and that representation is a projection, never a second authority"* (**DL-31**,
quoted in OD-81). This review supplies Room mode as a concrete, evidenced case for OD-81 and does not
pre-decide it: no service name, entity platform, or event schema is selected here, consistent with OD-81's
own closure boundary.

### Household-created automation and script explainability is already sufficient

**No new Explainability, provenance, or automation-registration integration point is required.**
[decision-trace.md](../models/decision-trace.md) already states the controlling rule: *"A Decision Trace
exists only where HTBW decided. Where a resident, a native automation, a script, a scene, or an external
integration caused a change, there is no HTBW decision and therefore no trace... What occurred is
recorded as a Domain Event with behaviour attribution instead."* [home-assistant-boundary.md](../architecture/home-assistant-boundary.md),
*Native automations, scripts, and scenes*, already specifies the available evidence in full: the
automation/script/scene involved, the invoked action, the resulting state transition, the triggering
event, Home Assistant's Context/Parent Context/User Context identifiers, and the related entity, device,
Area, Room, or person — *"where the platform does not supply it, it is not inferred."*
[why-did-this-happen.md](why-did-this-happen.md) Scenario 21 and Scenario 63 already demonstrate exactly
the Nap-to-shade causal chain this review tested, including the non-event case: a sibling
`automation_triggered` event either exists (and is cited) or does not (and the trace says so), never a
fabricated cause. **OD-64** remains the narrow, already-identified residual — verifying the precise
Recorder-events evidence surface — not a gap in the attribution architecture itself.

---

## Related documents

- [../models/truth.md](../models/truth.md)
- [../models/operational-trust.md](../models/operational-trust.md)
- [../architecture/failure-and-degradation.md](../architecture/failure-and-degradation.md)
- [why-did-this-happen.md](why-did-this-happen.md)
- [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md)
- [../models/decision-trace.md](../models/decision-trace.md)
- [../contracts/operational-trust-contract.md](../contracts/operational-trust-contract.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md) — **OD-81**, HTBW capability
  exposure and self-consumption
- [../reference-home/production-behavior-preservation/production-behavior-catalog.csv](../reference-home/production-behavior-preservation/production-behavior-catalog.csv)
