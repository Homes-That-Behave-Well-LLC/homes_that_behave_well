# ADR: Voice Identity Enrollment Evidence Retention, Voiceprint Regeneration, and Breaking Encoder Compatibility Governance

> **Document status: Canonical ADR.**
> Status: **Accepted** 2026-11-06. Records **DL-145** (issue **#208**, formal acceptance review PASS).
> Resolves **OD-96** in full.
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Terminology: [../models/glossary.md](../models/glossary.md),
> [../models/person-and-identity.md](../models/person-and-identity.md),
> [adr-voiceprint-gallery-structure-under-channel-diversity.md](adr-voiceprint-gallery-structure-under-channel-diversity.md).

---

## Status

**Accepted 2026-11-06.** Resolves every OD-96 acceptance criterion. This ADR creates **no new
responsibility**, **no new Identity state**, **no second Voiceprint**, **no Consent responsibility**,
and **no Voice Identity responsibility**. It does not reopen **DL-19**, **DL-30**, **DL-32**, **DL-38**
(F1–F9), **DL-41**, **DL-43** (extended, not reopened), **DL-50**, **DL-56**, **DL-92**, **DL-104**,
**DL-120**, **DL-136**, amended **DL-137**, **DL-140**, **DL-142**, or **DL-144** — each is consumed
unchanged. **OD-16** is not reopened.

---

## Context

A Voiceprint is a **derived** biometric Identity artifact (**DL-144**: one Person → one governed
Voiceprint Identity Profile). Its source material is the Person's Voice Identity **enrollment
recordings**. Owner review of **#175**/OD-87 discovered that OD-87 currently assumes every invalidated
Voiceprint requires manual re-enrollment — an assumption this decision shows is not necessarily true.
`privacy.md`'s already-accepted *Raw voice-sample retention* principle states that raw samples default
to zero retention beyond the processing window, but **"any retention is explicit, consented,
time-bounded, and inspectable"** — this decision is the first operationalization of that general
principle for Voice Identity enrollment evidence specifically. **DL-43**'s existing "Voice enrollment
samples" artifact row (temporary, zero default retention) remains the default; this decision adds an
explicitly declared, non-default artifact class alongside it, never replacing it.

---

## Decision

### 1. Core rule

**Voice Identity enrollment recordings may be retained only under an explicit household Integration
policy and applicable Person consent, for the narrow purpose of Voiceprint generation and
regeneration.** Absent both, enrollment recordings follow **DL-43**'s existing zero-default-retention
rule unchanged.

### 2. Initial Integration configuration — required policy choice

**During initial HTBW Integration configuration, before any Voice Identity enrollment occurs**, the
household must make an explicit, standing **Voice Identity Enrollment Evidence Retention** policy
choice, applying to initial enrollments, future enrollments, re-enrollments, and every future Voice
Identity application/encoder/audio-contract change. **The policy is household/Integration-scoped —
never Room-scoped, and never redefined Person-by-Person.** Room Configuration does not own it; Person
Configuration does not redefine the household default.

- **Option A — Retain for future regeneration.** HTBW securely retains the original enrollment
  recordings in protected local governed storage for the purpose of generating and regenerating the
  enrolled Person's Voiceprint. If a future Voice Identity encoder is incompatible with the current
  Voiceprint, HTBW first attempts to create and validate a replacement Voiceprint from those retained
  recordings; if the recordings do not satisfy the new encoder's requirements, the affected Person still
  needs to complete Voice Identity enrollment again.
- **Option B — Delete after Voiceprint creation.** HTBW deletes the original enrollment recordings after
  the Person's Voiceprint has been successfully created and validated. A future incompatible Voice
  Identity application update requires the affected Person to complete enrollment again.

This is the household's standing **Voice Identity Encoder Migration Policy**, not re-elicited at every
update. **The policy must exist before enrollment, because enrollment behavior itself depends on it** —
it is not deferred until the first encoder migration, by which time Option B recordings would correctly
no longer exist.

### 3. Household policy and Person consent are two separate axes

Distinguish **household/Integration policy** (may this HTBW household support retention of enrollment
recordings for regeneration at all?) from **Person consent** (may *this* Person's biometric enrollment
recordings actually be retained and reused for that permitted purpose?), consuming **DL-56** unchanged.
**Option A enables the retention capability; it never overrides consent withdrawal, and administrator
authority never substitutes for Person biometric consent.** No alternate consent system is created.

### 4. Retained enrollment audio is biometric source evidence

Retained enrollment recordings are formally classified as: Identity-owned biometric enrollment
evidence; **richer and more sensitive source material than the derived Voiceprint** (the architecture
must not assume retaining the derived Voiceprint carries identical privacy consequences to retaining
the source recordings); governed local data; an **internal runtime artifact**, never resident media,
and never a general-purpose audio archive. **DL-144 remains authoritative and is not reopened**: one
Person → one governed Voiceprint Identity Profile. Retained recordings are source evidence, never
another Voiceprint, an independent Identity confirmation, a per-channel governed profile, or an
alternate active Voiceprint, and are never counted as a runtime confirmation.

### 5. Purpose limitation

Retained enrollment recordings may be used **only** for Voice Identity enrollment, Voiceprint
generation, Voiceprint regeneration, and technically required validation directly associated with
generation/regeneration under accepted Voice Identity architecture. They are explicitly **never** reused
for Home Steward, Home Intelligence knowledge ingestion, RAG, general Reasoning, a transcription
archive, household-memory ingestion, preference learning, behavioral learning, media analysis, HTBW
model training, third-party model training, unrelated speech analysis, or any other unidentified future
purpose. A future new purpose requires its own separate governance and consent.

### 6. Protected storage and security

Where Option A is selected, retained enrollment recordings reside in a protected biometric-enrollment
evidence namespace, reusing `connected-storage.md`'s already-accepted **Governed namespace** pattern and
its existing classification of voiceprints and enrollment samples as **internal runtime artifacts,
never resident media** (already stated there, not newly invented). At minimum: the local-only
processing/storage boundary under already-accepted Voice Identity locality authority (**DL-120**,
unchanged); least-privilege access limited to components required for governed Voiceprint
generation/regeneration and administration; no routine household browsing; no Media Browser exposure
merely because files are audio; no ordinary media indexing; no Home Steward/RAG indexing; no
general-purpose document ingestion; protected backup behavior; governed deletion capability; Person
association; Voiceprint/source provenance; purpose limitation. **No implementation-specific ACL or
encryption mechanism is invented** where current security architecture has not already chosen one —
requirements are stated without inventing technology.

**§25, below, states the full Connected Storage artifact declaration satisfying `connected-storage.md`'s
existing 19-point checklist.**

### 7. #207 boundary — semantic classification, not physical placement

**This decision is not preempted by, and does not preempt, #207.** OD-96 establishes **what** this data
is, **who** governs it, **why** and **when** it may exist, **what** may and must never access it, and
**when** it must be deleted. **#207** retains the exact physical persistence placement where genuinely
unresolved. Where repository authority already resolves a placement detail (for example, that
enrollment samples and voiceprints are already classified as internal runtime artifacts under
`connected-storage.md`'s governed namespace), that detail is consumed, not left artificially open.

### 8. Policy change A → B

When the household changes from retain (A) to delete (B), the new policy becomes authoritative and
retained enrollment recordings must then be deleted according to current deletion/privacy/backup
governance — primary retained files, temporary files, processing/staging copies, and generated
transitory artifacts are all addressed; backup implications are reconciled per §22, below. **No
deletion guarantee is invented for uncontrolled/external copies architecture cannot honestly provide**,
and no normal active regeneration copy is left behind after the transition.

### 9. Policy change B → A

Changing from delete (B) to retain (A) is **prospective only** — previously deleted recordings are
**never recreated**. Existing Voiceprints do not become invalid merely because the household later
selects Option A. Re-enrollment is never forced solely to populate retained source evidence unless a
separately accepted requirement explicitly requires it. Future enrollment/re-enrollment recordings
follow the newly authoritative Option A policy, subject to Person consent.

### 10. Voice Identity application/runtime versus HTBW Integration

**The required Voice Identity application/runtime owns**: encoder implementation, embedding
generation, biometric representation, comparison mechanics, preprocessing implementation, model
runtime, compatibility-determination mechanics, regeneration mechanics, and technical Voiceprint
validation. **HTBW Integration owns/governs**: household policy, Person association, Identity
integration, retention policy, consent orchestration, authorization to use retained evidence, migration
policy, household acknowledgement, Communications, degraded household behavior, and migration
accountability/completion. Encoder implementation never moves into the HTBW Integration; the Voice
Identity runtime never decides household policy.

### 11. Voiceprint Compatibility Contract

**Govern the Voiceprint Compatibility Contract, not a bare encoder-version comparison.** Compatibility
may depend on encoder/model, embedding representation, feature extraction, preprocessing,
normalization, audio contract, or other technically material representation constraints — an encoder
package/version may change while compatibility remains intact, and compatibility may break even where
the nominal encoder identity does not change. The required Voice Identity application/runtime must
expose deterministic compatibility identity/results sufficient for HTBW to know **before** comparison
whether the current Voiceprint remains usable — never discovered from degrading recognition scores,
consistent with **DL-50**'s already-accepted "compatibility is enforced before comparison and never
warned about afterwards" rule.

### 12. Minimum HTBW ↔ Voice Identity contract (conceptual)

**Voice Identity application/runtime provides**: runtime/component identity/version; Voiceprint
Compatibility Contract identifier/version; stored-Voiceprint compatibility determination;
enrollment-evidence requirements; retained-evidence compatibility/sufficiency result; regeneration
capability; regeneration outcome; Voiceprint validation outcome; incompatibility reason/category where
safely useful. **HTBW provides**: governed Person context; enrollment request; authorized
enrollment-evidence reference; whether retained-evidence use is permitted by current policy/consent;
regeneration request; delete/remove-Voiceprint request; relevant lifecycle eligibility. Raw biometric
material is never exposed across this contract unnecessarily; exact API method names are not invented
here, since current repository authority does not yet define them.

### 13. Breaking Identity Update classification

Any update that intentionally makes previously valid Voiceprints incompatible is a **Breaking Identity
Update**, classified by **household consequence**, never by package ownership or marketing version
semantics — regardless of whether it originates from the Voice Identity application, an encoder/model
update, a preprocessing update, an audio-contract change, a compatible-runtime dependency, an
HTBW-packaged dependency, or another compatibility-boundary change. HTBW Integration is never assumed to
itself carry the encoder.

### 14. Compelling-reason gate (non-negotiable)

**If the HTBW project authors, controls, packages, recommends, or otherwise governs the required Voice
Identity application/runtime, a Voiceprint-invalidating compatibility change must not be introduced
merely because a newer encoder/model exists, benchmarks are fashionable, upstream published a newer
model, a different architecture looks more modern, or theoretical accuracy is modestly higher without a
demonstrated HTBW problem.** A breaking change requires documented compelling evidence: recurring HTBW
GitHub issues, production household evidence, reproducible false acceptances/rejections, inadequate
speaker separation, unacceptable far-field/noisy-room behavior, accepted performance/latency-criteria
failure, unacceptable compute requirements, a material privacy/security defect, an unsupported/
deprecated dependency, an incompatible upstream requirement, or inability to meet accepted architecture.

**Canonical stability preference**: absent evidence that the current Voice Identity implementation
materially fails accepted HTBW requirements, retaining the existing compatible implementation is
preferred to introducing a breaking change that invalidates household Voiceprints.

### 15. GitHub/production feedback loop and the breaking-change evidence package

HTBW's governance feedback loop (production household evidence → GitHub issues/support evidence →
problem pattern recognized → investigation authorized → candidate alternative evaluated → compatibility
consequence evaluated → breaking-change review → migration planning → release → household evidence) is
a principal evidence source for whether encoder investigation is warranted at all. **GitHub issue volume
alone is not proof; one anecdote alone is not necessarily proof; severity may justify action even
without high volume. No arbitrary numeric issue-count threshold is created** — engineering/governance
judgment supported by evidence applies.

Before approving an intentionally incompatible release, document at minimum: the deficiency in the
current implementation; supporting production/GitHub evidence; the candidate replacement; recognition,
false-acceptance, false-rejection, and speaker-separation comparison; far-field/noisy-room comparison
where applicable; latency/performance result; local-processing/privacy effect; compute/hardware effect;
Home Assistant/runtime compatibility; migration consequence; automatic regeneration capability;
expected manual-re-enrollment burden; and the reason maintaining compatibility is not preferable. **No
OD-16 threshold is decided here, and no arbitrary numerical acceptance criterion is invented where
Fusion Policy already owns it.**

### 16. Compatible update versus Breaking Identity Update

A pre-update compatibility determination is required. **Compatible**: normal update, no Voiceprint
migration merely because an application/encoder version changed. **Incompatible**: the Breaking
Identity Update path applies. Classification follows Voiceprint compatibility, never marketing version
semantics.

### 17. Pre-migration Person classification

Before committing a Breaking Identity Update, classify each Person:

- **Auto-regeneration possible**: an active Voiceprint exists; Option A applies; the Person's consent
  permits retained-evidence reuse; retained evidence exists; the Voice Identity runtime confirms the
  evidence satisfies the target compatibility requirements.
- **Manual re-enrollment required**: Option B applies; retained evidence is absent; consent prevents
  reuse; evidence is corrupt/unavailable; evidence fails target requirements; or regeneration/validation
  fails.
- **Unaffected**: current configuration/lifecycle means no migration action applies (no active
  Voiceprint, Voice Identity disabled, or another current-architecture terminal state).

**One Person's biometric status is never exposed to another without authorization.**

### 18. Regeneration is an opportunity, never a guarantee

**Rejected household-facing claim**: *"Option A means you will never need to re-enroll."* **Correct
promise**: *"Retaining the enrollment recordings may allow HTBW to regenerate your Voiceprint
automatically after a future compatibility-breaking Voice Identity update."* The new encoder/runtime
remains responsible for determining whether source recordings are sufficient; if not, manual
re-enrollment remains the fallback.

### 19. Administrator breaking-update acknowledgement

Before committing a Breaking Identity Update, the household administrator receives the actual assessed
consequence — a count of Voiceprints that can regenerate automatically, a count of household members
needing to create a new Voiceprint, confirmation that other accepted Identity methods are unaffected,
and confirmation that existing Voiceprints are not removed/replaced unless the new compatibility
boundary is successfully established — with controls to review affected people, acknowledge and
continue, or cancel/defer. **OD-96 defines the required acknowledgement semantics; OD-93 is now closed
as DL-148, placing this acknowledgement at the update/migration lifecycle event** — never a centralized
acceptance surface. See
[adr-contextual-governed-acceptance-placement.md](adr-contextual-governed-acceptance-placement.md).
Existing Home Assistant configuration/update
interaction patterns are used wherever they satisfy the requirement; no independent HTBW updater,
notification center, or confirmation framework is invented absent evidence native facilities are
insufficient (**P21** Home Assistant First).

**The administrator's acknowledgement authorizes applying the breaking household update. It does not
authorize retention or reuse of another Person's biometric source evidence.** For automatic
regeneration, household policy **and** Person consent **and** retained evidence **and** technical
compatibility must all independently permit it.

### 20. Safe migration order and the one-Voiceprint invariant

**Safe order**: detect compatibility break → establish compelling justification → determine affected
Persons → classify each Person → present administrator impact → administrator acknowledges → begin
upgrade → successfully establish the new compatibility boundary → attempt authorized automatic
regeneration → technically validate regenerated Voiceprints → transition validated Voiceprints to
authoritative versions → remove obsolete/unusable Voiceprints per Identity lifecycle → identify
remaining manual-re-enrollment cases → send governed Communications → track downstream OD-87 migration
completion. **Still-valid Voiceprints are never destroyed merely because the administrator
acknowledged the update, and never before the new compatibility boundary successfully commits.**

**DL-144 survives migration.** Per Person: old current Voiceprint → validated replacement → replacement
becomes current → obsolete Voiceprint retires/removes. Temporary implementation artifacts may exist as
technically required, but **there is never more than one active governed Voiceprint asserting identity
for one Person** — reusing existing Version Identity/Change Record semantics (**DL-104**), never a
dual-authority window.

### 21. Manual re-enrollment case and the OD-87 boundary

**OD-96 decides only that a Person lands in auto-regenerated, manual-re-enrollment-required, or
unaffected.** Preserving **DL-41** unchanged: voice evidence unavailable ≠ Person does not exist ≠
identity failure ≠ trust failure ≠ permission failure. Other Identity paths remain independent — a
sufficiently authenticated Companion App interaction remains usable without requiring redundant
Voiceprint verification (consuming **adr-voiceprint-gallery-structure-under-channel-diversity.md**'s
own scope clarification unchanged), transcription remains ungated (**DL-50**), and Person-specific
voice capability degrades conservatively. **OD-96 does not re-decide OD-87's own remaining household
degradation, notification, and completion semantics** for the manual-re-enrollment case — those remain
OD-87's (#175).

### 22. Partial household migration

Migration may be partial: one Person's automatic regeneration succeeds, another requires manual
re-enrollment, another has Voice Identity disabled — each reaches its own correct terminal state
independently, and the whole household's Voice Identity functionality is never held hostage to one
Person's pending enrollment.

### 23. Communications

**Every Person who had a Voiceprint and requires manual re-enrollment receives a governed Communication**
(consuming **DL-142** unchanged) explaining, without exposing another Person's state: that Voice
Identity technology changed; that the previous Voiceprint is incompatible; that Voice Identity may not
identify them through a shared voice assistant until enrollment completes; that other accepted Identity
mechanisms are unaffected; and current instructions for creating the replacement Voiceprint. **No second
messaging mechanism is created** — native Home Assistant delivery methods are used where current
Communication architecture already calls for them.

**No mandatory high-interruption Communication is invented for successful automatic regeneration.** The
administrator's own breaking-update acknowledgement already supplies household-level awareness; where
accepted privacy/transparency architecture requires an affected Person be informed, the notice is
informational and non-actionable only. No new urgency/category is created without supporting authority.

### 24. Backup

Reconciling `connected-storage.md`'s existing "Connected storage and Home Assistant Backup" rules
unchanged: retained biometric source evidence must retain its protection classification if backed up;
restore must not silently bypass current household policy, current Person consent, or erasure state;
A→B triggers governed deletion from current active retained storage; historical backup-deletion
behavior matches actual backup governance honestly. **HTBW never claims "all copies are immediately
destroyed" unless architecture can prove it** — if historical backups retain governed data until backup
expiry, that is stated honestly, and restoration/reconciliation honors the current deletion/consent
state.

### 25. Erasure and consent withdrawal

Consuming **DL-136** and **DL-56** unchanged: when retention/use permission ends, retained enrollment
evidence cannot remain usable for regeneration and is deleted per governed deletion semantics. **No
secret regeneration archive, convenience copy, RAG copy, media copy, or debug copy is maintained.**
Voiceprint/derived-artifact lifecycle continues under Identity authority unchanged.

### 26. Explainability

Where authorized, Explainability may establish: the applicable compatibility contract; why
incompatibility occurred; the household's A/B policy; whether retained recordings existed; whether
Person consent allowed reuse; whether regeneration was attempted and its technical outcome; why manual
enrollment was required; when the old Voiceprint stopped being authoritative and when the replacement
became authoritative; and the Voice Identity runtime/component version. Raw enrollment recordings,
embeddings, biometric vectors, and unnecessary sensitive internal biometric representation are **never
exposed** — governed references only.

### 27. Connected Storage artifact declaration

Reusing `connected-storage.md`'s existing 19-point artifact-declaration checklist unchanged (no second
checklist invented), the new artifact class is declared:

