# ADR: Vocabulary Change and Term-Withdrawal Consequences

> **Document status: Canonical ADR.**
> Status: **Accepted** 2026-11-06. Records **DL-143** (issue **#174**, formal acceptance review PASS).
> Resolves **OD-86** in full.
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Terminology: [../models/glossary.md](../models/glossary.md),
> [../models/contextual-vocabulary.md](../models/contextual-vocabulary.md),
> [../contracts/contextual-vocabulary-contract.md](../contracts/contextual-vocabulary-contract.md),
> [adr-room-configuration-ownership.md](adr-room-configuration-ownership.md).

---

## Status

**Accepted 2026-11-06.** Resolves every OD-86 acceptance criterion and exit criterion. This ADR creates
**no Vocabulary Registry responsibility**, **no new record class**, **no new dependency class**, **no
new Continuity scope**, **no compatibility/deprecation subsystem**, and **no vocabulary alias history
store**. It does not reopen **DL-15**, **DL-27**, **DL-30**, **DL-31**, **DL-33**, **DL-41**, **DL-45**,
**DL-56**, **DL-65**, **DL-66**, **DL-69**, **DL-70**, **DL-73**, **DL-88**, **DL-90**, **DL-92**,
**DL-103**, **DL-104**, **DL-111**, **DL-112**, **DL-113**, **DL-122**, **DL-124**, **DL-126**,
**DL-130**, **DL-133**, **DL-136**, amended **DL-137**, or **DL-140** — each is consumed unchanged.
**OD-13** (inheritance, **DL-70**), **OD-59** (exposure precedence, **DL-66**), **OD-63**/**OD-64**
(attribution/observation, **DL-73**/**DL-111**) are not reopened, narrowed, or absorbed.

---

## Context

`contextual-vocabulary.md`, `contextual-vocabulary-contract.md`, and
`adr-room-configuration-ownership.md` govern how a Vocabulary term **comes into existence** —
creation, native seeding, the seed-once lifecycle, `broken_mapping`, deterministic resolution, and the
prohibition on write-back. Of removal they state only that a withdrawn term "is removed through the
ordinary Room Configuration lifecycle, and its history is retained." **History retained is not habit
preserved** — what the home owes the people who still use the old word was unowned. The superseded
`adr-room-vocabulary-governance.md`, `room-vocabulary-registry-contract.md`, and
`room-vocabulary-registry-model.md` once carried a *managed vocabulary lifecycle* (create, update,
deprecate, retire); the constitutional refoundation's replacement set did not carry the
deprecate-and-retire half forward. **Those documents remain Historical and are not reactivated here —
they are cited only as evidence that the question once had an owner, never as authority for its
answer.**

**Owner direction governing this closure:** a governed vocabulary change, retargeting, or withdrawal
takes effect **immediately** when the new Room Configuration becomes authoritative. The previous term
immediately ceases to apply for current resolution and execution. HTBW creates no implicit alias,
compatibility alias, deprecation window, transition window, grace period, fallback to the old term, or
hidden support for a withdrawn term. **Current vocabulary governs current behavior. Historical
vocabulary governs historical truth. Explainability connects the two** — historical recognition never
reactivates a term for current execution.

---

## Decision

### 1. Current vocabulary is immediately authoritative

**When a governed vocabulary change becomes authoritative, the new vocabulary applies immediately.**
No transition interval exists unless the household explicitly configures both the old and new terms as
current vocabulary. HTBW does not wait one hour, one day, until restart, until the next Room refresh,
until a cache expires, or until the old term's retention expires. This restates, and does not alter,
`contextual-vocabulary.md`'s own Rule 2 (vocabulary is persisted) and Rule 3 (vocabulary is
deterministic) — the authoritative Room Configuration record **is** current vocabulary the moment it
commits; there is no separate activation step to decide.

### 2. Term change, retargeting, and withdrawal are three distinct outcomes

No compatibility behavior is added to any of the three.

| Outcome | Definition | Effect, once authoritative |
|---|---|---|
| **Term change / replacement** | The old term is removed; a new term is introduced for the same or a related target | The new term resolves immediately; the old term no longer resolves |
| **Retargeting** | The term itself remains; its target changes | The new target applies immediately; the old target is historical evidence only |
| **Withdrawal** | The term is removed without replacement | The term stops resolving immediately; historical evidence may still establish that it once existed |

A withdrawn, replaced, or retargeted term no longer participates in current resolution according to
its previous meaning. HTBW does not fall back to historical definitions, search retained vocabulary
history for a historical executable match, silently invoke the previous target, preserve hidden alias
behavior, or interpret user habit as permission to reactivate a term.

