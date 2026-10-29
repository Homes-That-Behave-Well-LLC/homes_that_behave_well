# Behavioral Governance

> **Document status: Canonical.**
> Behavioral Governance is **cross-cutting architecture and policy documentation. It is not a
> North-Star framework layer.** See [north-star.md](north-star.md).

---

## Purpose

Behavioral Governance is where the household's behavioral rules live, so that:

- they are not hidden inside device automations,
- they are not invented by Concierge at runtime,
- they are configurable by the household rather than hard-coded by the platform,
- and every outcome they produce is explainable.

---

## Division of labour

| Responsibility | Contribution |
|---|---|
| Operational Trust | Permissions, authority, ceilings, thresholds, and the governing priority policy |
| Continuity | Preferences, active sessions, transfer and resume intent |
| Truth | Current authoritative conditions, including Room modes |
| Stewardship | Obligations and their state |
| Concierge | Applies the applicable rules and resolves the current situation |

---

## Ownership rules

1. A behavioral rule belongs to Operational Trust if it states what is **allowed**.
2. A behavioral rule belongs to Continuity if it states what is **wanted or remembered**.
3. A behavioral rule belongs to Stewardship if it states what must be **cared for**.
4. A behavioral rule belongs to Truth if it states what **is**.
5. Concierge holds no rules of its own. It holds the **resolution procedure**.

---

## Scope rules

Rules are declared at a scope and resolved from the most specific applicable scope, subject to the
ceiling rule.

| Scope | Examples |
|---|---|
| Home | Security posture, safety policy, emergency behavior, quiet hours, global autonomy ceiling, global conflict policy, default privacy policy |
| Room | Room mode, existing room experience, room volumes, contextual vocabulary, participating assets, Room Help capabilities |
| Person | Preferred artist/genre/album/playlist, personal Follow-Me preference, communication re-presentation and delivery-surface preferences, identity-evidence associations |
| Asset | Authoritative identity, documentation, service plan, environmental limits, warranty, maintenance history, assigned caretaker, rooms served |
| Relationship | Person is caretaker of asset; device assigned to person; voice assistant participates in Room; sensor contributes to a Room composite; speaker participates in a Room music endpoint; asset serves a Room; person has a role in the Home or Room; resident has authority over a capability |

**Ceiling rule.** A broader autonomy or permission setting is a maximum. A more specific policy may
be more restrictive. A more specific policy must never silently become more permissive than the
governing ceiling.

---

## Explicit, Assisted, Autonomous

| Level | The home may |
|---|---|
| Explicit | Act only after direct human instruction |
| Assisted | Suggest, or ask for confirmation before acting |
| Autonomous | Act without asking when all required facts, permissions, confidence thresholds, and policies are satisfied |

The level applicable to a situation is the **most restrictive** of the applicable Home, Room, Person,
Experience, Asset, and Action policies.

---

## Ask versus Assume

The home asks rather than assumes when any of the following holds:

- The applicable autonomy level is Assisted.
- Identity is unresolved or below the required confidence threshold.
- Truth cannot establish a required fact, or two facts conflict.
- The action is classified as higher risk (security, safety, privacy, irreversible, cost-bearing).
- More than one person is affected and no priority policy resolves the conflict.
- An existing experience would be displaced and no policy grants displacement.
- A vocabulary term maps ambiguously.

The home assumes (acts without asking) only when the applicable level is Autonomous **and** every
required fact, permission, threshold, and policy is satisfied.

**Asking is a decision.** It produces a Decision Trace like any other outcome.

**Asking may also be an alternative to refusing.** Where identity confidence falls below what a
capability requires, Operational Trust may permit a governed **confirmation** instead of an immediate
refusal — and may equally **require** confirmation for a consequential action despite high
confidence. Neither direction changes the requirement itself: a confirmation is bounded, is never a
retroactive increase in confidence, and never authorises disclosure to the current audience. See
[../models/operational-trust.md](../models/operational-trust.md).

---

## Conflict resolution

Concierge owns the resolution of the current behavioral conflict. The governing policies and authority
rules come from Operational Trust; the relevant state comes from Truth, Continuity, and Stewardship.

Conflict classes that must be governable:

| Class | Description |
|---|---|
| Multiple-person space | Two or more people with different active or preferred experiences in one Room |
| Existing-experience priority | An incoming transfer versus an experience already running in the destination Room |
| Person authority | One person's authority to override another |
| Guest behavior | What a guest may see, hear, start, or change |
| Child-safe behavior | Restrictions applied to a person in a child role |
| Room-mode precedence | Nighttime, Privacy, or Quiet-hours modes versus a requested action |
| Session ownership | Who owns a session, and who may modify or end it |
| Session merging | Whether two sessions may combine, and under whose preferences |
| Suppression | When an otherwise valid behavior is intentionally withheld |
| Refusal | When an action must not be performed at all |
| Equal-priority policies | Two applicable policies with the same priority |
| Degraded and uncertain behavior | Behavior when facts, identity, or targets are unresolved |

