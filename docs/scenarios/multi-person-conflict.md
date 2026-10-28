# Scenario: Multi-Person Conflict

> **Document status: Canonical scenario.**
> Terminology: [../models/glossary.md](../models/glossary.md).
> Index: [README.md](README.md).

---

## Scenario 1 — Two people, one Den

### What the household experiences

Tom is listening to jazz in the Den. David walks in and says, "Play the news."

The home does not silently replace Tom's music. It asks David: "Tom is listening to jazz in here. Would
you like the news in the Den, or somewhere else?"

### What each responsibility does

| Step | Responsibility | Action |
|---|---|---|
| 1 | Room Configuration | Resolves Room Context → Den |
| 2 | Identity | Asserts candidate David, identity_confidence_band: High |
| 3 | Truth | The Den is occupied by Tom and David; an active session exists |
| 4 | Continuity | Reports the active session: owner Tom, experience class media, started in the Den |
| 5 | Operational Trust | David has no authority to displace Tom's session without confirmation |
| 6 | Concierge | Detects the conflict, and asks rather than acting |

**Concierge resolves conflicts among permitted outcomes. It does not grant itself authority to displace
a session.**

### What the home can say afterwards

> "I asked instead of switching because Tom's jazz was already playing in the Den, and I don't replace
> someone else's music without checking."

---

## Scenario 2 — Ambiguous identity in the Kitchen

### What the household experiences

Someone in the Kitchen says, "Play my playlist." The voice is a close match for both Tom and David.

The home says: "I'm not sure whether that's Tom or David — whose playlist would you like?"

### What each responsibility does

| Step | Responsibility | Action |
|---|---|---|
| 1 | Identity | Reports `ambiguous`: Tom 0.61, David 0.58, from voice only |
| 2 | Truth | Both Tom and David are believed present in the Living Space |
| 3 | Operational Trust | "My playlist" is a **personal** action requiring a resolved identity |
| 4 | Concierge | Asks for disambiguation rather than guessing |

**Identity must not silently select the highest-confidence candidate for a personal or authority-bearing
action.** Tom at 0.61 is not "probably Tom" — it is ambiguous, and ambiguity is a first-class output.

### The failure this prevents

Playing David's playlist for Tom is a small annoyance. The same silent selection applied to unlocking a
door, reading a message, or disarming an alarm is not.

---

## Scenario 3 — Unknown identity, benign action

### What the household experiences

Someone the home does not recognise says, "Turn on the lights" in the Den. The lights come on.

### What each responsibility does

| Step | Responsibility | Action |
|---|---|---|
| 1 | Identity | Reports `unknown` — no candidate can be asserted |
| 2 | Truth | The Den is occupied |
| 3 | Operational Trust | Lighting in an occupied room is a **benign** action class; permitted with unknown identity per household policy |
| 4 | Concierge | Acts, and records that identity was unknown |

The same speaker asking to unlock the front door receives a refusal, because that is a **safety-critical**
action class requiring high-confidence identity.

**Authority requirements scale with consequence.**

---

## Scenario 4 — A guest

### What the household experiences

A guest in the Living Space asks, "What's on Tom's calendar tomorrow?"

> "I can't share that."

### What each responsibility does

| Step | Responsibility | Action |
|---|---|---|
| 1 | Identity | Reports `unknown` |
| 2 | Operational Trust | Applies the least-privileged applicable policy — guest-safe |
| 3 | Operational Trust | Personal calendar content is not visible to unidentified people |
| 4 | Concierge | Refuses, without disclosing whether the calendar has anything on it |

**Never assume the most likely resident for an authority-bearing action.** The guest is not "probably
Tom" because Tom lives here.

The refusal also must not leak: "Tom has three meetings but I can't tell you about them" is a
disclosure.

---

## Scenario 5 — Two sessions meet in one Room

### What the household experiences

Tom's jazz is following him. David's podcast is already playing in the Living Space. Tom walks in.

The home does not merge them, does not silently stop either, and does not play both.

### What each responsibility does

| Step | Responsibility | Action |
|---|---|---|
| 1 | Truth | Both people are present in the Living Space; an active session exists |
| 2 | Continuity | Reports two sessions with different owners claiming one endpoint class |
| 3 | Continuity | Surfaces the conflict; **does not merge or terminate unilaterally** |
| 4 | Operational Trust | Neither person has authority to displace the other silently |
| 5 | Concierge | Suppresses the incoming transfer and offers Tom an alternative |

> "David's podcast is playing in the Living Space, so I left your jazz in the Office. Would you like it
> in the Den instead?"

**This is the worked example formalized as the Transfer-suppression outcome in Session Concurrency
Policy (`experience-and-session.md`, DL-102, resolving OD-27).** The session-merging algorithm for
cases where merging *is* permitted is deliberately open — **OD-24**.

---

## Scenario 6 — Child safety