### 3. Explicit multiple current terms remain allowed, and are not aliasing

This decision does not prohibit a household from deliberately configuring more than one current term
for the same target, where `contextual-vocabulary.md`'s existing model permits it. If both the old and
new words are explicitly current governed vocabulary, both resolve — this is ordinary current
configuration, never transitional aliasing, and HTBW never automatically creates the superseded
mapping merely because a replacement was configured.

### 4. Current resolution must never search history as fallback

**This is a critical acceptance criterion.** The current vocabulary-resolution path never says
"current lookup failed; search vocabulary history." That would silently make history executable.
Historical search is permitted only under an explicitly historical/Explainability/reconciliation
context (§6, below); current command resolution uses current vocabulary only. A withdrawn term's
immediate-failure behavior reuses `contextual-vocabulary.md`'s and
`contextual-vocabulary-contract.md`'s own already-accepted failure table unchanged: **"term not
configured in this Room"** — state that the term is not configured here, offer to show what is
available, never runtime-search. **No new state, response, or "deprecated vocabulary" runtime
capability is invented.** Where the interaction is conversational, this honestly reuses
`failure-and-degradation.md`'s existing **Not understood** response ("no deterministic HTBW Vocabulary
interpretation is available"), consistent with the already-accepted rule that a failed HTBW Vocabulary
match never silently authorizes an unrelated or materially broader native action (**DL-69**).

### 5. `broken_mapping` remains distinct from withdrawal

