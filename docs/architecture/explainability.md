# Human Trust and Explainability

> **Document status: Canonical.**
> Explainability is cross-cutting architecture. It is not a North-Star framework layer.

---

## Human Trust is the outcome

| | Question | Nature |
|---|---|---|
| Operational Trust | What is allowed? | A governed responsibility |
| Human Trust | Can people rely on the environment? | An **outcome** |

Human Trust is produced by behavior that is understandable, consistent, respectful, and reliable.
It is never implemented directly, never configured, and never claimed.

A home that acts correctly but cannot explain itself does not earn Human Trust.

---

## The explainability requirement

**Every material Concierge decision must be explainable.** This includes:

- Actions taken
- Actions intentionally not taken
- Questions asked
- Communications originated, delivered, and **suppressed**
- Delivery attempts and their outcomes, including outcomes that are honestly **unknown**
- Transfers suppressed
- Automation refused
- Conflicts resolved
- Obligations escalated

**Explainability is not optional logging added later. It is an architectural requirement from the
beginning.**

### Explainability constrains how decisions are made, not only how they are recorded

A decision reached by a route that cannot be stated plainly is **not** rescued by a well-formed trace.
Two consequences follow, and both are already binding elsewhere:

| Requirement | Consequence |
|---|---|
| **Prefer an explicit classification over an inferred one** | *"You marked it private"* is verifiable by the resident; *"it looked sensitive"* is not. Operational Trust prefers explicit privacy markings, household-configured classifications, and declared source classifications over content interpretation or sensitivity inference. See [../models/operational-trust.md](../models/operational-trust.md) |
| **Prefer a stated requirement over a derived one** | A configured Required Identity Band can be quoted, versioned, and reviewed. An improvised threshold cannot |

**Predictability and auditability are explainability properties**, not implementation conveniences: the
same item, classified the same way, on every surface, every time — with a source, a version, and a
change record behind it.

---

## Decision Trace requirement

Every decision evaluation must be capable of producing a Decision Trace containing:

- Trigger
- Explicit request, if any
- Room or contextual origin
- Evidence considered
- Identity assertions considered
- Authoritative Truth facts used
- Continuity state used
- Stewardship obligations used
- Operational Trust policies evaluated
- Room modes evaluated
- Existing experiences evaluated
- Conflicts found
- Policy or priority that prevailed
- Decision
- Action or intentional non-action
- Human-readable explanation
- Confidence and uncertainty
- Relevant timestamps or validity periods
- Result
- Failure or fallback, if any

The structure is defined in [../models/decision-trace.md](../models/decision-trace.md).

---

## Questions the platform must be able to answer

- Why did this happen?
- Why did this not happen?
- Which policy took priority?
- What fact caused the decision?
- What would need to change for a different outcome?
- Was this explicitly requested, suggested, or autonomous?
- **What caused this?** — and, where the evidence supports it, *which automation or script did this?*
- **Why didn't you tell me?**

The last question matters as much as the others. A resident must always be able to tell whether the
home acted because it was told to, because it suggested and was approved, or because it was permitted
to act on its own.

### The record boundary

Four questions, four owners. **They are not interchangeable.**

| Question | Answered from | Owner |
|---|---|---|
| What facts were established, and when? | Facts and Fact history | Truth |
| What occurred in the environment? | **Domain Events**, referencing native Home Assistant records where they exist and are retained | The responsibility that observed the occurrence |
| Why did HTBW make, allow, suppress, defer, or refuse a governed decision? | The **Decision Trace** | Concierge |
| What version of a governed record existed at a given time? | **Temporal Records** | The responsibility owning the record |

> **An occurrence is evidence for an explanation. It is not automatically a Decision Trace.**
>
> **Do not convert temporal proximity into asserted causation.** That two things happened in
> sequence is an observation. That one caused the other is a claim, and a claim requires evidence.

**HTBW never produces a Decision Trace for a decision HTBW did not make.** Where a native automation,
an external integration, or a resident caused a change, the honest answer names what is known and
states what is not held.

### Conversation as the interaction path

Home Assistant Conversation and Assist — with custom sentences and custom intents — may be the
**native interaction and presentation path** for explainability requests: *"Why did you do that?"*,
*"Why did you not do that?"*, *"Why did you tell me?"*, *"Why did you not tell me?"*, *"What
happened?"*, *"What changed?"*, *"What caused this?"*, *"Which automation or script did this?"*