### What the household experiences

A child in the Kitchen says, "Turn on the oven." Nothing happens, and the home explains.

### What each responsibility does

| Step | Responsibility | Action |
|---|---|---|
| 1 | Identity | Asserts the child, identity_confidence_band: High |
| 2 | Operational Trust | Child-safety policy prohibits heat-source control for this person |
| 3 | Concierge | Refuses and explains in age-appropriate language |

**The most restrictive applicable policy sets the ceiling.** The Home may permit autonomous kitchen
control; the person-scoped restriction wins.

---

## Scenario 7 — Evidence converges on Tom in the Den

| Evidence | Family | Contribution |
|---|---|---|
| Voice match for Tom, provider value **0.82** | Voice biometric | Supports **speaker attribution** |
| Tom's watch observed in the Den | Wearable proximity | Supports **Room presence**, at Tom's high configured reliability |
| Den occupancy active | Room occupancy | Corroborates context. **Identifies nobody** |
| Capture endpoint is the Den satellite | Endpoint context | Establishes where, not who |

Three reasonably independent families agree, nothing contradicts, and everything is current. The
assertion is **Tom, purpose current speaker in the Den, high confidence**, and the explanation says
why the evidence converged.

**The provider's 0.82 is still 0.82.** It was not overwritten. And high confidence is still not
permission — Operational Trust decides that separately.

---

## Scenario 8 — David's phone, which David often leaves behind

David's phone is observed in the Den. Occupancy is active.

**David's phone contributes at David's configured reliability, which is low and requires
corroboration** — because David leaves it behind, not because it is a phone. **No universal phone
weight is applied anywhere.**

David becomes a **candidate**. He is not confirmed present, and he is certainly not confirmed to be
speaking. Occupancy says a Room is occupied; it never says by whom. **Nothing sensitive proceeds on
this alone.**

---

## Scenario 9 — Evidence that disagrees

| Evidence | Bearing |
|---|---|
| Voice matches Tom at 0.82, through the Den satellite | Supports Tom as **speaker** |
| Tom's strongly bound watch is observed in the **Kitchen** | **Contradicts** Tom being present in the Den |
| David's phone is in the Den, occupancy active | Supports David's candidacy weakly; identifies nobody |

**The home does not add the signals up and move on.** The contradiction is claim-specific: it opposes
*Tom is in the Den* far more than it opposes *Tom spoke*. The outcome may remain uncertain or ask for
confirmation, and **the final reason records the contradiction** rather than quietly dropping it.

---

## Scenario 10 — Accounts, endpoints, and the people using them

| # | Situation | Outcome |
|---|---|---|
| 10a | Tom uses the companion app while authenticated | **Interaction initiator and authenticated session identity: Tom.** Room presence: not established. Current speaker: not established. **Physical holder of the device: unknown.** Operational Trust still evaluates the request |
| 10b | Someone uses the Den kiosk. Authenticated user is *Den Kiosk*; occupancy active; no voice, no person-bound proximity | **Endpoint context known. Human identity `unknown`.** The kiosk account is **not** a Person. Generic interaction remains available where authorised |
| 10c | Someone uses the Den kiosk **and speaks**; voice supports Tom; Tom's wearable is in the Den | The kiosk still supplies **endpoint and Room context only**. Voice and wearable support Tom. **The kiosk account never becomes Tom** — a fused speaker or Room-presence assertion is produced instead |

---

## Scenario 11 — What a household does not have, and what it has twice

| # | Situation | Outcome |
|---|---|---|
| 11a | The household owns **no wearables**. Voice supports a candidate; phone proximity agrees; occupancy is active | **The missing wearable is not evidence against anyone.** Fusion uses what exists, confidence is simply lower than it would be with stronger corroboration, and the interaction degrades gracefully |
| 11b | Phone proximity, a Wi-Fi tracker, native Person state from that phone, and companion-app location all report | **One device. One evidence family. One contribution** — not four confirmations. Native evidence is still referenced rather than duplicated |
| 11c | Tom's watch and David's phone are both in the Den, occupancy active, and the current voice matches Tom | Presence evidence supports **both** people. Voice distinguishes **the speaker**. **Room presence is not collapsed into speaker identity**, and both candidates stay visible in the reasoning |

---

## Scenario 12 — Weights, learning, and consent

| # | Situation | Outcome |
|---|---|---|
| 12a | Voice confidence is **0.82**; Tom's watch reliability is configured **0.90** | The result is **not** 0.86, not 1.72, and not any other arithmetic artefact. Both values are retained and distinct, fusion applies freshness, independence, context, contradiction, and claim type, and the outcome is stated as a band |
| 12b | Learning proposes raising Tom's watch reliability | The proposal references the observations behind it. **No silent change.** An authorised resident accepts it, acceptance creates a **Change Record**, **earlier Identity Assertions are untouched**, and the change is reversible and reconstructable |
| 12c | Consent for Voice Identity is withdrawn | Voice evidence becomes **ineligible for future fusion** — excluded, not down-weighted. Other evidence continues under its own consent and policy. Protected biometric material follows accepted retention rules, **prior records are not silently rewritten**, and the home stops using match scores |

