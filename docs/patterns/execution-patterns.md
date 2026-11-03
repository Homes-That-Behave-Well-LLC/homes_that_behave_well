# Execution Patterns

> **Document status: Active — subordinate to the HTBW canonical architecture.**
> Canonical authority: [../architecture/framework.md](../architecture/framework.md) and
> [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Superseded terminology appears in this document: "Composite Room" is now **Merged Room**, and
> "Interaction Space" is now **Room Context**. See [../models/glossary.md](../models/glossary.md).

## Purpose

Execution Patterns define how Concierge performs actions in response to user commands.

They ensure:

- fast execution
- deterministic behavior
- consistent use of Home Assistant capabilities
- no runtime discovery or decision ambiguity

---

## Core Principle

Execution must be pre-determined.

Concierge must never decide how to execute an action at runtime.

All execution paths must be:

- defined in configuration
- resolved before execution
- executed immediately once intent is known

---

## Execution Strategy Hierarchy

For any action, Concierge must use the following priority:

1. Scene (preferred)
2. Group
3. Direct entity control

State restoration is a configured execution mode that may override entity-level behavior for specific capabilities.

---

## Execution Resolution Flow

Execution must follow a deterministic resolution path:

1. Voice or UI input received
2. Home Assistant attempts alias/entity resolution
3. If resolved:
   → direct execution (scene/entity)
4. If not resolved:
   → Concierge resolves intent
   → maps to execution_preferences
5. Execution occurs using predefined strategy

Rules:

- must not introduce additional decision layers
- must not re-evaluate execution at runtime
- must not depend on AI for execution decisions

---

# 1. SCENE-BASED EXECUTION

---

## Definition

A scene represents a complete, pre-defined action.

Scenes are the preferred execution method when available.

---

## Rules

- scenes must be explicitly selected or matched via alias
- scenes must be owned by integrations
- Concierge must call scenes directly using scene.turn_on
- scenes are the primary execution target for user-facing actions

Concierge must not:

- interpret scene behavior
- break scenes into individual entity actions
- replicate scene logic

---

## Alias Integration

Scenes must be directly invocable through:

- entity name
- Home Assistant aliases

Example:

Entity:
scene.close_afternoon_shades

Aliases:
- block the sun
- close west shades

Execution:

Voice → Assist → alias match → scene.turn_on

---

## Benefits

- parallel execution
- integration-optimized performance
- minimal latency
- no orchestration overhead

---

## Example

Command:
Close the shades

Execution:
scene.turn_on(scene.all_shades_closed)

---

# 2. GROUP-BASED EXECUTION

---

## Definition

Groups represent collections of entities controlled together.

Used when a scene is not available.

---

## Rules

- groups must be pre-defined
- must map to a specific domain
- must allow a single-call execution

Execution:

single service call to group

---

## Example

Command:
Turn off the lights

Execution:
light.turn_off(group.great_room_lights)

---

# 3. DIRECT ENTITY EXECUTION

---

## Definition

Fallback when neither scene nor group is available.

---

## Rules

- entities must be pre-mapped in configuration
- execution must be batched
- fan-out must be minimized

---

## Example

Execution:

cover.close_cover:
- cover.kitchen
- cover.living_room
- cover.dining_room

---

# EXECUTION CONFIGURATION

---

Execution preferences must be defined in Concierge configuration.

Structure:

execution_preferences:
  <capability>:
    mode:
    target:

Example:

execution_preferences:
  shades:
    mode: scene
    target: scene.all_shades_closed

  lights:
    mode: group
    target: group.great_room_lights

---

## Rules

- execution must always use configured targets
- configuration must be validated before storage
- runtime must never infer execution preferences

---

# PHRASE-TO-EXECUTION MAPPING

---

Execution may be triggered by:

1. Entity name (Home Assistant)
2. Entity alias (Home Assistant)
3. Concierge orchestration

---

## Alias-First Rule

The system must always prefer:

1. direct entity/scene alias match
2. configured execution preference
3. Concierge orchestration

Example:

"movie time" → scene.movie_mode  
"close the shades" → execution_preferences.shades  

---

## Rules

- alias-based execution must bypass Concierge when possible
- Concierge must not override valid entity matches
- phrase mapping must not be duplicated outside HA

---

# COMPOSITE ROOM EXECUTION

---

Composite rooms must:

- aggregate execution targets across areas
- prefer composite-level scenes
- fallback to group or entity when required

Rules:

- composite execution must remain single-call when possible
- must not loop per room
- must not duplicate execution per area

---

## Context Promotion

When a command originates in a room:

- if room belongs to composite
  → use composite execution context

---

# AUDIO EXECUTION (REFERENCE)

---

Audio routing must follow:

1. preferred speaker
2. speaker candidates
3. voice device fallback

Rules:

- audio resolution must be precomputed
- must not delay execution

---

# PERFORMANCE RULES

---

Execution must:

- use a single service call whenever possible
- avoid iterative loops
- avoid runtime entity discovery
- avoid template evaluation during execution

Execution must not:

- perform per-request entity filtering
- introduce layered processing
- re-evaluate configuration

---

# FAILURE HANDLING

---

If execution target is unavailable:

- fallback to next execution level

Example:

scene missing → use group  
group missing → use entities  

If no execution path exists:

- return clear failure response
- do not attempt alternative inference

---

# AI USAGE

---

AI must not:

- determine execution strategy
- override execution preferences
- interpret raw entity data
- execute actions

AI may assist only in:

- interpreting user intent before mapping
- summarization (non-execution)

---

# SYSTEM BEHAVIOR RULES

---

The system must:

- prefer scenes over all other methods
- execute immediately once intent is resolved
- remain deterministic across all paths

The system must not:

- dynamically choose execution methods at runtime
- duplicate execution logic
- introduce ambiguity in action routing

Execution must be independent of identity.

Identity may influence:

- how a response is delivered
- which description is used

Identity must not influence:

- which action is executed
- how execution is performed
---

# RELATIONSHIP TO OTHER PATTERNS

---

## Voice Integration

Defines how commands are resolved (alias-first)

## Configuration Patterns

Define execution preferences

## Runtime Architecture

Defines execution flow

---

# 4. STATE RESTORATION EXECUTION

> **Canonical resolution: DL-124 (OD-78).** The value-class taxonomy, native-storage ownership,
> restoration semantics (reproduction only; derivation not authorised), precondition set, and
> Merged-Room/keyed-collection treatment below are superseded in substance by **DL-124** —
> [../models/continuity.md](../models/continuity.md) and
> [../governance/decision-ledger.md](../governance/decision-ledger.md). This section is retained as
> implementation-pattern guidance and must be read consistently with DL-124, never as an independent
> source of restoration semantics.

## Definition

State restoration allows entities to return to a previously known state instead of a fixed configuration.

This supports natural interactions such as:

- turn on the lamps → restore previous brightness levels  
- resume media → restore previous volume  
- turn lights back on → return to last known state  

---

## Rules

- restoration must be explicitly configured  
- restoration must use stored state  
- restoration must not rely on inference or heuristics  
- restoration **reproduces** the stored value, gated by DL-124's precondition set (current Truth, Room
  mode, Identity band, Operational Trust outcome, audience, safety, target/capability availability) —
  it never silently computes a different value and presents the result as remembered (DL-124 point 8)

