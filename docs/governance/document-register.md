# Document Register

> **Document status: Canonical governance.**
> Lifecycle rules: [document-lifecycle.md](document-lifecycle.md).
> Authority: [authority-order.md](authority-order.md).

---

## Purpose

**Every Markdown file in the HTBW repository is classified here. No file is unclassified.**

Dispositions: **New** · **Keep** · **Revise** · **Supersede** · **Merge** · **Archive**.
**No file is deleted by the refoundation.**

---

## 1. Root

| File | Status | Disposition | Canonical replacement |
|---|---|---|---|
| `README.md` | Canonical | **Revise** — rewritten on the seven-responsibility framework | — |

---

## 2. `docs/architecture/` — canonical

| File | Status | Disposition |
|---|---|---|
| `north-star.md` | Canonical (constitutional) | New |
| `principles.md` | Canonical (constitutional) | New |
| `framework.md` | Canonical (constitutional) | New |
| `dependency-view.md` | Canonical | New |
| `runtime-sequence.md` | Canonical | New |
| `greenfield-mandate.md` | Canonical | New |
| `home-assistant-boundary.md` | Canonical | New |
| `connected-storage.md` | Canonical | New. **Extended** (this review) with an explicit statement that this document *is* the canonical External Storage Contract, and an Asset Intelligence/Adoption reconciliation verified directly against the standalone product's own `document_storage.py` source (stable-`asset_id`-keyed folders, opaque per-document identifiers — already matching this document's governed-namespace rule, independently) |
| `behavioral-governance.md` | Canonical | New |
| `explainability.md` | Canonical | New |
| `failure-and-degradation.md` | Canonical | New |
| `privacy.md` | Canonical | New |
| `adr-htbw-core-refoundation.md` | Canonical ADR | New |
| `adr-identity-replaces-voice-identity-boundary.md` | Canonical ADR | New |
| `adr-truth-as-fact-engine.md` | Canonical ADR | New |
| `adr-room-configuration-ownership.md` | Canonical ADR | New |
| `adr-home-assistant-first-and-connected-storage.md` | Canonical ADR | New |
| `adr-historical-explainability-and-historical-truth.md` | Canonical ADR | New |
| `adr-temporal-record-model.md` | Canonical ADR | New |
| `adr-resident-communication-and-delivery-separation.md` | Canonical ADR | New |
| `adr-wyoming-compatible-voice-evidence-runtime.md` | Canonical ADR | **New** — Accepted 2026-08-25 as **DL-50** |
| `adr-governed-historical-retrieval-and-access.md` | Canonical ADR | **New** — Accepted 2026-11-04 as **DL-130** (Issue #81, OD-35) |
| `adr-product-disposition-and-legacy-adoption.md` | Canonical ADR | **New** — Accepted 2026-08-26 as **DL-51** and **DL-52**. Closes **OD-82**, opens **OD-85**, and amends the non-negotiable constraint in `authority-order.md` |
| `adr-household-knowledge-provider-governance.md` | Canonical ADR | **Accepted 2026-11-05** as **DL-81** (Issue #188, formal acceptance review PASS). Architecture-only; no V1 implementation authorized. Raised by the 2026-10 AI, Natural Interaction, and Household Knowledge Architecture Review (#188); acceptance completed alongside the Home Steward Product/Domain Definition review (#206) |
| `adr-generated-behavior-authoring-governance.md` | Active — subordinate | **New** — Recorded 2026-10-13, pending formal acceptance review at **Issue #188**, as **DL-83**. Governance lifecycle boundary only; no implementation authorized even if later accepted. Raised by the 2026-10 AI, Natural Interaction, and Household Knowledge Architecture Review (#188) |
| `adr-home-identity-and-home-intelligence-governance.md` | Canonical ADR | **Accepted 2026-10-14** as **DL-84**, **DL-85**, and **DL-86** (Issue #191, formal acceptance review PASS). Acceptance propagated to this register 2026-10-27 during the OD-67/#132 remediation (bookkeeping gap only, no re-review). Governance-only; no implementation, discovery mechanism, or technology stack authorized. Opened **OD-90**; **OD-90 and OD-77 are both now closed** (DL-115, 2026-11-02; DL-139, 2026-11-05), each independently selecting Foundation. Raised by the 2026-10 Home Identity and Home Intelligence Architecture Review (#191, closed) |
| `adr-stable-endpoint-identity-and-network-boundary-independence.md` | Canonical ADR | **Accepted 2026-10-27** as **DL-87**, **DL-88**, and **DL-89** (Issue #195, formal acceptance review PASS). Governance-only; no VLAN/firewall/DHCP/DNS/mDNS/wireless/switch/UniFi management or runtime endpoint-resolution implementation authorized even if later accepted. No OD identifier allocated. Raised by the 2026-10 Reference Home Network Segmentation and Stable Endpoint Identity Architecture Review (#195, closed) |
| `adr-decoupled-voice-interaction-capability-architecture.md` | Canonical ADR | **Accepted 2026-10-26** as **DL-90** and **DL-91** (Issue #198, formal acceptance review PASS). Governance-only; authorizes no implementation, vendor, STT/TTS engine, or technology stack. No OD identifier allocated. Refines (does not reopen) the still-pending **DL-88**'s `audio_output` term to `spoken_response_output`. Raised by the 2026-10 Decoupled Voice Interaction Capability Architecture Review (#198, closed) |
| `foundation-room-interaction-roles-specification.md` | Active — subordinate | **Owner-Accepted** (original material) — Implementation-readiness schema/contract specification operationalizing **DL-90**/**DL-91** for the Foundation Room Interaction Roles workstream. Owner Acceptance Review PASS (2026-10-26, Issue #199, closed) after remediating one data-model cardinality issue (commit `7096a38`). **Extended 2026-10-27 by Issue #196** to generalize the model to DL-88's `interface`/`physical_remote` roles and to resolve DL-87's implementation mechanics for this workstream (§18); **the #196 extension's own Owner Acceptance Review PASS (2026-10-27, Issue #196, closed), no remediation required.** Neither acceptance reopens the other, nor DL-87, DL-88, DL-90, or DL-91. Specification only; authorizes no executable implementation, pending an authorized HTBW Core implementation surface per the greenfield mandate |
| `performance-aware-voice-processing-specification.md` | Active — subordinate | **New** — Implementation-readiness specification operationalizing **DL-91** for the Performance-Aware Voice Processing workstream (processing stages, processing classes, routing/escalation evidence contract, provider independence, Voice Identity/Continuity/Operational Trust/Truth/Concierge boundaries, privacy, degradation, performance metrics, observability, Home Intelligence escalation). **Pending owner acceptance review (Issue #200, open — AWAITING OWNER ACCEPTANCE REVIEW).** Specification only; authorizes no executable implementation, pending an authorized HTBW Core implementation surface per the greenfield mandate |
| `htbw-framework-aligned-ux-and-information-architecture.md` | Active — subordinate | **New** — Documentation/UI-architecture direction only. Reconciles with the already-accepted Foundation/Truth/Stewardship/Continuity asset-responsibility split (`../models/asset.md`) and with **DL-51**/**DL-52**; corrects "migration"/"retirement" terminology to **Adoption**. Explicitly does not resolve **OD-85** (#172), **OD-81** (#159), or **OD-20** (#110); allocates no Decision Ledger entry. **Extended** (this review, "HTBW Experience & UI Architecture Standard" pass) with: subject-first primary navigation (People/Places/Assets) clarifying, not reopening, the existing BWF-navigation-model section; breadcrumbs/cross-Framework discoverability; Framework-as-education with an ownership/location/custody worked example; confirmation that `connected-storage.md` is the canonical External Storage Contract; HTBW Settings; Native First governing principle; Framework iconography requirement (flagged as not yet satisfied — follow-on design work); household-aware language/progressive disclosure; readiness/health/dependency-state model. No new Decision Ledger entry; no topic required category D (new architecture decision) |
| `adr-governed-record-persistence-mechanism.md` | Canonical ADR | **Accepted 2026-10-27** as **DL-92** (Issue #76, formal acceptance review PASS, following bounded reference/terminology corrections). Resolves **OD-01**'s persistence-mechanism residual, closing **OD-01** (DL-31, DL-92): Storage helper is the default mechanism for Current Projection, Change Record, and Snapshot; Connected Storage participates only as the already-accepted **DL-42** External History Retention extension (Change Records only, never Current Projections); distinguishes config-entry removal from governed-record deletion authority; restates no-second-Recorder (**DL-46**); defers **OD-05**, **OD-26**, **OD-29**, **OD-36**, **OD-37**, **OD-38**, **OD-39**, **OD-42**, **OD-49**, **OD-64**. Raised by the Issue #76 governed-record persistence review (#76, closed) |
| `adr-reasoning-provider-strategy.md` | Canonical ADR | **Accepted 2026-10-27** as **DL-93** (Issue #132, formal acceptance review PASS, following bounded stale-reference corrections). Resolves **OD-67**: permits local/self-hosted, household-approved cloud, or no Reasoning provider (none selected); distinguishes Reasoning, Home Intelligence (accepted **DL-86**, #191, an optional deployment/hosting boundary), and Home Steward (**accepted DL-131**, Issue #206); every evaluation resolves to an **effective Person** (resolved household Person, otherwise the designated Guest fallback Person Extension — **DL-71** — otherwise the **DL-33** unidentified-person policy; no Room involvement); defines Integration/Person configuration scopes only, with no runtime discovery; two independent Person capability gates (Allow General Questions, Allow Home Steward); configured provider fallback (Person → Integration-default → unavailable); permitted/prohibited purposes ("Reasoning may reason, never govern"); a factual-integrity response-quality profile; data minimization under Operational Trust; Explainability reusing the existing Decision Trace structure. Defers **OD-77**, **OD-07**, **OD-65**, **OD-66**, **OD-04**. Raised by the Issue #132 Reasoning Provider Strategy review (#132, closed) |
| `adr-home-steward-product-boundary.md` | Canonical ADR | **New, Accepted 2026-11-05** as **DL-131** (Issue #206, Governance Review, formal acceptance review PASS). Defines Home Steward as HTBW's locally governed AI knowledge-assistant product/domain, consuming **DL-81**, optionally hostable within **DL-86**, optionally configurable as a **DL-93** Reasoning Provider without altering DL-93's Person-only resolution order. Raised by the Home Steward Product/Domain Definition and Boundary review (#206, closed) |
| `adr-preservation-hold-governance.md` | Canonical ADR | **New, Accepted 2026-11-05** as **DL-132** (Issue #85, formal acceptance review PASS). Resolves **OD-39** in full except deletion-versus-preservation precedence, explicitly deferred to **OD-36**: placement/review/release authority (**DL-71**, **DL-109**), Governance-class identity/confirmation (**DL-76**), scope, no invented numeric duration default (restating **DL-97**), missed-review fail-safe behaviour, release-does-not-erase-history, hold-existence-as-governed-information, storage-boundary enforcement, and the honest native-HA-Recorder limitation. Raised by the Preservation Hold Governance review (#85, closed) |
| `adr-deletion-versus-preservation-reconciliation.md` | Canonical ADR | **New, Accepted 2026-11-05** as **DL-133** (Issue #82, formal acceptance review PASS). Resolves **OD-36** in full: a deletion/preservation collision becomes a governed conflict (no blind universal winner); a fourth, independently configured Conflict-Resolution Authority (**DL-71**, **DL-109**, **DL-76**); lowest-practical-granularity resolution; a required minimization sequence (generalising **DL-56**); restricted use of conflict-preserved payload (restating **DL-93**); pending-deletion reuse of **DL-45**; a late-Hold anti-abuse rule; honest Tombstone and native-HA-Recorder-limitation behaviour; **DL-110**'s adoption governing-parent resolution consumed unchanged. Raised by the Deletion Versus Preservation Reconciliation review (#82, closed) |
| `adr-incident-and-case-object-model.md` | Canonical ADR | **New, Accepted 2026-11-05** as **DL-134** (Issue #87, formal acceptance review PASS). Resolves **OD-41** in full: an Incident is a bounded, governed event scope, never a persisted object, Case, artifact, **DL-45** Governing Parent, durable actor profile, or store; no owning responsibility; constructed, never created, when a governed operation requires a bounded event context; no lifecycle; no **DL-47** retention of its own; shared scope reused across Historical Reconstruction/Preservation Hold/Evidence Package without a shared container; **DL-35** Unknown Actor Reference boundary fully preserved; Episode 9's next-evidence guidance resolved without a new Evidence responsibility. Raised by the Incident and Case Object Model review (#87, closed) |
| `adr-evidence-package-governance.md` | Canonical ADR | **New, Accepted 2026-11-05** as **DL-135** (Issue #86, formal acceptance review PASS). Resolves **OD-40** in full: projection-by-default, materialization requires an explicit separately-authorized request (never automatic); Evidence Package distinguished from **OD-09** comprehensive export; curated/bounded content with honest gap/withheld/redaction markers (reusing **DL-134**'s next-evidence states); Governing Parent via **DL-105**'s anchor-ownership rule (Home fallback), never the Incident (**DL-134**); restricted-use survival from **DL-133**; Integrity Manifest explicitly not forensic/legal/chain-of-custody sufficient; authority mapped onto existing **DL-76** Action-Risk Classes (Assembly=Disclosure, Materialization=Disclosure/Authenticated-override, External export=Governance) via the already-accepted Capability-Default → HTBW-Default → Household-Override tiering; Connected Storage/native-HA-Recorder limits restated unchanged. Raised by the Evidence Package Governance review (#86, closed) |
| `adr-data-portability-and-erasure-mechanics.md` | Canonical ADR | **New, Accepted 2026-11-05** as **DL-136** (Issue #78, formal acceptance review PASS). Resolves **OD-09** in full: Portability Export distinguished from Evidence Package (**DL-135**); on-demand governed projection, no permanent Portability Store; **Transient Export Artifact** materialized only by explicit separate authorization, household-configured short lifetime reusing **DL-122**'s preset/override shape, Governing Parent via **DL-105**'s anchor-ownership rule; mandatory Completeness Manifest; machine-readable representation required; **Temporal Portability Contract** extends **DL-30**'s verified native UTC/IANA-timezone evidence to the export surface (canonical UTC instant, event-time-rule local representation, IANA identifier, DST-safe, precision reusing **DL-129**'s observed/derived/inferred/estimated/unknown vocabulary); Portability authority reuses **DL-34**/**DL-71**/**DL-76**/**DL-135** (Assembly=Disclosure, Materialization=Disclosure/Authenticated-override, External transport=Governance); Erasure remains fully distributed, orchestrated-request authority Governance-class by analogy to **DL-132**/**DL-133**; **DL-133** governs every retention-floor/Hold collision unchanged; **DL-56**/**DL-45** consumed unchanged; **OD-05**/**OD-49** remain open for numeric values only, reusing **DL-47**'s mechanics-versus-values precedent. Raised by the Data Portability and Erasure Mechanics review (#78, closed) |
| `adr-explainability-persistence-and-retention.md` | Canonical ADR | **New, Accepted 2026-11-05** as **DL-137** (Issue #77, formal acceptance review PASS; amended 2026-11-05, same day, by targeted Owner clarification). Resolves **OD-05** in full: Decision Trace (process) distinguished from **Explainability Record** (persisted result) by persistence ownership only, never a global rename, not reopening **DL-15**/**DL-24**/**DL-27**/**DL-46**/**DL-129**; two canonical origins `outcome_generated`/`on_demand_decision_trace`, every on-demand invocation producing a new record, never deduplicated/backdated, formalizing **DL-129**'s own diagnostic-explanation clause as first-class under **DL-15**; **SQLite established as the default Explainability persistence technology** (Home Assistant Recorder precedent), a distinct database never written into the HA Recorder, narrowly reconciling **DL-129**'s "JSON-backed" descriptive detail via **DL-92**'s own encoding-is-implementation-mapping non-goal without reopening DL-129's authoritative-location/write-time-assembly/Room-normalization/storage-outage holdings; Connected Storage/Backup-growth boundary stated explicitly; **retention is governed entirely by the household-configured Explainability retention policy** (**DL-122** pattern) **— HTBW imposes no independent numeric architectural floor or ceiling, and DL-76's Action-Risk Classes classify action consequence only, never Explainability retention duration**; consent-lifecycle interaction restated from **DL-47**'s structural-floor separation; expiry requires a Tombstone, no indefinite shadow summary; one new follow-on governed issue created (HTBW Structured Data Persistence Placement Review), not executed. Raised by the Decision Trace Retention Floor and Ceiling review (#77, closed) |
| `adr-communication-retention-governance.md` | Canonical ADR | **New, Accepted 2026-11-05** as **DL-138** (Issue #118, formal acceptance review PASS). Resolves **OD-49** in full: Communication Content (substance conveyed, Minimal rendering projection anchor) and Communication Metadata (every other already-required field) classified separately; referenced source material never automatically Content; two independent, household-configured retention policies (**DL-122** preset/override shape) with **no independent architectural floor or ceiling**, applying the corrected **DL-137** philosophy; **DL-78** Category and **DL-77** Urgency never automatically dictate retention duration, optional per-Category override supported, never required; ordinary/on-demand Explainability reference never extends or resets Communication retention (**DL-47** holding rule minimizes first, **DL-132**/amended **DL-137** consumed unchanged); consent/erasure/Tombstone consume **DL-56**/**DL-133**/**DL-136** unchanged, Metadata not automatically exempt; persistence-technology placement routed to **#207** (unexecuted); **DL-136** Completeness Manifest reports Content/Metadata independently; also corrects stale pre-amendment-DL-137 dependency evidence previously posted on #118. Raised by the Communication Retention review (#118, closed) |
| `adr-person-to-external-resource-association-ownership.md` | Canonical ADR | **New, Accepted 2026-11-05** as **DL-139** (Issue #148, formal acceptance review PASS, following one bounded grounding correction resolved during this review itself). Resolves **OD-77** in full: Foundation owns the Person-scoped **External-Resource Association** assignment (**DL-85**), mirroring **DL-115**'s Home-scoped assignment; Options B–E (Identity, Continuity, Operational Trust, Concierge) rejected; internal Person-device associations (BLE, phone, watch) confirmed as Identity's (**DL-32**) and Continuity's, not Foundation precedent — the grounding correction identified and resolved in this review; requester-governed "my" resolution, never Room occupancy; Unknown Person/Guest inherit nothing (**DL-33**); shared resources are not automatic conflicts; reasoning-provider profile associations Foundation-owned where **DL-93**/**DL-131** support a Person-specific reference, DL-93's resolution order unchanged; no independent retention floor/ceiling (corrected **DL-137** philosophy); erasure (**DL-136**) distinguishes the association from the referenced resource; `continuity-use-cases.md` Use Case 6 changes U → A. Raised by the Person-to-External-Resource Association Ownership review (#148, closed) |
| `adr-explainability-presentation-and-assist-interaction-path.md` | Canonical ADR | **New, Accepted 2026-11-05** as **DL-140** (Issue #80, formal acceptance review PASS). Resolves **OD-30** in full: Terminology corrected (Decision Trace / Explainability Record / **Explainability Projection**, consuming **DL-137** unchanged); **Assist named the canonical household-facing Explainability interaction path**, extending **DL-130** without reopening it; Companion App (**DL-113**), dashboard/kiosk (**DL-88**), and voice (**DL-90**) named as Assist endpoints, never independent capabilities; endpoint contributes context, never authority (five explicit non-equations); Access/Disclosure/Presentation reused as three separable considerations via existing recorded-outcome fields, no new field created; per-request/per-audience/per-endpoint projection at read time (Option A + Option C's gating discipline); Option B (two persisted renderings) and any administrator bypass rejected outright; partial-authority honesty, affected-guest, and Unknown Person (**DL-33**) presentation behavior defined; actor reconstruction remains excluded (**DL-35**/**DL-130** unchanged); passive dashboard cards and direct database access not authorized. Raised by the Explainability Presentation review (#80, closed) |
| `adr-household-inbox-projection-semantics.md` | Canonical ADR | **New, Accepted 2026-11-05** as **DL-141** (Issue #116, formal acceptance review PASS, closed as part of the **Assist Interaction Governance Sweep** under Epic #147). Resolves **OD-47** in full: Communications-only scope (Option A, obligations remain **DL-117**'s own projection); request-centric refresh, no cache/store (Option C rejected); **accessed through Assist** (**DL-140**), scoped per requester, never per-Room/per-household; viewing not automatic acknowledgement but may constitute a Presentation event (**DL-95**/**DL-96**); filtered items receive Indication/Challenge/omission reusing **DL-94**'s three forms unchanged; the Inbox is not itself a Delivery Surface (**DL-53** not reopened); a broad Assist question may compose the Inbox and obligation projections without merging models. Raised by the Household Inbox Projection Semantics review (#116, closed) |
| `adr-communication-object-persistence.md` | Canonical ADR | **New, Accepted 2026-11-05** as **DL-142** (Issue #112, formal acceptance review PASS). Resolves **OD-42** in full: Communication is the authoritative governed record (**DL-28** unchanged); durability follows lifecycle — a Communication whose lifecycle extends beyond the creating transaction must be durably committed first, neither an always-persist-immediately nor a never-persist-until-resolved rule; persisted Content/Metadata consume **DL-138**'s classification unchanged, no duplicate field invented; source material referenced, never copied (**P30**); persistence mechanism consumes **DL-92** directly, no Communication-specific exception, Connected Storage available only as the already-accepted **DL-42** extension; **#207 not preempted**, exactly as **DL-137** independently settled Explainability's placement; native Home Assistant representation remains a **DL-31** projection, never authority; Home Assistant Notifications are the default HA-native delivery mechanism (**P21**); full delivery-mechanism matrix recorded (Companion App/mobile push, HA frontend/web, dashboard/kiosk, spoken Room announcement, email, SMS, other Notify targets, Assist/**DL-141** Household Inbox retrieval); dismissal ≠ acknowledgement, native notify "sent" ≠ delivery truth, native correlation identifiers never become Record Identity (**DL-104**); Recorder and `todo` restated as not Communication persistence (**DL-114**); Household Inbox restart behavior restated (no Inbox-specific state to lose, **DL-141** unchanged); external-copy boundary restated (**DL-136**). Raised by the Communication Persistence review (#112, closed) |
| `adr-vocabulary-change-and-withdrawal-consequences.md` | Canonical ADR | **New, Accepted 2026-11-06** as **DL-143** (Issue #174, formal acceptance review PASS). Resolves **OD-86** in full: a governed vocabulary change, retargeting, or withdrawal takes effect immediately, with term change/replacement, retargeting, and withdrawal defined as three distinct outcomes; no implicit alias, compatibility alias, deprecation window, transition window, or grace period exists unless the household explicitly configures both terms as current vocabulary; current resolution never searches history as a fallback, reusing the already-accepted `not_configured_here`/**Not understood** response unchanged, with `broken_mapping` kept distinct from withdrawal; historical vocabulary evidence is recognized for Explainability, provenance, and historical reconstruction only (consuming amended **DL-137**'s on-demand origin and Historical/Effective Scope, and **P30** Version Identity), never reactivating a term for current execution; household-authored automations, scripts, and scenes are never automatically rewritten, wrapped, renamed, or migrated (restating `why-did-this-happen.md` Scenario 17); retained governed references remain version-accurate and never become a current-execution fallback (**DL-27**/**DL-45**); no new Continuity scope is created, distinguishing a semantic-target-preserved value from a broken-vocabulary-dependency value; the wake-word sub-question is closed conservatively, preserving Issue #146 item 11's "HTBW builds nothing" conclusion unchanged; no write-back to native Home Assistant aliases is reopened and the seed-once lifecycle is unchanged; **OD-13**/**OD-59**/**OD-63**/**OD-64** are not reopened or absorbed. Raised by the Vocabulary Change and Term-Withdrawal Consequences review (#174, closed) |
| `adr-voiceprint-gallery-structure-under-channel-diversity.md` | Canonical ADR | **New, Accepted 2026-11-06** as **DL-144** (Issue #168, formal acceptance review PASS). Resolves **OD-83** in full: Alternative D selected at the governance level — each Person has exactly one governed Voiceprint Identity Profile, never per Room/microphone/satellite/phone; channel diversity is evidence provenance/quality context (**DL-38 F3**), never Person identity or authorization; voice contributes at most one evidence contribution per correlation family regardless of channel diversity (**DL-38 F2**); one governed voiceprint does not mandate one physical embedding or a specific aggregation algorithm, remaining implementation mapping beneath the governed artifact; runtime comparison never selects a channel-specific profile, known or unknown channel alike; **DL-32**/**DL-43** apply to the single governed Voiceprint unchanged; Identity identifies the Person, Operational Trust authorizes (restated); voiceprint comparison is scoped to voice-assistant-endpoint interactions requiring speaker identity from voice evidence, never a redundant check atop an already-sufficiently-authenticated interaction; **DL-120**'s HA-Prod-local-only locality ceiling consumed unchanged; Explainability must not imply multiple confirmations; **OD-16** not reopened; Issue #163 (Phase 3) updated to consume this decision, not executed. Raised by the Voiceprint Gallery Structure Under Channel Diversity review (#168, closed) |
| `adr-voice-identity-enrollment-evidence-retention-and-regeneration.md` | Canonical ADR | **New, Accepted 2026-11-06** as **DL-145** (Issue #208, formal acceptance review PASS). Resolves **OD-96** in full: Voice Identity enrollment recordings retained only under explicit household Integration policy (Option A — retain for regeneration, or Option B — delete after Voiceprint creation, chosen before enrollment and persisting across updates) and applicable Person consent (**DL-56**, a fully separate axis), for Voiceprint generation/regeneration only, excluding Home Steward/RAG/training/every other reuse; a **Voiceprint Compatibility Contract** (not a bare encoder-version string) determines validity before comparison; any Voiceprint-invalidating release is a **Breaking Identity Update** requiring a documented **compelling reason** under an architectural-stability preference; pre-migration per-Person classification (auto-regeneration-possible / manual-re-enrollment-required / unaffected); safe migration ordering preserves **DL-144** throughout (no dual-authority window, no premature destruction of still-valid Voiceprints); administrator acknowledgement explicitly distinct from Person biometric consent; governed Communications (**DL-142**) only where manual re-enrollment is actually required; backup/erasure addressed honestly (**DL-136**); the new retained-recording artifact class satisfies `connected-storage.md`'s existing 19-point artifact-declaration checklist; **#207**'s physical placement and **OD-93**'s surface placement are identified as related, neither decided here. Raised by the Voice Identity Enrollment Evidence Retention review (#208, closed) |

---

## 3. `docs/architecture/` — pre-refoundation

| File | Status | Disposition | Canonical replacement |
|---|---|---|---|
| `canonical-architecture.md` | Historical | **Supersede** | `north-star.md`, `framework.md`, `dependency-view.md`, `../governance/authority-order.md` |
| `system-flow.md` | Historical | Supersede | `runtime-sequence.md`, `dependency-view.md` |
| `concierge-runtime-architecture.md` | Historical | Supersede | `framework.md`, `../contracts/concierge-contract.md` |
| `context-before-intent.md` | Active — subordinate | Revise | Principle preserved in `runtime-sequence.md` |
| `identity-governance-reference.md` | Historical | Supersede | `../contracts/identity-contract.md` |
| `person-identity-and-enrollment-architecture.md` | Historical | Supersede | `../models/person-and-identity.md` |
| `voice-recognition-and-enrollment-architecture.md` | Historical | Supersede | `../models/person-and-identity.md` |
| `voice-profile-enrollment-architecture.md` | Historical | Supersede | `../models/person-and-identity.md` |
| `voice-profile-lifecycle-management.md` | Historical | Supersede | `../models/person-and-identity.md` |
| `voice-enrollment-lifecycle-and-state-machine.md` | Historical | Archive — enrollment-lifecycle evidence | `../models/person-and-identity.md` |
| `voice-enrollment-privacy-and-data-handling-policy.md` | Historical | Archive — privacy evidence | `privacy.md` |
| `voice-enrollment-storage-cleanup-and-retention-architecture.md` | Historical | Archive — retention evidence | `privacy.md`, `connected-storage.md` |
| `voice-identity-trust-and-data-residency-policy.md` | Historical | Archive — residency evidence | `privacy.md` |
| `voice-enrollment-modernization-roadmap.md` | Historical | Archive — planning record | — |
| `voice-enrollment-pr-boundary-plan.md` | Historical | Archive — planning record | — |
| `voice-enrollment-phase0-execution-package.md` | Historical | Archive — planning record | — |
| `voice-enrollment-phase0-issues-tracker.md` | Historical | Archive — planning record | — |
| `voice-identity-gold-gap-checklist.md` | Historical | Archive — quality record | — |
| `news-context-and-briefing-architecture.md` | Historical | Supersede | `../models/experience-and-session.md` |
| `adr-voice-identity-platform-service.md` | Historical | **Supersede** | `adr-identity-replaces-voice-identity-boundary.md` |
| `adr-voice-profile-enrollment-architecture.md` | Historical | Supersede | `adr-identity-replaces-voice-identity-boundary.md` |
| `adr-voice-enrollment-phase0-complete.md` | Historical | Archive — completion record | — |
| `adr-room-vocabulary-governance.md` | Historical | Supersede | `adr-room-configuration-ownership.md` |
| `adr-occupancy-and-presence-governance.md` | Historical | Supersede | `adr-truth-as-fact-engine.md` |
| `adr-capability-projection-governance.md` | Historical | Supersede | `adr-room-configuration-ownership.md` |
| `adr-experience-model-governance.md` | Historical | Supersede | `../models/experience-and-session.md` |
| `adr-personalization-governance.md` | Historical | Supersede | `../models/continuity.md` |
| `adr-household-memory-governance.md` | Historical | Supersede | `../models/continuity.md` |
| `adr-household-productivity-experience-governance.md` | Historical | Supersede | `../models/experience-and-session.md` |
| `adr-provenance-governance.md` | Historical | Supersede | `adr-truth-as-fact-engine.md`, `../models/decision-trace.md` |
| `adr-coordinator-v2-governance.md` | Historical | Supersede | `../contracts/concierge-contract.md` |
| `adr-concierge-v1-capability-preservation-governance.md` | Historical | Archive — capability-preservation evidence | `greenfield-mandate.md` |
| `hacs-and-platinum-governance-standard.md` | Operational | Keep | — |
| `hacs-platinum-contract-compliance-checklist.md` | Operational | Keep | — |
| `platinum-target-checklist.md` | Operational | Keep | — |
| `implementation-verification-checklist.md` | Operational | Keep | — |

---

## 4. `docs/models/` — canonical

| File | Status | Disposition |
|---|---|---|
| `glossary.md` | Canonical (constitutional) | New |
| `home.md` | Canonical | New |
| `room.md` | Canonical | New |
| `room-configuration.md` | Canonical | New |
| `contextual-vocabulary.md` | Canonical | New |
| `asset.md` | Canonical | New |
| `person-and-identity.md` | Canonical | New |
| `truth.md` | Canonical | New |
| `stewardship.md` | Canonical | New |
| `continuity.md` | Canonical | New |
| `experience-and-session.md` | Canonical | New |
| `operational-trust.md` | Canonical | New |
| `decision-trace.md` | Canonical | New — §"Source-class provenance..." (**DL-82**) added 2026-10-13, recorded pending formal acceptance review at **Issue #188**; remainder of document unaffected and remains canonical |
| `temporal-record.md` | Canonical | New |
| `communication.md` | Canonical | New |

---

## 5. `docs/models/` — pre-refoundation

| File | Status | Disposition | Canonical replacement |
|---|---|---|---|
| `room-model.md` | Historical | **Supersede** | `room.md`, `room-configuration.md` |
| `room-vocabulary-registry-model.md` | Historical | **Supersede** | `contextual-vocabulary.md` |
| `asset-model.md` | Historical | Supersede | `asset.md` |
| `person-profile-model.md` | Historical | Supersede | `person-and-identity.md` |
| `voice-profile-model.md` | Historical | Supersede | `person-and-identity.md` |
| `voice-enrollment-domain-model.md` | Historical | Archive — enrollment evidence | `person-and-identity.md` |
| `occupancy-presence-model.md` | Historical | Supersede | `truth.md` |
| `environment-model.md` | Historical | Supersede | `truth.md` |
| `event-model.md` | Historical | Supersede | `truth.md` |
| `signal-model.md` | Historical | Supersede | `truth.md` |
| `provenance-model.md` | Historical | Merge | `truth.md`, `decision-trace.md` |
| `exposure-model.md` | Historical | Merge | `room-configuration.md` |
| `capability-projection-model.md` | Historical | Supersede | `room-configuration.md` |
| `interaction-model.md` | Historical | Supersede | `room-configuration.md`, `../contracts/concierge-contract.md` |
| `experience-model.md` | Historical | Supersede | `experience-and-session.md` |
| `experience-restoration-context-model.md` | Historical | Supersede | `continuity.md` |
| `person-continuity-model.md` | Historical | Supersede | `continuity.md` |
| `person-room-affinity-model.md` | Historical | Supersede | `continuity.md` |
| `household-memory-model.md` | Historical | Supersede | `continuity.md` |
| `household-coordination-snapshot-model.md` | Historical | Supersede | `continuity.md` |
| `briefing-composition-model.md` | Historical | Supersede | `experience-and-session.md` |
| `calendar-experience-model.md` | Historical | Supersede | `experience-and-session.md` |
| `email-experience-model.md` | Historical | Supersede | `experience-and-session.md` |
| `task-experience-model.md` | Historical | Supersede | `experience-and-session.md` |
| `shopping-experience-model.md` | Historical | Supersede | `experience-and-session.md` |
| `knowledge-query-experience-model.md` | Historical | Supersede | `experience-and-session.md`, `contextual-vocabulary.md` |
| `multi-item-capture-result-model.md` | Historical | Archive — interpretation evidence | `../contracts/concierge-contract.md` |

---

## 6. `docs/contracts/` — canonical

| File | Status | Disposition |
|---|---|---|
| `README.md` | Canonical | New |
| `foundation-contract.md` | Canonical | New |
| `room-configuration-contract.md` | Canonical | New |
| `contextual-vocabulary-contract.md` | Canonical | New |
| `identity-contract.md` | Canonical | New |
| `truth-contract.md` | Canonical | New |
| `stewardship-contract.md` | Canonical | New |
| `continuity-contract.md` | Canonical | New |
| `operational-trust-contract.md` | Canonical | New |
| `concierge-contract.md` | Canonical + historical appendix | **Revise** — canonical sections 1–14 prepended; prior content retained as a marked appendix; §7 subsection *Compound and multi-item requests* (**DL-80**) added 2026-10-13, recorded pending formal acceptance review at **Issue #188**; §1–§14 otherwise unaffected and remain canonical |

---

## 7. `docs/contracts/` — pre-refoundation

| File | Status | Disposition | Canonical replacement |
|---|---|---|---|
| `composite-room-contract.md` | Historical | **Supersede** | `room-configuration-contract.md` |
| `room-interaction-contract.md` | Historical | Supersede | `room-configuration-contract.md` |
| `room-awareness-contract.md` | Historical | Supersede | `truth-contract.md`, `room-configuration-contract.md` |
| `room-vocabulary-registry-contract.md` | Historical | **Supersede** | `contextual-vocabulary-contract.md` |
| `capability-projection-contract.md` | Historical | Supersede | `room-configuration-contract.md` |
| `person-identity-contract.md` | Historical | **Supersede** | `identity-contract.md` |
| `voice-recognition-contract.md` | Historical | **Supersede** | `identity-contract.md` |
| `occupancy-and-presence-contract.md` | Historical | Supersede | `truth-contract.md` |
| `provenance-contract.md` | Historical | Merge | `truth-contract.md`, `../models/decision-trace.md` |
| `asset-intelligence-contract.md` | Historical | Supersede | `foundation-contract.md`, `stewardship-contract.md` |
| `experience-projection-contract.md` | Historical | Supersede | `../models/experience-and-session.md` |
| `experience-restoration-contract.md` | Historical | Supersede | `continuity-contract.md` |
| `person-continuity-affinity-contract.md` | Historical | Supersede | `continuity-contract.md` |
| `household-memory-contract.md` | Historical | Supersede | `continuity-contract.md` |
| `household-coordination-contract.md` | Historical | Supersede | `continuity-contract.md` |
| `calendar-email-experience-contract.md` | Historical | Supersede | `../models/experience-and-session.md` |
| `task-shopping-experience-contract.md` | Historical | Supersede | `../models/experience-and-session.md` |
| `knowledge-briefing-status-synthesis-contract.md` | Historical | Supersede | `../models/experience-and-session.md` |
| `multi-item-capture-interpretation-contract.md` | Historical | Archive — interpretation evidence | `concierge-contract.md` |
| `concierge-scope-contract.md` | Historical | Supersede | `concierge-contract.md`, `operational-trust-contract.md` |
| `concierge-signal-contract.md` | Historical | Supersede | `truth-contract.md` |
| `concierge-global-config-contract.md` | Historical | Supersede | `operational-trust-contract.md` |
| `concierge-global-context-contract.md` | Historical | Supersede | `truth-contract.md`, `room-configuration-contract.md` |
| `service-contracts.md` | Historical | Supersede | `README.md` |
| `performance-contract.md` | Active — subordinate | Revise | — |
| `v2-c1-contract-refactor-baseline.md` | Historical | Archive — refactor record | — |

---

## 8. `docs/scenarios/` — canonical

| File | Status | Disposition |
|---|---|---|
| `README.md` | Canonical | New |
| `room-vocabulary.md` | Canonical | New |
| `follow-me-media.md` | Canonical | New |
| `multi-person-conflict.md` | Canonical | New |
| `nighttime-suppression.md` | Canonical | New |
| `stewardship-obligations.md` | Canonical | New |
| `stewardship-use-cases.md` | Canonical | New — the eight canonical Stewardship use cases, added by the Episode 6 narrative-validation review |
| `continuity-use-cases.md` | Canonical | New — the fifteen canonical Continuity use cases, added by the Episode 7 narrative-validation review |
| `concierge-use-cases.md` | Canonical | New — the twenty canonical Concierge human-outcome use cases, added by the Episode 8 narrative-validation review. **Carries a maturity classification per use case and is explicitly not proof of implementation** |
| `why-did-this-happen.md` | Canonical | New |
| `where-is-tom.md` | Canonical | New |
| `where-is-maisey.md` | Canonical | New |
| `where-is-my-phone.md` | Canonical | New |
| `historical-retrieval-and-access.md` | Canonical | New — added by **DL-130** (Issue #81, OD-35) |

---

## 9. `docs/assessment/`

| File | Status | Disposition |
|---|---|---|
| `assessment-to-platform.md` | Canonical | New |

---

## 10. `docs/governance/`

| File | Status | Disposition |
|---|---|---|
| `authority-order.md` | Canonical | New |
| `document-lifecycle.md` | Canonical | New |
| `decision-ledger.md` | Canonical | New |
| `open-decision-issue-index.md` | Canonical | New — identifier-to-issue mapping for every open decision |
| `document-register.md` | Canonical | New (this document) |
| `architecture-backlog-execution-standard.md` | Operational | **New** — the repeatable backlog work-selection method (Priority → Dependency → Readiness → Dependency leverage) and greenfield-readiness assessment states, compiled 2026-10-27. **Creates no authority**, decides nothing, reprioritizes nothing, and closes nothing; no specific issue order or Priority label is encoded as permanent |
| `season-1-architectural-baseline.md` | Operational | **New** — point-in-time Season 1 baseline snapshot, 2026-08-25. **Creates no authority**; the decision ledger and the open-decision issue index prevail on any conflict |
| `home-assistant-release-review-standard.md` | Operational | **New** — the repeatable monthly Home Assistant release review process. **Creates no authority** and decides nothing; it makes the **P21** / **DL-30** verification obligation recurring rather than proposal-triggered |
| `public-claim-register.md` | Operational | **New** — traceability from material public claims to repository authority, compiled 2026-09-08. **Creates no authority**, accepts no public claim as architecture, and amends no public material |
| `season-1-traceability-matrix.md` | Operational | **New** — Season 1 narrative-to-architecture traceability, compiled 2026-09-08. **Creates no authority**; records coverage and gaps, and states its evidence limits |
| `external-publication-remediation-package.md` | Operational | **New** — exact publication-ready replacement content for external artifacts that could not be edited directly, compiled 2026-09-08. **Creates no authority**; nothing in it has been applied |
| `htbw-architecture-execution-grounding-standard.md` | Active — subordinate | Revise |
| `standard-implementation-prompt-header.md` | Active — subordinate | Revise |
| `issue-execution-review-checklist.md` | Operational | Keep |
| `cross-repo-ownership-drift-checklist.md` | Active — subordinate | Revise |
| `hacs-and-platinum-governance-gate.md` | Operational | Keep |
| `concierge-v2-roadmap-coverage-review.md` | Historical | Archive — roadmap record |
| `final-roadmap-closure-review.md` | Historical | Archive — closure record |

---

## 11. `docs/philosophy/`

| File | Status | Disposition |
|---|---|---|
| `homes-that-behave-well.md` | Active — subordinate | Revise — philosophy remains valid; framework references defer to canon |
| `concierge-philosophy.md` | Active — subordinate | Revise |

---

## 12. `docs/patterns/`

All pattern documents are **Active — subordinate**. They describe implementation technique, not
architecture ownership. Where they assert ownership, canonical authority prevails.

| File | Disposition |
|---|---|
| `advisory-patterns.md` | Revise |
| `ai-assisted-actions.md` | Revise |
| `configuration-patterns.md` | Revise |
| `execution-patterns.md` | Revise |
| `interaction-patterns.md` | Revise |
| `messaging-patterns.md` | Revise |
| `signal-patterns.md` | Revise |
| `temporary-artifact-lifecycle-pattern.md` | Revise |
| `ui-patterns.md` | Revise | **Partially revised** (this review): added native-HA-component conformance order, accessibility, responsive design, motion, configuration requirement types (Required/Capability Requirement/Enhancement), dependency states and Readiness-vs-Health, no-arbitrary-percentage rule, validation/defaults classification, destructive-action confirmation, search/filtering/scale, a third (Framework) iconography layer, and the formal UI Architecture Acceptance Gate. **Still carries known stale terminology** (flagged in-document, not corrected here): "Composite Room" should read **Merged Room** (**DL-67**/**DL-68**); "Global Context"/"Alerts" predate current BWF vocabulary. A full terminology pass remains follow-on work |
| `person-identity-patterns.md` | Revise — terminology superseded; see `../contracts/identity-contract.md` |
| `voice-integration-patterns.md` | Revise — terminology superseded; see `../contracts/identity-contract.md` |
| `voice-recognition-patterns.md` | Revise — terminology superseded; see `../contracts/identity-contract.md` |

---

## 13. `docs/development/`

| File | Status | Disposition |
|---|---|---|
| `architecture-guardrails.md` | Active — subordinate | Revise |
| `implementation-checklist.md` | Operational | Keep |

---

## 14. `docs/reference-home/`

All files in this directory are **Operational — discovery/evidence artifacts**. They create no
authority, are not architecture-of-record, and do not amend `decision-ledger.md`, `authority-order.md`,
or any canonical model/contract.

| File | Status | Disposition |
|---|---|---|
| `discovery/00-discovery-status.md` through `discovery/12-evidence-register.md` (13 files) + `discovery/*.csv` (5 files) + `discovery/reference-home-architecture.json` | Operational | New — 2026-10-07 full-environment Reference Home discovery pass (article-series/narrative-oriented) |
| `production-behavior-preservation/production-behavior-inventory.md` | Operational | New — 2026-10-13 production behavior preservation inventory (Concierge-scoped) |
| `production-behavior-preservation/production-automation-inventory.csv` | Operational | New — same pass |
| `production-behavior-preservation/production-script-inventory.csv` | Operational | New — same pass |
| `production-behavior-preservation/production-helper-inventory.csv` | Operational | New — same pass |
| `production-behavior-preservation/production-scene-inventory.csv` | Operational | New — same pass |
| `production-behavior-preservation/production-template-and-group-inventory.csv` | Operational | New — same pass |
| `production-behavior-preservation/production-behavior-catalog.csv` | Operational | New — same pass |
| `production-behavior-preservation/production-dependency-graph.md` | Operational | New — same pass |
| `production-behavior-preservation/production-dynamic-room-assembly-analysis.md` | Operational | New — same pass |
| `production-behavior-preservation/production-to-htbw-reconciliation-matrix.csv` | Operational | New — same pass |
| `production-behavior-preservation/production-migration-protection-matrix.csv` | Operational | New — same pass |
| `production-behavior-preservation/production-experience-regression-catalog.md` | Operational | New — same pass |
| `production-behavior-preservation/production-gaps-and-owner-review.md` | Operational | New — same pass |
| `production-behavior-preservation/production-evidence-register.md` | Operational | New — same pass |

**Scope note:** the 2026-10-13 pass is narrower than the 2026-10-07 pass in automation/script coverage
(26 of 84 automations; 44 of 50 scripts — scoped to the production "Concierge" and "Concierge Automation
Helpers" categories plus ungrouped automations) but substantially deeper for the items it covers (full
trigger/condition/action/dependency detail per item, a reconciliation matrix against accepted ADRs/
contracts, and a migration protection matrix). Neither pass supersedes the other; both are retained as
independent evidence per `document-lifecycle.md`'s "no file is deleted" rule.

---

## 15. `examples/`

All example documents are **Historical illustrations**, retained as evidence and as household framing.
Canonical scenarios: [../scenarios/README.md](../scenarios/README.md).

| File | Canonical successor |
|---|---|
| `examples/interaction-flows/concierge-to-asset-update.md` | `../scenarios/stewardship-obligations.md` |
| `examples/scenarios/artwork-risk.md` | `../scenarios/stewardship-obligations.md` |
| `examples/scenarios/calm-operation.md` | `../scenarios/nighttime-suppression.md` |
| `examples/scenarios/concierge-artwork-history.md` | `../scenarios/room-vocabulary.md` |
| `examples/scenarios/concierge-capability-discovery.md` | `../scenarios/room-vocabulary.md` |
| `examples/scenarios/concierge-personalization.md` | `../scenarios/follow-me-media.md` |
| `examples/scenarios/conflicting-asset-requirements.md` | `../scenarios/stewardship-obligations.md` |
| `examples/scenarios/data-closet-equipment.md` | `../scenarios/stewardship-obligations.md` |
| `examples/scenarios/event-explanation.md` | `../scenarios/why-did-this-happen.md` |
| `examples/scenarios/gradual-degradation.md` | `../scenarios/stewardship-obligations.md` |
| `examples/scenarios/missing-capability.md` | `../scenarios/room-vocabulary.md` |
| `examples/scenarios/multi-room-prioritization.md` | `../scenarios/multi-person-conflict.md` |
| `examples/scenarios/piano-preservation.md` | `../scenarios/stewardship-obligations.md` |
| `examples/scenarios/rare-book-placement.md` | `../scenarios/stewardship-obligations.md` |
| `examples/scenarios/room-change-summary.md` | `../scenarios/why-did-this-happen.md` |
| `examples/scenarios/room-dashboard-response.md` | `../scenarios/room-vocabulary.md` |

---

## Summary

Verified against the working tree: **186 Markdown files, 0 unclassified**, at the 2026-08 refoundation
baseline. **Updated 2026-10-13**: two new documents were added by the 2026-10 AI, Natural Interaction,
and Household Knowledge Architecture Review (#188), each banner-marked **Active — subordinate** (not
Canonical) because each is recorded pending formal acceptance review at **Issue #188** and is not yet
authoritative — see the rows above for `adr-household-knowledge-provider-governance.md` and
`adr-generated-behavior-authoring-governance.md`. No file was deleted or reclassified; the counts
below reflect that addition only and are not a full recount of the register.

**Also updated 2026-10-13**: `docs/reference-home/` (previously untracked, 18 pre-existing discovery
files plus 15 new production-behavior-preservation files, 33 total) is now registered under section 14
above, all banner-marked **Operational — discovery/evidence artifact**. None are Canonical; none amend
any accepted ADR, contract, model, or decision-ledger entry. This addition is not reflected in the
186-file/56-canonical baseline counts below, consistent with the #188 precedent immediately above.

**Updated 2026-10-14**: one new document was added by the 2026-10 Home Identity and Home Intelligence
Architecture Review (#191), banner-marked **Active — subordinate** (not Canonical) because it is
recorded pending formal acceptance review at **Issue #191** and is not yet authoritative — see the row
above for `adr-home-identity-and-home-intelligence-governance.md`. No file was deleted or reclassified;
the counts below reflect this addition only, consistent with the #188 precedent above.

**Correction recorded 2026-10-27 (during the OD-67/#132 remediation):** Issue #191 actually recorded a
PASS formal acceptance review on **2026-10-14** — the same day the document above was added — but this
was never propagated into this register, the decision ledger, or the ADR's own banner until now. **No
new review occurred; this is a bookkeeping correction only.**
`adr-home-identity-and-home-intelligence-governance.md` is reclassified **Canonical ADR**, accepted as
**DL-84**, **DL-85**, and **DL-86**. The counts below reflect one reclassification (Active —
subordinate → Canonical ADR, net zero to Total classified; −1 to Active — subordinate, +1 to new
canonical documents and Canonical total).

**Updated 2026-10**: one new document was added by the 2026-10 Reference Home Network Segmentation and
Stable Endpoint Identity Architecture Review (#195), initially banner-marked **Active — subordinate**
(not Canonical) while recorded pending formal acceptance review at **Issue #195**. **Issue #195
subsequently recorded a PASS formal acceptance review (2026-10-27)**, and
`adr-stable-endpoint-identity-and-network-boundary-independence.md` is reclassified **Canonical ADR**
accordingly — see the row above. No file was deleted; the counts below reflect one reclassification
(Active — subordinate → Canonical ADR, net zero to Total classified).

**Updated 2026-10**: one new document was added by the 2026-10 Decoupled Voice Interaction Capability
Architecture Review (#198), initially banner-marked **Active — subordinate** (not Canonical) while
recorded pending formal acceptance review at **Issue #198**. **Issue #198 subsequently recorded a PASS
formal acceptance review (2026-10-26)**, and `adr-decoupled-voice-interaction-capability-architecture.md`
is reclassified **Canonical ADR** accordingly — see the row above. **One further new document** was
added by the resulting Foundation Room Interaction Roles implementation-readiness specification work,
`foundation-room-interaction-roles-specification.md`, banner-marked **Active — subordinate** (a
specification operationalizing accepted architecture, not itself constitutional); **this document
subsequently received its own Owner Acceptance Review PASS (2026-10-26, Issue #199, closed)** after one
remediation, and remains classified **Active — subordinate** (a specification, not a constitutional
document, regardless of its own acceptance). **One further new document** was added by the Performance-
Aware Voice Processing implementation-readiness specification work, `performance-aware-voice-processing-specification.md`,
also banner-marked **Active — subordinate**, **pending its own owner acceptance review (Issue #200,
open)**. No file was deleted; the counts below reflect one reclassification (Active — subordinate →
Canonical ADR, net zero to the Active — subordinate count) and two additions (the two new specification
documents, +2 to both Active — subordinate and Total classified).

**Updated 2026-10-27**: one new document, `architecture-backlog-execution-standard.md`, was added to
record the durable backlog work-selection method established by the current architecture-backlog
sequencing review (Epic #147). Banner-marked **Operational**; it creates no authority, decides nothing,
and is not itself subject to owner acceptance review. The counts below reflect this one addition
(+1 to both Operational and Total classified).

**Updated 2026-10-28**: one new document, `adr-governed-record-persistence-mechanism.md`, was added,
drafting **DL-92** pending formal acceptance review at **Issue #76** (**OD-01**'s persistence-mechanism
residual). Banner-marked **Active — subordinate** (drafted, not yet constitutional). The counts below
reflect this one addition (+1 to both Active — subordinate and Total classified).

**Updated 2026-10-27 (continued), Issue #76 formal acceptance review PASS**:
`adr-governed-record-persistence-mechanism.md` is reclassified **Canonical ADR**, accepted as **DL-92**,
closing **OD-01** (DL-31, DL-92). The counts below reflect one reclassification (Active — subordinate
→ Canonical ADR, net zero to Total classified; −1 to Active — subordinate, +1 to new canonical
documents and Canonical total).

**Updated 2026-10-27 (continued)**: one new document, `adr-reasoning-provider-strategy.md`, was added,
drafting **DL-93** pending formal acceptance review at **Issue #132** (**OD-67**'s reasoning-provider
strategy). Banner-marked **Active — subordinate** (drafted, not yet constitutional). The counts below
reflect this one addition (+1 to both Active — subordinate and Total classified).

**Updated 2026-10-27 (continued), bookkeeping correction**: `adr-home-identity-and-home-intelligence-governance.md`
is reclassified **Canonical ADR**, as recorded above (Issue #191 formal acceptance review PASS,
2026-10-14; propagation delayed, no re-review). The counts below reflect one reclassification (Active
— subordinate → Canonical ADR, net zero to Total classified; −1 to Active — subordinate, +1 to new
canonical documents and Canonical total).

**Updated 2026-10-27 (continued), Issue #132 formal acceptance review PASS**:
`adr-reasoning-provider-strategy.md` is reclassified **Canonical ADR**, accepted as **DL-93**,
closing **OD-67**. The counts below reflect one reclassification (Active — subordinate → Canonical
ADR, net zero to Total classified; −1 to Active — subordinate, +1 to new canonical documents and
Canonical total).

**Updated 2026-11-05, Issue #206 formal acceptance review PASS (Home Steward Product/Domain
Definition and Boundary, DL-131)**: one new document, `adr-home-steward-product-boundary.md`, is added
as **Canonical ADR** from creation (+1 to new canonical documents, +1 to Canonical total, +1 to Total
classified). Alongside the same review, `adr-household-knowledge-provider-governance.md` completed its
own outstanding formal acceptance review (Issue #188, DL-81, PASS) and is reclassified **Canonical
ADR** (Active — subordinate → Canonical ADR, net zero to Total classified; −1 to Active — subordinate,
+1 to new canonical documents and Canonical total). `decision-trace.md` and `glossary.md` (both
already Canonical) are revised in place, not reclassified. **DL-80** and **DL-83** (and their own
documents, `concierge-contract.md` §7 and `adr-generated-behavior-authoring-governance.md`) are
**not** part of this update and remain Active — subordinate, pending #188 alone.

**Updated 2026-11-05 (continued), Issue #85 formal acceptance review PASS (Preservation Hold
Governance, DL-132)**: one new document, `adr-preservation-hold-governance.md`, is added as
**Canonical ADR** from creation (+1 to new canonical documents, +1 to Canonical total, +1 to Total
classified). `temporal-record.md`, `operational-trust.md`, `privacy.md`, `connected-storage.md`,
`decision-trace.md`, and `stewardship.md` (all already Canonical) are revised in place, extending their
existing Preservation Hold sections and correcting one stale OD-39/OD-36 cross-reference in
`privacy.md`; none is reclassified.

**Updated 2026-11-05 (continued), Issue #82 formal acceptance review PASS (Deletion Versus
Preservation Reconciliation, DL-133)**: one new document,
`adr-deletion-versus-preservation-reconciliation.md`, is added as **Canonical ADR** from creation (+1
to new canonical documents, +1 to Canonical total, +1 to Total classified). `temporal-record.md`,
`operational-trust.md`, `privacy.md`, `connected-storage.md`, and `decision-trace.md` (all already
Canonical) are revised in place, extending their existing deletion/preservation sections and resolving
the remaining bare `**OD-36**` cross-references to `**DL-133**`; none is reclassified.

**Updated 2026-11-05 (continued), Issue #87 formal acceptance review PASS (Incident and Case Object
Model, DL-134)**: one new document, `adr-incident-and-case-object-model.md`, is added as **Canonical
ADR** from creation (+1 to new canonical documents, +1 to Canonical total, +1 to Total classified).
`temporal-record.md`, `explainability.md`, and `glossary.md` (all already Canonical) are revised in
place, adding the *Incident scope* section/term and resolving the Episode 9 category-15/17 mapping;
`open-decision-issue-index.md` is updated; none is reclassified.

**Updated 2026-11-05 (continued), Issue #86 formal acceptance review PASS (Evidence Package
Governance, DL-135)**: one new document, `adr-evidence-package-governance.md`, is added as **Canonical
ADR** from creation (+1 to new canonical documents, +1 to Canonical total, +1 to Total classified).
`temporal-record.md`, `operational-trust.md`, `privacy.md`, `connected-storage.md`, and
`decision-trace.md` (all already Canonical) are revised in place, replacing the Evidence Package
section/rows with the full DL-135 resolution and resolving remaining bare `**OD-40**` cross-references
to `**DL-135**`; `connected-storage.md` additionally resolves stray stale `**OD-39**`/`**OD-36**`
cross-references (already resolved as **DL-132**/**DL-133**) found in the same pass;
`open-decision-issue-index.md` is updated; none is reclassified.

**Updated 2026-11-05 (continued), Issue #78 formal acceptance review PASS (Data Portability and
Erasure Mechanics, DL-136)**: one new document, `adr-data-portability-and-erasure-mechanics.md`, is
added as **Canonical ADR** from creation (+1 to new canonical documents, +1 to Canonical total, +1 to
Total classified). `temporal-record.md`, `operational-trust.md`, `privacy.md`, `connected-storage.md`,
`decision-trace.md`, `home-assistant-boundary.md`, `explainability.md`, and `glossary.md` (all already
Canonical) are revised in place, adding the *Portability Export* and *Erasure* sections/terms and the
Temporal Portability Contract, and resolving stray stale `**OD-39**`/`**OD-09**` cross-references
(already resolved as **DL-132**/this decision) found in the same pass; `open-decision-issue-index.md`
is updated; none is reclassified.

**Updated 2026-11-05 (continued), Issue #77 formal acceptance review PASS (Explainability
Persistence, Origins, and Retention, DL-137)**: one new document,
`adr-explainability-persistence-and-retention.md`, is added as **Canonical ADR** from creation (+1 to
new canonical documents, +1 to Canonical total, +1 to Total classified). `temporal-record.md`,
`operational-trust.md`, `privacy.md`, `connected-storage.md`, `decision-trace.md`, and `explainability.md`
(all already Canonical) are revised in place, adding the Decision Trace/Explainability Record
distinction, the `outcome_generated`/`on_demand_decision_trace` origins, the SQLite persistence-
technology decision, the Connected Storage/Backup-growth boundary, and the household-configured
retention model; `open-decision-issue-index.md` is updated; one new governed issue (HTBW
Structured Data Persistence Placement Review) is filed separately and is not itself a canonical
document; none is reclassified.

**Updated 2026-11-05 (continued, same day), targeted Owner clarification to accepted DL-137 (Issue
#77)**: no new document is created and no count changes. `adr-explainability-persistence-and-retention.md`,
`decision-ledger.md`, `decision-trace.md`, `privacy.md`, `operational-trust.md`, `temporal-record.md`,
and `open-decision-issue-index.md` are each revised in place to correct DL-137's retention holding —
retention is fully household-configured with no independent numeric architectural floor or ceiling,
and DL-76's Action-Risk Classes classify action consequence only, never Explainability retention
duration. DL-137 remains the same accepted decision, amended in place per repository convention; none
is reclassified.

**Updated 2026-11-05 (continued), Issue #118 formal acceptance review PASS (Communication Retention
Governance, DL-138)**: one new document, `adr-communication-retention-governance.md`, is added as
**Canonical ADR** from creation (+1 to new canonical documents, +1 to Canonical total, +1 to Total
classified). `communication.md`, `privacy.md`, `operational-trust.md`, and `glossary.md` (all already
Canonical) are revised in place, adding the Communication Content/Metadata classification, the
independent household-configured retention model (applying the corrected DL-137 philosophy), the
Category/Urgency retention boundary, and the Explainability-reference non-extension rule;
`open-decision-issue-index.md` is updated; a stale pre-amendment-DL-137 dependency-evidence comment on
#118 is corrected via issue comment, not by rewriting this register; Issue #207 remains open and
unexecuted; none is reclassified.

**Updated 2026-11-05 (continued), Issue #148 formal acceptance review PASS (Person-to-External-Resource
Association Ownership, DL-139)**: one new document, `adr-person-to-external-resource-association-ownership.md`,
is added as **Canonical ADR** from creation (+1 to new canonical documents, +1 to Canonical total, +1 to
Total classified). `person-and-identity.md`, `foundation-contract.md`, `continuity.md`,
`continuity-contract.md`, `continuity-use-cases.md`, `glossary.md`, and
`adr-home-identity-and-home-intelligence-governance.md` (all already Canonical) are revised in place:
naming Foundation in the previously-unassigned Person-extension row, confirming the shared
External-Resource Association shape is satisfied by both the Home-scoped (DL-115) and Person-scoped
(DL-139) assignments, updating Use Case 6 from U to A and the related Use Case 2/4 rows, and resolving
stale "OD-77 remains open" cross-references found in `foundation-contract.md`,
`adr-home-identity-and-home-intelligence-governance.md`, and this register's own DL-84–86 row;
`open-decision-issue-index.md` and `decision-ledger.md` are updated; none is reclassified.

**Updated 2026-11-05 (continued), Issue #80 formal acceptance review PASS (Explainability Presentation
— Assist as the Canonical Household-Facing Interaction Path, DL-140)**: one new document,
`adr-explainability-presentation-and-assist-interaction-path.md`, is added as **Canonical ADR** from
creation (+1 to new canonical documents, +1 to Canonical total, +1 to Total classified).
`decision-trace.md`, `explainability.md`, `operational-trust.md`, `privacy.md`, `concierge-contract.md`,
and `glossary.md` (all already Canonical) are revised in place: adding the **Explainability Projection**
term, naming Assist as the canonical household-facing Explainability interaction path and Companion
App/dashboard/kiosk/voice as its endpoints, stating the endpoint-contributes-context-not-authority
non-equations, and extending the existing Presentation decision field to cover endpoint/modality
eligibility for Explainability requests specifically — no new recorded-outcome field is created;
`open-decision-issue-index.md` and `decision-ledger.md` are updated; none is reclassified.

**Updated 2026-11-05 (continued), Issue #116 formal acceptance review PASS (Household Inbox Projection
Semantics, DL-141, closed as part of the Assist Interaction Governance Sweep)**: one new document,
`adr-household-inbox-projection-semantics.md`, is added as **Canonical ADR** from creation (+1 to new
canonical documents, +1 to Canonical total, +1 to Total classified). `communication.md`,
`glossary.md`, and `concierge-contract.md` (all already Canonical) are revised in place: stating the
Communications-only scope, request-centric no-cache refresh, Assist access path, per-requester
scoping, viewing/acknowledgement distinction, filtered-item behavior, and not-itself-a-Delivery-Surface
holding; a stray `communication.md` cross-reference (a tie-break configuration-surface follow-on
loosely "tracked under OD-47") is corrected to note it is not resolved by DL-141;
`open-decision-issue-index.md` and `decision-ledger.md` are updated; none is reclassified.

**Updated 2026-11-05 (continued), Issue #112 formal acceptance review PASS (Communication Object
Persistence and Home Assistant Representation, DL-142)**: one new document,
`adr-communication-object-persistence.md`, is added as **Canonical ADR** from creation (+1 to new
canonical documents, +1 to Canonical total, +1 to Total classified). `communication.md`,
`adr-resident-communication-and-delivery-separation.md`, `home-assistant-boundary.md`, and
`connected-storage.md` (all already Canonical) are revised in place: stating the lifecycle-based
durability rule, the persisted Content/Metadata field set (consuming **DL-138** unchanged), the
source-reference-not-copy boundary, the direct **DL-92** persistence-mechanism consumption with no
Communication-specific exception, the **#207** non-preemption, the native-HA-representation-as-
projection restatement, and the full delivery-mechanism matrix; `adr-resident-communication-and-
delivery-separation.md`'s own pre-**DL-92** "Connected-storage implications" section and several stale
rows in its "Open decisions" table (OD-47, OD-49, OD-51, OD-52, OD-56, OD-58, each since independently
closed) are reconciled in the same pass; `open-decision-issue-index.md` and `decision-ledger.md` are
updated; none is reclassified.

**Updated 2026-11-06, Issue #174 formal acceptance review PASS (Vocabulary Change and Term-Withdrawal
Consequences, DL-143)**: one new document, `adr-vocabulary-change-and-withdrawal-consequences.md`, is
added as **Canonical ADR** from creation (+1 to new canonical documents, +1 to Canonical total, +1 to
Total classified). `contextual-vocabulary.md`, `contextual-vocabulary-contract.md`,
`adr-room-configuration-ownership.md`, `continuity.md`, `decision-trace.md`,
`failure-and-degradation.md`, `why-did-this-happen.md`, `home-assistant-boundary.md`,
`concierge-contract.md`, and `glossary.md` (all already Canonical) are revised in place: stating the
immediate-change rule for term change/replacement/retargeting/withdrawal, the current-versus-historical
vocabulary distinction, the historical-evidence-never-executes rule (consuming amended **DL-137**'s
on-demand origin and Historical/Effective Scope), the never-rewrite-household-artifacts restatement, the
Continuity semantic-target-versus-broken-reference distinction, the conservative wake-word-sub-question
closure preserving Issue #146 item 11 unchanged, and a new Scenario 64 worked example; two stale
cross-references found and corrected in the same pass (`contextual-vocabulary.md`'s Open Decisions table
and `adr-room-configuration-ownership.md`'s own Open-decisions line each still listed the already-closed
**OD-13** as open); `open-decision-issue-index.md` and `decision-ledger.md` are updated; none is
reclassified.

**Updated 2026-11-06 (continued), Issue #168 formal acceptance review PASS (Voiceprint Gallery Structure
Under Channel Diversity, DL-144)**: one new document,
`adr-voiceprint-gallery-structure-under-channel-diversity.md`, is added as **Canonical ADR** from
creation (+1 to new canonical documents, +1 to Canonical total, +1 to Total classified).
`person-and-identity.md`, `identity-contract.md`, `adr-wyoming-compatible-voice-evidence-runtime.md`,
`operational-trust.md`, and `glossary.md` (all already Canonical) are revised in place: stating that each
Person has exactly one governed Voiceprint Identity Profile (Alternative D), channel diversity as
evidence provenance/quality context only (never identity or authorization), the governed-semantics-
versus-physical-representation boundary (no mandated aggregation algorithm), the known/unknown-channel
runtime-comparison rule, the voiceprint-comparison-scope clarification (voice-assistant-endpoint
interactions requiring speaker identity from voice evidence, never a redundant check atop an
already-authenticated session), and a new **Voiceprint (DL-144)** glossary entry; three stale
cross-references found and corrected in the same pass (`adr-wyoming-compatible-voice-evidence-runtime.
md`'s §32 Open-decisions table still listed **OD-06** and **OD-07** as "Engaged, not resolved," both
independently closed as **DL-56** and **DL-120**); `open-decision-issue-index.md` and
`decision-ledger.md` are updated, including a refreshed readiness check confirming **#175**/**OD-87**
now has zero remaining blockers; none is reclassified.

**Updated 2026-11-06 (continued), Issue #208 formal acceptance review PASS (Voice Identity Enrollment
Evidence Retention, Voiceprint Regeneration, and Breaking Encoder Compatibility Governance, DL-145)**:
one new document, `adr-voice-identity-enrollment-evidence-retention-and-regeneration.md`, is added as
**Canonical ADR** from creation (+1 to new canonical documents, +1 to Canonical total, +1 to Total
classified). `person-and-identity.md`, `identity-contract.md`,
`adr-wyoming-compatible-voice-evidence-runtime.md`,
`adr-voiceprint-gallery-structure-under-channel-diversity.md`, `privacy.md`, `connected-storage.md`,
`failure-and-degradation.md`, `communication.md`, and `glossary.md` (all already Canonical) are revised
in place: stating the household Option A/B enrollment-evidence retention policy (chosen before
enrollment, persisting across updates), the household-policy-versus-Person-consent separation, strict
purpose limitation, the Voiceprint Compatibility Contract concept, the Breaking Identity Update
classification and compelling-reason release gate, pre-migration Person classification, safe migration
ordering preserving **DL-144**, administrator-acknowledgement-versus-consent distinction, required
Communications, backup/erasure honesty, and a new declared Connected Storage artifact class (satisfying
the existing 19-point checklist, extending rather than replacing the existing zero-default-retention
enrollment-sample row); three new glossary entries (**Voice Identity Encoder Migration Policy**,
**Voiceprint Compatibility Contract**, **Breaking Identity Update**); one stale/overtaken statement
found and corrected in the same pass (`privacy.md`'s Preservation Hold section's "because those were
never stored" claim, no longer universally true now that Option A retention exists);
`open-decision-issue-index.md` and `decision-ledger.md` are updated, including a refreshed readiness
check confirming **#175**/**OD-87**'s prerequisite is now resolved; none is reclassified.

| Category | Count |
|---|---|
| New canonical documents | 77 |
| Revised in place | 2 (`README.md`, `concierge-contract.md`) |
| **Canonical total** (77 new + 2 revised) | **79** |
| Marked Active — subordinate | 23 |
| Marked Historical — superseded | 83 |
| Marked Historical illustration (`examples/`) | 16 |
| Marked Historical — planning/closure record | 2 |
| **Historical total** | **101** |
| Operational | 8 |
| **Total classified** | **211** |
| **Unclassified** | **0** |
| **Deleted** | **0** |

Every Markdown file in this repository carries a `> **Document status: ...**` banner immediately
after its H1. No file was deleted, moved, or renamed by the refoundation.

Three canonical documents were added after the original refoundation count of 181 files, under the
temporal-record governance decisions: `../models/temporal-record.md`,
`../architecture/adr-historical-explainability-and-historical-truth.md`, and
`../architecture/adr-temporal-record-model.md`. See
[decision-ledger.md](decision-ledger.md) entries **DL-24** through **DL-27**.

Two further canonical documents were added under the resident-communication governance decisions,
bringing the total to 186: `../models/communication.md` and
`../architecture/adr-resident-communication-and-delivery-separation.md`. See
[decision-ledger.md](decision-ledger.md) entries **DL-28** and **DL-29**.

---

## Related documents

- [document-lifecycle.md](document-lifecycle.md)
- [authority-order.md](authority-order.md)
- [decision-ledger.md](decision-ledger.md)