---

## Scenario 13 — A voice nobody recognises, and a device nobody owns

The Den is occupied. A voice command is captured. The voice provider evaluates successfully and
returns **no eligible match**. An unassociated proximity source is visible. There is no authenticated
user, and no person-bound evidence of any kind.

| # | Responsibility | Behaviour |
|---|---|---|
| 1 | Identity | Reports `unknown` for **speaker attribution**, with the **human participant supported**, at high confidence. Someone spoke |
| 2 | Identity | Reports the provider result as `unknown`, **not `unavailable`** — the provider worked and returned a correct negative |
| 3 | Identity | Records the unassociated proximity source as **unknown evidence**. It is not joined to the voice, and it establishes nobody |
| 4 | Truth | The Den is occupied. **No contextual person-presence Fact is produced**, because no person was identified |
| 5 | Operational Trust | Applies the **unidentified-person policy**. A low-risk Room-scoped request may proceed where the household permits it |
| 6 | Concierge | Acts or refuses per policy, and records that identity was unknown |

**No Person is created.** Nothing durable is written about the speaker. When the assertion expires,
nothing of this person remains beyond the governed evidence records and their ordinary retention.

---

## Scenario 14 — An unidentified visitor interacts with the home

| # | Situation | Outcome |
|---|---|---|
| 14a | "Turn on the lights." | Identity reports Unknown Person. Operational Trust applies the unidentified-person policy. Participating lights in the Room may be controlled where the household permits it. **No resident permission or preference is inherited, and no person-specific learning occurs** |
| 14b | "What's the weather?" | The policy decides whether the general-question capability is available at all. Where it is, **only household-neutral context may be supplied** — a reasoning provider receives no private household context merely because the request came from inside the home. **OD-67** is unaffected |
| 14c | "Play some music." | Household-neutral playback may be permitted, under Room-scoped volume and capability policy. **No resident listening preference is inferred, and no known-Person profile is trained** |

---

## Scenario 15 — Who may hear the answer

Tom asks the Den voice assistant to read his latest email. The evidence supports Tom as the current
speaker at high confidence, and Tom's Room presence at high confidence.

| # | Situation | Outcome |
|---|---|---|
| 15a | David's phone supports David's Room presence at moderate confidence; occupancy is active | Tom's **access** to the email and the **disclosure** of it through Room voice are two decisions. **David is not presumed unauthorised merely because he is present** — the outcome depends on content, classification, policy, consent, and authorisation. Audience uncertainty is retained, private delivery may be offered, and the Decision Trace records why audible disclosure was or was not selected |
| 15b | An Unknown Person is likely present instead | Tom may still be authorised to **access** the content. The unknown potential listener changes the **disclosure** evaluation. Private content is not read aloud automatically; Concierge may offer Tom an authorised private surface or a content-free indication. **The Unknown Person receives no personal content** |
| 15c | Audience detection is unavailable | **The home does not assume Tom is alone.** *No signal* is not *nobody there*. Operational Trust applies the configured uncertainty rule (**OD-71**) — confirm, deliver privately, degrade to indication, or refuse. **Tom's identity confidence remains high and separate; it is the audience that is uncertain** |

---

## Scenario 16 — A service visit the home cannot confirm

A service appointment exists for the morning. During part of that window, unknown-person evidence is
observed, an unassociated proximity source appears, and movement is observed across several Rooms.

| # | Behaviour |
|---|---|
| 1 | The actor remains **Unknown**. A scheduled visit is **context, not identification** |
| 2 | The observations may be correlated into an Unknown Actor hypothesis, and a possible path reconstructed |
| 3 | It must **not** state that the actor was the scheduled service provider because the times overlap, and must not describe anyone as a cleaner or a contractor |
| 4 | Any interaction during the visit follows the unidentified-person policy, exactly as for any other unidentified person |
| 5 | If a role association is later established by governed evidence it is **added**: the original Unknown Person and Unknown Actor evidence is preserved, and the source, confidence, and effective time of the association are recorded |

---

## Scenario 17 — "Show me where the unknown person went"

A resident asks for the path of the unknown person between 08:00 and 16:00, with the time spent in
each Room.

| # | Behaviour |
|---|---|
| 1 | **The request requires authorisation.** Movement history is among the most sensitive projections the home can produce, and Operational Trust governs access to it |
| 2 | The reconstruction distinguishes observed events, derived intervals, inferred transitions, estimated dwell times, unknown gaps, and contradicting observations |
| 3 | Dwell times are labelled **estimated**, and account for a late first observation, an early last observation, sensor timeout, gaps, and overlapping coverage |
| 4 | Multiple-actor uncertainty is preserved rather than resolved for tidiness |
| 5 | **No identity is invented**, and no gap is silently closed. A reconstruction containing an unreported gap is a defect |

