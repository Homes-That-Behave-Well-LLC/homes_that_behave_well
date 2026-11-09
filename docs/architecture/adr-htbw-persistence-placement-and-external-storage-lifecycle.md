# ADR: HTBW Repository-Wide Persistence Placement and External Storage Capability Lifecycle

> **Document status: Canonical ADR.**
> Status: **Accepted 2026-11-09.** Records **DL-151** (Issue **#207**, formal acceptance review PASS).
> Canonical authority: [framework.md](framework.md), [adr-governed-record-persistence-mechanism.md](adr-governed-record-persistence-mechanism.md)
> (**DL-92**), [connected-storage.md](connected-storage.md), [home-assistant-boundary.md](home-assistant-boundary.md).
> Terminology: [../models/glossary.md](../models/glossary.md).

---

## Status

**Accepted 2026-11-09.** Formal acceptance review on Issue #207 returned **PASS**. This ADR closes the
repository-wide classification **DL-137's own §17** identified as a necessary follow-on
("HTBW Structured Data Persistence Placement Review"), and formally accepts the External Storage
Capability Lifecycle model the Owner directed and #207/#209/#155 reconciled on 2026-11-09.

**This ADR reopens nothing.** DL-92 (Current Projection/Change Record/Snapshot mechanism), DL-129
(Decision Trace/Explainability authoritative location), DL-137 (Explainability SQLite technology),
DL-110 (Asset Intelligence Adoption custody/scope), DL-120 (HA-Prod/NAS locality), DL-136 (Portability/
Erasure), DL-144 (Voiceprint Gallery singularity), DL-145 (Voice Identity enrollment-evidence
retention), DL-148 (Contextual Governed-Acceptance Placement), and DL-31 (Home Assistant
representation strategy) are each consumed as precedent and binding, unchanged. Where this ADR
appears to restate one of them, the restatement is for the reader's convenience; the cited decision
remains the authority.

**This ADR creates no new responsibility.** The seven responsibilities (DL-01) are unchanged; no
Storage, Persistence, Database, or External-Storage-Capability responsibility is created. Physical
storage still owns nothing (DL-43).

---

## Context

`connected-storage.md` and `adr-governed-record-persistence-mechanism.md` (DL-92) each independently
and correctly decided their own narrow scope: DL-92 chose the Storage-helper-default mechanism for
Current Projection/Change Record/Snapshot; DL-137 chose SQLite specifically for the Explainability
repository; `connected-storage.md` established the governed-namespace and artifact-lifecycle rules for
whatever lands in Connected Storage. **None of them established a reusable, general-purpose decision
tree a future capability could consult without re-deriving placement judgment from scratch**, and none
of them established what happens when a *capability itself* — not merely one artifact — is enabled,
migrated, or disabled. Issue #207 was filed to close that gap. Separately, issue #209 (Voice Evidence
biometric storage governance) and issue #155 (Asset Intelligence legacy capability harvest) each
surfaced the same unanswered question from a different angle: where do durable artifacts that do not
fit a Storage-helper file actually live, and what happens to that storage across a capability's own
lifecycle (not merely one object's).

**Owner Direction, supplied 2026-11-09 and reconciled across #207/#209/#155**, resolved the household-
experience and capability-lifecycle shape. This ADR formally accepts that resolution as architecture,
completes the repository-wide classification matrix DL-137 called for, and determines the remaining
placement questions #209 and #155 were waiting on.

---

## Decision 1 — Repository-wide persistence decision tree

Evaluate, in this order, for every HTBW-governed data class:

| Step | Question | If yes |
|---|---|---|
| A | Is Home Assistant already authoritative for this data (Category 1 of `home-assistant-boundary.md`'s representation strategy — Area, Floor, Device, Entity, Label, Person, Config Entry)? | **Reference it.** Never duplicate. No HTBW store exists for it. |
| B | Is this household/Integration/Person/Room/Merged-Room *configuration* — declared, administrator-authored, naturally expressed as setup/options? | **Home Assistant Config Entry / Subentry / Options flow.** Already the accepted pattern (#201, DL-31). |
| C | Is this static, declarative, human-reviewable configuration that is not better served by a Config Entry/options UI? | **YAML**, only where a Config Entry/options flow is a worse fit than a reviewable file. **No current HTBW data class qualifies** — Config Entry/Subentry/options already covers every class step B would otherwise route to YAML, consistent with Home Assistant's own 2026.11+ config-flow-first direction. This step exists for a future class that might need it; it assigns none today. |
| D | Is this a growing, structured governed record set (Current Projection, Change Record, Snapshot, Decision Trace, Explainability Record, Historical Fact, Communication)? | **Home Assistant Storage helper**, one file per owning responsibility, **by default** (DL-92). **Exception: the single already-accepted Explainability/Decision Trace repository uses SQLite** (DL-137), because that record class is specifically structured, queryable, and growing in the way DL-137 found SQLite — following Home Assistant's own Recorder precedent — materially better suited than a JSON Storage-helper file. **No other class is assumed to belong in SQLite merely because DL-137 chose it for Explainability**; each class's own write/query/volume profile governs (see Decision 3, Classification Matrix). |
| E | Is this large, binary, document, media, or biometric artifact content — or a record class whose own governance (DL-43) already requires Connected Storage, or whose volume/retention profile defeats a single Storage-helper file? | **Governed External Storage** (Connected Storage), under the capability-driven lifecycle this ADR accepts (Decision 2). |
| F | Is this a replaceable technical cache intrinsic to one component's own runtime (a downloaded model artifact, a derived index rebuildable from its own authoritative source)? | **Component-local runtime storage** (e.g., the Voice Evidence App's own `/data`), **never promoted to household-governed storage.** It is not backed up as household data, not referenced by other responsibilities, and its loss triggers re-derivation, not data loss. |
| G | Is this transient runtime state with no governed meaning once the process ends? | **Do not persist**, unless an accepted requirement says otherwise. |
| H | None of the above fit? | **Return an explicit architecture-decision requirement.** Do not force the class into an existing mechanism merely for consistency. |

**A class is never assigned by analogy to a mechanism another class uses.** Each class is evaluated
against this tree on its own profile (owner, volume, query pattern, privacy, retention).

---

## Decision 2 — External Storage Capability Lifecycle (formally accepted)

This accepts, as architecture, the Owner Direction reconciled 2026-11-09 across #207/#209/#155,
building additively on `connected-storage.md`'s already-accepted "Users select storage. HTBW selects
paths" External Storage Contract (not reopened).

### 2.1 Household experience

The household connects External Storage **once**, through the accepted Home Assistant-native
external/network-storage mechanism. **Current Home Assistant evidence identifies Settings > System >
Storage as that native configuration surface** (verified current through `connected-storage.md`'s own
2026.11 revalidation sweep: *"Home Assistant 2026.11 does not change the documented Media-versus-Share
visibility semantics... the release adds a new local-disk storage location type, not a new visibility
rule"*). **This ADR does not hard-code that transient UI path into durable architecture**: any
implementing issue must revalidate the exact current official Home Assistant mechanism immediately
before implementation, because Home Assistant's own configuration surfaces evolve. The durable
architectural commitment is narrower and survives that evolution: *a single native, Home-Assistant-
provided external/network-storage connection, connected once, used by every HTBW capability that
needs durable external storage.*

This is an Integration/household-scoped HTBW capability. The household is never asked to separately
configure storage per HTBW capability (Voice Evidence, Voice Identity, Asset Documents, Explainability,
future Home Steward consumption). Once connected, HTBW owns the organization and lifecycle of
HTBW-managed structures beneath that connection — never the whole storage system, never a sibling
structure it did not create (section 2.6).

### 2.2 Initial HTBW storage initialization

On first acceptance of a healthy External Storage connection, HTBW establishes only its own governed
root (illustrative: `External Storage/HTBW/`; the exact name remains implementation mapping per
`connected-storage.md`'s existing rule, unless a stated interoperability requirement makes one
architectural). **Initialization principle: create only the base structure needed to establish and
validate the governed HTBW storage relationship.** Do not pre-create structures for capabilities the
household has not enabled.

### 2.3 Capability-driven provisioning

Storage structures are created **just in time**, capability by capability:

```text
Household enables capability
        ↓
HTBW determines storage requirements
        ↓
HTBW verifies External Storage is connected and healthy
        ↓
HTBW creates required capability structure
        ↓
HTBW initializes required files/database/schema where applicable
        ↓
HTBW validates required operations
        ↓
Capability becomes ready
```

Applies to Voice Identity, Asset Documents, Explainability (where it elects to use Connected Storage —
see Decision 3), and future accepted capabilities alike, regardless of whether the representation
beneath is files, SQLite, or another accepted durable format. The household never manually creates
folders, files, schemas, or databases.

### 2.4 Capability-driven deprovisioning

Storage lifecycle is **symmetric**, and this is a *capability-level* operation — distinct from the
already-accepted *artifact-level* "governing parent removed → cleanup" rule (`connected-storage.md`),
which still governs what happens when one governed object (one Asset, one Person) is removed:

```text
Household selects Disable
        ↓
HTBW determines the destructive consequences
        ↓
HTBW explains exactly what information will be removed
        ↓
Household explicitly confirms
        ↓
Capability stops
        ↓
Capability-owned active artifacts are deleted
        ↓
Capability-owned storage structures are removed
        ↓
Capability becomes disabled
```

Abandoned capability storage structures and durable artifacts are never left indefinitely after
explicit disable. Data is never silently deleted.

**Stop-capture is distinct from disable-capability, where architecture provides both concepts.**
*Where current authority does not yet distinguish these two semantics for a specific capability, this
ADR does not invent the distinction.* The implementing capability's own issue defines its disable/
delete semantics explicitly before shipping.

### 2.5 Destructive warning model

Before disabling a capability that owns durable artifacts, HTBW determines whether the change deletes
durable information, and if so, tells the household: what capability is being disabled; what classes
of active artifacts will be removed; whether re-enabling later recreates empty structures only;
whether information would need to be regenerated, recaptured, re-enrolled, or reacquired; and that
historical external-storage backup copies, if any, remain governed by the household's own backup-
retention policy rather than HTBW's active-storage deletion (section 2.7). The household is never
required to understand internal filenames, schemas, tables, paths, mounts, or implementation
technology — artifact descriptions are used instead.

**Preservation / higher-order retention (restated, not reopened).** Capability deprovisioning never
overrides an accepted higher-order governed preservation requirement. Where an accepted Preservation
Hold prevents destruction: the capability still stops as appropriate; held artifacts are never
silently destroyed; the household is told truthfully why destruction cannot yet complete; the
accepted higher-order governance is preserved. No new Preservation Hold mechanism is created.

### 2.6 Legacy sibling coexistence

**Connecting External Storage to HTBW does not transfer ownership of all existing files/folders on
that storage to HTBW.** HTBW owns only the governed structures it creates beneath its own accepted
root, unless a separately governed migration (DL-110, Adoption) explicitly transfers an artifact into
HTBW ownership:

```text
External Storage
├── existing / unrelated household content
├── asset_documents/        <- legacy Asset Intelligence ownership where present, untouched
└── HTBW/                   <- governed HTBW ownership
    └── capability structures created as required
```

HTBW must not rename, reorganize, delete, or scan/import legacy sibling structures merely because the
household connected the storage, and must not infer ownership merely from physical proximity. A
sibling `asset_documents/` root beside the HTBW root is expected and valid throughout Asset
Intelligence coexistence and progressive migration (Decision 5; #155's own migration algorithm).

### 2.7 External storage backup responsibility

**The household owns the backup/recovery policy for the connected External Storage capability as a
whole. HTBW capabilities do not independently create backup products.** Voice Evidence does not
schedule backups, replicate backup copies, administer Supervisor Backup, or acquire Supervisor backup
authority merely for biometric artifacts; Asset Documents and Explainability do not create separate
backup systems; a future Home Steward consuming documents does not create a separate storage-backup
mechanism merely because it consumes them. The model: **Household External Storage → household-
defined backup/recovery policy; HTBW manages active artifact lifecycle within that storage.**
External-storage backup history follows the household's own storage backup/retention policy. **HTBW
communicates active deletion honestly**: deleting an artifact from active HTBW storage does not imply
instantaneous deletion from historical external-storage backups (generalizes DL-136's and DL-145's
already-accepted honest-disclosure discipline to every Connected-Storage artifact class, not only the
two each of them separately named).

### 2.8 Failure / degradation (restated, not reopened)

If a capability requires External Storage and that storage becomes unavailable, read-only, full, or
corrupt, the capability is `unavailable`/degraded truthfully (DL-41). It never silently switches to
App `/data`, silently switches to Home Assistant config storage, creates another unmanaged persistent
store, fabricates successful persistence, or silently discards required durable artifacts. When
storage returns, HTBW reconciles and validates before declaring the capability ready again —
`connected-storage.md`'s existing "temporarily unavailable vs. permanently replaced" distinction
applies unchanged.

### 2.9 Consistent lifecycle principle

```text
ENABLE    → PROVISION       (just-in-time, capability-scoped)
MIGRATE   → COPY / VERIFY / TRANSFER OWNERSHIP / VERIFY RESOLUTION / CLEAN LEGACY
DISABLE   → WARN / CONFIRM / DELETE ACTIVE ARTIFACTS / CLEAN STRUCTURE
UNINSTALL → REMOVE WHAT REMAINS YOURS, SAFELY (verify ownership/content before destructive
            cleanup; never recursively destroy unexpected/unverified content)
```

Applies regardless of whether the governed persistence representation is files/directories, SQLite, or
another accepted durable mechanism.

---

## Decision 3 — Repository-wide classification matrix

| Data Class | Canonical Owner | Nature | Preferred Persistence | Physical Placement | Rationale / Authority |
|---|---|---|---|---|---|
| Area, Floor, Device, Entity, Label, Person (native), Config Entry | Home Assistant | Native registry | **Reference only** | Home Assistant | Category 1, `home-assistant-boundary.md` representation strategy |
| HTBW household Integration configuration | Foundation | Configuration | **Config Entry** | Home Assistant `.storage/core.config_entries` | DL-31; already implemented (#162, #201) |
| Room / Merged-Room configuration | Foundation | Configuration | **Config Subentry** | Home Assistant, beneath household entry | #201 accepted implementation; DL-31; DL-68 |
| Asset configuration, Asset relationships | Foundation | Current Projection | **Storage helper** | Home Assistant `.storage/` | DL-92 (Current Projection → Storage helper, native, never moved) |
| Stewardship configuration, obligations (condition + lifecycle, DL-48) | Stewardship | Current Projection + Change Record | **Storage helper** default; Connected Storage only if External History Retention (DL-42) is explicitly configured | Home Assistant `.storage/`, optionally extended | DL-92, DL-42, DL-47, DL-48 |
| Identity configuration (consent gate, retention-policy declaration) | Identity | Configuration | **Config Entry / options** | Home Assistant | DL-31, DL-56, DL-148 |
| Identity Assertions, where persisted | Identity | Governed record, retained with its supporting Decision Trace/history (DL-47) | **Same mechanism as the Decision Trace/history it supports** | Follows Explainability placement (Connected Storage, SQLite) | DL-47: *"retained with the Decision Trace or governed history it supports, never under a separate universal duration"* |
| **Voiceprints** | Identity (governance); App (technical store/lifecycle executor) | Internal Runtime Artifact, biometric | **Governed External Storage** (not App `/data`) | HA-Prod-admitted Share-usage Connected Storage namespace (Decision 4) | DL-43, DL-120, DL-144; #209 reconciliation |
| **Retained ten-recording enrollment sets** (RETAIN=YES only) | Identity (governance); App (technical store/lifecycle executor) | Internal Runtime Artifact, biometric source evidence | **Governed External Storage** | Same namespace as Voiceprints (Decision 4) | DL-145; #209 reconciliation |
| Truth current-state Facts | Truth | Evidence, not persisted independently | **Reference native entity state**; no HTBW copy | Home Assistant | `home-assistant-boundary.md`: "No copy for the purpose of having a copy" |
| Truth Historical Facts | Truth | Queryable Historical Record | **Storage helper** default; Connected Storage if External History Retention configured | Home Assistant `.storage/`, optionally extended | DL-92, DL-42, DL-47 |
| Continuity preferences / remembered values | Continuity | Current Projection | **Storage helper** | Home Assistant `.storage/` | DL-92 |
| Operational Trust configuration / policy | Operational Trust | Configuration + Current Projection | **Config Entry/options** + **Storage helper** for any growing override record | Home Assistant | DL-31, DL-92 |
| **Explainability records / Decision Trace** | Each responsibility produces; one shared repository | Queryable Historical Record, append-heavy | **SQLite** (verified exception to the Storage-helper default) | **Governed External Storage**, Share-usage namespace (unchanged from DL-129/DL-137) | DL-129, DL-137 — not reopened; this ADR confirms the capability-lifecycle model (Decision 2) now applies to it explicitly |
| Communications records | Concierge (orchestration); content/metadata classified separately (OD-49) | Current Projection + Change Record | **Storage helper** | Home Assistant `.storage/` | `adr-communication-object-persistence.md`, DL-138, DL-47 — not reopened |
| Portability metadata (Transient Export Artifact) | Requesting responsibility, orchestrated | Managed Content, short-lived | **Governed External Storage**, transient | HTBW root, auto-expiring | DL-136 |
| Tombstones | Each responsibility whose record it marks | Governed record, structural floor | **Same mechanism as the record class it tombstones** | Follows the tombstoned record | DL-47: *"a Tombstone outlives the record it marks, for the same reason"* |
| Preservation Hold metadata | Operational Trust authorizes; each responsibility enforces | Governed record, structural floor | **Same mechanism as the held record** | Follows the held record | DL-47, `adr-preservation-hold-governance.md` |
| **Asset Documents** | Foundation (anchor); Stewardship (significance, not the artifact) | Managed Content, document | **Governed External Storage** | Share-usage namespace, stable-identifier-keyed (Asset Subject ID + opaque document ID) | DL-43 (already accepted artifact class); DL-110 (Adoption keying precedent) |
| Connected Storage artifact references (governed reference metadata) | The owning responsibility | Part of the owning record's Current Projection | **Storage helper** (the reference); the artifact itself in Connected Storage | Home Assistant `.storage/` for the reference | `connected-storage.md`, "Artifact reference contract" |
| Home Steward / Household Knowledge Provider configuration | Future Home Steward product, reusing HTBW's single External Storage relationship | Configuration (if any) + derived indexes/embeddings | **Config Entry/options** for configuration; indexes/embeddings **not architected by this ADR** (Decision 6) | Not decided here | DL-81 (`adr-household-knowledge-provider-governance.md`) — consumes Document Storage by reference, never a second authority |
| Model caches (Voice Evidence App's pinned ONNX artifact) | App (technical, non-governed) | Replaceable technical cache | **Component-local runtime storage** (App's own `/data`) | App `/data`, never promoted to household storage | Public, digest-pinned, re-downloadable; #209's own backup-policy table (`backup_exclude`) |
| Transient correlation / runtime state | Each responsibility | Transient | **No persistence** | — | `home-assistant-boundary.md`; DL-43 |

**No row in this matrix is marked accepted without the authority cited in its own "Rationale /
Authority" column.** Rows without a specific prior DL citation (Home Steward indexes/embeddings) are
explicitly left undecided, consistent with Decision 6.

---

## Decision 4 — Canonical Connected Storage structure

**Root.** A single HTBW-managed namespace beneath the household's connected External Storage,
illustrated as `HTBW/` (exact name: implementation mapping, per `connected-storage.md`'s existing
rule, unless a stated interoperability requirement makes one architectural).

**Branch rule (restated, not reopened).** A new branch exists only when an accepted capability
introduces a governed artifact class with a complete DL-43 lifecycle declaration. Folders are not
reserved for capabilities that do not yet exist.

**Usage type (new, generalizing the Issue #146 conformance finding).** Every HTBW-governed artifact
class in Connected Storage defaults to a **Share-usage** network-storage connection, never a
**Media-usage** one, unless a specific, separately accepted requirement for media-browser visibility
exists. This generalizes the #146 finding (predecessor products wrongly placed sensitive artifacts
under a Media-usage path; the remediation was to a Share-usage target) into forward guidance for every
future class, rather than leaving it as a one-off remediation record. Voiceprints, retained
recordings, and the Explainability database are each **Internal Runtime Artifacts or Queryable
Historical Records** (`connected-storage.md`'s own interaction-model taxonomy) and are never resident
media regardless of usage type; Asset Documents are **Managed Content**, opened only through the
owning capability, never through storage browsing — Share-usage keeps them out of the media browser by
default as an additional, non-sole, visibility boundary.

**Keying.** Every HTBW-governed artifact beneath the root is keyed by a stable identifier — the
owning Foundation Subject ID (Asset, Person) plus an opaque per-artifact identifier where more than
one artifact exists per owner — never by display name, reusing DL-110's already-verified Adoption
keying precedent and `connected-storage.md`'s existing "no display-name keys" rule.

**Schema/version marker.** Where a capability's own artifact class requires compatibility
verification across versions (for example, the Voice Identity Voiceprint Compatibility Contract, DL-145
§11), that verification is the owning capability's own metadata, not a filesystem-level marker this
ADR invents.

---

## Decision 5 — Asset Intelligence coexistence and migration compatibility

**#155 (Legacy Capability Harvest — Asset Intelligence) already records the accepted Asset-by-Asset
migration algorithm** (COPY → VERIFY → UPDATE METADATA/OWNERSHIP → VERIFY RESOLUTION → DELETE VERIFIED
LEGACY → REMOVE EMPTY LEGACY STRUCTURE), reconciled 2026-11-09 with this ADR's own Owner Direction. This
ADR confirms the canonical HTBW root (Decision 4) is a valid, Share-usage-appropriate destination for
that migration, and that the legacy `asset_documents/` root coexists safely beside it (Decision 2.6)
without ownership collision. **This ADR does not re-decide the migration algorithm itself — #155 owns
it** — and does not execute any migration.

---

## Decision 6 — Explainability, Home Steward: confirmed and deliberately undecided

**Explainability (DL-137) is confirmed, not reopened.** SQLite remains the accepted technology for the
Explainability/Decision Trace repository. This ADR's only addition is applying the capability-lifecycle
model (Decision 2) to it explicitly: the SQLite database is provisioned when the household's
Explainability-dependent capabilities first require it (just-in-time, per 2.3), and its own backup
scope follows `adr-explainability-persistence-and-retention.md` §8's already-accepted "never assumed
included in an ordinary Home Assistant Backup merely because the database happens to be reachable"
rule — consistent with, and now an instance of, this ADR's own section 2.7.

**Home Steward / Household Knowledge Provider's own indexes and embeddings are deliberately not
architected here.** DL-81 already establishes that Household Knowledge Provider *consumes* Document
Storage and Asset Intelligence associations by reference, never becoming a second authority — that
boundary is unchanged. Whether its own derived indexes/embeddings belong in Connected Storage, a local
database, or another mechanism is **future Home Steward architecture's own question**, to be resolved
against this ADR's decision tree (Decision 1) when that capability is itself accepted in enough detail
to classify. This ADR commits only that, if External Storage is required, Home Steward reuses the
household's single existing connection (section 2.1) rather than requesting a second one, and that its
authorization remains explicitly source/resource-scoped — access to one HTBW storage class never
implies authority over all household data.

---

## Decision 7 — Voice Identity: exact physical-placement conclusion (closes #209's own remaining item)

Consuming Decisions 1–4 together, and #209's own already-reconciled Owner Direction:

- Production Voiceprints and retained enrollment recordings (RETAIN=YES) are placed under the
  canonical HTBW Connected Storage root (Decision 4), in a Voice-Identity-owned branch, keyed by the
  stable HTBW `person_id` (already the App's own internal keying convention, per `storage.py`'s
  person-key hashing — unchanged), using a Share-usage network-storage connection (Decision 4).
- The branch is created just-in-time, when Voice Identity is first enabled and a healthy External
  Storage connection exists (Decision 2.3) — never pre-created.
- The Voice Evidence App remains the authoritative technical store and lifecycle executor; this ADR
  changes *where* its authoritative bytes live, never *who* governs their lifecycle (identity-
  contract.md's App/Integration responsibility boundary, unchanged).
- App operational state (bearer secret, model cache, `app_state.json`) remains in the App's own
  private `/data` (Decision 1, step F) — it is not biometric, not household-durable, and not promoted
  to Connected Storage.
- Backup/recovery of the Voice-Identity branch follows the household's own External Storage backup
  policy (Decision 2.7) — not an App-specific or Integration-specific backup mechanism.
- **The App's access mechanism to Connected Storage (mount visibility from inside the App's own
  container, credentials, or an HTBW-mediated access pattern) is implementation detail for the
  implementing issue, re-validated against current official Home Assistant App/Supervisor
  documentation at that time** — this ADR does not design it, consistent with "do not over-specify
  filesystem implementation."

This closes #209's own remaining "exact physical placement mechanism" item at the architecture level.
The implementing issue still determines the concrete access mechanism and exact directory/representation
detail.

---

## What this ADR does not do

- Does not implement any runtime code, mount any storage, create any actual directory, or move any
  artifact.
- Does not select a NAS vendor, protocol, share name, or credential.
- Does not migrate Asset Intelligence documents or Voice Evidence artifacts.
- Does not execute #163, #155's migration, or #210's distribution split.
- Does not begin real household biometric enrollment — the first-production-enrollment gate (#209)
  is unchanged and still applies.
- Does not architect Home Steward's own future record classes (Decision 6).
- Does not reopen DL-92, DL-129, DL-137, DL-110, DL-120, DL-136, DL-144, DL-145, or DL-148.

## Related documents

- [connected-storage.md](connected-storage.md) — External Storage Contract, governed namespace,
  artifact lifecycle (extended, not replaced, by Decision 2 of this ADR).
- [adr-governed-record-persistence-mechanism.md](adr-governed-record-persistence-mechanism.md) (DL-92).
- [adr-explainability-persistence-and-retention.md](adr-explainability-persistence-and-retention.md)
  (DL-129, DL-137).
- [adr-product-disposition-and-legacy-adoption.md](adr-product-disposition-and-legacy-adoption.md)
  (DL-51, DL-52, DL-110).
- [adr-voice-identity-enrollment-evidence-retention-and-regeneration.md](adr-voice-identity-enrollment-evidence-retention-and-regeneration.md)
  (DL-145).
- [home-assistant-boundary.md](home-assistant-boundary.md) — representation strategy.
- [../contracts/identity-contract.md](../contracts/identity-contract.md) — Voice Evidence App boundary.
- [../governance/decision-ledger.md](../governance/decision-ledger.md) — **DL-151**.
