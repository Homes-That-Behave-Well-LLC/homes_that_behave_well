# Identity Contract

> **Document status: Canonical contract.**
> Responsibility: **Identity**. Model:
> [../models/person-and-identity.md](../models/person-and-identity.md).

---

## Owning responsibility

**Identity — who do we believe this is?**

Voice Identity is superseded as a platform-service boundary inside HTBW Core. **Voice is one identity
evidence source among many.** Any document asserting Voice Identity as a platform service or product
boundary within HTBW Core is superseded.

---

## What Identity guarantees

- An **identity assertion** carrying a candidate person, **the purpose it answers**, a confidence,
  contributing evidence classes and families, freshness, and a reason code
- Explicit representation of `known`, `ambiguous`, `unknown`, `unavailable`, and `not required`
- Evidence attribution sufficient for explanation, including **contradicting and unavailable evidence**
- **Provider match values preserved as reported**, never rewritten as fused confidence
- Enrollment, revocation, and diagnostic operations
- Privacy-safe outputs only
- **Confidence bounded by the evidence that supports it** — Identity never states more belief than its
  eligible evidence can carry

---

## Participation and consent

**Participation is optional, and participation requires consent.**

| Guarantee | Statement |
|---|---|
| Every evidence class is opt-in | **Voice identity evidence is available only for a consenting, enrolled participant.** Wearable, device, and person-scoped preference participation are equally opt-in |
| Declining is neutral | Fewer eligible families yield a **lower ceiling, never a penalty**. *Missing evidence is not contradicting evidence* |
| Declining is not exclusion | A person who has not consented must still be able to use the home in a **guest-safe** way |
| Enrollment is explicit | **Never a silent by-product of ordinary use** |
| Consent is scoped | Consenting to voice identity is **not** consent to calendar access |
| Consent gates eligibility | Evidence lacking valid consent is **excluded before weighting, never down-weighted**. **A withdrawn consent is not a reduced weight** |
| Revocation is complete | It removes the derived profile and its associations, not merely their use |

The governing chain — **Consent → Available Evidence → Identity → Operational Trust** — places
eligibility before fusion and sufficiency after it. **Consent determines what evidence may be used;
Operational Trust ensures those choices are applied consistently and respectfully.**