| # | Declaration | Statement |
|---|---|---|
| 1 | Artifact Type | Voice Identity enrollment recordings retained for Voiceprint regeneration |
| 2 | Owning responsibility | **Identity** |
| 3 | Creating capability | Voice Identity enrollment, where household policy is Option A |
| 4 | Required dependency | Option A household policy **and** applicable Person consent **and** a successfully completed, validated enrollment |
| 5 | Storage class | Internal Runtime Artifact (governed class, not a physical path) |
| 6 | Anchor | The Person's Voice Identity enrollment session and resulting Voiceprint (**DL-104** Record Identity/version) |
| 7 | Governing parent object | The Person's voice profile |
| 8 | Parent Removal Behavior | Removed when the voice profile is removed or consent is withdrawn |
| 9 | Interaction model | **Internal Runtime Artifact** — never Managed Content, never Queryable Historical Record |
| 10 | Retention strategy | Retained only while Option A policy and the Person's applicable consent both currently permit |
| 11 | Deletion trigger | A→B policy change, consent withdrawal, erasure request, profile removal, or other current Identity lifecycle trigger |
| 12 | Consent effect | Governs existence and retention directly (**DL-56**) — ineligible evidence is never merely down-weighted |
| 13 | Preservation Hold effect | Never held — a Preservation Hold cannot authorize retention of biometric source material beyond what household policy and Person consent already permit; this restates, and does not relax, the existing "a hold cannot preserve what was never permitted to be retained" principle |
| 14 | Behaviour when Connected Storage is unavailable | Enrollment/regeneration capability requiring retained evidence is `unavailable` under **DL-41**, naming the dependency; never silently skipped or substituted |
| 15 | Behaviour when storage is lost after creation | Reported honestly as unavailable; never fabricated as present; reconciled per `connected-storage.md`'s existing loss-after-creation rules |
| 16 | Historical and explainability requirements | Governed references only (§26); raw material never reconstructed from Explainability |
| 17 | Access restrictions | Components required for Voiceprint generation/regeneration and governed administration only; never ordinary household browsing, Media Browser exposure, media indexing, Home Steward/RAG indexing, or general document ingestion |
| 18 | Integrity or version requirements | Tied to the Voiceprint Compatibility Contract version applicable at capture time |
| 19 | Recovery or reconciliation behaviour | Reconciled per existing Connected Storage recovery rules; never silently recreated from an uncontrolled copy |

