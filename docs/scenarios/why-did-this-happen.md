# Scenario: Why Did This Happen?

> **Document status: Canonical scenario.**
> Terminology: [../models/glossary.md](../models/glossary.md).
> Index: [README.md](README.md).

---

## The six questions the home must always be able to answer

1. Why did this happen?
2. Why did this not happen?
3. What did you believe was true?
4. Who did you think I was?
5. Which policy or fact took priority?
6. What would have changed the outcome?

**A decision that cannot be explained is a defect.**

**Each of the six questions also has a past tense.** *Why did that happen — last month?* The home must
be able to answer for a single decision, a time range, an incident retrieval scope, a Room, a Merged
Room, an Asset, and a Person. See **P27** in
[../architecture/principles.md](../architecture/principles.md).

**A seventh question follows from the six.** *Why didn't you tell me?* A home that decided to stay
quiet must be able to say so. See **P31**, **P32**, and Scenario 15.

---

## Scenario 1 — Why did the jazz start?

### What the household experiences

Tom walks into the Den and jazz begins playing. He asks, "Why did you do that?"

> "I started jazz on the Den speakers because I recognised you, the Den was free, and you have jazz as
> your preferred genre. Quiet hours weren't active, so I didn't need to ask."

### Source attribution

| Element of the explanation | Supplied by |
|---|---|
| "I recognised you" | Identity — candidate Tom, identity_confidence_band: High |
| "the Den" | Room Configuration — Room Context resolved from the assistant's assigned Room |
| "the Den speakers" | Contextual Vocabulary — configured target set |
| "the Den was free" | Truth — no active session, Truth Confidence Band: High |
| "your preferred genre" | Continuity — person-scoped preference |
| "quiet hours weren't active" | Truth + Operational Trust — the fact, and the policy that consumed it |
| "I didn't need to ask" | Operational Trust — effective autonomy level was Autonomous |
| The sentence itself | Concierge |

**No responsibility authored a field it does not own.** Concierge composed the trace; it did not invent
its contents.

---

## Scenario 2 — Why did the music not follow me?

> "I did not move the music into the Primary Bedroom because the room is in Nighttime mode, and
> Nighttime mode does not allow music to arrive on its own. I also did not ask, because Nighttime mode
> does not allow me to interrupt."

**A non-action trace is as important as an action trace.** See
[nighttime-suppression.md](nighttime-suppression.md).

The explanation names the **deciding factor** — Nighttime mode — not every input that was evaluated. It
also explains the *second* non-action: why it did not even ask.

---

## Scenario 3 — Why did nothing respond to "the speakers"?

Tom says "play music on the speakers" in the Living Space, and the Sonos Beam stays silent.

> "The Beam is deliberately not part of *Speakers* in this room — it's set up for TV audio. Would you
> like me to use it anyway?"

**A deliberate exclusion must be explainable as deliberate**, not as a malfunction. The explanation
distinguishes *the thing does not exist*, *the thing is broken*, and *the thing is intentionally not
included* — three very different household situations.

---

## Scenario 4 — What did you believe was true?

Tom asks why the lights did not come on when he entered the Den.

> "I wasn't sure the Den was occupied — one of the two sensors I use in there isn't reporting, so I only
> had partial coverage, and I don't turn lights on for you unless I'm reasonably confident."

| Element | Supplied by |
|---|---|
| "wasn't sure" | Truth — reduced confidence |
| "one of the two sensors" | Truth — coverage 1 of 2 |
| "I use in there" | Room Configuration — eligible contributors |
| "reasonably confident" | Operational Trust — the threshold that applied |

**Uncertainty survived the whole pipeline and reached the resident.** The home did not act confidently
to conceal that it was unsure.

---

## Scenario 5 — Who did you think I was?

> "I wasn't certain it was you — your voice was a close match for David's, and I don't play someone's
> personal playlist unless I'm sure."

**"I was not certain it was you" is a valid, complete explanation.** It is better than a confident wrong
answer.

The trace records the candidates, their confidences, the evidence classes that contributed, the reason
code `ambiguous`, and the threshold that applied. It does **not** record or expose vectors, embeddings,
fingerprint payloads, or storage paths.

---

## Scenario 6 — Which policy took priority?

Tom asks why the home asked for confirmation when the Home is set to full autonomy.

> "The Den is set to check with you before changing media, even though the rest of the house is set to
> act on its own. The more restrictive setting wins."

| Element | Supplied by |
|---|---|
| The evaluated policies | Operational Trust |
| Which one was restrictive | Operational Trust |
| The effective autonomy level | Operational Trust |
| The ceiling rule explanation | Operational Trust, spoken by Concierge |

**The most restrictive applicable policy sets the ceiling**, and the home can say which policy that was.

---

## Scenario 7 — What would have changed the outcome?

> "I couldn't unlock the front door because I wasn't confident enough about who was asking. If you use
> the app or confirm on your phone, I can do it."

Explanations for refusals should state **what would change the outcome, where safe to do so**.

The boundary: the home must not coach an unidentified person on how to defeat a safety restriction. For
a safety-critical refusal to an unknown speaker, the correct answer is simply that it cannot be done.

---

## Scenario 8 — Privacy in explanations

Tom asks why the home went quiet at 9 PM.

> "The Primary Bedroom is in Nighttime mode, so I kept the announcements down."

Not: *"David went to bed early because his medication reminder fired at 8:45."*

**A trace shown to one person must not disclose another person's protected content.** Explanations pass
through Operational Trust visibility rules before they are spoken or displayed.

---

## Scenario 9 — A historical explanation survives a later policy change

One month ago, Tom's music did not follow him into the Primary Bedroom because the Nighttime policy
blocked incoming media. Since then, the household has changed the Nighttime policy to allow quiet
incoming media.

Tom asks again today: *"Why didn't the music follow me that night last month?"*

> "That night, the Primary Bedroom was in Nighttime mode, and the Nighttime setting in force at the
> time didn't allow music to arrive on its own. That setting has since been changed — the same request
> tonight would be allowed."

### Why this works

The original Decision Trace referenced the **exact version** of the Nighttime policy applied at the
time (**P30**). It did **not** copy the full policy payload into itself.

