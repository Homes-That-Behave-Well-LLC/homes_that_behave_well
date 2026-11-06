# ADR: Multi-Speaker Evidence and Speaker Plurality

> **Document status: Canonical ADR.**
> Status: **Accepted** 2026-11-06. Records **DL-147** (issue **#169**, formal acceptance review PASS).
> Resolves **OD-84** in full.
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Terminology: [../models/glossary.md](../models/glossary.md),
> [../models/person-and-identity.md](../models/person-and-identity.md),
> [adr-wyoming-compatible-voice-evidence-runtime.md](adr-wyoming-compatible-voice-evidence-runtime.md) §13, §17, §28.

---

## 1. Status

**Accepted 2026-11-06.** Resolves every OD-84 acceptance criterion in full. This ADR creates **no new
responsibility**, **no new Identity state**, **no new record class**, **no new confidence
representation**, **no new dependency class**, and decides **no threshold, margin, count, or quality
value**. It does not reopen **DL-15**, **DL-32**, **DL-33**, **DL-34**, **DL-35**, **DL-36**, **DL-37**,
**DL-38** (F1–F9), **DL-39**, **DL-41**, **DL-50**, **DL-69**, **DL-72**, **DL-90**, **DL-104**,
**DL-120**, amended **DL-137**, **DL-140**, or **DL-144** — each is consumed unchanged. **OD-16 is not
reopened.**

---

## 2. Context

**OD-84 is a defect, not merely a gap.** **DL-38 F8** yields `ambiguous` when the leading candidate
fails the governed separation requirement, and **`ambiguous` means one speaker whose identity could
not be separated between candidates**. **Two people speaking produces the same observable shape** —
several candidates scoring closely — **from the opposite cause**. Uncertainty about one voice and
plurality of voices are therefore currently indistinguishable at exactly the point where the
distinction matters most, and an implementation that reports plurality as `ambiguous` would conform to
the letter of **DL-38** while asserting something false.

**Episode 8 use-case evidence** (`concierge-use-cases.md` **C2**, **C16**) shows this is a
household-experience defect, not only an evidence-shape defect: *"I was not certain it was you"* and
*"I could not account for everyone in the room"* are different, both true, and today only the first is
expressible.

**Episode 10 Governance Harvest** separately surfaced a third, unrelated cause with the same
observable shape as neither of the above — a single speaker **confidently attributed to the wrong
Person**. That case is explicitly out of scope here; see §32.

---

## 3. Decision — Alternative B selected

**A voice capture may yield zero, one, or multiple Voice Identity evidence records, one per
supportably distinguished speaker region.**

Rejected alternatives are recorded in §§17–19. The decision does **not** redefine `ambiguous`, does
**not** reopen **DL-38**, **DL-34**, **DL-33**, or **OD-16**, and does **not** decide any numeric
threshold, margin, speaker-count cap, or segmentation parameter — those remain Fusion Policy and
implementation/Voice Identity App configuration, exactly as today.

---

## 4. Capture, speech region, and evidence record are three distinct concepts

A **capture** (or interaction) is the audio acquisition context — the input/container. It is not
itself an Identity assertion and carries no Person semantics merely because it may contain voice
audio.

**Speech region** is the existing canonical term — already accepted in **DL-50** and
[adr-wyoming-compatible-voice-evidence-runtime.md](adr-wyoming-compatible-voice-evidence-runtime.md)
§13 ("Detect speech regions, evaluate each separately, generate evidence from relevant regions") — for
a portion of captured audio the Voice Identity runtime has sufficient technical basis to treat as
belonging to one detected speaker, for the purpose of producing a Voice Identity evidence observation.
**No new term is coined.** Speech-region segmentation remains, unchanged, an **App capability** adopted
for controlled experimentation, and **region-level matching is a provider capability and never an
Identity decision** (**DL-50**).

A **Voice Identity evidence record** (the existing **unbound Voice Evidence Record**, **DL-50**)
remains the governed evidence artifact. It is produced from a qualified speech region, not from the
capture as a whole.

| Concept | What it is | Who produces it |
|---|---|---|
| Capture | Audio acquisition context/container | Voice satellite / Assist pipeline |
| Speech region | A segment of the capture supportably attributable to one speaker | Voice Identity App (provider), §13 |
| Voice Identity evidence record | Governed, unbound evidence for one qualified speech region | Voice Identity App (provider), consumed by Identity |

A capture may contain no usable speech, one speech region, several sequential speech regions, several
overlapping speakers, noise, or speech that cannot supportably be segmented. None of these states
places Person-identity semantics on the capture itself.

---

## 5. Evidence-record cardinality

**One capture may produce zero, one, or multiple Voice Identity evidence records:**

| Capture content | Evidence records produced |
|---|---|
| No speech region is supportably usable | **Zero** |
| One speech region is supportably usable | **One** |
| Multiple distinct speech regions are supportably distinguished and individually qualified | **Multiple** |

**Qualification remains governed** (**DL-50**, **DL-38**). Not every detected acoustic region becomes
Identity evidence — only a region the runtime has sufficient technical basis to treat as one speaker.
**One physical audio capture is never defined as equal to one Voice Identity evidence record.** The
capture is the input; speech regions are observations derived from it.

---

## 6. Each evidence record represents one speech region

Each resulting Voice Identity evidence record refers to **one** qualified speech region, and is
independently processed through the existing **Identity Fusion Function** (**DL-38**) to one of its
existing outcomes: `known` (with a confidence band, **DL-39**), `ambiguous`, `unknown` (with
`human_participant` support, **DL-33**), or `unavailable` (**DL-41**). **No outcome enumeration is
added.** Several simultaneous speaker identities are never merged into one ordinary Identity evidence
record merely to avoid producing multiple records.

---

## 7. `ambiguous` is unchanged — DL-38 F8

**NON-NEGOTIABLE. `ambiguous` is not redefined.**

`ambiguous` retains its exact **DL-38 F8** meaning: **one** speech region was evaluated, but the
leading candidate could not satisfy the governed separation requirement relative to competing
candidates (*"Tom and David candidates insufficiently separated"*). It does **not** mean two people
spoke, it does **not** mean multiple speakers were detected, and it does **not** mean audience
plurality. Where two or more candidates are plausible for the **same** speech region, all are reported
as `ambiguous`, exactly as today.

---

## 8. Plurality is a different observation

**Plurality** exists when the Voice Identity runtime can supportably establish that the capture
contains **more than one** distinct speech region. Where Region A yields Tom `known` and Region B
yields an unresolved human speaker, the expected outcome is **two** Voice Identity evidence records —
never one combined `ambiguous` record. Cause matters: uncertainty about one voice and evidence of two
voices are never collapsed into the same representation merely because their candidate-score shape can
look similar.

---

## 9. Unknown second speaker — DL-33 unchanged

Where a second (or further) speech region is supportably human speech but cannot be associated with
any known Person, it is represented using the **existing** `unknown` / Unknown Person semantics
(**DL-33**): a supported human participant, no eligible known Person, momentary, expiring with the
assertion. **No "Unknown Person #47," synthetic Person, temporary resident, guessed Person, or
inferred guest is created.** The useful evidence is exactly what **DL-33** already carries: *another
human speaker was detected, and Identity could not resolve that speaker to a known Person* — never
more, never less.

---

## 10. Multiple resolved speakers

Where two or more speech regions each independently resolve to a `known` candidate (for example Tom in
Region A, David in Region B), the expected result is **two separately qualified Voice Identity evidence
results concerning two speakers**. They are never merged into a shared Person assertion. David's
resolution never increases Tom's confidence, and David's evidence is never treated as corroboration of
Tom's — each assertion is produced by an independent run of the Identity Fusion Function against its
own speech region's evidence.

---

## 11. DL-38 F2 — one contribution per correlation family, restated explicitly

**Multiple speech regions never create multiple confirmations for the same Person.** Voice evidence
contributes **at most one** permitted contribution per applicable correlation/evidence family, per
**DL-38 F2**, unchanged:

- Two microphones hearing Tom is **not** two confirmations.
- Segmentation producing two adjacent regions of Tom's one continuous utterance is **not** two
  confirmations.
- Tom appearing in several regions within one correlated interaction is **not** independent
  confirmation merely because segmentation produced multiple records.

Plurality represents evidence of **distinct speakers** where supportable. It never increases evidence
weight by multiplying records for the same Person.

---

## 12. Multiple microphones or channels never imply multiple speakers

Channel diversity — two microphones, two satellites, two acoustic channels producing correlated
observations of the **same** speaker — is never, by itself, evidence of speaker plurality. **DL-144**'s
channel reasoning is unchanged and applies directly: distinct capture channels remain **evidence
provenance and quality context**, never a reason to assert a second speaker, and never a reason to
structure evidence per channel.

---

## 13. Common-capture correlation and provenance

Where several Voice Identity evidence records derive from one capture or interaction, sufficient
correlation/provenance is retained to establish their common origin: the shared capture/session
reference, each record's speech-region reference, relative timing, channel/source, the relationship
among the records, and the Voice Identity runtime/Fusion Policy context — using the **existing** Record
Identity and correlation architecture (**DL-104**, **DL-35**'s existing correlation discipline applied
by analogy, not reopened). **Independent confirmations are never created by losing this common-capture
lineage.**

---

## 14. The same Person across multiple regions within one capture

A single Person may legitimately speak in multiple distinct temporal regions within one capture or
session (Tom speaks, David speaks, Tom speaks again). The runtime may emit separate region-level
evidence observations for each occurrence. Identity/Fusion **never** counts Tom twice merely because
Tom appears in Region A and Region C within the same correlation family (**DL-38 F2**, §11). Physical
truth is preserved — the records are not forced to pretend A and C were one physical region — while
Fusion's one-contribution rule is enforced at the point of aggregation, not by suppressing the
region-level evidence.

---

## 15. Overlapping speech

**Supportably separable overlap:** if the runtime can supportably distinguish distinct speakers within
overlapping audio, multiple evidence records are produced exactly as for sequential regions (§5, §10).

**Not supportably separable:** where overlap cannot be supportably separated, **plurality is never
fabricated**. No second Person, no second Unknown Person, no plurality flag, and no identity candidate
unsupported by the audio may be produced. The existing evidence-quality/unavailable/insufficient
semantics apply, and `ambiguous` is never misused merely because overlapping audio exists — `ambiguous`
remains a one-speech-region, candidate-separation outcome (§7), not a representation of unseparated
overlap.

| Overlap condition | Representation |
|---|---|
| Supportably separated into distinct speaker regions | Multiple Voice Identity evidence records (§5) |
| Not supportably separated | Existing quality/unavailable/insufficient semantics. **Never** `ambiguous`, **never** fabricated plurality |

---

## 16. Supportability is required; no threshold is decided here

A mere hint of another voice is never automatically a second Identity evidence record. The Voice
Identity runtime must have sufficient technical evidence, under current implementation and Fusion
Policy governance, to treat audio as a separate speech region. **No numerical threshold, margin,
sample count, segmentation window, VAD threshold, overlap threshold, or speaker-count cap is decided
by this ADR.** **OD-16 remains resolved and is not reopened** — those coefficients remain Fusion Policy
and implementation/App configuration, exactly as before this decision.

---

## 17. Alternative A — rejected as the canonical target model, permitted as current conservative behavior

Keeping every additional voice as **quality metadata** only (the pre-DL-147 default) is rejected as the
**canonical target model** once supportable multi-speech-region segmentation exists, because it is
silently lossy where a household genuinely has two people talking (§8). **It is not rejected as current
runtime behavior**: until Phase 6/segmentation implementation exists and supportably detects multiple
regions, the runtime **may conservatively lack plurality evidence**, and this ADR does not require
fabricating evidence the runtime does not yet produce. Governance now permits the richer model (§5);
**implementation capability determines when that evidence actually exists.**

## 18. Alternative C — rejected as the canonical evidence model

A single Voice Identity evidence record plus a Boolean `plurality` indicator is rejected as the
canonical model. It loses region-specific information: it cannot faithfully carry "Tom resolved in one
region, a second human unresolved in another" as two independently qualified observations. If an
implementation computes an internal plurality indicator as part of segmentation, it **may** remain
implementation metadata — it is never the canonical substitute for separate speech-region evidence
records (§5–§6).

## 19. Alternative D — rejected as the primary ownership model

Treating speaker plurality as a Truth/Room Fact concern rather than Identity evidence is rejected as
the primary architecture. OD-84's question — **who spoke in this capture** — is Identity evidence, not
a Truth observation. Truth/Room Facts may independently represent that multiple people are
speaking/present in a Room; that does not replace Voice Identity evidence where the Voice Identity
runtime can itself distinguish the speaker observations. Speaker-identity evidence ownership is never
moved to Truth.

---

## 20. Speaker plurality is not audience composition — DL-34 unchanged

**CRITICAL boundary, restated.** *Who spoke* and *who could hear* are different questions. Resolving
Tom and David as two speakers does **not** automatically produce "Audience = Tom + David." Speaking
grants no disclosure, authorization, recipient status, or listener status by itself. **DL-34** remains
the sole governing authority for audience composition, and its six roles — **Requestor, Speaker,
Present Person, Potential Listener, Authorized Recipient, Delivery Target** — remain never collapsed
(§23). No second audience engine is created by this decision.

`communication.md`'s own **Composition states** table already carries *Multiple known Persons* and
*Unresolved plurality* as **audience** states — these answer *who could perceive*, and must not be
confused with the Voice Identity plurality this ADR defines, which answers *who spoke*. They are two
independently governed uses of the word "plurality," owned by two different responsibilities
(Operational Trust for audience composition, Identity for speaker evidence), and neither is redefined
or merged into the other by this decision.

## 21. Speaker plurality may inform, never determine, audience evidence

Evidence that another Person spoke may be relevant evidence that another human is present in some
sense, and existing audience/context systems may consume it **if current architecture already permits
that evidence type** (**DL-34**). Voice Identity itself never asserts "this Person is therefore a
Potential Listener." **DL-34** remains the governing authority; no second audience engine, no implied
listener role, and no disclosure grant is produced by a Voice Identity evidence record alone.

## 22. Unresolved plurality and Operational Trust

Where Region A resolves Tom and Region B is an unresolved human speaker, Voice Identity may truthfully
report both: Tom spoke, and another human speaker was detected but not resolved. Operational Trust then
consumes whatever current audience/context evidence architecture already permits — **Region B is never
collapsed into "Tom ambiguous"** (§8), and Tom's successful resolution never, by itself, exposes
protected information about the second speaker. Audience uncertainty remains separately governed under
**DL-34** and **OD-71**.

## 23. Requestor ≠ Speaker ≠ Audience

**DL-34**'s role separation is preserved without exception. The Person who spoke is not assumed to be
the Requestor unless current interaction architecture establishes that relationship; a speaker is not
assumed to be a Potential Listener solely from a Voice Identity evidence record; and several resolved
speakers are never assumed to be an authorized audience. Existing role/context contracts govern these
questions; this ADR decides none of them.

---

## 24. Explainability

Explainability (**P27**) must distinguish three cases, each gated by existing Operational Trust
disclosure authorization before any are spoken or displayed:

| Case | Example explanation |
|---|---|
| **Identity ambiguity** (one speech region, DL-38 F8) | *"I was not certain whether the speaker was Tom or David."* |
| **Partially resolved plurality** (one resolved, one unresolved region) | *"I identified Tom speaking, and I detected another speaker I could not identify."* |
| **Resolved plurality** (two or more resolved regions) | *"I detected separate speaker evidence associated with Tom and David."* |

No explanation discloses another Person's identity merely because Explainability can technically
resolve the evidence — disclosure is evaluated exactly as any other Communication/explanation content
(**DL-34**).

## 25. Explainability must not overstate segmentation

Where the runtime could not supportably separate overlapping speech (§15), Explainability must not
assert *"two people spoke"* unless evidence actually establishes that. Permitted phrasing states only
what evidence supports: overlapping speech reduced evidence quality, speaker evidence could not be
separated, or voice identification was unavailable/insufficient for that region. **No invented
plurality is ever explained as fact.**

---

## 26. Phase 4 / #164 impact

Phase 4 (Runtime Matching and Unbound Evidence, **#164**) must understand, without being executed
here:

- One capture may ultimately carry or produce multiple region-specific evidence observations, not
  exactly one.
- Correlation-family handling (**DL-38 F2**) must prevent multiplication of confirmation across those
  observations.
- Consumer contracts must not assume capture cardinality equals one Voice Identity result (§5).
- `ambiguous` retains its one-speech-region meaning (§7) and is never used to represent plurality.

Dependency/acceptance evidence is posted to **#164** as part of this decision's closure. **#164 is not
executed by this ADR.**

## 27. Phase 6 / #166 impact

Phase 6 (Advanced Audio Processing, **#166**) is the principal implementation mechanism likely to
surface multiple speakers, through its already-adopted **speech-region segmentation** App capability.
Dependency/acceptance evidence posted to **#166** requires, without being executed here:

- Region segmentation may produce zero, one, or multiple regions (§5).
- Each supportably distinct speech region may yield separate Voice Identity evidence (§6).
- Common-capture/session provenance is retained across resulting records (§13).
- Overlapping speech is never fabricated into plurality (§15).
- An unresolved second speaker uses **DL-33** semantics unchanged (§9).
- No duplicate confirmations are created under **DL-38 F2** (§11).
- `ambiguous` is never used for plurality (§7–§8).

**#166 is not executed by this ADR**, and nothing here authorizes speaker-conditioned extraction
(already validation-required and not accepted behaviour) or raw rejected-audio retention (already
gated, never enabled by default).

---

## 28. No new confidence representation

No plurality confidence, speaker-count confidence, multi-speaker score, or special confidence type is
created. Each speech region uses the **existing** evidence qualification/confidence semantics (**DL-38**,
**DL-39**) unchanged. Whether segmentation is technically supportable remains an implementation/Fusion
Policy concern. **DL-36 is not reopened.**

## 29. No new Identity state

No Identity state such as `multi_person`, `plural_identity`, `crowd`, or `group_identity` is created.
Identity continues to resolve Persons from evidence; a capture may simply supply evidence concerning
multiple speaker observations through the existing `known` / `ambiguous` / `unknown` / `unavailable` /
`not required` outcome set, unchanged.

## 30. No synthetic group Person

Tom and David are never represented as a synthetic group Person ("Tom+David"), and two unresolved
voices are never represented as one "Group Unknown Person." Plurality is evidence cardinality — how
many qualified evidence records a capture produces — never Person creation.

## 31. No new responsibility

Identity remains responsible for Person resolution from evidence. The Voice Identity runtime/App
provides voice evidence and performs speech-region segmentation as an existing App capability.
Operational Trust governs authorization/disclosure. Concierge consumes governed outcomes. Truth may
independently represent Room/world observations within its own existing boundary (§19). No "Speaker
Responsibility," "Multi-Speaker Responsibility," "Diarization Responsibility," or "Plurality
Responsibility" is created.

---

## 32. Confidently wrong attribution is out of scope — #173

Episode 10 separately recorded a third, distinct cause with the same observable shape as neither
ambiguity nor plurality: **one speaker, confidently but incorrectly attributed to the wrong Person**.
This is not an uncertainty problem — the assertion looks correct, and there is nothing in the evidence
to report — and it is a correction/explainability question about what the household may do afterward,
never an evidence-cardinality question. **OD-84 does not absorb it.** **DL-32** and **DL-38** remain
unchanged: an earlier assertion is never rewritten merely because a later correction appears, so a
correction would be a new record, never an edit — but that correction architecture is not decided here.

**#173 classification.** #173 (Episode 9/10 Narrative Validation) tracks broader Episode 9/10
narrative-validation and scenario-artifact work; its own required-work checklist does not currently
list the confidently-wrong-attribution gap as a named item, and no dedicated open decision exists for
it. This gap is therefore classified as **evidence only** at this time — recorded in
`decision-ledger.md`'s existing Episode 10 Governance Harvest notes and restated here — with a
recommendation, not a decision, that #173's own Episode 9 Explainability review (which already
evaluates the adjacent confidence-representation gaps) is the appropriate place to determine whether it
warrants an identifier of its own. **This ADR does not create that identifier and does not decide the
correction architecture.**

---

## 33. Privacy

Speaker-plurality evidence can itself be sensitive: that another Person was present, that another
Person spoke, that an identified Person participated, or that an unidentified human participant
existed. **Operational Trust governs disclosure of all of it** (**DL-34**). Explainability must not
reveal another Person's identity, household participant count, or unresolved-participant state when
that information is not authorized for the requester/audience — exactly the existing
**unidentified-person policy** behavior already applied to the Identity Artifact Invalidation case
(**DL-146**).

## 34. Retention and Record Identity

Each resulting Voice Identity evidence record follows the **existing** Identity-evidence
retention/provenance rules (**DL-43**, **DL-47**). No new retention class is created merely because
several records originate from one capture; sufficient correlation/provenance to explain their common
origin is retained under the existing Record Identity/Version Identity architecture (§13). Raw audio is
not persisted merely because plurality was detected, unless existing voice/audio retention policy
independently permits it (**DL-50**'s own gated raw-rejected-audio rule, unchanged).

---

## 35. Failure and degradation

| Condition | Representation |
|---|---|
| No usable speech in the capture | No usable Voice Identity evidence (zero records, §5) |
| One speech region, candidates too close | `ambiguous` (**DL-38 F8**, §7) |
| Multiple speech regions supportably distinguished | Plurality — multiple region-level evidence records (§5, §8) |
| Multiple/overlapping voices suspected but not supportably separated | Existing evidence-quality/unavailable/insufficient semantics (§15). **Never** `ambiguous` merely for convenience, **never** fabricated plurality |

---

## 36. Required answers to OD-84

| Question | Answer |
|---|---|
| Selected alternative | **B** |
| Capture cardinality | One capture may yield zero, one, or multiple Voice Identity evidence records |
| Evidence-record cardinality | Each resulting record represents one supportably distinguished speech region |
| `ambiguous` | Unchanged **DL-38 F8** meaning: one speech region whose Person identity cannot be sufficiently separated among candidates |
| Plurality | Multiple supportably distinguished speech regions |
| Unknown second speaker | Existing **DL-33** Unknown Person/unresolved-human-participant semantics |
| Multiple known speakers | Represented as separately qualified evidence records |
| **DL-38 F2** | Multiple records never multiply confirmation within the same correlation family |
| **DL-34** | Resolved speakers do not establish audience composition |
| Overlap | Represented as plurality only where technically supportable; otherwise quality/unavailability |
| **OD-16** | Not reopened |
| Wrong attribution | Out of scope; #173 evidence route preserved (§32) |

---

## 37. Explicit non-goals

This ADR does **not**: implement speech-region segmentation or speaker diarization; implement Voice
Identity comparison; decide a speaker-separation threshold, candidate margin, number-of-speakers cap,
segmentation window length, VAD threshold, or overlap threshold; execute **#164** or **#166**; decide
the confidently-wrong-attribution correction architecture; reopen **DL-32**, **DL-33**, **DL-34**,
**DL-35**, **DL-36**, **DL-38**, **DL-39**, **DL-41**, **DL-50**, or **DL-144**; or reopen **OD-16**.

---

## 38. Related decisions

**DL-15** · **DL-32** · **DL-33** · **DL-34** · **DL-35** · **DL-36** · **DL-37** · **DL-38** (F1–F9) ·
**DL-39** · **DL-41** · **DL-43** · **DL-47** · **DL-50** · **DL-69** · **DL-72** · **DL-90** ·
**DL-104** · **DL-120** · amended **DL-137** · **DL-140** · **DL-144** · **DL-146** — each consumed
unchanged, none reopened. **OD-16** resolved and not reopened.

## 39. Related documents

- [../models/person-and-identity.md](../models/person-and-identity.md)
- [../contracts/identity-contract.md](../contracts/identity-contract.md)
- [adr-wyoming-compatible-voice-evidence-runtime.md](adr-wyoming-compatible-voice-evidence-runtime.md)
- [adr-voiceprint-gallery-structure-under-channel-diversity.md](adr-voiceprint-gallery-structure-under-channel-diversity.md)
- [../models/operational-trust.md](../models/operational-trust.md)
- [../models/communication.md](../models/communication.md)
- [../architecture/failure-and-degradation.md](../architecture/failure-and-degradation.md)
- [../models/decision-trace.md](../models/decision-trace.md)
- [../architecture/explainability.md](../architecture/explainability.md)
- [../scenarios/concierge-use-cases.md](../scenarios/concierge-use-cases.md)
- [../models/glossary.md](../models/glossary.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