A withdrawn term is **not** necessarily `broken_mapping`. It may simply no longer exist in current
vocabulary — a `not_configured_here` resolution, exactly as any never-configured term produces. A
**current** term whose mapped target cannot be resolved remains `broken_mapping`, unchanged
(`contextual-vocabulary.md`'s existing seed-once-lifecycle section). Historical Explainability may
distinguish the two; neither is conflated with the other, and this decision adds no third state.

### 6. Historical vocabulary evidence is read-only, and never executes

**Historical evidence may recognize a previous vocabulary term for Explainability, provenance,
historical reconstruction, historical Decision/Explainability evidence, and diagnosis of why a current
interaction did not resolve.** This recognition **never** makes the previous term valid for current
command resolution or execution. Consuming amended **DL-137** unchanged: an on-demand question ("Why
didn't Movie Time work?") produces a new Explainability Record under the `on_demand_decision_trace`
origin, created now, with its own **Historical/Effective Scope** set to the time of the failed or
historical interaction being explained — never the time of the question. Where authorized, the Home
may report, for example, *"Movie Time was no longer configured when you made that request. The
vocabulary had changed to Cinema."* **That explanation does not reactivate Movie Time, and does not
execute Cinema as a side effect of explaining.**

**Historical/current distinction, stated precisely:**

| | Used for | Never used for |
|---|---|---|
| **Current vocabulary** | Current intent/command/target resolution; current household-facing execution | Historical explanation |
| **Historical vocabulary evidence** | Provenance; Explainability; historical reconstruction; understanding previous decisions; explaining why an old term stopped working; interpreting historical traces accurately | A fallback executor for current resolution |

**Version Identity** (**P30**) is preserved unchanged: a historical Explainability Record or Decision
Trace retains the exact vocabulary mapping and version applicable at its own Effective Time (for
example, "Movie Time → Scene X at vocabulary version V17"); a later vocabulary change never rewrites
that historical identity. Conversely, **if a term was already withdrawn at the time of an earlier
interaction**, Explainability must not imply it was still valid then — temporal truth is preserved in
both directions, restating `decision-trace.md`'s existing "a policy change never rewrites an earlier
trace" rule (**P27**), applied to vocabulary specifically.

**Where historical vocabulary evidence has expired or been deleted** under its own already-accepted
retention policy, Explainability reports evidence unavailable or vocabulary history no longer
retained — it never fabricates the old mapping from current scene names, guesses, Continuity data, user
habit, or native aliases (restating **P15**: uncertainty must remain visible, never converted into
false certainty).

**Disclosure.** Vocabulary history may itself reveal household routines, private Room usage, protected
activities, or occupancy. Explainability of a vocabulary change remains audience-governed exactly as
any other Explainability Projection (**DL-140** unchanged) — Assist does not automatically reveal
vocabulary history merely because someone asks; Operational Trust disclosure rules apply unchanged.

**Interaction path.** Consuming **DL-140** unchanged: a conversational "why" question about vocabulary
uses Assist — endpoint → Assist → Explainability capability → on-demand Decision Trace where required
→ historical vocabulary evidence → Operational Trust/audience governance → Explainability Projection →
Assist → endpoint. **No vocabulary-specific UI, and no separate mobile/kiosk/voice vocabulary
explanation, is created.**

### 7. Household-authored automations, scripts, and scenes are never rewritten

Restating the existing prohibition (`why-did-this-happen.md` Scenario 17) unchanged: HTBW never
automatically edits, rewrites, wraps, migrates, renames, or replaces a household-authored automation,
script, scene, or other named executor merely because vocabulary changes. **Visibility, not repair**:
where HTBW can determine that a household-authored artifact now references a stale or broken
vocabulary-related dependency, the condition is surfaced using the existing governed-reference/failure
architecture (for example, *"The automation Evening Movie still references something that is no longer
valid under the current configuration"*) — using exact current canonical vocabulary and reference
semantics, never claiming the automation is broken absent evidence, and never silently repairing it.

### 8. Retained governed references distinguish historical explanation from current execution

Consuming **DL-27**, **DL-45**, and **P30** unchanged: a governed historical record may reference a
vocabulary mapping, target, version, Room/context, and source artifact exactly as before. **Vocabulary
change does not mutate a historical reference.** A retained reference may still identify "Movie Time →
Scene X under V17" — **that never authorizes interpreting Movie Time as Scene X today.** This
distinction — **resolve for historical explanation** versus **resolve for current execution** — is
explicit and is never collapsed. If a current reference becomes broken (its target no longer exists),
existing broken-reference/reconciliation semantics (**DL-27**'s dangling-reference reporting) apply
unchanged; no vocabulary-specific reference system is built.

### 9. Continuity values are not automatically migrated

**No new Continuity scope is created.** Person-scoped and Room-scoped Continuity remain the only
accepted scopes, restating `continuity.md`'s existing "habit continuity and vocabulary continuity are
review lenses, not Continuity scopes" section unchanged. When a Continuity value was captured under
vocabulary that later changes, HTBW does not automatically rewrite the retained value merely because
its household-facing term changed. Two cases, distinguished explicitly:

- **A. The retained value references the underlying semantic target.** If the underlying governed
  target still exists and the record references that target/version correctly, the remembered value
  remains meaningful — a label change alone does not invalidate semantic identity. Do not rewrite its
  provenance to the new term.
- **B. The retained value depends only on a vocabulary reference that is now broken.** Use existing
  broken-reference/failure/reconciliation semantics (**DL-27**/`failure-and-degradation.md`). Do not
  guess or silently remap using historical vocabulary, and do not invent a Continuity vocabulary
  migration subsystem.

### 10. No new retention rule; honest unavailability where evidence has expired

OD-86 creates no new vocabulary retention duration. Vocabulary history is governed entirely by the
household's own already-accepted configuration-history/Change-Record/version/retention/deletion/
portability architecture (**DL-43**, **DL-44**, **DL-47**, **DL-92**, **DL-136**) — HTBW does not
preserve old vocabulary indefinitely solely to support habit compatibility. Where retention has
expired or erasure has occurred, Explainability is honest about reduced future historical
explainability rather than fabricating a prior meaning (§6, above); no special export class is created
for withdrawn terms beyond what current portability architecture already provides.

### 11. The wake-word sub-question is closed conservatively

**#146 item 11 is complete; its conclusion (HTBW builds nothing — no audio-source provenance
discriminator is justified) is preserved unchanged.** OD-86 inherits nothing from item 11 beyond its
own original scope: the household-facing consequence of *changing* a wake word. **This decision creates
no wake-word ownership, configuration, alias, migration, deprecation window, detection behavior,
persistence, or fallback.** People may continue saying an old wake word; that behavior is governed
entirely by the native configured voice platform, never by an HTBW compatibility mechanism. **Wake-word
Explainability boundary, stated precisely**: if a request never reaches HTBW because the native voice
platform never activates after an obsolete wake word, HTBW may have no event or evidence of that
utterance, and must not claim to explain something it never observed. Where sufficient native evidence
is available through already-accepted mechanisms and current governance permits its use, Explainability
may describe what is actually evidenced — HTBW invents no wake-word telemetry and creates no HTBW
audio-source provenance discriminator.

### 12. Out-of-scope boundaries restated, not reopened

- **OD-13 (vocabulary inheritance across scopes, closed as DL-70)** is a different question and is not
  absorbed here. This decision does not alter Home-scope inheritance, shadowing, or precedence.
- **OD-59 (exposure precedence between HTBW and native Assist exposure, closed as DL-66)** is not
  reopened. Changing vocabulary does not change accepted exposure precedence.
- **OD-63/OD-64 (Behaviour Attribution and native behaviour observation, closed as DL-73/DL-111)**
  remain their own decisions. **DL-111 already confirmed this boundary**: the native `entity_id`-based
  observation anchor never drifts with vocabulary change; this decision restates, and does not alter,
  that finding. A vocabulary change may affect how an observation is *explained*, never how it is
  attributed or observed.

### 13. No write-back to native Home Assistant aliases; seed-once remains unchanged

Restating `contextual-vocabulary.md`'s existing "No automatic write-back" section unchanged: an HTBW
vocabulary change — term change, retargeting, or withdrawal — never writes aliases into Home Assistant,
removes aliases from Home Assistant, synchronizes into native HA alias configuration, derives HTBW
vocabulary from HA aliases after the seed-once lifecycle, or updates native HA aliases on retargeting.
**No write-back direction is reopened.** The current native-seeding lifecycle remains as accepted: OD-86
applies only after the household has governed vocabulary, and HTBW never turns historical vocabulary
into a second seed source or re-seeds a withdrawn term from a surviving native HA alias after the
household has removed it — doing so would defeat household authority over its own governed vocabulary.

### 14. Required answers to OD-86's six open questions

1. **Recognition of a superseded term.** For current execution: **no**. Change and withdrawal are
   immediate; no transitional behavior exists. Historical evidence may recognize the term for
   Explainability and provenance only (§6).
2. **What the home may say.** Through Assist/Explainability, where authorized, the Home may explain
   that a term is no longer configured and, where evidence survives and disclosure permits, identify
   the vocabulary change and current term. Room Configuration owns vocabulary; Explainability/Assist
   presents the governed explanation (§6).
3. **Explanation after the change.** The exact historical vocabulary version remains valid evidence
   under **P30**; on-demand Explainability may use it. Historical recognition never enables execution
   (§6).
4. **Household-authored automations/scripts/scenes.** Never automatically rewritten, wrapped, renamed,
   or migrated. Stale or broken references are surfaced where evidence permits — visibility, not
   repair (§7).
5. **Retained references.** Historical references remain version-accurate. A current broken reference
   uses existing reconciliation/failure semantics. Historical references never become a current
   execution fallback (§8).
6. **Continuity values.** Not rewritten merely because vocabulary changed. The underlying semantic
   target remains valid where independently referenced; a vocabulary-dependent broken reference uses
   existing failure semantics. No new Continuity scope (§9).

---

## Explicit non-goals

- **No Vocabulary Registry, Vocabulary lifecycle, or any new responsibility is created.** Room
  Configuration remains the sole owner of the vocabulary mapping; Concierge remains its consumer only.
- **No new record class, dependency class, or Continuity scope is created.**
- **No compatibility/deprecation subsystem, transitional alias, grace period, or vocabulary alias
  history store is created.**
- **No wake-word ownership, configuration, alias, or compatibility mechanism is created.**
- **No write-back to native Home Assistant aliases, in either direction, is reopened.**
- **DL-15, DL-27, DL-30, DL-31, DL-33, DL-41, DL-45, DL-56, DL-65, DL-66, DL-69, DL-70, DL-73, DL-88,
  DL-90, DL-92, DL-103, DL-104, DL-111, DL-112, DL-113, DL-122, DL-124, DL-126, DL-130, DL-133, DL-136,
  amended DL-137, and DL-140 are not reopened.**
- **No unrelated Owner policy is invented.**

---

## Related documents

- [../models/contextual-vocabulary.md](../models/contextual-vocabulary.md)
- [../contracts/contextual-vocabulary-contract.md](../contracts/contextual-vocabulary-contract.md)
- [adr-room-configuration-ownership.md](adr-room-configuration-ownership.md)
- [../models/continuity.md](../models/continuity.md)
- [../contracts/continuity-contract.md](../contracts/continuity-contract.md)
- [../models/decision-trace.md](../models/decision-trace.md)
- [explainability.md](explainability.md)
- [failure-and-degradation.md](failure-and-degradation.md)
- [../scenarios/why-did-this-happen.md](../scenarios/why-did-this-happen.md)
- [home-assistant-boundary.md](home-assistant-boundary.md)
- [adr-explainability-persistence-and-retention.md](adr-explainability-persistence-and-retention.md)
  (amended **DL-137**)
- [adr-explainability-presentation-and-assist-interaction-path.md](adr-explainability-presentation-and-assist-interaction-path.md)
  (**DL-140**)
- [../models/glossary.md](../models/glossary.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