---

## Scenario 18 — An opening, a path, and no accusation

An exterior opening event is followed by occupancy in the Den, on the stairs, in the primary bedroom,
and in a closet, then an exit event. Camera references exist. Household mode classified the presence
as unexpected.

| # | Behaviour |
|---|---|
| 1 | A possible Unknown Actor path may be reconstructed, with entry through the opening labelled **observed** or **inferred** according to what the evidence actually supports |
| 2 | Video is **referenced** in the systems that own it, never copied in order to correlate it, and **never asserted to depict the actor** without supporting evidence |
| 3 | The reconstruction may state the opening event, the unknown-person evidence, the possible path, the video references, the policy classification, and the Communications or alarms produced |
| 4 | It must **not** claim forced entry, theft, criminal intent, an identity, a single actor, or legal proof. **"Robber", "burglar", and "intruder" are not identity outcomes** |
| 5 | A Preservation Hold or an Evidence Package may apply under accepted policy. Both remain HTBW architectural terms, and **neither is a claim of legal effect** |

---

## Scenario 19 — One person, or two

Two unassociated proximity sources are observed, occupancy overlaps in separated Rooms, two unmatched
voices are captured, and camera evidence is incomplete.

| # | Behaviour |
|---|---|
| 1 | The architecture does **not** force one actor, and does **not** force two |
| 2 | Two unassociated sources are not assumed to be two people, and two unmatched voices are not assumed to be two people |
| 3 | Alternative reconstructions are retained side by side, with their reason codes |
| 4 | The honest answer is stated: at least one unknown person was supported, and the evidence cannot reliably determine whether one or several actors were present |

---

## Scenario 20 — The unknown actor turns out to have been someone

A week later, governed evidence establishes that the Unknown Actor from Scenario 16 was a specific
known person.

| # | Behaviour |
|---|---|
| 1 | The original observations, assertions, and confidences are **unchanged** |
| 2 | The association is **additive** and governed: who or what established it, with what confidence, from what Effective Time, and a Change Record where one is required |
| 3 | **Earlier Identity Assertions are not rewritten.** The earlier `unknown` outcomes remain correct records of what was known then |
| 4 | No permission is granted retroactively, and no past decision becomes reinterpretable as though the identity had been known |
| 5 | The reconstruction can show **what was known at each point in time**, not only what is known now |

---

## Scenario 21 — Requests that need no identity at all

| # | Request | Behaviour |
|---|---|---|
| a | *"What time is it?"* | No identity is required. Concierge answers. **No presentation threshold is evaluated, no candidate is named, and no attribution is recorded merely to answer** |
| b | *"Play music"* | No identity is required for the household-neutral action. **The requirement belongs to the capability, not the person** — playing on a shared speaker and reaching into a Person's music account are two different requirements (**DL-31**, **OD-01**) |
| c | *"Turn on the Apple TV"* | Powering a shared device is household-neutral. **This does not imply authority over any account signed in on it**, and *no identity required* is a governed requirement, **not an absence of governance** |
| d | *"What's the capital of France?"* | Answerable from household-neutral context. **The reasoning provider receives no identity, no household-private context, and no candidate name** (**OD-67**), and its involvement never makes it the sensitivity classifier |

---

## Scenario 22 — Speaking a name

| # | Situation | Behaviour |
|---|---|---|
| a | Confidence meets the Identity Presentation Threshold | Concierge may say *"Good morning, Tom."* **This grants nothing** — no calendar, no preferences, no session, no resource, no attribution, and no learning eligibility (**DL-36**, **OD-65**) |
| b | Confidence is below the threshold | The home answers **without naming anyone**. It does not guess, does not say *"probably Tom"* as though it were fact, and does not fall silent when a neutral answer is available |
| c | Another Person is present | Naming a candidate aloud is a **disclosure**, evaluated against audience composition before it is spoken (**DL-34**). Meeting the presentation threshold does not settle whether the name may be said in this Room, to this audience, on this surface |

---

## Scenario 23 — Capability access thresholds

| # | Situation | Behaviour |
|---|---|---|
| a | Asset maintenance history at moderate confidence | The threshold belongs to **the asset record**, not to the requestor. Moderate confidence may suffice for a household-neutral maintenance record and be insufficient for a Person-scoped one. **The presentation threshold is irrelevant here** |
| b | A public manual versus a private appraisal | **One asset, two requirements.** Reading the manual, reading the appraisal, editing the record, and deleting it are **four protected operations**, and they are never collapsed into one threshold (**DL-36**). This creates **no duplicate asset definition** |

---