| Requirement | Demonstrated |
|---|---|
| The explanation remains accurate after the policy changed | The trace resolves the prior policy version, not today's |
| No full payload was copied | Only a Governed Reference plus a minimal explanation projection — the household-language policy name — was retained |
| The change itself is explainable | Operational Trust's policy Change Record supplies *when it changed and who changed it* |

**This is the decisive test of P30.** Had the trace re-read today's policy, the home would have
confidently given a false account of its own past behaviour. Had the trace copied the whole policy,
the home would be storing a complete archive on every decision.

---

## Scenario 10 — A configuration change is independently explainable

The Sonos Beam in the Living Space is changed from **not selected** to **deliberately excluded**.

> "The Beam was moved out of *Speakers* in the Living Space on 3 March by Tom, and marked as
> deliberately excluded because it's set up for TV audio. Before that it simply hadn't been selected."

### What the Change Record supplies

| Element | Value in this scenario |
|---|---|
| Subject | Living Space Room Configuration — *Speakers* target set |
| Change type | Participation state change |
| Prior state | `not_selected` |
| New state | `deliberately_excluded` |
| Effective Time | When the change took effect |
| Recorded Time | When HTBW recorded it |
| Actor | Tom, via the configuration surface |
| Reason | "Set up for TV audio" |
| Version references | Prior and new configuration versions |

### Boundaries demonstrated

- **Future** Room Help answers and music decisions read the **Current Projection**. They do not replay
  history.
- **Past** decisions reference the applicable **prior version**. Scenario 3's explanation is unchanged
  by today's edit.
- The three participation states are **not collapsed**. *"Not selected"* and *"deliberately excluded"*
  remain distinct in the historical record, because they mean different things to the household.

---

## Scenario 11 — The lifecycle of a Historical Fact

A Presence Fact for Tom in the Den is **established** at 19:02 with Truth Confidence Band: High. At
19:40 a contributor drops out and the **confidence changes** to Truth Confidence Band: Moderate. At
20:15 a newer fact **supersedes** it when Tom is observed in the Kitchen. At 20:45 the original fact
**operationally expires**.

> "Between 7 and 8 that evening I believed you were in the Den. I was confident at first, then less so
> when one of the sensors stopped reporting, and at quarter past eight I concluded you'd moved to the
> Kitchen."

### What Truth guarantees here

- Each of the four transitions is **separately reconstructable** as a Change Record.
- The Historical Fact retains the Subject, Statement, **confidence at the time**, Provenance, evidence
  references, Coverage, and Freshness — not the raw sensor stream.
- **None of these historical versions may be used as a current fact.** The 19:02 fact is not evidence
  that Tom is in the Den now, and cannot silently become current again. Re-establishing it requires new
  evidence and a new transition.
- **Truth owns this history.** Continuity, Concierge, and Operational Trust reference it; none keeps
  its own copy.

---

## Scenario 12 — A historical gap is reported, not concealed

Tom asks about an event from eleven months ago. The Decision Trace still exists, but a native Home
Assistant state row it referenced has since been purged by the recorder's retention policy.

> "I have my record of the decision, and I can tell you the motion sensor's reading was part of it —
> but the underlying sensor history from that far back is no longer kept, so I can't show you the
> reading itself."

### What the home must and must not say

| Must | Must not |
|---|---|
| The reference existed | Imply the source event never occurred |
| The source record is **no longer retained** | Say the record **never existed** |
| The historical explanation is **limited** | Present an incomplete reconstruction as complete |
| Name the reason where known — retention policy | Fabricate or interpolate the missing value |

**A reconstruction containing an unreported gap is a defect.** The same rule applies to HTBW's own
records: a purged, deleted, or redacted governed record leaves a **Tombstone**, so that *"the record
was removed"* never becomes indistinguishable from *"nothing happened"*.

---

## Scenario 13 — A Preservation Hold protects an explanation

A household dispute arises about an access decision. A person with authority places the relevant
Decision Trace within a Preservation Hold scope.

### What happens

| Effect | Detail |
|---|---|
| The trace is exempted from normal purge | Operational Trust authorised the hold; Concierge enforces it over its own records |
| **Referenced versions are protected transitively** | The exact Identity Assertion version, policy version, and Room Configuration version the trace cites are protected by **their own owners**, because a trace whose references have been purged can no longer explain anything |
| No payloads are duplicated | The hold protects the referenced records where they live. It does not copy them into the trace |
| **Visibility does not increase** | Preserving the record is not disclosing it. Who may read the trace is unchanged by the hold |
| Prohibited raw data remains unretained | No raw voice sample or biometric internal is preserved, because none was ever stored. A hold cannot resurrect what does not exist |
| The hold is explainable | Who placed it, when, under what authority, and when it will be reviewed |

**A held trace whose required references have been silently purged is a preservation failure.**

---

## Scenario 14 — An Evidence Package for a date range

A person with authority requests everything the home holds relating to the week of the water leak.

The assembled package states, on its face:

- When it was assembled, by whose authority, and over what scope
- Which record classes are included, and which are excluded
- Which fields were redacted, and under what policy
- Which records are missing, and which were purged
- Which records exist but are **withheld by policy**
- Which historical gaps are known

> "This covers 4 to 11 November. Three obligation records are included and two Decision Traces. One
> person's presence detail is withheld under the household privacy policy. Sensor history before
> 6 November is no longer kept. This is what I hold — it isn't everything that happened."

### Boundaries demonstrated

- The package is a **projection**. It creates no alternative historical source of truth and does not
  become authoritative over the records it summarises.
- Assembled again next month it may legitimately differ, because retention and redaction advance.
- **It never claims completeness when gaps exist.**
- **It claims no legal status.** Evidence Package is an HTBW architectural term, not a claim of court
  admissibility, chain-of-custody sufficiency, or regulatory compliance. See
  [../architecture/privacy.md](../architecture/privacy.md).

---

## Scenario 15 — "Why didn't you tell me the garage was open?"

The next morning, a resident asks why the home said nothing about the garage door being open the
previous evening.

This is the decisive joint test of **P27**, **P31**, and **P32**. It cannot be answered from an
action log, because **nothing was done**. It is answered from the governed Communication record.

