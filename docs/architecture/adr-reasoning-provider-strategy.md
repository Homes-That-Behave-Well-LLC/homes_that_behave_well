# ADR: Reasoning Provider Strategy

> **Document status: Active — subordinate to the HTBW canonical architecture.**
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Drafts decision **DL-93**, recorded pending formal acceptance review at **Issue #132**.
> **Not yet authoritative. Creates no new responsibility.**
> Terminology: [../models/glossary.md](../models/glossary.md).

---

## Status

**Recorded, pending formal acceptance review (Issue #132). Not yet authoritative.**

Resolves **OD-67**: which classes of Reasoning provider HTBW may use, for which purposes, under which
governance. No provider, vendor, model, or technology stack is selected here, and no provider
abstraction, API, or transport is designed here, consistent with the issue's own standing rule and with
**DL-30**.

This ADR creates **no new responsibility**. The seven responsibilities recorded in **DL-01** are
unchanged. The **Reasoning Provider owns nothing** — this restates, and does not relax, the glossary's
existing definition.

**This ADR distinguishes Reasoning from Home Intelligence.** Home Intelligence's own governance
(**DL-86**) is recorded pending formal acceptance review at **Issue #191** and is not yet authoritative.
This ADR does not accept, decide, or redefine **DL-86** or any Home Intelligence boundary. It confirms
only that General Reasoning and Home Intelligence are separate capabilities and configuration surfaces
— a separation the glossary's drafted Home Intelligence entry already assumes (a deployment that "may
host... a Reasoning Provider," never *is* one) — and that confirmation holds regardless of **DL-86**'s
own eventual acceptance outcome, because it rests on the already-accepted Reasoning Provider definition
alone.

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
  request is the household-neutral **unidentified-person policy**, owned by Operational Trust.
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
  narrowed by this ADR.
- **home-assistant-boundary.md** — HTBW **selects or references** an already-configured native
  capability (a conversation agent, an Assist pipeline) rather than copying its credentials, endpoints,
  or model configuration; this ADR confirms this is the representation mechanism for a configured
  Reasoning provider, closing the table's own "OD-67 — not preempted here" / "OD-67 stays open" markers.

**What remains genuinely open after these facts:** which provider classes a household may configure,
for which purposes, at which configuration scopes, resolved through which precedence and fallback, with
which disclosure and Explainability obligations. This ADR decides those architectural questions.

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

## Decision — Reasoning versus Home Intelligence

**Reasoning** and **Home Intelligence** are separate capabilities and separate configuration/
authorization surfaces. Provider *technology* does not define capability *ownership*: a local model
such as Ollama is not inherently Home Intelligence and is not inherently General Reasoning: which
capability a configured technology serves is a configuration fact, not a property of the technology.

- **General Reasoning** may support: general knowledge questions; conversational wording and
  presentation; summarisation; natural-language interpretation; reasoning over context HTBW has
  explicitly authorised and supplied; and other explicitly declared Reasoning-dependent HTBW functions.
- **Home Intelligence** is a separate, optional product/deployment boundary (drafted **DL-86**, pending
  **#191**) concerned with governed Home and household knowledge, which **may host** a Household
  Knowledge Provider pipeline (drafted **DL-81**, pending **#188**) and **may host** a Reasoning
  Provider, without becoming a Reasoning Provider itself.

**Neither implies the other's availability.** If no applicable General Reasoning provider is
configured, general questions are unavailable **while** a separately configured and authorised Home
Intelligence capability may still answer an eligible home-based question. **Home Intelligence is never
inserted into the General Reasoning fallback chain, and General Reasoning is never used as an
undeclared substitute for Home Intelligence.** This ADR does not allocate Home Intelligence's own
architecture, configuration surface, or discovery/trust-establishment mechanics (**#190**); it states
only that the two capabilities, and their authorization paths, remain distinct, and that this
distinction holds whether or not **DL-86**/**#191** is ultimately accepted in its current drafted form.

---

## Decision — configuration model

General Reasoning is configured at exactly three scopes, and **establishes nothing about its own
availability beyond what each scope configures**:

### Integration scope

Integration Configuration owns the available Reasoning-provider inventory and may designate one
configured provider as the **Integration-default Reasoning provider**. No provider, inventory entry, or
default is created by this capability outside of explicit configuration — **HTBW performs no runtime
discovery**: it does not scan the network for a model, discover a local provider at runtime, search
Home Assistant for an alternative conversation agent, select an unconfigured conversation agent, infer
that a reachable endpoint may perform Reasoning, substitute another configured provider outside the
governed resolution chain, or treat network reachability as configuration. If no Reasoning provider is
configured at Integration scope: General Reasoning is not an available capability, Room setup does not
offer Reasoning enablement or provider selection, Person setup does not offer a Person-level provider
selection, and runtime attempts no discovery or manufacture of Reasoning.

A configured Reasoning provider is represented the way **home-assistant-boundary.md** already requires
for *"referenced provider or integration configuration"*: HTBW **selects or references** the
already-configured native capability (a conversation agent, an Assist pipeline, or an equivalent
configured integration); it never copies credentials, endpoints, or model configuration, and it stores
only its own governance (scope, purpose authorization, fallback role).

### Room scope

Room Configuration may, as an instance of the already-accepted "what can I do here?" capability-exposure
question (`room-configuration.md`, *Room Help and capability exposure*):

- allow or prohibit **General Questions** for that Room;
- select a Room-scoped Reasoning provider, drawn only from the Integration-configured inventory.

Room Configuration does not invent a new participation state, vocabulary mechanism, or exposure rule to
carry this: **Allow General Questions** is a Room-scoped authorization setting, owned by Operational
Trust under **DL-39** wherever it is surfaced in configuration, and Room Configuration exposes it the
same way it exposes any other capability setting.

### Person scope

Person Configuration may, within accepted Person boundaries:

- allow or prohibit **General Questions** for that Person;
- select a Person-scoped Reasoning provider, drawn only from the Integration-configured inventory, when
  General Questions are allowed for that Person.

A Person-scoped provider is an explicit **override candidate**, never a requirement. **The
Person-to-provider association's own storage and lifecycle mechanics remain OD-77's (#148)** — this ADR
defines only the permissible use and resolution semantics of a configured association, never where or
how that association record is kept. **A Reasoning-provider selection is never duplicated as a
Continuity presentation preference**: the explicit Person Reasoning-provider assignment is canonical
for provider assignment, and Continuity's existing preferred-delivery/preferred-presentation preference
governs wording and delivery form, never which provider answers.

---

## Decision — authorization precedes provider resolution

**Allow General Questions** (Room-scoped, Person-scoped) is a specific authorization for General
Reasoning. **It is not a blanket "AI allowed" setting** and does not govern deterministic Home control,
Concierge generally, Home Intelligence, Stewardship, Continuity, or any other capability that does not
itself declare a Reasoning dependency.

**Provider availability and provider selection do not grant authorization.** Authorization is evaluated
**before** provider resolution is attempted, and a denied authorization never reaches provider
resolution at all.

### Recognized Person

When a Person is resolved with a **Required Identity Band sufficient for the General Reasoning
authorization purpose** (an Operational-Trust-owned threshold under **DL-39**, not a value this ADR
sets):

- The Person's **Allow General Questions** setting is authoritative.
- **NO is terminal.** General Reasoning is prohibited for that Person; resolution stops immediately; the
  Person provider, Room provider, and Integration-default provider are none of them tried. This holds
  **even where the Room's own Allow General Questions is YES** — Person denial is never overridden by
  Room permission.
- **YES authorizes** General Reasoning for that Person, and provider resolution may proceed, **even
  where the Room's own Allow General Questions is NO** — a recognized, authorized Person's own setting
  prevails over the Room's.

This ADR does not define what "sufficient" means as a band value or a confidence mechanic; it
references the existing Identity/Operational-Trust threshold ownership (**DL-39**) exactly as every
other Operational-Trust-owned threshold is referenced.

### Unresolved or Unknown Person

When no Person is resolved with sufficient confidence for this purpose: Person authorization is **not
evaluated**, no Person-scoped provider is used, and **Room authorization governs**:

- If Room Allow General Questions = **NO**: General Reasoning is prohibited in that Room for the
  unresolved/Unknown speaker; resolution stops immediately; the Integration-default provider is **not**
  tried.
- If Room Allow General Questions = **YES**: General Reasoning is authorized at Room scope, and provider
  resolution proceeds through the Room and Integration-default providers.

An Unknown or unresolved speaker's access remains bounded by the already-accepted household-neutral
context default (**DL-33**) and ordinary Operational Trust disclosure rules regardless of provider
availability: **provider availability never authorizes household-private context.**

---

## Decision — provider resolution (configured fallback, never discovery)

**For a recognized, authorized Person:**

1. Try the **Person-configured** Reasoning provider, if one exists.
2. If absent or unavailable, try the **Room-configured** Reasoning provider, if one exists. *Absence of
   a Person provider means inheritance to the next configured scope, never denial.*
3. If absent or unavailable, try the **Integration-default** Reasoning provider, if configured.
4. If absent or unavailable, General Reasoning is **unavailable**, and the missing dependency is named
   (**DL-41**).

**For an unresolved/Unknown speaker in a Room that authorizes General Questions:**

1. Try the **Room-configured** Reasoning provider, if one exists.
2. If absent or unavailable, try the **Integration-default** Reasoning provider, if configured.
3. If absent or unavailable, General Reasoning is **unavailable**, and the missing dependency is named.

**Terminal authorization denial never enters the fallback chain.** A provider's own *unavailability*
(not configured, configured but invalid, or configured but currently unreachable) may advance resolution
to the next configured scope; an *authorization denial* never does — the two outcomes are evaluated
independently and are never collapsed, consistent with **DL-41**'s existing "capability unavailable is a
dependency outcome, never a trust failure... or permission failure" rule applied to this specific
dependency. **No provider outside this configured chain is ever selected.**

The **Integration-default Reasoning provider** is not merely a conversational fallback: it is the
default Reasoning capability available to any explicitly provider-dependent HTBW function that declares
Reasoning as a capability dependency, is permitted under this decision, has authorized context to
supply, and has no more specific applicable configured provider. This ADR establishes the
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
- become the system of record, become Home Intelligence, replace deterministic Home-control logic, or
  serve as the reasoning of record.

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
Operational Trust permits for that request, Person, Room, provider, and purpose; and explicitly governed
supporting material. Provider configuration does **not** automatically authorize access to Person
profiles, calendars, email, Decision Traces, Home Intelligence, household-private context, Asset
records, Home history, current occupancy, or other sensitive information. **Operational Trust determines
disclosure scope. The Reasoning provider never determines its own disclosure scope** — restating
**DL-34** for this specific input class.

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

- provider identity/reference, and whether it was Person-, Room-, or Integration-default scope;
- whether fallback occurred, and why;
- whether the invocation was General Reasoning or Home Intelligence;
- the purpose the provider served, and the authorized context class supplied;
- provider residency (local/self-hosted or external/cloud), where governed and relevant;
- the authorization outcome and, where denial occurred, that it was denial rather than unavailability.

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

---

## Architectural boundaries preserved, not absorbed

| Decision/issue | What it retains |
|---|---|
| **OD-77** (#148) | Person-to-provider association **storage and lifecycle mechanics** |
| **OD-07** (#95) | Voice processing locality — a different provider class; the "prefer local-first AI" setting is OD-07's own privacy-boundary question, not a Continuity preference |
| **OD-65** (#130) | Learning eligibility — whether a provider-inferred value may enter the promotion ladder |
| **OD-66** (#131) | Delegation boundary for an external **autonomous policy engine that decides** — a different thing from a Reasoning provider that is consulted and never decides |
| **OD-04** (#97) | Wider Operational Trust policy precedence; person/Room authorization gating here reuses, not reopens, OD-04's ordering |
| **#185** | MCP transport-preference research — a transport question, not a provider-classification question |
| **Home Intelligence** (**DL-86**, pending #191) | Its own configuration, authorization, deployment, and discovery/trust-establishment mechanics (**#190**) |
| **Truth** | Facts — never provider output without the governed promotion path |
| **Concierge** | Orchestrates provider use as a consulted component; never becomes Truth or authorization authority |
| **Continuity** | Preferred delivery/presentation wording; never a competing Reasoning-provider preference |

**No Provider or Reasoning responsibility is created.** No vendor, model, provider abstraction, API, or
transport is selected or designed by this ADR.

---

## Explicit non-goals

- Does not select a vendor, model, or provider technology.
- Does not design the provider abstraction, API, or transport (including MCP — **#185**).
- Does not decide Person-to-provider association storage/lifecycle (**OD-77**, #148).
- Does not decide voice-processing locality (**OD-07**, #95).
- Does not decide learning-evidence eligibility (**OD-65**, #130).
- Does not decide the external autonomous-policy-engine delegation boundary (**OD-66**, #131).
- Does not decide wider Operational Trust policy precedence (**OD-04**, #97).
- Does not accept, decide, or redefine Home Intelligence's own architecture (**DL-86**, pending #191).
- Does not promote any provider response to an HTBW Fact or authorized action.
- Does not create a new artifact/record class for Explainability provenance.
- Does not reopen **DL-30**, **DL-33**, **DL-34**, **DL-39**, **DL-41**, **DL-43**, **DL-46**, **DL-56**,
  **DL-66**, or **DL-73**.
- **This entry is drafted content, not yet a closed decision; it must not be cited as equivalent to
  DL-01–DL-92 until #132's formal acceptance review records a result.**

---

## Test and acceptance scenarios

See the companion acceptance-scenario record in the Issue #132 execution comment for the full
scenario-by-scenario evaluation (Scenarios 1–22). All scenarios are satisfied by the decision above
without inventing additional architecture; none requires a new record class, a new responsibility, or a
provider selection.

---

## Related documents

- [../models/glossary.md](../models/glossary.md) — Reasoning Provider, Home Intelligence, Delegated
  Adaptive Behaviour
- [../models/operational-trust.md](../models/operational-trust.md) — General questions and reasoning
  providers; Required Identity Band ownership
- [../models/continuity.md](../models/continuity.md) — person-scoped preference boundary
- [../models/room-configuration.md](../models/room-configuration.md) — Room Help and capability exposure
- [../models/decision-trace.md](../models/decision-trace.md) — Explainability structure
- [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md) — referenced
  provider/integration configuration representation
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
- [../governance/open-decision-issue-index.md](../governance/open-decision-issue-index.md)
