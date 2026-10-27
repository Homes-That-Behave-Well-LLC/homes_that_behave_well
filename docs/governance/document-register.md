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
| `connected-storage.md` | Canonical | New |
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
| `adr-product-disposition-and-legacy-adoption.md` | Canonical ADR | **New** — Accepted 2026-08-26 as **DL-51** and **DL-52**. Closes **OD-82**, opens **OD-85**, and amends the non-negotiable constraint in `authority-order.md` |
| `adr-household-knowledge-provider-governance.md` | Active — subordinate | **New** — Recorded 2026-10-13, pending formal acceptance review at **Issue #188**, as **DL-81**. Architecture-only; no V1 implementation authorized even if later accepted. Raised by the 2026-10 AI, Natural Interaction, and Household Knowledge Architecture Review (#188) |
| `adr-generated-behavior-authoring-governance.md` | Active — subordinate | **New** — Recorded 2026-10-13, pending formal acceptance review at **Issue #188**, as **DL-83**. Governance lifecycle boundary only; no implementation authorized even if later accepted. Raised by the 2026-10 AI, Natural Interaction, and Household Knowledge Architecture Review (#188) |
| `adr-home-identity-and-home-intelligence-governance.md` | Active — subordinate | **New** — Recorded 2026-10-14, pending formal acceptance review at **Issue #191**, as **DL-84**, **DL-85**, and **DL-86**. Governance-only; no implementation, discovery mechanism, or technology stack authorized even if later accepted. Opens **OD-90**. Raised by the 2026-10 Home Identity and Home Intelligence Architecture Review (#191) |
| `adr-stable-endpoint-identity-and-network-boundary-independence.md` | Canonical ADR | **Accepted 2026-10-27** as **DL-87**, **DL-88**, and **DL-89** (Issue #195, formal acceptance review PASS). Governance-only; no VLAN/firewall/DHCP/DNS/mDNS/wireless/switch/UniFi management or runtime endpoint-resolution implementation authorized even if later accepted. No OD identifier allocated. Raised by the 2026-10 Reference Home Network Segmentation and Stable Endpoint Identity Architecture Review (#195, closed) |
| `adr-decoupled-voice-interaction-capability-architecture.md` | Canonical ADR | **Accepted 2026-10-26** as **DL-90** and **DL-91** (Issue #198, formal acceptance review PASS). Governance-only; authorizes no implementation, vendor, STT/TTS engine, or technology stack. No OD identifier allocated. Refines (does not reopen) the still-pending **DL-88**'s `audio_output` term to `spoken_response_output`. Raised by the 2026-10 Decoupled Voice Interaction Capability Architecture Review (#198, closed) |
| `foundation-room-interaction-roles-specification.md` | Active — subordinate | **Owner-Accepted** (original material) — Implementation-readiness schema/contract specification operationalizing **DL-90**/**DL-91** for the Foundation Room Interaction Roles workstream. Owner Acceptance Review PASS (2026-10-26, Issue #199, closed) after remediating one data-model cardinality issue (commit `7096a38`). **Extended 2026-10-27 by Issue #196** to generalize the model to DL-88's `interface`/`physical_remote` roles and to resolve DL-87's implementation mechanics for this workstream (§18); **the #196 extension's own Owner Acceptance Review PASS (2026-10-27, Issue #196, closed), no remediation required.** Neither acceptance reopens the other, nor DL-87, DL-88, DL-90, or DL-91. Specification only; authorizes no executable implementation, pending an authorized HTBW Core implementation surface per the greenfield mandate |
| `performance-aware-voice-processing-specification.md` | Active — subordinate | **New** — Implementation-readiness specification operationalizing **DL-91** for the Performance-Aware Voice Processing workstream (processing stages, processing classes, routing/escalation evidence contract, provider independence, Voice Identity/Continuity/Operational Trust/Truth/Concierge boundaries, privacy, degradation, performance metrics, observability, Home Intelligence escalation). **Pending owner acceptance review (Issue #200, open — AWAITING OWNER ACCEPTANCE REVIEW).** Specification only; authorizes no executable implementation, pending an authorized HTBW Core implementation surface per the greenfield mandate |
| `htbw-framework-aligned-ux-and-information-architecture.md` | Active — subordinate | **New** — Documentation/UI-architecture direction only. Reconciles with the already-accepted Foundation/Truth/Stewardship/Continuity asset-responsibility split (`../models/asset.md`) and with **DL-51**/**DL-52**; corrects "migration"/"retirement" terminology to **Adoption**. Explicitly does not resolve **OD-85** (#172), **OD-81** (#159), or **OD-20** (#110); allocates no Decision Ledger entry |
| `adr-governed-record-persistence-mechanism.md` | Canonical ADR | **Accepted 2026-10-27** as **DL-92** (Issue #76, formal acceptance review PASS, following bounded reference/terminology corrections). Resolves **OD-01**'s persistence-mechanism residual, closing **OD-01** (DL-31, DL-92): Storage helper is the default mechanism for Current Projection, Change Record, and Snapshot; Connected Storage participates only as the already-accepted **DL-42** External History Retention extension (Change Records only, never Current Projections); distinguishes config-entry removal from governed-record deletion authority; restates no-second-Recorder (**DL-46**); defers **OD-05**, **OD-26**, **OD-29**, **OD-36**, **OD-37**, **OD-38**, **OD-39**, **OD-42**, **OD-49**, **OD-64**. Raised by the Issue #76 governed-record persistence review (#76, closed) |

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
| `ui-patterns.md` | Revise |
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

| Category | Count |
|---|---|
| New canonical documents | 59 |
| Revised in place | 2 (`README.md`, `concierge-contract.md`) |
| **Canonical total** (59 new + 2 revised) | **61** |
| Marked Active — subordinate | 25 |
| Marked Historical — superseded | 83 |
| Marked Historical illustration (`examples/`) | 16 |
| Marked Historical — planning/closure record | 2 |
| **Historical total** | **101** |
| Operational | 8 |
| **Total classified** | **195** |
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