| Question | Answered from | Answer |
|---|---|---|
| Did you know? | Truth Fact history (**P28**) | The garage-open Fact was established at 22:14 with high confidence |
| Did you decide to tell me? | The creation Change Record | A Communication was created at 22:14, category `condition`, audience `role(adult)` |
| Did you decide **not** to? | The suppression Change Record **and its Decision Trace** | The audible Den announcement was suppressed at 22:15, because an unidentified guest was contextually present |
| Did you try? | Delivery Attempt Change Records | One attempt to a personal surface at 22:15 |
| Did it arrive? | The attempt outcome | `Delivered`. `Presented` is **unknown** — that surface cannot attest presentation |
| Did I acknowledge it? | Acknowledgement Domain Event | None recorded |
| Is it still outstanding? | The Current Projection | Superseded at 06:02, when the door was closed and the originator resolved it |
| Do you still hold the record? | The record, or its Tombstone | The records are retained |

> "I did know. I created a message about it at 10:14 last night, and I decided not to say it aloud in
> the Den because someone I could not identify was there. I sent it to your phone at 10:15 and your
> phone accepted it — but I cannot tell whether you saw it, and you never acknowledged it. This
> morning the door closed, so I withdrew the message."

### Boundaries demonstrated

- **The Communication existed independently of any delivery.** It was created, suppressed on one
  surface, attempted on another, and withdrawn — one object throughout (**P31**).
- **Permission to act was never permission to announce.** The home may have been permitted to close
  the door; it was not permitted to say so aloud in front of a guest (**P32**).
- **Suppression is a first-class recorded outcome**, with its own Decision Trace. Silence is never
  unrecorded.
- **`Presented` is honestly `unknown`** and is never inferred from `Delivered` (**P15**).
- **Unknown does not decay into "not acknowledged."** The home says it cannot tell.
- **The audience was a specification, not a device.** The surface was resolved at delivery time.
- **`Resolved by origin` is not `Acknowledged`.** The resident may never have seen it, and the home
  says so rather than implying the matter was handled.
- Delivery history is Change Records referencing the Communication by version. **Nothing is embedded
  inside the Communication.**
- **No new responsibility is involved.** Truth knew, Operational Trust classified, Stewardship held
  no obligation here, and Concierge decided, delivered, suppressed, and recorded.

---

## Scenario 16 — A resident overrides an automation-selected lamp level

### What the household experiences

An evening automation set the office lamp to 30%. Tom raises it to 70%.

### The expected architectural result

| Element | Outcome |
|---|---|
| The occurrence | A **Domain Event**, owned by the responsibility that observed it |
| Attribution | **Direct resident interaction**, where identity confidence supports it; otherwise recorded room-scoped and unattributed |
| Interpretation | Evidence that the automation's value did not suit the resident. **Evidence only** |
| Behaviour | **Nothing changes automatically.** No preference is written and no policy is created (**P26**) |
| Explainability | "The automation set it to 30%, and you changed it to 70%." Both facts are held; neither is merged into the other |

**A correction is a signal, not an instruction to the architecture.** Eligibility of this evidence is
**OD-65**.

---

## Scenario 17 — A native automation triggers a script that changes several lights

### What the household experiences

The household's own "Evening" automation runs a script, and four lights change.

### The expected architectural result

| Element | Outcome |
|---|---|
| Ownership | **The household owns this behaviour through Home Assistant.** HTBW owns none of it |
| The record | Domain Events referencing the automation, the script, the affected entities, and the platform context identifiers |
| Correlation | The parent context relationship, **where Home Assistant supplies it**, links the automation to the script and to the resulting changes (**OD-38**) |
| Decision Trace | **None.** HTBW made no decision, and **HTBW never fabricates a trace for a decision it did not make** |
| Explainability | "Your Evening automation ran the Evening Lights script, and these four lights changed." |
| Requirement on the household | **None.** The automation is not rewritten, wrapped, or migrated |

---

## Scenario 18 — HTBW applies a learned room lighting preference

### What the household experiences

The office lamp comes to 70% at dusk without anyone asking.

### The expected architectural result

| Element | Outcome |
|---|---|
| Precondition | A suggestion was made, **a person with authority accepted it**, and Operational Trust granted an autonomy ceiling |
| Ownership | The approved preference is **room-scoped and owned by Continuity**. The permission is Operational Trust's |
| The decision | Concierge decides, and produces a **Decision Trace** naming the approved policy version and the evidence relied upon |
| Attribution | **HTBW adaptive policy** |
| Explainability | "You accepted this in March, so I set the office lamp to 70% at dusk. You can pause or remove it." |
| If never accepted | The home **asks** instead. Silent promotion is prohibited (**P26**, **DL-21**) |

---

## Scenario 19 — An external integration changes a light on its own

### What the household experiences

An adaptive lighting integration shifts the office lamp's colour temperature. HTBW did not ask it to.

### The expected architectural result

| Element | Outcome |
|---|---|
| Permission | **The integration is not prohibited.** Established third-party integrations are legitimate participants |
| Classification, if the household declared a delegation boundary for it | **Delegated external adaptive behaviour** (**OD-66**) |
| Classification, if no delegation was declared | **Opaque behaviour with a known actor.** The integration is named; **no claim is made about who decided** |
| Why the distinction matters | **Execution is not decision.** That an integration performed the action does not by itself make it a delegated decision-maker |
| The record | A Domain Event attributing the change to that integration, **where the evidence identifies it** |
| Decision Trace | **None from HTBW** |
| Explainability | "The adaptive lighting integration changed this. **I don't hold its reasoning.**" |
| Prohibited | Claiming HTBW decided it; claiming to know the integration's internal logic; **or leaving the resident with silence** |

**Reduced explainability is disclosed, never concealed and never invented.**

---

## Scenario 20 — A reasoning provider improves the wording of an explanation

### What the household experiences

The answer Tom hears is fluent and natural rather than mechanical.

### The expected architectural result

| Element | Outcome |
|---|---|
| What the provider did | Improved **wording, summarisation, and presentation** |
| What the provider did not do | **Establish a fact, assert a cause, attribute an action, or grant an authority** |
| Grounding | Every claim in the sentence traces to a governed record — a Fact, a Domain Event, a Change Record, or a Decision Trace |
| If a record is missing | The explanation **says so**. The provider must not fill the gap (**P15**) |
| Ownership | Truth still owns the facts, Concierge still owns the reasoning of record, Operational Trust still governs disclosure |
| Replaceability | **The provider is replaceable.** Removing it degrades phrasing, never correctness |