## Scenario 24 — A confirmation opportunity

Tom asks for his calendar. Confidence is below the requirement.

| # | Situation | Behaviour |
|---|---|---|
| a | The shortfall | **A shortfall is not automatically a refusal.** Operational Trust may offer confirmation instead. The challenge is itself a Communication and is audience-evaluated before it is spoken (**DL-37**) |
| b | *"Yes"* | Adequate only where policy accepts a verbal confirmation for this capability. It produces a **bounded** confirmed interaction — this purpose, this capability, this channel, this Room, this Person, for a governed time — and **the original assertion remains at its original confidence** |
| c | A different voice answers *"Yes"* | The confirming voice is evidence in its own right. **A confirmation on behalf of someone else is not a confirmation**, and identity evidence contradicting the candidate makes the outcome `Unclear` or `Denied`, never `Confirmed` |
| d | *"No, I'm David"* | The original assertion is preserved and the contradiction recorded. **A stated name is a claim, not an identification.** David is not established, **the next-highest candidate is never silently selected**, no association is created, no profile is trained, and no weight changes (**DL-32**) |

---

## Scenario 25 — A confirmation requirement

| # | Situation | Behaviour |
|---|---|---|
| a | *"Add a new administrator"* | Confirmation is **required regardless of confidence**. Very high confidence does not satisfy it, and **a spoken *yes* on the same channel is not adequate** — that channel already supplied the evidence in question |
| b | Confirmation on an authenticated phone | Satisfies the strength the capability demanded. It **says nothing about who is in the Room**, and therefore authorises no disclosure (**DL-34**) |
| c | The confirmation expires | It is **expired, not weakened**. The request is re-evaluated. `Expired` is never rendered as `Confirmed`, and an expired confirmation is never carried silently forward |

---

## Scenario 26 — Access is not disclosure

Tom asks for a private calendar entry.

| # | Situation | Behaviour |
|---|---|---|
| a | David is present | Access may be permitted **and disclosure refused**. *Access allowed, private delivery available* must remain representable, and a redirect to a private surface is a legitimate outcome (**DL-34**) |
| b | An Unknown Person is present | An unidentified participant is **not an authorized recipient**. The absence of an identification is not the absence of a listener |
| c | Confidence is below threshold **and** an Unknown Person is present | **Two separate decisions, both recorded.** A confirmation may resolve the access question and **still leaves the disclosure question open** — confirmation is never bounded by audience |

---

## Scenario 27 — The challenge itself discloses

*"I think I am speaking with Tom. Can you confirm?"* announces to the Room that the home believes Tom
is present.

| # | Behaviour |
|---|---|
| 1 | The challenge is a **Communication**, with an audience composition, a Delivery Surface, and a disclosure decision (**DL-34**, **DL-37**) |
| 2 | Naming a candidate aloud, asking neutrally without naming anyone, and redirecting to an authorized private surface are **three different disclosure outcomes** |
| 3 | **No wording is prescribed.** The requirement is that the challenge is governed |
| 4 | Where audience composition is uncertain, the policy applied is **OD-71** |

---

## Scenario 28 — One anchor, one corroboration, one ceiling

Tom speaks through the Den voice assistant. Voice supports Tom at 0.82; Tom's watch is observed in the
Den with high configured reliability; Den occupancy is active; the capture endpoint is the Den
satellite; nothing contradicts.

| # | Behaviour |
|---|---|
| 1 | **The provider value remains 0.82, as reported.** It is never rewritten as the fused result |
| 2 | Watch reliability stays a **separate** configured value. The two are not multiplied or averaged |
| 3 | Voice is the **anchor family** for Speaker Attribution — the only eligible family whose ceiling permits it to support that claim |
| 4 | The watch is an **independent family** and adds **one bounded corroboration step**, not a second score |
| 5 | **Occupancy supports context, not identity.** Its ceiling for Speaker Attribution is nil, so it contributes no step |
| 6 | Endpoint Context records the Den satellite. It identifies a **thing**, and asserts no person |
| 7 | The outcome is `known`, with supporting evidence, families, reason codes, and the **Fusion Policy version** retained. **No permission decision is made** |

---

## Scenario 29 — Purpose decides everything

| # | Situation | Behaviour |
|---|---|---|
| a | David's phone observed in the Den; occupancy active; no voice, no wearable | Phone proximity may anchor **Room Presence** for David at its configured reliability. It **cannot** anchor Speaker Attribution — its ceiling for that purpose is nil, so David is **not** the current speaker. No universal phone weight is used, and David's configured value applies, not a device-type default |
| b | Voice supports Tom; the authenticated application user is David; purpose is Speaker Attribution | Voice is relevant to speaker attribution; the authenticated user is relevant to **Authenticated Session Identity** and **Interaction Initiator**. **They are not averaged, because they answer different questions.** Tom may be the speaker and David the session holder **with no contradiction at all** |
| c | Household presence is strongly supported; Room Presence is not | **Household Presence may be `known` while Room Presence is `unknown` or unsupported.** A native tracker's zone evidence is never promoted into a Room claim the source does not supply |

