# Home Assistant Boundary

> **Document status: Canonical.**
> Governed by the Home Assistant First principle (P21) in [principles.md](principles.md).

---

## Position

**HTBW extends Home Assistant. HTBW does not compete with Home Assistant.**

Home Assistant is the initial reference platform. The HTBW framework itself remains vendor-agnostic
and must be able to assess and describe homes built on other platforms.

---

## Home Assistant First

Before introducing any new model, storage mechanism, workflow, configuration system, UI concept,
registry, or architectural construct:

1. Review official Home Assistant documentation.
2. Review official Home Assistant developer documentation.
3. Review official Assist and Voice Assistant documentation.
4. Determine whether Home Assistant already provides a documented pattern.

Prefer Home Assistant primitives whenever they appropriately represent the requirement.

An HTBW extension is justified **only** when Home Assistant cannot practically represent the required
information. The justification belongs in an ADR or in
[../governance/decision-ledger.md](../governance/decision-ledger.md).

### Current-state acquisition and refresh (DL-59)

Verified against official Home Assistant developer documentation:

| Claim | Finding | Proves | Does not prove |
|---|---|---|---|
| Entity update model | An entity either **polls** (`should_poll` true; Home Assistant asks for a value on an interval) or **pushes** (`should_poll` false; the integration calls `schedule_update_ha_state()` when its own event occurs) | Two distinct, integration-declared update mechanisms exist | That any given entity supports a forced new physical reading |
| `available` property | `bool`, default `True`, "indicate if Home Assistant is able to read the state or control the underlying device" | `available`/`unavailable` is an authoritative platform signal | That an *available* entity's value is freshly measured |
| `homeassistant.update_entity` action | "Forces one or more entities to refresh their data right away" | A native, documented refresh request mechanism exists | That the request produces a new physical observation, or that every integration honours it identically |
| `last_changed` / `last_updated` | Standard state-object timestamps (last value change; last time the state was written, even unchanged) | HA already timestamps state transitions | A universal "current vs. historical" field — no such generic distinction exists platform-wide |

**Burden of proof discharged**: no universal forced-refresh capability is claimed. Per-integration
refresh support must be individually verified before Truth relies on it; push-only, event-driven, and
advertisement-based integrations (BLE proximity, PIR motion, doorbell events) are not assumed to support
one. See `truth.md`, *Fact Validity and Current-State Evaluation (DL-59)*.

### Same-purpose environmental aggregation (DL-62)

Verified against official Home Assistant integration documentation, evaluated for **OD-17**:

| Helper | What it computes | Combines multiple entities? | Preserves per-source provenance? | Satisfies the Truth Fact contract? |
|---|---|---|---|---|
| **Statistics** | A statistical characteristic (`mean`, `median`, `change`, `count`, and others) of **one source sensor's own history** over a sampling window | **No** — one entity only | Not applicable — single source | An executor/provider for a single-source time-window derivation, never a same-purpose multi-sensor combination |
| **Filter** | A signal-processing algorithm (`lowpass`, `outlier`, `range`, moving average) smoothing **one source sensor's own** noisy readings | **No** — one entity only | Not applicable — single source | An executor/provider for single-source noise reduction, never same-purpose aggregation |
| **Min/Max** | `min`, `max`, `last`, `mean`, `median`, `range`, or `sum` **across at least two configured entities of the same unit** | **Yes** | No — reports only the computed value, not which entity produced it | **Discharges DL-30 directly if a genuinely narrow same-purpose aggregation use case is ever accepted** — HTBW invents no bespoke aggregation engine in advance of one |

**Finding**: no native helper combines multiple equivalent sensors *and* preserves the per-source
provenance, coverage, and Truth Confidence a Composite Fact would require — but **DL-62** establishes
that the ordinary Room Environment path never needs one, since Room Configuration selects a single
**Primary Authority** per purpose. Min/Max remains available, unused today, as the burden-of-proof
discharge for any narrow future same-purpose aggregation need, without inventing an HTBW aggregation
algorithm speculatively. See `room-configuration.md`, *Primary Authority is required for the ordinary
path (DL-62)*.

### Provider-derived environmental indicator evidence (DL-62 clarification)

Reviewed against architecture-owner-supplied air-Q product documentation and its Home Assistant entity
exposure — no local implementation of an air-Q integration exists in this portfolio's repositories at
the time of this review; this is external product evidence, not code inspected in-repo.

| air-Q entity family | Classification | Basis |
|---|---|---|
| Temperature, Humidity, CO2, CO, NO2, O3, PM1/PM2.5/PM10, Pressure, Noise/Max Noise, VOC, Formaldehyde | **Direct Environmental Measurement** | Reported as the device's own observation of an environmental property |
| Absolute Humidity, Dew Point | **Provider-Derived Environmental Indicator** | Calculated by the device from other measurements; documented as device-calculated, not HTBW-calculated |
| Mold-Free Index | **Provider-Derived Environmental Indicator, trend-based** | air-Q's own documentation states it uses humidity and temperature **trends over a period**, not current values alone — never recreated by HTBW (**DL-30**) |
| Health Index | **Provider-Derived Environmental Indicator** | air-Q's own documentation states it is calculated from provider-selected limit sources and the worst measured variable at a point in time; HTBW does not validate the provider's cited limits |
| Performance Index | **Provider-Derived Environmental Indicator** | air-Q's own documentation states it is a cumulative calculation of provider-attributed performance reductions from environmental loads (e.g. CO2, temperature); never a measurement of a Person |
| Virus Index | **Provider-derived but insufficiently documented** | No sufficient provider documentation was reviewed to state its exact basis; HTBW invents no meaning for it and does not use it for a health, safety, or diagnostic claim |

**Home Assistant First conclusion**: where a provider (air-Q or otherwise) already exposes a
Dew Point, Mold-Free Index, Health Index, Performance Index, or comparable indicator as a native
entity, that entity is preferred over an HTBW-invented equivalent (**DL-30**) — HTBW selects it as a
Primary Authority candidate and reads its current published value; it does not reverse-engineer the
provider's algorithm, and it does not treat the provider's internal inputs as separate HTBW
contributors. See `truth.md`, *Direct measurements and provider-derived indicators are both
Authority-Derived (DL-62 clarification)*.

### Governed conflict resolution (DL-63)

**No native Home Assistant capability performs governed cross-source conflict resolution.** Each
entity publishes its own state independently; Home Assistant does not reconcile disagreeing entities
into one arbitrated value. This burden of proof is straightforward: the absence of a native
reconciliation capability is the residual HTBW owns as **DL-63**. **Native state remains independently
authoritative for each entity** — HTBW never rewrites a native entity's state to reflect a conflict
outcome, and a genuine Truth conflict's published outcome (reduced confidence, unresolved, or
`unknown`) exists only as a Truth Fact, never as a second copy of, or edit to, native state. See
`truth.md`, *Genuine Truth Conflict (DL-63)*.

### Issue #146 verification pass (2026-10-06)

