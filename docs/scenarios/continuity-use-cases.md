# Canonical Continuity Use Cases

> **Document status: Canonical scenario.**
> Terminology: [../models/glossary.md](../models/glossary.md).
> Index: [README.md](README.md). Owning responsibility: **Continuity**.
> Model: [../models/continuity.md](../models/continuity.md),
> [../models/experience-and-session.md](../models/experience-and-session.md).
> Contract: [../contracts/continuity-contract.md](../contracts/continuity-contract.md).
> Companion scenario: [follow-me-media.md](follow-me-media.md).

---

## Purpose

[follow-me-media.md](follow-me-media.md) proves the **handoff** — transfer versus resume, eligibility
versus decision, suppression as a deliberate outcome. This document proves the **boundary of
remembering**: what Continuity actually holds, what it merely references, what belongs to another
responsibility that happens to have a history, and what the home must never claim to remember.

These fifteen use cases arose as **architecture stress tests** during narrative development of
*Season 1 Episode 7 — Continuity: How Does a Home Remember What Matters?* They are recorded here as
canonical Continuity use cases and as **future acceptance scenarios**.

**The narrative is not architecture.** It was used to find questions the accepted architecture must
answer. Where it proposed something the accepted architecture does not support, the accepted
architecture prevailed and the narration is remediated. See
[../governance/decision-ledger.md](../governance/decision-ledger.md).

**Use Case 16** has a different origin: the Experience Continuity and Remembered Preferences production
experience outcome review, grounded in the production behavior-preservation inventory rather than the
Episode 7 narrative. It is recorded under the same acceptance-scenario discipline as the first fifteen.

---

## The doctrine these use cases enforce

> **Continuity holds what the household wants remembered so an experience can continue. It does not
> hold everything that happened, it does not decide what happens next, and it does not become the
> owner of another responsibility's history.**

Stated in the form the household hears:

> **The home remembers what lets life continue.**

Behind that summary, precisely:

| Statement | Owner |
|---|---|
| *What is true right now* | **Truth** |
| *Who is engaging, and how confidently* | **Identity** |
| *What matters and requires care* | **Stewardship** |
| *What is wanted, and what was left running* | **Continuity** |
| *Whether this is appropriate for this request, in this context* | **Operational Trust** |
| *What should happen now, and how it is said* | **Concierge** |
| *The action itself* | An **executor** — a Home Assistant automation, script, scene, service call, integration, or a person |

**Continuity supplies state, intent, and eligibility. Continuity does not choose the final action**
([../contracts/continuity-contract.md](../contracts/continuity-contract.md), *The decisive boundary*;
[../architecture/dependency-view.md](../architecture/dependency-view.md) rule 5).

---

## The four separations this document exists to protect

**1. A memory is not an observation.**
An occurrence in the household is a **Domain Event**, owned by the responsibility that observed it. A
change to a governed record is a **Change Record**. Neither is a Continuity preference.
See [../models/glossary.md](../models/glossary.md) and
[../models/temporal-record.md](../models/temporal-record.md).

**2. An observation is not a preference.**
An observed pattern must not silently become an autonomous policy (**P26**, **DL-21**). The promotion
ladder — *Observation → Pattern → Suggestion → Approved preference → Adaptive policy* — is stated in
[../architecture/behavioral-governance.md](../architecture/behavioral-governance.md) and is not
restated here.

**3. A preference is not a recommendation, and a recommendation is not an authorisation.**
A Preference is *a person-scoped or room-scoped statement of what is wanted*; it *is not a fact and
not a policy* ([../models/glossary.md](../models/glossary.md)). A Reasoning Provider *owns nothing*,
and *its recommendation never silently becomes an authorised action* (same source; strategy is
**OD-67**).

**4. Continuity is not the home's history.**
Each responsibility owns the history of its own records under the shared temporal model
([../models/temporal-record.md](../models/temporal-record.md)). Truth owns Fact history. Stewardship
owns obligation, maintenance, service, and caretaker history. Concierge owns decision history.
Continuity owns **preference, session, resume, transfer, and experience history — and nothing else**.

---

## Status legend

HTBW Core is **greenfield** ([../architecture/greenfield-mandate.md](../architecture/greenfield-mandate.md),
**DL-19**). Nothing in this document asserts an implemented HTBW Core capability.

| Code | Meaning |
|---|---|
| **A** | **Accepted architecture** — stated in a canonical HTBW document |
| **E** | **Architectural expectation** — follows from accepted architecture, not yet written into a canonical model or contract |
| **U** | **Unresolved decision** — held by a named open decision (OD) |
| **F** | **Future implementation requirement** — no HTBW Core implementation exists |
| **N** | **Not governed** — the repository says nothing, and nothing here creates it |
| **P** | **Partially present in a separate released product** — Asset Intelligence, Voice Identity, or Concierge. **This is not HTBW Core capability** and creates no compatibility requirement (**DL-19**) |

---

## The household used throughout

The household of [README.md](README.md), extended only where a use case requires it:

```
Home
├── Living Space            (Merged Room: Kitchen + Dining + Living)
├── Den
├── Office
├── Primary Bedroom
├── Music Room
└── Garage

People:  Tom, David
Pets:    Maisey
Assets:  Sonos speakers, Sonos Beam, LG television, Apple TV,
         7 shades, 1918 A.B. Chase 6' Grand Piano,
         a signed watercolour in the Den
```

---

## How to read a use case

Each use case is presented as:

1. **Human outcome** — what the household actually gets
2. **Preconditions** — what must already be true, configured, or consented
3. **Ownership map** — the fourteen handoffs, each with exactly one owner
4. **Walkthrough** — the attributed steps, where the use case needs one
5. **Expected outcome, failure behaviour, and explanation**
6. **Acceptance scenarios** — what a conforming implementation must and must not do
7. **Implementation status and unresolved decisions**

**Every ownership map answers the same fourteen questions**, so the use cases can be compared without
re-reading them:

| # | Question |
|---|---|
| 1 | Authoritative Truth inputs |
| 2 | Identity requirements |
| 3 | Consent and Operational Trust requirements |
| 4 | What Continuity supplies |
| 5 | Memory scope |
| 6 | Source of record |
| 7 | Who decides |
| 8 | Who executes |
| 9 | Explainability |
| 10 | Retention and lifecycle |
| 11 | Guest and Unknown Person behaviour |
| 12 | Multi-person conflict behaviour |
| 13 | Failure behaviour |
| 14 | What must never happen |

---

# Use Case 1 — Comfort Restoration

## Human outcome

Tom says *"turn on the lamps"* in the Office and gets the light level he actually uses, not a
factory-default 100%.

## Preconditions

| Precondition | Owner | Status |
|---|---|---|
| Office lamp vocabulary is configured | Room Configuration / Contextual Vocabulary | **A** |
| A room-scoped lamp level exists as a Continuity record | **Continuity** | **A** — [../models/continuity.md](../models/continuity.md) holds *last lamp levels, last speaker volume* |
| Restoration is explicitly configured rather than inferred | Household configuration | **A** — [../patterns/execution-patterns.md](../patterns/execution-patterns.md), *State Restoration Execution* |
| **Which remembered value class is restored** | — | **U — OD-78** |

## Ownership map

| # | Question | Owner | Statement |
|---|---|---|---|
| 1 | Authoritative Truth inputs | **Truth** | Current entity availability, Room mode, and any environmental constraint. **A remembered value is not a Fact** |
| 2 | Identity requirements | **Identity** | **None for a room-scoped value.** A *person*-preferred level requires an Identity Assertion meeting the configured band (**DL-39**, **DL-36**) |
| 3 | Consent and Operational Trust requirements | **Operational Trust** | Whether the level may be applied at Explicit, Assisted, or Autonomous level; whether Room mode prohibits it |
| 4 | What Continuity supplies | **Continuity** | The remembered value and its scope. **Not the decision to apply it** |
| 5 | Memory scope | **Room-scoped** for lamp level, music volume, duck volume, TTS volume. **Person-scoped** only where an approved preference exists | **A** |
| 6 | Source of record | **Home Assistant** for current entity state (**DL-46**). Continuity for the governed remembered value | **A** |
| 7 | Who decides | **Concierge** | — |
| 8 | Who executes | An **executor** — service call, scene, or script | — |
| 9 | Explainability | **Decision Trace** | Which remembered value, at which version (**P30**, **DL-27**), and why it was applied or not |
| 10 | Retention and lifecycle | **DL-47** | Preference history is Continuity's; entity-state history is Home Assistant's and is **not copied** (**DL-46**) |
| 11 | Guest and Unknown Person behaviour | **Operational Trust** | An Unknown Person *owns no preferences or history, inherits nothing from any resident, generates no person-scoped learning* (**DL-33**) |
| 12 | Multi-person conflict behaviour | **Operational Trust** / **Concierge** | Room-scoped values are shared; a person-scoped value is not applied on another person's behalf |
| 13 | Failure behaviour | **Continuity** | *Do not substitute a platform default silently; state that the preference could not be read* |
| 14 | What must never happen | — | **Guessing a previous value, reconstructing state from history, or presenting a default as a remembered value** |