**The consent scope model, the canonical consent record, self- and proxy-consent, Person Setup as the
capture and review experience, withdrawal/deletion semantics, and the DL-43/DL-47 resolution are
accepted as DL-56** — see [../models/person-and-identity.md](../models/person-and-identity.md#consent-dl-56).
Withdrawing Voice Identity participation excludes the evidence **immediately**, before weighting, and
triggers **DL-43** deletion of the voiceprint, derived profile, and any temporary samples; it is never
merely down-weighted. **Observation is not Person Association**: environmental observation (a camera
image containing a person, a BLE device's presence, motion, occupancy) requires no person-association
consent, and correlation capability is never itself authorization to associate an observation with a
named Person.

---

## What Identity will never guarantee

- Authoritative room occupancy
- Authoritative presence in a contextual space
- What activity is occurring
- What should happen
- What a person prefers
- What a person is permitted to do

> **Identity is advisory context. Identity is not authentication and not authorization.**

---

## The three-way distinction

Consumers must never collapse these.

| Concept | Owner | Example |
|---|---|---|
| Identity Evidence | Identity | A voice sample matched Tom's profile at 0.91 |
| Identity Assertion | Identity | Candidate Tom, identity_confidence_band: High, from voice + BLE + phone |
| Contextual Person-Presence Fact | **Truth** | Tom is present in the Den, carrying its own **Truth Confidence Band** (**DL-58**), never the Identity Assertion's band |

An identity assertion is an **input** to a presence fact. **No consumer may record an assertion as a
fact.**

---

## Evidence sources

Voice matching, BLE devices, assigned phones, watches, and tablets, companion-app signals, presence
trackers, Wi-Fi associations, room-transition evidence, vehicle associations, explicit household
enrollment, and future sources.

No source is architecturally privileged. **Reliability is configured per Person-to-source association**
— never per device type — and the fusion function is accepted as **DL-38**.

### What a voice evidence provider may and may not return

**A voice provider is one evidence source and holds none of Identity's responsibilities.** The runtime
topology that produces this evidence is accepted as **DL-50** and recorded in
[../architecture/adr-wyoming-compatible-voice-evidence-runtime.md](../architecture/adr-wyoming-compatible-voice-evidence-runtime.md).
**Providers produce evidence; HTBW produces decisions.**

| The provider returns | The provider never returns |
|---|---|
| An **ordered candidate list** with a provider-reported score for each candidate | A resolved Person (**DL-06**, **DL-32**) |
| Winner-to-runner-up **separation data** and ambiguity indicators | A confidence band — bands are Identity's output (**DL-39**) |
| **Encoder family, encoder version, and audio-contract version** | Fused confidence (**DL-32**) |
| Audio-quality and speech-region metadata | A threshold verdict — Operational Trust owns every threshold (**DL-36**) |
| `no-match`, `unavailable`, and `incompatible` outcomes | Authorization, permission, a Trust outcome, or a Concierge outcome |

**Four rules bind the boundary.**

| Rule | Statement |
|---|---|
| **A provider match value is not portable** | The same similarity metric yields materially different operating points across encoders and preprocessing. A provider value is meaningful **only within its own provider**, is never compared across providers, and is never rendered to the household. The four bands are the only cross-provider currency |
| **A provider that evaluated and found nothing yields `unknown`** | Never `unavailable` (**DL-33**) |
| **A non-match never suppresses transcription** | Voice comparison is enrichment. It never gates speech-to-text, and identity never travels inside transcript content |
| **Compatibility is enforced before comparison** | Encoder family, encoder version, and audio-contract version must match. A mismatch produces an explicit **DL-41** outcome — *configured but invalid* — and never a comparison made on assumption |

### What Identity guarantees about evidence

| Guarantee | Statement |
|---|---|
| Every assertion states its purpose | Speaker Attribution, Room Presence, Household Presence, Interaction Initiator, Authenticated Session Identity, or Endpoint Context. **There is no general-purpose identity score** |
| Reliability is person-specific | Configured on the association between one Person and one evidence source. A device type may suggest a default; **it never sets the authoritative value** |
| Configured reliability is not measured accuracy | A configured weight is a **contribution weight**, stated as a band. It is never presented as measured accuracy |
| Freshness applies | A source's contribution depends on how recently it was observed, for the claim being evaluated |
| Correlated evidence counts once | Observations sharing an **evidence family** are not counted as independent confirmations. **Independence is never assumed from separate entities** |
| Contradiction is retained | Contradicting, unavailable, and ambiguous evidence are recorded with the final reason, and are claim-specific. **This is DL-38's own contradiction handling inside fusion — Truth's genuine-conflict rules (DL-63) never reuse or duplicate it, and apply only to Truth's own consumption of the resulting Assertion** |
| Absence is neutral | **Missing evidence is not contradicting evidence.** Not configured, unavailable, not observed, stale, disabled, and consent-withdrawn are distinct states |
| Consent gates eligibility | Evidence lacking valid consent is **excluded before weighting**, not down-weighted |
| Native associations are consumed | Where Home Assistant holds the Person-to-tracker relationship, **HTBW does not maintain a competing one** |
| History is not rewritten | Changing a reliability value **never alters an earlier assertion** |

### What Identity guarantees about fusion

| Guarantee | Statement |
|---|---|
| **Identity fuses; nobody else does** | Truth, Operational Trust, Concierge, Communication, and reasoning providers **never fuse identity evidence** and never re-weight it |
| **Deterministic** | The same inputs, at the same evaluation time, under the same **Fusion Policy version**, produce the same result |
| **Monotonic** | An eligible supporting observation never lowers a result; a contradicting one never raises it |
| **Stepped, never summed or averaged** | Support is set by one anchor family and raised by bounded corroboration steps. **Percentages are never added, averaged, or multiplied together** |
| **Ceilinged by what the source can establish** | A family never contributes above the highest level it can reach **for that assertion purpose** |
| **One contribution per correlation family** | Additional observations in a family may improve observation quality; they never become a second confirmation |
| **Absence is neutral** | Fewer available sources produce a **lower ceiling**, never a penalty, and never a denominator effect |
| **Separation is required for `known`** | The leading candidate must reach the purpose minimum **and** exceed the next candidate by a governed margin. Otherwise `ambiguous` |
| **No candidate is forced** | A leading candidate below the minimum yields `unknown`, not a weak `known` |
| **Confirmation is never an input** | A confirmation outcome never enters fusion and never recalculates a result (**DL-37**) |
| **Belief, not probability** | The result is governed belief. It is **never presented as a calibrated probability, likelihood, or measured accuracy** |
| **Versioned** | Every assertion references the Fusion Policy version that produced it, and **earlier assertions are never recalculated** |
| **Testable without hardware** | Deterministic fixtures reproduce results without live biometric or proximity hardware |
| **Exactly four bands** | A `known` assertion carries **one of Low, Moderate, High, or Very High** — ordered, purpose-specific, and describing identity support only (**DL-39**) |
| **No `None` band** | Identity never produces `None`. `None` is an **Operational Trust requirement value**, never an Identity output |
| **Band is not permission** | A band carries no access, presentation, personalization, disclosure, confirmation, or authentication meaning |
| **State is not band** | Bands apply only to `known`. `ambiguous`, `unknown`, `unavailable`, and `not required` carry **no band** |
| **Confirmation never changes a band** | A confirmation outcome is a separate governed record. The assertion's band is unchanged by it (**DL-37**) |

The fusion architecture is [../models/person-and-identity.md](../models/person-and-identity.md).

---

## What consumers may rely upon

| Consumer | May rely upon |
|---|---|
| Truth | Assertions as evidence toward presence and occupancy facts |
| Operational Trust | The candidate and confidence, to apply thresholds by action-risk class |
| Continuity | The asserted owner of a session, subject to confidence |
| Concierge | The assertion for attribution and explanation |

---

## What consumers must never assume

- That an assertion is a fact
- That the highest-confidence candidate may be silently selected for an authority-bearing action
- That a stale assertion is current
- That `unknown` may be treated as the most likely resident
- That `not required` means identity was confirmed
- That an assertion authorizes anything by itself
- **That an assertion for one purpose answers another** — household presence is not room presence,
  room presence is not speaker attribution, and an authenticated account is not a physical person
- That a managed endpoint or kiosk account identifies the human using it
- That occupancy identifies a Person
- **That a pet tag, asset tag, or other non-person tracker is identity evidence** — it belongs to Truth as a Location Fact source and never enters fusion
- **That a device-location Fact identifies the location of the Person bound to the device**
- **That an Engagement Fact identifies who is engaging** — it states that an interaction is occurring and nothing more
- **That a "Current Engager" exists** — the term is rejected; use the applicable assertion purpose
- That a provider match value is the home's own confidence
- **That `unknown` means nobody is there** — an Unknown Person may be present and interacting
- That `unknown` is an error, a degraded mode, or a condition to be retried away
- That an unknown evidence source identifies, or will later identify, a person
- That two unassociated observations close in time belong to the same human
- That an Unknown Person is entitled to, or excluded from, anything by Identity's report alone
- **That a confidence value carries its own threshold** — sufficiency belongs to the consumer, and is not universal
- **That a successful confirmation raised, completed, or corrected the assertion it was raised against**
- That a confirmation granted for one purpose, capability, operation, channel, Room, or moment covers another
- That being permitted to address someone by name implies permission to act as them, or to read anything of theirs
- **That a consumer may re-weight, re-combine, or recompute identity evidence** — a reference is not permission to re-run fusion
- That a confidence value is a probability, a likelihood, or a measured accuracy
- That two assertions produced under different Fusion Policy versions are directly comparable without stating so
- **That `None` is an Identity band, or that an Unknown Person, `not required`, `unavailable`, or `ambiguous` result carries a band**
- **That a prior assertion is the current-speaker assertion** — being a permanently valid historical record never makes it applicable to a new interaction (**DL-64**)
- **That continuous Room occupancy preserves the identity of a prior speaker**
- That a prior presentation eligibility, band, or confirmation may be carried into the next interaction
- That a successful confirmation established an authenticated session, or that it altered the band

---

## Assertion Validity and Applicability (DL-64)

An identity assertion describes a moment, not a session.

- An assertion is a **permanently correct historical record** of what evidence supported, for its
  stated purpose, at the moment it was produced (**DL-64**) — it never "expires" in the sense of
  becoming false.
- **Current-Interaction Applicability is re-evaluated fresh, on demand**, by re-running the Identity
  Fusion Function against current eligible evidence — never by consulting a stored expiry timestamp.
  `unknown` and `unavailable` are never reused as though current.
- **No Assertion Purpose requires a fixed validity duration.** Fusion Policy's own per-source freshness
  windows, graduated reduction, and hard cutoff already bound what counts as current eligible evidence.
- **A runtime attribution context must not become a long-lived identity session.**

**Assertion Validity, Current-Interaction Applicability, and Retention are three distinct concepts**
(**DL-64**), and no fixed validity window is architecture.

**An assertion lifetime is not a confirmation lifetime.** Assertion Validity is permanent and belongs
to Identity (**DL-64**). How long a governed confirmation covers a request is **DL-37** and belongs to
Operational Trust. The two must never be conflated, and **a confirmation never extends the life of the
assertion it was raised against**.

**Validity is not applicability.** An assertion remains a valid historical record forever, for the
purpose and moment it was produced. It does **not** thereby become the current-speaker
assertion for a new interaction. Identity guarantees that a consumer needing a current result
receives one evaluated from **current eligible evidence**, and never a prior assertion revived
because presence continued (**DL-39**).

---

## Uncertainty and unknown representation

| Reason code | Meaning |
|---|---|
| `known` | A candidate is asserted with sufficient confidence |
| `ambiguous` | Two or more candidates are plausible; all are reported with confidences |
| `unknown` | A participant or presence is supported, but no eligible known Person can be established |
| `unavailable` | Identity could not be evaluated; a dependency failed |
| `not_required` | The interaction does not require identity |

### Unknown Person

> **Unknown is a valid identity outcome, and Identity must not overstate confidence to avoid it.**
> **The home should not be more confident than the evidence supports.**

`unknown` carries whether a **human participant** is supported. Identity guarantees that consumers
can distinguish these two situations, because they have opposite governance consequences:

| Situation | Reported as |
|---|---|
| A person is present or interacting, and no eligible known Person can be established | `unknown`, human participant **supported** |
| There is no evidence that any person is present or interacting | `unknown`, human participant **not supported** |

Identity further guarantees:

- A provider that evaluated successfully and returned no eligible match is reported as `unknown`, **never `unavailable`**
- An Unknown Person assertion carries **no** Person reference, and creates none
- No Home Assistant Person is created, named, or implied to represent an unidentified human
- An unknown evidence source is reported as evidence, and never as an identity
- Nothing durable is accumulated about an unidentified human by virtue of the observation

---

## Failure and degradation behavior

Identity **fails closed**.

| Condition | Behavior |
|---|---|
| Identity unresolved | Report `unknown`; consumers apply guest-safe treatment |
| A human participant is supported, but no known Person is eligible | Report `unknown` with the participant supported; this is a valid result, not a fault |
| A provider returned no eligible match | Report `unknown`; **never** `unavailable` |
| Two identities plausible | Report `ambiguous` with all candidates; do not silently select |
| Evidence sources disagree | Report the disagreement with attribution; reduce confidence |
| Evidence stale | Reduce confidence or withdraw the assertion |
| Dependency failure | Report `unavailable`; never degrade to a guess |

### Prohibited fusion behaviour

1. Adding provider values and configured weights together as though they were the same quantity
2. Counting correlated observations from one device as independent confirmations
3. Discarding contradicting evidence to reach a cleaner answer
4. Treating a missing optional source as evidence against a candidate
5. Using evidence for which consent is absent or withdrawn
6. Applying a universal per-device-type weight in place of the person-specific association
7. Producing a single purpose-free identity score

---

## Privacy constraints

- Consent is required, scoped, recorded, attributable, and revocable. **Identity owns the consent
  lifecycle**: capture, scope, renewal, expiry, and revocation. Foundation holds the consent record;
  Operational Trust owns consent policy and enforcement.
- Enrollment artifacts are temporary; derived profiles are durable and separately governed
- **Biometric internals — vectors, embeddings, fingerprint payloads, artifact internals, and storage
  paths — are never exposed** through services, diagnostics, logs, telemetry, or explanations, and
  are never passed to a consuming responsibility. Consumers, including Truth, receive assertions only.
- Only safe metadata is exposed: state, quality summary, confidence band, reason code
- Revocation removes the derived profile and its associations, not merely their use
- Presence history derived from identity evidence is among the most sensitive household data

See [../architecture/privacy.md](../architecture/privacy.md).

---

## Explainability contributions

Identity supplies to the Decision Trace: the candidate or candidates, the confidence, contributing
evidence classes, the reason code, and the threshold that applied.

A resident must be able to hear *"I was not certain it was you"* as a valid explanation.

---

## Open decisions

| ID | Question |
|---|---|
| OD-07 | Local versus cloud voice implementation |
| OD-08 | **Resolved** as **DL-39** and **DL-40**. Four Identity bands — Low, Moderate, High, Very High; `None` is an Operational Trust requirement; Operational Trust owns every threshold and every Required Confirmation Strength |
| OD-15 | **Closed — DL-64.** "Assertion lifetime" was a conflation of Assertion Validity (permanent), Current-Interaction Applicability (re-evaluated per interaction via fresh fusion, no fixed window), and Retention (DL-47's). Cross-purpose assertion eligibility is accepted, bounded by Room occupancy and the Person's configured primary evidence source |
| OD-16 | **Resolved** as **DL-32** and **DL-38**. Remaining coefficients are Fusion Policy configuration |
| OD-80 | **Resolved** as **DL-50**. A capability may declare an execution host; Wyoming is the preferred voice-pipeline boundary; a provider reports candidates and Identity alone resolves |
| OD-83 | Voiceprint gallery structure under channel diversity — person-global, per-channel, hybrid, or quality-only |
| OD-84 | Multi-speaker evidence and speaker plurality. **`ambiguous` is one speaker whose identity could not be separated; it is not two speakers** |

## Related documents

- [../models/person-and-identity.md](../models/person-and-identity.md)
- [truth-contract.md](truth-contract.md)
- [operational-trust-contract.md](operational-trust-contract.md)
- [../architecture/adr-identity-replaces-voice-identity-boundary.md](../architecture/adr-identity-replaces-voice-identity-boundary.md)
- [../architecture/adr-decoupled-voice-interaction-capability-architecture.md](../architecture/adr-decoupled-voice-interaction-capability-architecture.md) — Voice Identity remains independently owned regardless of which STT engine or capture device is selected (drafted, pending #198)