**Exact physical placement is #207's own determination, not preempted here (§7).**

---

## Explicit non-goals

- **No Voiceprint generation/regeneration is implemented. No encoder is selected. No storage/security
  mechanism implementation occurs.** This is governance, not implementation.
- **No new responsibility, Identity state, or second Voiceprint is created.**
- **No Consent responsibility is created**; **DL-56** governs unchanged.
- **OD-16 is not reopened** — no sample count, threshold, or margin is decided here.
- **#175/OD-87's own remaining notification/degradation/completion questions are not decided here** (now closed as **DL-146**).
- **OD-93's (#203) interaction-surface placement is not decided here** (now closed as **DL-148**;
  see [adr-contextual-governed-acceptance-placement.md](adr-contextual-governed-acceptance-placement.md)).
- **#207's physical persistence placement is not decided here.**
- **DL-19, DL-30, DL-32, DL-38 (F1–F9), DL-41, DL-43, DL-50, DL-56, DL-92, DL-104, DL-120, DL-136,
  amended DL-137, DL-140, DL-142, and DL-144 are not reopened.**
- **No unrelated Owner policy is invented.**

---

## Related documents

- [../models/person-and-identity.md](../models/person-and-identity.md)
- [../contracts/identity-contract.md](../contracts/identity-contract.md)
- [adr-wyoming-compatible-voice-evidence-runtime.md](adr-wyoming-compatible-voice-evidence-runtime.md)
  (**DL-50**)
- [adr-voiceprint-gallery-structure-under-channel-diversity.md](adr-voiceprint-gallery-structure-under-channel-diversity.md)
  (**DL-144**)
- [privacy.md](privacy.md)
- [connected-storage.md](connected-storage.md)
- [failure-and-degradation.md](failure-and-degradation.md)
- [../models/communication.md](../models/communication.md)
- [adr-communication-object-persistence.md](adr-communication-object-persistence.md) (**DL-142**)
- [adr-contextual-governed-acceptance-placement.md](adr-contextual-governed-acceptance-placement.md) (**DL-148**)
- [../models/glossary.md](../models/glossary.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
