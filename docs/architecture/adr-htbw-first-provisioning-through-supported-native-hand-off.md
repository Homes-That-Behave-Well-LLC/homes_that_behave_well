# ADR: HTBW-First Provisioning Through Supported Native Hand-off

> **Document status: Canonical ADR.**
> Status: **Accepted** 2026-11-06. Records **DL-149** (issue **#192**, formal acceptance review PASS).
> Resolves **OD-91** in full.
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Terminology: [../models/glossary.md](../models/glossary.md),
> [../models/room.md](../models/room.md),
> [../models/person-and-identity.md](../models/person-and-identity.md).

---

## 1. Status

**Accepted 2026-11-06.** Resolves every OD-91 acceptance criterion and all five of its remaining
questions. This ADR creates **no new responsibility**, **no parallel Area/Floor/Person hierarchy**,
**no unassigned-Room feature independent of the hand-off mechanism it defines**, and **no private or
unsupported Home Assistant API use**. It does not reopen **DL-16**, **DL-30**, **DL-31**, **DL-65**,
**DL-67**, **DL-68**, **DL-104**, **DL-125** (OD-10), or **DL-139** (OD-77) — each is consumed
unchanged.

---

## 2. Context — the premise re-examined

#192's own prior verification pass (`home-assistant-boundary.md`, "Issue #146 HTBW-first provisioning
verification pass," 2026-10-16) answered a narrower question than OD-91 actually needs: *whether an
integration may independently, silently create or mutate a resident's Area/Floor/Person*. The Owner's
clarification distinguishes that from a **second** question this ADR exists to answer: *whether an
authenticated resident, operating an HTBW-provided configuration experience, may cause Home Assistant
to create a native object through the same supported, documented mechanism Home Assistant's own
frontend itself uses* — a user-authorized action, not integration autonomy.

**This ADR re-verifies the second question directly against current Home Assistant developer
documentation and current `home-assistant/core` source**, per **DL-30**'s ordered burden of proof, and
distinguishes it explicitly from the first question, which remains answered as before.

---

## 3. Phase 1 — Re-verified Home Assistant creation boundary

| Object | HA frontend creation path | Backend mechanism | Supported for HTBW use? | Result/identifier | Resume/reference mechanism | Evidence classification |
|---|---|---|---|---|---|---|
| **Floor** | Settings → Areas & Zones → Floors tab → Add floor | Generic storage-collection WebSocket command (`collection.DictStorageCollectionWebsocket` pattern) registered under the `floor` domain, backed by `homeassistant.helpers.floor_registry.async_create()` | **NOT supported for integration use** | `floor_id` (string) | `my.home-assistant.io/redirect/areas` ("Floors & areas") | **VERIFIED_UNSUPPORTED** — strengthened in this pass (§4) |
| **Area** | Settings → Areas & Zones → Areas tab → Add area | Same storage-collection pattern, backed by `homeassistant.helpers.area_registry.async_create()` | **NOT supported for integration use** | `area_id` (string) | `my.home-assistant.io/redirect/areas` ("Floors & areas") | **VERIFIED_UNSUPPORTED** — reconfirmed, strengthened (§5) |
| **Person** | Settings → People → Add person | Same storage-collection pattern, backed by `homeassistant.components.person.async_create_person()`; optionally also creates a full HA user/login account through a nested, separate dialog | **NOT supported for third-party use** | Person `entity_id` / storage item `id` | `my.home-assistant.io/redirect/people` ("People") | **VERIFIED_UNSUPPORTED FOR THIRD-PARTY USE** — reconfirmed, strengthened (§6) |

**Evidence classification scale used**: `VERIFIED_SUPPORTED`, `VERIFIED_UNSUPPORTED`,
`VERIFIED_INTERNAL_ONLY`, `UNVERIFIABLE`/`UNDOCUMENTED`. None of the three objects is converted from
`UNVERIFIABLE` to `UNSUPPORTED` without evidence (**DL-30**) — each conclusion below states exactly
what was found.

---

## 4. Floor — re-verified and strengthened

**Prior finding** (`home-assistant-boundary.md`, 2026-10-16): "UNVERIFIED, NEGATIVE BY ANALOGY" — no
dedicated Floor-registry developer-documentation page exists, and the conclusion rested on analogy to
Area alone.

**New evidence, this pass:**

- `contributors.home-assistant.io/architecture/core/registries/` (current, fetched 2026-11-06) states,
  in its own registries table: *"Areas and floors | How the user describes their home | Area
  registry"* — Floor is not merely analogized to Area; the current architecture-overview documentation
  **textually groups** Floor with Area as one resident-owned concept, governed by the same linked Area
  registry developer page and its "Areas belong to the user" statement.
- **Exhaustive empirical verification**: a repository-wide code search of `home-assistant/core`
  (`gh search code "floor_registry.async_create(" --repo home-assistant/core`) returns **zero
  production-code matches across the entire codebase** — every result is a test file
  (`tests/components/...`, `tests/helpers/...`). **Not even Home Assistant's own onboarding component
  calls `floor_registry.async_create()`.** Across roughly a thousand bundled integrations, none creates
  a Floor programmatically.

**Conclusion: `VERIFIED_UNSUPPORTED`** — upgraded from analogy to direct textual grouping plus
exhaustive empirical absence of any production precedent anywhere in the ecosystem. This is still not
an explicit per-object prohibition sentence equivalent to Area's; the evidence classification states
the distinction honestly rather than overclaiming a documentation page that does not exist.

---

## 5. Area — reconfirmed and strengthened

**Prior finding**: `VERIFIED_UNSUPPORTED`, based on `contributors.home-assistant.io/core/integrations/
area-registry/`'s explicit statement: *"Areas belong to the user. Your integration does not create or
change them."*

**New evidence, this pass:** that statement is current as of 2026-11-06 (re-fetched directly) and
remains unchanged. It draws no distinction between automatic/silent creation and user-authorized
creation through an integration-provided UI — the sentence is unqualified. **Exhaustive empirical
verification**: `gh search code "area_registry.async_create(" --repo home-assistant/core` returns
exactly **one** non-test production match across the entire codebase —
`homeassistant/components/onboarding/views.py` — Home Assistant's own first-party bootstrap component,
not a third-party-style integration. Every other match is a test file. No bundled integration, despite
hundreds having devices that plausibly "know their own room," creates an Area directly; they use
`suggested_area` instead (§7).

**Conclusion: `VERIFIED_UNSUPPORTED`**, reconfirmed, now with whole-ecosystem empirical backing in
addition to the explicit documentation statement. **The Owner's distinction between silent and
user-authorized creation does not change this conclusion** — it was tested directly against both the
unqualified documentation statement and actual ecosystem practice, and neither supports it.

---

## 6. Person — reconfirmed and strengthened

**Prior finding**: `VERIFIED_UNSUPPORTED FOR THIRD-PARTY USE` — `async_create_person`'s only caller is
Home Assistant's own `onboarding` component.

**New evidence, this pass:**

- Current `homeassistant/components/person/__init__.py` (dev branch, fetched 2026-11-06) confirms
  `async_create_person` remains exported in the module's `__all__` (making it technically importable)
  but unchanged in behavior: it calls `storage_collection.async_create_item(...)` — the same generic
  mechanism the frontend's "Add person" dialog invokes through
  `PersonStorageCollectionWebsocket(collection.DictStorageCollectionWebsocket)`.
- **Exhaustive empirical verification**: `gh search code "async_create_person" --repo home-assistant/
  core` returns exactly **three** matches in the entire codebase: the function's own definition
  (`person/__init__.py`), its sole caller (`onboarding/views.py`), and its own test
  (`tests/components/person/test_init.py`). **Zero third-party integrations call it.**
- **Current official end-user documentation** (`www.home-assistant.io/integrations/person/`, fetched
  2026-11-06) confirms the Person integration's **only** exposed action is `person.reload` (reloads
  YAML) — there is no `person.create` action, and the only creation paths named anywhere are the UI
  (**Settings → People → Add person**) and YAML.
