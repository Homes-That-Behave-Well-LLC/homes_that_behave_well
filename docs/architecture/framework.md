# HTBW Framework Responsibilities

> **Document status: Canonical (constitutional).**
> Subordinate only to [north-star.md](north-star.md).
> Terminology: [docs/models/glossary.md](../models/glossary.md).

This document defines each framework responsibility: what it owns, what it consumes, what it
provides, and — critically — what it does **not** own.

**Structure (DL-153).** The **BehavesWell Framework** has **six stages** — Truth, Identity, Operational
Trust, Stewardship, Continuity, Concierge — each of which is an architectural responsibility.
**BehavesWell Core** applies them over **Layer 0 Foundation**, the platform substrate. Foundation is
**not** a seventh Framework stage. Together they form the **seven-layer BehavesWell Core architectural
stack**, presented below from Layer 0 upward. Every ownership statement in this document is unchanged
by DL-153; only the presentation order changed. "HTBW" in this document is pre-DL-153 shorthand (see
[../models/glossary.md](../models/glossary.md)). See
[adr-behaveswell-framework-foundation-core-edition-and-context-identity.md](adr-behaveswell-framework-foundation-core-edition-and-context-identity.md).

Every responsibility has a contract in [docs/contracts/](../contracts/README.md) and one or more
models in [docs/models/](../models/glossary.md).

---

## Layer 0 — Foundation — *What platform model and native capabilities provide the substrate?*

Foundation is Layer 0, the substrate on which BehavesWell Core applies the six Framework stages. In
the current edition, **BehavesWell Core, Home Assistant Edition**, Home Assistant supplies the native
substrate and remains authoritative for its native concepts; the Foundation-owned models below are
BehavesWell Core's governed extensions of it. Foundation's guarantee to the six stages is *what exists,
and how we describe it*.

Foundation establishes the shared models, vocabulary, contracts, identifiers, provenance, temporal
conventions, and configuration primitives used by every other responsibility.

**Foundation owns the canonical definitions of:**

Home, Physical Room, Room, Merged Room, Person, Pet, Asset reference, Relationship, Evidence,
Assertion, Fact, Preference, Policy, Obligation, Experience, Session, Decision, Decision Trace,
Communication, Delivery, Delivery Attempt, Delivery Surface, Role, Caretaker relationship.

> **"Notification" is superseded as an HTBW domain term.** The canonical term is **Communication**,
> and a notification is one delivery outcome among several. See
> [../models/communication.md](../models/communication.md) and **DL-28**.

**Foundation also owns Room Configuration** — the interaction-definition model that declares
participation, exposure, contextual vocabulary, Room Help, and composite-fact inputs. See
[../models/room-configuration.md](../models/room-configuration.md).

**Foundation also owns the shared temporal model** — the temporal, version, change-record, snapshot,
correlation, and provenance conventions every responsibility uses to record its own history. See
[../models/temporal-record.md](../models/temporal-record.md).

**Foundation also owns the communication model** — the definitions of Communication, Delivery,
Delivery Attempt, Delivery Surface, Urgency, and the delivery-outcome states. **Foundation owns no
Communication.** Any responsibility may originate one; Concierge decides and records delivery. See
[../models/communication.md](../models/communication.md).

**Foundation does not own every fact or behavior merely because it defines the shared model.**

Specifically, Foundation defines what a *Fact* is; **Truth** decides what is factual now.
Foundation defines what an *Obligation* is; **Stewardship** decides which obligations exist.
Foundation defines what a *Policy* is; **Operational Trust** decides which policies apply.
Foundation defines what a *Change Record* is; **each responsibility owns the history of its own
records**.

Contract: [../contracts/foundation-contract.md](../contracts/foundation-contract.md)

---

## Stage 1 — Truth — *What is actually true now?*

Truth is a **first-class authoritative fact engine**. Truth is not a section of Foundation.

**Truth consumes** evidence and assertions from devices, sensors, assets, Identity, voice events,
BLE events, media systems, calendars where authorized, environmental sources, Room Configuration,
and other governed sources.