---

## Scenario 30 — Contradiction, correlation, and absence

| # | Situation | Behaviour |
|---|---|---|
| a | Voice supports Tom in the Den, but Tom's strongly bound watch is in the Kitchen | Contradiction is **claim-specific**. The watch contradicts *Tom is present in the Den* far more than it bears on his session identity. **The signals are not blindly added.** Bounded reduction applies, and the result may be reduced, `ambiguous`, or unresolved. **The contradiction stays visible** |
| b | Tom's phone produces BLE, a Wi-Fi tracker, companion-app location, and native Person state | **One correlation family, one contribution.** These are not four confirmations. The native Person is derived from its trackers and shares their family. Native references are preserved by reference (**DL-31**), and the explanation records the correlation treatment |
| c | The household owns no wearables | **Missing evidence is not negative evidence.** Absence never subtracts and never enters a denominator. The available evidence is evaluated, the **ceiling** may be lower than a corroborated case, and the capability remains fully functional |
| d | Tom's watch and phone both support Tom, but both are stale | Freshness reduces the contribution or excludes the observation. **Configured reliability never overrides staleness** — reliability is applied *after* freshness and can only lower or hold. Reason codes name the stale evidence |
| e | An optional source is simply not configured | **Not configured** is distinct from unavailable, not observed, stale, disabled, contradictory, and no match. The household is not penalised for declining it |

---

## Scenario 31 — Known, Ambiguous, Unknown, and Unavailable

| # | Situation | Behaviour |
|---|---|---|
| a | Tom and David are both likely in the Den; voice supports Tom | **Room Presence may support both**, while **Speaker Attribution** supports Tom. Presence is never collapsed into speaker identity |
| b | Two known candidates finish close together | The **separation requirement** is not met, so the outcome is `ambiguous`. **The numerically highest candidate is never silently selected**, and competing candidate information is retained safely |
| c | Human participation is strongly supported; the best known candidate is weak | The outcome is `unknown` with `human_participant` supported. **A weak known candidate is never forced**, and the reason is explainable |
| d | Speech captured, occupancy active, an unassociated proximity source observed, no known-person evidence | `unknown`, human participant **supported**. **The provider is not marked unavailable** — it worked. The unassociated source and the unmatched voice are **two observations, not one identity**, and no synthetic Person is created |
| e | The voice provider is offline | Its evidence is **unavailable**. Other evidence may still support other purposes. If a **required** input for the requested purpose cannot be evaluated, the state is `unavailable` — **never rendered as `unknown`, and never as a known candidate** |

---

## Scenario 32 — Eligibility, not weighting

| # | Situation | Behaviour |
|---|---|---|
| a | Voice consent is withdrawn | Voice evidence becomes **ineligible and is excluded before weighting** — it is **not** merely down-weighted. The exclusion reason is preserved. Other eligible evidence remains available, and protected biometric material follows accepted retention policy |
| b | A managed kiosk initiates an interaction; the kiosk account and Room are known; no voice match | **Endpoint Context is known. The endpoint account is not a human identity.** Speaker Attribution may be `unknown` with human participation supported. No synthetic Person is created, and the kiosk account never silently becomes the person using it |
| c | A reasoning provider suggests who it thinks is speaking | **Not eligible identity evidence.** No accepted contract admits it, so it never enters the candidate set and never enters fusion. **General reasoning does not become identity fusion** (**OD-67**) |

---

## Scenario 33 — Policy version and history

| # | Situation | Behaviour |
|---|---|---|
| a | A person-specific reliability value is changed after household approval | A **Change Record** is created through the promotion ladder. **New** assertions use the new Fusion Policy version; **earlier assertions are unchanged**, and no silent retroactive recalculation occurs |
| b | An old assertion is explained after the policy changed | The explanation names the **Fusion Policy version that produced it** and stays accurate. Today's policy is never silently re-read to describe last month's result (**P27**, **P30**) |
| c | Confirmation succeeds after a Moderate assertion | **The fusion result remains Moderate.** Confirmation is not fused, the function is not re-run with *confirmation = 100*, and Operational Trust authorises the bounded request separately. **Both records survive** (**DL-37**) |

---

## Scenario 34 — Identity is not required

*"Play household music."*

| # | Behaviour |
|---|---|
| 1 | Identity may record `not required` for the purpose. **No fusion is performed**, and no candidate set is built |
| 2 | `not required` is distinct from `unknown`, from `unavailable`, and from a failed evaluation |
| 3 | **Identity draws no permission conclusion.** Whether the request proceeds is Operational Trust's (**DL-36**) |

---

## Scenario 35 — One assertion, two independent consumers

