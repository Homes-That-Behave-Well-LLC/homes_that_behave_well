# ADR: Reasoning Provider Strategy

> **Document status: Canonical ADR.**
> Status: **Accepted** 2026-10-27. Records **DL-93** (issue **#132**, formal acceptance review PASS,
> following bounded stale-reference corrections made during the review).
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Resolves **OD-67**.
> Terminology: [../models/glossary.md](../models/glossary.md).

---

## Status

**Accepted 2026-10-27.** Formal acceptance review on Issue #132 returned **PASS**. Bounded
stale-reference corrections were made during the acceptance review itself (an ambiguous "separately-owned"
characterization of the proposed Home Steward product term in this ADR's own Status section; a stale
"General Reasoning" glossary entry still describing the pre-remediation Room-scope/Person-versus-Room
precedence model; two stale "drafted as DL-93, pending #132" references in
`home-assistant-boundary.md`'s representation table) — the decision itself is unchanged by any of these
corrections.

Resolves **OD-67**: which classes of Reasoning provider HTBW may use, for which purposes, under which
governance. No provider, vendor, model, or technology stack is selected here, and no provider
abstraction, API, or transport is designed here, consistent with the issue's own standing rule and with
**DL-30**.

This ADR creates **no new responsibility**. The seven responsibilities recorded in **DL-01** are
unchanged. The **Reasoning Provider owns nothing** — this restates, and does not relax, the glossary's
existing definition.

**Remediated 2026-10-27, prior to any formal acceptance review, in response to owner review.** The
original draft (commit `62a2e0b`) included Room-level General Reasoning authorization and a Room
provider fallback. **This was removed.** General Reasoning authorization belongs to the **effective
Person context** (the resolved household Person, or the household's designated Guest fallback Person
Extension where one exists, or the **DL-33** unidentified-person policy otherwise) — never to a Room. A
Room retains only its already-accepted, genuinely spatial responsibilities (interaction location,
input/output surface selection, delivery). This remediation also introduces **Home Steward** as a
working name, bounded here only to the extent of stating it is independent of General Reasoning; the
Home Steward product itself is not defined or owned by this ADR.

**This ADR distinguishes Reasoning from Home Intelligence, and from Home Steward.** Home Intelligence's
own governance (**DL-84**, **DL-85**, **DL-86**) was **accepted 2026-10-14 (Issue #191, formal
acceptance review PASS)** — a status this ADR's original draft understated, because the acceptance had
not yet been propagated into this repository's governance documents when the original draft was
written; see *Notes on the 2026-10 Home Identity and Home Intelligence Architecture Review* in
[decision-ledger.md](../governance/decision-ledger.md). This ADR does not decide, narrow, or redefine
**DL-86** or any Home Intelligence boundary; it confirms only that General Reasoning, Home Intelligence
(an optional deployment/hosting boundary — **DL-86**), and Home Steward (a tentative, proposed product
name whose ownership is undecided — see below) are three distinct concepts that must not be collapsed.

---

## Context

**Already accepted and reused, not reopened:**

- A **Reasoning Provider owns nothing** — not facts, not authority, not the reasoning of record; its
  output never silently becomes a Fact, and its recommendation never silently becomes an authorised
  action (glossary; restated in **DL-73**, **DL-82** (drafted, pending #188)).
- **DL-41** — a Reasoning provider is a declared capability dependency: absent a configured, valid,
  available provider, the dependent capability is **unavailable and names the missing dependency**, and
  **no local approximation stands in for it**.
- **DL-34** — a reasoning provider is never the sensitivity classifier; disclosure is evaluated against
  audience composition, never against requestor identity.
- **DL-33** — Unknown Person is a valid Identity Assertion outcome; an Unknown Person creates no
  profile, inherits nothing, and generates no person-scoped learning; what an Unknown Person may
  request is the household-neutral **unidentified-person policy**, owned by Operational Trust as a
  **policy subject**, never a profile.
- **DL-71** — a household may designate **exactly one** existing, deliberately configured Person
  (ordinarily a Known Non-Resident Person, commonly named "Guest") as the **Guest fallback Person
  Extension** consulted when Identity yields Unknown Person. Consulting that Person's own configured
  settings as interaction defaults **creates no Identity Assertion binding** Unknown Person to it —
  Unknown Person remains exactly what DL-33 states. Where no fallback is designated, DL-33's
  household-neutral treatment applies instead. The designated fallback Person Extension **may hold
  permissions if the household deliberately configures them** — none of that is prohibited by default.
- **DL-84** (accepted, #191) — Guest is **not a fourth identity class**: a Role, applied either to a
  configured Known Non-Resident Person or to the Unidentified-Person Policy Operational Trust applies
  when Identity yields Unknown Person. This ADR relies on this distinction and does not reopen it.
- **DL-39** — Operational Trust owns every threshold, including a **Required Identity Band**, wherever
  it is surfaced in configuration; Identity, Concierge, Communication, and Continuity own none. Bands
  are ordered and carry no access meaning by themselves; **no new band, likelihood score, or numeric
  threshold is created by this ADR.**
- **DL-56** — consent is required for person association and person-scoped participation; this is
  already **closed** (previously **OD-06**, the dependency named in Issue #132's own body).
- **DL-66** — native Home Assistant Assist exposure and HTBW Exposure are distinct; this ADR does not
  reopen that boundary.
- **DL-73** — Behaviour Source Attribution and Decision Authority Attribution are distinct; a
  reasoning-provider recommendation and an external autonomous policy engine are **Decision
  Authorities**, never Behaviour Sources.
- **DL-43** — no externally stored artifact exists without a documented lifecycle; a retained complete
  provider interaction would be a new artifact class requiring its own declaration before introduction.
- **DL-81, DL-82, DL-83** (drafted, pending #188) — each already restates "OD-67 unchanged" and
  consumes the Reasoning Provider concept by reference; none decides OD-67, and none is reopened or
  narrowed by this ADR. **DL-81 describes an architecture-only Household Knowledge Provider pipeline**
  — ingestion, retrieval, reasoning, and provenance for household documents/records; it does not name,
  define, or constitute a commercial product, and it does not mention "Home Steward." **Issue #188 is
  itself a governance-review record, not architecture authority, and is not an Open Decision** (#188's
  own authority note); it has no standing to assign ownership of a product-naming decision. **Any
  relationship between a prospective "Home Steward" product and DL-81's pipeline is undecided** — it
  may eventually be one consumed capability, an architectural service used by multiple products, or
  related some other governed way, once DL-81 itself is formally accepted and a separate product
  decision is made. This ADR asserts none of those relationships.
- **DL-86** (accepted, #191) — Home Intelligence is an optional deployment/hosting boundary that may
  host **both** DL-81's Household Knowledge Provider pipeline **and** a Reasoning Provider; it is a
  "where," not a "what," and is not itself a product name for either capability it may host.
- **home-assistant-boundary.md** — HTBW **selects or references** an already-configured native
  capability (a conversation agent, an Assist pipeline) rather than copying its credentials, endpoints,
  or model configuration; this ADR confirms this is the representation mechanism for a configured
  Reasoning provider, closing the table's own "OD-67 — not preempted here" / "OD-67 stays open" markers.

**What remains genuinely open after these facts:** which provider classes a household may configure,
for which purposes, at which configuration scopes, resolved through which precedence and fallback for
the effective Person, with which disclosure and Explainability obligations, and how General Reasoning
authorization is independent of a separate Home Steward authorization. This ADR decides those
architectural questions.

---

## Decision — permissible provider classes (DL-93)

HTBW permits all three household postures, and selects none of them:

1. A **local or self-hosted** Reasoning provider.
2. A **household-approved external/cloud** Reasoning provider.
3. **No Reasoning provider configured.**

**No provider class is mandatory.** A household may legitimately choose not to configure General
Reasoning; General Reasoning then becomes an **unavailable capability** under **DL-41**, named as such,
and every other HTBW capability continues operating. **Local residency is never automatically
trustworthy, and external/cloud residency is never automatically prohibited** — governance (purpose
bounds, data minimisation, disclosure, the no-Fact/no-authority invariants) applies identically
regardless of where a configured provider runs. Residency is a **material, disclosed configuration and
provenance attribute**, never a trust shortcut.

---

## Decision — Reasoning, Home Intelligence, and Home Steward

**Reasoning**, **Home Intelligence**, and **Home Steward** are three distinct concepts. Provider
*technology* does not define capability *ownership*: a local model such as Ollama is not inherently
Home Intelligence and is not inherently General Reasoning — which capability a configured technology
serves is a configuration fact, not a property of the technology.

- **General Reasoning** (this ADR, DL-93) may support: general knowledge questions; conversational
  wording and presentation; summarisation; natural-language interpretation; reasoning over context HTBW
  has explicitly authorised and supplied; and other explicitly declared Reasoning-dependent HTBW
  functions.
- **Home Intelligence** (accepted **DL-86**, #191) is a separate, optional product/deployment boundary
  — a "where," not a "what" — that **may host** a Household Knowledge Provider pipeline (drafted
  **DL-81**, pending **#188**) and **may host** a Reasoning Provider, without becoming either one
  itself.
- **Home Steward** is a tentative household-facing product name discussed during this ADR's owner
  review for a prospective, separate commercial product providing governed information about the
  household (documents, financial/banking information, Asset manuals, insurance, maintenance,
  administrative information). **This is a proposed product term, not an accepted or canonical product
  boundary. This ADR does not define, name, or own the Home Steward product**, and does not assert any
  relationship between it and the drafted Household Knowledge Provider pipeline (**DL-81**, itself
  non-binding, architecture-only, and pending #188). That pipeline may eventually be one capability
  Home Steward consumes, an architectural service multiple products use, or related some other governed
  way — **none of those relationships is decided here, and Home Steward is not stated to be equivalent
  to the Household Knowledge Provider.** No existing issue has been identified as owning the Home
  Steward product-naming/boundary decision; this ADR states only the authorization-independence pattern
  below and leaves that product governance question explicitly open.

**None implies another's availability.** If no applicable General Reasoning provider is configured,
general questions are unavailable **while** a separately configured and authorised Home Intelligence
capability — hosting a Household Knowledge Provider, a future Home Steward product, or something else —
may still answer an eligible home-based question. **Home Intelligence and Home Steward are never
inserted into the General Reasoning fallback chain, and General Reasoning is never used as an
undeclared substitute for either.** This ADR does not allocate Home Intelligence's own configuration
surface or discovery/trust-establishment mechanics (**#190**), and does not allocate Home Steward's
product architecture, deployment, or information-category authorization taxonomy; it states only that
the three capabilities, and their authorization paths, remain distinct.

---

## Decision — configuration model

General Reasoning is configured at exactly **two** scopes, and **establishes nothing about its own
availability beyond what each scope configures**. There is no Room scope for General Reasoning
authorization or provider assignment.

### Integration scope

Integration Configuration owns the available Reasoning-provider inventory and may designate one
configured provider as the **Integration-default Reasoning provider**. No provider, inventory entry, or
default is created by this capability outside of explicit configuration — **HTBW performs no runtime
discovery**: it does not scan the network for a model, discover a local provider at runtime, search
Home Assistant for an alternative conversation agent, select an unconfigured conversation agent, infer
that a reachable endpoint may perform Reasoning, substitute another configured provider outside the
governed resolution chain, or treat network reachability as configuration. If no Reasoning provider is
configured at Integration scope: General Reasoning is not an available capability, Person setup does
not offer a Person-level provider selection, and runtime attempts no discovery or manufacture of
Reasoning.

A configured Reasoning provider is represented the way **home-assistant-boundary.md** already requires
for *"referenced provider or integration configuration"*: HTBW **selects or references** the
already-configured native capability (a conversation agent, an Assist pipeline, or an equivalent
configured integration); it never copies credentials, endpoints, or model configuration, and it stores
only its own governance (purpose authorization, fallback role).

### Person scope

Person Configuration provides, for every Person, independently:

- **Allow General Questions: YES / NO** — General Reasoning authorization.
- **Allow Home Steward: YES / NO** — a top-level capability gate for the separately-governed Home
  Steward product (see *Home Steward authorization*, below). **These are independent settings, never
  one combined "Allow AI" setting**; a Person may legitimately hold any of the four combinations.
- An **optional Person-specific Reasoning provider**, drawn only from the Integration-configured
  inventory, selectable only when Allow General Questions is YES.

A Person-scoped provider is an explicit **override candidate**, never a requirement. **The
Person-to-provider association's own storage and lifecycle mechanics remain OD-77's (#148)** — this ADR
defines only the permissible use and resolution semantics of a configured association, never where or
how that association record is kept. **A Reasoning-provider selection is never duplicated as a
Continuity presentation preference**: the explicit Person Reasoning-provider assignment is canonical
for provider assignment, and Continuity's existing preferred-delivery/preferred-presentation preference
governs wording and delivery form, never which provider answers, and never either capability-
authorization gate.

### Room's retained, genuinely spatial responsibilities

A Room is never an authorization owner for General Reasoning or Home Steward, and never carries a
Reasoning-provider assignment. A Room continues to supply, as already accepted:

- the room-scoped interaction relationships already established for Foundation Room Interaction Roles
  (`voice_input`, `spoken_response_output`, `interface`, physical remote, and other accepted
  room-scoped capabilities);
- **interaction location** — where the request originated;
- **input/output surface selection** — which device captured the request and which device delivers the
  response;
- **authorized Room context** supplied to an authorized Reasoning invocation, where Operational Trust
  permits it, as ordinary context — never as an authorization signal of its own;
- any separately governed Room policy not owned by OD-67 (for example native Assist exposure, **DL-66**,
  unaffected and unreopened here).

**A Room providing interaction context and a delivery surface is not the same thing as a Room granting
or denying General Reasoning or Home Steward** — the two were collapsed in this ADR's original draft
and are separated here.

---

## Decision — the effective Person

Every General Reasoning (and Home Steward) authorization evaluation resolves to exactly one **effective
Person** before any capability gate is read:

1. **The resolved household Person**, when Identity and Operational Trust permit Person-scoped use
   (ordinary Identity resolution, unchanged — **DL-38**, **DL-39**).
2. Otherwise, **the household's designated Guest fallback Person Extension**, if the household has
   deliberately configured one (**DL-71**) — a real, named Person whose own configured settings are
   consulted as the interaction default. **This creates no Identity Assertion binding** Unknown Person
   to that Person; Identity's own result remains exactly `unknown`, in every record including the
   Decision Trace, unchanged from DL-33.
3. Otherwise (no household Person resolved, and no Guest fallback designated), **the DL-33
   unidentified-person policy** — a policy subject, not a Person — applies. Where no policy value is
   recorded for General Questions or Home Steward specifically, the setting is **unresolved
   configuration**, not a silent default; this ADR does not invent one.

**No second anonymous-person type, pseudo-person, room-person, or runtime-only profile is created.**
This ADR does not define a numeric identity-likelihood threshold: whether a household Person is
"sufficiently resolved" to serve as the effective Person is answered entirely by existing Identity/
Operational-Trust authority (**DL-39**'s Required Identity Band mechanism), never by a value this ADR
invents.

**There is no Room involvement in resolving the effective Person or in evaluating its capability
gates.** A Room may supply interaction context (where the request was made, which surfaces are
available) consumed *by* the effective-Person evaluation; it is never itself a party to that
evaluation.

---

## Decision — General Reasoning authorization

**Allow General Questions: YES / NO** is a Person-scoped (the effective Person's own) setting. **It is
not a blanket "AI allowed" setting** and does not govern deterministic Home control, Concierge
generally, Home Intelligence, Home Steward, Stewardship, Continuity, or any other capability that does
not itself declare a Reasoning dependency.

**Provider availability and provider selection do not grant authorization.** Authorization is evaluated
**before** provider resolution is attempted, against the effective Person's own setting:

- **NO is terminal.** General Reasoning is prohibited for the effective Person; resolution stops
  immediately; no Person-specific provider is tried; no Integration-default provider is tried; no
  provider is discovered; Home Steward is never substituted as a workaround; the result is reported as
  a **prohibition**, never described as provider unavailability.
- **YES authorizes** General Reasoning for the effective Person, and provider resolution may proceed.

---

## Decision — Home Steward authorization

**Allow Home Steward: YES / NO** is a second, independent Person-scoped (effective Person's own)
setting — **a top-level capability gate only**, established by Person Configuration alongside Allow
General Questions. The two settings are never combined into one "Allow AI" setting; a Person may
legitimately hold any of the four combinations (General Questions YES/Home Steward YES, YES/NO, NO/YES,
NO/NO). The Guest fallback Person Extension, where designated, carries the same two independent
settings as any other Person.

- **NO** prohibits the effective Person from invoking Home Steward. General Reasoning must never be
  used to bypass this prohibition, and Home Steward must never answer through another interaction path
  merely because a Reasoning provider happens to be available.
- **YES establishes capability eligibility only.** It is **not** universal access to all Home Steward
  information. Later, finer-grained authorization — for example distinguishing maintenance/manual
  information, Asset records, financial/banking information, insurance/legal information, and
  administrative household information — remains required for a specific request and remains **outside
  OD-67's scope**. This ADR preserves that seam; it does not design the taxonomy. **No existing issue
  has been confirmed as the owner of that finer-grained taxonomy** — it belongs to whatever future
  Home Steward product-governance decision is made, in combination with Operational Trust's existing
  disclosure-evaluation authority (**DL-34**); this ADR does not assign it to #188 or to draft DL-81,
  neither of which defines or accepts a Home Steward product.

**Reasoning and Home Steward are independent capabilities, evaluated independently.** A Person may be
denied General Reasoning but permitted Home Steward, or the reverse. An unavailable General Reasoning
provider does not make Home Steward unavailable, and an unavailable Home Steward product does not make
General Reasoning unavailable. Home Steward is never inserted into the General Reasoning fallback
chain; General Reasoning is never used as an undeclared substitute for Home Steward.

---

## Decision — provider resolution (configured fallback, never discovery)

**For an effective Person authorized for General Questions (YES):**

1. Try the **Person-specific** Reasoning provider, if one is configured and available.
2. If absent or unavailable, try the **Integration-default** Reasoning provider, if configured and
   available. *Absence of a Person-specific provider means inheritance from the Integration default,
   never denial.*
3. If absent or unavailable, General Reasoning is **unavailable**, and the missing dependency is named
   (**DL-41**). No Home Steward substitution. No approximation.

**There is no Room-configured provider and no Room fallback step.** Resolution is exactly Person →
Integration default → unavailable.

**Terminal authorization denial never enters the fallback chain.** A provider's own *unavailability*
(not configured, configured but invalid, or configured but currently unreachable) may advance resolution
to the next configured scope; an *authorization denial* never does — the two outcomes are evaluated
independently and are never collapsed, consistent with **DL-41**'s existing "capability unavailable is a
dependency outcome, never a trust failure... or permission failure" rule applied to this specific
dependency. **No provider outside this configured chain is ever selected; there is no runtime
discovery.**

The **Integration-default Reasoning provider** has two governed roles: (1) fallback for an effective
Person who is authorized for General Questions but has no available Person-specific provider; (2) the
default provider for any other explicitly provider-dependent HTBW function that declares Reasoning as a
capability dependency, is permitted under this decision, has authorized context to supply, and has
Operational Trust permission to disclose that context. **The existence of an Integration-default
provider grants no blanket authority to use it, no access to household information, and no
authorization for an effective Person whose own setting is NO.** This ADR establishes the
default-provider principle and its governance boundary; it does not enumerate speculative future HTBW
functions that may declare this dependency.

---

## Decision — permitted and prohibited purposes

**Reasoning may reason. Reasoning may never govern.**

Permitted purposes: general knowledge questions; wording and conversational presentation;
summarisation; natural-language interpretation; reasoning over context HTBW has explicitly authorized
and supplied; and other explicitly declared Reasoning-dependent HTBW functions not enumerated here.

A Reasoning provider must **never**:

- become a Fact source merely because it produced an answer, or have its output become an HTBW Fact
  without the already-governed promotion/acceptance path;
- classify privacy or sensitivity (restates **DL-34** unchanged);
- grant access or permission, authorize an action, or determine an Operational Trust outcome;
- silently create a Person preference, a Room policy, or a household policy;
- fabricate a device, entity, service, capability, Person, Asset, or Home condition;
- become the system of record, become Home Intelligence or Home Steward, replace deterministic
  Home-control logic, or serve as the reasoning of record;
- answer a Home Steward-eligible request as a workaround when the effective Person's Allow Home Steward
  setting is NO, or when Home Steward itself is unavailable.

A provider recommendation is **governed input**. It is never automatically an authorized action —
restating, for this specific input class, the already-accepted rule that a recommendation is never
silently promoted to an authorized outcome.

---

## Decision — factual-integrity profile (response quality, not Fact promotion)

Every General Reasoning invocation applies a standing factual-integrity profile requiring the provider
to: prioritise factual accuracy; prefer authoritative and reputable sources where sources are available;
distinguish established information from inference, opinion, or uncertainty; acknowledge insufficient
evidence; avoid manufacturing certainty or presenting unsupported claims as established fact; and
identify meaningful source limitations where the provider itself can do so.

**This is a response-quality requirement, not a Truth-ownership change.** A factual-looking provider
answer remains provider output unless and until a separately governed process legitimately promotes
appropriate information into HTBW Truth or another governed record (**DL-46**, **P28**). An ordinary
General Reasoning answer does not need to become an HTBW Fact merely to be spoken. **Where a maintained
integration already supplies an attribute as source metadata, a Reasoning provider must not be used to
infer a replacement merely for convenience** — restating **DL-30**'s ordered burden of proof for this
specific case (a maintained integration, DL-30 step two, outranks a new Reasoning-provider inference,
DL-30 step four, where the integration already satisfies the requirement).

---

## Decision — data minimization, consent, and disclosure

Configuring a Reasoning provider **does not grant blanket access** to household information. For each
invocation, HTBW may supply only: the minimum context needed for the authorized task; context
Operational Trust permits for the effective Person, provider, and purpose; and explicitly governed
supporting material (which may include authorized Room context, supplied as ordinary content, never as
an authorization signal). Provider configuration does **not** automatically authorize access to Person
profiles, calendars, email, Decision Traces, Home Intelligence, Home Steward, household-private
context, Asset records, Home history, current occupancy, or other sensitive information. **Operational
Trust determines disclosure scope. The Reasoning provider never determines its own disclosure scope** —
restating **DL-34** for this specific input class.

**Configuration-time disclosure** must clearly state, where applicable: local/self-hosted versus
external/cloud residency; that authorized context may leave the Home for an external provider; the
purposes for which the provider may be used; the configured fallback role; and the effect of not
configuring a provider. **Routine per-interaction responses do not require repeated spoken provider
disclosure merely because a provider was used** — consistent with Concierge's existing restraint against
announcing merely because an action was permitted. Per-interaction disclosure remains governed by
existing privacy, consent, change-in-context, and Operational Trust rules; this ADR does not weaken or
duplicate them.

---

## Decision — Explainability and provenance

**No new record class is created.** The existing Decision Trace structure (`decision-trace.md`) already
records policies evaluated, restrictions applied, action taken, and result; Reasoning-specific
provenance is ordinary content within that existing structure, not a new artifact:

- the **effective Person** used, and whether it was a resolved household Person or the Guest fallback
  Person Extension;
- the **capability requested** — General Reasoning or Home Steward;
- the **capability-authorization result**, and, where denied, that it was a **prohibition**, distinct
  from provider/product unavailability;
- provider identity/reference, and whether it was Person-specific or Integration-default scope;
- whether fallback occurred, and why;
- the purpose the provider served, and the authorized context class supplied;
- provider residency (local/self-hosted or external/cloud), where governed and relevant;
- which provider or product was responsible for a given response, for later "where did that answer come
  from?" queries, answered from recorded provenance, never reconstructed.

Where an explanation cites a Reasoning-provider suggestion as evidence, the source-class discipline
already drafted at **DL-82** (pending #188) — never presenting a provider suggestion as household fact —
applies without this ADR depending on DL-82's own acceptance; the underlying "never silently becomes a
Fact" invariant is already accepted independently (glossary; **DL-73**).

**A complete prompt or complete provider response is not retained by default.** If a complete provider
interaction is ever retained, it requires its own accepted **DL-43** artifact declaration — type, owning
responsibility, retention, deletion trigger, consent effect, Preservation Hold effect — before
introduction, exactly as any other artifact class. Ordinary Explainability provenance (the bullets
above) is not itself the complete interaction and does not require this declaration.

---

## Decision analysis

The issue's original options, evaluated against accepted architecture and the above:

| Option | Disposition |
|---|---|
| **A. Local-only providers permitted** | **Rejected as the sole posture.** Mandating local-only would make local residency a trust shortcut this ADR explicitly rejects, and would exclude households without capable local hardware from a capability nothing requires to be local |
| **B. Any provider class, household-declared, mandatory disclosure** | **Adopted as the governing shape**, bounded by purpose (below) rather than left open-ended |
| **C. Purpose-scoped — presentation only, never interpretation** | **Adopted as a bounding principle, not as the sole permitted purpose set** — "Reasoning may reason, may not govern" bounds *authority*, while permitted purposes include more than presentation (summarisation, natural-language interpretation, authorized-context reasoning), consistent with already-accepted uses this issue's own evidence (Issue #132 comments) shows already exist in practice |
| **D. No Reasoning provider at all** | **Adopted as a fully legitimate posture, never a constitutional mandate** — a household may choose this; HTBW does not choose it for every household |

**Recommendation, stated once, not as an undecided options paper:** a governed version of **Option B**
— any of the three permitted provider classes (local/self-hosted, household-approved cloud, none),
household-declared at Integration scope with mandatory configuration-time disclosure — **bounded by
Option C's purpose discipline** (Reasoning may reason, may never govern) **and explicitly including
Option D's no-provider posture as first-class**, never a degraded fallback state. Option A is rejected
as a universal mandate; nothing here prevents a household from choosing local-only for itself.
Authorization is resolved against the effective Person, never a Room, per this remediation.

---

## Architectural boundaries preserved, not absorbed

| Decision/issue | What it retains |
|---|---|
| **OD-77** (#148) | Person-to-provider association **storage and lifecycle mechanics** |
| **OD-07** (#95) | Voice processing locality — a different provider class; the "prefer local-first AI" setting is OD-07's own privacy-boundary question, not a Continuity preference |
| **OD-65** (#130) | Learning eligibility — whether a provider-inferred value may enter the promotion ladder |
| **OD-66** (#131) | Delegation boundary for an external **autonomous policy engine that decides** — a different thing from a Reasoning provider that is consulted and never decides |
| **OD-04** (#97) | Wider Operational Trust policy precedence; effective-Person authorization gating here reuses, not reopens, OD-04's ordering |
| **#185** | MCP transport-preference research — a transport question, not a provider-classification question |
| **Home Intelligence** (accepted **DL-86**, #191) | Its own configuration, authorization, deployment, and discovery/trust-establishment mechanics (**#190**) |
| **Home Steward** (proposed product term, ownership unassigned) | Its own product definition, naming adoption, deployment, and finer-grained information-category authorization taxonomy — **not owned by #188 or draft DL-81**, neither of which names or defines it; this ADR states only that it is independent of General Reasoning |
| **Truth** | Facts — never provider output without the governed promotion path |
| **Concierge** | Orchestrates provider use as a consulted component; never becomes Truth or authorization authority |
| **Continuity** | Preferred delivery/presentation wording; never a competing Reasoning-provider or Home Steward preference |
| **Room Configuration** | Interaction location, input/output surface selection, authorized Room context supply, and its own already-accepted room-scoped interaction relationships — **never** General Reasoning or Home Steward authorization, and never a provider assignment |

**No Provider, Reasoning, or Home Steward responsibility is created.** No vendor, model, provider
abstraction, API, or transport is selected or designed by this ADR.

---

## Explicit non-goals

- Does not select a vendor, model, or provider technology.
- Does not design the provider abstraction, API, or transport (including MCP — **#185**).
- Does not decide Person-to-provider association storage/lifecycle (**OD-77**, #148).
- Does not decide voice-processing locality (**OD-07**, #95).
- Does not decide learning-evidence eligibility (**OD-65**, #130).
- Does not decide the external autonomous-policy-engine delegation boundary (**OD-66**, #131).
- Does not decide wider Operational Trust policy precedence (**OD-04**, #97).
- Does not accept, decide, or redefine Home Intelligence's own architecture (accepted **DL-86**, #191).
- Does not define, name, or own the Home Steward product, its deployment, its finer-grained
  information-category authorization taxonomy, or its relationship (if any) to the drafted Household
  Knowledge Provider (**DL-81**, pending #188). **Does not assign Home Steward product ownership to
  #188 or to draft DL-81**; #188 is a governance-review record, not architecture authority, and DL-81
  does not name, define, or constitute Home Steward.
- Does not make Room Configuration an authorization owner for General Reasoning or Home Steward, and
  does not create a Room-level provider assignment.
- Does not invent a numeric identity-likelihood threshold for the effective-Person determination.
- Does not promote any provider response to an HTBW Fact or authorized action.
- Does not create a new artifact/record class for Explainability provenance.
- Does not reopen **DL-30**, **DL-33**, **DL-34**, **DL-39**, **DL-41**, **DL-43**, **DL-46**, **DL-56**,
  **DL-66**, **DL-71**, **DL-73**, or **DL-84**.
- **Accepted 2026-10-27 (Issue #132, formal acceptance review PASS). DL-93 is a closed, binding
  decision, equivalent in standing to DL-01–DL-92.**

---

## Test and acceptance scenarios

See the companion acceptance-scenario record in the Issue #132 execution comments for the full
General Reasoning/effective-Person scenario set (Scenarios 1–18 from the prior remediation, unchanged
by this correction, plus preserved scenarios on factual-integrity, minimum-context, provider-
recommendation-is-not-authority, sensitivity-classification prohibition, and DL-43 artifact retention).

**Home Steward seam scenarios, revised to test only the authorization seam this ADR may legitimately
establish — not Home Steward's product architecture:**

- **Scenario A — General Reasoning allowed, Home Steward denied.** General Reasoning proceeds; Home
  Steward use is prohibited; General Reasoning cannot bypass the prohibition.
- **Scenario B — General Reasoning denied, Home Steward allowed.** General Reasoning is prohibited;
  Home Steward may proceed only if separately configured and available; Home Steward remains subject
  to finer-grained authorization.
- **Scenario C — Home Steward top-level YES, sensitive category denied.** Top-level eligibility does
  not grant the sensitive category; access remains denied; General Reasoning cannot bypass the
  restriction.
- **Scenario D — Home Steward product not configured.** Allow Home Steward YES does not manufacture
  the product; the capability reports unavailable; nothing is discovered dynamically; General
  Reasoning does not substitute.
- **Scenario E — Draft Household Knowledge Provider (DL-81) later rejected at #188.** DL-93's General
  Reasoning architecture remains fully coherent; the Home Steward seam remains proposed and
  non-implementing; no binding dependency on draft DL-81 ever existed.
- **Scenario F — Draft Household Knowledge Provider (DL-81) later accepted at #188.** Acceptance alone
  does not automatically make that pipeline "Home Steward," and does not automatically make #188 or
  DL-81 the Home Steward product's owner; a separate, future product-governance decision determines
  whether and how Home Steward consumes it.
- **Scenario G — Same underlying technology.** Use of the same model/runtime for more than one
  capability never merges General Reasoning, Home Intelligence, Home Steward, or the Household
  Knowledge Provider into one capability.
- **Scenario H — Ask the source of a response.** Explainability distinguishes the General Reasoning
  provider, a Home Intelligence-hosted capability, a Home Steward response, and a Household Knowledge
  Provider pipeline where applicable; no concept is substituted for another.

All scenarios are satisfied by the decision above without inventing additional architecture; none
requires a new record class, a new responsibility, a provider selection, or a decision about Home
Steward's product boundary.

---

## Related documents

- [../models/glossary.md](../models/glossary.md) — Reasoning Provider, General Reasoning, Home
  Intelligence, Home Steward, Delegated Adaptive Behaviour
- [../models/operational-trust.md](../models/operational-trust.md) — General Reasoning/Home Steward
  authorization; Required Identity Band ownership
- [../models/continuity.md](../models/continuity.md) — person-scoped preference boundary
- [../models/person-and-identity.md](../models/person-and-identity.md) — Guest fallback Person
  Extension (**DL-71**), Unknown Person (**DL-33**)
- [../models/room-configuration.md](../models/room-configuration.md) — Room's retained spatial
  responsibilities
- [../models/decision-trace.md](../models/decision-trace.md) — Explainability structure
- [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md) — referenced
  provider/integration configuration representation
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
- [../governance/open-decision-issue-index.md](../governance/open-decision-issue-index.md)