Evidence produced against the Issue #146 verification backlog. **This section records verification
outcomes only. No architecture decision is made here, no ownership boundary changes, and no open
decision is closed.** Home Assistant Core source was consulted under the Issue #146 authority order
(official documentation first, source only where documentation was insufficient), pinned to
`home-assistant/core` commit
[`c571d9d3a96e6fda0a23e754ca0f2906ae63ee84`](https://github.com/home-assistant/core/commit/c571d9d3a96e6fda0a23e754ca0f2906ae63ee84)
(`dev` branch, fetched 2026-10-06) — not a tagged release, so re-confirm against the deployed stable
release before treating any version-sensitive detail as permanent.

#### Storage helper mechanism (item 1, 2026-10-06)

| DL-30 element | Finding |
|---|---|
| Capability evaluated | `homeassistant.helpers.storage.Store` |
| Source | `homeassistant/helpers/storage.py`, class `Store` (`async_save`, `async_delay_save`, `async_load`, `_async_write_data`, `async_remove`), home-assistant/core commit `c571d9d3a96e6fda0a23e754ca0f2906ae63ee84` |
| Constitutional requirement served | OD-01 (governed-record persistence shape) |
| Verified | Persists versioned JSON under `.storage/<key>` inside the Home Assistant config directory; `async_save` writes immediately, `async_delay_save` debounces; `atomic_writes=True` uses `write_utf8_file_atomic`; schema migration via `_async_migrate_func` keyed on `version`/`minor_version`; on JSON corruption the file is renamed to `<path>.corrupt.<timestamp>`, a Repairs issue (`storage_corruption_<key>_<timestamp>`, `IssueSeverity.CRITICAL`) is raised, and load returns `None` — never a silent crash or silent data loss; `async_remove()` deletes the file outright, but is called only by the owning integration's own code, never by a documented resident-facing action |
| Remaining gap | Not established whether `.storage/` content is covered by Home Assistant's native Backup feature; not established whether a Store-backed file is ever presented to a resident as removable configuration (a **config entry** is documented as user-removable — a *different* native object, and must not be conflated with a Store file) |
| Why a lower layer cannot satisfy it | HTBW requires an explicit, documented durability and removability classification before treating any persistence mechanism as satisfying OD-01; an unverified assumption would violate this issue's own standing rule |

**Does not discharge OD-01.** Narrows it: the mechanism's durability, versioning, and failure-handling behaviour are now evidenced; backup coverage and removable-configuration framing remain open. See `connected-storage.md` for the corresponding narrowing note.

#### Floor registry (item 2, 2026-10-06) — VERIFIED_SUPPORTED

| DL-30 element | Finding |
|---|---|
| Capability evaluated | `homeassistant.helpers.floor_registry.FloorRegistry` |
| Source | `homeassistant/helpers/floor_registry.py` (`async_create`, `async_update`, `async_delete`, `async_reorder`, `async_get_floor`, `async_get_floor_by_name`, `async_get_floors_by_alias`, `async_list_floors`, `EVENT_FLOOR_REGISTRY_UPDATED`), commit `c571d9d3a96e6fda0a23e754ca0f2906ae63ee84`; `https://developers.home-assistant.io/docs/area_registry_index/` (official, current) |
| Constitutional requirement served | OD-10 (scope hierarchy; whether Floors are first-class) |
| Verified | Full read and CRUD API exists for integrations; every create/update/delete/reorder fires `EVENT_FLOOR_REGISTRY_UPDATED` with `{action, floor_id}` on the event bus, so an integration may observe Floor registry changes without polling; **a Floor does not hold a membership list** — each Area registry entry instead carries its own `floor_id`, so "which Areas belong to this Floor" is answered by querying Areas, not the Floor registry |
| Remaining gap | None for the literal item-2 question (read, membership, change-notification) |
| Why a lower layer cannot satisfy it | Not applicable — native capability fully discharges the burden |

**Discharges item 2 of Issue #146.** Does not itself decide OD-10 (#135), which retains its own governance question (whether Floors should be first-class scope) independent of this capability finding.

#### Label registry (item 4, 2026-10-06) — VERIFIED_SUPPORTED

| DL-30 element | Finding |
|---|---|
| Capability evaluated | `homeassistant.helpers.label_registry.LabelRegistry` |
| Source | `homeassistant/helpers/label_registry.py` (`async_create`, `async_update`, `async_delete`, `async_get_label`, `async_get_label_by_name`, `async_list_labels`, `EVENT_LABEL_REGISTRY_UPDATED`), commit `c571d9d3a96e6fda0a23e754ca0f2906ae63ee84` |
| Constitutional requirement served | OD-68 (managed label projection mechanism) |
| Verified | Full read/CRUD API mirroring the Floor registry pattern; every mutation fires `EVENT_LABEL_REGISTRY_UPDATED` with `{action, label_id}`; **assignment is held on the assignable object's own registry entry**, not on the label — confirmed for the Area registry (`labels: set[str]`, per the official Area registry page). Device and Entity registry assignment was reasoned by the same registry architecture but **not independently re-fetched this session** |
| Remaining gap | Device-registry and Entity-registry `labels` fields were not independently re-verified this session (reasoned by pattern only) |
| Why a lower layer cannot satisfy it | Not applicable for the Area case; the Device/Entity case is a small residual verification, not a burden-of-proof failure |

**Discharges item 4 of Issue #146** for create/read/update/delete and for Area assignment. Does not decide OD-68's own naming/seeding/reconciliation question.

#### Automation and script trace retention (item 6, 2026-10-06) — PARTIALLY_VERIFIED

| DL-30 element | Finding |
|---|---|
| Capability evaluated | Automation/script execution traces (`trace` component) |
| Source | `homeassistant/components/trace/const.py` (`DEFAULT_STORED_TRACES = 5`, `CONF_STORED_TRACES`, `DATA_TRACE_STORE: HassKey[Store[dict[str, list]]]`), commit `c571d9d3a96e6fda0a23e754ca0f2906ae63ee84`; `https://www.home-assistant.io/docs/automation/troubleshooting/` (official, current) |
| Constitutional requirement served | OD-64 (native behaviour observation), and through it OD-63, OD-65 |
| Verified | Home Assistant retains the **5 most recent traces per automation or script by default**, configurable per-automation via `stored_traces:`; traces are persisted through the **same `Store` helper mechanism as item 1** (`DATA_TRACE_STORE`), so **traces survive a restart** — this corrects the 2026-09-08 review comment's framing, which left retention-across-restart as unverified; official troubleshooting documentation confirms a trace records which condition/action step a run stopped at, the entities/devices/areas an action targeted, and that "View trace" is available only "while Home Assistant still keeps the trace of that run" |
| Remaining gap | Whether trace data is exposed through a **documented, stable integration-facing API**, as distinct from the WebSocket commands the frontend itself uses, is still not established |
| Why a lower layer cannot satisfy it | Retention count and persistence are now native-verified; the cross-integration retrieval contract question is a distinct, still-open sub-question |

**Materially advances item 6.** The non-event case (no trigger → no trace, per the 2026-08-26 Episode 9 review) is unaffected and remains a confirmed negative finding.

#### Long-term statistics as a historical-aggregate source (item 12, 2026-10-06) — PARTIALLY_VERIFIED

| DL-30 element | Finding |
|---|---|
| Capability evaluated | Recorder long-term statistics for `sensor` entities |
| Source | `https://developers.home-assistant.io/docs/core/entity/sensor/#long-term-statistics` (official, current) |
| Constitutional requirement served | OD-35 (historical retrieval and access) |
| Verified | For `state_class: MEASUREMENT`, Home Assistant compiles **hourly min/max/mean every 5 minutes**; for `TOTAL`/`TOTAL_INCREASING`, it compiles a **sum** on the same cadence. The mechanism and its hourly resolution for a "brightest today"-style query are documented and current |
| Remaining gap | Whether the statistics **retrieval** function reports an unreported interval **coverage gap** explicitly, or silently omits/interpolates it, is **not established** by this citation — this is the constitutionally load-bearing half of item 12 under `temporal-record.md`'s "a reconstruction containing an unreported gap is a defect" |
| Why a lower layer cannot satisfy it | The compilation mechanism is native-verified; the gap-reporting behaviour of the query surface requires a further, separate source check not performed this session |

**Partially discharges item 12.** The gap-reporting question remains open and must not be assumed either way.

#### Already-discharged items with stale cross-references in Issue #146

Four items in Issue #146's own "Remaining questions" list cite an **already-closed** open decision as
the thing they block, and the underlying DL-30 burden for each is **already recorded elsewhere in this
document**:

| Item | Issue #146 cites as blocked | Actual status | Where already recorded |
|---|---|---|---|
| 5 — Presentation attestation | #121 (OD-55) | **OD-55 closed as DL-54** (`decision-ledger.md`, "Notes on the presentation attestation decision") | Per-surface evidence (Sonos, Music Assistant, `assist_satellite`, Roku, Apple TV, LG webOS, UniFi Protect, Companion App, `persistent_notification`) already verified there |
| 7 — Repairs ignore lifecycle | #140 (OD-60) | **OD-60 closed as DL-65** | *Repairs adoption scope (DL-65)*, above in this document — "Ignoring an issue does not delete or resolve it... until the integration deletes it or the resident completes its repair flow" |
| 8 — Assist entity exposure | #103 (OD-59) | **OD-59 closed as DL-66** | *Exposure precedence (DL-66)*, above in this document, which explicitly states the specific read/observe mechanism "remains a per-implementation DL-30 verification... and does not block this architectural rule" |
| 9 — Conversation custom intents / pre-answer filtering | #133 (OD-62) | **OD-62 closed as DL-69** | *Governed conversational retrieval and command resolution (DL-69)*, above — the documented `async_handle_message(user_input, chat_log)` extension point means a custom Conversation agent is, by construction, the sole author of its own response and therefore the native mechanism for applying any filtering before an answer is produced |

**These four items no longer block anything.** Their continued presence in Issue #146's "Remaining
questions" and "Blocking Status" table is a stale cross-reference, not an open gap — recorded as a
finding, not corrected in the issue body by this document (that correction belongs in the issue
comment, not in canonical architecture text).

### Issue #146 remediation pass (2026-10-06, continued)

Second evidence pass against the same backlog, same authority order (official documentation first,
Core source pinned to commit
[`c571d9d3a96e6fda0a23e754ca0f2906ae63ee84`](https://github.com/home-assistant/core/commit/c571d9d3a96e6fda0a23e754ca0f2906ae63ee84)
only where documentation was insufficient). **No architecture decision is made here.**

#### Storage helper — backup coverage and removability (item 1, continued) — VERIFIED_SUPPORTED / VERIFIED_NEGATIVE

| DL-30 element | Finding |
|---|---|
| Capability evaluated | Whether `.storage/` (the `Store` helper's directory) is covered by Home Assistant's native Backup feature, and whether a Store-backed record is ever presented to a resident as independently removable configuration |
| Source | [Common tasks — Backups](https://www.home-assistant.io/common-tasks/general/#backups) (official, current): *"A full backup includes the following directories: `config`, `share`, `addons`..., `ssl`, `media`"*; `Store.path` resolves to `hass.config.path(STORAGE_DIR, key)` i.e. `<config>/.storage/<key>` (`homeassistant/helpers/storage.py`) |
| Verified | **Backup coverage: VERIFIED_SUPPORTED.** `.storage/` lives inside the `config` directory, which a full backup always includes and a partial backup may include by resident selection. **Removability: VERIFIED_NEGATIVE.** Official documentation describes removing an *integration instance* (device + entities) but documents no resident-facing action that independently deletes a Store-backed file; source confirms deletion only happens via `Store.async_remove()`, called by the owning integration's own code — never exposed as a resident UI action |
| Remaining gap | None for either sub-question as literally asked |
| Why a lower layer cannot satisfy it | Not applicable — both sub-questions are now discharged |

**Fully discharges item 1's two named sub-questions.** OD-01 (#76) residual is now narrowed to the semantic-meaning question already recorded in the first pass (resident-vs-automation attribution, absent-value state, provenance/version identity, declared retention, policy governance) — none of which a lower layer (Store, or Backup) can supply, which is why HTBW's own governed-record layer remains justified for *that* residual specifically.

#### Native Room/Area proximity for portable surfaces (item 3) — VERIFIED_NEGATIVE

| DL-30 element | Finding |
|---|---|
| Capability evaluated | Whether a documented native capability resolves a portable interaction surface (phone, wearable, companion device) to **Area or Room granularity** |
| Source | [Private BLE Device](https://www.home-assistant.io/integrations/private_ble_device/) (official, current): *"it can also tell you an estimated distance to the nearest Bluetooth dongle or proxy and its signal strength"*; [Bluetooth integration](https://www.home-assistant.io/integrations/bluetooth/) (official, current): each scanner (adapter or proxy) has its own assigned Area, visible under **Settings > Connectivity > Bluetooth > Adapters** |
| Verified | **VERIFIED_NEGATIVE.** The only documented portable-device proximity capability is *home/away* plus *distance-to-nearest-scanner*. Home Assistant documents no capability that itself resolves this to a Room/Area value. A per-scanner Area assignment exists as a separate, independent fact; Home Assistant does not combine "nearest scanner" with "that scanner's Area" into a stated, supported device-location output |
| Remaining gap | None — this is a clean documented negative, not an absence-of-documentation case |
| Why a lower layer cannot satisfy it | Not applicable to this ruling; no replacement design is proposed here (none is authorized) |

**Household-level presence, GPS zones, and home/not-home state were explicitly excluded from this finding**, per Issue #146's own instruction — they were not treated as Room-level evidence at any point in this evaluation. **Discharges item 3.** OD-73 (#134) remains blocked on this negative finding; a governance decision on whether HTBW may compute Room/Area granularity itself from the raw primitives (nearest-scanner distance + per-scanner Area) is for OD-73 to make, not this issue.

#### Automation and script trace retrieval — public contract (item 6, continued) — VERIFIED_NEGATIVE

| DL-30 element | Finding |
|---|---|
| Capability evaluated | Whether trace data has a documented, stable, **integration-facing** retrieval contract, as distinct from internal or frontend-only access |
| Source | `homeassistant/components/trace/websocket_api.py` and `homeassistant/components/trace/__init__.py`, commit above |
| Verified | **VERIFIED_NEGATIVE.** Every trace-retrieval command (`trace/get`, `trace/list`, `trace/contexts`, plus all debug/breakpoint commands) is registered exclusively via `@websocket_api.websocket_command` and `@websocket_api.require_admin` — an admin-only, frontend-facing WebSocket contract. The component's own public export list (`trace/__init__.py` `__all__`) is exactly `CONF_STORED_TRACES`, `TRACE_CONFIG_SCHEMA`, `ActionTrace`, `async_store_trace` — the retrieval functions (`async_get_trace`, `async_list_traces`, `async_list_contexts`, all in a private `.util` module) are **not** part of that export list |
| Remaining gap | None for the public-contract question |
| Why a lower layer cannot satisfy it | Not applicable — the negative finding is itself the discharge |

**Retention, continued.** Traces are saved to the `Store` helper (`DATA_TRACE_STORE`, key `trace.saved_traces`) only at `EVENT_HOMEASSISTANT_STOP` — confirming the 2026-10-06 first-pass finding that traces survive a graceful restart, via the same mechanism as item 1. **Fully discharges item 6**: retention duration (5, configurable) and persistence mechanism were established in the first pass; this pass establishes that no stable public integration-facing retrieval API exists. A custom integration reading trace data today would be depending on an explicitly internal module, which this document records as **unsupported for that purpose**.

#### Long-term statistics — missing-interval behaviour (item 12, continued) — VERIFIED_SUPPORTED

| DL-30 element | Finding |
|---|---|
| Capability evaluated | Whether `statistics_during_period` (the native statistics retrieval function) explicitly reports missing intervals, returns absent buckets, silently omits intervals, interpolates, or leaves gap interpretation to the consumer |
| Source | `homeassistant/components/recorder/statistics.py`, functions `statistics_during_period`, `_statistics_during_period_with_session`, `_sorted_statistics_to_dict`, commit above |
| Verified | **VERIFIED_SUPPORTED, for the "silently omits / leaves gap interpretation to the consumer" outcome.** The result is built by querying only the rows that actually exist for the requested window; `_sorted_statistics_to_dict` pre-seeds each requested `statistic_id` with an empty list, then appends only the DB rows found — there is **no synthetic row, no null placeholder, and no interpolation** for a period with no compiled data. A caller must detect a gap itself by comparing each returned row's `start`/`end` against the expected cadence; Home Assistant performs no gap detection or reporting on the caller's behalf. Separately, `compile_missing_statistics` self-heals **compilation** gaps caused by a restart, up to the recorder's `keep_days` window — but a source entity that was itself unavailable during a period produces a genuine, permanently uncompiled gap that is never backfilled or flagged |
| Remaining gap | None for the gap-reporting question itself |
| Why a lower layer cannot satisfy it | Confirms the `temporal-record.md` concern directly: if HTBW uses native statistics as a historical-aggregate source (OD-35), **HTBW must perform its own gap detection and reporting on top of the raw rows** — native statistics provides none, so this is a genuine, documented residual for OD-35 to decide, not an assumption |

**Fully discharges item 12.** No differences among statistic types were found that change this answer — `MEASUREMENT` (min/max/mean) and `TOTAL`/`TOTAL_INCREASING` (sum) rows are built through the same row-presence-only logic.

#### Context and actor-attribution propagation (item 13, continued) — VERIFIED_NEGATIVE

| DL-30 element | Finding |
|---|---|
| Capability evaluated | Which actor/origin fields on `Context`, `Event`, `State`, and `ServiceCall` are guaranteed, conditionally present, propagated, synthesized, lost, or internal-only |
| Source | `homeassistant/core.py`, classes `Context`, `Event`, `State`, `ServiceCall`, `EventBus`, `ServiceRegistry`, commit above |
| Verified | **VERIFIED_NEGATIVE for a hidden or undocumented resolved-actor field; exhaustive field classification otherwise VERIFIED_SUPPORTED.** `Context.__slots__` is exactly `(id, parent_id, user_id, origin_event)` — a complete, closed set, confirmed directly from the class definition. Every `Event`, `State`, and `ServiceCall` carries a `Context` (auto-created with a fresh id when none is supplied) |
| Classification | **Guaranteed:** `context.id` (always a valid ULID, every Event/State/ServiceCall). **Conditionally present:** `context.user_id` (only non-`None` when an authenticated Home Assistant user initiated the action chain — e.g. a logged-in person's UI action; automation- and script-originated calls routinely carry `user_id=None`); `context.parent_id` (only set where the firing code explicitly constructs a child context — chaining behaviour itself lives in `helpers/script.py`/`components/automation`, consistent with, but not re-verified against, this document's existing `OD-38` correlation note). **Synthesized:** none — nothing in `core.py` computes or guesses an actor; `user_id` is passed through verbatim or absent. **Lost / internal-only:** `Context.origin_event` — present on the Python object but explicitly excluded from `_as_dict()`/`as_dict()`, so it is never serialized to WebSocket, REST, the recorder, or any consumer outside the exact same in-process Python object reference |
| Remaining gap | Automation-side parent-context chaining was reasoned from the existing boundary note, not independently re-verified against `helpers/script.py` source this session |
| Why a lower layer cannot satisfy it | Confirms, with an exhaustive source-level field list rather than a documentation-absence inference, that **no native mechanism maps `user_id` (an authenticated Home Assistant user) to an HTBW-resolvable Person**, and no undocumented fifth field exists to carry one |

**Fully discharges item 13's core question** (whether an undocumented native actor-resolution field or extension point exists): it does not. **Still open:** whether `parent_id` chaining, independently re-verified at the automation/script layer, is sufficient evidence for OD-38's own correlation-strategy decision — that re-verification is a small residual, not a blocker to this item's own terminal status.

#### Voice pipeline native capability — Step A (item 11) — VERIFIED_SUPPORTED

| DL-30 element | Finding |
|---|---|
| Capability evaluated | Satellite/pipeline voice activity detection (VAD), wake-word engine configuration, per-Room media-player-state availability, and documented Assist pipeline extension points |
| Source | [Assist pipelines](https://developers.home-assistant.io/docs/voice/pipelines/) (official developer docs, current); [The Home Assistant approach to wake words](https://www.home-assistant.io/voice_control/about_wake_word/) (official, current) |
| Verified | **Wake word:** three engine families documented — openWakeWord (server-side default), microWakeWord (on-device, ESP32-S3 class and Android Companion App), Porcupine (29 words, alternative). Per-satellite wake word is user-selectable ("Users can pick per configured voice assistant what wake word to listen for"). **VAD:** two distinct, both documented — client-side VAD ("Clients should avoid unnecessary audio streaming by using a local voice activity detector") and Home Assistant's own internal VAD, which extends the wake-word timeout while speech continues; the pipeline additionally emits explicit `stt-vad-start`/`stt-vad-end` events with millisecond-relative timestamps marking a voice command's observed start and end. **Audio-enhancement configuration** (closest documented analogue to "sensitivity"): `noise_suppression_level` (0–4), `auto_gain_dbfs` (0–31), `volume_multiplier`, all documented `input` fields of the `wake_word` pipeline stage. **Pipeline extension points:** the four-stage sequence (`wake_word` → `stt` → `intent` → `tts`) is run via the documented `assist_pipeline/run` WebSocket command with a full documented event stream (`run-start`/`run-end`, per-stage start/end events) and a complete documented error-code taxonomy (`wake-engine-missing`, `wake-word-timeout`, `stt-no-text-recognized`, etc.) |
| Remaining gap | Per-Room `media_player` state availability was not re-fetched this session; it is already established via this document's existing Area/entity-registry evidence (an entity's Area assignment makes its state queryable per-Room) and `truth.md`'s existing acceptance of *"the television is in use"* as a Fact |
| Why a lower layer cannot satisfy it | Not applicable — Step A is a native-capability inventory, not a justification for building anything |

**Discharges Step A of item 11's A–F sub-evaluation.** Steps B–F remain outstanding; Step B specifically requires real household measurement and is addressed by the Track B protocol delivered with this pass (see Issue #146 comment).

### Issue #146 voice explainability evidence pass (2026-10-06)

Evidence produced from a live Production incident investigation (October 2026 Voice Explainability
investigation), conducted entirely as Production-read, Development-change discipline — no Production
file, configuration, or data was modified to produce this evidence. Core source consulted under the
same authority order, pinned to the same commit as the passes above,
[`c571d9d3a96e6fda0a23e754ca0f2906ae63ee84`](https://github.com/home-assistant/core/commit/c571d9d3a96e6fda0a23e754ca0f2906ae63ee84).
**This section records verification outcomes only. No architecture decision is made here, no
ownership boundary changes, and no open decision is closed.**

#### Assist Debug run storage, retention, and cross-system correlation (item 14) — VERIFIED_SUPPORTED / VERIFIED_NEGATIVE

| DL-30 element | Finding |
|---|---|
| Capability evaluated | The Assist Debug run record shown under Settings → Voice assistants → Assistant → Debug, and the two WebSocket commands (`assist_pipeline/pipeline_debug/list`, `assist_pipeline/pipeline_debug/get`) that supply it |
| Source | `homeassistant/components/assist_pipeline/run.py` (`PipelineRun.__post_init__`, `STORED_PIPELINE_RUNS = 10`, `LimitedSizeDict`), `homeassistant/components/assist_pipeline/websocket_api.py` (`websocket_list_runs`, `websocket_get_run`), commit above |
| Verified | **Storage location: in-memory only, `hass.data`.** A Debug run is held in `pipeline_data.pipeline_debug[pipeline_id][run.id]`, a `LimitedSizeDict(size_limit=STORED_PIPELINE_RUNS)` keyed by a fresh ULID (`PipelineRun.id`) generated per run — **not `.storage`, not Recorder, not browser storage**. **Retention: `STORED_PIPELINE_RUNS = 10` per `pipeline_id`**, pure count-based FIFO eviction, no time-based rule. **Restart behaviour: VERIFIED_NEGATIVE for survival.** No `Store`/`.storage` write path exists anywhere in the run-debug code path (the component's only `Store` usage, `PipelineStorageCollection`/`PipelineStore`, persists Pipeline **configuration** — engines, languages, name — never run or event history), so a restart (or the process ending for any reason) destroys every held Debug run unconditionally. **Retrieval keys: only `pipeline_id` + `pipeline_run_id`.** `conversation_id` and `satellite_id` are recorded *inside* a retrieved run's own `RUN_START` event payload, never as an independent lookup key, and **no lookup by Recorder `context_id`, by timestamp, or by Home Assistant Context exists at all** |
| Remaining gap | None for the literal storage/retention/retrieval question |
| Why a lower layer cannot satisfy it | Confirms, from source rather than documentation absence, that Assist Debug is categorically **ephemeral operational evidence** — it directly evidences the problem framed by **OD-38** (no durable correlation identifier strategy) and **OD-64** (which platform-supplied execution evidence HTBW may reference, and its retention) rather than solving either |

**Discharges item 14.** Does not itself decide OD-38 or OD-64; narrows both with a verified negative (no persistence, no cross-system key) that either decision must account for rather than assume.

#### Recorder and Assist Debug use separate identity systems, with no native correlation (item 15) — VERIFIED_NEGATIVE

| DL-30 element | Finding |
|---|---|
| Capability evaluated | Whether a documented or source-verified mechanism maps a Recorder `context_id` to an Assist Debug `pipeline_run_id`, `conversation_id`, or `satellite_id`, or the reverse |
| Source | `homeassistant/components/assist_pipeline/run.py` (`PipelineRun.context: Context`, `PipelineRun.start()`), `homeassistant/core.py` (`Context.__slots__`), commit above; a real Production incident reconstruction correlating a Recorder `context_id` burst with an Assist satellite's `listening`/`processing`/`responding`/`idle` state sequence |
| Verified | **VERIFIED_NEGATIVE for a native mapping.** `PipelineRun.context` is a real `homeassistant.core.Context`, created once per run and propagated to any service call the run's intent handling performs — this is *why* a Recorder-side `context_id` with no parent can be observed to originate from a voice interaction at all. But that `context.id` is **never written into the `RUN_START` event payload and never exposed by either Debug WebSocket command** — Recorder and Assist Debug can each independently evidence the same real-world interaction, and **the only practical bridge between them, demonstrated in the Production reconstruction, is timestamp and target-entity correlation**, not a shared identifier |
| Remaining gap | None for the literal mapping question — the negative is itself the finding |
| Why a lower layer cannot satisfy it | This is the concrete, source- and incident-verified version of **OD-38**'s own framing (*"Context does not establish semantic reasoning... does not prove causation beyond the documented relationship"*) applied specifically to the voice-evidence pair Issue #146 and OD-64 already anticipate |

**Discharges item 15.** Directly narrows **OD-38**: a durable correlation strategy, if HTBW ever adopts one, cannot assume `context_id` and `pipeline_run_id` are the same identifier or are natively joinable — any join HTBW performs would itself be an HTBW-authored correlation, not an observed native fact, and would need to be represented honestly as such.

#### UTC and household-local timestamp normalisation (item 16) — VERIFIED_SUPPORTED

| DL-30 element | Finding |
|---|---|
| Capability evaluated | Whether Home Assistant's Recorder and `.storage` timestamps are UTC, and whether the configured household time zone is independently verifiable |
| Source | `P:\.storage\core.config` (`"time_zone": "America/Chicago"`, Production, read-only); every Recorder and `.storage` timestamp inspected this session carries an explicit `+00:00` offset |
| Verified | Recorder and `.storage` timestamps are **UTC**, confirmed directly from the data rather than assumed; the configured household time zone is independently stored and must be read, not inferred, before any resident-facing or investigative timestamp comparison is performed. A household-local timestamp supplied for an investigation (for example *"7:31 AM"*) requires explicit conversion against the configured time zone and its current UTC offset (which varies with Daylight Saving Time) before it can be compared against any native record |
| Remaining gap | None |
| Why a lower layer cannot satisfy it | Not applicable — this is a verified platform convention, not a gap. Recorded here because the October 2026 investigation itself was initially obscured by skipping this normalisation step, which is a recurring operational hazard worth naming rather than a new capability question |

**Discharges item 16.** Feeds **explainability.md**'s resident-facing explanation requirement directly: any explanation surfacing a timestamp to a resident must state it in household-local time, derived from the verified `time_zone` configuration, never in raw UTC.

---

## What Home Assistant may provide

- Device Registry
- Entity Registry
- Area Registry
- Floors
- Labels
- Person entities
- State changes
- Events
- Services and actions
- Calendars
- Media players
- Voice-assistant events and Assist pipelines
- Integration data
- Automation infrastructure
- Config flows and options flows
- Recorder state history, including prior-state linkage and deduplicated attributes
- Event bus and recorded events
- Context identifiers, parent context identifiers, and user context identifiers
- History panel, CSV export, and the history REST endpoint
- Activity (Logbook)
- Long-term statistics
- Recorder retention, purge actions, and include/exclude filters
- Attribute recording controls
- State restoration across restart
- Config-entry versioning and migration
- Area aliases, and Area environmental entity assignments where the household has configured them
- Repairs issues and guided repair flows
- Conversation, custom sentences, and custom intents
- To-do entities, with their triggers and conditions
- Tag scan events
- Backup, including automatic backup and its result reporting
- Native automations, scripts, scenes, and blueprints authored by the household

---

## What HTBW owns

- The canonical framework
- The household domain model
- Responsibility contracts
- Room and Merged Room configuration
- Participation and exposure
- Contextual vocabulary
- Identity assertions
- Truth facts
- Stewardship obligations
- Continuity sessions and preferences
- Operational Trust policy
- Concierge decisions
- Decision Traces
- Explainability
- Assessment traceability
- The unified HTBW resident experience

---

## Object distinctions

These object kinds are **not** interchangeable. Treating them as the same object is a defect.

| HTBW concept | Possible Home Assistant backing | Why they differ |
|---|---|---|
| Physical Room | Area, including its `aliases`, `floor_id`, `labels`, and its assigned `temperature_entity_id` and `humidity_entity_id` | An Area is a registry grouping. A Physical Room is a household place with environmental and maintenance meaning. The Area registry now carries **native environmental entity assignments**, which HTBW consumes rather than duplicates. **Each such slot seeds a default Room Environment Purpose proposal, never automatic participation, and is never written back** (**DL-60**, resolved **OD-61**). |
| Room / Merged Room | One or more Areas | A Room is an interaction context. Home Assistant has no equivalent construct. |
| Asset | Zero, one, or many Devices | Many Assets have no device at all. One Asset may span several Devices. |
| Capability | One or many Entities | A capability is expressed in household terms; entities are platform terms. |
| Vocabulary Term | None | Home Assistant aliases operate per entity; HTBW vocabulary is Room-scoped and may target a configured group. |
| Person | `person` entity | HTBW Person carries roles, identity evidence associations, preferences, and authority that the entity does not. |
| Pet | None | No native primitive exists. |
| Service (provider) | None | No native primitive exists. |
| Fact | State | A state is evidence. A Fact is governed, provenance-bearing, and confidence-bearing. **No native Fact-confidence construct exists**; the Truth Confidence Band representation is an HTBW judgement about the state, never a replacement for it (**DL-58**). **No native current-vs-historical validity construct exists either**; Fact Validity is a separate HTBW judgement layered over native state, availability, and timestamps (**DL-59**). |
| Obligation | Calendar event or `todo` item (partially) | An obligation has accountability, lifecycle, and escalation semantics beyond a calendar entry. |
| Session | None | Media player state is evidence about a session, not the session. |
| Policy | None | Automations encode behavior; they do not express governed authority. |
| Decision Trace | Logbook (partially) | The logbook records what changed, not why a decision was reached or refused. |
| Historical Fact | Recorder `states` row (partially) | A recorded state is historical **evidence**. A Historical Fact is a governed conclusion carrying confidence at the time, provenance, coverage, validity, and lifecycle. |
| Change Record | Recorder `states` row with `old_state_id` (partially) | Home Assistant links prior state per entity. A Change Record spans non-entity subjects, names an owning responsibility, carries privacy and retention classification, and survives purge policy independently. |
| Domain Event | Bus event | A bus event is a platform occurrence. A Domain Event is a governed household occurrence with an owner and provenance. |
| Snapshot | Long-term statistics (partially) | Statistics are numeric downsamples of entity measurements. A Snapshot is governed state across a bounded scope, identifying exact record versions. |
| Version Identity | Config-entry `version` (not equivalent) | A config-entry version is a **schema** version used for migration. It does not identify an exact state of a record and produces no change record. |
| Correlation and causation | Context ID, Parent Context ID, User Context ID | Home Assistant context is the closest native primitive and must be evaluated before any HTBW alternative is designed. Whether it is adopted is **OD-38**. |
| Preservation Hold | None | Recorder purge is global or entity-scoped. **No per-record purge exemption exists.** |
| Tombstone | None | Purge deletes rows, leaving nothing to distinguish *"the record was removed"* from *"nothing happened"*. |
| Communication | Notification, persistent notification, or `alert` (none equivalent) | A notification is a **delivery outcome**. A Communication is a governed household interaction with identity, version, audience, category, urgency, lifecycle, and history that exists whether or not anything was ever sent. |
| Delivery Attempt | A `notify` or `assist_satellite` action call | An action call is fire-and-forget. A Delivery Attempt is a recorded, bounded act to one surface with its own governed outcome. |
| Audience | `target`, notify group, or entity list | A target is a device or entity. An Audience is a **specification of people** — a person, role, authority class, or *anyone present with authority*. Home Assistant has no equivalent. |
| Urgency | iOS `interruption-level`, Android channel `importance` | Two different, non-portable per-platform ladders, neither governed by household policy. HTBW Urgency is an Operational Trust **entitlement** mapped downward, never adopted upward. |
| Acknowledgement | `alert` acknowledgement, `clear_notification`, `mobile_app_notification_cleared` | Dismissal identifies nobody. HTBW Acknowledgement is **person-attributed**. `context.user_id` on `mobile_app_notification_action` is the only native attribution path, and only for actionable notifications. |
| HTBW **Alert** category | The `alert` integration | ⚠️ **Name collision.** The HTBW Alert category describes *what a Communication is about*. The `alert` integration is a **condition-driven retry mechanism** watching an entity state. They are not the same object and must never be conflated. |
| Household Inbox | The notifications panel | The panel is a stored list of persistent notifications. The Household Inbox is a **projection**, filtered by the viewer's authority at read time, and is never persisted. |
| Suppression | Nothing | A notification that was not sent leaves no native trace. HTBW records a suppression as a governed change with a Decision Trace. **"Nothing was sent" and "we decided not to send" are different facts.** |
| **Exposure** (HTBW, **P6**, **P7**, **DL-11**) | Assist entity exposure settings | ⚠️ **Name collision.** Assist exposure decides whether an **assistant may target or interact with** an entity. HTBW Exposure decides whether, and how, the **existence of or information about** something may be perceptible to a resident. They are different concepts and must never be merged. |
| HTBW configuration defect | Repairs issue in the issue registry | A Repairs issue is a **surface** for an administrator-correctable problem. It is not the defect definition, not an obligation, and not a Communication. |
| Native automation, script, scene, blueprint | Automation, script, scene, blueprint | These are **native participants** the household owns through Home Assistant. HTBW references and observes them. HTBW does not own, absorb, rewrite, or replace them. |
| Behaviour source | Context ID, Parent Context ID, User Context ID, and the originating integration where identifiable | Context supplies correlation and, where the platform supplies it, an attributable user. It does not supply the household meaning of *what caused this*, which HTBW records as behaviour attribution on the **Domain Event**. See [../models/temporal-record.md](../models/temporal-record.md). |

### Exposure precedence (DL-66)

Resolves **OD-59**. Full acceptance record is **DL-66** in
[decision-ledger.md](../governance/decision-ledger.md); this section is the canonical model.

> **Home Assistant Assist exposure is a platform safety boundary. HTBW may narrow it. HTBW must never
> widen past it, and must never bypass it.**

- Assist exposure determines whether an assistant **may target or interact with** an entity, and
  Home Assistant documents its purpose as safety-driven: preventing sensitive devices, such as locks
  and garage doors, from being controlled inadvertently by voice.
- HTBW Exposure determines whether, and how, **the existence of or information about** something may
  be perceptible to a resident — through vocabulary, Room Help, UI, conversation, or another
  interaction surface (**DL-11**).
- **These are not the same concept, and neither is a proposal for the other.** Unlike a native name
  (**OD-14**, an informational seed a household may freely override) or a native environmental slot
  (**DL-60**, a proposal Room Configuration may accept, decline, or supersede), native Assist exposure
  is never treated as a default HTBW's own governed state may end up overriding upward — because the
  native setting is a deliberate safety precondition, not a suggestion. **HTBW may only ever narrow
  it, never widen past it.**
- **This rule is scoped to voice- and conversation-mediated interaction**: vocabulary resolution, Room
  Help spoken answers, and conversational discussion, retrieval, targeting, or suggestion (**OD-62**
  consumes this boundary without redefining it). **HTBW must not use voice to convey information
  about, or act upon, an entity that Home Assistant has not exposed to the applicable assistant.**
- **A non-voice surface (a UI panel, a dashboard) is independently governed by Room Configuration and
  is not bounded by native Assist exposure** — Assist exposure's own documented purpose is scoped to
  assistant targeting, not general visibility.
- **HTBW never writes back to native Assist exposure**, under any configuration (**DL-31**, **DL-65**'s
  projection model).
- **Divergence between the two is never, by itself, a defect or a Repairs issue** (**DL-65**): an
  entity Assist-exposed but HTBW-excluded is an ordinary deliberate exclusion; an entity HTBW-included
  but Assist-hidden is a **configuration condition** — reported so the household understands that
  voice cannot currently reach an otherwise-configured capability — resolved entirely by the
  precedence rule above, without administrator intervention.
- **The specific native mechanism for reading current Assist exposure state and observing changes to
  it remains a per-implementation DL-30 verification** — mirroring DL-60's own per-slot precedent —
  and does not block this architectural rule, which holds regardless of the reading mechanism
  ultimately used.

HTBW Exposure is defined in [../models/room-configuration.md](../models/room-configuration.md). **This
is the canonical explanation of the distinction; other documents cross-reference it rather than
restate it.**

Four states are involved, and **they must never be collapsed into one**:

| State | Owner | Question it answers |
|---|---|---|
| Native Assist exposure | Home Assistant | May an assistant target this entity at all? |
| HTBW participation | Room Configuration | Does this object take part in this Room's interaction model? |
| HTBW contextual exposure | Room Configuration | Is it reachable by a term, and offered in Room Help? |
| Authority | Operational Trust | May this resident act on it, or know it exists? |

**Configuring a contextual term exposes nothing to Assist and grants no authority.** Home Assistant
documents exposure as the control that prevents sensitive devices, such as locks and garage doors,
being controlled inadvertently by voice; HTBW narrows that boundary and never routes around it.

### Merged Room native representation (DL-68)

Resolves **OD-70**. Full acceptance record is **DL-68** in
[decision-ledger.md](../governance/decision-ledger.md); this section is the canonical model.

> **A Merged Room has no native Home Assistant representation, and none is invented.**

A consumer inventory was reviewed against dashboards, native automations, Assist/Conversation, native
targeting, scripts, scenes, labels, groups, administrative views, and external integrations. **None
had a canonical, implemented requirement for a native projection.**

| Native construct | Disposition |
|---|---|
| **Area** | Rejected. No native "Area composed of Areas" concept is documented (`https://developers.home-assistant.io/docs/area_registry_index/`); inventing one risks a second physical-topology authority competing with the constituent Areas, which **DL-31** forbids |
| **Floor** | Rejected for this purpose. Floor already exists for native physical hierarchy ("Downstairs", "Upstairs"), independently satisfying the household's broader-grouping need per **DL-67** — reusing it for a curated conversational context would blur that distinction |
| **Group** | Rejected as a representation. An entity group carries targets, never vocabulary, participation, or interaction context; Concierge's own execution may still use a native group internally as a target-set optimization (**DL-31**, **DL-55**), which represents nothing about the Merged Room itself |
| **Scene** | Rejected. A Merged Room's configured outcome may resolve to a Scene or script as its execution target (**DL-55**), but a Merged Room is never itself a Scene |
| **Label** | Not adopted. No proven consumer requires it, and the integration-facing label-management API remains unverified, matching **OD-68**'s own unresolved finding — this does not decide or preempt **OD-68** |

**Assist and Conversation must never receive a native Merged Room projection** — not only because none
is needed, but because one would be unsafe: [contextual-vocabulary.md](../models/contextual-vocabulary.md)'s
"resolution compiles down to native targets" rule means HTBW's vocabulary layer already resolves a
term to a concrete, governed entity/device target set **before** any native targeting occurs. A native
Area or Label standing in for a Merged Room would let Home Assistant's own **built-in** conversation
agent resolve it directly through native area-slot matching (`https://developers.home-assistant.io/docs/voice/overview/`,
`https://www.home-assistant.io/voice_control/aliases/`), bypassing HTBW's curated participation,
exclusions, and the **DL-66** Exposure ceiling for exactly the interaction context **DL-67** exists to
curate.

**Constituent removal uses the existing model, with no new rule.** A deleted constituent Area produces
a broken reference under the existing deletion-is-directional model above (**DL-31**); an affected
vocabulary term becomes `broken_mapping` exactly as [contextual-vocabulary.md](../models/contextual-vocabulary.md)
already defines; historical configuration is preserved and no stale membership is implied; a Repairs
projection is created only where **DL-65**'s configuration-invariant eligibility test is independently
satisfied — never merely because a target became unavailable.

**Command-routing, no-match, and native-fallback behaviour are explicitly not decided here.** They
belong to **OD-62**, which owns the retrieval/command surface and custom sentence and intent
definition, and are recorded there as evidence — resolved as **DL-69**, immediately below.

### Governed conversational retrieval and command resolution (DL-69)

Resolves **OD-62**. Full acceptance record is **DL-69** in
[decision-ledger.md](../governance/decision-ledger.md); this section is the canonical model.

**Home Assistant retains its documented Voice pipeline and execution facilities in full. HTBW supplies
governed household meaning at the Conversation extension point and pre-resolves it before any native
targeting occurs.**

| Claim | Documentation | Proves | Does not prove |
|---|---|---|---|
| The Assist Pipeline runs wake word, Speech-to-Text, Conversation/Intent, Text-to-Speech in order | `https://developers.home-assistant.io/docs/voice/overview/`, `https://developers.home-assistant.io/docs/voice/pipelines/` | The documented stage sequence and WebSocket run API | Nothing about HTBW-specific vocabulary or command semantics |
| A Conversation entity implements `async_handle_message(user_input: ConversationInput, chat_log)` and receives `text`, `context`, `conversation_id`, `language` | `https://developers.home-assistant.io/docs/core/entity/conversation` | The documented custom-agent extension point and its documented input fields | That any additional metadata (confidence, Area, device beyond an optional pipeline-level `device_id`) is available |
| An Intent carries `hass`, `platform`, `intent_type`, `slots`, `text_input`, `language` | `https://developers.home-assistant.io/docs/intent_index/` | The documented Intent object shape | A confidence score or alternative transcript |
| The Conversation API returns `continue_conversation`, a `conversation_id`, and a `response` of type `action_done`, `query_answer`, or `error` (`no_intent_match`, `no_valid_targets`, `failed_to_handle`, `unknown`) | `https://developers.home-assistant.io/docs/intent_conversation_api` | Home Assistant's own documented no-match/error taxonomy and multi-turn tracking | That a custom agent may see recognition confidence or a ranked alternative-candidate list |
| Custom sentences may extend or create an intent, with slots and a templated conversation response, via a sentence trigger | `https://www.home-assistant.io/voice_control/custom_sentences/` | A native, documented mechanism for household-declared phrases and responses | That native sentence matching can be intercepted, re-ranked, or confirmed by an external agent |
| `light.turn_on` accepts brightness, color, color temperature, effect, and transition as **optional** parameters | `https://www.home-assistant.io/integrations/light/` | That omitting these parameters is supported | That omission universally restores a previously set brightness — actual behaviour is device/integration-specific |

**DL-30 result**: the native Voice, Conversation, and Intent facilities fully satisfy the pipeline,
recognition, and execution requirements; **HTBW's residual, proven gap is household-specific
Vocabulary, context resolution, cardinality, and a no-match/fallback safety boundary** — see
[contextual-vocabulary.md](../models/contextual-vocabulary.md). No parallel Speech-to-Text, Assist
Pipeline, Conversation, Intent, or execution engine is built.

**The unified command-resolution sequence, the cardinality rule, the no-match/native-fallback
invariant, conversational retrieval classes, pre-answer filtering, and the honest response vocabulary
are all recorded in** [contextual-vocabulary.md](../models/contextual-vocabulary.md) **and**
[failure-and-degradation.md](failure-and-degradation.md) **rather than restated here.**

### Repairs is a surface, not an owner

**Repairs is the preferred Home Assistant surface for HTBW integration configuration defects and
administrator-correctable platform problems** — a Room whose constituent Area was deleted, a
vocabulary term whose target no longer exists, an unreachable connected-storage anchor.

| Rule | Statement |
|---|---|
| Repairs does not own the defect | The defect definition remains with the responsibility that detected it |
| Repairs is not an obligation store | A household obligation is Stewardship-owned and never becomes a Repairs issue |
| Repairs is not a Communication | A Repairs issue is not addressed to an audience and carries no Urgency entitlement |
| Ignoring is not acknowledgement | **Ignoring a Repair identifies nobody.** It is not a person-attributed acknowledgement of a Communication |
| Severity is not Urgency | `IssueSeverity` is a developer-facing platform ladder, not resident-facing Urgency |

Adoption scope is resolved as **DL-65**, below.

### Repairs adoption scope (DL-65)

Resolves **OD-60**. Full acceptance record is **DL-65** in
[decision-ledger.md](../governance/decision-ledger.md); this section is the canonical model.

#### Defect State versus Repairs Projection

**HTBW Defect State is authoritative; the Repairs issue is a projection of it, never the reverse.**
Verified directly against official Home Assistant developer documentation for the Repairs platform:

| Verified platform behavior | Finding |
|---|---|
| An integration calls `async_create_issue` / `async_delete_issue` itself | Home Assistant performs **no independent defect detection** — the integration is the sole authority on whether its own defect state exists |
| `is_persistent` only controls dashboard visibility across a restart | It does not cause Home Assistant to re-detect anything; a non-persistent issue simply stops showing until the integration recreates it |
| **Ignoring an issue does not delete or resolve it** | An ignored issue remains in the registry, suppressed from the dashboard, **until the integration deletes it or the resident completes its repair flow** |
| A fixed issue is removed by walking its `RepairsFlow` | Only a successful repair flow, or the integration's own deletion call, ends an issue's existence |

**This discharges DL-30's burden of proof for the projection model**: Home Assistant's own registry has
no way to learn a defect resolved except being told so by the integration that detected it, which is
precisely the `HTBW Defect State → Repairs Projection` model this decision adopts. HTBW does not
maintain a second, parallel defect store — the owning responsibility's own existing state (a DL-41
capability outcome, a broken governed reference, a detected configuration invariant) **is** the Defect
State, and Repairs is the surface it drives.

#### The Repairs eligibility test

A condition is Repairs-eligible only where **all** of the following hold:

1. It is a **configuration or dependency defect** an administrator can correct through Home Assistant's
   own administrative surfaces (config entries, options, entity/area/label registries) — never through
   ordinary Room Setup, Stewardship's care flow, or a resident's ordinary request.
2. It is **not** a difference Truth, Identity, or Stewardship already resolves through their own
   accepted current/`unknown`/reduced-confidence/obligation vocabulary.
3. It **names or implies no household obligation, care, health, or performance**.
4. It is a **standing configuration or dependency state**, not a transient runtime outcome that
   resolves itself as evidence or availability changes.

| Category | Genuine Repairs candidate? | Owner | Governing decision |
|---|---|---|---|
| Missing or invalid capability dependency (Connected Storage unavailable, a missing integration or provider) | **Yes** | The responsibility that declared the dependency | **DL-41** |
| A broken governed reference (a Room's selected Primary Authority, an Asset relationship, a caretaker reference, a vocabulary target pointing to a deleted native object) | **Yes** | Room Configuration / Foundation | DL-31, DL-45 |
| Two configuration records simultaneously claiming exclusive Primary Authority for one Environmental Purpose | **Yes** — a configuration invariant ordinary runtime evaluation cannot resolve on its own | Room Configuration | **DL-62**, **DL-65** |
| A native Area proposal diverging from an explicit HTBW selection | **No** — a configuration condition, visible through Room Configuration's own lifecycle | Room Configuration | **DL-60** |
| A native Assist exposure setting diverging from HTBW Exposure | **No**, by the same general rule — the specific reporting mechanism remains **OD-59**'s own | Room Configuration | **DL-65**, OD-59 |
| A native Label diverging from the authoritative Asset Type | **Only the reconciliation failure**, never the Asset Type itself, which is never at risk | Foundation | **DL-65**, OD-68 |
| A persistent Truth conflict, by itself | **No** — Truth records it via Domain Event; only becomes Repairs-eligible where the owning configuration responsibility independently identifies a genuine defect behind it | Truth records; Room Configuration (or the relevant owner) raises | **DL-63**, **DL-65** |
| An Identity Assertion outcome (`unknown`, `unavailable`, `ambiguous`) or an assertion's validity/applicability state | **No** — self-resolving, re-evaluated fresh per interaction | Identity | **DL-64** |
| A Provider-Derived Environmental Indicator's reported value | **No** — the provider's own data, not an HTBW defect | Truth | **DL-62** |
| A Stewardship obligation (tuning, humidity, filter replacement) | **Never** | Stewardship | Confirmed unchanged |
| A dashboard projection differing from another projection | **No** — projections are never authoritative and never each other's defect | The owning projection's responsibility | DL-61 |

#### Fixable versus informational

A Repairs issue is **fixable through a `RepairsFlow`** only where HTBW can deterministically correct
the underlying configuration itself, non-judgmentally — for example removing a stale reference to a
deleted object. It is **informational-only** where correction requires a household judgment HTBW must
not make on its own — for example choosing which of two claimed Primary Authorities to keep. **Repairs
never becomes configuration authority**: every fixable flow performs exactly the change a resident
could otherwise make through Room Setup or the native registries.

#### Severity

`IssueSeverity` has exactly three values, per Home Assistant's own developer documentation:

| Severity | Home Assistant's definition | HTBW mapping |
|---|---|---|
| `CRITICAL` | "Considered reserved, only used for true panic" | **Essentially never claimed by HTBW** |
| `ERROR` | "Something is currently broken and needs immediate attention" | A capability currently unavailable (**DL-41**), or a reference currently broken |
| `WARNING` | "Something breaks in the future... and needs attention" | A configuration condition that has not yet blocked anything but warrants review |

**Severity is derived only from the owning responsibility's own already-accepted state** — never from
Stewardship significance, Operational Trust Urgency, or resident-facing consequence (**DL-46**,
OD-46) — preserving the existing boundary rather than creating a new one.

#### Ignore lifecycle and re-raise

**Ignoring an issue never changes HTBW's own Defect State.** Per the verified platform behavior above,
an ignored issue is merely suppressed from the dashboard; the owning responsibility continues to treat
its underlying condition exactly as before, and **ignoring is not evidence that the defect was
addressed** — consistent with **OD-45**'s existing rule that ignoring is not a person-attributed
acknowledgement.

**Re-raising invents no timer or second lifecycle.** Because Home Assistant persists an issue until
HTBW itself deletes it, "re-raise" is simply the owning responsibility's own **existing**
state-evaluation trigger — a Room Configuration change, a DL-41 capability re-check, a startup
reconciliation — recreating the issue if the underlying condition still or again holds. No new
schedule, timer, or event model is created; this mirrors the discipline already applied to DL-63's
persistent-conflict recording and DL-64's rejection of fixed validity windows.

---

## Representation strategy

The accepted representation rule is **DL-31** in
[../governance/decision-ledger.md](../governance/decision-ledger.md). It governs how HTBW references,
extends, and projects Home Assistant objects. The **persistence model** for governed HTBW records is
settled by **DL-46** and **DL-47**; the remaining **representation mechanism** — config entry,
subentry, or private storage — is the residual part of **OD-01**.

### The rule

> **Home Assistant remains authoritative for native registry objects and for every property those
> objects natively own.**
>
> **HTBW references native objects by their stable Home Assistant identifiers and retains only the
> additional information required to satisfy an HTBW constitutional requirement.**

| Rule | Statement |
|---|---|
| Reference, do not copy | Native data is **read from Home Assistant when needed**. It is not copied into HTBW storage for convenience |
| No duplicate maintenance | **No resident may be required to maintain the same information twice** |
| Prefer native representation | Where an HTBW concept benefits from native visibility, discovery, state, automation, targeting, dashboards, actions, Area relationships, or entity behaviour, prefer creating or using a native representation over a parallel object hierarchy |
| Extension by reference | An HTBW extension attaches meaning **to** a native object. It does not absorb it |
| Precise ownership language | Never write *"Home Assistant owns the HTBW concept."* Distinguish **semantic definition**, **native representation**, **extension data**, **runtime state**, and **registry authority** |

Once an HTBW concept has a native representation: Home Assistant is authoritative for the registry
object, its native fields, and its native relationships; HTBW holds only the governance, meaning,
stewardship, identity, continuity, policy, explainability, or historical information that is not
natively represented; and HTBW references the native object by its stable identifier.

### The three representation categories

| Category | Definition | Members |
|---|---|---|
| **1 — Referenced and extended** | The native object exists independently of HTBW | Area, Floor, Device, Entity, Label, Person, Config Entry |
| **2 — Represented natively** | The concept originates in an HTBW requirement but benefits from a native representation the integration creates and manages | Asset Device, Asset-derived Entity, managed classification Label |
| **3 — Governed HTBW records** | No sufficient native representation exists | Merged Room (confirmed, **DL-68**), Decision Trace, Communication, Temporal Record, Preservation Hold, Evidence Package, Stewardship Obligation, Continuity Preference |

Category 3 still **references** native objects where a relationship exists, still avoids copying
native definitions, and may still project into native surfaces. **A projection never becomes the
authoritative HTBW record.**

### What every extension must define

1. Native object type · 2. Native stable identifier · 3. HTBW extension type · 4. HTBW owner ·
5. Additional fields retained · 6. Native fields explicitly **not** copied · 7. Behaviour on rename ·
8. Behaviour on Area or Floor move · 9. Behaviour when unavailable · 10. Behaviour when disabled ·
11. Behaviour when removed · 12. Tombstone or historical-reference behaviour · 13. Repair behaviour
for a broken reference · 14. Projection behaviour, if any · 15. Explainability and historical
implications.

Rename, Area change, and Floor change require **no synchronisation**, because nothing was copied. A
removed native object produces a **broken reference**, which is reported through the Repairs boundary
above and never silently rewritten in history.

### Deletion is directional

| Case | Rule |
|---|---|
| Deleting an HTBW extension of a **referenced** native object | **Never deletes the native object.** The extension is removed; the Area, Device, Entity, Person, or Label remains |
| Deleting an HTBW extension of an **HTBW-created** native object | May remove the native representation **only** where HTBW created it, the relationship is explicitly governed, the user is authorised, and referential and historical consequences have been evaluated |
| Removing an association | Removes participation. It deletes nothing |
| Removing a managed Label | Removes a **projection**. It never changes the authoritative HTBW classification |
| Native object deleted outside HTBW | Produces a broken reference. **Historical references are never silently rewritten**, and HTBW does not recreate the object without governed user intent |

Home Assistant supports integration-initiated device removal through the opt-in
`async_remove_config_entry_device` pattern; where a native representation HTBW created is removed,
that supported pattern applies.

### Home Assistant First applies to storage and retention

> **Home Assistant owns Home Assistant data. HTBW consumes it.**

The representation rule above is a rule about **models**. It applies identically to **storage and
retention**: where Home Assistant already governs and retains the information, **HTBW creates no
parallel store and no second retention model**.

| Home Assistant governs and retains | HTBW does |
|---|---|
| Recorder state history and long-term statistics | Consume through the boundary. **No copy for the purpose of having a copy** |
| Entity state and attributes | Consume as evidence. Truth governs Facts; it does not restate state |
| Device state and registry data | Reference by stable identifier |
| Person state and `user_id` linkage | Reference and extend. No parallel person store |
| Area membership, floors, labels, aliases | Reference. No parallel registry |
| Recorder retention and purge | **Follow it.** HTBW does not run a second purge over native history |
| Native metadata | Reference. Never mirror for convenience |

**Duplication requires a governed gap, never a preference.** The only justification for an HTBW
record alongside a native one is a documented governance requirement that Home Assistant cannot
satisfy — recorded under the ordered burden of proof (**P21**, **DL-30**) and reviewed in the
temporal and communication capability reviews below. Convenience, query shape, performance
speculation, and *"it is easier to own it"* are not justifications. **Wanting longer retention is not
a gap**; it is a reason to extend retention through Connected Storage, not to copy native history.

**HTBW builds no second Recorder.** Native state history has one owner. An HTBW governed record
alongside it exists to carry governance that Recorder cannot express — classification, versioning,
Tombstones, Preservation Holds — and never to restate the state itself.

Where a gap **is** established, the extension governs; it does not replace. A native record remains
authoritative, and a purged native record resolves to *"no longer retained"*, never *"never
existed."* **The presence of Connected Storage changes none of this** — it does not transfer
ownership of native data, and external history is an HTBW **extension**, never a replacement for
Home Assistant history, which remains the source while it is available.

**Extending retention beyond the Home Assistant window is a Connected Storage capability**, with its
own dependency and its own configured window. Without Connected Storage, HTBW follows the available
Home Assistant storage and retention boundaries: capabilities that need no external artifact remain
available, and those that do are **unavailable** rather than degraded into a local store. See
[connected-storage.md](connected-storage.md).

**Home Assistant is also the storage provider itself.** It owns the network-storage connection —
protocol, mount, credentials, and administration — and HTBW selects none of them. HTBW's ownership
begins only after a valid storage dependency has been made available (**DL-44**). Home Assistant
First applies to the storage *connection* exactly as it applies to storage *content*: HTBW does not
build what the platform already provides.

### Object-by-object representation

Read together with the object distinctions above: that table says which concepts are **not the same
thing**; this one says **how each is referenced, extended, and projected**.

| Concept | Native HA object | Native authority | HTBW relationship | Extension owner | HTBW data retained | Native projection | Duplication prohibited | Residual question |
|---|---|---|---|---|---|---|---|---|
| Area | Area | Name, picture, `floor_id`, `aliases`, `labels`, assigned temperature and humidity entities | Reference by area ID | Foundation | None beyond the reference | Not applicable | Area name, picture, floor, aliases, labels | — |
| Floor | Floor | Native floor object | Reference | Foundation | None beyond the reference | Not applicable | Floor definitions | **OD-10** — whether Floor is a first-class HTBW scope. Developer documentation unverifiable |
| Room Configuration | Area (constituents) | The Areas themselves | Extends one or more Areas | Foundation (Room Configuration) | Participation, exposure, vocabulary, exclusions, Room Help, capability exposure, composite-fact inputs, experience endpoints | Not applicable | Anything the Area natively owns | **OD-11** |
| Merged Room | None | Not applicable | References constituent Areas or Rooms | Foundation (Room Configuration) | Merged interaction, participation, vocabulary, and experience semantics | **None (DL-68)** | Constituent Area definitions | Resolved — **DL-68** |
| Existing Device | Device | Identifiers, manufacturer, model, `model_id`, serial number, versions, `via_device`, `area_id`, config entries | Reference by device ID | The responsibility using it | Participation and governed references only | Not applicable | A competing device registry; native device metadata | — |
| Existing Entity | Entity | `unique_id`, entity ID, state, attributes, device and area assignment | Reference by entity ID; read state as evidence | The responsibility using it | Participation, evidence role, governed references | Not applicable | A competing entity registry; native state as a second current-state authority | — |
| Asset | Zero, one, or many Devices | Whatever native objects exist | Semantic definition is HTBW's | Foundation (asset model) | Identity, descriptive knowledge, documentation references, limits, relationships | See Asset Device | Native device metadata | — |
| Asset Device | Device | The registry entry, once created | **Created and managed by the integration** where the Asset has no native backing | Foundation (asset model) | The device ID, plus Asset extension data | The Asset made visible to dashboards, automations, targeting, and Assist | Re-creating a Device for an Asset that already has one | — |
| Asset-derived Entity | Entity | The registry entry and the published state | Created by the integration where the state is useful natively | The responsibility that determines the value | The entity ID and the determination inputs | Attention or obligation state made consumable natively | A second authority for the value it publishes | **OD-69** |
| Label | Label | The label object | Reference; and create and manage a **reserved subset** | Foundation | Which managed labels are HTBW-maintained | The projection mechanism itself | A competing general-purpose label system; deleting or overwriting resident labels | **OD-68** |
| Asset Type | Label (projection only) | The label object, not the classification | Authoritative in HTBW | **Foundation (asset model)** | The authoritative type value and its change history | Managed reserved Labels, derived | Requiring residents to maintain type and labels separately | **OD-68** |
| Person | `person` entity | Name, picture, device trackers, optional user association, access flags | Reference by the native Person | **Distributed** — each extension keeps its own owner | Consent, identity-evidence associations, roles, preferences, obligations, communication and external-service references | Not applicable | A second Person record; native name, picture, presence relationships, or user association | — |
| Person-associated tracker or evidence source | `device_tracker`, and other native evidence | The association and the tracker state | Consumes the resulting evidence | Identity | The **Identity Evidence Association** — person-specific reliability, claim applicability, freshness, family, consent — and assertion records | Not applicable | A duplicate person-to-tracker registry | **DL-32**, **DL-38**, **DL-39** |
| Unknown Person | **None — and none is created** | Not applicable | An Identity Assertion outcome carrying no Person reference | Identity | The assertion only, expiring with it | **Never projected** | Creating a Person named *Guest*, *Visitor*, *Unknown*, or similar to carry a policy | **DL-33** |
| External camera or video evidence | Owned by the providing integration | The media, its identifiers, and its retention | **Referenced**, never copied | Concierge, within a reconstruction | The reference, the times, and the stated relationship to a hypothesis | Not applicable | Copying media in order to correlate it; asserting that a clip depicts an actor | **OD-40**; **DL-35** |
| HTBW Config Entry | Config Entry | The entry and its data | HTBW's own configuration | Foundation | HTBW configuration | Not applicable | — | — |
| Referenced provider or integration configuration | Another integration's Config Entry, conversation agent, or Assist pipeline | Credentials, endpoints, model and connection configuration | **Selects or references** the already-configured capability | The responsibility governing its use | Allowed use, disclosure constraints, authority constraints, orchestration policy | Not applicable | Credentials, endpoints, model configuration, connection information | **OD-67** — not preempted here |
| Communication | None equivalent | Not applicable | Governed HTBW record | Foundation defines; Concierge decides delivery | The full Communication model | Delivery surfaces; Household Inbox as a projection | Treating a notification as the Communication | **OD-42** |
| Decision Trace | Logbook / Activity (partially) | The native entry, if one is written | Governed HTBW record | Concierge | The full trace | Optional native entry as a projection | Treating a native entry as the trace | **OD-29** |
| Temporal Record | Recorder rows (partially) | The native rows | Governed HTBW record | The owning responsibility | Change Records, Domain Events, Snapshots, versions | Not applicable | Treating recorder history as governed history | **OD-01** residual |
| Stewardship Obligation | Calendar or `todo` (partially) | The projected item | Governed HTBW record | Stewardship | Significance, accountability, state, escalation intent | Calendar or `todo` item | Treating list completion as fulfilment | **OD-23** |
| Continuity Preference | None | Not applicable | Governed HTBW record | Continuity | Person-scoped and room-scoped preferences | Not applicable | Treating media-player state as the preference | — |
| Native name | Device name, Entity name | The name itself, including a registry name the resident set | **Read through the native reference** | Not applicable | Nothing | Not applicable | An independently maintained HTBW name for the same object | — |
| Native Assist alias | Alias on an **entity, Area, or Floor** | The alias | **Read.** May seed a contextual term | Not applicable | Nothing; the seed becomes an HTBW term, not a stored alias | Not applicable | An HTBW alias store; automatic write-back; automatic import over a household term | — |
| Contextual Vocabulary term | None | Not applicable | HTBW extension held **by reference** to the native target | Foundation (Room Configuration) | Term, target set, scope, exclusions, mapping source | **None — never projected as a native alias** | Duplicating native names as HTBW vocabulary merely to reproduce them | **OD-13** |
| Assist exposure | Per-entity, per-assistant exposure | Whether an assistant may target the entity | **Read and narrowed, never bypassed** | Operational Trust narrows use; Room Configuration narrows participation | Nothing | Not applicable | Treating a contextual term as exposure, or exposure as authority | **OD-59** |

> **HTBW must never create a native Person to represent someone it cannot identify.** A *Guest*,
> *Visitor*, or *Unknown* Person would write a fiction into a registry HTBW does not own, and would
> make an unidentified stranger indistinguishable from a household member. **Unidentified people
> require no Person object and no enrollment** (**DL-33**). A Person the household deliberately
> creates for a *specific* non-resident is a different thing entirely — that person is **known**.

### Representation scenarios

| # | Situation | Required architectural result |
|---|---|---|
| 1 | An existing Area receives a Room Configuration | Name, picture, floor, and native metadata are **read from Home Assistant**. Room Configuration stores only interaction extensions. **An Area rename requires no synchronisation** |
| 2 | Two Areas participate in a Merged Room | The Merged Room **references** both. Constituent definitions are not copied, native changes remain visible through the reference, and merged interaction semantics stay HTBW-owned |
| 3 | Stewardship initiates an Instrument Asset | The integration creates a native Device through the supported registration pattern; managed reserved Labels mark it; **Asset Type is authoritative as Instrument**; the resident maintains no matching labels by hand; HTBW retains only Instrument-specific extension data |
| 4 | An Asset's attention state becomes adverse | The determination stays with the responsibility that owns it — obligation state is **Stewardship's**, current conditions are **Truth's**. The value is **projected** through a native Entity so native automations and orchestration can consume it. **The Entity is a projection, never a competing authority**, and the determination remains explainable to its inputs and policy |
| 5 | A resident changes Asset Type from Furniture to Antique | The authoritative type changes through the governed HTBW mechanism, only HTBW-managed labels are reconciled, **resident-created labels are untouched**, the change is recorded, and **a projection failure never changes the authoritative type** |
| 6 | A resident removes an HTBW-managed Asset label | **The authoritative Asset Type is unchanged.** The missing label never reclassifies the Asset. Whether the projection is restored, reported through Repairs, or left pending reconciliation is **OD-68** |
| 7 | A native Person is extended with mailbox and calendar references | **No second Person record is created.** Native data stays native; HTBW retains only governed extension references; **each extension keeps its own owner** |
| 8 | The native Person is renamed, or its picture changes | HTBW reads the updated native values. **No synchronisation exists, because nothing was copied** |
| 9 | HTBW uses an already-configured capability | HTBW **selects** the existing configuration through a supported selection mechanism. Credentials, endpoints, and model configuration are **not copied**. HTBW stores only its own governance. **OD-67 stays open** |
| 10 | A referenced Device is deleted outside HTBW | The reference becomes **unresolved and is reported**, historical references are **not rewritten**, and HTBW does not recreate the Device without governed user intent |

### Verified platform basis

| Claim | Documentation |
|---|---|
| Device properties, and manual device registration by an integration against a config entry | `https://developers.home-assistant.io/docs/device_registry_index/` |
| Integration-initiated device removal is opt-in through `async_remove_config_entry_device` | `https://developers.home-assistant.io/docs/device_registry_index/` |
| `entry_type` accepts only `None` or the `service` member — **there is no extensible device-level classification field** | `https://developers.home-assistant.io/docs/device_registry_index/` |
| Entity registration requires a stable `unique_id`, with documented acceptable and unacceptable sources | `https://developers.home-assistant.io/docs/entity_registry_index/` |
| Labels apply to areas, devices, entities, automations, scenes, scripts, and helpers, and can be used as targets | `https://www.home-assistant.io/docs/organizing/labels/` |
| A configuration entry can be selected, returning its entry ID, optionally filtered to one integration | `https://www.home-assistant.io/docs/blueprint/selectors/` |
| A conversation agent can be selected, returning its ID; an Assist pipeline can be selected | `https://www.home-assistant.io/docs/blueprint/selectors/` |
| Person links device trackers and may be associated with a user account | `https://www.home-assistant.io/integrations/person/` |
| A device tracker's state is a zone name, `Home`, `Not home`, `unavailable`, or `unknown` — **the granularity is the zone, never a Room or Area** | `https://www.home-assistant.io/integrations/device_tracker/` |
| `tracking_type` distinguishes **position** trackers from **connection** trackers, and a connection tracker **assumes** the device is in its associated zone while connected | `https://www.home-assistant.io/integrations/device_tracker/` |
| Legacy device trackers carry neither `tracking_type` nor `in_zones`, and are scheduled for removal in the first half of 2027 | `https://www.home-assistant.io/integrations/device_tracker/` |
| Assist uses entity, Area, and Floor names **and configured aliases**; aliases may be added to an entity, an Area, or a Floor | `https://www.home-assistant.io/voice_control/aliases/` |
| Configured aliases are **not used by Assist alone** — they may also be used by Google Assistant | `https://www.home-assistant.io/voice_control/aliases/` |
| The **same alias may be applied to entities in different Areas**, matched in conjunction with the Area name | `https://www.home-assistant.io/voice_control/aliases/` |
| Entities must be exposed per assistant, to prevent sensitive devices being controlled inadvertently by voice | `https://www.home-assistant.io/voice_control/voice_remote_expose_devices/` |

> **Device class is not extensible at the device level.** `entry_type` supports only `None` and
> `service`, and device classes are **entity** classifications drawn from per-domain enumerations.
> **HTBW must not claim a custom device class of "Asset", and must not repurpose native registry
> fields.** Labels are the native classification projection.

> **Not verified:** any API for creating or managing Label objects from an integration, and the Floor
> registry developer pages. **No links are recorded for them, and none are fabricated.** The
> architectural requirement for a managed classification projection stands; **its mechanism is
> OD-68**, and **OD-10** is unaffected.

> **No native Device-level alias is documented**, and **no integration-facing alias-writing capability
> is documented** — Home Assistant describes alias editing as a resident interface action. Neither is
> claimed here. **Do not describe native aliases as globally unique, globally conflicting,
> Area-scoped, Device-scoped, or assistant-scoped**; the documentation supports none of those
> characterisations, and explicitly describes reusing one alias across Areas.

> **Not verified:** any native Room-level or Area-level BLE proximity capability, and any native
> *kiosk* concept. **Device tracker granularity is documented as the zone**, and a connection tracker's
> zone is documented as an **assumption** while connected. **HTBW must not claim native Room-level
> presence detection, and must not treat a kiosk account as anything other than a Home Assistant
> user account.** Native tracker evidence therefore supports **Household Presence**; **Room Presence
> requires evidence whose Room granularity is actually grounded**, and where it is not, no Room
> Presence claim is asserted. **OD-16** is bounded accordingly.

### Names, aliases, and contextual vocabulary

The same reference-and-extension rule governs household language. **Native naming information may
seed an HTBW contextual term. A seed is not synchronisation, and nothing is ever written back.**

| Rule | Statement |
|---|---|
| Native authority | Home Assistant owns native names, native aliases, native exposure, and native object identity |
| Extension by reference | A contextual term attaches Room-scoped household meaning **to** the native target |
| No duplicate maintenance | A resident who named an object in Home Assistant is **never asked to name it again** to make it usable |
| Native projection only where appropriate | A contextual term is **not** projected as a native alias, because it may name a group, a capability, or a Room-dependent target that no alias can carry — and because configured aliases reach assistants beyond Assist |
| No reverse synchronisation | A native rename never overwrites a household-defined term, and an HTBW term never rewrites a native alias |

> **Where a native target concept already expresses the required set safely — an Area, a Floor, a
> label, a domain, a device class, or a documented intent slot — prefer the native target and record
> which was used.** Retain HTBW resolution only where Room-specific participation, exclusions,
> grouping, or household meaning is additionally required. This is **DL-30** applied to language.

**Derived recognition forms of a configured term are HTBW-internal.** They are generated from the
household's own term, they are never written to Home Assistant, and they create no native alias, no
native object, and no additional exposure.

The full rule, the seed-once lifecycle, recognition forms, and Merged Room treatment are in
[../models/contextual-vocabulary.md](../models/contextual-vocabulary.md). **OD-14 is resolved by it.**
**OD-70** and **OD-13** are untouched.

---

## Temporal capability review

Conducted under **P21** against official Home Assistant documentation. The full review, with
documentation links and the reviewed capability list, is recorded in
[adr-temporal-record-model.md](adr-temporal-record-model.md).

### Patterns to evaluate before designing an HTBW alternative

Each of the following must be evaluated before any HTBW equivalent is designed:

- `old_state_id` or equivalent prior-state linkage
- Context ID
- Parent Context ID
- User Context ID
- Deduplicated attributes
- Recorder retention
- Long-term statistics
- Config-entry update and migration patterns
- Assist pipeline event context

### Gaps that justify extension

These, and only these, justify an HTBW temporal extension:

| Gap | Consequence |
|---|---|
| No per-record purge exemption | A Preservation Hold is unimplementable natively |
| No governed-record versioning | A Decision Trace cannot reference the policy version it applied |
| No governed non-entity subjects | Room, Merged Room, Asset, Person, obligation, session, and incident retrieval cannot be expressed |
| No governed-Fact semantics | Historical Facts cannot be represented |
| No field-level historical redaction | Attribute exclusion is permanent and class-level, and cannot redact a recorded row |
| No Tombstone distinction | Removal and absence become indistinguishable |
| No per-record retention classification | Floors and ceilings cannot coexist per record class |
| No durable structured Decision Trace | Activity records what changed, not why |
| No Preservation Hold semantics | Holds have no native representation |

### Purged native records

When a referenced native Home Assistant record has been purged, the governed HTBW reference must
resolve to **"no longer retained"** — never **"never existed."** Silently converting a purged record
into an absent one is a false statement about the household.

**The explanation survives the purge without a copy.** The accepted Fact that Truth recorded — its
Statement, confidence at the time, Provenance, and Freshness — remains available and carries what was
material to the decision. **It was never a copy of the native row, and it must not be widened into
one** (**DL-46**).

**Storage helper documentation was not verified during this review, and no link to it is recorded.**
**OD-01's residual must not be closed on assumed Storage helper behaviour.** Two facts about config
entries *are* verified and narrow it: Home Assistant documents config entries and subentries as
**configuration data created and removed by the user through the UI**, which makes them structurally
unsuitable for immutable historical records.

---

## Communication capability review

Conducted under **P21** against official Home Assistant documentation, version **2026.8.2**. The full
review, with verified documentation links, capability list, and gaps **G1**–**G11**, is recorded in
[adr-resident-communication-and-delivery-separation.md](adr-resident-communication-and-delivery-separation.md).

> **Home Assistant is used for delivery. It is not used for communication governance.**

### Patterns to evaluate before designing an HTBW alternative

- `notify` entities, `notify.send_message`, and notify groups
- `persistent_notification.create` / `dismiss` / `dismiss_all`, and `notification_id` replacement
- Companion `tag` replacement, `clear_notification`, and `timeout`
- `assist_satellite.announce`, `ask_question`, and `start_conversation`
- `tts.speak` and `tts.say`
- `alert` `repeat`, `can_acknowledge`, `skip_first`, and `done_message`
- `todo` incomplete-item state and its triggers
- `mobile_app_notification_action` and `mobile_app_notification_cleared`, including
  `context.id`, `context.parent_id`, and `context.user_id`
- `authenticationRequired` action step-up

`assist_satellite.start_conversation` is the natural implementation of the **retrieval
conversation**; `announce` is the natural implementation of **content-free indication**.

### Gaps that justify extension

| Gap | Consequence |
|---|---|
| No audience model | P32 has no native anchor; targets are entities, never people |
| No cross-surface communication identity | *"Was this conveyed?"* is natively unanswerable |
| Delivery is fire-and-forget | `Delivered` and `Presented` are natively unattestable for most surfaces |
| Acknowledgement is not person-attributed at the domain level | Acknowledgement requires HTBW-side identity binding |
| **No suppression record** | Directly defeats **P27** |
| Acknowledgement is not guaranteed to arrive | Unknown must be representable and must never decay into *not acknowledged* |
| No governed retention for notifications | Retention floors cannot be honoured natively |
| No tombstone for a cleared or purged notification | Removal and absence become indistinguishable |
| Urgency is per-platform and non-portable | Urgency must be an HTBW concept mapped downward |
| Escalation is retry only — `alert.repeat` never changes audience | Confirms that retry and escalation are distinct |
| `alert` is condition-driven, not communication-driven | Cannot represent a Communication whose subject is an Obligation |

### Misuse to avoid

- **`todo` is an outstanding-obligation surface, not a communication inbox.** Do not conflate them.
- **`alert` is a retry implementation, not an escalation model.** Its `repeat` list changes timing,
  never audience.
- **Do not adopt the Home Assistant notification object as the HTBW Communication object.**

### Documentation not verified

> **Dashboard visibility semantics, `media_player` delivery semantics, and voice-satellite indicator
> behaviour were not verified during this review, and no links to them are recorded.** Open decisions
> **OD-43**, **OD-55**, and **OD-57** must not be closed on assumed behaviour in those areas.

**Update (DL-53):** Dashboard view visibility and `media_player` delivery semantics were subsequently
located and verified for the Delivery Surface capability decision — see the Home Assistant First
review in [adr-resident-communication-and-delivery-separation.md](adr-resident-communication-and-delivery-separation.md#delivery-surface-capability-model-dl-53).
**Voice-satellite indicator (light/LED) behaviour remains not verified**, and no link to it is recorded
anywhere in this repository; **OD-55** and **OD-57** still must not be closed on assumed behaviour
there.

---

## Platform capability review

Conducted under **P21** and the **P21 burden of proof** in [principles.md](principles.md).
Documentation version **2026.8.2**. This is the durable architecture record of the platform alignment
review. It records what was evaluated, what remains, and which decision each finding affects.

### Documentation reviewed

| Capability | Documentation | Verified |
|---|---|---|
| Architecture overview | `https://developers.home-assistant.io/docs/architecture_index/` | Yes |
| Entity registry | `https://developers.home-assistant.io/docs/entity_registry_index/` | Yes |
| Device registry | `https://developers.home-assistant.io/docs/device_registry_index/` | Yes |
| Area registry | `https://developers.home-assistant.io/docs/area_registry_index/` | Yes |
| Built-in intents | `https://developers.home-assistant.io/docs/intent_builtin/` | Yes |
| Repairs platform | `https://developers.home-assistant.io/docs/core/platform/repairs/` | Yes |
| Repairs | `https://www.home-assistant.io/integrations/repairs/` | Yes |
| Recorder | `https://www.home-assistant.io/integrations/recorder/` | Yes |
| Activity | `https://www.home-assistant.io/integrations/logbook/` | Yes |
| History | `https://www.home-assistant.io/integrations/history/` | Yes |
| To-do list | `https://www.home-assistant.io/integrations/todo/` | Yes |
| Person | `https://www.home-assistant.io/integrations/person/` | Yes |
| Conversation | `https://www.home-assistant.io/integrations/conversation/` | Yes |
| Backup | `https://www.home-assistant.io/integrations/backup/` | Yes |
| Tags | `https://www.home-assistant.io/integrations/tag/` | Yes |
| Areas | `https://www.home-assistant.io/docs/organizing/areas/` | Yes |
| Labels | `https://www.home-assistant.io/docs/organizing/labels/` | Yes |
| Exposing entities to Assist | `https://www.home-assistant.io/voice_control/voice_remote_expose_devices/` | Yes |
| Local Assist pipeline | `https://www.home-assistant.io/voice_control/voice_remote_local_assistant/` | Yes |
| Wyoming Protocol integration | `https://www.home-assistant.io/integrations/wyoming/` | Yes |
| Wyoming Protocol specification | `https://github.com/OHF-Voice/wyoming` | Yes |
| Wyoming app packaging reference | `https://github.com/rhasspy/wyoming-addons` | Yes |

> **Not verified during this review:** the Floor registry and Label registry developer pages, which
> did not resolve. **No links are recorded for them, and none are fabricated.** **OD-10** must not be
> closed on assumed Floor-registry behaviour.

### Native capability evaluated, and the outcome

| Native capability | Evidence | HTBW extension required | Remaining constitutional gap | Decision affected |
|---|---|---|---|---|
| Area registry, including `aliases`, `floor_id`, `labels`, and assigned temperature and humidity entities | Area registry attribute table | Room and Merged Room only | No interaction context; no participation or exposure state | **OD-61** |
| Entity and device registries, `unique_id`, `via_device` | Registry documentation | Asset and Capability only | Registry objects carry no household meaning | **OD-01** |
| Person entity, `user_id` linkage, administrator and local-access-only flags | Person integration | Roles, authority classes, evidence association | No household role model; administrator is binary — **never treated as care, guardianship, or proxy-consent authority** (**DL-56**, **DL-57**) | **DL-39**, **DL-40**, **DL-56**, **DL-57** |
| Device tracker states, `tracking_type`, `in_zones`, coordinates and `gps_accuracy`, and the Person-to-tracker relationship | Device tracker integration | Person-specific reliability, claim applicability, freshness, correlation | **Zone granularity only**, and a connection tracker assumes its zone. No Room-level presence, and no person-specific reliability | **OD-16** |
| Assist entity exposure | Exposing entities to Assist | HTBW Exposure, which is a different concept | Native exposure governs assistant targeting, not resident perception | **OD-59** |
| Built-in intents, including `name` / `area` / `floor` / `domain` / `device_class` slot combinations, and `HassRespond`, `HassNevermind`, `HassGetState`, `HassBroadcast` | Built-in intents | Room-scoped vocabulary, groups, exclusions, Merged Room semantics | No Room-scoped vocabulary; broadcast targets satellites, never an audience | **OD-13**, **OD-14**, **OD-52** |
| Conversation, custom sentences, `intent_script`, custom intents | Conversation integration | Governed retrieval scopes and authority filtering | Conversation owns no records and no authority | **OD-62** |
| Repairs issue registry, `severity`, `is_fixable`, `is_persistent`, `learn_more_url`, ignore semantics, `RepairsFlow` | Repairs platform documentation | Defect definition only | Ignoring identifies nobody; severity is developer-facing | **DL-65** |
| To-do entities, with `item_added`, `item_completed`, `item_removed` triggers and completion conditions | To-do list integration | Obligation, significance, accountability, escalation | Completion is a list state, not proof that care occurred | **OD-23** |
| Recorder, `purge_keep_days`, `recorder.purge_entities`, include and exclude filters | Recorder integration | Governed retention, holds, tombstones | Purge is global or entity-scoped; there is no per-record exemption | **DL-47**, **OD-01**, **OD-39** |
| Activity, and `logbook.log` custom entries | Activity integration | Decision Trace | Activity records what changed, never why | **OD-29** |
| History panel export and the history REST endpoint | History integration | Governed export scope | Export is entity-scoped and ungoverned | **OD-09**, **OD-35** |
| Backup, automatic backup, and backup result reporting | Backup integration | Nothing for platform-resident state | Connected storage is outside backup scope unless deliberately placed within it | **OD-09**, **OD-36** |
| Tag scan events carrying `tag_id`, `name`, and `device_id` | Tags integration | Confidence banding and evidence fusion | A tag identifies an object and a scanner, never a person | **OD-16** |
| Labels across areas, devices, entities, automations, scenes, scripts, and helpers | Labels documentation | Nothing | Labels are flat, global, and ungoverned | — |
| Assist pipelines, Wyoming, local speech-to-text and text-to-speech | Local Assist pipeline | Identity evidence governance | Speech-to-Phrase is close-ended and does not support open-ended items out of the box | **OD-07** |
| Wyoming Protocol, as the audio and voice-service boundary — JSONL plus PCM; service types `asr`, `tts`, `wake`, `handle`, `intent`, `satellite`, `mic`, `snd`; `user-event` as the user-defined extension point; `select-program`; `info.satellite.area` | Wyoming Protocol specification and integration | Voice evidence production and governance | **No speaker, identification, verification, or biometric service type exists, and no speaker-evidence event exists.** `info.satellite.area` carries an area **name**, not a stable `area_id`, so it never resolves a Room by itself under **DL-31** | **DL-50** — adopted as the preferred voice-pipeline boundary; the protocol gap is recorded, not filled |

### Maintained integration and ecosystem capability evaluated

| Area | Capability | Position |
|---|---|---|
| Presence and identity evidence | Device trackers, companion-app signals, BLE presence projects, camera-based detection | **Consume as evidence.** HTBW does not build presence detection. A detection is never an Identity Assertion (**DL-06**) |
| Media | Media players and established media-management projects | **Consume.** HTBW does not re-implement media routing or library management. A Session is not media-player state |
| Autonomous lighting and comparable policy add-ons | Third-party engines that decide and act on their own | **Permitted, under an explicit delegation boundary.** See below |
| Transport | Matter, Z-Wave, Zigbee, ESPHome | **Consume.** No governance implication |

### New HTBW capability avoided

The review found **no requirement for a new HTBW responsibility, store, history mechanism, escalation
ladder, or source of truth.** Every finding resolved to *consume a native capability*, *record a
distinction*, or *govern an existing capability more precisely*.

### Execution host for an HTBW capability

**This document previously addressed apps — formerly add-ons — only as third-party engines that decide
and act, governed as a delegation boundary under OD-66.** An app, container, or host application used
as the **execution host for HTBW's own capability** is a different thing, and it was nowhere addressed.
That omission was **OD-80**, **resolved 2026-08-25 as DL-50** and recorded in
[adr-wyoming-compatible-voice-evidence-runtime.md](adr-wyoming-compatible-voice-evidence-runtime.md).

**The distinction is not cosmetic.** A third-party engine under **OD-66** *decides and acts on its own*
and is governed as a delegation. An execution host **decides nothing** — it runs HTBW's own capability
because the integration process cannot, and every decision remains with the responsibility that owns
it. Governing one as the other would either grant a runtime authority it does not have, or refuse a
run-time arrangement that carries no authority at all.

**Two things are already settled and are not held open by OD-80.**

| Settled | Statement |
|---|---|
| **Availability** | Where an execution host is declared and is missing, unreachable, or incompatible, the capability is **unavailable and names why** under **DL-41**. **HTBW does not emulate it**, does not substitute an approximation, and does not silently reduce the capability to something weaker sharing its name |
| **Manifest requirements** | A hard `manifest.json` `requirements` entry is an **all-or-nothing gate for the entire integration**. A dependency that is optional to a capability **must not be declared there**, or a degraded capability becomes a total setup failure. This is verified behaviour, not a precaution |

**What DL-50 decided.** A capability that cannot execute inside the integration process **may declare
an execution host**, named in its dependency declaration and in the Decision Trace. **The rule is a
per-capability declared host; a Home Assistant app is the reference deployment and not the
architecture**, because **P25** keeps Home Assistant the first implementation environment and not a
constraint, and apps exist only on some installation types. **The Wyoming protocol is the preferred
voice-pipeline interoperability boundary** wherever HTBW requires runtime audio, discharging the
**DL-30** burden at step 2 — and Wyoming is a protocol, never an HTBW component, with no third-party
voice project becoming a mandatory dependency.

**Three boundaries are unaffected by it.** Data residency remains **OD-07**. Third-party
engines that decide and act remain **OD-66**. **HTBW acquires no host operating-system
administration**, consistent with the storage boundary — HTBW's ownership begins only once a valid
host has been made available, and covers what HTBW runs there and how it governs it.

---

## Native automations, scripts, and scenes

**HTBW must coexist with behaviour the household authored in Home Assistant.** Automations, scripts,
scenes, blueprints, and integration-generated behaviour are native participants. HTBW observes them.

| Rule | Statement |
|---|---|
| No ownership | HTBW does not own, absorb, replace, or require the rewriting of any native automation, script, scene, or blueprint |
| Reference, do not copy | HTBW references native objects by their platform identifiers rather than copying their definitions, unless a documented gap requires otherwise (**P30**) |
| Observation is evidence | What HTBW observes is recorded as a **Domain Event**, owned by the responsibility that observed it. It is not a Decision Trace |
| No fabricated trace | **HTBW never produces a Decision Trace for a decision HTBW did not make** |

Where the platform supplies the evidence, an observation may reference the automation, script, or
scene involved; the invoked action; the resulting state transition; the triggering event; the Context,
Parent Context, and User Context identifiers; the related entity, device, Area, Room, or person; the
initiating resident where attributable; the observable result; and the source integration where
identifiable. **Where the platform does not supply it, it is not inferred.** The evidence model is
**OD-64**.

---

## What Home Assistant context can and cannot establish

Recorded under **OD-38**, which **remains open**.

| Context may support | Context does not establish |
|---|---|
| Correlation of related events into one reconstructable sequence | Semantic reasoning about why anything happened |
| A relationship between an initiating operation and a resulting operation, **where Home Assistant supplies that relationship** through a parent context | Causation beyond what that documented relationship supports |
| Resident attribution, **only where the platform actually supplies an attributable user** | A resident's identity where the platform supplies no user |

Context is **not** HTBW Version Identity: a context identifier correlates occurrences and does not
identify an exact state of a governed record. Context is **not** a Decision Trace: it links what
happened and never records why. **OD-38 must not be closed until all of its acceptance criteria are
satisfied.**

### Native evidence entering identity fusion

Native objects enter the Identity Fusion Function **by reference only** (**DL-31**), and each carries
the ceiling of what the platform genuinely supplies (**DL-30**, **DL-38**).

| Native source | May support | Must not be promoted into |
|---|---|---|
| Native Person state | Household Presence, at the granularity the platform supplies | Room Presence, or speaker attribution |
| Device Tracker, and its **source tracker** | Household Presence; zone membership as the platform reports it | A Room-level claim the tracker does not supply |
| Native zone information | The zone the platform reports | An HTBW Room, unless the deployment genuinely grounds the mapping |
| Authenticated user, and context user identifier | Authenticated Session Identity; Interaction Initiator **where the platform actually supplies a user** | The physical holder, the current speaker, or presence |
| Device and Entity identifiers | Stable reference for an Identity Evidence Association | A copied registry, or an identity of their own |
| Voice-assistant capture context | Endpoint Context, and the bound in which a voice match is meaningful | Any human identity |

**A native Person is derived from its trackers, and shares their evidence family.** Consuming the
native Person state and the trackers that produce it is **one contribution, not several** — a separate
entity identifier is not proof of independence, and neither is a separate integration.

**Room-level proximity detection and managed-endpoint human identity remain unverified.** No
integration-level documentation establishing native Room-level BLE detection, or a native kiosk
identity concept, has been verified. **A Room-Presence ceiling may therefore be claimed only where the
specific deployment's source genuinely supplies it**, and fusion must not be designed against any
particular proximity implementation or voice provider.

---

## Location and engagement capability review

Conducted under **P21** and the ordered burden of proof in **DL-30**. Each row records the capability
evaluated, the documentation status, the HTBW constitutional requirement being tested, and the
**burden-of-proof status**.

> **A burden is discharged only when the evaluation records the capability, the source documentation, the
> constitutional requirement, the remaining gap, and why the lower layer cannot practically satisfy it.**
> **An undocumented evaluation does not discharge the burden, and unverifiable documentation leaves the
> decision open.** Nothing below is asserted beyond what documentation supports, and **no capability is
> fabricated or assumed.**

| # | Capability evaluated | Documentation status | HTBW requirement tested | Burden status |
|---|---|---|---|---|
| **L1** | **Pet location** — any native primitive representing a Pet or its location | **No native primitive exists.** [Object distinctions](#object-distinctions) already records *Pet — None — No native primitive exists* | A Pet-subject Location Fact with confidence, provenance, freshness, and validity | **Step 1 fails on documented absence.** Steps 2–4 **not evaluated**; **not discharged** |
| **L2** | **Pet tag location** — deriving a Pet's Room from a worn tag, collar, or beacon | **Not verified.** Native tag scan events are documented, and they supply a tag identifier, a tag name, and the scanning device — **an interaction with a tagged object**, not a continuous location. No native worn-tag Room-location capability has been located | A Room-granularity Pet Location Fact | **Not discharged.** A tag-location claim may be published **for the tag**; a Pet-location claim at Room granularity may not be asserted from it |
| **L3** | **Device location** — native `device_tracker` and Person state as the source of *where is my phone?* | **Verified.** *"A device tracker's state is a zone name, `Home`, `Not home`, `unavailable`, or `unknown` — the granularity is the zone, never a Room or Area."* `tracking_type` distinguishes **position** from **connection** trackers, and a connection tracker **assumes** the device is in its associated zone while connected | A Device-subject Location Fact | **Discharged at zone granularity only.** Native capability satisfies *where is this device, by zone*. **HTBW adds governed meaning — subject typing, confidence, provenance, freshness, validity, preserved conflict, `unknown` — and builds no second device tracker.** A **Room-level** device claim is **not discharged** |
| **L4** | **Room-level device proximity** — any native capability placing a device in an Area or Room | **Not verified.** Explicitly recorded above: *"**Not verified:** any native Room-level or Area-level BLE proximity capability"* | Room-granularity Device and Person Location Facts; Room Presence ceilings | **Not discharged.** A Room-Presence or Room-level device ceiling may be claimed **only where a specific deployment's source genuinely grounds it**, and never by default |
| **L5** | **Room-level BLE proximity** — native Bluetooth or BLE integrations as a Room-granularity source | **Not verified.** No integration-level documentation establishing native Room-level BLE detection has been located | Room Presence and Room-level Location Facts | **Not discharged.** Fusion must not be designed against any particular proximity implementation |
| **L6** | **Companion App room attribution** — whether the Companion App supplies an Area or Room for an interaction or for the device | **Not verified.** Companion-app signals are documented as an evidence source; **no room-attribution capability has been located and none is claimed** | Room Context for a Companion App interaction; Room-granularity device location | **Not discharged.** **OD-73** is bounded accordingly and must not be closed on assumed Companion App behaviour |
| **L7** | **Mobile-surface Room Context** — resolving the Room a request is evaluated against, for a phone, wearable, Companion App, or browser session | **Not verified**, and additionally **blocked on ownership**: Room Context is owned by Foundation, which [dependency-view.md](dependency-view.md) rule 6 forbids from consuming Truth | Room Context resolution; complete Decision Trace field 5 | **Not discharged**, on both documentary and constitutional grounds. **Open decision OD-73** |
| **L8** | **Kiosk** — any native concept of a kiosk as distinct from a user account | **Not verified.** Explicitly recorded above: *"no native kiosk concept"* | Endpoint Context; probable Room context for a managed endpoint | **Not discharged.** *"HTBW must not treat a kiosk account as anything other than a Home Assistant user account"* |
| **L9** | **Recorder and history as a location-history store** | **Verified.** Recorder state history, long-term statistics, retention, and purge are documented and authoritative | Historical location explainability (**P27**) | **Discharged in Home Assistant's favour.** **HTBW builds no second Recorder and no parallel location history** (**DL-42**, **DL-46**). Durable explanation after native expiry is carried by the accepted **Fact**, not by a copied row. **Wanting longer retention is not a gap**; it is a reason to extend through Connected Storage |
| **L10** | **Areas, Floors, Devices, Entities, Person** as the referenced substrate for every Location Fact Subject | **Verified** for Area, Device, Entity, and Person. **Floor registry developer pages not verified** (**OD-10**) | Stable Subject references under **DL-31** | **Discharged.** Every Fact Subject is **referenced by stable identifier and never copied** |

### What follows from this review

- **Truth may publish a Location Fact only at the granularity its evidence actually grounds.** Zone-level
  evidence yields a zone-level Fact. *"Tom's phone is home"* is honest; *"Tom's phone is in the Den"* is
  not, unless the deployment supplies genuinely Room-grounded evidence.
- **HTBW builds no second device tracker, no second Recorder, and no parallel location history.** The
  governed meaning HTBW adds is subject typing, confidence, provenance, freshness, validity, coverage,
  preserved conflict, first-class `unknown`, and lifecycle — **never the position itself**.
- **A pet tag is evidence about a tag.** It is never independently evidence about the Pet's location, and
  it is **never** identity evidence about a person.
- **L1, L2, L4, L5, L6, L7, and L8 are open burdens.** Where the relevant documentation cannot be
  verified, the burden is not discharged and the decision remains open (**DL-30**). **No implementation may
  proceed on an undischarged row by assuming the capability exists.**

---

## Adaptive behaviour and delegation

Four classes must remain distinguishable. **Established third-party adaptive integrations are not
prohibited. What is required is an explicit delegation boundary and an honest statement of the
explainability limit.**

| Class | Who decided | Who executed | Explainability guarantee |
|---|---|---|---|
| **HTBW-governed adaptive behaviour** | HTBW | HTBW, through governed interfaces | Full. Governed, attributable, permission-checked, historically reconstructable, and carrying a Decision Trace |
| **HTBW-directed external execution** | HTBW | A native mechanism or an external integration | Full for the decision. HTBW retains the Decision Trace; the observation records the execution evidence Home Assistant supplies |
| **Delegated external adaptive behaviour** | Another policy engine | That engine | **Partial, and disclosed as partial.** HTBW may observe the resulting behaviour and must identify it as delegated where evidence supports that identification. HTBW must not claim to know the external engine's internal reasoning unless that reasoning was supplied as governed evidence |
| **Opaque or unattributed behaviour** | Unknown | Unknown | **Honest limitation.** HTBW reports what is known and does not invent the missing cause |

> **Reduced explainability must be disclosed, never concealed and never fabricated.** *"The lighting
> integration changed this, and I do not hold its reasoning"* is a valid and required answer. *"I
> decided this"* would be false.

**Execution is not decision.** An integration that carried out an HTBW decision is an **executor**,
and HTBW retains the Decision Trace. **Delegation is explicit**: it arises from a declared boundary,
not from the observation that an integration performed an action. Where no delegation was declared
and no decision-maker is evidenced, the behaviour is **opaque** — recorded with the actor that is
known and no claim about who decided.

The delegation boundary is **OD-66**.

---

## Native Experience

HTBW surfaces should feel like Home Assistant. Prefer HA navigation patterns, dialogs, selectors,
forms, configuration flows, and interaction conventions.

Residents should feel *"this is Home Assistant enhanced by HTBW,"* not *"this is a separate
application."*

UI placement never changes architectural ownership. A Room-oriented HTBW screen may present Room
Configuration, but Room Configuration remains Foundation-owned.

---

## Deliberately undecided

This refoundation does **not** decide whether each HTBW object becomes a Home Assistant config entry,
config subentry, device, entity, registry item, helper, or private storage record. **This includes
the persistence shape of Change Records, Snapshots, and Current Projections.**

That is a later technical design decision. It is recorded as an open decision:
**OD-01** in [../governance/decision-ledger.md](../governance/decision-ledger.md), which now owns
this residual alone. Related open decisions **OD-35**, **OD-38**, and **OD-42** are likewise not
resolved here. The platform alignment review adds **OD-59** through **OD-67**, and none of them is
resolved here either.

Do not resolve them inside a contract, model, or scenario document.

---

## Home Assistant 2026.9 re-verification

> **This section is additive. It does not replace, amend, or invalidate the four capability reviews
> above, and it does not change their recorded documentation version.** Those reviews were conducted
> against documentation version **2026.8.2** and that evidence date stands as recorded. This section
> records a **separate, later re-verification** conducted 2026-09-08 under the monthly process in
> [../governance/home-assistant-release-review-standard.md](../governance/home-assistant-release-review-standard.md),
> against **Home Assistant Core 2026.9** (released 2026-09-02) and patch **2026.9.1**.
> **Everything here is a finding or a recommendation. Nothing here is an accepted decision.**
> Full review: **#179**.

### Verification pins

| Review | Documentation version | Status |
|---|---|---|
| Temporal capability review | **2026.8.2** | Re-verified 2026-09-08 against 2026.9 — **one row narrowed**, see **R1** |
| Communication capability review | **2026.8.2** | Re-verified 2026-09-08 against 2026.9 — **one row narrowed**, see **R4** |
| Platform capability review | **2026.8.2** | Re-verified 2026-09-08 against 2026.9 — **no row invalidated**; **R5** adds a distinction |
| Location and engagement capability review | **2026.8.2** | Re-verified 2026-09-08 against 2026.9 — **no row invalidated** |

**No previously verified row was found to be false.** Two were **narrowed** by new native capability.

### Re-verification rows, in the DL-30 five-part form

| # | Capability evaluated | Source documentation | HTBW requirement tested | Remaining gap | Why a lower layer cannot satisfy it |
|---|---|---|---|---|---|
| **R1** | **Activity decision causality** — the Activity details dialog now presents what started a change (a person, a state change, a schedule, an integration, or a restart), the automations or scripts it passed through, and the entity's own change, each step clickable, with navigation into automation traces and millisecond timestamps | Release notes 2026.9, *From what changed to why it changed* | Historical explainability (**P27**, **P28**); the Decision Trace | **Narrowed, not closed.** The recorded gap *"Activity records what changed, not why"* is now **partly satisfied for execution causality**. Native Activity still carries **no** identity assertion or confidence, evidence or provenance, context or household posture, authority or policy evaluation, alternatives considered, or policy version applied | **The native layer now satisfies execution causality and HTBW must not rebuild it.** The residual is governed meaning, which no native record represents (**DL-46**) |
| **R2** | **Automation trace per-step targets** — traces now show which entities, devices, and areas each step targeted | Release notes 2026.9, *Other noteworthy changes* | Referenceable execution evidence for a Decision Trace | **Not discharged.** Whether trace data is **programmatically retrievable by an integration**, and **for how long it is retained**, remains unverified. **#146 item 6** | **Not established.** Presentation improved; the integration-facing interface is undocumented, so the burden is not discharged (**DL-30**) |
| **R3** | **Actor projection into native context** — whether HTBW may attribute an event or service call to a resolved actor | WebSocket API (`Context` shape in `state_changed`, `call_service`, `fire_event`); Events page; Integration service actions page; Conversation API page | Attribution of a voice, kiosk, ambient, or physical-control interaction to the person HTBW resolved | **NOT VERIFIED — and this is deliberately not recorded as verified absence.** The documented `Context` is `{ id, parent_id, user_id }` and `user_id` denotes an **authenticated Home Assistant user**; the documented Conversation API inputs are exactly `text`, `language`, `agent_id`, `conversation_id`. **No supported native resolved-actor projection mechanism was verified in the official interfaces reviewed. Source and development-environment validation is required before concluding that no supported extension point exists** | **Not established, in either direction.** An undocumented evaluation does not discharge the burden, and **absence of documentation is not absence of capability** (**DL-30**) |
| **R4** | **Persistent notification replacement semantics** — updating an existing notification now fires `update_type` `updated` rather than `added` | Release notes 2026.9, *Backward-incompatible changes* | Presentation attestation; re-presentation semantics | **Narrowed.** Replacement is now distinguishable from creation. `updated` is still **not** attestation that anyone saw anything, so *"`Delivered` is not `Presented`"* remains natively unsatisfied. **#146 item 5** | **Native events report dispatch, not perception.** No native mechanism attests presentation for most surfaces |
| **R5** | **Resident-facing severity** — the Security dashboard gains an *Active alerts* section in which the household chooses which entities may trigger it and whether each is an `Alert` or a `Warning` | Release notes 2026.9, *Active alerts and favorites for the Security dashboard* | Urgency and interruption entitlement | **Two distinct native severities now exist and must not be conflated.** The previously verified row *"`IssueSeverity` is a developer-facing platform ladder and is not resident-facing Urgency"* **remains true and is unchanged**. Separately, a **resident-facing, household-declared, two-valued presentation severity** now exists. It carries **no audience, no entitlement, no interruption policy, no acknowledgement, and no obligation subject** | **The native gap is unchanged**: *"No audience model — targets are entities, never people."* A per-entity colour cannot carry an entitlement |
| **R6** | **Chart accessibility** — charts become a keyboard focus stop with per-point navigation, a screen-reader live region, and an audio tone per point; line and bar charts including the Energy device breakdown, **not** timelines, sankey diagrams, or network graphs | Release notes 2026.9, *Accessibility for charts!* | *Native Experience*; **P18** | **None for native charts.** | **Fully satisfied natively.** **An HTBW surface that renders its own chart now regresses accessibility relative to native**, so the native component is preferred |
| **R7** | **Device registry — child devices** — 2026.9 introduces child devices referencing `parent_device_id`; `config/device_registry/list` returns a mix of two entry kinds, and a child carries **no** `connections`, `via_device_id`, `entry_type`, `manufacturer`, `model`, `hw_version`, `sw_version`, or `serial_number`. A child with a null `area_id` **inherits its parent's area** | Developer blog, *Device registry WebSocket API changes* and *More device registry deprecations, new helpers and validation* | **DL-31** reference-and-extend; Device-subject Facts | **None architecturally.** Two conformance rules follow for future implementation: **never assume every device-list entry carries `entry_type`, `connections`, or `via_device_id`**, and **resolve a child device's Area by falling back to the parent when `area_id` is null** | **Fully satisfied natively.** **DL-31** already forbids copying the registry. The previously verified row *"Device `entry_type` supports only `None` and `service`"* is unchanged for regular devices |
| **R8** | **Cloud speech-to-text (Labs)** — a new cloud engine targeting accents, background noise, and non-English languages, available through **Labs**, which Home Assistant states **may not be a permanent addition** | Release notes 2026.9, *Test the new voice processing* | Voice interaction quality | **Not a dependency and must not become one.** A capability whose withdrawal is announced in advance cannot satisfy a **DL-41** dependency. A stated no-retention guarantee is **evidence, not a locality property**, and does not answer **OD-07** | **Out of scope for this boundary.** HTBW consumes speech-to-text output and does not select the engine. **Transcription quality is not speaker evidence**, and **DL-50** stands: speaker evidence never gates transcription |
| **R9** | **Connected-storage capacity reporting** — the Storage page shows per-mount usage with amber past 85% and red past 95% | Release notes 2026.9, *How full is your network storage?* | Artifact lifecycle (**DL-43**), dependency availability (**DL-41**) | **None.** **HTBW must not build a connected-storage capacity monitor** | **Fully satisfied natively.** **Capacity is not retention**: a full mount is a dependency-unavailable condition, not a retention outcome |

### What follows from this re-verification

- **The largest consequence is a simplification, not a gap.** Any planned HTBW work that would
  reconstruct immediate source attribution, automation lineage, or trace navigation is now
  **duplicative** and should be removed from scope by the decision that owns it — **OD-63**, **OD-64**,
  and **OD-29**. **This section recommends that; it does not decide it.**
- **`#129` (OD-64) is partially satisfied by native capability** on the presentation and navigability
  side, and **not** on retrievability, retention, or the non-event case.
- **The non-event case is untouched by 2026.9.** If an automation never triggered there is no trace and
  no per-condition record, so *"which condition failed"* remains natively unanswerable, and reading
  automation configuration to assert that a condition *would have* failed remains prohibited.
- **No accepted decision is amended, and no open decision is closed, by this section.**
- **Update (2026-10-06, Issue #146 item 6):** **R2's retention-duration gap is now resolved.** Source
  inspection (`homeassistant/components/trace/const.py`) confirms `DEFAULT_STORED_TRACES = 5`,
  configurable per automation/script via `stored_traces:`, persisted through the `Store` helper so
  traces **survive a restart**. R2's **retrievability-by-integration** gap is unchanged and remains
  unverified. See *Issue #146 verification pass (2026-10-06)*, above.

---

## Related documents

- [principles.md](principles.md)
- [connected-storage.md](connected-storage.md)
- [greenfield-mandate.md](greenfield-mandate.md)
- [behavioral-governance.md](behavioral-governance.md)
- [explainability.md](explainability.md)
- [../models/temporal-record.md](../models/temporal-record.md)
- [../models/communication.md](../models/communication.md)
- [../models/room-configuration.md](../models/room-configuration.md)
- [adr-home-assistant-first-and-connected-storage.md](adr-home-assistant-first-and-connected-storage.md)
- [adr-temporal-record-model.md](adr-temporal-record-model.md)
- [adr-resident-communication-and-delivery-separation.md](adr-resident-communication-and-delivery-separation.md)