**The platform does not hard-code one universal answer for all homes.** It defines the model that
lets a household configure the governing policy, and it requires that whichever policy prevails is
recorded and explainable.

---

## Follow-Me, transfer, and resume

Follow-Me is a **policy-governed handoff**, not a motion-triggered movement.

Requirements that must all hold before a transfer is even eligible:

- Follow-Me is enabled for the person or session.
- Identity is resolved with sufficient confidence.
- The room transition is unambiguous: origin and destination are both known and different.
- Manual-stop protection is not active.
- Manual-stop cooldown is not active.
- The destination Room has configured, valid, available playback targets.

Blocks that must be representable and explainable:

- Follow-Me disabled, or a never-transfer preference is set.
- Identity unresolved, ambiguous, or below threshold.
- Room transition ambiguous or missed.
- Origin or destination Room unavailable.
- Destination Room is in a mode that prohibits incoming media.
- An existing experience in the destination Room has priority.
- Another person's session would be displaced without authority.
- Movement occurred **between constituent Rooms of the same Merged Room** — this is not a transfer at
  all. See [../models/room.md](../models/room.md).

Resume is distinct from transfer: transfer moves an active session; resume re-establishes a session
that is no longer active. Both are governed by Continuity intent plus Operational Trust policy, and
both are decided by Concierge.

---

## Priority hierarchy

The household configures priority. The framework requires that a priority policy exist, that it be
explicit, and that it be recorded in every Decision Trace where it applied.

A representative default that a household may adopt or override:

1. Safety
2. Security
3. Explicit human instruction, from a person with authority
4. Room mode restrictions
5. Existing Room experience
6. Stewardship obligation escalation
7. Continuity transfer or resume intent
8. Learned or suggested behavior

**The exact global priority order is not decided by this framework.** It is open decision **OD-04** in
[../governance/decision-ledger.md](../governance/decision-ledger.md).

---

## Learning and adaptation

**P26** states the constitutional rule: *an observed pattern must not silently become an autonomous
policy.* This section documents how that rule is governed. It **creates no responsibility and no new
model.**

| Concern | Owner |
|---|---|
| The observation that a pattern exists | The responsibility that observed it, as a **Domain Event** |
| The preference, once approved | **Continuity** — person-scoped or room-scoped, per [../contracts/continuity-contract.md](../contracts/continuity-contract.md) |
| Whether a learned behaviour may be promoted, and to what autonomy ceiling | **Operational Trust** |
| Whether to act on it now, and the record of why | **Concierge**, through the Decision Trace |
| Who the observation is attributed to | **Identity**, subject to confidence thresholds |

**No responsibility is added.** Learning is a *source of proposals*. It is never a source of truth,
never a source of authority, and never an owner.

### The promotion ladder

| Stage | What exists | What the home may do |
|---|---|---|
| Observation | A Domain Event | Nothing behavioural |
| Pattern | A repeated observation | Nothing behavioural |
| Suggestion | A proposal, attributed and evidenced | **Ask** |
| Approved preference | A Continuity preference, versioned | Apply as a preference |
| Adaptive policy | An approved behaviour with an autonomy ceiling | Act within the ceiling, and record why |

**Where an accepted proposal changes governed configuration rather than a preference, the owning
responsibility records the change.** A proposal to adjust a person's identity-evidence reliability is
accepted into **Identity** configuration, not into a Continuity preference — the ladder is the same,
the owner is not. See [../models/person-and-identity.md](../models/person-and-identity.md).

**A Fusion Policy change is governed by the same ladder.** Reliability mappings, correlation
treatment, freshness rules, contradiction rules, candidate comparison, confidence normalisation, and
band mapping are Identity configuration. An observed-performance or calibration finding is a
**suggestion**, never an applied change; **learning never alters a Fusion Policy silently**; and an
accepted change applies to **new** assertions only — **earlier assertions are never recalculated**
(**DL-38**).

**Every stage transition is a governed change with a Change Record.** Acceptance, rejection,
correction, pause, forgetting, and revocation are all recorded, so that a past adaptive action stays
reconstructable after the preference has changed (**P30**). The lifecycle is **OD-28**.

### Scoping follows the existing rule

The person-scoped and room-scoped split is already decided and is **not re-opened here**. Preferred
artist, genre, album, and playlist are **person-scoped**, so they may follow a person between rooms.
Last song, last genre, music volume, duck volume, TTS volume, and room resume state are
**room-scoped**. Learning must respect that split rather than invent a new one: a lamp level adjusted
in one room is room-scoped evidence; a musical taste is person-scoped evidence.

### Evidence rules