**Truth owns authoritative facts**, including presence, occupancy, environmental, engagement,
device, contextual, room-state, active-room-mode, and current-activity facts; Composite Facts;
evidence freshness; fact confidence; provenance; and fact validity and expiration.

**Truth is also the system of record for historical Facts.** Operational expiration removes a Fact
from *what is true now*; it does not delete *what was true then*. Truth owns Fact history and the
eight Fact lifecycle transitions. No consumer may maintain a competing or re-derived Fact history.
See **P28** in [principles.md](principles.md).

Examples: *Tom is present in the Den. The Living Space is occupied. A conversation is active. Music
is already playing. The television is in use. The Primary Bedroom is in Nighttime mode. The room
temperature is 72 degrees. The garage door is open. The room moved from occupied to unoccupied.*

Truth may combine multiple eligible contributing sensors into a single **Composite Fact**. "Composite
Fact" concerns combining evidence and is unrelated to the superseded term "Composite Room" (now
**Merged Room**), which concerns combining Physical Rooms.

**Truth must not:** trigger actions, control devices, make resident-facing behavioral decisions, own
preferences, own authority or permission, hide uncertainty, or automatically convert weak evidence
into a definitive fact.

Model: [../models/truth.md](../models/truth.md)
Contract: [../contracts/truth-contract.md](../contracts/truth-contract.md)

---

## Stage 2 — Identity — *Who do we believe this is?*

**Voice Identity is not a separate product boundary in HTBW Core.** The responsibility is
**Identity**, and **voice is one identity-evidence source**.

**Identity may consume:** voice matching, BLE devices, assigned phones, assigned watches, assigned
tablets, Home Assistant companion-app signals, presence trackers, Wi-Fi associations,
room-transition evidence, vehicle associations, future identity sources, and explicit household
enrollment.

**Identity owns:** the person identity profile; associations between a person and identity-evidence
sources; voice-profile references; assigned-device relationships used for identity; candidate-person
assertions; identity confidence; identity evidence attribution; enrollment, revocation, and identity
diagnostics; and privacy treatment of identity evidence.

**Identity produces assertions**, for example:

```
candidate_person: Tom
confidence:       0.94
evidence:         voice + BLE + assigned phone
```

**Identity does not determine:** authoritative room occupancy, authoritative presence in a
contextual space, what activity is occurring, what should happen, what a person prefers, or what a
person is permitted to do.

Model: [../models/person-and-identity.md](../models/person-and-identity.md)
Contract: [../contracts/identity-contract.md](../contracts/identity-contract.md)

---

## Stage 3 — Operational Trust — *What is allowed?*

**Operational Trust owns:** roles; permissions; authority; privacy boundaries; consent;
authentication requirements; identity-confidence thresholds; action-risk classifications; explicit /
assisted / autonomous ceilings; confirmation requirements; override rights; priority policy;
conflict policy; guest-safe behavior; child-safe behavior; service-provider behavior; caretaker
authority; security authority; who may disarm an alarm; who may unlock a door; who may view or hear
private information; who may access calendars, messages, email, or history; who may override whom;
whether an action must be refused; whether an action must be confirmed; room-mode restrictions;
privacy modes; quiet-hour restrictions; safety and security precedence; and decision-trace
visibility and retention policy.

**Operational Trust does not determine who a person is.** It consumes Identity and Truth when
evaluating whether the requirements for an action have been met.

### Autonomy model

| Level | Meaning |
|---|---|
| Explicit | The home acts only after direct human instruction. |
| Assisted | The home may suggest, or ask for confirmation. |
| Autonomous | The home may act without asking when all required facts, permissions, confidence thresholds, and policies are satisfied. |

A broad autonomy setting establishes a **ceiling**. More specific person, room, experience, asset,
or action policies may be **more restrictive**. A narrower policy must never silently become more
permissive than the governing ceiling.

Model: [../models/operational-trust.md](../models/operational-trust.md)
Contract: [../contracts/operational-trust-contract.md](../contracts/operational-trust-contract.md)

---

## Stage 4 — Stewardship — *What matters, and what must be cared for?*