Lamp control is configured with **Required Identity Band `None`**. Address by Name is enabled at
**High**.

| # | Situation | Behaviour |
|---|---|---|
| a | Current speaker: Tom, **High**. *"Turn on the lamps."* | Lamps proceed **without relying on Tom's identity**. Address by Name independently qualifies. Response: *"Tom, I have turned on the lamps."* The trace states that identity was **unnecessary for access** and **sufficient for presentation** |
| b | Current speaker: Tom, **Moderate** | Lamps still proceed. Response is neutral: *"I have turned on the lamps."* **The action is not denied because a presentation threshold was unmet** |
| c | Current speaker: Unknown Person | Lamps may proceed where every other policy permits. Response is neutral. **No synthetic Person is created and no person-scoped learning occurs** (**DL-33**, **OD-65**) |
| d | Address by Name is **disabled**; current speaker Tom at **Very High** | Capability access uses its own requirement. **Tom is not named.** High confidence never overrides a disabled presentation policy |
| e | A calendar operation is configured `None` while Tom is **High** | Access does not rely on identity. The unusual policy is represented honestly, Address by Name remains a separate evaluation, and **Identity imposes no hidden minimum** |

The trace never says *"High exceeded `None`."* It says **known-Person identity was not required for
this operation** (**DL-39**).

---

## Scenario 36 — Occupancy continues; the person changes

Tom is in the Den, his watch is in the Den, and voice supports Tom. He asks for the lamps and is
answered *"Tom, I have turned on the lamps."* Tom then leaves and David enters. **Room occupancy never
becomes inactive.**

| # | Situation | Behaviour |
|---|---|---|
| a | David speaks | Identity evaluates the **current** interaction from current eligible evidence. Tom's watch is no longer in the Den, and Tom's voice is not the current voice |
| b | Tom's prior assertion | **Not reused.** Continuous occupancy is not continuous identity, and the prior band is not carried forward |
| c | Tom's prior naming eligibility | **Not reused.** The response must not address David as Tom |
| d | An Unknown Person enters instead of David | The prior Tom assertion does not persist as current speaker. The current result may be `unknown`, and **named presentation is not used** |
| e | Tom's prior assertion | It remains a **permanently valid historical record** (**DL-64**) — this does not make Tom the new speaker. The prior assertion **remains a correct historical record** for its original purpose and moment; the new interaction receives a new evaluation |

> **Continuous presence is not continuous authentication.**

---

## Scenario 37 — Confirmation is spent by its operation

Tom is `known` at **Moderate**. The calendar's requirement is **Very High**, with confirmation permitted as
a substitute. Tom confirms by an accepted method and the calendar operation proceeds.

| # | Situation | Behaviour |
|---|---|---|
| a | The Identity Assertion afterwards | **Still Moderate.** Confirmation adds a separate governed record and **never changes the band** (**DL-37**) |
| b | Tom then asks for email | **Re-evaluated** against the mailbox's own requirement. The calendar confirmation is **not** reused |
| c | Tom immediately asks a second calendar question | **Re-evaluated by default.** If the household has configured a bounded multi-step task, **its bound is explicit and stated**; no general session is created |
| d | Tom leaves and David enters while occupancy remains active | Tom's confirmation **does not persist**. David is not treated as Tom, and **Room presence preserves no authorisation** |
| e | The calendar requires **Very High** and Tom is **High** with no confirmation given | Operational Trust identifies an **insufficient band**. Confirmation may be offered where configured, at the **Required Confirmation Strength** the calendar declares. **Identity remains High** — the refusal or the challenge is a **Trust** outcome, never an Identity one |
| f | The declared strength is **Strong**, and the deployment has no verified mechanism meeting it | The confirmation outcome is **`Unavailable`**. The operation is refused or degraded under normal policy, and **the requirement is never quietly downgraded to Verbal** |

---

## Scenario 38 — Purpose, state, and policy version

| # | Situation | Behaviour |
|---|---|---|
| a | Tom is **High** for `current_speaker` and **Low** for room presence | Presentation based on the current-speaker purpose may qualify where policy permits. **The room-presence band is never substituted**, and the two assertions stay separate (**DL-38 F1**) |
| b | Music requires no identity | Access evaluation may record `not required`. If Address by Name is nonetheless considered, a **separate current-speaker assertion** is produced for that decision. Access and presentation remain independent |
| c | An Unknown Person requests a capability requiring **Moderate** | The known-Person requirement is not satisfied. Operational Trust decides whether confirmation or another route is permitted. **The Unknown Person is assigned neither `Low` nor `None`** |
| d | The Address by Name threshold is changed from **High** to **Very High** | The change follows accepted configuration-history governance. **Earlier presentations remain explainable under the prior setting**, Identity Assertions are **not** recalculated, and the next response applies the current setting (**P27**, **P30**) |

