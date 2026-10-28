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
- **Communication re-presentation preference (DL-99)** — a strictly opt-in, Person-scoped preference
  for whether an outstanding Communication should be re-presented (a new Delivery Attempt) as the
  person moves between Rooms, optionally refined by Category/Urgency; where enabled, the household
  configures the permitted repetition behaviour during Integration setup — no HTBW-wide default
  repetition count or cooldown exists
- **Preferred delivery and preferred presentation** — how a resident wants to be told, and in what
  form. Ownership was already stated in
  [../scenarios/stewardship-use-cases.md](../scenarios/stewardship-use-cases.md) and
  [communication.md](communication.md); it is named here so the list is complete. **The ordinary
  preference dimensions — verbosity, explanation depth, citation, convenience modality, locale, and
  choice among supported languages — are now enumerated under *Presentation Preference Scope and
  Precedence (DL-100)* below.** Accessibility/accommodation and required-comprehension language are
  **Person-borne requirements, not ordinary preferences** (DL-100); per-capability override is
  explicitly excluded (DL-100). The only prior enumerations, in
  [person-profile-model.md](person-profile-model.md) and
  [../contracts/service-contracts.md](../contracts/service-contracts.md), remain **Historical and
  superseded**, and neither is authority. **Whether a person-scoped preference may name or steer a
  reasoning provider is resolved: it does not.** The explicit Person
  Reasoning-provider assignment, the **Allow General Questions** authorization, and the **Allow Home
  Steward** authorization (**OD-67**, accepted **DL-93**, Issue #132) are canonical for provider assignment and
  capability authorization, made through Person Configuration, never through a Continuity preference;
  Continuity's preferred delivery/presentation preference governs wording and delivery form only, and
  is never a second configuration authority for either capability gate. **The scope at which a
  presentation preference may exist, and what takes precedence when a Room persona and a person
  preference disagree, is resolved as DL-100, closing OD-79** — Room decorative character (persona,
  voice) belongs to Foundation/Room Configuration, never Continuity; see *Presentation Preference
  Scope and Precedence (DL-100)* below
- **Person-borne presentation requirements (DL-100)** — accessibility/accommodation and
  required-comprehension language, held by Continuity as a distinct, non-overridable record class,
  never an ordinary preference. See *Presentation Preference Scope and Precedence (DL-100)* below
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
- **Session concurrency (DL-102)** — governed by endpoint-class contention, not Session/Experience
  class; a second Person's mere co-presence never creates a participant, a competing owner, or a
  concurrency conflict. Full policy: [experience-and-session.md](experience-and-session.md), *Session
  Concurrency Policy (DL-102)*

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

### Communication re-presentation is a preference, not a transfer (DL-99)

An outstanding **Communication** has no location and is never transferred, moved, or duplicated.
Where a person moves and a Communication remains outstanding, Concierge may make a **new Delivery
Attempt** on a newly appropriate surface. The trigger is a Room transition Fact (Truth-owned), reused
unchanged from the Follow-Me eligibility rules above — an unambiguous transition; a missed or
ambiguous one is never retroactively invented. An explicit resident request is **Retrieval**, a
separate existing mechanism, never re-presentation.

| Question | Owner |
|---|---|
| Does the resident want this? | **Continuity** — a sibling preference in the informal Follow-Me family, its own object |
| Is it permitted on the new surface? | **Operational Trust** (**P32**) |
| Is it attempted, and where? | **Concierge** |

**This preference is not coupled to media transfer eligibility.** The Follow-Me eligibility rules
above govern sessions, not Communications.

**The preference is Person-scoped and strictly opt-in** — reaffirming this contract's own rule that a
missing preference is never silently replaced by a platform default; absence of configuration is an
unmet precondition, never a fabricated value. It may optionally be refined by Category (**DL-78**)
and/or Urgency (**DL-77**), inventing no new classification axis. **Owner Policy Response (Issue
#117)**: where enabled, the household configures the permitted repetition behaviour — any repetition
limit and/or cooldown — during Integration setup; **no HTBW-wide default repetition count or cooldown
exists**. Where enabled but no repetition policy is configured, this is never license to re-present on
every qualifying Room transition indefinitely — the Communication remains outstanding under its
existing lifecycle regardless. `Acknowledged`, `Resolved by origin`/`Expired`/`Superseded`, and
`Undeliverable` each stop further re-presentation, directly confirmed for the acknowledged case by
[../scenarios/continuity-use-cases.md](../scenarios/continuity-use-cases.md) Use Case 2 Acceptance
Scenario 2.3. Formally distinct from Delivery Retry (**DL-98**); non-compounding is structural via
Concierge's existing "exactly one governed outcome" rule. Resolved as **DL-99**, closing **OD-48**. See
[communication.md](communication.md).

---

## Presentation Preference Scope and Precedence (DL-100)

**Resolves OD-79 in full.** "Presentation preference" was never one thing. This section is the
canonical classification and precedence rule; [room-configuration.md](room-configuration.md) and
[../contracts/room-configuration-contract.md](../contracts/room-configuration-contract.md) hold Room
decorative character's own ownership statement and reference this rule rather than restating it.

### Continuity still has exactly two scopes

This decision adds **no third scope**. It clarifies that **Room-scoped does not imply one owner for
every Room-scoped value** — the scope is the Room; ownership still depends on the dimension's
architectural class. Room-scoped **remembered experience** (TTS volume, duck volume, current Room
experience, Room-specific resume state) remains Continuity's, unchanged. Room-scoped **decorative
presentation character** (persona, configured TTS voice) belongs to **Foundation / Room
Configuration**, as part of the Room's durable interaction definition — a different kind of thing
than a remembered value, and never moved into Continuity by this decision.

### The complete dimension classification

| Dimension | Class | Scope / owner | Precedence |
|---|---|---|---|
| Accessibility / accommodation need | **Person-borne requirement** | Person-scoped (Continuity holds the record; Operational Trust gates application) | Always applies when Identity is sufficient; no scope may override |
| Required-comprehension language | **Person-borne requirement** | Person-scoped (Continuity holds the record; Operational Trust gates application) | Always applies when Identity is sufficient; no scope may override |
| Required presentation modality (an accessibility need) | **Person-borne requirement** | Person-scoped (Continuity) | Always applies when Identity is sufficient; no scope may override |
| Choice among multiple reliably understood languages | Ordinary preference | Person-scoped (Continuity) | Adapts the Room baseline |
| Locale | Ordinary preference | Person-scoped (Continuity) | Adapts the Room baseline |
| Verbosity | Ordinary preference | Person-scoped (Continuity) | Adapts the Room baseline |
| Explanation depth | Ordinary preference | Person-scoped (Continuity) | Adapts the Room baseline |
| Citation / evidence presentation style | Ordinary preference | Person-scoped (Continuity) | Adapts the Room baseline |
| Modality as mere convenience (not an accessibility need) | Ordinary preference | Person-scoped (Continuity), bounded by Delivery Surface capability (**DL-53**) | Adapts the Room baseline |
| Persona (title / description) | Room decorative character | Room-scoped (Foundation / Room Configuration) | **Baseline** |
| Configured TTS voice | Room decorative character | Room-scoped (Foundation / Room Configuration) | **Baseline** |
| TTS volume, duck volume, current Room experience | Remembered experience state — **unaffected by this decision** | Room-scoped (Continuity) | Composes independently of persona/voice |
| Capability-specific override | **Explicitly excluded from this decision** — no accepted use case or model requires a generic per-capability override engine | — | Not governed here; a future capability may declare its own narrower presentation setting under this same precedence model if a genuine need is shown, without creating a new engine |
| Re-presentation preference | **Already resolved — DL-99** | Person-scoped (Continuity) | Not reopened here |

### Person-borne requirements: a distinct record class, not a new responsibility

An accessibility/accommodation need and a required-comprehension language are **not ordinary
Preferences** — a Preference is "a person-scoped or room-scoped statement of what is wanted"
([glossary.md](glossary.md)); a Person-borne requirement states what is **needed** for the Person to
reliably understand and use the Home, and is never weighed against a Room's decorative character.
**Continuity still holds the record** — the same responsibility that already holds "preferred
delivery and preferred presentation" — but as a distinct, non-overridable class, exactly as
**Person Environmental Requirements** show "requirement" is already an accepted record shape distinct
from an ordinary preference elsewhere in this repository (**DL-61**), without requiring a new
responsibility here: Identity supplies the assertion (**DL-38**, unchanged); Operational Trust gates
*whether* it may currently be applied, through the same **Capability Access Threshold** that already
gates every Person-scoped preference (**DL-36**, **DL-39**, unchanged — not a new threshold model);
Concierge applies and renders it. **No new responsibility, store, Identity model, or Operational
Trust model is created.**

### Precedence, in order

1. **Person-borne requirements** (accessibility/accommodation, required-comprehension language,
   required modality) apply whenever Identity meets the required Capability Access Threshold. **No
   Room decorative character, and no ordinary preference, is ever a candidate to override one.**
2. **Applicable ordinary Person-scoped preferences** (verbosity, explanation depth, citation style,
   locale, language choice among supported languages, convenience modality) apply next, when Identity
   is sufficient, **adapting the compatible aspects of the Room baseline** — composing with it on
   unrelated axes rather than wholesale replacing it.
3. **Room decorative character** (persona, voice) supplies the baseline within whatever compatible
   presentation space remains after 1 and 2.
4. **Plain failure/degradation** applies wherever a required accommodation, required-comprehension
   language, or required modality cannot currently be satisfied — the capability gap is named
   plainly; nothing is silently substituted or approximated (**DL-41**, reaffirmed by the Owner Policy
   Response on Issue #152).

**A configured Room baseline is not a fabricated Person preference.** It is an independently
configured Room Configuration value, not a stand-in invented because a Person preference happened to
be missing; `continuity-contract.md`'s existing rule that a missing preference is never silently
replaced by a platform default is therefore **not violated** by the Room baseline applying on its own
terms — the Room baseline was never a substitute for anything Person-specific in the first place.

### Identity-sufficient and Identity-insufficient behaviour

When a Person is sufficiently resolved for Person-scoped presentation (Capability Access Threshold
met): retrieve and apply Person-borne requirements; retrieve and apply applicable ordinary
preferences; compose both with the compatible Room baseline; record scope, owner, and exact version
in the Decision Trace (**P30**).

When Identity does not meet the required band: **no resident preference or requirement is applied**
— being addressed by name (the lower **Identity Presentation Threshold**) authorises none of this
(**DL-36**, **DL-39**). The configured Room decorative baseline may still apply, **inheriting no
resident preference or history**, extending Use Case 5's existing "neutral presentation" finding into
a concrete Room-context shape: neutral, here, **is** the Room's own unmodified decorative baseline. A
suspected but unattributable accessibility/comprehension need is never invented for an unresolved
Person; the safe failure behaviour above applies instead.

### Multiple people present

**Audience governs regardless of presentation** (**DL-34**, unchanged) — presentation never widens
disclosure, and one present person's preference is never applied to content another present person
may not receive (`continuity-use-cases.md` Use Case 5, Scenario 5.3).

For a single response genuinely and jointly addressed to more than one sufficiently resolved Person:

- **Conflicting Person-borne requirements** (for example, one person requires visual, another can use
  speech) are each independently non-overridable — the response satisfies the **union** of applicable
  requirements where jointly deliverable (for example, rendering both a visual and a spoken form
  together satisfies both), reusing the existing independent-per-recipient evaluation model
  (**DL-71**); where no single joint rendering can satisfy every present requirement, delivery falls
  back to separate, independently evaluated Delivery Attempts per recipient (**DL-54**, **DL-71**),
  never to silently satisfying only one person's requirement.
- **Conflicting ordinary preferences** (for example, one person prefers concise, another prefers
  detailed) are never arbitrarily resolved by selecting one resident over another. **Neither
  individual preference is applied; the Room decorative baseline governs instead** — the same
  already-established neutral fallback used when Identity is insufficient, extended here to the case
  where Identity is sufficient for both but no single preference can govern a jointly addressed
  response.
- **Matching ordinary preferences** across every addressed Person apply normally — there is no
  conflict to resolve.

### Guest and Unknown Person

An **Unknown Person** owns no preference, requirement, or history, and inherits nothing from any
resident (**DL-33**, unchanged). **Guest is a trust/permissions Role, never an identity or preference
class** ([glossary.md](glossary.md)) — a Guest does not inherit a resident's preferences or
requirements merely by being present. The Room's configured decorative baseline may still apply to an
Unknown Person or a Guest, because it carries no resident-specific content and implies no
recognition. A deliberately configured **Known Non-Resident Person** (a real, intentionally enrolled
Guest) may hold their own Person-scoped preferences and requirements exactly like any other
sufficiently resolved Person — this is ordinary Person Extension behaviour (**DL-71**), not a
Guest-specific exception. The **Guest fallback Person Extension** (**DL-71**) remains available,
unchanged, as a deliberate household configuration choice distinct from the Room's own baseline.

### Provider boundaries, reaffirmed

A **Reasoning Provider** owns no presentation preference or requirement; its unavailability degrades
phrasing only, never correctness, and is never silently approximated (**DL-41**, **DL-93**/**OD-67**,
unchanged — not reopened here). The Room's configured **TTS voice** is a presentation/output-rendering
capability, never a Reasoning Provider, and never implies one; where the configured voice or a
required modality is unavailable, the capability is named as unavailable (**DL-41**), never silently
substituted with another decorative choice. Room Mode remains **Foundation/Room Configuration's**
existing governed appropriateness state ([glossary.md](glossary.md), *Mode*); this decision does not
extend Mode into a presentation-precedence mechanism — whether Mode may someday select among
configured decorative profiles is not decided here.

### Trace, retention, and the never-changes-truth invariant

Decision Trace already records the exact version of every Continuity preference consulted (**P30**);
this decision extends the same citation discipline to Person-borne requirements and to the Room
decorative-character version consulted, plus the precedence outcome, any discarded incompatible
dimension, and any capability/provider failure — **no second trace mechanism is created**. Retention
follows **DL-47** unchanged for every record class here: ordinary preferences, Person-borne
requirements, and Room decorative character are each a **Current Projection** that lives while its
object lives, with any change retained as a **Change Record** under that object's own lifecycle — no
new store. **No presentation setting or requirement, of any class, ever alters a Fact, threshold,
authority outcome, disclosure entitlement, conclusion, obligation state, Urgency, Category, or
Identity confidence** — persona, voice, language, locale, verbosity, explanation depth, citation
style, and modality alter rendering only. A translation must preserve semantic meaning; a plain
language/accommodation rendering must preserve every required caveat and material fact.

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
| OD-24 | Session-merging algorithm when two people's sessions meet in one Room. **DL-102 confirms OD-27 is resolved and supplies the concurrency facts this decision consumes (endpoint-class contention, owners/participants, displacement-authorization state) — OD-24 still owns merge mechanics, resulting ownership, preference resolution, and separation in full** |
| OD-25 | Resume eligibility window defaults per experience class |
| OD-26 | Whether experience history is retained per person, per room, or both, and for how long |
| OD-27 | **Closed — DL-102.** Session concurrency is governed by endpoint-class contention, not Session/Experience class; Personal-versus-Room remains meaningful for ownership/privacy only; suppressed-transfer and conflict-reported-not-started are distinct, both already-existing outcomes; participant join requires an explicit Operational-Trust-evaluated act, never mere co-presence; duplicate playback is a semantic `Current Room` guarantee only, never a provider-render guarantee |
| OD-33 | **Closed — DL-43, DL-46, DL-47.** Retention is declared inside every governed record lifecycle; experience-history scope and duration remain **OD-26** |
| OD-48 | **Closed — DL-99.** Re-presentation preference for outstanding Communications — opt-in, Person-scoped, optionally refined by Category/Urgency; no HTBW-wide default repetition count or cooldown; not coupled to Follow-Me media eligibility |
| OD-77 | Ownership of the association between a Person and an external service, account, calendar, mailbox, or media profile |
| OD-78 | Remembered-value classes and restoration semantics — reproduce a prior value, or compute a currently appropriate one |
| OD-79 | **Closed — DL-100.** Presentation preference scope and precedence: Continuity retains exactly two scopes; Room decorative character (persona, voice) belongs to Foundation/Room Configuration; accessibility/accommodation and required-comprehension language are non-overridable Person-borne requirements, not ordinary preferences; precedence is requirement → applicable preference → Room baseline → plain failure |

## Related documents

- [experience-and-session.md](experience-and-session.md)
- [operational-trust.md](operational-trust.md)
- [temporal-record.md](temporal-record.md)
- [../architecture/behavioral-governance.md](../architecture/behavioral-governance.md)
- [../contracts/continuity-contract.md](../contracts/continuity-contract.md)
