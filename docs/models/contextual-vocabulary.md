# Contextual Vocabulary Model

> **Document status: Canonical model.**
> Terminology: [glossary.md](glossary.md). Owning responsibility: **Foundation**, as part of
> [room-configuration.md](room-configuration.md).
> Contract: [../contracts/contextual-vocabulary-contract.md](../contracts/contextual-vocabulary-contract.md)

---

## Purpose

Residents speak household language. The platform speaks platform language. Contextual Vocabulary is
the explicit, persisted bridge between them, scoped to a Room.

## Question answered

*What do you call this, here?*

---

## What residents must never need to know

- Home Assistant entity IDs
- Home Assistant device names
- Manufacturer names
- Model names
- Formal asset names
- Internal service names
- The individual member names of an explicitly configured group

---

## Mapping examples

| Vocabulary Term | Maps to |
|---|---|
| **Lights** | explicitly selected overhead ceiling lights |
| **Lamps** | explicitly selected table or floor lamps |
| **Shades** | explicitly selected shades in the Room |
| **Speakers** | explicitly selected Sonos music speakers |
| **TV** | the explicitly selected LG television |
| **Media Player** | the explicitly selected Apple TV |
| **Piano** | the asset whose authoritative name is *1918 A.B. Chase 6' Grand Piano* |

---

## The platform domain must not dictate household vocabulary

Home Assistant may classify several devices as `media_player`, while HTBW Room Vocabulary
distinguishes:

- Speakers
- TV
- Media Player

Home Assistant may classify both ceiling fixtures and table lamps as `light`, while HTBW Room
Vocabulary distinguishes:

- Lights
- Lamps

**This household distinction is preserved. The device domain is an implementation detail, not a
household concept.**

---

## Rules

1. **Vocabulary is explicitly configured.** A term exists because the household created it.
2. **Vocabulary is persisted.** It survives restarts, reconfiguration, and platform upgrades.
3. **Vocabulary is deterministic.** The same term in the same Room resolves to the same target set
   every time.
4. **Vocabulary resolution must not require a runtime search of all devices in the Room.**
5. **Vocabulary resolution must not rely on guessing from entity names.**
6. **Vocabulary does not rename or replace the authoritative asset.** It provides a human interaction
   term within the configured Room context.
7. **The same word may have different configured targets in different Rooms.** "Speakers" in the Den
   is not "Speakers" in the Living Space.
8. **A derived recognition form is subordinate to the configured term it came from.** It never becomes
   a vocabulary entry, and a configured term always outranks it.

---

## What a term may resolve to

- One asset
- Multiple assets
- A configured asset group
- A controllable capability
- A knowledge asset
- An experience endpoint

A term that resolves to a group is addressed as one thing. The resident says "Shades", and seven
configured shades respond, without the resident knowing there are seven.

---

## Ownership

> **Do not define vocabulary as owned by Concierge.**
>
> **Room Configuration owns the mapping. Concierge consumes the resolved target.**

| Step | Owner |
|---|---|
| Define the term and its target set | Room Configuration |
| Persist the mapping | Room Configuration |
| Resolve term → target set for a Room Context | Room Configuration |
| Decide whether the resolved action is permitted | Operational Trust |
| Decide what should happen | Concierge |
| Execute | Concierge, through governed interfaces |

### Resolution compiles down to native targets

A resolved target set should **compile or map to native Home Assistant target concepts and intent
slots** — entities, devices, Areas, labels, domains, and device classes — so that execution and
voice handling use the platform rather than a parallel mechanism.

> **HTBW vocabulary remains richer than the native concept, and must not be reduced to Home Assistant
> entity aliases.** It carries Room-scoped meaning, participating assets, explicit exclusions,
> configured capability exposure, and Merged Room semantics. A native alias carries none of those.

---

## Native names and aliases

**OD-14 is resolved: native naming information is an *input*, and never an *authority*.** Governed by
**DL-31** and
[../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md).

Home Assistant documents that Assist uses *"the names of your entities, areas and floors, as well as
any aliases you've configured"*, that aliases may be added to an **entity, an Area, or a Floor**, and
that configured aliases *"are not only used by Assist, but can also be used by Google Assistant"*.

