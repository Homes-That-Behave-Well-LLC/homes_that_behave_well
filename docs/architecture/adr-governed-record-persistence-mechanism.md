# ADR: Governed Record Persistence Mechanism

> **Document status: Active — subordinate to the HTBW canonical architecture.**
> Canonical authority: [framework.md](framework.md), [adr-temporal-record-model.md](adr-temporal-record-model.md),
> and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Drafts decision **DL-92**, recorded pending formal acceptance review at **Issue #76**.
> **Not yet authoritative. Creates no new responsibility.**
> Terminology: [../models/glossary.md](../models/glossary.md).

---

## Status

**Recorded, pending formal acceptance review (Issue #76). Not yet authoritative.**

Resolves the persistence-mechanism residual of **OD-01**, left open by
[adr-temporal-record-model.md](adr-temporal-record-model.md) ("Deliberately not decided... identifier
encoding, or per-responsibility persistence strategy") after that ADR settled the temporal record
*model* (**DL-26**, **DL-27**, accepted) and after **OD-34** closed on persistence ownership/namespace
(**DL-42**, **DL-44**, **DL-45**, **DL-47**, accepted) without resolving the mechanism. Consistent with
this repository's established practice that a drafted decision is recorded first and separately
undergoes formal acceptance review before being treated as binding.

**This ADR makes no Home Assistant capability determination of its own.** The platform facts it relies
on were independently verified by **Issue #146** (items 1, continued) and are consumed here, not
re-researched. This ADR makes only the **architectural choice** those facts leave open.

This ADR creates **no new responsibility**. The seven responsibilities recorded in **DL-01** are
unchanged, and no central History, Memory, Persistence, or Repository responsibility is created.

---

## Context

**Platform facts (verified by Issue #146, consumed here as input):**

- The Home Assistant Storage helper (`Store`) persists versioned JSON under `.storage/<key>` inside the
  Home Assistant config directory: immediate (`async_save`) and debounced (`async_delay_save`) writes,
  optional atomic writes, schema migration via `_async_migrate_func`, and a documented
  corruption-recovery path (rename-and-continue plus a Repairs issue, never silent data loss).
- `.storage/` is covered by Home Assistant's native Backup feature (included in a full backup, selectable
  in a partial backup).
- No native, resident-facing action independently removes a Store-backed file. Removal is source-level
  only (`Store.async_remove()`, called by the owning integration's own code), never a documented UI
  action — unlike a **config entry or subentry**, which Home Assistant documents as user-created,
  user-removable configuration data, and which this repository's ledger already excludes on that basis
  as structurally unsuitable for immutable historical records.
- Native Home Assistant history (Recorder, Logbook, long-term statistics) cannot hold governed records
  regardless of mechanism choice: no per-record purge exemption (no Preservation Hold is possible), no
  governed-record versioning, no non-entity subjects (Room, Asset, Person, obligation, session,
  incident), no governed-Fact semantics, no field-level historical redaction, no Tombstone distinction,
  no per-record retention classification, and no structured Decision Trace
  (`adr-temporal-record-model.md`, "Gaps requiring extension," G1–G9). **This is why HTBW persists its
  own governed meaning at all (DL-46) — it is not an argument against the Storage helper as the
  mechanism HTBW uses to persist that governed meaning**, since every one of G1–G9 is a property HTBW's
  own schema and code supply, not a property Recorder or the Storage helper must supply.

**What remains genuinely open after these facts:** whether HTBW's own governed records — which the
platform facts above make Storage-helper-admissible — should be persisted there, on Connected Storage,
or split; what happens to a governed record across config-entry reload/removal/re-add; and whether the
chosen mechanism can express retention and honor a future Preservation Hold. This ADR decides those
architectural questions.

---

## Decision — persistence mechanism by record class (DL-92)

### Current Projection

**Mechanism: native Home Assistant Storage helper, one file per owning responsibility. Always native —
never moved to Connected Storage.**

A Current Projection answers *what is true or configured now* and **must not require replay of complete
history during normal operation** (`temporal-record.md`). Runtime availability must not depend on an
optional external dependency: Connected Storage can be absent, and current operation must remain safe
(**DL-41**, **DL-42**). The Storage helper's verified behavior — durable, backup-covered, not
resident-removable — is sufficient and requires no external dependency.

### Change Record

**Mechanism: native Home Assistant Storage helper by default, one file (or bounded set of files) per
owning responsibility. Connected Storage is available solely as the already-accepted External History
Retention extension (DL-42) a responsibility may configure for longer retention than is practical to
keep natively — never as a second, independently authoritative copy.**

The Storage helper is architecturally admissible for immutable Change Records: it is not
resident-removable, it is backup-covered, and because HTBW's own code governs the file's entire
content, HTBW can implement whatever retention, redaction, and hold logic a record class requires — the
mechanism imposes none of its own and forecloses none. **DL-42 already defines the extension path**:
External History Retention is "Disabled by default, in which case HTBW follows Home Assistant
[native-mechanism] retention"; where a household or responsibility configures it, the configured window
becomes "both the retention window and the purge window" for the externally held portion, and "no
separate archive tier is introduced." This ADR does not create a new mechanism for that extension; it
confirms that the already-accepted External History Retention concept is how Connected Storage
participates in Change Record persistence, and that participation is **optional per responsibility**,
never a universal requirement.

**This ADR decides the mechanism for Current Projection, Change Record, and Snapshot only — the three
record classes #76/OD-01 own.** Domain Event and Decision Trace are two further record kinds defined by
[temporal-record.md](../models/temporal-record.md), and their own persistence surfaces remain separately
owned: Domain Event's native-evidence reference mechanics are **OD-64** (#129), and Decision Trace's
persistence surface is **OD-29** (#79), whose own stated options include the Home Assistant Logbook,
Connected Storage, or both — not only the Storage helper. **This ADR does not decide OD-29 or OD-64, and
does not foreclose either from selecting a mechanism different from the one decided here.** A
responsibility is free to apply this ADR's Storage-helper-default pattern to its own Decision Trace or
Domain Event records once #79/#129 make that choice, but that adoption is theirs to make, not an
automatic consequence of this entry.

### Snapshot

**Mechanism: the same mechanism currently holding the Change Records it summarizes, for the same owning
responsibility.**

A Snapshot "is retained no longer than the records it summarises" (**DL-47**) and must never become an
independent source of truth (`temporal-record.md`). A Snapshot's storage location is therefore not an
independent choice: it must co-locate with, and share the lifecycle of, the history it accelerates. If a
responsibility's Change Records move to Connected Storage under External History Retention, that
responsibility's Snapshots move with them; Current Projections are never affected, because Snapshots
never substitute for them. **The Storage helper (or Connected Storage, where configured) supplies only
the persistence mechanics — a file, a write, a migration path.** Snapshot *semantics* — what triggers
one, its cadence, and its scope — remain entirely HTBW's own and are **OD-37**'s question (#83), wholly
independent of which mechanism this ADR selects.

---

## Decision analysis

| | A. Storage helper (native) | B. Connected Storage (mandatory, all classes) | C. Split (native projections, external history) | D. Config entry/subentry |
|---|---|---|---|---|
| Home Assistant First (DL-30) | Satisfied — rank-1 native capability, now verified | Not preferred — skips a satisfying native layer | Satisfied for projections; see A for the native portion | N/A — already excluded |
| Availability consequence | None — no external dependency for any record class | Every historical capability becomes a declared, unavailable-without-it dependency (DL-41) | Current state always available; history only if Connected Storage is required, which this decision does not make it | N/A |
| Retention capability | Full — HTBW's own code governs the file; no native TTL to fight | Full, but only where Connected Storage is present | Same as A for the native portion | N/A |
| Hold capability | Full — nothing purges a Store-backed file automatically | Full where present | Same as A | N/A |
| Deletion/lifecycle consequence | Explicit, source-level only; never an automatic side effect of config-entry removal | Same, plus a second dependency surface to reconcile on removal | Same as A, plus reconciliation across two mechanisms when extension is configured | N/A |
| Backup consequence | Covered by native Home Assistant Backup (verified) | Covered by whatever backs Connected Storage; not HTBW's concern (DL-44) | Both apply to their respective portions | N/A |
| Dependency consequence | None | Mandatory DL-41 dependency for all historical explainability | Mandatory only for the externally extended portion, and only where configured | N/A |
| Complexity | Lowest — one native mechanism | One mechanism, but a hard dependency | Two mechanisms, reconciliation required, but only when the household opts in | N/A |
| Greenfield refactoring risk | Lowest — matches what Issue #76's own comment 0 observed already works in practice (the reference implementation's Change Record shape), without its collisions | Highest availability risk if adopted as a baseline requirement | Low — the "split" only activates per responsibility, on configuration, using an already-accepted mechanism | N/A |

**Recommendation: Option A as the authoritative baseline for all three record classes, with Option C's
split realized only through the already-accepted DL-42 External History Retention extension, never as a
second mandatory mechanism.** Option B is rejected as a *mandatory* baseline because it would make
ordinary historical explainability a declared dependency on hardware most households do not need for
this purpose, which **DL-41**/**DL-42** require to be named and visible, not silently assumed. Option D
remains excluded on the already-verified evidence that a config entry or subentry is user-removable
configuration data.

---

## Config-entry removal / integration lifecycle

**Integration configuration removal is explicitly distinguished from governed-record deletion
authority. They are never equivalent.**

- Unloading the HTBW integration (`async_unload_entry`) does not delete, recreate, or otherwise alter
  any governed record. Current Projections remain on disk; they are simply not being written while
  unloaded.
- Removing the HTBW config entry does not, by itself, delete governed records. Native removal of a
  Store-backed file is source-level only (verified: `Store.async_remove()`, called by owning-integration
  code, never a documented resident-facing action) — so unless HTBW's own code explicitly invokes it,
  removing the config entry leaves governed records exactly where they are.
- **This ADR concludes, as an architectural inference from the verified source-level mechanics above —
  not as an independently tested reload/remove/re-add cycle — that** re-adding the HTBW integration
  after removal would resume reading the same Storage-helper files, because the `Store`'s key and path
  are never tied to the config entry's own lifecycle. **This specific sequence was not empirically
  exercised by Issue #146** and must not be cited as a verified platform guarantee; it is presented here
  as a reasoned conclusion from the verified `Store`/config-entry independence, open to correction if a
  future verification pass finds otherwise.
- A Home Assistant restart does not, by itself, affect Storage-helper-persisted data; `async_load`
  reads what `async_save`/`async_delay_save` last wrote.
- **Governed record deletion requires an explicit governed authority** — DL-45 parent-removal cleanup,
  an accepted OD-36 deletion/preservation reconciliation, a Preservation Hold's own release (OD-39), or
  an accepted retention expiry (OD-05, OD-26, OD-49) — never a side effect of a resident removing or
  reinstalling the HTBW integration itself. This restates DL-45's existing default ("the ordinary
  default is cleanup when the parent disappears") for the specific case of the HTBW integration's own
  config entry: **the HTBW config entry is not itself the "governing parent" of every governed record it
  happens to enable writing** — each record's own governing parent (the Room, Asset, Person, obligation,
  or other Foundation object the record describes) remains the relevant parent for DL-45 purposes,
  unaffected by whether HTBW itself is currently installed.

---

## Retention seam (mechanism only — no retention value decided here)

The selected mechanism must be able to **express and enforce** a Retention Classification per **DL-47**;
it does not supply a default or a value. Because HTBW's own code owns the entire content of its
Storage-helper file(s), per-record retention metadata, a declared floor/ceiling, and selective pruning
are all implementable as ordinary application logic — the mechanism imposes neither a global retention
window nor an inability to differentiate by class.

**A count-based or size-based ring buffer (fixed-length list, oldest-discarded-first) is explicitly
rejected as a conforming retention mechanism**, independent of the record count chosen, because it
cannot express a floor, a ceiling, or a Preservation Hold exemption — it can only express a bound. This
restates, for the mechanism decided here, the collision Issue #76's own evidence comment (Asset
Intelligence rank-4 evidence) already identified: "a Preservation Hold cannot survive a ring buffer."

Retention duration values remain **OD-05**, **OD-26**, and **OD-49** — not decided here.

---

## Preservation Hold seam (mechanism only — no hold governance decided here)

Because nothing purges a Storage-helper file automatically, a hold is implementable as ordinary
application logic: HTBW's own pruning/retention-enforcement code checks hold state before removing a
record, exactly as it must check a retention floor. The mechanism selected here is **hold-capable by
construction** — no mechanism-level change is required once **OD-39** defines hold authority, review,
and release; this ADR only confirms the chosen mechanism will not need to change to support it.

---

## No-second-Recorder restatement

This decision persists only the governed meaning Home Assistant does not already represent (**DL-46**).
It does not persist a second copy of Recorder rows, Logbook entries, long-term statistics, or any other
native history Home Assistant already retains. Where a governed record references native state, it
references it by governed reference (**DL-27**, **DL-31**), never by copying the native payload.

---

## Migration principle (mechanism changes, not identifier strategy)

A future, separately authorized migration to a different physical mechanism must preserve the following,
regardless of mechanism:

- **Canonical record identity survives a mechanism change.** A storage key, file path, or row position
  is never treated as a record's canonical identity.
- **Governed References are not storage-path identities.** A reference resolves through whatever
  identifier scheme **OD-38** eventually establishes, not through where the record happens to be
  physically stored today.
- **Migration cannot silently rewrite historical meaning.** A mechanism change moves records; it does
  not reinterpret, merge, or re-derive them.

This ADR does not decide **OD-38**'s identifier/correlation strategy and does not require Home Assistant
Context IDs or any other specific scheme to be adopted.

---

## Reconciliation with the Explainability architecture

This ADR's mechanism choice is tested against, and does not alter, the already-accepted explainability
invariant — that HTBW captures the governed meaning required for later explanation **when the decision
or change occurs**, rather than reconstructing it later from transient native evidence. That invariant
is constitutional, not newly asserted here: **DL-46** already states plainly that HTBW persists "what
the platform does not naturally represent" and that "durable explanation after native expiry is already
provided and requires no new construct"; **DL-26**/**DL-27** already require governed change and exact
version references rather than copies; and [authority-order.md](../governance/authority-order.md) lists
explainability as a non-negotiable constraint independent of mechanism.

**Why the Storage helper satisfies this invariant without Connected Storage.** Home Assistant's native
Recorder purges by a configured, often short, retention window, and Assist Debug and automation/script
traces are capped at a small number of recent runs (Issue #146, items 1, 6). The Storage helper, by
contrast, has **no native TTL and no forced purge** — HTBW's own code governs its retention entirely.
A Change Record, Decision Trace, or Snapshot held in a Storage-helper file therefore **outlives native
Recorder/Assist-Debug/trace retention by construction**, which is exactly what
[why-did-this-happen.md](../scenarios/why-did-this-happen.md) Scenario 60 ("a native event referenced
by an old Decision Trace has expired") requires: the trace remains valid, and the accepted Fact it
referenced — not a copy of the expired native row — carries what was material. This ADR's mechanism
choice is what makes that scenario's "no longer retained, never never existed" rule implementable
without a second Recorder.

**Why Connected Storage is not required for this invariant to hold.** Scenario 22 ("No Connected
Storage is configured") already establishes that explanations, Truth, and native history "all operate
normally" without it, and that the household is "a smaller home, not a broken one." Connected Storage
only extends retention beyond the native floor (**DL-42**'s External History Retention); it does not
supply the baseline capability to explain a decision at all. Treating it as mandatory for ordinary
historical explainability (rejected Option B above) would contradict Scenario 22 and the **DL-41**
declared-dependency rule.

**What this ADR does not change.** The schema of what is captured at decision time (the Decision
Trace's twenty required elements, a Change Record's constitutionally required fields) is already
settled by [decision-trace.md](../models/decision-trace.md) and
[temporal-record.md](../models/temporal-record.md) and is untouched by this ADR. This ADR answers only
*where* that already-defined content is written, not *what* is written or *when* it is captured.

---

## Relationship to existing decisions, issues, and reviews

| Item | Relationship to this ADR |
|---|---|
| **DL-26**, **DL-27** (temporal record model, accepted) | Reused, not reopened. This ADR supplies only the mechanism the model already anticipated |
| **DL-30** (Home Assistant First) | Satisfied — the native Storage helper is adopted ahead of Connected Storage, consistent with the ordered burden of proof, now discharged for this question by Issue #146 |
| **DL-31** (reference-and-extend, not copy) | Reused. Current Projections never duplicate native Home Assistant state they can instead reference |
| **DL-41** (declared dependencies) | Reused. Connected Storage remains a declared, named, optional dependency for the External History Retention extension only — never a silent or mandatory one |
| **DL-42**, **DL-44**, **DL-45**, **DL-47** (accepted, OD-02/OD-03/OD-34 closures) | Reused, not reopened. This ADR applies the already-accepted ownership, namespace, parent-removal, and retention-declaration rules to the mechanism chosen here; it narrows no prior closure |
| **DL-46** (native activity vs. governed meaning) | Reused, restated explicitly as the no-second-Recorder rule above |
| **Issue #146** (item 1, continued) | Platform-evidence input to this ADR; not re-researched or redecided here |
| **OD-01** (#76) | Resolved by this ADR's **DL-92**, pending #76's own formal acceptance review |
| **OD-05** (#77), **OD-26** (#125), **OD-49** (#118) | Unaffected. Retention *values* remain theirs; this ADR confirms only that the mechanism can express whatever value they set |
| **OD-36** (#82), **OD-39** (#85) | Unaffected. Deletion/preservation reconciliation and Preservation Hold authority/governance remain theirs; this ADR confirms only that the mechanism can honor whatever they decide |
| **OD-38** (identifier/correlation strategy) | Unaffected and not decided here; see Migration principle above |
| **OD-29** (#79), **OD-37** (#83), **OD-42** (#112) | Downstream; see Open-Issue Impact Review in the #76 execution comment for current disposition |
| **OD-64** (native behaviour observation, #129) | Unaffected and not decided here; Domain Event's native-evidence reference mechanics remain theirs |
| Asset Intelligence rank-4 evidence (cited in #76 comment 0) | Used as worked example and counterexample only, per `greenfield-mandate.md`; no implementation choice is carried forward as architecture merely because it already works that way |

---

## Explicit non-goals

- Does not decide retention duration values for any record class (**OD-05**, **OD-26**, **OD-49**).
- Does not decide Preservation Hold authority, creation, review, or release (**OD-39**).
- Does not decide deletion-versus-preservation reconciliation (**OD-36**).
- Does not decide the identifier/correlation/causation strategy, including whether Home Assistant
  Context IDs are adopted (**OD-38**).
- Does not decide Snapshot triggers, cadence, or scope (**OD-37**).
- Does not select database technology, serialization format, or physical file layout beyond "one
  Storage-helper file (or bounded set) per owning responsibility" — exact keys and schemas are
  implementation mapping.
- Does not decide Decision Trace's own persistence surface (**OD-29**, #79) or Domain Event's native-
  evidence reference mechanics (**OD-64**); both remain separately owned and may select a mechanism
  other than the one decided here.
- Does not create a History, Memory, Persistence, Repository, Storage, or Dependency responsibility.
- Does not make Connected Storage a mandatory dependency for any record class.
- Does not reopen **DL-26**, **DL-27**, **DL-30**, **DL-31**, **DL-41**, **DL-42**, **DL-44**, **DL-45**,
  **DL-46**, or **DL-47**.
- **This entry is drafted content, not yet a closed decision; it must not be cited as equivalent to
  DL-01–DL-91 until #76's formal acceptance review records a result.**

---

## Related documents

- [adr-temporal-record-model.md](adr-temporal-record-model.md)
- [../models/temporal-record.md](../models/temporal-record.md)
- [connected-storage.md](connected-storage.md)
- [home-assistant-boundary.md](home-assistant-boundary.md)
- [failure-and-degradation.md](failure-and-degradation.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
- [../governance/open-decision-issue-index.md](../governance/open-decision-issue-index.md)
