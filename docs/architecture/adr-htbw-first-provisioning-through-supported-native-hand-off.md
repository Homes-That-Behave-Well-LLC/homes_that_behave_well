# ADR: HTBW-First Provisioning Through Supported Native Hand-off

> **Document status: Canonical ADR.**
> Status: **Accepted 2026-11-06, AMENDED 2026-11-06 following Owner-directed remediation.** Records
> **DL-149** (issue **#192**). The original formal acceptance review PASS of 2026-11-06 is **superseded**
> by this amendment's own repeated formal acceptance review — see §0.
> Resolves **OD-91** in full.
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Terminology: [../models/glossary.md](../models/glossary.md),
> [../models/room.md](../models/room.md),
> [../models/person-and-identity.md](../models/person-and-identity.md).

---

## 0. Remediation (2026-11-06) — read this first

**The original version of this ADR (commit `5ffe9a4`) concluded Tier 2 (supported hand-off) for Floor,
Area, and Person alike, and was accepted with a formal acceptance review PASS.** The Owner determined
that acceptance **premature**: the evidence supporting it traced only whether ordinary integrations
independently call `area_registry.async_create()`, `floor_registry.async_create()`, or
`async_create_person()` through internal Python APIs — a different, narrower question than whether an
authenticated administrator, operating an HTBW-provided **frontend** experience, may invoke the same
supported administrative WebSocket command Home Assistant's own frontend uses. That full
frontend-to-backend trace had not been performed.

**This amendment performs that trace** (§§3–7) and **reaches a materially different conclusion for the
mechanism, while preserving the original ADR's central invariant unchanged**: Home Assistant remains
the sole authoritative owner of Area, Floor, and Person; HTBW never becomes a second source of truth;
no private or unsupported API is ever used. **What changes is this**: the relevant administrative
WebSocket commands (`config/area_registry/create`, `config/floor_registry/create`, `person/create`) are
**not frontend-only in any technical or documented sense** — they are registered on Home Assistant's
general-purpose WebSocket API, gated only by `@websocket_api.require_admin`, with no origin restriction
anywhere in their implementation. **A custom panel** (an officially documented, supported HTBW
interaction-surface option that receives the same `hass` object, including `hass.callWS`, as the core
settings pages) **can therefore invoke them directly and reach Tier 1** — provided HTBW's own
provisioning experience is implemented as a custom panel for that step. **A Config Flow or Options
Flow cannot** — those run entirely server-side with no browser/WebSocket access, so Tier 2 remains the
correct, necessary mechanism wherever HTBW's provisioning experience is implemented that way instead.

**Disposition: B — DL-149 AMENDED, not affirmed, superseded, or deferred.** The central model (Home
Assistant First, reference-and-extend, no second source of truth, no parallel hierarchy) is unchanged
and not reopened. The mechanism-availability conclusion is corrected: Tier 1 is available via a custom
panel for all three objects; Tier 2 remains the correct fallback for a Config/Options-Flow-based
surface. **This repeated formal acceptance review (§16) is the one that governs.** The prior PASS is
provenance, not current governance status.

---

## 1. Status

**Accepted 2026-11-06; amended 2026-11-06.** Resolves every OD-91 acceptance criterion and all five of
its remaining questions. This ADR creates **no new responsibility**, **no parallel Area/Floor/Person
hierarchy**, **no unassigned-Room feature independent of the hand-off/creation mechanism it defines**,
and **no private or unsupported Home Assistant API use**. It does not reopen **DL-16**, **DL-30**,
**DL-31**, **DL-65**, **DL-67**, **DL-68**, **DL-104**, **DL-125** (OD-10), or **DL-139** (OD-77) —
each is consumed unchanged.

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

## 3. Phase 1 — Complete frontend-to-backend trace (remediation)

**The original verification matrix below is superseded.** It recorded only the backend Python registry
method and concluded `VERIFIED_UNSUPPORTED` from the absence of third-party Python callers. **It did not
trace the frontend action, the exact network command, or the backend command's own authorization
boundary** — all now supplied.

| Object | Frontend file/function | Data-layer call | Exact command | Backend registration | Authorization | Registry mutation | Response |
|---|---|---|---|---|---|---|---|
| **Floor** | `src/panels/config/areas/ha-config-areas-dashboard.ts`, `_openFloorDialog()` → `dialog-floor-registry-detail.ts`'s `_updateEntry()` | `createFloorRegistryEntry(hass.callWS, values)` (`src/data/floor_registry.ts`) | `config/floor_registry/create` | `homeassistant/components/config/floor_registry.py`, `websocket_create_floor`, registered via `websocket_api.async_register_command` in the `config` integration's `async_setup` | `@websocket_api.require_admin` | `floor_registry.async_get(hass).async_create(**data)` | `connection.send_result(msg["id"], entry_dict)` — includes `floor_id` |
| **Area** | `ha-config-areas-dashboard.ts`, `_openAreaDialog()` → `dialog-area-registry-detail.ts`'s `_updateEntry()` | `createAreaRegistryEntry(hass, values)` (`src/data/area/area_registry.ts`) → `hass.callWS({type: "config/area_registry/create", ...values})` | `config/area_registry/create` | `homeassistant/components/config/area_registry.py`, `websocket_create_area`, registered in the `config` integration's `async_setup` | `@websocket_api.require_admin` | `area_registry.async_get(hass).async_create(**data)` | `connection.send_result(msg["id"], entry.json_fragment)` — includes `area_id` |
| **Person** | `src/panels/config/person/ha-config-person.ts` → `dialog-person-detail.ts`'s create path | `createPerson(hass, values)` (`src/data/person.ts`) → `hass.callWS({type: "person/create", ...values})` | `person/create` | `homeassistant/components/person/__init__.py`'s `PersonStorageCollectionWebsocket(collection.DictStorageCollectionWebsocket)`, registered via the generic `homeassistant/helpers/collection.py` `StorageCollectionWebsocket.async_setup()` under the `person` domain prefix | `@websocket_api.require_admin` (applied generically by `collection.py`'s `ws_create_item` registration, identical pattern to Area/Floor) | `storage_collection.async_create_item(data)` | `connection.send_result(msg["id"], item)` — includes the generated storage `id` |

**All three commands share one identical, uniform architecture**: a `@websocket_api.require_admin`-gated
command registered on Home Assistant's general-purpose WebSocket dispatcher, calling straight through to
the same registry/storage-collection mutation method the prior pass already found. **The only
previously-missing fact was that this entire path is reached by the frontend over the same WebSocket API
every authenticated client uses — never a special, frontend-origin-restricted channel** (§5).

**Evidence sources, all fetched/searched directly 2026-11-06**: `home-assistant/frontend` (`dev` branch)
— `ha-config-areas-dashboard.ts`, `dialog-area-registry-detail.ts`, `show-dialog-area-registry-detail.ts`,
`data/area/area_registry.ts`, `dialog-floor-registry-detail.ts`, `data/floor_registry.ts`,
`dialog-person-detail.ts`, `data/person.ts`; `home-assistant/core` (`dev` branch) —
`homeassistant/components/config/area_registry.py`, `homeassistant/components/config/floor_registry.py`,
`homeassistant/components/person/__init__.py`, `homeassistant/helpers/collection.py`.

**Evidence classification scale used (remediated)**: `VERIFIED_SUPPORTED_FOR_HTBW`,
`VERIFIED_SUPPORTED_HA_FRONTEND_ONLY`, `VERIFIED_UNSUPPORTED_FOR_HTBW`, `VERIFIED_INTERNAL_ONLY`,
`UNVERIFIABLE`/`UNDOCUMENTED`. No object is converted from `UNVERIFIABLE` to a supported/unsupported
classification without the complete trace above (**DL-30**).

---

## 4. Floor — complete trace and support-boundary determination

**Prior finding (original pass)**: "UNVERIFIED, NEGATIVE BY ANALOGY," later strengthened in this ADR's
first version to `VERIFIED_UNSUPPORTED`, both based solely on Python call-site counts.

**Remediated trace**: §3's table. `config/floor_registry/create` is registered identically to Area
(below), gated only by `@websocket_api.require_admin`.

**Support-boundary determination (Phase 5, applied identically to Area and Person — the reasoning is
common to all three and stated once here, cross-referenced from §5 and §6):**

1. *Formally documented as a per-object public API?* No dedicated page names `config/floor_registry/
   create` as a "use this from your integration" API. But `contributors.home-assistant.io/core/
   internals/websocket-api/` (current, re-fetched 2026-11-06) documents the WebSocket API itself as
   **"the main API: the frontend and the companion apps use it for nearly everything,"** states
   explicitly that **"almost every integration with a UI registers commands of its own,"** and directs
   developers that **"for the rest, the frontend source is the best place to see how they are
   called"** — i.e., official guidance affirmatively expects developers to learn command shapes from
   frontend source, not merely tolerates it.
2. *An authenticated administrative command Home Assistant's own frontend uses?* Yes — confirmed
   directly in source (§3).
3. *Intentionally exposed through Home Assistant's frontend connection layer?* Yes — registered on the
   shared, hass-wide WebSocket command dispatcher used for every other command, not a separate or
   isolated channel.
4. *Restricted technically or by documented architecture to Home Assistant's own frontend?* **No such
   restriction exists anywhere in the command registration or handler code.** `@websocket_api.
   require_admin` checks only `connection.user.is_admin` — there is no check of which panel, origin, or
   client issued the message.
5. *Can a custom frontend panel invoke it?* **Yes.** `contributors.home-assistant.io/frontend/
   custom-ui/panel/` (current, re-fetched 2026-11-06) states a custom panel is **"a custom element that
   gets the same `hass` object as everything else"** — including `hass.callWS`, the exact method the
   core dashboard uses (§3). **Can a Config Flow or Options Flow?** No — those execute entirely
   server-side in Python, rendering a generic declarative schema with no browser/WebSocket access of
   any kind; they have no `hass.connection` to call through, and could only reach the registry by
   calling `floor_registry.async_create()` directly in Python — the original, still-unsupported path
   (§7 restates why that remains forbidden).
6. *If custom/integration frontend use is prohibited, what proves it?* No such prohibition was found —
   not in the WebSocket API documentation, the custom-panel documentation, or the command's own
   registration code. The "Areas belong to the user" sentence (§5) is written in the context of, and
   cited from, the Area-registry page describing **integration Python helper usage** — a different
   extensibility mechanism from a custom panel's browser-side WebSocket call.
7. *No prohibition found → none is invented*, consistent with this instruction.
8. *Callable but undocumented → classify UNVERIFIABLE rather than SUPPORTED?* Not applicable here: the
   evidence is not "merely callable" — it is affirmatively, generically documented as the main
   client-facing API, with custom panels documented as receiving equal access, and no origin-restriction
   exists anywhere to rebut it. This is a different evidentiary posture from Python call-site analysis
   alone, and the classification below states precisely what converges and what remains a reasoned
   architectural conclusion rather than a single explicit sentence.
9–12. *Maintenance dependency, typed helper, used outside core settings, ecosystem precedent?* The
   frontend supplies a typed helper (`createFloorRegistryEntry`) used only within the core settings
   dashboard today; no other bundled panel currently calls it. This remains a **genuine HTBW-specific
   implementation dependency on a Home Assistant frontend data-layer pattern**, not a blocker to
   support, but a maintenance consideration recorded honestly.

**Conclusion: `VERIFIED_SUPPORTED_FOR_HTBW` via a custom panel; `VERIFIED_SUPPORTED_HA_FRONTEND_ONLY`
—  effectively unreachable — from a Config Flow or Options Flow**, which lack the browser connection
entirely. **Selected tier: Tier 1, conditioned on HTBW's provisioning surface being a custom panel
(§8a); Tier 2 (§9) remains correct wherever that surface is a Config/Options Flow instead.**

---

## 5. Area — complete trace and support-boundary determination

**Prior finding**: `VERIFIED_UNSUPPORTED`, from the documentation statement *"Areas belong to the user.
Your integration does not create or change them"* plus Python call-site analysis.

**Remediated trace**: §3's table. `config/area_registry/create` is registered identically to Floor,
gated only by `@websocket_api.require_admin`, with no origin restriction.

**Support-boundary determination**: identical to §4's twelve-point analysis, which applies without
variation — the same `config` integration module registers both commands with the same decorator and
no object-specific restriction. **The critical distinction the Owner raised is directly resolved here**:
"Areas belong to the user. Your integration does not create or change them" describes **integration
Python code calling `area_registry.async_create()` directly** — the page's own code examples and
surrounding prose are entirely about Python helper usage (`from homeassistant.helpers import
area_registry as ar`). It says nothing about, and does not contemplate, a **custom panel's own
browser-side WebSocket call**, made on an authenticated administrator's own explicit action, through the
identical command and authorization gate the core settings page itself uses. These are architecturally
distinct mechanisms, and the sentence does not extend to the second one without evidence it was ever
intended to — none was found.

**Conclusion: `VERIFIED_SUPPORTED_FOR_HTBW` via a custom panel; Tier 2 remains necessary from a
Config/Options Flow.** The original Python-callability finding is **not overturned** — it remains true,
and still fully forecloses calling `area_registry.async_create()` directly from backend integration
code (Config Flow/Options Flow would still have to do exactly that, and remains forbidden from doing
so, §13). What changes is that a **different, officially supported mechanism** — the admin WebSocket
command, reachable only from a custom panel — exists and was not previously traced.

---

## 6. Person — complete trace, support-boundary determination, and security trace

**Prior finding**: `VERIFIED_UNSUPPORTED FOR THIRD-PARTY USE`, from `async_create_person`'s sole
Python caller being `onboarding`.

**Remediated trace**: §3's table. `person/create` is registered through the identical generic
`collection.py` `StorageCollectionWebsocket` pattern used by Area and Floor (and by Label, Zone, and
several other registries), gated by the same `@websocket_api.require_admin` check, with the same
absence of any origin restriction. The support-boundary determination in §4 applies identically.

**Conclusion: `VERIFIED_SUPPORTED_FOR_HTBW` via a custom panel; Tier 2 remains necessary from a
Config/Options Flow.** As with Area, the original Python-callability finding for
`async_create_person()` directly is **not overturned** and remains forbidden (§13); the custom-panel
WebSocket path is the distinct, newly-traced, supported mechanism.

**Person-specific security trace (Phase 6).** `person/create`'s payload schema (`CREATE_FIELDS`,
`homeassistant/components/person/__init__.py`) is: `name` (required), `user_id` (**optional**, nullable),
`device_trackers` (optional list). **Creating a Person and creating a Home Assistant user/login account
are two separate operations, and the supported API itself distinguishes them**:

- **Person-only creation**: `person/create` called with `user_id` omitted or `null`. No account, no
  credential, no authentication provider entry is touched. The official end-user documentation
  confirms this exact outcome is already a first-class native state ("they cannot have their own
  dashboard... but they can still be used for device tracking... and be included in automations").
- **Person associated with an existing user**: `person/create` with `user_id` set to an already-existing
  user's ID. Still no credential creation — the user already exists.
- **Person plus a brand-new user/login**: reached only through the native "Add person" dialog's
  separate, nested "Add user" sub-flow, which is a distinct frontend action against Home Assistant's
  **auth** component, not the `person/create` command at all.

**Decision: HTBW invokes only Person-only creation (`user_id` omitted).** HTBW **never** requests,
triggers, or orchestrates the user/login-creation pathway, and **never manages passwords, authentication
providers, login credentials, refresh tokens, or Home Assistant user security** in any form. This is an
explicit, permanent non-goal (§17), independent of whether the user-creation pathway is itself
technically reachable from a custom panel — it is never invoked.

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
object accepts a hint value from an integration. HTBW never invents one. This remains independent of
§§4–6's own Tier 1/custom-panel finding — it is a separate, narrower, device-registration-time
mechanism, never superseded or broadened by this amendment.

---

## 8. Phase 2 — Tier selection (amended)

Per the ordered preference (Tier 1 — supported native creation orchestrated directly; Tier 2 —
supported hand-off to native creation UI with resume; Tier 3 — explicit hand-off using the best
available mechanism; Forbidden — private/unsupported API use), the remediated evidence (§§4–6) changes
the prior conclusion:

| Object | Tier (via custom panel) | Tier (via Config/Options Flow) | Why |
|---|---|---|---|
| Floor | **Tier 1** | Tier 2 | `config/floor_registry/create`: `VERIFIED_SUPPORTED_FOR_HTBW` from a custom panel (§4); unreachable from server-side flow code |
| Area | **Tier 1** | Tier 2 | `config/area_registry/create`: `VERIFIED_SUPPORTED_FOR_HTBW` from a custom panel (§5); unreachable from server-side flow code |
| Person | **Tier 1** (person-only, `user_id` omitted) | Tier 2 | `person/create`: `VERIFIED_SUPPORTED_FOR_HTBW` from a custom panel (§6); unreachable from server-side flow code; user/login creation never invoked regardless |

**Tier 1 is reached uniformly across all three objects, conditioned on the HTBW interaction surface
itself (§8a)** — this is not "forcing a common result" against the evidence; the underlying mechanism
genuinely is identical for all three (§3). **Tier 2 remains the correct, necessary tier wherever HTBW's
provisioning experience for that step is implemented as a Config Flow or Options Flow instead**, since
those surfaces have no access to the mechanism Tier 1 requires.

---

## 8a. HTBW interaction surface (Phase 13)

**This ADR does not mandate that HTBW build a custom panel.** It establishes what each surface type can
and cannot legitimately do:

| Surface | Authenticated `hass` connection? | Admin authorization available? | Tier 1 commands valid from here? | Native HA frontend pattern precedent? |
|---|---|---|---|---|
| **Custom panel** (registered via `panel_custom`'s `async_register_panel()`) | **Yes** — receives the same `hass` object as every built-in page, including `hass.callWS` | Yes — Home Assistant resolves admin status per authenticated connection, independent of which panel issued the call | **Yes** | Yes — this is exactly how the core Settings pages themselves are implemented; no other precedent is required because the mechanism is architecturally general-purpose (§4) |
| **Config Flow** | No — server-side Python only, no browser/WebSocket access | N/A | **No** | N/A |
| **Options Flow** | No — same as Config Flow | N/A | **No** | N/A |
| **Repairs/guided-repair flow** | No — same category as Config/Options Flow | N/A | **No** | Reserved for administrator-correctable defects (**DL-148**), not provisioning |

**If HTBW implements the relevant provisioning step as a custom panel**, that panel may invoke
`config/area_registry/create`, `config/floor_registry/create`, or `person/create` (person-only) directly
on the authenticated administrator's own explicit action, reaching Tier 1. **If HTBW implements that
step as a Config Flow or Options Flow instead** (a legitimate, simpler choice this ADR does not
foreclose), Tier 2 (§9) is the correct and necessary mechanism for that step, because the surface itself
cannot reach Tier 1. **Either choice preserves the invariant**: *HTBW-first means one coherent household
experience, not a second source of truth.*

---

## 9. The Tier 2 fallback mechanism — My Home Assistant

**Where HTBW's provisioning step is implemented as a Config Flow or Options Flow (§8a), Tier 2 applies**,
using **"My Home Assistant"** (`my.home-assistant.io`) — Home Assistant's own documented, supported
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
invocation). **This is the fallback mechanism this ADR adopts for all three objects wherever Tier 1 is
not reachable from the active surface.**

---

## 10. Decision — the HTBW-first provisioning experience

**Tier 1 path (HTBW provisioning step implemented as a custom panel):**

```
HTBW Integration Setup
    ↓
Household / Foundation setup (custom panel)
    ↓
Resident names a Floor/Room/Person directly in the HTBW panel
    ↓
Panel invokes config/floor_registry/create, config/area_registry/create, or person/create
    directly (admin-authenticated hass.callWS) — native object created and its stable
    identifier (floor_id/area_id/person id) returned in the same interaction (§4–§6, §8a)
    ↓
HTBW configures its own Room/Physical Room or Person extensions against that identifier
    ↓
Continue progressive HTBW commissioning
```

**Tier 2 path (HTBW provisioning step implemented as a Config Flow or Options Flow):**

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

**Neither sequence is a mandated rigid order** — a resident may define Rooms before Floors, or a Person
before any Room, and an already-existing native object short-circuits its own creation/hand-off step
entirely (reference-only, per the issue's own Option A, applied automatically wherever it already
holds). **The architectural invariant, unchanged by which path is used**: the resident experiences one
coherent HTBW-guided provisioning journey, while Home Assistant remains the authoritative owner of its
native objects. **Neither path ever makes HTBW the source of truth for that object** (**DL-31**
unchanged) — Tier 1 creates the object through Home Assistant's own supported command, exactly as its
own frontend would; Tier 2 creates it through the resident's own action on Home Assistant's own native
surface.

---

## 11. Pending-link reassessment (Phase 12) — a pending link, not a general unassigned-Room feature

**Reassessed under Tier 1's availability.** Where HTBW's provisioning step reaches Tier 1 (§8, §8a),
native creation and the returned stable identifier (`floor_id`/`area_id`/person `id`) occur **within
one governed HTBW interaction** — the custom panel's own `hass.callWS` call returns the identifier
synchronously as part of that same request/response exchange (§3). **A full hand-off/resume pending
state is therefore not required merely to bridge a navigation-away-and-back gap, because none exists
for Tier 1.** What remains necessary, even for Tier 1, is **ordinary crash/failure recovery**: the WS
request could fail validation (§15 scenario 7), hit a name collision (§15 scenario 8), or Home Assistant
could restart between the resident's intent capture and the request completing, or between the native
object being created and HTBW's own extension-configuration step completing (§15 scenarios 9–11). **A
narrowly scoped pending state remains justified for this reason alone, not as a UX bridge** — it is
retained, not preserved merely because it was already documented, because the evidence above
independently requires it.

**Where HTBW's provisioning step is Tier 2 (§9)**, the full hand-off/resume pending state remains
necessary for the reason originally stated: the hand-off genuinely takes the resident away from HTBW's
own interaction and back, and HTBW must hold durable state describing what is in progress across that
gap.

**The issue's own Option C ("unassigned Room Configuration state") is accepted only in this narrow,
bounded form, in either tier, never as a general-purpose standing feature** independent of an active
creation/hand-off.

**The accepted state is a Pending Area Link (or, for Tier 1, a narrower Creation-Intent record), not an
unassigned Room:**

- A Room Configuration record may be initiated and named, and its intended Vocabulary may begin, before
  its constituent Area reference is resolved.
- This is represented as the Room Configuration's own constituent-Area reference being in a **pending**
  state — reusing the existing Room model's own distinction between a valid reference and a **broken
  reference** (`room.md`, "A constituent Area is deleted in Home Assistant → Report a broken
  constituent reference") — a pending-not-yet-created reference is the symmetric, pre-creation case of
  the same honest-reference discipline, never a second native-object store.
- **Required fields for the pending state, either tier**: a creation-intent identifier (HTBW-internal,
  never presented as a native identifier); the resident-entered provisional label (name only, never
  treated as native identity, §12); the native-object reference once creation succeeds; lifecycle
  states (`pending` → `resolved` or `cancelled`); expiry/cancellation (resident-initiated only, never a
  timeout); restart recovery (durable, surviving a Home Assistant restart or HTBW reload); and
  ambiguity handling (§12) — an explicit prohibition applies throughout: **a provisional, resident-
  entered label is never treated as the native object's identity.**
- **This pending state exists only as part of an active creation (Tier 1) or hand-off/resume (Tier 2)
  flow.** It is not offered as a freestanding "create a Room with no Area, indefinitely" feature
  decoupled from either, and this ADR does not decide whether such a freestanding feature is
  independently needed elsewhere — none was found required by current canonical architecture during
  this review.
- **Foundation remains responsible** for the governed relationship between native Home Assistant
  objects and the household/Room model (unchanged); the pending-link state is Foundation's own Room
  Configuration record attribute, never a new record class, never a new responsibility.

**The existing distinctions are fully preserved and never collapsed**: Home Assistant Area, HTBW
Physical Room, HTBW Room Configuration, and Merged Room remain four separate concepts exactly as
`glossary.md` and `room.md` already define them. A pending-link Room Configuration is still a Room
Configuration — it is simply one whose constituent reference has not yet resolved.

**Person receives the same treatment, by direct analogy**: a Person-scoped configuration record (roles,
permissions, Voice Identity settings, and the other extensions `person-and-identity.md` already names)
may begin before the native Person exists, holding a pending native-Person-link state through either
Tier's own mechanism, never a second Person record (**DL-31**, unchanged — "a second Person record is
never created").

---

## 12. Resume, detection, and disambiguation

**For a Tier 1 creation request** (§8, §8a): the native identifier returns directly in the same
`hass.callWS` response (§3) — ordinarily no detection/disambiguation step is needed at all, since HTBW
already knows exactly which native object it just created. **Detection/disambiguation applies to Tier 1
only in the failure-recovery case** — the request's success is uncertain (connection dropped, HA
restarted mid-request) and HTBW must determine, on resuming, whether the object was actually created
before concluding so.

**For every Tier 2 hand-off, and for Tier 1's own failure-recovery case alike:**

- **HTBW preserves in-progress provisioning state** as part of the owning record itself (the Room
  Configuration's or Person extension's own pending-link attribute, §11) — durable, surviving a Home
  Assistant restart or an HTBW reload, because it is ordinary configuration state, never an
  in-memory-only flow variable.
- **The resident returns** to HTBW (reopening the relevant configuration step) whenever they choose;
  no deadline or timeout is imposed.
- **HTBW detects candidate native objects** by comparing the current registry state against what
  existed when the hand-off/request began, surfacing objects that did not exist before, using the
  registry's own stable identifiers (**DL-31**) — never by guessing from name similarity alone.
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
  creation/hand-off or cancel the HTBW-side item entirely.
- **The resident may create a differently named object than HTBW's own captured intent** (Tier 2) or
  change the name before submitting (Tier 1). This is never treated as an error — identity is
  established by the resident's **explicit confirmation** or the Tier 1 response's own returned
  identifier (never by comparing the native object's name against HTBW's originally captured name).
- **A native object subsequently renamed in Home Assistant** is followed by its stable identifier
  (**DL-31**); no re-confirmation is triggered merely by a rename.
- **A native object deleted after HTBW has referenced it** is handled by the existing broken-reference/
  reconciliation rules already accepted for Rooms (`room.md`'s "report a broken constituent reference;
  do not silently shrink the Room") and Foundation generally (**DL-65**). **HTBW never silently
  recreates a deleted native object** — recreation, if the resident wants it, is a new, explicit,
  resident-initiated act, indistinguishable architecturally from original creation, through either
  Tier.
- **A Tier 1 command returns a validation failure or a name-collision error** (§15 scenarios 7–8): the
  error is surfaced to the resident exactly as Home Assistant's own frontend would surface it (§3's
  `invalid_info` error code); HTBW never retries silently or guesses a corrected value.

---

## 13. Forbidden tier, restated

**HTBW never invokes a private, undocumented, or unsupported Home Assistant mechanism to create or
mutate a native object, regardless of which tier applies.** This is unchanged by Tier 1's availability:
Tier 1 uses `config/area_registry/create`, `config/floor_registry/create`, and `person/create` — each a
**documented, general-purpose, admin-gated WebSocket command**, never `area_registry.async_create()`,
`floor_registry.async_create()`, or `async_create_person()` called directly in backend Python, which
**remain forbidden** regardless of their technical callability (**DL-30** — "existence of a callable
method is not itself a supported integration mechanism," restated directly). No parallel Area, Floor,
or Person hierarchy is ever created as a substitute. **HTBW never requests, triggers, or orchestrates
Home Assistant user/login credential creation** (§6), regardless of tier.

---

## 14. Resident-facing language (conceptual, not prescribed)

Regardless of tier, HTBW's own setup experience may read naturally as ordinary HTBW provisioning —
"Add Room," "Add Person," "Add Floor" — without exposing implementation mechanics unnecessarily to the
resident. **Explainability must nevertheless be able to show**, where asked or reviewed, that the
underlying Floor/Area/Person is a native Home Assistant object that HTBW references and extends, never
a second HTBW-owned record (§15).

**Where Tier 1 applies** (custom panel), the resident experiences creation as a single, uninterrupted
step within HTBW's own interface — no boundary language is required, because no hand-off occurs.

**Where Tier 2 applies** (Config/Options Flow) and hand-off is required, the language explains the
boundary honestly without requiring the resident to understand the architecture — conceptually: *"Home
Assistant manages [Floors/Areas/People] for your home. We'll take you there to add this one, then bring
you back here to continue."* **This exact wording is illustrative only** and is not adopted as
repository UX copy by this ADR; final wording is implementation/UX mapping, consistent with repository
language conventions established elsewhere.

---

## 15. Explainability

A Decision Trace or equivalent governed reference can state, where authorized: whether the Room/Person
was created natively through a Tier 1 panel action or a Tier 2 hand-off, referenced from an
already-existing native object, or is currently pending native creation; which tier and interaction
surface were used; where HTBW supplied a `suggested_area` value Home Assistant ultimately recorded; and
which native identifier the HTBW record currently references. **No duplicate copy of native object
content is ever created merely to support this explanation** — the reference is to the native object's
own stable identifier, consistent with existing Explainability discipline (`decision-trace.md`'s
reference-not-copy rule, unchanged).

---

## 16. Acceptance scenarios validated

| # | Scenario | Outcome |
|---|---|---|
| 1 | New HA+HTBW install, no Floors exist, resident creates "First Floor" through HTBW | Tier 1 (custom panel, §8a) direct creation, or Tier 2 hand-off (§9) if the surface is Config/Options Flow |
| 2 | New HA+HTBW install, no Areas exist, resident creates "Den" through HTBW | Same as above, Area |
| 3 | Area "Den" already exists | Reference-only; no creation/hand-off needed (§10, §12) |
| 4 | New household Person entered through HTBW | Tier 1 (person-only, `user_id` omitted) or Tier 2 hand-off; pending Person-link resolved per §11–§12 |
| 5 | Native Person already exists | HTBW attaches extensions; no duplicate Person created (**DL-31**) |
| 6 | HTBW's surface for the step is a Config/Options Flow (Tier 1 unreachable) | Governed Tier 2 hand-off via My Home Assistant; resumes on return |
| 7 | Resident cancels native creation (either tier) | Pending state remains, reportable; retry or cancel available (§12) |
| 8 | Resident renames during native creation | Resident's explicit confirmation (Tier 2) or the Tier 1 response's own returned identifier establishes identity, never name-matching (§12) |
| 9 | Two possible native objects exist on resume | HTBW never guesses; explicit disambiguation required (§12) |
| 10 | Home Assistant restarts during the provisioning journey (either tier) | Pending/creation-intent state is durable configuration state; survives restart (§11–§12) |
| 11 | HTBW reloads after the native object exists but before extension configuration completes | Pending state re-detects the existing object and resumes extension configuration (§12) |
| 12 | Native object later renamed in Home Assistant | Followed by stable identifier; no re-confirmation (§12) |
| 13 | Native object deleted after HTBW referenced it | Existing broken-reference/reconciliation rules apply; never silently recreated (§12) |
| 14 | No private/unsupported API is ever invoked, either tier | §13 |
| 15 | The resulting Floor/Area/Person is fully native and normally manageable in Home Assistant | Confirmed — nothing is a projection-only shadow object; it is the real native object (§10) |
| 16 | HTBW extensions remain governed by their existing authoritative owner | Unchanged (Foundation/Identity/Continuity/Operational Trust, per existing ownership) |
| 17 | Administrator starts Add Area in native HA UI directly (not through HTBW) | Unaffected — this ADR governs only HTBW-initiated creation; the native path is unchanged |
| 18 | Administrator starts Add Floor in native HA UI directly | Same as above |
| 19 | Administrator starts Add Person without creating a user | Native `person/create` with `user_id` omitted — the same Tier 1 command and payload HTBW itself uses (§6) |
| 20 | Administrator starts Add Person with a new HA user | A separate, distinct frontend action against the **auth** component, never `person/create`; HTBW never invokes it (§6) |
| 21 | HTBW's Tier 1 command is attempted by a non-administrator session | `@websocket_api.require_admin` rejects it with an `unauthorized` error, identical to the native frontend's own behavior; HTBW surfaces this honestly, never bypasses it |
| 22 | Tier 1 command returns a validation failure | Surfaced via the same `invalid_info` error Home Assistant's own frontend receives; never silently retried or guessed |
| 23 | Tier 1 command returns a name collision | Same as above |
| 24 | HTBW never sends credentials or bypasses security boundaries | §6, §13 |
| 25 | HTBW never calls a private Python registry mutation method, either tier | §13 |
| 26 | Tier 2 deep-link fallback remains available wherever Tier 1 is unavailable from the active surface | §8, §8a, §9 |

---

## 17. Explicit non-goals

This ADR does **not**: implement a custom panel, Config Flow, or Options Flow in code; implement the
detection/resume mechanics in code; mandate that HTBW build a custom panel (§8a) — Config Flow/Options
Flow with Tier 2 fallback remains an equally legitimate choice; invent a general-purpose, freestanding
"unassigned Room" feature independent of an active creation/hand-off; invent a "suggested Person" or
"suggested Floor" mechanism (none exists); authorize HTBW to request, trigger, or manage Home Assistant
user accounts, login credentials, authentication providers, or refresh tokens, under any tier (§6);
reopen **DL-16**, **DL-30**, **DL-31**, **DL-65**, **DL-67**, **DL-68**, **DL-104**,
**OD-10**/**DL-125**, or **OD-77**/**DL-139**; or decide any exact resident-facing wording or screen
layout.

---

## 18. Related decisions

**DL-16** · **DL-30** · **DL-31** · **DL-65** · **DL-67** · **DL-68** · **DL-104** · **DL-125**
(**OD-10**) · **DL-139** (**OD-77**) · **DL-148** (Home Assistant First native-pattern matrix, Options
Flow/Repairs boundary reused) — each consumed unchanged, none reopened.

## 19. Related documents

- [../models/room.md](../models/room.md)
- [../models/room-configuration.md](../models/room-configuration.md)
- [../models/person-and-identity.md](../models/person-and-identity.md)
- [../contracts/foundation-contract.md](../contracts/foundation-contract.md)
- [../contracts/room-configuration-contract.md](../contracts/room-configuration-contract.md)
- [home-assistant-boundary.md](home-assistant-boundary.md)
- [adr-contextual-governed-acceptance-placement.md](adr-contextual-governed-acceptance-placement.md) (**DL-148**)
- [../models/decision-trace.md](../models/decision-trace.md)
- [../models/glossary.md](../models/glossary.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