Provider strategy is **OD-67**. **No provider is selected here.**

---

## Scenario 21 — "Why did the office lamp come on?"

### What the household experiences

Tom asks the question aloud. He does not know, and should not need to know, which of the previous five
situations produced the change.

### The expected architectural result

The home answers with **whichever cause the evidence actually supports**:

| If the cause was | The home says |
|---|---|
| A resident | "You changed it, at 7:42." |
| A native automation or script | "Your Evening automation ran the Evening Lights script." |
| An HTBW decision | "I did, because you asked me to, and here is the policy that allowed it." |
| An approved adaptive policy | "You accepted this preference in March, so I applied it." |
| An external integration | "The adaptive lighting integration did. I don't hold its reasoning." |
| **Unknown** | **"It changed at 7:42, and I can't tell you what caused it."** |

| Element | Outcome |
|---|---|
| Surface | Assist and Conversation may carry the question and the answer. **Conversation owns nothing** |
| Authority | Operational Trust decides whether this listener may receive this answer |
| Assembly | Concierge assembles the answer from governed records held by their owners |
| Prohibited | **Converting temporal proximity into asserted causation.** "The automation ran shortly before" is not "the automation caused it" |

**The unknown answer is a correct answer.** Governed retrieval through Conversation is **DL-69**
(resolved **OD-62**).

---

## Scenario 22 — No Connected Storage is configured

The home is fully set up in Home Assistant. No connected storage has been attached.

| Aspect | Behaviour |
|---|---|
| What still works | Everything that needs no external artifact. Rooms, vocabulary, presence, Truth, Operational Trust, explanations, and native history all operate normally |
| Asset documents | The capability is **unavailable**. *"Storing documents needs connected storage, which is not set up yet"* |
| Voice enrollment | Unavailable where it requires an external artifact |
| Extended history | Unavailable. HTBW follows **Home Assistant retention**, and says so |
| Prohibited | Creating an unmanaged local store, writing artifacts into entity attributes or a helper, or presenting any of this as a refusal or a permission problem |

**A home without connected storage is a smaller home, not a broken one.** Nothing is emulated
(**DL-41**, **DL-42**).

---

## Scenario 23 — Connected Storage is healthy, retention set to one year

| Aspect | Behaviour |
|---|---|
| Dependency | Satisfied. Dependent capabilities are **available** |
| History | Native Home Assistant history remains the source while it is available. HTBW **extends** retention to one year; it does not replace or re-record native history |
| Purge | Records older than one year are removed by a **governed recurring purge**. The frequency of that purge is an implementation matter and is not stated as architecture |
| Archive | **None.** There is no tier between "retained" and "removed" |
| After purge | A question about an older event is answered *"that is no longer retained"* — never *"that never happened"* |

---

## Scenario 24 — A resident uploads an asset document

Tom adds the boiler's service certificate.

| Aspect | Behaviour |
|---|---|
| Dependency | Connected Storage. Without it the capability is unavailable and says so |
| Owner | **Foundation** owns the Asset and its documentation anchor. **Stewardship owns the boiler's significance and care obligations, not the document** |
| Anchor | The document references the governed Asset record and, through it, the native Device representation. It is **not copied into Home Assistant** |
| Retention | Retained **while the Asset exists**. It does not expire because it is old |
| Deletion | The Asset is removed, or Tom explicitly removes the document |
| If unreachable later | Reported as **unavailable**. Never reported as *"there is no certificate"* |

---

## Scenario 25 — Voice enrollment succeeds

| Step | Behaviour |
|---|---|
| Consent | Captured first. Without it, enrollment is **ineligible** — an eligibility failure, not a dependency failure |
| Samples | Temporary. Retained only long enough to generate the profile |
| On success | Samples are **removed**. The derived profile is retained while the voice profile remains enabled and consent remains valid |
| Later assertions | Reference **evidence classes and reason codes**. Raw samples never become historical identity evidence, and biometric internals — including storage paths — are never exposed |

---

## Scenario 26 — Voice enrollment fails or is cancelled

| Aspect | Behaviour |
|---|---|
| Samples | **Removed** under bounded cleanup. Abandonment is not a retention strategy |
| Partial artifacts | Not retained "in case they are useful later" |
| Identity | Unchanged. A failed enrollment produces **no assertion, no profile, and no evidence** |
| Explanation | *"Enrollment did not complete, and the recordings were not kept"* |

---

## Scenario 27 — A resident asks for an email to be sent, and no email integration exists

| Aspect | Behaviour |
|---|---|
| Dependency | **Missing.** The capability is unavailable |
| Identity | **Not evaluated.** There is nothing to permit |
| Operational Trust | **Not evaluated** |
| Answer | *"Sending email is not set up in this home"* — the missing dependency is named |
| Decision Trace | Records that the capability was unavailable, which dependency was missing, and that identity and requirement **were not evaluated** |
| Prohibited | *"You are not allowed to do that"*; offering a confirmation that could not help; delivering through some other channel that borrows the name |

---

## Scenario 28 — Email exists, but identity is insufficient

Same request. The integration is configured and healthy.

| Aspect | Behaviour |
|---|---|
| Dependency | **Satisfied** |
| Identity | Evaluated. `known`, **Low** |
| Requirement | **Very High** |
| Outcome | **Identity insufficient** — not a missing capability |
| Answer | *"I am not confident enough that it is you"*, with a confirmation offered where policy permits |

Scenarios 27 and 28 produce the same *"no email was sent"* and **must never share an explanation**.

---

## Scenario 29 — A reasoning provider is unavailable

| Aspect | Behaviour |
|---|---|
| Not configured | Capability **unavailable**, named as such |
| Configured but invalid | Unavailable, reported as a **configuration defect** rather than an absence |
| Configured but temporarily unreachable | Unavailable, reported as a **transient condition** where that is known |
| Explanations | Continue. A provider **improves wording; it never owns the explanation** (Scenario 20), so the governed answer is still given, unpolished |
| Prohibited | A local approximation presented under the same name; a silent reduction in scope; rendering the absence as a refusal |

Which classes of provider are permissible remains **OD-67**.

---

## Scenario 30 — Connected Storage becomes unavailable after artifacts exist