> **Conversation owns nothing.** Not facts, not occurrences, not history, not Decision Traces, and
> not authority. It is a way of asking and a way of answering.

| Concern | Authority |
|---|---|
| Facts and Fact history | Truth |
| What occurred | The observing responsibility, through Domain Events |
| Reconstructable historical versions | Temporal Records |
| Governed reasoning | Decision Traces |
| Whether this listener may receive this answer | Operational Trust |
| Assembling and presenting the answer | Concierge |

A reasoning provider may improve wording, summarisation, or presentation. **It must not fabricate
missing facts, causation, attribution, or authority.** Provider strategy is **OD-67**, and
governed conversational retrieval and command resolution is **DL-69** (resolved **OD-62**).

HTBW does **not** state that every explanation is AI-generated, and HTBW does **not** introduce a new
query language. The retrieval scopes above remain the model; Conversation is one surface onto them.

---

## Historical Explainability

**Explainability has a temporal dimension.** A home that can explain only its most recent decision
cannot account for itself. **P27** in [principles.md](principles.md) makes historical explainability
an architectural requirement.

The home must retain enough governed information to reconstruct what it observed, what it believed,
what it knew, what it decided, why it decided so, and why the alternatives were rejected — across
these retrieval scopes:

| Scope | Example question |
|---|---|
| A single decision | "Why did the music not follow me last night?" |
| A time range | "What happened in this home between Friday and Sunday?" |
| An incident retrieval scope | "Show me everything relating to the water leak." |
| A Room or Merged Room | "What changed about the Living Space configuration this year?" |
| An Asset | "What is the care and custody history of this instrument?" |
| A Person | "What does the home hold about me, and why?" |
| A **Communication** | "Why didn't you tell me the garage was open?" |
| A correlation or causation chain | "What else followed from that request?" |
| A **location conclusion** | "Why do you think Tom is in the Den?" · "Why can't you tell me where my phone is?" |

### The location retrieval scope

A location answer must be explainable to the evidence that produced it, and **its refusals and
uncertainties must be as explainable as its conclusions**.

| Question | Answered from |
|---|---|
| Why do you believe that? | The Location Fact's provenance and, for a **Person** subject, the referenced Identity Assertion with its supporting and contradicting evidence families |
| Why are you not sure? | The conflict record — contradicting evidence is **preserved, never averaged away** |
| Why won't you say? | The **disclosure** decision, recorded separately from the access decision (**DL-34**) |
| Why don't you know which room? | The **granularity basis** — where only zone-level evidence exists, the home says so rather than guessing a Room |
| Where was it before? | Truth's Fact history. **A Historical Fact is never presented as current** |

> **Access to movement histories and reconstructions is governed by Operational Trust and must not be
> reachable through generic Room Help or a general-question capability** (**DL-35**, **OD-35**).

### The communication retrieval scope

*"Why didn't you tell me?"* is answered from governed Communication records:

| Question | Records |
|---|---|
| Did you know? | Truth Fact history (**P28**) |
| Did you decide to tell me? | The creation Change Record |
| Did you decide **not** to? | The suppression Change Record **and its Decision Trace** |
| Did you try? | Delivery Attempt Change Records |
| Did it arrive? | Delivered and Presented, or an honest `unknown` |
| Did I acknowledge it? | The acknowledgement Domain Event, with identity attribution |
| Is it still outstanding? | The Current Projection |
| Do you still hold the record? | The record, or its **Tombstone** |

See [../models/communication.md](../models/communication.md).

### Historical Explainability is cross-cutting, not a responsibility

Historical Explainability **assembles** governed historical records held by their canonical owners.
**It owns no historical store, duplicates no responsibility, and creates no new responsibility.**
Truth owns Fact history; Stewardship owns obligation history; Continuity owns preference and session
history; Operational Trust owns policy history; Room Configuration owns configuration history;
Concierge owns decision history, **including communication delivery history**. See
[framework.md](framework.md).

### Explanations must survive change

Under **P30**, a Decision Trace references the **exact versions** of the Facts, assertions, policies,
obligations, preferences, sessions, configuration, and vocabulary it used. An explanation must
therefore remain accurate after the current configuration or policy has changed. An explanation that
silently re-reads today's policy to describe last month's decision is a defect.