The system must not:

- guess previous values  
- reconstruct state from history  
- override explicit scene execution  

---

## State Source

Restored state must come from **a native Home Assistant Helper entity (or an equivalent native store
DL-30 verifies)** — this is DL-124's resolution of the previously undefined "runtime state snapshot or
cache." HTBW holds no copy of the value itself.

Rules:

- state must be captured before state-changing actions occur, subject to DL-124's dwell/attribution
  capture-eligibility rule — a value's own stability is never by itself evidence of resident authorship
- the native Helper is the system of record; HTBW stores no duplicate runtime cache
- retrieval reads the native Helper's current value directly (no history queries); recent native state
  **may** be consulted only to evaluate capture eligibility at the moment of writing, never as the
  source of a restored value

---

## Execution Behavior

Flow:

1. retrieve stored state  
2. validate entity availability  
3. apply state using a single batched call when possible  

---

## Example

Previous state:

lights: brightness 60%  

Command:  
turn on the lamps  

Execution:  
light.turn_on with brightness 60%  

---

## Configuration Example

execution_preferences:
  lights:
    mode: restore  

---

## Fallback Behavior

If restore state is unavailable:

- fallback to configured execution hierarchy (scene → group → entity)  
- must not fail silently  

---

## Performance Rules

- restoration must not introduce delay  
- must not query history systems  
- must use pre-stored runtime values  

---

## System Constraints

Restoration must:

- be deterministic  
- be explainable  
- be consistent across executions  

Restoration must not:

- override scenes triggered via alias  
- compete with explicit execution paths  

---

# FINAL PRINCIPLE

Execution defines how changes happen in the home.

It must always be:

- fast
- predictable
- pre-defined

The system must never think about how to execute—it must already know.