| Rule | Statement |
|---|---|
| Not all observation is evidence | Which observations may contribute, and which are excluded, is **OD-65, resolved as DL-112**. **Eligibility, sufficiency, and acceptance are formally distinct**: eligible evidence may participate in analysis; sufficient evidence justifies a Pattern/Suggestion (a qualitative test — more than one independently corroborating, context-consistent observation; no numeric threshold is fixed); only acceptance creates a preference |
| **A resident adjustment and an automation-generated value are not the same evidence** | Correcting an automation's output is a signal about the resident. The automation's own output is not. **Absence of automation evidence is never evidence of manual action** — it may mean expired evidence, an unsupported surface, another integration, or a genuinely unattributed source (**DL-73**, **DL-111**) |
| Identity bounds attribution | An observation may be attributed to a person only where identity confidence meets the threshold. Below it, the evidence is room-scoped or discarded, never guessed |
| **Competing residents never merge, and the reason is structural, not a policy choice** (**DL-112**) | A person-scoped value never actually conflicts between residents — each Person's own preference is independently stored and read back only when that Person is identified. A room-scoped value is operational history, not a contested preference, so there is nothing to average. Real-time application precedence for two residents simultaneously present with conflicting already-accepted preferences is explicitly out of this scope (a future policy-precedence question, never invented here) |
| **Dismissal is non-acceptance, never automatic negative evidence** (**DL-112**) | A bare dismissal is recorded through the applicable suggestion lifecycle; repeated dismissal may itself become a reportable Pattern about the proposal's own treatment ("this has been repeatedly dismissed"), **never** "the resident dislikes this outcome." Explicit rejection is a distinct, further lifecycle state (**OD-28**) |
| **Evidence carries its context, and a Pattern must stay context-consistent** (**DL-112**) | An observation made under a household Mode remains eligible, carrying that Mode as ordinary provenance; a Pattern may only be built from observations of genuinely the same behaviour — mixing Mode-context and ordinary-context observations into one Pattern would misrepresent repetition. This is a direct consequence of existing Domain Event provenance fidelity, not a new scope or a categorical exclusion rule |
| Feedback is new evidence | A correction adds evidence. **It does not rewrite the history that preceded it** |
| Confidence is stated, not implied | A suggestion carries the strength of its evidence, in terms a resident can understand |
| Staleness is a property | Evidence and approved preferences age. How they expire is **OD-28** |

### Requirements that always hold

1. A suggestion requires acceptance by a person with authority before it becomes a preference.
2. Promotion to an adaptive policy requires an Operational Trust permission and an autonomy ceiling.
3. **An adaptive action produces a Decision Trace like any other decision**, naming the approved
   policy version and the evidence relied upon.
4. A resident may ask *what was learned, and why*, and receive an answer grounded in governed records.
5. A resident may ask *what evidence influenced this*, and receive the referenced evidence.
6. A revoked policy stops applying immediately, and past decisions taken under it remain explainable.

### Prohibited

- Silent promotion of an observation into behaviour.
- Learning that produces an outcome no one can explain.
- Attributing an observation to a person on insufficient identity confidence.
- Treating a learned preference as a Fact. Facts are Truth's, and a preference is not a fact.
- Creating a learning store, a learning history, or a learning responsibility.
- Averaging, voting, or merging competing residents' evidence into one preference (**DL-112**).
- Treating a bare dismissal as negative preference evidence, or silence as acceptance (**DL-112**).
- Building a Pattern from observations that are not genuinely context-consistent (**DL-112**).
- A Person-plus-Room preference scope, invented to retain a compound observation.

---

## Acceptance examples

These scenarios are architectural acceptance examples for this document.

| Scenario | Document |
|---|---|
| Living Space shades resolved from vocabulary | [../scenarios/room-vocabulary.md](../scenarios/room-vocabulary.md) |
| Follow-Me into an empty Room | [../scenarios/follow-me-media.md](../scenarios/follow-me-media.md) |
| Existing audio priority and multi-person conflict | [../scenarios/multi-person-conflict.md](../scenarios/multi-person-conflict.md) |
| Nighttime suppression | [../scenarios/nighttime-suppression.md](../scenarios/nighttime-suppression.md) |
| Garage door obligation after a threshold time | [../scenarios/stewardship-obligations.md](../scenarios/stewardship-obligations.md) |
| "Why didn't my music follow me?" | [../scenarios/why-did-this-happen.md](../scenarios/why-did-this-happen.md) |

---

## Prohibitions

- Do not hide behavioral rules inside device automations.
- Do not let Concierge invent rules at runtime.
- Do not encode a household's preferred priority order as a platform constant.
- Do not treat a suppression as a failure. A suppression is a governed outcome and must be explained.
- Do not require the household to rewrite existing Home Assistant automations, scripts, or scenes.
  HTBW coexists with them; it does not absorb them. See
  [home-assistant-boundary.md](home-assistant-boundary.md).

---

## Related documents

- [../models/operational-trust.md](../models/operational-trust.md)
- [../models/continuity.md](../models/continuity.md)
- [../models/temporal-record.md](../models/temporal-record.md)
- [home-assistant-boundary.md](home-assistant-boundary.md)
- [explainability.md](explainability.md)
- [failure-and-degradation.md](failure-and-degradation.md)