Stewardship is a meaningful responsibility. It is **not** a synonym for inventory.

Stewardship asks: what matters, what must be cared for, what obligations exist, and who is
accountable?

**It asks those questions *for* the household, from what the household has declared — not *about* the
household.** The household declares what matters and what caring for it means; Stewardship represents
those care expectations, evaluates authoritative observations against them, and creates governed care
obligations when attention is required. **No universal HTBW hierarchy of importance exists**, and
**people and pets are never Assets**, though both may carry care obligations.

**Stewardship owns** significance, care, obligations, lifecycle accountability, and ongoing
responsibility for assets, the home, rooms and environmental conditions, people (where appropriate
and consented), pets, vehicles, consumables, services, and safety-related conditions.

Representative obligations: maintenance and service plans, service schedules, service and
maintenance history, warranty milestones, replacement planning, caretaker assignment, medication
reminders, vet appointments, pet medication/food/walk obligations, environmental limits that must be
protected, filter replacement, inspection schedules, the home-maintenance calendar,
caretaker-calendar projection, overdue obligations, escalation of unmet obligations, a garage door
that should be secured after a defined time, and windows that should not remain unlocked under
defined conditions.

**Stewardship owns the obligation. Stewardship does not own the resulting Communication or physical
action.** **Stewardship never calls a Home Assistant service.** Where the household has authorised it,
an executor may resolve a condition before anyone is told anything — the executor acts, and
Stewardship observes whether the care condition returned to an acceptable state.

Stewardship also owns the **single escalation ladder** — changing *who* is accountable when an
obligation remains unmet (**OD-22**). Repeating a delivery to the *same* audience is **retry**, is a
Concierge concern, and is never called escalation.

Worked separation:

| Responsibility | Statement |
|---|---|
| Truth | The garage door is open, and the current time is after 10 PM. |
| Stewardship | The home's security-care obligation is unmet. |
| Operational Trust | Automatic closing is permitted, prohibited, or requires confirmation. |
| Concierge | Close, ask, convey, defer, or escalate — and explain. |

A second worked separation, for outbound communication under **P32**:

| Responsibility | Statement |
|---|---|
| Truth | Water is detected under the sink, and guests are present in the Den. |
| Stewardship | The home's safety-care obligation is unmet. |
| Operational Trust | Interrupting is permitted; an audible Den announcement is not. |
| Concierge | Deliver to a personal surface, suppress the Den announcement, record both, explain both. |

Model: [../models/stewardship.md](../models/stewardship.md)
Contract: [../contracts/stewardship-contract.md](../contracts/stewardship-contract.md)

---

## Stage 5 — Continuity — *What should be remembered, restored, resumed, or transferred?*

Continuity is more than storage and more than a preference list.

**Continuity owns or governs:** person-scoped preferences; room-scoped experience settings; active
experience state; experience history; resume state; transfer state; Follow-Me intent; Follow-Me
enabled/disabled state; ask-before-transfer preference; never-transfer preference; active personal
media sessions; active room experiences; session ownership; session participants; origin room;
current room; transfer eligibility; resume eligibility; blocking state supplied by other
responsibilities; and the experience lifecycle.

| Scope | Examples |
|---|---|
| Person-scoped | Preferred artist, genre, album, playlist; personal media defaults; personal Follow-Me setting; a request to have music follow; current personal media session |
| Room-scoped | Last song played in the room; last genre played in the room; music volume; duck volume; TTS volume; current room experience; room-specific resume state |

**Preserved rule:** preferred artist, genre, album, and playlist are **person-scoped**, not
person-plus-room-scoped, so preferences may follow a person across rooms.

Continuity must support explicit, assisted, and autonomous experience continuity.

**Continuity provides preferences, active state, and transfer or resume intent. Continuity does not
choose the final action.**

Models: [../models/continuity.md](../models/continuity.md),
[../models/experience-and-session.md](../models/experience-and-session.md)
Contract: [../contracts/continuity-contract.md](../contracts/continuity-contract.md)

---

## Stage 6 — Concierge — *What should happen now?*

