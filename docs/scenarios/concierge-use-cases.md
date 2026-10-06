# Concierge Human Outcome Use Cases

> **Document status: Canonical scenario.**
> Terminology: [../models/glossary.md](../models/glossary.md).
> Owning responsibility: **Concierge**. Contract:
> [../contracts/concierge-contract.md](../contracts/concierge-contract.md).
> **This document is architecture and outcome guidance. It is not proof of implementation.**

---

## Purpose

**The Concierge question is: given the governed context presently available to the home, what is the
most helpful appropriate next response?**

These twenty use cases record the **human outcomes** Concierge is expected to coordinate, and trace
each one to the responsibilities, decisions, and open questions that govern it. They exist so that the
architecture can be tested against what a household actually experiences.

**They are not a feature list, a roadmap commitment, or evidence that anything is built.**

---

## How to read the maturity classification

**HTBW Core contains no implementation code.** This repository is architecture. Where a standalone
released product implements something resembling a use case, that is recorded as **product evidence**
and never as HTBW implementation — **DL-19** creates no compatibility requirement in either direction.

| Class | Meaning |
|---|---|
| **A — Implemented** | Repository code and accepted evidence demonstrate the behaviour exists. **No use case below carries this classification, because HTBW Core has no code.** |
| **B — Architecturally supported** | Accepted architecture and contracts support the behaviour; the complete experience is not implemented |
| **C — Planned** | An approved roadmap item or implementation issue represents it |
| **D — North Star** | An intended future outcome; implementation is not authorised |
| **E — Blocked** | Depends on unresolved architecture, including an open decision |
| **F — Research required** | Plausible, but repository evidence is insufficient to adopt it |

---

## What Concierge is, and is not

**Concierge consumes governed inputs and coordinates experience delivery.** It is **not** an automation
engine, a rules engine, a source of Truth, an Identity resolver, an authorisation authority, an owner
of assets or obligations, an owner of durable memory, a prediction engine, or an unrestricted agent.

The nine **permitted outcomes** — act, propose then act on confirmation, ask for disambiguation, choose
the benign action, defer, convey without acting, escalate, do nothing and be able to say why, refuse
and explain — are already accepted in
[../contracts/concierge-contract.md](../contracts/concierge-contract.md) §7, together with sixteen
hard prohibitions. **Nothing in this document adds to either list.**

### Two responsibility names used in Episode 8 that HTBW does not have

**There is no Experience Delivery responsibility and no Communication or Messaging responsibility.**
[../governance/authority-order.md](../governance/authority-order.md) states as a non-negotiable
constraint that *"there is no Communication, Messaging, Inbox, Delivery, or Escalation responsibility;
no central delivery owner; no central inbox owner; and no second escalation ladder."* Delivery is
**Concierge's**, and a Delivery Surface is a platform concern, not a responsibility.

**There is no Intelligence responsibility.** Where a use case below says a calculation or comparison is
performed, the question of whether a reasoning provider may be consulted at all is **OD-67**, and a
provider's output *never silently becomes a Fact*.

---

## Doctrine reviewed from the Episode 8 narrative

Ten candidate principles were tested against accepted architecture. **None is elevated to
constitutional status**, because seven are already accepted in substance and elevating a restatement
would create two authorities for one rule.

| # | Candidate principle | Disposition |
|---|---|---|
| 1 | The home should know the minimum information necessary to help | **Already accepted.** [../architecture/privacy.md](../architecture/privacy.md) minimisation; **P27** is a floor *and* a ceiling. Retained as narrative |
| 2 | The home needs enough governed context, not everything | **Already accepted.** [../architecture/context-before-intent.md](../architecture/context-before-intent.md); *context before intent* in [../architecture/runtime-sequence.md](../architecture/runtime-sequence.md); concierge-contract §10. Retained as narrative |
| 3 | Information may come from many places. Judgment belongs at home | **Concierge guidance — recorded here, not elevated.** No accepted document states that *information source is not decision location*. It is recorded below as guidance because elevating it would preempt **OD-07** and **OD-67**, which own locality and provider strategy |
| 4 | Connectivity does not relocate responsibility | **Concierge guidance — recorded here, not elevated.** Same reason, and the supporting platform facts are unverified — see UC5 and **#146** |
| 5 | A resident or guest chooses what the home may remember about them | **Already accepted.** [../models/person-and-identity.md](../models/person-and-identity.md) *participation is optional and requires consent*; **DL-33**; identity-contract *declining is not exclusion*. Retained as narrative |
| 6 | Recognition does not imply permission | **Already accepted.** *Identity is not authentication and not authorization* ([../architecture/adr-identity-replaces-voice-identity-boundary.md](../architecture/adr-identity-replaces-voice-identity-boundary.md)); **DL-36** *presentation is not personalization*; **DL-39** a band carries no access meaning. Retained as narrative |
| 7 | The best response may be to wait, ask, recommend, route differently, or do nothing | **Already accepted, near-verbatim.** concierge-contract §7. Retained as narrative |
| 8 | Concierge should not create more notifications; it should recognise when assistance becomes useful | **Split.** The first half is **already accepted** — **DL-28** makes *Notification* not an HTBW term. The second half is **Concierge guidance recorded here**, and is the doctrinal seed of UC6 and UC7 |
| 9 | Providers produce evidence. HTBW produces decisions | **Already accepted for voice as DL-50.** **Not generalised here.** Generalising it to every provider class touches **OD-66** and **OD-67** and is not this document's to decide |
| 10 | The right response, channel, audience, and moment matter as much as the information | **Already accepted.** **DL-28** communication is separate from delivery; **DL-29** permission to act is not permission to announce; concierge-contract §3 |

### The three statements recorded as Concierge guidance

> **Information may come from many places. Judgment belongs at home.**
> A household may deliberately connect authoritative external services. Consuming a record from one
> does not move an HTBW decision outside the home, and does not transfer ownership of that record to
> HTBW (**DL-31**). *Local first* does not mean *cloud never*; it means the **source of information**
> and the **location of judgment** are separate questions.

> **Connectivity does not relocate responsibility.**
> That a resident can reach the home from elsewhere says nothing about where the home's reasoning
> happens or what leaves it. **This statement requires platform verification before it is relied
> upon** — see UC5.

> **Concierge recognises when assistance becomes useful; it does not manufacture reasons to speak.**
> A governed opportunity is a moment when existing, already-governed information becomes more useful
> than it was a moment ago. It is never an excuse to originate a Communication that nothing owns.