| Rule | Behaviour |
|---|---|
| Creation | **Suspended.** New artifacts are not created, and retention is not extended |
| Persistence claims | **Never made.** A write that did not happen is never reported as saved |
| Relocation | **Prohibited.** No recreation elsewhere, no unmanaged local fallback |
| Existing metadata | **Preserved.** Governed references are not deleted because storage is absent |
| Resolution | An affected document resolves to **unavailable**, never to *"never existed"* |
| Surfacing | Reported through the accepted degradation and Repairs surfaces |
| Recovery | Temporary unavailability and **permanent replacement** are different conditions. Reconciliation mechanics are not settled here |

---

## Scenario 31 — An Evidence Package is generated but not saved

| Aspect | Behaviour |
|---|---|
| Nature | A **projection**, assembled on demand from governed records |
| Storage | **None.** Generating it creates no artifact and no store |
| Repeat request | Assembled again from the same governed records |
| Prohibited | Caching it into a persistent evidence store because assembly was expensive |

---

## Scenario 32 — An Evidence Package is explicitly saved

| Aspect | Behaviour |
|---|---|
| Trigger | A resident or deployment **deliberately** saves or exports the package |
| Consequence | The saved copy **is an artifact** and requires its own lifecycle declaration — owner, storage class, retention, deletion trigger, access restrictions, and Preservation Hold effect |
| Limit | **Retention never makes it legal proof.** Saving changes its lifecycle, not its standing |
| Open | Assembly, transport, integrity, and audience remain **OD-40** |

The same rule applies to a **Historical Reconstruction**: a projection until deliberately saved, and
an artifact with a declared lifecycle afterwards.

---

## Scenario 33 — A Preservation Hold covers history older than the retention window

External History Retention is one year. A hold covers records from eighteen months ago.

| Aspect | Behaviour |
|---|---|
| Purge | **Suspended** for the covered records. The configured period is a ceiling, not an authority |
| Duplication | **Prohibited.** The hold is a marker on the existing records, never a copy into a separate store |
| Artifact class | **None is created.** A hold is not an artifact |
| On release | Release **deletes nothing by itself**. Ordinary retention resumes, and removal then follows the normal lifecycle |
| Open | Release authority and process remain **OD-39**; reconciliation with retention floors remains **OD-36** |

---

## Scenario 34 — The retention period is changed from one year to six months

| Aspect | Behaviour |
|---|---|
| Nature | A **governed change**, recorded and historically explainable |
| Earlier decisions | Remain explainable **under the setting that applied when they were made** (**P27**, **P30**) |
| Held records | **Not deleted.** A Preservation Hold survives the change |
| Retention floors | **Not overridden.** A **P27** floor outranks the configured ceiling |
| Everything else | Removed under the ordinary governed purge, not as a bulk erasure |
| Afterwards | Removed records answer *"no longer retained"*, with the retention change available as the reason |

---

## Scenario 35 — A future capability proposes a new artifact

Someone proposes storing a new class of file.

| Question | Requirement |
|---|---|
| Is it native? | If Home Assistant already represents it, **it is not an artifact** (**P21**, **DL-30**) |
| Declarations | Type, owning responsibility, creating capability, required dependency, storage class, anchor, retention, deletion trigger, consent effect, hold effect, behaviour without storage, behaviour on storage loss, historical requirements, access restrictions, and where applicable integrity and recovery |
| Undecided answers | **Not permitted.** *"We have not decided"* blocks introduction; it is not a permissive default |
| Registry | **None is created.** The declaration lives with the artifact class's architecture |

**An unanswered question is an unmet burden of proof** (**DL-43**).

---

## Scenario 36 — A resident opens an Asset document

Tom wants the boiler's service certificate.

| Step | Behaviour |
|---|---|
| Discovery | The document is **listed through Asset Intelligence**, against the Asset. Tom does not go looking for a folder |
| Authority | **Operational Trust is evaluated** before the document is presented |
| Retrieval | The document is retrieved through its **governed artifact reference** |
| Path | The physical path is **not exposed** as the authoritative interface, and not shown in diagnostics or service responses |
| Operations | Review, download, and print are available where policy permits |

**The storage hierarchy never appears.** The resident interacts with the Asset (**DL-44**).

---

## Scenario 37 — A resident deletes one Asset document

| Aspect | Behaviour |
|---|---|
| Artifact | Removed |
| Reference | Removed or tombstoned under the accepted lifecycle rules |
| Structure | Empty dependent structures may be removed |
| The Asset | **Remains.** Deleting a document is not deleting the thing it describes |

---

## Scenario 38 — A resident deletes an Asset

| Step | Behaviour |
|---|---|
| Enumerate | All dependent documents and references are identified |
| Evaluate | Preservation Holds, retention floors, and consent rules are checked **first** |
| Delete | Eligible documents are removed |
| Structures | Empty Asset structures are removed |
| Held artifacts | **Remain governed and explained.** A hold is not overridden because the parent disappeared |
| Native objects | The backing Device follows **its own** lifecycle; it is not deleted because an artifact folder was cleaned |
| Failure | Reported through Repairs or accepted degradation. Deletion is **not reported complete** while mandatory cleanup is unresolved, unless a pending-cleanup state is accepted |
| Payload | Historical governance records may remain; **they do not retain the document payload without authority** |

---

## Scenario 39 — Voice enrollment succeeds and is cleaned up

| Aspect | Behaviour |
|---|---|
| Voiceprint | Created |
| Temporary samples | **Cleaned up.** A voiceprint is not claimed successfully complete while mandatory sample cleanup is outstanding, unless the accepted model distinguishes *generated* from *cleanup-complete* |
| Identity | Receives a **governed reference**, not a file |
| Resident browsing | **None is exposed.** The voiceprint is an Internal Runtime Artifact |
| Failure | Surfaced. Cleanup that did not happen is not reported as though it did |

---

## Scenario 40 — A voice profile is deleted

| Aspect | Behaviour |
|---|---|
| Artifacts | The voiceprint and remaining derived profile artifacts are removed |
| References | Removed or tombstoned |
| History | **Earlier Identity Assertions remain unchanged.** An assertion made while the profile was valid stays historically true |
| Later explanations | Report that the evidence source no longer exists — never that the past did not happen |
| Failure | **Visible**, through Repairs or accepted degradation |
| Internals | Biometric internals and **storage paths are never exposed**, including in the failure report |

