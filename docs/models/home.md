# Home Model

> **Document status: Canonical model.**
> Terminology: [glossary.md](glossary.md). Owning responsibility: **Foundation**.

---

## Purpose

The Home is the outermost governed scope. It is the container for Rooms, People, Pets, Assets,
Services, Relationships, and home-scoped policy.

## Question answered

*What is the whole household, and what is true or governed at the level of the whole household?*

---

## Owns

- Home identity and identification
- The set of Physical Rooms
- The set of Rooms and Merged Rooms
- The set of People and their Roles in the Home
- The set of Pets
- The set of Assets
- The set of Services and providers
- The Relationship set that binds the above
- Home-scoped configuration primitives

## Home-scoped state and policy

Home-scope is where household-wide behavior is declared:

- Security posture
- Safety policy
- Emergency behavior
- Quiet hours
- Home maintenance calendar
- Maturity review interval (**DL-107**) — household-configured; HTBW defines no default interval
- Global autonomy ceiling
- Global conflict policy
- Default privacy policy

Ownership of these items follows the responsibility model: Foundation defines the *shape*,
Operational Trust owns *policy*, Stewardship owns the *maintenance calendar's obligations*, and Truth
owns *current home-level facts* such as "the home is in Away state" or "a whole-Home maturity review
became due" — the latter compared against the Home-level **last whole-Home maturity review performed**
tracking point (**DL-107**). Where no interval is configured, the maturity-review backstop is
**Configuration Incomplete** and reported as such, never silently defaulted or disabled; see
[../assessment/assessment-to-platform.md](../assessment/assessment-to-platform.md), "Reassessment
Cadence and Triggers (DL-107)".

---

## Consumes

Nothing. Foundation is definitional.

## Provides

- Canonical identifiers for every household object
- Scope resolution: Home → Room → Person → Asset → Relationship
- Temporal conventions (timestamps, validity windows, time zone handling)
- Provenance conventions shared by every responsibility

---

## Explicit non-responsibilities

The Home model does **not**:

- Decide what is currently true (Truth)
- Decide what is allowed (Operational Trust)
- Decide what matters or what must be cared for (Stewardship)
- Store preferences or sessions (Continuity)
- Orchestrate anything (Concierge)

---

## Structure

```
Home
 ├── Physical Rooms          (normally backed by HA Areas)
 ├── Rooms                   (1..n Physical Rooms; Merged Room when n > 1)
 │    └── Room Configuration (participation, exposure, vocabulary, Room Help, composite inputs)
 ├── People                  (roles, identity-evidence associations)
 ├── Pets
 ├── Assets
 ├── Services / Providers
 └── Relationships
```

Floors may exist as an intermediate grouping where the household or platform provides them. Floors
are a **grouping**, not an interaction context. Residents interact with Rooms.

---

## Scope rules

Declared in full in [../architecture/behavioral-governance.md](../architecture/behavioral-governance.md).

| Scope | Representative content |
|---|---|
| Home | Security posture, safety policy, emergency behavior, quiet hours, home maintenance calendar, maturity review interval (**DL-107**), global autonomy ceiling, global conflict policy, default privacy policy |
| Room | See [room.md](room.md) and [room-configuration.md](room-configuration.md) |
| Person | See [person-and-identity.md](person-and-identity.md) and [continuity.md](continuity.md) |
| Asset | See [asset.md](asset.md) |
| Relationship | See below |

## Relationship scope

Relationships are first-class, not implied. Representative relationships:

- Person is caretaker of Asset
- Device is assigned to Person
- Voice assistant participates in Room
- Sensor contributes evidence to a Room composite fact
- Speaker participates in a Room music endpoint
- Asset belongs to or serves a Room
- Person has a Role in the Home
- Person has a Role in a Room
- Resident has authority over an Asset or capability

Each relationship carries provenance and may be explicitly configured, derived, or observed — and
which of those it is must be recorded. See principle P26 in
[../architecture/principles.md](../architecture/principles.md).

---

## Failure behavior

- A Home with no Rooms is a valid but unconfigured state and must be reported as such.
- An object whose Home scope cannot be resolved is a diagnosable error, never a silent default.

## Privacy considerations

Home-scope aggregates the most sensitive combinations of household data. Home-level summaries must
respect the audience present. See [../architecture/privacy.md](../architecture/privacy.md).

## Explainability requirements

Any decision that used a home-scoped policy must name that policy in its Decision Trace.

---

## Open decisions

| ID | Question |
|---|---|
| OD-01 | Whether a Home is represented as a Home Assistant config entry, subentry, or private record |
| OD-10 | Whether Floors are modelled as first-class HTBW scope or consumed only as a Home Assistant grouping |

## Related documents

- [room.md](room.md), [room-configuration.md](room-configuration.md)
- [../contracts/foundation-contract.md](../contracts/foundation-contract.md)
- [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md)