Concierge is the orchestration and resident-interaction responsibility.

**Concierge consumes:** resolved room context; resolved vocabulary targets; asset capabilities;
Identity assertions; Truth facts; Continuity preferences; active experience state; Stewardship
obligations; Operational Trust decisions and policies; the current room mode; the existing room
experience; and explicit human intent.

**Concierge owns:** interaction orchestration; intent handling after contextual target resolution;
decision evaluation; conflict resolution; experience coordination; action planning; routing;
execution requests; resolution of a Communication audience to delivery surfaces; the decision to
deliver, suppress, defer, or retry, and the record of every resulting state transition; questions and
suggestions; the resident-facing response; Decision Trace creation; and human-readable explanations.

**Concierge owns delivery, not communication significance.** It does not decide that something
matters, who may hear it, or what it is entitled to interrupt — those belong to the originator and to
Operational Trust. See [../models/communication.md](../models/communication.md).

**Concierge does not own:** asset inventory; authoritative asset identity; person identity; raw
identity evidence; authoritative Truth; personal preferences; Stewardship obligations; security
permissions; room membership; room vocabulary definitions; or runtime discovery of which assets a
household meant when an explicit room mapping exists.

Concierge resolves competing preferences, sessions, eligible actions, and policies.

**Concierge does not resolve "competing Truths" by inventing a preferred fact.** If evidence or facts
conflict, Truth preserves or resolves the uncertainty according to its own contract.

> **Concierge orchestrates. It does not own everything it consumes.**

Contract: [../contracts/concierge-contract.md](../contracts/concierge-contract.md)

---

## History ownership

Every responsibility owns the history of its own records. **There is no History responsibility, no
central history owner, no central snapshot owner, and no central preservation-hold enforcer.**

| History | Owner |
|---|---|
| Fact history; Fact lifecycle transitions | **Truth** |
| Identity Assertion history; identity-consent lifecycle history — evidence classes and reason codes only, never biometric internals | **Identity** |
| Obligation, maintenance, service, significance, and caretaker-assignment history | **Stewardship** |
| Preference, session, resume, and transfer history | **Continuity** |
| Policy, authorization-decision, privacy-policy, retention-policy, and preservation-hold authority history | **Operational Trust** |
| Room and Merged Room membership, participation, not-selected, deliberately-excluded, exposure, vocabulary, voice-assistant assignment, Composite Fact contributor-selection, and capability-definition history | **Room Configuration** (Foundation) |
| Decision history, through Decision Traces | **Concierge** |
| The temporal, version, change-record, snapshot, correlation, and provenance **models** | **Foundation** |

**Communication delivery history is decision history and is therefore already owned by Concierge.**
No row is added for it, and **no Communication, Messaging, Inbox, Delivery, or Escalation
responsibility exists**. See [../models/communication.md](../models/communication.md).

**Historical Explainability assembles these records.** It owns no store and creates no eighth
responsibility. See [../models/temporal-record.md](../models/temporal-record.md) and
[adr-historical-explainability-and-historical-truth.md](adr-historical-explainability-and-historical-truth.md).

---

## The HTBW asset model and the standalone product

The standalone **Asset Intelligence** integration remains a separate released product with its own
lifecycle. It is not merged, deprecated, or made a compatibility requirement by this framework.

Within HTBW, the **asset model** is descriptive knowledge owned by Foundation, and **significance and
care** are owned by Stewardship. See [../models/asset.md](../models/asset.md).

Home Assistant Device, Home Assistant Entity, HTBW Asset, Person, Pet, Room, and Service are
**distinct object kinds** and must never be treated as the same object. Their distinctions are
defined in [../models/glossary.md](../models/glossary.md) and
[home-assistant-boundary.md](home-assistant-boundary.md).

---

## Related documents

- [dependency-view.md](dependency-view.md)
- [runtime-sequence.md](runtime-sequence.md)
- [behavioral-governance.md](behavioral-governance.md)
- [explainability.md](explainability.md)
- [../models/temporal-record.md](../models/temporal-record.md)
- [../contracts/README.md](../contracts/README.md)