### Limitations must remain explainable

Retention is a **floor as well as a ceiling**. Where privacy requires removal or redaction, the
resulting limitation must itself remain explainable. The home says *"I no longer hold that record"*
rather than falling silent or, worse, implying that nothing happened.

A historical reconstruction containing an **unreported gap** is a defect. See
[../models/temporal-record.md](../models/temporal-record.md) and [privacy.md](privacy.md).

---

## Two paired forms

Every explanation exists in two paired forms. Neither is sufficient alone.

| Form | Purpose | Audience |
|---|---|---|
| Machine-readable | Diagnostics, assessment, validation, auditing, regression detection | Tools, maintainers, the assessment workbook |
| Human-readable | Understanding and trust | Residents |

The human-readable form is derived from the machine-readable form. It must never assert something
the trace does not support.

---

## Example

> "Your Jazz session is configured to follow you. It did not move into the Kitchen because music was
> already playing there, and the current policy gives the existing room experience priority."

This single sentence contains:

| Element | Source |
|---|---|
| An active session with Follow-Me intent | Continuity |
| The destination Room | Room Configuration and Truth |
| Music already playing there | Truth |
| Existing-experience priority | Operational Trust policy |
| The intentional non-action | Concierge decision |

---

## Explanation quality rules

1. **Name the fact, not the mechanism.** "Music was already playing" — not "the destination state
   evaluation returned occupied-media".
2. **Name the governing policy in household terms.** Residents must be able to find and change it.
3. **State uncertainty when it existed.** "I was not certain it was you" is a valid explanation.
4. **Explain non-actions with the same care as actions.**
5. **Say what would change the outcome** when the resident asks, and when the trace supports it.
6. **Never fabricate a reason.** If the trace is incomplete, say so.

---

## What is persisted for explanation, and what is never persisted

**Home Assistant retains what happened to the house. HTBW retains what the house made of it.**
Entity and device states, state changes, native events, occupancy and motion, media-player state,
Person and Device Tracker state, natively provided automation activity, and Recorder history are the
platform's, and HTBW **consumes them by governed reference rather than copying them** (**DL-46**).

What HTBW persists is what the platform does not represent at all: **purpose-specific Identity
Assertions and safe evidence summaries, Decision Traces, Operational Trust evaluations, policy
outcomes, attribution, explicit Change Records, capability-dependency outcomes, audience and
disclosure outcomes, governed non-actions, reason codes, historical policy and Fusion Policy
versions, Tombstones, and broken-reference state.**

**A longer retention requirement is never authority to copy native history.** HTBW does not retain
every state transition, Recorder row, automation trace, sensor payload, voice interaction, or
provider response. **Durable explanation after native expiry needs no copy**: the accepted Fact that
Truth recorded — its Statement, confidence at the time, Provenance, and Freshness — carries what was
material to the decision, and a purged native reference resolves to *"no longer retained"*, never
*"never existed."*

### Explainability is a governed record, not a reasoning log

**HTBW must never persist private internal deliberation.** Chain-of-thought, hidden prompts,
unrestricted model reasoning, raw provider deliberation, provider secrets, biometric internals,
voiceprint vectors or embeddings, raw voice recordings, unnecessary conversation transcript, and
unnecessary raw sensor payloads are all outside the record.

**The governed reason for a decision is not the same thing as the private route to it.** A trace
states the request, the Facts consulted, the identity determination as bands and evidence classes,
the policies evaluated, the conflicts and alternatives, and the outcome. **The explanation must
remain truthful after every sensitive detail is redacted** — if it does not, the explanation was
resting on something it should never have retained.

**Where identity was not required, the explanation says so.** It may record that identity supported
attribution or named presentation, and it must **never imply that identity authorised an operation
that required none**. The flattering version of a decision is not permitted to displace the accurate
one.

### Explainability Evidence Record (accepted as DL-73; OD-63 closed)

