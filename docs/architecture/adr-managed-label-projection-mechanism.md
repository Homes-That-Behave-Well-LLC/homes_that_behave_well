# ADR: Managed Label Projection Mechanism

> **Document status: Canonical ADR.**
> Status: **Accepted 2026-11-06.** Records **DL-150** (issue **#141**, formal acceptance review PASS).
> Resolves **OD-68** in full.
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Terminology: [../models/asset.md](../models/asset.md), [home-assistant-boundary.md](home-assistant-boundary.md),
> [../models/glossary.md](../models/glossary.md).

---

## 1. Status

**Accepted 2026-11-06.** Resolves every OD-68 acceptance criterion and all eight of its remaining
questions. This ADR creates **no second authority over Asset Type**, **no second Label registry**, **no
new behavioral-policy mechanism**, and **no new Repairs category**. It does not reopen **DL-30**,
**DL-31**, **DL-65**, or **DL-114** — each is consumed unchanged. It does not decide **OD-69** (already
closed, **DL-61**) or **OD-21** (already closed, **DL-75**).

---

## 2. Context — what was already settled, and what was left open

**DL-31** already settled the architectural requirement: Asset Type is authoritative in HTBW, owned by
Foundation; where a native representation benefits the household, it is created or used **as a
projection, never a second authority**. `asset.md`'s Asset Type section already states the same
conclusion for Labels specifically, naming Device class unavailable for this purpose. **Option A —
namespaced reserved labels with a stable internal HTBW taxonomy key and a stable Home Assistant label
identifier — was the Owner's selected direction**, and is accepted here as the mechanism.

What remained open, recorded against **OD-68**, was the mechanism: naming/namespacing, stable
identification across renames, idempotent seeding, collision handling, taxonomy versioning and upgrade
additions, retirement, and reconciliation reporting — all blocked on an unverified platform capability.

**Issue #146 (2026-10-06, addendum 2026-11-03) discharged the DL-30 burden for this item**:
`homeassistant.helpers.label_registry.LabelRegistry` provides full CRUD (`async_create`, `async_update`,
`async_delete`), read (`async_get_label`, `async_get_label_by_name`, `async_list_labels`), and fires
`EVENT_LABEL_REGISTRY_UPDATED` on every mutation. Label **assignment** lives on the assignable object's
own registry entry (`labels: set[str]`), independently confirmed for the Area registry and, by the
2026-11-03 addendum, for the Device registry. Per `asset.md`'s Native representation section, an
Asset's native backing is a **Device** (or a reference to one or more existing Devices) — never an
Entity and never an Area — so **Device-registry label assignment is the only assignable-target capability
this decision requires, and it is verified**. Entity-registry `labels` remains a reasoned, non-blocking
residual that this decision does not need and does not claim.

**#155 (Legacy Capability Harvest)** recorded that the standalone Asset Intelligence product resolves
debounce policy by matching labels such as `asset_type:painting` and `sensitivity:high` against a
`label_profiles` map every cycle — **running the projection backwards**, with no provenance, a global
and ungoverned namespace, and two competing authorities for the same classification. That evidence
informs this decision (rank-four, not itself authority) and is explicitly rejected as canonical
architecture below (§10).

**DL-114** supplies the general publishing/self-consumption restrictions a native entity or service
would need to satisfy; it does not decide this mechanism and is not reopened. **DL-65** supplies the
general Repairs-eligibility test; it does not decide whether this specific drift is Repairs-eligible or
self-healing, which is this decision's own residual (§13).

---

## 3. Decision — Option A, authority direction

**Option A is accepted**: namespaced reserved labels, identified by a stable internal HTBW taxonomy key
and a stable Home Assistant `label_id`.

**Direction of authority, stated explicitly and never reversed:**

```
Foundation Asset Type  →  HTBW managed projection logic  →  Home Assistant Label
```

Never the reverse. A native Label **never** determines Asset Type, Significance, Stewardship policy,
alerting cadence, debounce policy, risk handling, Operational Trust, or any other governed behaviour.
**Asset Type remains authoritative in HTBW/Foundation. Home Assistant remains the sole authoritative
owner of the native Label object.** The mapping between them is projection metadata, not a second
authority over either.

---

## 4. Reserved taxonomy

HTBW maintains a versioned reserved Asset Type label taxonomy. Each entry conceptually carries:

- a **stable HTBW taxonomy key** (internal, never resident-facing as an identity — e.g. `fine_art`,
  `sculpture`, `collection`, `antique`, `furniture`, `instrument`; examples, not a closed taxonomy, per
  `asset.md`);
- a **current human-readable display name**;
- the **taxonomy version** the entry was introduced in;
- **current or retired** status;
- the **Home Assistant `label_id`** once an HTBW-managed native Label has been created for it.

**The display name is never the stable identity, and the Home Assistant `label_id` is never the Asset
Type identity.** Asset Type remains the classification; the taxonomy key and `label_id` are projection
bookkeeping beneath it. A display-name change never changes the taxonomy key; a native rename never
changes the taxonomy key; a taxonomy-key choice is implementation mapping, not prescribed by this
decision beyond stability.

---

## 5. Namespacing

Reserved labels use a clearly HTBW-managed, collision-resistant, human-readable namespace. The
recommended pattern is:

```
HTBW · Asset Type · <Display Name>
```

for example `HTBW · Asset Type · Fine Art`. The exact punctuation is adjustable only where current
Home Assistant Label naming constraints or repository conventions materially require it; the
architectural requirements are that the name is recognizable as HTBW-managed, recognizable as an Asset
Type projection, collision-resistant, human-readable, and that stable identity never depends on the
exact punctuation. An unnamespaced, visually ambiguous label such as bare `Fine Art` is never used for
a managed projection — that form is reserved for a resident's own label the household owns and HTBW is
not managing.

---

## 6. Ownership proof — a name match is never ownership

**A label name matching the reserved namespace never, by itself, proves HTBW ownership.** HTBW may
mutate, rename, unassign, or reconcile a native Label only where it can prove the Label is part of its
own managed projection, through the stored taxonomy-key ↔ `label_id` mapping (§4) and any further
provenance the current projection-metadata architecture records. Ownership is never inferred from name
alone, because a resident may have independently created a label with the identical display name before
HTBW ever seeded it (§7, Case D).

---

## 7. Idempotent seeding and reconciliation

For each active taxonomy entry, reconciliation evaluates exactly one of four cases:

| Case | Condition | Action |
|---|---|---|
| **A** | Stored `label_id` exists and resolves to the expected HTBW-managed Label | Reconcile permitted projection properties (e.g. display name, where ownership is proven); create nothing |
| **B** | Stored `label_id` exists but the Label no longer resolves | Treat as projection drift, not an Asset Type change; evaluate whether safe recreation is possible without collision (§8); recreate only under the same ownership/collision rules as Case C/D |
| **C** | No stored `label_id`, and the reserved display name does not exist | Create the native Label through the verified `async_create`; capture the returned `label_id`; persist the taxonomy-key ↔ `label_id` mapping |
| **D** | No stored `label_id`, and the reserved display name already exists | **Name collision.** Do not adopt, overwrite, rename, or delete the existing Label; establish a projection defect (§13); do not silently create a second, indistinguishable label |

**Repeated reconciliation of an already-correct state (Case A) creates no new Label and performs no
unnecessary update.** This is the idempotence requirement: seeding, startup, a taxonomy-version bump,
and an `EVENT_LABEL_REGISTRY_UPDATED` notification may all trigger reconciliation (§12), and every one
of them converges on the same result without duplication.

### Resident-created collision (Case D, worked)

Before HTBW seeds `HTBW · Asset Type · Fine Art`, a resident independently creates a Label with that
exact name. HTBW must not adopt it, overwrite it, rename it, delete it, or assign it as though HTBW
created it, and must not attach any behavioral authority to it. Expected outcome: the collision is
detected; HTBW establishes that ownership cannot be proven; the resident's Label is preserved untouched;
no second, indistinguishable Label is silently created; the authoritative Asset Type is unchanged; a
projection defect is established and reported through Repairs only where it is standing and
administrator-correctable (§13).

**No resident-created Label is ever sacrificed to satisfy projection — this holds without exception,
for seeding, rename, assignment reconciliation, Asset Type change, taxonomy upgrade, retirement, and
recovery from drift alike.**

---

## 8. Renames

The HTBW taxonomy key remains stable regardless of any rename. Where the same HTBW-managed Label still
exists (its `label_id` resolves and ownership is proven), a display-name change updates that Label
through the verified `async_update` API — **HTBW never deletes and recreates a Label merely because its
display text changed**, because Home Assistant natively supports update. A **resident-created** Label is
never renamed by HTBW reconciliation, regardless of what its name happens to be.

---

## 9. Asset assignment reconciliation

For an Asset whose authoritative Asset Type is `T`, HTBW computes the single desired managed Label
corresponding to `T` and reconciles the Asset's backing Device assignment so that:

- the desired HTBW-managed Asset Type Label is assigned;
- any **obsolete** HTBW-managed Asset Type Label assignment (for example, left over from a prior Asset
  Type) is removed;
- every unrelated resident-created label on that Device remains untouched;
- every non-Asset-Type HTBW-managed label (if any exists under a separate decision) is left unmodified
  by this reconciliation.

**Reconciliation never clears and rebuilds the full label set.** It operates only on the proven
HTBW-managed Asset Type subset.

### Asset Type change, worked

An Asset's authoritative type changes from Fine Art to Antique through the governed HTBW mechanism.
Expected: the authoritative type changes first, through HTBW/Foundation — never through a native Label
edit; the old managed Fine Art assignment is removed from the Device; the new managed Antique assignment
is added; every resident label on that Device is preserved exactly as it was.

---

## 10. One-way authority: a projected Label is never read back

**Stated explicitly and without exception: a projected Home Assistant Label is never read back as a
behavioral, classification, Significance, Trust, or policy input.**

This formally closes the defect **#155** recorded: the legacy Asset Intelligence implementation keyed
`_resolve_debounce_policy` from label strings such as `asset_type:painting` and `sensitivity:high`,
making a resident's rename or deletion of a flat, global, ungoverned label **silently** change how long a
risk condition could persist before the household was told — authority running through the Label, not
through the authoritative Asset Type. **This direction of authority is rejected as canonical HTBW
architecture and must not be carried forward.** No code of the following shape is ever implemented:

```
if label == "HTBW · Asset Type · Fine Art":
    asset.asset_type = fine_art
```

nor:

```
label → debounce → policy
label → alert cadence
label → Significance
label → risk policy
```

A resident editing, renaming, unassigning, or deleting a projected native Label never silently changes
Asset Type, Asset classification, Significance, Stewardship policy, alerting cadence, debounce policy,
risk handling, Operational Trust, or any governed household behaviour. **A broken projection is a
projection defect. It is never a classification change.**

---

## 11. Class-level defaults

The household outcome the legacy evidence surfaced remains valuable: a painting and a games console may
legitimately warrant different monitoring/alerting defaults, and asking a household to hand-tune every
object individually would be a poor experience. **Where a class-level behavioral default exists or is
later introduced, it attaches to the authoritative Asset Type and its governed configuration — never to
the derived Label.**

```
Asset Type → governed class/default policy → behavior
```

The native Label may make the Asset Type visible and targetable in Home Assistant dashboards,
automations, and targeting. **It never drives policy back into HTBW.** This decision does not create a
new acceptance mechanism, does not decide specific default values, and does not reopen Significance or
Stewardship architecture: a shipped default is a proposal, never a household declaration, consistent
with `stewardship.md`'s existing acceptance discipline.

**Significance-shaped keys are out of scope here.** A legacy key such as `sensitivity:high` is not an
Asset Type, is never migrated into the Asset Type taxonomy, and is never blessed as a managed Asset Type
Label. It is evidence of a household-value/significance concern, already routed to and resolved by
**OD-21 (closed as DL-75)** — this decision does not reopen that closure and makes no further change to
it.

---

## 12. Taxonomy versioning, upgrades, and retirement

**An explicit taxonomy version governs the projection schema and taxonomy.** It does not version Asset
Type itself — Asset Type's own identity is independent of this decision's taxonomy-version counter.

**On a taxonomy-version upgrade:**

- existing stable taxonomy keys remain stable;
- existing `label_id` mappings remain stable wherever the native Label still exists;
- new taxonomy entries are seeded idempotently, exactly as Case C in §7 — a version bump alone never
  forces a full reseed;
- a display-name change on upgrade reconciles only proven HTBW-managed Labels, per §8;
- retirement (below) applies unchanged;
- a collision never establishes ownership, regardless of taxonomy version;
- every reconciliation outcome remains explainable (§14).

**Retirement**: HTBW stops assigning a retired entry's managed Label to new or reconciled Assets, and
removes existing HTBW-managed assignments of it where appropriate. **HTBW never automatically deletes
the Home Assistant Label object itself** on retirement — the Label may remain as a native object a
resident continues to use for other purposes. If a resident later reuses the retired display name or
object for an unrelated purpose, **HTBW never reclaims it.**

**Reconciliation triggers** may include, at concept level: integration startup; an Asset Type change; an
Asset appearing or disappearing; a taxonomy-version change; a relevant `EVENT_LABEL_REGISTRY_UPDATED`
notification; a Device's label-assignment state changing; an administrator resolving a Repairs issue; or
another accepted lifecycle event. The exact mechanism (listener, event subscription, debounced task,
coordinator refresh, startup callback) is implementation mapping, not prescribed here. **No polling
requirement is created** — `EVENT_LABEL_REGISTRY_UPDATED` is consumed where technically appropriate
instead.

---

## 13. Reconciliation failure, transient drift, and Repairs eligibility

**Not every drift condition becomes a Repairs issue.** Where reconciliation can safely and automatically
restore the projection and the condition is transient, it **reconciles silently** — for example, a
resident removes a managed assignment while the managed Label itself still exists and ownership remains
provable, or a startup pass finds an otherwise-valid assignment missing. The household is never nagged
about self-healing projection drift.

**Repairs (DL-65) is used only for a standing, administrator-correctable projection defect**, consistent
with DL-65's own generalized eligibility test and its explicit example of this exact case (*"a native
Label disagreeing with the authoritative Asset Type... remains a configuration condition... escalating
to Repairs only where the divergence separately meets the genuine-defect test"*). Genuine candidates
include: a resident-created reserved-name collision (§7, Case D); a stored `label_id` that cannot be
reconciled safely (§7, Case B); native Label creation or update that repeatedly fails; assignment that
repeatedly fails; an ownership/provenance conflict that prevents safe reconciliation; or a target Device
that cannot support the required native assignment. **Repairs is never raised for a successful automatic
reconciliation, a transient API error that resolves, ordinary startup sequencing, or a resident-created
label simply existing outside the HTBW namespace.**

A Repairs projection, where raised, explains: the authoritative Asset Type; the expected managed Label;
the actual defect; whether a collision exists; whether ownership is uncertain; the affected Device; the
safe corrective action; and confirmation that Asset Type and governed behaviour remain unchanged.
**Resolving a Repairs issue never becomes Asset Type, Label, or classification authority** — if an
administrator changes the actual Asset Type, that happens through the authoritative Asset/Foundation
path, never through the Repairs record. **In every failure mode — creation failure, assignment failure,
missing Label, resident deletion, resident rename — Asset Type and governed behaviour remain unchanged.**

---

## 14. Explainability

Where authorized, Explainability distinguishes: the authoritative Asset Type; the required managed
native Label; the native `label_id`; the current assignment state; the taxonomy version; HTBW-managed
versus resident-created ownership; collision; rename; retirement; the reconciliation action taken;
projection failure; and Repairs status. The Home can answer:

> *"Why does this asset have this label?"*
> **"Because its HTBW Asset Type is Fine Art, which projects to the managed Home Assistant label `HTBW
> · Asset Type · Fine Art`."**

and, where a projected Label disagrees with the authoritative Asset Type:

> **"Projection drift — the authoritative Asset Type remains [T]; the native Label reflects an earlier
> or externally altered state and does not change it."**

---

## 15. Privacy and disclosure

A native Label is Home Assistant-visible state, readable wherever the registry is. An Asset Type label
can disclose that a household owns fine art or another valued class of object — a disclosure the
household may not have intended merely by classifying the Asset. This decision projects only the Asset
Type classification itself, never Person identity or private Significance judgement, into the Asset Type
namespace — `sensitivity:high` and equivalent value-judgement keys are explicitly excluded (§11). Broader
disclosure/exposure restrictions are governed by **DL-114**, consumed and not reopened here.

---

## 16. Retention and artifact impact

No new authoritative artifact class is created. Asset Type remains authoritative under Foundation; the
Home Assistant Label remains the authoritative native object, derived relative to Asset Type; the
taxonomy-key ↔ `label_id` mapping is governed projection metadata under existing architecture, not a
second registry. Home Assistant Recorder/retention consequences for the Label object itself follow
existing Home Assistant behaviour and **DL-114**/**DL-47** where applicable. **No second Label registry
is created.**

---

## 17. Home Assistant First

**Native capability, verified (DL-30 discharged for this item):** `LabelRegistry` full CRUD and read;
`EVENT_LABEL_REGISTRY_UPDATED` on every mutation; assignment held on the assignable object's own entry,
confirmed for Area and Device registries (Issue #146, addendum 2026-11-03). **Device is the only
assignable target this decision requires**, because an Asset's native backing is a Device (`asset.md`,
Native representation) — Entity-registry `labels` remains a non-blocking residual this decision does not
need. No private or unsupported Home Assistant API is invoked anywhere in this mechanism — every
operation uses the documented `LabelRegistry` helper surface. No custom "Asset" or "managed label"
device class is claimed (`asset.md`, already decided). Native state (the Label object) remains
authoritative for itself throughout; HTBW never becomes a second store for it.

---

## 18. Required answers to OD-68

| # | Question | Answer |
|---|---|---|
| 1 | Naming/namespacing | `HTBW · Asset Type · <Display Name>` (§5); stable identity never depends on display punctuation |
| 2 | Stable identification | Stable HTBW taxonomy key + Home Assistant `label_id` (§4); name match alone never proves ownership (§6) |
| 3 | Idempotent seeding | Four-case reconciliation (§7); correct state (Case A) produces no new Label; missing Label (Case B) recovers only safely |
| 4 | Collision handling | Resident-created collision (Case D) is preserved, never adopted/overwritten/renamed/deleted; projection defect raised (§7, §13) |
| 5 | Taxonomy versioning/upgrades | Explicit taxonomy version; stable keys/`label_id`s survive upgrade; new entries seeded idempotently; display changes reconcile only proven managed Labels (§12) |
| 6 | Retirement | Stop assigning; remove managed assignments; never auto-delete the Label object; never silently reclaim a reused name (§12) |
| 7 | Label-management API | DL-30 burden discharged by Issue #146 for CRUD, read, update, events, and Device assignment (§2, §17) |
| 8 | Reconciliation failure | Self-healing transient drift reconciles silently; standing administrator-correctable defects use DL-65 Repairs; projection failure never changes Asset Type or governed behaviour (§13) |

---

## 19. Explicit non-goals

This ADR does **not**: implement the label projection, the reconciliation loop, or any production code;
execute the Asset Intelligence migration; create any new Asset Type; create Significance or Stewardship
policy; decide specific class-level default values or a new acceptance mechanism for them; reopen
**OD-16** or unrelated Voice architecture; reopen **OD-69** (closed, **DL-61**) or **OD-21** (closed,
**DL-75**); reopen **DL-114**'s general publishing/self-consumption restrictions; or claim any private or
unsupported Home Assistant API.

---

## 20. Related decisions

**DL-30** · **DL-31** · **DL-61** (OD-69) · **DL-65** (OD-60) · **DL-75** (OD-21) · **DL-114** (OD-81) —
each consumed unchanged, none reopened.

## 21. Related documents

- [../models/asset.md](../models/asset.md) — Asset Type, Native representation
- [home-assistant-boundary.md](home-assistant-boundary.md) — Label registry verification (Issue #146)
- [../governance/decision-ledger.md](../governance/decision-ledger.md) — DL-150, OD-68
- [../models/glossary.md](../models/glossary.md) — Managed Label, Native Representation
