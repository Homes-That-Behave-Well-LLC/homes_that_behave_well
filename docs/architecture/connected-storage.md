# Connected Storage

> **Document status: Canonical.**
> Governed by the Connected Storage principle (P22) in [principles.md](principles.md).

---

## Why this exists

The same pattern was discovered independently in Asset Intelligence, Voice Identity, and Concierge:
some household information cannot be practically represented inside Home Assistant-native storage
models, yet it must remain firmly attached to the Home Assistant object it describes.

This document makes that pattern canonical instead of leaving each implementation to reinvent it.

---

## Rule

1. **Home Assistant First.** If a Home Assistant primitive can practically represent the
   information, use it. See [home-assistant-boundary.md](home-assistant-boundary.md).
2. **Connected storage is the exception, not the default.**
3. **Every connected-storage record must maintain traceability back to its Home Assistant
   system-of-record object.**
4. Connected storage never becomes a shadow system of record for something Home Assistant already
   owns authoritatively.

---

## Connected Storage is a capability dependency

> **Where an artifact requires Connected Storage, Connected Storage is a dependency of the
> capability — not an optimisation of it.**

Connected Storage is **required** whenever HTBW must persist an artifact that does not practically
fit Home Assistant's native storage or retention model. Where it is absent or unconfigured, the
capability that needs it is **unavailable**, in the sense defined in
[failure-and-degradation.md](failure-and-degradation.md).

| Capability | Requires Connected Storage because |
|---|---|
| Asset documents, manuals, invoices, warranty records | Home Assistant stores no document body for a Device |
| Voiceprints and derived identity profiles | No native store exists, and consent-scoped deletion is required |
| Preservation Hold enforcement | Recorder offers **no per-record purge exemption** |
| Extended historical retention beyond the Recorder window | Recorder retention is global and entity-scoped |
| Historical reconstruction artifacts | No native governed-record versioning exists |
| Materialised Evidence Packages | Only where a package is written down rather than assembled on demand |

**HTBW does not emulate external storage.** Three failures are prohibited outright:

- **No unmanaged local repository.** A capability may not degrade into writing files to an
  undeclared location because Connected Storage was not configured.
- **No silent scope reduction.** A capability may not quietly become a weaker capability that shares
  its name.
- **No duplication into Home Assistant.** An artifact that does not fit a native storage model is not
  made to fit by forcing it into attributes, entity state, or a helper.

Unavailability here is a **dependency outcome** and is explained as one: *"Connected Storage is not
configured, so documents cannot be stored."* It is never rendered as a refusal, a permission failure,
or an identity failure.

### When Connected Storage is lost after artifacts exist

Absence before creation and loss after creation are different conditions, and the second is the more
dangerous one.

| Rule | Statement |
|---|---|
| Suspend creation | New artifact creation and retention extension are **suspended** while persistence cannot be guaranteed |
| Never claim success | **Do not report a write as persisted** when it was not |
| No silent relocation | **Do not recreate artifacts elsewhere**, and **do not fall back to an unmanaged local path** |
| No silent destruction | **Do not delete governed metadata or references merely because storage is temporarily absent.** Temporary unavailability is not deletion |
| Preserve references | Governed references and known metadata are preserved where it is safe to do so, and resolve to *"unavailable"* rather than *"never existed"* |
| Surface the condition | The condition is reported through the accepted degradation and Repairs surfaces |

**Temporarily unavailable** and **permanently replaced** are distinct. A replacement is a governed
change with historical consequences, not a silent re-point. **Reconciliation mechanics — how existing
artifacts are re-verified against restored or replaced storage — are an open implementation matter
and are not settled here.**

---

## Home Assistant is the storage provider

> **HTBW does not own network storage. It uses the connected storage Home Assistant already
> provides.**

Home Assistant natively supports attaching network storage and surfacing it to Home Assistant and
its apps. **That capability is the provider.** HTBW consumes it and owns nothing beneath it.

Verified against Home Assistant documentation for **2026.8.2**:

| Verified platform fact | Source |
|---|---|
| Network storage is added under **Settings > System > Storage**, with **NFS** and **CIFS** (version 2.1+) targets | [Common tasks — OS, Network storage](https://www.home-assistant.io/common-tasks/os/#network-storage) |
| Each target declares a **usage type**: **Backup**, **Media**, or **Share** | [Common tasks — OS, Usage types](https://www.home-assistant.io/common-tasks/os/#usage-types) |
| A **Media** target creates a named directory under `/media`; a **Share** target creates a named directory under `/share`. Both are accessible to Home Assistant and apps | [Common tasks — OS, Usage types](https://www.home-assistant.io/common-tasks/os/#usage-types) |
| Media from connected network storage is **automatically added to the local media browser** | [Setting up local media sources](https://www.home-assistant.io/more-info/local-media/setup-media/#prerequisites) |
| Files under a media directory are **accessible to users logged in to Home Assistant**, unlike the public `www` folder | [Setting up local media sources](https://www.home-assistant.io/more-info/local-media/setup-media/) |
| Additional media directories require explicit `media_dirs` configuration | [Media source](https://www.home-assistant.io/integrations/media_source/#using-custom-or-additional-media-folders) |

**HTBW therefore does not own**, and must not attempt to own:

- Network protocol selection between NFS and CIFS
- Share mounting or unmounting
- Network credentials
- NAS or server discovery
- SMB or NFS implementation
- Host operating-system mount configuration
- General network-storage administration

Those belong to **Home Assistant or the deployment**. HTBW's ownership begins **after** Home
Assistant has made a valid storage dependency available, and covers only what HTBW puts there and
how it governs it.

**Two platform assumptions are recorded rather than assumed away.** The network storage feature
documented above is a **Home Assistant Operating System** capability, and it requires **Home
Assistant OS 10.2 or later**. On other installation types the mount is provided by the deployment
instead. This changes **who provides** the dependency; it does not change HTBW's position, which is
that **HTBW is a consumer of a provided storage dependency in every case** (**DL-41**).

---

## Persistence, not an access surface

> **Connected Storage provides persistence. HTBW provides every governed interaction with the
> artifact.**

**Residents never need filesystem navigation to use an HTBW feature.** Capabilities reach artifacts
through **governed artifact references**, and residents reach them through the capability that owns
them.

The storage namespace is explicitly **not**:

- A general resident file browser
- A second Home Assistant user interface
- A generic document-management system
- An alternative media library
- **A direct authorisation surface**

| Capability | The resident interacts with | Governed operations |
|---|---|---|
| **Asset documents** | The **Asset** and its document list — never the storage hierarchy | List, add, open, review, download, print, delete |
| **Voice Identity** | The **enrollment session** and the **voice profile** | Create session, capture phrases, generate voiceprint, delete temporary samples, delete profile |
| **Activity History** | A **question** — *what happened*, *why did this happen*, *why did this not happen*, *who was supported as present*, *what occurred in this Room in this period* | Retain, query, explain, reconstruct, hold, purge |

**Identity is the only ordinary runtime consumer of a voiceprint**, through the accepted Voice
Identity boundary. A resident does not browse, open, print, download, or directly manipulate a
voiceprint, and **residents do not browse raw history files**.

### Media exposure is a visibility boundary, not a security boundary

Home Assistant's documented behaviour makes **Media**-usage storage visible in the media browser and
**Share**-usage storage not visible there by default. That difference is useful and is recorded — but
its limits are recorded with it.

| Statement | Standing |
|---|---|
| Placing an artifact outside a media-exposed directory **reduces incidental exposure** | Supported by documented behaviour |
| Media files are protected by **Home Assistant authentication** | Documented |
| Media files are therefore restricted to **a specific resident** | **Not established.** The documentation establishes authentication, not per-person authorisation |
| An unlisted or unplayable file type is **inaccessible by every path** | **Not established, and must not be claimed.** The documentation describes playback support, not access control, and the same directories are reachable through file-access apps |

Consequently:

- **Media visibility is treated as an additional visibility boundary, never as the sole security or
  authorisation control.**
- **Artifact access remains governed by HTBW, Operational Trust, privacy, and consent**, which are
  the security boundary.
- **HTBW must not expose sensitive internal artifacts through the media browser for convenience.**
  Voiceprints, temporary enrollment samples, and governed history are **internal runtime artifacts**
  and are not resident media unless a separately accepted requirement explicitly permits it.
- **Asset documents may be opened through the owning capability** using a supported retrieval
  mechanism, **without requiring general storage browsing**.

---

## Governed namespace

HTBW requires **one governed namespace** within the provided storage, organised so that artifact
classes cannot collide, orphan, or blur into one another.

```text
HTBW
    Function or artifact class
        Governing object or artifact instance
            Artifacts
```

Illustrative only — these are **logical** shapes, not accepted paths:

```text
HTBW
    Asset Intelligence
        Asset reference
            Artifacts

HTBW
    Activity History
        Governed history structure

HTBW
    Voice Identity
        Person or voice-profile reference
            Governed artifacts
```

**What is architecture:**

| Requirement | Statement |
|---|---|
| One namespace | A **single HTBW-managed root** within the provided storage |
| Functional separation | Separation by **artifact-owning function or artifact class** |
| Collision-resistant references | Governing objects are referenced by a **stable identifier** |
| No resident-supplied identity | **No resident-supplied path is the authoritative object identifier** |
| No display-name keys | **A display name is never the only storage key.** Renaming a Room, Asset, or Person does not orphan its artifacts |
| Traceable | Every structure resolves to its governing Home Assistant or HTBW object |
| No cross-capability mixing | One capability's artifacts do not live inside another's structure |
| Safe cleanup | Empty dependent structures are removable |
| Migratable | Relocation is achieved by **updating governed references**, not by rewriting hardcoded user-facing paths |

**What remains implementation mapping:** exact root name, folder names, separators, casing, path
depth, and file naming — **unless a specific interoperability requirement makes one of them
architectural**, in which case that requirement is stated explicitly rather than assumed.

**Substructure is not designed ahead of need.** A new branch is introduced **only** when an accepted
capability introduces an artifact class with a complete lifecycle declaration (**DL-43**). Folders
are not reserved for capabilities that do not yet exist.

---

## Artifact reference contract

An artifact is located and governed through a **governed reference**, not through a path a resident
typed or a name a resident chose.

| Element | Requirement |
|---|---|
| Artifact identifier | Stable and collision-resistant |
| Artifact class | Required |
| Owning responsibility | Required |
| Creating capability | Required |
| Governing parent-object reference | Required |
| Home Assistant native-object reference | Where applicable |
| Storage namespace or storage class | Required |
| Relative artifact locator | Required |
| Content or format metadata | **Only as the owning capability requires** |
| Created time | Required |
| Lifecycle policy reference | Required |
| Retention strategy | Required |
| Deletion trigger | Required |
| Consent effect | Where applicable |
| Preservation effect | Where applicable |
| Integrity or version metadata | Where required |
| Availability state | Required |
| Broken-reference state | Required |
| Reconciliation state | Where cleanup or verification may be pending |

Two constraints:

- **Do not copy native Home Assistant registry properties into the reference** merely to populate it.
  A reference **points at** the native object; it does not restate it (**P21**, **DL-31**).
- **Do not expose physical storage paths** through ordinary UI, diagnostics, Repairs, or service
  responses where a governed artifact identifier is sufficient. A path is an implementation detail,
  not a public identifier.

**File formats remain capability-specific.** A document is whatever format the household gave it; a
voiceprint is whatever the voice profile requires; a history record is whatever its record class
requires. **No universal payload schema is imposed**, and none is required for HTBW to locate,
govern, retain, or delete an artifact.

### Artifact interaction models

Every artifact class declares **one** interaction model. This is a governance classification, not a
second artifact model, and it **does not replace the lifecycle declaration** each class must still
make.

| Model | Examples | Governed operations | Resident browsing |
|---|---|---|---|
| **Managed Content** | Asset documents; explicitly saved Evidence Packages; explicitly saved Historical Reconstructions | List, add, open, review, download, print, delete, export | Through the **owning capability**, never through storage |
| **Internal Runtime Artifact** | Voiceprints; temporary enrollment artifacts; internal manifests; capability-specific runtime artifacts | Create, validate, use internally, replace, delete, reconcile | **None** |
| **Queryable Historical Record** | Extended Activity History; governed historical Truth; decision history | Retain, query, explain, reconstruct, hold, purge | **None.** Interaction is by question, not by file |

---

## Governing parent and cleanup

> **Every externally stored artifact declares a governing parent object and a Parent Removal
> Behavior. The ordinary default is cleanup; continued existence requires an accepted reason.**

When a governing parent object is removed, HTBW:

| # | Step |
|---|---|
| 1 | Identifies all dependent artifacts |
| 2 | Identifies all dependent artifact references |
| 3 | Evaluates Preservation Holds, retention floors, consent rules, and other lifecycle constraints |
| 4 | Deletes artifacts no longer governed by a valid retention or preservation requirement |
| 5 | Removes dependent references |
| 6 | Removes empty capability-owned structures |
| 7 | Preserves required Tombstones, Change Records, Decision Traces, and lifecycle evidence |
| 8 | Reports failures through Repairs or accepted degradation behaviour |
| 9 | **Never claims cleanup succeeded when storage was unavailable** |
| 10 | Reconciles incomplete cleanup once the dependency is available again |

**Cleanup never silently overrides** a Preservation Hold, a required retention floor, an Evidence
Package lifecycle, historical explainability, or any other accepted governance. Where a constraint
holds an artifact, the artifact remains — **governed and explained**, not quietly retained.

**Retention and parent cleanup are distinct mechanisms.** Time-window purge does not substitute for
parent-object cleanup, and parent-object cleanup does not substitute for time-window purge. An
object-scoped record class may be subject to both.

### Cleanup while storage is unavailable

Cleanup triggered while Connected Storage is unavailable follows the loss rules above, with one
addition: **the obligation is preserved, not discarded.**

- **Payload deletion is not claimed.** *"Removed"* is not said of something that still exists.
- **A governed pending-cleanup state is retained** using the existing reconciliation model, so that
  later recovery can identify what cleanup remains outstanding.
- **The reference is not silently discarded.** Discarding the reference would convert a pending
  obligation into an orphan.
- **The artifact is not recreated elsewhere.**
- **The dependency condition is surfaced.**
- **Retry and reconciliation timing are implementation mapping**, not architecture.

Reconciliation of this obligation against retention floors and Preservation Holds is owned by
**OD-36**; no separate decision is created for it.

---

## Storage structure boundary

**Conceptual storage classes and the namespace rules above are architecture. Physical layout is
not.** No root name, folder name, path, or file format is accepted here, and none may be treated as
accepted because it appears in an implementation.

---

## Candidate connected-storage content

- Documentation
- Manuals
- Photos
- Warranties
- Service records
- Voice samples
- Voiceprints and derived identity profiles
- Enrollment artifacts
- Room vocabulary definitions
- Room participation definitions
- Assessment outputs
- Stewardship artifacts
- Decision Traces
- Change Records, Snapshots, and Historical Facts — **only** under the narrow justification below

---

## Required traceability

Each connected-storage record carries an explicit reference to its anchor object.

```
HA Device            ↔  Asset documentation, manuals, photos, warranty, service history
HA Person            ↔  Identity profile, identity-evidence associations, consent records
HA Area / Areas      ↔  Room Configuration
Room Configuration   ↔  Vocabulary definitions, participation definitions, exclusions, Room Help
HA Calendar          ↔  Stewardship obligation projections
Decision evaluation  ↔  Decision Trace
HA Context ID        ↔  Correlation and causation linkage (subject to OD-38)
```

Traceability requirements:

| Requirement | Statement |
|---|---|
| Anchored | Every record names the Home Assistant object it describes. |
| Resolvable | A broken anchor is a diagnosable condition, never a silent orphan. |
| Reversible | Deleting the anchor object must produce a defined outcome for the connected record. |
| Provenance-bearing | Every record records where it came from and when. |
| Privacy-governed | Retention, visibility, and deletion follow [privacy.md](privacy.md). |

---

## Temporal records — a narrow justification

Connected storage is **potentially** justified for temporal records **only** where Home Assistant
cannot satisfy required governance. The reviewed gaps are:

- No per-record purge exemption
- No governed-record versioning
- No field-level historical redaction
- No Tombstone distinction
- No per-record retention classification
- No durable structured Decision Trace
- No governed non-entity subjects
- No Preservation Hold semantics

**This is not broad permission to create a parallel history system.** The full review is in
[adr-temporal-record-model.md](adr-temporal-record-model.md); the gap analysis is in
[home-assistant-boundary.md](home-assistant-boundary.md).

### Rules for temporal records in connected storage

1. **Anchor, do not copy.** Evidence references point at native Home Assistant records rather than
   copying their payloads. Potential anchors: Home Assistant Area or HTBW Room, Home Assistant
   Device or HTBW Asset, Home Assistant Person, Home Assistant Entity, Context ID, Parent Context ID,
   User Context ID, and the decision evaluation identifier.
2. **Reference exact versions.** Governed records reference versions, not mutable objects (**P30**).
3. **A purged native record resolves to "no longer retained", never "never existed."**
4. **Do not duplicate referenced payloads to satisfy a Preservation Hold.** Protect the referenced
   records according to their canonical owners.
5. Home Assistant remains the system of record for everything it owns authoritatively. A governed
   HTBW history alongside it is an extension, never a replacement.

### Communication records — a narrower justification still

Governed Communication records and their Change Records are **potentially** justified in connected
storage **only** where a retention floor exceeds what native Home Assistant retention preserves. The
reviewed gaps that support this are narrow:

- **No suppression record** — a notification not sent leaves no native trace
- **No governed retention** — notification history is subject to recorder purge
- **No tombstone** — a cleared or purged notification is indistinguishable from one that never existed

**This creates no general licence to store communication content outside Home Assistant.** The rules
above apply unchanged, and communication **content** and **metadata** are classified separately for
retention. Delivery remains a Home Assistant concern in every case. The full review is in
[adr-resident-communication-and-delivery-separation.md](adr-resident-communication-and-delivery-separation.md).

---

## Prohibitions

- Do not duplicate Home Assistant registry data into connected storage "for convenience".
- Do not use connected storage to bypass a Home Assistant capability that already exists.
- Do not store connected records without an anchor.
- Do not treat connected storage as a reason to introduce a compatibility requirement.
- Do not treat the temporal-record justification as general permission to build a parallel history
  or event store.
- Do not store communication **content** in connected storage for convenience, or because it is
  easier than governing retention where the content already lives.
- Do not build a communication inbox, message store, or delivery queue in connected storage. The
  Household Inbox is a **projection**, not a store.
- Do not emulate connected storage when it is absent. **An unmanaged local repository is not a
  fallback**, and a capability that needs connected storage is unavailable without it.
- Do not introduce an artifact without its lifecycle declarations. **An undeclared lifecycle is a defect,
  not a permissive default.**
- Do not introduce a separate archive tier for aged records. External History Retention is a single
  window that is also the purge boundary.

### Connected storage and Home Assistant Backup

Home Assistant Backup protects Home Assistant. **Connected storage sits outside Home Assistant, and
is therefore outside the backup boundary unless the deployment deliberately places it inside and that
placement has been verified.**

| Rule | Statement |
|---|---|
| No assumed coverage | **Do not claim that connected records are included in a Home Assistant backup** unless the deployment makes it true and the inclusion has been verified |
| Coverage is a deployment property | Whether a mounted path is within backup scope depends on the installation, not on this architecture |
| The justification does not widen | Backup convenience is **not** a reason to move records into connected storage. The narrow justification above is unchanged |
| A gap must be explainable | If governed records are outside backup coverage, that limitation is itself a diagnosable, explainable condition |

Reconciliation with retention floors and Preservation Holds is **OD-36**; export and deletion
mechanics are **OD-09**.

---

## Artifact governance

> **No artifact stored outside Home Assistant may exist without a documented lifecycle.**

Anchoring says *what an artifact belongs to*. It does not say *how long it lives* or *what ends it*.
Every artifact class stored outside Home Assistant must declare all of the following **before it is
introduced**:

| # | Declaration | The question it answers |
|---|---|---|
| 1 | **Artifact Type** | What class of thing is this? |
| 2 | **Owning responsibility** | Which responsibility owns its meaning and lifecycle? |
| 3 | **Creating capability** | Which capability brings it into existence? |
| 4 | **Required dependency** | What must exist for it to be created at all? |
| 5 | **Storage class** | Which governed class does it belong to? **Not a physical path** |
| 6 | **Anchor** | Which native object or governed record does it reference? |
| 7 | **Governing parent object** | What does it belong to, such that removing that thing ends it? |
| 8 | **Parent Removal Behavior** | What happens to it when the governing parent is removed? |
| 9 | **Interaction model** | Managed Content, Internal Runtime Artifact, or Queryable Historical Record |
| 10 | **Retention strategy** | How long is it retained, and on what condition? |
| 11 | **Deletion trigger** | What causes it to be removed? |
| 12 | **Consent effect** | Does consent govern its retention, and does withdrawal delete it? |
| 13 | **Preservation Hold effect** | Can a hold defer its deletion? |
| 14 | **Behaviour when Connected Storage is unavailable** | What happens before it is created? |
| 15 | **Behaviour when storage is lost after creation** | What happens to it and to its references? |
| 16 | **Historical and explainability requirements** | What must remain reconstructable and reportable (**P27**)? |
| 17 | **Access restrictions** | Who may see it, and what must never be exposed? |
| 18 | **Integrity or version requirements** | Where applicable |
| 19 | **Recovery or reconciliation behaviour** | Where applicable |

**A retention strategy need not be a duration.** *"Retained while the anchor asset exists"* is a
complete answer; *"we have not decided"* is not. **Artifact classes do not share one retention
strategy**, and none is imposed on them. An artifact whose retention or deletion strategy is unstated
**must not be created** — the gap is a defect, not a permissive default.

This creates **no artifact registry and no artifact service**. The declaration lives with the
architecture of the artifact class, owned by the responsibility that owns the artifact. **Physical
storage owns nothing.**

### Accepted artifact retention strategies

| Artifact | Owner | Retention | Deletion | Notes |
|---|---|---|---|---|
| **Asset documents** — manuals, invoices, warranties, photos, appraisals, service records | **Foundation**, which owns the Asset and its documentation anchor. **Stewardship owns significance and care, not the document artifact** | Retained while the anchor Asset exists | The Asset is removed, or the resident explicitly removes the document | **No ordinary age-based purge.** A document does not expire because it is old. Deletion respects applicable preservation and retention constraints. Anchored to the native Device representation and the governed Asset record. Unreachable documentation is reported as **unavailable**, never as absence. See [../models/asset.md](../models/asset.md) |
| **Voice enrollment samples** | **Identity**, which owns the enrollment and consent lifecycle | **Temporary.** Retained only as long as required to complete voiceprint generation or an explicitly governed retry | Removed on success, and on cancellation, failure cleanup, consent withdrawal, or expiry under policy | Zero default retention. **Raw samples never become historical identity evidence merely because they existed.** Required only where samples cannot remain transient within an accepted processing boundary. See [../patterns/temporary-artifact-lifecycle-pattern.md](../patterns/temporary-artifact-lifecycle-pattern.md) |
| **Voiceprints and derived identity profiles** | **Identity**, which owns the consent lifecycle; Foundation holds the consent record on the Person | Retained while the governed voice profile remains enabled **and consent remains valid** | Profile removal, or **consent withdrawal** | **Revocation removes the derived profile and its associations, not merely their use.** Biometric internals — vectors, embeddings, payloads, and **storage paths** — are never exposed. **Deleting a voiceprint never rewrites an earlier Identity Assertion**; identity history retains evidence classes and reason codes only. See [../models/person-and-identity.md](../models/person-and-identity.md) |
| **Extended historical records** | The responsibility owning each record | The configured External History Retention period | Governed purge at the configured boundary | Preservation Holds and retention floors take precedence. See below |
| **Preservation Hold** | **Operational Trust** authorises; each responsibility enforces over its own records | A governance **marker or state on governed records** — **not an artifact class of its own** | Released under **OD-39** | **Never a duplicate payload or separate evidence store.** It suspends ordinary deletion where applicable. **Releasing a hold does not itself delete anything** — ordinary retention policy then resumes. Hold metadata follows the accepted historical and privacy model |
| **Evidence Package** | **Concierge** and **Operational Trust** | **Not retained by default.** A projection assembled on demand | Not applicable while it remains a projection | Where a resident or deployment **explicitly saves or exports** a package, **the saved copy becomes an artifact** and must declare its own lifecycle, access, and preservation behaviour. **Retention never makes it legal proof.** Assembly, transport, integrity, and audience remain **OD-40** |
| **Historical Reconstruction** | The responsibility owning the reconstructed records | **Not retained.** A projection, never a store (see [../models/temporal-record.md](../models/temporal-record.md)) | Not applicable while it remains a projection | Where a reconstruction is **explicitly saved or exported**, the saved copy becomes an artifact and must declare a lifecycle. **No persistent reconstruction store is created by implication** |

Consent and Preservation Hold both act on deletion and must be evaluated before it: consent
withdrawal **causes** deletion, and a Preservation Hold **defers** it. Their reconciliation with
retention floors is **OD-36**.

### Parent Removal Behavior by artifact class

| Artifact | Governing parent | Interaction model | Behaviour when the parent is removed |
|---|---|---|---|
| **Asset document** | The **Asset** | Managed Content | Deleted unless an overriding retention or preservation rule applies. Asset-specific structures are removed when empty |
| **Voice enrollment sample** | The **enrollment session** | Internal Runtime Artifact | Removed on completion, cancellation, failure, or session expiry |
| **Voiceprint or derived profile** | The **voice profile**, and above it the **Person** | Internal Runtime Artifact | Deleted with the profile; deleted with the Person; **no orphan profile remains** |
| **Extended historical record** | Its **record class**, and where object-scoped, the object | Queryable Historical Record | Object-scoped records follow the object; time-scoped records follow the retention window. **Both mechanisms apply where both are relevant** |
| **Saved Evidence Package** | The **package record** that caused it to be saved | Managed Content | Its declared Parent Removal Behavior governs; holds and retention rules are honoured first |
| **Saved Historical Reconstruction** | The **record that caused it to be saved** | Managed Content | As above |

**Native Home Assistant objects follow their own lifecycle** and are never deleted merely because an
HTBW artifact structure was cleaned. Cleanup runs **downward** from the parent to the artifacts, not
upward.

#### Asset deletion

When an Asset is deleted through governed HTBW behaviour: all Asset-associated artifact references
are enumerated; every Asset document without an overriding retention or preservation rule is
deleted; Asset-specific structures are removed once empty; cleanup failure is **surfaced**; and the
Asset deletion is **not reported complete while mandatory cleanup remains unresolved**, unless the
accepted lifecycle explicitly supports a pending-cleanup state. Historical governance records may
remain where required, **but they must not retain the document payload without authority**.

Deleting a **single Asset document** deletes that artifact, removes or tombstones its governed
reference under the accepted lifecycle rules, may remove empty dependent structures, and **leaves the
Asset in place**. Ownership is unchanged: **Foundation owns the Asset and its documentation anchor**,
and Stewardship owns significance and care.

#### Voice Identity deletion

| Event | Required behaviour |
|---|---|
| **Enrollment succeeds** | Temporary recordings are removed; working artifacts are removed or minimised under their lifecycle; cleanup failure is surfaced. A voiceprint is **not claimed successfully complete** while mandatory sample cleanup is outstanding, unless the accepted model explicitly distinguishes *generated* from *cleanup-complete* |
| **Enrollment is cancelled or fails** | Recordings and working artifacts follow governed cleanup; **no unmanaged recording remains indefinitely**; **no voiceprint is claimed** |
| **Voice profile is deleted** | Voiceprint artifacts and remaining derived profile artifacts are deleted; references are removed or tombstoned; **earlier Identity Assertions remain historically unchanged** |
| **Person is deleted** | Every Voice Identity profile and artifact governed by that Person is evaluated for cleanup; payloads are removed unless preservation or retention authority requires otherwise; consent records and historical governance records follow their own accepted lifecycle; **no orphan voice profile remains** |

**Voiceprint internals and their storage paths are never exposed**, including during cleanup and in
any failure report.

#### Room-scoped artifacts — a rule held in reserve

**No Room artifact class is created here.** If a future accepted capability introduces Room-scoped
external artifacts, its declaration must state Parent Removal Behavior for the Room. On Room removal:
Room-scoped artifacts are evaluated for cleanup; references are removed or tombstoned; empty
Room-scoped structures are removed; **artifacts shared with another valid governing object are not
deleted merely because one Room disappeared**; **merged Room and constituent Room ownership is
resolved before deletion**; and preservation and historical requirements remain active throughout.

### External history retention

**Without Connected Storage, HTBW follows Home Assistant retention.** Recorder's configured purge
governs, and HTBW claims nothing beyond it. This is the default and requires no configuration.

**With Connected Storage, retention may be extended** beyond the Home Assistant window as a single
configured value:

| Setting | Values |
|---|---|
| **External History Retention** | Disabled, or a configured period — for example 90 days, 180 days, 365 days, 2 years, 5 years |

The configured value is **both the retention window and the purge window**. Anything older than the
configured period is removed by a **governed recurring purge**, and no separate archive tier is
introduced. **A tier is not created because data is old**; it would require its own justification,
its own lifecycle declaration, and its own review of the Home Assistant First burden of proof. No
*"archive after X, purge after Y"* model exists unless a future decision explicitly governs one.

**Purge frequency is not architecture.** The requirement is that the configured window is enforced
regularly and explainably. Job timing, scheduling, and runtime cadence are implementation choices
and are not fixed here.

Four constraints bound this:

- **The configured period is an ordinary ceiling, not an authority.** It never overrides a retention
  floor required for historical explainability (**P27**), and **a Preservation Hold suspends ordinary
  purge** for the records it covers. Per record class, retention is declared inside the lifecycle
  under **DL-47**, and **four structural floors survive any configured window** — Tombstones,
  consent-lifecycle records, held records, and the versions required to keep a held Decision Trace
  explainable.
- **Purge is not silence.** A record removed by external retention is still distinguishable from one
  that never existed, under the temporal degradation rules in
  [failure-and-degradation.md](failure-and-degradation.md).
- **Changing the configured duration is a governed change.** It must be historically explainable, and
  an earlier decision remains explainable under the setting that applied when it was made (**P27**,
  **P30**).
- **Reducing the duration never silently deletes protected records.** The new window applies subject
  to Preservation Holds and retention floors, and removal follows the accepted lifecycle rules rather
  than taking effect as a bulk erasure.

### Artifact review checklist

Every proposal for a new artifact must answer all ten questions before it is accepted:

| # | Question |
|---|---|
| 1 | Does it require Connected Storage? |
| 2 | Which responsibility owns it? |
| 3 | What structure stores it, and what is its anchor? |
| 4 | What is the retention strategy? |
| 5 | What is the deletion strategy? |
| 6 | Does consent affect its retention, and does withdrawal delete it? |
| 7 | Does a Preservation Hold defer its deletion? |
| 8 | What happens when Connected Storage is unavailable, and what happens if it is lost after the artifact exists? |
| 9 | What dependencies does the capability declare, and which are mandatory? |
| 10 | Is the capability unavailable when a mandatory dependency is missing? |

An unanswered question is an unmet burden of proof (**P21**, **DL-30**), and the artifact is not
introduced.

---

## Deliberately undecided

**The storage provider is decided.** Home Assistant provides the connected storage, and the
namespace, reference contract, interaction models, and cleanup rules above are architecture. **OD-02
and OD-03 are closed by DL-42, DL-43, DL-44, and DL-45.**

What remains is **implementation mapping**, not open architecture: exact root and folder names, path
depth and separators, file naming, and the concrete encoding of each capability's own payload. **File
formats are capability-specific and no universal payload schema is required.** Encryption,
credentials, mount behaviour, backup, replication, and quota belong to **Home Assistant or the
deployment** unless HTBW records an explicit unmet requirement, which it currently has not.

The persistence **model** for Change Records, Snapshots, Historical Facts, and Decision Traces is
settled by **DL-42**, **DL-44**, **DL-46**, and **DL-47**; **OD-34 is closed**. The remaining
**representation mechanism** is the residual of **OD-01**, and the identifier strategy is **OD-38**.
Neither is resolved here. Communication object persistence is **OD-42**, and communication retention
floors and ceilings are **OD-49**. Neither is resolved here.

**Update (2026-10-06, Issue #146 verification pass).** The `Store` helper mechanism itself is now
**partially verified against `home-assistant/core` source** — see
[home-assistant-boundary.md, "Storage helper mechanism (item 1)"](home-assistant-boundary.md#storage-helper-mechanism-item-1-2026-10-06)
for the full DL-30 record. **What is now established**: disk persistence under `.storage/<key>` as
versioned JSON with migration support, debounced (`async_delay_save`) and immediate (`async_save`)
write paths, optional atomic writes, and a documented corruption-recovery path (rename-and-continue,
never silent data loss). **What remains unverified**: whether `.storage/` content is included in
Home Assistant's native Backup feature, and whether Store-backed files are ever presented to a
resident as removable configuration the way a config entry is. **OD-01's residual must not be closed**
on the strength of this partial verification — the backup-coverage and removable-configuration
questions are still open, and OD-34 closed without relying on any Storage helper assumption, because
the persistence *model* never depended on the mechanism.

**The artifact declarations above are a requirement, not a schema.** Requiring every artifact to
state its class, owner, parent, lifecycle, interaction model, and cleanup behaviour decides nothing
about encoding. **DL-47 extends that same requirement to every governed record class**, deletion and
preservation reconciliation remains **OD-36**, and the default value of External History Retention
is a deployment choice rather than an architectural one.

---

## Related documents

- [home-assistant-boundary.md](home-assistant-boundary.md)
- [failure-and-degradation.md](failure-and-degradation.md)
- [privacy.md](privacy.md)
- [../models/temporal-record.md](../models/temporal-record.md)
- [../models/communication.md](../models/communication.md)
- [../patterns/temporary-artifact-lifecycle-pattern.md](../patterns/temporary-artifact-lifecycle-pattern.md)
- [adr-home-assistant-first-and-connected-storage.md](adr-home-assistant-first-and-connected-storage.md)
- [adr-temporal-record-model.md](adr-temporal-record-model.md)
- [adr-resident-communication-and-delivery-separation.md](adr-resident-communication-and-delivery-separation.md)
