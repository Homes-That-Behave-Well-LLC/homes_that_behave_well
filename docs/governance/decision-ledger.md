# Decision Ledger

> **Document status: Canonical governance.**
> Authority: [authority-order.md](authority-order.md).

---

## Purpose

The record of what the refoundation decided, and what it deliberately left open.

**A deliberately open decision is not a gap.** Recording it honestly is better than inventing an
answer the household has not chosen.

---

## Part 1 — Accepted decisions

| ID | Decision | Supersedes | ADR |
|---|---|---|---|
| **DL-01** | HTBW Core is defined by **seven responsibilities**: Foundation, Stewardship, Identity, Truth, Continuity, Operational Trust, Concierge | The four-service platform model | [adr-htbw-core-refoundation.md](../architecture/adr-htbw-core-refoundation.md) |
| **DL-02** | **Human Trust is an outcome, not a layer.** It cannot be implemented directly | Any treatment of trust as a component | [adr-htbw-core-refoundation.md](../architecture/adr-htbw-core-refoundation.md) |
| **DL-03** | **Behavioral Governance is cross-cutting**, not a layer | Any treatment of governance as a service | [adr-htbw-core-refoundation.md](../architecture/adr-htbw-core-refoundation.md) |
| **DL-04** | **Truth is a first-class authoritative fact engine.** Foundation defines what a Fact is; Truth decides what is factual now | "Foundation owns truth" | [adr-truth-as-fact-engine.md](../architecture/adr-truth-as-fact-engine.md) |
| **DL-05** | **Voice Identity is superseded as a platform-service boundary.** The responsibility is **Identity**; voice is one evidence source | `adr-voice-identity-platform-service.md` | [adr-identity-replaces-voice-identity-boundary.md](../architecture/adr-identity-replaces-voice-identity-boundary.md) |
| **DL-06** | Identity Evidence, Identity Assertion, and Contextual Person-Presence Fact are **three distinct objects** with two distinct owners | Conflation of identity with presence | [adr-identity-replaces-voice-identity-boundary.md](../architecture/adr-identity-replaces-voice-identity-boundary.md) |
| **DL-07** | **Stewardship** is a first-class responsibility for significance, care, obligations, and lifecycle accountability | Stewardship as inventory; Asset Intelligence as the "what matters" layer | [adr-htbw-core-refoundation.md](../architecture/adr-htbw-core-refoundation.md) |
| **DL-08** | The **HTBW asset model is Foundation-owned descriptive knowledge**. The standalone Asset Intelligence product remains separate, with no compatibility requirement | Asset Intelligence as an HTBW Core layer | [adr-htbw-core-refoundation.md](../architecture/adr-htbw-core-refoundation.md) |
| **DL-09** | **Room Configuration is owned by Foundation**, and is an interaction-definition model | Room Configuration implicitly inside Concierge | [adr-room-configuration-ownership.md](../architecture/adr-room-configuration-ownership.md) |
| **DL-10** | **Contextual Vocabulary is part of Room Configuration.** Concierge consumes the resolved target | Vocabulary owned by Concierge | [adr-room-configuration-ownership.md](../architecture/adr-room-configuration-ownership.md) |
| **DL-11** | **Existence, Participation, Exposure, and Authority are four distinct states** | Conflation of existence with availability | [adr-room-configuration-ownership.md](../architecture/adr-room-configuration-ownership.md) |
| **DL-12** | **"Merged Room" is the single canonical term.** "Composite Room", "Operational Space", "Interaction Space", "Listening Area", and bare "Space" are superseded | The terminology fork across 15+ documents | [adr-htbw-core-refoundation.md](../architecture/adr-htbw-core-refoundation.md) |
| **DL-13** | A Room and a Merged Room **behave identically**. Movement between constituent Physical Rooms of one Merged Room is not a transfer | Special-case orchestration for composites | [adr-room-configuration-ownership.md](../architecture/adr-room-configuration-ownership.md) |
| **DL-14** | **Operational Trust** owns authority; it is distinct from Human Trust | Absence of an authority owner | [adr-htbw-core-refoundation.md](../architecture/adr-htbw-core-refoundation.md) |
| **DL-15** | The **Decision Trace** is a required output of every decision, action, non-action, and suppression | Explainability as an optional feature | [adr-htbw-core-refoundation.md](../architecture/adr-htbw-core-refoundation.md) |
| **DL-16** | **Home Assistant First** — HA capability is used before HTBW builds its own (P21) | Parallel HTBW primitives by default | [adr-home-assistant-first-and-connected-storage.md](../architecture/adr-home-assistant-first-and-connected-storage.md) |
| **DL-17** | **Connected Storage** — durable household knowledge lives in attached storage with explicit traceability (P22) | Implicit or hidden storage | [adr-home-assistant-first-and-connected-storage.md](../architecture/adr-home-assistant-first-and-connected-storage.md) |
| **DL-18** | **Native Experience** — HTBW presents as a native part of Home Assistant; no invented UI standards (P23) | Custom UI conventions | [adr-home-assistant-first-and-connected-storage.md](../architecture/adr-home-assistant-first-and-connected-storage.md) |
| **DL-19** | **HTBW Core is greenfield.** No compatibility requirement with Asset Intelligence, Voice Identity, or Concierge | Implicit migration obligations | [adr-htbw-core-refoundation.md](../architecture/adr-htbw-core-refoundation.md) |
| **DL-20** | **The framework is vendor-agnostic.** Home Assistant is the first implementation environment, not a constraint | Platform-shaped architecture | [adr-home-assistant-first-and-connected-storage.md](../architecture/adr-home-assistant-first-and-connected-storage.md) |
| **DL-21** | **A learned suggestion is not an autonomous policy** (P26) | Silent promotion of learned patterns | [adr-htbw-core-refoundation.md](../architecture/adr-htbw-core-refoundation.md) |
| **DL-22** | The **assessment-to-platform traceability model** is canonical | Untraced recommendations | [adr-htbw-core-refoundation.md](../architecture/adr-htbw-core-refoundation.md) |
| **DL-23** | The **authority order** in [authority-order.md](authority-order.md) governs all conflicts | Ad-hoc precedence | [adr-htbw-core-refoundation.md](../architecture/adr-htbw-core-refoundation.md) |
| **DL-24** | **Historical Explainability is a constitutional requirement** (P27). The home must retain enough governed information to reconstruct what it observed, believed, knew, and decided, and why. Retention is a **floor as well as a ceiling**. Historical Explainability is cross-cutting and owns no store | Explainability treated as single-decision only; retention treated only as a limit | [adr-historical-explainability-and-historical-truth.md](../architecture/adr-historical-explainability-and-historical-truth.md) |
| **DL-25** | **Truth is the system of record for both present and historical Facts** (P28). Operational expiration removes a Fact from *what is true now*; it does not delete *what was true then*. Truth owns Fact history and the eight lifecycle transitions. No consumer may maintain a competing or re-derived Fact history | Fact history unowned; `event-model.md` "event history remains authoritative" | [adr-historical-explainability-and-historical-truth.md](../architecture/adr-historical-explainability-and-historical-truth.md) |
| **DL-26** | **History is recorded as governed change, not as repeated full copies** (P29). A Current Projection answers what is true now; history consists of immutable Change Records and Domain Events, accelerated by Snapshots. HTBW must not require comparison of complete stored payloads to discover what changed | Full-payload versioning as the default history pattern; pure event sourcing | [adr-temporal-record-model.md](../architecture/adr-temporal-record-model.md) |
| **DL-27** | **Governed records reference exact versions and do not copy complete payloads** (P30). An explanation must remain accurate after configuration or policy changes. A dangling reference is reported, never silently rendered as though the source record never existed | Decision Traces embedding copies of their inputs | [adr-temporal-record-model.md](../architecture/adr-temporal-record-model.md) |
| **DL-28** | **Communication is separate from delivery** (P31). A Communication is a household interaction that exists independently of transport. Origination establishes that something must be conveyed, to whom, and with what significance; delivery establishes surface, moment, form, and whether at all. A Communication is never defined as a notification, push message, announcement, or indicator | Communication modelled as a transport artifact; delivery-channel enumerations embedded in domain models; *Notification* and *Message* as HTBW domain terms | [adr-resident-communication-and-delivery-separation.md](../architecture/adr-resident-communication-and-delivery-separation.md) |
| **DL-29** | **Permission to act does not imply permission to announce** (P32). Outbound communication is governed by the Existence → Participation → Exposure → Authority chain, evaluated against who can perceive the delivery surface. Where context is insufficient to deliver safely, the **delivery** degrades, not the governance | Exposure rules treated as applying only to requested disclosure | [adr-resident-communication-and-delivery-separation.md](../architecture/adr-resident-communication-and-delivery-separation.md) |
| **DL-30** | **Home Assistant First carries an ordered burden of proof** (P21). Native capability, then an existing maintained integration or ecosystem capability, then an HTBW extension that governs an existing capability, then — only then — a new HTBW capability. Each step must record the capability evaluated, the source documentation, the constitutional requirement, the remaining gap, and why the lower layer cannot practically satisfy it. **An undocumented evaluation does not discharge the burden, and unverifiable documentation leaves the decision open** | "Home Assistant First" asserted as a preference discharged by assertion | [principles.md](../architecture/principles.md), [home-assistant-boundary.md](../architecture/home-assistant-boundary.md) |
| **DL-31** | **HTBW references native Home Assistant objects and extends them; it does not copy them** (P21, P30). Home Assistant remains authoritative for its registry objects and every property those objects natively own. HTBW references them by stable identifier and retains only the additional information required by a constitutional requirement. Where an HTBW concept benefits from native visibility, state, targeting, or automation, a **native representation** is created or used in preference to a parallel hierarchy — and that representation is a projection, never a second authority. **No resident may be required to maintain the same information twice** | Native metadata mirrored into HTBW storage; parallel registries; a projection treated as the authoritative record; residents maintaining the same value in two places | [home-assistant-boundary.md](../architecture/home-assistant-boundary.md), [../models/asset.md](../models/asset.md), [../models/room-configuration.md](../models/room-configuration.md), [../models/person-and-identity.md](../models/person-and-identity.md) |
| **DL-32** | **Identity evidence reliability belongs to the Person-to-evidence-source association, not to the evidence type** (P26, P30, DL-06, DL-31). Every Identity Assertion states the **purpose** it answers, and no general-purpose identity score exists. A source contributes only to the claims it can actually establish, only where consent permits, weighted by the reliability configured for **that Person and that source**, adjusted for freshness, grouped into evidence families so correlated observations are not counted twice, and offset by claim-specific contradiction. **Configured reliability is a contribution weight, never measured accuracy. A provider match value is retained as reported and is never rewritten as fused confidence. Missing evidence is not contradicting evidence.** Identity performs fusion; Truth decides what becomes a Fact; Operational Trust decides permission separately. Reliability may be proposed by learning but **never silently changed**, and a change never rewrites an earlier assertion | Universal per-device-type weights; adding provider values to configured weights; counting one device's observations as independent confirmations; a kiosk account treated as a person; occupancy treated as identity; authentication treated as physical presence; confidence treated as permission | [../models/person-and-identity.md](../models/person-and-identity.md), [../contracts/identity-contract.md](../contracts/identity-contract.md), [home-assistant-boundary.md](../architecture/home-assistant-boundary.md) |
| **DL-33** | **Unknown Person is a valid Identity Assertion outcome, and never a native Person** (P15, DL-06, DL-31, DL-32). Identity may establish with high confidence that a human participant exists while being unable to associate that participant with any known Person. This is the existing `unknown` state, carrying whether a **human participant** is supported so that *"someone is here and I do not know who"* is distinguishable from *"I have no evidence anyone is here"*. A provider that evaluated successfully and returned no eligible match yields `unknown`, **never `unavailable`**. An Unknown Person expires with the assertion, references no Person, **creates no Home Assistant Person**, owns no preferences or history, inherits nothing from any resident, generates **no person-scoped learning**, and grants nothing. What an Unknown Person may request, control, or receive is the **unidentified-person policy**, owned by Operational Trust as a policy subject rather than a profile | A synthetic *Guest*, *Visitor*, or *Unknown* Person created to carry a policy; `unknown` reported as `unavailable`, an error, or an absence; a durable unknown-person profile that accumulates across visits; an unknown evidence source treated as a person, a role, or a recurring individual; occupancy treated as identity; resident permissions or preferences inherited by an unidentified person | [../models/person-and-identity.md](../models/person-and-identity.md), [../models/operational-trust.md](../models/operational-trust.md), [../contracts/identity-contract.md](../contracts/identity-contract.md), [home-assistant-boundary.md](../architecture/home-assistant-boundary.md) |
| **DL-34** | **Disclosure is evaluated against audience composition, not against requestor identity** (P32, DL-28, DL-29). Establishing who asked does not establish that everyone able to perceive the answer is an authorized recipient. **DL-29 stated this for unprompted communication; it applies identically to a solicited answer.** Access and disclosure are two separate Operational Trust decisions, and *access allowed, disclosure not appropriate* and *access allowed, private delivery available* must remain representable. **Audience composition** — who may perceive content through a proposed surface — is a governed input that **consumes** accepted identity assertions and presence Facts, **identifies nobody**, is never a second identity fusion, and must retain its uncertainty. Requestor, Speaker, Present Person, Potential Listener, Authorized Recipient, and Delivery Target answer different questions and are never collapsed | A single audience field; requestor authorization treated as room-wide authorization; occupancy count treated as audience identity; a detected device treated as proof its owner can hear; absence of evidence treated as proof of solitude; audience inference producing a person identity; a surface treated as private because it is a phone; a reasoning provider used as the sensitivity classifier | [../models/operational-trust.md](../models/operational-trust.md), [../models/communication.md](../models/communication.md), [principles.md](../architecture/principles.md) |
| **DL-35** | **A historically correlated actor is a bounded reference within one reconstruction, never an identity** (P15, P21, P22, P30, DL-30, DL-31). An **Unknown Actor Reference** groups observations sufficiently supported as belonging to one actor within a defined reconstruction scope. It is part of the projection, not a store, and it asserts no Person, role, occupation, intent, or criminality. **Temporal proximity alone never establishes correlation**; adjacency, travel plausibility, evidence continuity, entry and exit, contradictions, and competing-actor evidence are all evaluated, alternatives are preserved, and original evidence is never rewritten. One actor, several actors, and **unresolved plurality** are all representable. Observations, derived intervals, inferred transitions, estimated dwell times, and unknown gaps are **labelled distinctly**. Externally owned video is **referenced, never copied**, and is never asserted to depict the actor. Later identification is **additive**, preserving the original uncertainty and granting no retroactive permission | An actor or surveillance store independent of governed records; a cross-scope or reusable unknown-actor identity; joining an unknown proximity source and an unmatched voice because they co-occurred; presenting an estimate as a direct observation; implying continuous surveillance from intermittent evidence; describing an unknown actor as a cleaner, contractor, guest, intruder, burglar, or robber without governed evidence; treating an Evidence Package as legal proof | [../models/temporal-record.md](../models/temporal-record.md), [privacy.md](../architecture/privacy.md), [home-assistant-boundary.md](../architecture/home-assistant-boundary.md) |
| **DL-36** | **Identity supplies confidence; the consumer determines sufficiency, and sufficiency is never universal** (P15, DL-06, DL-32). One purpose-specific Identity Assertion is consumed by **four materially distinct evaluations** — the **Identity Presentation Threshold**, the **Capability Access Threshold**, **disclosure evaluation**, and **confirmation** — and satisfying one never satisfies another. **Operational Trust owns all four**, including the presentation threshold, because speaking a name is itself a disclosure. Identity never judges its own sufficiency; Concierge applies presentation and orchestrates confirmation but sets no threshold; Communication, Continuity, and reasoning providers set none. The requirement belongs to **what is being protected** — the capability, the protected resource, the protected operation, or the action-risk class — and attaches to the existing **Authority** state of Existence → Participation → Exposure → Authority. **Read, write, delete, and governance operations are never collapsed into one threshold.** *No identity required* is a legitimate requirement and is **never** an absence of governance. **Presentation is not personalization**: being addressed by name authorises no preference, session, resource, attribution, or learning | One universal confidence threshold, or a general-purpose identity score used as a gate; a threshold owned by Identity, Concierge, Communication, or a provider; presentation treated as access; access treated as personalization; access treated as disclosure; one threshold covering both read and delete; *no identity required* treated as *no policy applies*; a Person preference treated as a permission; a reasoning provider deciding sensitivity | [../models/operational-trust.md](../models/operational-trust.md), [../models/person-and-identity.md](../models/person-and-identity.md), [../contracts/operational-trust-contract.md](../contracts/operational-trust-contract.md), [../contracts/identity-contract.md](../contracts/identity-contract.md) |
| **DL-37** | **A confirmation is a bounded interaction outcome, and never retroactive certainty** (P15, P27, DL-32, DL-34, DL-36). Confirmation is the existing `permitted_with_confirmation` outcome and the existing bounded identity evidence source; **no second confirmation model exists**. **Confirmation Opportunity** — offered instead of refusal when confidence falls short — and **Confirmation Requirement** — demanded regardless of confidence — are different, and both are held by the protected capability or operation. A successful confirmation produces a **separate governed record**; it **never rewrites the provider match, the fused confidence, the evidence, the original assertion, or earlier uncertainty**, and **`Confirmed` is a scoped interaction state, not the top of the confidence scale**. **The capability declares the confirmation strength it requires**, and a spoken *yes* is not adequate for permission changes, enrollment, security configuration, financially consequential action, highly sensitive disclosure, Preservation Hold release, evidence deletion, or administrator changes. Every confirmation is bounded by purpose, capability and operation, interaction, channel, Room, Person, and time — **and never by audience**. `Denied`, `Unclear`, `Cancelled`, `Unavailable`, and `Expired` are first-class outcomes; a denial preserves the original assertion, records the contradiction, and **never silently promotes the next candidate or establishes the stated alternative**. **A confirmation challenge is itself a Communication** and is audience-evaluated before it is spoken | Confirmation rendered as 100 percent, as certainty, or as authentication; an original assertion rewritten or re-scored after confirmation; an unbounded or session-like confirmation; a confirmation for one capability silently covering another; identity or access confirmation treated as disclosure authorisation; a spoken *yes* accepted for every operation; a confirmation mechanism declaring its own sufficiency; `Unclear` or `Expired` treated as `Confirmed`; a denial creating a durable association, training a voice profile, or altering evidence weights; a candidate name announced aloud without audience evaluation | [../models/operational-trust.md](../models/operational-trust.md), [../models/person-and-identity.md](../models/person-and-identity.md), [../models/communication.md](../models/communication.md), [../models/decision-trace.md](../models/decision-trace.md) |
| **DL-38** | **The Identity Fusion Function is deterministic, ordinal, purpose-scoped, and stepped** (P15, P21, P26, P27, P30, DL-06, DL-31, DL-32, DL-33, DL-36, DL-37). Fusion begins with the **assertion purpose** and a **bounded candidate set**; ineligible evidence is **excluded before weighting, never down-weighted**. Nine rules govern the aggregation: **(F1)** each evidence family carries the highest support level it can reach **for that purpose**, and the assertion never exceeds the highest such ceiling; **(F2)** each correlation family yields **exactly one** contribution, and further observations in it may improve observation quality but never become a second confirmation; **(F3)** within a family, each qualification stage — provider match, observation quality, freshness, configured association reliability — may only **lower or hold**, and the four are **never multiplied into one product**; **(F4)** one **anchor family** sets the result and each **additional independent** family raises it by one **bounded step**, never by summation; **(F5)** a source requiring corroboration anchors only to a reduced ceiling; **(F6)** contradiction applies **bounded reduction** against the specific candidate and claim, and is never averaged away; **(F7)** absence is neutral — fewer sources yield a **lower ceiling, never a penalty and never a denominator effect**; **(F8)** `known` requires the leading candidate to reach the purpose minimum **and** satisfy a governed **separation** requirement, otherwise `ambiguous`; **(F9)** the function is **deterministic and monotonic** under a stated **Fusion Policy version**. Outcome selection is **ordered** so `not required`, `unavailable`, `unknown`, `ambiguous`, and `known` cannot blur, and **a weak candidate is never forced**. Freshness requires source- and purpose-specific windows, graduated reduction, and a hard cutoff together; **no duration is prescribed**. The output is an **ordinal support level mapped to a confidence band** through a versioned band map — **the band is authoritative**, a normalised numeric is a deterministic ordering value and **never a probability, likelihood, or measured accuracy**, and **one enumeration serves every purpose**. Every assertion references its **Fusion Policy version**; changes follow the existing promotion ladder and **never recalculate an earlier assertion**. The function is **uncalibrated by construction**, testable through deterministic fixtures requiring no biometric or proximity hardware. **Identity fuses; nobody else does**, and **confirmation is never an input** | Adding, averaging, or multiplying percentages; a weighted average that penalises a household for owning fewer sources; a Bayesian or belief-combination model claiming calibrated probability the home cannot support; treating separate entities or integrations as proof of independence; a native Person counted separately from the trackers producing it; the numerically highest candidate silently selected; a weak known candidate returned instead of Unknown Person; `unavailable` rendered as `unknown`; a consumer re-weighting or recomputing identity evidence; a confirmation fused as certainty; a reasoning provider nominating a candidate; a universal device-type weight; a Fusion Policy changed silently by learning; earlier assertions recalculated under a new policy | [../models/person-and-identity.md](../models/person-and-identity.md), [../contracts/identity-contract.md](../contracts/identity-contract.md), [../models/decision-trace.md](../models/decision-trace.md), [home-assistant-boundary.md](../architecture/home-assistant-boundary.md) |
| **DL-39** | **Identity has exactly four confidence bands; `None` belongs to Operational Trust** (P15, P27, P30, P32, DL-06, DL-32, DL-33, DL-34, DL-36, DL-37, DL-38). A `known` Identity Assertion carries one of **Low < Moderate < High < Very High** — ordered, purpose-specific, produced by **DL-38**, privacy-safe, and describing **only the strength of identity support**. The bands are **ordered**, and the ordering is authoritative; the labels are words because bands are never added, averaged, or treated as a distance, and an ordinal numeral invites exactly that misreading. A band carries **no access, presentation, personalization, disclosure, audience, confirmation, authentication, consequence-class, or sensitivity meaning**, and **Very High is not certainty, confirmation, or authentication**. **`None` is not an Identity band**: it is one of five **Required Identity Band** values — `None`, Low, Moderate, High, Very High — owned by **Operational Trust** and meaning *no known-Person identity is required for this operation*. An operation permitted under `None` is explained as *identity was not required*, **never** as a band exceeding `None`. **State and band are different dimensions**: bands apply only to `known`; `ambiguous`, `unknown`, `unavailable`, and `not required` carry **no band**, and an Unknown Person is assigned neither a band nor `None`. **Operational Trust owns every threshold**, including **Address by Name** — enabled state, minimum current band, neutral fallback, audience evaluation — wherever it is surfaced in configuration; Identity, Concierge, Communication, and Continuity own none. **Access and presentation are evaluated independently from the same assertion and may differ**, and a presentation threshold that is not met produces neutral wording and **never denies the action**. **Every interaction is evaluated from current eligible evidence for the applicable assertion purpose.** HTBW creates **no long-lived Identity session**: continuous Room occupancy is not continuous authentication, and a prior assertion, band, access grant, naming eligibility, or confirmation is **never revived because presence remained active**. **Assertion validity (OD-15) is not current-interaction applicability** — a valid assertion may remain a correct historical record while being inapplicable to a new interaction. **A confirmation is consumed by the protected operation that required it**: no occupancy grace period, no authenticated session, no automatic carry-forward, and **no change to the Identity band**; a bounded multi-step task must state its bound explicitly. Sensor debouncing belongs to evidence freshness under **DL-38** and never becomes an authorisation, presentation, or confirmation lifetime. Decision Trace records **identity result, requirement, access decision, presentation decision, and confirmation** as five separate outcomes | A fifth band called `None`; `None` treated as an Identity output; a band used as a permission, or described as authorising access; a band assigned to `unknown`, `ambiguous`, `unavailable`, or `not required`; `ambiguous` rendered as `Low`; an Unknown Person assigned a band; a threshold owned by Identity, Concierge, or Communication because of where it is configured; an action denied because a presentation threshold was not met; a name spoken from a prior interaction's eligibility; identity preserved by continuous occupancy; a presence-based or grace-period confirmation lifetime; a confirmation treated as an authenticated session or as raising the band; a valid assertion treated as the current-speaker assertion; access and presentation recorded as one outcome | [../models/person-and-identity.md](../models/person-and-identity.md), [../models/operational-trust.md](../models/operational-trust.md), [../contracts/identity-contract.md](../contracts/identity-contract.md), [../contracts/operational-trust-contract.md](../contracts/operational-trust-contract.md), [../models/communication.md](../models/communication.md), [../models/decision-trace.md](../models/decision-trace.md) |
| **DL-40** | **Required Confirmation Strength is an ordered class set; a class is not a mechanism** (P15, P27, P30, DL-32, DL-36, DL-37, DL-39). Operational Trust configures, for each protected operation, a **Required Confirmation Strength** on the ordered set **`None` < Verbal < Authenticated < Strong**, alongside and independent of the **Required Identity Band**. **What separates the classes is independence** — from the evidence that produced the assertion and from the channel that carried the request — **not friction, effort, or ceremony**. **Verbal** is an in-interaction acknowledgement on the channel already in use, and is therefore corroborated by evidence that was already insufficient; **Authenticated** requires a surface carrying a governed authenticated user context; **Strong** requires a factor deliberately independent of both the evidence and the channel. **A strength class is a governance statement, not a platform claim.** A class is satisfied only by a mechanism the deployment has **verified** as meeting it; **no mechanism is prescribed, assumed, or required to exist**, and no mechanism is credited with a class because it feels secure. Where a required class has no verified available mechanism, the confirmation outcome is the existing **`Unavailable`** and the operation is refused or degraded under normal policy — **a required strength is never silently downgraded to a weaker class**. Which class each capability, protected operation, and action-risk class requires is **configuration** resolved with **OD-51**, not architecture. **DL-37 is unchanged and unreopened**: this decision fills the enumeration slot DL-37 explicitly deferred, and every DL-37 rule stands — a confirmation is consumed by the operation that required it, is bounded, **never changes the Identity band**, and a spoken *yes* remains inadequate on its own for permission changes, identity enrollment, security configuration, financially consequential action, highly sensitive disclosure, Preservation Hold release, evidence deletion, and administrator changes | Confirmation strength is a **classification**, not an implementation; naming a required strength is not prescribing a mechanism; an unavailable strength never degrades to a weaker one; a strength class never becomes a second permission system, a second confirmation system, or an authenticated session | [../models/operational-trust.md](../models/operational-trust.md), [../contracts/operational-trust-contract.md](../contracts/operational-trust-contract.md), [../models/glossary.md](../models/glossary.md) |
| **DL-41** | **Capabilities declare dependencies, and a missing dependency disables the capability** (P21, P24, DL-30, DL-36, DL-39, DL-40). Every capability declares the preconditions without which it cannot exist in this home: a **native Home Assistant capability**, an **integration**, a **provider**, **Connected Storage**, **consent**, or **configuration**. Where a declared dependency is missing the capability is **unavailable**, the missing dependency is **named**, and the household is told in a sentence it can act on. **A native Home Assistant capability satisfies a dependency where it fully represents the requirement** (P21, DL-30); an **integration or provider** satisfies a non-native dependency where it is configured, valid, and available, presence in configuration not being sufficient; **Connected Storage** satisfies an artifact or extended-retention dependency; **consent** is an **eligibility** dependency and never a platform dependency; **configuration** satisfies a dependency on a declared setting. **A capability may declare several dependencies**: all **mandatory** dependencies must be satisfied for it to be available, while an unmet **optional** dependency improves quality without ever causing unavailability, and an undeclared load-bearing dependency is a defect. Availability turns on a dependency being **usable, not merely named** — not configured, configured but invalid, configured but currently unavailable, healthy, degraded but usable, and removed are distinguishable states, and a degraded-but-usable dependency is recorded rather than hidden. **HTBW does not emulate a missing dependency** — it does not substitute an approximation, build a local stand-in, or silently reduce the capability to something weaker that shares its name. **Capability unavailable is a dependency outcome, never a trust failure, an identity failure, or a permission failure**; expressing one as the other is a defect in both directions, because a household told it lacks permission when it lacks an integration cannot fix its home, and a genuine refusal dismissed as a setup problem is a safety failure. **Three questions are independent and evaluated in order** — *can this happen at all?* (declared dependencies), *who is this?* (Identity, DL-38 and DL-39), *may this happen?* (Operational Trust, DL-36, DL-39, DL-40). **Dependency is evaluated first**: where a capability is unavailable, identity is not consulted and no requirement is evaluated, and identity is likewise not evaluated where the protected operation requires none. An unavailable capability never lowers a threshold, and a satisfied threshold never conjures a missing dependency. **Five outcomes stay distinct and are never collapsed** — dependency unavailable, identity insufficient, Operational Trust denied, disclosure not appropriate, and runtime failure — each with a different cause, remedy, and explanation; exact wording is not prescribed, but the distinction is required. A Decision Trace records capability availability, the missing dependency, and that identity and requirement were not evaluated. **Truth may establish Facts about dependency health and Repairs may surface a defect, without either becoming the owner of the capability or its dependency declaration**, and **no runtime health protocol is defined**. **This creates no Capability responsibility, no capability registry service, and no dependency broker**; declaring a precondition is a property of a capability, owned by the responsibility that owns it, and the seven responsibilities are unchanged | A dependency failure rendered as a denial or an identity failure; the five outcomes collapsed into one generic failure; a threshold treated as a substitute for a dependency; an emulated, approximated, or silently reduced capability; an undeclared load-bearing dependency; an optional dependency causing unavailability; a dependency treated as present because it is named in configuration; identity evaluated for an unavailable capability, or where the operation requires none; a Capability responsibility, registry, or broker; a dependency evaluated after identity | [../architecture/failure-and-degradation.md](../architecture/failure-and-degradation.md), [../models/operational-trust.md](../models/operational-trust.md), [../contracts/operational-trust-contract.md](../contracts/operational-trust-contract.md), [../models/decision-trace.md](../models/decision-trace.md) |
| **DL-42** | **Home Assistant owns Home Assistant data; Connected Storage is a capability dependency** (P21, P22, P27, P30, DL-30, DL-31, DL-41). **HTBW follows Home Assistant storage, retention, and artifact models by default** and creates no parallel store and no second retention model for information Home Assistant already governs and retains — Recorder history and long-term statistics, entity state and attributes, device state and registry data, Person state and `user_id` linkage, Area membership, floors, labels, aliases, Recorder retention and purge, and native metadata. These are **consumed through the accepted boundary**, not duplicated, and **HTBW builds no second Recorder**. **Duplication requires a documented governed gap, never a preference**: convenience, query shape, performance speculation, and *"it is easier to own it"* are not justifications, **wanting longer retention is not a gap**, and the ordered burden of proof (**DL-30**) applies unchanged. **The presence of Connected Storage transfers no ownership of native data**, and external history is an HTBW **extension** that uses native history as its source while available, never a replacement for it. **Duplication requires a documented governed gap, never a preference**: convenience, query shape, performance speculation, and *"it is easier to own it"* are not justifications, and the ordered burden of proof (**DL-30**) applies unchanged. **Connected Storage is required** wherever HTBW must persist an artifact that does not practically fit a native storage or retention model — asset documents, manuals, invoices, warranty records, voiceprints, materialised evidence packages, preservation and historical-reconstruction artifacts, and future HTBW-generated artifacts. **Without it the dependent capability is unavailable** under **DL-41** — capabilities needing no external artifact remain available — and three failures are prohibited: **no unmanaged local repository**, **no silent scope reduction**, and **no forcing of an artifact into attributes, entity state, or a helper to make it fit**. **Where storage is lost after artifacts exist**, creation and retention extension are **suspended**, persistence is **never claimed**, artifacts are **never recreated elsewhere**, and governed metadata and references are **not deleted merely because storage is temporarily absent** — they resolve to *"unavailable"* rather than *"never existed"*, and the condition is surfaced through the accepted degradation and Repairs surfaces; temporary unavailability and permanent replacement are distinct, and reconciliation mechanics remain an open implementation matter. **Conceptual storage classes are architecture; physical layout is not** — no root, folder, path, or format is accepted here, and technology, encryption, synchronisation, credentials, mount, backup, replication, migration, quota, and recovery tooling remain **OD-02** and **OD-03**, **both since closed by DL-44 and DL-45**. **External History Retention** is a single configured value that is **both the retention window and the purge window** — Disabled by default, in which case HTBW follows Home Assistant retention; where configured, anything older is removed by a **governed recurring purge** and **no separate archive tier is introduced**, with no *"archive after X, purge after Y"* model unless a future decision explicitly governs one. **Purge frequency is not architecture**: the window must be enforced regularly and explainably, but job timing and cadence are implementation choices. The configured period is an **ordinary ceiling, never an authority**: it overrides no retention floor required by **P27**, **a Preservation Hold suspends ordinary purge** for the records it covers, and retention per record class is declared inside the lifecycle under **DL-47**, with four structural floors that survive any configured window. **Changing the configured duration is a governed, historically explainable change**, an earlier decision remains explainable under the setting that applied when it was made, and **reducing the duration never silently deletes held or protected records**. Purge is not silence — a removed record stays distinguishable from one that never existed | A parallel store for natively governed data; a second Recorder; a second purge over native history; duplication justified by convenience or by a wish for longer retention; an unmanaged local fallback when Connected Storage is absent or lost; artifacts silently recreated elsewhere; persistence claimed when a write did not occur; governed metadata deleted because storage is temporarily unavailable; a hardcoded storage path treated as accepted architecture; a purge cadence treated as architecture; an archive tier created because data is old; a configured window treated as authority over a retention floor or a Preservation Hold; a reduced window applied as a bulk erasure; storage unavailability rendered as a refusal | [../architecture/connected-storage.md](../architecture/connected-storage.md), [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md), [../architecture/failure-and-degradation.md](../architecture/failure-and-degradation.md) |
| **DL-43** | **No externally stored artifact exists without a documented lifecycle** (P21, P22, P27, DL-30, DL-41, DL-42). Every artifact class stored outside Home Assistant declares, **before it is introduced**, its **Artifact Type; owning responsibility; creating capability; required dependency; storage class** (a governed class, **not a physical path**); **anchor** to a native object or governed record; **retention strategy; deletion trigger; consent effect; Preservation Hold effect; behaviour when Connected Storage is unavailable; behaviour when storage is lost after creation; historical and explainability requirements (P27); access restrictions**; and, where applicable, **integrity or version requirements** and **recovery or reconciliation behaviour**. A retention strategy need not be a duration — *"retained while the anchor asset exists"* is a complete answer — but **"undecided" is not**, and an artifact whose retention or deletion strategy is unstated **must not be created**. **Artifact classes do not share one retention strategy**, and none is imposed on them. The accepted strategies are: **asset documents**, owned by **Foundation** which owns the Asset and its documentation anchor — **Stewardship owns significance and care, not the document artifact** — retained while the anchor Asset exists, deleted when the Asset is removed or the resident explicitly removes the document, with **no ordinary age-based purge** and unreachable documentation reported as **unavailable** rather than absent; **voice enrollment samples**, owned by **Identity**, temporary with zero default retention, removed on success and on cancellation, failure cleanup, consent withdrawal, or policy expiry, and **never becoming historical identity evidence merely because they existed**; **voiceprints and derived identity profiles**, owned by **Identity**, retained while the governed profile remains enabled **and consent remains valid**, deleted on profile removal or **consent withdrawal** — revocation removing the derived profile and its associations rather than merely their use — with biometric internals including **storage paths** never exposed, and **deletion of a voiceprint never rewriting an earlier Identity Assertion**; **extended historical records** governed by External History Retention under **DL-42**; **Preservation Hold** a marker or state on governed records and **not an artifact class of its own**, so duplicating payloads to satisfy a hold remains prohibited, **releasing a hold does not itself delete anything** but restores ordinary retention, and release remains **OD-39**; **Historical Reconstruction** a projection that is never retained, creating **no persistent reconstruction store by implication**; **Evidence Package** a projection assembled on demand and **not retained by default**, so only a deliberately materialised copy becomes an artifact and must then declare its own lifecycle, access, and preservation behaviour in its own right — **retention never making it legal proof** — with assembly, transport, integrity, and audience remaining **OD-40**. Consent and Preservation Hold both act on deletion and are evaluated before it — consent withdrawal **causes** deletion, a hold **defers** it — and their reconciliation with retention floors remains **OD-36**. Every future artifact proposal answers the artifact review checklist, and an unanswered question is an unmet burden of proof. **This creates no artifact registry and no artifact service**; the declaration lives with the architecture of the artifact class, owned by the responsibility that owns the artifact, and **physical storage owns nothing** | An artifact introduced without its declarations; an undeclared lifecycle treated as a permissive default; one retention strategy imposed across artifact classes; an ordinary age-based purge of asset documents; voice samples retained after enrollment completes, or treated as historical identity evidence; consent withdrawal treated as a visibility change; voiceprint deletion rewriting an earlier Identity Assertion; a Preservation Hold artifact class; a persisted Evidence Package or Historical Reconstruction store; an artifact registry or artifact service | [../architecture/connected-storage.md](../architecture/connected-storage.md), [../patterns/temporary-artifact-lifecycle-pattern.md](../patterns/temporary-artifact-lifecycle-pattern.md), [../architecture/privacy.md](../architecture/privacy.md), [../models/glossary.md](../models/glossary.md) |
| **DL-44** | **Home Assistant is the storage provider; Connected Storage is persistence, not an access surface** (P21, P22, P23, DL-30, DL-41, DL-42, DL-43). HTBW uses the connected storage Home Assistant already provides and **owns nothing beneath it**: not protocol selection between NFS and CIFS, not share mounting, not network credentials, not server discovery, not host mount configuration, and not general network-storage administration. Those belong to **Home Assistant or the deployment**; HTBW's ownership begins only once a valid storage dependency has been made available, and covers what HTBW puts there and how it governs it. **Connected Storage provides persistence; HTBW provides every governed interaction with the artifact.** Residents never require filesystem navigation to use an HTBW feature: they interact with the **Asset** and its document list, with the **enrollment session** and **voice profile**, and with **a question** about what happened — never with a storage hierarchy. The namespace is **not a resident file browser, not a second Home Assistant UI, not a generic document-management system, not an alternative media library, and not a direct authorisation surface**. **Media-browser exposure is a visibility boundary, never the sole security or authorisation control**: Home Assistant documentation establishes that media directories are protected by **authentication**, not by per-person authorisation, and establishes nothing about a file type being unreachable by every path, so sensitive internal artifacts — voiceprints, temporary samples, governed history — are **not exposed as resident media** absent a separately accepted requirement, and **HTBW, Operational Trust, privacy, and consent remain the security boundary**. HTBW requires **one governed namespace** with **separation by artifact-owning function or artifact class, collision-resistant governing-object references, no resident-supplied path as the authoritative identifier, no display name as the only storage key, traceability to the governing object, no cross-capability artifact mixing, removable empty structures, and migration through governed references rather than hardcoded user-facing paths**. Exact root and folder names, path depth, separators, and file naming are **implementation mapping** unless a stated interoperability requirement makes one architectural, and **a new branch is introduced only when an accepted capability declares an artifact class under DL-43**. Artifacts are located through a **governed reference**, never through a typed path or a chosen name; native registry properties are **not copied into the reference** merely to populate it; and **physical storage paths are not exposed** through ordinary UI, diagnostics, Repairs, or service responses where a governed identifier suffices. **File formats remain capability-specific and no universal payload schema is imposed.** Every artifact class declares one **interaction model** — **Managed Content**, **Internal Runtime Artifact**, or **Queryable Historical Record** — which classifies governed operations and resident visibility without replacing the DL-43 lifecycle declaration. **This creates no Storage, Artifact, Repository, Capability, or Dependency responsibility**; Connected Storage remains an architectural boundary and a capability dependency, and the seven responsibilities are unchanged | HTBW selecting or managing a storage protocol, mount, or credential; a generic resident file browser; storage treated as an authorisation surface; My Media visibility treated as a security control; an internal runtime artifact exposed as resident media for convenience; a resident-supplied path or display name used as the authoritative identifier; a physical path exposed as a public identifier; native registry properties copied into an artifact reference; a universal payload schema imposed across capabilities; folders reserved for capabilities that do not exist; a Storage, Artifact, or Repository responsibility | [../architecture/connected-storage.md](../architecture/connected-storage.md), [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md), [../architecture/privacy.md](../architecture/privacy.md), [../models/asset.md](../models/asset.md) |
| **DL-45** | **Every artifact declares a governing parent, and parent removal cleans up** (P21, P27, DL-41, DL-42, DL-43, DL-44). Every externally stored artifact declares a **governing parent object** and a **Parent Removal Behavior**. **The ordinary default is cleanup when the parent disappears; continued existence requires an explicit accepted reason.** On removal HTBW identifies dependent artifacts and references, evaluates Preservation Holds, retention floors, consent rules, and other lifecycle constraints, deletes artifacts no longer governed by a valid requirement, removes dependent references, removes empty capability-owned structures, preserves required Tombstones, Change Records, Decision Traces, and lifecycle evidence, reports failures through Repairs or accepted degradation, **never claims cleanup succeeded while storage was unavailable**, and reconciles incomplete cleanup once the dependency returns. **Cleanup never silently overrides** a Preservation Hold, a retention floor, an Evidence Package lifecycle, or historical explainability. **Retention and parent cleanup are distinct mechanisms**: time-window purge does not substitute for parent-object cleanup, parent-object cleanup does not substitute for time-window purge, and an object-scoped record class may be subject to both. **Native Home Assistant objects follow their own lifecycle** and are never deleted because an HTBW artifact structure was cleaned. Per class: deleting an **Asset** enumerates its artifact references, deletes every document without an overriding retention or preservation rule, removes empty Asset structures, surfaces cleanup failure, and **is not reported complete while mandatory cleanup remains unresolved** unless the accepted lifecycle supports a pending-cleanup state, with historical governance records permitted to remain but **never retaining the document payload without authority**; deleting a **single Asset document** removes the artifact, removes or tombstones its reference, may remove empty structures, and **leaves the Asset**; **voice enrollment success** removes temporary recordings and working artifacts and **does not claim a voiceprint successfully complete while mandatory sample cleanup is outstanding** unless the accepted model distinguishes generated from cleanup-complete; **cancellation or failure** leaves **no unmanaged recording and claims no voiceprint**; **voice profile deletion** removes voiceprint and derived artifacts and **leaves earlier Identity Assertions historically unchanged**; **Person deletion** evaluates every Person-governed voice profile and artifact so that **no orphan profile remains**, with consent and historical governance records following their own lifecycle. **No Room artifact class is created here**; if a future accepted capability introduces Room-scoped artifacts, its declaration states Room Parent Removal Behavior, artifacts shared with another valid governing object are **not** deleted because one Room disappeared, and merged-Room ownership is resolved before deletion. **Where storage is unavailable during cleanup the obligation is preserved, not discarded**: deletion is not claimed, a governed pending-cleanup state is retained under the existing reconciliation model, the reference is not silently discarded, the artifact is not recreated elsewhere, and the condition is surfaced; **retry and reconciliation timing are implementation mapping**, and reconciliation against floors and holds is owned by **OD-36** without a new decision | An artifact without a declared governing parent or Parent Removal Behavior; an orphan artifact surviving its parent by default; a voice profile surviving its Person; cleanup that silently overrides a hold or a retention floor; cleanup reported successful while storage was unavailable; a discarded reference converting a pending obligation into an orphan; a native object deleted because an artifact folder was cleaned; time-window purge substituted for parent cleanup, or the reverse; a Room artifact class invented to satisfy a future rule | [../architecture/connected-storage.md](../architecture/connected-storage.md), [../architecture/failure-and-degradation.md](../architecture/failure-and-degradation.md), [../models/asset.md](../models/asset.md), [../models/person-and-identity.md](../models/person-and-identity.md) |
| **DL-46** | **Home Assistant retains native activity; HTBW retains the governed meaning Home Assistant does not represent** (P8, P21, P27, P28, P30, DL-04, DL-31, DL-42). Home Assistant remains authoritative for entity and device states, state changes, native events, occupancy and motion state, media-player state, Person and Device Tracker state, natively provided automation and script activity, and Recorder history. **HTBW consumes these by governed reference and persists no second copy merely to explain a decision later.** What HTBW persists is what the platform does not naturally represent: **purpose-specific Identity Assertions, safe identity-evidence summaries, Decision Traces, Operational Trust evaluations, policy outcomes, attribution, explicit Change Records, capability-dependency outcomes, audience and disclosure outcomes, governed non-actions, reason codes, historical policy and Fusion Policy versions, cleanup obligations, Tombstones, and broken-reference state**. **The Decision Trace is the canonical explainability spine**, linking trigger or request, relevant Facts, Identity Assertion, capability availability, Operational Trust evaluation, conflicts and alternatives, decision, action or non-action, observed outcome, and resident-safe explanation. It **references rather than copies** (P30), and **no second explainability model, reasoning record, or parallel decision history is created beside it**. **A longer HTBW retention requirement is never authority to copy native history**: HTBW does not retain every state transition, Recorder row, automation trace, sensor payload, voice interaction, or provider response, and any native payload copied into HTBW storage requires a separately documented governed gap and its own lifecycle. **Durable explanation after native expiry is already provided and requires no new construct**: the accepted Fact that Truth recorded — its Subject, Statement, confidence at the time, Provenance, evidence references or classes, Coverage, and Freshness — is the bounded summary, and it is **material to the decision, never a copied Recorder row**; a purged native reference resolves to *"no longer retained"*, never *"never existed"*. **Significance is already settled and creates no new owner**: a Decision Trace records an **HTBW decision evaluation**, not an occurrence, so a native state change with no HTBW decision produces no trace, an occurrence is evidence for an explanation rather than a trace of its own, and **HTBW never produces a Decision Trace for a decision HTBW did not make**. **Explainability is a governed record, never a reasoning log**: HTBW must not persist private chain-of-thought, hidden prompts, unrestricted model reasoning, raw provider deliberation, provider secrets, biometric internals, voiceprint vectors or embeddings, raw voice recordings, unnecessary conversation transcript, or unnecessary raw sensor payloads, and **the explanation must remain truthful after every sensitive detail is redacted**. Where identity was **not required**, the trace states that plainly and **never implies that identity authorised the operation**, while remaining free to record that identity supported attribution or named presentation. **This creates no History, Explainability, Persistence, Audit, or Activity responsibility, no generic event warehouse, and no second Recorder** | Copying native state history so HTBW can retain it longer; a second Recorder, event warehouse, or parallel decision history; a new Reasoning Record beside the Decision Trace; persisted chain-of-thought, embeddings, or raw samples; a Decision Trace for an occurrence HTBW did not decide; a trace claiming identity authorised an operation that required none; a purged reference rendered as though nothing happened; a bounded Fact summary widened into a Recorder replica; a History, Explainability, or Persistence responsibility | [../architecture/explainability.md](../architecture/explainability.md), [../models/decision-trace.md](../models/decision-trace.md), [../models/temporal-record.md](../models/temporal-record.md), [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md) |
| **DL-47** | **Every governed record class declares its retention, exactly as every artifact class does** (P1, P27, P28, DL-42, DL-43, DL-45, DL-46). DL-43 required a declared lifecycle before an **artifact** could exist; the same rule now binds every **governed record class**, whether it is held in Home Assistant or in Connected Storage. **A record class whose retention is unstated must not be accepted**, *"undecided"* is not a retention strategy, and **one retention rule is not imposed across classes**. The accepted rules are: a **Current Projection** lives while its object lives and is replaced rather than retained; a **Change Record** is retained under the lifecycle of the governed object it describes, and under External History Retention where it is externally held, carrying its own **Retention Classification**; a **Domain Event** follows External History Retention; a **Snapshot** is an accelerator and **is retained no longer than the records it summarises**, never outliving the change history it accelerates; a **Decision Trace** is governed explainability history and follows **External History Retention** unless an accepted floor or a Preservation Hold applies, and **holding a trace preserves the governed source versions required to keep it explainable** rather than duplicating their payloads; a **Historical Fact** is Truth-owned governed history following External History Retention, with per-Fact-class differentiation an **Operational Trust policy matter, not architecture**; a persisted **Identity Assertion** is retained **with the Decision Trace or governed history it supports**, never under a separate universal duration and never as a licence to retain biometric internals; **Communication** records follow the same rule with content and metadata classified separately (**OD-49**); **Preservation Hold** metadata follows hold governance and **is not removed by ordinary purge, because a purge that erases the proof of the hold defeats the hold**; a **Tombstone** outlives the record it marks, for the same reason; **saved Evidence Packages and saved Historical Reconstructions** take their own artifact lifecycle under DL-43, while unsaved ones are projections that retain nothing. **Four structural floors survive any configured window**: Tombstones, consent-lifecycle records, records under Preservation Hold, and the governed versions required to keep a held Decision Trace explainable. **External History Retention is the ceiling and the purge boundary; it overrides no floor and no hold.** Everything remaining is a **household configuration value, not architecture** — the numeric floor and ceiling per class, the trace floor (**OD-05**), the experience-history question (**OD-26**), and the communication content-versus-metadata classification (**OD-49**) — and **no universal retention matrix is required, because retention is declared inside every lifecycle**. **This creates no retention registry, no retention service, and no central purge owner**; each responsibility enforces retention over its own records | A governed record class accepted without a declared retention; an undeclared retention treated as a permissive default; one retention rule imposed across every class; a Snapshot outliving the Change Records it summarises; an Identity Assertion retained on its own universal clock; Preservation Hold metadata or a Tombstone removed by ordinary purge; a configured window overriding a floor or a hold; a retention registry, retention service, or central purge owner; a universal retention matrix rebuilt outside the lifecycle declarations | [../models/temporal-record.md](../models/temporal-record.md), [../models/operational-trust.md](../models/operational-trust.md), [../architecture/privacy.md](../architecture/privacy.md), [../models/truth.md](../models/truth.md) |

| **DL-48** | **Obligation condition and obligation lifecycle are orthogonal, and closure requires evidence** (P21, P26, P27, P28, DL-15, DL-26, DL-27, DL-46, DL-47). An obligation carries **two independent fields**. Its **condition state** answers *what is true of the world relative to the care expectation* and remains exactly the accepted six — `met`, `due`, `unmet`, `overdue`, `waived`, `unknown`. Its **lifecycle state** answers *what has happened to the obligation record itself* and is `raised`, `active`, `deferred`, `closed`, `reopened`. **Deferral and closure are removed from the condition set and may never be added to it**, which resolves the defect this was raised on: the Stewardship history description named two lifecycle outcomes as though they were states. **Every lifecycle transition is a Change Record written at the moment of transition** (**DL-26**), never derived later by comparing stored payloads, carrying actor, recorded time, effective time where it differs, reason where supplied, and **version-pinned references** to the care expectation evaluated against (**P30**, **DL-27**). **One new record class is accepted — the Care Evidence Record** — which is what closes an obligation and which declares its own **Retention Classification** under **DL-47**. It carries exactly one evidence kind: `observed`, where Truth established that the condition resolved; `attested`, where a person with accountability recorded that care occurred and Truth cannot observe it; `performed`, where an executor reported completion **and** Truth or an attestation confirms the outcome; or `waived`, a household decision that closes the obligation **without asserting that care occurred**. **An executor reporting success is not closure**, and neither is a dismissed reminder, a ticked projection, or a requested action. **`unknown` is never `met`** and **absence of evidence is never compliance**. A **reopened** obligation retains its identity so a repeatedly unmet obligation stays reportable as a pattern. **Grouping of simultaneous obligations is a projection concern and is not part of the obligation model** (**OD-23**). **A satisfied-without-action obligation is now distinguishable from a performed one** by its evidence kind | Deferral and closure as condition states; closure by dismissal, tick, request, or executor report; snapshot comparison to discover lifecycle change | [../models/stewardship.md](../models/stewardship.md), [../contracts/stewardship-contract.md](../contracts/stewardship-contract.md), [../models/temporal-record.md](../models/temporal-record.md) |
| **DL-49** | **Custody is a time-bounded accountability record owned by Stewardship, and is neither ownership, nor caretaking, nor location** (P21, DL-07, DL-08, DL-26, DL-27, DL-45, DL-46, DL-47, DL-48). A **Custody Period** records **who is accountable for a subject, for a bounded time**, carrying the custodian designation, the declared custody location context, an agreement reference where one exists, the party bearing insurance responsibility for the period, the begin time, the expected end time where agreed, the actual end time on closure, purpose, and notes. **Foundation defines the object type and continues to own the Asset, the `owner-of` and `caretaker-of` relationship types, and the `located-in` declared location; Stewardship owns the Custody Period record, its lifecycle, and its history**, because a custody period must consume Truth and must produce obligations, and dependency-view rule 6 forbids Foundation from consuming anything. **No new Foundation relationship type is created**: `owner-of` and `caretaker-of` are **durable**, custody is **episodic**, and episodic accountability belongs on a time-bounded record rather than in a standing relationship set — whether a role-bearing construct later supersedes this remains **OD-77**, which this decision neither expands nor resolves. **The custodian designation may be a governed reference to an existing Foundation object or free text**, and free text is preserved verbatim in history with the actor who recorded it. **A Custody Period opens on a recorded Check-Out and closes only on a recorded Check-In**; physical return is a Truth Location Fact and is **evidence toward** closure, never closure itself, because Truth can establish where something is and cannot establish that an accountability period has been accounted for. **A custody transfer changes the accountable party, the declared custody location context, and insurance responsibility for the period. It does not change ownership, the asset's declared `located-in` home, its observed current location, or its significance.** **HTBW does not adopt a fixed custody-status enumeration as canonical**, and a Custody Period instead carries a governed lifecycle of `opened`, `updated`, `closed`, `corrected`, and `adversely_resolved`, each transition written as a Change Record. The current custodian is the open Custody Period, or the household by default — **and the absence of an open period is a statement about accountability only, never about location: on-site status requires a Truth Location Fact or Foundation's declared `located-in`, and is never inferred from ownership or from the absence of a custody record.** **In transit and in storage are Custody Periods whose custodian is the carrier or the storage provider**, not separate states, which lets a household record every leg or none — and **no unrecorded leg is ever inferred**. **Overdue is not a custody state**: an expected end time that passes leaves custody unchanged and the period open, and changes only the obligation that expectation created. **Lost and stolen are not custody states and are never custodians**; they are coordinated outcomes in which Truth reports location `unknown`, the Custody Period ends `adversely_resolved` with a recorded disposition **while preserving the last known custodian**, Stewardship raises the resulting obligations, Operational Trust may authorise a **Preservation Hold**, and a declaration of theft is recorded with provenance rather than inferred — and an adverse resolution **never satisfies** the return obligation, which closes only by a Care Evidence Record of kind `waived`. **Condition evidence, photographs, appraisals, conservator and repair reports, contracts, and insurance material are Asset documents under the Asset as governing parent** (**DL-45**), referenced from the custody record by **version-pinned governed reference and never copied into it** (**DL-27**, **P30**) | Custody as ownership, as current location, or as an enumerated state machine; overdue, lost, or stolen as custody states; a first-class Counterparty object; document payloads duplicated into custody records; inferred chain-of-custody legs | [../models/stewardship.md](../models/stewardship.md), [../contracts/stewardship-contract.md](../contracts/stewardship-contract.md), [../models/asset.md](../models/asset.md), [../contracts/foundation-contract.md](../contracts/foundation-contract.md), [../models/glossary.md](../models/glossary.md) |
| **DL-50** | **A capability may declare an execution host, and a voice provider reports candidates that Identity alone resolves** (P21, P25, DL-05, DL-06, DL-30, DL-32, DL-33, DL-36, DL-38, DL-39, DL-41, DL-43, DL-44, DL-47). **An HTBW capability that cannot execute inside the Home Assistant integration process may declare an execution host**, named in the capability's dependency declaration and in the Decision Trace exactly as any other dependency is. **The rule is a per-capability declared host; a Home Assistant app is the reference deployment and not the architecture** — because **P25** keeps Home Assistant the first implementation environment and not a constraint, and apps exist only on some installation types, so **no answer may bind HTBW to one deployment topology**. Refusing a host outright was rejected as a large capability loss taken by omission; a household-provided external service remains **permitted** as a declared host and engages **OD-07** and consent rather than being foreclosed; native-only was rejected because it would have removed voice evidence entirely on the verified host. **One conformance rule is recorded verbatim: a hard manifest `requirements` entry is an all-or-nothing gate for the entire integration, so a dependency that is optional to a capability must not be declared there, or a degraded capability becomes a total setup failure.** **DL-41 applies unchanged**: a host that is missing, unreachable, or incompatible makes the capability **unavailable and names why**, with **no approximation, no substitution, no local stand-in, and no silent reduction to something weaker sharing its name**, and **capability unavailable is never expressed as a trust failure, an identity failure, or a permission failure**. **An execution host is not a third-party engine that decides and acts** — it decides nothing, every decision remains with the responsibility that owns it, and delegation therefore remains **OD-66** and is not resolved here; **data residency remains OD-07** and is not resolved here; and **HTBW acquires no host operating-system administration**, consistent with the storage boundary. **The Wyoming protocol is the preferred voice-pipeline interoperability boundary** wherever HTBW requires runtime audio, discharging the **DL-30** burden at step 2 as an existing maintained ecosystem capability; **Wyoming is a protocol and never an HTBW component**, and **no third-party voice project becomes a mandatory HTBW dependency**. **Providers produce evidence and HTBW produces decisions**: a voice provider emits an **unbound Voice Evidence Record** carrying an **ordered candidate list with a provider-reported score for each candidate**, separation data, ambiguity indicators, quality and channel metadata, and **encoder family, encoder version, and audio-contract version**, and it resolves **no person**, emits **no confidence band**, produces **no fused confidence**, reaches **no threshold verdict**, and authorises **nothing** — **a provider match value is retained as reported and is never rewritten as fused confidence**, and a provider value is **meaningful only within its own provider**, never compared across providers and never rendered to the household. **Compatibility is enforced before comparison and never warned about afterwards**, an incompatible gallery is an explicit **DL-41** outcome, and a model upgrade requires a governed migration path rather than a documented instruction to re-enroll. **Speaker evidence is enrichment and never a gate**: a non-match, an unknown speaker, an unavailable host, or an incompatible gallery **never suppresses the transcript**, `unknown` is never reported as `unavailable`, and **identity never travels inside transcript content** in any form, because an assertion placed in a content field is logged, retained, and passed onward with no audience evaluation. **Region-level matching is a provider capability and never an Identity decision**; **speaker-conditioned audio extraction is validation-required and is not accepted behaviour**; **passive conversation-state evidence is a North Star and no implementation is authorised**; and **raw rejected-audio retention is not enabled by default and requires a declared purpose, duration, access controls, deletion behaviour, consent and privacy review, and a DL-43 artifact declaration before it exists**. **No new responsibility, record class, artifact class, retention rule, threshold, or confidence representation is created by this decision, and no add-on, container, runtime, model, or vendor is selected by it** | Every **DL-30** rung implicitly assuming execution inside the integration process; apps addressed **only** as third-party engines that decide and act; a single-winner provider match treated as an identity answer; a provider-emitted confidence band; a universal provider confidence threshold | [adr-wyoming-compatible-voice-evidence-runtime.md](../architecture/adr-wyoming-compatible-voice-evidence-runtime.md) |
| **DL-51** | **Product disposition is stated per product, never for the portfolio** (P21, P25, DL-05, DL-07, DL-08, DL-19). **Asset Intelligence remains a released standalone integration** with its own lifecycle, existing installations continue to function, and **it is not retired**; HTBW **absorbs equivalent functionality directly**, and **HTBW must never require Asset Intelligence to be installed** — it is never a prerequisite, never a mandatory DL-41 dependency, and never a condition of any resident-facing outcome. **Voice Identity functionality is absorbed into HTBW and the standalone integration will sunset**, with Identity remaining a first-class HTBW responsibility and the published v0.1.0 artifact carrying a **stated disposition** rather than being silently abandoned; the premise that it has no installed footprint is recorded as an **assumption about installs, not a fact about artifacts**. **Concierge functionality is absorbed into HTBW and the standalone integration will sunset**, with Concierge remaining a first-class HTBW responsibility. **The responsibility and the product are separable and this decision depends on that separation**: a responsibility may be first-class inside HTBW while its released product continues, and a product may sunset while its responsibility is unchanged. **Absorbing functionality is not adopting a schema**, and **DL-19 is unchanged** — no compatibility requirement flows upward from any of the three into HTBW Core, sunset or retained. The non-negotiable constraint in authority-order.md is **amended, never deleted**, and the flattening of three products into one class is corrected as the defect it was | One disposition asserted for three products; a product statement read as a responsibility statement, or the reverse; sunset treated as permission to inherit the sunsetting product's defects; retirement of Asset Intelligence; any resident-facing capability made conditional on Asset Intelligence being installed | [adr-product-disposition-and-legacy-adoption.md](../architecture/adr-product-disposition-and-legacy-adoption.md) |
| **DL-52** | **Adoption is one-time, authoritative, and terminating** (P15, P27, P28, P30, DL-19, DL-26, DL-31, DL-41, DL-45, DL-48, DL-49). HTBW supports an **Asset Intelligence Adoption experience whose purpose is preserving resident investment**: **a resident's investment in describing their household survives the transition**, and HTBW does not require a resident to recreate information that already exists. Adoption is a **bounded, resident-initiated act that completes and does not recur**; it creates **no declared capability dependency**, so **HTBW continues to function if the source product is removed**; it is **one-way with no write-back and no synchronisation loop**; **HTBW becomes authoritative for adopted records** and authority does not remain shared; and **every adopted record carries provenance naming the source product and its exact version**. The greenfield ambiguity is **resolved in favour of the bounded reading** — the migration-adapter prohibition targets compatibility **as a constraint on HTBW Core design** and **implicit** obligations, and an explicit, optional, one-way, terminating adoption that constrains no HTBW model is outside it, because **adoption maps into HTBW's own accepted models and reports unmappable content as *not adopted***. **Adopted history is not HTBW history**: relationships and limits transfer as **declarations**, service and maintenance records become **Care Evidence Records of kind `attested` and never `observed`**, custody history becomes a **Custody Period**, change history becomes **Change Records** with rewritten provenance, and **observational history never becomes a Truth Fact or Historical Fact**, because a Historical Fact carries confidence at the time, provenance, coverage, freshness, and a lifecycle HTBW never executed. **A default the household never saw is not a declaration**, so shipped defaults and profile constants are not adopted as declarations. Adoption is a **bulk authority transfer over household records and not a configuration action**: **Operational Trust authorises it**, it **produces a Decision Trace** recording what was offered, adopted, skipped, and unmappable, **`Skip` and partial adoption are first-class outcomes**, and adoption is **idempotent**. **Native objects are referenced and never copied (DL-31)**, while the source product's **private store is copied once with lineage**, because a Governed Reference cannot survive removal of its referent and a reference-only adoption would leave a household with broken references where their data used to be | Continuous synchronisation; write-back to the source product; adoption as a runtime dependency; shared or ambiguous authority after adoption; adopted observations published as Truth Facts or Historical Facts; adopted care records recorded as `observed`; an HTBW model shaped by the source product's storage; adoption performed without authorisation, without a trace, or without provenance; a second Recorder or parallel history | [adr-product-disposition-and-legacy-adoption.md](../architecture/adr-product-disposition-and-legacy-adoption.md) |
| **DL-53** | **A Delivery Surface declares capability dimensions and Potential Perceptibility, and never declares itself private** (P21, P30, P32, DL-28, DL-29, DL-34, DL-37, DL-40, DL-41, DL-44). A Delivery Surface declares seven **capability dimensions** — Supported Modalities, Content Constraints, Interactivity Capability, Persistence Behavior, Recipient Acknowledgement Capability, **Presentation Attestation Capability** (defaulting to **Unsupported**, so `Presented` is recorded as **unknown** and never decays into *not presented*), and **Recipient Attribution Capability** — plus a **Potential Perceptibility** declaration, extensible and never a closed device, domain, or integration list. **No device type, integration type, authentication state, media-browser visibility, or dashboard-view display toggle is sufficient evidence that a surface is private**, and **a portable surface receives no automatic privacy classification**. Foundation owns the capability model and schema; the integration declares verified technical characteristics; the household declares contextual perceptibility and may configure evidence combinations within platform constraints; Truth supplies current facts; Operational Trust owns the disclosure-risk determination; Concierge selects the Delivery Target and performs the attempt. Where Operational Trust finds audience certainty, attribution, or disclosure insufficient, it confirms at the **Required Confirmation Strength** the protected content requires (**DL-40**), moves confirmation to a capable surface, degrades to a compliant delivery or indication, or fails safely and names the reason — **reusing DL-37 and DL-40 rather than a second assurance scale**. Recipient Attribution Capability declares what evidence a surface can contribute; it is never itself a confirmation-strength or confidence scale. The mechanism resolving Room Context for a non-room-bound surface remains **OD-73**, which this decision depends on and does not preempt | A closed device catalogue as the capability model; a surface declared private by device type, authentication, or visibility toggle; a fixed content-to-surface mapping; a fourth confirmation/assurance scale duplicating DL-40; Foundation evaluating runtime Truth to resolve perceptibility | [adr-resident-communication-and-delivery-separation.md](../architecture/adr-resident-communication-and-delivery-separation.md) |
| **DL-54** | **Presentation is a technical claim distinct from Delivery, Perception, Acknowledgement, and outcome satisfaction; its outcome is exactly Presented, Failed, Unknown, or Attestation Unavailable** (P15, DL-30, DL-41, DL-53). A Delivery Attempt's Presentation Outcome is evaluated by the **modality and evidence actually returned**, never by device type, vendor, integration name, or Home Assistant entity domain. **Attestation Unavailable** is a capability fact (the surface's Presentation Attestation Capability is Unsupported, per **DL-53**); **Unknown** is a per-attempt evidentiary gap on a surface that can sometimes attest; neither decays into **Failed** or "not presented", and a successful service call alone is never evidence of **Presented** — only an independently observed platform state transition is admitted. Empty-room audio may be technically **Presented** while human Perception remains **Unknown**; the two are never conflated in either direction. A known **Failed** presentation enters the existing graceful-degradation governance, preserving the original failure alongside any compliant fallback; an **Unknown** outcome passes forward unrewritten into any required acknowledgement stage, and a later acknowledgement is additive evidence that never rewrites the historical Presentation Outcome | Presentation inferred from a successful service call or from `Delivered`; Attestation Unavailable and Unknown collapsed into one value; a device domain or vendor used to determine presentation capability; empty-room playback equated with perception, or Presentation forced to Unknown merely because Perception is Unknown; Unknown auto-triggering failure, retry, escalation, or suppression | [adr-resident-communication-and-delivery-separation.md](../architecture/adr-resident-communication-and-delivery-separation.md) |
| **DL-55** | **Explicit Room Configuration participation already selects the execution provider; the Asset model already anchors endpoint identity across providers; a Room-defined multi-endpoint outcome is a narrow projection over DL-54, never a replacement for it** (P21, DL-09, DL-31, DL-41, DL-53, DL-54). Where one physical endpoint is represented by more than one technical provider, **Room Configuration's existing rule that a participating target is identified explicitly** (a concrete native reference, never an abstract capability class) already resolves which provider executes; **no separate runtime provider-precedence mechanism is required for execution**. A provider whose entity was not selected may still contribute identity, capability, or connectivity evidence through Truth, but never becomes a competing execution or attestation authority for that participating target. **Endpoint identity across multiple provider records for one physical thing is the existing Asset model's concern** where the household has declared an Asset (one Asset may be represented by several Devices); where no Asset is declared, the participating target's own native reference is a sufficient anchor, and matching by name, room, IP address, vendor, or product type is never required or permitted. **A Room-defined outcome spanning several participating endpoints carries its own room-level Presentation Outcome**: `Presented` where at least one participating endpoint achieved `Presented`, carrying a **Degraded** quality label when any did not, with every endpoint-level DL-54 outcome remaining individually visible — never averaged, scored, or collapsed into a single room-health value. **Device interaction capability and workflow participation remain independently declared per surface under DL-53** — a presentation surface needs no acknowledgement capability of its own, and a workflow may obtain confirmation on a different surface or channel (**DL-37**, **DL-40**). **Capability evolution is unchanged DL-41 and Room Configuration behaviour**: a capability that disappears is a broken or degraded participation reference, reported and never silently substituted, and household intent is preserved throughout. **Room Configuration's experience-endpoint category set (music, video, announcement, conversation) is confirmed as the existing, extensible presentation-purpose vocabulary** — no Presentation Grid or capability-discovery authority is created | A runtime provider-precedence mechanism invented where explicit participation already selects the provider; a new endpoint-identity construct where the Asset model already anchors one; a room-level outcome expressed as a health score, percentage, or new authority replacing DL-54; a presentation surface assumed to carry acknowledgement capability; a new capability-discovery or Presentation Grid responsibility | [../models/room-configuration.md](../models/room-configuration.md), [../architecture/failure-and-degradation.md](../architecture/failure-and-degradation.md), [../models/asset.md](../models/asset.md) |
| **DL-56** | **Consent is required for person association and person-scoped participation, never for environmental observation by itself; the household-facing experience is participation-based, the canonical record beneath it is precise** (P15, P21, DL-18, DL-31, DL-33, DL-38, DL-41, DL-43, DL-47). **Observation is not Person Association**: a camera image containing a person, motion, occupancy, a BLE device's presence, or an unidentified interaction requires no person-association consent; correlation capability is never itself authorization. Consent is required only to **associate** an observation, a voiceprint, a BLE/phone/watch device, or an authenticated session with a named Person, or to perform person-scoped learning, personalization, or Stewardship. **Person Setup is the primary consent capture and review experience**, coordinating with, never duplicating, native Home Assistant Person maintenance (**DL-31**); its present location inside the Concierge implementation is rank-4 evidence, not final ownership. Foundation holds the canonical consent record (person/participation reference, evidence source, capability, data class, state, scope, granted/effective/withdrawal time, self-or-proxy actor, surface, deletion and retention-floor effects); Identity owns the lifecycle; Operational Trust decides whether a capability may proceed given consent state; Concierge presents the interaction; **no Consent responsibility is created**. **Self-consent and proxy consent are both supported, and a proxy action never masquerades as self-consent** — the acting person is authenticated and recorded, the subject and scope are recorded, and **who qualifies as an authorized proxy is resolved as **DL-57****, not duplicated here; a native administrator flag is never treated as care or proxy authority. A **contextual continuity path** ("would you like me to remember you?") remains Person Setup, conversational rather than comprehensive: declining creates no durable profile and no person-scoped learning (**DL-33**); consenting creates only the minimum disclosed record, never automatic access to email, calendar, administration, or resident-level capability, and never a synthetic Guest Person. **Withdrawal is explicit and capability-specific**: Voice Identity withdrawal excludes evidence immediately before weighting (**DL-38**) and deletes voiceprints, derived profiles, and temporary samples (**DL-43**); device removal ends person association while the device may continue as an unidentified-device observation; dependent capabilities become unavailable and name the missing dependency (**DL-41**). **DL-43 and DL-47 are reconciled by keeping two records separate in kind**: biometric and derived identity material is deleted; that consent existed, its scope, who recorded it, when it ended, and that deletion was triggered survive as a structural floor, never sufficient to reconstruct what was deleted. **Consent remains effective until explicitly withdrawn and never silently expires**; optional reaffirmation is a distinct recorded event, and no response, a missed prompt, or inactivity is never withdrawal. **A consent change never rewrites a historical Decision Trace**; post-withdrawal observations are never attributed to the person through the withdrawn association. **Consent not given, consent declined, consent withdrawn, permission denied, dependency missing, and unknown are six distinct, never-collapsed household-facing states.** Whether previously unassociated observations may ever be exceptionally correlated for a legal or incident request is **not decided here** and is tracked separately as **OD-89** | A synthetic Guest/Visitor/Unknown Person created from mere observation or co-presence; identity-association consent inferred from a data-source configuration action or the reverse; voice evidence down-weighted instead of excluded on withdrawal; a hidden or silently retained device association after removal; consent treated as expiring by default; a renewal prompt's silence treated as withdrawal; a historical Decision Trace rewritten after a consent change; a proxy action recorded or presented as self-consent; a native administrator flag treated as proxy or care authority; a second, inconsistent consent model alongside the canonical record; a Consent responsibility | [../models/person-and-identity.md](../models/person-and-identity.md), [../contracts/identity-contract.md](../contracts/identity-contract.md), [../architecture/privacy.md](../architecture/privacy.md) |
| **DL-57** | **Delegated Stewardship authority is an explicit, scoped grant — never inferred from a relationship, Role, or administrator status** (P26, DL-31, DL-36, DL-41, DL-48, DL-49, DL-56). One person may hold explicit authority over another Person's, Asset's, or Pet's Stewardship content — to view, receive, declare, update, schedule, complete, or manage an obligation — only through a **Delegated Access Grant** naming its subject, grantee, specific operations, scope, grant basis, and effective/revocation time; the Foundation `caretaker-of` relationship continues to record accountability only, never access. **Operations are never collapsed** (DL-36): permission to view, receive, or complete an obligation does not itself confer permission for any other operation. A competent adult retains self-authority over their own grants and may explicitly delegate; a minor or a person unable to act independently may be represented by an authenticated administrator acting as proxy; **a native Home Assistant administrator flag is never itself care, guardianship, or proxy authority**, and formal legal qualification (guardianship, power of attorney, or equivalent) is explicitly outside HTBW's scope — HTBW records that a proxy grant was established and by whom, asserting no legal sufficiency. **Identity evidence never transfers with a grant**: a caretaker's device or voiceprint is never evidence for the cared-for person, and a proxy-facilitated identity class the subject cannot usably provide remains unavailable under DL-41, never manufactured or substituted. A non-resident authorized participant (a housekeeper, dogsitter, or conservator) may hold a minimal Person record carrying only the grants explicitly configured for them — no second Person directory is created. Revocation is immediate and prospective; existing obligations remain Stewardship-owned governed records the household may reassign; historical actions remain attributed to the actor and grant valid at the time. **An obligation remaining unmet with accountability unchanged is continuing notification, not automatic escalation** — escalation specifically means a configured change of accountable party, and OD-22 applies only there | Invented Care, Caregiver, Guardianship, Delegation, or Authorized Abilities responsibility; access inferred from `caretaker-of`, a Role, or an administrator flag; operations collapsed into a single undifferentiated grant; identity evidence substituted across persons; automatic escalation triggered by an incomplete obligation absent a configured accountability change | [stewardship.md](../models/stewardship.md), [person-and-identity.md](../models/person-and-identity.md) |

| **DL-58** | **Truth Fact Confidence describes the strength of qualified evidentiary support for a Fact under the applicable Truth evaluation policy — never probability, measured accuracy, or certainty — and is represented as one uniform ordinal enumeration, Low < Moderate < High < Very High, applied identically across every Fact Subject and Fact class** (P15, P21, P26, P30, DL-04, DL-25, DL-38, DL-39, DL-41, DL-47). Truth Confidence and Identity Confidence (**DL-39**) are structurally separate, independently owned concepts that happen to share household-facing labels: a Truth Confidence Band is never an Identity Confidence Band, the two are never converted, averaged, or compared arithmetically, and a Pet, Asset, or Device Fact is structurally unable to carry an Identity Confidence Band. **Confidence is independent of freshness (OD-18), provenance, and contributor coverage (OD-17)** — each is a separate mandatory Fact dimension, never collapsed into the band. Cross-Fact-class comparability is ordinal and semantic only, never arithmetic. An optional normalised numeric may accompany the band as a non-authoritative deterministic ordering value only, never resident-facing probability, likelihood, calibration, or accuracy, and never authorizing anything; none is mandated. `None`, `unknown`, `unresolved`, `stale`, and `withdrawn` remain first-class Fact states, never a fifth confidence band. Every Historical Fact retains its Truth Confidence Band and the Truth evaluation-policy version that produced it; a later policy change never rewrites a prior Fact. Composite Fact derivation (**OD-17**), Fact validity and freshness effects (**OD-18**), and conflict-resolution effects (**OD-19**) each consume this representation without redefining it, and none of them, nor **OD-72**, may borrow the Identity Fusion Function or DL-39 bands | A fifth Truth Confidence band; a Truth Confidence Band presented as probability, accuracy, or certainty; a Truth Confidence Band converted to or compared against a DL-39 Identity Confidence Band; a Pet, Asset, or Device Fact carrying an Identity Confidence Band; confidence collapsed with freshness, provenance, or coverage; a resident-facing confidence numeric; a per-Fact-class confidence vocabulary; a Historical Fact rewritten by a later policy change | [../models/truth.md](../models/truth.md), [../contracts/truth-contract.md](../contracts/truth-contract.md), [../models/decision-trace.md](../models/decision-trace.md) |
| **DL-59** | **Truth distinguishes two Fact source shapes — Current-State Sources and Point-in-Time Observation Sources, classified by documented integration semantics, never by domain or device class alone — and governs operational Fact validity accordingly** (P15, P21, DL-04, DL-25, DL-30, DL-34, DL-38, DL-41, DL-47, DL-58). **For a current-state determination, Truth evaluates the most current authoritative Home Assistant state available at evaluation time** — as though reading the current dashboard — **and never prefers an older cached HTBW interpretation over healthier newer native state**; no HTBW-imposed generic delay is applied to a healthy current-state source. A current-state Fact remains current while its source is available and its documented semantics support a current claim, and ceases immediately — never through elapsed HTBW time — when the source becomes unavailable, becomes unknown, or its documented semantics no longer support the claim. A point-in-time observation's Fact carries an operational validity window; when it elapses, the Fact **operationally expires**; it is **withdrawn** when a supporting condition changes or contradicting current evidence emerges (**OD-19**); it is never presented as current after either. **`expired`, `unavailable`, and `never observed` remain three distinct, always-named outcomes.** **Truth Confidence (DL-58) and Fact Validity are separate dimensions**: the confidence originally established for a Fact is never decayed by elapsed time alone; validity states whether the Fact remains current, confidence states how strongly it was supported when established. Operational expiration is one of **DL-25**'s eight Truth lifecycle transitions, materialized through the existing Domain Event / Change Record mechanism (**temporal-record.md**); no second event model is created, and consumers reevaluate on that event or, where it has not yet materialized, at query time — **there is exactly one authoritative validity result**. **On-demand refresh is bounded**: an integration's documented refresh mechanism (for example Home Assistant's `update_entity` action) may be requested only where that integration's support is verified under **DL-30**'s burden of proof; a refresh request **never manufactures a physical observation** and never proves a new reading occurred; push-only, event-driven, and advertisement-based sources may not support one at all. **Expired or unavailable presence never decays into absence or solitude** (**DL-34**); Room Occupancy (a Room-subject current-state Fact) and Contextual Person-Presence (a Person-subject Fact derived through Identity, **DL-38**) remain the existing separate Facts this decision does not redefine. **Freshness and validity windows are household configuration values, not architecture** (mirroring **DL-47**), stated per Fact class and Subject where the household chooses to differentiate them, never overriding consent, never converting last-known into current, and never silently learned (**P26**, **DL-21**) | An HTBW-imposed generic delay applied to a healthy current-state source; a stale current-state reading retained merely because Home Assistant still displays it; a point-in-time observation presented as current; expired or unavailable presence rendered as absence or solitude; confidence decayed by elapsed time alone; a second Fact-expiration event model; independent consumer-computed validity windows; a forced-refresh claim for an integration whose support is undocumented; a household-configured window converting last-known into current or bypassing consent | [../models/truth.md](../models/truth.md), [../contracts/truth-contract.md](../contracts/truth-contract.md), [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md), [../models/temporal-record.md](../models/temporal-record.md) |

| **DL-60** | **Room Configuration defines an extensible Room Environment Standard of household-oriented Environmental Purposes, disambiguates multiple candidate sources per purpose as Primary Authority, Secondary/Corroborating, Composite Contributor, or Explicit Exclusion, and treats a documented native Area environmental entity slot as a default proposal — never automatic participation, never a silent override, never written back** (P15, P21, DL-09, DL-11, DL-30, DL-31, DL-41, DL-55, DL-58, DL-59). **The Environmental Purpose set (temperature, humidity, dew point, illuminance, UV, VOC, particulates, CO2, mold index, leak, pressure, vibration, noise, window/orientation/exposure characteristics, and others) is extensible, never closed**; it names available household-oriented meanings a source may be mapped to, asserts no household has every sensor, invents no reading for an absent one, and never converts an absent sensor into a normal, healthy, or safe default. **Where more than one eligible source exists for one Environmental Purpose in a Room, Room Configuration represents four distinct, non-collapsible states** — at most one **Primary Authority** per purpose for direct Room-level questions; any number of **Secondary/Corroborating** sources contributing supporting evidence without answering the direct question; any number of **Composite Contributors** feeding an **OD-17** Composite Fact; and **Explicit Exclusion** — and runtime never arbitrates among equivalent same-purpose sources by order, recency, or vendor preference. **One Room Environment configuration serves both direct current-state questions and composite/care derivations**; no separate mapping exists per consumer (Concierge, Stewardship, Asset care evaluation, and Truth all consume the same participant and authority selection). **A native Area environmental entity slot whose documented semantics correspond to an accepted Environmental Purpose (verified per-slot under DL-30, never assumed) seeds a default proposal exactly as OD-14 already established for naming** — never automatic silent participation, honouring **DL-11**; the household is never asked to reconfigure information Home Assistant already holds, honouring **DL-31**. An explicit HTBW selection or exclusion, once made, is never silently overridden by a later native (re)assignment; a later native change becomes a new proposal alongside the existing configuration, and the resulting divergence is a Room Configuration condition, explainable and reviewable, never a Repairs defect and never a silent Fact change. **HTBW never writes the selection back to the native Area assignment.** For a **Merged Room**, eligible sources are surfaced from every constituent Room with the source Room visible; no entity is copied; Room Configuration selects constituent-Room sources into the Merged Room's own primary/secondary/composite/excluded states per purpose. **A derived Environmental Purpose** (for example dew point, derived from a Room's configured temperature and humidity) is declared by Room Configuration and computed by Truth as an application of its existing Composite Fact concept — combining more than one input via a documented deterministic formula rather than a same-dimension aggregation choice; the specific formula is implementation mapping, not decided here, and a missing required input Fact makes the derived Fact `unknown`, never invented. **This creates no new responsibility, no second Room registry, no second vocabulary system, and no second composite-fact store** — it is an extension of Room Configuration's existing three-state participation model (Participating / Not Selected / Deliberately Excluded), applied per Environmental Purpose | A closed or per-household-exhaustive Environmental Purpose list; an absent sensor rendered as a normal, healthy, or safe reading; primary authority, secondary evidence, composite contribution, and exclusion collapsed into one boolean; runtime arbitration among equivalent same-purpose sources; a native Area slot treated as automatic participation; an explicit HTBW selection or exclusion silently overridden by a later native reassignment; a native assignment written back by HTBW; a Merged Room copying constituent entities; a derived value invented when its required input is unavailable; a second Room registry, environmental store, vocabulary system, or composite-fact store | [../models/room-configuration.md](../models/room-configuration.md), [../contracts/room-configuration-contract.md](../contracts/room-configuration-contract.md), [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md) |

| **DL-61** | **A Room has no intrinsic universal health state; Asset-derived Entity projection reuses Stewardship's and Truth's existing owned vocabularies, never an invented health scale; and a Person may declare Environmental Requirements through Person Setup, evaluated by Stewardship exactly as an Asset's environmental limits already are, against current Room Environment Facts while a valid Contextual Person-Presence Fact places the Person there** (P15, P21, P26, P32, DL-09, DL-11, DL-31, DL-34, DL-38, DL-41, DL-42, DL-46, DL-47, DL-56, DL-57, DL-58, DL-59, DL-60). **Asset-derived Entity projection (resolves OD-69):** a projected Entity is a projection, never a second authority; the determining responsibility keeps the determination — Stewardship's existing obligation vocabulary (`met`/`due`/`unmet`/`overdue`/`waived`/`unknown`) and Truth's existing Fact vocabulary are the only projected vocabularies, and **no asset-health or room-health scale is invented**; a projected Entity resolves back to its Asset; an `unknown` determination projects as `unknown`, never a stale prior value; a projected Entity is never externally writable, and any write is structurally prevented or ignored, never becoming the value. **Person Environmental Requirements** reuse the Asset environmental-limit shape without converting a Person into an Asset: a minimum, maximum, acceptable range, applicable **DL-60** Environmental Purpose, significance, provenance (self or **DL-57** proxy), consent state, effective period, and withdrawal history, coordinated through Person Setup, held by Foundation, evaluated by Stewardship, disclosed under Operational Trust, and reusing **DL-56**/**DL-57** consent and proxy governance without a new authority model. **Preference, Requirement, and medical/clinical threshold remain three distinct kinds**: a preference may guide personalization or an Advisory; a requirement drives Stewardship evaluation; **HTBW invents and validates no clinical or medical threshold**. **Location-driven evaluation**: a Person's requirement is evaluated against current Room Environment Facts only while a valid Contextual Person-Presence Fact places the Person in that Room; where location is unknown, no current suitability claim is made and the prior Room is never treated as current; where a required Fact is unavailable, the requirement evaluates to `unknown`, never assumed met or unmet. **Every Person, Pet, and Asset subject in a Room is evaluated independently** — never averaged, never ranked, never merged into one verdict; conflicting requirements between subjects are surfaced, never silently resolved. **Environmental Coverage, Configuration Completeness, and Truth Confidence are three separate, non-collapsible measures**: Configuration Completeness is the fraction of a Room's household-selected applicable Environmental Purposes that currently have a configured source (Room Configuration); Environmental Coverage is the fraction of *configured* purposes currently available with a valid Fact (a projection over Truth's per-Fact validity, **DL-59**); Truth Confidence (**DL-58**) remains per-Fact only. **None of the three may be renamed into, averaged into, or presented as the other**, and an unconfigured but inapplicable purpose never reduces either measure. **Room Environmental Status is a non-authoritative dashboard projection** over current per-subject Stewardship evaluations for applicable Persons, Pets, and Assets in a Room — never a Truth Fact, never a probability, never a medical or clinical status, and never a replacement for an individual requirement evaluation; any color is presentation only, and every projected state must drill through to its underlying subject, Fact, requirement, evaluation, significance, provenance, confidence, and validity. **Room Health, Room Confidence, and People Health are rejected as authoritative terms** (`glossary.md` Rejected Terms, extending **DL-60**): Room Health decomposes into current Room Environment Facts, Environmental Coverage, Configuration Completeness, and an Environmental Stewardship Summary; a legacy "sensors configured over all possible dimensions" calculation is Configuration Completeness, never Confidence; People Health is replaced by Person Environmental Requirements and their per-requirement Stewardship evaluations. **HTBW asserts no diagnosis, clinical advice, wellness score, medical claim, or life-safety guarantee** at any point in this decision | A universal Room Health, Room Confidence, or People Health authority; an invented asset-health or room-health scale; a projected Entity treated as a second authority or externally writable; a Person modeled as an Asset; a clinical or medical threshold invented or validated by HTBW; a prior Room treated as current when location is unknown; a missing Fact assumed met, unmet, healthy, or unhealthy; multiple subjects in a Room averaged, ranked, or merged into one verdict; Environmental Coverage, Configuration Completeness, or Truth Confidence collapsed into one another; an unconfigured-but-inapplicable purpose counted against coverage or completeness; a dashboard color treated as authoritative or medical; a diagnosis, clinical recommendation, wellness score, or life-safety guarantee | [../models/asset.md](../models/asset.md), [../models/stewardship.md](../models/stewardship.md), [../contracts/stewardship-contract.md](../contracts/stewardship-contract.md), [../models/person-and-identity.md](../models/person-and-identity.md), [../models/room-configuration.md](../models/room-configuration.md), [../models/glossary.md](../models/glossary.md) |

| **DL-62** | **Resolves OD-17.** For every directly measured **DL-60** Environmental Purpose, Room Configuration selects one **Primary Authority** as the required, deterministic ordinary Room-level source — identically for a Physical Room and a Merged Room (**DL-13**) — and Truth reads that single selected source's current state (**DL-59**) as an **Authority-Derived Fact** carrying **DL-58** Truth Confidence and no contributor coverage; runtime never arbitrates among equivalent same-purpose sources, and an unconfigured purpose is unavailable, never an implicit composite fallback. **No accepted household use case requires averaging, median-combining, weighting, or otherwise aggregating multiple equivalent same-purpose sensors into one ordinary Room Environment Fact**, and same-purpose **Composite Contributor** aggregation is removed from that ordinary path, narrowing **DL-60**'s four-state disambiguation to three — **Primary Authority**, **Secondary/Corroborating**, **Explicit Exclusion**; if a genuinely narrow future use case for same-purpose aggregation is ever accepted, Home Assistant's native Min/Max helper (documented `mean`/`median`/`min`/`max`/`range`/`sum` over configured entities) discharges **DL-30**'s burden of proof without a new HTBW aggregation engine, and that use case is decided on its own governed terms rather than preserved speculatively now. **Formula-Derived Facts remain structurally distinct from same-purpose aggregation**: a Formula-Derived Fact (for example Dew Point) combines **different** Environmental Purposes' current Facts through a named, versioned derivation, and must preserve its input Fact references, input validity, input confidence, derivation identity and version, formula or provider provenance, produced value, unit, Truth Confidence, validity, and a named failure reason where not produced; a missing or invalid mandatory input publishes the Formula-Derived Fact as `unknown` — never a partial calculation, never a retained last value — and the missing input is named. **Dew Point's formula class and versioning discipline are accepted; the specific formula remains implementation mapping, verified per DL-30. Mold Index and Condensation Risk remain unresolved** — no HTBW-endorsed formula exists, and HTBW invents no clinical, medical, or safety-threshold formula. **Environmental Coverage, Configuration Completeness, and Room Environmental Stewardship Summary remain DL-61's** dashboard projections, never Composite Facts and unaffected by this decision. **OD-19 receives only the current, valid, selected Primary Authority (or Formula-Derived Fact inputs) Room Configuration designates, and never reintroduces runtime arbitration among equivalent same-purpose sources this decision eliminates** (P15, P21, DL-04, DL-09, DL-11, DL-13, DL-25, DL-30, DL-41, DL-47, DL-58, DL-59, DL-60, DL-61) | Same-purpose sensor averaging, median-combining, or weighting invented as an ordinary-path default; Composite Contributor treated as a silent fallback when no Primary Authority is configured; a Formula-Derived Fact publishing a partial result or retaining a stale value when a mandatory input is missing; an invented Mold Index or Condensation Risk formula; OD-19 arbitrating among equivalent sources by order, recency, or vendor preference | [room-configuration.md](../models/room-configuration.md), [truth.md](../models/truth.md) |

| **DL-63** | **Resolves OD-19.** A genuine Truth conflict exists only when two or more currently eligible, semantically comparable claims address the same Subject, predicate/Fact purpose, context, and evaluation time, remain independently eligible after Truth's qualification order runs, and are mutually incompatible, with no accepted authority-selection, validity, availability, configuration, Identity, or Stewardship rule already explaining the difference. **Truth qualifies evidence in a fixed order before any conflict determination**: same Subject; same predicate/purpose; same context; same evaluation time or overlapping validity; current availability (**DL-41**); **DL-59** validity; configuration eligibility (Room Configuration's designated Primary Authority/Secondary/Excluded participation); consent and policy eligibility; authority selection; semantic comparability; only then contradiction determination; only then conflict-outcome application. **Evidence excluded before the contradiction step is not conflicting evidence** — an expired value is invalid, not contradictory; an unavailable source is unavailable, not contradictory; an unselected candidate is not an authority and does not conflict with the selected Primary Authority; a Provider-Derived Environmental Indicator has different semantics from a direct measurement or a Stewardship evaluation and is never compared as competing evidence for the same purpose; missing evidence is absence, not contradiction. **Same-purpose environmental sensor disagreement is not an ordinary Truth conflict** (**DL-62**): an unselected sensor's differing value is a source-specific diagnostic value, never a competing Room authority, and never reduces the selected Primary Authority's confidence. **A native Area environmental slot's proposal diverging from an explicit Room Configuration selection is a configuration condition, not a runtime conflict** (**DL-60**) — HTBW never writes back, never silently switches, and the divergence remains visible and explainable, escalating to Repairs only where **OD-60**'s own administrator-correctable-defect criteria are independently met (for example two configuration records both claiming exclusive Primary Authority for one purpose). **A Provider-Derived Environmental Indicator does not conflict with a direct measurement or a Stewardship evaluation merely because the values differ in shape, scale, or outcome** — the statements have different predicates and owners (post-**DL-62** clarification). **Conflicting Person, Pet, or Asset Environmental Requirements against one current Room Fact remain Stewardship's own** (**DL-61**): Truth publishes one current Fact; Stewardship maintains independent per-subject evaluations; no average requirement, majority rule, or subject ranking is created. **Identity contradiction among evidence families remains DL-38's own**, resolved inside the Identity Fusion Function before Truth ever receives the resulting purpose-specific Assertion; this decision does not reuse, duplicate, or reach past that Assertion to its underlying evidence. **Assertion lifetime and cross-purpose assertion eligibility remain OD-15's own** and are not decided here; OD-15's own recorded boundary (a prior purpose-specific Assertion's contribution to a later, different-purpose determination ends when the supporting Room's occupancy transitions to unoccupied or the Person's configured primary evidence source no longer supports that Room) is consumed without redefinition where OD-15 accepts it. **Where a genuine Truth conflict remains after qualification, Truth publishes exactly one of**: a single Fact at a reduced **DL-58** Truth Confidence Band (never raised by contradiction, never Very High), recorded with the applicable reason and Conflict Policy version, only where a governed resolution rule or an accepted authority applies; an **unresolved** Fact naming every competing claim, its source, and its value, where no resolution rule applies; or **`unknown`**, where nothing can be honestly asserted — a successful, honest outcome, never conflated with **`unavailable`** (an evaluation that could not occur, **DL-41**) or with absence of evidence. **Truth never averages contradictory evidence, never applies majority voting, and never adopts a universal provenance-class precedence** — a native entity, an HTBW Fact, an external provider, and a derived Fact are never ranked by class alone; only an accepted authority-selection rule (Room Configuration's Primary Authority, Person Setup, or an Identity Evidence Association) establishes precedence. **A range-valued Fact is not adopted for any current Fact class** — no accepted Fact class canonically requires one, and one is not invented merely to escape an unresolved contradiction; this is deferred, not decided. Disagreement thresholds, where meaningful, are Fact-class-scoped **Conflict Policy** configuration — named, versioned, unit-stated, and explainable — never a single universal numeric; some Fact classes (categorical location, occupancy, online/offline) have none. A conflict's appearance, continuation, and resolution are recorded through the existing Domain Event / Change Record mechanism (`temporal-record.md`) — no second conflict-history store is created — and a later resolution publishes a new Fact without rewriting the prior `unknown` or reduced-confidence outcome. **Persistent conflict** (a Conflict-Policy-configured recurrence/continuity condition) may indicate a likely administrator-correctable defect and is evaluated against **OD-60**'s Repairs criteria separately from the runtime Fact outcome; ordinary transient disagreement, a briefly unavailable source, or a native-proposal/HTBW divergence are not automatically Repairs-eligible (P15, P21, DL-04, DL-09, DL-11, DL-13, DL-25, DL-30, DL-32, DL-35, DL-38, DL-39, DL-41, DL-47, DL-58, DL-59, DL-60, DL-61, DL-62) | Averaging contradictory evidence into a confident value; a universal numeric disagreement threshold; a universal provenance-class precedence order; treating an unselected sensor, a native Area proposal, a provider-derived indicator, or a Stewardship conflict as a Truth conflict; reusing the Identity Fusion Function or DL-39 bands for Truth-side conflict; raising confidence through contradiction; conflating unknown with unavailable or with absence of evidence; inventing a range-valued Fact without an accepted Fact class requiring one; a second conflict-history store | [truth.md](../models/truth.md), [truth-contract.md](../contracts/truth-contract.md) |

| **DL-64** | **Resolves OD-15.** Identity Assertion "lifetime" was a conflation of three distinct concepts, now formally separated. **Assertion Validity**: an Identity Assertion, once produced by the **DL-38** Fusion Function, remains a **permanently correct historical record** of what evidence supported, for its stated purpose, at its produced moment; it is never revoked, decayed, or invalidated by elapsed time alone, and **DL-47** governs its retention (with its Decision Trace or governed history, never a separate universal duration) entirely independently of this. **Current-Interaction Applicability**: whether a produced Assertion is evidence-appropriate for the interaction, participant, and purpose being evaluated **now**; this is never answered by checking whether a stored assertion has "not yet expired," because HTBW creates **no long-lived Identity session** (**DL-39**) — a consumer needing a current purpose-specific result triggers a **fresh evaluation of DL-38's Fusion Function against current eligible evidence**, which already applies its own per-source freshness windows, graduated reduction, and hard cutoff as Fusion Policy configuration (**DL-38**); **no separate, second "assertion validity window" mechanism is created, and no fixed duration by confidence band, by Assertion Purpose, or otherwise is architecture**. **No Assertion Purpose among the six** (Speaker Attribution, Room Presence, Household Presence, Interaction Initiator, Authenticated Session Identity, Endpoint Context) **requires a fixed validity window**; each is re-evaluated identically on demand from current eligible evidence, and any purpose-specific difference lives in **DL-38**'s existing ceilings, freshness rules, and eligibility gates, never in a new per-purpose timer. **Cross-purpose assertion eligibility is accepted**: a prior purpose-specific Assertion's contribution to a later, different-purpose determination (for example a Speaker Attribution assertion informing a subsequent Room Presence evaluation) ends when either the supporting Room's occupancy transitions to `unoccupied` or the Person's configured primary evidence source no longer supports that Room — only one break is required — consistent with **DL-63**'s own consumption of this boundary; a new Assertion Purpose evaluation is required where a different Person speaks in an occupied Room, and the prior Assertion is never reused as the current-speaker Assertion for someone else. **Applicability is evaluated before DL-63's Truth-side conflict qualification ever runs**: an Assertion that is not currently applicable is excluded as ineligible evidence within **DL-38**'s own fusion, never surfacing to Truth as a candidate claim requiring conflict resolution. **No expiry Domain Event is created**: applicability loss follows from already-modeled Fact-level transitions (for example a Room Occupancy Fact's own **DL-25** lifecycle transition to `unoccupied`) that the existing Domain Event / Change Record mechanism already records; a second lifecycle framework is not created. **An implementation may cache or reuse a recently-produced Assertion as a performance optimization** equivalent to re-running fusion, keyed to a Fusion-Policy-configured, versioned, band-aware duration — this remains implementation mapping under the existing **OD-16** precedent (Fusion Policy coefficients are configuration, not architecture), never a second governed validity-window construct (P15, P26, P27, P30, DL-04, DL-25, DL-32, DL-36, DL-37, DL-38, DL-39, DL-47, DL-63) | A fixed per-band or per-purpose assertion validity duration treated as architecture; an assertion "expiring" and being silently reused as current merely because a timer had not elapsed; a long-lived Identity session; continuous Room occupancy treated as continuous identity; a confirmation extending assertion life; a second conflict/applicability event model; retention conflated with validity or applicability | [person-and-identity.md](../models/person-and-identity.md), [identity-contract.md](../contracts/identity-contract.md) |

| **DL-65** | **Resolves OD-60.** Repairs is a **projection** of an HTBW-owned, authoritative **Defect State** — never the reverse, and never a second authority: the owning responsibility (Room Configuration, Foundation, Identity, Truth, or Operational Trust) detects and holds the defect; Repairs is the Home Assistant surface that responsibility uses to tell an administrator, and creates or deletes the corresponding issue as its own defect state changes. **A condition is Repairs-eligible only where it is a configuration or dependency defect an administrator can correct through Home Assistant's administrative surfaces** — never a household obligation (Stewardship, confirmed unchanged), never a Communication, never an acknowledgement, never a Truth runtime outcome by itself, never an Identity Assertion outcome by itself, never a Provider-Derived Environmental Indicator's reported value, and never a difference between two dashboard projections. **Genuine Repairs candidates**: a missing or invalid **DL-41** capability dependency (Connected Storage unavailable, a missing integration or provider); a broken governed reference (a Room's selected Primary Authority, an Asset relationship, a caretaker reference, or a vocabulary target pointing to a deleted native object); and a configuration invariant violated in a way ordinary runtime evaluation cannot resolve on its own (for example two configuration records simultaneously claiming exclusive Primary Authority for one Environmental Purpose). **Configuration divergence, by itself, is never automatically Repairs-eligible** (**DL-60**'s own rule, now generalized): a native proposal disagreeing with an explicit HTBW selection, a native Assist exposure setting disagreeing with HTBW Exposure (**OD-59**), or a native Label disagreeing with the authoritative Asset Type (**OD-68**) each remain a **configuration condition** — visible and explainable through the owning responsibility's own lifecycle — escalating to Repairs only where the divergence separately meets the genuine-defect test above, never merely because two values differ. **A persistent Truth conflict (DL-63) does not, by itself, become a Repairs issue**: Truth records the conflict's appearance, continuation, and resolution through the existing Domain Event mechanism, and a Repairs issue is raised only where the responsibility owning the relevant configuration (typically Room Configuration) independently identifies that the persistence pattern reveals a genuine configuration defect (for example, duplicate Primary Authority) rather than two legitimately configured sources merely disagreeing. **Fixable versus informational**: a Repairs issue is fixable through a `RepairsFlow` only where HTBW can deterministically correct the underlying configuration itself (for example removing a stale reference); it is informational-only where correction requires administrator judgment HTBW must not make (for example choosing which of two claimed Primary Authorities to keep) — **Repairs never becomes configuration authority**, and every fixable flow performs exactly the change a resident could have made themselves through Room Setup or the native registries. **Severity** is drawn only from Home Assistant's own three-value `IssueSeverity` (verified: CRITICAL reserved for true panic and essentially never claimed by HTBW; ERROR for a capability currently unavailable or a reference currently broken; WARNING for a configuration condition that has not yet blocked anything but warrants review), mapped from the owning responsibility's own already-accepted state (**DL-41** capability outcomes, a broken governed reference, a detected configuration invariant violation) — **never from Stewardship significance, Operational Trust Urgency, or resident-facing consequence** (**DL-46**, **OD-46**). **The ignore lifecycle is verified against official Home Assistant documentation**: ignoring an issue neither deletes nor resolves it; an ignored issue persists in the registry, suppressed from the dashboard, until the owning integration deletes it (because its own defect state cleared) or the resident completes its repair flow — **ignoring therefore never changes HTBW's own Defect State**, confirming **OD-45**'s existing rule that ignoring is not a person-attributed acknowledgement. **Re-raising is not a timer**: because HTBW's own Defect State is authoritative and Home Assistant persists an issue until HTBW itself deletes it, "re-raise" is simply the owning responsibility's own existing state-evaluation trigger (a Room Configuration change, a capability-dependency re-check, a startup reconciliation) recreating the issue if the condition still or again holds — no new schedule, timer, or event model is invented (P15, P21, DL-16, DL-25, DL-30, DL-31, DL-41, DL-45, DL-46, DL-60, DL-61, DL-62, DL-63, DL-64) | Repairs treated as an obligation store, a Communication surface, or an acknowledgement mechanism; a Repairs issue treated as the authoritative defect record rather than a projection of one; configuration divergence escalated to Repairs merely because two values differ; a persistent Truth conflict automatically becoming a Repairs issue; a Repairs flow choosing between two legitimately configured options on the household's behalf; `severity` mapped from Stewardship significance or Operational Trust Urgency; ignoring an issue treated as resolving or acknowledging the underlying defect; an invented re-raise timer | [architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md), [models/stewardship.md](../models/stewardship.md), [models/asset.md](../models/asset.md) |

| **DL-66** | **Resolves OD-59.** Native Home Assistant Assist entity exposure and HTBW's own constitutional **Exposure** state (**DL-11**) are not the same concept: native Assist exposure is a platform **safety boundary** restricting whether any assistant may target or control an entity by voice at all — documented by Home Assistant as existing specifically so sensitive devices cannot be controlled inadvertently by voice commands — while HTBW Exposure is Room Configuration's own governed decision, for a participating object, of whether a capability is intentionally made available to residents through vocabulary, Room Help, UI, conversation, or another interaction surface. **For voice- and conversation-mediated interaction specifically** (vocabulary resolution, Room Help spoken answers, and conversational discussion, retrieval, targeting, or suggestion) **HTBW Exposure may never exceed native Assist exposure**: HTBW may narrow — excluding something Assist would permit — but must never widen past a native exclusion, and never bypasses it under any configuration. **This is a narrower rule than OD-14 or DL-60's pattern, not a mechanical reapplication of it**: unlike a native name (an informational seed a household may freely override) or a native environmental slot (a proposal Room Configuration may accept, decline, or supersede), native Assist exposure is never treated as a mere default HTBW's own governed state may end up overriding upward — only narrowing is ever permitted, because the native setting is itself a deliberate safety precondition, not an informational suggestion. **HTBW Exposure for a non-voice surface (a UI panel, a dashboard) is independently governed by Room Configuration and is not bounded by native Assist exposure**, since Assist exposure's own documented purpose is scoped to assistant targeting, not general visibility. **HTBW never writes back to native Assist exposure** under any circumstance (**DL-31**, **DL-65**'s projection model, **OD-14** precedent). **Divergence between the two is never, by itself, a defect**: an entity Assist-exposed but HTBW-excluded is an ordinary deliberate exclusion, explainable as such; an entity HTBW-included but Assist-hidden is a configuration condition — explainable through Room Configuration's own lifecycle, informing the household that voice cannot currently reach an otherwise-configured capability — and neither is ever a Repairs issue (**DL-65**): every ordinary divergence scenario resolves through this precedence rule without administrator intervention, and none constitutes a standing configuration or dependency defect DL-65 recognizes. **Governed retrieval through Conversation (OD-62) consumes this boundary as one of its own inputs without redefining it** — which entities are voice-discussable, targetable, or retrievable is answered here; how a retrieval question is answered, filtered, and reported as unanswerable remains OD-62's own. **The specific native mechanism for reading current Assist exposure state and observing changes to it remains to be verified per DL-30 at implementation time** — mirroring DL-60's own per-slot verification requirement — an implementation-mapping residual, not an architectural blocker, since the precedence rule holds regardless of which mechanism ultimately reads the setting (P5, P6, P7, P21, P30, DL-11, DL-16, DL-18, DL-30, DL-31, DL-60, DL-65) | HTBW silently widening past a native Assist exclusion; treating Assist exposure as a mere seed or default HTBW may freely override upward; writing an HTBW exposure decision back to native Assist exposure; treating ordinary Assist-vs-HTBW divergence as a Repairs defect; conflating HTBW Exposure (DL-11) with native Assist exposure as one setting; bounding UI or dashboard visibility by native Assist exposure where no accepted requirement does so | [models/room-configuration.md](../models/room-configuration.md), [architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md) |

| **DL-67** | **Resolves OD-11.** A Merged Room is not a general-purpose or capability-specific grouping mechanism; it is the same Room contract Foundation and Room Configuration already define — vocabulary, participation, exposure, Room Help, experience endpoints, and composite-fact input selection (**DL-11**, **DL-12**, **DL-13**, **DL-62**) — applied to a constituent set of more than one Physical Room. It exists to give the household **one curated conversational interaction context** spanning several physical spaces, never to duplicate a general grouping capability Home Assistant already provides. **A Physical Room (Area) may be a constituent of at most one Merged Room at a time.** This is a necessary architectural invariant, not merely the simplest configuration choice: **DL-13**'s "a Room and a Merged Room behave identically" and its rejection of special-case orchestration both presuppose exactly one, unambiguous Room Context per Physical Room. Allowing overlapping membership would force every consumer of Room Context — Truth's composite-fact input selection and current-state evaluation (**DL-62**), Continuity's session, audience, and transfer detection, Operational Trust's policy scoping, and Room Configuration's own vocabulary resolution — to add its own selection or precedence rule for which Merged Room currently applies. That is precisely the special-case orchestration **DL-13** exists to prevent, and it is incompatible with **DL-63**'s conflict-qualification order, which already assumes Room Context has been resolved to a single value before Truth ever evaluates "same context." **This is confirmed by existing Concierge implementation evidence, not merely assumed**: composite (Merged Room) configuration already structurally excludes an Area already belonging to an enabled composite from being offered when creating or editing another composite, and composite configuration already carries conversational-context properties (persona, TTS voice/language, AI knowledge enablement) alongside curated device/asset participation lists, confirming the interaction-context reading over a general-grouping reading. **A household's desire for a broader or different grouping than its configured Merged Rooms (for example "Downstairs lights") is met by Home Assistant's own native Floor, Area, and group/scene targeting, never by an overlapping HTBW Merged Room**: an Area already belongs to at most one Floor natively, and no accepted gap requires HTBW to duplicate that hierarchy as an overlapping interaction-context construct (**DL-16**, **DL-30**). If a household wants "Downstairs" as its own curated interaction context, it configures a Merged Room for it in place of the narrower one its constituent Physical Rooms previously belonged to — an ordinary reconfiguration (a Change Record), never a technical limitation. **No double-counting is structurally possible**: a Physical Room's sensors, devices, and assets belong to exactly one Merged Room's aggregated participation and vocabulary set at a time, so a composite or Formula-Derived Fact input set (**DL-62**) is never ambiguous about which Room it belongs to. **Movement between two Merged Rooms that do not share a constituent Physical Room is an ordinary Room transfer**, exactly as movement between any two distinct Rooms already is (**DL-13**); the only case that would complicate **DL-13**'s simplification — movement between two Merged Rooms that share a constituent Physical Room — cannot arise, because that sharing is excluded by this decision. **Constituent Area definitions are never copied**; a Merged Room only ever references its constituent Physical Rooms, unaffected by this decision | [../models/room.md](../models/room.md), [../models/room-configuration.md](../models/room-configuration.md) |

| **DL-68** | **Resolves OD-70. ACCEPTED, NO NATIVE REPRESENTATION.** A Merged Room is an HTBW-owned, curated interaction and vocabulary context referencing two or more exclusive (**DL-67**) constituent Physical Rooms; it lets household language resolve to preconfigured targets and outcomes without the resident naming every constituent Room or device. It is not an Area, a Floor, a generic group, a physical-topology authority, a copied entity registry, a Scene, or a second source of native Area membership. **No native Home Assistant construct receives any part of this identity.** A consumer inventory (dashboards, native automations, Assist/Conversation, native targeting, scripts, scenes, labels, groups, administrative views, external integrations) found **no canonical, implemented consumer that requires a native projection**: a household dashboard view of "Living Space" is served by Concierge's own configuration surface; a native automation wanting to target "Living Space" can already target its constituent Areas or HTBW's own resolved target set directly, and wanting the convenience of one native object is exactly the preference **DL-42** and [contextual-vocabulary.md](../models/contextual-vocabulary.md) already exclude ("do not construct a duplicate group for convenience"); Concierge's own execution already reuses native scripts and scenes as targets (**DL-55**) without the Merged Room itself needing native form. **Assist and Conversation must not receive a native Merged Room projection, not merely because none is needed but because one would be actively unsafe**: [contextual-vocabulary.md](../models/contextual-vocabulary.md)'s existing "resolution compiles down to native targets" rule means HTBW's own vocabulary layer pre-resolves a term to a concrete, governed entity/device target set before any native targeting occurs; a native Area or Label reachable by Home Assistant's own documented Assist area-slot matching (`https://developers.home-assistant.io/docs/voice/overview/`, `https://www.home-assistant.io/voice_control/aliases/`) would let the **built-in** conversation agent resolve "Living Space" entities directly, bypassing HTBW's curated participation, exclusions, and the **DL-66** Exposure ceiling for exactly the Room DL-67 created to be curated. **Area is rejected**: no native Area-composed-of-Areas concept is documented (`https://developers.home-assistant.io/docs/area_registry_index/`), and inventing one would risk a second physical-topology authority competing with Kitchen, Dining Room, and Living Room as native Areas, which **DL-31** forbids. **Floor is rejected for this purpose**: Floor remains reserved for native physical hierarchy ("Downstairs", "Upstairs"), which already, and independently of Merged Rooms, satisfies the household's broader/different-grouping need under **DL-67**'s own resolution of that question; reusing Floor for a curated conversational context would blur the distinction DL-67 draws. **Group is rejected as a Merged Room representation**: an entity group carries targets, never vocabulary, participation, exposure, or interaction context, and nothing here forecloses Concierge's own internal execution from optionally using a native group as an execution convenience for an already-resolved vocabulary target set (**DL-31**, **DL-55**), which is implementation mapping, not a representation of the Merged Room itself. **Scene is rejected as a Merged Room representation**: a Merged Room's configured outcome may resolve to a scene or script as its execution target, exactly as already accepted (**DL-55**), but a Merged Room is never itself a Scene. **Label is not adopted now**: no proven consumer requires it, and the integration-facing label-management API remains unverified (shared finding with **OD-68**, unresolved); this is not a Label decision and does not preempt OD-68. **Constituent removal uses the existing model without a new rule**: a deleted constituent Area produces a broken reference under the existing deletion-is-directional and broken-reference model (**DL-31**, **DL-65**), an affected vocabulary term becomes `broken_mapping` exactly as [contextual-vocabulary.md](../models/contextual-vocabulary.md) already defines, historical configuration is preserved, no stale membership is implied, and a Repairs projection is created only where **DL-65**'s configuration-invariant eligibility test is independently satisfied — never merely because a target became unavailable. **The scene-controller metaphor is memorialized as explanatory, not as new architecture**: a configured Room or Merged Room vocabulary term behaves like a named button on a preconfigured scene controller — recognized vocabulary invokes a previously configured meaning rather than triggering runtime discovery — and this illustrates, without replacing, the existing configuration-time semantic definition, deterministic lookup, and bounded target selection already accepted in [room-configuration.md](../models/room-configuration.md) and [contextual-vocabulary.md](../models/contextual-vocabulary.md); it does not mean every phrase becomes a Scene, that a Merged Room is a Scene, or that Identity, Operational Trust, Assist Exposure, or current native state are ever bypassed. **Command-routing, no-match, and native-fallback requirements are explicitly not decided here**: they belong to **OD-62**, which owns custom sentence and intent definition and the retrieval/command surface, and are recorded there as evidence, not settled by this closure | Creating a native Area, Floor, Label, or Group to represent a Merged Room; a native construct invented merely for hypothetical dashboard or automation convenience; Assist/Conversation resolving Merged Room vocabulary natively instead of through HTBW's pre-resolved target set; treating a Scene or group as the Merged Room itself; a Repairs projection created merely because a constituent target became unavailable | [../models/room.md](../models/room.md), [../models/room-configuration.md](../models/room-configuration.md), [../models/contextual-vocabulary.md](../models/contextual-vocabulary.md), [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md) |

| **DL-69** | **Resolves OD-62.** **Scope amendment recorded, not silently made**: OD-62's own written scope was governed conversational *retrieval* (current-state answers, explanations, historical-boundary confirmation); this closure explicitly *expands* it, at the architecture-owner's direction, to also cover governed conversational *command resolution* and to elevate **Vocabulary** to a first-class HTBW concept — because command resolution already lived, unnamed, inside the accepted Contextual Vocabulary/Room Configuration model (**DL-09**, **DL-10**), and formalizing it here closes a real gap rather than inventing a second retrieval authority. **Home Assistant's own documented Voice architecture is retained in full and is not duplicated**: Assist Pipeline (wake word → STT → Conversation/Intent → TTS), the Conversation integration and its custom-agent extension point, the Intent framework (`intent_type`, `slots`, `text_input`, `language`), and the Conversation API's three response types (`action_done`, `query_answer`, `error` with `no_intent_match`/`no_valid_targets`/`failed_to_handle`/`unknown`) are the verified native facilities HTBW extends (`https://developers.home-assistant.io/docs/voice/overview/`, `https://developers.home-assistant.io/docs/intent_conversation_api`, `https://developers.home-assistant.io/docs/intent_index`, `https://developers.home-assistant.io/docs/core/entity/conversation`). **No confidence score, alternative transcript, or device/area metadata beyond an optional pipeline-level `device_id` is documented as available to a conversation agent** — none is claimed. **Custom sentences** (sentence triggers extending or creating an intent, with slots and a templated conversation response) are the verified native extension point for household-declared phrases (`https://www.home-assistant.io/voice_control/custom_sentences/`). **Vocabulary is accepted as a first-class HTBW concept, without creating a new responsibility**: it is the governed household-language layer, already owned by Foundation/Room Configuration (**DL-09**, **DL-10**) for Room- and Merged-Room-scoped terms, and now explicitly extended — under that same ownership, coordinated through Person Setup — to Person-scoped terms for Person-owned capabilities (a configured mailbox, calendar, or news source may be called "Mail", "Inbox", "Calendar", "Schedule", "News", or "Brief" per Person, exactly as **person-and-identity.md** already references those capabilities "through the responsibility that governs their use"). **Vocabulary is not a native identifier, a formal Asset name, a provider name, a globally unique registry name, a permission, an exposure decision, an execution authorization, identity proof, or an uncontrolled prompt synonym**; native Home Assistant Assist aliases remain a distinct, separately governed concept (**OD-14**) that may only ever *seed* a Vocabulary term, never define or synchronise with it. **Vocabulary is contextual, not globally unique**: the accepted context types are Physical Room, Merged Room, Person, Household, Capability, and Interaction (active clarification). **A tested precedence order is accepted for resolving which context applies**: (1) an active clarification context from the same interaction; (2) current Person context, for a Person-owned capability; (3) the current exclusive Merged Room (**DL-67**); (4) the current Physical Room; (5) native handling, only under the governed fallback rule below. **A sixth, Household-wide inherited tier is explicitly not accepted here and remains OD-13's own open question** — this order does not assume inheritance from Home scope exists, and OD-13 alone may add or reject that tier. **Vocabulary target shapes are formalized, none of them new**: single target, named target set, category set, Asset, service/information capability, Person-scoped service, governed execution outcome, and retrieval class — each already a configuration mapping to stable native references, per the existing "no entity-state copy, no parallel registry" rule (**DL-31**). **Vocabulary cardinality is a configuration property, never an English-grammar algorithm**: a household may configure a collection term (for example "Lamps") whose target set has more than one member, and may separately configure member-level terms (for example "Sofa Lamp", "Corner Lamp", "Reading Lamp") for the same members; **language-specific singular/plural morphology is implementation mapping, never constitutional architecture**, and no add-s or other language-specific rule is prescribed. **This reconciles, rather than overrides, the existing accepted rule that a plural form never creates or expands a group and that a derived recognition form resolves to exactly its authoritative term's target set** (`contextual-vocabulary-contract.md`): where a household has *not* configured member-level terms, a singular derived form of a configured collection term continues to resolve to that term's whole target set exactly as already accepted; where a household *has* configured distinct member-level terms for members of a collection, a singular utterance that could equally match more than one of those already-configured member terms is the existing `ambiguous` state (**more than one configured mapping matches**), resolved by the existing failure-behavior rule — **ask which was meant, offering only exposed, contextual, member-level terms, never full native names, never unconfigured devices, never targets outside the resolved Room or Merged Room context**. **The command-resolution sequence is unified and Merged-Room-aware**: Home Assistant's documented Assist Pipeline stages run; the receiving endpoint supplies its Room assignment as the default Room Context; the exclusive Merged Room (**DL-67**) is resolved if applicable; HTBW evaluates the utterance against configured Vocabulary in the resolved context (Physical Room, Merged Room, or current Person, per the precedence above), compiling to a concrete governed target set **before** any native targeting occurs (**DL-68**); Identity, Operational Trust, Assist Exposure (**DL-66**), HTBW Exposure, consent, audience, and confirmation are evaluated; execution uses the closest accepted native Intent, service, script, scene, or HTBW entry point; **native fallback is considered only afterward, and only where safe.** **A failed HTBW vocabulary match must never silently authorize an unrelated or materially broader native action** — this is the accepted resolution of the architecture-owner's "Bedtime" failure scenario. Six outcomes are distinguished: a **deterministic HTBW match** executes after governance checks; an **ambiguous HTBW match** clarifies from bounded, contextual, exposed candidates only; **no HTBW match with an exact, permitted, exposed, and safe native candidate** may hand off directly; **no HTBW match with a plausible but non-equivalent native interpretation** must never execute silently — it clarifies, replays what was heard, or safely refuses; **no HTBW match and no safe native match** returns an honest no-match response; and **recognized text carrying residual uncertainty** may only be replayed or offered as a bounded "did you mean" suggestion drawn from already-configured Vocabulary or a verified-safe native target — never an open-model invention, never executed before confirmation, and always preserving the original transcript. **No recognition-confidence claim is made**, because none is documented as available. **A generic activation command (for example "turn on the lamps") preserves the household's existing accepted state rather than forcing a changed one**: **Continuity already owns "last lamp levels" as accepted Person- and Room-scoped state** (`continuity.md`) — a generic command consults that existing record where one exists, and Home Assistant's own documentation states only that `light.turn_on`'s brightness, color, and other parameters are *optional*, never that omitting them universally restores a prior level; the exact device/integration-level outcome for a target with no recorded Continuity level remains implementation mapping, verified individually under **DL-30**, not claimed here. **Explicit requests for a specific level, color, or scene are unaffected** and always take the state the resident asked for. **Conversational retrieval classes are enumerated** (current non-sensitive state; current Provider-Derived Environmental Indicators, with provider attribution preserved per **DL-62**'s clarification; current Stewardship status, subject to Identity/audience/privacy rules; recent Decision Trace explanation, resident-safe per **DL-46**; current obligations; and honest unknown/unavailable outcomes) — **historical reconstruction and movement-history questions are explicitly excluded and remain OD-35's own retrieval-surface question**, never reachable through this or any generic capability (**DL-35**). **Filtering occurs before an answer is assembled, never by post-hoc redaction**: capability classification, source identification, current actor/Unknown Person determination, audience composition and its uncertainty (**DL-34**, evidence routed to **OD-71** for its own default policy), access threshold, presentation threshold (**DL-36**), Assist Exposure and HTBW Exposure (**DL-66**), and reconstruction-class exclusion (**DL-35**) are all evaluated before content is constructed; only the authorized answer or bounded candidate list is ever built. **An honest response vocabulary is accepted, extending rather than replacing the existing governed fallback vocabulary** (`failure-and-degradation.md`): Unknown, Unavailable, Not understood, Clarification required, Not authorized, Cannot answer here, and Unsupported are distinguished, and the spoken wording is itself audience-safe — *"I can't answer that here"*, never a sentence that discloses the very thing being withheld. **Decision Trace requirements are extended** (`decision-trace.md`) to carry the receiving endpoint, recognized text, Vocabulary context and match, singular/plural interpretation, candidate and clarification sets, suggested alternative, native-fallback candidate, match classification and no-match reason, and the pre-answer filtering outcomes, without creating a second explainability model. **Ownership is unchanged**: Home Assistant owns its native Voice pipeline, entities, services, scripts, scenes, and automations; Foundation/Room Configuration owns Vocabulary's definition and Room/Merged-Room mappings; Person Setup coordinates Person-scoped Vocabulary; Identity owns current-person evidence; Operational Trust owns every threshold, audience, and confirmation decision; Truth owns Facts; Stewardship owns obligations; Concierge owns answer assembly, clarification, and execution coordination; **Conversation owns nothing.** **No parallel Voice pipeline, no parallel native execution engine, and no second entity, device, Room, Asset, or conversation-history store is created.** OD-13 retains inheritance/override/collision/transitivity/morphology questions; OD-29 retains trace persistence location (independent of this closure); OD-30 retains full surface enumeration for trace visibility (this closure supplies evidence that Conversation is one such surface, audience-filtered); OD-35 retains the historical-reconstruction retrieval surface; OD-67 remains explicitly independent, as its own text already states; OD-71 retains the audience-uncertainty default policy | Vocabulary treated as a native identifier, a permission, or an exposure decision; a parallel Voice, Conversation, Intent, or execution engine; a new Vocabulary or Conversation responsibility; recognition-confidence claims without documentation; silent broader native fallback on HTBW no-match; post-hoc redaction as a substitute for pre-answer filtering; historical reconstruction answered through generic retrieval; an English-only cardinality algorithm treated as architecture | [../models/contextual-vocabulary.md](../models/contextual-vocabulary.md), [../contracts/contextual-vocabulary-contract.md](../contracts/contextual-vocabulary-contract.md), [../models/room-configuration.md](../models/room-configuration.md), [../models/decision-trace.md](../models/decision-trace.md), [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md), [../architecture/failure-and-degradation.md](../architecture/failure-and-degradation.md) |

| **DL-70** | **Resolves OD-13.** **Does not reopen DL-69**: Vocabulary remains first-class, under the same Foundation/Room Configuration ownership, coordinated through Person Setup for Person-scoped terms. **Four Vocabulary scopes are accepted**: Home (the household-facing "Global"), Room, Merged Room, and Person. **A Physical Room and a Merged Room behave identically in every respect once configured** — Vocabulary, devices, Assets, services, personas, environmental outputs, execution targets, and explainability all follow the same rules (**DL-13**, **DL-67**); **the only difference is the candidate pool offered during setup** — a Physical Room's candidates are objects assigned to that Room, a Merged Room's candidates are objects assigned to any of its constituent Rooms (**room.md**'s existing "Participation is explicit" rule, unchanged) — and no separate inheritance logic is created for Merged Rooms. **A term may be defined at Home scope and is accepted as inherited everywhere no narrower term exists**; **a Room or Merged Room may shadow a Home-scoped term** with its own definition, which applies only within that Room or Merged Room and leaves the Home-scoped term unaffected everywhere else — this is shadowing, never replacement, and never a second copy. **DL-69's context-precedence order is extended by exactly one tier, in the position DL-69 itself reserved**: active clarification → current Person, for a Person-owned capability → current exclusive Merged Room → current Physical Room → **Home (Global) scope** → native fallback, only under the governed no-match rule. **Vocabulary and Fulfillment are formally distinguished as separate concerns (Option D), in addition to the shadowing rule, not instead of it**: Vocabulary is the household word; Fulfillment is which provider, target, script, Asset, capability, or source currently satisfies it. **A Vocabulary term may remain Home-scoped and stable while its Fulfillment varies by Room, Merged Room, or Person** — confirmed by existing Concierge implementation evidence, where `weather_source_entity_ids`, `news_source_entity_ids`, and Person `email_source_ref`/`calendar_source_ref`/`shopping_source_ref` are already Room-, Merged-Room-, and Person-scoped Fulfillment fields independent of any word chosen for them. **Person Vocabulary is confirmed restricted to Person-owned capabilities and resources** (a configured mailbox, calendar, shopping list, or similar) **and never redefines Room- or Merged-Room-owned device Vocabulary**: DL-69's own precedence order already gates Person context to "a Person-owned capability," and allowing a Person to redefine a Room's device term would break DL-69's "two voice assistants in the same Room produce the same target resolution" invariant by making the same utterance in the same Room resolve differently depending on who spoke — no accepted architecture supports that, and none is introduced here. **Collision behaviour is stated for four cases**: (1) the same word in two different Rooms is not a collision at all — ordinary Room scoping, already accepted; (2) two simultaneous definitions of the same word in the *same* scope is a configuration-invariant violation, never silently arbitrated at runtime — setup must prevent it, and where it nonetheless occurs it is evaluated as a **DL-65** Repairs candidate (a configuration invariant ordinary runtime evaluation cannot resolve), exactly as a duplicate Primary Authority already is; (3) Home versus Room is shadowing, as stated above; (4) Person versus Room is valid only where the Person-scoped term genuinely names a Person-owned capability and is resolved through the precedence order above — a Person is never permitted to redefine a Room- or Merged-Room-owned device term, which remains Room Configuration's sole authority. **Floor participation is explicitly deferred**: **OD-10** remains open, and no Floor Vocabulary scope is created ahead of it. **Asset relationship (how a Person may engage with an Asset) is confirmed already separate from Vocabulary (what Asset is being referenced) and is not decided here**: Vocabulary resolution already carries no permission implication (existing Contextual Vocabulary Contract rule), Asset's own model already carries `owner-of`/`caretaker-of` as Foundation relationship *types* with Stewardship owning the caretaker assignment, and engagement authority is Operational Trust's; the architecture-owner's specific "default Guest, Person record holds only exceptions" sparse-declaration proposal is **not adopted or invented here** — it is recorded as evidence toward **OD-52** (Audience Specification), which already anticipates exactly this through the blocked "Guest-asset interpretation" scenario, and is not decided or preempted by this closure. **Explainability is extended** (not replaced): the Decision Trace's existing Vocabulary field group (**DL-69**) now also carries the winning scope, any shadowed/losing scopes, whether the term was inherited or Room/Merged-Room/Person-explicit, and the Fulfillment source actually used — enabling *"here, News means the household's News term, using the Den's configured sources"* as a single resident-safe sentence. **A known Concierge implementation gap is recorded, not fixed**: the current device/entity Vocabulary resolver treats an unscoped registry entry as matching only an unscoped (no Room, no Person) resolution call, and does not yet fall back to a Home-scoped entry when resolving inside a specific Room — this is implementation mapping for a future change, not an architectural blocker. **OD-86 is confirmed unaffected and not absorbed**: OD-13 governs Vocabulary across scopes at a point in time; OD-86 governs what the household is owed when a term changes or withdraws across time, within a scope | A new Room-Merged-Room behavioral distinction beyond candidate selection; a Person redefining Room-owned device Vocabulary; silent runtime arbitration of a same-scope Vocabulary collision; a Floor Vocabulary scope created ahead of OD-10; a new Asset-engagement classification invented inside a Vocabulary decision; Fulfillment conflated with Vocabulary | [../models/contextual-vocabulary.md](../models/contextual-vocabulary.md), [../contracts/contextual-vocabulary-contract.md](../contracts/contextual-vocabulary-contract.md), [../models/room.md](../models/room.md), [../models/room-configuration.md](../models/room-configuration.md), [../models/decision-trace.md](../models/decision-trace.md) |

| **DL-71** | **Resolves OD-52.** **Scope boundary stated first**: this decision defines Intended Audience Specification only — who a Communication or Stewardship obligation is *for*, and how a specification resolves to Persons. It does **not** decide the escalation ladder (**OD-22**), the Communication/Delivery-Attempt lifecycle enumeration (**OD-44**), acknowledgement semantics (**OD-45**), retention (**OD-49**), retry policy (**OD-54**), or the default policy for uncertain audience composition (**OD-71**, unaffected) — each is confirmed, by its own issue text, to depend on or be independent of this closure, and none is decided here. **"Person Extension" is adopted as a household-facing collective name, not a new object**: **DL-31**'s "distributed, each extension keeps its own owner" is reaffirmed unchanged — Foundation keeps roles, relationships, and consent; Identity keeps evidence associations; Continuity keeps preferences; Operational Trust keeps authority and disclosure policy; Stewardship keeps obligations and relationship assignments; Room Configuration/Person Setup keeps Person-scoped Vocabulary (**DL-69**, **DL-70**). Person Setup remains the shared configuration *experience* across that distributed ownership; no unified store is created. **Guest fallback**: a household may designate **exactly one** existing, deliberately configured Person (ordinarily a **Known Non-Resident Person**, **DL-33**) as the default Person Extension consulted when Identity yields **Unknown Person**. Consulting that designated Person's own distributed settings (permissions, Vocabulary, preferences) as interaction defaults **creates no Identity Assertion binding Unknown Person to it** — Unknown Person remains exactly what **DL-33** already states, in every record, including the Decision Trace. The designated fallback Person Extension may hold resources, Vocabulary, permissions, and relationships if the household deliberately configures them; **none of that is prohibited by default**. Where no fallback is designated, existing **DL-33** household-neutral treatment applies unchanged. **A known, remembered Person who is configured at guest-level permission gains no additional authority from being recognized**: this requires no new mechanism — **DL-36**/**DL-39** already hold access and presentation independent of identity confidence, and *"Sarah is recognized and remembered"* is fully satisfied by Sarah's own Person Extension being configured at guest-tier, evaluated exactly as any other Person's would be. **A real Concierge implementation finding is recorded, not fixed**: `PreferenceIdentityState.GUEST` is used as a peer of `KNOWN`/`UNKNOWN` in a personalization-eligibility helper; under this decision it must be understood, and should be reframed at implementation time, as "the personalization decision is being evaluated under the designated fallback Person Extension because Identity's own state is `unknown`" — never as a fourth Identity state, which **DL-33**/**DL-38**/**DL-39** do not recognize. **Copy Settings From Person is a setup-time convenience, never a Role or runtime inheritance mechanism**: it may copy only permissions and allowed interactions, Person Vocabulary, and preferences/presentation defaults; it **must never** copy mail accounts, calendars, shopping lists, voiceprints, phones, presence devices, email addresses, delivery devices, Person-specific services, relationships, caretaker assignments, Asset ownership, consent records, historical activity, identity evidence, or any other Person-bound resource. The copied values are persisted directly into the destination Person Extension's own distributed records; the destination is immediately independent; **no synchronization and no runtime inheritance exist**; runtime reads only the destination Person's own configured values. A later "Reset copied settings from Person" is a new explicit copy, never a resumed link. **No general runtime Role hierarchy is created**: the existing **Role** concept (a named position — resident, owner, child, guest, service provider — used by Operational Trust to derive authority) is unchanged and unextended; any informal household label for a copy-settings pattern is setup metadata only, never an authorization construct. **The relationship model required now is exactly one: `caretaker-of` (already accepted, Foundation-typed per the asset model and **DL-49**), formally clarified as many-to-many** — one Person may be caretaker-of many subjects (a Person, Pet, or Asset), and one subject may have many caretakers — **no broader relationship taxonomy is invented**. Stewardship remains the single authority for the current assignment records (already stated: "Foundation defines the relationship; Stewardship owns the assignment"); the Person view ("Relationships: Caretaker of Maisey, Caretaker of Piano") and the subject view ("Caretakers: Tom, David") are **both projections over the same assignment records**, never independently editable copies. **Accountability is not access, unchanged (DL-57)**: resolving "Caretaker of Maisey" to candidate Persons via the relationship record is necessary but not sufficient — each candidate must also hold a currently valid **Delegated Access Grant** with at least the `receive` operation to become an Authorized Recipient, and at least `complete` to close a shared obligation; a bare relationship never itself grants authority. **Five Intended Audience Specification forms are accepted**, refining the existing table rather than replacing it: **(1) Named Person** — one identified Person, resolved by direct reference, no Assertion Purpose beyond identifying the object; **(2) Role / Authority Class** — a named position or stated authority, unscoped to any subject, resolved by Operational Trust against currently eligible Persons holding it; **(3) Relationship-based** (new, formalizing "Caretaker of X") — a predicate scoped to a specific Subject, resolved through Stewardship's current assignment records, never through presence or identity evidence, and cross-checked against **DL-57** for actual authorization; **(4) Anyone Present With Authority / whoever is home** — resolved against current Room or Household Presence (Truth, an explicit Assertion Purpose) crossed with Operational Trust's current authority evaluation; **(5) Household** — all residents, via Foundation's roster. Every form carries a canonical name, an owner, a resolution source, an Assertion Purpose where evidence-based (Relationship-based and Household have none — they are configuration lookups, not evidence), a resolution time, an uncertainty outcome, a no-recipient outcome, a too-broad outcome, mandatory Operational Trust evaluation, and Decision Trace evidence. **Re-resolution**: the original specification is fixed at origination and never rewritten; the *resolved recipient set* is re-evaluated at each Delivery Attempt for a dynamic form (Relationship-based, Anyone-Present) — extending the existing "visibility is never stored resolved" principle from composition to specification resolution; prior Delivery Attempt records are never rewritten by a later relationship change; escalation (**OD-22**) creates or records a new specification rather than silently mutating the original. **Resolved to nobody**: the Communication is never silently discarded, never redirected to a convenient Person, and never sent broadly by default; Stewardship's existing "a caretaker is unassigned → report an accountability gap, escalate per policy" failure behaviour applies unchanged; a Repairs projection is created only where **DL-65**'s own configuration-invariant test is independently satisfied. **Resolved too broadly**: not itself an error; Operational Trust evaluates content sensitivity, current identity confidence, audience composition, Authorized Recipient status, and Delivery Surface capability exactly as already accepted (**DL-34**, **DL-53**), and where the audience cannot be safely determined, delivery degrades and the Communication is preserved — disclosure is never broadened and the audience is never assumed known. **Notice and completion semantics are fully expressible under already-accepted architecture, and no new object or state machine is created**: no "Notice" object is introduced — household "Notice" language is Stewardship's Obligation (what matters) plus the Communication(s) that convey it, two already-separate, already-owned concepts. **One Completion Satisfies All** is one Stewardship obligation record naming multiple accountable caretakers, each already able to hold the `complete` operation of a **DL-57** Delegated Access Grant over the same record — closing it once, for everyone, exactly as **DL-48**'s Care Evidence Record already works; **Each Recipient Must Complete** is the same existing obligation model applied as multiple independent obligation records, one per accountable Person, each closed by its own Care Evidence Record. "Completion Mode" is accepted **only as explanatory vocabulary** describing which of these two existing configurations was used — never a new stored state. The existing **Caretaker-calendar projection** already guarantees a clean open list: it is a live, read-time projection over the one governed obligation record, exactly like the Household Inbox, so a shared item's closure is reflected for every caretaker without a stored per-recipient duplicate ever existing to clean up. **Completion (Stewardship), Acknowledgement (OD-45), and Delivery/Presentation Outcome (OD-44/DL-54) remain three distinct, already-separated concepts and are not collapsed here** | A single unified Person Extension store; Unknown Person treated as, or silently becoming, a known identity; a fourth Identity state named "guest"; a general Role hierarchy or Role-template store; runtime inheritance or synchronization from a copy-settings source Person; a broad relationship taxonomy invented to close this decision; independently editable relationship copies in Person and Asset/Pet records; a bare relationship treated as access authority; a new Notice object; a new Stewardship completion state machine; silent broad disclosure when an audience resolves to nobody or too broadly | [../models/communication.md](../models/communication.md), [../models/person-and-identity.md](../models/person-and-identity.md), [../models/stewardship.md](../models/stewardship.md), [../contracts/stewardship-contract.md](../contracts/stewardship-contract.md), [../models/operational-trust.md](../models/operational-trust.md), [../models/decision-trace.md](../models/decision-trace.md), [../models/glossary.md](../models/glossary.md) |

| **DL-72** | **Resolves OD-71. DL-34 is not reopened**: Audience Composition still identifies nobody, is never a second identity fusion, and its existing states — Unresolved plurality, Audience unknown, Audience detection unavailable — remain exactly as accepted, each now consumed rather than redefined. **System-Initiated Communication and Person-Requested Response are formally distinguished, neither previously named**: a System-Initiated Communication is one HTBW originates without a current explicit request (a medication reminder, new private Mail, a Calendar reminder, a Stewardship warning); a Person-Requested Response answers a Person's current explicit request ("What is on my Calendar?", "Read my Mail", "Send that to my phone"). **The explicit request is evidence of the requestor's willingness to receive an authorized response through the current interaction context — it is never unrestricted consent** and is bounded: it does not authorize disclosure of another Person's information, does not reach a prohibited reconstruction (**DL-35**), does not satisfy insufficient requester authority or applicability, and is void where the current surface cannot safely present the response. *"Read that here"* is evidence of willingness for this interaction only; *"send that to my phone"* resolves the **requestor's own** authorized private destination, never a convenient or nearby device. **The accepted default policy for a System-Initiated Communication under audience uncertainty is an ordered path, evaluated in this order, not a mandatory sequence of every step**: (1) authorized private delivery to each intended recipient's own configured destination, where available and qualified; (2) content-free Indication, where its own audience evaluation and **OD-57**'s eventual mandatory-threshold rule permit it; (3) a neutral confirmation or clarification challenge that names no candidate, subject, relationship, or sensitive content, where a genuinely neutral form exists; (4) deferral or refusal of audible delivery, preserving the Communication for retry (**OD-54**) or escalation (**OD-22**). **This is the privacy-preserving floor and applies even where no household configuration exists** — a missing configuration must never result in audible private disclosure. **Two Person Setup preferences are formally distinguished, where only one previously existed informally**: **Ordinary Delivery Preference** (already Continuity's, per `stewardship-use-cases.md` and `communication.md` — where Communications normally go) and the new **Audience-Uncertainty Routing Preference** (also Continuity's, evaluated for permission and safety by Operational Trust exactly as the ordinary preference already is) — where should a Communication route *when audience composition cannot be safely established*. **The uncertainty preference is not an Audience Composition claim, not a statement that a device is always private, not a bypass of Operational Trust, not a substitute for Delivery Surface capability, and not a request to identify the Room** — it supplies a desired degradation path; Operational Trust determines whether that path is currently permitted; Concierge selects the Delivery Target. A household-wide Global default (accepted as "prefer authorized private delivery") applies where no Person-specific preference exists; **a Person preference may select among already-allowed degradation behaviours and may never weaken the privacy floor or authorize a prohibited disclosure**. **Authorized Private Delivery Surface criteria are extended, not replaced**: the existing rule (target association, authenticated user, governed device binding, delivery capability, audience restriction, content classification, applicable policy — `communication.md`) now additionally requires sufficient Potential Perceptibility evidence for the attempted delivery (**DL-53**), current availability, that the surface is **not known to be shared** and **not merely nearby**, a currently governed device-Person association, and the required Presentation Outcome support (**DL-54**); the selection must be explainable. **No platform capability to detect lock-screen state, current physical possession, or shared-device status is claimed** — where the platform cannot establish privacy, the uncertainty is retained and the next degradation step applies; this remains an **OD-43**/**DL-30** implementation-time verification, not an architectural claim. **A phone, wearable, or dashboard is only potentially private and must pass the full test; a shared tablet, shared phone, television, Room display, kitchen dashboard, or Room speaker is never automatically private.** **Unresolved plurality, Audience unknown, Audience detection unavailable, and contradictory evidence remain four distinct diagnostic conditions, not one**: the first three are **DL-34**'s own existing composition states, consumed here rather than redefined; contradictory evidence, if it remains a genuine conflict after **DL-63**'s qualification order, is treated identically to the other three for disposition purposes (the same default order applies) while the Decision Trace preserves which condition actually applied. **Room and Merged Room receive identical treatment, with no second rule**: a Merged Room's wider constituent-Room Potential Listener and Delivery Surface pool changes the composition **inputs** Operational Trust evaluates, never the policy itself (**DL-13**, **DL-67**–**DL-70**). **Content-classification and Mode variation are acknowledged as legitimate inputs and explicitly routed rather than decided**: the risk-class enumeration is **OD-51**'s; the mandatory-versus-optional threshold for Indication is **OD-57**'s; Mode (an already-accepted governed Room or Home state) may be consulted as an input without any new Mode value being invented here. **Content-free Indication remains the accepted degradation path (unchanged) and is itself audience-evaluated as a Communication**: it must disclose no recipient identity, subject, content, private relationship, sensitive content class, or the existence of a concealed resource — *"there is a private notification available"* is illustrative of a safe form; *"Tom, you have a medication reminder,"* *"someone has a medical notice,"* and *"the caretaker of Maisey has a reminder"* each illustrate an unsafe one. **A neutral confirmation or clarification challenge is bounded by information class, not by prescribed wording** (**DL-37**): it must never name a candidate Person, a private subject or resource, a caretaker relationship, the sensitive action or content, or protected history; *"would you like that sent privately?"* and *"where would you like the response?"* illustrate permitted forms, while naming a candidate ("Tom, is that you?") or a relationship ("are you Maisey's caretaker?") illustrates a prohibited one under uncertainty. **Guest fallback and Unknown Person remain exactly as DL-71 already states**: the designated fallback never becomes a private Authorized Recipient, never supplies or receives another Person's redirected Communication, and Unknown Person remains Identity's own state; an Unknown Person's possible presence is itself one of the uncertainty conditions this default policy already handles, requiring no separate rule. **Multiple relationship-based recipients (DL-71) are evaluated independently**: each candidate's private-surface qualification and uncertainty preference are assessed separately, delivery to one never establishes delivery to another, each is its own Delivery Attempt, and the underlying shared Stewardship obligation (One Completion Satisfies All, where configured) remains singular and distinct from delivery or acknowledgement. **Delivery degrades; governance does not (P32, DL-29, reaffirmed unchanged)**: the Intended Audience, content classification, and authorization requirements never change under uncertainty; only the Delivery Target and Presentation Outcome may; the audience is never broadened, a Room speaker is never treated as private, non-detection is never treated as solitude, the original Communication is never rewritten, and Indication is never reported as content delivery | Reopening DL-34 or its composition states; treating a Person's explicit request as unrestricted consent or as authorization for another Person's information; a mandatory-every-step degradation sequence; a device presumed private by type alone; an invented lock-screen or shared-device detection capability; a second Merged Room uncertainty rule; a new Mode value or risk-class enumeration; a prescribed neutral-challenge sentence; Guest fallback treated as a private Authorized Recipient; independent recipients collapsed into one delivery record; broadened disclosure, or Indication reported as delivered content, under uncertainty | [../models/communication.md](../models/communication.md), [../models/operational-trust.md](../models/operational-trust.md), [../models/continuity.md](../models/continuity.md), [../architecture/privacy.md](../architecture/privacy.md), [../models/decision-trace.md](../models/decision-trace.md) |

---

## Part 2 — Open decisions

Each is deliberately unresolved. None blocks the constitutional foundation.

> **GitHub issues are the authoritative source for the current status, remaining questions,
> dependencies, and closure evidence of every open decision below.** This ledger remains authoritative
> for **what the decision is** and for every accepted decision in Part 1. The identifier-to-issue
> mapping, with dependency summaries, is
> [open-decision-issue-index.md](open-decision-issue-index.md); the governance backlog Epic is issue
> **#147**.

| ID | Question | Responsibilities affected | Recommended ADR topic |
|---|---|---|---|
| **OD-01** | Home Assistant representation strategy — **partially resolved**. The reference-and-extension rule, the three representation categories, and the object-by-object mapping are accepted as **DL-31** and recorded in [home-assistant-boundary.md](../architecture/home-assistant-boundary.md). **The residual is the persistence shape of Change Records, Snapshots, and Current Projections** — config entry, subentry, or private storage — which **OD-01 now owns alone**. It was previously duplicated in **OD-34**; OD-34 has closed on the persistence *model*, and this mechanism question was not carried with it. **Narrowed by verified platform documentation**: config entries and subentries are **user-created, user-removable configuration data**, which makes them structurally unsuitable for immutable historical records. It **remains open** because the Storage helper documentation could not be verified. Classification mechanics are **OD-68**, Entity projection is **OD-69**, Merged Room projection is **OD-70** | Foundation, Room Configuration | Governed-record persistence shape |
| **OD-02** | **Resolved as DL-43, DL-44, and DL-45.** The question was the connected-storage **format** for vocabulary, participation, and documentation. Its architectural content was how HTBW **locates and governs** an externally stored record, and that is answered by the **governed artifact reference contract** — stable identifier, class, owning responsibility, creating capability, governing parent, native anchor, storage class, relative locator, lifecycle policy, retention, deletion trigger, consent and preservation effects, availability, broken-reference, and reconciliation state — together with the artifact declaration and interaction model required of every class. **No universal payload schema is required, and file formats remain capability-specific.** Remaining encoding choices are per-capability implementation | Foundation, Room Configuration | **Closed — DL-43, DL-44, DL-45** |
| **OD-03** | **Resolved as DL-42, DL-44, and DL-45.** The question was storage technology, encryption, and synchronisation. **Home Assistant is the storage provider**: it owns protocol selection, mounting, credentials, and network-storage administration, and HTBW selects none of them. What HTBW must own is settled by DL-44: **one governed namespace, separation by artifact-owning function or class, collision-resistant references, no resident-supplied path or display name as an identifier, traceability to the governing object, no cross-capability mixing, removable empty structures, and migration through governed references**. Exact root and folder names, path depth, and file naming are **implementation mapping**. Encryption, backup, replication, and quota belong to Home Assistant or the deployment, and **HTBW records no unmet requirement against them** | All | **Closed — DL-42, DL-44, DL-45** |
| **OD-04** | Exact global priority order across policy scopes, **including the ordering applied to competing Communications**. **Unchanged by DL-36.** Threshold and confirmation requirements are ordinary policy statements resolved by the existing precedence order and the existing most-restrictive rule; **they introduce no new precedence mechanism, no threshold-specific ordering, and no override path**. A household default, a Room policy, a capability requirement, and a per-operation requirement compete exactly as any other policies do, and **a Person preference is never a permission** | Operational Trust, Concierge | Policy precedence order |
| **OD-05** | Decision Trace retention **floor and ceiling** — how long a trace must be kept to satisfy P27, and how long it may be kept under privacy minimisation. **Narrowed by DL-47: the rule is settled — a trace is governed explainability history following External History Retention unless an accepted floor or a Preservation Hold applies, and holding a trace preserves the versions that keep it explainable. Only the values remain** | Concierge, Operational Trust | Trace retention floor and ceiling |
| **OD-06** | **Resolved as DL-56.** Consent user experience — the scope model, canonical record, Person Setup as the capture/review surface, self/proxy consent, contextual continuity, withdrawal/deletion, the DL-43/DL-47 reconciliation, duration, historical explainability, and the six consent/authorization states are accepted. The observation-versus-Person-Association boundary is now explicit. Proxy-authority qualification resolved as **DL-57**; exceptional legal/incident correlation is tracked separately as **OD-89** | Identity, Operational Trust | **Closed — DL-56** |
| **OD-07** | Local versus cloud voice implementation | Identity | Voice processing locality |
| **OD-08** | **Resolved as DL-39 and DL-40.** **Resolved:** Identity produces **exactly four confidence bands** — **Low < Moderate < High < Very High** — carried only by a `known` assertion, describing identity support only, and carrying no access, presentation, personalization, disclosure, audience, confirmation, or authentication meaning. **`None` is not an Identity band**; it is one of five **Required Identity Band** values owned by Operational Trust, meaning *no known-Person identity is required for this operation*. **State and band are separate dimensions**, and an Unknown Person is assigned neither. **Operational Trust owns every threshold**, including **Address by Name**, regardless of configuration surface. **Access and presentation are evaluated independently** and may differ. **Every interaction is evaluated from current eligible evidence**; there is **no long-lived Identity session**, continuous occupancy is not continuous authentication, and **assertion validity is not current-interaction applicability**. **Confirmation is consumed by its protected operation**, has no occupancy grace period, and never changes the band. Per-class and per-capability defaults, the Address by Name default, and the Presentation Threshold default are **configuration**, resolved with **OD-51**'s risk-class enumeration, and are not held open here. Household-facing band **labels** are adopted as **Low, Moderate, High, Very High**; the ordering is authoritative and the labels carry no operational meaning. **Residual discharged as DL-40.** The residual was framed as *which mechanisms* constitute a stronger-than-verbal confirmation, and that framing conflated two separable things. **A required strength is a classification; an implemented mechanism is a platform capability.** Architecture needs only the ordered class set **`None` < Verbal < Authenticated < Strong**, the rule that a capability declares the class it requires, and the rule that a class is satisfied only by a mechanism the deployment has verified as meeting it. **No Home Assistant mechanism is prescribed or assumed** — companion-application, push, PIN, and secondary-factor confirmation remain unverified against official documentation and remain barred from prescription — and where no verified mechanism meets a required class the outcome is `Unavailable`, never a downgrade. Mechanism mapping is deployment configuration and platform capability discovery, not an open architectural question. **DL-37** stands unchanged: the capability declares the strength it requires, and a spoken *yes* remains inadequate for permission changes, enrollment, security configuration, financially consequential action, highly sensitive disclosure, Preservation Hold release, evidence deletion, and administrator changes | Identity, Operational Trust | Closed — DL-39, DL-40 |
| **OD-09** | Export and deletion mechanics, **evaluated against the native History export and history endpoint, and against Backup**. Native export is entity-scoped and ungoverned, and connected storage is outside Backup scope unless the deployment deliberately places it within it | All | Data portability and erasure |
| **OD-10** | Whether Floors are a first-class scope. **The Floor registry developer documentation could not be verified; this must not be closed on assumed Floor-registry behaviour** | Foundation, Operational Trust | Scope hierarchy |
| **OD-11** | **Resolved as DL-67.** A Merged Room is a curated conversational interaction context, not a general grouping mechanism; a Physical Room may participate in at most one Merged Room at a time; overlapping membership would reintroduce the special-case orchestration **DL-13** rejects; broader or capability-specific groupings ("Downstairs") are met by Home Assistant's own native Floor/Area targeting, never by an overlapping Merged Room | Foundation, Room Configuration | **Closed — DL-67** |
| **OD-12** | Whether exclusion reasons are structured or free text | Room Configuration | Exclusion metadata |
| **OD-13** | **Resolved as DL-70.** A term may be defined at Home scope and is inherited everywhere no narrower term exists; a Room or Merged Room may shadow it (never replace it); Vocabulary and Fulfillment are distinguished as separate concerns; Person Vocabulary stays restricted to Person-owned capabilities; collision behaviour and explainability are stated; Floor participation stays deferred to **OD-10**; Asset-engagement defaults are routed to **OD-52**, not decided here | Foundation, Room Configuration | **Closed — DL-70** |
| **OD-14** | **Resolved.** Home Assistant naming information is an **input** to HTBW vocabulary and never an authority. A native name or Assist alias may **seed** a contextual term; the seed is attributed to Home Assistant, is not synchronised afterwards, and is **never written back**. A household-defined term is never overwritten by a native change. Recorded in [../models/contextual-vocabulary.md](../models/contextual-vocabulary.md) and [home-assistant-boundary.md](../architecture/home-assistant-boundary.md) under **DL-31**. **OD-13** is unaffected | Contextual Vocabulary | Resolved — no ADR required |
| **OD-15** | **Resolved as DL-64.** "Assertion lifetime" was a conflation of **Assertion Validity** (permanent historical record, **DL-47**-governed retention only), **Current-Interaction Applicability** (re-evaluated per interaction via fresh **DL-38** fusion from current eligible evidence — no fixed window, no new event, condition-bounded), and **Retention** (already **DL-47**'s, unaffected). No Assertion Purpose requires a fixed validity window. **Cross-purpose assertion eligibility is accepted**: a prior purpose-specific Assertion's contribution to a later different-purpose determination ends when the supporting Room's occupancy transitions to `unoccupied` or the Person's configured primary evidence source leaves that Room. Applicability is evaluated before **DL-63**'s conflict qualification ever runs | Identity, Truth | **Closed — DL-64** |
| **OD-16** | **Resolved.** Identity evidence weighting is complete. The evidence architecture was accepted as **DL-32**, and the **Identity Fusion Function** is now accepted as **DL-38** and recorded in [../models/person-and-identity.md](../models/person-and-identity.md): assertion-purpose-first evaluation, bounded candidate generation, eligibility gating before weighting, the nine fusion rules **F1–F9**, ordered outcome selection, freshness treatment, confidence-output semantics, Fusion Policy versioning, the calibration boundary, and deterministic fixtures. **No mathematics was invented**: the function is ordinal and stepped rather than arithmetic, and it makes no probabilistic claim. **Remaining values are implementation mapping, not architecture** — freshness durations, the number and size of corroboration and reduction steps, the separation margin, per-purpose minimums, and reason-code strings are all **Fusion Policy configuration**, versioned and governed, and none of them is an unresolved architectural question. Band **naming and operational meaning** are now accepted as **DL-39**. Room-granularity ceilings remain bounded by unverified native Room-level detection, which limits one source's ceiling and not the function | Identity | Resolved — accepted as DL-38 |
| **OD-17** | **Resolved as DL-62.** Ordinary Room Environment measurements never aggregate equivalent same-purpose sensors — Room Configuration selects one **Primary Authority** per Environmental Purpose, required and deterministic, identically for a Physical Room and a Merged Room (**DL-13**); Composite Contributor is removed from that ordinary path, narrowing **DL-60**'s disambiguation to Primary Authority / Secondary-Corroborating / Explicit Exclusion. OD-17's remaining and now-accepted content is **Formula-Derived Fact governance** — input availability, provenance, versioning, and failure semantics (never the specific formula, which stays implementation mapping): **Dew Point**'s formula class and versioning discipline are accepted; **Mold Index** and **Condensation Risk** remain unresolved, with no HTBW-endorsed formula invented. **Environmental Coverage, Configuration Completeness, and Room Environmental Stewardship Summary remain DL-61's**, never OD-17's. Consumes, without redefining, **DL-58** Truth Confidence and **DL-59** current-state/validity semantics | Truth, Room Configuration | **Closed — DL-62** |
| **OD-18** | **Resolved as DL-59.** Truth distinguishes Current-State Sources from Point-in-Time Observation Sources; current-state Facts read the most current authoritative Home Assistant state at evaluation time; operational expiration is a DL-25 lifecycle transition materialized through the existing Domain Event mechanism; Truth Confidence (DL-58) is never decayed by elapsed time alone; freshness/validity windows are household configuration, not architecture | Truth | **Closed — DL-59** |
| **OD-19** | **Resolved as DL-63.** A genuine Truth conflict requires the same Subject, predicate, context, and evaluation time, independent eligibility after Truth's qualification order, and mutual incompatibility with no accepted authority/validity/availability/configuration/Identity/Stewardship rule already explaining the difference. Same-purpose environmental sensor disagreement (**DL-62**), native Area proposal divergence (**DL-60**), Provider-Derived Environmental Indicators (post-**DL-62** clarification), and Person/Pet/Asset requirement conflicts (**DL-61**) are confirmed as not Truth conflicts. Identity contradiction remains **DL-38**'s; assertion lifetime and cross-purpose eligibility remain **OD-15**'s, consumed without redefinition. Truth publishes a reduced-confidence Fact, an unresolved Fact, or `unknown`, governed by a versioned Fact-class Conflict Policy; no range-valued Fact is adopted; persistent conflict is recorded through the existing Domain Event mechanism and evaluated against **OD-60**'s Repairs criteria separately from the runtime outcome | Truth, Room Configuration, Stewardship | **Closed — DL-63** |
| **OD-20** | Whether HTBW Core consumes the standalone Asset Intelligence product as an optional evidence source. **Framed by DL-41: if it does, it is a declared capability dependency, and its absence makes the dependent capability unavailable rather than degraded** | Foundation, Stewardship | Optional product integration |
| **OD-21** | How significance is expressed — ordinal band, score, or household vocabulary | Stewardship | Significance representation |
| **OD-22** | Escalation ladder semantics and defaults. **This is the single escalation ladder, and it serves Communications as well as obligations.** Repeating delivery to the same audience is retry, not escalation | Stewardship, Operational Trust | Escalation model |
| **OD-23** | Whether obligations project into HA calendars, `todo` entities, or a connected store. **A `todo` projection does not own the obligation, and item completion is a list state, not proof that care occurred** | Stewardship | Obligation projection |
| **OD-24** | Session-merging algorithm when two people's sessions meet in one Room | Continuity, Concierge | Session merge policy |
| **OD-25** | Resume eligibility window defaults per experience class | Continuity | Resume eligibility |
| **OD-26** | Whether experience history is retained per person, per room, or both, and for how long. **Narrowed by DL-47: experience history is a governed record class following External History Retention with its own Retention Classification; the scoping and duration questions remain** | Continuity | History retention |
| **OD-27** | Whether concurrent same-class sessions in one Room are permitted by default | Continuity | Concurrency policy |
| **OD-28** | The learned-preference lifecycle — how a suggestion is proposed, accepted, rejected, corrected, paused, forgotten, versioned, and revoked, and how acceptance is recorded so that a past adaptive action stays reconstructable after the preference changes (**P26**, **DL-21**). Evidence eligibility is **OD-65** | Operational Trust, Continuity | Learned-policy promotion |
| **OD-29** | Where Decision Traces are persisted — HA Activity, connected storage, or both, **including purge exemption and Governed Reference resolvability**. **Activity records what changed and never why, so an Activity entry is a projection of a trace and never the trace itself** | Concierge | Trace persistence |
| **OD-30** | Which surfaces expose Decision Traces, and to whom | Concierge, Operational Trust | Trace visibility |
| **OD-31** | Whether assessment records are stored in connected storage as first-class documents. **If they are, DL-43 applies and the five artifact declarations must be stated as part of the answer** | Assessment, Foundation | Assessment record storage |
| **OD-32** | Reassessment cadence, per-item or per-home | Assessment, Stewardship | Maturity review cadence |
| **OD-33** | **Resolved as DL-43, DL-46, and DL-47.** The question was the retention floor and ceiling per record class and Fact class, and it presumed a **universal retention matrix**. No matrix is required: **retention is declared inside every lifecycle**, and DL-47 extends that obligation from artifact classes to every governed record class. Every current class now has a rule — Current Projection, Change Record, Domain Event, Snapshot, Decision Trace, Historical Fact, Identity Assertion, Communication, Preservation Hold metadata, Tombstone, and saved projections — with **External History Retention as the ceiling and purge boundary** and **four structural floors that survive any configured window**: Tombstones, consent-lifecycle records, held records, and the versions required to keep a held trace explainable. Per-Fact-class differentiation is an Operational Trust **policy** matter. The remaining numeric values are household configuration and are held by **OD-05**, **OD-26**, and **OD-49** | All | **Closed — DL-43, DL-46, DL-47** |
| **OD-34** | **Resolved as DL-42, DL-44, DL-46, and DL-47.** The question was the persistence strategy for Change Records, Snapshots, Historical Facts, and Decision Traces. The **temporal-persistence model** is complete: what is persisted, referenced, projected, temporary, or saved only on request is settled by the Temporal Record model; ownership is settled by the history-ownership table; immutability, bitemporality, and Version Identity are constitutional; **Home Assistant remains authoritative for native history and HTBW builds no second Recorder** (DL-42); the **Decision Trace is the explainability spine** and durable explanation after native expiry is carried by the accepted Fact rather than by a copied row (DL-46); retention is declared per record class (DL-47); and externally held records follow the governed namespace and reference contract (DL-44). **The residual that remained was never OD-34's**: *config entry, subentry, or private storage* is the **Home Assistant representation mechanism**, stated verbatim in **OD-01**, and it is retained there rather than duplicated here. Serialization, indexing, batching, compression, scheduling, and database technology are **implementation mapping** | All | **Closed — DL-42, DL-44, DL-46, DL-47** |
| **OD-35** | Historical query surface and access, **including access to actor reconstructions and movement histories**, which Operational Trust governs and which must not be reachable through generic Room Help or a general-question capability (**DL-35**) | All | Historical retrieval and access |
| **OD-36** | Reconciliation of deletion and export obligations with retention floors and Preservation Holds, **noting that Recorder offers no per-record purge exemption and that Backup coverage of connected storage must be verified for the deployment rather than assumed**. **Narrowed by DL-45, which adds parent-object cleanup as a deletion trigger and assigns the pending-cleanup and post-recovery reconciliation obligation here rather than to a new decision. The unresolved question is unchanged: how a deletion obligation and a preservation obligation are reconciled when they conflict** | Operational Trust, All | Deletion versus preservation |
| **OD-37** | Snapshot triggers, cadence, and scope per responsibility | All | Snapshot policy |
| **OD-38** | Version identity, correlation, and causation identifier strategy, **including evaluation of Home Assistant Context IDs**. Context may support correlation, may support an initiating-to-resulting relationship where Home Assistant supplies a parent context, and may support resident attribution only where the platform supplies an attributable user. **Context does not establish semantic reasoning, does not replace Version Identity, does not replace a Decision Trace, and does not prove causation beyond the documented relationship** | Foundation, All | Identifier and correlation strategy |
| **OD-39** | Preservation Hold authority, duration, review, release, and conflict with deletion. **Bounded by DL-43: a hold is a marker on records and is not an artifact class of its own**, so no hold payload store may be introduced while this remains open. **Bounded further by DL-45: a hold survives parent-object removal and cleanup never silently overrides it. Hold release remains separate from parent deletion and remains unresolved** | Operational Trust | Preservation Hold governance |
| **OD-40** | Evidence Package assembly, transport, integrity representation, and audience. **Bounded by DL-43: a package is a projection assembled on demand and is not retained by default**, so no package store may be introduced while this remains open; a deliberately materialised copy is an artifact and must declare its own lifecycle. **Further narrowed by DL-44 and DL-45: a saved package is Managed Content, reached through the owning capability rather than through storage, and its governing parent and Parent Removal Behavior are part of that declaration. Assembly, transport, integrity representation, and audience remain unresolved** | Concierge, Operational Trust | Evidence Package governance |
| **OD-41** | **Incident and Case object model** — whether an Incident remains an ad hoc retrieval scope only, or may become a persisted Incident or Case object. **An Unknown Actor Reference is a reconstruction-scoped projection (DL-35) and does not settle this decision in either direction** | Foundation, Operational Trust, Concierge | Incident and Case object model |
| **OD-42** | Communication object persistence and Home Assistant representation — subordinate to **OD-01**, which now owns the persistence-mechanism residual alone | Foundation, All | Communication persistence |
| **OD-43** | **Resolved as DL-53.** Delivery Surface capability model — what a surface can convey, **to whom it is perceptible**, and whether it can attest presentation. Capability dimensions, Potential Perceptibility, the no-private-surface rule, and the presentation-attestation default are now accepted; a residual **Recipient-Attribution Assurance Levels** proposal was found to duplicate **DL-40** and was resolved by reusing **Required Confirmation Strength** rather than adopting a second scale. Portable-surface Room Context resolution remains **OD-73**; which surface classes can attest remains **OD-55**; audience specification remains **OD-52**; the indication threshold remains **OD-57** | Foundation, Concierge | **Closed — DL-53** |
| **OD-44** | Delivery outcome semantics across the **two levels** — Communication lifecycle state and Delivery Attempt outcome | Concierge, Foundation | Delivery outcome semantics |
| **OD-45** | Acknowledgement semantics — receipt, acknowledger identification, and whether unacknowledged delivery constitutes failure. **Ignoring a Home Assistant Repairs issue is not a person-attributed acknowledgement and must not be adopted as one** | Concierge, Operational Trust | Acknowledgement semantics |
| **OD-46** | Urgency classification **as an Operational Trust entitlement**, its relation to action-risk classification, and its mapping to non-portable platform ladders. **`IssueSeverity` is a developer-facing platform ladder and is not resident-facing Urgency** | Operational Trust | Urgency entitlement model |
| **OD-47** | Household Inbox — **resolved as a projection**. Residual question is projection scope and refresh semantics | Concierge | Inbox projection semantics |
| **OD-48** | Re-presentation preference for outstanding Communications, and its relation to the Follow-Me preference family | Continuity, Concierge | Re-presentation preference |
| **OD-49** | Communication retention floor and ceiling, with **content and metadata classified separately** — formerly subordinate to **OD-33**, which has closed. **DL-47 settles the rule: Communication records follow the governed-record retention model with content and metadata classified separately. What remains is that separate classification itself, and the values** | Operational Trust, All | Communication retention |
| **OD-50** | **Resolved**: there is one escalation architecture. The residual question is the ladder itself, which is **OD-22** | Stewardship, Operational Trust | Resolved into OD-22 |
| **OD-51** | Interruption governance — **resolved** as an Operational Trust action-risk class. Residual question is risk-class enumeration and defaults. **Widened by DL-36 and DL-37: each risk class now carries both a required identity confidence and a required confirmation strength**, so the enumeration settled here is a direct input to the **Required Identity Band** accepted as **DL-39** and the **Required Confirmation Strength** accepted as **DL-40** | Operational Trust | Interruption risk classes |
| **OD-52** | **Resolved as DL-71.** Five Intended Audience Specification forms accepted (Named Person, Role/Authority Class, Relationship-based, Anyone Present With Authority, Household); `caretaker-of` clarified as many-to-many with Stewardship as single assignment authority; Guest fallback is a designated existing Person Extension, never a new Identity state; Copy Settings From Person is setup-only, no runtime inheritance; One-Completion-Satisfies-All and Each-Recipient-Must-Complete are both already expressible under **DL-48**/**DL-57**, no new Notice object or completion state machine created; escalation (**OD-22**), lifecycle enumeration (**OD-44**), acknowledgement (**OD-45**), retention (**OD-49**), retry (**OD-54**), and audience-uncertainty default policy (**OD-71**) remain their own owners' | Operational Trust, Concierge, Foundation, Stewardship | **Closed — DL-71** |
| **OD-53** | Communication category enumeration, and confirmation of the Category × Urgency separation | Foundation, Operational Trust | Communication taxonomy |
| **OD-54** | Delivery retry policy — attempts, intervals, surface progression, and give-up semantics. **Explicitly not escalation** | Concierge | Delivery retry policy |
| **OD-55** | **Resolved as DL-54.** Presentation attestation — which surface classes can attest `Presented`, how `unknown` is represented, and how it is prevented from decaying into *not presented*. The outcome model (Presented / Failed / Unknown / Attestation Unavailable) and the modality-not-device-class evaluation rule are now accepted; per-surface evidence for `media_player`, Sonos, Music Assistant, `assist_satellite`, Roku, Apple TV, LG webOS TV, UniFi Protect camera speakers, mobile notifications, `persistent_notification`, and dashboard/kiosk rendering is recorded in the ADR's Home Assistant First review. Acknowledgement semantics remain **OD-45**; delivery outcome semantics generally remain **OD-44**; retry remains **OD-54** | Foundation, Concierge | **Closed — DL-54** |
| **OD-56** | Safety-category scope — whether HTBW may originate safety-category Communications at all, given the life-safety non-claim | Operational Trust, Stewardship | Safety-category scope |
| **OD-57** | Indication versus content separation — when content-free indication becomes mandatory degradation. Content-free indication is the accepted degradation path when audience composition is uncertain (**DL-34**, **OD-71**) | Operational Trust, Concierge | Indication and content separation |
| **OD-58** | Terminology supersession scope — whether *Notification* and *Message* are formally superseded in the **DL-12** sense | Foundation | Terminology supersession |
| **OD-59** | **Resolved as DL-66.** Native Assist exposure (a platform safety boundary on voice targeting) and HTBW Exposure (Room Configuration's own governed household-facing availability decision, DL-11) are distinct concepts. For voice/conversation-mediated interaction, HTBW Exposure may narrow but never exceed native Assist exposure, and never writes back to it. Non-voice surfaces (UI/dashboard) are independently governed by Room Configuration. Ordinary divergence between the two is never a defect and never Repairs-eligible (DL-65); it is explainable as a deliberate exclusion or a configuration condition. OD-62 consumes this boundary without redefining it. The specific native read/observe mechanism remains a DL-30 implementation-time verification, not an architectural blocker | Foundation, Room Configuration, Operational Trust | **Closed — DL-66** |
| **OD-60** | **Resolved as DL-65.** Repairs is a projection of an HTBW-owned Defect State, never a second authority. Genuine Repairs candidates: DL-41 missing/invalid capability dependencies, broken governed references, and configuration invariants ordinary runtime evaluation cannot resolve (e.g. duplicate Primary Authority). Configuration divergence (native-vs-HTBW), Provider-Derived Indicator values, Stewardship obligations, Truth runtime outcomes, and Identity Assertion outcomes are confirmed never automatically Repairs-eligible. Severity maps from Home Assistant's own 3-value IssueSeverity via each owning responsibility's already-accepted state, never from Stewardship significance or Operational Trust Urgency. Ignore lifecycle and re-raise behavior verified against official Home Assistant documentation: ignoring never deletes/resolves the issue or changes HTBW's Defect State; re-raise is the owning responsibility's own existing state-evaluation trigger, no new timer | Foundation, Room Configuration, Truth, Identity, Concierge | **Closed — DL-65** |
| **OD-61** | **Resolved as DL-60.** A native Area environmental entity slot (verified per-slot under DL-30) seeds a default proposal for the corresponding Room Environment Purpose, never automatic participation and never a silent override of an explicit HTBW selection or exclusion; HTBW never writes back. Related: **OD-17**, **OD-19** | Truth, Room Configuration | **Closed — DL-60** |
| **OD-62** | **Resolved as DL-69.** Scope amended (architecture-owner directed) from retrieval-only to retrieval **and** command resolution. Vocabulary is accepted as a first-class HTBW concept under existing Foundation/Room Configuration ownership (no new responsibility); a unified, Merged-Room-aware command-resolution sequence, a cardinality/clarification rule, a no-match/native-fallback invariant (resolves the "Bedtime" scenario), and enumerated retrieval classes with pre-answer filtering are accepted; historical reconstruction remains excluded to **OD-35** | Concierge, Operational Trust, Foundation | **Closed — DL-69** |
| **OD-63** | **Behaviour attribution** — the *semantic* model: the enumeration of behaviour sources, the evidence required to assert each, the confidence representation, and how *unattributed* is represented so that it never decays into a guess. **Person attribution remains bounded by Identity and creates no identification of its own.** **DL-38 sharpens the boundary: a behaviour source is not an identity evidence source.** Attribution consumes a completed Identity Assertion by reference and **never enters the Identity Fusion Function, never nominates a candidate, and never re-weights identity evidence**. Which platform evidence is captured is **OD-64**; declaration of an external decision-maker is **OD-66** | Foundation, Concierge, Truth | Behaviour attribution |
| **OD-64** | **Native automation, script, scene, and blueprint awareness** — the *evidence* question: which platform-supplied execution evidence HTBW references, how it is anchored, and its retention. **HTBW must not require the household to rewrite existing automations.** **Native execution evidence is not identity evidence (DL-38)**: an automation, script, scene, or blueprint execution record is evidence about *what changed a device*, and it is never admitted to the Identity Fusion Function nor used to nominate a candidate Person. How that evidence is interpreted as a behaviour source is **OD-63** | Foundation, Concierge | Native behaviour observation |
| **OD-65** | **Learning evidence eligibility** — which observations may contribute to a learned suggestion and which are excluded; how a resident's manual adjustment is distinguished from an automation-generated value; how competing residents' observations are handled; and how room-scoped and person-scoped learning are separated. Attribution itself is **OD-63**; lifecycle and revocation are **OD-28**. **An Unknown Person's interactions are never eligible evidence for person-scoped learning (DL-33)**. **Presentation is not personalization (DL-36): naming a candidate, or meeting the Identity Presentation Threshold, creates no learning eligibility of any kind**, and a denied or unclear confirmation never trains a profile or alters an evidence weight (**DL-37**). **A learned proposal may target a Fusion Policy value — reliability, correlation, freshness, contradiction, candidate comparison, normalisation, or band mapping — but never applies silently, and never recalculates an earlier assertion (DL-38)** | Continuity, Identity, Operational Trust | Learning evidence eligibility |
| **OD-66** | **Delegated external adaptive behaviour** — how an autonomous third-party policy engine is declared, bounded, observed, and disclosed, and how the reduced explainability of delegated behaviour is stated honestly to residents. **Execution by an integration does not by itself constitute delegation** | Operational Trust, Concierge | Delegation boundary |
| **OD-67** | **Reasoning Provider Strategy** — which classes of provider HTBW may use, for which purposes, under which governance. **No provider is selected here, and no provider abstraction is designed or presumed here.** Closure of **OD-62** does not depend on it. **Unknown Person access defaults to household-neutral context (DL-33)**, and household-private context is not authorised merely because a request originated inside the home. **Under DL-41 a reasoning provider is a declared capability dependency: where none is configured, valid, and available, the dependent capability is unavailable and says so, and no local approximation stands in for it. Which classes of provider are permissible remains open** | Concierge, Operational Trust, All | Reasoning provider strategy |
| **OD-68** | **Managed classification projection** — the reserved label taxonomy for Asset Type and any comparable classification: naming, stable identification, idempotent seeding, detection of existing labels, collision handling, taxonomy versioning, additions on upgrade, retirement, preservation of resident-created labels, and reconciliation reporting. **The architectural requirement is settled by DL-31; only the mechanism is open**, because no integration-facing label-management documentation could be verified. Closure must preserve: Asset Type stays authoritative in HTBW, labels stay derived, resident labels are never removed or overwritten, and a projection failure never changes a classification | Foundation, Stewardship | Managed label projection mechanism |
| **OD-69** | **Resolved as DL-61.** Asset-derived Entity projection reuses Stewardship's and Truth's existing owned vocabularies; no asset-health or room-health scale is invented; a projected Entity resolves back to its Asset, projects `unknown` honestly, and is never externally writable. Person Environmental Requirements, Environmental Coverage/Configuration Completeness/Truth Confidence separation, Room Environmental Status, and the Room Health/Room Confidence/People Health disposition are accepted alongside it | Foundation, Stewardship, Truth | **Closed — DL-61** |
| **OD-70** | **Resolved as DL-68.** ACCEPTED, NO NATIVE REPRESENTATION — a Merged Room is a curated interaction/vocabulary context, never an Area, Floor, group, or Label; no proven consumer requires a native projection, and Assist/Conversation must not receive one; constituent removal uses the existing broken-reference/Repairs model without a new rule; command-routing and native-fallback questions are routed to **OD-62** as evidence, not decided here | Foundation, Room Configuration | **Closed — DL-68** |
| **OD-71** | **Resolved as DL-72.** System-Initiated Communication and Person-Requested Response are distinguished; a bounded default degradation order (private delivery → Indication → neutral challenge → defer/refuse) applies under audience uncertainty; two distinct Person Setup preferences (ordinary delivery, audience-uncertainty routing) are accepted under Continuity; Authorized Private Delivery Surface criteria are extended without claiming unverified platform detection; unresolved plurality, audience unknown, audience detection unavailable, and contradictory evidence remain four distinct, explainable conditions; risk-class enumeration remains **OD-51** and the indication-mandatory threshold remains **OD-57** | Operational Trust, Concierge | **Closed — DL-72** |
| **OD-72** | **Unknown Actor correlation confidence** — how the evaluated correlation factors combine into a hypothesis confidence or quality band, and how that band is named and calibrated. **The correlation requirements are accepted as DL-35, and no mathematics is invented to close this.** Distinct from **OD-16**, which concerned identifying a *known* Person from identity evidence; this concerns grouping observations without identifying anyone. **OD-16's resolution as DL-38 does not close this decision and must not be borrowed to close it.** The Identity Fusion Function answers a purpose-specific *current* identity question against a bounded candidate set of known Persons; unknown-actor correlation groups *historical* observations into hypotheses while **identifying nobody**, and it has no candidate set, no Person-to-source associations, and no known-candidate separation. Shared primitives — freshness, observation quality, evidence families, contradiction — **may be referenced, but the function is not reused**. Access to the resulting reconstructions is **OD-35**; whether an Incident becomes a persisted object is **OD-41**. **Bounded against OD-74/DL-58**: this decision does not borrow the Truth Confidence Band representation for engagement, identity, or unknown-actor plurality semantics, and remains its own vocabulary | Concierge, Truth, Operational Trust | Actor correlation confidence |
| **OD-73** | **Interaction-Surface Room Context Resolution** — how **Room Context** is resolved when an interaction originates from a surface that is **not bound to a Room**: a phone, a wearable, a Companion App action, a browser session, or any other portable or mobile surface. **The constitutional concern is ownership and direction, not convenience.** Room Context is owned by **Foundation / Room Configuration**, whose accepted resolution order begins at *voice assistant identity* and whose failure behaviour states *"Never infer from device naming"*; yet [../models/glossary.md](../models/glossary.md) already asserts that Room Context may be established *"by a UI surface"*, and [../models/room-configuration.md](../models/room-configuration.md) already claims to provide *"Resolved Room Context for a given voice assistant **or surface**"* — **neither of which is defined**. The obvious input is illegal for the owner: deriving Room Context from a device's current location would require **Foundation to consume a Truth Fact at runtime**, contradicting [../architecture/dependency-view.md](../architecture/dependency-view.md) rule 6 — *"Foundation feeds everything and consumes nothing"* — and a naïve remedy risks the cycle **Room Context → Truth facts for that Room → Identity Room Presence → Room Context**, which the graph prohibits. **The native evidence is documented as insufficient**: device tracker granularity is verified as the **zone, never a Room or Area**, a connection tracker's zone is a documented **assumption**, and no native Room-level or Area-level BLE proximity capability has been verified, so under **DL-30** the burden of proof is **not discharged**. **This is also an explainability defect**: a Decision Trace must record Room Context and how it was resolved, and `room_context.resolved_from` currently has **no legal value** for this path, making the trace incomplete by its own definition. **Alternatives to evaluate, none preferred here: (A)** refuse — a non-room-bound surface never establishes Room Context, and the request is stated at Home scope or the resident is asked; **(B)** explicit household-configured surface-to-Room binding, exactly as for a voice assistant; **(C)** Room Configuration supplies the candidate Room set and its rules while **Concierge** consumes the Truth device-location Fact and selects, recording the selection in the trace; **(D)** Truth publishes an Engagement Fact carrying Room scope which Room Configuration consumes — **which violates dependency rule 6 unless that rule is amended by an accepted ADR**; **(E)** Room Context becomes multi-valued — *resolved*, *provisional*, *unresolved* — with provisional Room Context permitted only for capability classes Operational Trust marks tolerant; **(F)** interaction-surface Room Context is a Foundation-declared function over a Truth Fact **reference**, evaluated on request rather than by Foundation itself. **Closure must preserve**: a single named owner; a demonstrably **acyclic** dependency graph with the reasoning recorded; dependency rule 6 either preserved or amended by ADR and **never silently contradicted**; an enumerated `resolved_from` vocabulary sufficient for every trace to state honestly how Room Context was resolved; governed behaviour for unresolved context, unknown device Room, a device outside the Home, an unconfigured Room, a **constituent Room of a Merged Room** (**DL-13**: no transfer, no context change), and two equally supported candidate Rooms; the rule that Room Context resolution **never produces, alters, or substitutes for an Identity Assertion**; and **DL-30** discharged or the Room-granularity claim explicitly reduced. **Creates no responsibility, no second Room registry, and no second device tracker.** Related: **OD-11**, **OD-15**, **OD-51**, **OD-61**, **OD-63**, **OD-74**. **Must not be closed on assumed Home Assistant behaviour, on an unverified Companion App capability, or on implementation convenience in a reference integration** | Foundation, Room Configuration, Truth, Concierge | Interaction-surface Room Context resolution |
| **OD-74** | **Resolved as DL-58.** Truth Fact Confidence is defined, structurally separated from DL-39 Identity Confidence, represented as one uniform ordinal band (Low < Moderate < High < Very High) across every Fact Subject and Fact class, and bounded away from freshness, provenance, coverage, and conflict resolution, which remain OD-18, and OD-19's own. OD-17 consumes the representation for composite-fact derivation without redefining it | Truth | **Closed — DL-58** |
| **OD-75** | **Resolved as DL-48 and DL-49.** Obligation **condition** and obligation **lifecycle** are now orthogonal; deferral and closure are lifecycle transitions carried by **Change Records**; the **Care Evidence Record** defines what closes an obligation and distinguishes *satisfied without action* from *performed*; and custody is resolved as a Stewardship-owned **Custody Period**. **Formal acceptance review completed 2026-08-20 with a result of PASS, and issue #105 is closed as the completed governance record for OD-75.** The original question is retained for the record: **Obligation lifecycle completeness** — how a care obligation is **deferred**, **closed**, **reopened**, **grouped**, and what constitutes **accepted evidence that care occurred**. **This is a defect, not merely a gap.** [../models/stewardship.md](../models/stewardship.md) enumerates the obligation states as `met`, `due`, `unmet`, `overdue`, `waived`, and `unknown`, and in the same document describes obligation history as *raised, met, unmet, escalated, deferred, closed* — naming two lifecycle outcomes that **are not states**. The same document already establishes that **completion is not proof of fulfilment**, that marking a projected `todo` item complete is a list state rather than evidence of care, and that **absence of evidence is never compliance** — which together make *what does count as evidence* a question the architecture asks and does not answer. **Bounded by what is already accepted and not reopened here**: an obligation is never closed by a dismissed reminder, a ticked projection, a requested action, or an executor reporting success, because the projection does not own the obligation and an action is not an outcome; `unknown` is never `met`; a repeatedly unmet obligation makes the **pattern itself reportable**; and Stewardship observes closure from **Truth**, not from having asked for something. **Alternatives to evaluate, none preferred here: (A)** extend the state set with `deferred` and `closed` and define the transitions; **(B)** keep the six states and model deferral and closure as **Change Records** over an unchanged state, so history carries the lifecycle and the state stays a condition; **(C)** separate *condition state* from *lifecycle state* as two orthogonal fields; **(D)** define an Evidence-of-Care record class with its own retention under **DL-47**. Grouping of simultaneous obligations, and whether a *satisfied without action* obligation is distinguishable from a *performed* one, are part of this decision. **No new responsibility, store, or history owner may be created to close it**, and significance representation remains **OD-21**, escalation semantics remain **OD-22**, and projection surface remains **OD-23** | Stewardship, Concierge, Operational Trust | **Closed — DL-48, DL-49** |
| **OD-76** | **Resolved as DL-57.** Delegated Stewardship authority — one person may hold explicit, scoped access over another Person's, Asset's, or Pet's Stewardship content only through a **Delegated Access Grant** (subject, grantee, operations, scope, grant basis, effective/revocation time), never through relationship or Role inference alone. A competent adult retains self-authority and may delegate; a minor or a person unable to act independently may be represented by an authenticated administrator acting as proxy; a native administrator flag is never itself care or guardianship authority, and formal legal qualification is explicitly outside HTBW's scope. Identity evidence never transfers with a grant. Revocation is immediate and prospective; existing obligations remain governed records the household may reassign; historical actions remain attributed to the actor and grant valid at the time. An incomplete obligation with accountability unchanged is continuing notification, not automatic escalation — **OD-22** applies only where the household configures an actual change of accountable party | Stewardship, Foundation, Operational Trust, Identity | **Closed — DL-57** |

| **OD-77** | **Person-to-external-resource association ownership** — which responsibility owns the governed association between a **Person** and an **external service, account, calendar, mailbox, media profile, audiobook account, or reasoning-provider profile**, and how that association is created, referenced, disclosed, reassigned, revoked, detected as stale, and deleted. **The gap is specific and verified.** [../models/person-and-identity.md](../models/person-and-identity.md) lists *Mailbox, calendar, and other external-service references* in the Person-extension table and assigns them to *the responsibility that governs their use* — **naming no responsibility** — while [../contracts/foundation-contract.md](../contracts/foundation-contract.md) declares the relationship types as **caretaker-of, owner-of, serves-room, and located-in**, **none of which expresses that an account belongs to a Person**. Continuity's ownership list does not contain it. **Every personal-resource outcome depends on it**: whose calendar is read for *what is on my calendar*, whose mailbox is summarised, whose audiobook progress is resumed, and whose media profile shapes a suggestion. **Bounded by what is already accepted and not reopened here**: the underlying provider configuration is **never copied** and HTBW owns **no calendar contents, mailbox contents, provider credentials, or tokens** (**P21**, **P22**, **DL-46**); connected storage **never becomes a shadow system of record** for something Home Assistant already owns authoritatively; an **Unknown Person references no Person, inherits nothing, and grants nothing** (**DL-33**); *who may access calendars, messages, email, or history* remains **Operational Trust's**; a dangling reference is **reported, never silently rendered as though the source record never existed** (**P30**); and a missing or invalid association makes the dependent capability **unavailable and names the missing dependency** (**DL-41**). **Alternatives to evaluate, none preferred here: (A)** a Foundation relationship type, consistent with `caretaker-of` and `owner-of`, since Foundation already owns relationships and consumes nothing; **(B)** an Identity-owned association, on the argument that it resembles the Person-to-evidence-source association of **DL-32**, accepting the risk of conflating *who is this* with *what is theirs*; **(C)** a Continuity-held reference, accepting that Continuity would then hold something it currently does not, and that **DL-46** still forbids copying its content; **(D)** an Operational-Trust-held entitlement with no separate association object, accepting that a permission is not an identity of a resource; **(E)** a Concierge-held consumption binding, **which would move governance into Concierge and is recorded here only so that it can be rejected explicitly**. Whether the household authors the association, or it is derived from a provider integration's own account binding, is part of this decision. **No new responsibility is created by this decision**, and revocation, participant removal, reassignment, stale-association detection, and deletion must be answered together with erasure mechanics (**OD-09**) and the consent experience (**OD-06**) | Foundation, Identity, Continuity, Operational Trust, Concierge | Person-to-external-resource association |
| **OD-78** | **Remembered-value classes and restoration semantics** — which class of remembered value a restoration draws from, and whether restoration **reproduces a prior value** or **computes a currently appropriate one**. **This is a defect, not merely a gap.** [../models/continuity.md](../models/continuity.md) claims *last lamp levels, last speaker volume* and *last song played in the room* as Continuity-held, and [../architecture/framework.md](../architecture/framework.md) repeats the room-scoped list, **yet the only restoration mechanics stated anywhere are in the subordinate** [../patterns/execution-patterns.md](../patterns/execution-patterns.md), which requires restoration to *use stored state*, forbids *guessing previous values* and *reconstructing state from history*, and sources restored state from a *runtime state snapshot or cache* — **a mechanism no canonical model, contract, or ADR names**. The classes a household actually distinguishes — **last observed value, last successful value, last person-selected value, configured default, person preference, room preference, experience preference, and restored state** — are **nowhere enumerated**, so *last lamp level* is ambiguous between at least four of them. **There is also an unresolved tension with DL-46**, which makes Home Assistant authoritative for entity and device states and requires HTBW to persist **no second copy merely to explain later**: a Continuity-held *last lamp level* is either governed meaning Home Assistant does not represent, or a second copy of native state, and **the repository does not say which**. **Bounded by what is already accepted and not reopened here**: a remembered value is **never a Fact** and is never presented as one; an unaccepted pattern **never becomes a preference** (**P26**, **DL-21**); a missing preference is **stated, never replaced by a silent platform default**; the household's own scenes, scripts, and automations are **not rewritten, wrapped, or migrated**; and current Truth, Room mode, Identity confidence, Operational Trust, audience composition, and safety remain **preconditions to applying any remembered value, never overridden by it**. **Alternatives to evaluate, none preferred here: (A)** reproduce the stored value only, treating restoration as replay and refusing where the stored value is invalid under current conditions; **(B)** compute a currently appropriate value from the remembered value plus current Truth, accepting that the result is a derivation and must be explainable as one; **(C)** name the value classes explicitly and let the household configure which class each capability restores from; **(D)** confine restoration to Session resume and remove environmental-state restoration from Continuity entirely, leaving it to native Home Assistant scenes; **(E)** treat the runtime restoration cache as a Home Assistant concern under **P21** and hold only the approved preference in Continuity. **Whether a prior or preferred room temperature is a Continuity-held value at all is part of this decision**, since no canonical document currently states that it is. **No new responsibility, store, or history owner is created by this decision** | Continuity, Truth, Operational Trust, Concierge | Remembered-value classes and restoration semantics |

| **OD-79** | **Presentation preference scope and precedence** — at which scopes a **presentation preference** may exist, which responsibility owns each scope, and **what takes precedence when two scopes disagree**. **This is a defect, not merely a gap.** [../models/continuity.md](../models/continuity.md) and [../contracts/continuity-contract.md](../contracts/continuity-contract.md) enumerate exactly two scopes, and **neither tier contains voice, language, persona, verbosity, explanation depth, or delivery modality** — yet **TTS volume is room-scoped**, placing the adjacent concern inside Continuity's room tier while leaving the voice that speaks at that volume ungoverned. **Person scope is settled**: [../scenarios/stewardship-use-cases.md](../scenarios/stewardship-use-cases.md) and [../models/communication.md](../models/communication.md) both attribute preferred delivery and preferred presentation to **Continuity**. **Room scope has no owner**, and two candidates exist that the repository chooses between nowhere — **Continuity**, as a room-scoped experience setting consistent with TTS volume, or **Foundation / Room Configuration**, as part of the Room's interaction definition, which already owns which voice assistants participate in a Room. The only document naming the concept, [../contracts/concierge-scope-contract.md](../contracts/concierge-scope-contract.md) — *room persona and voice overrides* — is **Historical and superseded**. **There is also no precedence rule, and the conflict is concrete**: a Room may carry a persona, a voice, and a language while a Person carries an interaction style, and nothing states what happens when a concise-preferring resident asks a question in a Room configured with an expansive persona. **OD-04 does not cover it**, because that decision governs *policy* precedence and the glossary is explicit that a Preference *is not a fact and not a policy*. The dimensions themselves are enumerated only in [../models/person-profile-model.md](../models/person-profile-model.md) and [../contracts/service-contracts.md](../contracts/service-contracts.md), **both Historical and neither authority**. **Bounded by what is already accepted and not reopened here**: a preference influences presentation only and **never alters a Fact, a threshold, an authority outcome, or a conclusion**; applying a Person's preference is a **person-scoped capability access** evaluated by Operational Trust against the current Identity Assertion (**DL-36**); **presentation is not personalization**, and being addressed by name grants no preference application and no learning eligibility (**DL-36**, **OD-65**); an **Unknown Person owns no preferences and inherits nothing** (**DL-33**); guests must not receive residents' preferences; **audience governs disclosure regardless of presentation** (**DL-34**, **P32**), so a persona never widens what may be said; a reasoning provider **owns nothing** and its absence makes the dependent capability unavailable rather than approximated (**DL-41**); and the **person-scoped versus room-scoped split is preserved**. **Alternatives to evaluate, none preferred here: (A)** person scope only, with no Room persona, accepting the loss of a wanted capability; **(B)** Continuity holds both tiers with person overriding room where Identity suffices, requiring a stated fallback below threshold; **(C)** split ownership, with the Room's voice and language as Room Configuration and style, depth, and modality as Continuity at person scope, accepting a seam the household may feel; **(D)** three declared tiers of household, room, and person, accepting a scope tier the Continuity model deliberately does not have; **(E)** separate **character** from **accommodation**, treating persona and voice as decorative and room-scoped while verbosity, modality, language, and accessibility are person-borne and always win. **Whichever option is chosen, the decision must answer whether an accessibility or language need is a preference subject to precedence at all, or an entitlement that no Room setting may override.** **No new responsibility, model, store, or history owner is created by this decision**, and no third scope tier is introduced unless the decision explicitly accepts one | Continuity, Foundation, Operational Trust, Concierge | Presentation preference scope and precedence |

| **OD-80** | **Resolved as DL-50.** **Capability execution host** — the question was **where an HTBW capability may execute** when the Home Assistant integration process cannot host it, and how that host is declared, governed, and made explainable. **This is a defect, not merely a gap.** **DL-30**'s ordered burden runs native capability, then existing maintained integration, then HTBW extension governing existing capability, then new HTBW capability — and **every rung assumes execution inside the integration process**. [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md) addresses add-ons **only** as third-party engines that decide and act, governed as a delegation boundary under **OD-66**; **an add-on as a host for HTBW's own capability is nowhere addressed**. **The failure is verified rather than hypothetical**: a speaker-embedding encoder declared as a manifest requirement had **no installable wheel on the target host** — no build for the interpreter version below one release line and no build for the platform libc above it, so **no released version satisfied the host at all** — and because Home Assistant's manifest `requirements` install is a **hard precondition for `async_setup_component`**, the resolution failure failed the **entire integration** before any of its own code ran, **regardless of how carefully that code had been written to degrade without the dependency**. The response was to move the encoder into an application running on the host device, **a topology this repository neither describes, permits, nor forbids**. **This is not OD-07**, which asks *where processing happens* in trust and residency terms; this asks **what process hosts it**, and a capability may be entirely local yet still unhostable in the integration process. **It is also not simply DL-41**, which governs a dependency that is absent — here the dependency is specified, correct, and **structurally uninstallable**, which may still resolve to permanent unavailability but should be decided deliberately rather than by omission. **Bounded by what is already accepted and not reopened here**: **P21** and the **DL-30** ordered burden stand and must be extended rather than bypassed; **DL-41** stands, so a capability whose host is unavailable is **unavailable and names why**, with **no approximation, substitution, or silent reduction**; **P25** keeps Home Assistant the first implementation environment and **not a constraint on the architecture**, so no answer may bind HTBW to one deployment topology; data residency remains **OD-07**; third-party engines that decide and act remain **OD-66**; and HTBW acquires **no host operating-system administration**, consistent with the existing storage boundary. **Alternatives to evaluate, none preferred here: (A)** refuse, leaving such a capability permanently unavailable and explained as such, accepting a large capability loss taken by omission; **(B)** a Home Assistant add-on as a governed execution host declared as a **DL-41** dependency, accepting that add-ons exist only on some installation types so availability becomes deployment-dependent; **(C)** a household-provided external service or device referenced like any other provider, accepting a widened trust surface that engages **OD-07** and consent; **(D)** a per-capability declared host named in the dependency declaration and in the Decision Trace, the most explainable and the most to specify; **(E)** native-only, bounding capability ambition to what the Home Assistant environment can already install. **One conformance rule should be recorded whichever option is chosen**: a hard manifest `requirements` entry is an **all-or-nothing gate for the entire integration**, so a dependency that is optional to a capability **must not be declared there**, or a degraded capability becomes a total setup failure. **No new responsibility is created by this decision**, and no add-on, container, runtime, model, or vendor is selected by it. **Resolved 2026-08-25 as DL-50** on the evidence that four independent open-source speaker-recognition projects for Home Assistant all execute their encoder outside the Home Assistant Core process, which is evidence at step 2 of the **DL-30** ordered burden. **Alternative (D) is the accepted rule and (B) is the reference deployment only**; **(C)** is not foreclosed and remains available as a declared host engaging **OD-07**; **(A)** and **(E)** are rejected. **The conformance rule is recorded verbatim in DL-50.** **What this closure does not do**: it resolves neither **OD-07** nor **OD-66**, it selects no add-on, container, runtime, model, or vendor, and it authorises no implementation. **Two residuals were separated rather than absorbed**: the product-portfolio question is **OD-82**, and voiceprint gallery structure under channel diversity is **OD-83** | All, Identity, Concierge, Operational Trust | **Closed — DL-50** |
| **OD-81** | **HTBW capability exposure and self-consumption** — **whether HTBW publishes its own capabilities as first-class Home Assistant services, events, entities, and addressable household objects that a resident may call from their own automations, scripts, blueprints, and dashboards**, and **whether HTBW's own components must consume those same public interfaces rather than private internal paths**. **The gap is directional and verified.** **DL-16**, **DL-30**, **DL-42**, **DL-44**, and **DL-46** all govern HTBW **consuming** Home Assistant; **nothing governs HTBW publishing to Home Assistant for household consumption**. [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md) enumerates what Home Assistant may provide and what HTBW owns, and contains **no statement about a service HTBW registers, an event HTBW fires, an entity HTBW creates as a public surface, or a household automation consuming HTBW**. **DL-11 does not answer it**: Exposure there is the constitutional state of being perceptible to a resident and is explicitly **not Home Assistant Assist entity exposure**, so it governs narrowing, never publishing. **The direction is already anticipated but never generalised**: **DL-31**'s representation strategy states that where an HTBW concept benefits from native visibility, state, targeting, **or automation**, a native representation is created or used in preference to a parallel hierarchy **and that representation is a projection, never a second authority** — yet that is a rule about *representations of concepts*, and the three cases that instantiate it remain individually open as **OD-23**, **OD-69**, and **OD-70**, with no parent question asking whether a general public capability surface should exist at all. **The self-consumption half is a separate unresolved choice**: [../contracts/concierge-contract.md](../contracts/concierge-contract.md) already requires that all state changes occur **through the owning responsibility's governed interface**, but **no canonical document defines what a governed interface is**, and whether it must be the same surface a resident may call is undecided. **The evidence is implementation-verified**: three shipped products independently exposed roughly twenty-four services and twenty bus events, thirty-five services, and a services-only integration respectively, and households already automate against them, so the question is whether that becomes governed platform behaviour or remains accidental. **Closure must preserve**: a projection is never a second authority; **Operational Trust evaluates appropriateness before any effect regardless of who invoked it**, so a public surface is never an authority bypass; a **Decision Trace** is produced for every invocation including a resident-initiated one, which makes caller attribution a live concern under **OD-63** and **OD-64**; **DL-42**'s prohibition on a second Recorder cuts both ways, because Home Assistant's Recorder retains whatever HTBW publishes, making retention a **consequence** of publishing rather than a separate choice and engaging **DL-47** and **OD-05**; and disclosure governance binds, because an entity state is readable by every Home Assistant user with **no audience evaluation**, so publishing a Person, an identity state, or a confidence band as an entity is a disclosure surface under **DL-34** and **DL-39** and a numeric confidence value is disclosed only where policy governs it and the audience permits. **Two vocabularies are prohibited in advance**: **room health is not an HTBW term** and **HTBW defines no asset health state model**, so neither may be introduced as a published entity to close this. **This decision selects no service name, no entity platform, no event schema, and no catalog format**, and **preempts nothing** — **OD-23**, **OD-59**, **OD-62**, **OD-63**, **OD-64**, **OD-68**, **OD-69**, **OD-70**, and **OD-73** each retain their own question and may be decided before or after it | All, Foundation, Concierge, Operational Trust | HTBW capability exposure and self-consumption |
| **OD-82** | **Resolved as DL-51 and DL-52.** **HTBW product consolidation and retirement** — **whether the standalone Asset Intelligence, Voice Identity, and Concierge products are harvested into a unified HTBW product and retired, or continue as separate released products**, and what becomes of their released artifacts, namespaces, entity identifiers, storage, and installed households if they are. **This is a verified contradiction, not a gap.** [authority-order.md](authority-order.md) records as a **non-negotiable constraint binding regardless of rank** that *"Asset Intelligence, Voice Identity, and Concierge remain **separate released products** with their own lifecycles"*; **DL-08** states the same for Asset Intelligence and **DL-19** states the greenfield form of it for all three. **An execution premise dated 2026-08-25 asserts the opposite** — that the three are being harvested into and retired in favour of a unified HTBW project — and that assertion cannot be adopted by implementation, by an ADR, or by prose, because a non-negotiable constraint is changed only by a decision that names it. **What is already settled and is not reopened by raising this**: **DL-05** stands, so Identity is the responsibility and voice is one evidence source regardless of the outcome; **DL-19** stands, so no compatibility requirement flows upward from any of the three into HTBW Core whether they are retired or retained; **DL-07** stands, so Stewardship owns significance and care; and the ledger's existing consolidation language for Asset Intelligence is a **responsibility** statement and was never a **product** statement, which is precisely the distinction this decision must hold. **The two are genuinely separable and must not be collapsed**: a responsibility may be first-class inside HTBW while its released product continues, and a product may be retired while its responsibility is unchanged — **OD-20** already depends on that separation, because it asks whether HTBW Core consumes the standalone Asset Intelligence product as an optional evidence source, and that question is only meaningful while a separate product exists. **What must be answered whichever way it goes**: whether installed households are migrated, left in place, or told the product is unsupported; whether released entity identifiers, unique identifiers, and storage keys survive; whether **DL-31**'s prohibition on requiring a resident to maintain the same information twice is satisfied during any overlap period; whether **DL-41** capability dependencies naming a standalone product remain resolvable; and whether **DL-45** parent-removal cleanup is triggered by a product retirement, which it must not be, because retiring a product is not removing a household's governing parent objects. **Alternatives to evaluate, none preferred here: (A)** retain all three as separate released products, leaving the constraint unchanged and the premise rejected; **(B)** consolidate into one HTBW product and amend the constraint by an accepted decision that states the migration obligations explicitly; **(C)** consolidate the **responsibilities** while retaining the released products as thin compatibility surfaces for existing households; **(D)** retire selectively, product by product, each with its own migration record. **No implementation artifact, namespace, domain, or entity identifier is renamed by raising this**, consistent with the existing rule that implementation artifacts are not renamed to match architectural words. **Resolved 2026-08-26 as DL-51 and DL-52**: alternative (D) accepted, with the refinement that **Asset Intelligence is not retired at all** and that **HTBW must never require it to be installed**; the standalone Voice Identity and Concierge integrations sunset while Identity and Concierge remain first-class responsibilities; the release footprint was **verified** (Asset Intelligence 27 releases, Voice Identity one v0.1.0 artifact, Concierge none), so the *no released-user footprint* premise is recorded as an **assumption about installs**; the non-negotiable constraint is **amended to a per-product form rather than deleted**; the canonical contradiction across authority-order.md, greenfield-mandate.md, north-star.md, and adr-htbw-core-refoundation.md is reconciled; and the adoption residual is separated as **OD-85** rather than absorbed here | All | **Closed — DL-51, DL-52** |
| **OD-83** | **Voiceprint gallery structure under channel diversity** — **whether a Person holds one voiceprint gallery entry derived from samples across every capture channel, a derived profile per channel, or a hybrid**, and how a runtime comparison selects among them. **Separated from DL-50 deliberately, and it must not be settled by implementation choice.** **DL-50** accepts channel-aware enrollment, so a voiceprint **records where enrollment occurred** — microphone source, satellite source, room, capture distance, and audio characteristics. **Recording where enrollment occurred is not the same as deciding how the gallery is structured**, and conflating the two would decide this question silently the first time an implementation chose a storage shape. **The question is real rather than theoretical**: a voiceprint derived on a handset is not equally representative of audio captured by a distant room satellite, which is the failure mode channel-aware enrollment was adopted to address, and a single averaged profile and a set of per-channel profiles behave differently against the same runtime audio. **Bounded by what is already accepted and not reopened here**: **DL-38** stands, so whichever structure is chosen it yields **one contribution per correlation family** and never several confirmations from one person's several profiles — **F2** forbids that directly; **DL-32** stands, so reliability remains configured per Person-to-source association and a per-channel profile is never a second source; **DL-43** stands, so voiceprints are Identity-owned and retained while the profile is enabled and consent remains valid, and any per-channel multiplication inherits that rule rather than creating a new one; **OD-16** stands, so sample counts, quality thresholds, and separation margins remain Fusion Policy configuration and are **not** part of this question. **Alternatives to evaluate, none preferred here: (A)** one person-global gallery entry built from channel-diverse samples, simplest and weakest where channels differ sharply; **(B)** a derived profile per channel, strongest per-channel accuracy and the most lifecycle surface, requiring an explicit rule that they never count as independent confirmations; **(C)** a hybrid, a person-global entry with per-channel refinements consulted when the capture channel is known; **(D)** channel recorded as evidence quality only, with no structural effect, letting **DL-38**'s observation-quality stage carry it. **This decision creates no new record class and no new artifact class**, and whichever alternative is chosen, an incompatible or absent profile remains a **DL-41** capability outcome rather than an identity failure | Identity | Voiceprint gallery structure |
| **OD-84** | **Multi-speaker evidence and speaker plurality** — **whether a voice evidence record may report that more than one person spoke within one capture**, and how a consumer distinguishes that from uncertainty about a single speaker. **This is a defect, not merely a gap.** **DL-38 F8** yields `ambiguous` when the leading candidate fails the governed separation requirement, and **`ambiguous` means one speaker whose identity could not be separated between candidates** — yet **two people speaking produces the same observable shape**, several candidates scoring closely, **from the opposite cause**. Uncertainty and plurality are therefore **currently indistinguishable at the point where the distinction matters most**, and an implementation that reports plurality as `ambiguous` would be conforming to the letter of an accepted rule while asserting something false. **HTBW already represents plurality twice, and in neither place is it a speaker**: **DL-35** makes *one actor, several actors, and unresolved plurality* representable for an **Unknown Actor Reference** within a historical reconstruction, and [../models/communication.md](../models/communication.md) carries *Multiple known Persons* and *Unresolved plurality* as **audience composition** states — but **DL-34** states that audience composition *identifies nobody* and *is never a second identity fusion*, so it may not be borrowed, and **audience answers who could hear while this question asks who spoke**, which **DL-34** itself separates by naming Requestor, Speaker, Present Person, Potential Listener, Authorized Recipient, and Delivery Target as six distinct roles that are never collapsed. **Bounded by what is already accepted and not reopened here**: **DL-38** stands entire and no fusion rule is amended, so whatever is decided must not turn a second speaker into a second confirmation of the first — **F2** forbids that directly; **DL-33** stands, so an unidentified second speaker is `unknown` with a supported human participant and never a synthetic Person; **DL-36** stands, so nothing here decides sufficiency for any purpose; **DL-34** stands, so a resolved second speaker is **not** thereby an audience determination and grants no disclosure; and **OD-16** stands, so no margin, count, or threshold is at issue. **Alternatives to evaluate, none preferred here: (A)** one capture yields exactly one speaker evidence record and additional voices remain **quality metadata**, the current position by default, simplest and silently lossy where a household genuinely has two people talking; **(B)** one capture may yield **several** evidence records, one per detected speaker region, each independently qualified, which is the most faithful and the most work for every consumer; **(C)** one evidence record carrying an explicit **plurality indicator** alongside its candidate list, distinguishing *uncertain* from *several* without multiplying records; **(D)** plurality treated as a **Truth** concern about the Room rather than an Identity concern about the capture, consistent with speech activity being a Room Fact. **Whichever is chosen, `ambiguous` must retain its accepted meaning**, and **no new responsibility, record class, or confidence representation may be created to carry plurality** | Identity, Truth, Operational Trust | Multi-speaker evidence and speaker plurality |
| **OD-85** | **Adoption scope, artifact custody, and coexistence behaviour** — the residual of **OD-82** after **DL-52** settled the *shape* of adoption. **DL-52 is not reopened by this**: adoption is already accepted as one-time, authoritative, terminating, non-synchronising, lineage-preserving, Operational-Trust-authorised, traced, and idempotent, and the transfer table separating declarations from adopted history is already accepted. **Four questions remain.** **(1) Granularity and scope** — what is offered for adoption and at what unit: a room, an asset, a document set, a history class, or the whole configuration; whether partial adoption within a unit is permitted; and how an already-adopted unit is recognised so that adoption stays **idempotent**. **(2) The governing parent of an adopted connected-storage artifact** — an Asset Intelligence document lives on connected storage under a path encoding **its** governing parent, and **DL-45** makes cleanup follow that parent, so a resident uninstalling the source product could delete artifacts HTBW now depends on; the decision must state whether adoption **re-anchors** the governing parent, **copies** the artifact, or **records the dependency and tells the household plainly**, and it must distinguish a resident-initiated uninstall of a coexisting product from a **retention-driven deletion** and from a **product retirement**, which are three different events with three different obligations. **(3) Coexistence** — how the home behaves while both products remain installed, given that both may publish overlapping conclusions to Home Assistant; **no synchronisation loop can arise because DL-52 makes adoption one-way and terminating**, but publishing conflicts are real and belong with **OD-69** and **OD-81**, and this decision must say which of the two holds each case rather than creating a third. **(4) Surface** — where adoption is detected, offered, reviewed, and explained. **HTBW has no onboarding or first-run experience architecture at all**, and the only occurrence of *onboarding* in a model document is in the Historical interaction-model.md, so this part must not be closed by assuming a surface that has never been defined; **detection and prompting are a surface concern and adoption is an authority concern**, and the decision must keep them apart. **Bounded by DL-52 throughout**: nothing here may reintroduce synchronisation, shared authority, a runtime dependency, an adopted Truth Fact, or an HTBW model shaped by the source product's storage. **Applies to Asset Intelligence only** — Voice Identity and Concierge have no household data footprint requiring an adoption path (**DL-51**). Related: **OD-20**, **OD-36**, **OD-01**, **OD-69**, **OD-81** | Foundation, Stewardship, Operational Trust, Concierge | Legacy adoption scope and coexistence |
| **OD-86** | **Vocabulary change and term-withdrawal consequences** — **what the home owes the household when a Contextual Vocabulary term is changed, retargeted, or withdrawn.** The accepted model governs how a term is **created**, how a native value may **seed** it, what a term whose target no longer resolves becomes, and that a term the household withdraws is removed through the ordinary Room Configuration lifecycle with its history retained. **What is not governed is the consequence for the people who still use the old word.** Open: whether a superseded term is recognised at all and for how long; whether the home may say that a word it once understood is no longer configured, and which responsibility says it; how a vocabulary change is explained afterwards, given that a Decision Trace references the exact vocabulary version under **P30** and therefore remains accurate while the household habit does not; what becomes of household-authored automations, scripts, and scenes that named the previous target, which HTBW may reference but must never rewrite, wrap, or migrate; what becomes of retained references in governed records; and what becomes of Continuity room-scoped and person-scoped values captured under the earlier term. **This question exists because the superseded managed-vocabulary-lifecycle authority was not carried forward** — `adr-room-vocabulary-governance.md`, `room-vocabulary-registry-contract.md`, and `room-vocabulary-registry-model.md` are Historical, and **nothing in this decision reactivates them**. **A wake-word change is admissible here only as a household-facing vocabulary sub-question and remains deferred behind the native-capability evaluation recorded as item 11 of issue #146**; **no wake-word decision is opened, and no wake-word implementation, configuration, or ownership is implied**. **Raising this asserts no transitional aliasing, no deprecation window, and no withdrawal behaviour**, **creates no record class and no Continuity scope**, and **treats habit continuity and vocabulary continuity as review lenses rather than as a third Continuity tier**. Inheritance of vocabulary across scopes is the different question already held by **OD-13**. Related: **OD-13**, **OD-59**, **OD-63**, **OD-64** | Foundation, Room Configuration, Continuity, Concierge | Vocabulary change and term-withdrawal consequences |
| **OD-87** | **Identity artifact invalidation as a governed household event** — **what the household is owed when previously sufficient identity artifacts stop being usable and every enrolled Person must enrol again.** The **mechanism is already accepted and is not reopened**: an encoder, audio-contract, or comparability change that renders an artifact unusable is a **DL-41** capability outcome, in which the capability is **unavailable**, the missing or invalid dependency is **named**, and the outcome is **never rendered as a trust, permission, or identity failure**. **What has no owner is the household event that follows.** Open: how the household is told, and by which responsibility, that identity artifacts are no longer usable; whether that notification is a **Communication** and under what classification, urgency, and audience; what the home does in the interval before re-enrolment, given that **an outcome that varies by person requires a sufficient Identity Assertion** and must therefore degrade honestly rather than be applied to the wrong person; which fallback and unidentified-person behaviour applies meanwhile; whether **consent** previously given for an evidence source survives the artifact derived from it or must be sought again; and what constitutes completion and accountability for a bulk household act of this kind. **This has the same shape as the bulk household act settled by DL-52 for adoption, and is raised separately rather than absorbed into it.** **It does not reopen OD-16** — no threshold, sample count, duration, separation margin, or quality value is in scope. **It changes no compatibility mechanism**, **creates no dependency class**, **creates no responsibility**, **restores no Voice Identity responsibility**, and **asserts no re-enrolment experience**. Related: **OD-06**, **OD-07**, **OD-15**, **OD-83**, **OD-85** | Identity, Operational Trust, Concierge | Identity artifact invalidation as a governed household event |
| **OD-88** | **Resolved as DL-55.** Dynamic Capability Discovery and Room-Defined Presentation Outcomes — how HTBW resolves, at delivery time, which currently available technical provider and evidence path satisfies a Room-defined presentation purpose when one physical endpoint may be represented by more than one provider, and how conflicting or partial evidence across providers, endpoints, and a multi-endpoint Room-defined outcome is resolved and explained. **Governance-harvest result: every question reduced to an existing owner.** Provider/execution selection is Room Configuration's existing explicit-participation rule; endpoint identity is the existing Asset model; the room-level outcome is a narrow, bounded projection over the existing **DL-54** outcomes; device-interaction/workflow boundary is existing **DL-53** dimension independence; capability evolution is existing **DL-41** plus Room Configuration's existing failure behaviour; the presentation-purpose vocabulary is Room Configuration's existing, already-extensible experience-endpoint category set. **This is distinct from, and does not reopen, Room Configuration's existing ownership of the static household-declared vocabulary-to-target mapping**, which remains Foundation's, unchanged | Foundation, Truth, Concierge, Operational Trust | **Closed — DL-55** |
| **OD-89** | **Exceptional Retrospective Correlation and Legal/Incident Access to Unassociated Observations** — whether previously unassociated camera or device observations may ever be correlated for a legal request, a household-initiated incident review, or another exceptional-access case; if so, who may authorize it, what authority basis is required, whether it is technically possible without reconstructing prohibited biometric or derived identity material (**DL-43**), and what audit, disclosure, retention, and preservation implications follow. **Raised by OD-06/DL-56, which explicitly declines to decide it and creates no bypass of its ordinary consent requirement.** No existing repository authority governs this; only the generic legal/regulatory non-claim exists, which is a disclaimer, not an authorization framework | Operational Trust, Identity, Truth | Exceptional retrospective correlation and legal/incident access |

---

### Notes on the audience-uncertainty disclosure policy decision

**OD-71 closed as DL-72.** The architecture-owner's preferred default (system-initiated content
prefers authorized private delivery under audience uncertainty) was tested against **DL-34**'s
existing composition states rather than assumed, and it held cleanly because **DL-34** already
distinguishes "Unresolved plurality," "Audience unknown," and "Audience detection unavailable" as
three separate states — this closure only needed to state what Operational Trust *does* with them, not
invent new ones. **A genuinely new distinction — System-Initiated Communication versus
Person-Requested Response — was formalized because no accepted document previously separated them**,
even though `communication.md`'s "Multi-person communication" step table already implicitly assumed
an originator without naming the two cases distinctly. **Two Person Setup preferences were split from
one existing, informally singular concept**: `stewardship-use-cases.md` already established that
Continuity owns "preferred notification paths" while Operational Trust decides when they apply — this
closure adds a second, distinct Continuity-owned preference (audience-uncertainty routing) using the
identical ownership pattern, rather than overloading the first. **The Authorized Private Delivery
Surface criteria were extended, not invented**: `communication.md`'s existing seven-part test was
kept in full and four additional dimensions were added, each traceable to already-accepted decisions
(**DL-53** Potential Perceptibility, **DL-54** Presentation Outcome) — and, following the mission's own
explicit caution, lock-screen state, current physical possession, and shared-device status were
deliberately **not** claimed as detectable platform capabilities; where the platform cannot establish
privacy, the existing "delivery degrades, not the governance" rule (**DL-29**) absorbs the gap rather
than a fabricated detection mechanism. **Scope discipline was maintained throughout**: the risk-class
enumeration (**OD-51**) and the indication-mandatory threshold (**OD-57**, which lists OD-71 as its own
blocker and is now unblocked) were referenced and routed, never decided. **No new Mode value, no new
Merged Room rule, and no new confirmation/assurance scale were introduced** — Merged Room composition
inputs widen under **DL-67**–**DL-70** exactly as already accepted, while the uncertainty policy itself
does not change; DL-71's multiple-caretaker and Guest-fallback rules were consumed without
redefinition.

---

### Notes on the audience specification and Person Extension decision

**OD-52 closed as DL-71.** The mission's own instruction to route rather than absorb was tested
against every candidate: escalation (**OD-22**), lifecycle/acknowledgement (**OD-44**/**OD-45**),
retention (**OD-49**), retry (**OD-54**), and audience-uncertainty default policy (**OD-71**) were
each checked against their own issue text and confirmed to depend on, or be independent of, this
closure without requiring this decision to resolve them. **A genuine conflict between the
architecture-owner's proposed "Person Extension" and existing accepted architecture was found and
reconciled, not silently overridden**: **DL-31** already states that HTBW's extension of a native
Person is "distributed — each extension keeps its own owner," which a single unified Person Extension
record would have contradicted. The reconciliation adopts "Person Extension" as a household-facing
*name* for that same distributed set, changing no ownership. **A second, narrower terminology
overlap was found and split rather than left ambiguous**: the existing glossary already used
"Caretaker" two ways — as a bare Role (an authority classification like "adult" or "child") and as
the specific `caretaker-of` relationship to a named subject — and the architecture-owner's "Caretaker
of Maisey" phrasing is the latter, not the former. Splitting **Role/Authority Class** from
**Relationship-based** as two distinct Audience Specification forms resolves the overlap without
renaming either existing concept. **The Notice/completion question was the largest finding**: rather
than needing a new object, both patterns the architecture-owner described turned out to already be
directly expressible by combining two already-accepted decisions — **DL-48**'s obligation model and
**DL-57**'s Delegated Access Grant, whose `complete` operation may already be held by more than one
grantee over one record. One Completion Satisfies All is one obligation with multiple caretakers
each able to close it; Each Recipient Must Complete is multiple independent obligations, one per
Person. Neither required new Stewardship architecture — only the explanatory label "Completion Mode"
was added, to make an existing configuration choice explainable to the household. **A real Concierge
implementation finding was recorded rather than fixed**: `PreferenceIdentityState.GUEST` is used as a
peer of `KNOWN`/`UNKNOWN`, which risks exactly the conflation **DL-33** forbids (Guest treated as a
fourth Identity state); this is flagged for implementation-time reframing, not corrected here, since
this session is architecture-only and the finding belongs to the Concierge repository. **Caretaker-of
cardinality (many-to-many) was clarified as a narrow reading of already-accepted Foundation
relationship semantics**, not a new relationship taxonomy — nothing in the asset model or **DL-49**
previously stated a cardinality limit, and the household's own Maisey/Piano examples require one.

---

### Notes on the Vocabulary inheritance and scope decision

**OD-13 closed as DL-70.** The mission's own instruction not to assume the issue's three listed
options were exhaustive was tested directly: Option D ("Vocabulary inheritance and Fulfillment
inheritance are distinct concerns") was accepted **in addition to** Option B's shadowing behaviour,
not as a substitute for it — the household's own "News" example (a stable word, a provider order that
differs by Room) only makes sense once the two are separated, and real Concierge implementation
evidence corroborated this directly: `weather_source_entity_ids`, `news_source_entity_ids`, and the
Person-scoped `email_source_ref`/`calendar_source_ref`/`shopping_source_ref` fields already vary by
Room, Merged Room, and Person in the current codebase, independent of whatever word a household might
one day choose for them. **The Merged Room validation was confirmed, not merely assumed**: `room.md`'s
existing "Participation is explicit" rule and **DL-13**/**DL-67** together already establish that a
Merged Room behaves identically to a Room once configured, with candidate selection during setup as
the sole difference — this closure states that plainly rather than leaving it to be inferred.
**A real, if narrow, gap between the architecture-owner's proposal and verified evidence was found and
reconciled rather than ignored**: the mission's own "Global Settings" examples (weather source, news
source, AI provider, TTS provider) do not, on inspection, describe a single concept — AI/TTS *provider*
selection is native Home Assistant integration configuration already covered by **DL-31**'s
"referenced provider or integration configuration" row and gated by **OD-67**, entirely outside
Vocabulary's scope; weather/news *source* selection is Fulfillment, already Room/Merged-Room-scoped in
the real implementation; only the *word* itself ("Weather", "News") is a genuine Vocabulary question,
and it is the Home-scope tier this decision adds that answers it. **The Asset-relationship proposal
was deliberately not adopted inside this decision**: Vocabulary answering *what* is referenced and
Operational Trust/Foundation's existing relationship types answering *how a Person may engage* were
already separated by an existing contract rule, so inventing a new "default Guest, exceptions-only"
classification here would have exceeded OD-13's own scope; it is recorded as evidence toward **OD-52**
instead, which already has a blocked scenario naming exactly this question. **A genuine implementation
gap was found and recorded, not fixed**: Concierge's current device/entity Vocabulary resolver has no
fallback from an unscoped (Home-scope) entry into a Room-scoped resolution call — it only matches an
unscoped entry when resolving with no Room or Person scope at all — confirming the Home-scope tier
this decision accepts is genuinely greenfield, exactly as OD-13's own "current implementation: none"
already stated.

---

### Notes on the governed conversational retrieval and command resolution decision

**OD-62 closed as DL-69.** The architecture-owner's instruction not to assume retrieval includes
execution was honoured by making the scope amendment explicit rather than silent: OD-62's own written
acceptance criteria were entirely about retrieval and explanation, and command execution had no open
decision of its own — it was already latent inside the accepted Contextual Vocabulary model (**DL-09**,
**DL-10**), never formalized. Rather than inventing a new issue or a new responsibility for it, this
closure extends the existing owner. **Every Home Assistant Voice claim was checked against official
developer documentation before being relied upon**, and several plausible assumptions were deliberately
not made: no confidence score or alternative transcript is documented as available to a custom
conversation agent; no device/area metadata beyond an optional pipeline-level `device_id` is
documented; and `light.turn_on`'s parameters are documented as optional, never as guaranteeing a
universal "restore previous brightness" behaviour. On that last point, the real owner was found rather
than invented: `continuity.md` already accepts "last lamp levels" as governed Person- and Room-scoped
state, which is the existing mechanism a generic "turn on" should consult — no new Continuity record
was created. **A genuine near-contradiction was found and reconciled, not overridden**: the existing
Contextual Vocabulary Contract already states that a plural form never creates a group and that a
derived recognition form resolves to exactly its authoritative term's target set — which, read alone,
would make a singular utterance of a configured collection term resolve the whole set every time, never
asking which member was meant. The reconciliation is that this rule was never tested against a
household that has *also* configured distinct member-level terms; where it has, more than one already-
configured mapping now matches, which is precisely the existing `ambiguous` state already accepted in
the same contract. No new state was invented — the existing `ambiguous` outcome simply now applies to
this case too. **The "Bedtime" failure scenario is resolved architecturally, not diagnosed as a specific
bug**: no literal "bedtime" handling was found in the Concierge implementation, confirming this is an
illustrative failure mode rather than a located defect; the accepted invariant is that a failed HTBW
vocabulary match must never silently authorize an unrelated or materially broader native action,
consistent with `failure-and-degradation.md`'s pre-existing governed fallback vocabulary, none of whose
entries is "silently hand off to a system that may interpret the request differently." **Real Concierge
implementation evidence corroborated rather than substituted for the architecture**: `services.py`
already implements canonical-term-plus-alias vocabulary registries scoped by Room/Merged-Room, already
treats more than one matching target as an error requiring resolution rather than picking one
arbitrarily, and already carries an extensive named `fallback_reason`/refusal-message pattern for room
audio — the same discipline this closure now states architecturally for command vocabulary generally.
OD-13, OD-29, OD-30, OD-35, OD-67, and OD-71 each retain their own residual questions, confirmed via
their own issue text rather than assumed; none is decided or preempted by this closure.

---

### Notes on the Merged Room native representation decision

**OD-70 closed as DL-68.** The consumer inventory the architecture-owner requested was performed
against real candidates rather than assumed: dashboards, native automations, Assist/Conversation,
native targeting, scripts, scenes, labels, groups, administrative views, and external integrations.
**None had a canonical, implemented requirement for a native Merged Room projection.** Two findings
sharpened the result beyond "no consumer needs it": first, the repository's own existing
`home-assistant-boundary.md` representation-strategy table already classified Merged Room under
**Category 3 — "no sufficient native representation exists"** — alongside Decision Trace and
Communication — before this closure, another case of the model already knowing the answer the
governance layer had not yet ratified. Second, and more consequential, `contextual-vocabulary.md`'s
existing "resolution compiles down to native targets" rule showed that projecting a Merged Room
natively would not be neutral: HTBW's vocabulary layer already pre-resolves a term to a concrete
governed entity set **before** any native targeting happens, so a native Area or Label reachable by
Home Assistant's own documented Assist area-slot matching would let the **built-in** conversation
agent bypass HTBW's curated participation, exclusions, and **DL-66** Exposure narrowing for exactly
the interaction context **DL-67** created to be curated. Area, Floor, Group, and Scene were each
evaluated against verified platform documentation and rejected as Merged Room representations for
reasons specific to each (no native "Area of Areas" concept; Floor already independently satisfies
the broader-grouping need **DL-67** identified; a Group carries targets, never vocabulary or
interaction context; a Scene is a Merged Room's execution target, never the Room itself). Label was
not adopted — not because it was evaluated and found wanting, but because no proven consumer exists
and the integration-facing label-management API remains unverified, matching **OD-68**'s own
unresolved finding; this does not decide OD-68 and does not preempt it. The scene-controller metaphor
the architecture-owner supplied was memorialized as an explanatory illustration of already-accepted
configuration-time semantic definition and deterministic lookup, not as new architecture. Per the
architecture-owner's own explicit framing, command-routing, no-match, and native-fallback
requirements (including the Bedtime failure scenario) were kept out of this closure and recorded as
evidence on **OD-62** instead, since OD-62 owns the retrieval/command surface and custom sentence and
intent definition.

---

### Notes on the Merged Room composition decision

**OD-11 closed as DL-67.** The architecture-owner's hypothesis — a Merged Room is a curated
conversational interaction context, so a Physical Room participates in at most one at a time — was
tested against **DL-13**'s existing text and against real Concierge implementation evidence rather than
assumed, and it held on both counts. **DL-13** already states that a Room and a Merged Room behave
identically and rejects special-case orchestration; that rule is coherent only if every consumer of
Room Context (Truth's composite-fact selection, Continuity's sessions and transfers, Operational
Trust's policy scoping, and Room Configuration's own vocabulary resolution) can rely on exactly one
applicable Room Context per Physical Room. Overlapping membership would force each of those consumers
to invent its own selection or precedence rule, which is the special-case orchestration **DL-13**
exists to prevent, and it would conflict with **DL-63**'s conflict-qualification order, which already
assumes Room Context is a resolved, single value before Truth's qualification even begins. **The two
rejected options were not rejected for being merely more complex — each was shown to actively
reintroduce architecture the ledger already forecloses**: multiple Merged Rooms selected by capability
class would require a new per-consumer selection rule everywhere Room Context is used, and multiple
Merged Rooms with explicit precedence would invent a new precedence dimension that collides with
**OD-04**'s already-open policy-precedence question and with **DL-60**'s existing per-purpose Primary
Authority selection. **Real implementation evidence corroborated the architectural reasoning rather
than substituting for it**: Concierge's composite (Merged Room) configuration already structurally
excludes an Area belonging to one enabled composite from being offered when creating or editing
another, and composite configuration already carries conversational-context properties (persona, TTS
voice/language, AI knowledge enablement) alongside curated device/asset participation lists — this is
what an interaction context looks like in a working implementation, not a generic grouping utility.
**A household's legitimate desire for a different or broader grouping is not lost**: Home Assistant's
own Floor and Area hierarchy already provides it natively (an Area belongs to at most one Floor), so
"Downstairs lights" is handled by Home Assistant's own targeting, never by an overlapping HTBW Merged
Room — reconfiguring which Merged Room a Physical Room belongs to remains an ordinary household choice,
recorded as a Change Record, never a technical limitation. **OD-70** (Merged Room native projection) and
**OD-13** (Contextual Vocabulary Inheritance) both depend on this decision and were updated with the
single-membership boundary; neither is decided by it.

---

### Notes on the exposure precedence decision

**OD-59 closed as DL-66.** The architecture-owner's hypothesis — native input, HTBW governed state,
never written back, divergence surfaced administratively — was tested against OD-14 (naming) and
DL-60 (native environmental assignment) rather than assumed, and it holds only **partly**. The
"never write back" half transfers directly. The "native seeds a proposal HTBW may accept, decline, or
supersede" half does **not** transfer, and the distinction matters: a native name is an **informational
seed** a household may freely override in either direction, and a native environmental slot is a
**proposal** Room Configuration may accept or decline — but native Assist exposure is, by Home
Assistant's own stated purpose, a **safety precondition** ("to avoid that sensitive devices... can be
controlled inadvertently by voice commands"), not a suggestion. Treating it as a mere seed would permit
HTBW to widen past a resident's deliberate safety exclusion, which no accepted principle supports and
which **DL-11**'s own text already forecloses ("Assist exposure is a platform boundary that HTBW may
narrow and must never bypass") — this sentence existed in `room-configuration.md` before this closure,
asserted as design intent but never formally ratified as its own Decision Ledger entry. **DL-66 is that
ratification**, not an invention.

**A scope refinement was necessary and is new**: the precedence rule binds **voice- and
conversation-mediated** HTBW Exposure only. Home Assistant's own documentation frames Assist exposure
as a targeting/control safety gate, not a general visibility control; a UI panel or dashboard already
has its own native visibility mechanisms independent of Assist exposure. Binding non-voice HTBW
Exposure to a voice-specific native safety setting would have been an unjustified over-reach in the
other direction.

**Every divergence scenario resolved to "not a defect, not Repairs," which simplifies rather than
complicates OD-60's own generalized rule (DL-65)**: an Assist-exposed-but-HTBW-excluded entity is an
ordinary deliberate exclusion; an HTBW-included-but-Assist-hidden entity is a configuration condition
capped by the precedence rule; neither requires administrator correction, because the precedence rule
itself resolves the interaction coherently every time. No new Repairs category was created.

**The one item left for implementation, not architecture**: the exact native mechanism for reading
current Assist exposure state and observing changes to it could not be verified from available
documentation, mirroring the identical gap DL-60 accepted for native environmental slots (verified
individually under DL-30 at implementation time rather than blocking the architectural decision on an
unverified mechanism).

See `docs/models/room-configuration.md` and `docs/architecture/home-assistant-boundary.md`'s expanded
*Exposure precedence* section.

---

### Notes on the Repairs projection decision

**OD-60 closed as DL-65.** The architecture-owner's suspicion was confirmed: several candidate Repairs
conditions the original issue listed had already been reassigned by DL-60 through DL-64, and the
review's job was to make that reassignment explicit rather than leave OD-60 re-litigating settled
ground. Environmental-proposal divergence was already narrowed to a configuration condition by
**DL-60**; conflicting Person/Pet/Asset requirements and Provider-Derived Indicator differences were
already excluded from Truth-conflict scope, and by extension from Repairs, by **DL-61**/**DL-62**;
persistent Truth conflicts were already bounded to *"evaluated against OD-60's own
administrator-correctable-defect criteria separately from the runtime outcome"* by **DL-63**; and
Identity's own validity/applicability outcomes were confirmed permanently self-resolving, never
Repairs-eligible in their own right, by **DL-64**.

**The central mechanism question — is a Repairs issue the defect, or a projection of one — was settled
by direct verification of official Home Assistant developer documentation**, not by preference. HTBW
does not merely infer the projection model from DL-31's general pattern: the platform's own Repairs
lifecycle proves it. An integration calls `async_create_issue` and `async_delete_issue` itself; Home
Assistant performs no independent defect detection of its own. **Ignoring an issue does not delete it
or resolve it** — an ignored issue persists in the registry, suppressed only from the dashboard, until
the owning integration deletes it (because its own defect state cleared) or the resident completes its
repair flow. This directly proves the architecture-owner's expected model — `HTBW Defect State →
Repairs Projection`, never the reverse — because Home Assistant's own registry has no other way to
learn that a defect resolved except being told so by the integration that is, definitionally, the
authority on its own defect state.

**This also settled the re-raise question without inventing a timer.** Because ignoring never clears
the underlying condition and Home Assistant persists the issue until HTBW itself deletes it,
"re-raising" is nothing more than the owning responsibility's own **existing** state-evaluation trigger
— a Room Configuration change, a DL-41 capability re-check, a startup reconciliation — recreating the
issue if the condition still holds. No second lifecycle framework, and no arbitrary recheck interval,
was created; this mirrors the same discipline applied to DL-63's persistent-conflict recording and
DL-64's rejection of fixed validity windows.

**A single unifying eligibility test was extracted** from the category-by-category review, so future
decisions (**OD-59**, **OD-68**, and any new capability) do not have to re-derive it: Repairs is for a
**configuration or dependency defect an administrator can correct through Home Assistant's own
administrative surfaces** — never a difference between two legitimately configured values, never a
Truth/Identity runtime outcome that resolves itself as evidence changes, and never anything that names
or implies a household obligation, a person's care, health, or performance. **Fixable-through-repair-flow
is reserved for changes HTBW can make deterministically and non-judgmentally** (removing a stale
reference); a choice between two legitimately configured options remains informational-only, because
**Repairs must never become configuration authority**.

**Severity was resolved by verification, not invention**: Home Assistant's own `IssueSeverity` has
exactly three values (`CRITICAL`, `ERROR`, `WARNING`), and HTBW maps onto them from each owning
responsibility's already-accepted state — never from Stewardship significance or Operational Trust
Urgency, preserving **DL-46**'s existing boundary rather than creating a new one.

See `docs/architecture/home-assistant-boundary.md`'s expanded *Repairs is a surface, not an owner*
section, `docs/models/truth.md`'s *Persistent conflict and Repairs*, and `docs/models/room-configuration.md`.

---

### Notes on the assertion validity, applicability, and retention decision

**OD-15 closed as DL-64.** The review began from the architecture-owner's suspicion that "assertion
lifetime" hid a conflation, and the repository's own history confirmed it before any new text was
written: the DL-39 acceptance episode already states *"assertion validity is not current-interaction
applicability"* verbatim, the DL-38 fusion episode already states *"OD-15 keeps assertion lifetime,
which is not observation freshness,"* and a later episode had already recorded, without closing the
decision, *"OD-15 is amended for boundary only, and is not closed. Validity is a window; applicability
is a question about this interaction."* `person-and-identity.md` had independently grown two sections
that were quietly in tension: an older *"Identity assertions are short-lived"* passage suggesting
band-dependent expiry windows (Model A), and a fuller, later *"Current-interaction applicability"*
section already arguing that a valid assertion need not be reused at all, because every interaction
evaluates current eligible evidence fresh (Model C). **This was the hidden conflation** — not a
missing decision, but two unreconciled drafts of the same boundary, one of them still implying a timer
that the rest of the architecture had already made unnecessary.

**Three concepts are now formally separated.** **Assertion Validity**: an Identity Assertion, once
produced, is a permanently correct historical record of what evidence supported at that moment — it is
never revoked or decayed by elapsed time, and it does not need to "expire" for the architecture to
behave correctly, because nothing downstream treats an old assertion as current merely because a clock
has not run out. **Current-Interaction Applicability**: whether an assertion is evidence-appropriate
for *this* interaction — answered not by consulting a stored expiry timestamp, but by triggering a
**fresh** run of DL-38's Fusion Function against current eligible evidence, which already carries its
own per-source freshness windows, graduated reduction, and hard cutoff as **Fusion Policy**
configuration. **Retention**: already fully settled by DL-47 (a persisted Assertion is retained with
its Decision Trace or governed history, never a separate universal duration) and untouched here.

**Model C (historical validity + condition-bounded applicability re-evaluation) was chosen over Model A
(fixed per-band timers) on repository evidence, not preference.** DL-38 states plainly that "no
duration is prescribed" for observation freshness, and DL-39 states that "every interaction is
evaluated from current eligible evidence" and that HTBW creates "no long-lived Identity session." Both
already point at Model C. **The Voice Identity implementation evidence previously recorded against
this decision** (band-dependent 30/15/5-second windows with a 60-second hard cap) is not contrary
evidence: under the same reasoning already applied to OD-16's fusion coefficients, these numbers are
**Fusion Policy configuration for an assertion-reuse cache**, a legitimate performance optimization
equivalent to "would fresh fusion produce the same result," never a second architectural validity
mechanism. **No fixed duration was invented to close this decision**, honoring the mission's explicit
instruction not to select windows before determining whether windows were required at all.

**The one genuinely open question — cross-purpose assertion eligibility — is now accepted**, extending
rather than merely cross-referencing the boundary **DL-63** had already recorded as evidence: a prior
purpose-specific Assertion's contribution to a later, different-purpose determination ends when the
supporting Room's occupancy transitions to `unoccupied`, or the Person's configured primary evidence
source no longer supports that Room. **Applicability is confirmed to precede DL-63's conflict
qualification order**: an inapplicable Assertion is excluded as ineligible evidence inside DL-38's own
fusion, and never reaches Truth as a candidate claim requiring conflict resolution at all.

**No new responsibility, event type, or store was created.** Applicability loss is a consequence of
Fact-level transitions (for example a Room Occupancy Fact's own DL-25 lifecycle transition) the
existing Domain Event mechanism already records, not a new "assertion expired" event.

See `docs/models/person-and-identity.md`'s reconciled applicability and validity sections, and
`docs/contracts/identity-contract.md`'s parallel guarantees.

---

### Notes on the genuine Truth conflict decision

**OD-19 closed as DL-63.** Grounding began by inventorying every conflict scenario the original issue
raised and classifying each against DL-58 through DL-62: the two-thermostats and two-humidity-sensors
examples were written before Primary Authority became required and are no longer Truth conflicts at
all — an unselected sensor was never a competing Room authority, it is a source-specific diagnostic
value; the native-Area-versus-HTBW-input-set question is already settled as configuration divergence by
**DL-60**; the person-associated-device (watch-versus-phone) example belongs to **DL-38**'s Identity
Fusion Function while evidence is being fused into one purpose-specific Assertion, not to Truth's own
conflict rules. What survived scrutiny as **genuinely** OD-19's — two independently eligible,
semantically comparable current claims for the same Subject/predicate/context/time that remain
incompatible after every accepted authority, validity, availability, configuration, Identity, and
Stewardship boundary has been applied — was already partially answered by `truth.md`'s existing
*Conflicting evidence* and *Location conflict cases* material (permitted outcomes: reduced confidence /
unresolved / `unknown` / withdrawn; the device-left-behind, pet-tag, and declared-versus-current-location
cases). **DL-63's contribution is the general governing procedure those specific cases already
implied but never named**: a fixed qualification order that must run before any contradiction
determination (so an expired, unavailable, unselected, or differently-scoped claim is excluded *before*
it can ever be called "conflicting"), a versioned Fact-class **Conflict Policy** in place of a universal
numeric threshold, an explicit rejection of universal provenance-class precedence, reuse of the
existing Domain Event / temporal-record mechanism for persistent-conflict lifecycle rather than a new
event model, and an explicit Repairs boundary (**OD-60**) separating an administrator-correctable
configuration defect from ordinary transient runtime disagreement.

**Two related open decisions were deliberately not touched.** **OD-15** (Identity Assertion Lifetime)
retains sole ownership of whether, and for how long, a prior purpose-specific Assertion (for example a
Speaker Attribution) remains eligible evidence for a later, different-purpose determination (for
example Room Presence) — DL-63 consumes OD-15's own already-recorded boundary condition (a break on
occupancy transitioning to unoccupied, or the Person's configured primary evidence source leaving the
Room) without redefining it, and does not resolve OD-15. **OD-72** (Unknown Actor Correlation Confidence)
was reviewed and found unaffected: it concerns grouping *historical* observations into hypotheses while
identifying nobody, a different question from a *current* Truth Fact conflict between eligible claims,
and DL-63 does not reuse or alter its boundary.

**No new responsibility, engine, or store was created.** Truth's existing permitted-outcome vocabulary
(reduced-confidence Fact, unresolved Fact, `unknown`, withdrawn) is accepted as-is; the qualification
order and Conflict Policy formalize how Truth reaches that vocabulary, and the Domain Event mechanism
already accepted for Fact lifecycle transitions is reused unchanged for conflict appearance and
resolution.

See `docs/models/truth.md`, *Genuine Truth Conflict (DL-63)*, and `docs/contracts/truth-contract.md`'s
parallel guarantee section.

---

### Notes on the provider-derived environmental indicator clarification (DL-62)

**No decision was created, reopened, or amended by this work.** This is a documentation clarification
of **DL-62**, prompted by architecture-owner-supplied evidence about the air-Q device's Home Assistant
entity exposure (Dew Point, Mold-Free Index, Health Index, Performance Index, Virus Index) — no local
implementation of an air-Q integration exists in this portfolio at the time of review; the evidence is
external product documentation, evaluated as rank-4-equivalent input, not code inspected in-repo.

**The clarification**: DL-62's Formula-Derived Fact concept applies only where **HTBW itself performs
a derivation**. A provider's own internal calculation — however many measurements or trends it
combines — never converts a selected entity into an HTBW Formula-Derived Fact; it remains an
**Authority-Derived Fact** sourced from a **Provider-Derived Environmental Indicator**, exactly as a
Direct Environmental Measurement is. This was implicit in DL-62's original text ("the specific formula
remains implementation mapping") but had not been named as its own classification axis, distinguishing
*who calculates the value* (provider vs. HTBW) from *what mechanism produces the Truth Fact*
(Authority-Derived vs. Formula-Derived vs. Composite). The two axes were at risk of being conflated the
first time a real multi-input provider indicator (air-Q's Health Index, Performance Index) was
encountered, since a superficial reading of "combines more than one measurement" could wrongly suggest
Formula-Derived Fact treatment, re-derivation, or validation of the provider's internal calculation —
none of which DL-62 ever required or permits.

**Household-facing outcome preserved**: a Room may display a selected provider's Health Index,
Performance Index, Mold-Free Index, and Virus Index as provider-attributed Environmental Indicators
alongside its direct measurements; Stewardship continues to evaluate each Person's, Pet's, and Asset's
explicitly configured Environmental Requirement independently against current Room Environment Facts,
and a favorable or unfavorable provider index never overrides, proves, or diagnoses that evaluation
(**DL-61**, unaffected).

**Implementation evidence recorded, not fixed** (out of scope, different repositories): Asset
Intelligence's `environment.py` computes its own `_calculate_mold_index` — an Asset-Intelligence-invented
formula from temperature, humidity, and derived dew point, predating this repository's governance —
which is exactly the invention DL-62 declines to make canonical ("Mold Index... remains unresolved; no
HTBW-endorsed formula exists"). This is legacy rank-4 evidence, already broadly covered by the existing
Asset Intelligence legacy capability harvest (register **#155**); evidence posted there, not fixed here.
Concierge's existing "Room Confidence"/"People Health" selectable labels (already tracked on **OD-69**,
closed as **DL-61**) remain the same previously-found conflict — unchanged by this clarification.

See `docs/models/truth.md`, *Direct measurements and provider-derived indicators are both
Authority-Derived (DL-62 clarification)*, and `docs/models/room-configuration.md`, *A Primary Authority
may be a Direct Environmental Measurement or a Provider-Derived Environmental Indicator (DL-62
clarification)*.

---

### Notes on the composite-fact and Primary Authority decision

**OD-17 closed as DL-62**, following an architecture-owner-directed second reconciliation review after
the earlier DL-60/DL-61 scope-narrowing (recorded below). The review's central test was: *does any
accepted household outcome require combining multiple equivalent measurements of the same
Environmental Purpose into one authoritative Room Fact?* An exhaustive inventory of every canonical
scenario mentioning multiple environmental sensors found none — Scenario 6 of
`room-vocabulary.md` and the humidity examples in `stewardship-obligations.md` and
`stewardship-use-cases.md` were illustrative worked examples written before **DL-60** existed, not
evidence of an accepted requirement, and all three have been corrected to the **Primary Authority**
framing this decision establishes. The Asset Intelligence implementation's `"aggregation": "mean"`
configuration pattern (harvested as rank-4 evidence against the original OD-17) was confirmed as
historical implementation evidence only, not proof of a genuine household need.

**Composite Contributor is removed, not narrowly retained, from the ordinary Room Environment path** —
Disposition A of the review's own framework, chosen over narrow retention (Disposition B) or advanced
availability (Disposition C) because no accepted use case, contract requirement, or Home-Assistant-First
justification survived scrutiny, and **DL-30**'s burden of proof was never discharged for inventing a
bespoke aggregation algorithm. Home Assistant's native **Min/Max** helper was verified (official
integration documentation) to compute `mean`/`median`/`min`/`max`/`range`/`sum` across multiple
same-unit entities already — meaning any genuinely narrow future same-purpose aggregation need is
satisfied without a new HTBW engine, discharging DL-30 in advance without inventing the mechanism
speculatively today. The Statistics and Filter helpers were also reviewed and found to operate on a
single source sensor's own history, never combining multiple entities, and so are not applicable to
this question.

**This narrows DL-60's four-state disambiguation to three** (Primary Authority, Secondary/Corroborating,
Explicit Exclusion) by later clarification, not by silently rewriting DL-60's historical acceptance
record — DL-60's Part 1 row is left untouched as an accurate record of what was accepted at that time.
Formula-Derived Facts (Dew Point, Mold Index, Condensation Risk) were confirmed structurally distinct
from same-purpose aggregation throughout: they combine **different** Environmental Purposes' Facts, and
their governance (input availability, provenance, versioning, failure semantics) is the substantive
content OD-17 retained and closed. Dew Point's formula class and versioning discipline were found ready
to accept; Mold Index and Condensation Risk were found to have no HTBW-endorsed formula and remain
unresolved, deliberately, rather than invented under schedule pressure.

---

### Notes on the environmental stewardship and legacy-terminology decision

**Recorded 2026-09-15. OD-69 is closed as DL-61.** A Room has no intrinsic universal health state; it
has current Environmental Facts under **DL-60**. Whether those conditions are suitable depends entirely
on whose requirement is being evaluated, and that evaluation is Stewardship's, not Truth's and not the
Room's.

**Asset-derived Entity projection (OD-69's own original scope) is resolved conservatively**: a
projected Entity reuses Stewardship's existing obligation vocabulary and Truth's existing Fact
vocabulary — never an invented scale. It resolves back to its Asset, projects `unknown` honestly rather
than a stale value, and is structurally never a second authority, including against external writes.

**Person Environmental Requirements formalize an already-flagged architectural expectation** — the
Aging-Parent Support use case's *"Accessibility and environmental support requirements"* row, previously
status **E**, is now **A**. The pattern is not invented; it is the Asset environmental-limit pattern
(declared limit + Truth Fact + Stewardship evaluation), already accepted for Assets, extended to Person
Setup exactly as Stewardship's own scope of care already includes *"people where consented"*
(`stewardship-contract.md`). No new responsibility, no new authority model, and no conversion of a
Person into an Asset was introduced. Self- and proxy-configuration reuse **DL-56** and **DL-57**
exactly — an authenticated administrator may facilitate a requirement for a minor or a dependent Person,
recorded as acting-as-proxy, with formal legal or medical sufficiency asserted by nobody.

**Preference, Requirement, and medical/clinical threshold are kept as three distinct kinds.** HTBW
invents and validates no clinical threshold; a Requirement drives Stewardship evaluation; a Preference
guides personalization; neither becomes a diagnosis.

**Location-driven evaluation is bounded exactly as Truth and Stewardship already require**: a Person's
requirement is evaluated only while a valid Contextual Person-Presence Fact places them in the Room
(**DL-59**); unknown location produces no current suitability claim, and the prior Room is never
substituted as current. A missing required Fact evaluates to `unknown`, never met, unmet, healthy, or
unhealthy. **Every Person, Pet, and Asset in a Room is evaluated independently** — no averaging, no
ranking, no silent resolution of conflicting requirements.

**Three measures are kept permanently separate**: **Configuration Completeness** (how much of a
household's *selected applicable* Environmental Purpose set has a configured source — a Room
Configuration concern), **Environmental Coverage** (how many of the *configured* purposes currently have
a valid Fact — a projection over Truth's existing per-Fact validity), and **Truth Confidence**
(**DL-58**, per-Fact only). An unconfigured but inapplicable purpose (no UV requirement in a Room with
no UV sensor) never counts against either measure — missing configuration is not an environmental
failure, and unavailable current data is not missing configuration.

**Room Environmental Status is accepted as a non-authoritative dashboard projection** over current
per-subject Stewardship evaluations, never a Truth Fact, never a probability, never medical or clinical.
Any presentation color is presentation only; every projected state must drill through to its subject,
Fact, requirement, evaluation, significance, provenance, confidence, and validity.

**Room Health, Room Confidence, and People Health are formally rejected as authoritative terms**,
extending **DL-60**'s prior finding by name in `glossary.md`'s Rejected Terms table. Room Health
decomposes into current Facts, Coverage, Completeness, and an Environmental Stewardship Summary; a
legacy "sensors configured over all possible dimensions" calculation is renamed Configuration
Completeness, never Confidence; People Health is replaced by Person Environmental Requirements and their
per-requirement evaluations. **The Concierge implementation conflict DL-60 already found and routed to
this issue** (`environment_information_outputs` offering "Room Confidence"/"People Health" as selectable
labels) **remains unfixed by this decision** — it is implementation remediation in a different
repository, outside this review's scope, and is reaffirmed rather than resolved here.

**No diagnosis, clinical advice, wellness score, medical claim, or life-safety guarantee is introduced
anywhere in this decision.** No new responsibility, second environmental model, duplicate Person/Asset
configuration, or synthetic authority was created. Home Assistant was not installed. No runtime
behaviour was implemented.

---

### Notes on the Room Environment Standard and native environmental slot decision

**Recorded 2026-09-15. OD-61 is closed as DL-60.** A native Area environmental entity slot
(`temperature_entity_id`, `humidity_entity_id`, and any future documented slot whose semantics
correspond to an accepted Room Environment Purpose, each verified individually under **DL-30**) seeds
a **default proposal** for that purpose — mirroring **OD-14**'s naming precedent exactly. It is never
automatic silent participation (**DL-11**), and the household is never asked to reconfigure information
Home Assistant already holds (**DL-31**). An explicit HTBW selection or exclusion, once made, is never
silently overridden by a later native reassignment; the later change becomes a new proposal alongside
the existing configuration, and the divergence is a Room Configuration condition — explainable and
reviewable, never a Repairs defect (**OD-60** is unaffected) and never a silently changed Fact. **HTBW
never writes the selection back to the native Area assignment.**

**The Room Environment Standard is accepted as an extensible household-oriented Environmental Purpose
schema** — temperature, humidity, dew point, illuminance, UV, VOC, particulates, CO2, mold index, leak,
pressure, vibration, noise, and window/orientation/exposure characteristics among others — reconciling
validated Asset Intelligence implementation evidence (rank-4) as a workable purpose taxonomy without
treating Asset Intelligence as its canonical owner. The set is never closed, never claims a household
has every sensor, never invents a reading for an absent one, and never converts an absent sensor into
a normal, healthy, or safe default.

**Multiple same-purpose sources are disambiguated as four distinct, non-collapsible states**: **Primary
Authority** (at most one per purpose, for direct Room-level questions), **Secondary/Corroborating**
(supporting evidence, not the direct answer), **Composite Contributor** (feeds an **OD-17** Composite
Fact), and **Explicit Exclusion**. Runtime never arbitrates among equivalent same-purpose sources by
order, recency, or vendor preference — only the household's Room Configuration selection determines the
primary. **One Room Environment configuration serves both direct current-state questions and
composite/care derivations**; Concierge, Stewardship, Asset care evaluation, and Truth all consume the
same participant and authority selection — no separate mapping is created per consumer, directly
satisfying the architecture-owner's "configure the Room once" outcome.

**Merged Rooms surface eligible sources from every constituent Room with the source Room visible**; no
entity is copied; Room Configuration selects constituent-Room sources into the Merged Room's own
primary/secondary/composite/excluded states per purpose; **OD-17** computes the resulting Composite
Fact and **OD-19** handles disagreement — neither is decided here.

**A derived Environmental Purpose** (for example dew point, derived from a Room's configured
temperature and humidity) is declared by Room Configuration and computed by Truth as an application of
its existing Composite Fact concept — a documented deterministic formula combining more than one input,
rather than a same-dimension aggregation choice. The specific formula is implementation mapping, not
decided here; a missing required input Fact makes the derived Fact `unknown`, never invented.

**Room Health, Room Confidence, and People Health remain non-authoritative and uninvented**, reaffirming
the already-accepted prohibition in `stewardship.md` (cross-referencing **OD-69**): no synthetic Room
Health, Room Confidence, or People Health verdict exists in canonical architecture. **A conflict was
found, not resolved, and is recorded rather than hidden**: current Concierge implementation evidence
(`environment_information_outputs`) literally offers **"People Health"** and **"Room Confidence"** as
selectable household-facing output labels, which is inconsistent with this prohibition. This is
**implementation remediation evidence, not an architecture change** — no runtime or implementation
change was made in this review, consistent with the instruction not to implement outside a separately
governed implementation issue. An evidence comment was posted to **OD-69** (#142) carrying this finding;
a narrowly scoped Concierge implementation-remediation issue is recommended as follow-on work, to be
raised in the `concierge` repository, not this one.

**No new responsibility, second Room registry, environmental state store, sensor registry, vocabulary
system, or composite-fact store was created.** Room Configuration's existing three-state participation
model (Participating / Not Selected / Deliberately Excluded) was extended per Environmental Purpose,
not replaced. Home Assistant was not installed. No runtime behaviour or consolidated user interface was
implemented.

---

### Notes on the Fact validity and current-state evaluation decision

**Recorded 2026-09-15. OD-18 is closed as DL-59.** Truth distinguishes two Fact source shapes —
**Current-State Sources** and **Point-in-Time Observation Sources** — classified by documented
integration semantics, never by domain or device class alone. For a current-state determination,
Truth evaluates the most current authoritative Home Assistant state available at evaluation time,
exactly as the household would by looking at the current dashboard, and never prefers an older cached
HTBW interpretation over healthier newer native state; no HTBW-imposed generic delay is applied to a
healthy current-state source. A current-state Fact ceases being current immediately — never through
elapsed HTBW time — when its source becomes unavailable, becomes unknown, or its documented semantics
no longer support the claim. A point-in-time observation carries an operational validity window; when
it elapses the Fact **operationally expires**; `expired`, `unavailable`, and `never observed` remain
three distinct, always-named outcomes.

**Truth Confidence (DL-58) and Fact Validity are separate dimensions, permanently.** The confidence
originally established for a Fact is never decayed by elapsed time alone — validity states whether the
Fact remains current; confidence states how strongly it was supported when established. Operational
expiration is one of DL-25's eight Truth lifecycle transitions, materialized through the existing
Domain Event / Change Record mechanism; no second event model was created, and there is exactly one
authoritative validity result — consumers reevaluate on that event or, where it has not yet
materialized, at query time.

**On-demand refresh is bounded, not universal.** Home Assistant's `homeassistant.update_entity` action
("forces one or more entities to refresh their data right away") was verified as the native mechanism,
but per official Home Assistant developer documentation an entity is either polled on an interval or
pushes its own updates when the underlying event occurs — a refresh request asks the integration to
refresh, and never manufactures a physical observation or proves one occurred. Push-only, event-driven,
and advertisement-based sources (BLE proximity, PIR motion, doorbell events) may not support a
meaningful forced refresh at all. Any claim that a specific integration supports forced refresh must
discharge DL-30's burden of proof per integration; none is asserted as universal here.

**Expired or unavailable presence never decays into absence or solitude** (DL-34). Room Occupancy (a
Room-subject current-state Fact) and Contextual Person-Presence (a Person-subject Fact Truth derives
by consuming an Identity Assertion as one input, per the already-accepted DL-38 fusion and the
already-accepted "Identity assertions become presence facts" rule in `truth.md`) remain exactly the
Facts already defined; this decision redefines neither.

**Freshness and validity windows are household configuration values, not architecture**, mirroring
DL-47's own established pattern: per-class and per-Subject differentiation is available where a
household chooses it, never overriding consent, never converting last-known into current, and never
silently learned (P26, DL-21).

**Scope boundaries honoured, not absorbed.** This decision does not decide, and does not pre-empt:

- **Contextual Person-Presence multi-evidence combination** (occupancy + person-associated BLE +
  voice-derived evidence) — already accepted architecture under DL-38 (Identity fusion) and Truth's
  existing single-input consumption rule; no gap exists, and OD-17 does not own it either, since OD-17
  governs environmental/device Composite Facts only.
- **Person-specific evidence reliability** (for example a configured-stronger watch versus a
  configured-weaker phone) — already accepted architecture under DL-32/DL-38's Identity Evidence
  Association model; no universal device-type precedence was created or considered.
- **Whether a purpose-specific assertion (for example Speaker Attribution) remains eligible evidence
  for a later, different-purpose assertion (for example Room Presence)** — this is OD-15's own
  remaining question 6, genuinely open, and is not decided here. An evidence comment was posted to
  OD-15 (#96) carrying the voice-interaction-continuity scenario as acceptance-scenario material.
- **Watch-versus-phone and other person-associated-device conflicts** — OD-19's own scope; an evidence
  comment was posted to OD-19 (#90).

**No new responsibility, Fact class, event model, or store was created.** Home Assistant was not
installed. No runtime behaviour was implemented.

---

### Notes on the Truth Fact confidence decision

**Recorded 2026-09-15. OD-74 is closed as DL-58.** Truth Fact Confidence describes the strength of
qualified evidentiary support for a Fact under the applicable Truth evaluation policy — never
probability, measured accuracy, certainty, or Identity Confidence — and is represented as one
uniform ordinal band, Low < Moderate < High < Very High, applied identically across every Fact Subject
(Home, Room, Merged Room, Person, Pet, Asset, Device) and Fact class. Per-Fact-class derivation,
evidence ceilings, and publication requirements may differ; the vocabulary does not.

**Structural separation from DL-39 is explicit and permanent.** A Truth Confidence Band and a DL-39
Identity Confidence Band share household-facing labels but are separately owned, separately typed
concepts: `truth_confidence_band` and `identity_confidence_band` in machine form, never a shared
generic confidence field. A Pet, Asset, or Device Fact is structurally unable to carry an Identity
Confidence Band. The two-stage Person-location path is preserved exactly: Identity produces a
purpose-specific Identity Assertion carrying its own band; Truth then evaluates eligible inputs and
may publish a Contextual Person-Presence Fact carrying its own, independently derived Truth Confidence
Band. The two values are never converted, averaged, or compared as though they measured the same
thing.

**Confidence, freshness, provenance, and coverage remain four separate mandatory Fact dimensions**,
never collapsed into one field. **OD-18** owns freshness and validity effects; **OD-17** owns
Composite Fact derivation and what contributor coverage (for example *2 of 3*) means for a published
band; **OD-19** owns conflict-resolution effects. None of the three redefines the representation this
decision accepts, and none may borrow the Identity Fusion Function or DL-39 bands — the same
prohibition **OD-72** already observes for unknown-actor correlation confidence.

**An optional normalised numeric may accompany the band as a non-authoritative deterministic ordering
value only** — never resident-facing probability, likelihood, calibration, or accuracy, and never
authorizing anything. No such numeric is mandated by this decision; none is introduced into the
canonical model, since no accepted consumer currently requires one.

**Every informal canonical `confidence: high` and raw-numeric Identity-confidence usage was corrected
to the typed representation** across `truth.md`, `truth-contract.md`, `decision-trace.md`,
`person-and-identity.md`, `identity-contract.md`, `failure-and-degradation.md`, and the affected
canonical scenarios. The historical/superseded `occupancy-presence-model.md` numeric `0.92` and
`provenance-model.md` numeric examples were left untouched as historical evidence, consistent with
their existing non-authority status, and `occupancy-presence-model.md`'s own callout is updated to
point at the resolved decision rather than an open one.

**No new responsibility, Fact class, parallel location-assertion type, per-Subject confidence model,
probability model, accuracy model, second Truth representation, or store was created.** Home Assistant
was not installed. No runtime implementation was added beyond documentation.

---

### Notes on the delegated Stewardship authority decision

**Recorded 2026-09-15. OD-76 is closed as DL-57.** One person may hold explicit, scoped Stewardship
authority delegated by another — over a Person's care, an Asset's conservation, or a Pet's care —
never through role, relationship, or administrator-status inference. The **Delegated Access Grant**
gives this one reusable shape: subject, grantee, explicit non-collapsible operations (view / receive /
declare / update / schedule / complete / manage), scope, grant basis, and effective/revocation time.
Foundation continues to type `caretaker-of`/`owner-of` as accountability records; Stewardship owns the
grant's record and lifecycle, the same division **DL-49** already established for Custody Periods.

The capacity question is addressed rather than left silent: a competent adult retains self-authority
and may delegate; a minor or a person unable to act independently may be represented by an
authenticated administrator acting as proxy — extending **DL-56**'s proxy placeholder rather than
duplicating it. **A native Home Assistant administrator flag is never itself care, guardianship, or
proxy authority**, and formal legal qualification (guardianship, power of attorney, conservatorship)
is explicitly outside HTBW's scope: HTBW records that a proxy grant was established and by whom, and
asserts no legal sufficiency.

Identity evidence never transfers with a grant — a caretaker's device or voiceprint is never evidence
for the cared-for person, and where a proxy-facilitated identity class cannot be usably provided by
the subject, that class is **unavailable** under **DL-41**, never manufactured or substituted; Voice
Identity is never required for Stewardship participation. A non-resident authorized participant (a
housekeeper, dogsitter, sculpture conservator, or collections administrator) may hold a **minimal
Person record** carrying only the grants explicitly configured for them — no second Person directory,
no new occupational-role authority. Revocation is immediate and prospective; existing obligations
remain Stewardship-owned governed records the household may reassign; historical actions remain
attributed to the actor and grant valid at the time.

**OD-22's escalation ladder is not automatically triggered by an incomplete obligation.** Stewardship's
own existing language — escalation means changing *who* is accountable — is applied literally: ordinary
continuing notification with accountability unchanged requires no new construct, and OD-22 applies only
where the household has configured an actual accountability change.

**Scope boundary honoured, not absorbed: OD-77 (Person-to-External-Resource Association Ownership)**
remains undecided and is not pre-empted here. OD-76 defines the general delegated-authority *grant*
primitive over Stewardship subjects (Person care, Asset conservation, Pet care); OD-77 separately owns
*which responsibility names the association* between a Person and an external account, calendar, or
mailbox. A future combination — one person's Delegated Access Grant reaching an external resource that
OD-77 anchors — is for OD-77 to accept once it resolves ownership, not decided here. An evidence
comment was posted to issue #148 accordingly.

**No Care, Caregiver, Guardianship, Delegation, or Authorized Abilities responsibility was created.**
People remain Persons, never Assets. No second Person directory was created. Home Assistant was not
installed. No runtime behaviour was implemented beyond what a separately governed implementation issue
requires.

---

### Notes on the consent decision

**Recorded 2026-09-15. OD-06 is closed as DL-56.** The consent scope model (participation-based at
the household surface, precise underneath), the canonical consent record, Person Setup's architectural
placement, self/proxy consent, contextual continuity, withdrawal/deletion, the DL-43/DL-47
reconciliation, duration and renewal, historical explainability, and the six state distinctions are
accepted; full text is **DL-56** above and
[person-and-identity.md](../models/person-and-identity.md#consent-dl-56).

**The OD-06/OD-76 boundary is preserved, not duplicated.** OD-06 establishes that self- and
proxy-consent paths exist, that a proxy action must be explicit and authenticated, and that it must
never masquerade as self-consent. **Who qualifies as an authorized proxy** — administrator eligibility,
parent/guardian/caregiver/steward authority, capacity, delegation, revocation, and competing-proxy
conflict — **remains entirely OD-76's**, updated with this evidence on issue #106 but not decided
here. A native Home Assistant administrator flag is explicitly never treated as care or proxy
authority.

**Frequent-guest / ad-hoc continuity had no existing canonical owner** — verified: no repository
document uses "Frequent Guest," "remember me," or an equivalent term as an accepted concept prior to
this decision. It is folded into OD-06 itself as a contextual Person Setup path, per the issue's own
framing, rather than filed as a separate issue.

**Exceptional retrospective correlation for legal or incident requests has no existing canonical
owner** — verified: only the generic legal/regulatory non-claim exists across several ADRs, which is a
disclaimer, not an authorization framework. Raised as **OD-89 (#183)**, explicitly bounded so it
creates no consent bypass and preempts none of its own eventual alternatives.

**Home Assistant First (DL-18) discharged**: config/options-flow-based Person Setup, extended with
explicit per-action disclosure, is confirmed sufficient; no bespoke consent UI standard is introduced.
The native Person entity's `user_id` linkage supplies the proxy-consent audit actor; its binary
administrator flag is confirmed insufficient, and is not used, for authorizing proxy scope.

**Residual decisions updated with evidence, not closed**: **OD-76** (#106), **OD-65** (#130), **OD-09**
(#78), **OD-36** (#82), **OD-07** (#95) each receive this decision's evidence; none is closed by it.

### Notes on the dynamic capability discovery and room-outcome decision

**Recorded 2026-09-15. OD-88 is closed as DL-55, a governance-harvest outcome: no new responsibility,
no new capability-discovery subsystem, and no Presentation Grid authority was created.** Every
question the issue raised reduced to an existing owner:

- **Provider/execution selection** — `room-configuration.md`'s existing rule that *"the participating
  target or capability is identified explicitly"* already means the household's concrete native
  reference, not an abstract capability class, so no runtime provider-precedence mechanism is
  needed. A non-selected provider may still contribute evidence through Truth; it never becomes a
  competing execution authority.
- **Endpoint identity across providers** — the existing Asset model already states that **"a single
  physical object may be an Asset and be represented by several Devices and many Entities"** and that
  such an Asset **"remains the single household-meaningful object"**. Where no Asset is declared, the
  participating target's own native reference is sufficient; no new identity construct was needed.
- **Room-level outcome** — genuinely narrow new content, accepted here: a Room-defined outcome across
  several participating endpoints is `Presented` where at least one succeeded, carrying a **Degraded**
  label when any did not, added as a new row in `failure-and-degradation.md`'s Required behaviors
  table, extending its existing partial-speaker-group precedent. Endpoint-level **DL-54** outcomes are
  never averaged, scored, or replaced.
- **Device interaction versus workflow participation** — already separated by **DL-53**'s independent
  per-surface capability dimensions (Presentation Attestation Capability and Recipient Acknowledgement
  Capability are declared independently); combined with the existing confirmation-redirect mechanics
  in **DL-37**/**DL-40**, a presentation surface has never needed acknowledgement capability of its
  own.
- **Capability evolution** — already covered by **DL-41**'s dependency-health states and
  `room-configuration.md`'s existing failure-behaviour row (*"A participating target no longer exists
  → Report a broken participation reference; do not silently drop it"*).
- **Presentation Grid** — `room-configuration-contract.md` already names **"which experience endpoints
  exist (music, video, announcement, conversation)"** as Room Configuration's; this is confirmed as
  extensible household vocabulary, not a closed list requiring a new authority.

**Validation answers, for the record**: (1) provider precedence for *execution* is not required once
explicit participation is recognised as already selecting the provider; a narrower evidence-provenance
question remains but has an owner (Truth) and needed no new mechanism. (2) Not applicable — no
surviving Question 3 (superseded by the finding above). (3) A room-level outcome-**quality** label is
required and is accepted, narrowly, as a projection; a room-level outcome-**authority** is not. (4) Yes
— the existing partial-availability precedent extends cleanly. (5) Yes, confirmed. (6) No. (7) Nothing
genuinely unresolved remains outside what DL-55 states; no follow-on issue was required.

### Notes on the presentation attestation decision

**Recorded 2026-09-15. OD-55 is closed as DL-54.** The Presentation Outcome model (Presented / Failed
/ Unknown / Attestation Unavailable), the distinction between a capability limitation and a per-attempt
evidentiary gap, the modality-not-device-class evaluation rule, and the empty-room-audio worked example
are accepted; full text is **DL-54** above and [communication.md](../models/communication.md).

**The Home Assistant First review for this decision extends, and partially resolves, the burden
recorded against OD-43, OD-55, and OD-57.** Dashboard visibility and `media_player` delivery semantics
were already verified for **DL-53**. This review additionally verified Sonos, Music Assistant,
`assist_satellite`, Roku, Apple TV, LG webOS TV, UniFi Protect camera speakers, mobile (Companion App)
notifications, and `persistent_notification` — see the ADR's Home Assistant First review table.
**Every mobile-notification and `persistent_notification` presentation claim is Attestation
Unavailable**: no "displayed" event is documented anywhere for either surface, only interaction
(tap/dismiss) events, which are acknowledgement-adjacent evidence, never presentation evidence.
**The physical voice-satellite light/LED indicator remains not verified and is not required**: the
`assist_satellite` `responding` state transition, not any indicator light, is the evidence a
`Presented` claim rests on for that surface. **OD-57 still carries the unresolved portion of this
gate** for any surface it separately depends on.

**A successful service call is never evidence of `Presented`, confirmed against three separate
integrations.** LG webOS TV's `notify` action can report success while a documented firmware
limitation silently drops part of the payload; Apple TV's own FAQ states plainly that tvOS apps
decide which remote commands they honour and that device state cannot be confirmed without directly
querying it; Roku's remote commands are typed strings with no acknowledgement of on-screen effect.
**All three are classified conservatively**: `Presented` is credited only where an independently
observed platform state (a `media_player` state transition, or Roku's own `active_app` sensor)
confirms it — never from command or service-call acceptance alone.

**Residual decisions narrowed in scope, not closed**: **OD-44** (delivery outcome semantics generally)
and **OD-45** (acknowledgement) each receive this decision's evidence but keep their own remaining
questions; **OD-54** (retry) inherits the Failed/Unknown distinction as an input to its stop
conditions, undecided here.

**One cross-cutting discovery exceeded this decision's scope and is preserved, not absorbed**: dynamic,
runtime, multi-provider capability and evidence discovery for a Room-defined, possibly multi-endpoint
presentation outcome (provider precedence and conflict, endpoint identity across providers, artifact
interaction requirements, and room-level outcome-quality aggregation) has no existing owner and is
raised as **OD-88 (#182)**, distinct from Room Configuration's unchanged, already-accepted static
vocabulary-to-target mapping.

### Notes on the delivery surface capability decision

**Recorded 2026-09-15. OD-43 is closed as DL-53.** Capability dimensions, Potential Perceptibility,
split ownership, portable-surface boundary preservation, the no-private-surface rule, and the
presentation-attestation default are accepted; full text is **DL-53** above and
[communication.md](../models/communication.md).

**A supplied fourth scale was rejected as a duplicate, not accepted.** The closure proposal for OD-43
included **Recipient-Attribution Assurance Levels: `None` / `Low` / `Moderate` / `High`**, an ordered,
evidence-derived, mechanism-verified class set governing whether a confirmation or attribution result
is strong enough to authorize disclosure. **This is the same governance question DL-40 already
answers** — **Required Confirmation Strength: `None` < Verbal < Authenticated < Strong** — and **DL-37**
states plainly that *no second confirmation model exists*. The correction: **Recipient Attribution
Capability** is accepted as a declared **surface property** (what evidence a surface can supply); the
strength required to act on that evidence remains **DL-40's** alone. No new scale, threshold, or
confirmation model was created.

**The DL-30 burden the ledger recorded against OD-43 is discharged for this decision.** The *Notes on
the communication open decisions* section below required dashboard visibility semantics and
`media_player` delivery semantics to be *"located and reviewed first"* before OD-43 could close. Both
were: dashboard view `visible` is verified as a per-user **display toggle for the view tab only**
(*"the URL path is still accessible"* regardless of setting), confirming it is not an authorization
control; `media_player` state and triggers are verified as evidence of technical delivery acceptance
only, with no acknowledgement, no per-listener evidence, and no presentation-attestation capability.
**Voice-satellite indicator behaviour remains not verified** and is not required by this decision;
**OD-55** and **OD-57** still must not be closed on assumed behaviour there.

**OD-73 is not closed and is not preempted.** DL-53 states what a Delivery Surface declares for a
portable surface — capability dimensions and a Potential Perceptibility declaration that receives no
automatic privacy classification — and defers the exact Room Context resolution mechanism entirely to
OD-73, consuming whatever OD-73 accepts as one Truth input among others.

**Residual decisions unaffected in substance, narrowed in scope**: **OD-52** (audience
specification), **OD-55** (presentation attestation enumeration), **OD-57** (indication threshold),
and **OD-71** (audience-uncertainty policy) each keep their own remaining questions; none is closed by
DL-53, and DL-53 creates no new dependency any of them did not already carry.

### Notes on the Episode 10 governance narrative validation

**Recorded 2026-08-27. This review produced no accepted decision, amended none, and reopened none.**
Fifteen concepts raised by the Episode 10 Governance narrative were tested against the canonical set.
**Two open decisions were raised — OD-86 and OD-87 — and every other concept was either already
accepted, already owned by an existing open decision, or correctly absent.** The ledger moves to
**eighty-seven identifiers, eleven closed, seventy-six open**.

**The two headline doctrines are already constitutional and required no elevation.** *Household
experience is the measure of success* and *the home must not require people to compensate for
architectural complexity* are **P18** — *"Separate responsibilities must produce a unified household
experience. Residents must never be asked to understand the framework in order to use the home."*
They are reinforced by **P19**, under which **Human Trust is an outcome that is earned and never
implemented**, and by [../scenarios/README.md](../scenarios/README.md), which states that a framework
is only as good as the household outcomes it produces and that the canonical scenarios are **the
acceptance tests for the architecture**. **Restating either as a new principle would create two
authorities for one rule**, which is the defect the authority order exists to prevent.

**One concept is contradicted as worded, and is corrected here rather than accommodated.** The
proposition *"Voice Identity is a governance dependency when outcomes vary by individual"* cannot be
adopted in that form. **Voice Identity is not a responsibility** —
[adr-identity-replaces-voice-identity-boundary.md](../architecture/adr-identity-replaces-voice-identity-boundary.md)
replaced it with **Identity**, and **DL-51** states product disposition separately. **DL-41's
dependency classes are a native Home Assistant capability, an integration, a provider, Connected
Storage, consent, and configuration**, and Identity is not among them;
[failure-and-degradation.md](../architecture/failure-and-degradation.md) requires that a missing
dependency is *"never rendered as a permission or identity failure"*. The defensible content of the
proposition is already accepted in substance, and its canonical formulation is recorded here: **an
outcome that varies by person requires a sufficient Identity Assertion.** That is a **precondition**,
evaluated exactly as [../scenarios/continuity-use-cases.md](../scenarios/continuity-use-cases.md)
already states — *"applying a person's preferences is a person-scoped capability access, evaluated
against the current Identity Assertion"*. **It creates no dependency class, no new evaluation stage,
and no responsibility.**

**A person is never classified.** *Acceptance by the least technically interested participant* is
inadmissible as written, because it is a durable characterisation of a human being, and
[../contracts/stewardship-contract.md](../contracts/stewardship-contract.md) states that HTBW
*"assigns no human worth and ranks no household member"*. The admissible form is a **test applied to
a decision and to the experience it produces**: whether the outcome can be accepted and used without
requiring implementation knowledge, specialised architectural understanding, undocumented vocabulary,
or continuing intervention by whoever in the household maintains the system. **No person attribute,
score, ranking, tier, or classification is created**, and **household acceptance never overrides a
safety, privacy, consent, or Operational Trust outcome.**

**No debt construct is created.** *Experience debt*, *vocabulary debt*, *identity debt*, and
*migration debt* are admitted as **narrative and review lenses only**. The word appears normatively in
this repository exactly once — **P24, greenfield without compatibility debt** — and adding four
architectural classes named for a metaphor would duplicate questions that already have owners. Two of
the four pointed at something real, and those two are raised in HTBW's own vocabulary as **OD-86** and
**OD-87**; the other two describe residuals already carried by **OD-85** and by the transition review
on issue **#171**.

**No wake-word decision is opened.** Wake-word detection occurs **before any HTBW responsibility
engages** and is a native satellite capability, so under **P21** and the **DL-30** ordered burden of
proof it must be evaluated natively first. That evaluation already exists as **item 11 of issue
#146**, in which *HTBW builds nothing* is an explicitly passing outcome. **A wake word is
nevertheless household-facing vocabulary**, so the household-facing consequence of changing one is
admissible under **OD-86** as a sub-question and remains deferred behind #146. **No wake-word
implementation, configuration, ownership, or governance is created or implied.**

**Habit continuity and vocabulary continuity name real concerns and are not new Continuity scopes.**
[../models/continuity.md](../models/continuity.md) holds exactly two scopes — person-scoped and
room-scoped — and **their absence from those scopes must not be used to invent a third tier**. The
genuine defect sits elsewhere and is now **OD-86**: the managed-vocabulary-lifecycle authority of the
superseded `adr-room-vocabulary-governance.md` **was not carried forward** into the canonical
vocabulary set, which governs how a term is created, seeded, and resolved, and says of removal only
that a withdrawn term goes through the ordinary Room Configuration lifecycle with its history
retained. **The consequence for the people who still use the old word is ungoverned.** **Nothing here
reactivates the superseded documents.**

**A confidently wrong identity attribution has no canonical treatment, and a household-scale
re-enrolment has no owner.** `unknown` and `ambiguous` are governed thoroughly by **DL-33**,
**DL-38**, and **OD-84**, but the case in which the home understands the request correctly and acts
on **the wrong person** appears only in subordinate pattern documents and in Historical material.
Correction is constrained by **DL-32** and **DL-38**, under which an earlier assertion is never
rewritten — so a correction is a **new record**, not an edit, which is precisely why it needs a stated
owner. The larger related household event, in which an encoder, audio-contract, or comparability
change invalidates every enrolled artifact, is raised as **OD-87**. **Its mechanism is already settled
by DL-41 and is not reopened**, **OD-16 is not reopened**, and **no threshold, sample count, duration,
margin, or quality value is in scope.**

**Three gaps were tested and found already owned, and are not raised again.** *Transition governance*
and *onboarding* are the surface residual already recorded in **OD-85** and on issue **#171**;
**DL-52 governs the transfer of authority, not the whole household transition experience**, and that
clarification belongs in the ADR rather than in a new decision. *Household impact evaluation inside
the assessment record* would change the accepted meaning of a canonical document, so it is **routed
for decision**, and [../assessment/assessment-to-platform.md](../assessment/assessment-to-platform.md)
**is not edited ahead of that routing**. *The Home Architecture Workbook* is referenced by
[../architecture/north-star.md](../architecture/north-star.md) and **does not exist in this
repository** — the same defect already recorded for the visual canon on issue **#150**, and raised as
governed documentation work rather than as an architectural decision.

**This note creates nothing.** It introduces **no responsibility and no eighth layer**, **no DL-41
dependency class**, **no record class**, **no Continuity scope**, **no confidence representation**,
**no person attribute or ranking**, **no debt construct**, and **no wake-word governance**. It changes
the meaning of no accepted decision, and **the narrative remains a stress test and never authority**.

---

### Notes on the product disposition and legacy adoption decisions

**DL-51** and **DL-52** were accepted on 2026-08-26, closing **OD-82** and opening **OD-85**. They
followed a repository-grounded review of the transition strategy for Asset Intelligence, Voice
Identity, and Concierge, recorded in
[adr-product-disposition-and-legacy-adoption.md](../architecture/adr-product-disposition-and-legacy-adoption.md).

**What was actually wrong.** The non-negotiable constraint in [authority-order.md](authority-order.md)
flattened three products into one class. **Two canonical constitutional documents already disagreed
with it**: [greenfield-mandate.md](../architecture/greenfield-mandate.md) called Voice Identity and
Concierge *"exploratory projects"*, and [north-star.md](../architecture/north-star.md) called Voice
Identity *"superseded as a product boundary inside HTBW Core"* while giving Concierge **no product
disposition at all**. **The asymmetry was already in the canonical tier, and the flattening was the
defect.** These decisions correct it rather than introducing a new position.

**What was verified rather than assumed.** The release footprint of each repository was checked:
Asset Intelligence **27 releases**, Voice Identity **one release, v0.1.0**, Concierge **none**. The
premise that Voice Identity has no released-user footprint is therefore **an assumption about
installs, not a fact about artifacts**, and **DL-51** states an artifact disposition regardless of
install count. **A published artifact that is silently abandoned leaves a household with no
explanation.**

**What these decisions do not do.**

- They do **not** retire Asset Intelligence, and **DL-51** says so explicitly.
- They do **not** weaken **DL-19**. No compatibility requirement flows upward from any of the three,
  and **absorbing functionality is not adopting a schema**.
- They do **not** create a responsibility. **Adoption is a capability**, and the seven-responsibility
  framework is unchanged.
- They do **not** make Truth a recipient of adopted data. **Truth receives nothing by adoption.**
- They do **not** make Continuity depend on adopted history. Continuity's two scopes are unchanged.
- They do **not** decide **OD-20**. Runtime consumption remains open, now bounded by the rule that
  **HTBW must never require Asset Intelligence to be installed**.
- They do **not** resolve **OD-01**. Adopted records still need somewhere to live.

**The greenfield reading, settled.** [greenfield-mandate.md](../architecture/greenfield-mandate.md)
lists **migration adapters** among things that must never be introduced *as a constraint on HTBW Core
design*, and **DL-19**'s prohibited pattern is *implicit migration obligations*. **DL-52** settles
this in favour of the bounded reading: an **explicit, optional, one-way, terminating** adoption that
constrains no HTBW model is outside the prohibition, and the prohibition keeps its full force through
the rule that **unmappable content is reported as *not adopted* rather than accommodated**.

**Why Reference Over Copy does not apply to the source product's private store.** **DL-31** governs
native Home Assistant objects, which both products already reference and neither copies. Asset
Intelligence's own store is **neither a native record nor a governed HTBW record**. A Governed
Reference cannot survive removal of its referent, so a reference-only adoption would leave a household
that later uninstalled the product **holding broken references where their data used to be**. **The
copy is the correct outcome here, and lineage is what makes it honest rather than a fabrication.**

**The distinction most likely to be got wrong in implementation.** *Adopted history is not HTBW
history.* Relationships and limits are **declarations** and transfer cleanly. A service record becomes
a **Care Evidence Record of kind `attested`** — never `observed`, because HTBW did not observe it. An
observational history **never becomes a Truth Fact or Historical Fact**, because a Historical Fact
carries confidence at the time, provenance, coverage, freshness, and a **lifecycle HTBW never
executed**; adopting one would make the home assert it knew something it never knew.

**These decisions preempt nothing.** **OD-85** holds the four residual questions — granularity,
artifact custody, coexistence, and surface. **OD-36** is extended rather than reopened, to cover an
artifact whose governing parent is removed by a different product than the one now depending on it.
**OD-69** and **OD-81** continue to hold publishing conflicts, and **no third owner is created for
them**.

---

### Notes on the capability-exposure open decision

**OD-81 creates no capability, no surface, and no catalog.** It asks one previously unasked question:
whether HTBW **publishes** to Home Assistant, having only ever governed how it **consumes** from it.
Every accepted decision on the boundary — **DL-16**, **DL-30**, **DL-42**, **DL-44**, **DL-46** —
runs in the consuming direction, and the boundary document names what Home Assistant may provide and
what HTBW owns without once naming a service HTBW registers, an event HTBW fires, or an entity HTBW
creates for a resident to automate against. **DL-11's Exposure is not this question**: it is the
constitutional state of being perceptible to a resident, and it explicitly is not Home Assistant
Assist entity exposure, so it governs narrowing and never publishing.

**The question is raised as a parent, not as a replacement.** **DL-31** already anticipates the
direction for representations — where an HTBW concept benefits from native visibility, state,
targeting, or automation, a native representation is preferred to a parallel hierarchy and remains a
projection rather than a second authority — and three decisions already instantiate it for one case
each: obligations under **OD-23**, Asset-derived values under **OD-69**, and Merged Rooms under
**OD-70**. **None of those asks whether a general public capability surface should exist**, and none
addresses services, events, or self-consumption at all. OD-81 therefore sits above them and
**preempts none of them**; each may be decided before or after it, and a decision there does not
decide the general question here.

**Two invariants are already settled and are not reopened by raising this.** A projection is never a
second authority, and **Operational Trust evaluates appropriateness before any effect regardless of
who invoked it** — a public surface is a way in, never an authority bypass, and a resident-initiated
invocation is subject to exactly the evaluation an interaction-initiated one is. What follows from
that is a live concern rather than a settled one: every invocation still produces a **Decision
Trace**, so **who invoked it** becomes attribution work already owned by **OD-63** and **OD-64**.

**Publishing has a retention consequence that is not a separate choice.** **DL-42** forbids a second
Recorder, and Home Assistant's Recorder retains whatever HTBW publishes as entity state. **A decision
to publish is therefore also a decision about what is retained**, engaging **DL-47** and **OD-05**,
and that consequence must be reasoned about rather than inherited.

**Disclosure binds hardest on the most attractive proposals.** An entity state is readable by every
Home Assistant user and carries **no audience evaluation**, so publishing a Person, an identity
state, or a confidence band as an entity is a disclosure surface under **DL-34** and **DL-39**, and
privacy governance already restricts a numeric confidence value to where policy governs it and the
audience permits. Convenient automation context and governed disclosure pull in opposite directions
here, and that tension is the substance of the decision rather than an obstacle to it.

**Two vocabularies are prohibited in advance so they cannot enter through a published entity.**
**Room health is not an HTBW term**, and **HTBW defines no asset health state model** — the latter
already stated in **OD-69**. Neither may be introduced as a sensor, an event, or a catalog heading.

**This note introduces no construct.** It defines **no service**, **no event schema**, **no entity
platform**, **no household object type**, **no catalog format**, and **no self-consumption rule**. It
**amends no accepted decision** and **reopens none**. The ledger moves to eighty-one identifiers,
nine closed, seventy-two open.

---

### Notes on the voice-evidence runtime review

**Recorded 2026-08-25. Updated the same day on acceptance.** The review produced
[../architecture/adr-wyoming-compatible-voice-evidence-runtime.md](../architecture/adr-wyoming-compatible-voice-evidence-runtime.md),
**accepted as DL-50**, which closes **OD-80** and raises **OD-82** and **OD-83**.

**Acceptance settles three things and authorises no fourth.** It settles **where a capability may
execute**, **what a voice provider returns**, and **what may never happen to a transcript**. It
authorises **no implementation** — the roadmap phases are separately tracked, speaker-conditioned
extraction remains validation-gated, and passive conversation-state evidence remains a North Star that
the ADR explicitly does not approve.

**The review was a comparative examination of four third-party speaker-recognition projects for Home
Assistant, the official Wyoming protocol, and the current reference implementation.** Its principal
finding is that **OD-80's verified failure has a verified ecosystem answer**: every one of the four
projects executes its neural encoder **outside the Home Assistant Core process**, and not one attempts
in-process execution. That is evidence at step 2 of the **DL-30** ordered burden, and it is why the
decision is a rule rather than a described workaround.

**Two protocol facts were verified and are recorded because their absence is load-bearing.** The
Wyoming protocol advertises the service types `asr`, `tts`, `wake`, `handle`, `intent`, `satellite`,
`mic`, and `snd`, and **defines no speaker, identification, verification, or biometric service type
and no speaker-evidence event**. It does define `user-event`, a user-defined event carrying `name`,
`data`, and `context`, and servers are documented to drop unrecognised events. **The gap is therefore
real and the sanctioned extension path already exists**, which is why the decision records the gap and
declines to invent a protocol extension.

**One correlation finding narrows nothing and closes nothing, but it must not be lost.** Wyoming does
**not** close the correlation gap. `info.satellite.area` carries an area **name**, and **DL-31**
requires reference by stable identifier, so a satellite area name never resolves a Room by itself. The
existing position stands unchanged: evidence is produced **unbound**, the consumer supplies
correlation context explicitly, and **temporal proximity alone never establishes correlation**, which
**DL-35** already states.

**Three boundary drifts were found in the reference implementation and are recorded as evidence, not
as decisions.** A provider-emitted confidence enumeration collapses **state** and **band** into one
value, which **DL-39** separates; a provider-side attribution record resolves a person, which **DL-06**
and **DL-32** assign to Identity; and a single default confidence constant contradicts **DL-36**'s
*sufficiency is never universal*. **None of these is a new open decision.** Each is a conformance
finding against an already-accepted decision, and each belongs to implementation remediation rather
than to architecture. The same implementation is **ahead of every project reviewed** on encoder
version pinning and on the correlation boundary, and that is recorded with equal weight.

**No decision about thresholds was taken, and none was needed.** **OD-16** already resolved that
separation margins, per-purpose minimums, freshness durations, and confidence thresholds are **Fusion
Policy configuration, versioned and governed, and none of them is an unresolved architectural
question**. The review observed that the same cosine metric produces an operating point near 0.30 in
one project and near 0.82 in another, which is a demonstration of that decision rather than a
challenge to it: **a provider match value is not portable across providers**, and **DL-32**'s rule that
it is *retained as reported and never rewritten as fused confidence* is what makes the four bands the
only cross-provider currency.

**Eight harvested patterns are accepted as implementation patterns, and one of them is a
classification rather than a capability.** Out-of-process runtime, Wyoming-compatible participation,
top-N candidate evidence, channel-aware enrollment, speech-region segmentation, rejection telemetry,
and provider abstraction are adopted where appropriate. **Passive conversation-state remains North
Star only.** **Each pattern is reimplemented as an HTBW-owned contract**; every source project is
MIT-licensed; **no third-party source code is taken**; and **no single-maintainer project becomes a
mandatory dependency**, which matters because every project reviewed has exactly one contributor.

**Two residuals were separated rather than absorbed, and both separations are load-bearing.**
**OD-82** is the product-portfolio question, kept out of the ADR because a non-negotiable constraint in
[authority-order.md](authority-order.md) is changed only by a decision that names it, and the ADR
holds whichever way it is decided. **OD-83** is voiceprint gallery structure, kept out because
**recording where enrollment occurred is not the same as deciding how the gallery is structured** —
and had they been merged, the second question would have been answered silently by the first
implementation that chose a storage shape.

**One terminology question was resolved without a decision, because naming is not architecture.**
**DL-05** supersedes *Voice Identity* as a platform-service boundary, and the responsibility is
**Identity**. The out-of-process runtime keeps its released artifact name; its **architectural role
name is Voice Evidence Provider Runtime**; it is a capability component and never a responsibility.
The existing rule that implementation artifacts are not renamed to match architectural words is
applied here exactly as it was applied to Asset Intelligence.

**One contradiction was found that the review had no authority to resolve, and it was raised rather
than absorbed.** The execution premise asserted that the three standalone products are being retired
into a unified HTBW product, and [authority-order.md](authority-order.md) records their separateness
as a **non-negotiable constraint binding regardless of rank**. That is **OD-82**, and **DL-50** holds
whichever way it is decided, because it governs the responsibility architecture and not the product
portfolio.

**This note introduces no construct.** It creates **no responsibility**, **no record class**, **no
artifact class**, **no retention rule**, **no threshold**, and **no confidence representation**. It
**amends no accepted decision other than by adding DL-50**, and **reopens none**. At acceptance the
ledger stood at eighty-three identifiers, ten closed, seventy-three open; the post-acceptance harvest
recorded below moves it to eighty-four, ten closed, seventy-four open.

---

### Notes on the Episode 8 Concierge narrative validation

**Recorded 2026-08-25. This review produced no decision, and the ledger is unchanged.** Twenty
Concierge human-outcome use cases were documented in
[../scenarios/concierge-use-cases.md](../scenarios/concierge-use-cases.md) and traced against accepted
architecture. **No open decision was created, no accepted decision was reopened, and no new
construct — responsibility, record class, artifact class, retention rule, threshold, or confidence
representation — was introduced.**

**The narrative is a stress test, never authority**, and the strongest evidence that the architecture
withstood it is arithmetic. **Fourteen of twenty-four Concierge facets are already accepted, no facet
is missing, and none requires a new construct. Eleven of twenty cross-cutting questions are answered
by accepted architecture, and every one of the nine that are open is an existing open decision.**

**No use case is classified as implemented, because HTBW Core contains no code.** That is stated
plainly in the catalogue rather than softened. Where a standalone released product implements
something resembling a use case, it is recorded as **product evidence** and never as HTBW
implementation, consistent with **DL-19**.

**Three responsibilities named in the Episode 8 material do not exist, and the catalogue corrects
them rather than accommodating them.** There is no **Experience Delivery** responsibility — delivery is
Concierge's and a Delivery Surface is a platform concern. There is no **Communication or Messaging**
responsibility — [authority-order.md](authority-order.md) forbids it as a non-negotiable constraint.
There is no **Intelligence** responsibility — whether a reasoning provider may be consulted at all is
**OD-67**, and a provider's output never silently becomes a Fact. **A compelling story is not
authority to add a responsibility.**

**Ten candidate principles were tested and none was elevated.** Seven are already accepted in
substance, and elevating a restatement would create two authorities for one rule — the defect the
authority order exists to prevent. Three are recorded inside the catalogue as **Concierge guidance,
explicitly subordinate to canon**: *information may come from many places, judgment belongs at home*;
*connectivity does not relocate responsibility*; and *Concierge recognises when assistance becomes
useful*. The first two were deliberately **not** elevated because doing so would preempt **OD-07** and
**OD-67**, and the second rests on platform facts this repository has not verified. **DL-50**'s
*providers produce evidence, HTBW produces decisions* was deliberately **not generalised** beyond
voice for the same reason.

**One apparent gap was tested and found already answered, which is worth recording because it looked
like a decision.** Unprompted assistance — the shopping list becoming useful at the shop, the vehicle
recommendation the evening before a long day — appeared to need an owner for *who decides that an
opportunity exists*. [../models/communication.md](../models/communication.md) already states that
**any responsibility may originate a Communication**, so the originator is whichever responsibility
owns the underlying matter, and the residual question is only **who owns the association between a
person and an external list or calendar**, which is **OD-77**. **No new decision was justified.**

**The review's most useful output is a sequencing signal rather than a finding.** Twelve of the
twenty use cases are blocked, and the blockers concentrate almost entirely in five existing decisions
— **OD-06**, **OD-77**, **OD-43**, **OD-84**, and **OD-52**. **Deciding those five would unblock ten
of the twelve.**

**This note introduces no construct**, amends no accepted decision, and reopens none. The ledger
remains at eighty-four identifiers, ten closed, seventy-four open.

---

### Notes on the post-acceptance voice-evidence architecture harvest

**Recorded 2026-08-25, after DL-50 was accepted.** Twenty patterns raised during the voice-evidence
research were tested against the accepted architecture to determine whether any remained trapped
outside the architecture-of-record. **Fifteen were already incorporated, four were partial and are
already tracked, and one was missing.** **The harvest amends no accepted decision, reopens none, and
creates no document.**

**The one missing pattern is OD-84, and it is a defect rather than an absence.** **DL-38 F8** yields
`ambiguous` when the leading candidate fails the governed separation requirement, and `ambiguous`
means **one speaker whose identity could not be separated between candidates**. **Two people speaking
produces the same observable shape from the opposite cause** — several candidates scoring closely —
so uncertainty and plurality are **currently indistinguishable at the point where the distinction
matters most**, and an implementation reporting plurality as `ambiguous` would conform to the letter
of an accepted rule while asserting something false. **HTBW already represents plurality twice and in
neither place is it a speaker**: **DL-35** for an Unknown Actor Reference in a historical
reconstruction, and [../models/communication.md](../models/communication.md) for **audience
composition**, which **DL-34** states *identifies nobody* and *is never a second identity fusion*.
**Audience answers who could hear; this question asks who spoke**, and **DL-34** itself keeps the six
roles distinct. The urgency is concrete rather than theoretical: **speech-region segmentation is the
mechanism that would surface a second speaker, and it is scheduled to ship into a model that has
nowhere to put the finding**.

**Two proposals were tested against the repository and deliberately answered no.** A separate
`voice-evidence-provider-contract.md` is **not** created, because
[../contracts/README.md](../contracts/README.md) defines a contract as *the explicit boundary of a
responsibility*, describing *obligations between responsibilities, not transport, schema, or platform
mechanics* — and **a provider is a component, not a responsibility**, so such a file would be a
category error and would fragment the boundary that
[../contracts/identity-contract.md](../contracts/identity-contract.md) already carries. A **provider
plug-in or registry framework** is likewise **not** created: **DL-41** already enumerates *a provider*
among its dependency classes, and building a registration framework would be a **new HTBW capability**
requiring the **DL-30** ordered burden to be discharged first, which nothing in the research
discharges.

**Four partial patterns were found, and none of them justified a new decision.** Channel-diversity
gallery strategy is **OD-83**, already open. **Provider optional-feature discovery** and
**provider-substitution migration** are **contract work**, folded into Phase 1 rather than raised as
questions — the first because Patterns 5, 6, and 8 are optional capabilities a provider may or may not
offer, and the second because section 16's model-upgrade rule already answers the substitution case
once it is stated as applying to a change of provider and not only of model. **Microphone governance**
is **already sufficient for the active path** — Room participation under **DL-11**, per-source consent
under **DL-32**, and purpose authority under **DL-36** together answer whether a microphone may
contribute evidence to a resident-initiated interaction — and is **insufficient only for the passive
path**, which is a North Star with microphone-governance policy already named among its prerequisites.
**A prerequisite that is already recorded is not a gap.**

**Two apparent gaps were tested and found to be settled positions rather than omissions.** **Enrollment
quality scoring** is deliberately not canonical: the enrollment-sufficiency note below already refuses
*no canonical threshold, sample count, duration, margin, or quality score*, and quality is expressed as
**gates**, not as a published score. **Audio-quality scoring** is likewise already held: **DL-38 F3**
names **observation quality** as a qualification stage that may only lower or hold, and
[../models/person-and-identity.md](../models/person-and-identity.md) already lists *quality summary*
among the safe metadata Identity may emit. Neither needed anything added.

**Conversation-active remains where DL-50 put it, and that placement is itself the finding.** The
distinction between **conversation active** and **conversation content** exists **only in the accepted
ADR** and appears in no canonical model. **That is correct and must not be repaired**: writing it into
[../models/truth.md](../models/truth.md) would grant canonical standing to a capability that is
explicitly a **North Star with no implementation authorised**, which is the failure mode the North Star
classification exists to prevent. The prohibitions that protect it — no transcript requirement, no
semantic requirement, no ambient recording, no conversation storage — are already carried by **DL-42**,
**DL-46**, and [../architecture/privacy.md](../architecture/privacy.md) independently of the ADR.

**No contradiction was found**, no responsibility boundary was moved, and the provider boundary remains
extensible: a future encoder, an alternate provider, an experimental provider, or a future
Wyoming-compatible provider is adopted under **DL-41** as a declared dependency and under **DL-50** as
a candidate-reporting provider, **without redesigning Identity**.

**This note introduces no construct.** It creates **no responsibility**, **no record class**, **no
artifact class**, **no retention rule**, **no threshold**, and **no confidence representation**. It
**amends no accepted decision** and **reopens none**. The ledger moves to eighty-four identifiers, ten
closed, seventy-four open.

---

### Notes on the custody and obligation-lifecycle decision

**Recorded 2026-08-20. DL-48 and DL-49 were accepted, and OD-75 is closed by them. Formal acceptance
review completed the same day with a result of PASS, and issue #105 is closed as the completed
governance record for OD-75.**

**The acceptance review confirmed the accepted outcomes rather than restating them**, and the ones it
named are held in canon: obligation condition and lifecycle are orthogonal; **`met` means satisfied to
date, not completed**; a Care Evidence Record provides governed closure by observation, attestation,
performance, or waiver; a **Custody Period** is Stewardship-owned and carries the lifecycle `opened`,
`updated`, `closed`, `corrected`, `adversely_resolved`; custody is separate from ownership,
caretaking, declared location, observed location, significance, and risk; a lost or stolen period ends
`adversely_resolved` with the **last known custodian preserved**; and recovery opens a **new** period
rather than rewriting the adverse one. The review also confirmed what was **not** done: no Asset
Intelligence schema was adopted, no ownership moved into Continuity or Concierge, **OD-77 was neither
expanded nor silently resolved**, no current physical location is inferred from custody, and **no
issue was closed solely because documentation changed**.

**Implementation remains separate** and is gated by the applicable persistence, retention,
preservation, relationship, document, and Home Assistant First decisions. **Issue #155 remains open**
as the Asset Intelligence legacy capability harvest register.

**The household outcome this had to serve**: preserve a complete, explainable custody chain for a
significant asset; know who is accountable and where it is expected to be; protect return commitments;
preserve condition and contractual evidence; and support insurance, provenance, conservation, and
eventual retirement — **without confusing custody with ownership, caretaking, declared location,
current location, risk, or environmental truth**.

**Three household requirements were challenged and corrected rather than adopted:**

| Proposed | Verdict | Accepted form |
|---|---|---|
| Custody states *Owned On Site*, *On Loan Out*, *In Transit*, *In Storage*, *Lost*, *Stolen* | **Rejected as a fixed enumeration** | **HTBW adopts no fixed custody-status enumeration as canonical**, though a Custody Period does carry a governed lifecycle. *In transit* and *in storage* are Custody Periods whose custodian is the carrier or storage provider; *owned on site* is **not a custody statement at all** and requires a Truth Location Fact or a declared `located-in`; *overdue*, *lost*, and *stolen* are not custody states |
| A *Counterparty* object | **Rejected** | The custodian designation is a **governed reference to an existing Foundation object, or free text preserved verbatim** with the actor who recorded it. No new object was demonstrated as necessary |
| A *custodian* Foundation relationship type | **Rejected** | `owner-of` and `caretaker-of` are **durable**; custody is **episodic**. Episodic accountability belongs on a time-bounded record. **OD-77 was neither expanded nor resolved** |

**One tension required care rather than a ruling either way.** The household requires that an open loan
stay open until Check-In is explicitly recorded, while the accepted rule is that *Stewardship observes
closure from Truth, not from having asked for something*. Both are honoured because they concern
different subjects: **Truth can establish where something is; it cannot establish that an
accountability period has been accounted for.** Physical return is therefore **evidence toward
closure**, and the Check-In is a **Care Evidence Record** of kind `attested`. **This is not a ticked
projection** — it is a household attestation of a real-world event, carrying the return date, the
condition, and its evidence.

**The custody findings decided the obligation half.** Asset Intelligence had independently built a
plain custody **state** alongside a loan **lifecycle** — which is alternative **(C)**, already working
in a neighbouring domain. Its `expected_return_date` versus `actual_return_date` pair is **completion
evidence by construction**, which is alternative **(D)**. **DL-48 therefore accepts (C) as the shape,
(B) as the mechanism, and (D) as what closes — and rejects (A)**, because putting *deferred* and
*closed* into the condition set is the precise category error this decision was raised on.

**Four boundaries were deliberately preserved:**

- **Continuity owns none of this.** Custody, care history, environmental history, insurance
  responsibility, and asset provenance are **not Continuity's** merely because they persist. Use Case 1
  of [../scenarios/stewardship-use-cases.md](../scenarios/stewardship-use-cases.md) records
  *Continuity interaction — None*, and it stands.
- **Concierge owns no obligation and no reminder policy.** Stewardship originates the Communication;
  Operational Trust governs entitlement, interruption, and audience; Concierge decides whether, when,
  and how. **Reminder lead time and cadence are household policy, not canonical constants.**
- **No dashboard colour became a Fact.** *Blue* and *purple* for within-period and beyond-expected-return
  are presentation candidates over an obligation condition state, and the projection surface remains
  **OD-23**.
- **No second risk authority was created.** When an asset is off site and household environmental
  evidence is unavailable, **Truth publishes no Fact it cannot support** and the dependent evaluation is
  **unavailable and says so** (**DL-41**) — never green, never red. Significance persists, custody
  persists, the return obligation persists, and the environmental conclusion does not.

**Corrections recorded at formal acceptance review, 2026-08-20.** The accepted direction was not
reopened; four statements were imprecise and are corrected here and in the canonical documents.

| Imprecise as first written | Corrected |
|---|---|
| *"The home knows the sculpture is at the DMA."* | **A custody record never establishes current physical location.** The architecture-faithful sentence is *"the custody record says the sculpture is in the museum's custody."* Current physical location requires a **Truth** Location Fact |
| *"Owned on site is the absence of an open Custody Period plus an `owner-of` relationship."* | **Withdrawn.** The absence of an open Custody Period means only that **no non-default custodian is currently recorded**. On-site status requires a Truth Location Fact or Foundation's declared `located-in`, and is **never inferred from ownership** |
| *"There is no custody state machine."* | **Imprecise.** A Custody Period **does** have a governed lifecycle — `opened`, `updated`, `closed`, `corrected`, `adversely_resolved`. What HTBW declines to adopt is the **legacy fixed custody-status enumeration** as canonical |
| *`met` used without definition* | **`met` means satisfied to date, not completed.** This is the meaning the model already carried — implicit in the filter, tuning, and preservation obligations — and it is now stated. **No new condition value was introduced**, and `met` is never asserted from absence |

**One field was decomposed** without creating an object: *insurance responsibility* is genuinely
several things — the **insurer** and **insured party**, which live on the policy artifact; the party
**responsible for maintaining coverage** and the party **accountable for a claim**, which are
period-scoped and live on the Custody Period; and the **governing agreement**, which is an Asset
document referenced without copying. Ownership and custody remain independent of all of them.

**No Asset Intelligence schema was adopted.** No object model, storage schema, event schema, state
enumeration, or field name was copied, and the legacy snapshot-comparison pattern is explicitly
excluded: **custody and obligation changes are semantic Change Records written at the moment of
change** (**DL-26**).

**These decisions preempt nothing else.** They decide no significance representation (**OD-21**), no
escalation ladder (**OD-22**), no obligation projection surface (**OD-23**), no acknowledgement
semantics (**OD-45**), no interruption risk classes (**OD-51**), no retry policy (**OD-54**), no
audience specification (**OD-52**), no delegated care authority (**OD-76**), no person-to-resource
association (**OD-77**), and no governed-record persistence shape (**OD-01**).

---

### Notes on the Episode 4 and Episode 5 narrative-validation clarifications

**Recorded 2026-08-17. No decision was created, closed, reopened, or amended by this work.**

Narrative development of **Season 1 Episode 4 (Identity)** and **Season 1 Episode 5 (Operational
Trust)** surfaced eleven points at which accepted architecture was **correct but under-stated** — true
by implication from **DL-32**, **DL-33**, **DL-34**, **DL-36**, **DL-37**, **DL-38**, **DL-39**,
**P15**, **P16**, **P26**, and **P32**, yet not written plainly enough to be implementable or
teachable. They were memorialized as **clarifications inside the existing Identity, Operational
Trust, privacy, and explainability documents**, not as ledger entries.

| Clarification | Already implied by | Where memorialized |
|---|---|---|
| Identity establishes confidence; Operational Trust evaluates **sufficiency for a specific request**, never generalized trustworthiness | **DL-36** | Operational Trust model and contract |
| Operational Trust **applies** household values; it does not **author** them | **DL-36**, **P26** | Operational Trust model and contract |
| **Participation is optional and requires consent**; voice identity evidence is available only for a consenting, enrolled participant | **DL-38** eligibility gate; privacy consent requirements | Identity model and contract, Operational Trust model and contract, privacy |
| **Consent → Available Evidence → Identity → Operational Trust** | **DL-32**, **DL-38** | Identity model and contract, Operational Trust model and contract, privacy |
| **Audience awareness is a first-class input**; identity confidence may be unchanged while the outcome varies | **DL-34**, **P32** | Operational Trust model and contract |
| **Disclosure is separate from knowledge** — *can the home know?* versus *should the home share?* | **DL-34**, **P32** | Operational Trust model and contract, privacy |
| Operational Trust **prefers explicit metadata and classifications** over content interpretation or sensitivity inference | **DL-34** (a reasoning provider is never the sensitivity classifier), **P15**, **P16** | Operational Trust model and contract, explainability |
| **Confidence requirements are configured per capability**; there is no universal threshold | **DL-36**, **DL-39**, **OD-51** | Operational Trust model and contract |
| **"Not now" is a valid outcome** — Allow, Require Confirmation, Defer, Redirect, Abstain, Deny | Existing authority and disclosure outcomes; **P16**, **DL-15** | Operational Trust model and contract |
| Operational Trust evaluates **eight inputs** before producing an outcome | Distributed across the above | Operational Trust model and contract |
| **Unknown is a valid identity outcome**; the home must not be more confident than the evidence supports | **DL-33**, **DL-38** rules **F1–F8** | Identity model and contract |

**Three boundaries were deliberately preserved rather than adjusted:**

- **The six outcome shapes are a household-facing reading, not a new enumeration.** The authoritative
  authority outcomes remain `permitted`, `prohibited`, `permitted_with_confirmation`,
  `permitted_with_escalation`, and `undecidable`; the disclosure outcomes remain as accepted under
  **DL-34**. **Operational Trust owns the constraint — *not at this moment*, *not on this surface* —
  and Concierge owns the expression of it.** *Defer* and *Redirect* remain Concierge outcomes and were
  **not** relocated.
- **No native privacy-marking capability is claimed.** The preference for explicit classification is
  stated at the architectural level; **which native fields carry such a marking remains subject to the
  ordered burden of proof in DL-30**, and no such field is asserted anywhere in this repository.
- **No new responsibility, model, threshold, or store was created**, and no ownership moved. Identity
  still fuses; Truth still owns Facts; Operational Trust still owns every threshold; Concierge still
  owns decisions and the Decision Trace; the household still owns its values.

**These clarifications preempt nothing.** They decide no risk-class enumeration (**OD-51**), no
assertion validity window (**OD-15**), no consent user experience (**OD-06**), no audience-uncertainty
policy (**OD-71**), no reasoning-provider strategy (**OD-67**), and no learning eligibility
(**OD-65**).

### Notes on the Episode 6 narrative-validation clarifications

**Recorded 2026-08-18. No decision was created, closed, reopened, or amended by this work, other than
the opening of OD-75 and OD-76 above.**

Narrative development of **Season 1 Episode 6 (Stewardship — *How Does a Home Know What Matters?*)**
was used as an **architecture stress test**, in the same manner as Episodes 4 and 5. The narrative is
**not** authoritative architecture and was not incorporated as such. It was used to find questions the
accepted architecture must answer.

**The proposed episode doctrine was validated and accepted as a human-facing summary**, with the
precise architectural wording recorded behind it:

| Proposed narrative statement | Verdict | Precise architectural wording |
|---|---|---|
| *The household determines what matters* | **Accepted** | The household **declares** what matters and defines the relevant care expectations, through registration, configuration, caretaker assignment, consent, policy, relationship records, care profiles, schedules, declared environmental requirements, or a default it **explicitly chose** |
| *Stewardship helps care for it* | **Accepted as the human-facing summary** | Stewardship **represents those care expectations, evaluates authoritative observations against them, and creates governed care obligations when attention is required** |
| *Stewardship often appears as automation* | **Accepted, with a boundary** | The **automation is the executor**. Stewardship states that an obligation is unmet; Operational Trust governs; Concierge decides; an executor acts |
| *Stewardship exists to support care* | **Accepted** | Consistent with **DL-07** |
| *Sometimes automation is used to take corrective action before anyone needs to be notified* | **Contradicted as written** | The corrective action is real and permitted; **attributing it to Stewardship is not**. Remediated narration is recorded below |
| *Operational Trust enforces what is appropriate* | **Rejected** | **Enforcement is execution.** The canonical wording is *Operational Trust determines what is appropriate for this request, in this context*, and it appears in this repository nowhere else |
| *Care results in action when attention is required* | **Superseded** | **Care creates an obligation when attention is required.** Whether an action follows is Operational Trust's, Concierge's, and the executor's |

**Seven points were found where accepted architecture was correct but under-stated** — true by
implication from **DL-07**, **DL-08**, **DL-19**, **DL-21**, **DL-25**, **DL-26**, **DL-31**,
**DL-36**, **DL-41**, **DL-42**, **DL-46**, **DL-47**, **P21**, **P26**, **P28**, and **P32**, yet not
written plainly enough to be implementable or teachable. They were memorialized as **clarifications
inside existing documents**, not as ledger entries.

| Clarification | Already implied by | Where memorialized |
|---|---|---|
| **The household declares what matters; Stewardship represents that declaration.** Stewardship never decides on the household's behalf that something matters | **DL-07**, **DL-21**, **P26**; the provenance requirement on significance; the Operational Trust *applies, does not author* rule | Stewardship model and contract, framework |
| **There is no universal HTBW hierarchy of importance.** Price, appraisal, sensor count, Identity participation, residency, and registration confer no significance | **DL-21**, **P26**; the absence of any ranking construct anywhere in the repository | Stewardship model and contract, glossary |
| **People are not Assets. Pets are not Assets.** Both may carry care obligations without being modelled as property | The asset model's object-distinction table; the glossary Person and Pet entries; *the Pet is not a Person* in the obligations scenario | Asset model, glossary, Stewardship model and contract |
| **Stewardship does not begin with an alert.** It begins with a declaration and a care definition; a reminder, advisory, corrective action, or escalation is a later consequence | The obligation structure, which requires a subject, statement, significance, schedule or condition, and provenance **before** any state can be evaluated | Stewardship model and contract, use-case document |
| **Stewardship never calls a Home Assistant service**, and an automation resolving a condition quietly is the **executor** acting, not Stewardship | *Stewardship never closes the door*; dependency-view rule 4 *Stewardship does not act*; **P32** *acting is not announcing* | Stewardship model and contract, framework, use-case document |
| **The canonical Operational Trust verb is *determines … for this request, in this context*.** *Enforces* is rejected; the unqualified *determines* is rejected | **DL-36**; *Operational Trust applies household values; it does not author them* | Operational Trust model and contract |
| **Continuity is not a child of Stewardship.** Stewardship history is Stewardship's; general preferences, Follow-Me, resume, transfer, and experience restoration never move into Stewardship | *Each responsibility owns the history of its own records*; the Continuity ownership list | Continuity model and contract |

**Four boundaries were deliberately preserved rather than adjusted:**

- **The obligation boundary is authoritative and was not relaxed.** *Stewardship owns the obligation;
  Stewardship does not own the resulting Communication or physical action* stands unchanged. The
  Episode 6 corrective-action narration is remediated **toward** the architecture, not the reverse.
- **The Asset Intelligence consolidation was already accepted and was not re-decided.** **DL-07**
  removed *what matters* from Asset Intelligence; **DL-08** placed the descriptive asset record with
  Foundation and kept the standalone product separate; **DL-19** removed every compatibility
  requirement; `asset-intelligence-contract.md` is Historical and superseded. **No implementation
  artifact, integration, namespace, storage schema, event name, or user interface was renamed or
  removed to make words match**, and none may be. Whether HTBW Core consumes the product as an
  optional evidence source remains **OD-20**.
- **No new responsibility, model, threshold, store, or history owner was created**, and no ownership
  moved. Truth still owns current and historical Facts; Foundation still owns the descriptive asset
  record and the relationship types; Operational Trust still owns every threshold and all disclosure;
  Concierge still owns decisions, delivery, and the Decision Trace; Continuity still owns preferences
  and sessions; the household still owns its values.
- **"Room health" and "asset health" remain undefined, deliberately.** HTBW defines no such state
  model and none may be invented (**OD-69**). A household-facing room summary is a **projection** over
  Truth Facts and Stewardship obligation states with the fields kept separate and separately
  explainable.

**Two genuine defects were found and are now open decisions**, rather than being closed by invention:

- **OD-75** — the obligation state set does not contain the *deferred* and *closed* outcomes the same
  document's history description names, and *what counts as evidence that care occurred* is asked and
  unanswered.
- **OD-76** — no caregiver relationship or delegated care authority exists, so a care obligation
  declared for one Person by another is **unsupported**. The aging-parent use case is documented with
  that gap stated plainly rather than papered over.

**These clarifications preempt nothing.** They decide no significance representation (**OD-21**), no
escalation ladder (**OD-22**), no obligation projection surface (**OD-23**), no Asset-derived Entity
vocabulary (**OD-69**), no consent user experience (**OD-06**), no safety-category scope (**OD-56**),
no urgency entitlement model (**OD-46**), no audience specification (**OD-52**), no executor-evidence
model (**OD-63**, **OD-64**), and no optional Asset Intelligence integration (**OD-20**).

**The eight validated use cases were added to
[../scenarios/stewardship-use-cases.md](../scenarios/stewardship-use-cases.md)** as canonical
Stewardship use cases and future acceptance scenarios: Artwork Preservation, Pet Stewardship,
Aging-Parent Support, Washing-Machine Leak Protection, Window-Shade Battery Maintenance, HVAC Filter
Maintenance, Irrigation Stewardship, and Antique Piano Stewardship. **No production capability is
asserted by that document**; HTBW Core remains greenfield under **DL-19**.

---

### Notes on the Episode 7 narrative-validation clarifications

**Recorded 2026-08-20. No decision was created, closed, reopened, or amended by this work, other than
the opening of OD-77 and OD-78 above.**

Narrative development of **Season 1 Episode 7 (Continuity — *How Does a Home Remember What
Matters?*)** was used as an **architecture stress test**, in the same manner as Episodes 4, 5, and 6.
The narrative is **not** authoritative architecture and was not incorporated as such. It was used to
find questions the accepted architecture must answer.

**The proposed episode doctrine was validated**, with the precise architectural wording recorded
behind it:

| Proposed narrative statement | Verdict | Precise architectural wording |
|---|---|---|
| *What Should Be Remembered?* as the internal framework question | **Accepted** | It is the abbreviated form already used in the [../architecture/north-star.md](../architecture/north-star.md) framework diagram. The full canonical question is *what should be remembered, restored, resumed, or transferred?* and the episode must not narrow Continuity to memory alone |
| *A Home That Behaves Well remembers what matters so comfort, experiences, relationships, commitments, and care can continue* | **Accepted as the human-facing summary** | Continuity holds **preferences, sessions, resume and transfer state, and experience history**. Relationships, commitments, and care are held by **Foundation**, the **source system**, and **Stewardship** respectively; Continuity holds how the household wants them delivered |
| *Continuity is not unlimited memory or a generic data store* | **Accepted** | The constraint is already binding through **DL-46** (no second copy), **DL-47** (every record class declares its retention), and **P22** (no shadow system of record) |
| *Continuity preserves governed observations and patterns* | **Contradicted as written** | An **observation is a Domain Event owned by the responsibility that observed it**, and an unaccepted pattern is **nothing behavioural**. Continuity holds the **approved preference** — never the observation that produced it |
| *Continuity preserves watering history, moisture history, rainfall, and prior outcomes* | **Contradicted** | [../scenarios/stewardship-use-cases.md](../scenarios/stewardship-use-cases.md) Use Case 7 records **Continuity interaction — None**. Weather Facts are **Truth's Historical Facts**; watering obligations and outcomes are **Stewardship's** |
| *Continuity preserves relevant history, associations, and commitments for care* | **Contradicted** | **Stewardship history is Stewardship's.** Continuity's contribution to a care Communication is the **preferred delivery, preferred presentation, and re-presentation preference**, and nothing else |
| *Stewardship marked the commitment as requiring care* (dental appointment) | **Contradicted** | **A calendar appointment is not a care obligation.** Stewardship represents a care expectation **the household declared**; it never decides on the household's behalf that something matters |
| *"I need to make dinner"* authorising a room-to-room media transfer | **Not yet governed** | The canonical trigger is an **explicit instruction** or an **already-enabled Follow-Me preference**. No accepted document maps an indirect utterance to a media transfer, and **DL-30** is not discharged by assertion |
| *The home learned the routine* | **Accepted only with qualification** | *The home noticed the pattern, asked whether you wanted it, and does it because you said yes.* Silent promotion is prohibited (**P26**, **DL-21**) |
| *Continuity reconnects the person to the governed personal context* | **Not yet governed** | The Person-to-external-resource association has **no named owner** — **OD-77** |

**Seven points were found where accepted architecture was correct but under-stated** — true by
implication from **DL-21**, **DL-26**, **DL-27**, **DL-30**, **DL-33**, **DL-41**, **DL-46**,
**DL-47**, **P21**, **P22**, **P26**, **P28**, **P30**, and **P32**, yet not written plainly enough to
be implementable or teachable. They were memorialized as **clarifications inside existing documents**,
not as ledger entries.

| Clarification | Already implied by | Where memorialized |
|---|---|---|
| **Continuity holds preferred delivery and preferred presentation**, and the preference *dimensions* are enumerated only in Historical documents that are not authority | The Stewardship use-case ownership map; the Communication model's Continuity row; *preferred interaction patterns* in the Continuity model | Continuity model and contract, use-case document |
| **Continuity holds the approved preference, never the observation.** An observation is a Domain Event owned by its observer | **P26**; the Continuity model's own learning paragraph | Continuity model and contract, use-case document |
| **Continuity holds no external-service reference.** Calendar, mailbox, account, and media-profile associations are not in its ownership list | The Continuity ownership list; the Person-extension table's unassigned row | Continuity model and contract, use-case document, **OD-77** |
| **A record does not become Continuity's because it is personal.** Care history is Stewardship's; environmental history is Truth's; source content is the provider's | *Each responsibility owns the history of its own records*; **DL-46** | Continuity model and contract, use-case document |
| **A remembered value is not a Fact**, and current Truth, Room mode, Identity, Operational Trust, audience, and safety are preconditions to applying one, never overridden by it | The Continuity blocking-state model; dependency-view rule 5 | Continuity model and contract, use-case document, **OD-78** |
| **There is no Journey, checkpoint, or progress-marker object.** Provider-owned playback position stays with the provider; Continuity holds resume eligibility and a Governed Reference | The glossary's Experience and Session entries; **DL-46**; **P30** | Continuity model and contract, use-case document |
| **Continuity neither formulates nor presents a recommendation** | Dependency-view rule 5; the Reasoning Provider glossary entry | Continuity model and contract, use-case document |

**Five boundaries were deliberately preserved rather than adjusted:**

- **The person-scoped versus room-scoped split is authoritative and was not extended.** Preferred
  artist, genre, album, and playlist are person-scoped; last song, last genre, music volume, duck
  volume, and TTS volume are room-scoped. **The proposed household-, asset-, experience-, journey-,
  capability-, and relationship-scoped memory list was not adopted**, because those are the scopes of
  *other responsibilities' records*, not of Continuity preferences.
- **The superseded memory documents were not revived.** `household-memory-model.md`,
  `household-memory-contract.md`, `person-continuity-model.md`,
  `person-continuity-affinity-contract.md`, `person-room-affinity-model.md`,
  `experience-restoration-context-model.md`, `experience-restoration-contract.md`,
  `adr-household-memory-governance.md`, and `adr-personalization-governance.md` are all **Historical
  and superseded**, their canonical replacement is the Continuity model and contract, and
  [../architecture/adr-historical-explainability-and-historical-truth.md](../architecture/adr-historical-explainability-and-historical-truth.md)
  states that their **former ownership boundaries are not reactivated**. **There is no Household
  Memory responsibility, no Historical Intelligence responsibility, and no Affinity responsibility**,
  and none may be created to carry Episode 7 material.
- **No new responsibility, model, object, store, threshold, or history owner was created**, and no
  ownership moved. Truth still owns Facts and Fact history; Foundation still owns object definitions
  and relationship types; Stewardship still owns obligations and care history; Operational Trust still
  owns every threshold, all disclosure, and all retention policy; Concierge still owns decisions,
  delivery, and the Decision Trace; Continuity still owns preferences, sessions, and experience
  history; the household still owns its values.
- **Household traditions, plant-care knowledge, and travel-time computation remain undefined,
  deliberately.** A repository-wide search returns no canonical match for *tradition*, *ritual*, or
  *travel time*, and **none was invented here**. A recurring household moment is an **Experience** or
  a household-authored Home Assistant automation; deciding that a recurrence *matters* is a
  **household declaration**.
- **A recommendation is not an authorisation, and a reasoning provider is not an authority.** *A
  reasoning provider owns nothing… its output never silently becomes a Fact, and its recommendation
  never silently becomes an authorised action.* Provider strategy remains **OD-67**, and **DL-41**
  makes a provider a declared capability dependency for which **no local approximation stands in**.

**Two genuine defects were found and are now open decisions**, rather than being closed by invention:

- **OD-77** — the Person-to-external-resource association is named in the Person-extension table with
  **no owning responsibility**, and no accepted relationship type expresses it. Every personal-resource
  outcome in Episode 7 depends on it.
- **OD-78** — the remembered-value classes are nowhere enumerated, restoration mechanics exist only in
  a subordinate patterns document, and a Continuity-held *last lamp level* sits in unresolved tension
  with **DL-46**.

**A third defect was found while reviewing the retiring Concierge configuration surfaces**, and is
recorded as **OD-79**: **presentation preference scope and precedence**. Person scope is settled as
Continuity's, room scope has **no owner**, the Continuity scope tables contain **neither**, and no rule
states what happens when a Room persona and a person's interaction preference disagree. The dimension
enumeration gap noted in the clarification table above is part of the same decision.

**One documentation-governance defect was found that is not an open decision.**
[../architecture/north-star.md](../architecture/north-star.md) declares itself *subordinate only to
the North-Star framework as represented in the HTBW video-series artifacts*, **yet no video-series
visual artifact exists in this repository**, and a repository-wide search for `CORE-08` and for any
visual register returns nothing. The highest-ranked authority in the governance chain is therefore
**unversioned, unregistered, and unreviewable**. It is tracked as documentation remediation alongside
**#145**, and **no visual asset was created, altered, or asserted by this review**. The review
validated the repository's canonical equivalent instead — the framework diagram node in
[../architecture/north-star.md](../architecture/north-star.md), and
[../architecture/framework.md](../architecture/framework.md) section 5.

**These clarifications preempt nothing.** They decide no learned-policy lifecycle (**OD-28**), no
learning evidence eligibility (**OD-65**), no behaviour attribution (**OD-63**), no native behaviour
observation (**OD-64**), no session merge (**OD-24**), no resume window (**OD-25**), no experience
history retention (**OD-26**), no session concurrency (**OD-27**), no re-presentation preference
(**OD-48**), no reasoning-provider strategy (**OD-67**), no delegation boundary (**OD-66**), no
audience specification (**OD-52**), no interruption risk classes (**OD-51**), no erasure mechanics
(**OD-09**), and no deletion-versus-preservation reconciliation (**OD-36**).

**The fifteen validated use cases were added to
[../scenarios/continuity-use-cases.md](../scenarios/continuity-use-cases.md)** as canonical Continuity
use cases and future acceptance scenarios: Comfort Restoration, the Dental Appointment Reminder,
Follow-Me Music, Audiobook Resume, Interaction Styles, Person-to-Calendar and Person-to-Mailbox
Associations, the Morning Calendar Rhythm, Maisey's Care Continuity, Artwork Caretaker Notification,
Irrigation and Weather, Content Recommendation Candidates, Household Traditions, Correction and
Deletion, Guests and Multi-Person Conflict, and Explaining What Was Remembered. **No production
capability is asserted by that document**; HTBW Core remains greenfield under **DL-19**.

---

### Notes on the Asset Intelligence legacy capability harvest

**Recorded 2026-08-20. No decision was created, closed, reopened, or amended by this work.**

The released **Asset Intelligence** HACS product was reviewed end to end — services, coordinator,
evaluation, storage, config and options flows, diagnostics, entities, events, frontend surfaces,
tests, and its own open issues — to harvest household outcomes and operational lessons **before** the
product is retired into HTBW. The register is **#155**.

**Asset Intelligence implementation is rank-four evidence** under
[authority-order.md](authority-order.md). It demonstrated outcomes, revealed refinements, exposed
gaps, and supplied reference patterns. **It created no architecture authority and resolved no open
decision.**

**No new open decision was required.** Every gap found is owned by an existing accepted decision or an
already-open one. The harvest tested roughly twenty-four services, twenty domain event types, twelve
accumulating record classes, nine environment signal categories, and five interaction surfaces against
the canon, and the canon already answered the ownership questions.

**Two findings are contradictions with accepted architecture rather than gaps**, and in both cases the
governing sentence was already written:

- **Shipped care defaults are applied as though declared.** The product ships a `baseline_adult`
  human-comfort profile and per-asset-type debounce profiles, and evaluates against them whether or
  not the household ever saw them. [../models/stewardship.md](../models/stewardship.md) already
  states that a default must be one the household **explicitly chose**, and that **a default the
  household never saw is not a declaration**. The household outcome — low-friction setup — is worth
  preserving; the mechanism is not. A default is a **proposal** until accepted. The residual question,
  what provenance an accepted default carries, is recorded on **OD-21**.
- **Home Assistant labels are read back as behavioural authority.** A `label_profiles` map keyed
  `asset_type:painting` and `sensitivity:high` selects the debounce policy that decides how long a
  risk condition must persist before a household is told. **OD-68** preserves the opposite direction —
  *Asset Type stays authoritative in HTBW, labels stay derived* — and labels are recorded in
  [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md) as **flat,
  global, and ungoverned**. A projection is not an input. Recorded on **OD-68**, with the
  significance-shaped key routed to **OD-21**.

**One negative result is worth recording.** The most mature implementation in the portfolio reached
release without any **significance** field at all, expressing what matters implicitly through
registration and declared limits — and, where it needed a significance-shaped concept, inventing it as
an ungoverned label. It also holds purchase price and estimated value and **uses neither in any
evaluation**, independently honouring the accepted rule that **price confers no significance**.

**Fifteen reference patterns were identified for preservation**, recorded in full on **#155**. The
most architecturally significant are: the **Change Record shape** — changed-field list, explicit
before and after, and actor — which satisfies **DL-26** as written; **bounded audit payload
constants**, a refinement this repository names nowhere; **domain events published on the native Home
Assistant event bus**, which is **DL-46** done correctly and which exists in the same codebase as the
pattern that violates it; **reason strings that carry the observation, the threshold, and the
mechanism**; and **honest unknowns**, where missing data produces a stated warning and never a
violation.

**Refinements with no canonical home** were recorded against the decisions that own them rather than
being adopted: temporal **debounce** and value **hysteresis** as stability-before-commitment rules
(**OD-18**) — independently invented by two separate products, which is the strongest argument that
the architecture should name the primitive; **per-signal aggregation across multiple contributors**
(**OD-17**); a four-value confidence enumeration in which **staleness competes with coverage for a
single field** (**OD-18**, **OD-74**); **soft and hard threshold pairs** (**OD-21**); **loan terms**
including counterparty, expected return, and insurance responsibility (**OD-75**); and a **transient
export artifact** with an unconditional sixty-second lifetime (**OD-09**).

**Nothing was migrated, and no schema was adopted.** No object model, storage schema, event schema,
ring-buffer bound, `.storage` layout, media path, panel design, hardcoded category, audience class,
confidence percentage, or profile naming was copied into this repository, and none may be on the
strength of this review alone. **No implementation was modified in any repository**, no HTBW
governance was placed in the Asset Intelligence repository, and **no issue was closed**.

---

### Notes on the enrollment sufficiency and re-enrollment governance challenge

**A proposed open decision was raised, tested, and rejected. No identifier was issued, and the ledger
is unchanged at eighty identifiers.** The Concierge and Voice Identity legacy capability harvest
proposed a decision on *enrollment sufficiency and re-enrollment obligation*, on the grounds that two
implementations ship different enrollment constants and that one of them emits a re-enrollment
instruction with no governed owner. A narrow challenge established that **accepted architecture
already governs both questions**, and that issuing the decision would have **reopened resolved
work**. This note records the result so the question is not raised a third time.

**Enrollment sufficiency is four layers, not one, and each already has an owner.** *Enrollment-data
adequacy* — whether there is enough usable evidence to construct a derived profile — belongs to
**Identity**, which owns enrollment, revocation, and identity diagnostics, and whose enrollment
**state and quality** are already required to be **inspectable by the enrolled person** and
expressible as a **quality summary** under the safe-metadata rule. *Where that quality enters an
assertion* is settled by **DL-32**, which places reliability on the **Person-to-evidence-source
association** rather than on the evidence type, and by **DL-38 (F3)**, which already names
**configured association reliability** as a qualification stage that **may only lower or hold**. A
better-enrolled voice profile lawfully raises the ceiling that the voice family can reach for a
person, and a marginal one lawfully lowers it; **the slot exists and is occupied**. *Assertion
producibility* is **DL-38 (F1)** and **(F8)**, where `known` requires the purpose minimum **and** a
governed separation requirement and is otherwise `ambiguous`. *Capability sufficiency* is **DL-36**
and the **Required Identity Band**, owned by **Operational Trust**, where **sufficiency is never
universal**. **These four are never collapsed into one question, and the harvest's central error was
to collapse them.**

**The literal values were already settled as non-architecture, by a resolved decision.** **OD-16**
states that the remaining values are **implementation mapping, not architecture** — naming
**freshness durations**, the **separation margin**, **per-purpose minimums**, and **reason-code
strings** as **Fusion Policy configuration**, versioned and governed, and **none of them an
unresolved architectural question** — and **DL-38** adds that **no duration is prescribed**. Sample
counts, minimum durations, quality thresholds, prompt-category diversity, and capture-distance
diversity are of exactly that class. **Two implementations holding different constants is calibration
divergence, not an architecture gap**, and **making a shipped constant canonical would contradict
DL-36 and reopen OD-16**.

**Re-enrollment is a dependency outcome, and creates no obligation by default.** An incompatible,
superseded, or revoked derived profile is an **Identity lifecycle result**; **DL-43** already ties a
voiceprint's existence to the profile remaining enabled **and consent remaining valid**. The
household-facing consequence is **DL-41**, which already enumerates **configured but invalid** among
the distinguishable dependency states, requires that the capability be **unavailable**, that the
missing dependency be **named**, and that the household be told **in a sentence it can act on**,
forbids **emulating** the missing dependency, and insists that **capability unavailable is never a
trust failure, an identity failure, or a permission failure**. **Stewardship raises nothing**,
because the household **declares** what matters and **a default the household never saw is not a
declaration**; an implementation emitting a re-enrollment instruction is a **remediation hint**, not
a declaration. **DL-48 is referenced here as not applicable by default, not applied.** Where a
household does explicitly declare that maintaining voice recognition matters, the existing DL-48
machinery already carries it, and **no new construct is required for that path**. Telling the
household is ordinary **Communication**: any responsibility may originate one, and **Concierge**
decides and records delivery.

**The governed sequence is therefore already complete**: Identity reports that no compatible profile
is available; **DL-41** reports voice attribution unavailable and names the incompatible dependency;
**Operational Trust** evaluates whether another evidence path satisfies the Required Identity Band
for the request; **Concierge** offers re-enrollment as **optional corrective action**; **Stewardship
creates no obligation**.

**This note creates nothing.** It introduces **no Enrollment Sufficiency construct**, **no enrollment
quality model**, **no re-enrollment obligation class**, and **no canonical threshold, sample count,
duration, margin, or quality score**. It **amends no accepted decision**, **reopens none**, and
**preempts nothing** — **OD-15** still owns assertion lifetime, **OD-06** still owns the consent
experience including revocation and the currently absent authorisation to enrol another person,
**OD-07** still owns voice processing locality, and the execution host — without which none of these
values can be validated at all — was **OD-80**, since **accepted as DL-50**.

**A separate finding is recorded rather than resolved.** Real-time voice comparison is **not a
validated capability**. Its plumbing is live-proven — evidence production executes on a real host and
correctly returns a no-match outcome — but **no `known` attribution has ever been produced from a
live utterance**, because at the time of this note the encoder had no accepted execution host. **That
blocker is removed by DL-50, and the finding is not thereby discharged**: an accepted host is a
precondition for validation, never a substitute for it. **No calibration value in
either implementation has been validated**, and none may be described as calibrated, canonical, or
household-ready on the strength of this review.

---

### Notes on the legacy documentation knowledge harvest

**This harvest produced no decision, and the ledger is unchanged.** A documentation-only review of
the Concierge, Voice Identity, and Asset Intelligence repositories was completed after their code
harvests, covering two hundred and thirty documents in one repository, seventy in another, and nine
in the third. **Three legacy-product reviews have now produced zero new open decisions.** That is the
third consecutive confirmation that the accepted architecture is materially complete, and it is
recorded here so the pattern is not mistaken for insufficient scrutiny.

**A legacy filename is not an authority claim.** The legacy sets contain documents named as ADRs,
contracts, and architecture that were authored against the pre-refoundation architecture, and others
that remain marked *proposed* while dependent documents treat them as settled. **Every legacy
document is rank-four historical evidence**, and none acquires standing from its filename, its
heading, or the confidence of its wording.

**Four accepted decisions were independently rediscovered by products that did not share them.**
Dependency naming distinct from permission failure (**DL-41**) appears in one product as a refusal
category set and in another as a per-reason retry vocabulary; a recommendation is never a decision
(**DL-21**) appears as an advisory boundary, a repairs boundary, and a consumption boundary in three
separate codebases; reference rather than copy with an exact version (**DL-27**) appears as a
contract-version rule that forces migration and forbids silent fallback; and **DL-33**'s requirement
that `unknown` remain expressible appears as a five-state fail-closed matrix. **Independent
rediscovery is the strongest available evidence that a decision describes something real**, and these
four are accordingly recorded as candidates for formal acceptance review rather than as new work.

**Stability before commitment has now been invented four times.** Two products and one household
automation pattern each arrived at a dwell, debounce, or hysteresis rule without shared design, and
the third product added a deliberate severity exemption so that critical signals escalate
immediately. **OD-18** owns the primitive; the intervals do not belong to this ledger.

**The largest finding is not architectural.** The legacy documentation sets hold a substantial body
of **operational refinement** — precedence ladders, fallback ladders, dwell intervals, cleanup
taxonomies, outcome classifications, and household-facing wording — which is not architecture, has
almost no canonical home, and would be lost when those repositories go quiet. Two extensions were
made to subordinate documents to preserve the parts that clarify an accepted requirement:
[../architecture/failure-and-degradation.md](../architecture/failure-and-degradation.md) records the
validation-is-not-discovery boundary, refusal categorisation, per-reason retry eligibility, the
separation of a machine-safe reason code from a household sentence, and the rule that **silence must
never be used to hide a refusal**; and
[../patterns/temporary-artifact-lifecycle-pattern.md](../patterns/temporary-artifact-lifecycle-pattern.md)
records the distinction between an idempotent and a completed cleanup, the reconciliation taxonomy,
the prohibition on reporting cleanup successful while storage was unavailable, sanitised failure
detail, self-expiring artifacts, and payload bounds rather than count bounds alone. **Both additions
are explicitly non-normative, add no requirement, and canonise no value.** The remainder is held
outside this ledger as a standing implementation-planning input.

**This note creates nothing.** It introduces **no outcome-classification model**, **no refusal
taxonomy**, **no retry policy**, **no reconciliation model**, and **no household wording standard**.
It **amends no accepted decision**, **reopens none**, and **preempts nothing** — **OD-04** still owns
policy precedence, **OD-18** still owns stability before commitment, **OD-29** and **OD-30** still
own trace persistence and visibility, and **OD-78** still owns remembered-value classes. **No legacy
schema, threshold, calibration value, vocabulary, or product ownership was imported**, and the
superseded vocabulary those documents use — *composite room*, *household memory*, *affinity*,
*experience model* — is not reactivated by being quoted.

---

### Notes on the location and engagement-context open decisions

**OD-73 and OD-74 create no responsibility, no model, and no new object.** Foundation continues to own
object definitions, the `located-in` relationship, and Room Configuration; Identity continues to own
assertions and fusion; Truth continues to own Facts and Fact history; Operational Trust continues to own
permission, disclosure, and every threshold; Concierge continues to own decisions and the Decision Trace.
**There is no Location, Engagement, Presence, or Engager responsibility, and none may be created to hold
this material.**

**No new model was created, deliberately.** The **Truth Fact** already carries a first-class, subject-typed
`Subject` field, so extending its enumeration to *Home, Room, Merged Room, Person, Pet, Asset, Device*
achieves everything five parallel location-assertion types would have achieved — with one owner, one
lifecycle, one provenance model, one conflict model, and one retention rule (**DL-47**). **A
`PersonLocationAssertion`, `PetLocationAssertion`, `AssetLocationAssertion`, `DeviceLocationAssertion`,
`CurrentEngagerAssertion`, or `EngagementContext` model must not be created.** *Location Fact* and
*Engagement Fact* are **Fact classes of the existing model**, not new models.

**One structural asymmetry is deliberate and must not be smoothed away.** A **Person**-subject location
Fact requires an Identity Assertion first (**DL-06**, **P9**), because establishing *which human* is a
fusion question over a bounded candidate set of known Persons. A **Pet**, **Asset**, or **Device** subject
requires **no Identity Assertion and must not be routed through Identity**, because there is no *which
human* question — Identity's candidate set contains known Persons only, and **DL-39** bands describe
identity support only. *"Where is Maisey?"* and *"Where is my phone?"* are **Truth-only** questions;
*"Where is Tom?"* is a two-stage question.

**"Current Engager" is rejected as an HTBW term.** It does not appear in this repository, and the concept
it names is already decomposed — more precisely — into the six **Assertion Purposes** accepted under
**DL-32**: Speaker Attribution, Room Presence, Household Presence, Interaction Initiator, Authenticated
Session Identity, and Endpoint Context. **A single fused engager result would recreate the general-purpose
identity score that DL-32 and DL-38 prohibit**, would break the **F1** purpose ceilings, would break
**DL-36**'s four independent consumers, would break **DL-34**'s separation of Requestor, Speaker, Present
Person, Potential Listener, Authorized Recipient, and Delivery Target, and would make the kiosk safeguard
unimplementable — because that safeguard *is* the purpose separation. The rejection is recorded in
[../models/glossary.md](../models/glossary.md).

**The Truth and Identity direction was already settled and is not reopened.** **DL-06**, **P9**, and
[../architecture/dependency-view.md](../architecture/dependency-view.md) rule 2 are unchanged: Identity
feeds Truth; Truth does not feed Identity authority. **The apparent circularity is a documentation defect,
not an architectural one**, and it is remediated by explanatory notes in
[../models/truth.md](../models/truth.md), [../architecture/dependency-view.md](../architecture/dependency-view.md),
and [../architecture/runtime-sequence.md](../architecture/runtime-sequence.md). **Truth's Room-occupancy
Fact precedes fusion; Truth's Contextual Person-Presence Fact follows it. They are different Fact Subjects,
and the sequence is not a cycle.**

**Only two open decisions were created, from a larger candidate set.** Extending the Fact Subject
enumeration, defining *Location Fact* and *Engagement Fact*, separating declared from current location,
stating non-Person evidence ceilings, declaring Pet and Device governing parents and retention, and
enumerating disclosure rules for device- and pet-derived location were **not** created as open decisions,
because **ownership for each is already determinate** — only the statement was missing, and it has now been
made. Creating decisions for them would have manufactured uncertainty the architecture does not have.

**Two documentary bounds apply and are recorded in the Platform Capability Review.** Device tracker
granularity is documented as the **zone**, and a connection tracker's zone as an **assumption**; **no
native Room-level or Area-level BLE proximity capability, no native pet-location capability, and no native
kiosk concept could be verified.** Under **DL-30** those burdens are **not discharged**, and no Room-level
claim may be asserted from them.

**OD-73 and OD-74 preempt nothing else.** They decide no composite-fact aggregation (**OD-17**), no Fact
validity defaults (**OD-18**), no conflict-resolution rules (**OD-19**), no assertion validity window
(**OD-15**), no risk-class enumeration (**OD-51**), no audience-uncertainty policy (**OD-71**), no
behaviour attribution (**OD-63**), and no unknown-actor correlation confidence (**OD-72**).

### Notes on the temporal open decisions

**The unverified Storage helper guard now attaches to OD-01, not to OD-34.** The official Home
Assistant Storage helper documentation could not be verified during the temporal-record review, and
no link to it is recorded anywhere in this repository. It must be located and reviewed first.
**OD-01's residual — config entry, subentry, or private storage — must not be closed on assumed
Storage helper behaviour.** OD-34 closed without relying on any such assumption, because the
temporal-persistence *model* never depended on the mechanism; it is recorded as closed on that basis
and on no other.

**Two facts about config entries are verified and constrain the residual.** Home Assistant documents
config entries as **configuration data created by a user via the UI** and **removable by the user**,
and documents subentries as configuration **added by the user via the UI**. A store that a resident
creates and deletes as configuration is therefore **structurally unsuitable for immutable historical
records**, and OD-01 is narrowed accordingly. See
[config entries](https://developers.home-assistant.io/docs/config_entries_index/).

**OD-41 does not create a responsibility.** Should a persisted Incident or Case object be adopted,
Foundation would define the model, Operational Trust would govern authority, and Concierge could
coordinate creation, assembly, narration, and export. For now, an **Incident is at least a retrieval
scope** over governed records; nothing here states that it can never become a durable object.

### Notes on the communication open decisions

**OD-42 through OD-58 create no responsibility.** Foundation defines the communication model,
Operational Trust governs entitlement and visibility, originators originate, and Concierge decides
and records delivery. **There is no Communication, Messaging, Inbox, Delivery, or Escalation
responsibility, no central delivery owner, no central inbox owner, and no second escalation ladder.**

**OD-47, OD-50, and OD-51 are recorded as partially resolved.** The Household Inbox is a projection;
there is one escalation architecture; interruption is an Operational Trust action-risk class. Only
their residual questions remain open, and reopening the resolved parts requires a new ADR.

**OD-43, OD-55, and OD-57 must not be closed on assumed Home Assistant behaviour.** Dashboard
visibility semantics, `media_player` delivery semantics, and voice-satellite indicator behaviour were
**not verified** during the communication review, and no links to them are recorded anywhere in this
repository. They must be located and reviewed first.

**OD-56 is bounded by the life-safety non-claim.** HTBW is not a life-safety system, and no closure
of OD-56 may assert smoke detection, carbon-monoxide detection, medical alerting, security
monitoring, or emergency-notification sufficiency.

**Update, 2026-09-15: OD-43's portion of this gate is discharged.** Dashboard visibility semantics
and `media_player` delivery semantics were located, reviewed, and verified for **DL-53** (see *Notes
on the delivery surface capability decision* above and the Home Assistant First review in
[adr-resident-communication-and-delivery-separation.md](../architecture/adr-resident-communication-and-delivery-separation.md#delivery-surface-capability-model-dl-53)).
**Voice-satellite indicator behaviour remains not verified**, and **OD-55** and **OD-57** still must
not be closed on assumed behaviour there.

### Notes on the platform-alignment open decisions

**OD-59 through OD-67 create no responsibility.** There is no Activity, Learning, Adaptation,
Attribution, Conversation, or Reasoning responsibility. Truth continues to own Facts and Fact
history; Continuity continues to own preferences and sessions; Operational Trust continues to own
permission; Stewardship continues to own obligations and the single escalation ladder; Concierge
continues to own decisions, delivery, and the Decision Trace. **What occurred in the household
remains a Domain Event, owned by the responsibility that observed it** — see
[../models/temporal-record.md](../models/temporal-record.md).

> **Do not close an open decision solely because a native Home Assistant capability exists.** The
> existence of a capability is evidence at step 1 of the **DL-30** burden of proof. Closure additionally
> requires that the constitutional requirement be satisfied, or that the remaining gap be recorded.

**OD-10 must not be closed on assumed Floor-registry behaviour, and OD-61 must not be closed on
assumed Area-registry behaviour beyond the documented attributes.** The Floor registry and Label
registry developer pages did not resolve during the platform alignment review, and no links to them
are recorded anywhere in this repository.

**OD-67 must classify each candidate accurately before evaluating it.** These are different things
and must not be merged: a conversation mechanism; a speech-to-text provider; a text-to-speech
provider; a conversation agent; a general reasoning provider; a local model; a cloud model; a
retrieval mechanism; and an action-execution mechanism. **Home Assistant Cloud must not be
characterised as a reasoning provider unless official Home Assistant or Nabu Casa documentation
supports that characterisation.** Record the precise documented capability instead.

Invariants that any closure of **OD-67** must preserve:

- Truth owns Facts. **A provider's output never silently becomes a Fact.**
- The Decision Trace owns governed reasoning. A provider does not author the reasoning of record.
- Operational Trust owns permission. **A recommendation never silently becomes an authorised action.**
- Concierge orchestrates. A provider is a consulted component, never a decision owner.
- **A model is replaceable.** No architecture may depend on one provider's behaviour.
- Explanations must remain grounded in governed records.
- Sensitive context is supplied only under the consent, privacy, and authority rules.

### Notes on the representation open decisions

**DL-31 creates no responsibility, no registry, and no new object.** It states how existing HTBW
concepts relate to existing Home Assistant objects. Foundation continues to own descriptive
knowledge, including **Asset Type**; Stewardship continues to own significance, care, and
obligations; Truth continues to own the evaluation of current conditions.

> **A native representation is a projection.** It makes an HTBW concept visible, targetable, and
> automatable in Home Assistant. It never becomes the authoritative record, and its absence,
> deletion, or failure never changes what HTBW holds to be true.

**OD-68, OD-69, and OD-70 are each independently closable.** None depends on the residual of
**OD-01**, and closing any of them does not close the others.

**OD-01's residual must not be closed on assumed storage behaviour.** It **now owns that residual
alone** — OD-34 previously duplicated it and has since closed on the persistence *model* without
relying on any such assumption. The Home Assistant storage-helper documentation could not be verified
during this review. Under **DL-30**, unverifiable documentation leaves the decision open.

**DL-31 preempts nothing.** It decides nothing about identity confidence thresholds (**OD-08**),
identity evidence weighting (**OD-16**), the governed-record representation mechanism (**OD-01**
residual), or reasoning provider strategy (**OD-67**).

**No custom device class exists.** Device `entry_type` accepts only `None` and the `service` member,
and device classes are entity classifications drawn from per-domain enumerations. **HTBW must not
claim a custom device class, and must not repurpose native registry fields to carry HTBW meaning.**

**Household language follows the same rule, and this resolves OD-14.** Home Assistant owns native
names, native Assist aliases, and native Assist exposure. HTBW reads them, may use them to **seed** a
contextual term, and stores only the Room-scoped meaning Home Assistant does not natively represent.
**Nothing is synchronised in either direction**, because a contextual term may name a group, a
capability, or a Room-dependent target that no alias can carry — and because Home Assistant documents
that configured aliases may also be used by assistants beyond Assist. **No new open decision was
required**, and **OD-13**, **OD-59**, and **OD-70** are untouched.

> **Do not assert that Home Assistant treats aliases as globally conflicting.** The documentation
> describes the same alias applied to entities in different Areas, matched in conjunction with the
> Area name. The write-back prohibition rests on scope and reach, not on a claimed native conflict.

### Notes on the identity-evidence open decisions

**DL-32 introduces no responsibility and no model.** The Person-to-evidence-source association was
already listed among the things Identity owns; **DL-32 names and governs it rather than creating it.**
No second Person record, no parallel person-to-tracker registry, no identity history store, and no
generic event store exists as a result.

**Ownership is unchanged.** Identity performs fusion and owns the reliability configuration, because
that configuration determines how identity evidence is *interpreted*. **Continuity does not own it**
merely because personal habits inform it. Truth is not an identity fusion engine, Concierge is not,
and Operational Trust does not calculate identity — it evaluates permission **after** an assertion
exists.

**OD-16 could not close cleanly at the time, and was not forced.** The governing architecture was
complete, but the **aggregation function** — how weighted, fresh, correlated, and contradicted evidence
becomes one confidence result — was genuinely unresolved. **Inventing arithmetic to close a decision
would have been the defect, not the closure.** *It was subsequently resolved as **DL-38**, without
inventing arithmetic — see the notes on the fusion decision below.*

**A second bound is documentary.** Device tracker granularity is documented as the **zone**, and a
connection tracker's zone is documented as an **assumption** while connected. **No native Room-level
BLE capability and no native kiosk concept could be verified**, so none is claimed, and Room Presence
is asserted only from evidence whose Room granularity is actually grounded.

**DL-32 preempts nothing else.** It decides no confidence bands (**OD-08**), no validity windows
(**OD-15**), no voice processing locality (**OD-07**), no consent user experience (**OD-06**), no
learning lifecycle (**OD-28**), no learning evidence eligibility (**OD-65**), no behaviour attribution
model (**OD-63**), no native execution evidence capture (**OD-64**), and no retention floor
(**OD-05**, **OD-26**, **OD-49**).

**Derived recognition forms are the same projection rule again, and required no decision.** A
resident configures one term; HTBW may derive additional forms of **that term** for matching, and a
derived form is subordinate, generated, explainable, and never a vocabulary entry. **No plural field,
no second authoritative value, and no new state exist.** A configured term always outranks a derived
form, so **plurality never creates a group** — group vocabulary remains explicitly configured. The
authoritative term is whatever form the household chose; **HTBW must not require singular terms**,
since the canonical vocabulary examples are themselves plural.

### Notes on the unknown-person, audience, and actor decisions

**DL-33, DL-34, and DL-35 introduce no responsibility and no owner.** Identity keeps assertions and
fusion; Truth keeps Facts; Operational Trust keeps permission, disclosure, and the unidentified-person
policy; Concierge keeps orchestration, delivery selection after permission, and the reconstruction
projection; Communication remains the governed object. There is no Actor, Audience, Security,
Privacy, or Surveillance owner, and none may be created to hold this material.

**No new model was created.** Unknown Person is the existing `unknown` assertion state carrying
whether a human participant is supported — the one element the model genuinely lacked, and the
smallest compatible extension. The unidentified-person policy is the phrase already used by
[../architecture/failure-and-degradation.md](../architecture/failure-and-degradation.md) and
[../architecture/runtime-sequence.md](../architecture/runtime-sequence.md), stated as a governed
policy rather than only as a fallback. The Unknown Actor Reference lives inside the existing
Historical Reconstruction projection and creates no store.

**Only two open decisions were created, from three candidates.** Audience-uncertainty policy
(**OD-71**) and actor-correlation confidence (**OD-72**) are each materially distinct, independently
closable, and owned. A third candidate — the unidentified-person capability defaults — was **not**
created: the architecture is accepted here, and the defaults are already the subject matter of
**OD-51** and **OD-08**. Creating it would have duplicated both.

**OD-08 and OD-16 were both open at this point.** Neither residual was resolved by this work. **OD-16 concerns
identifying a known Person from identity evidence; OD-72 concerns grouping observations without
identifying anyone.** They are different questions with different outputs, and neither aggregation
function is invented here.

**DL-35 preempts nothing else.** **DL-47** and **OD-39** own retention and hold governance,
**OD-40** still owns Evidence Package assembly and audience, **OD-41** still owns whether an Incident
becomes a persisted object, **OD-38** still owns correlation identifiers, and **OD-63** and **OD-64**
still own behaviour attribution and native execution evidence — an Unknown Actor answers *who was
moving*, never *what changed a device*.

**One documentary bound applies.** Externally owned video is referenced on whatever identifiers and
integrity metadata the owning system supplies. **No claim is made here about what any specific camera
integration exposes**, because no such documentation was verified; where the owning system supplies
nothing stable, the reconstruction records that limitation rather than substituting one.

### Notes on the confidence-consumption decisions

**DL-36 and DL-37 introduce no responsibility, no model, and no file.** Both are recorded inside the
existing Operational Trust and Identity material. Every structure they rely on already existed: the
`permitted_with_confirmation` authority outcome, the four-row action-risk table, the *Explicit
confirmation* evidence row and its explicit exclusion of *permanent certainty*, the **Authority**
state of Existence → Participation → Exposure → Authority, and
[../architecture/framework.md](../architecture/framework.md)'s assignment of *identity-confidence
thresholds* and *confirmation requirements* to Operational Trust. **Nothing is duplicated and nothing
superseded is revived.**

**They are separate because they answer different questions.** DL-36 answers *who decides whether
confidence is enough*. DL-37 answers *what a confirmation is worth once it is given*. A household
could accept the first and still get the second catastrophically wrong — by treating a confirmed
interaction as an authenticated session, or as a retroactive correction of the assertion behind it.

**No new open decision is created, deliberately.** Confirmation strength, scope, and lifetime are not
a new unresolved choice: **OD-08 already claims *confirmation scope and lifetime* as its own
residual**, so a separate decision would duplicate it. **OD-15 is not the confirmation decision** — it
is identity *assertion* validity, owned by Identity — and conflating the two would place a confirmation
policy under the wrong responsibility. Seven existing decisions were amended instead.

**OD-08 did not close then, and the residual stood at four parts** — band enumeration and meaning,
per-class and per-operation requirements, confirmation method strength and lifetime, and the
presentation-threshold default. Part (a) was blocked at the time: **OD-16's aggregation function had
to be settled first**, because a band cannot be named or calibrated before the value that produces it
is defined. **OD-16 was therefore the minimum next decision, and it was not closed here** — *it closed
subsequently as **DL-38**, and part (a) is now unblocked.*

**These decisions preempt nothing else.** **OD-43** still owns
surface perceptibility, **OD-52** still owns audience specification, **OD-57** still owns the
indication-versus-content boundary, **OD-67** still owns reasoning-provider strategy, **OD-71** still
owns audience-uncertainty policy, **OD-72** still owns unknown-actor correlation confidence, **OD-06**
still owns consent experience, and **OD-01** with **DL-31** still owns person-scoped connected
resources — a Person-anchored external account is referenced through its anchor, and **ownership is
never inferred from a connection's name**.

**One documentary bound applies.** **No confirmation mechanism is prescribed.** No companion
application, push confirmation, PIN, or secondary-factor capability has been verified against official
Home Assistant documentation, so stronger-than-verbal confirmation is described only as *available
where the platform genuinely supports it*. **OD-08(c) was not closed on an assumed mechanism.** *It was subsequently settled as **DL-40**, which classifies required strength without prescribing any mechanism.*

### Notes on the fusion decision

**DL-38 closes OD-16 without inventing mathematics.** The chosen function is **ordinal and stepped**,
not arithmetic. Additive scoring, weighted averaging, Bayesian fusion, and belief-combination models
were each evaluated and rejected on repository grounds: averaging **penalises a household for owning
fewer sources**, contradicting *missing evidence is not contradicting evidence*; probabilistic fusion
requires priors and an independence assumption the correlation rules explicitly deny, and would state
a **calibrated probability the home cannot support**; belief combination is not explainable in
household language. The stepped form is the **minimum** architecture satisfying every accepted
constraint at once.

**No responsibility, model, store, or file was created.** DL-38 is recorded inside the existing
Identity material. Every structure it uses already existed — the assertion purpose enumeration, the
five assertion states, the Identity Evidence Association, evidence families, the freshness,
correlation, contradiction, and absence sections, the fifteen-step fusion process, and the promotion
ladder. **DL-38 supplies the aggregation rules those sections were waiting for.**

**Zero new open decisions.** Everything left is **Fusion Policy configuration**: freshness durations,
step sizes, separation margins, per-purpose minimums, and reason-code strings. These are versioned,
governed, and household-configurable, and none is a materially distinct architectural question, so
none warrants an open decision of its own. Per the acceptance rule, **OD-16 is not held open for
operational tuning.**

**The OD-08 handoff is one-directional and now discharged.** DL-38 defines the *output semantics* — an
ordinal support level mapped to a confidence band through a versioned map, with **one enumeration
serving every assertion purpose**. **OD-08** names the bands and assigns operational meaning.
**OD-08(a) was unblocked and OD-08 became the minimum next decision.** Neither reopens the other, and
the former circular dependency is dissolved. *The bands were subsequently enumerated as **DL-39**.*

**Boundaries preserved rather than absorbed.** **OD-15** keeps assertion lifetime, which is not
observation freshness. **OD-72** keeps unknown-actor correlation, which has no candidate set, no
Person-to-source associations, and identifies nobody — **the fusion function must not be borrowed to
close it**. **OD-63** and **OD-64** keep behaviour attribution and native execution evidence, neither
of which is identity evidence. **OD-65** keeps learning eligibility, and a learned Fusion Policy
proposal never applies silently. **DL-36** and **DL-37** are untouched: fusion produces belief,
Operational Trust produces permission, and **confirmation is never an input**.

**One documentary bound applies.** **Native Room-level proximity detection and native managed-endpoint
human identity remain unverified.** This bounds a single evidence family's Room-Presence *ceiling* in
a given deployment; it does not bound the function, and fusion is deliberately designed against no
particular proximity implementation or voice provider.

### Notes on the confidence-band decision

**DL-39 completes the separation OD-08 was raised to settle.** Identity produces four bands and
nothing else. Operational Trust chooses among five requirement values, one of which is `None`. The
asymmetry is deliberate and is the whole decision: **four outputs, five requirements**, because *"no
identity is required here"* is a statement about a protected operation, never about a person.

**The rejected shape was a five-value band scale beginning at `None`.** It reads naturally and is
wrong in three ways. It puts a permission concept inside an evidence result. It makes *"identity was
not required"* indistinguishable from *"identity was evaluated and found absent"*. And it invites the
sentence *"High exceeded `None`, therefore the action was authorised"* — which manufactures an
identity dependency the policy does not have, and would make a correctly permitted action appear to
fail whenever identity happened to be weak.

**No band was given operational meaning.** A band says how strongly identity is supported for its
purpose. What that is *enough for* is a requirement, and every requirement is Operational Trust's.
This is DL-36 applied to the enumeration rather than restated beside it.

**The names were not allowed to hold the decision open.** The ordering, the semantics, the contract,
and the requirement values were fixed before the labels were chosen, and choosing them changed none
of it. **Low, Moderate, High, Very High** were adopted because they are already how this repository
and the household describe identity strength, because they read correctly in an explanation a
resident hears, and because **words resist arithmetic** where an ordinal numeral invites it. **A band
name applies only to a `known` Identity Assertion.** Truth facts, human-participant support, and
Unknown Actor correlation also speak of confidence; none of them carries an Identity band, and the
shared adjective never implies a shared scale.

**Three lifetime confusions are closed together.** Continuous occupancy is not continuous
authentication; a valid assertion is not the current-speaker assertion; and a confirmation is spent by
the operation that required it. Each of these, left implicit, produces the same failure — the home
keeps talking to someone who left. **No grace period, session, or presence-linked lifetime exists
anywhere in the model**, and sensor debouncing stays inside evidence freshness under DL-38 where it
belongs.

**Nothing was created.** No responsibility, no second confidence model, no second permission model, no
second confirmation model, no Identity session, no Identity Controller, no new precedence order, no
new file. **DL-36, DL-37, and DL-38 are intact and unamended**, and the Identity Fusion Function is
untouched. **DL-40 fills the enumeration slot DL-37 itself deferred**, which is completion, not
reopening.

**The last residual was a framing error, not a missing fact.** OD-08 held the **confirmation
method-strength enumeration** open as *documentarily bounded*, because no companion-application,
push, PIN, or secondary-factor mechanism has been verified against official Home Assistant
documentation. That bound is real and remains in force — **no mechanism may be prescribed until it is
verified** — but it never bound the architecture. **A required strength is a classification; an
implemented mechanism is a platform capability**, and only the second needs documentation. **DL-40**
settles the first: an ordered class set, a rule that the capability declares the class it requires, a
rule that only a verified mechanism satisfies a class, and `Unavailable` where none does. Mechanism
mapping is deployment configuration, not an open decision. **Per-class defaults were not treated as a
residual**; they are configuration resolved with OD-51. **OD-08 therefore closes.**

**OD-15 is amended for boundary only, and is not closed.** Validity is a window; applicability is a
question about *this* interaction. A window creates no permission and no confirmation persistence.

---

### Notes on capability dependency, storage, and artifact lifecycle

**DL-41, DL-42, and DL-43 answer three questions that the repository had never asked.** HTBW had a
rich model of *may this happen* and no model at all of *can this happen here*. It had a Connected
Storage principle and no statement of what Home Assistant already owns. It had per-artifact rules and
no requirement that an artifact declare a lifecycle before it exists. The three decisions close those
gaps in that order, and each depends on the one before it.

**They introduce no responsibility.** There is no Capability responsibility, no Storage
responsibility, no Artifact responsibility, no capability registry, no dependency registry, no
artifact registry, and no dependency broker. A declared dependency is a **property of a capability**,
owned by the responsibility that owns the capability, in the same way that a required Confirmation
Strength is a property of a protected operation under **DL-40**. Adding an owner would have been the
easy mistake and the wrong one.

**The dependency question is deliberately upstream of both identity and permission.** *Can this
happen at all* is answered before *who is this*, which is answered before *may this happen*. This
ordering is not a convenience; it is what prevents the two failure modes that motivated **DL-41**.
Rendering an absent integration as a refusal teaches a household that the home is withholding
something it could do. Rendering a policy denial as a missing feature teaches the opposite, and
invites someone to go looking for a configuration change that will never help. The five distinct
outcomes exist for the same reason: **a wrong explanation is a governance failure, not a wording
problem**.

**DL-42 states for storage what DL-31 stated for models.** It is the storage face of Home Assistant
First, not a new principle. Its sharpest clause is the one about justification: duplication requires
a **documented governed gap**, and a wish for longer retention is not a gap. That is precisely the
argument that would otherwise be used to build a second Recorder, and it is refused here in advance.
Where Connected Storage is absent, HTBW does not shrink into a local imitation of it — the dependent
capability is simply unavailable, and says so.

**External History Retention is one value on purpose.** A retention window and a purge window that
can drift apart become two policies, then a tier, then an archive, then a second retention model
inside the thing that was meant to extend the first. Collapsing them into a single configured period
makes that drift impossible to introduce accidentally. The period is a **ceiling**: it never
overrides a **P27** floor, and a Preservation Hold suspends it. **Purge cadence was deliberately left
unstated** — the repository has never accepted a runtime schedule as architecture, and this decision
does not become the first to do so.

**DL-43 is a burden-of-proof decision rather than a schema.** The declarations it requires are
questions, not fields, and their purpose is to make an undeclared lifecycle impossible to defend.
Two of them do the real work. *What happens when storage is lost after the artifact exists* is the
question that separates a governed artifact from an orphan, and it was the gap most likely to be
discovered in production rather than in review. *Does consent delete it* is the question that keeps
withdrawal from decaying into a visibility toggle.

**Projections were held apart from artifacts throughout.** An Evidence Package and a Historical
Reconstruction are assembled from governed records on demand, and neither becomes a store because it
was useful once. Only a deliberately saved copy is an artifact, and it then carries a full lifecycle
declaration of its own. A Preservation Hold is likewise a **marker on records**, never a duplicated
payload — the temporal-record rules already prohibited copying, and DL-43 does not quietly reopen it.

**Nothing here settles a mechanism.** Storage technology, layout, encryption, synchronisation,
recovery tooling, dependency health detection, purge scheduling, and reconciliation after storage
replacement all remain open, and are recorded as such against **OD-02**, **OD-03**, **OD-33**,
**OD-34**, **OD-36**, **OD-39**, **OD-40**, and **OD-67**. Each of those was amended for boundary
only. **None was closed**, because in every case the technical or policy question that kept it open
is still unanswered.

**Subsequently — OD-02 and OD-03 were closed by DL-44 and DL-45**, once the storage-provider
boundary was established and the residual questions were shown to be implementation mapping rather
than architecture. **OD-33 and OD-34 were later closed by DL-46 and DL-47**, on the retention and
persistence *model* rather than on any storage mechanism. The remainder of the list is unaffected,
and purge scheduling, recovery tooling, and reconciliation after storage replacement remain open.

---

### Notes on the storage-provider and cleanup decisions

**DL-44 removes a question HTBW should never have been asking.** Storage technology had been carried
as an open decision since the foundation, as though HTBW would one day choose between SMB and NFS.
Home Assistant already makes that choice, already mounts the share, already holds the credentials,
and already surfaces the result. **P21** had the answer the whole time; the decision only had to be
read. HTBW's ownership begins where Home Assistant's ends, and not one step earlier.

**The harder half of DL-44 is the sentence about access.** Persistence and user experience had
quietly blurred together, and the blur was about to produce a file browser. It is worth being
explicit about why that would have been wrong: a resident who must find a folder to reach a manual is
a resident the architecture has failed. **The Asset lists its documents. The profile owns its
voiceprint. A question retrieves history.** Storage is the floor, not the room.

**The My Media finding was deliberately written down at its true strength and no higher.** Home
Assistant documentation establishes that media directories are protected by **authentication** —
which is a real and useful property — and establishes nothing whatever about per-person
authorisation, nor about an unlisted file type being unreachable by every path. The same directories
are reachable through file-access apps. So the finding is recorded as a **visibility boundary**, and
**Operational Trust remains the security boundary**. It would have been easy, and wrong, to let a
convenient platform behaviour stand in for governance.

**OD-02 closed because its architectural content turned out not to be a schema.** The question was
*"what format?"*, but what HTBW actually needed was the ability to **find, govern, retain, and delete**
an artifact — and that is a reference contract, not a file format. A manual is a PDF because the
manufacturer made it one. A voiceprint is whatever its encoder produces. **Imposing one payload
schema across those would have been an architecture serving itself.** What remains is per-capability
encoding, which is implementation.

**OD-03 closed on the provider boundary plus nine namespace rules.** The rules that matter are the
negative ones: **no resident-supplied path as an identifier**, and **no display name as the only
storage key**. Both are how artifact stores become unrecoverable — someone renames a Room, and the
artifacts beneath it are orphaned by an operation nobody thought was destructive. Folder names stayed
implementation on purpose; **an architecture that names folders has started building a product**.

**DL-45 exists because absence of a rule is itself a rule.** With nothing stated, every artifact
would have survived its parent, and the store would have filled with material belonging to Assets
that no longer exist and People who have been removed. **The default is now cleanup, and continued
existence has to be argued for.** Two guards keep that from becoming its own hazard: a hold or a
retention floor always outranks it, and **cleanup is never reported successful when storage was
unavailable** — a claim of deletion is a claim about the world, and HTBW does not make one it cannot
support.

**Retention and parent cleanup were kept as two mechanisms on purpose.** A time window and a
governing object answer different questions, and collapsing them would mean either that deleting an
Asset silently waits for a purge cycle, or that a purge cycle silently deletes something still
owned. An object-scoped record class is simply subject to both.

**No new decision was created for pending cleanup.** The obligation to reconcile a deletion that
could not complete is the same obligation **OD-36** already carries, and inventing a second decision
for it would have split one question across two records. **OD-33, OD-34, OD-36, OD-39, and OD-40 were
narrowed and none was closed**, because storage placement was never what kept any of them open.
**OD-33 and OD-34 closed later, under DL-46 and DL-47, for entirely different reasons.**

---

### Notes on explainability persistence and retention

**DL-46 records a separation that was already true and had never been said in one place.** Home
Assistant retains what happened to the house; HTBW retains what the house made of it. Occupancy
became active, a voice interaction occurred, playback began — those are the platform's. That Tom was
supported as the current speaker at High confidence, that wearable and voice evidence contributed,
that music required no known identity, that identity nevertheless supported naming him in the reply —
**none of that exists anywhere in Home Assistant, and none of it can be recovered from a state
table.** That is the boundary, and it settles the retention argument as well: a longer retention
requirement never becomes a licence to copy the platform's history into HTBW's.

**The "bounded summary" turned out to be something the repository already had.** The review began
expecting to invent a way for a Decision Trace to stay meaningful after a native event ages out, and
found the answer already accepted: **the Fact is the summary.** Truth records the Subject, Statement,
confidence at the time, Provenance, evidence references, Coverage, and Freshness — *"the Den was
accepted as occupied"* — and it was never a copy of the sensor row. **No new construct was created,
because creating one would have quietly rebuilt the Recorder under a gentler name.**

**Significance needed no owner either.** The rule was already in the record boundary: *an occurrence
is evidence for an explanation; it is not automatically a Decision Trace*, and **HTBW never produces
a trace for a decision HTBW did not make**. A trace tracks a decision, not an event. Every proposal
for a significance threshold, a capture policy, or an event filter would have been a way of solving a
problem the boundary had already dissolved.

**The most important line in DL-46 is a prohibition on flattery.** A trace that says *"Tom was
recognised, therefore the music played"* is more satisfying than the truth, which is that the music
required no identity at all and would have played for anyone. **The home is not permitted the
flattering version.** Identity may be recorded as supporting attribution and named presentation; it
may not be dressed up as authorisation it never provided.

**DL-47 closed OD-33 by removing the thing OD-33 was asking for.** The decision wanted a retention
matrix — every record class down one axis, floors and ceilings across the other. Such a table would
have been obsolete the moment a capability declared a new record class, and it would have lived apart
from the classes it governed, which is how retention tables drift out of truth. **DL-43 had already
proved the better shape**: retention is declared inside the lifecycle, by whoever owns the class, and
a class with no declared retention is not accepted. DL-47 does nothing cleverer than apply that rule
to records as well as artifacts.

**Four floors survive any configured window, and they share one reason.** A Tombstone, a
consent-lifecycle record, a held record, and the versions that keep a held trace explainable are all
things whose removal would erase the evidence of the removal. **A purge that deletes the proof of the
purge has not enforced retention; it has covered its tracks.**

**OD-34 closed on a duplication, not on a discovery.** Its residual — *config entry, subentry, or
private storage* — was stated word for word in **OD-01**, which owns Home Assistant representation
and is where a representation question belongs. Two decisions holding one residual is not caution; it
is an ownership defect, and it kept OD-34 open long after the temporal-persistence model was
finished. **The repository's standing guard was honoured rather than removed**: the Storage helper
documentation is still unverified, so the guard was **re-pointed at OD-01**, where the unverified
dependency actually lives. OD-34 closed without relying on any assumption about it.

**One verified fact narrowed OD-01 on the way past.** Home Assistant documents config entries as
configuration data **created and removed by the user through the UI**, and subentries likewise.
**A store the resident can delete as configuration cannot hold immutable history** — so one of the
three candidates is now excluded on evidence rather than preference. The remaining choice still waits
on documentation that has not been found.

**OD-05, OD-26, and OD-49 were narrowed and left open.** Each now has its rule and lacks only its
value, which is a household configuration question. **No decision was created in this review**, and
the fourteen scenarios were added to an existing file rather than a new one.

---

### Notes on the October 2026 Voice Explainability investigation

**The problem is retention, not evidence generation.** A real Production incident — a resident's
voice command resolving to a broad light action instead of its governed routine — was reconstructed
in full from native Home Assistant sources alone: a Recorder `context_id` burst with no parent,
correlated by timing against an Assist satellite's own `listening → processing → responding → idle`
sequence, against a background of two competing voice-entry automations (one live, one disabled)
discovered only by reading the household's own configuration. **Home Assistant already produces
enough evidence to explain many voice actions. It does not keep that evidence long enough, in a form
that can be joined to itself.**

**Assist Debug and Recorder are confirmed, at the source level, to be two separate evidence systems
with no native bridge.** Assist Debug holds the richest single-interaction record available — STT
output, intent input and output, successful and failed entities, TTS response, exact stage timing —
but it lives only in `hass.data`, capped at ten runs per pipeline, and is gone on the next restart.
Recorder holds durable execution evidence indefinitely, keyed by `context_id`, but **never** the
pipeline-side identifiers. **Nothing in Home Assistant joins them.** This is the concrete, now
source-verified shape of **OD-38**'s own question — whether and how Context IDs are adopted as HTBW's
correlation strategy — and of **OD-64**'s question of which platform-supplied execution evidence HTBW
references and retains. **Neither is closed by this finding.** The finding narrows both: any future
correlation strategy must assume no native join exists and must say, honestly, when it is
HTBW-authored correlation rather than an observed platform fact.

**Identity in a voice-originated explanation is not one question but several, and the investigation
needed all of them kept separate.** A household's report of *who* spoke is not the same thing as a
`context.user_id` (which this investigation again confirmed is `None` for every automation- and
voice-originated context examined), is not the same thing as the device or satellite a context can be
timing-correlated against, and is not the same thing as an unresolved actor. **This is not a new
decision.** **DL-35**'s Unknown Actor Reference, **OD-63**'s behaviour-attribution semantic model, and
this document's own exhaustive `Context` field classification (`home-assistant-boundary.md`, item 13)
already hold these distinctions; the investigation is recorded as a confirming exercise, not a
discovery, and as a caution that **future voice evidence work must keep reporting which of these it
means, every time, rather than collapsing them under one word.**

**A UTC-versus-household-local defect obscured evidence before it illuminated anything.** Every
Recorder and `.storage` timestamp is UTC; the configured household time zone is a separate, verified
fact (`core.config`); and comparing a resident's reported local time against raw UTC evidence without
that conversion produced a materially wrong investigative window before it was caught. This is recorded
as an operational-discipline finding, not an architectural one: any resident-facing explanation
carrying a timestamp must state it in household-local time, a requirement **explainability.md** now
states directly.

**Assist Debug is operational evidence; Recorder is execution evidence; a trustworthy explanation
needs both, and neither is currently durable enough on its own to answer "why did it do that" after
the fact.** A new candidate concept — named **Voice Interaction Evidence** at the time of this note,
and subsequently broadened into the **Explainability Evidence Record** hypothesis (see the
continuation note below) — is named in [explainability.md](../architecture/explainability.md) to hold
the shape of what a durable record would need to carry, explicitly **not** as a storage design and
explicitly in tension with **DL-46**'s existing "HTBW does not retain... a voice interaction" — a
tension the new section names rather than resolves, leaving its resolution to **OD-29**, **OD-38**,
and **OD-64**.

**Voice Explainability belongs to HTBW governance, not to Home Assistant customization.** No change to
Home Assistant's own configuration, behaviour, or retention was made or proposed by this
investigation, and none is proposed here. Where HTBW eventually collects its own explainability
record, it does so as an external, referencing observer — consistent with **DL-16** and **DL-46** —
never by modifying native Assist Debug retention or Recorder behaviour to compensate.

**No new open decision was created, and none was closed.** **OD-29**, **OD-38**, **OD-64**, and
**OD-72** are each narrowed by verified evidence recorded in `home-assistant-boundary.md` and
`explainability.md`; none is resolved, and this review decided nothing.

---

### Notes on the Explainability Evidence Record hypothesis (continuation, 2026-10-06)

**Voice turned out to be one Source, not the governing shape.** Working the same reasoning that
produced Voice Interaction Evidence against a non-voice case — a wall switch, a kiosk, an occupancy
sensor — showed the same six questions recur regardless of source: who, if anyone; where this
originated; what the initiating occurrence was; what Home Assistant actually executed; what was
observed to result; and how that becomes a truthful account. **Voice Interaction Evidence is retained,
unchanged in its own content, as the voice-specific worked case of a broader hypothesis —
Explainability Evidence Record — rather than superseded by it.**

**Almost the entire hypothesis turned out to already be owned, once it was stated stage by stage.**
Person/Actor is **DL-38**'s Identity Fusion Function, evaluated against whichever of the six existing
**Assertion Purposes** applies — nothing in the hypothesis required a seventh. Source is the existing
**Behaviour Source** enumeration. Execution is the existing Context/Parent Context/User Context
evidence already recorded under **OD-38**. Outcome is the existing Domain Event resulting-state
evidence, and, for a Communication, **DL-54**'s already-accepted Presentation Outcome. Explanation is
the existing record boundary — Facts to Truth, occurrences to Domain Events, HTBW decisions to the
Decision Trace, record versions to Temporal Records — assembled by Concierge, which owns none of what
it assembles. **Stating the hypothesis did not discover six new ownership questions. It found one.**

**The one word in the hypothesis that could not be kept is "Activity."** `glossary.md` and
`temporal-record.md` both already and independently foreclose it: Activity is reserved for the
distinct Home Assistant integration of that name, and behaviour attribution "does not require, and
must not become, a separate Activity model, Activity responsibility, or Activity store." The
hypothesis's initiating-occurrence stage is recorded using the already-accepted **Trigger** and
**Domain Event** instead. **This is reuse under an existing prohibition, not a style choice**, and it
is recorded here so the collision is never rediscovered as if it were new.

**The genuinely open residual is narrower than the hypothesis first appeared, and it already has an
owner.** **OD-63** already asks for *"the enumeration of behaviour sources, the evidence required to
assert each, the confidence representation, and how unattributed is represented."* A voice interaction
carries Pipeline ID, Pipeline Run ID, Conversation ID, and Satellite ID; a kiosk interaction, a
wall-switch press, and a schedule trigger each carry different native evidence. Whether one
source-neutral evidence shape is required, or whether each Behaviour Source category simply states its
own fields under OD-63's existing ownership, **is OD-63's question, informed by this hypothesis, and
is not decided here.**

**Source, Endpoint, and Person remain independently owned and were not collapsed.** The hypothesis's
Kiosk, Guest, and Identity Triangulation worked examples are **DL-38 and DL-32 applied, not extended**
— a kiosk or satellite may carry a proxy association to a Person, which contributes evidence at its
configured reliability exactly as any other source does, and a kiosk is confirmed, by this
repository's own native-evidence review (`home-assistant-boundary.md`, **L8**), to have **no native
concept of its own** beyond an ordinary Home Assistant user account. **A kiosk, a switch, and a
satellite are Sources. None of them is a Person, and none of this hypothesis's examples says
otherwise.**

**No new decision was created, and none was closed by this continuation.** **OD-63** gains the
sharpest statement yet of its own residual; **OD-38**, **OD-64**, **OD-72**, and **OD-29** are narrowed
exactly as the prior note recorded, and no further than that. **No eighth responsibility was created**
— Concierge continues to assemble an explanation from evidence it does not own, exactly as
`decision-trace.md` and `explainability.md` already required before this review began.

---

## Part 3 — Recorded supersessions

| Superseded | Replaced by |
|---|---|
| The four-service platform model | [../architecture/north-star.md](../architecture/north-star.md), [../architecture/framework.md](../architecture/framework.md) |
| `canonical-architecture.md` | [../architecture/north-star.md](../architecture/north-star.md), [../architecture/framework.md](../architecture/framework.md), [../architecture/dependency-view.md](../architecture/dependency-view.md) |
| `adr-voice-identity-platform-service.md` | [../architecture/adr-identity-replaces-voice-identity-boundary.md](../architecture/adr-identity-replaces-voice-identity-boundary.md) |
| "Foundation owns truth" statements | [../contracts/truth-contract.md](../contracts/truth-contract.md) |
| `composite-room-contract.md` | [../contracts/room-configuration-contract.md](../contracts/room-configuration-contract.md) |
| `room-vocabulary-registry-contract.md` | [../contracts/contextual-vocabulary-contract.md](../contracts/contextual-vocabulary-contract.md) |
| `person-identity-contract.md`, `voice-recognition-contract.md` | [../contracts/identity-contract.md](../contracts/identity-contract.md) |
| *Notification* as an HTBW domain term | **Communication** (the object) or **Delivery** / **Delivery Attempt** (the act). See [../models/communication.md](../models/communication.md). Retained only as Home Assistant platform vocabulary. Formal supersession scope is **OD-58** |
| "Alias-first" as the **source of truth for household phrases**, in the subordinate pattern and philosophy documents | [../models/contextual-vocabulary.md](../models/contextual-vocabulary.md). Native aliases remain a **seed and a native execution target**; they are not the authority for household vocabulary. Resolved under **OD-14** |
| *Message* as an HTBW domain term | **Communication**. Retained only for external provider content where the provider is the system of record. Formal supersession scope is **OD-58** |
| The Concierge "Communication Model" delivery levels — Info, Attention, Urgent | The orthogonal **Category** and **Urgency** axes in [../models/communication.md](../models/communication.md) |
| "Operational Trust **enforces** what is appropriate", and the unqualified "Operational Trust determines what is appropriate" | **Operational Trust determines what is appropriate for this request, in this context**, paired with *the household defines what appropriate means*. Enforcement is execution and belongs to an executor. See [../models/operational-trust.md](../models/operational-trust.md) |
| "Care results in action when attention is required" | **Care creates an obligation when attention is required.** Whether an action follows is Operational Trust's, Concierge's, and the executor's. See [../models/stewardship.md](../models/stewardship.md) |
| "Stewardship determines what matters" | **The household declares what matters; Stewardship represents that declaration** as care expectations and evaluates observations against them. See [../models/stewardship.md](../models/stewardship.md) |
| "Room health" and "asset health" as state models | **Neither exists and neither may be invented** (**OD-69**). The constituent statements are a **Truth** Fact and a **Stewardship** obligation state, kept separate. *Room health* survives only in pre-refoundation and historical illustration documents |

The complete per-file disposition is in [document-register.md](document-register.md).

---

## Related documents

- [authority-order.md](authority-order.md)
- [open-decision-issue-index.md](open-decision-issue-index.md) — the canonical issue link for every open decision
- [document-lifecycle.md](document-lifecycle.md)
- [document-register.md](document-register.md)
- [../architecture/principles.md](../architecture/principles.md)
- [../models/temporal-record.md](../models/temporal-record.md)
- [../models/communication.md](../models/communication.md)
- [../architecture/adr-resident-communication-and-delivery-separation.md](../architecture/adr-resident-communication-and-delivery-separation.md)