---

## Scenario 41 — A Person is deleted

| Aspect | Behaviour |
|---|---|
| Scope | **Every** Voice Identity profile and artifact governed by that Person is evaluated for cleanup |
| Payloads | Removed unless preservation or retention authority requires otherwise |
| Consent records | Follow their **own** accepted lifecycle |
| Historical governance | Remains **only where authorised** |
| Result | **No orphan profile remains.** A voice profile does not outlive the Person it belongs to |

---

## Scenario 42 — "What happened three months ago?"

| Aspect | Behaviour |
|---|---|
| Mechanism | HTBW **queries** governed Activity History. Tom asks a question; he does not open a file |
| Authority | **Operational Trust governs access** to the answer and to its detail |
| Surface | History files are **never** the interaction surface |
| Content | The response distinguishes **observations from inferences**, and reports gaps rather than filling them |
| If purged | *"That is no longer retained"* — never *"that never happened"* |

---

## Scenario 43 — Connected Storage is unavailable during an Asset deletion

| Rule | Behaviour |
|---|---|
| Claim | **Deletion is not claimed.** *"Removed"* is not said of something that still exists |
| State | A governed **pending-cleanup** state is retained, so later recovery can identify what remains outstanding |
| Reference | **Not silently discarded.** Discarding it would turn a pending obligation into an orphan |
| Relocation | The artifact is **not** recreated elsewhere |
| Surfacing | Reported through **Repairs** or accepted degradation |
| Reconciliation | Runs when storage returns. Timing is implementation, not architecture, and the obligation is owned by **OD-36** |

---

## Scenario 44 — A future Room-scoped artifact and the Room is deleted

**No Room artifact class exists today, and this scenario creates none.** It records the rule that
would apply if an accepted capability introduced one.

| Aspect | Behaviour |
|---|---|
| Governing rule | The artifact's declared **Parent Removal Behavior for the Room** |
| Eligible artifacts | Cleaned up; references removed or tombstoned |
| Shared artifacts | **Preserved.** An artifact governed by another valid object is not deleted because one Room disappeared |
| Merged Rooms | Merged-Room and constituent-Room ownership is **resolved before** deletion |
| Structures | Empty Room-scoped structures are removed when eligible |
| Preservation | Holds and historical requirements remain active throughout |

---

## Scenario 45 — A resident opens My Media

| Aspect | Behaviour |
|---|---|
| Internal artifacts | Voiceprints, temporary samples, and governed history are **not intentionally exposed as general media** |
| File-type filtering | Treated as an **additional visibility boundary**, never the sole authorisation mechanism |
| Authentication | Home Assistant protects media directories by **authentication**, which is not the same as per-person authorisation, and is not claimed to be |
| Unreachability | **Not claimed.** That an unlisted file type cannot be reached by any path is not established by documentation, and is not asserted |
| Governed path | **HTBW remains the access path**, and Operational Trust remains the security boundary |

---

## Scenario 46 — A saved Evidence Package's governing record is deleted

| Aspect | Behaviour |
|---|---|
| Trigger | The package was **deliberately saved**, so it is an artifact with its own declared lifecycle |
| Governing rule | Its declared **Parent Removal Behavior** is evaluated |
| Precedence | Holds and retention rules are honoured **first** |
| Cleanup | Eligible payload is deleted and empty structures are removed |
| Unchanged | Assembly, transport, integrity, and audience remain **OD-40**; nothing here settles them |

---

## Scenario 47 — Extended history records reach the retention boundary

| Aspect | Behaviour |
|---|---|
| Mechanism | A **governed recurring purge** removes eligible records. Cadence is implementation, not architecture |
| Browsing | **Not required and not offered.** No folder is opened to purge anything |
| Held records | **Remain.** A Preservation Hold suspends ordinary purge |
| Object-scoped records | Also subject to parent-object cleanup. **The two mechanisms do not replace each other** |
| Explainability | The outcome is explainable: a removed record answers *"no longer retained"*, with the retention setting as the reason |

---

## Scenario 48 — Den occupancy becomes active and HTBW decides nothing

| Aspect | Behaviour |
|---|---|
| Native record | Home Assistant records the occupancy state change. **That is the record, and it is complete** |
| HTBW duplicate | **None.** HTBW does not copy the state change into a governed store so it can be retained longer |
| Decision Trace | **None.** A trace records an HTBW **decision evaluation**, not an occurrence |
| If HTBW consumed it | A governed **reference** to the native change, plus any Fact Truth accepted from it |
| Later explanation | Assembled from the native reference and the accepted Fact, **not** from a stored copy |
| The rule | *An occurrence is evidence for an explanation. It is not automatically a Decision Trace* |

**A home that traced every occurrence would be a home that traced nothing, because the traces that
mattered would be indistinguishable from the ones that did not.**

---

## Scenario 49 — Tom asks the Den to play Jazz

| Element | What is persisted | Where it lives |
|---|---|---|
| The spoken request and the voice interaction | Referenced | Home Assistant |
| The raw audio | **Nothing** | Never retained |
| Voiceprint vectors or embeddings | **Nothing** | Never retained |
| Identity determination | Assertion purpose, state, **confidence band**, evidence **families**, Fusion Policy version | HTBW Identity Assertion, referenced by the trace |
| Den occupancy | Referenced natively; the **accepted Fact** carries what was material | Home Assistant + Truth |
| Vocabulary resolution of *Speakers* | Recorded in the trace | HTBW |
| Access decision | **Identity was not required for playback** | HTBW Decision Trace |
| Presentation decision | Identity **qualified the home to use Tom's name** | HTBW Decision Trace |
| Playback | Referenced | Home Assistant media-player state |

**The access line and the presentation line are recorded separately and must stay separate.** The
music required no known identity and would have played for anyone who asked. **The trace must not say
"I recognised you, so I played it."** That sentence is warmer, shorter, and false about why the home
acted. Identity earned the home the right to say *Tom* — nothing more.

---

## Scenario 50 — Three months later: "Why did Jazz play in the Den?"