| Object | Home Assistant owns | HTBW behaviour |
|---|---|---|
| Native name | The Device or Entity name, including any registry name the resident set | **Read through the native reference.** Never duplicated as an independently maintained HTBW name |
| Native Assist alias | The alias, on the objects Home Assistant documents — **entity, Area, and Floor** | **Read.** May seed a term. Never overwritten by HTBW, and never a second store |
| Native Assist exposure | Whether an assistant may target the entity | A platform boundary HTBW may narrow and must never bypass |
| Contextual Vocabulary term | Nothing | **HTBW extension, held by reference to the native target** |

> **No native Device-level alias is documented.** Do not assert one. Do not describe native aliases as
> globally unique, globally conflicting, Area-scoped, Device-scoped, or assistant-scoped — Home
> Assistant documents none of those characterisations, and explicitly describes the **same alias
> applied to entities in different Areas**, matched in conjunction with the Area name.

### Seeding

When a native Device or Entity first becomes a participating target and no term exists for it, HTBW
may **seed** the term from native naming information.

A seed is a **starting point**. It is not a second authority, not continuous synchronisation, not a
permanent copy, and not an instruction to write anything back. It carries no claim that the native
name is the best household term.

Applicable native sources, in order of applicability: an applicable native Assist alias; the native
Entity name; the native Device name; any other documented native display name; and, only as a
deterministic fallback, a value derived from a native identifier.

**Where several native aliases apply, HTBW must not silently choose one.** All applicable native
values are offered as selectable seeds, attributed to Home Assistant, and none becomes active
vocabulary without acceptance. **Home Assistant does not document a precedence among an object's
aliases**, so no precedence is asserted; which seed is offered first is an implementation mapping, not
an architectural decision, and it does not reopen this model.

### The seed-once lifecycle

Seed status is a value of the **mapping source** this model already records for explainability. **It
is not a new model.**

| Mapping source | Meaning | Behaviour when the native value later changes |
|---|---|---|
| `native_seed` | Proposed from a native value; not yet accepted; no term is active | May be refreshed from the native value |
| `accepted_native_seed` | The resident accepted the native value unchanged | May be refreshed **only** where the accepted lifecycle permits it |
| `household_defined` | The resident supplied or edited the term | **Never automatically overwritten.** HTBW may surface that the native value changed and offer re-import |

A term whose target no longer resolves is `broken_mapping`; a term the household withdraws is removed
through the ordinary Room Configuration lifecycle, and its history is retained. **Seed status and
resolution state are different axes and must not be collapsed.**

### No automatic write-back

> **HTBW must never automatically write Room-scoped Contextual Vocabulary into native Home Assistant
> aliases.**

The rule does **not** rest on a claim that Home Assistant treats aliases as globally conflicting — the
documentation states the opposite for Area-disambiguated cases. It rests on four differences that the
documentation does support:

1. **A native alias is shared beyond Assist.** Home Assistant documents that configured aliases may
   also be used by Google Assistant. Writing an HTBW term back would change behaviour outside HTBW,
   in a surface HTBW does not govern.
2. **An HTBW term may not name a single entity at all.** It may resolve to a configured group, a
   capability, a knowledge asset, or an experience endpoint. There is no native alias equivalent.
3. **HTBW Room context is not Area context.** A Room may span Areas, and a Merged Room changes the
   applicable target set without changing any native object.
4. **Participation and explicit exclusion are not representable as an alias.** The Beam's exclusion
   from *Speakers* is configuration, and an alias cannot carry it.

Equally, **HTBW never automatically imports native alias changes over a household-defined term.**
Divergence between the native name and the household term is **intentional and supported**, and
nothing in either direction is synchronised.

An explicit, separate, resident-initiated action to publish an eligible object-scoped term as a native
alias is **neither required nor adopted here**. Home Assistant documents alias editing as a resident
interface action; **no integration-facing alias-writing capability is documented**, so none is claimed.
Were such an action ever adopted, it would have to be explicit, separate from saving a Room
Configuration, validated, limited to a term naming exactly one native object, never used for a group or
context-dependent term, never a means of altering exposure, and clearly identified as changing native
Home Assistant configuration. **The canonical behaviour remains no write-back.**