**These are guidance, subordinate to canon.** Where they conflict with an accepted decision, the
accepted decision prevails.

---

## The twenty use cases

| # | Title | Maturity | Principal blocker |
|---|---|---|---|
| **C1** | Conversation-aware interruption management | **D — North Star** | Passive monitoring unauthorised; **OD-84** |
| **C2** | Known and unidentified conversation participants | **E — Blocked** | **OD-84** (#169) |
| **C3** | Transient knowledge and purpose-limited forgetting | **B — Architecturally supported** | Values are household configuration under **DL-59** |
| **C4** | Local-first decision making with connected cloud sources | **B — Architecturally supported** | **OD-07**, **OD-67** for the edges |
| **C5** | Home Assistant remote access education | **F — Research required** | Platform verification (**#146**) |
| **C6** | Shopping-list opportunity recognition | **E — Blocked** | **OD-77** (#148) |
| **C7** | EV readiness and preventive guidance | **E — Blocked** | **OD-77**; no travel-demand governance |
| **C8** | Home battery backup and resource optimisation | **E — Blocked** | **OD-51**, **OD-67** |
| **C9** | Guest capability discovery and vocabulary education | **B — Architecturally supported** | **OD-59**, **OD-13** |
| **C10** | Guest-asset interpretation and household storytelling | **E — Blocked** | **OD-52** (#100) |
| **C11** | Asset knowledge becomes household action | **E — Blocked** | **OD-77**, **OD-23** |
| **C12** | Outcome-based room comfort | **B — Architecturally supported** | **OD-04**, **OD-78** |
| **C13** | First-visit guest consent and introduction | **E — Blocked** | **OD-06** (#94) |
| **C14** | Returning-guest hospitality | **E — Blocked** | **OD-06**, **OD-15** |
| **C15** | Guest relationship learning | **E — Blocked** | **OD-06**, **OD-28**, **OD-65** |
| **C16** | Multi-party relationship-aware disclosure | **E — Blocked** | **OD-84**, **OD-71** |
| **C17** | Channel selection across the household experience | **E — Blocked** | **OD-43** (#113) |
| **C18** | Importance, urgency, escalation, and follow-up | **E — Blocked** | **OD-46**, **OD-51**, **OD-53**, **OD-22** |
| **C19** | Explainability | **B — Architecturally supported** | **OD-30** for surfaces |
| **C20** | Do nothing as a valid Concierge response | **B — Architecturally supported** | None |

**Six of twenty are architecturally supported today. One is North Star. One requires research. Twelve
are blocked, and every blocker is an existing open decision.** No use case is implemented.

---

# C1 — Conversation-aware interruption management

## Human outcome

Tom and David are talking in the Den. Something important arrives. The home notices that people are
speaking, decides that talking over them is the wrong thing to do, sends the detail quietly to Tom's
phone, and — once the room is quiet again — says only *"Tom, I sent an important update to your
phone."* **It never knows what they were talking about, and never keeps a record that they talked.**

| Field | Statement |
|---|---|
| **Trigger** | A Communication becomes available while speech activity is occurring in the Room |
| **Participants** | Tom, David, the Room, the Communication's originator |
| **Authoritative inputs** | Speech activity from the Voice Evidence Provider Runtime; Room from Room Configuration; audience composition from Operational Trust |
| **Required Truth** | A current-state Fact that speech activity is occurring. **This Fact class does not exist and is not authorised** |
| **Identity requirement** | Optional. Candidate speaker evidence may raise or lower audience certainty; **`unknown` is fully sufficient for the decision to defer** |
| **Operational Trust** | Whether spoken disclosure is appropriate for the apparent audience (**DL-34**); whether microphone-derived evidence is permitted for the purpose |
| **Stewardship** | Owns the significance of the underlying matter and originates the Communication. **It does not decide when to speak** |
| **Continuity** | **None required.** Conversation state has no ongoing governed purpose once the delivery decision is made |
| **Concierge** | Selects timing, channel, and form. Defers the spoken part; delivers the detail privately; re-presents a content-free acknowledgement later |
| **Available channels** | Room voice assistant, Companion App notification, personal mobile device, deferral, no delivery |
| **Expected response** | **Defer** the spoken delivery, **deliver privately**, then **convey without acting** a content-free notice |
| **Confirmation required** | No |
| **Explainability** | *"I sent that privately because people were speaking in the Den."* **Never** *"because I heard you discussing X"* |
| **Retention and expiry** | Speech-activity state is transient and expires when its declared purpose ends. **No transcript created, none retained, no conversation content processed.** The Communication and its Delivery Attempts are retained under **DL-47** |
| **Failure and degradation** | Provider unavailable → speech activity `unknown` → **do not announce**; concierge-contract §11 already requires *"occupancy unknown and the surface is shared → do not announce; reduce to content-free indication, choose a personal surface, or defer"* |
| **Privacy** | Passive microphone use is the most sensitive capability in this catalogue. **It requires explicit governance and acceptance before implementation** |
| **Maturity** | **D — North Star** |
| **Implementation evidence** | None |
| **Related decisions** | **DL-28**, **DL-29**, **DL-34**, **DL-50** §25, **DL-47**; concierge-contract §7, §11, §12 |
| **Related issues** | **#167** (Phase 7), **#169** (OD-84) |
| **Open decisions** | **OD-84**, **OD-74** (Truth Fact confidence — **DL-39 bands may not be borrowed**), **OD-71** |

### Required distinctions

Listening for speech activity is not transcription · voice activity detection is not semantic
processing · participant evidence is not conversation content · current-state evidence is not durable
memory · **an interruption decision is not an authorisation decision**.

### Acceptance scenarios

| # | Given | Then | Must not |
|---|---|---|---|
| C1.1 | Speech activity in the Room, an ordinary Communication | Defer the spoken delivery; deliver privately | Speak over the conversation |
| C1.2 | Speech activity ends | A content-free acknowledgement may be spoken **if still useful** | Repeat the content aloud |
| C1.3 | The provider is unavailable | Speech activity is `unknown`; do not announce | Treat `unknown` as *nobody is talking* |
| C1.4 | Any of the above | No transcript exists at any point | Create one "just to decide" |

---

# C2 — Known and unidentified conversation participants

## Human outcome

Several people are talking. The home is fairly sure Tom is one of them. It cannot place at least one
other voice. **It does not need that person's name.** Knowing that *somebody it cannot place is in the
room* is exactly the information that makes speaking the wrong choice.

| Field | Statement |
|---|---|
| **Trigger** | Voice and other evidence indicate more than one apparent participant, at least one unidentified |
| **Authoritative inputs** | Candidate evidence from the provider; other Identity evidence families; audience composition |
| **Required Truth** | Current Room and contextual presence |
| **Identity requirement** | Must preserve `known`, `unknown`, `ambiguous`, `unavailable` — **and plurality, which it cannot currently express** |
| **Operational Trust** | Evaluates the apparent audience and selects a permitted alternative surface |
| **Continuity** | None |
| **Concierge** | Routes privately; may acknowledge non-sensitively later |
| **Expected response** | Private delivery; suppress spoken disclosure |
| **Confirmation required** | No |
| **Explainability** | *"I sent it privately because I could not account for everyone in the room."* |
| **Retention and expiry** | Transient; expires with the decision |
| **Failure and degradation** | Fewer evidence families lower the ceiling; **absence is neutral** (**DL-38 F7**) and never a penalty |
| **Privacy** | An unidentified person is never named, profiled, or accumulated across visits (**DL-33**) |
| **Maturity** | **E — Blocked** |
| **Open decisions** | **OD-84** (#169), **OD-71** (#104) |

### The distinction that must not collapse

**One speaker whose identity is ambiguous is not the same condition as several people speaking.** They
produce the same observable shape — several candidates scoring closely — **from opposite causes**.
`ambiguous` means the first. **OD-84** owns whether the second is expressible, and until it is decided
an implementation **must not report plurality as `ambiguous`**.

### Acceptance scenarios

| # | Given | Then | Must not |
|---|---|---|---|
| C2.1 | Tom `known`, one voice unmatched | Private delivery | Name or profile the unmatched voice |
| C2.2 | Two candidates score closely for one voice | `ambiguous` | Report this as *two people are present* |
| C2.3 | Two voices are genuinely present | Recorded as **quality metadata** pending OD-84 | Report it as `ambiguous` |

---

# C3 — Transient knowledge and purpose-limited forgetting

## Human outcome

The home knew, for about ninety seconds, that people were talking. It used that to decide how to
deliver something. Then it stopped knowing, because there was no longer any reason to.

| Field | Statement |
|---|---|
| **Trigger** | A transient Fact is created for a bounded decision |
| **Required Truth** | Truth owns Fact validity and expiration. **Operational expiration removes a Fact from *what is true now*; it does not delete *what was true then*** (**DL-25**) |
| **Continuity** | **Holds nothing.** Continuity scopes are person-scoped and room-scoped, and neither contains conversation state |
| **Concierge** | Consumes the Fact for the immediate decision and retains only the Decision Trace |
| **Retention and expiry** | Every governed record class declares its retention (**DL-47**); *undecided* is not a retention strategy. The Decision Trace outlives the Fact and **references** it rather than copying it (**DL-27**) |
| **Explainability** | The trace must remain answerable after the Fact expires — **DL-46**: the accepted Fact Truth recorded carries the durable explanation, not a copied payload |
| **Failure and degradation** | If the trace cannot be written, that is a defect and is reported (concierge-contract §11) |
| **Privacy** | Presence history derived from identity evidence is among the most sensitive household data |
| **Maturity** | **B — Architecturally supported** |
| **Open decisions** | **DL-59** (freshness values are household configuration), **OD-05** (trace retention values) |

### Doctrine confirmed, not created

*Not everything known should be remembered* · *information may be useful now without deserving durable
memory* · *purpose determines retention*. **All three are already accepted** through **DL-43**,
**DL-46**, and **DL-47**. This use case reinforces them and adds nothing.

---

# C4 — Local-first decision making with connected cloud sources

## Human outcome

The household deliberately connects a calendar, a mailbox, a weather service, a package tracker. The
home uses what they say. **What the home concludes, and what it does about it, stays at home.**

| Field | Statement |
|---|---|
| **Trigger** | A governed decision requires information a connected external service owns |
| **Authoritative inputs** | The external service remains the **system of record** for its own records |
| **Required Truth** | Truth may accept external information as evidence for a Fact. **A provider's output never silently becomes a Fact** |
| **Operational Trust** | Governs whether the source may be used for the purpose, and what may be disclosed from it |
| **Concierge** | Coordinates using the information; never claims ownership of it |
| **Retention and expiry** | **HTBW references and does not copy** (**DL-31**, **DL-27**). A longer retention requirement is **never** authority to copy external history (**DL-46**) |
| **Explainability** | The source is named and version-pinned; a dangling reference is **reported, never silently rendered as though the source never existed** (**DL-27**) |
| **Failure and degradation** | Source unavailable → the dependent capability is **unavailable and says so** (**DL-41**), never approximated |
| **Privacy** | Person-scoped external content is access-gated and audience-evaluated before it reaches any surface |
| **Maturity** | **B — Architecturally supported** |
| **Open decisions** | **OD-07** (locality), **OD-67** (reasoning provider strategy), **OD-77** (#148 — who owns the person-to-service association) |

### Required distinctions

*Local first* does not mean *cloud never* · information source is not decision location · connected is
not uncontrolled · **an external system retains ownership of its records** · HTBW does not acquire
ownership by consuming.

---

# C5 — Home Assistant remote access education

## Human outcome

A resident away from home opens the Companion App and the home responds. Nothing about that
connection means the home's reasoning happened somewhere else.

| Field | Statement |
|---|---|
| **Trigger** | A resident interacts from outside the home |
| **Concierge** | Delivers the mobile experience through a permitted personal surface |
| **Maturity** | **F — Research required** |
| **Why** | The repository holds **no verified platform documentation** on remote-access behaviour. **DL-30** states that *"unverifiable documentation leaves the decision open"*, and [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md) already records which platform pages were and were not verified |
| **Related issues** | **#146** — Home Assistant native capability verification backlog |

### The five things that must be distinguished, and are not yet documented

Remote **connectivity** · cloud-**originated** authoritative data · local Home Assistant **processing**
· local HTBW **decision making** · explicitly configured cloud **processing**, if any.

**No claim beyond repository evidence and official Home Assistant documentation may be made about any
of them.** Until #146 supplies verified sources, this use case is documented and **not** adopted.

---

# C6 — Shopping-list opportunity recognition

## Human outcome

Tom is at the grocery store. There are things on the household list. His phone tells him — once,
usefully, and he can turn it off.

| Field | Statement |
|---|---|
| **Trigger** | A governed location signal coincides with an active list |
| **Authoritative inputs** | Companion App location; the list's owning service |
| **Required Truth** | Current location from an authoritative configured source. **Zone granularity only** — the boundary document records that device trackers offer no Room-level presence |
| **Identity requirement** | Which person the list and the location belong to |
| **Operational Trust** | Whether a location-triggered prompt is permitted for this person, on this surface, at this moment |
| **Stewardship** | Establishes that the items matter **only if the household declared it**. *A default the household never saw is not a declaration* |
| **Continuity** | May hold the unfinished list context as **person-scoped** continuity |
| **Concierge** | Judges usefulness, selects the mobile channel, suppresses repetition |
| **Confirmation required** | No — but it must be **dismissible and adjustable** |
| **Retention and expiry** | The opportunity expires when the person leaves or the list empties. Location is **referenced**, never accumulated into a movement history |
| **Failure and degradation** | Location `unknown` → no prompt. **`unknown` is never *not at the store*** |
| **Privacy** | A location-triggered prompt reveals that the home is watching where someone is. It is person-scoped and must never be delivered to a shared surface |
| **Maturity** | **E — Blocked** |
| **Open decisions** | **OD-77** (#148) — **who owns the association between a person and their shopping list is undecided**; **OD-54** (#120) repeat suppression; **OD-43** (#113) surface capability |

### The four questions this use case asks, and where they land

| Question | Answer |
|---|---|
| Is *grocery store* a geofence, place category, or named zone? | **Undecided.** Home Assistant Zones are verified; place categories are not. **#146** |
| Who owns the shopping list? | **OD-77.** Every task and shopping experience contract in this repository is **Historical — superseded** |
| How is repeated prompting prevented? | **OD-54.** *Repeating delivery to the same audience is retry, not escalation* |
| What if several household members are at the store? | **OD-52** audience specification; the list is one subject with several eligible recipients |

---

# C7 — EV readiness and preventive guidance

## Human outcome

Today an automation says *"range is under 100 miles, plug in."* The intended future is that the home
says *"you did not plug in, and tomorrow looks like a long day"* — and is right often enough to be
worth listening to.

| Field | Statement |
|---|---|
| **Trigger** | Vehicle state crosses a **household-declared** readiness threshold |
| **Required Truth** | Range, location, charging state, arrival — all Facts with freshness |
| **Stewardship** | Vehicle readiness as a **care outcome**. The stewardship contract already names *vehicles* among its subjects |
| **Continuity** | May hold the unfinished reminder interaction |
| **Operational Trust** | Governs calendar use, disclosure, and interruption entitlement |
| **Concierge** | Judges present usefulness, selects the channel, follows up, and **recommends — never charges** |
| **Confirmation required** | **Yes** for any action. A recommendation is not authorisation |
| **Retention and expiry** | Notification history and prior deferral are **Communication** records under **DL-47** |
| **Failure and degradation** | No reliable travel estimate → say less, not more. **Degrade the claim, never the governance** |
| **Maturity** | **E — Blocked** |
| **Open decisions** | **OD-77** (person-to-calendar association), **DL-75** (significance representation, resolved), **OD-51** (interruption risk classes) |

### Guardrails

Do not represent calendar-derived mileage as exact unless a reliable source exists · **do not invent
route data** · not every calendar event requires vehicle travel · a recommendation is not authority to
begin charging · **the 100-mile threshold is configuration, never an architectural constant**.

> **No canonical governance exists for travel-time or travel-demand computation.** Any estimate is
> currently an unsupported claim, and stating it as a Fact would violate **DL-04**.

---

# C8 — Home battery backup and resource optimisation

## Human outcome

The power is out. The battery is carrying the house. The home says which things it would turn off to
keep the important things running longer — **and asks first**.

| Field | Statement |
|---|---|
| **Trigger** | Utility power lost; battery discharging |
| **Required Truth** | Load, battery state, charge direction, utility state, solar production, circuit visibility where available |
| **Stewardship** | Declares which household capabilities matter during an outage. **Nothing is *nonessential* until the household says so** |
| **Continuity** | May hold the current experience context. **It does not own energy history** — Home Assistant does (**DL-42**) |
| **Operational Trust** | Governs data use and whether a proposed action may proceed |
| **Concierge** | Presents options, sequences them, seeks confirmation |
| **Confirmation required** | **Yes.** Every load change |
| **Explainability** | Which measurement, which threshold, **whose declaration**, and what was compared |
| **Failure and degradation** | No circuit-level visibility → give **truthful degraded** advice. *"I can see total consumption but not which circuits"* is a complete answer |
| **Privacy** | Medical-equipment dependency is among the most sensitive facts a household holds and is never disclosed to a shared surface |
| **Maturity** | **E — Blocked** |
| **Open decisions** | **DL-75** significance representation (resolved), **OD-51** risk classes, **OD-67** whether a provider may compute options |

### Guardrails

**Do not invent runtime estimates** — if no authoritative source publishes one, HTBW has none · do not
characterise a load as nonessential without a household declaration · **never propose turning off a
safety-critical load** · recommendation is not action · **HTBW is not a life-safety system**, and an
outage advisory is never a substitute for medical alerting or emergency services.

---

# C9 — Guest capability discovery and vocabulary education

## Human outcome

A guest asks *"what can I do here?"* and hears: *"You're in the Den. Here you can adjust the lamp
level, adjust the overhead light, play music, adjust the shades, watch television, and change the
temperature."* **The words are the household's words, and nothing unavailable or unpermitted is
mentioned.**

| Field | Statement |
|---|---|
| **Trigger** | A capability question in a Room |
| **Required Truth** | Current Room; current capability availability |
| **Identity requirement** | An assertion, or `unknown`. **`unknown` is a complete answer here** — guest-safe treatment is the documented default |
| **Operational Trust** | Filters the list by who is asking. [room-vocabulary.md](room-vocabulary.md) already records this: *"filters by who is asking — a child or guest may see less"* |
| **Foundation** | Room Configuration owns which capabilities participate and Contextual Vocabulary owns what they are called (**DL-09**, **DL-10**) |
| **Concierge** | Composes the orientation. **It must not runtime-search devices to satisfy a vocabulary term** (concierge-contract prohibition 3) |
| **Expected response** | Room name, permitted capabilities, household vocabulary, understandable examples |
| **Explainability** | *"The Beam is deliberately not part of Speakers in this room"* is already a required Concierge sentence |
| **Failure and degradation** | Room unresolved → **do not guess a Room**; state it and ask |
| **Privacy** | An unavailable or unpermitted capability is **not mentioned**. Absence of mention is not a lie; enumerating what a guest may not do is a disclosure |
| **Maturity** | **B — Architecturally supported** |
| **Related decisions** | **DL-09**, **DL-10**, **DL-11**, **DL-41**; room-configuration-contract; [room-vocabulary.md](room-vocabulary.md) |
| **Open decisions** | **OD-59** exposure precedence (#103), **OD-13** vocabulary inheritance (#138) |

### The five questions

Room vocabulary is governed by **Foundation / Room Configuration** · synonyms are Contextual Vocabulary
with a singular term and a derived plural · unavailable capabilities are excluded by **DL-41** and
**DL-11 Exposure** · residents and guests differ by **Operational Trust filtering, not by two lists** ·
when Identity is uncertain, **guest-safe treatment applies and the answer is still useful**.

---

# C10 — Guest-asset interpretation and household storytelling

## Human outcome

A guest asks about the room's interesting things and gets the household's own approved story — not a
catalogue, not an appraisal, and nothing the household would not say aloud to a visitor.

| Field | Statement |
|---|---|
| **Required Truth** | Current Room |
| **Identity requirement** | Guest, known non-resident, resident, or `unknown` |
| **Stewardship** | Owns what the objects are, why they matter, and their care relationships |
| **Foundation** | The Asset record and its household-authored descriptions |
| **Operational Trust** | Determines what may be disclosed to the present audience |
| **Concierge** | Selects, sequences, and presents |
| **Continuity** | May hold a **consented** unfinished visit experience |
| **Confirmation required** | No |
| **Retention and expiry** | Nothing about the guest is retained absent consent (**C13**) |
| **Failure and degradation** | No approved description → the item is **omitted silently**, never improvised |
| **Privacy** | **Never** disclose valuations, security details, private provenance, ownership records, or maintenance sensitivities |
| **Maturity** | **E — Blocked** |
| **Open decisions** | **OD-52** (#100) audience specification |

### Guardrails

**Do not fabricate object stories.** Use household-approved descriptions only · **not every asset
record is guest-visible** · an absent audience variant **fails closed**, and the item is simply not
mentioned.

> **Product evidence, not HTBW implementation.** The standalone Asset Intelligence product holds two
> household-authored description variants labelled *Guest* and *Owner* — an explicit audience
> classification rather than a sensitivity inference. It is recorded as evidence toward **OD-52** and
> creates no HTBW requirement (**DL-19**).

---

# C11 — Asset knowledge becomes household action

## Human outcome

*"When was the piano last tuned?"* → an answer. *"Remind me to contact the tuner"* → a real task, in
the household's real task system, without repeating who or what.

| Field | Statement |
|---|---|
| **Trigger** | A question followed by a request that depends on it |
| **Required Truth** | The authoritative maintenance Fact |
| **Identity requirement** | The requesting person, for a personal task |
| **Stewardship** | Owns the piano's care requirement, the caretaker relationship, and any obligation |
| **Continuity** | Holds the **active conversational reference** to the piano and the tuner. **It does not own the task** |
| **Operational Trust** | Governs personal task creation and disclosure |
| **Concierge** | Interprets the follow-up, **asks for missing information**, coordinates creation |
| **Confirmation required** | **Yes** where target, owner, or timing is missing |
| **Retention and expiry** | The conversational reference expires with the interaction. The **task belongs to the task service** |
| **Failure and degradation** | Task service unavailable → **say so**; never silently drop the request |
| **Maturity** | **E — Blocked** |
| **Open decisions** | **OD-77** (#148) task/list ownership, **OD-23** (#109) obligation projection |

### Guardrails

Concierge does not own the piano record · Continuity does not own the task · **do not create a task
without sufficient target, owner, and timing** · **if no due date is given, follow accepted
task-creation policy rather than inventing one** — and no such policy is yet accepted.

---

# C12 — Outcome-based room comfort

## Human outcome

Someone says *"make the room comfortable"* and the room becomes comfortable — for the people actually
in it, without a debate about degrees.

| Field | Statement |
|---|---|
| **Required Truth** | Room, occupants, light level, temperature, humidity, shade state, active experience |
| **Identity requirement** | Person assertions for whoever is present |
| **Operational Trust** | Which personalisation is appropriate, and whether each change may proceed |
| **Stewardship** | Comfort and preservation priorities where an Asset constrains the room |
| **Continuity** | Person-scoped and room-scoped preferences, and the current room experience |
| **Concierge** | **Owns this outright** — concierge-contract §3 gives it *interpretation of intent*, *selection among permitted actions*, and *conflict resolution between competing permitted outcomes* |
| **Confirmation required** | Where occupants conflict, or the request is ambiguous |
| **Failure and degradation** | A partial outcome is **reported precisely**; never claim success |
| **Privacy** | One occupant's preference is never disclosed while satisfying another's |
| **Maturity** | **B — Architecturally supported** |
| **Open decisions** | **OD-04** (#97) policy precedence, **OD-78** (#149) remembered-value classes and restoration semantics |

### Guardrails

**Comfort is not one universal temperature or brightness** · do not silently choose among conflicting
occupants — [multi-person-conflict.md](multi-person-conflict.md) is the canonical treatment ·
**do not override a deliberate manual stop** · safety, energy, preservation, and guest policy all
bind · **explain or ask when the request is ambiguous**.

---

# C13 — First-visit guest consent and introduction

## Human outcome

Someone the home does not know keeps turning up. At a sensible moment it asks their name — and then,
separately, asks whether they would like to be remembered. **Saying no costs them nothing.**

| Field | Statement |
|---|---|
| **Trigger** | Repeated unidentified presence, or an unclaimed device observed repeatedly |
| **Required Truth** | Repeated presence **without claiming identity** |
| **Identity requirement** | **Must not resolve a person from an unclaimed device.** *An unknown evidence source is not a person* (**DL-33**) |
| **Operational Trust** | Whether asking is appropriate at all, on this surface, at this moment |
| **Concierge** | Chooses the moment, channel, and wording |
| **Continuity** | Creates durable context **only after governed consent** |
| **Confirmation required** | **Yes, twice, and separately** — a name is one thing; durable recognition is another |
| **Explainability** | The person must be able to ask what the home knows about them and get a truthful answer |
| **Retention and expiry** | Nothing durable before consent. Consent is scoped, recorded, attributable, and revocable |
| **Failure and degradation** | Declining must **not degrade basic guest hospitality**. *Declining is not exclusion* |
| **Privacy** | **A provided name is not consent to biometric enrollment.** Device association, voiceprint enrollment, preference storage, and future recognition are **distinct consent scopes** |
| **Maturity** | **E — Blocked** |
| **Open decisions** | **OD-06** (#94) consent capture and revocation experience |

### Guardrails

Detection is not identity · recognition is not consent · **avoid repeatedly asking after a decline** ·
the person can inspect, adjust, revoke, and delete · **no synthetic Guest Person is ever created**
(**DL-33**).

---

# C14 — Returning-guest hospitality

## Human outcome

Sarah, who chose to be remembered, comes back. *"Welcome back, Sarah. Would you like the Den set up
the way you had it last time?"* — **offered, not assumed.**

| Field | Statement |
|---|---|
| **Identity requirement** | A governed assertion for a **known non-resident Person** — a real configured Person, not a synthetic one |
| **Operational Trust** | Confirms recognition and personalised disclosure remain appropriate, and owns the **Address by Name** threshold (**DL-39**) |
| **Continuity** | Provides consented guest context and valid preferences |
| **Concierge** | Welcomes and **offers** |
| **Confirmation required** | **Yes** where policy requires an offer rather than restoration |
| **Retention and expiry** | Consent scope and expiry are authoritative. **Revoked or expired consent is honoured immediately** |
| **Failure and degradation** | Consent expired → treat as a first visit, **without implying the home forgot something it should have kept** |
| **Privacy** | **Do not announce a guest's identity to an inappropriate audience** — greeting by name is itself a disclosure |
| **Maturity** | **E — Blocked** |
| **Open decisions** | **OD-06** (#94), **OD-15** (#96) assertion lifetime |

### Guardrails

Prior consent is not unlimited permission · **do not expose visit history unnecessarily** · do not
silently restore preferences where policy requires an offer.

---

# C15 — Guest relationship learning

## Human outcome

Over several visits the home gets better at hosting Sarah — because she chose that, and can change her
mind.

| Field | Statement |
|---|---|
| **Observable governed facts** | Visit recurrence, rooms used, stated preferences, accepted or declined offers, consented devices, voice evidence **only if separately permitted** |
| **Identity requirement** | Consent scope per evidence source, per purpose |
| **Operational Trust** | Owns whether an observation may become a learned preference |
| **Continuity** | Person-scoped guest preferences. **Continuity scopes are person-scoped and room-scoped only** — there is no household or relationship scope to put this in |
| **Concierge** | Improves hospitality within governed boundaries |
| **Retention and expiry** | **Unresolved.** When relationship memory expires is not decided |
| **Privacy** | The guest inspects, corrects, revokes, and deletes |
| **Maturity** | **E — Blocked** |
| **Open decisions** | **OD-06** (#94), **OD-28** (#127) learned-policy promotion lifecycle, **OD-65** (#130) learning evidence eligibility, **OD-26** (#125) history retention |

### The architectural questions, and where they land

| Question | Where it belongs |
|---|---|
| Which responsibility owns the guest relationship? | The guest is a **Person**; Foundation holds the record, Continuity holds person-scoped preference, Operational Trust holds authority. **No relationship object is created** |
| Does Stewardship establish that the relationship matters? | **No.** Stewardship owns care and obligation, not social significance |
| What may Continuity preserve? | Consented person-scoped preferences only |
| Inferred versus explicit preference? | **DL-21** — *a learned suggestion is not an autonomous policy*, and **OD-28** owns the lifecycle |
| When does relationship memory expire? | **Undecided.** **OD-26** |

**The home does not infer personal importance from visit frequency.** *Frequency is not significance.*

---

# C16 — Multi-party relationship-aware disclosure

## Human outcome

Four people are in the room. The home knows two, half-knows one, and cannot place the fourth. **It
behaves according to the person it is least sure about.**

| Field | Statement |
|---|---|
| **Identity requirement** | Assertions plus `unknown` plus — **when OD-84 permits** — plurality |
| **Operational Trust** | **Owns the disclosure decision.** Audience composition *identifies nobody* and *must retain its uncertainty* |
| **Concierge** | Selects the delivery strategy appropriate to the **least certain relevant audience state** |
| **Possible responses** | Speak fully · speak a neutral notice · deliver privately · display personally · wait · ask · suppress · escalate through a permitted channel for critical items |
| **Confirmation required** | Where policy demands it |
| **Explainability** | *"I could not account for everyone present"* |
| **Failure and degradation** | *Audience unknown* and *audience detection unavailable* are **distinct composition states** and must not collapse |
| **Privacy** | **Absence of evidence is never proof of solitude** (**DL-34**) |
| **Maturity** | **E — Blocked** |
| **Open decisions** | **OD-84** (#169), **OD-71** (#104) audience-uncertainty disclosure policy, **OD-52** (#100) |

**Multi-speaker architecture is not decided by this document.** OD-84 is open, and use-case
documentation is not a decision surface.

---

# C17 — Channel selection across the household experience

## Human outcome

The right thing reaches the right person in the right way — spoken, on a phone, on a watch, on a
screen, later, or not at all.

| Field | Statement |
|---|---|
| **Candidate channels** | Room voice assistant · Companion App · personal mobile · wearable · Room kiosk · household display · television · email · connected messaging · visual indicator · deferred follow-up · **no delivery** |
| **Operational Trust** | Audience eligibility, visibility classification, urgency entitlement |
| **Concierge** | **Owns resolution of an audience specification to Delivery Surfaces**, and every Delivery Attempt |
| **Confirmation required** | No |
| **Explainability** | Every attempt and outcome is recorded; *"why didn't you tell me?"* must be answerable |
| **Retention and expiry** | Delivery history is **Change Records referencing the Communication**, never embedded in it |
| **Failure and degradation** | No permitted surface → **Undeliverable**, recorded and reported, **never silent**. `Presented` is never inferred from `Delivered` |
| **Privacy** | Visibility is re-evaluated at **each** attempt; a stored resolved visibility is never reused |
| **Maturity** | **E — Blocked** |
| **Open decisions** | **OD-43** (#113) delivery surface capability model — **the blocking decision**; **OD-44** (#114), **OD-45** (#115), **OD-54** (#120), **OD-55** (#121), **OD-57** (#102) |

### Channel status

**No channel is implemented in HTBW.** Which surfaces exist, which can attest presentation, which are
private, and which support acknowledgement is **exactly what OD-43 owns**, and it is open. This
document does not pre-answer it.

---

# C18 — Importance, urgency, escalation, and follow-up

## Human outcome

A shopping reminder and a battery warning do not behave the same way, and neither becomes background
noise.

| Field | Statement |
|---|---|
| **Who determines importance** | **Stewardship** — significance and the escalation ladder |
| **Who determines urgency** | **Operational Trust.** *Urgency is an entitlement granted by Operational Trust, never a property the originator asserts* |
| **Who determines risk** | **Operational Trust** — action-risk class |
| **What Concierge coordinates** | Timing, surface, sequencing, retry, deferral, re-presentation, and the record of every attempt |
| **Confirmation required** | Per the Required Confirmation Strength of the protected operation (**DL-40**) |
| **Retention and expiry** | Communication lifecycle states are accepted; **retention values are not** |
| **Failure and degradation** | An acknowledgement that never arrives stays **unknown** and **never decays into *not acknowledged*** |
| **Maturity** | **E — Blocked** |
| **Open decisions** | **OD-46** (#98), **OD-51** (#99), **OD-53** (#119), **OD-22** (#108), **OD-45** (#115), **OD-48** (#117), **OD-49** (#118), **OD-54** (#120) |

**Repeating delivery to the same audience is retry and belongs to Concierge. Changing the audience is
escalation and belongs to Stewardship's ladder and Operational Trust's authority.** These are already
separated and must not be re-merged.

---

# C19 — Explainability

## Human outcome

*"Why did you send that to my phone instead of saying it?"* gets a true answer that does not expose
anyone else.

| Field | Statement |
|---|---|
| **Concierge** | **Composes** the Decision Trace from every contributing responsibility and authors only its own fields: conflicts detected, resolution applied, action taken, action suppressed, suppression reason, alternative considered |
| **Expected response** | *"I sent the update privately because speech activity and an unidentified participant made spoken disclosure inappropriate."* |
| **Must never reveal** | Biometric internals · protected policy mechanics · another person's private information · implementation detail unsuited to the audience · **unsupported causal claims** |
| **Failure and degradation** | *"I can't tell you what caused it"* is an accepted answer — [why-did-this-happen.md](why-did-this-happen.md) Scenario 21 |
| **Privacy** | An explanation is itself a disclosure and is audience-evaluated |
| **Maturity** | **B — Architecturally supported** |
| **Related decisions** | **DL-15**, **DL-27**, **DL-46**; [../models/decision-trace.md](../models/decision-trace.md); concierge-contract §13 |
| **Open decisions** | **OD-29** (#79) trace persistence, **OD-30** (#80) trace visibility |

**The contract already requires the exact sentence shape this use case asks for.** What is open is
*where traces live* and *who may see them* — not whether they exist.

---

# C20 — Do nothing as a valid Concierge response

## Human outcome

The home stays quiet, and that was a decision — not a gap.

| Field | Statement |
|---|---|
| **When** | Assistance unnecessary · already handled · wrong moment · expired · declined · disclosure not permitted · confidence insufficient · interruption costs more than it is worth · no safe fallback |
| **Concierge** | Produces **exactly one governed outcome** and **always** a Decision Trace |
| **Expected response** | Do nothing · defer · or a truthful capability-unavailable statement |
| **Explainability** | **"Doing nothing is a decision and is traced"** — concierge-contract §7, verbatim |
| **Failure and degradation** | Silence caused by a **missing dependency** is a **DL-41** capability outcome that **names the dependency**, and is never presented as a judgement the home did not make |
| **Maturity** | **B — Architecturally supported** |
| **Related decisions** | **DL-15**, **DL-41**; [nighttime-suppression.md](nighttime-suppression.md); [why-did-this-happen.md](why-did-this-happen.md) |
| **Open decisions** | None |

**This is the most fully supported use case in the catalogue.** Suppression as a deliberate,
explainable outcome is already a canonical scenario, and **DL-15** requires a trace for *every
decision, action, non-action, and suppression*.

### The failure to avoid

Reporting a **dependency outage as a trust decision** — which teaches the resident to distrust a
judgement the home never made.

---

## Episode 8 traceability

| # | Story | Primary Concierge facet | Supporting responsibilities | Maturity | Blocker | Narrative value |
|---|---|---|---|---|---|---|
| 1 | Conversation active, send privately, acknowledge later | Timing and channel selection | Truth, Identity, Operational Trust | **D** | Passive monitoring; **OD-84** | The home is considerate without being nosy |
| 2 | An unidentified participant changes disclosure | Audience-aware delivery | Identity, Operational Trust | **E** | **OD-84** | Not knowing someone is itself useful information |
| 3 | Transient conversation state expires | Context assembly | Truth, Continuity | **B** | **DL-59** values (household configuration) | Forgetting on purpose is a feature |
| 4 | The shopping list becomes useful at the store | Opportunity recognition | Identity, Truth, Continuity | **E** | **OD-77** | Help arrives at the moment it is useful |
| 5 | EV readiness considers charging and future need | Preventive guidance | Truth, Stewardship | **E** | **OD-77**; no travel governance | The home looks one day ahead |
| 6 | Battery backup prompts resource preservation | Recommendation and confirmation | Truth, Stewardship | **E** | **OD-51**, **OD-67** | The home advises; the household decides |
| 7 | A guest asks what can be done in the Den | Capability discovery | Foundation, Operational Trust | **B** | **OD-59** | Hospitality is orientation, not a manual |
| 8 | A guest asks about the artwork | Experience storytelling | Stewardship, Foundation | **E** | **OD-52** | The house tells its own story, in the household's words |
| 9 | Piano maintenance becomes a follow-up task | Knowledge-to-action continuation | Stewardship, Continuity | **E** | **OD-77**, **OD-23** | A question turns into a commitment without repeating yourself |
| 10 | *Make the room comfortable* | Outcome interpretation | Truth, Identity, Continuity | **B** | **OD-04** | You ask for an outcome, not a device list |
| 11 | A guest chooses whether to introduce themselves | Consent capture | Identity, Operational Trust | **E** | **OD-06** | The guest is asked, not enrolled |
| 12 | A returning guest receives consented hospitality | Existing relationship use | Identity, Continuity | **E** | **OD-06** | Being remembered is a choice that can be unmade |
| 13 | Connected cloud information, local judgment | Context assembly | Truth, Operational Trust | **B** | **OD-07**, **OD-67** | Where facts come from is not where decisions are made |
| 14 | Remote access without relocating reasoning | Channel selection | — | **F** | **#146** | Reaching your home is not exposing it |
| 15 | Silence or waiting as a valid decision | No-action outcome | All | **B** | None | The best help is sometimes none |

---

## Concierge facet coverage

| # | Facet | Status |
|---|---|---|
| 1 | Context assembly | **Already accepted** — runtime-sequence, context-before-intent |
| 2 | Response selection | **Already accepted** — concierge-contract §7 |
| 3 | Timing | **Already accepted** — §3 |
| 4 | Channel selection | **Partially represented** — owned by §3; the surface model is **OD-43** |
| 5 | Audience-aware delivery | **Already accepted** — **DL-29**, **DL-34** |
| 6 | Recommendation | **Already accepted** — §7 *convey without acting*; **DL-21** |
| 7 | Confirmation | **Already accepted** — **DL-37**, **DL-40** |
| 8 | Escalation | **Already accepted** — Stewardship's ladder; §5 prohibition 15 |
| 9 | Deferral | **Already accepted** — §7 |
| 10 | Re-presentation | **Blocked** — **OD-48** |
| 11 | Delivery acknowledgement | **Blocked** — **OD-45** |
| 12 | Recovery | **Already accepted** — §11 |
| 13 | Explainability | **Already accepted** — §13, **DL-15** |
| 14 | No-action outcome | **Already accepted** — §7, and traced |
| 15 | Guest onboarding | **Blocked** — **OD-06** |
| 16 | Consent capture | **Blocked** — **OD-06** |
| 17 | Existing relationship use | **Blocked** — **OD-06**, **OD-15** |
| 18 | Outcome interpretation | **Already accepted** — §3 *interpretation of intent*, *selection among permitted actions*, *conflict resolution* |
| 19 | Knowledge-to-action continuation | **Blocked** — **OD-77**, **OD-23** |
| 20 | Resource optimisation | **Blocked** — **OD-51**, **OD-67** |
| 21 | Preventive guidance | **Partially represented** — Stewardship obligations exist; the forward-looking estimate has no governance |
| 22 | Opportunity recognition | **Partially represented** — *any responsibility may originate a Communication*; the opportunity trigger is per-originator |
| 23 | Capability discovery | **Already accepted** — room-configuration-contract, **DL-41** |
| 24 | Experience storytelling | **Blocked** — **OD-52** |

**Fourteen of twenty-four facets are already accepted. No facet is missing. No facet requires a new
architectural construct.**

---

## Cross-cutting questions

| # | Question | Answered by |
|---|---|---|
| 1 | How does Concierge know which channels are available? | **Open — OD-43** |
| 2 | Which channels are private? | **Open — OD-43**, **OD-71** |
| 3 | Room-specific vocabulary? | **Answered** — Contextual Vocabulary, **DL-10** |
| 4 | Guest-appropriate capability descriptions? | **Answered** — Operational Trust filtering; **DL-11** Exposure |
| 5 | Unfinished offers remembered and re-presented? | **Open — OD-48** |
| 6 | Repeated notifications suppressed? | **Open — OD-54** |
| 7 | Deadlines and expiry? | **Partially — OD-49**; lifecycle states accepted, values open |
| 8 | Urgency and importance? | **Answered in ownership** — Stewardship significance, Operational Trust urgency. **Values open — OD-46**, **OD-53** |
| 9 | Recommendations distinguished from commands? | **Answered** — **DL-21**, §7 |
| 10 | Recommended actions authorised? | **Answered** — Operational Trust; §5 prohibition 4 |
| 11 | Outcome-based requests decomposed? | **Answered** — §3, and conflicts by **OD-04** |
| 12 | Conflicts among occupants? | **Answered** — [multi-person-conflict.md](multi-person-conflict.md); precedence **OD-04** |
| 13 | Guest consent scopes? | **Open — OD-06** |
| 14 | Consent revoked? | **Answered in principle** — revocation removes the derived profile, not merely its use. **Experience open — OD-06** |
| 15 | Known and unknown audience members? | **Answered** — composition states in [../models/communication.md](../models/communication.md) |
| 16 | Multi-speaker plurality? | **Open — OD-84** |
| 17 | Transient facts consumed without becoming durable? | **Answered** — **DL-25**, **DL-46**, **DL-47** |
| 18 | Local decision making with connected services? | **Answered in principle** — **DL-31**, **DL-42**, **DL-46**. Edges in **OD-07**, **OD-67** |
| 19 | Decision Traces exposed safely? | **Open — OD-30** |
| 20 | Deliberate no-action represented? | **Answered** — **DL-15**; §7; [nighttime-suppression.md](nighttime-suppression.md) |

**Eleven of twenty are answered by accepted architecture. Nine are open, and every one of them is an
existing open decision. This review created none.**

---

## North Star and validation-gated capabilities

**None of the following is implemented, and none is presented as implemented.**

Passive speech-activity monitoring · real-time conversation-active state · multi-speaker
identification · unknown-speaker audience use · conversation-break detection · passive guest-device
observation · voice-based returning-guest recognition · cross-calendar travel-demand estimation ·
automatic battery-load optimisation · speaker-conditioned extraction · ambient participant
identification.

---

## Related documents

- [README.md](README.md)
- [../contracts/concierge-contract.md](../contracts/concierge-contract.md)
- [../models/communication.md](../models/communication.md)
- [../models/decision-trace.md](../models/decision-trace.md)
- [../models/operational-trust.md](../models/operational-trust.md)
- [../models/person-and-identity.md](../models/person-and-identity.md)
- [../architecture/adr-resident-communication-and-delivery-separation.md](../architecture/adr-resident-communication-and-delivery-separation.md)
- [../architecture/adr-wyoming-compatible-voice-evidence-runtime.md](../architecture/adr-wyoming-compatible-voice-evidence-runtime.md)
- [multi-person-conflict.md](multi-person-conflict.md)
- [nighttime-suppression.md](nighttime-suppression.md)
- [room-vocabulary.md](room-vocabulary.md)
- [why-did-this-happen.md](why-did-this-happen.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
- [../governance/open-decision-issue-index.md](../governance/open-decision-issue-index.md)
