# ADR — Temporal Record Model

> **Document status: Accepted ADR.**
> Authority: rank 1 in [../governance/authority-order.md](../governance/authority-order.md).
> Establishes **P29** and **P30**, and accepted decisions **DL-26** and **DL-27**.
> Position ADR: [adr-historical-explainability-and-historical-truth.md](adr-historical-explainability-and-historical-truth.md).

---

## Status

Accepted.

This ADR establishes the **mechanism**. The constitutional position — that the home must account for
itself across time, and that Truth owns Fact history — is established separately in
[adr-historical-explainability-and-historical-truth.md](adr-historical-explainability-and-historical-truth.md).

The two are separated deliberately. The position should be stable for the life of the framework. The
mechanism may be revised after implementation experience without reopening the position.

---

## Context

### The constitution was silent where cost is determined

P27 and P28 require that history be retained. Neither says anything about the **shape** of the
retained record.

A silent constitution does not produce a neutral implementation. It produces the default one. This is
a **P1** argument applied to structure rather than to behaviour: *if no principle owns the shape of
history, the shape is invented at runtime* — differently by each responsibility, making cross-subject
reconstruction impossible.

### The Asset Intelligence lesson, stated accurately

The Asset Intelligence reference implementation was examined as architectural evidence. It was not
modified.

**Asset Intelligence did not lack field-level diff capture.** It created compact field-level changes
at write time, and it compacted large collection changes into counts and deltas rather than copying
complete collections. That instinct was sound and is preserved by this ADR.

The architectural problems were structural:

| # | Problem |
|---|---|
| 1 | Change records were embedded inside the mutable Asset payload |
| 2 | History was not independently addressable |
| 3 | History was not independently retainable |
| 4 | History could not be placed on hold independently |
| 5 | The entire shared JSON store was rewritten on save |
| 6 | Audit history was silently truncated |
| 7 | Truncation left no tombstone |
| 8 | Change records lacked independent record identity |
| 9 | Change records lacked prior-version and new-version references |
| 10 | Change records lacked correlation and causation |
| 11 | Historical retrieval was assembled from multiple differently shaped arrays |

**The accepted lesson:** change records must become **governed, independently addressable,
independently retainable, version-anchored records**.

Problem 3 is the one that matters most for governance. Because history lived as a field on the live
object, it could not be retained, redacted, exported, or held independently — and was destroyed with
the object. That alone makes preservation holds impossible.

Problem 7 is the one that matters most for honesty. Silent truncation converts *"we discarded the
record"* into *"nothing happened"*, which is a false statement about the household.

### Home Assistant had already converged on the answer

The recorder's `states` table carries an explicit prior-state pointer, hash-deduplicated attributes
so unchanged data is not re-stored, and native correlation, causation, and actor identity through
context columns. Long-term statistics implement periodic downsampled snapshots that are never purged.

Home Assistant already runs a live projection, an append-only detail layer with a bounded window, and
a permanently retained downsampled layer beyond it. **The hybrid model is not a novel architecture.
It is the platform's own.**

---

## Decision

### P29 — History is recorded as change, not as repeated copies

A governed record has a **Current Projection**. Its history consists of immutable **Change Records**
and **Domain Events**, accelerated where useful by **Snapshots**.

Normal operation reads Current Projections. Historical reconstruction uses the nearest valid Snapshot
and the Change Records that follow it. **HTBW must not require comparison of complete stored payloads
to discover what changed.**

### P30 — Governed records reference exact versions

A record depending on another responsibility's output references the **exact version** of that
governed record rather than copying its payload. A minimal immutable explanation projection may be
retained beside the reference where durable human readability requires it.

**An explanation must remain accurate after current configuration or policy changes.** A reference
transfers no ownership and permits no re-derivation. A dangling reference is reported, never silently
rendered as though the source record never existed.

### The hybrid temporal model

Adopted in full:

1. Current Projections
2. Append-only meaningful Change Records
3. Domain Events
4. Periodic or policy-triggered Snapshots
5. Decision Traces
6. Governed References between exact record versions
7. Reconstruction from the nearest valid Snapshot plus subsequent Change Records

### The five record kinds

