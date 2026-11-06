# ADR: Voiceprint Gallery Structure Under Channel Diversity

> **Document status: Canonical ADR.**
> Status: **Accepted** 2026-11-06. Records **DL-144** (issue **#168**, formal acceptance review PASS).
> Resolves **OD-83** in full.
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Terminology: [../models/glossary.md](../models/glossary.md),
> [../models/person-and-identity.md](../models/person-and-identity.md),
> [adr-wyoming-compatible-voice-evidence-runtime.md](adr-wyoming-compatible-voice-evidence-runtime.md).

---

## Status

**Accepted 2026-11-06.** Resolves every OD-83 acceptance criterion. This ADR creates **no new
responsibility**, **no new record class**, **no second evidence source**, **no channel-authorization
model**, and **no per-channel, per-Room, per-microphone, or per-phone governed voiceprint**. It does not
reopen **DL-06**, **DL-30**, **DL-31**, **DL-32**, **DL-33**, **DL-36**, **DL-38** (including **F1–F9**),
**DL-39**, **DL-41**, **DL-43**, **DL-50**, **DL-56**, **DL-71**, **DL-72**, **DL-76**, **DL-90**,
**DL-93**, **DL-104**, **DL-111**, **DL-113**, **DL-119**, **DL-120**, **DL-127**, **DL-139**, or **OD-16**
(resolved as **DL-32**/**DL-38**) — each is consumed unchanged.

---

## Context

**DL-50** (`adr-wyoming-compatible-voice-evidence-runtime.md`) accepted **channel-aware enrollment**
(Harvested Pattern 4): a voiceprint records where enrollment occurred — microphone or satellite source,
Room, capture distance, and audio characteristics. DL-50 **deliberately did not decide** how the gallery
itself is *structured* — one person-global entry, a profile per channel, or a hybrid — recording this
residual explicitly as **OD-83** so it would not be settled silently by whichever implementation chose
a storage shape first. A 2026-10-14 governance review of harvested enrollment-UX and encoder-identity
evidence confirmed the question remains genuinely open at the implementation level
(`custom_components/voice_identity/fingerprint.py` still raises
`NotImplementedError("Speaker fingerprint generation is not implemented yet.")`) and does not favor any
one alternative.

**Owner direction governing this closure:** **Alternative D** is selected at the governance level. **Each
Person has exactly one governed Voiceprint Identity Profile.** A Person does not have a voiceprint per
Room, per microphone, per voice satellite, per phone, or per capture channel, and does not acquire
multiple governed voice identities merely because enrollment occurred through different channels.
Channel diversity remains important — but it describes enrollment-evidence provenance, runtime
observation provenance, audio/capture characteristics, evidence quality, and confidence qualification,
**never** Person identity, a separate voiceprint identity, channel authorization, or independent
confirmations. **Identity identifies the Person. Operational Trust determines what that identified
Person may do in the current context.**

---

## Decision

### 1. Each Person has exactly one governed Voiceprint Identity Profile

**Alternative D is accepted; Alternatives B and C are rejected as the governed architecture; the
restrictive reading of Alternative A (one mandatory mathematically-averaged representation independent
of channel context) is rejected.** The accepted semantic result is: **one governed Person Voiceprint
profile, plus channel-diverse enrollment evidence, plus channel-aware runtime evidence quality** — not
a naive averaged profile, and not multiple governed identities.

HTBW does **not** create governed identities such as "Tom — Office voiceprint," "Tom — Den voiceprint,"
"Tom — Bedroom voiceprint," or "Tom — Phone voiceprint." The Person remains one Person. The Person has
one governed voiceprint profile. This restates `person-and-identity.md`'s own Identity Evidence
Association model unchanged: **Identity Evidence Association binds one Person to one evidence
source** (above) — voice remains **one** evidence source per Person, not one source per channel.

### 2. The one-Person-identity analogy, bounded

The conceptual model is similar to one Person having one governed Home Assistant/household identity: a
Person may interact through many devices and endpoints without that creating a different Person
identity per endpoint. Likewise, one Person has one governed Voiceprint, which may be informed by
multiple enrollment samples captured through different channels. **This analogy is illustrative only**
and is not extended into implementation details this decision does not authorize (for example, it does
not imply a specific storage schema, a specific authentication mechanism, or any other property beyond
the governed one-Person/one-Voiceprint cardinality it is used to explain).

### 3. Channel-diverse enrollment is preserved unchanged (DL-50)

Enrollment evidence may come from multiple contexts — a standalone Room microphone, a Wyoming voice
satellite, a phone microphone, or another accepted voice capture endpoint. Each enrollment sample may
retain provenance such as capture endpoint, microphone/source identity, Room, capture distance where
known, audio characteristics, timestamp, quality characteristics, and encoder/model version where
current architecture records it (`adr-wyoming-compatible-voice-evidence-runtime.md` §12, unchanged).
**All such evidence contributes to the one Person voiceprint profile.** HTBW does not create a
separately governed Person voiceprint merely because one enrollment sample came from another
microphone.

### 4. Governed semantics versus physical representation

**One governed voiceprint profile does not mandate any particular internal mathematical
representation.** This decision does not require arithmetic averaging, centroid calculation, one
physical embedding, one stored vector, weighted averaging, or a particular pooling algorithm. The
eventual implementation may internally represent the Person voiceprint using whatever technically
justified model structure is required, **provided the governed semantics remain**: one Person → one
governed Voiceprint Identity Profile → one voice-evidence contribution per correlation family (§9,
below). Physical implementation storage shape never redefines the governed model. Model-internal
multiple embeddings or channel-sensitive features, if an implementation uses them, remain beneath the
one governed Person Voiceprint and never become multiple identity artifacts or multiple confirmations
unless future measured evidence demonstrates a new governance construct is actually necessary (none is
found here).

### 5. Channel is evidence provenance and quality context, never identity or authorization

Capture-channel identity belongs to evidence provenance and quality, consistent with
`person-and-identity.md`'s existing *What each evidence source establishes* and *Identity Evidence
Associations* sections. A channel may affect evidence quality, observation qualification, similarity
confidence, reliability, and Fusion Policy qualification (**DL-38 F3**, unchanged). **It does not select
another Person identity, and it does not decide what the Person is allowed to do.** This clarifies, and
does not alter, D's own trade-off framing: channel diversity is not irrelevant — it is handled by the
existing evidence-quality/Fusion architecture rather than by multiplying governed voiceprint identities.

### 6. Alternative B (per-channel governed profiles) is rejected

HTBW does not create `Voiceprint(Person, Office)`, `Voiceprint(Person, Den)`, `Voiceprint(Person,
Bedroom)`, or `Voiceprint(Person, Phone)` as governed constructs. Person identity is not channel-specific;
per-channel structures would multiply lifecycle complexity unnecessarily, fragment consent/removal,
require a new runtime profile-selection mechanism, risk being mistaken for independent confirmations,
and risk leaking authorization concerns into Identity. The capture channel belongs to evidence context,
not Person identity.

### 7. Alternative C (hybrid governed profile selection) is rejected

HTBW does not establish a global Person voiceprint plus governed channel-specific refinement identities
plus a runtime channel-selection hierarchy as governed architecture. If an implementation internally
uses channel-sensitive features or multiple enrollment embeddings, that remains implementation detail
beneath the one governed Person Voiceprint (§4, above) — it is not exposed as multiple identity
artifacts.

### 8. Identity identifies the Person; Operational Trust authorizes

Restating `person-and-identity.md`'s existing boundary unchanged: **Identity answers *who is this
Person?*** Voice evidence contributes to that determination. **Identity never answers** whether a Person
is allowed to use a channel, perform an action in a Room, or access information through an endpoint —
those are Operational Trust's authorization questions. Channel-specific authorization is never encoded
into the voiceprint or Identity model. Once Identity sufficiently resolves the Person, Operational
Trust evaluates the applicable context (capability, Room, endpoint, audience, purpose, disclosure,
modality, policy). *Tom matched through the Den microphone* means Identity: Tom — it never means *Tom
is authorized because this is the Den microphone*.

A capture channel may affect how much confidence Identity places in a voice observation (a known,
calibrated Room endpoint versus an unknown or noisy capture channel) — that is evidence quality, never
a different Person identity. An untrusted or low-quality channel may cause the voice evidence
contribution to be lowered, held, insufficient, or unavailable under current Fusion Policy (**DL-38
F3**) — it never creates an identity failure or an alternate Person, and a known channel never confers
authorization by itself.

### 9. Scope of voice/voiceprint comparison: when it is invoked at all

**Voiceprint verification is used for interactions originating from voice-assistant endpoints where the
speaker's Person identity must be established from voice evidence.** It is **not** an additional
authentication challenge layered onto an interaction already bound to a sufficiently authenticated
Person — for example, that Person's own authenticated Companion App session, which already supplies its
own distinct evidence (*Authenticated Session Identity*, per `person-and-identity.md`'s *What each
evidence source establishes* table). Voice comparison and an authenticated-session evidence path are two
different, already-distinguished evidence sources answering the same underlying Identity question
(*who is this Person?*) through different means appropriate to different interaction origins — **one is
never redundantly re-run as a second check on top of the other's already-sufficient result.** This is a
scope clarification of when the one governed Voiceprint (§1) is consulted at all; it creates no new
evidence source, no new Identity Assertion purpose, and does not alter Fusion (**DL-38**) or the
Identity/Operational-Trust boundary (§8) in any other respect.

### 10. Runtime comparison: no profile selection by channel

At runtime: (1) a voice observation is captured; (2) available capture-channel/provenance context is
recorded; (3) audio is evaluated against the Person's one voiceprint model/gallery according to current
implementation/Fusion architecture; (4) channel/quality context qualifies the resulting evidence
(**DL-38 F3**); (5) voice contributes at most one correlation-family contribution (**DL-38 F2**, §11
below); (6) Identity fusion proceeds (**DL-38**); (7) the Person may or may not become sufficiently
resolved; (8) Operational Trust evaluates subsequent use (§8). **There is no runtime selection step of
"choose Tom's Den voiceprint."** There is only Tom's governed Voiceprint.

**Known channel.** Available channel context qualifies the evidence under existing Fusion Policy
(**DL-38 F3**) — it does not itself confer authorization (§8).

**Unknown channel.** Unknown capture channel does not require selecting a fallback voiceprint. There is
only one governed Person Voiceprint. Where channel identity/context is unavailable: compare under the
normal Person voiceprint process; mark channel information unknown/unavailable; omit any channel-specific
quality contribution that cannot be established; run existing Fusion Policy on the evidence actually
available. Unknown channel does not itself mean identity failed, and does not itself mean voice
evidence is accepted — it is an evidence-quality/context limitation. **DL-41** applies where
capability/evidence constraints make the voice comparison unavailable.

### 11. DL-38 F2 — one contribution per correlation family, restated for channel diversity

**Voice contributes at most one evidence contribution per correlation family.** Multiple enrollment
channels do not become multiple confirmations. Multiple internal embeddings do not become multiple
confirmations. Multiple microphones contributing to one correlated voice interaction do not
automatically become independent confirmations. An Office sample, a Den sample, and a Phone sample are
never counted as three supporting identity signals — they belong to the same voice evidence family
**DL-38 F2** already governs, unchanged.

### 12. DL-32 — channel is not a second evidence source

Reliability remains configured through the accepted Person-to-source association model (**DL-32**,
unchanged). A capture channel does not become a second evidence source merely because it is physically
different — there is no governed per-channel profile to be a second source **in the first place** (§§6–7,
above). The semantic requirement DL-32 already carries is restated for this question specifically:
per-channel voice evidence must not multiply identity confirmations.

### 13. Consent, profile removal, and retention (DL-43, unchanged)

The one Person Voiceprint remains usable only while the profile is enabled and required consent remains
valid (**DL-43**, unchanged). Consent withdrawal applies to the Person voiceprint and its governed
enrollment evidence according to current architecture — household administrators are never required to
discover and revoke an "Office Voiceprint," "Den Voiceprint," "Bedroom Voiceprint," or "Phone
Voiceprint," because those governed identities do not exist. Removing the Person's voiceprint
removes/disables the one governed voice identity profile according to existing Identity lifecycle rules;
any enrollment evidence retained as part of that voiceprint follows the same accepted lifecycle,
retention, and consent rules. **No channel-specific residual identity profile survives after the Person
Voiceprint has been removed.** Retention does not invent per-channel retention periods, different
Room-voiceprint retention, phone-voiceprint retention, or channel-specific deletion semantics — one
governed Person Voiceprint means one governed Identity lifecycle.

### 14. Privacy and raw audio

Voiceprint is sensitive Identity evidence. Reducing governed profile multiplication reduces unnecessary
privacy/lifecycle surface. Enrollment embeddings, raw enrollment audio, model internals, and channel
history are not exposed merely because channel-aware evidence exists — existing Identity/Operational-
Trust/privacy governance (`privacy.md`) remains authoritative. **This decision does not assume raw
enrollment audio must be retained merely because channel provenance is retained**; it does not invent a
raw-audio archive, and does not decide raw-audio retention beyond what current accepted voice-evidence/
privacy architecture already requires. **DL-120's HA-Prod-local-only ceiling for speaker-biometric
processing is consumed unchanged** — this decision does not reopen locality, and locality remains
orthogonal to configured reliability (**DL-32**) exactly as DL-120 already states.

### 15. Failure and degradation (DL-41, unchanged)

| Condition | Outcome |
|---|---|
| Voiceprint absent | Voice comparison unavailable as an Identity evidence capability |
| Voiceprint disabled | Voice evidence unavailable |
| Consent invalid/withdrawn | Voice evidence unavailable, per current consent architecture |
| Capture quality insufficient | Voice evidence lowered/held/unavailable under Fusion Policy |
| Channel unknown | Channel-specific quality evidence unavailable; evidence that remains is used |
| Model/encoder incompatible | Voice evidence capability unavailable under current version/failure architecture (`adr-wyoming-compatible-voice-evidence-runtime.md` §16) |

**None of these means the Person does not exist.** None alone silently becomes an identity mismatch.
Current canonical outcome vocabulary (`not required`/`unavailable`/`unknown`/`ambiguous`/`known`,
**DL-38**) is used throughout, never a special "deprecated channel" or "missing channel" outcome.

### 16. Explainability must not imply multiple confirmations

A governed explanation of Identity reasoning may state, where authorized: that voice evidence
contributed; which capture endpoint/channel supplied the observation; whether channel context was known
or unknown; whether evidence quality was reduced or held; that one Person Voiceprint was compared; and
whether the voice contribution was or was not sufficient, alongside other contributing evidence and the
Fusion result. **If multiple channel-diverse enrollment samples informed the Person Voiceprint,
Explainability must not claim "Three voice profiles confirmed Tom."** The Voice evidence family
contributed **one** governed contribution (**DL-38 F2**, restated). Explainability must not say "Tom
failed identity" when the voice capability was merely unavailable, and must not expose sensitive
biometric internals unnecessarily.

**If Identity resolves the Person but Operational Trust refuses an action, Explainability preserves the
distinction**: Identity — Tom sufficiently resolved; Authorization — action refused in current context.
A refusal is never blamed on the microphone, a channel-specific voiceprint, or Identity, unless that is
actually the evidence.

### 17. New hardware and model/encoder version changes do not create a new Person identity

Adding or replacing a microphone or voice satellite does not require creating a new governed Person
voice identity simply because hardware changed; the new endpoint may require Room configuration,
calibration, or evidence-quality validation, but the Person's one governed Voiceprint remains
conceptually stable. If a model/encoder change produces incompatible embeddings, current capability/
version/lifecycle rules apply (`adr-wyoming-compatible-voice-evidence-runtime.md` §16, unchanged) — this
decision does not transform encoder implementation identity into Person identity, and does not decide
model-migration/re-enrollment policy beyond what is already accepted.

### 18. Person voice identity and channel/endpoint identity remain distinct

The Person voiceprint is associated with the Person. The capture endpoint/channel has its own identity/
configuration under current Room/Foundation/device architecture. At runtime an observation may include
both, and they carry different meanings — they are never merged. Voice enrollment or runtime audio
arriving through a phone/mobile device is the same Person voiceprint plus mobile capture provenance/
context, never a mobile voiceprint; Room satellite audio does not create a Room voiceprint; multiple
microphones in the same Room do not multiply the Person's voiceprint.

### 19. Phase 3 (#163) impact — documentation only, not executed

**Issue #163 (Phase 3 — channel-aware enrollment) must be updated to consume this decision; it is not
executed by this decision.** Phase 3 must implement and test: one Person Voiceprint; channel-aware
enrollment capture/provenance; channel-aware runtime evidence quality; no per-channel governed gallery;
no runtime channel-profile selection; unknown-channel behavior; one voice contribution per correlation
family; and consent/profile removal across the full Person Voiceprint. **No voiceprint-generation code
is written by this closure**, and no sample count, phrase corpus, similarity threshold, or separation
margin is decided here — those remain **OD-16**'s own Fusion Policy/implementation configuration,
unreopened.

---

## Explicit non-goals

- **No new responsibility, record class, dependency class, or second evidence source is created.**
- **No governed per-Room, per-microphone, per-satellite, or per-phone voiceprint is created.**
- **No channel-authorization model is created**; channel never confers authorization.
- **No aggregation mathematics, sample count, phrase corpus, similarity threshold, or separation margin
  is decided** — **OD-16** is not reopened.
- **No raw-audio archive is invented.**
- **DL-06, DL-30, DL-31, DL-32, DL-33, DL-36, DL-38 (F1–F9), DL-39, DL-41, DL-43, DL-50, DL-56, DL-71,
  DL-72, DL-76, DL-90, DL-93, DL-104, DL-111, DL-113, DL-119, DL-120, DL-127, and DL-139 are not
  reopened.**
- **Phase 3 (#163) is not executed by this decision.**
- **No unrelated Owner policy is invented.**

---

## Related documents

- [../models/person-and-identity.md](../models/person-and-identity.md)
- [../contracts/identity-contract.md](../contracts/identity-contract.md)
- [adr-wyoming-compatible-voice-evidence-runtime.md](adr-wyoming-compatible-voice-evidence-runtime.md)
  (**DL-50**)
- [../models/operational-trust.md](../models/operational-trust.md)
- [../contracts/operational-trust-contract.md](../contracts/operational-trust-contract.md)
- [failure-and-degradation.md](failure-and-degradation.md)
- [privacy.md](privacy.md)
- [../models/glossary.md](../models/glossary.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
- [adr-voice-identity-enrollment-evidence-retention-and-regeneration.md](adr-voice-identity-enrollment-evidence-retention-and-regeneration.md)
  (**DL-145**)
