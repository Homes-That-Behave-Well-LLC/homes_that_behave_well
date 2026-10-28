# UI Patterns

> **Document status: Active — subordinate to the HTBW canonical architecture.**
> Canonical authority: [../architecture/framework.md](../architecture/framework.md) and
> [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> **Known stale terminology, not yet fully reconciled (tracked, not silently fixed):** this document
> predates several since-accepted decisions. "Composite Room"/"composite tile" (§23) is superseded
> terminology — the accepted term is **Merged Room** (**DL-67**, **DL-68**); "Global Context" (§18) and
> "Alerts" predate the current seven-responsibility vocabulary and should be read against
> [../architecture/htbw-framework-aligned-ux-and-information-architecture.md](../architecture/htbw-framework-aligned-ux-and-information-architecture.md)'s
> Subject/Perspective/Scope/Filter/Surface vocabulary (§9 there) rather than taken as a competing model.
> A full terminology pass is follow-on work (see that document's final report, item H), not performed
> in this edit.

## Purpose

UI Patterns define how the system presents information and interacts with the user.

They ensure all interfaces are:

- consistent
- predictable
- explainable
- aligned with Home Assistant standards
- derived from system configuration and runtime models

---

## Core Principle

The user interface must feel native to Home Assistant while delivering a more disciplined and predictable experience.

---

## Foundational Rule

The UI is a projection of configuration and runtime state.

The UI must not:

- execute system logic directly
- act as a source of truth
- store independent state

---

## System Boundary (Critical)

The system is divided into:

### Global Configuration

- AI providers
- external integrations (M365, etc.)
- authentication and system settings
- archive storage destination wiring (for example NAS URI)

Not exposed in main UI.

Operational exception for archive visibility:

- Concierge main UI may show archive health/status and offer export actions
- Concierge main UI must not edit archive destination connection settings
- archive destination edits must remain in integration options (gear/cog)
- archive policy toggles and export controls in main UI must be disabled or hidden until a valid archive destination is configured

---

### Operational UI

- rooms
- interactions
- signals
- global context usage
- scene exposure and configuration

These are Home Assistant-native sections and flows, not a separate UI shell.
They should be implemented with native panels, cards, dialogs, and selectors so the experience remains indistinguishable from Home Assistant.

---

## Foundations

The UI must always:

- reflect system state clearly
- preserve user context
- avoid unnecessary complexity
- prioritize understanding over control

---

# 1. Navigation Patterns

## Breadcrumb Navigation

Breadcrumbs must:

- always be visible
- reflect the user's entry path
- be fully clickable
- not force hierarchy

Example:

Home > Living Room > Painting  
Alerts > Painting  
Documents > Appraisal  

---

## Back Navigation

Back navigation must restore:

- selected tab
- filters
- scroll position (best effort)

---

## Cross-Domain Navigation

Cross-cutting views must remain independent.

Examples:

- Alerts
- Documents
- History
- Interactions

Rules:

- do not force hierarchy
- preserve original context

---

# 2. Information Hierarchy

Every screen must follow:

1. Status
2. Context
3. Explanation
4. Actions
5. History

---

## Example: Room Dashboard

Status:
- room state
- confidence

Context:
- environment summary
- global context availability

Explanation:
- primary issue or insight

Actions:
- available interactions

History:
- optional drill-down

---

# 3. Progressive Disclosure

The UI must reveal information progressively.

Rules:

- show high-level state first
- allow drill-down for detail
- never overwhelm the user

---

# 4. State Visibility and Explainability

The UI must always show:

- what is happening
- why it is happening
- confidence in the result

---

# 5. Empty State Handling

The UI must never show unexplained gaps.

When data is missing:

- explain why
- guide resolution

---

# 6. Action Patterns

## Core Rule

UI actions do NOT execute system behavior directly.

UI must:

- call services
- reflect results

---

## Buttons

Buttons must:

- follow HA standards
- provide immediate feedback
- reflect loading/disabled state

---

## Confirmation

Required for:

- destructive actions
- major configuration changes

---

# 7. Dialog (Popup) Patterns

Dialogs must:

- use HA native components
- be consistent in layout

---

# 8. Iconography

### Layer 1: Native

- entities
- sensors

### Layer 2: System

- signals
- context
- interactions

---

# 9. Color Semantics

- Blue → context  
- Green → normal  
- Amber → warning  
- Red → critical  
- Gray → unknown  

---

# 10. Layout Patterns

Structure:

- top → summary
- middle → context and explanation
- bottom → detail and history

---

# 11. Consistency Rules

The same concept must appear identically everywhere.

---

# 12. State Synchronization

UI must:

- read from runtime models (coordinator/store)
- not compute state
- not simulate final state

---

# 13. Voice and UI Alignment

Voice and UI must match:

- terminology
- explanation
- behavior

---

# 14. Performance and Responsiveness

UI must:

- feel immediate
- not perform heavy logic
- rely on precomputed data

---

# 15. Interaction Feedback and Perceived Performance

## Rule

Every user action must produce immediate visible feedback.

### Immediate Feedback

- highlight selection
- update state instantly

### In-Progress Feedback

- spinner
- disabled state

### Completion Feedback

- state update
- confirmation

---

# 16. Interaction Panel Pattern (NEW)

## Purpose

Provides a unified surface for:

- signals
- context
- actions
- workflows

---

## Structure

Room Interaction Panel:

- Context (weather, news, email)
- Signals (laundry, calendar)
- Actions (available controls)
- Workflows (setup, guided flows)

---

## Rules

- must display only active interactions
- must not store independent state
- must reflect interaction model

---

# 17. Scene and Alias Visibility (NEW)

Scenes must be visible and configurable.

UI must show:

- scene name
- aliases (from Home Assistant)
- enable/disable for room
- composite inclusion

---

## Rules

- aliases are source-of-truth (HA)
- UI may allow editing aliases
- UI must not duplicate phrase systems

---

# 18. Global Context UI Pattern (NEW)

Global context must be configurable in UI.

Examples:

- weather
- news
- calendar
- email

---

## Rules

- enable/disable per context
- configure summarization behavior
- support per-room projection
- when a room dashboard target exists, support projection of global context digest cards (including news)
- when a room or person phone target exists, support projection of global context digest payloads to mobile app
- keep visual payload aligned with voice digest selection for consistency across channels

---

# 19. Configuration Projection Rule (CRITICAL)

UI must always reflect:

- configuration (store)
- runtime state (models)

UI must never:

- be the source of configuration truth
- modify behavior outside services

---

## Flow

UI → service call → validation → store update → runtime update → UI refresh

---

# 20. Optimistic vs Confirmed Updates

Optimistic:

- safe UI-only updates

Confirmed:

- required for state changes and execution

---

# 21. Relationship to Runtime

UI must:

- call Concierge services
- render interaction model
- reflect execution results

UI must not:

- directly manipulate entities
- bypass execution patterns
- perform orchestration

---

# 22. User Experience Principles

The UI must always:

- prioritize clarity
- minimize effort
- build trust
- avoid noise

---

# 23. Merged Room UI Pattern (NEW)

Merged room (composite) creation must be managed from the main Concierge UI.

Required UI flow:

1. user enters merge mode from main screen
2. user provides merged room name
3. user selects member rooms using room-card checkboxes
4. user confirms merge

Rules:

- merge mode must only allow selecting rooms on the same floor
- cross-floor selection must be rejected with clear inline feedback
- merge confirmation must show selected rooms and floor before save

---

## Main Screen Projection Rules

After merge succeeds:

- member room tiles must be replaced by one composite tile
- composite tile title must use the merged room name
- composite tile must list member room names for quick reference
- member room tiles must not remain visible as primary cards in that view

If merge is removed:

- composite tile must be removed
- member room tiles must return

---

## Composite Edit and Unmerge Pattern

Composite tiles must expose an Edit action from the main Concierge UI.

Edit UI must include:

- editable composite name
- checklist of current member rooms
- save action with validation feedback

Rules:

- unchecking one room removes that room from the composite
- if one room is removed, that room tile must reappear in the main screen while remaining members stay as a composite tile
- if all rooms are removed, the composite must be dismantled and removed from the main screen
- when dismantled, all individual room tiles must return

---

Composite rename rules:

- rename must happen in the same Edit flow
- updated name must appear on the composite tile immediately after confirmed save

---

## Composite Detail Configuration Rules

Selecting a composite tile must open composite detail configuration.

Composite device selectors must be built from the union of devices across all member rooms.

Rules:

- no duplicate entities in selector lists
- ordering must be deterministic
- unavailable entities must be visibly marked

---

# 24. Setup Mode: Rooms And People (NEW)

The main setup experience must allow choosing setup intent first.

Required setup entry choices:

- Rooms And Areas
- People

Rules:

- selection must be explicit before entering definitions
- each setup path must keep its own forms, validation, and guidance
- switching paths must preserve unsaved work warning behavior

---

## Rooms And Areas Setup Path

The rooms path configures:

- rooms
- merged spaces
- controllable device scope per room and space

This path remains the foundation for deterministic local-first resolution.

---

## People Setup Path

The people path must use Home Assistant person entities as the starting point.

People setup configures:

- BLE proximity device links such as iPhone and watch sources
- Aqara room presence device links used as supporting context
- optional voice enrollment status
- mobile app interaction targets (for example phone and iPad)
- household classification (minor/adult)

People setup must not duplicate person identity records outside Home Assistant references.

People setup must treat device links as editable parts of the person definition.
People setup must allow enabling or disabling each mobile target per person.
People setup must allow explicitly marking a person as a minor.

Minor setup guidance:

- when person is marked as minor, default to child-safe data handling and reduced audit detail
- display plain-language guardian notice for consent-sensitive features (for example voice enrollment)
- minor/adult classification must be explicitly selected and never inferred from behavior
- provide a standard minor AI setting with explicit choices:
	- block general Q&A
	- allow restricted intent classes only
	- allow general Q&A (only when policy permits)

Interaction option filtering rule:

- when a person is identified or explicitly selected, UI delivery options must only show that person's enabled mobile app targets
- device class labels should be visible (for example phone, tablet)


---

# 25. People Tiles Pattern (NEW)

People should be represented in tiles, similar to room tiles.

People tiles should show:

- linked BLE proximity devices
- linked room presence devices

Tile actions should include:

- link or unlink devices

Rules:

- people tiles are projections of model state
- tile actions must call services
- no direct state mutation in UI

---

# 26. Mid-Conversation Style Adjustment Surface (NEW)

The UI should expose recent style adjustments captured during conversation.

Examples:

- switched to brief responses
- reduced follow-up prompts
- enabled more detail

Rules:

- each adjustment must be explainable in plain language
- users must be able to keep, undo, or reset adjustments
- saved adjustments must update person profile deterministically
- selections must persist through services, not direct UI mutation

---

# 27. Person Enrollment Detail Pattern (NEW)

The person detail screen must show enrollment and device-binding state.

Required detail sections:

- identity overview
- linked BLE proximity devices
- linked room presence devices
- voice enrollment status
- interaction style summary
- recent corrections and adjustments

Rules:

- device links must be editable from the detail screen
- voice enrollment may be enabled or deferred independently
- details must remain human understandable and plain language
- selections must persist through services, not direct UI mutation

---

# 28. Native HA Component Conformance Order

**"Native First. Native Extended."** HTBW is a Home Assistant integration; it uses current official
Home Assistant developer documentation, object models, frontend components, selectors, forms,
registries, and interaction conventions wherever they satisfy a requirement. Before any new HTBW UI
element is created, apply this order:

1. Use a native Home Assistant component directly (entity/device/area/floor/label/tag selectors,
   native form controls, dialogs, conditional form behavior).
2. Configure or constrain the native component.
3. Compose native components into an HTBW experience.
4. Extend an established Home Assistant pattern, documenting the HTBW-specific requirement driving
   the extension.
5. Create a custom HTBW component **only** when none of the above satisfies the requirement, and
   document explicitly why no native pattern applies.

A custom HTBW component, where genuinely necessary, still uses Home Assistant design conventions,
reuses Home Assistant components where technically appropriate, and honors Home Assistant theming,
accessibility conventions, responsive behavior, interaction patterns, and platform terminology. **Do
not substitute a generic web control, and do not create a control that merely looks similar to a Home
Assistant control** — the objective is a luxury Home Assistant experience, not a luxury application
embedded inside one.

# 29. Accessibility

Follow Home Assistant frontend conventions and current applicable accessibility guidance for:
keyboard navigation, focus visibility, screen-reader labeling, semantic controls (never a `<div>`
masquerading as a control), contrast, touch targets, reduced motion where applicable, and
communicating meaning without color alone — directly extending §9's existing color-semantics table,
which must never be the sole channel for a status distinction.

# 30. Responsive Design

The commissioning experience accounts for desktop, tablet, phone, and the Home Assistant Companion
App/WebView and other supported presentation contexts. Composition adapts by form factor; a desktop
layout is never preserved where doing so makes the interface unusable on a smaller surface. This
extends, and does not replace, §13's existing "Performance and Responsiveness" rule.

# 31. Motion

Use animation purposefully — expansion, drill-in, help panels, and meaningful state transitions —
never decoratively merely to appear premium. This extends §15's existing Interaction Feedback
patterns; motion communicates state change, not brand polish.

# 32. Configuration Requirement Types

Do not reduce every configuration item to a flat Required/Optional binary. Where accepted architecture
supports the distinction (reusing **DL-41**'s own mandatory/optional dependency model, never a new
one), present:

| Type | Meaning |
|---|---|
| **Required** | HTBW cannot operate without it |
| **Capability Requirement** | HTBW operates; a specific capability depends on it (**DL-41** mandatory dependency for that capability) |
| **Enhancement** | The capability remains available; configuring this improves the experience (**DL-41** optional dependency) |

# 33. Dependency States, Readiness, and Health

Reusing **DL-41**'s already-distinguishable dependency states (not configured; configured but invalid;
configured but currently unavailable; healthy; degraded but usable; removed), the UI distinguishes
**Readiness** ("is this correctly commissioned?") from **Health** ("is this currently operating
correctly?") — a correctly commissioned capability may be temporarily unavailable without implying
improper commissioning. **No arbitrary completion percentage is shown** absent a future governed
mathematical definition for one; use meaningful states (Ready, Needs Attention, Unavailable
Dependency, Not Configured, Degraded) instead. Not every incomplete condition is an error — a Home can
be intentionally and correctly commissioned without every optional capability enabled.

# 34. Validation and Defaults

Prefer preventing invalid configuration over accepting it and surfacing an error afterward; use
Home Assistant-native selector filtering/validation where supported. Distinguish **invalid**,
**incomplete**, **unusual but permitted**, **unavailable**, and **degraded** — these are never
equivalent and never presented identically.

Every default is a product decision, never invented for UI convenience. Where useful, classify a
default's provenance as: Home Assistant/platform default; HTBW architectural default; discovered
household value; or intentionally unset. **Privacy, authorization, autonomy, identity, communication,
and trust-related defaults require explicit architectural grounding** — reusing, never bypassing, the
owning responsibility's own accepted rule (for example **DL-97**'s "no HTBW-wide default grace-period
value exists" pattern for escalation timing).

# 35. Destructive or Consequential Actions

Extends §6's existing Confirmation rule. Reserve explicit confirmation for genuinely consequential
actions — deletion, removing a relationship with downstream effects, reset, disabling a capability,
changing privacy/authority behavior, or an action that makes another capability unavailable — and
**explain the specific consequence**, never a generic "Are you sure?" Trivial actions never show a
confirmation dialog.

# 36. Search, Filtering, and Scale

Design People/Places/Assets collections so the architecture can support larger professional
installations — search, filtering, sorting, and grouping, using Home Assistant-native interaction
patterns, added when the collection genuinely needs them. Do not prematurely convert HTBW into an
enterprise data-grid application.

# 37. Empty States

Extends §5's existing Empty State Handling rule. An empty state teaches: what belongs here, why it
matters, and the next appropriate action — never a bare "No assets found." If the missing content must
first be configured elsewhere, say where it comes from and what remains unavailable until it exists.

# 38. Errors

Extends §4's existing State Visibility and Explainability rule. An error explains what happened, why,
what is affected, what the resident can do, and where to go — never a stack trace or low-level
implementation text in the normal experience. Deeper diagnostic detail remains reachable for
integrators through the same progressively-disclosed path (§3; the UX document's §25).

# 39. Iconography — Framework Layer Added

Extends §8's existing two-layer model (Layer 1: Native entity/sensor icons; Layer 2: System
signal/context/interaction icons) with a third, explicitly separate layer:

- **Layer 3: Framework** — the seven canonical responsibility icons (Foundation, Identity, Truth,
  Operational Trust, Stewardship, Continuity, Concierge) and genuinely HTBW-specific semantic icons.
  See [../architecture/htbw-framework-aligned-ux-and-information-architecture.md](../architecture/htbw-framework-aligned-ux-and-information-architecture.md)
  §24 — **this iconography does not yet exist and is tracked as follow-on design work, not produced
  by this edit.**

Layers 1 and 2 are never redesigned for Framework branding; Layer 3 never redesigns a standard Home
Assistant interaction icon merely for visual consistency.

# 40. UI Architecture Acceptance Gate

Every future HTBW UI experience, before it is considered architecturally conformant, demonstrates:

| Dimension | Required demonstration |
|---|---|
| **Architecture** | Correct Framework responsibility and subject scope; no duplicate ownership; no competing Home Assistant registry/model; correct **DL-41** dependency semantics; correct configuration authority |
| **Home Assistant conformance** | Native pattern investigated first (§28); native component used where appropriate; extension justified where used; no generic web control substituted for an appropriate native one; HA interaction conventions and theming followed |
| **Experience** | Screen purpose is understandable; household vocabulary used appropriately (never altering architectural meaning, per the UX document §25); help available where judgment is required; provenance understandable; consequences explained (§35); progressive disclosure manages complexity; context preserved; breadcrumbs/orientation correct (UX document §19); cross-Framework discovery reaches the authoritative owner |
| **Quality** | Responsive (§30); accessible (§29); theme-aware; empty (§37), loading, unavailable, and degraded states designed; errors actionable (§38); validation appropriate (§34) |
| **Outcome** | A knowledgeable homeowner can make the decision without external documentation ("Luxury" acceptance test); a professional integrator can still reach needed technical detail; the experience feels HTBW-branded; controls feel natively Home Assistant |

**"Luxury" acceptance test**: could an intelligent homeowner who understands their own household make
this configuration decision correctly without consulting external documentation? If not, determine
whether wording, discovery, contextual information, help, consequence clarity, provenance clarity, or
unnecessary low-level exposure is the gap — then verify an experienced integrator can still reach the
technical detail needed to commission and diagnose the system.

---

# Final Principle

The UI is not a control surface.

It is a window into a system that already knows what to do.

The user should feel:

- confident
- informed
- in control—without needing to manage complexity