**This rule extends unchanged to a governed public service parameter** (**DL-114**, resolving **OD-81**):
a resident-authored vocabulary term may be supplied as a named Request-Parameter to a governed HTBW
capability and resolved privately, at invocation time, under the current Room Context — exactly as a
voice utterance already resolves under **DL-69** — but the term itself never becomes a native alias, a
published object catalog, or a durable target list merely because it can be addressed through a service.

### Groups stay in HTBW

A term resolving to a group is a Room Configuration mapping. **HTBW does not write the group term as
an alias onto every member.** Native targets are referenced, not copied.

Where a native target concept — an Area, a Floor, a label, a domain, a device class, or a documented
intent slot — already expresses the required set safely, **prefer the native target** and record which
native representation was used. Retain HTBW resolution only where Room-specific participation,
exclusions, grouping, or household meaning is additionally required. **Do not construct a duplicate
group for convenience.**

### Merged Rooms

A Merged Room is a Room, and vocabulary behaves identically in one. Because **participation in a
Merged Room is explicit and never inherited automatically**, merged vocabulary is **declared** in the
Merged Room's configuration rather than accumulated from its constituents. Where constituent Rooms use
the same term for different targets and the merged configuration does not declare the outcome, the
result is `ambiguous` and is surfaced, not guessed. Explicit exclusions survive merging, constituent
membership is retained so unmerging restores constituent behaviour, and **no native alias changes at
any point**. **A Merged Room has no native projection: DL-68 (resolved OD-70) found no proven consumer
requiring one, and Assist/Conversation must never receive one**, because this model's own resolution
rule above means HTBW already compiles a term to a concrete governed target set before any native
targeting occurs — a native stand-in would let Home Assistant's built-in conversation agent bypass
that curation entirely.

---

## Vocabulary is a first-class HTBW concept (DL-69)

Resolves **OD-62**. Full acceptance record is **DL-69** in
[../governance/decision-ledger.md](../governance/decision-ledger.md); this section is the canonical
model.

**Vocabulary is the governed household-language layer that maps a natural word or phrase to a
referenced Room, Merged Room, device, target set, Asset, service, information source, capability, or
another accepted HTBW meaning within an applicable context.** It answers *"what does this household
call this?"* Everything already stated in this document about Room-scoped Contextual Vocabulary is
Vocabulary — this section names the concept explicitly and extends it beyond Room scope. **This does
not create a new responsibility.** Vocabulary remains owned by Foundation, as part of Room
Configuration (**DL-09**, **DL-10**), for Room- and Merged-Room-scoped terms; **Person Setup
coordinates Person-scoped Vocabulary under the same concept**, exactly as it already coordinates other
Person-owned associations.

Vocabulary is **not**: a native Home Assistant identifier; a native Device or Entity name; a
replacement for a formal Asset name; a copied provider name; a globally unique registry name; a
permission; an exposure decision; an execution authorization; current proof of identity; a universally
visible alias; or an uncontrolled prompt synonym. Native Assist aliases remain a distinct, separately
governed concept (**OD-14**) that may only ever *seed* a Vocabulary term.

### Vocabulary context types

Vocabulary is **contextual, not globally unique**. The same word may mean different things, or nothing
at all, depending on which context is currently applicable. The accepted context types are:

| Context | Example |
|---|---|
| Physical Room | "Sofa Lamp" in the Den |
| Merged Room | "Art Lights" in Living Space |
| Person | "Mail" for Tom, "Inbox" for another Person, for the same underlying mailbox capability |
| **Home (Global)** | "Piano", "Front Door" — a term with no narrower configured scope, inherited everywhere (**DL-70**, resolved **OD-13**) |
| Capability | A term scoped to what it names rather than where — a service or information source |
| Interaction (active clarification) | The bounded candidate set offered during an in-progress clarification |

### Context precedence

Where more than one context could apply, the **narrowest context that deterministically resolves the
meaning** is used, in this tested order:

1. **Active clarification context** — a candidate already offered in this interaction.
2. **Current Person context**, for a Person-owned capability (a mailbox, calendar, shopping list, or
   news source configured per Person). **Never for a Room- or Merged-Room-owned device term** — a
   Person may never redefine what a Room calls its own devices (**DL-70**).
3. **The current exclusive Merged Room** (**DL-67**).
4. **The current Physical Room.**
5. **Home (Global) scope** — a term defined once and inherited everywhere no narrower term exists
   (**DL-70**, resolved **OD-13**).
6. **Native handling**, only under the governed no-match and fallback rule below.

**A Room or Merged Room may shadow a Home-scoped term with its own definition.** Shadowing applies
only within that Room or Merged Room; the Home-scoped term is unaffected everywhere else. This is
never replacement, and never a second copy of the same word.

### Vocabulary versus Fulfillment (DL-70)

**Vocabulary is the household word. Fulfillment is which provider, target, script, Asset, capability,
or source currently satisfies it.** A Vocabulary term may remain Home-scoped and stable while its
Fulfillment varies by Room, Merged Room, or Person — for example the word "News" stays the same
everywhere, while the Office's configured news sources differ from the Den's. This is not a new
mechanism: Room, Merged Room, and Person configuration already carry Fulfillment fields (source and
target selections) independently of the word chosen for them.

### Vocabulary target shapes

A term may resolve to any of the following, each an existing configuration mapping to stable native
references — never a copy of entity state, and never a parallel registry:

| Shape | Example |
|---|---|
| Single target | "Sofa Lamp" → one entity |
| Named target set | "Art Lights" → Living Room Art Lights + Dining Room Art Lights |
| Category set | "Lamps" → Sofa Lamp + Corner Lamp + Reading Lamp |
| Asset | "Piano" → the formally named Asset |
| Service or information capability | "News" → a configured news capability |
| Person-scoped service | "Mail" → the current Person's configured mailbox capability |
| Governed execution outcome | "Music" → the Room's accepted Music entry point |
| Retrieval class | "Why did this happen?" → the resident-safe Decision Trace explanation capability |

### Vocabulary cardinality is configuration, never grammar (DL-69)

**A collection term's target-set size, and whether member-level terms are separately configured, are
configuration properties. Language-specific singular/plural morphology is implementation mapping and
is never hard-coded into this architecture.**