## Expected outcome, failure behaviour, and explanation

> *"I set the Office lamps to the level you normally use here."*

If the remembered value cannot be read, the home says so rather than silently applying a default.

## Acceptance scenarios

| # | Given | Then | Must not |
|---|---|---|---|
| 1.1 | A room-scoped lamp level exists | It is applied where policy permits | Apply a *person* level without a sufficient Identity Assertion |
| 1.2 | No remembered value exists | The home states the absence | Substitute a platform default silently |
| 1.3 | A person-preferred level exists but was never accepted | The home **asks** | Apply it silently (**P26**, **DL-21**) |
| 1.4 | Room mode prohibits the change | Suppressed, with a reason in the trace | Present suppression as a failure |
| 1.5 | The remembered value conflicts with a current environmental constraint | **Unresolved — OD-78** | Assert that the architecture already decides this |

## Implementation status and unresolved decisions

**F** — no HTBW Core implementation exists.

| Concern | Held by |
|---|---|
| Whether restoration reproduces a prior value or computes a currently appropriate one; the value classes (*last observed*, *last successful*, *last person-selected*, *configured default*, *preference*) | **OD-78** |
| Prior/preferred **room temperature** as a Continuity-held value | **N** — no canonical document states it |
| Learned-preference promotion | **OD-28**; evidence eligibility **OD-65 (resolved — DL-112)** |

---

# Use Case 2 — The Dental Appointment Reminder

## Human outcome

Tom is in the Den in the evening. The home tells him about tomorrow's 6:30 dental appointment at a
moment that is actually useful, and does not announce it in front of guests.

## Preconditions

| Precondition | Owner | Status |
|---|---|---|
| A calendar integration is configured and available | Home Assistant | **A** — **P21** |
| **The association between Tom and that calendar** | — | **U — OD-77** |
| Interruption appropriateness for this moment | **Operational Trust** | **A** — defaults are **OD-51** |
| Audience composition in the Den | **Truth** → **Operational Trust** | **A** — **DL-34**; specification is **OD-52** |

## Ownership map

| # | Question | Owner | Statement |
|---|---|---|---|
| 1 | Authoritative Truth inputs | **Truth** | Tom is present in the Den; who else is present; current time |
| 2 | Identity requirements | **Identity** | A person-directed Communication requires an Identity Assertion meeting the configured band |
| 3 | Consent and Operational Trust requirements | **Operational Trust** | Whether Tom's calendar content may be disclosed, on this surface, before this audience (**DL-34**, **P32**) |
| 4 | What Continuity supplies | **Continuity** | **Preferred delivery and preferred presentation**, and the **re-presentation preference** if Tom moves (**DL-99**). **Not the appointment** |
| 5 | Memory scope | **Person-scoped** for the delivery/presentation preference | **A** |
| 6 | Source of record | **The calendar provider.** HTBW holds a reference; *the underlying configuration is never copied* ([../models/person-and-identity.md](../models/person-and-identity.md)) | **A** |
| 7 | Who decides | **Concierge** | Whether, when, where, and how to say it |
| 8 | Who executes | **Concierge**, through a governed delivery surface | — |
| 9 | Explainability | **Decision Trace** | Why now, why here, why this surface, and why not earlier |
| 10 | Retention and lifecycle | **DL-47**, **OD-49** | Communication content and metadata are classified **separately** |
| 11 | Guest and Unknown Person behaviour | **Operational Trust** | Private content is not disclosed to an unresolved audience; the fallback is **OD-71** |
| 12 | Multi-person conflict behaviour | **Operational Trust** | David's presence changes the audience, not the truth of the appointment |
| 13 | Failure behaviour | **DL-41** | No calendar provider configured, valid, and available → **the capability is unavailable and says so**. No local approximation stands in for it |
| 14 | What must never happen | — | **Claiming a departure time the home cannot compute**, or treating a calendar entry as a Stewardship care obligation the household never declared |

## The architecture-faithful narration

| Proposed narration | Verdict | Correct wording |
|---|---|---|
| *The Home remembered the commitment* | **Requires qualification** | The **calendar provider** holds the commitment. The home **reconnected Tom to it** and chose an appropriate moment |
| *Continuity preserved the association and relevant context* | **Not yet governed** | The person-to-calendar association has **no named owner** — **OD-77** |
| *Concierge selected an appropriate moment to remind* | **Accepted** | — |
| *Operational Trust permitted disclosure* | **Accepted** | — |
| *Stewardship marked the commitment as requiring care* | **Contradicted** | **A calendar appointment is not a care obligation.** Stewardship represents a care expectation **the household declared**; it never decides on the household's behalf that something matters |

## Acceptance scenarios

| # | Given | Then | Must not |
|---|---|---|---|
| 2.1 | Guests are present | Content-free indication or deferral, per **OD-71** | Read a private appointment aloud |
| 2.2 | The calendar provider is unavailable | The capability is unavailable and names the missing dependency | Present a stale entry as current |
| 2.3 | Tom acknowledges | Re-presentation stops | Repeat on every surface Tom passes |
| 2.4 | Travel time is requested | **Not a claimed capability** | Assert a departure time |

## Implementation status and unresolved decisions