- **Person creation is also security-sensitive beyond Area/Floor**: the "Add person" dialog may
  optionally create a full Home Assistant **user account and login credential** for that Person
  (`www.home-assistant.io/integrations/person/`, "Adding a person to Home Assistant," steps 4–5). This
  is independently a reason this operation is not delegated to integration code, regardless of the
  storage-collection mechanism's technical callability.

**Conclusion: `VERIFIED_UNSUPPORTED FOR THIRD-PARTY USE`**, reconfirmed, now with whole-ecosystem
empirical backing and an additional, independent security rationale (credential creation).

---

## 7. `suggested_area` — scope confirmed, not a general solution

Re-verified directly against `contributors.home-assistant.io/core/integrations/area-registry/`:
`suggested_area` is a field on `DeviceInfo` (or an argument to the device registry's
`async_get_or_create`), applied **only when a device is being registered and does not already have an
Area**. It is explicitly a one-time hint ("Use it when the device or service knows which room it is
in, like a room name set in its own app") — **it is never a general Room/Floor/Person provisioning
mechanism**, and this ADR does not treat it as one.

**Where it applies**: when HTBW orchestrates the addition of a new device (for example, guiding a
resident through a vendor integration's own config flow for a new Zigbee/Z-Wave/Matter device) and
HTBW already knows, from its own Room Configuration, which Room the device belongs to, HTBW **may**
supply the matching native Area name as `suggested_area` on that device's registration. **HTBW supplies
the suggestion; Home Assistant applies it only if the resident has not already set an Area for that
device, and the resident may always override it.** This never creates or mutates an Area itself — it
only pre-fills a native field already designed for exactly this purpose.

**No equivalent "suggested Person" or "suggested Floor" concept exists.** No API surface for either
object accepts a hint value from an integration. HTBW never invents one. For Floor and Person, the only
available path is the hand-off defined in §9–§11.

---

## 8. Phase 2 — Tier selection

Per the ordered preference (Tier 1 — supported native creation orchestrated directly; Tier 2 —
supported hand-off to native creation UI with resume; Tier 3 — explicit hand-off using the best
available mechanism; Forbidden — private/unsupported API use), each object's own verified evidence
(§§4–6) determines its tier **independently**:

| Object | Tier | Why |
|---|---|---|
| Floor | **Tier 2** | No supported direct-creation mechanism (§4); a supported, documented native navigation mechanism exists (§9) |
| Area | **Tier 2** | No supported direct-creation mechanism (§5); same supported navigation mechanism applies |
| Person | **Tier 2** | No supported direct-creation mechanism (§6); same supported navigation mechanism applies |

**None reaches Tier 1.** Home Assistant does not currently support direct, integration-orchestrated
native creation for any of the three objects, even from an authenticated resident's own HTBW
configuration experience. **Tier 1 is not forced where the evidence does not support it.**

---

## 9. The supported hand-off mechanism — My Home Assistant

**"My Home Assistant"** (`my.home-assistant.io`) is Home Assistant's own documented, supported
deep-linking service, already used throughout official Home Assistant documentation (including the
Person integration's own end-user page, which links `Settings → People` through
`my.home-assistant.io/redirect/people`). Its current redirect catalogue
(`github.com/home-assistant/my.home-assistant.io/blob/main/redirect.json`, fetched 2026-11-06)
includes:

| Redirect | Destination | Applies to |
|---|---|---|
| `areas` | The combined "Floors & areas" settings page | Floor, Area |
| `people` | The People settings page | Person |

**This lands the resident on the native settings list page, not a pre-filled "create new" dialog.**
The resident still performs the final "Add Floor"/"Add Area"/"Add person" action themselves, inside
Home Assistant's own native surface — consistent with Tier 2's own definition ("Home Assistant provides
a supported way to launch/navigate/orchestrate the native creation UI," never a claim of direct
invocation). **This is the mechanism this ADR adopts for all three objects.**

---

## 10. Decision — the HTBW-first provisioning experience

```
HTBW Integration Setup
    ↓
Household / Foundation setup
    ↓
Define intended Floors (names captured by HTBW)
    ↓
Hand off to My Home Assistant "areas" redirect (Floors tab) for each not already present
    ↓
Resident returns; HTBW detects/confirms the new native Floor(s) (§12)
    ↓
Define intended Rooms (names, vocabulary captured by HTBW)
    ↓
Hand off to My Home Assistant "areas" redirect (Areas tab) for each Area not already present
    ↓
Resident returns; HTBW detects/confirms the new native Area(s) (§12)
    ↓
Configure HTBW Room/Physical Room extensions (Foundation, unchanged — DL-31)
    ↓
Define household Persons
    ↓
Hand off to My Home Assistant "people" redirect for each Person not already present
    ↓
Resident returns; HTBW detects/confirms the new native Person(s) (§12)
    ↓
Configure HTBW Person extensions (Identity/Continuity/Operational Trust — unchanged ownership)
    ↓
Continue progressive HTBW commissioning
```

**This sequence is illustrative, not a mandated rigid order** — a resident may define Rooms before
Floors, or a Person before any Room, and an already-existing native object short-circuits its own
hand-off step entirely (reference-only, per the issue's own Option A, applied automatically wherever it
already holds). **The architectural invariant**: the resident experiences one coherent HTBW-guided
provisioning journey, while Home Assistant remains the authoritative owner of its native objects.
**Causing a native object to be created through this hand-off never makes HTBW the source of truth for
that object** (**DL-31** unchanged).

---

## 11. Room/Area relationship — a pending link, not a general unassigned-Room feature

**The issue's own Option C ("unassigned Room Configuration state") is accepted only in a narrow,
bounded form, never as a general-purpose standing feature.**

Because Tier 1 is unavailable for Area (§5, §8), a Room Configuration initiated through HTBW genuinely
cannot be backed by a native Area at the moment the resident names it — the hand-off in §9 necessarily
takes time, and Phase 8's own resume requirement (§12) independently requires HTBW to hold *some*
durable state describing what is in progress. **This is not invented merely to avoid setup-ordering
friction**: it is the direct, necessary consequence of Tier 2 being the verified ceiling, combined with
the already-required resume mechanics.

**The accepted state is a Pending Area Link, not an unassigned Room:**

- A Room Configuration record may be initiated and named, and its intended Vocabulary may begin, before
  its constituent Area reference is resolved.
- This is represented as the Room Configuration's own constituent-Area reference being in a **pending**
  state — reusing the existing Room model's own distinction between a valid reference and a **broken
  reference** (`room.md`, "A constituent Area is deleted in Home Assistant → Report a broken
  constituent reference") — a pending-not-yet-created reference is the symmetric, pre-creation case of
  the same honest-reference discipline, never a second native-object store.
- **This pending state exists only as part of the hand-off/resume flow defined in §9–§12.** It is not
  offered as a freestanding "create a Room with no Area, indefinitely" feature decoupled from an active
  hand-off, and this ADR does not decide whether such a freestanding feature is independently needed
  elsewhere — none was found required by current canonical architecture during this review.
- **Foundation remains responsible** for the governed relationship between native Home Assistant
  objects and the household/Room model (unchanged); the pending-link state is Foundation's own Room
  Configuration record attribute, never a new record class, never a new responsibility.

**The existing distinctions are fully preserved and never collapsed**: Home Assistant Area, HTBW
Physical Room, HTBW Room Configuration, and Merged Room remain four separate concepts exactly as
`glossary.md` and `room.md` already define them. A pending-link Room Configuration is still a Room
Configuration — it is simply one whose constituent reference has not yet resolved.

**Person receives the same treatment, by direct analogy**: a Person-scoped configuration record (roles,
permissions, Voice Identity settings, and the other extensions `person-and-identity.md` already names)
may begin before the native Person exists, holding a pending native-Person-link state through the same
hand-off/resume mechanism, never a second Person record (**DL-31**, unchanged — "a second Person record
is never created").

---

## 12. Resume, detection, and disambiguation

For every Tier 2 hand-off:

- **HTBW preserves in-progress provisioning state** as part of the owning record itself (the Room
  Configuration's or Person extension's own pending-link attribute, §11) — durable, surviving a Home
  Assistant restart or an HTBW reload, because it is ordinary configuration state, never an
  in-memory-only flow variable.
- **The resident returns** to HTBW (reopening the relevant configuration step) whenever they choose;
  no deadline or timeout is imposed.
- **HTBW detects candidate native objects** by comparing the current registry state against what
  existed when the hand-off began, surfacing objects that did not exist before, using the registry's
  own stable identifiers (**DL-31**) — never by guessing from name similarity alone.
- **Disambiguation is always explicit.** Where more than one plausible native object exists — a newly
  created one, an already-existing one with a similar name, or several newly created in the same
  session — HTBW presents the candidate set and **requires the resident's own explicit confirmation**
  of which native object the pending link resolves to. This reuses the repository's existing
  no-silent-guess discipline (already established for Vocabulary and Concierge: "ask, offering only
  exposed options" — never silently selected).
- **The resident may select an already-existing object instead of a newly created one.** This is fully
  valid and collapses the flow to the already-covered reference-only case (Option A) — no hand-off was
  actually required in retrospect, and none is repeated.
- **The resident may cancel native creation.** The Room Configuration or Person extension remains in
  its pending state, explicitly reportable (never silently abandoned), and the resident may retry the
  hand-off or cancel the HTBW-side item entirely.
- **The resident may create a differently named object than HTBW's own captured intent.** This is
  never treated as an error — identity is established by the resident's **explicit confirmation**
  (previous bullet), never by comparing the native object's name against HTBW's originally captured
  name.
- **A native object subsequently renamed in Home Assistant** is followed by its stable identifier
  (**DL-31**); no re-confirmation is triggered merely by a rename.
- **A native object deleted after HTBW has referenced it** is handled by the existing broken-reference/
  reconciliation rules already accepted for Rooms (`room.md`'s "report a broken constituent reference;
  do not silently shrink the Room") and Foundation generally (**DL-65**). **HTBW never silently
  recreates a deleted native object** — recreation, if the resident wants it, is a new, explicit,
  resident-initiated act, indistinguishable architecturally from original creation.

---

## 13. Forbidden tier, restated

**HTBW never invokes a private, undocumented, or unsupported Home Assistant registry implementation
merely to avoid the hand-off in §9**, regardless of the fact that `area_registry.async_create()`,
`floor_registry.async_create()`, and `async_create_person()` are each technically callable Python
functions. **Technical callability is not architectural support** (**DL-30** — "existence of a
callable method is not itself a supported integration mechanism," restated directly from the prior
verification pass and reconfirmed by this one). No parallel Area, Floor, or Person hierarchy is ever
created as a substitute.

---

## 14. Resident-facing language (conceptual, not prescribed)

Where Tier 2 applies, HTBW's own setup experience may still read naturally as ordinary HTBW
provisioning — "Add Room," "Add Person," "Add Floor" — without exposing implementation mechanics
unnecessarily to the resident. **Explainability must nevertheless be able to show**, where asked or
reviewed, that the underlying Floor/Area/Person is a native Home Assistant object that HTBW references
and extends, never a second HTBW-owned record (§15).

When hand-off is required, the language explains the boundary honestly without requiring the resident
to understand the architecture — conceptually: *"Home Assistant manages [Floors/Areas/People] for your
home. We'll take you there to add this one, then bring you back here to continue."* **This exact
wording is illustrative only** and is not adopted as repository UX copy by this ADR; final wording is
implementation/UX mapping, consistent with repository language conventions established elsewhere.

---

## 15. Explainability

A Decision Trace or equivalent governed reference can state, where authorized: whether the Room/Person
was created natively through this hand-off, referenced from an already-existing native object, or is
currently pending native creation; where HTBW supplied a `suggested_area` value Home Assistant
ultimately recorded; and which native identifier the HTBW record currently references. **No duplicate
copy of native object content is ever created merely to support this explanation** — the reference is
to the native object's own stable identifier, consistent with existing Explainability discipline
(`decision-trace.md`'s reference-not-copy rule, unchanged).

---

## 16. Acceptance scenarios validated

| # | Scenario | Outcome |
|---|---|---|
| 1 | New HA+HTBW install, no Floors exist, resident creates "First Floor" through HTBW | Tier 2 hand-off (§9); pending link (§11) resolved on return (§12) |
| 2 | New HA+HTBW install, no Areas exist, resident creates "Den" through HTBW | Same as above, Area |
| 3 | Area "Den" already exists | Reference-only; no hand-off (§10, §12) |
| 4 | New household Person entered through HTBW | Tier 2 hand-off; pending Person-link resolved on return |
| 5 | Native Person already exists | HTBW attaches extensions; no duplicate Person created (**DL-31**) |
| 6 | Native creation unsupported (all three objects) | Governed hand-off via My Home Assistant; resumes on return |
| 7 | Resident cancels native creation | Pending state remains, reportable; retry or cancel available (§12) |
| 8 | Resident renames during native creation | Resident's explicit confirmation establishes identity, never name-matching (§12) |
| 9 | Two possible native objects exist on resume | HTBW never guesses; explicit disambiguation required (§12) |
| 10 | Home Assistant restarts during the provisioning journey | Pending state is durable configuration state; survives restart (§12) |
| 11 | HTBW reloads after the native object exists but before extension configuration completes | Pending state re-detects the existing object and resumes extension configuration (§12) |
| 12 | Native object later renamed in Home Assistant | Followed by stable identifier; no re-confirmation (§12) |
| 13 | Native object deleted after HTBW referenced it | Existing broken-reference/reconciliation rules apply; never silently recreated (§12) |
| 14 | No private/unsupported API is ever invoked | §13 |
| 15 | The resulting Floor/Area/Person is fully native and normally manageable in Home Assistant | Confirmed — nothing is a projection-only shadow object; it is the real native object (§10) |
| 16 | HTBW extensions remain governed by their existing authoritative owner | Unchanged (Foundation/Identity/Continuity/Operational Trust, per existing ownership) |

---

## 17. Explicit non-goals

This ADR does **not**: implement any config/options flow UI; implement the detection/resume mechanics
in code; invent a general-purpose, freestanding "unassigned Room" feature independent of an active
hand-off; invent a "suggested Person" or "suggested Floor" mechanism (none exists); reopen **DL-16**,
**DL-30**, **DL-31**, **DL-65**, **DL-67**, **DL-68**, **DL-104**, **OD-10**/**DL-125**, or
**OD-77**/**DL-139**; or decide any exact resident-facing wording or screen layout.

---

## 18. Related decisions

**DL-16** · **DL-30** · **DL-31** · **DL-65** · **DL-67** · **DL-68** · **DL-104** · **DL-125**
(**OD-10**) · **DL-139** (**OD-77**) — each consumed unchanged, none reopened.

## 19. Related documents

- [../models/room.md](../models/room.md)
- [../models/room-configuration.md](../models/room-configuration.md)
- [../models/person-and-identity.md](../models/person-and-identity.md)
- [../contracts/foundation-contract.md](../contracts/foundation-contract.md)
- [../contracts/room-configuration-contract.md](../contracts/room-configuration-contract.md)
- [home-assistant-boundary.md](home-assistant-boundary.md)
- [../models/decision-trace.md](../models/decision-trace.md)
- [../models/glossary.md](../models/glossary.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