| Kind | Question | Mutability | Owner |
|---|---|---|---|
| Current Projection | What is true or configured now? | Mutable; replaced | The owning responsibility |
| Change Record | What changed, when, why, by whom, from which version to which? | Immutable once recorded | The owning responsibility |
| Domain Event | What meaningful occurrence happened? | Immutable once recorded | The observing responsibility |
| Snapshot | What was the governed state at a point in time? | Immutable; derivable | The owning responsibility |
| Decision Trace | Why did Concierge act or not act? | Immutable | Concierge |

**A Domain Event is something that happened in the household. A Change Record is something that
happened to a governed record.** They are not collapsed into a generic event type, and the superseded
event model is not revived as a new owner.

### Version Identity, Bitemporality, Reconstruction

- Every governed record carries a **version identity**; every Change Record names prior and new
  versions; every dependent record references versions, not objects.
- **Effective Time** and **Recorded Time** are both constitutional. A correction never overwrites; it
  is a new Change Record with its own Recorded Time and the corrected Effective Time.
- **State at time T** is reconstructed from the nearest valid Snapshot at or before T plus subsequent
  Change Records applied in Effective Time order. Gaps are reported, never fabricated or silently
  closed. A reconstruction containing an unreported gap is a defect.

### Current Projections and Snapshots

- Historical records must never become the normal runtime query path.
- The Current Projection is authoritative for the present; historical records are authoritative for
  the past; a mismatch is a defect.
- A Snapshot is an accelerator, not an independent source of truth. It identifies included versions
  and last-applied Change Records, does not rewrite history, does not replace provenance, honours
  later redaction and deletion, does not reinstate removed content, and does not hide gaps.

The full model is [../models/temporal-record.md](../models/temporal-record.md).

### Accepted decisions established

| ID | Decision |
|---|---|
| **DL-26** | History is recorded as governed change, not as repeated full copies |
| **DL-27** | Governed records reference exact versions and do not copy complete payloads |

### Deliberately not decided

This ADR does **not** select a database, storage technology, serialization format, snapshot interval,
identifier encoding, or per-responsibility persistence strategy. **Responsibilities are not required
to share a persistence technology.**

---

## Responsibility impact

| Responsibility | Impact |
|---|---|
| **Foundation** | Defines the shared temporal, version, change-record, snapshot, correlation, and provenance models in [../models/temporal-record.md](../models/temporal-record.md). Produces and owns no other responsibility's history |
| **Stewardship** | Obligation, maintenance, service, significance, and caretaker-assignment history recorded as Change Records |
| **Identity** | Assertion and consent-lifecycle history recorded as Change Records carrying evidence classes and reason codes only |
| **Truth** | Fact lifecycle transitions recorded as Change Records; Historical Facts retained with provenance, evidence references, confidence at the time, coverage, and freshness |
| **Continuity** | Preference, session, resume, and transfer history recorded as Change Records |
| **Operational Trust** | Owns retention classification, privacy classification policy, and Preservation Hold authority. Policy history recorded as Change Records so a past decision can cite the policy version applied |
| **Concierge** | Decision Traces reference exact versions instead of copying payloads. Assembles Historical Reconstruction and Evidence Packages as projections |
| **Room Configuration** (Foundation) | Membership, participation, exclusion, exposure, vocabulary, assignment, and contributor-selection changes produce Change Records with prior and new version references |

---

## No new responsibility

**The seven-responsibility framework is unchanged.** Human Trust remains an outcome. Temporal record
and change-history architecture is **cross-cutting**, in the same way privacy and failure behaviour
already are.

This ADR creates **no** History, Memory, Household Memory, Case Management, or Evidence
responsibility; **no** central history owner; **no** central snapshot owner; and **no** central
preservation-hold enforcer.

Each responsibility records its own history. Each snapshots its own scope. Each enforces holds over
its own records. Foundation defines the shared model and owns none of the resulting history.

[../models/household-memory-model.md](../models/household-memory-model.md),
[adr-household-memory-governance.md](adr-household-memory-governance.md), and
[../models/event-model.md](../models/event-model.md) remain Historical or Superseded, and their former
ownership boundaries are not reactivated.

---

## Alternatives considered

