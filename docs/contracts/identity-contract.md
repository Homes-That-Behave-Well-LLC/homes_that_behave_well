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
| Identity Evidence | Identity | A voice sample matched Tom's Voiceprint at Voiceprint Match Level `high` |
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
| A **complete Person-associated comparison result** — one stable `person_id` and one ordinal **Voiceprint Match Level** for **every** eligible enrolled Voiceprint, never a truncated top-N (reconciled by Phase 1, #161 — see [Voice Evidence App boundary](#voice-evidence-app-boundary--four-contracts-phase-1-161)) | A resolved Person (**DL-06**, **DL-32**) |
| Nothing further about separation or ambiguity — **Identity evaluates both** from the complete result (**DL-38 F8**) | A confidence band — bands are Identity's output (**DL-39**) |
| **Encoder family, encoder version, and audio-contract version**, reported through handshake/synchronization and bound to each result by its Voiceprint Compatibility Contract identifier (**DL-145**) | Fused confidence (**DL-32**) |
| An optional coarse **observation-quality** summary, and one result per qualified speech region where speech-region segmentation is in use (**DL-147**) | A threshold verdict — Operational Trust owns every threshold (**DL-36**) |
| `unavailable`, `incompatible`, `comparison_failed`, and `no_usable_observation` technical outcomes. *No match* is the lowest Match Level, not a separate outcome | Authorization, permission, a Trust outcome, or a Concierge outcome |
| | A raw numeric similarity or distance, an embedding, the Voiceprint artifact, or a storage path |

**Four rules bind the boundary.**

| Rule | Statement |
|---|---|
| **A provider match value is not portable** | The same similarity metric yields materially different operating points across encoders and preprocessing. A provider value is meaningful **only within its own provider**, is never compared across providers, and is never rendered to the household. The four bands are the only cross-provider currency. **For voice, the provider match value crosses the boundary only as an ordinal Voiceprint Match Level**; the App's native numeric score and the calibration that maps it to a level stay inside the App, bound to its Voiceprint Compatibility Contract |
| **A provider that evaluated and found nothing yields `unknown`** | A successful comparison in which every Voiceprint is at `no_match` is a voice-family `unknown`, never `unavailable` (**DL-33**) |
| **A non-match never suppresses transcription** | Voice comparison is enrichment. It never gates speech-to-text, and identity never travels inside transcript content |
| **Compatibility is enforced before comparison** | Encoder family, encoder version, and audio-contract version must match. A mismatch produces an explicit **DL-41** outcome — *configured but invalid* — and never a comparison made on assumption |
| **Speaker-biometric processing is HA-Prod-local only** | Enrollment audio, embedding/voiceprint generation, retained voiceprints, runtime comparison audio/embeddings, and the matching operation itself must use a currently HA-Prod-admitted resource (**DL-119**, **DL-120**); never an external/cloud provider, regardless of process, host, or network placement. The resulting assertion carries no biometric payload and is unaffected |
| **Each Person has exactly one governed Voiceprint Identity Profile (DL-144)** | Never per Room, microphone, satellite, or phone. Channel-diverse enrollment and runtime capture context are evidence provenance/quality only — never identity or authorization. Voice contributes at most one correlation-family contribution regardless of how many channels or samples informed it. Voiceprint comparison is scoped to interactions originating from voice-assistant endpoints requiring the speaker's identity from voice evidence; it is never a redundant check on an interaction already bound through another sufficient evidence source, such as Authenticated Session Identity |
| **Enrollment recordings may be retained only under explicit household policy and Person consent (DL-145)** | The source material a Voiceprint is derived from is retained only where the household's standing Integration-scoped Voice Identity Encoder Migration Policy (Option A) permits it, and only with the Person's own applicable consent — never overridden by administrator authority. Purpose is strictly limited to Voiceprint generation/regeneration; retained recordings are never reused for Home Steward, RAG, model training, or any other purpose. A Voiceprint-invalidating Voice Identity release requires a documented compelling reason under an architectural-stability preference — never introduced merely because a newer encoder exists |
| **A Person classified manual-re-enrollment-required is not identity/trust/permission-failed (DL-146)** | Voiceprint unavailability pending re-enrollment is a **DL-41** capability outcome only. Other Identity evidence, including an authenticated Companion App session, remains independently usable; transcription stays ungated. A governed Communication (**DL-142**) is sent; existing consent survives where scope/purpose are unchanged; an unidentified speaker is never told another Person's migration status |
| **One capture may yield zero, one, or multiple Voice Identity evidence records (DL-147)** | One per supportably distinguished speech region. `ambiguous` retains its **DL-38 F8** one-speech-region meaning and never represents plurality; multiple records never multiply confirmation for the same Person within one correlation family (**DL-38 F2**); an unresolved second speaker uses existing **DL-33** semantics; resolved speakers never establish audience composition (**DL-34**) |

### Voice Evidence App boundary — four contracts (Phase 1, #161)

**Accepted 2026-11-07 by Phase 1 (issue #161) contract reconciliation.** This section consumes
**DL-50** and does not reopen it. It reconciles DL-50 §11's conceptual provider contract against later
accepted authority (**DL-120**, **DL-144**, **DL-145**, **DL-146**, **DL-147**, **DL-148**) and explicit
Owner direction. It creates **no responsibility, record class, artifact class, retention rule,
threshold, or confidence representation**. These are **semantic** obligations. Transport, message
encoding, discovery mechanics, polling or listener choice, and storage paths belong to later phases
(#162–#165).

**Post-acceptance remediation (2026-11-07, Owner review).** Three bounded corrections supersede the
first acceptance's wording, which remains in git history and the #161 record:

1. Retention policy is **read by the App** from governed configuration, never pushed by HTBW.
2. Governance ownership is separated explicitly from technical storage and lifecycle execution.
3. Enrollment is **exactly ten recordings**, a governed workflow cardinality.

Everything else in this section stands as first accepted. "The App" means the **Voice Evidence Provider Runtime** (**DL-50** D4), whose released
artifact name is the **HTBW Voice Identity App**. It is a **capability component that executes for
Identity**. It is never a responsibility, never a second identity authority, and never Person
resolution. **The App produces biometric comparison evidence. HTBW produces decisions.**

> **Annotated 2026-11-10 (DL-153, DL-154; Issue #216).** The released artifact was in fact published as
> **HTBW Voice Evidence** (slug `htbw_voice_evidence`), not "HTBW Voice Identity App". Its current
> public identity is **BehavesWell Voice Evidence**, the **BehavesWell Voice Evidence App**: an
> independent, environment-neutral product that supplies governed voice-comparison evidence to
> BehavesWell Core **Identity** through the contracts below. "HTBW" in this section names BehavesWell
> Core, Home Assistant Edition. Every boundary, contract, and invariant below is unchanged. See
> [../architecture/adr-behaveswell-voice-evidence-product-identity.md](../architecture/adr-behaveswell-voice-evidence-product-identity.md).

#### Responsibility boundary

| HTBW Integration (acting for Identity) owns | The App owns, as authoritative technical store and lifecycle executor |
|---|---|
| Person Setup / Person Configuration, and the stable HTBW `person_id` | Receipt of the handed-off enrollment recordings |
| The Voice Identity consent gate (**DL-56**) | Encoder execution and the Voiceprint Compatibility Contract it implements (**DL-145** §11) |
| The enrollment UX and capture of **exactly ten** enrollment recordings, then their handoff with `person_id`. **Its responsibility for those recordings ends at successful handoff** | Voiceprint creation, and technical enforcement of one Voiceprint per `person_id` |
| Establishing the household retention policy as governed Integration configuration (**DL-145** §2, placed by **DL-148**). It does not instruct the App on any recording's disposition | Biometric Voiceprint storage, and storage of handed-off and retained recordings |
| The live voice-assistant interaction, its correlation, and the observation timestamp | Reading the governed household retention policy, and disposing of or retaining recordings after handoff accordingly |
| All contextual evidence: Room, occupancy, presence, BLE, personal devices, relationships | Voiceprint rebuild after an encoder change, where retained recordings permit |
| Identity: evidence qualification, fusion, separation, disambiguation, confidence, Person resolution, `unknown`/`ambiguous` outcomes, and correction history | Cleanup when a rebuild is impossible, and all other App-owned cleanup |
| Breaking Identity Update governance: compelling reason, classification, administrator acknowledgement, Communications (**DL-145** §13–§23, **DL-146**) | Runtime utterance encoding |
| Operational Trust handoff, and the UI presentation of enrollment availability | Comparison against the full eligible Voiceprint population, and production of ordinal Match Levels |
| | App health, version, capability, and compatibility reporting |

**Governance owner versus technical store (terminology reconciled by the #161 remediation).** When
**DL-43** and **DL-145** §27 say an artifact is "owned by **Identity**", they name its **owning
responsibility**. That is the **governance owner**, which declares the lifecycle (purpose, retention,
deletion triggers, consent effect). DL-43 adds that *"physical storage owns nothing"*.

**Identity is one of the seven responsibilities. It is not the HTBW Integration
(`custom_components/htbw`), which is a component**, as the App is (**DL-50** D4). Two roles are
therefore distinct:

- **Governance owner: Identity.** It decides what the artifact means and what lifecycle governs it.
- **Authoritative technical store and lifecycle executor: the App.** After successful handoff, the App
  stores, retains, disposes of, rebuilds, and deletes the Voiceprint, the handed-off and retained
  recordings, Voiceprint-specific derived encoder artifacts, and App-side biometric metadata. It does
  so by executing Identity's declared lifecycle and the household's governed configuration.

**The biometric Voiceprint artifact does not live in the HTBW Integration.** "Identity owns the
Voiceprint" never means `custom_components/htbw` stores it. The Integration holds no second copy, keeps
no recordings after handoff, does not decide or execute their later disposition, does not delete App
files, and does not orchestrate App-side rebuild mechanics. The App invents no retention policy,
interprets no consent, and resolves no Person.

**The App never receives contextual Identity evidence**: no Room, occupancy, presence, BLE,
personal-device, household-relationship, Operational Trust, authorization, Concierge, or interaction
history. That evidence stays inside Home Assistant under HTBW authority, where Identity fuses it.

#### Invariants

| # | Invariant | Statement |
|---|---|---|
| I1 | **One Voiceprint per Person** (**DL-144**) | `person_id` → zero or one current Voiceprint. There is never a second, primary/secondary, averaged, merged, or "best of" Voiceprint. While a Voiceprint exists, enrollment is **unavailable** for that Person. Re-enrollment requires delete first (Contract D), then established absence, then consent-gated enrollment. During migration, a validated replacement retires the obsolete Voiceprint without any dual-authority window (**DL-145** §20) |
| I2 | **The App is authoritative for existence** | Person Configuration reflects the App's synchronized report of whether a Voiceprint exists. **HTBW never concludes a Voiceprint exists merely because it remembers a successful enrollment** |
| I3 | **Consent gates capture, and never crosses** (**DL-56**) | Voice Identity consent is presented **first** in Person Setup. Without it, the enrollment workflow is unavailable, no capture begins, zero recordings exist, and nothing is sent to the App. **Receipt of a legitimate enrollment request therefore means HTBW has already satisfied consent.** The App never requests, interprets, establishes, or overrides consent, and no consent field crosses the boundary. Withdrawal makes voice evidence ineligible **immediately, inside HTBW** (**DL-38** stage 1), and triggers Contract D |
| I4 | **Evidence, never decisions** | The App never returns final Person resolution, Identity confidence, fused confidence, an Identity Confidence Band, a separation verdict, a Trust result, permission, authorization, or a Concierge outcome |
| I5 | **No biometric internals cross** | Recordings cross **once, inbound**, at enrollment handoff. A runtime voice sample crosses **once, inbound**, per comparison. Voiceprints, embeddings, encoded observations, raw provider scores, and storage paths **never** cross (**DL-43**, **DL-120**, `privacy.md`) |
| I6 | **HA-Prod-local** (**DL-120**) | The App, its Voiceprints, any retained recordings, and every comparison execute only on an HA-Prod-admitted resource |
| I7 | **No biometric artifact in the Integration** | The Voiceprint, handed-off recordings, retained recordings, and derived encoder artifacts are stored only by the App. The Integration holds only the Voice Profile and the synchronized state from Contract A |
| I8 | **Ten-recording enrollment cardinality** | Contract B hands off **exactly ten** successfully captured recordings. That is the governed workflow cardinality of the current HTBW Voice Enrollment experience. **It is not a biometric sufficiency threshold, encoder calibration constant, quality threshold, or provider requirement.** Sufficiency and calibration remain provider/implementation mapping, and **DL-36** is unaffected. The App neither selects nor advertises the count |

#### Contract A — Handshake and synchronization

**Purpose.** Establish whether the Integration and the App can currently work together correctly, and
synchronize App-held Voiceprint state into Person Configuration. **This is operational, capability, and
lifecycle state. It is never Identity evidence.**

**When.** At Integration startup, after App reconnection or recovery, and whenever either side reports
a change to synchronized state. **HTBW decides Person Configuration availability only after
synchronization.** The mechanism (request, push, or poll) is Phase 2's to choose.

| Direction | Conceptual content |
|---|---|
| App → HTBW | `contract_version`; `app_version`; `status` and `reason_code` (available, unavailable, or incompatible, naming the cause); the **Voiceprint Compatibility Contract** identity `compatibility_id`, with `encoder_family`, `encoder_version`, and `audio_contract_version` (**DL-50** §16, **DL-145** §11); `optional_capabilities`; and **one entry per `person_id` for which the App holds any enrollment state**: `voiceprint_exists`, `voiceprint_state` (`current` or `incompatible`), and `retained_recordings` (present or absent). **While a Breaking Identity Update is pending or in progress, it also reports** the target `compatibility_id`; per `person_id`, a `rebuild_assessment` (`possible` or `not_possible`, with a reason category) — whether retained recordings exist and satisfy the target encoder (**DL-145** §12, §17); and, once migration runs, a per-Person `migration_outcome` (`regenerated` or `removed`, with a reason category such as no retained recordings, reuse not permitted, insufficient for the target, or validation failed) |
| HTBW → App | `contract_version`. **Once the administrator has acknowledged a Breaking Identity Update**, HTBW also sends a single **`migration_authorization`** for the target `compatibility_id`. This is the household-level governance gate of **DL-145** §12 and §19 — an authorization, not lifecycle policy, and never a sequence of per-Person instructions |

**What Contract A never carries.** Contract A is not a general configuration-synchronization protocol.
It never carries the household retention policy, a per-Person retention disposition, a per-enrollment
retention choice, or consent state. **The App reads the household's governed retention configuration
itself** (**DL-145** §2), at the point where it decides what happens to recordings it owns. HTBW
governance *establishes* that policy in Integration configuration (**DL-148**); the App *executes* it.
**Mechanism (Owner decision, #162):** on a Supervisor-managed install, the HTBW household entry
mirrors that one value into the App's **own official app options** through Home Assistant's
app-options helper. That is configuration synchronization, not an artifact-disposition command and not
part of Contracts A–D. The App reads its own options, which needs no Home Assistant or Supervisor
administrator authority, and owns every resulting decision. The App's option is an operational mirror,
never a second household authority. The App may *report* the value it is applying in Contract A
status, so HTBW can detect divergence and re-mirror; it is never pushed through Contract A. The App
never receives the retention value in any Contract A–D field, and never as an Integration-issued
disposition instruction. **The App
never advertises or changes the enrollment count**, because enrollment cardinality is governed by HTBW
(I8). The audio input format DL-145 §12 calls "enrollment-evidence requirements" is expressed by
`audio_contract_version`.

**Rules.**

- **Absence is authoritative.** A `person_id` the App does not report has no Voiceprint. If HTBW
  remembers an enrollment the App does not report, Person Configuration shows **Not Enrolled** and
  recalculates enrollment availability, subject to consent.
- **An unreachable App is a DL-41 outcome, not an absence.** While the App is unavailable, Voiceprint
  existence is unknown. Voice evidence is `unavailable`, and enrollment is unavailable because its
  dependency is missing. **HTBW never infers "not enrolled" from an unreachable App**, and never
  emulates it.
- **Versions.** If the two sides do not share a `contract_version` major version, the result is
  `incompatible` under **DL-41**, and the household is told which dependency to act on (Contract
  versioning, below).
- **Optional capabilities are DL-41 optional dependencies.** Harvested Patterns 5, 6, and 8 (speech-region
  segmentation, rejection telemetry, passive capture), together with any other capability **DL-50**
  §31 names as optional, are declared in `optional_capabilities`. **A missing optional capability
  never makes the App unavailable.** It reduces optional functionality or quality only. **A missing
  required capability makes the App unavailable or incompatible as governed.** Declaring a capability
  never authorizes it: speaker-conditioned extraction remains validation-gated (**DL-50** §24), and
  passive capture remains a North Star (**DL-50** §25). **There is no provider registry or plug-in
  framework** (**DL-41**, **DL-30**).

#### Contract B — Enrollment

**Preconditions, all held by HTBW.**

- Voice Identity consent has been granted in Person Setup (I3).
- The household retention policy has been established (**DL-145** §2).
- Contract A is synchronized and the App is available.
- **The App reports no Voiceprint for this `person_id`** (I1).
- **Exactly ten enrollment recordings have been successfully captured** (I8).

**HTBW responsibility.** Run the enrollment experience, capture **exactly ten** recordings, associate
them with the stable `person_id`, and hand them off. Partial enrollment, a provider-selected or
App-requested count, and a dynamically inferred count are prohibited until later accepted architecture
changes this. **Capture provenance** — channel, endpoint, microphone, Room, and capture distance
(**DL-144**, Pattern 4) — **is recorded in HTBW's Voice Profile and does not cross.**

| Direction | Conceptual content |
|---|---|
| HTBW → App | `person_id`; `recordings[10]` |
| App → HTBW | `person_id`; `outcome` (`created` or `enrollment_failed`); `reason_code` on failure, as a category such as insufficient quality, invalid recording count, unsupported audio, Voiceprint already exists, or App unavailable |

**Never sent:** a consent flag; the retention choice or any retention disposition; Room, channel,
presence, BLE, or other evidence; Identity confidence; a provider threshold; a display name as identity
authority; the existing Voiceprint population; or any authorization result beyond the governed
workflow having been allowed to occur.

**Consent and retention at handoff.** A valid ten-recording handoff is sufficient evidence to the App
that the HTBW-side consent prerequisite was satisfied. The Person's Voice Identity consent at the gate
already discloses the household's retention behaviour (Person Setup, **DL-56**), so the Person's
applicable consent under **DL-145** §3 is established **before** handoff. Narrowing or withdrawing that
consent is Voice Identity withdrawal under **DL-56**, and it triggers Contract D. A distinct
retention-only consent control is **not** introduced here; if one is ever proposed, it requires its
own governance.

**After successful handoff, the Integration's responsibility for the recordings ends.** HTBW keeps no
copy (**DL-43**) and manages none of their later disposition. The App, as authoritative technical
store and lifecycle executor:

1. validates the recordings. A set other than ten, or one that fails technical validation, yields
   `enrollment_failed`. Biometric sufficiency and quality judgement are the App's own implementation
   mapping, never a count it selects;
2. encodes them and creates the Person's **one** Voiceprint, associated with the supplied `person_id`;
3. **reads the household's governed retention configuration** and acts on it. Under **Option A**,
   after successful Voiceprint creation and validation, it retains the ten recordings in the governed
   retained-recording location (**DL-145** §6/§27; physical placement is **#207**) and owns their
   future rebuild use. Under **Option B**, it disposes of them (**DL-43**). On `enrollment_failed`, it
   always disposes of them, because retention requires a successfully completed and validated
   enrollment (**DL-145** §27, row 4);
4. reports the outcome. After `created`, HTBW reflects `voiceprint_exists = true`, and enrollment
   becomes unavailable.

Retained recordings serve **only** Voiceprint generation and regeneration (**DL-145** §5). They are
never an audio archive, Person-history audio, training data, Concierge material, or household
reasoning material.

#### Contract C — Runtime comparison

| Direction | Conceptual content |
|---|---|
| HTBW → App | `request_id`; `observed_at`; `voice_sample` |
| App → HTBW | `request_id`; `compatibility_id`; one or more `results`. Each result carries an optional `region` (present only when speech-region segmentation is in use, **DL-147**), an optional `observation_quality` (`adequate` or `degraded`), and `matches` — **one `{person_id, match_level}` entry for every eligible enrolled Voiceprint**. Alternatively, the App returns one technical outcome: `unavailable`, `incompatible`, `comparison_failed`, or `no_usable_observation` |

- **`request_id`** is opaque and minted by HTBW. It pairs a response with its request and carries **no**
  conversation, device, Room, satellite, or pipeline meaning. Evidence therefore remains **unbound**,
  and binding stays in HTBW (**DL-50** §15). Where a later-phase audio seam (#165) cannot carry it,
  §15's binding rules apply unchanged, and recency-only matching remains prohibited.
- **`observed_at`** is when the voice observation was made. It is never when the App started or
  finished processing, or when HTBW received the response. HTBW holds it authoritatively in its
  interaction record and supplies it once. **No other timestamp is invented**, and there is **no
  provider expiry**, because freshness belongs to Identity (**DL-38**).
- **The Voiceprint population is never sent.** The App already holds it. HTBW also never sends a Person
  roster, Room, occupancy, presence, BLE, Identity confidence, Trust, authorization, or Concierge
  context.

**App runtime work.** Receive the sample, encode it with the configured encoder, and compare the
encoded observation against **every eligible enrolled Voiceprint** — every `current` Voiceprint under
the active Voiceprint Compatibility Contract. Incompatible Voiceprints are excluded before comparison
(**DL-50** §16), and Contract A already reports them. Assign each comparison an ordinal Match Level,
and return the **complete** set.

- **No early termination.** The App does not stop after the first strong or Very High match.
  Vectorized, matrix, accelerated, or indexed comparison is permitted later, but **may never omit
  potentially competing evidence**.
- **No top-N truncation.** **DL-50** Pattern 3's purpose — candidate sets rather than a single winner,
  so that Identity can evaluate separation — is met by the complete result, which is its superset.
- **Multiple `very_high` results are valid evidence.** A well-discriminated population ordinarily yields
  at most one, but that is an expectation, not a guarantee. **All are returned.** None is selected,
  demoted, suppressed, or ranked as the winner by comparison order, and **Identity disambiguates**
  using governed evidence the App never sees.
- **Person association is metadata, not resolution.** `{person_id, match_level}` means *"the Voiceprint
  HTBW enrolled for this `person_id` produced this technical Match Level"*. It never means the App
  resolved the speaker. Display names are never stable identity.
- **Malformed means rejected** (**DL-50** §21). If a result omits a synchronized eligible `person_id`,
  or its `compatibility_id` does not match the synchronized state, HTBW rejects it and
  resynchronizes through Contract A. A partial result is never consumed.
- When Contract A reports no `current` Voiceprint, HTBW does not request a comparison. If one is
  requested anyway, the App returns `unavailable`, naming the missing enrollment (**DL-50** §18).

**Voiceprint Match Level.** This is the voice provider's **Provider Match Value**, expressed on one
governed ordinal scale: `no_match` < `low` < `moderate` < `high` < `very_high`.

- **The App alone translates** its native similarity or distance into a level. Calibration is
  provider-specific, bound to the Voiceprint Compatibility Contract, and is **implementation mapping,
  not architecture**: no calibration value is canonical or validated (**OD-16**).
- **It is not a confidence band, not Identity confidence, not a probability, and not a threshold
  verdict.** Its labels share words with the **DL-39** bands, but it is never one. **Identity never
  copies a Match Level into a band.**
- Identity applies it at **DL-38** qualification stage 3, *provider match value*, where it may only
  lower or hold. The mapping is **Fusion Policy** configuration. **DL-32** holds: the Match Level is
  retained as reported and never rewritten as fused confidence.
- Identity evaluates separation and ambiguity (**DL-38 F8**) from the complete result. Two or more
  candidates at the leading level never satisfy separation from voice alone.
- It is never rendered to the household as a number or percentage.

#### Contract D — Delete and enrollment cleanup

| Direction | Conceptual content |
|---|---|
| HTBW → App | `person_id` — delete enrollment |
| App → HTBW | `person_id`; `outcome` (`deleted` or `delete_failed`); `reason_code` on failure |

**HTBW triggers:** a voluntary re-enrollment, Voice Identity consent withdrawal (**DL-56**), voice-profile
removal, Person deletion, or an erasure request (**DL-136**).

**The App performs complete cleanup of App-owned enrollment state for that Person.** That means the
current Voiceprint, any retained enrollment recordings, derived encoder artifacts that exist solely for
that Voiceprint, and App-owned technical enrollment metadata. **HTBW needs no App file paths or deletion
mechanics.** Deleting an absent enrollment succeeds, because the operation is idempotent.

**After `deleted`,** the App reports no Voiceprint for the `person_id`. HTBW reflects
`voiceprint_exists = false`, and enrollment may become available again, subject to consent. **Enrollment
never becomes available before absence is established**, either by this acknowledgement or by Contract
A synchronization.

**On `delete_failed` or an unreachable App,** HTBW keeps voice evidence ineligible wherever consent was
withdrawn (I3), reconciles at the next synchronization, and never reports deletion as complete
(**DL-41**). The consent-lifecycle facts that survive deletion are HTBW's **DL-47** structural floor,
never App state.

**A retention-only change is not Contract D.** When the household policy moves from A to B, the App
reads the changed governed configuration itself and disposes of retained recordings (**DL-145** §8).
No Integration instruction is involved, and Voiceprints are unaffected. A change from B to A is
prospective only (**DL-145** §9).

#### Encoder and provider migration

**A change of encoder, model, preprocessing, audio contract, or provider that breaks the Voiceprint
Compatibility Contract is a Breaking Identity Update, never an ordinary configuration change**
(**DL-50** §16, **DL-145** §13). **Substituting one provider for another is the same event with a wider
blast radius**: every Voiceprint becomes incompatible at once.

- **HTBW governs** (**DL-145** §14–§23, **DL-146**). It applies the compelling-reason gate. **Before
  committing**, it classifies each Person from Contract A state (`voiceprint_state`,
  `retained_recordings`, and the App's `rebuild_assessment` against the target `compatibility_id`). It
  obtains administrator acknowledgement at the update lifecycle event (**DL-148**), then sends the
  single `migration_authorization`. It also sends governed Communications and records migration
  completion. **It never sends recordings back to the App and never orchestrates per-Person rebuild
  steps.**
- **The App performs the mechanics** once it receives `migration_authorization` and the new
  compatibility boundary commits. For each incompatible Voiceprint:
  - **If retained recordings exist, the governed household policy permits reuse (Option A), and they
    satisfy the target encoder,** the App reads the recordings it holds, rebuilds the Voiceprint, validates it, and replaces the obsolete one. There is
    never more than one active Voiceprint. It reports `migration_outcome = regenerated` and
    `voiceprint_state = current`.
  - **Otherwise, or if the rebuild or validation fails,** the App deletes the incompatible Voiceprint
    and its unusable enrollment artifacts. It reports `migration_outcome = removed`, with the reason,
    and reports that no Voiceprint exists.
- HTBW reflects the synchronized result. Where a Voiceprint is now absent, re-enrollment becomes
  available subject to consent, and the **DL-146** manual-re-enrollment path applies. **HTBW does not
  orchestrate App-side rebuild steps.**
- **Still-valid Voiceprints are never destroyed before the new boundary commits** (**DL-145** §20). An
  incompatible Voiceprint is **never compared and never presented as usable enrollment**.

#### Restore-time compatibility re-validation (accepted 2026-11-09, Issue #209, formal governance acceptance PASS)

**Storage recovery is never treated as equivalent to a live, authorized migration.** After App
reinstall, storage reconnect, or a Home Assistant/App restore, the App re-establishes Voiceprint state
from first principles rather than trusting a stale in-memory or Integration-side assumption:

1. rediscover and reconnect the authoritative storage;
2. read candidate Voiceprint metadata;
3. validate artifact integrity;
4. validate the Person relationship where applicable;
5. validate `compatibility_id` against the currently active encoder identity;
6. validate `encoder_family`/`encoder_version`;
7. validate `audio_contract_version` compatibility;
8. validate lifecycle state (`current` vs. `incompatible`);
9. reject, or mark `incompatible`, any Voiceprint that cannot safely become `current`;
10. **never silently resurrect an obsolete, pre-migration, or otherwise incompatible Voiceprint as
    `current` merely because its file exists after a restore.**

This extends **DL-144**'s existing "never more than one active governed Voiceprint per Person" and
**DL-41**'s existing failure/degradation semantics to the restore case specifically, which neither
decision previously addressed in those terms. It reopens neither. Implementation and tests for this
sequence are governed separately (Issue #212); this contract fixes the required sequence, not its
code.

#### Contract versioning

**The contract is versioned as a whole (A–D), never field by field.** `contract_version` is
`major.minor`:

- A **major** difference means incompatible semantics. Neither side guesses, and the result is
  `incompatible` under **DL-41**.
- A **minor** increment adds optional content only. An unrecognized optional field or capability is
  ignored, never treated as an error.

The initial version is **1.0**. Three versions are deliberately distinct and are never conflated: the
`contract_version`, the App's `app_version`, and the Voiceprint Compatibility Contract
`compatibility_id`. Coupling the contract to one encoder or provider implementation is prohibited
(**DL-50** Pattern 7).

#### Field vocabulary

Names are reconciled against the existing implementation record (**DL-50** §11), but **an
exploratory or superseded implementation never overrides this contract**. The "Governance owner /
technical store" column follows the terminology reconciliation under **Responsibility boundary**.

| Field | Meaning | Governance owner / technical store | Required | Contract | Why it crosses | Implementation analogue | Compatibility concern |
|---|---|---|---|---|---|---|---|
| `contract_version` | Semantic contract version | Both sides | Required | A | Compatibility before any use | App `api_version` | Renamed: it versions the semantic contract, not an HTTP API |
| `app_version` | Runtime/component version | App | Required | A | **DL-145** §12 Explainability and diagnostics | — | None |
| `status`, `reason_code` | Availability and its named cause | App | Required | A, and every response | **DL-41** names the missing dependency | App health `status` / `reason_code` | Values constrained to available / unavailable / incompatible |
| `compatibility_id` | Voiceprint Compatibility Contract identity | App | Required | A; echoed in C | Binds evidence to encoder identity without repeating it per result (**DL-50** §16) | — (new; **DL-145** §11) | Mismatch triggers resynchronization |
| `encoder_family`, `encoder_version`, `audio_contract_version` | Encoder identity | App | Required | A | **DL-50** §16; recorded on the HTBW evidence record from synchronized state | Same names (`artifact_persistence.py`, App health) | Preserved unchanged |
| `optional_capabilities` | Declared optional features | App | Required (may be empty) | A | Avoids assumed or refused capabilities (**DL-41**) | — | Additive by minor version |
| `person_id` | Stable HTBW Person reference | HTBW | Required | A, B, C, D | The only association key; display names are never identity | `person_id` (`contracts.py`, `attribution_models.py`) | `voice_profile_id` / `profile_id` / `voiceprint_id` are **not** adopted, because one Voiceprint per Person makes them redundant at this boundary |
| `voiceprint_exists` | Whether the App holds a Voiceprint | App (authoritative) | Required | A, D | Drives Person Configuration (I2) | — | None |
| `voiceprint_state` | `current` or `incompatible` | App | Required when the Voiceprint exists | A | Migration classification (**DL-145** §17) | `compatibility_readiness` | None |
| `retained_recordings` | Whether retained recordings are present | App | Required | A | Migration classification and Explainability (**DL-145** §17, §26) | — | Presence only; content never crosses |
| `rebuild_assessment` | Whether retained recordings exist and satisfy a pending target encoder | App | Required while a Breaking Identity Update is pending | A | Pre-migration classification (**DL-145** §12, §17) | — | Reason category only; no biometric detail |
| `migration_authorization` | Household-level authorization to apply a Breaking Identity Update for a target `compatibility_id` | HTBW | Required to start migration | A (HTBW → App) | **DL-145** §12 regeneration request, issued after §19 acknowledgement | — | Never per-Person orchestration |
| `migration_outcome` | Per-Person migration result: `regenerated` or `removed` | App | Required after migration | A | **DL-145** §17, §20; **DL-146** | — | Reason category only |
| `recordings[10]` | The ten-recording enrollment set | Identity / App after handoff | Required, exactly ten | B | Voiceprint creation | Enrollment samples (`TARGET = 10`) | Fixed workflow cardinality (I8); not a sufficiency or calibration value; inbound once |
| `outcome` | Technical result of B, C, or D | App | Required | B, C, D | The lifecycle result | — | Never Person resolution |
| `request_id` | Opaque request correlation token | HTBW | Required | C | Pairs a response with its request | — | Never `conversation_id`, `device_id`, `room_id`, `satellite_id`, or `pipeline_id` (**DL-50** §15) |
| `observed_at` | When the observation was made | HTBW | Required | C (request) | Identity correlates it with contemporaneous evidence | — | Not echoed; HTBW holds it |
| `voice_sample` | Utterance audio | Identity / App (transient) | Required | C | The thing being compared | Assist audio stream | Inbound once; never retained by default (**DL-43**) |
| `region` | Speech-region index | App | Optional | C | **DL-147** per-region evidence | — | Present only when segmentation is in use |
| `observation_quality` | Coarse quality summary | App | Optional | C | **DL-38 F3** stage 4; "quality summary" is safe metadata | — | Absence holds rather than lowers |
| `matches[].match_level` | Ordinal Voiceprint Match Level | App | Required | C | The minimum evidence Identity needs | `ComparisonResult.known_matches` (internal list) | Replaces numeric `confidence`, `ConfidenceBand`, `best_match` / `second_best_match`, `is_ambiguous`, and `is_confident`. Each is retired at this boundary |

**Draft properties challenged and moved, not lost:**

- `evidence_id` is minted by HTBW when it records the Voice Evidence Record.
- Provider identity and version move to Contract A.
- Source device and Room are HTBW's own interaction context.
- Expiry is removed, because freshness is Identity's.
- Speech-region detail, audio-quality detail, processing metadata, and warnings stay in **App
  operational diagnostics**. Phase 2 must declare their lifecycle before they persist (**DL-43**).
- Winner/runner-up separation, ambiguity indicators, and top-N ordering are evaluated by Identity from
  the complete result.
- `no-match` becomes the lowest Match Level, not a duplicate outcome.

#### Retention and artifact mapping

**No new artifact class is created.** Every artifact maps to an existing **DL-43**, **DL-47**, or
**DL-145** declaration. **Governance owner** is the DL-43/DL-145 "owning responsibility". It is
distinct from the component that stores the artifact and executes its lifecycle.

| Artifact | Governance owner (DL-43/DL-145) | Authoritative technical store | Lifecycle executor | Retention authority | Deletion executor | Integration stores a copy? | App stores a copy? |
|---|---|---|---|---|---|---|---|
| Enrollment recording **before** handoff | Identity (**DL-43** voice enrollment samples) | HTBW Integration, transiently during capture | HTBW Integration | **DL-43**: temporary, zero default retention | HTBW Integration — on successful handoff, cancellation, or failure | Transiently, only until handoff | No |
| Enrollment recording **after** handoff | Identity (**DL-43**) | App | App | Household governed retention configuration (**DL-145** §2), read by the App; **DL-43** default | App — after Voiceprint creation and validation (Option B) or on failure | **No** | Yes, until disposition |
| Retained enrollment recordings | Identity (**DL-145** §27) | App, in the **DL-145** §6 governed namespace (physical placement **#207**; **DL-120**) | App, including future rebuild use | **DL-145**: Option A household policy, plus the Person's consent established at the gate | App — on A→B (read from configuration), Contract D, or migration removal | **No** | Yes |
| Voiceprint artifact | Identity (**DL-43** voiceprints and derived profiles) | App | App: creation, rebuild, removal | **DL-43**: while the profile is enabled and consent is valid | App — on Contract D, or when incompatible and not rebuildable | **No** (I7) | Yes, the only copy |
| App-specific derived biometric artifacts and App-side biometric metadata | Identity (**DL-43**, with its Voiceprint) | App | App | With its Voiceprint | App, with its Voiceprint | **No** | Yes |
| Runtime voice sample / encoded observation (Speaker Embedding) | Voice Evidence Provider Runtime temporary processing artifact (**DL-43**) | App, transiently | App | **DL-43**: transient | App, at end of comparison | No | Transiently |
| Integration-side Voice Profile and synchronized projection (existence, compatibility, Contract A state) | Identity (**DL-43** profile; **DL-47** Current Projection; **DL-56** consent floor) | HTBW Integration | HTBW Integration | **DL-43** / **DL-47** | HTBW Integration — profile removal; projection replaced by synchronization | Yes — metadata only, never biometric | No |
| Comparison result, recorded as the Voice Evidence Record | Identity (**DL-47**) | HTBW Integration | HTBW Integration | **DL-47**: with the Decision Trace or governed history it supports | HTBW Integration | Yes — safe metadata only | No |

**HTBW capturing a recording does not make HTBW its lifecycle executor after successful handoff.**
The App applies the declared lifecycle on Identity's behalf.

#### What Phase 2 and later consume

**#162 onward consume this section rather than rediscovering it.** That covers the four contracts and
their field vocabulary, the responsibility split, the consent boundary, the Voiceprint lifecycle,
handshake and synchronization semantics, comparison semantics, and retention and migration
requirements. **Corrected by the #161 post-acceptance remediation (2026-11-07):**

- HTBW never pushes retention policy or disposition; the App reads the governed configuration itself.
- The Integration stores no biometric artifact (I7).
- Enrollment is exactly ten recordings (I8).

Transport (HTTP, Wyoming, or another), authentication mechanics, the mechanism by which the App reads
governed configuration, encoder selection, Match Level calibration, and storage placement remain #162's
and later phases' to decide, within these semantics.

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
| OD-07 | **Resolved as DL-120.** Speaker-biometric Identity processing (voiceprint/embedding generation, runtime comparison) is Home Production (HA-Prod)-local only (**DL-119**); STT/TTS follow their own general residency framework, reusing **DL-93**'s precedent; Reasoning remains **DL-93**'s own |
| OD-08 | **Resolved** as **DL-39** and **DL-40**. Four Identity bands — Low, Moderate, High, Very High; `None` is an Operational Trust requirement; Operational Trust owns every threshold and every Required Confirmation Strength |
| OD-15 | **Closed — DL-64.** "Assertion lifetime" was a conflation of Assertion Validity (permanent), Current-Interaction Applicability (re-evaluated per interaction via fresh fusion, no fixed window), and Retention (DL-47's). Cross-purpose assertion eligibility is accepted, bounded by Room occupancy and the Person's configured primary evidence source |
| OD-16 | **Resolved** as **DL-32** and **DL-38**. Remaining coefficients are Fusion Policy configuration |
| OD-80 | **Resolved** as **DL-50**. A capability may declare an execution host; Wyoming is the preferred voice-pipeline boundary; a provider reports candidates and Identity alone resolves |
| OD-83 | **Closed — DL-144.** Voiceprint gallery structure under channel diversity — Alternative D accepted: each Person has exactly one governed Voiceprint Identity Profile; channel is evidence provenance/quality context only, never identity or authorization; no per-channel, per-Room, per-microphone, or per-phone governed voiceprint; voice contributes at most one correlation-family contribution (**DL-38 F2**) regardless of channel diversity; no aggregation mathematics, sample count, or threshold decided (**OD-16** not reopened) |
| OD-96 | **Closed — DL-145.** Voice Identity Enrollment Evidence Retention, Voiceprint Regeneration, and Breaking Encoder Compatibility Governance — enrollment recordings retained only under explicit household Integration policy (Option A/B, chosen before enrollment, persisting across updates) and applicable Person consent, for Voiceprint generation/regeneration only; a Voiceprint Compatibility Contract (not a bare encoder version) determines whether a Breaking Identity Update applies; a compelling-reason gate/stability preference bounds any Voiceprint-invalidating release; per-Person pre-migration classification (auto-regenerated / manual-re-enrollment-required / unaffected); **DL-144** preserved throughout migration, no dual-authority window |
| OD-87 | **Closed — DL-146.** Identity Artifact Invalidation as a Governed Household Event — applies only to Persons **DL-145** classifies manual-re-enrollment-required; Voiceprint unavailability is a **DL-41** outcome only, never identity/trust/permission failure; other evidence and an authenticated Companion App session remain usable, transcription stays ungated; governed Communication (**DL-142**, Category System); consent survives where scope/purpose unchanged; per-Person/household completion defined; separate from adoption, **OD-93** owns surface placement |
| OD-84 | **Closed — DL-147.** Multi-Speaker Evidence and Speaker Plurality — Alternative B accepted: one capture may yield zero, one, or multiple Voice Identity evidence records, one per supportably distinguished speech region; `ambiguous` unchanged (**DL-38 F8**, one speech region only); **DL-38 F2** prevents multiple records from multiplying confirmation for the same Person; unresolved second speaker uses existing **DL-33** semantics; resolved speakers never establish audience composition (**DL-34**); overlap represented as plurality only where technically supportable; confidently-wrong-attribution correction excluded from scope (**#173** evidence only); **OD-16** not reopened |

## Related documents

- [../models/person-and-identity.md](../models/person-and-identity.md)
- [truth-contract.md](truth-contract.md)
- [operational-trust-contract.md](operational-trust-contract.md)
- [../architecture/adr-identity-replaces-voice-identity-boundary.md](../architecture/adr-identity-replaces-voice-identity-boundary.md)
- [../architecture/adr-decoupled-voice-interaction-capability-architecture.md](../architecture/adr-decoupled-voice-interaction-capability-architecture.md) — Voice Identity remains independently owned regardless of which STT engine or capture device is selected (**DL-91**, accepted)
- [../architecture/adr-wyoming-compatible-voice-evidence-runtime.md](../architecture/adr-wyoming-compatible-voice-evidence-runtime.md)
  (**DL-50**)
- [../architecture/adr-voiceprint-gallery-structure-under-channel-diversity.md](../architecture/adr-voiceprint-gallery-structure-under-channel-diversity.md)
  (**DL-144**)
- [../architecture/adr-voice-identity-enrollment-evidence-retention-and-regeneration.md](../architecture/adr-voice-identity-enrollment-evidence-retention-and-regeneration.md)
  (**DL-145**)
- [../architecture/adr-identity-artifact-invalidation-as-a-governed-household-event.md](../architecture/adr-identity-artifact-invalidation-as-a-governed-household-event.md)
  (**DL-146**)
- [../architecture/adr-multi-speaker-evidence-and-speaker-plurality.md](../architecture/adr-multi-speaker-evidence-and-speaker-plurality.md)
  (**DL-147**)