A household may configure a collection term ("Lamps") whose target set has more than one member, and
may separately configure a member-level term for one or more of those members ("Sofa Lamp", "Corner
Lamp", "Reading Lamp"). **This reconciles, rather than overrides, the existing recognition-form rule
above** ("a derived recognition form resolves to exactly its authoritative term's target set", and "a
plural form never creates or expands a group"):

- Where a household has **not** configured member-level terms, a singular derived form of a configured
  collection term continues to resolve to that term's whole target set, exactly as already accepted.
  "Turn on the lamp" behaves as a recognition form of "Lamps" and activates the full configured set.
- Where a household **has** configured distinct member-level terms for members of a collection, a
  singular utterance that could equally match more than one already-configured member term is the
  existing `ambiguous` state ("more than one configured mapping matches") — **no new state is
  introduced.** The existing failure-behaviour rule applies: ask which was meant, offering only
  exposed, contextual, member-level terms ("Sofa Lamp, Corner Lamp, or Reading Lamp"), **never full
  native device names, never unconfigured devices, and never targets outside the resolved Room or
  Merged Room context.**

Member-level terms, where configured, are ordinary Contextual Vocabulary entries scoped identically to
any other term. **Setup should support configuring member-level terms alongside a collection term**,
so a later singular reference has genuine bounded candidates rather than none.

### Command resolution and safe native fallback (DL-69)

**Home Assistant's documented Assist Pipeline, Conversation, and Intent facilities are retained in
full and are not duplicated** (see
[../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md), *Governed
conversational retrieval and command resolution*). HTBW supplies household-specific meaning at the
Conversation extension point; Home Assistant supplies the pipeline and execution facilities.

The accepted resolution sequence:

1. Home Assistant's documented pipeline stages run (wake word, Speech-to-Text, Conversation/Intent,
   Text-to-Speech).
2. The receiving voice-assistant endpoint supplies its Room assignment as the default Room Context.
3. **DL-67** resolves the exclusive Merged Room, if the Physical Room participates in one.
4. HTBW evaluates the utterance against configured Vocabulary in the resolved context (Physical Room,
   Merged Room, or current Person, per the precedence order above), compiling to a concrete, governed
   target set **before** any native targeting occurs.
5. A governed match resolves to its configured target or execution entry point; Identity, Operational
   Trust, Assist Exposure (**DL-66**), HTBW Exposure, consent, audience, and confirmation requirements
   still apply.
6. Execution uses the closest accepted native Intent, service, script, scene, or HTBW entry point.
7. **Native fallback is considered only afterward, and only where safe.**

**A failed HTBW vocabulary match must never silently authorize an unrelated or materially broader
native action.** Six outcomes are distinguished:

| Outcome | Behaviour |
|---|---|
| Deterministic HTBW match | Execute after governance checks |
| Ambiguous HTBW match | Clarify from bounded, contextual, exposed candidates only |
| No HTBW match, exact/permitted/exposed/safe native candidate | Native handoff may proceed |
| No HTBW match, plausible but non-equivalent native interpretation | **Never execute silently.** Clarify, replay what was heard, or safely refuse |
| No HTBW match, no safe native match | Return an honest no-match response |
| Recognized text with residual uncertainty | Replay what was heard, or offer a bounded "did you mean" suggestion — never execute before confirmation |

A "did you mean" suggestion is drawn only from already-configured Vocabulary or a verified-safe native
target, is never an open-model invention, never converts semantic similarity into authorization, never
discloses unauthorized candidates, and always preserves the original recognized text for explanation.
**No recognition-confidence claim is made, because none is documented as available** to a custom
conversation agent (see the home-assistant-boundary.md verified-sources table).

This is the accepted resolution of the architecture-owner's "Bedtime" scenario: a resident says
"Bedtime"; no configured Vocabulary matches; the correct outcome is a safe refusal, a replay, a bounded
suggestion requiring confirmation, or an exact/permitted/safe native handoff — **never** a materially
broader native action (such as turning on every Room light) executed without confirmation merely
because some native interpretation existed.

### Generic activation preserves existing state (DL-69)

A generic activation command ("turn on the lamps") **preserves the household's existing accepted state
rather than forcing a changed one.** [continuity.md](continuity.md) already accepts "last lamp levels"
as governed Person- and Room-scoped state; a generic command consults that existing record where one
exists. Home Assistant's own light documentation states only that `light.turn_on`'s brightness, color,
and other parameters are **optional** — it does not document a universal "restore previous brightness"
behaviour, and none is claimed here. The exact device- or integration-level outcome where no
Continuity record exists remains implementation mapping, verified individually under **DL-30**.
**An explicit request for a specific level, color, or scene is unaffected** and always takes the state
the resident asked for.

### Person-scoped Vocabulary

A Person may configure their own term for a Person-owned capability — a mailbox called "Mail" by one
Person and "Inbox" by another, a calendar called "Schedule" by one and "Calendar" by another, or a
shopping list called "Groceries" or "Liquor Run" — exactly as
[person-and-identity.md](person-and-identity.md) already references such capabilities "through the
responsibility that governs their use." **No Person-specific Vocabulary, or the existence of the
underlying capability, is disclosed to another Person without authorization**, and an Unknown Person
receives no Person-scoped mapping (**DL-33**).

**Person Vocabulary is restricted to Person-owned capabilities and resources, and never redefines a
Room- or Merged-Room-owned device term (DL-70).** A Person is never permitted to give their own
private meaning to a Room's devices — device and Asset Vocabulary remains Room Configuration's sole
authority. Allowing otherwise would mean the same utterance, in the same Room, resolving differently
depending on who spoke it, which breaks the existing "two voice assistants in the same Room produce
the same target resolution" guarantee.

### Vocabulary collision behaviour (DL-70)

| Case | Behaviour |
|---|---|
| The same word in two different Rooms (or Merged Rooms) | **Not a collision.** Ordinary Room scoping — each resolves within its own context |
| Two simultaneous definitions of the same word in the *same* scope | A **configuration-invariant violation**, never silently arbitrated at runtime. Setup must prevent it; where it nonetheless occurs, it is a **DL-65** Repairs candidate (a configuration invariant ordinary runtime evaluation cannot resolve), exactly as a duplicate Primary Authority already is |
| Home scope versus Room or Merged Room | **Shadowing** — the Room's definition applies only within that Room; the Home-scoped term is unaffected everywhere else |
| Person versus Room | **Valid** only where the Person-scoped term genuinely names a Person-owned capability, resolved through the context-precedence order above. **Never valid** as a Person redefining a Room- or Merged-Room-owned device term |

---

## Changing or withdrawing a term — the household consequence is open

This model governs how a term **comes into existence**: it is created by the household, may be seeded
from a native value, resolves deterministically, and becomes `broken_mapping` when its target no longer
resolves. Of removal it says only that a term the household withdraws is **removed through the ordinary
Room Configuration lifecycle, and its history is retained**.

> **History retained is not habit preserved.** **What the home owes the people who still use the old
> word is not settled, and is OD-86.**

Open there, and deliberately unanswered here: whether a superseded term is recognised at all and for how
long; whether the home may say that a word it once understood is no longer configured, and which
responsibility says it; how a change is explained afterwards, given that under **P30** a Decision Trace
references the exact vocabulary version and so remains accurate while the household habit does not;
what is owed regarding household-authored automations, scripts, and scenes that named the previous
target; and what becomes of retained references and of Continuity values captured under the earlier
term.

**Nothing is asserted here.** **No transitional alias, deprecation window, grace period, or withdrawal
behaviour is introduced by recording this**, and none may be inferred from it. Rule 6 stands unchanged:
vocabulary never renames or replaces the authoritative asset. HTBW references household automations as
named executors and **never rewrites, wraps, or migrates them**.

**This question exists because it was once owned and was not carried forward.** The superseded
`adr-room-vocabulary-governance.md`, `room-vocabulary-registry-contract.md`, and
`room-vocabulary-registry-model.md` carried a *managed vocabulary lifecycle*. **They are Historical and
are not reactivated** — they are evidence that the question existed, never authority for its answer.

**Inheritance across scopes is a different question and remains OD-13.**

---

## Recognition forms

**A resident configures one term. HTBW may derive additional forms of that term so that ordinary
speech is understood.** A recognition form is a **projection of the configured term** — the same
pattern **DL-31** applies to native objects — and never a second vocabulary record.

| Authoritative term | May be recognised as |
|---|---|
| Lamp | Lamp, Lamps |
| Shade | Shade, Shades |
| Speaker | Speaker, Speakers |
| Shades | Shades, Shade |

> **The authoritative term is whatever the household configured, in whatever form they chose.** This
> model's own examples — *Lights*, *Lamps*, *Shades*, *Speakers* — are plural, and remain valid
> exactly as configured. **HTBW must not require a singular term, must not rewrite a configured term
> into another form, and must not add a second field for any other form.**

A recognition form is:

- **generated**, from the configured term alone
- **not independently configured, owned, exposed, or persisted as vocabulary**
- **traceable** to the authoritative term, and explainable
- **resolved to exactly the authoritative term's target set** — nothing more and nothing less

> **Derivation never reads the target.** A recognition form is derived from the configured term, never
> from a native name, an alias, an entity ID, a device class, or a domain. Rule 5 — *resolution must
> not rely on guessing from entity names* — is unchanged and unweakened.

### A configured term always wins

| Situation | Outcome |
|---|---|
| The spoken word matches a configured term in this Room | The configured mapping resolves. **Derivation is not consulted at all** |
| It matches only a derived form of one configured term | That term resolves, to that term's target set |
| It matches derived forms of two or more configured terms, and no configured term | `ambiguous`. Ask which was meant. **Never guess** |

This uses the resolution states this model already defines. **It is not a new state model, and it
adds no new field.**

### Grammatical form is not group meaning

**Pluralisation does not multiply targets.**

| Concept | What it is | Where it comes from |
|---|---|---|
| *Lamps* as a **recognition form** of *Lamp* | The same meaning, said differently | Derived |
| *Lamps* as a **group term** — the Corner, Sofa, and Bookcase lamps | A different, larger target set | **Explicitly configured**, as *Groups stay in HTBW* above |

Where the household has configured *Lamps* as a group, that configured mapping resolves — because a
configured term always wins. **A plural form alone never creates, implies, or expands a group**, and
nothing here changes existing group behaviour.

### Language, display, and scope

Derivation is **language-dependent**. HTBW must not assume the morphology of one language applies to
another. Where a form cannot be derived safely, **HTBW derives nothing** and the configured term still
resolves exactly as configured.

Residents may be shown which forms will be understood, alongside the term they configured, so that
behaviour is visible rather than hidden. **The display is read-only and derived; only the
authoritative term is editable.** This is an architecture expectation — it prescribes no frontend
technology, layout, or component, and requires no additional stored value.

Recognition forms participate exactly as their authoritative term participates — in Room Help,
participation, exposure, authority, target resolution, and Merged Rooms alike. **They introduce no
Merged Room semantics of their own**, and **OD-70** remains untouched.

---

## Knowledge assets

A vocabulary term may resolve to a knowledge asset rather than a controllable capability.

```
Authoritative asset name:  1918 A.B. Chase 6' Grand Piano
Room vocabulary term:      Piano
Resident asks:             "Tell me about the piano"
Resolution:                Room Context → term "Piano" → that asset → asset knowledge
```

The asset's authoritative identity is unchanged. The vocabulary term is an interaction alias, not a
rename.

---

## Consumes

- The Room's participation set from [room-configuration.md](room-configuration.md)
- Foundation asset identifiers and capability descriptions

## Provides

- Deterministic term → target-set resolution scoped to a Room
- The exposed-term list used by Room Help
- Configuration provenance for explainability

---

## Explicit non-responsibilities

Contextual Vocabulary does **not**:

- Decide whether the resolved action is permitted
- Decide what should happen
- Rename the authoritative asset
- Discover targets at runtime
- Infer meaning from entity naming conventions

---

## Failure behavior

| Condition | Behavior |
|---|---|
| Term not configured in this Room | State that the term is not configured here. Offer to show what is available. Never runtime-search. |
| Term maps to targets that no longer exist | Report a broken mapping as a configuration problem. Do not silently substitute. |
| Term maps ambiguously (two configured mappings match) | Ask which was meant, offering only exposed options. Record the ambiguity. |
| Term resolves to a partially available group | Apply the configured partial-availability policy; report which members were unavailable. |
| The Room Context is unresolved | Do not attempt vocabulary resolution. Resolve the Room first. |

## Privacy considerations

Exposing a term makes a capability discoverable by anyone who can speak in the Room. Sensitive
capabilities must be protected by Operational Trust authority, not by an obscure term.

## Explainability requirements

Every resolution records: Room Context, term, resolved target set, mapping source. Every failed or
ambiguous resolution records the reason and what the resident could do about it.

Where a derived recognition form was matched, the resolution records **the form heard and the
authoritative term it resolved to**, so that the household can see why a word was understood.
Explanations are still spoken in the household term. **Residents are never required to understand
linguistic mechanics to receive a usable explanation.**

---

## Representative scenarios

- [../scenarios/room-vocabulary.md](../scenarios/room-vocabulary.md)

## Open decisions

| ID | Question |
|---|---|
| OD-02 | **Closed — DL-43, DL-44, DL-45.** Vocabulary definitions are located through a governed artifact reference; encoding remains capability-specific |
| OD-13 | Whether vocabulary terms may be inherited from Home scope and overridden per Room |
| OD-14 | **Resolved.** Native aliases are an **input** — a seed — and never an authority. See *Native names and aliases* above |
| OD-86 | **What the home owes the household when a term is changed, retargeted, or withdrawn.** Raised 2026-08-27. See *Changing or withdrawing a term* above. A wake-word change is admissible there only as a household-vocabulary sub-question and remains deferred behind **#146** |

## Related documents

- [room-configuration.md](room-configuration.md)
- [room.md](room.md)
- [../contracts/contextual-vocabulary-contract.md](../contracts/contextual-vocabulary-contract.md)
- [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md)