| # | Alternative |
|---|---|
| A | Full-payload versioning — store a complete copy of the record on every change |
| B | Pure event sourcing — current state exists only as a fold over an immutable log |
| C | Change records with no snapshots |
| D | Snapshots only, with no change records |
| E | Current state only; history delegated wholly to the Home Assistant recorder |
| F | Hybrid: Current Projections, Change Records, Domain Events, Snapshots, and version references |
| G | Hybrid, but with one persistence strategy mandated for all seven responsibilities |

---

## Alternatives rejected

| # | Rejected because |
|---|---|
| **A** | Storage grows with change frequency multiplied by record size, not with information content. Answering *what changed* requires comparison. Write amplification rewrites unchanged data on every save. This is the pattern the reference implementation demonstrated, with the consequences listed in Context |
| **B** | **Decisive objection: privacy.** An append-only-forever log cannot honour deletion, revocation, or redaction, all of which [privacy.md](privacy.md) requires. It also violates the Current Projection requirement, freezes early schema choices permanently, forces uniform persistence on all responsibilities, makes corrections inexplicable in household language, and has no Home Assistant primitive |
| **C** | Reconstruction cost grows without bound, and history becomes unreconstructable once early Change Records are purged |
| **D** | Reintroduces full-payload comparison to answer *what changed*, and can never answer *why* or *by whom*. Alternative A with a longer interval |
| **E** | Seriously considered under **P21**. Rejected because the recorder stores entity states, not governed Facts; has no subject beyond an entity, making Room, Asset, Person, and incident retrieval impossible; and **cannot exempt a record from purge**, so Preservation Holds cannot exist |
| **F** | **Accepted** |
| **G** | Contradicts the requirement that responsibilities need not share a persistence strategy. Truth's Fact history, Stewardship's obligation history, and Concierge's Decision Traces have materially different volume, sensitivity, and query profiles. The constitution mandates the **model**, never the **store** |

---

## Privacy consequences

Historical Explainability and Historical Truth establish retention **floors**. Privacy establishes
retention **ceilings**. **Both bind.** Full reconciliation is in [privacy.md](privacy.md).

### Field-level redaction

Change Record **values** are privacy-classified separately from Change Record **metadata**. Values
may be redacted; the fact that a change occurred, its subject, field class, actor, Effective Time,
Recorded Time, removal authority, and record identity survive.

**A redacted record remains a record.** Redaction must not silently convert *"something changed but
the value is no longer retained"* into *"no change occurred."*

### Tombstones

When a governed record is deleted, purged, or truncated, a Tombstone remains where required. These
must always be distinguishable: no event occurred; no record was created; a record existed but was
purged; deleted; redacted; is unavailable; or is withheld by policy.

**Do not silently truncate history.** This is the direct correction of problems 6 and 7 in Context.

### Snapshot privacy hazard

A Snapshot taken before a field is later redacted would reinstate removed content on reconstruction.
Snapshots must therefore be redactable in place or re-derivable, and **must never reintroduce content
removed under privacy policy**. This hazard is created by the hybrid model and does not exist in the
alternatives, so it is constitutionalised alongside it.

### Never retained through this architecture

Raw voice samples by default; biometric vectors; embeddings; fingerprint payloads; biometric artifact
internals; biometric storage paths; complete raw sensor streams; complete source payloads copied into
Decision Traces.

Retained instead, where policy permits: evidence references, evidence classes, contributor identity,
reason codes, confidence bands, coverage, provenance, and lifecycle transitions.

### Preservation Hold

Operational Trust authorises; each owning responsibility enforces over its own records. A hold is
discoverable, attributable, bounded or periodically reviewed, independent of visibility, and
explainable. **A hold does not automatically increase visibility**, and cannot preserve raw biometric
internals or raw voice samples, because those were never stored.

**Transitive hold integrity:** because Decision Traces use exact version references, holding a trace
must also preserve the governed source versions required to keep it explainable. A held trace whose
required references have been silently purged is a preservation failure. **Do not duplicate
referenced payloads merely to satisfy a hold** — protect the referenced records according to their
canonical owners.

### Evidence Package

A projection over governed records, recording its assembly time, requesting authority, scope, filters,
included and excluded record classes, redactions, missing- and purged-record markers,
withheld-by-policy markers, known gaps, and provenance references. It creates no alternative
historical source of truth, does not become authoritative over the records it summarises, may
legitimately differ when assembled at different times, and **must never claim completeness when gaps
exist**.