| Aspect | Behaviour |
|---|---|
| Source | The **Decision Trace**, which is governed HTBW history and did not expire with the native events |
| Native references | Those still retained resolve normally |
| Expired native references | Resolve to *"no longer retained"* — **never** *"never existed"* |
| The gap that is not a gap | The **accepted Fact** — *the Den was accepted as occupied, high confidence, from motion and presence* — still carries what was material. **It was never a copy of the sensor row** |
| Identity | Reported as **band and evidence class**, exactly as recorded. No biometric internal was ever stored, so none is missing |
| Access versus presentation | Reported as recorded: playback required no identity; the name did |
| Access control | **Operational Trust governs** who may receive this answer and at what detail |
| Missing detail | Stated plainly. *"I no longer hold that"* is an answer; silence is not |

---

## Scenario 51 — A protected email request is denied

**Five distinct causes exist, and collapsing them produces a wrong explanation.**

| Cause | The honest sentence |
|---|---|
| Missing dependency | *"I cannot reach email at all right now."* The capability is **unavailable** — it did not decide against you |
| Identity below the required band | *"I am not confident enough that it is you."* The band required, the band reached, and the reason code are recorded |
| Trust or policy restriction | *"You are recognised; this is not permitted here."* Identity **succeeded** and the answer is still no |
| Disclosure restriction | *"Not in this room, or not with others present."* The content, not the person, is the constraint |
| Runtime failure | *"Something went wrong."* No governed decision was made at all |

| Aspect | Behaviour |
|---|---|
| Trace | Produced in **every** case. A denial is a governed non-action |
| Recorded | The required band, the reached band, the policy version, the audience considered, and the alternative considered |
| Never recorded | Message content HTBW was not permitted to disclose |
| The failure to avoid | Reporting a **dependency outage as a trust decision**, which teaches the resident to distrust a judgement the home never made |

---

## Scenario 52 — Address by Name threshold moves from Moderate to High

| Aspect | Behaviour |
|---|---|
| Record | An explicit **Change Record** on the governed policy object |
| Contents | Prior value, new value, changed field, **actor attribution**, Effective Time, Recorded Time, Retention Classification |
| Reconstruction | **Never by diffing snapshots.** *"What was the prior value"* must not require payload comparison |
| Earlier traces | Reference the **policy version that applied when they were made** and remain correct |
| Later traces | Reference the new version. **No earlier trace is rewritten** |
| Attribution | Who changed it is part of the record. *Something changed* is not an explanation |

---

## Scenario 53 — Asset document metadata changes

| Aspect | Behaviour |
|---|---|
| Record | A **Change Record** against the Asset's governed record |
| Artifact | The stored file is **unchanged**; metadata and artifact are distinct |
| Reference | The governed artifact reference is stable across the metadata change |
| Retention | The Change Record follows the Asset's lifecycle; the document follows its **DL-43** declaration |
| Not created | No new artifact, no new version copy of the file |

---

## Scenario 54 — A voiceprint is deleted

| Aspect | Behaviour |
|---|---|
| Trigger | Consent withdrawal, profile disablement, or Person deletion (**DL-43**, **DL-45**) |
| Artifact | The voiceprint and any derived profile are removed |
| Earlier Identity Assertions | **Unchanged.** They recorded bands, evidence classes, and reason codes — never biometric internals — so nothing about them depended on the deleted artifact |
| Earlier Decision Traces | Remain explainable. **The deletion removes a capability, not a history** |
| Consent record | The **consent-lifecycle record survives** as a structural floor. Deleting the proof of withdrawal would defeat the withdrawal |
| Future identification | Voice evidence is simply no longer available. The home says so rather than degrading silently |
| Never true | *"That person was never identified."* The past is not rewritten by a present deletion |

---

## Scenario 55 — External History Retention is set to one year

| Aspect | Behaviour |
|---|---|
| Nature | A **governed configuration change**, itself producing a Change Record with actor attribution |
| Effect | It is a **ceiling and the purge boundary** for externally held governed records |
| Native history | **Unaffected.** Recorder retention is Home Assistant's, and this setting does not reach it |
| Structural floors | Survive it — Tombstones, consent-lifecycle records, held records, and the versions needed to keep a held Decision Trace explainable |
| Preservation Holds | Suspend ordinary purge regardless of the window |
| Reducing it later | Applies subject to floors and holds, through the accepted lifecycle rather than as a bulk erasure |
| Earlier decisions | Remain explainable **under the setting that applied when they were made** |

---

## Scenario 56 — A new capability proposes a new governed record

| Aspect | Behaviour |
|---|---|
| Burden | It must **declare its retention** before the record class is accepted (**DL-47**) |
| Not acceptable | *"Undecided."* An unstated retention is not a permissive default |
| Also required | Owning responsibility, deletion trigger, consent effect, Preservation Hold effect, privacy classification, and governing parent |
| Not required | Registration in any registry. **No retention registry, retention service, or central purge owner exists** |
| Not permitted | A generic *"records"* class that inherits someone else's rule by proximity |
| Why | A matrix maintained apart from the classes it governs drifts out of truth. **A declaration inside the lifecycle cannot** |

---

## Scenario 57 — Connected Storage is unavailable during a governed decision

| Aspect | Behaviour |
|---|---|
| The decision | Proceeds if it does not require the external record; the home does not stall for history |
| Durable explainability | **Not claimed if it was not achieved.** The home does not report a record it failed to write |
| Local fallback | **None.** An unmanaged local store is a second Recorder acquired by accident |
| Sensitive inputs | **Not retained as a workaround.** Raw audio does not become acceptable because storage was down |
| Surfacing | Reported through **Repairs** or accepted degradation |
| Reconciliation | Runs when storage returns; the obligation is owned by **OD-36** |
| Honesty rule | *"I acted, and I could not record why durably"* is a worse outcome than success and a far better one than a false claim |

---

## Scenario 58 — A Historical Reconstruction is generated but not saved

| Aspect | Behaviour |
|---|---|
| Nature | A **projection**, assembled on request from records held by their canonical owners |
| Retention | **Nothing.** It retains no record and creates no artifact |
| Ownership | Historical Explainability **owns no store** and duplicates no responsibility |
| Access | Governed by **Operational Trust**, and not reachable through generic Room Help |
| Regeneration | Later regeneration may legitimately differ if underlying records have since been purged, and the difference is explained rather than hidden |