> **Status: accepted architecture.** OD-63 is closed as **DL-73**. The Source, Execution, Outcome, and
> Explanation stages below are confirmed against real Production evidence (the Primary Bedroom Good
> Morning voice incident, the Pantry Assist Debug retained pipeline example, and the Tom's Office
> overhead light investigation), and **Decision Authority** — the concept this hypothesis originally
> lacked — is accepted alongside them. **Person/Actor** as a stage name and the "Triggering
> Occurrence" stage are reconciled, not separately adopted: Actor is Identity's existing
> assertion-purpose model, and the triggering occurrence is folded into **Source** rather than kept as
> a seventh position, because **Trigger**/**Domain Event** already name that concept. The canonical
> chain is **Actor → Source → Decision Authority → Execution → Outcome → Explanation**.

The October 2026 Voice Explainability investigation first named this as **Voice Interaction
Evidence**. Working the same reasoning against a non-voice case (a wall switch, a kiosk selection, an
occupancy sensor) showed voice is **one evidence source among several, not the governing shape**.
**Voice Interaction Evidence is retained below as the voice-specific worked case of the broader
hypothesis, not discarded.**

#### The hypothesis

A resident-facing explanation for *"why did this happen"* draws on evidence that, across every source
type, separates into the same six questions, in this order:

```text
Person / Actor  →  Source  →  Triggering Occurrence  →  Execution  →  Outcome  →  Explanation
```

**This is not a new runtime sequence, a new store, or a new responsibility.** Read stage by stage,
every position in this chain is already owned, and already accepted, by existing architecture — the
hypothesis's only contribution is naming the chain and showing that the same six positions recur
across every source type, not only voice:

| Hypothesis stage | What it asks | Already owned by |
|---|---|---|
| **Person / Actor** | Who is most likely associated with this, if anyone? | **DL-38**'s Identity Fusion Function, evaluated for the applicable **Assertion Purpose** ([person-and-identity.md](../models/person-and-identity.md)) — **Speaker Attribution**, **Room Presence**, **Household Presence**, **Interaction Initiator**, **Authenticated Session Identity**, or **Endpoint Context**. **Unknown Person** (**DL-33**) and **No Person / autonomous** are both already first-class outcomes; no new actor state is introduced |
| **Source** | Where did this originate — physically or logically — independently of who, if anyone, is attributed to it? | The existing **Behaviour Source** enumeration ([temporal-record.md](../models/temporal-record.md), [glossary.md](../models/glossary.md)) — direct resident interaction, a native automation, script, or scene, manual physical interaction, an HTBW decision or adaptive policy, an external integration, an external autonomous policy engine, a reasoning-provider recommendation, or **unknown/unattributed** |
| **Triggering Occurrence** | What was the one initiating occurrence? | The existing **Trigger** ([glossary.md](../models/glossary.md): *"the event that begins a decision evaluation"*) and the existing **Domain Event** ([temporal-record.md](../models/temporal-record.md)) — **not** a new construct (see naming note below) |
| **Execution** | What did Home Assistant, or another authorized environment, actually do? | Home Assistant **Context**, **Parent Context**, **User Context** ([home-assistant-boundary.md](home-assistant-boundary.md), *What Home Assistant context can and cannot establish*, **OD-38**), native automation/script/scene execution evidence (**OD-64**) |
| **Outcome** | What was observed to actually result, as distinct from what was requested? | Recorder state history and the Domain Event's own resulting-state evidence; for a Communication, the existing **Presentation Outcome** (**DL-54**: Presented / Failed / Unknown / Attestation Unavailable) |
| **Explanation** | How is this assembled into a truthful, resident-understandable account? | The existing record boundary above (*Facts* → Truth, *what occurred* → Domain Event, *why HTBW decided* → Decision Trace, *record version* → Temporal Record), assembled and presented by **Concierge**, which **owns none of the underlying evidence it assembles** |

**A naming collision is recorded, not resolved by assertion.** The hypothesis's "initiating
occurrence" stage cannot be named **Activity**: [glossary.md](../models/glossary.md) already states
*"Activity is also the name of the Home Assistant integration... There is no HTBW Activity model, no
Activity responsibility, and no Activity store,"* and
[temporal-record.md](../models/temporal-record.md) independently states that behaviour attribution
*"does not require, and must not become, a separate Activity model, Activity responsibility, or
Activity store."* **This hypothesis reuses Trigger and Domain Event for that stage precisely because
the term is already spoken for**, not as a stylistic preference.

**Where no HTBW decision was made, there is no Decision Trace, and that is correct, not a gap.**
[decision-trace.md](../models/decision-trace.md) is explicit: *"A Decision Trace exists only where
HTBW decided... What occurred is recorded as a Domain Event with behaviour attribution instead."* The
October 6 incident (below) produced no Decision Trace for exactly this reason — no HTBW decision
occurred — and the hypothesis's Execution/Outcome/Explanation stages resolve to Domain Event evidence,
not to a fabricated trace.

#### Source, Endpoint, and Person are already kept apart — this hypothesis does not re-decide it

[person-and-identity.md](../models/person-and-identity.md)'s **Endpoint Context** purpose already
states plainly that a managed endpoint "identifies a **thing**, not a person," and
[home-assistant-boundary.md](home-assistant-boundary.md)'s native-evidence review (**L8**) already
verifies that Home Assistant has **no native kiosk concept** at all — *"HTBW must not treat a kiosk
account as anything other than a Home Assistant user account."* **A kiosk, a wall switch, a voice
satellite, and an occupancy sensor are each a Source/Endpoint. None of them is automatically a Person.**
A kiosk, satellite, or device may carry a **proxy association** to a Person — evidence that
contributes to the Fusion Function at its own configured reliability — but a proxy association is
**evidence, never identity**, exactly as **DL-32** already requires of every evidence source. This
hypothesis adds no exception.

**The Identity Triangulation worked example below illustrates DL-38 already applied to Household and
Room Presence evidence. It is not a new fusion mechanism and must not be read as one.**

> **Worked example (illustrative only — not a claim about any specific event):** a wall switch is
> pressed in the Primary Bedroom. The switch press is the **Source**; the Primary Bedroom is **Room
> Context**; a Person's wearable and phone observed in that Room, with the Room occupied and no
> competing candidate, are **Household/Room Presence evidence** fused under **DL-38**'s existing rules
> into a candidate Identity Assertion with its own confidence band. **This demonstrates the existing
> Fusion Function applied to a non-voice Source. It is never read as proof that a named person
> physically pressed the switch** — the assertion remains a purpose-specific, confidence-bearing
> candidate, exactly as DL-38 already requires, capable of returning **Unknown** or **No Person**.

#### Resolved residual (OD-63 closed as DL-73)

**Evidence-per-source is resolved via a generative test, not an enumerated table.** The Known/
Probable/Unknown Source tier applies uniformly to any Behaviour Source by the same same-context-
evidence shape already demonstrated for Voice, Dashboard/App, Occupancy Automation, Native Automation,
Script, Schedule, and Probable Physical Wall Switch/Dimmer; a native script, a scene activation, or an
external non-autonomous integration is classified by the identical test, not by a bespoke per-item
statement. **Whether a single source-neutral evidence shape is required, or whether each Behaviour
Source category states its own native evidence fields, is immaterial under the generative test** —
both produce the same Known/Probable/Unknown outcome from the same underlying evidence.

**Alternative-explanation handling is resolved**: HTBW never presents competing candidate sources as
parallel outputs; it returns the single best-supportable attribution, or Unknown Source where none
reaches threshold, and a recurring Unknown Source is itself governance evidence.

**Revision-additivity is resolved by inheritance**, not by a new mechanism: the existing Change Record
immutability discipline (**DL-26**, **DL-27**) and **DL-35**'s identical rule for the Unknown Actor
Reference already require that a later observation never rewrites an earlier attribution record.

**No open residual remains under OD-63.** OD-38, OD-64, and OD-72 remain independently open on their
own questions, narrowed but not decided by this closure.

#### An existing tension this hypothesis must not silently resolve

**DL-46** already states plainly that *"HTBW does not retain every state transition, Recorder row,
automation trace, sensor payload, **voice interaction**, or provider response."* Any evidence capture
this hypothesis eventually justifies is only defensible, if accepted at all, as the same kind of thing
**DL-46** already permits — "what the platform does not naturally represent" — captured
**contemporaneously, at the moment evidence is material to an HTBW decision or to a Domain Event's
behaviour attribution**, never as a retroactive bulk copy of Assist Debug or Recorder history for its
own sake. **This section names that tension. It does not resolve it.**

#### Voice Interaction Evidence (retained as the voice-specific worked case)

The October 2026 investigation verified, at the Home Assistant source level and against a real
Production incident, that Assist Debug run data — STT output, intent input and output, successful and
failed entities, TTS response, and precise stage timing — is **in-memory only, capped at the ten most
recent runs per pipeline, and destroyed on every restart** (see
[home-assistant-boundary.md](home-assistant-boundary.md), *Assist Debug run storage, retention, and
cross-system correlation*). Recorder retains execution evidence (`context_id`, service calls, entity
changes, automation chains) indefinitely by comparison, but **the two use separate identity systems
with no native, durable correlation** between a Recorder `context_id` and a `pipeline_run_id` or
`conversation_id`. This remains the clearest and most fully source-verified single-source case; it is
not generalized beyond voice by this paragraph, only by the hypothesis above.

##### October 6 reference case (principal example, not universal proof)

The Primary Bedroom "Good Morning" incident, reconstructed entirely from native evidence:

| Hypothesis stage | What the evidence actually supports |
|---|---|
| Person / Actor | **Unknown from runtime evidence.** Every examined `context.user_id` was `None`. **Household-reported actor: David** — recorded as a household report, never as a runtime-established identity |
| Source | Voice — the Primary Bedroom voice satellite |
| Endpoint | Primary Bedroom Voice PE (the satellite device) |
| Triggering Occurrence | A voice interaction, timing-correlated to the satellite's `listening → processing → responding → idle` sequence |
| Execution | A single root Home Assistant Context (no parent) issuing `homeassistant.turn_on`/`light.turn_on` for five Primary Bedroom-area lights, landing inside the `processing`→`responding` window |
| Outcome | Five lights observed **on**; the governed Good Morning automation **did not trigger**; the governed Good Morning script **did not execute**; no automation or script caused the light change |
| Explanation | No Decision Trace exists, correctly, because HTBW made no decision. The exact recognized text and selected intent were **not retained** — Assist Debug held at most the ten most recent runs for that pipeline, in process memory, and did not survive to the point of this investigation |

**This is not retroactively claimed as the exact STT text or exact intent — that evidence no longer
exists and is not reconstructed.**

##### Pantry reference case (known-good shape, not generalized)

A retained Assist Debug run for a Pantry voice interaction demonstrates what a **currently retained**
run looks like: Source Voice, Endpoint the Pantry voice satellite, recognized text *"Close kitchen
shade,"* processed locally, successful target Kitchen Shade, response *"Closing,"* with Pipeline ID,
Pipeline Run ID, Conversation ID, and Satellite ID all present, and full STT, intent, targeting, and
TTS stages available. **This demonstrates only what Home Assistant generates while a run remains
retained — it is not evidence that any other interaction, including the October 6 incident, was ever
in the same state.**



An explanation must not disclose information the listener is not permitted to receive.

- A guest asking why a light did not turn on must not learn a resident's calendar contents.
- An explanation may state that a policy prevented an action without naming a protected fact.
- Decision Trace visibility and retention are Operational Trust policy decisions.

See [privacy.md](privacy.md).

---

## Where explainability is produced

| Responsibility | Contribution to the trace |
|---|---|
| Foundation / Room Configuration | Resolved Room Context, resolved vocabulary target set, participation and exposure state |
| Identity | Candidate person, confidence, contributing evidence, reason code |
| Truth | Facts used, provenance, confidence, freshness, validity |
| Continuity | Preferences, active sessions, transfer or resume intent |
| Stewardship | Obligations considered and their state |
| Operational Trust | Policies evaluated, thresholds applied, ceiling in force, prevailing priority |
| Concierge | Conflicts found, decision, action or intentional non-action, both explanation forms |
| Concierge | Communications originated, suppressed with reason, attempted, delivered, presented or `unknown`, acknowledged, expired, and superseded |

**Concierge owns the trace. Concierge does not own the contents contributed by other
responsibilities.**

---

## Related documents

- [../models/decision-trace.md](../models/decision-trace.md)
- [../models/temporal-record.md](../models/temporal-record.md)
- [../models/communication.md](../models/communication.md)
- [behavioral-governance.md](behavioral-governance.md)
- [failure-and-degradation.md](failure-and-degradation.md)
- [adr-historical-explainability-and-historical-truth.md](adr-historical-explainability-and-historical-truth.md)
- [adr-resident-communication-and-delivery-separation.md](adr-resident-communication-and-delivery-separation.md)
- [../scenarios/why-did-this-happen.md](../scenarios/why-did-this-happen.md)