---

## Legal and regulatory non-claim

**This architecture does not claim to produce legal-grade evidence.**

HTBW does not assert court admissibility, legal chain-of-custody sufficiency, tamper-evidence
certification, forensic certification, regulatory compliance, or compliance with any legal retention
regime.

Any legal, regulatory, insurance, investigative, or court-admissibility requirement requires separate
professional and technical validation.

**Preservation Hold and Evidence Package are HTBW architectural terms. They are not claims of legal
effect.**

---

## Home Assistant First review

Conducted under **P21** against official Home Assistant documentation, not remembered behaviour.

### Documentation reviewed

| Capability | Official documentation |
|---|---|
| Recorder | `https://www.home-assistant.io/integrations/recorder/` |
| State history — `states` schema | `https://data.home-assistant.io/docs/states/` |
| Events — `events` schema | `https://data.home-assistant.io/docs/events/` |
| History | `https://www.home-assistant.io/integrations/history/` |
| Activity (Logbook) | `https://www.home-assistant.io/integrations/logbook/` |
| Long-term statistics | `https://data.home-assistant.io/docs/statistics/` |
| Long-term statistics — entity requirements, state classes, `RestoreSensor` | `https://developers.home-assistant.io/docs/core/entity/sensor/` |
| State restoration and attribute recording controls | `https://developers.home-assistant.io/docs/core/entity/` |
| Events (developer) | `https://developers.home-assistant.io/docs/dev_101_events/` |
| Config Entries — lifecycle, migration, update | `https://developers.home-assistant.io/docs/config_entries_index/` |
| Assist pipeline events | `https://developers.home-assistant.io/docs/voice/pipelines/` |

**Storage helper: not verified as of this ADR's own Home Assistant First review.** The official Home Assistant
Storage helper developer documentation could not be retrieved during this review. **No Storage helper
documentation link is recorded here, and none is fabricated.** Storage helper behaviour was therefore
unattested by official documentation in this ADR at the time it was written.

> **OD-01's residual — config entry, subentry, or private storage — must not be closed based on
> assumed Storage helper behaviour.** The official documentation must be located and reviewed first.
> **OD-34 has since closed on the persistence model, without relying on any Storage helper
> assumption**, and the mechanism residual it duplicated is now held by OD-01 alone.