---

## Scenario 39 — Room delivery, standing permission, and message-scoped authorization (DL-94)

Tom has configured a Room-Delivery Audience Preference permitting Room delivery at **Interrupt
Current Activity** Urgency or above, for a **Household** audience, but not for **Guest**.

| # | Situation | Behaviour | Must not |
|---|---|---|---|
| a | Tom alone; a Critical, Room-eligible Communication | Normal Room delivery | Request authorization when standing permission already covers the audience |
| b | Tom with David (Household); Room-eligible | Normal Room delivery under the Preference; no exception requested | Treat David's presence as requiring a one-message exception merely because Tom is not alone |
| c | Tom with an unpermitted Guest; Room-eligible; private delivery has failed; the Challenge itself is safe | A Room-Delivery Authorization Challenge is issued, disclosing only existence, Urgency, that private delivery failed, and the request | Disclose subject, Category, relationship, or content before Explicit Yes |
| d | Same as (c); Tom responds Explicit Yes | Room delivery of **this Communication only**; Tom's standing Preference is unchanged | Treat the Yes as a new standing permission for Guest audiences generally |
| e | Same as (c); Tom responds Explicit No | No Room delivery for this Communication; no repeat request for it; private delivery continues | Mark the Communication delivered, refused, cancelled, or acknowledged |
| f | Same as (c); no response | The Communication remains outstanding under the existing retry lifecycle (**OD-54**); private delivery continues | Infer denial or consent from silence |
| g | A Communication Tom's Preference never made Room-eligible (e.g. below **Interrupt Current Activity**), Guest present | No Room interaction of any kind — not Indication, not a Challenge | Offer a Room-delivery exception for non-Room-eligible content |
| h | The Challenge itself would disclose (for example, only one possible subject exists in context) | The existing further-degradation path applies (neutral challenge/defer/refuse) | Issue the Challenge anyway merely because standing permission was insufficient |
| i | A second, later Communication of the same type arrives after Tom's earlier Explicit Yes | Evaluated fresh from the standing Preference; the earlier authorization does not apply | Reuse the previous message's authorization for a different Communication |
| j | Private delivery succeeds while a Room-authorization request is still unresolved | The Communication completes; the pending authorization need expires with delivery | Continue prompting for Room authorization after delivery has completed |

---

## Rules demonstrated

1. Identity `ambiguous` and `unknown` are first-class, and are never silently resolved.
2. Authority requirements scale with action risk.
3. Sessions have owners, and displacement requires authority.
4. Concierge asks rather than guessing.
5. Refusals do not leak the content they are protecting.
6. Restriction always wins over permission.
7. **Reliability is configured per Person and source, never per device type.**
8. **Occupancy is not identity, an account is not a person, and authentication is not presence.**
9. **Correlated evidence counts once; missing evidence counts as nothing.**
10. **A provider's value and the home's confidence are different numbers, and both survive.**
11. **Unknown Person is a valid outcome, never a failure, and never a synthetic Person.**
12. **A provider's correct negative is not an unavailable service.**
13. **Knowing who asked does not establish who may hear the answer.**
14. **Correlation requires more than co-occurrence, and an estimate is never an observation.**
15. **There is no universal threshold. The requirement belongs to what is being protected.**
16. **Being addressed by name grants nothing; presentation is not access and not personalization.**
17. **A confirmation is bounded, and never makes the assertion behind it more confident.**
18. **A confirmation challenge is itself a disclosure.**
19. **Fusion is stepped, not summed. One anchor family, bounded corroboration, a purpose ceiling.**
20. **Absence lowers the ceiling; it never applies a penalty.**
21. **Qualification only ever reduces — provider match, quality, freshness, and reliability are never multiplied together.**
22. **Every assertion names the Fusion Policy version that produced it.**
23. **A Person's own co-presence with another Person is not thereby an unauthorized audience; a
    message-scoped Room-delivery authorization never becomes standing permission, and standing
    permission is evaluated independently of any single Communication's outcome (DL-94).**
23. **`None` is a Trust requirement, not an Identity band. Identity produces four bands and never `None`.**
24. **Access and presentation are decided independently; an unmet presentation threshold never denies an action.**
25. **Continuous occupancy is not continuous identity, and a valid assertion is not the current-speaker assertion.**
26. **A confirmation is spent by the operation that required it. There is no presence grace period.**

---

## Related documents

- [../models/person-and-identity.md](../models/person-and-identity.md)
- [../contracts/identity-contract.md](../contracts/identity-contract.md)
- [../models/operational-trust.md](../models/operational-trust.md)
- [../models/communication.md](../models/communication.md)
- [../models/temporal-record.md](../models/temporal-record.md)
- [../models/experience-and-session.md](../models/experience-and-session.md)
- [../architecture/behavioral-governance.md](../architecture/behavioral-governance.md)
- [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md)