**F**. Held by **OD-77** (person-to-calendar association), **OD-51** (interruption risk classes),
**OD-52** (audience specification), **OD-71** (audience uncertainty), **OD-44**/**OD-45** (delivery
and acknowledgement semantics), **OD-54** (retry is never escalation). Re-presentation is resolved
(**DL-99**); implementation itself remains unbuilt regardless, per the greenfield status above.
**Travel-time and routing computation are `N` — not governed, not claimed.**

---

# Use Case 3 — Follow-Me Music, Den to Kitchen

## Human outcome

Tom is listening to jazz in the Den, goes to cook, and the jazz is playing in the Living Space when
he gets there — at a sensible volume, without duplicating in the Den.

## Preconditions

| Precondition | Owner | Status |
|---|---|---|
| Follow-Me enabled for the person or session | **Continuity** | **A** |
| Identity resolved above the configured band | **Identity** | **A** |
| Unambiguous room transition, origin and destination both known and different | **Truth** | **A** |
| Manual-stop protection and cooldown not active | **Continuity** | **A** |
| Destination Room has configured, valid, available playback targets | Room Configuration + **Truth** | **A** |

## Ownership map

| # | Question | Owner | Statement |
|---|---|---|---|
| 1 | Authoritative Truth inputs | **Truth** | Presence, room transition, existing destination experience, endpoint availability, Room mode |
| 2 | Identity requirements | **Identity** | Whose session is this, and is the person in the destination the session owner |
| 3 | Consent and Operational Trust requirements | **Operational Trust** | Explicit / Assisted / Autonomous mode; authority to displace another person's session |
| 4 | What Continuity supplies | **Continuity** | Session identity, owner, participants, origin Room, current Room, Follow-Me intent, **transfer eligibility with blocking attribution** |
| 5 | Memory scope | **Person-scoped**: preferred artist, genre, album, playlist; personal Follow-Me setting; current personal media session. **Room-scoped**: last song, last genre, music volume, duck volume, TTS volume | **A** — the preserved scoping rule |
| 6 | Source of record | **The media provider and Home Assistant** for playback state (**DL-46**, **P21**) | **A** |
| 7 | Who decides | **Concierge** | — |
| 8 | Who executes | **Concierge**, through governed interfaces | Continuity never performs playback |
| 9 | Explainability | **Decision Trace** | *"I moved the jazz because you asked the music to follow you, I recognised you here, and the room was free"* |
| 10 | Retention and lifecycle | **DL-47** | Session and transfer history are Continuity's; scope and duration of experience history are **OD-26** |
| 11 | Guest and Unknown Person behaviour | **Operational Trust** | An Unknown Person owns no session and inherits no preference (**DL-33**) |
| 12 | Multi-person conflict behaviour | **Operational Trust** / **Concierge** | *Another person's session would be displaced without authority* is a representable block. Concurrency is resolved as **DL-102** (endpoint-class contention; suppressed transfer, as in this use case); merge policy remains **OD-24** |
| 13 | Failure behaviour | **Continuity** | Missed transition → treat the newly observed Room as current, record the gap, **do not retroactively transfer**. Partial speaker-group availability → configured policy, and say which members were unavailable |
| 14 | What must never happen | — | **Motion-triggered movement.** Follow-Me is a policy-governed handoff |

## The utterance problem

The proposed narration has Tom say *"I need to make dinner"* and the home answer *"I'll move the music
to the kitchen for you."*

| Element | Verdict | Basis |
|---|---|---|
| The transfer itself | **Supported** | [follow-me-media.md](follow-me-media.md) Scenario 1 |
| An **explicit** trigger — *"Have the music follow me"* | **Supported** | The canonical trigger in every accepted document |
| A **standing** Follow-Me preference producing an autonomous move | **Supported** | The Autonomous mode, *because policy permits it* |
| **Inferring a media-transfer intent from *"I need to make dinner"*** | **Not yet governed** | No accepted document maps an indirect utterance to a room-to-room media transfer. Intent interpretation is Concierge's, but **no rule authorises this inference**, and **DL-30** is not discharged by assertion |
| Movement inside the **Living Space** Merged Room | **Neither transfer nor resume** | No Room Context changed |

**Narration remedy:** either Tom asks for the music to follow him, or the household has already
enabled Follow-Me and the home moves it because the household said it may. The home may also **offer**
— *"Would you like the music in the kitchen?"* — which is the Assisted mode and is fully governed.

## Acceptance scenarios

| # | Given | Then | Must not |
|---|---|---|---|
| 3.1 | Follow-Me enabled, transition unambiguous, destination free | Eligible; Concierge transfers | Treat eligibility as the decision |
| 3.2 | Destination Room in Nighttime mode | `transfer_eligible: false`, `blocked_by: operational_trust` | Report suppression as a failure |
| 3.3 | David's session is already active in the destination | Displacement requires authority | Merge or terminate unilaterally |
| 3.4 | Kitchen and Dining are inside the Living Space Merged Room | Nothing happens, and nothing needs to | Invent a merged-room orchestration path |
| 3.5 | Tom stopped the music by hand a minute ago | Manual-stop protection blocks the move | Override a manual stop |
| 3.6 | The provider's session cannot be handed off | **Unresolved** — provider session semantics are `N` | Claim a governed handoff protocol exists |

## Implementation status and unresolved decisions

**F**. Governed: eligibility, blocking, scoping, suppression, concurrency (**DL-102**, resolving
**OD-27** — endpoint-class contention, not Session/Experience class; duplicate playback is a semantic
`Current Room` guarantee only, never a provider-render guarantee). Unresolved: **OD-24** merge,
**OD-25** resume window. **Not governed (`N`)**: provider session-state handoff, grouped/joined
playback spanning separate non-merged Rooms (within one Merged Room this requires no new architecture
— **DL-13**), and indirect-intent inference.

---

# Use Case 4 — Audiobook Resume

## Human outcome

David picks up his book in the Primary Bedroom where he left it in the Den yesterday.

## Preconditions

| Precondition | Owner | Status |
|---|---|---|
| A resume candidate exists within its eligibility window | **Continuity** | **A** — window defaults are **OD-25** |
| The playback position | **The audiobook provider** | **A** — **DL-46**, **P21** |
| **The association between David and that audiobook account** | — | **U — OD-77** |

## Ownership map

| # | Question | Owner | Statement |
|---|---|---|---|
| 1 | Authoritative Truth inputs | **Truth** | David is present; the destination Room has no conflicting active session |
| 2 | Identity requirements | **Identity** | Person-scoped resume requires a sufficient Identity Assertion |
| 3 | Consent and Operational Trust requirements | **Operational Trust** | Whether resume is Explicit, Assisted, or Autonomous for this class |
| 4 | What Continuity supplies | **Continuity** | Resume state, resume eligibility, session ownership, and a **Governed Reference** to the provider's position |
| 5 | Memory scope | **Person-scoped** session ownership; **room-scoped** resume state where the household configured it that way | **A** |
| 6 | Source of record | **The provider.** HTBW *persists no second copy merely to explain later* (**DL-46**) | **A** |
| 7 | Who decides | **Concierge** | Offer, resume, or stay silent |
| 8 | Who executes | An executor, through governed interfaces | — |
| 9 | Explainability | **Decision Trace** | *"You left this in the Den yesterday evening"* |
| 10 | Retention and lifecycle | **OD-25**, **OD-26**, **DL-47** | When a resume candidate expires, and whether experience history is per person, per room, or both |
| 11 | Guest and Unknown Person behaviour | **DL-33** | An Unknown Person has no resume candidate and inherits none |
| 12 | Multi-person conflict behaviour | **Continuity** → **Operational Trust** | Household-shared progress and person-specific progress are different records; the distinction depends on **OD-77** |
| 13 | Failure behaviour | **DL-41** | Provider unavailable → capability unavailable, dependency named. **A remembered position is never re-derived** |
| 14 | What must never happen | — | **Duplicating the provider's playback position into HTBW as a second source of record** |

## On the words *journey*, *checkpoint*, and *progress marker*

**None of these is a first-class HTBW model.** The glossary defines **Experience** and **Session**;
there is no Journey object, no checkpoint object, and no progress-marker object. They are acceptable
as **narrative groupings** and must not be presented as architecture. What is real is: an Experience,
a Session with a lifecycle, a resume candidate, an eligibility window, and a **Governed Reference** to
provider-owned state.

## Acceptance scenarios

| # | Given | Then | Must not |
|---|---|---|---|
| 4.1 | A resume candidate is within its window | Concierge may offer or resume, per policy | Resume autonomously where the mode is Assisted |
| 4.2 | The window has expired | No offer | Offer a months-old candidate as though it were current |
| 4.3 | Provider position and remembered reference disagree | **The provider is authoritative** | Present the HTBW reference as the position |
| 4.4 | Two people share one household account | **Unresolved — OD-77** | Attribute one person's progress to another |

## Implementation status and unresolved decisions

**F**. Held by **OD-25**, **OD-26**, **OD-77**. Conflict resolution between provider state and
remembered reference is `E` — it follows from **DL-46** but is not written into a canonical model.

---

# Use Case 5 — Tom and David's Interaction Styles

## Human outcome

Tom gets the thorough answer with its evidence. David gets the short one. Neither gets a *different*
answer.

## Preconditions

| Precondition | Owner | Status |
|---|---|---|
| Continuity holds preferred delivery and preferred presentation | **Continuity** | **A** — [stewardship-use-cases.md](stewardship-use-cases.md) ownership map row 11; [../models/communication.md](../models/communication.md) *Continuity — re-presentation preference and personal surface defaults* |
| Identity resolves the person to a band sufficient for person-scoped preference application | **Identity** → **Operational Trust** | **A** — **DL-36**, **DL-39** |
| **The preference dimensions themselves** — verbosity, depth, citation, modality, locale, accessibility, per-capability override | — | **A — DL-100.** Accessibility/comprehension are Person-borne requirements, never overridden by Room character; the rest are ordinary Continuity preferences; Room persona/voice are Foundation/Room Configuration's |

## Ownership map

| # | Question | Owner | Statement |
|---|---|---|---|
| 1 | Authoritative Truth inputs | **Truth** | Who is present and can perceive the surface |
| 2 | Identity requirements | **Identity** | **Applying a person's preferences is a person-scoped capability access**, evaluated against the current Identity Assertion — *not a consequence of the home having addressed someone by name* |
| 3 | Consent and Operational Trust requirements | **Operational Trust** | Whether person-scoped preference participation is consented; consent *gates eligibility, not weight* |
| 4 | What Continuity supplies | **Continuity** | The preferred delivery and presentation, versioned and revocable |
| 5 | Memory scope | **Person-scoped** | **A** |
| 6 | Source of record | **Continuity** | This is one of the few classes HTBW genuinely owns |
| 7 | Who decides | **Concierge** | Presentation is Concierge's; the preference is not |
| 8 | Who executes | **Concierge**, optionally assisted by a **Reasoning Provider** | The provider *owns nothing* |
| 9 | Explainability | **Decision Trace** | The **exact version** of the preference used (**P30**) |
| 10 | Retention and lifecycle | **DL-47** | Preference history is Continuity's |
| 11 | Guest and Unknown Person behaviour | **DL-33** | An Unknown Person *owns no preferences* and *inherits nothing from any resident* |
| 12 | Multi-person conflict behaviour | **Operational Trust** | With both present, the audience governs; one person's verbosity preference does not select what the other may hear |
| 13 | Failure behaviour | **DL-41** | No reasoning provider configured, valid, and available → the dependent capability is unavailable and says so. **Removing the provider degrades phrasing, never correctness** |
| 14 | What must never happen | — | **A presentation preference changing what is true.** Preferences influence how something is said, never whether it is so |

## Where the preference dimensions actually stand

| Dimension | Where it appears | Status |
|---|---|---|
| `verbosity: minimal / balanced / detailed` | [../models/person-profile-model.md](../models/person-profile-model.md) | **Historical — superseded.** Not authority |
| *person context may tune verbosity and detail level only* | [../contracts/service-contracts.md](../contracts/service-contracts.md) | **Historical — superseded.** Not authority |
| *presentation preferences* | [../architecture/adr-personalization-governance.md](../architecture/adr-personalization-governance.md) | **Historical — superseded.** Not authority |
| *Preferred interaction patterns* | [../models/continuity.md](../models/continuity.md) | **Canonical**, and now fully enumerated and classified by *Presentation Preference Scope and Precedence (DL-100)* |

**The ownership is settled — Continuity. The enumeration and Room-scope precedence are now settled —
DL-100 (resolving OD-79).**

**Whether a person-scoped preference may name or steer a reasoning provider is resolved — it does not
(OD-67, accepted DL-93)**, and nothing here presumes a provider abstraction.

## Acceptance scenarios

| # | Given | Then | Must not |
|---|---|---|---|
| 5.1 | Tom's detailed preference is held and Identity is sufficient | The answer is fuller | Change any fact, threshold, or conclusion |
| 5.2 | Identity is below the required band | Neutral presentation | Refuse the underlying request because a *presentation* threshold was unmet |
| 5.3 | Both Tom and David are present | Audience governs | Apply one resident's preference to content the other may not receive |
| 5.4 | The reasoning provider is unavailable | Plain, correct phrasing | Silently approximate it locally |

## Implementation status and unresolved decisions

**F**. Ownership **A**; enumeration **A — DL-100**; provider preference **resolved — DL-93 (OD-67)**; consent experience **OD-06**.

---

# Use Case 6 — Person-to-Calendar and Person-to-Mailbox Associations

## Human outcome

*"What's on my calendar?"* returns Tom's calendar for Tom and David's for David, without either
gaining access to the other's.

## Preconditions

| Precondition | Owner | Status |
|---|---|---|
| Calendar and mailbox integrations exist and are configured | Home Assistant | **A** — **P21** |
| HTBW references them and never copies their configuration | Foundation / **P22** | **A** — [../models/person-and-identity.md](../models/person-and-identity.md) |
| **A governed person-to-external-resource association with a named owner** | — | **U — OD-77.** This is the defect |

## The verified gap

[../models/person-and-identity.md](../models/person-and-identity.md) lists the extension:

> | Mailbox, calendar, and other external-service references | Referenced through the responsibility that governs their use; **the underlying configuration is never copied** |

**No responsibility is named**, and [../contracts/foundation-contract.md](../contracts/foundation-contract.md)
declares the relationship types as **`caretaker-of`, `owner-of`, `serves-room`, and `located-in`** —
none of which expresses *this account belongs to this person*.

Every personal-resource use case in this document depends on that association: the dental reminder,
the audiobook resume, the person-scoped media profile, and the mail summary. **It is recorded as a
defect rather than invented here.**

## Ownership map

| # | Question | Owner | Statement |
|---|---|---|---|
| 1 | Authoritative Truth inputs | **Truth** | Presence and audience only. An association is a definition, not a Fact |
| 2 | Identity requirements | **Identity** | Establishes *who is asking*, to a band the capability requires |
| 3 | Consent and Operational Trust requirements | **Operational Trust** | *Who may access calendars, messages, email, or history* is explicitly Operational Trust's |
| 4 | What Continuity supplies | **Continuity** | **Preferred delivery and presentation only.** Continuity's ownership list does **not** include external-service references |
| 5 | Memory scope | **Person-scoped**, once an owner exists | **U — OD-77** |
| 6 | Source of record | **The provider.** HTBW owns no calendar contents, no mailbox contents, and **no credentials** | **A** — **P22**, [../architecture/connected-storage.md](../architecture/connected-storage.md) |
| 7 | Who decides | **Concierge** | — |
| 8 | Who executes | The provider integration | — |
| 9 | Explainability | **Decision Trace** | Which association was used, and why the request was answered or refused |
| 10 | Retention and lifecycle | **DL-43**, **DL-45**, **DL-47** | Revocation, reassignment, participant removal, and stale-association detection are part of **OD-77** |
| 11 | Guest and Unknown Person behaviour | **DL-33** | An Unknown Person *references no Person* and *grants nothing*. Access defaults to household-neutral context |
| 12 | Multi-person conflict behaviour | **Operational Trust** | *My calendar* resolves through the requestor's association, never through room occupancy |
| 13 | Failure behaviour | **DL-41** | No association, or a broken reference → capability unavailable, dependency named. A dangling reference *is reported, never silently rendered as though the source record never existed* |
| 14 | What must never happen | — | **HTBW storing credentials, tokens, calendar contents, or mailbox contents**; or resolving *my calendar* by guessing from who is in the room |

## The four-line claim, corrected

| Proposed line | Verdict |
|---|---|
| *Identity establishes who is engaging* | **Supported** |
| *Continuity reconnects the person to the governed personal context* | **Not yet governed.** No document assigns this to Continuity — **OD-77** |
| *Operational Trust determines whether the resource may be accessed or disclosed* | **Supported** |
| *Concierge consumes that context to fulfil an appropriate request* | **Supported** |

## Acceptance scenarios

| # | Given | Then | Must not |
|---|---|---|---|
| 6.1 | Tom asks for *my calendar* | The association resolves from the **requestor** | Resolve from room occupancy |
| 6.2 | A person leaves the household | The association is revocable and its removal is recorded | Leave an orphaned association resolving silently |
| 6.3 | A guest asks | Household-neutral context only | Inherit any resident association |
| 6.4 | The integration is removed | Broken-reference state is reported | Render the capability as though it still worked |

## Implementation status and unresolved decisions

**U / F**. **OD-77** is the governing decision. Dependent: **OD-06** consent experience, **OD-09**
portability and erasure, **DL-69** (resolved **OD-62**) governed conversational retrieval.

---

# Use Case 7 — The Morning Calendar Rhythm

## Human outcome

Tom makes coffee most mornings and asks for the day's calendar. Eventually the home offers first —
but only because Tom said it could.

## Ownership map

| # | Question | Owner | Statement |
|---|---|---|---|
| 1 | Authoritative Truth inputs | **Truth** | Presence in the Living Space; time of day |
| 2 | Identity requirements | **Identity** | *An observation may be attributed to a person only where identity confidence meets the threshold. Below it, the evidence is room-scoped or discarded, never guessed* |
| 3 | Consent and Operational Trust requirements | **Operational Trust** | Whether the context may be used at all, and whether an unsolicited offer is an acceptable interruption (**OD-51**) |
| 4 | What Continuity supplies | **Continuity** | **The approved preference — not the observations.** The observation that produced the suggestion is a **Domain Event owned by the responsibility that observed it** |
| 5 | Memory scope | **Person-scoped** or **room-scoped** — *learning respects this split rather than replacing it* | **A** |
| 6 | Source of record | Home Assistant for native activity (**DL-46**); Continuity for the approved preference | **A** |
| 7 | Who decides | **Concierge** | Whether, when, and how to offer |
| 8 | Who executes | **Concierge** | — |
| 9 | Explainability | **Decision Trace** | *"You accepted this in March, so I offer it at this time. You can pause or remove it."* |
| 10 | Retention and lifecycle | **OD-28** | Proposal, acceptance, rejection, correction, pause, forgetting, versioning, revocation — *every stage transition is a governed change with a Change Record* |
| 11 | Guest and Unknown Person behaviour | **DL-33**, **OD-65 (resolved — DL-112)** | An Unknown Person's interactions *are never eligible evidence for person-scoped learning* |
| 12 | Multi-person conflict behaviour | **Operational Trust** | An offer in a shared room is an audience-evaluated Communication |
| 13 | Failure behaviour | **Concierge** | Dismissal is recorded; **resolved — OD-65 / DL-112**: dismissal is non-acceptance, never automatic negative evidence; repeated dismissal is reportable as its own Pattern about the proposal's treatment, never as "the resident dislikes the outcome" |
| 14 | What must never happen | — | **Silent promotion.** *An observed pattern must not silently become an autonomous policy* (**P26**, **DL-21**) |

## Is *"the home learned the routine"* valid public language?

**Only with qualification.** The accurate public sentence is:

> *"The home noticed the pattern, asked whether you wanted it, and does it because you said yes."*

Saying *the home learned* without the acceptance step describes a system this architecture explicitly
prohibits. The full ladder is in
[../architecture/behavioral-governance.md](../architecture/behavioral-governance.md), and
[why-did-this-happen.md](why-did-this-happen.md) Scenarios 16 and 18 are the canonical worked pair:
Scenario 16 — *nothing changes automatically*; Scenario 18 — *a person with authority accepted it*.

## Acceptance scenarios

| # | Given | Then | Must not |
|---|---|---|---|
| 7.1 | A pattern is observed | Nothing behavioural happens | Write a preference |
| 7.2 | A suggestion is made and accepted | It becomes a versioned, revocable Continuity preference | Store it as a separate learned-preference store |
| 7.3 | The offer is repeatedly dismissed | The pattern is itself reportable | Keep offering unchanged and unrecorded |
| 7.4 | Identity is below threshold that morning | Room-scoped evidence, or none | Attribute the observation to Tom |

## Implementation status and unresolved decisions

**F**. **OD-28** lifecycle; **OD-65** evidence eligibility, **resolved — DL-112**; **OD-63** attribution,
**resolved — DL-73**; **OD-64** native observation, **resolved — DL-111**; **OD-51** interruption.

---

# Use Case 8 — Maisey's Care Continuity

## Human outcome

Maisey's medication, vet visits, and follow-ups are not forgotten, and the reminder arrives the way
the household wants to receive it.

## The boundary this use case exists to protect

| Element | Owner | Not |
|---|---|---|
| That Maisey's care matters, and what caring means | **The household declares; Stewardship represents** | Not Continuity |
| The medication schedule and its obligation state | **Stewardship** | Not Continuity |
| Medication-reminder, veterinary, and follow-up **history** | **Stewardship** | Not Continuity |
| **Preferred delivery, preferred presentation, re-presentation** | **Continuity** | Not Stewardship |
| Whether the reminder may be delivered here, now, to this audience | **Operational Trust** | — |
| Whether it is delivered, and how it is said | **Concierge** | — |

**Stewardship history is Stewardship's**, under the shared temporal model — *each responsibility owns
the history of its own records*. **Continuity may consume it; Continuity does not become its owner.**
Equally, **no general preference, Follow-Me, resume, transfer, or experience restoration moves into
Stewardship.**

**A Pet is not a Person and is not an Asset.** See [../models/asset.md](../models/asset.md) and
[stewardship-use-cases.md](stewardship-use-cases.md) Use Case 2.

## Ownership map

| # | Question | Owner | Statement |
|---|---|---|---|
| 1 | Authoritative Truth inputs | **Truth** | Whether the household is present, and audience composition |
| 2 | Identity requirements | **Identity** | Only for a person-directed Communication |
| 3 | Consent and Operational Trust requirements | **Operational Trust** | Delivery entitlement and disclosure |
| 4 | What Continuity supplies | **Continuity** | Delivery and presentation preference, and re-presentation (**DL-99**) — **nothing else** |
| 5 | Memory scope | **Person-scoped** preference; the obligation is **Stewardship-scoped** | **A** |
| 6 | Source of record | **Stewardship** for the obligation; a native Calendar, Schedule, or `todo` where the household uses one (**OD-23**) | **A / U** |
| 7 | Who decides | **Concierge** | — |
| 8 | Who executes | An executor, or a person | **Stewardship never acts** |
| 9 | Explainability | **Decision Trace** | The obligation, the declaration, the authority, and the outcome |
| 10 | Retention and lifecycle | **DL-47** | Obligation and care history follow Stewardship's retention, not Continuity's |
| 11 | Guest and Unknown Person behaviour | **Operational Trust** | Pet-health content is household-private by default |
| 12 | Multi-person conflict behaviour | **Stewardship** | Caretaker assignment and the escalation ladder are Stewardship's (**OD-22**) |
| 13 | Failure behaviour | **Stewardship** | *Absence of evidence is never compliance*; `unknown` is never `met` |
| 14 | What must never happen | — | **Continuity absorbing care history**, or a dismissed reminder closing an obligation |

## Acceptance scenarios

| # | Given | Then | Must not |
|---|---|---|---|
| 8.1 | A dose is due | A Stewardship obligation exists | Model it as a Continuity resume candidate |
| 8.2 | The reminder is dismissed | The obligation remains open | Close it (**OD-75**) |
| 8.3 | Tom prefers spoken reminders in the Den | Continuity supplies that preference | Let Stewardship choose the surface |

## Implementation status and unresolved decisions

**F**. **OD-75** obligation lifecycle and completion evidence, **OD-22** escalation, **OD-23**
projection surface. Re-presentation is resolved (**DL-99**); implementation itself remains unbuilt
regardless, per the greenfield status above.

---

# Use Case 9 — Artwork Caretaker Notification

## Human outcome

Conditions in the Den drift outside the watercolour's declared limits, and the right person hears
about it in the right way.

## Ownership map

| # | Question | Owner | Statement |
|---|---|---|---|
| 1 | Authoritative Truth inputs | **Truth** | Den temperature, humidity, illuminance — with confidence, provenance, and freshness |
| 2 | Identity requirements | **Identity** | Required for the person-directed Communication, not for the assessment |
| 3 | Consent and Operational Trust requirements | **Operational Trust** | Which channel, which audience, and what may be disclosed |
| 4 | What Continuity supplies | **Continuity** | The caretaker's preferred delivery and presentation, and re-presentation if they move |
| 5 | Memory scope | **Person-scoped** preference only | **A** |
| 6 | Source of record | **Foundation** for the Asset and its declared limits; **Stewardship** for significance and caretaker assignment; **Truth** for conditions | **A** |
| 7 | Who decides | **Concierge** | — |
| 8 | Who executes | An executor | **Stewardship never closes the door** |
| 9 | Explainability | **Decision Trace** | Asset limit → Truth Fact → obligation → authority → action |
| 10 | Retention and lifecycle | **DL-47** | Obligation history is Stewardship's |
| 11 | Guest and Unknown Person behaviour | **Operational Trust** | Asset value and location are sensitive |
| 12 | Multi-person conflict behaviour | **Stewardship** | The escalation ladder decides who is next (**OD-22**) |
| 13 | Failure behaviour | **DL-41** | A missing sensor makes the assessment `unknown`, never `met` |
| 14 | What must never happen | — | **Continuity supplying the significance, the limit, or the caretaker.** Those are Stewardship's and Foundation's |

This use case is deliberately thin on the Continuity side. **That thinness is the finding**: the full
walkthrough already exists as [stewardship-use-cases.md](stewardship-use-cases.md) Use Case 1, and
Continuity's entire contribution is *how the caretaker prefers to be told*.

---

# Use Case 10 — Irrigation and Weather

## Human outcome

The garden is watered responsibly, and skipped cycles are explainable.

## The correction this use case records

The proposed narration assigned to Continuity: *last watering event, watering history, soil-moisture
history, recent rainfall, weather observations, seasonal patterns, prior outcomes, relevant care
history.*

**This is contradicted by accepted architecture.**
[stewardship-use-cases.md](stewardship-use-cases.md) Use Case 7 ownership map row 11 reads:

> | 11 | Continuity interaction | **None** | — |

and row 12:

> | 12 | Retention | **DL-47** | Obligation and decision history; **weather Facts are Truth's Historical Facts** |

| Element | Correct owner |
|---|---|
| Rainfall, forecast, soil-moisture observations, and their history | **Truth**, as Facts and Historical Facts |
| The watering requirement and whether it is satisfied | **Stewardship** |
| Watering-event and outcome history | **Stewardship** obligation and care history, plus Home Assistant's own automation activity (**DL-46**) |
| Municipal or household water restriction | **Operational Trust** — *a prohibition, not a preference to be weighed* |
| The recommendation candidate | A permitted **Reasoning Provider**, which *owns nothing* — **OD-67** |
| Whether to offer, and how it is worded | **Concierge** |
| Opening the valve | The **irrigation controller integration, automation, or schedule**. *Stewardship never opens a valve* |
| Preferred delivery of the offer | **Continuity** |

**Continuity's role in this scenario is the delivery preference and nothing more.**

## What must never happen

| Prohibition | Basis |
|---|---|
| Inferring soil condition from rainfall | *No unsupported soil inference. Absent a moisture sensor, the home does not know whether the ground is wet* |
| Stewardship owning, fetching, or caching weather | *Stewardship does not own weather truth, and does not fetch a forecast* |
| An LLM becoming the authority for plant care | *A reasoning provider owns nothing… its output never silently becomes a Fact, and its recommendation never silently becomes an authorised action* |
| A recommendation becoming an authorisation | *Operational Trust owns permission. A recommendation never silently becomes an authorised action* |
| Watering automatically without household authorisation | The autonomy ceiling is Operational Trust's |
| Presenting a fallback decision as a weather-informed one | Acceptance scenario 7.7 |

## Where plant-care knowledge belongs

| Candidate framing | Verdict |
|---|---|
| Ephemeral AI output | **Permitted, but authoritative for nothing.** Retained as *the consultation record, and the decision that accepted it* ([../models/temporal-record.md](../models/temporal-record.md)) |
| A reviewed household care profile | **The architecture-faithful home** — the household **declares** the care expectation; Stewardship represents it |
| Governed external knowledge owned by HTBW | **Not governed.** HTBW defines no plant-care knowledge base and none is created here |

**Deterministic environmental logic is sufficient for the obligation. AI assistance is optional,
replaceable, and never load-bearing** — removing it degrades phrasing, never correctness.

## Implementation status and unresolved decisions

**F**. **OD-63** attribution, **OD-64** native automation as governed executor evidence, **OD-67**
reasoning-provider strategy, **OD-75** *satisfied without action* versus *performed*.

---

# Use Case 11 — Music, Book, and Television Recommendation Candidates

## Human outcome

Suggestions that feel like they know the household, without the household feeling watched.

## Ownership map

| # | Question | Owner | Statement |
|---|---|---|---|
| 1 | Authoritative Truth inputs | **Truth** | Who is present, and what is playing now |
| 2 | Identity requirements | **Identity** | Person-scoped observation requires a sufficient assertion; otherwise room-scoped or discarded |
| 3 | Consent and Operational Trust requirements | **Operational Trust** | Whether the data may be used at all |
| 4 | What Continuity supplies | **Continuity** | Person-scoped preferred artist, genre, album, playlist; room-scoped last song and last genre; experience history |
| 5 | Memory scope | The **preserved scoping rule** — taste is a property of the person; volume is a property of the room | **A** |
| 6 | Source of record | **The content provider** remains authoritative for playback history and its own recommendations (**P21**, **DL-46**) | **A** |
| 7 | Who decides | **Concierge** | Whether, when, and how to present |
| 8 | Who executes | **Concierge** | — |
| 9 | Explainability | **Decision Trace** | Why this was suggested, and on what evidence |
| 10 | Retention and lifecycle | **OD-26**, **DL-47** | Experience-history scope and duration are open |
| 11 | Guest and Unknown Person behaviour | **DL-33** | No person-scoped learning from an Unknown Person; guests must not see residents' preferences or history |
| 12 | Multi-person conflict behaviour | **Operational Trust** | Shared viewing is not personal viewing; a recommendation before guests is an audience-evaluated disclosure |
| 13 | Failure behaviour | **DL-41** | Provider or reasoning-provider unavailable → the capability is unavailable and says so |
| 14 | What must never happen | — | **Continuity recommending anything.** *Continuity feeds Concierge; Continuity does not choose* |

## Where each proposed element actually sits

| Proposed element | Owner | Status |
|---|---|---|
| Preferred artist, genre, album, playlist | **Continuity**, person-scoped | **A** |
| Last song, last genre, music/duck/TTS volume | **Continuity**, room-scoped | **A** |
| Completion, skip, abandonment, engagement observations | **Domain Events**, owned by the responsibility that observed them; native media activity stays with Home Assistant (**DL-46**) | **E** |
| Correlating observations into candidates | A permitted intelligence, under **OD-28** / **OD-65 (resolved — DL-112)** / **OD-67 (resolved — DL-93)** | **U, pending OD-28 only** |
| Presenting the recommendation | **Concierge** | **A** |
| Accidental playback, preference correction, feedback, expiry | **OD-28**; eligibility itself resolved — **OD-65 / DL-112** (one-off/accidental activity is explicitly insufficient for a Pattern; a correction is new evidence, never a rewrite) | **Partially A — expiry/lifecycle pending OD-28** |

## Acceptance scenarios

| # | Given | Then | Must not |
|---|---|---|---|
| 11.1 | A guest plays something | It is not eligible person-scoped evidence | Attribute it to a resident |
| 11.2 | A track was played by accident | Correction is possible | Treat one play as a preference |
| 11.3 | A candidate exists but was never accepted | The home may **offer** | Apply it as a policy |
| 11.4 | The provider offers its own recommendations | The provider remains authoritative for them | Present a provider recommendation as an HTBW conclusion |

---

# Use Case 12 — Household Traditions

## Human outcome

The Sunday dinner lighting, the holiday scene, the welcome-home moment — the things that make a house
feel like this household's home.

## The honest finding

**The repository says nothing about traditions, rituals, celebrations, or household culture.** A
repository-wide search returns no match for *tradition* or *ritual* in any canonical document.

**Nothing is created here to fill that silence.** What the architecture *does* already provide:

| Narrative idea | Nearest accepted construct | Status |
|---|---|---|
| A recurring shared moment | An **Experience** — *a coherent household-facing activity that can be started, transferred, resumed, suppressed, or ended* | **A** |
| An authored household routine | A household-owned Home Assistant scene, script, or automation. *The household owns this behaviour through Home Assistant. HTBW owns none of it* | **A** |
| A repeated occurrence noticed by the home | A **Pattern** on the promotion ladder — *nothing behavioural* | **A** |
| *The home decided this is now a tradition* | **Prohibited** | **P26**, **DL-21** |

**The risk the narration must not take:** a repeated event is a pattern, not a meaning. Deciding that
a recurrence *matters* is a **household declaration**, and *Stewardship never decides on the
household's behalf that something matters*. The same rule protects traditions.

Household agency, transparency, editability, expiry, and explainability are therefore already
required — through the promotion ladder, **OD-28**, and **DL-47** — without a tradition model.

**Status: `N` — not governed, and legitimately narratable only as a future possibility.**

---

# Use Case 13 — Correction, Revocation, Expiration, and Deletion

## Human outcome

The home learned the wrong thing, and Tom can fix it — and the fix is itself explainable.

## Ownership map

| # | Question | Owner | Statement |
|---|---|---|---|
| 1 | Authoritative Truth inputs | **Truth** | Not engaged. Correcting a preference is not correcting a Fact |
| 2 | Identity requirements | **Identity** | Correcting a person-scoped preference requires authority over it |
| 3 | Consent and Operational Trust requirements | **Operational Trust** | Owns retention policy, privacy policy, and **Preservation Hold** authority |
| 4 | What Continuity supplies | **Continuity** | The preference, its version history, and its revocability |
| 5 | Memory scope | Whatever scope the record already had | **A** |
| 6 | Source of record | Each responsibility, for its own records | **A** |
| 7 | Who decides | The **household** | Correction is a household right, not a system judgement |
| 8 | Who executes | The owning responsibility | — |
| 9 | Explainability | **Decision Trace** | *A correction must not overwrite prior history. A correction is a new Change Record* |
| 10 | Retention and lifecycle | **DL-47** | *Every governed record class declares its retention.* *"Undecided" is not a retention strategy* |
| 11 | Guest and Unknown Person behaviour | **DL-33** | There is nothing to correct; an Unknown Person holds nothing |
| 12 | Multi-person conflict behaviour | **Operational Trust** | Who may correct whose preference is an authority question |
| 13 | Failure behaviour | **P30** | A Decision Trace references the **exact version** used, so a past explanation stays accurate after the preference changed |
| 14 | What must never happen | — | **Overwriting history to make the present tidy**; deleting a record under Preservation Hold |

## The memory classes, and who owns each

This is the distinction the narration needs and the repository had not stated in one place:

| Class | Owner | Lifecycle |
|---|---|---|
| **Current operational memory** — what is wanted, what is running | **Continuity**, as a Current Projection | Replaced rather than retained (**DL-47**) |
| **Historical evidence** — what was observed | The responsibility that observed it, as **Domain Events** | External History Retention |
| **Historical Fact** — what was true then | **Truth** | Truth-owned history; *never presented as current or actionable* |
| **Learned preference** — an accepted proposal | **Continuity**, versioned and revocable | **OD-28** |
| **Inferred pattern** — not yet accepted | Not a preference and not a store | *Nothing behavioural* |
| **Authored household policy** | **Operational Trust** | Policy version history |
| **External source reference** | A **Governed Reference**; the source keeps the content | Broken references are reported, never silently hidden |
| **Source-owned content** — calendar entries, mail, playback position | **The provider** | HTBW *persists no second copy merely to explain later* (**DL-46**) |
| **Derived recommendation** | Nobody owns it as truth. *A reasoning provider owns nothing* | Retained as the consultation record and the decision that accepted it |
| **Retained explanation artifact** — the Decision Trace | **Concierge** | External History Retention, unless a floor or Preservation Hold applies (**DL-47**, **OD-05**, **OD-29**) |

## Why Continuity cannot become a data lake

Three accepted rules do this work, and no fourth is needed:

1. **DL-46** — Home Assistant retains native activity; HTBW retains only the governed meaning Home
   Assistant does not represent, **by reference rather than copy**.
2. **DL-47** — every governed record class declares its retention, or it is not accepted.
3. **P22 / connected storage** — *connected storage never becomes a shadow system of record for
   something Home Assistant already owns authoritatively.*

## Acceptance scenarios

| # | Given | Then | Must not |
|---|---|---|---|
| 13.1 | Tom corrects a learned preference | A new Change Record; the old version remains referenceable | Overwrite the prior value |
| 13.2 | Tom revokes a preference | The adaptive policy stops; past actions remain explainable | Erase the trace that explained them |
| 13.3 | A retention ceiling is reached | The record expires per its class | Apply one retention rule across all classes |
| 13.4 | A Preservation Hold applies | Normal purge is blocked | Treat the hold as a legal claim |
| 13.5 | Deletion and a retention floor conflict | **Unresolved — OD-36** | Resolve it by preference |

---

# Use Case 14 — Guests, Unknown People, and Multi-Person Conflict

## Human outcome

Nobody's private context leaks, and nobody is guessed at.

## The accepted rules, restated in one place

| Rule | Basis |
|---|---|
| **Unknown Person is a valid outcome**, and never a native Person | **DL-33** |
| An Unknown Person *owns no preferences or history, inherits nothing from any resident, generates no person-scoped learning, and grants nothing* | **DL-33** |
| Unknown Person access defaults to **household-neutral context** | **DL-33** |
| *Guests must not see residents' preferences or history* | Continuity model and contract, privacy constraints |
| **Participation is optional and requires consent**; consent *gates eligibility, not weight* | [../architecture/privacy.md](../architecture/privacy.md) |
| An observation is attributed to a person only where confidence meets the threshold; below it, **room-scoped or discarded, never guessed** | [../architecture/behavioral-governance.md](../architecture/behavioral-governance.md) |
| Displacing another person's session requires **authority granted by Operational Trust** | [../models/experience-and-session.md](../models/experience-and-session.md) |
| Two sessions claiming one Room are **surfaced to Concierge, never merged or terminated unilaterally** | Continuity contract |
| Audience composition is a first-class input, and **disclosure is separate from knowledge** | **DL-34**, **P32** |

## Unresolved

**OD-24** session merge · **OD-27** concurrency · **OD-52** audience specification · **OD-71** audience
uncertainty · **OD-72** unknown-actor correlation confidence.

The full walkthrough is [multi-person-conflict.md](multi-person-conflict.md); it is not duplicated
here.

---

# Use Case 15 — Explaining What Was Remembered

## Human outcome

*"Why did you do that?"* has an answer, every time — including *"I can't tell you."*

## What the home can say

| Situation | The home says |
|---|---|
| A remembered room value was applied | *"I set it to the level this room normally uses."* |
| An accepted preference was applied | *"You accepted this in March, so I applied it. You can pause or remove it."* |
| A transfer was suppressed | *"I did not move the music into the Primary Bedroom, because the room is in Nighttime mode."* |
| A preference could not be read | *"I could not read your preference for this, so I did not guess."* |
| A dependency is missing | *"I can't do that — no calendar is connected."* |
| A provider acted on its own | *"The adaptive lighting integration changed this. I don't hold its reasoning."* |
| Nothing supports a cause | *"It changed at 7:42, and I can't tell you what caused it."* |

## The rules behind those sentences

| Rule | Basis |
|---|---|
| Every transfer, suppression, resume offer, and refusal records intent, eligibility outcome, blocking reason, and the responsibility that supplied it | Continuity contract |
| **A suppressed transfer must be explainable as a deliberate outcome, not as a failure** | Continuity contract |
| Each block is a **reason**, and each reason must reach the Decision Trace | Continuity model |
| A Decision Trace references the **exact version** of the preference or session it used | **P30**, **DL-27** |
| **The unknown answer is a correct answer** | [why-did-this-happen.md](why-did-this-happen.md) Scenario 21 |
| *Converting temporal proximity into asserted causation* is prohibited | [why-did-this-happen.md](why-did-this-happen.md) Scenario 21 |
| Whether this listener may receive this answer is **Operational Trust's** | **DL-34**; visibility is **OD-30**; retrieval is **DL-69** (resolved **OD-62**) |

---

## What this document deliberately does not do

- **It creates no responsibility, model, object, store, threshold, or history owner.**
- **It does not revive Household Memory, Person Continuity, Affinity, Experience Restoration, or
  Historical Intelligence.** Those documents are **Historical — superseded**, their canonical
  replacement is [../models/continuity.md](../models/continuity.md), and their former ownership
  boundaries are **not** reactivated.
- **It does not introduce a Journey, checkpoint, progress-marker, tradition, plant-care-knowledge, or
  travel-time model.**
- **It does not move Stewardship history, Truth Fact history, or Concierge decision history into
  Continuity.**
- **It asserts no implemented HTBW Core capability.**

---

# Use Case 16 — Room-Aware Music Continuity, Guest/Default Fallback, and Music Assistant Resolution

## Human outcome

Tom listens to jazz in the Den, walks to the Kitchen, and says *"Play what I was listening to."* The
Kitchen plays Tom's jazz, at the Kitchen's own configured volume, through the Kitchen's configured
media capability. Later, David plays different music in the Den. When Tom returns to the Den and says
*"Resume the music,"* the Den's own current session resumes — not Tom's jazz from memory, and not
David's session attributed to Tom. A guest with no configured preference, asking for music in the
Kitchen, gets the household's configured default or the designated Guest fallback Person Extension's
preference — never a fabricated "Kitchen taste."

## Preconditions

| Precondition | Owner | Status |
|---|---|---|
| Target Room or Merged Room is resolved (current Interaction Space, or an explicit cross-room target) | Room Configuration / Contextual Vocabulary | **A** — accepted disposition, [room-vocabulary.md](room-vocabulary.md) |
| A Person-scoped Governed Reference to a resumable listening context exists | Continuity | **A** — the same abstraction as Use Case 4's audiobook position, applied to music |
| The target Room has a configured media capability and Room-scoped audio values | Room Configuration | **A** |
| Music Assistant is configured and available, where the household uses it | Home Assistant / Music Assistant | **A**, where configured — [home-assistant-boundary.md](../architecture/home-assistant-boundary.md), *Music Assistant capability review* |

## Ownership map

| # | Question | Owner | Statement |
|---|---|---|---|
| 1 | Target place | Room Configuration / Contextual Vocabulary (Experience Family 1) | Explicit cross-room naming and the current Interaction Space use the same resolution and the same execution model. The Den supplies interaction-origin context only; it does not supply the Kitchen's player, volume, or Room-scoped state |
| 2 | What Continuity supplies | **Continuity** | Tom's Person-scoped last-genre / last-played Governed Reference, **or** the target Room's Room-scoped last song / current experience — never collapsed into one record |
| 3 | Memory scope | **Person-scoped:** preferred artist, genre, album, playlist; current personal media session. **Room-scoped:** last song and last genre played in the room, music/duck/TTS volume, current room experience | **A** — [continuity.md](../models/continuity.md) Scope rules |
| 4 | Guest/default experience | **Continuity** (the already-accepted **Guest fallback Person Extension**, **DL-71**) or **Room Configuration** (a configured default) | **A** — neither is a third Continuity scope, and neither is a fabricated Person invented to hold a Room's taste |
| 5 | Precedence | Explicit request first; Person-scoped Continuity; Room/session Continuity; guest/default context; otherwise no fallback | Settled now: **an explicit request is never overridden by remembered state of any scope** — Continuity never supplies an instruction. Full ordering among the remembered scopes, and which remembered-value class applies, remains **OD-78** |
| 6 | Music resolution | **Music Assistant**, where configured | **A** — [home-assistant-boundary.md](../architecture/home-assistant-boundary.md) |
| 7 | Execution | The target Room's configured media capability — a native Music Assistant player provider, or a supported Home Assistant Media Player fallback | **A** |
| 8 | Who decides | **Concierge** | Composes applicable state from 2–6 and executes through governed interfaces |
| 9 | Multi-person conflict | **Operational Trust** / **Concierge** | The Den's current session (David's) is a Room-scoped record, distinct from Tom's Person-scoped reference. *"Resume the music"* in the Den resumes the Den's session; *"play what I was listening to"* uses the speaker's own Person-scoped reference. Session merge is **OD-24**; concurrency is **OD-27** |
| 10 | Degradation | [home-assistant-boundary.md](../architecture/home-assistant-boundary.md) / [failure-and-degradation.md](../architecture/failure-and-degradation.md) | If Music Assistant is unavailable: basic player control (pause, stop, resume, volume) continues through the target Room's media capability where supported; a semantic request (search, artist, album, playlist, genre) degrades explicitly and is never silently reassigned to a different provider, a static mapping, or an unrelated favorite |
| 11 | Explainability | **Decision Trace** | Requested intent; which Continuity scope (Person, Room/session, or guest/default) supplied the applied state; the resolved target Room; Music Assistant availability; the player/provider that executed; whether degradation occurred |

## Acceptance scenarios

| # | Given | Then | Must not |
|---|---|---|---|
| 16.1 | Kitchen's "Lights" vocabulary term resolves to several configured fixtures, each with its own resume value | Each fixture restores its own value | Collapse to one generic Room-level brightness |
| 16.2 | A fixture has a resume value and the resident states an explicit level | The explicit level governs | Apply the resume value over an explicit instruction |
| 16.3 | Standing in Den, the resident says *"Play music in the kitchen"* | Kitchen's configured player and Room-scoped volume are used | Use the Den's values merely because the interaction originated there |
| 16.4 | Tom's last genre is Jazz and Tom says *"Play classical music"* | Classical governs | Apply Jazz because it is remembered |
| 16.5 | Tom's Person-scoped reference exists; Tom says *"Play what I was listening to"* in a new Room | The target Room's player and Room-scoped volume execute Tom's Person-scoped reference | Assume the target Room supplies Tom's musical taste |
| 16.6 | David played different music in the Den after Tom left; Tom returns and says *"Resume the music"* | The Den's own current/last Room-scoped session resumes | Resume Tom's Person-scoped reference instead of the Den's session, or attribute David's session to Tom |
| 16.7 | No applicable identified-Person preference exists; a Guest fallback Person Extension or a Room Configuration default is configured | That configured default or Person Extension preference may supply the experience | Fabricate a resident preference, or invent a Person representing the Room's taste |
| 16.8 | Music Assistant is configured and the resident asks for an artist, album, playlist, or genre | Music Assistant resolves it; the target Room's media capability plays it | Recreate catalog/search/resolution behaviour in Concierge |
| 16.9 | Music Assistant is the configured resolver and is unavailable; the resident makes the same semantic request | Governed failure/degradation behaviour follows; basic player control remains available where supported | Silently substitute a Sonos Favorite, a static genre map, or an unrelated provider; claim success |
| 16.10 | The configured player is reachable through a native Music Assistant player provider or a supported Home Assistant Media Player fallback | The configured, supported path is used; the HTBW responsibility boundary is unchanged | Treat the fallback path as a reason to change who resolves music or who executes playback |
| 16.11 | A configured Merged Room owns a shared audio experience | One canonical Merged Room configuration supplies the applicable Room-scoped continuity | Duplicate physical-Room lists as architecture (see the Main Living Area prior art below) |
| 16.12 | The target Room has Room-scoped TTS and duck volume while music plays | The target Room's values are used | Let Person music taste redefine the Room's interaction-volume behaviour |
| 16.13 | A Person is identified but the requested Person-scoped value cannot be read | Accepted precedence and failure/degradation policy apply | Silently invent a preference |
| 16.14 | Music selection used Person continuity, guest/default context, Room/session continuity, or a degradation path | Decision Trace captures enough to explain the choice (field 11 above) | — |

## Production provenance

Production is prior art for the **scope** of remembered state, not for its implementation mechanism.
[production-behavior-inventory.md](../reference-home/production-behavior-preservation/production-behavior-inventory.md)
and the per-row evidence in
[production-automation-inventory.csv](../reference-home/production-behavior-preservation/production-automation-inventory.csv),
[production-script-inventory.csv](../reference-home/production-behavior-preservation/production-script-inventory.csv), and
[production-helper-inventory.csv](../reference-home/production-behavior-preservation/production-helper-inventory.csv)
teach:

| Production prior art | What it corroborates |
|---|---|
| 49 individual `input_number.<light>_learned_brightness` helpers (**BHV-11**, **BHV-12**) | Individual fixtures have different resume values — Room-scoped granularity is per fixture, not one room value |
| Per-room `<room>_speaker_profile` (chat/music/duck) (**BHV-01**, **BHV-07**) | A Room has an appropriate playback volume independent of musical taste |
| `sonos_speak_with_ducking_room`'s duck/chat volume handling (**BHV-01**, **BHV-13**) | Duck and TTS volume describe place-specific interaction behaviour |
| `concierge_intentional_learning_ha_voice` ("remember this") (**BHV-12**) | Explicit preference-retention is a useful, distinct interaction from implicit learning |
| `<room>_speaker_profile_last_media` structured audit line (**BHV-09**) | A resumable listening context needs more than a title — title, artist, album, source, type, id |
| The Sonos-Favorites/static-genre-map split from Music-Assistant-backed playback (**BHV-09**, **BHV-10**) | HTBW needs one semantic music-resolution boundary, not a provider-specific split |
| The hardcoded "Main Living Area" room list (**BHV-07**) | Canonical Merged Room continuity is needed in place of duplicated physical-Room lists |

Production has **no person-scoped remembered media, volume, or brightness concept at all** — every
helper and audit trail found is Room- or house-scoped. This is evidence that HTBW's Person-scoped
preferences (preferred artist, genre, album, playlist) are a genuine improvement HTBW must capture,
not something to preserve a production mechanism for.

## Implementation status and unresolved decisions

**F** — no HTBW Core implementation exists. Governed now: scope separation (Person/Room/Fixture
granularity/guest-default), explicit-request precedence, the Music Assistant resolution boundary, and
graceful degradation without semantic degradation. Deferred to existing open decisions: **OD-78**
(remembered-value classes and restoration semantics — the primary owner of the detailed precedence and
provenance questions above), **OD-24** (session merge), **OD-25** (resume eligibility window), **OD-26**
(history retention scope), **OD-27** (concurrency), **OD-28** (learned-preference promotion; evidence
eligibility **OD-65**, resolved — **DL-112**). None of these is resolved, reopened, or duplicated by this Use Case.

---

## Related documents

- [../models/continuity.md](../models/continuity.md)
- [../models/experience-and-session.md](../models/experience-and-session.md)
- [../contracts/continuity-contract.md](../contracts/continuity-contract.md)
- [../architecture/behavioral-governance.md](../architecture/behavioral-governance.md)
- [../models/temporal-record.md](../models/temporal-record.md)
- [follow-me-media.md](follow-me-media.md)
- [multi-person-conflict.md](multi-person-conflict.md)
- [nighttime-suppression.md](nighttime-suppression.md)
- [why-did-this-happen.md](why-did-this-happen.md)
- [stewardship-use-cases.md](stewardship-use-cases.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