**Update (2026-10-06, Issue #146, items 1 and 1-continued).** The Storage helper has since been
verified against official Home Assistant documentation and, where documentation was insufficient,
pinned Home Assistant Core source. Durability, versioned-JSON persistence, migration, corruption
recovery, native Backup coverage, and non-removability (unlike a config entry or subentry) are now all
established — see
[home-assistant-boundary.md, "Storage helper mechanism (item 1)"](home-assistant-boundary.md#storage-helper-mechanism-item-1-2026-10-06)
and
["...continued"](home-assistant-boundary.md#storage-helper--backup-coverage-and-removability-item-1-continued--verified_supported--verified_negative).
**OD-01's persistence-mechanism residual was drafted as DL-92**
([adr-governed-record-persistence-mechanism.md](adr-governed-record-persistence-mechanism.md)) and has
since been **accepted 2026-10-27 (Issue #76, formal acceptance review PASS); OD-01 is closed as
DL-31/DL-92** — this corrects this ADR's own 2026-08-20 "not verified" finding, which is retained above
as the historical record of what was known when this ADR was written.

### Capabilities found

| Capability | What it explicitly provides |
|---|---|
| Recorder `states` | Per-entity state history; `old_state_id` foreign key to the immediately prior state; `last_changed_ts` distinguished from `last_updated_ts`; attributes stored in `state_attributes`, hash-indexed and shared many-to-one so unchanged attributes are not duplicated; `entity_id` normalised into `states_meta` |
| Recorder `events` | Arbitrary custom events; `event_data` hash-deduplicated and shared many-to-one; `event_types` normalised |
| Context identifiers | `context_id`, parent context, and user context, carried on both states and events, and documented as the mechanism by which related events share a context |
| Recorder retention | `auto_purge` nightly; `purge_keep_days` default 10; `auto_repack`; `recorder.purge` and `recorder.purge_entities` actions |
| Recorder filters | `include` and `exclude` by domain, entity, entity glob, and event type, with a documented precedence order |
| Attribute recording controls | Class-level exclusion of state attributes from recorder history, including a match-all form |
| Long-term statistics | Five-minute and hourly aggregate tables; **the long-term statistics table is never purged**; metadata carries a source and supports externally supplied statistics |
| History | History panel, CSV export from the panel, and a history REST endpoint; automatic fall-back from recorder data to long-term statistics beyond the purge window |
| Activity (Logbook) | Reverse-chronological human-readable stream over recorder data, with a service for custom entries |
| Event bus | Fire and listen, with JSON-serialisable data and component-prefixed event names |
| Config Entries | Persistent configuration with a version and a migration hook; update through the sanctioned update function only; documented lifecycle states; subentries |
| State restoration | Restore of last state across restart, including a sensor-specific form preserving the native value |
| Assist pipeline | Structured stage events with defined error codes, plus conversation and device identifiers |

### Home Assistant patterns to evaluate before designing HTBW alternatives

Under **P21**, each of the following must be evaluated before any HTBW equivalent is designed:

- `old_state_id` or equivalent prior-state linkage
- Context ID
- Parent Context ID
- User Context ID
- Deduplicated attributes
- Recorder retention
- Long-term statistics
- Config-entry update and migration patterns
- Assist pipeline event context

Whether Home Assistant context identifiers are adopted as HTBW's correlation and causation
identifiers is **OD-38**.

### Gaps requiring extension

| # | Gap | Consequence |
|---|---|---|
| G1 | **No per-record purge exemption** — purge is global or entity-scoped, with no way to protect a single record | **A Preservation Hold is unimplementable in the recorder.** The decisive gap |
| G2 | **No governed-record versioning** — config-entry versions are schema versions for migration, and updating a config entry produces no change record | A Decision Trace cannot reference a policy version. P30 is unimplementable natively |
| G3 | **No governed non-entity subjects** — subjects are entities or statistic identifiers | Room, Merged Room, Asset, Person, obligation, session, and incident retrieval cannot be expressed |
| G4 | **No governed-Fact semantics** — a state carries no confidence, provenance, coverage, validity, or lifecycle; statistics are numeric-only | Historical Facts cannot be represented |
| G5 | **No field-level historical redaction** — attribute exclusion is permanent and class-level, and cannot redact an already-recorded row | Field-level redaction under retention policy is impossible |
| G6 | **No Tombstone distinction** — purge deletes rows, leaving nothing to distinguish removal from absence | *"No event occurred"* and *"the record was purged"* become indistinguishable |
| G7 | **No per-record retention classification** — retention is a single global setting plus filters | Floors and ceilings cannot coexist per record class |
| G8 | **No durable structured Decision Trace** — the Activity stream records what changed, not why a decision was reached or refused | Decision Traces cannot live there as structured records |
| G9 | **No Preservation Hold semantics** | Holds have no native representation |

---

## Connected-storage implications

The justification is **narrow**. Connected storage is potentially justified for temporal records only
where Home Assistant cannot satisfy required governance — specifically G1, G2, G5, G6, G7, G8, G3,
and G9 above.

**This is not broad permission to create a parallel history system.**

- Connected records remain **anchored** to Home Assistant objects.
- Evidence references **point at** native Home Assistant records rather than copying their payloads.
- Where a referenced Home Assistant record has been purged, the governed HTBW reference resolves to
  an explicit state such as *"no longer retained"* — never *"never existed."*

Potential anchors: Home Assistant Area or HTBW Room; Home Assistant Device or HTBW Asset; Home
Assistant Person; Home Assistant Entity; Context ID; Parent Context ID; User Context ID; and the
decision evaluation identifier.

See [connected-storage.md](connected-storage.md).

---

## Open decisions

None is closed by this ADR.

| ID | Question |
|---|---|
| **OD-37** | Snapshot triggers, cadence, and scope per responsibility |
| **OD-38** | Version identity, correlation, and causation identifier strategy, including evaluation of Home Assistant Context IDs |
| **OD-39** | Preservation Hold authority, duration, review, release, and conflict with deletion |
| **OD-40** | Evidence Package assembly, transport, integrity representation, and audience |
| **OD-41** | Incident and Case object model |
| **OD-33** | **Closed — DL-43, DL-46, DL-47.** Retention is declared inside every governed record and artifact lifecycle rather than in a universal matrix |
| **OD-34** | **Closed — DL-42, DL-44, DL-46, DL-47.** The temporal-persistence model is complete; the representation mechanism is the residual of **OD-01** |
| **OD-35** | Historical query surface and access |
| **OD-36** | Reconciliation of deletion and export obligations with retention floors and Preservation Holds |
| **OD-01** | **Closed — DL-31, DL-92** (accepted 2026-10-27, Issue #76, formal acceptance review PASS). Representation strategy is **DL-31**; the persistence-mechanism residual (Current Projection, Change Record, Snapshot) is **DL-92** — see [adr-governed-record-persistence-mechanism.md](adr-governed-record-persistence-mechanism.md). Decision Trace's own mechanism remains **OD-29**; Snapshot triggers/cadence/scope remain **OD-37** |
| **OD-29** *(amended)* | Now includes purge exemption and Governed Reference resolvability |

### On OD-41

An **Incident** is defined for this adoption as **at least a retrieval scope** over governed records.

This ADR does **not** constitutionally state that an Incident can never become a durable object.
Whether an Incident or Case becomes a persisted object — with identity, title, description, status,
scope, reviewer notes, hold references, package references, review history, resolution, and closure
reason — is **OD-41**, and is not decided here.

Should it be adopted, it would create **no new responsibility**: Foundation would define the model,
Operational Trust would govern authority, and Concierge could coordinate creation, assembly,
narration, and export.

---

## Consequences

**Positive**

- The shape of history is owned, so it is not invented per responsibility.
- *What changed, when, who, why, from which version* is answerable from records rather than from
  comparison.
- Historical explanation survives later configuration and policy change.
- Preservation holds and evidence packages become expressible.
- The architecture aligns with, rather than duplicates, Home Assistant's own temporal design.

**Costs and obligations**

- Every governed change must produce a Change Record, which is a new obligation on every
  responsibility.
- Version identity must exist before Decision Traces can reference versions.
- Snapshots introduce a redaction hazard that must be actively managed.
- Transitive hold integrity makes holds more expensive than they first appear.

**Risks**

| Risk | Mitigation |
|---|---|
| P29 drifts into implementation detail | The principle names no database, format, cadence, or identifier scheme; if a revision cannot avoid technical nouns, it has drifted and belongs in the model, not the constitution |
| The narrow connected-storage justification is read broadly | The justification is enumerated gap by gap, and the anchoring and no-shadow-store rules are restated |
| Snapshots silently defeat redaction | The snapshot privacy hazard is constitutionalised alongside snapshots |
| Change Records are read as Domain Events | The distinction is stated in the principle, the model, and the glossary |
| Preservation Hold is read as a legal instrument | The explicit non-claim, repeated in four documents |

---

## Validation requirements

1. **Terminology consistency** across the canonical tier for every new term.
2. **No Household Memory revival.**
3. **Ownership uniqueness** — every history has exactly one owner; no eighth responsibility implied.
4. **Domain Event versus Change Record** distinction stated and never collapsed.
5. **Retention floor-and-ceiling consistency.**
6. **Snapshot-redaction protection** present wherever snapshots are described.
7. **Tombstone requirement** present and referenced from failure behaviour.
8. **Legal and regulatory non-claim** present verbatim in the four required documents.

Additionally, the following scenario must pass: a Decision Trace produced under one policy version
must still explain correctly after that policy is later changed, resolving the exact version applied
at the time, **without any full policy payload having been copied into the trace**. If that cannot be
demonstrated, **P30 is not correctly expressed**. See
[../scenarios/why-did-this-happen.md](../scenarios/why-did-this-happen.md).

---

## Related documents

- [adr-historical-explainability-and-historical-truth.md](adr-historical-explainability-and-historical-truth.md)
- [../models/temporal-record.md](../models/temporal-record.md)
- [principles.md](principles.md)
- [privacy.md](privacy.md)
- [home-assistant-boundary.md](home-assistant-boundary.md)
- [connected-storage.md](connected-storage.md)
- [../models/decision-trace.md](../models/decision-trace.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