---

## Scenario 59 — A Historical Reconstruction is saved

| Aspect | Behaviour |
|---|---|
| Change of nature | Saving it **materialises an artifact**, and it takes an artifact lifecycle under **DL-43** |
| Required declaration | Owning responsibility, governing parent, retention, deletion trigger, consent effect, hold effect |
| Parent removal | Governed by its declared **Parent Removal Behavior** (**DL-45**) |
| Divergence | The saved copy is a **point-in-time projection** and may diverge from later governed truth. It is labelled as such, never presented as current |
| Not a store | One saved projection does not make Historical Explainability an owner of history |

---

## Scenario 60 — A native event referenced by an old Decision Trace has expired

| Aspect | Behaviour |
|---|---|
| Resolution | **"No longer retained."** Never *"never existed"*, and never silence |
| The trace | **Remains valid.** It recorded a decision, and the decision was made |
| What survives | The accepted Fact — Statement, confidence at the time, Provenance, Freshness — carrying what was material |
| What is not done | HTBW does **not** retroactively copy native rows to prevent this, and did not copy them in advance either |
| Explanation quality | The limitation is itself explained: *"the underlying event has aged out of Home Assistant's history; here is what I accepted from it at the time"* |

---

## Scenario 61 — A policy decision produces no action

| Aspect | Behaviour |
|---|---|
| Trace | **Produced.** A non-action trace is as important as an action trace (**P16**, **DL-15**) |
| Recorded | The policy evaluated and its version, the restriction applied, the alternative considered and why it too was rejected |
| Suppressed Communication | Always traced, including the audience considered and each surface rejected with its reason |
| Silence | **A home that decided to stay quiet and cannot say so is the condition P27 exists to prevent** |
| Not recorded | Any reasoning the home is not permitted to retain. The non-action is explainable without it |

---

## Scenario 62 — "Why did the exhaust fan turn on?" (Source versus Decision Authority)

### What the household experiences

Tom asks why the piano-room exhaust fan turned on. The honest answer has two distinct parts, and the
home does not collapse them into one.

### The expected architectural result

> "The humidity sensor crossed the healthy range for the piano, and Asset Intelligence turned the fan
> on because of it."

| Element | Supplied by |
|---|---|
| Source — *what initiated this* | The humidity sensor's state change (**Known Source** — a same-context-id sibling execution event) |
| Decision Authority — *why the decision was made* | Asset Intelligence's own significance evaluation against the piano's declared environmental limit |
| Execution | A Home Assistant automation calling `fan.turn_on` |

**Source and Decision Authority are never collapsed.** "Humidity sensor triggered fan" is true but
shallower; "Asset Intelligence turned on the fan because humidity exceeded the healthy range for the
piano" is preferred **because the evidence supports it**, per the explainability hierarchy — Decision
Authority, else Source, else the originating integration, else Unknown (**DL-73**). Where the Decision
Authority's own reasoning is not evidenced, the home falls back to naming the Source rather than
inventing a richer explanation it cannot support.

---

## Scenario 63 — A physical wall switch, and what the home does not say

### What the household experiences

Tom asks why the office overhead light turned on. No voice request, no dashboard action, and no
automation_triggered sibling event exists for that exact context.

### The expected architectural result

> "It turned on, consistent with the wall switch — there's no automation, dashboard action, or voice
> request tied to that change."

| Element | Outcome |
|---|---|
| Classification | **Probable Source** — a root-context state change with no competing source evidence, consistent with a documented, per-integration-verified device pattern for this entity-backed device class (**DL-30**, **DL-73**) |
| What the home does not say | It does not say "you turned on the light," because no Identity Assertion supports that, and it does not say "I don't know," because the device pattern does support a specific, named explanation |
| Prohibited | Presenting this alongside other unproven candidates as a list of equally-weighted theories. **HTBW never returns parallel candidate explanations** — it returns this one, best-supportable attribution |

### A variant: no pattern is verified

Where the integration's physical-interaction behaviour has **not** been verified (**DL-30**'s burden of
proof undischarged), the same occurrence is **Unknown Source**, not Probable Source — a documented
pattern is required, never assumed from device type alone.

> "It turned on. I can't tell you what caused it."

**A recurring Unknown Source for the same device is itself governance evidence** — it may indicate a
missing or unverified device pattern, missing integration telemetry, or an uncovered Behaviour Source
category, surfaced for review rather than silently tolerated or quietly upgraded to a guess.

---

## Explanation quality rules

1. Use **household vocabulary**, never entity IDs or internal service names.
2. Name the **deciding factor**, not every evaluated input.
3. State **uncertainty honestly**.
4. **Never fabricate** a rationale after the fact.
5. For refusals, state **what would change the outcome**, where safe.
6. **Respect privacy** — never disclose another person's protected content.

---

## What is always recorded

Whether or not anyone asks, every decision — action, non-action, or suppression — produces a Decision
Trace with all twenty required elements. Fields that do not apply are recorded as `not_applicable`;
fields that could not be obtained are recorded as `unavailable`. **Neither is silently omitted.**

**If the trace cannot be written, that is itself a reportable defect.**

### And what is always recorded about change

Every governed change to a governed record produces a **Change Record** naming what changed, when it
became effective, when it was recorded, who or what changed it, why, and which versions it replaced
and established. **A silently unrecorded governed change is a defect, and silent truncation of history
is prohibited.**

### And what is always recorded about communication

Every Communication records its creation, every suppression with its Decision Trace, every Delivery
Attempt and its outcome, every acknowledgement, expiry, and supersession. Where a surface cannot
attest presentation, the outcome is recorded as **unknown** and never inferred.

**Silent non-delivery is prohibited.** *"Nothing was sent"* and *"we decided not to send"* are
different facts.

---

## Related documents

- [../models/decision-trace.md](../models/decision-trace.md)
- [../models/temporal-record.md](../models/temporal-record.md)
- [../models/communication.md](../models/communication.md)
- [../architecture/explainability.md](../architecture/explainability.md)
- [../architecture/privacy.md](../architecture/privacy.md)
- [../architecture/adr-resident-communication-and-delivery-separation.md](../architecture/adr-resident-communication-and-delivery-separation.md)
- [nighttime-suppression.md](nighttime-suppression.md)
