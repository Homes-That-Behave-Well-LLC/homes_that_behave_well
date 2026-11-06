# Operational Trust Model

> **Document status: Canonical model.**
> Terminology: [glossary.md](glossary.md). Owning responsibility: **Operational Trust**.
> Contract: [../contracts/operational-trust-contract.md](../contracts/operational-trust-contract.md)

---

## Purpose

Operational Trust is the responsibility for **what is allowed**.

It is distinct from **Human Trust**, which is the outcome the household experiences when the home
behaves predictably and explains itself. Human Trust is not a layer and cannot be implemented
directly. See [../architecture/explainability.md](../architecture/explainability.md).

## Question answered

*What is allowed — by whom, where, when, and under what conditions?*

Stated in the form the household hears:

> **Operational Trust determines what is appropriate for this request, in this context.**

### The canonical verb

**The qualifier is not decoration.** *For this request, in this context* is what keeps the sentence
true, and the statement must never be shortened to *"Operational Trust determines what is
appropriate."* unqualified.

| Wording | Status | Why |
|---|---|---|
| **Operational Trust determines what is appropriate for this request, in this context** | **Canonical** | The determination is about a **request**, bounded by a **context**, against requirements the household authored |
| The household defines what *appropriate* means | **Canonical** | The complementary half. Neither sentence is complete without the other |
| Operational Trust **evaluates** | **Compatible** | Used throughout this model for the act of weighing the eight inputs. It is a description of the mechanism, not a substitute for the responsibility statement |
| Operational Trust **applies** household values | **Canonical** | Stated below — it applies them; it does not author them |
| Operational Trust **enforces** what is appropriate | **Rejected** | **Enforcement is execution.** Operational Trust produces a **governed decision**; Concierge decides what should happen now; an **executor** performs it. This wording appears nowhere in this repository and must not be introduced |
| Operational Trust **determines what is appropriate** (unqualified) | **Rejected** | Read alone it suggests Operational Trust authors household values. It does not |

### What Operational Trust evaluates before producing an outcome

| Input | Supplied by |
|---|---|
| **Identity confidence** — the current, purpose-specific assertion and its band | Identity |
| **Audience awareness** — who can perceive the outcome, and the residual uncertainty in that | Truth and Identity, composed under **DL-34** |
| **Context** — Room, Merged Room, mode, time, occupancy, current activity | Truth and Room Configuration |
| **Consent** — whether the required consent exists, is in scope, and is current | Foundation holds the record; Identity owns the lifecycle |
| **Privacy markings and classifications** — explicit sensitivity carried by the content itself | The source of the content, or household configuration |
| **Disclosure requirements** — what may be conveyed, on which surface, to this audience | This model |
| **Household policy** — the values the household has configured | The household |
| **Capability requirements** — the Required Identity Band and Required Confirmation Strength of what is being protected | This model, per capability and per operation |

**No single input decides an outcome.** A high confidence band does not authorise; an unknown audience
does not automatically refuse; a satisfied capability requirement does not license disclosure.
Operational Trust weighs all eight and produces **one** outcome, with its reason and policy reference.

### Sufficiency, not trustworthiness

> **Operational Trust does not evaluate whether a person is trustworthy.**

It evaluates whether the **available confidence is sufficient** for a **specific** requested capability
or action, in the **current** context. The subject of the judgement is the **request**, never the
person.

| Operational Trust asks | Operational Trust never asks |
|---|---|
| Is this confidence sufficient for **this capability**? | Is this person trustworthy? |
| Is it sufficient for **this operation** on it — read, write, delete, govern? | Does the home like or approve of this person? |
| Is it sufficient **here, now, with these people present**? | Has this person earned a general standing? |
| Is confirmation available, and does this operation require it? | Should confidence be raised so the request can proceed? |

**The same person, at the same confidence, may be sufficient for one request and insufficient for the
next in the same breath.** That is not inconsistency; it is the requirement belonging to **what is
being protected**, never to the person (**DL-36**).

### Operational Trust applies household values; it does not author them

> **The framework provides governance. The household provides the values.**

| The household decides | Operational Trust does |
|---|---|
| Participation expectations — who takes part, and through which evidence | Applies them, and excludes what is not permitted |
| Disclosure expectations — what may be said, and in front of whom | Applies them per request, per surface, per audience |
| Privacy expectations — what is sensitive in this home | Applies them, and refuses where they are not met |
| Confidence requirements — how sure the home must be, per capability | Applies them, and **never lowers a requirement to reach a result** |
| Operational preferences — autonomy ceilings, quiet hours, modes | Applies them under the ceiling rule |

Operational Trust supplies the **structure** in which those choices are expressed, the **consistency**
with which they are applied, and the **explanation** of what was applied and why. **It does not decide
what the household ought to value**, and it never substitutes its own judgement for a household
decision it finds inconvenient.

> **Consistency is the product.** A household that configures a value once should see it applied the
> same way in every Room, on every surface, for every requester — and should be able to ask why.

---

## Owns

- Authority
- Permission
- Restrictions
- Guest access
- **Unidentified-person policy** — what an Unknown Person may request, control, or receive
- Child safety
- Quiet hours
- Nighttime restrictions
- Room-level authority
- Person-level authority
- Autonomy level
- Confirmation requirements
- **Identity-confidence sufficiency** — how much confidence a given presentation, capability, resource, or operation requires
- **Identity Presentation Threshold** — when the home may speak as though a candidate identity is likely
- **Confirmation strength, scope, and lifetime** — which confirmation method an operation requires, and what a successful confirmation covers
- Consent boundaries
- Safety-critical restrictions
- Escalation permissions
- Suppression policy
- Interruption policy
- Privacy visibility policy
- Policy provenance and precedence
- **Home Production (HA-Prod) trust-boundary admission** — whether a specific, Foundation-referenced resource (service, App instance, execution host, or storage connection) is an admitted HA-Prod member, and the policy consequences of that membership (**DL-119**)
- **Communication Urgency entitlement** — what a Communication is entitled to interrupt
- **Audience eligibility** — who may receive a Communication, and who may hear it
- **Communication visibility classification**, re-evaluated at each Delivery Attempt
- **Disclosure appropriateness** — whether content may be conveyed through a proposed surface in the current audience context
- **Communication retention classification**, with content and metadata classified separately

---

## Consumes

- Identity assertions (who is believed to be asking)
- Truth facts (what is actually true now — room mode, time, occupancy, device state)
- Foundation Person roles, Room definitions, and Relationships
- Stewardship significance — a **Significance Declaration** (**DL-75**), consumed as one input to risk
  classification and confirmation requirements; **never itself the risk class or the confirmation
  requirement**, and never converted to or from Identity Confidence (**DL-39**) or Truth Confidence
  (**DL-58**)
- Household-configured policy

**Operational Trust does not determine who a person is.** It consumes an identity assertion, applies
a confidence threshold appropriate to the action class, and decides what that assertion is sufficient
to authorize.

---

## Provides

- Authority decisions: permitted, prohibited, permitted with confirmation, permitted with escalation
- Required autonomy level for a given action in a given context
- Confirmation and consent requirements
- Suppression and interruption rules
- Visibility rules for privacy-governed content
- The reason and policy reference behind every decision

---

## "Not now" is a valid outcome

> **Knowing the answer does not always mean the home should provide it.**

An Operational Trust outcome is not binary. **Refusal is not the only alternative to compliance**, and
a home whose only two behaviours are *do it* and *no* will be experienced as either careless or
obstructive.

Six outcome shapes are what the household actually experiences. **Each is produced by existing
constructs — no new enumeration is introduced, and no ownership moves.**

| Household-facing shape | Meaning | Produced by |
|---|---|---|
| **Allow** | Proceed at the effective autonomy level | Authority outcome `permitted` |
| **Require Confirmation** | Proceed only after a governed confirmation of the required strength | Authority outcome `permitted_with_confirmation` (**DL-37**, **DL-40**) |
| **Defer** | Permitted, but **not at this moment** — the timing, mode, or interruption policy governs | Operational Trust supplies the **suppression or interruption constraint**; Concierge expresses it as its **Defer** outcome |
| **Redirect** | Permitted, but **not on this surface** — a more appropriate audience or surface exists | The disclosure outcome *access allowed, private delivery available*; Concierge selects the surface |
| **Abstain** | The decision **cannot be made safely** — a required input is unknown, or audience composition is unresolved | Authority outcome `undecidable`, or the disclosure outcome *identity or audience insufficient*, degrading under **OD-71** |
| **Deny** | The action must not proceed | Authority outcome `prohibited` |

> **Read the ownership column carefully. Operational Trust owns the *constraint*; Concierge owns the
> *expression* of it.** Operational Trust says *not at this moment* and *not on this surface*;
> Concierge decides to defer, to redirect, to ask, or to say nothing, and records the Decision Trace.
> **This table names outcomes the household perceives. It does not relocate a decision, and it does
> not replace the authoritative enumerations** in
> [../contracts/operational-trust-contract.md](../contracts/operational-trust-contract.md) and
> [../contracts/concierge-contract.md](../contracts/concierge-contract.md).

Three rules bind all six:

- **Every shape is traced.** *Defer*, *Redirect*, and *Abstain* are **Intentional Non-Actions** under
  **P16** and **DL-15**, and each produces a Decision Trace stating what was withheld and why.
- **A degraded outcome is correct behaviour, not a failure.** *"I will tell you when we are alone"* is
  a governed result, not an apology, and **the delivery degrades — the governance does not** (**P32**).
- **No shape is a silent one.** A home that decided to stay quiet and cannot say so is in exactly the
  condition **P27** was written to prevent.

---

## Consent ownership

Consent is touched by three responsibilities. Ownership is divided as follows and must not be
re-litigated elsewhere.

| Aspect | Owner | Meaning |
|---|---|---|
| **Consent record** | Foundation | The durable record attached to the Person: what was consented to, by whom, when, and its provenance |
| **Consent lifecycle** | Identity | Capture, scope, reaffirmation, and revocation of consent for identity evidence and enrollment. **Consent does not silently expire** (**DL-56**); an "expiry" is only a household- or legal-policy-mandated boundary stated explicitly, never a default |
| **Consent policy and enforcement** | **Operational Trust** | Which actions require consent, what consent is sufficient, and refusal when consent is missing or withdrawn |

Operational Trust does not capture consent and does not store the record. It decides what consent is
required and refuses when it is absent. **Missing consent is never implied consent.** The scope model,
canonical record, self/proxy distinction, withdrawal semantics, and state distinctions (**consent not
given** / **declined** / **withdrawn** / **permission denied** / **dependency missing** / **unknown**)
are accepted as **DL-56** — see
[../models/person-and-identity.md](../models/person-and-identity.md#consent-dl-56).

### Participation is optional, and participation requires consent

> **No person is required to participate in any identity-evidence source, and a person who declines
> loses no ability to live in the home.**

| Participation class | Requires consent | Effect of declining |
|---|---|---|
| **Voice identity evidence** | **Yes** — available only for a consenting, enrolled participant | No voice-derived candidate is nominated for that person. Their voice is not matched, and their absence from the candidate set is **neutral, never a penalty** |
| **Wearable evidence** | **Yes** | The wearable family contributes nothing for that person |
| **Device or phone evidence** | **Yes** | The device family contributes nothing for that person |
| **Preference participation** — person-scoped preferences, history, and learning | **Yes** | The home behaves household-neutrally for that person |

Four rules follow, and none of them is configurable:

- **Declining is not a fault, a degraded mode, or a defect.** It produces fewer eligible evidence
  families, which under **F7** yields a **lower ceiling — never a penalty and never a denominator
  effect**. *Missing evidence is not contradicting evidence.*
- **A person who has not consented must still be able to use the home in a guest-safe way**, as
  [../architecture/privacy.md](../architecture/privacy.md) already requires.
- **Enrollment is an explicit act, never a silent by-product of ordinary use**, and consent is scoped:
  *consenting to voice identity is not consent to calendar access.*
- **Revocation is available at any time**, and removes the derived profile and its associations — not
  merely their use.

### Consent governs the evidence that exists at all

The relationship is a **chain**, and each link is owned by a different responsibility:

```text
CONSENT             what the household and the person have permitted
    ↓
AVAILABLE EVIDENCE  the eligible evidence set — what may be used at all
    ↓
IDENTITY            fusion over that set, producing a purpose-specific assertion
    ↓
OPERATIONAL TRUST   sufficiency, audience, disclosure, and the outcome
```

| Link | Owner | Rule |
|---|---|---|
| Consent → Available Evidence | Consent record **Foundation**; lifecycle **Identity**; policy and enforcement **Operational Trust** | Evidence lacking valid consent is **excluded before weighting, never down-weighted** (**DL-38**, eligibility gate) |
| Available Evidence → Identity | **Identity** | Identity fuses only what is eligible. **No other responsibility fuses** |
| Identity → Operational Trust | **Operational Trust** | Confidence is consumed, never recomputed. **A reference is not permission to re-run fusion** |

> **Consent determines what evidence may be used. Operational Trust ensures those choices are applied
> consistently and respectfully.**

Two consequences are worth stating plainly, because both are easy to get wrong:

- **A withdrawn consent is not a reduced weight.** The evidence leaves the eligible set entirely, and
  the assertion is produced as though the source did not exist.
- **Consistency is owed in both directions.** A household that permitted a source must see it used;
  a person who declined one must never find it used *"just this once"* because the outcome would have
  been convenient.

The consent user experience is open decision **OD-06**. See
[../architecture/privacy.md](../architecture/privacy.md).

---

## The autonomy model

| Level | Meaning |
|---|---|
| **Explicit** | Act only on direct instruction |
| **Assisted** | Propose, then act on confirmation |
| **Autonomous** | Act without asking, within policy |

### The ceiling rule

> **The most restrictive applicable policy sets the ceiling.**

If the Home permits Autonomous behavior, the Room permits Assisted behavior, and the Person's policy
permits Autonomous behavior, then the effective level is **Assisted**. Restriction always wins over
permission.

The ceiling rule applies across every scope: Home, Room, Person, Asset, Relationship,
Experience class, and Action-risk class.

---

## Scope and precedence

| Scope | Examples |
|---|---|
| Home | Quiet hours, away mode, global autonomy ceiling |
| Room (including Merged Room, behaving identically — **DL-13**) | Nighttime restrictions, child-safe rooms, no-media rooms |
| Person | Child safety, guest limitation, caretaker elevation |
| Asset | Safety-critical devices, irreplaceable assets |
| Relationship | Caretaker-of, owner-of elevation |
| Experience class | Media may be suppressed while care escalations are not |
| Action-risk class | Locks, garage doors, and heat sources require higher confidence |
| External Decision Authority (delegation, **DL-118**) | A declared external policy engine; Type-2 (unmediated) action is capped at Convenience/Disclosure regardless of any other scope's permission |

**Floor adds no scope here (resolved — DL-125).** A native Home Assistant Floor is referenced for
targeting only; it is never a policy-authorship unit, and a Floor-targeted action's fan-out is
evaluated at each entity's own already-accepted scope (ordinarily Room) independently.

**Mode, capability, and operation are applicability/condition dimensions, never scopes (resolved —
DL-126).** Mode is a governed Room- or Home-scoped Truth fact that *selects* which Room/Home policy
applies (`../scenarios/nighttime-suppression.md` Scenario 1); a capability declares the Action-Risk
Class that governs it; Operation Type (Read/Write/Delete/Govern, **DL-36**/**DL-76**) is the
independent axis selecting which threshold within a Risk Class applies. None of the three is added to
the scope table above. **Person is dual in kind, never dual in precedence**: a Person-scoped statement
is either a Policy (ceiling-relevant, authored under Operational Trust) or a Preference
(candidate-value-relevant only, authored under Continuity) — **a Person preference never becomes a
ceiling and never becomes permission**.

**Most-restrictive combination across scopes is precise (resolved — DL-126).** Each applicable scope
yields one of the five accepted outcomes below. (i) Any applicable `prohibited` makes the final outcome
`prohibited`. (ii) Absent (i), any applicable `undecidable` makes the final outcome `undecidable` —
never rendered as `permitted`. (iii) Absent (i) and (ii), every applicable
`permitted_with_confirmation` and `permitted_with_escalation` requirement combines cumulatively — each
is independently discharged, and satisfying one never substitutes for another. (iv) Only if every
applicable scope yields `permitted` does the final outcome become `permitted`, at the most restrictive
applicable autonomy level. A narrower scope's `permitted` never cancels a broader or otherwise-
applicable scope's more restrictive outcome.

Precedence within a scope, same-scope conflict resolution, and the competing-Communication ordering
algorithm are recorded in
[../architecture/behavioral-governance.md](../architecture/behavioral-governance.md) and
[../models/communication.md](../models/communication.md), **resolved as DL-126 (OD-04)**.

**Threshold resolution introduces no new precedence order.** A presentation threshold, a capability
requirement, and a confirmation requirement are ordinary policy statements evaluated in the scopes
above, under the ceiling rule. A constitutional prohibition is never overridden by any of them; a
narrower scope may restrict but never silently relax a governing ceiling; and whether a Person may
relax a household setting is itself a policy. **A Person preference is never a permission.** **Resolved
as DL-126.**

---

## Identity confidence and action risk

Authority requirements scale with consequence.

| Action risk | Example | Identity requirement |
|---|---|---|
| Benign | Turn on a lamp in an occupied room | May proceed with unknown identity, per policy |
| Personal | Play *my* playlist | Requires a resolved identity |
| Sensitive | Read a calendar or message | Requires a resolved identity above threshold |
| Safety-critical | Unlock a door, open a garage, control a heat source | Requires a high-confidence identity and may require confirmation regardless |

**This table is illustrative only.** The canonical, constitutional enumeration is **Action-Risk Class
(DL-76)**, below.

## Action-Risk Classes (DL-76)

Resolves **OD-51**. Risk Classification answers **"what happens if this is wrong?"** — a consequence
question, never an operation-type question (below).

### The six constitutional Action-Risk Classes

| Risk Class | Consequence if wrong |
|---|---|
| **Convenience** | Minor, easily reversed — a lamp left on, a volume misset |
| **Disclosure** | Information is revealed that should not have been |
| **Financial** | Money is spent, committed, or put at risk |
| **Safety** | A person or pet's physical wellbeing is put at risk |
| **Security** | Physical or digital access is granted that should not have been |
| **Governance** | A governance record, policy, identity, or evidentiary record is altered or destroyed |

### Operation Type is a separate concern (DL-36, unchanged)

**Risk Class and Operation Type (Read, Write, Delete, Govern) are independent axes.** No matrix is
required. Write+Convenience, Write+Security, and Delete+Governance may all exist simultaneously for
different protected operations. Risk Classification answers *"what happens if this is wrong?"*;
Operation Type answers *"what kind of action is occurring?"*.

### Default Required Identity Band (discharges the DL-39 deferral)

| Risk Class | Required Identity Band |
|---|---|
| Convenience | `None` |
| Disclosure | Moderate |
| Financial | High |
| Safety | High |
| Security | High |
| Governance | Very High |

### Default Required Confirmation Strength (discharges the DL-40 deferral)

| Risk Class | Required Confirmation Strength |
|---|---|
| Convenience | `None` |
| Disclosure | Verbal |
| Financial | Authenticated |
| Safety | Authenticated |
| Security | Authenticated |
| Governance | Strong |

**These are required-strength defaults, not a claim that a verified mechanism exists to satisfy
them.** Issue #146 item 10 established **`VERIFIED_NOT_SUPPORTED`, stable**, for every
companion-application, push, PIN, or secondary-factor confirmation mechanism reviewed to date. **DL-40
governs this exactly as DL-40 already requires**: where a required class has no verified available
mechanism, the outcome is `Unavailable`, and the operation is refused or degraded under normal policy
— **never a silent downgrade to a weaker class**. Setting a Governance default of Strong does not
assert a Strong mechanism exists.

### Default Address by Name and Identity Presentation Threshold (a second DL-39 deferral)

Two distinct, independently configurable settings, never collapsed into one:

| Risk Class | Address by Name | Identity Presentation Threshold |
|---|---|---|
| Convenience | Low | `None` |
| Disclosure | Moderate | Moderate |
| Financial | High | High |
| Safety | High | High |
| Security | High | High |
| Governance | Very High | Very High |

**Address by Name** governs specifically whether a Person's name may be spoken, since speaking a name
is itself a disclosure (**DL-36**). The **Identity Presentation Threshold** governs the broader
question of whether the home may behave as though a candidate identity is likely (a greeting, a
person-scoped suggestion). Address by Name is the setting through which the Identity Presentation
Threshold is most commonly expressed, but the two remain separately configurable.

### Default configuration model

Every value above is **HTBW Default Configuration, never HTBW Fixed Configuration**. Operational Trust
owns the Risk Class enumeration, every default above, and every threshold. Households may override
defaults through governed configuration.

### Override model

| Tier | Owns |
|---|---|
| **Capability Default** | The capability or protected operation declares its Risk Class |
| **HTBW Default** | Operational Trust's default Required Identity Band and Confirmation Strength for that class |
| **Household Override** | Governed configuration raising or lowering the applied requirement |

A household raising **Unlock Exterior Door** from Security's default (High + Authenticated) to Very
High + Strong is a valid override.

### Object-specific overrides

**Explicitly supported, restating DL-36** — *the requirement belongs to what is being protected* —
not a new mechanism. Two objects sharing one capability may carry different requirements:

| Object | Risk Class | Required Identity Band | Required Confirmation Strength |
|---|---|---|---|
| Safe Lock | Security | Very High | Strong |
| Closet Lock | Security | Moderate | Verbal |

Both use the same lock capability. The requirement is governed configuration on the **protected
object**, never on the capability itself.

### Configuration Authority Composition (DL-109)

Resolves **OD-92** in full. **No general cross-responsibility configuration-authority tier model
exists.** A request to change a configuration record — adding a Room participant, changing Exposure,
setting a Room Authority rule, adjusting a Person preference — is itself an ordinary protected
operation, evaluated exactly like any other, through this model's own Action-Risk Classification
above. **"What permission does this configuration change require?" already has a complete, dynamic
answer, varying per requested mutation, not per configuration item as a whole.**

**DL-11's "Authority" state is a different concept from configuration-change authority, and the two
must never be conflated.** `room-configuration.md`'s Authority state governs whether a person or
process may *use* an already-exposed capability. Whether a person may *edit the configuration itself*
— who participates, what is exposed, what Authority rule applies — is a separate, governed action,
evaluated by Operational Trust through this section, never through a second meaning of "Authority."
Changing a Room Configuration Authority rule is itself typically a **Governance**-class mutation
("a governance record, policy, identity, or evidentiary record is altered"), already fully gated by
the table above.

**A previously proposed four-tier model (household-configurable; household-configurable-with-consent;
administrator/integrator-configurable; governed/high-consequence) is rejected as an independent
authority mechanism:**

| Proposed tier | Disposition |
|---|---|
| household-configurable | Redundant — already Convenience/Disclosure Risk Class with `None`/Low default |
| household-configurable-with-consent | Conflates **DL-56** consent (genuinely engaged only where the mutation is itself a Person-association change — binding a device, voiceprint, or authenticated session, or person-scoped learning) with ordinary **DL-40** Confirmation Strength (every other elevated-confirmation case). The two are never presented under one label |
| administrator/integrator-configurable | Depends on an "Integrator" authority role that does not exist anywhere in canonical architecture. "Administrator" exists only as the native, authenticated Home Assistant administrator flag already reused by **DL-37**, **DL-40**, and **DL-79**, conferring no care, guardianship, or proxy authority beyond that (**DL-57**). Where a household wants a more capable or trusted configuration role, the already-accepted mechanism is **DL-71**'s Role/Authority Class — a household-configured Role, the same "owner/administrator-equivalent Role" pattern **DL-97** already reuses — never a newly invented construct |
| governed/high-consequence | Redundant — already the existing **Governance** (or, depending on the specific mutation, **Safety**/**Security**) Risk Class |

**A non-binding, resident-facing composed descriptor vocabulary is permitted, never required.** A
surface may render explanatory labels ("you can change this directly," "this needs additional
confirmation," "this is a governed change") **entirely derived, at render time, from each item's own
already-governed facts** — Action-Risk Class, Operation Type, genuine DL-56 consent-dependency where
one exists, and Required Confirmation Strength. **The descriptor is never cached or stored as an
independent authoritative field**, and can never override Operational Trust's actual evaluation; where
the two disagree, the label was wrong and must be corrected, never the reverse. This creates no second
authorization engine.

**Configuration ownership and change authority are distinct.** Foundation, Room Configuration, and
Continuity own the shape and scope of the configuration records they each already own; Operational
Trust alone decides, per mutation, whether a requested change may proceed — exactly as it decides for
any other protected operation.

### The Required Identity Band


Every protected capability and protected operation carries a **Required Identity Band**. It is an
Operational Trust configuration value, and it takes exactly one of five values:

| Requirement value | Meaning |
|---|---|
| **`None`** | **No known-Person identity is required for this operation** |
| **Low** | A `known` assertion at **Low** or higher, for the required assertion purpose |
| **Moderate** | A `known` assertion at **Moderate** or higher |
| **High** | A `known` assertion at **High** or higher |
| **Very High** | A `known` assertion at **Very High** |

> **`None` is a Trust requirement, not an Identity output.** Identity produces four bands. Operational
> Trust chooses among five requirement values, one of which is *"identity is not the gate here"*.

**`None` is not the bottom of the band scale, and nothing is *"above"* it.** When a requirement is
`None` and Identity independently reports `known`, candidate Tom, **High**, the honest account is:

> Known-Person identity was not required for this operation.

**Never** *"High exceeded `None`, therefore the action was authorised."* Representing it that way
manufactures an identity dependency the policy does not have, and would make the action wrongly
appear to fail when identity is weak.

An Unknown Person does **not** satisfy `Low`. `Low` requires a `known` assertion; the
unidentified-person policy governs whether an Unknown Person may proceed by another route
(**DL-33**).

### A missing dependency is not a Trust decision

> **Operational Trust answers *may this happen?* It never answers *can this happen at all?***

Where a capability's declared dependency is missing — no integration, no provider, no Connected
Storage, no consent, no required configuration — the capability is **unavailable**, and Operational
Trust **evaluates nothing**. There is no requirement to meet, no threshold to compare, and no
confirmation to offer.

The boundary runs both ways:

- **A dependency failure is never expressed as a refusal, a denial, or an unmet requirement.** Telling
  a household it lacks permission when it lacks an integration is a defect.
- **A satisfied requirement never supplies a missing dependency.** No band, confirmation, or authority
  level causes a capability to exist.

Dependency, identity, and permission are three independent questions, evaluated in that order. See
[../architecture/failure-and-degradation.md](../architecture/failure-and-degradation.md).

**No responsibility becomes the owner of a dependency by observing it.** Truth may establish current
Facts about a dependency's health where that is accepted, and Repairs may surface a configuration or
availability defect to the household, **without either becoming the owner of the capability or of its
dependency declaration**. Concierge orchestrates and explains; it **does not own dependency truth**,
and it may not proceed on an unavailable capability by choosing a different path that carries the same
name. Connected Storage is an **architectural boundary**, not a responsibility, and its presence or
absence confers no authority.

### One Identity result, independent consumers

The same current Identity Assertion is read by several Operational Trust evaluations **independently**.
Each applies its own requirement, and **each may reach a different outcome from the same assertion**.

Worked example — *"Turn on the lamps"*:

| Evaluation | Requirement | Current assertion | Outcome |
|---|---|---|---|
| Lamp control | Required Identity Band `None` | `known`, Tom, **High** | Proceeds. **Identity was not consulted as a gate** |
| Address by Name | Required current band **High** | `known`, Tom, **High** | Naming permitted, subject to disclosure |

Concierge may therefore answer *"Tom, I have turned on the lamps."* Had the current band been
**Moderate**,
**the lamps would still have been turned on** and the answer would have been *"I have turned on the
lamps."* — neutral, not refused.

> **A presentation threshold that is not met never denies an action.** Collapsing the two is a defect.

### Threshold configuration scopes

A Required Identity Band, a presentation threshold, and a confirmation requirement are ordinary
policy statements, resolved under the **existing** scope precedence and ceiling rule above. **No new
precedence model is introduced.** They may be stated at household or general-setting scope, Room,
capability, protected resource, protected operation, Person-owned external resource, or current mode.

> **The configuration surface never changes ownership.**

A setting exposed in Room Configuration is still owned by Operational Trust if it determines
permission or identity sufficiency. A setting exposed in Person configuration does not become
Identity's merely because it names a Person. A setting exposed in a Concierge screen does not become
Concierge's merely because Concierge renders the result. **Identity never owns a threshold;
Concierge, Communication, and Continuity never own one.**

Defaults per capability and per Action-Risk Class are **configuration**, resolved with **DL-76**'s
enumeration and defaults, above. They are not constitutional beyond the enumeration itself, and
household and object-specific overrides are always available.

### Identity supplies confidence; Operational Trust decides sufficiency

> **Identity does not decide whether its own confidence is enough.**

Identity produces a **purpose-specific** confidence result and stops there (**DL-32**). Whether that
result is sufficient depends entirely on what is being asked for, and **there is no universal
threshold**. The requirement may vary by presentation behaviour, requested capability, protected
resource, requested operation, consequence class, content sensitivity, disclosure surface, audience
composition, household mode, current Room, applicable policy, and whether confirmation is available
at all.

Concierge may **apply** an accepted presentation policy when choosing its wording. **It never sets or
overrides a threshold** — and neither does Communication, Continuity, Identity, or any reasoning
provider.

### Four consumers of one confidence result

One Identity Assertion is consumed by four **materially distinct** evaluations. Each answers a
different question, each may be satisfied while another is not, and **none implies another**.

| Consumer | The question | Owner | Applied by |
|---|---|---|---|
| **Identity Presentation Threshold** | May the home behave conversationally as though this candidate is likely? | Operational Trust | Concierge |
| **Capability Access Threshold** | Is this assertion sufficient for this capability, resource, and operation? | Operational Trust | Operational Trust |
| **Disclosure evaluation** | May the resulting content be conveyed on this surface, to this audience? | Operational Trust | Operational Trust |
| **Confirmation** | May a governed confirmation substitute for missing confidence — or is confirmation required despite it? | Operational Trust | Concierge orchestrates the exchange |

**Meeting one threshold never satisfies another.** Being addressed by name grants no access; access
grants no disclosure; and disclosure permitted to one audience grants nothing for the next.

### The Identity Presentation Threshold

The Presentation Threshold governs whether the home may **speak as though** a candidate identity is
likely enough for low-consequence conversational treatment: addressing a Person by name, a
personalised greeting, a preferred form of address, a person-scoped suggestion, resuming
conversational continuity, or a non-sensitive conversational style.

**Operational Trust owns it** — not because Concierge renders the language, but because **speaking a
name is itself a disclosure.** It tells everyone who can hear that the home believes a particular
Person is present, and it carries the same audience consequences as any other utterance (**DL-34**,
**P32**).

| Presentation does imply | Presentation must never imply |
|---|---|
| The home believes a candidate is likely, for the stated purpose | Access granted, or permission granted |
| A configured low-consequence threshold was met | Identity confirmed, or mathematically certain |
| — | Physical presence established for some other purpose |
| — | Disclosure authorised, or a permanent authenticated session |

Below the threshold, **neutral presentation is the correct behaviour, not an apology**: *"Good
morning"* rather than *"Good morning, Tom"*. Where policy permits, a candidate may be named
**tentatively** — *"I think I am speaking with Tom"* — but a tentative naming is still a naming and is
evaluated as one.

Where the assertion is `ambiguous`, **no candidate is presented.** Silently presenting the leading
candidate is prohibited here exactly as it is for an authority-bearing action.

**An Unknown Person can never meet a named-Person presentation threshold**, because there is no name
to present (**DL-33**). Neutral presentation is the only available treatment.

Whether the threshold is household-wide, mode-specific, Room-specific, or relaxable by a Person — and
its default — is **configuration**, resolved under the existing scope precedence rather than a new
one. Every presentation choice, **including a neutral one**, is explainable through the Decision
Trace.

### Address by Name

**Address by Name** is the general HTBW presentation setting through which the Identity Presentation
Threshold is expressed for the most common case: whether the home may speak a Person's name.

| Element | Requirement |
|---|---|
| Enabled or disabled | A household may switch naming off entirely |
| **Required current Identity band** | The minimum band the **current applicable** assertion must reach |
| Neutral fallback | When the threshold is not met, the home speaks neutrally. **This is correct behaviour, not a failure** |
| Audience-aware evaluation | Speaking a name is a disclosure and is evaluated against audience composition before it is spoken (**DL-34**) |
| Current-interaction evaluation | Evaluated at response time, from the current assertion. **A prior interaction's eligibility is never reused** |

With Address by Name enabled at **High**: a current speaker assertion of Tom at **High** permits the
name where disclosure policy allows; the same assertion at **Moderate** produces neutral wording.
**Disabled means disabled** — **Very High** does not override it, because high confidence is not a
permission.

Address by Name grants **nothing else**: no capability access, no personalization, no person-scoped
learning, no private information, no session resumption, no attribution of a consequential action, no
disclosure beyond the name itself, and no confirmation.

**Operational Trust owns the setting. Concierge applies the permitted wording.**

### Presentation is evaluated at response time

> **A presentation decision is made from the assertion that is current when the response is
> generated.**

An earlier response's naming eligibility is never carried forward. If Tom is named in one interaction,
then leaves while the Room stays occupied and David speaks, the next response is evaluated from
David's interaction: a new current-speaker assertion, a new band, a new presentation decision.

**The home must not say *"Tom, I have turned on the lamps"* unless current evidence independently
supports Tom at the configured threshold.** Continuous occupancy supplies no such support.
See [person-and-identity.md](person-and-identity.md).

### Presentation is not personalization

> **Being addressed as Tom does not make the home act as Tom.**

| Aspect | Presentation | Personalization |
|---|---|---|
| What it is | How the home addresses the participant | Use of person-scoped preferences, history, continuity, or learned behaviour |
| Typical requirement | Lower | Higher |
| Owner of the rule | Operational Trust | Operational Trust, over preferences owned by Continuity |

Addressing a candidate by name does **not** authorise applying that Person's preferences, resuming
their session, reading their resources, attributing a consequential action to them, learning from the
interaction as them (**P26**, **OD-65**), or disclosing anything of theirs. **Personalization is a
person-scoped capability access, not a presentation**, and is evaluated as one. See
[continuity.md](continuity.md).

### The Capability Access Threshold

The Capability Access Threshold is the minimum identity confidence, or confirmation state, required
before a capability, resource, or operation may be exercised.

> **The requirement belongs to what is being protected — never to the person, never to the evidence
> source, and never to Identity.**

It attaches to the **Authority** state of the existing Existence → Participation → Exposure →
Authority chain (see [room-configuration.md](room-configuration.md)). **No new access-control object
is introduced.** A requirement may be stated against a capability, a protected resource, a protected
operation, or an action-risk class, and is resolved under the ceiling rule like any other policy.

A requirement may need to express: the capability or protected resource and its owner; the requested
operation; the **required assertion purpose**; the minimum acceptable confidence band; whether
confirmation may substitute for missing confidence; the required confirmation strength; audience
sensitivity and whether private delivery exists; whether an Unknown Person or a known non-resident
Person is eligible; the consequence class; the applicable Room, mode, or scope; the policy owner;
default and override provenance; the historical version; and the explanation owed on refusal. **These
are policy attributes carried by reference inside existing Operational Trust policy**, not a new
universal access-control record.

**Read, write, delete, and governance operations are never collapsed into one threshold.** One
resource may require one level to view a public manual, another to view an appraisal, another to
record a service visit, and confirmation to change ownership or release preserved evidence. A
calendar may distinguish availability, event subjects, full detail, creation, modification, deletion,
and sharing. Email may distinguish an unread count, sender and subject, full content, sending,
replying, deleting, and forwarding. **Operation-specific requirements must not force duplicate
resource definitions.**

*No identity required* is a legitimate requirement and is **not** an absence of governance. It is
expressed as the **Required Identity Band `None`** above. It means identity is not the gate; Room
participation, capability exposure, current mode, the unidentified-person policy, consent, and every
other applicable policy still apply. **"Anyone may
play music" never means "anyone may change the media account, its credentials, or household media
policy."**

### Confidence requirements are configured per capability

> **The framework provides no universal confidence threshold, and none may be invented.**

A requirement belongs to **what is being protected** and is configured by the **household**.
Operational Trust supplies the structure and applies the result; it does not author the value.

| Capability | Illustrative shape of the requirement |
|---|---|
| **Greeting a person by name** | A presentation threshold. Where it is not met, the home speaks **neutrally** — and **never refuses the underlying action** |
| **Applying person-scoped preferences** | A personalization requirement, evaluated as **person-scoped capability access** — higher than presentation, and never implied by it |
| **Alarm or security control** | A capability access requirement, plausibly with a **Required Confirmation Strength** above `Verbal`, regardless of band |
| **Calendar disclosure** | An access requirement for the resource, a **separate** requirement per operation (availability, subject, full detail, create, modify, delete, share), and a **separate** disclosure evaluation against the audience |
| **Email disclosure** | The same three-way separation — unread count, sender and subject, and full content are **different** protected operations |

Four rules bind this table:

- **The values are illustrative, not defaults.** No number, band, or strength is prescribed here.
  The canonical Risk-Class enumeration and defaults are **DL-76**, above.
- **Households define the requirements; Operational Trust applies them.** A household that wants
  greetings at a low bar and calendars at a high one is expressing a value, not misconfiguring.
- **Requirements are never lowered to reach a result.** Where confidence falls short, the governed
  responses are confirmation where policy offers it, a degraded outcome, or refusal — **never a
  relaxed threshold.**
- **Satisfying one capability's requirement satisfies no other.** The four consumers above are
  evaluated independently, every time.

Action-Risk Class enumeration and defaults are **DL-76**. The confidence and confirmation strength
each class requires is **configuration** expressed through the Required Identity Band and the
confirmation requirement, resolved with that enumeration.

### Every evaluation uses the current assertion

> **Operational Trust evaluates the interaction in front of it, not the one before it.**

A requirement is applied against a **current, purpose-appropriate** Identity Assertion. Operational
Trust never revives a prior assertion because the Room stayed occupied, because a Person was here a
moment ago, or because the same request was permitted last time.

| Never sufficient on its own | Because |
|---|---|
| Continuous Room occupancy | Occupancy is a Room fact. Occupants change while it stays true |
| A prior speaker attribution | The speaker may have changed |
| A prior granted access | Permission was granted for that request, at that moment |
| A prior successful confirmation | Confirmation is consumed by its operation |
| An assertion that remains a permanently valid historical record (**DL-64**) | Validity is not current-interaction applicability |

**Continuous presence is not continuous authentication.** Any debouncing or stabilisation of a noisy
sensor belongs inside evidence freshness and Fusion Policy under **DL-38** — it is an
observation-quality mechanism and must never become an identity-session, authorisation, confirmation,
or presentation lifetime. **Sensor stabilisation is not authorisation persistence.**

### Person-scoped connected resources

A person-scoped external resource — a mailbox, a calendar, a personal message source — is a
**protected resource referenced by its Person anchor**, under **DL-31** and **OD-01**: the native
Home Assistant Person remains the anchor, HTBW holds only a governed extension reference, and
credentials and provider configuration are **not copied** where another integration owns them.

> **Resource ownership is never inferred from a connection's name.** A connection labelled with a
> Person's name does not establish that the Person owns it, nor that the requestor is that Person.

Operational Trust defines who may invoke which operation against the resource, at what confidence,
under what confirmation. **Disclosure of the result is evaluated separately.** No provider operation
and no provider's technical behaviour is specified or assumed here.

### Interrupting is a governed action, on its own axis

**Interruption is not a Risk Class. Risk and Interruption are formally separate, independent axes**
(**DL-76**, correcting this section's prior provisional text, which treated interruption as an
action-risk class while **OD-51** remained open). **DL-76 owns Action Risk; DL-77 owns
Interruption Classification.** A Medication Reminder may carry low Action Risk and high Interruption;
an Unlock Door Request may carry high Action Risk and low Interruption — both remain representable,
and neither axis is derived from the other. Operational Trust consumes both independently when
governing whether, and how, a Communication may interrupt.

> **A category must never function as a bypass.** A safety or critical classification is an
> Operational-Trust-granted **entitlement** — revocable, explainable, and traced. It is never a right
> that an originator confers upon itself by naming its own category.

Action-Risk Class enumeration and defaults are **DL-76**. Urgency Entitlement is **DL-77**, below.

## Delegation Boundary (DL-118)

Resolves **OD-66**. Governs how HTBW knowingly permits, bounds, observes, attributes, discloses, and
explains **Delegated Adaptive Behaviour** — behaviour decided by an **external autonomous policy
engine** rather than HTBW (`glossary.md`). An external policy engine is a **Decision Authority**, never
a Behaviour Source (**DL-73**); this decision supplies the one piece DL-73 deliberately deferred: how
such a Decision Authority is **declared**.

### Executor versus delegate, restated

**Where the decision is made, never implementation topology, is the discriminator.** An integration
executing a decision HTBW already made is an **executor** under an ordinary HTBW Decision Trace
(unaffected; also distinct from **OD-80**/**DL-50**'s Capability Execution Host, which decides
nothing at all). An engine that decides on its own, within a declared boundary, is a **delegate**
under this decision.

### Declaration is explicit, never inferred

**HTBW treats behaviour as authorized Delegated Adaptive Behaviour only following an explicit
household declaration** — never detected, never inferred from timing or pattern (restating, not
reopening, the existing "timing alone never establishes attribution" and "never silently learned"
rules, **DL-73**, **P26**). Absent a declaration, an observed external-sourced action is recorded
exactly as any other occurrence — a Domain Event carrying whatever Source/Decision-Authority
attribution the evidence actually supports (**DL-73**) — and is never promoted to "authorized" merely
because it was observed.

### The Delegation Boundary is a new scope within the existing autonomy model, not a new policy type

**Delegation reuses the existing ceiling-rule autonomy model** (above) by adding **External Decision
Authority** as a recognised scope, alongside Home, Room, Person, Asset, Relationship, Experience
class, and Action-risk class — the most restrictive applicable policy still sets the ceiling. **No new
policy construct is created.** The declaration itself carries: the external engine's own stable
reference (Foundation-typed, structurally analogous to the existing `located-in`/`owner-of`/
External-Resource Association reference pattern — Foundation identifies *which* external system this
is; it never owns the authorization); the bounded scope (capability, target/Room, temporal limits);
the applicable Action-Risk Class ceiling; effective and revocation time; and provenance. **Foundation
owns the reference; Operational Trust owns the bounded entitlement; the external engine owns only its
own reasoning and whatever it is independently, externally authoritative for** — never any HTBW
responsibility, capability, policy, identity, authorization, Truth, or Stewardship content.

### Mediated (Type 1) versus unmediated (Type 2) action

**Type 1 — mediated.** The delegate requests an effect through an HTBW-governed capability surface.
The identical Operational Trust evaluation applies as to any other requester, **with no caller-origin
exception** (restating **DL-114**'s existing "the contract already makes no caller-origin distinction"
rule) — a declared delegation never substitutes for the Action-Risk Class's own required Confirmation
Strength (**DL-76**); a request outside the declared boundary is denied exactly as any other
unauthorized request.

**Type 2 — unmediated.** The delegate acts directly on a device, integration, or other subsystem HTBW
does not mediate; HTBW can only observe the resulting state afterward, per **DL-111**'s verified
evidence model (the `history` REST/WebSocket contract, with Context as supporting evidence; rich
automation/trace detail is **VERIFIED_NEGATIVE** for external retrieval). **HTBW cannot deny, confirm,
or undo a Type-2 action before it occurs, and must never claim otherwise.**

### Owner Policy Decision — Type-2 Risk-Class cap

**A declared Type-2 delegation boundary is constitutionally capped at the Convenience and Disclosure
Risk Classes.** Financial, Safety, Security, and Governance effects may be delegated only through a
Type-1, HTBW-mediated path where Confirmation Strength can actually be enforced before execution.
This is a structural floor, not an ordinary Household Override under **DL-76**'s three-tier model —
the limiting fact is architectural (pre-execution enforcement is impossible for Type 2), not a risk
preference a household could reasonably raise. **This does not claim HTBW can prevent a household
from operating a higher-risk external system outside HTBW's own declaration**: if such a system acts,
HTBW observes, attributes, and reports to the extent evidence supports, under **DL-73**, but never
represents it as authorized Delegated Adaptive Behaviour, and never implies it was pre-authorized,
confirmed, blocked, or preventable when it was not.

### Observation, never inference

HTBW may state only what evidence actually supports: that an action occurred, its target, requested/
effected value, timestamp, Source/Decision-Authority attribution at whatever tier the evidence
reaches (**DL-73**), and whether the observed effect falls inside or outside the declared boundary.
**HTBW must never infer or fabricate** motive, rationale, optimisation goal, internal policy state,
confidence, or model reasoning. Where the external engine itself supplies a reason, policy identifier,
or confidence value, HTBW may retain and cite it **as the engine's own externally asserted evidence**
— never reworded into HTBW's own reasoning, and never silently adopted as a Fact.

### Decision Trace and Domain Event, correctly distinguished

**The delegated action itself produces a Domain Event with Decision-Authority attribution (DL-73),
never its own Decision Trace** — restating, not reopening, "HTBW never produces a Decision Trace for
a decision HTBW did not make" (**DL-46**). A Decision Trace is produced only for HTBW's **own**
subsequent evaluation: whether the observed action falls inside the declared boundary, and what, if
anything, HTBW does next.

### Honest reduced explainability

Residents must be able to learn, in plain language and from governed records alone: who decided this
(HTBW or a named external delegate); what action occurred and when; whether it fell inside the
declared boundary; what evidence HTBW actually holds; and — stated plainly, never silently omitted —
what reasoning HTBW does **not** hold. HTBW never manufactures a "why" it does not have.

### Out-of-boundary behaviour

**Type 1**: denied by ordinary Operational Trust evaluation — no new mechanism. **Type 2**: HTBW
records the occurrence, attributes it per **DL-73**, compares it against the declared boundary, and
**reports** the violation to the household through the existing Communication/disclosure path — it
does **not** automatically reverse, suppress, or revoke the declaration; revocation remains a
household action against the declaration's own lifecycle, consistent with "do not invent automatic
revocation unless governed."

### Data disclosure is independent of action delegation

**Authorizing a delegate to act is never authorization to disclose household data to it.** Any
household state, Room, Person, or care/health information the external engine would need to decide is
independently governed by existing disclosure architecture (**DL-34**, audience-evaluated, never
assumed from access) — delegation of an action never implies, and never silently grants, data
disclosure; each is declared and evaluated separately.

### Distinct from Reasoning Provider, DL-83, and DL-114

A **Reasoning Provider** (**DL-93**) supplies reasoning to HTBW and owns no decision authority — the
opposite shape from a delegate, which owns its own decision and no HTBW authority; both may use
similar technology, which is irrelevant to responsibility ownership. **DL-83** (generated, persistent
HTBW-authored behaviour) remains HTBW's own decision under HTBW's own lifecycle — never this
decision's concern merely because generation involved a model. A third party invoking an **HTBW
service published under DL-114** is a request surface, never automatically delegated authority — the
identical Operational Trust evaluation already governs it, with no caller-origin exception, exactly as
Type 1 above; DL-114's own MCP/external-agent exposure question remains independently open and is not
decided here.

### Lifecycle

The declaration reuses existing governed-configuration mechanics: Record Identity and Version Identity
(**DL-104**), Change Records carrying Effective/Recorded Time and provenance (**DL-26**, **DL-27**,
**P30**) for creation, modification, suspension, and revocation; a stale or unresolvable external
engine reference resolves to unavailable and is reported, never silently dropped (**P30**). No new
lifecycle model is created.

## Home Production (HA-Prod) Trust-Boundary Admission (DL-119)

Full definition: [home-assistant-boundary.md, "Home Production (HA-Prod) trust boundary"](../architecture/home-assistant-boundary.md#home-production-ha-prod-trust-boundary-dl-119).

**Operational Trust owns the admission decision, never the resource's identity.** Foundation types and
holds a stable resource reference (`{Subject Type, Subject ID, Version Identity}`, **DL-104**) for any
service, App instance, execution host, or storage connection a household may consider for Home
Production. Operational Trust owns a separate, versioned **admission record** — the trust/policy
decision that a referenced resource is, or is not, currently an HA-Prod member, within what scope, and
as of when — citing Foundation's reference exactly as Operational Trust already **consumes** Stewardship's
Significance Declaration (above): never embedded inside Foundation's own record, never invented without
one. **This is the identical "Foundation feeds everything and consumes nothing" discipline applied to a
new question, not a new policy type.**

**Membership is not a disclosure grant and not a security certification.** An admitted resource gains no
access to Home data beyond its own already-authorized scope merely by being admitted; existing disclosure
evaluation (above, **DL-34**) is unweakened. Membership means *an explicitly governed participant
approved to satisfy HA-Prod locality/residency requirements within its authorized scope* — nothing more.

**Enforcement is bounded to mediated requests.** For a capability requiring HA-Prod-local processing,
Operational Trust checks current admission validity before permitting a resource to be treated as
local; absent or invalid, **DL-41** governs unchanged (`unavailable`, dependency named, no substitution
outside the required boundary). For genuinely unmediated external traffic, Operational Trust claims no
routing control, consistent with the honesty standard **DL-118** already established for unmediated
delegated action.

**Distinct from the Delegation Boundary above and from Execution Host (DL-50).** An admitted HA-Prod
resource decides nothing on its own — it is a trust/residency classification, never a decision
authority, and never conflated with a declared execution host, which answers a different, orthogonal
question (*where may this run*, not *is this inside the boundary*).

**First consumer: DL-120.** Speaker-biometric Identity processing's hard local-only ceiling
(voiceprint/embedding generation and runtime comparison) is the first capability-level rule built
directly on this admission test — no new residency concept, Foundation/Operational-Trust split, or
enforcement model was created for it. **DL-120's locality ceiling applies to the one governed Person
Voiceprint (DL-144) unchanged** — gallery structure and locality are orthogonal questions, neither
reopening the other.

## Urgency Entitlement (DL-77)


Resolves **OD-46**. Urgency is the **maximum interruption entitlement** Operational Trust grants to a
Communication. An originator may **propose**; **Operational Trust determines and grants.**

### The canonical ladder

Exactly four levels, fixed and **cumulative** — each a maximum permitted interruption, never a
mandatory delivery behaviour:

| Level | Entitlement adds |
|---|---|
| **No Interruption** | Retained; presented when context permits; may not interrupt a current activity, active Mode, protected time, or a sleeping person |
| **Interrupt Current Activity** | May interrupt a current activity or active Mode when other governance permits; may not override protected time or wake/disturb merely by this level |
| **Override Protected Time** | May override quiet hours or another governed protected-time condition when other governance permits; may not wake/disturb merely by this level |
| **Wake or Disturb** | May wake or deliberately disturb the intended audience when all other governance permits |

> **A category must never function as a bypass.** A safety or critical classification is an
> Operational-Trust-granted **entitlement** — revocable, explainable, and traced. It is never a right
> that an originator confers upon itself by naming its own category. Urgency is orthogonal to
> Category: Category describes what a Communication is about, Urgency describes what it may
> interrupt. The two axes must never be merged. See [communication.md](communication.md).

### Category is consumed, never owned (DL-78)

**Operational Trust never approves, rejects, reinterprets, replaces, repairs, or reclassifies a
Category, and never determines what a Communication is about.** It **consumes** Category — the closed,
seven-value enumeration (Stewardship, Security, Care, Environment, Experience, System, Safety)
Foundation owns — as one input among several to disclosure, audience, privacy, consent, Urgency, and
other governed-appropriateness decisions. **Operational Trust owns appropriateness, never semantic
classification.** Every originator draws from the identical closed enumeration, so no per-Communication
admissibility judgment exists for Operational Trust to make.

### Relationship to Action-Risk Classification (DL-76)

**Urgency and Action-Risk Classification are independent models.** Operational Trust consumes the
applicable Risk Class, thresholds, asset-class and individual-asset configuration, and household
policy as **one input among several** — current facts, context, audience, identity confidence,
consent, privacy, disclosure policy, active Mode, protected-time status, presence, and escalation
state all also apply. **There is no required one-to-one mapping**: two circumstances sharing a Risk
Class may receive different Urgency, and Urgency determination is never a blind numeric calculation.
Configuration may never bypass audience, privacy, consent, disclosure, identity, authority, or
life-safety governance.

### Six distinct values, never collapsed into one field

| Value | Meaning |
|---|---|
| **Originator Proposal** | The optional level the originator proposes. Advisory only — never the granted entitlement merely because proposed, never prescriptive of surface or timing, never able to bypass Operational Trust. Its absence is itself recorded |
| **Canonical HTBW Recommendation** | The current baseline recommendation for the governed scenario or configuration scope |
| **Learned Household Recommendation** | A Suggestion-stage proposal under the existing **P26**/**DL-21** learning promotion ladder (**resolved — OD-28 / DL-123**), derived from repeated accepted Household Overrides — never silently applied, requires explicit acceptance, rejection never alters configuration |
| **Configured Value** | The value currently accepted for the applicable scope |
| **Household Override State** | Whether the configured value differs from the recommendation, with provenance |
| **Granted Runtime Entitlement** | What Operational Trust actually grants, after evaluating configured policy and current facts |

**Recommended-value and override pattern.** The household must be able to view every canonical level,
see HTBW's recommendation, accept it, choose another, see override status, and understand the
consequence. **Visibility and explicit choice are canonical; a specific UI control is not.**

**Learned Household Recommendations and reset reuse existing mechanisms, inventing none.** A Learned
Household Recommendation is simply a Suggestion whose subject is an Urgency default — the same ladder
**DL-75** already applied to Significance. **Reset to the HTBW baseline extends DL-76's three-tier
override model** (Capability Default → HTBW Default → Household Override) with an explicit Reset
action: it shows the proposed changes, requires a sufficiently identified and authorized actor and
explicit confirmation, removes the Household Override and any unaccepted Learned Household
Recommendation within the selected scope, and restores the Configured Value to the Canonical HTBW
Recommendation. **Reset never rewrites history** — prior values and the reset decision remain
explainable through existing versioning, Change Records, and the Decision Trace.

### Urgency may be reevaluated

Operational Trust reevaluates the granted entitlement when material inputs change — facts, risk
evaluation, threshold state, escalation state, configuration, audience, presence, active Mode,
protected-time status, or other relevant context. **A reevaluation is a new Operational Trust
determination. It is never automatically retry, and never automatically escalation.** Elapsed time
alone is never sufficient to increase Urgency absent an accepted threshold, policy, risk change, or
escalation rule that makes it materially relevant.

**Effect of a decrease:** pending delivery must immediately respect the new, lower entitlement;
completed delivery remains historical fact and is never rewritten; queued delivery or retry requiring
the former entitlement is cancelled or replanned; the reevaluation, the prior entitlement, and the new
entitlement remain explainable.

### Precedence remains OD-04's

Urgency grants interruption **eligibility**; it does not order Communications that are otherwise
eligible. **OD-04 owns relative precedence**, including the ordering of Communications sharing one
Urgency level. This decision creates no second precedence mechanism.

### Audience, privacy, consent, and disclosure are never overridden

Guest eligibility, and every other audience question, is governed by the Communication's own audience
policy (**DL-34**), **never by an Urgency exception** — a Communication whose governed audience
includes all current occupants (a smoke or carbon-monoxide condition) was never granted that audience
**by** its Urgency. Audience determines who may receive it; disclosure governs what may be revealed;
Urgency governs what may be interrupted; Concierge governs how to help within all three.

**Permission to interrupt is not permission to disclose** (**DL-29**, **DL-34**, **P32**). Where the
granted entitlement cannot be exercised without violating audience, privacy, consent, or disclosure
governance, **delivery degrades** — surface change, content-free Indication, a Room-Delivery
Authorization Challenge where Room-eligible and safe (**DL-94**), or non-delivery — **the governance
never does**, and both the granted entitlement and the degradation are recorded.

### Concierge and surface separation

Urgency sets the maximum. **Concierge decides whether, when, through which surface, and in what
form**, operating only within the granted entitlement, the governed audience, privacy/consent/
disclosure restrictions, and verified surface capability (**DL-53**). Concierge may choose less
disruptive delivery than the maximum allowed, may never exceed the granted entitlement, and a material
choice to use less than the maximum remains explainable.

**Delivery Surface capability verification restates DL-53 directly, not reopened**: a surface
exercises only capability it can verifiably honour, and HTBW never falsely claims an entitlement was
fulfilled.

### Platform mapping

HTBW's canonical Urgency determination is mapped downward by the Delivery Surface adapter to a
verified platform capability where one exists. The mapping never renames an HTBW level, never treats a
platform ladder as the HTBW ladder, never lets a platform severity determine Operational Trust policy,
and never lets a platform limitation rewrite the canonical model. **Two existing, unrelated platform
severities are reaffirmed, not merged**: the developer-facing three-value `IssueSeverity`, and the Home
Assistant 2026.9 Security-dashboard resident-facing, household-declared, two-valued `Alert`/`Warning`
presentation severity (see
[../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md)) — **neither
is adopted as an HTBW Urgency value**; both carry no audience, no entitlement, and no interruption
policy.

### Deferral is distinct from Urgency, and is not redesigned here

A deferral request ("remind me in 30 minutes") changes delivery eligibility or timing; **it does not
itself change the granted Urgency.** Not every identified person may defer every Communication: a
deferral requires an identified actor, sufficient identity confidence for the requested action, an
Operational Trust authority determination, evaluation of whether the Communication type is deferrable
and of the requested duration or condition, and an explainable allow-or-deny outcome. **This restates,
and does not relocate, the existing ownership `stewardship.md` already records**: acknowledgement,
snooze, suppression, and duplicate-prevention semantics remain **OD-45** and **OD-54**. A later
Operational Trust reevaluation may terminate or supersede a deferral where changed facts justify a
stronger entitlement.

### Responsibility boundaries

| Responsibility | Owns | Does not own |
|---|---|---|
| **Operational Trust** | Urgency recommendation, determination, grant, reevaluation; authority to accept, override, reset, or defer | The Communication itself |
| **Originating responsibility** | The Communication, Category, and its optional proposed Urgency | The granted entitlement, surface, timing, form, or final audience |
| **Identity** | Evidence and confidence | Authority |
| **Concierge** | Whether, when, surface, and form within the entitlement | Urgency, audience policy, privacy policy, disclosure authority, or Risk Class |

**No new Communication, Messaging, Delivery, Escalation, Urgency, Recommendation, or Deferral
responsibility is created.**

### Life-safety boundary

Restates the existing non-negotiable constraint, now fully reconciled as **DL-79**. HTBW is not a
life-safety system and never describes a Communication as a certified alarm, a guaranteed
emergency-warning system, or a substitute for a native smoke, carbon-monoxide, fire, security, or
water-shutoff system. HTBW may communicate about native device state or supplement native behaviour,
but **never suppresses, defers, delays, or replaces a native alarm**, and never claims responsibility
for native alarm delivery. **A certified life-safety or protective device remains authoritative for
its own domain** — Operational Trust never reinterprets or restates its claim as stronger.

### One-time Administrator acknowledgement (DL-79)

Before Safety capabilities are enabled for a Home, an authenticated, logged-in **Administrator** must
accept a one-time acknowledgement stating the non-life-safety boundary, that Safety-related
capabilities may become `Unavailable` (**DL-41**), and that Safety follows ordinary audience, privacy,
consent, disclosure, Urgency, and delivery governance. **Operational Trust determines whether the
accepting identity holds Administrator authority**, reusing the existing authenticated-administrator
pattern already accepted for other administrator-gated changes (**DL-37**, **DL-40**) — **a native
administrator flag confers no care, guardianship, or proxy authority** (**DL-57**, unchanged). The
acceptance record reuses **DL-56**'s consent-record shape (actor, scope, granted/effective time,
version), extended here to a Home-level governance-boundary acceptance. An installer's technical setup
action is never household acceptance. Reacceptance is required only for a material governance-boundary
change, never for routine software changes. **The onboarding or commissioning surface that captures
this acknowledgement is not decided here** — the repository has no onboarding architecture today, a
residual **OD-85** (#172) already owns.

### Evidence-quality-proportionate conclusions and Investigation Needed (DL-79)

Every conclusion Operational Trust evaluates or consumes — Safety or otherwise — is expressed in
proportion to the evidence quality supporting it, reusing **DL-58** Truth Confidence and **DL-38**
Identity confidence; no Safety-specific confidence ladder exists. Where evidence is missing, stale, or
conflicting, Operational Trust never forces a conclusion, restating **DL-41** unchanged. **Investigation
Needed** is a governed conclusion/handling outcome — never a Category, an Urgency level, or a
guarantee — applied where evidence supports household attention but not a stronger conclusion; it never
automatically grants broader Urgency, audience, or disclosure. See
[communication.md](communication.md).

---

## The unidentified-person policy

When Identity reports `unknown` with a human participant supported, Operational Trust evaluates the
request against the **unidentified-person policy** — the least-privileged applicable policy already
required by the failure behaviour below, stated here as a governed policy rather than only as a
fallback.

> **The unidentified-person policy is a policy subject. It is not a profile, and it is not a person.**

It has no preferences, no history, no learning, and no identity. It is the set of rules the household
configures for *whoever we cannot identify*, and it is evaluated exactly like any other policy scope,
under the ceiling rule.

| The policy may permit | The policy may restrict |
|---|---|
| Controlling participating lights and shades in the current Room | Reading personal email, calendar, or communications |
| Household-neutral media playback | Resident-specific schedules, routines, and preferences |
| Asking for the time, the weather, or a household-neutral question | Private household history and movement history |
| A configured general-question capability | Creating or influencing person-specific learning |
| Non-sensitive Room Help | Modifying identity associations, consent, or permissions |
| — | High-consequence and safety-critical actions |
| — | Any content whose audience is not authorised |

**These illustrate the policy's shape. They are not defaults.** The canonical Risk-Class enumeration
and defaults are **DL-76**; the Required Identity Band per class is **configuration** under **DL-39**.

Two consequences are not configurable:

- **No resident permission, preference, or history is inherited.** An Unknown Person never acts as,
  or on behalf of, a resident.
- **No person-scoped learning is created.** An Unknown Person's interactions are not eligible
  evidence for a person-scoped learned preference (**OD-65**). Room-scoped observation, where the
  household permits it, stays room-scoped and person-free.

### General questions and reasoning providers

Where the policy permits a general-question capability, the boundary is the **context supplied**, not
the phrasing of the question:

- Only **household-neutral** context may be supplied unless policy explicitly permits more
- Household-private context is **not** authorised merely because the request originated inside the home
- A general answer must not expose resident-specific data
- The provider owns no identity, permission, Truth, or household authority, and must never infer or create one

The provider remains replaceable. Provider strategy is **accepted DL-93** (**OD-67**, closed, Issue
#132), summarized below.

### Allow General Questions and Allow Home Steward (accepted, DL-93, Issue #132)

**Allow General Questions** and **Allow Home Steward** are two **independent** Person-scoped
authorization settings, owned by Operational Trust under **DL-39** wherever they are surfaced in
configuration (Person Configuration exposes them; it does not own their semantics). **Neither is a
blanket "AI allowed" setting**, and neither governs deterministic Home control, Concierge generally,
Home Intelligence, Stewardship, Continuity, or any other capability that does not itself declare the
corresponding dependency. **There is no Room-scoped authorization or Room provider assignment for
either capability.**

Every evaluation resolves to exactly one **effective Person** first: the resolved household Person when
Identity/Operational Trust permit Person-scoped use; otherwise the household's designated **Guest
fallback Person Extension** (**DL-71**) if one is configured — a real Person whose own settings are
consulted, creating no Identity Assertion binding; otherwise the **DL-33** unidentified-person policy.
**No Room is ever consulted in this resolution.**

Authorization is evaluated **before** provider resolution, never after, against the effective Person's
own setting:

- **NO is terminal** — resolution stops immediately; no provider is tried; the result is a
  **prohibition**, never described as unavailability.
- **YES authorizes** resolution to proceed.

This ADR does not define "sufficiently resolved" as a band value or score; it references the existing
**DL-39** Required Identity Band ownership exactly as every other Operational-Trust-owned threshold is
referenced.

**Configured fallback, never discovery:** effective Person's own provider, then the Integration-default
provider, then unavailable. A terminal authorization denial never enters this chain; provider
unavailability (not configured, invalid, or unreachable) may advance to the next configured scope, but
is never expressed as a trust or permission outcome (**DL-41**). No provider outside this configured
chain is ever selected — HTBW performs no runtime discovery of a Reasoning provider.

**Allow Home Steward YES is a top-level eligibility gate only**, never universal information access;
finer-grained category authorization (financial, maintenance, insurance, and similar) remains separately
governed. Allow General Questions and Allow Home Steward are independent: denial of one never affects
the other, and neither is a fallback for the other.

See [../architecture/adr-reasoning-provider-strategy.md](../architecture/adr-reasoning-provider-strategy.md)
for the full drafted decision.

---

## Disclosure is evaluated against the audience, not the requestor

> **Establishing who asked does not establish that everyone able to perceive the answer is an
> authorised recipient.**

### Disclosure is separate from knowledge

> **The question is not *"can the home know?"* It is *"should the home share?"***

These are two different questions, answered at two different points, by two different responsibilities.
Collapsing them is the single most common way a home that is behaving correctly still behaves badly.

| | Knowledge acquisition | Disclosure decision |
|---|---|---|
| The question | May this be **established**? | May this be **conveyed**, here, now, to these people? |
| Owner | **Identity** for assertions; **Truth** for Facts; **Foundation** for definitions; **Operational Trust** for whether the evidence is eligible at all | **Operational Trust** |
| Governed by | Consent, evidence eligibility, participation | Audience composition, classification, surface, mode, policy |
| When evaluated | When evidence arrives | At the moment of conveying, and **again** at each Delivery Attempt |
| A negative means | *The home cannot establish this* | *The home will not say this, here, now* |

**The home may legitimately know something it will not say**, and that is not a defect — it is the
architecture working. **A home that shares everything it knows has no privacy model at all.**

The inverse is equally binding: **the home must never establish something merely because disclosing it
would be useful.** Knowledge acquisition is gated by consent and evidence eligibility, and a
disclosure requirement never reaches back to authorise collection.

### Audience awareness is a first-class input

> **Operational Trust evaluates who is asking *and* who is listening.**

Requestor identity answers *may this person have this?* **Audience composition answers *may this be
said where it can be heard?*** Both are required, and neither substitutes for the other.

**The decisive property: identity confidence may remain completely unchanged while the outcome
varies.** The same request, by the same person, at the same band, in the same Room, may be answered
aloud, answered privately, answered without content, or declined — **because the room changed, not
because the person did.**

| Audience context | Identity confidence | Typical governed outcome |
|---|---|---|
| **Alone** | Unchanged | Content may be conveyed on the shared surface |
| **A known participant is present**, authorised for this content | Unchanged | Content may be conveyed; the audience is eligible |
| **A known participant is present**, *not* authorised for this content | Unchanged | Content withheld on this surface; a private surface or content-free indication may be offered |
| **A guest is present** | Unchanged | Guests are **never an audience by default**; conservative treatment applies |
| **An unidentified person is present** — `unknown`, human participant supported | Unchanged | Audience composition carries **residual uncertainty**; degrade rather than assume solitude |
| **Audience composition cannot be established** | Unchanged | **OD-71** governs: confirm, degrade to content-free indication, redirect to a private surface, or refuse |

Three rules bind every row:

- **Audience composition identifies nobody.** It **consumes** accepted identity assertions and presence
  Facts, is **never a second identity fusion**, and **retains its uncertainty** (**DL-34**).
- **Absence of evidence is never proof of solitude.** An empty audience list means *nothing was
  detected*, not *nobody is there*.
- **A detected device is not proof its owner can hear**, and **a surface is not private merely because
  it is a phone**.

**Requestor, Speaker, Present Person, Potential Listener, Authorized Recipient, and Delivery Target
answer different questions and are never collapsed.**

### Authorized Recipient resolution from a relationship (DL-71)

Where an Intended Audience Specification is **Relationship-based** (for example "Caretaker of
Maisey"), Stewardship's current relationship record supplies **candidates**, never authorization.
**Holding the relationship is not, by itself, sufficient**: a candidate becomes an Authorized
Recipient only where Operational Trust also confirms a currently valid **Delegated Access Grant**
(**DL-57**) covering at least the `receive` operation for that subject's Stewardship content — and
at least `complete` where the candidate is also expected to be able to close a shared obligation.
This is the existing **DL-57** rule ("accountability is not access") applied to audience resolution,
not a new authority model.

### Prefer explicit metadata over inferred sensitivity

> **Where content carries an explicit classification, Operational Trust uses it. It does not attempt
> to work out how sensitive something is by reading it.**

This is an implementation-bearing preference, and it follows directly from accepted architecture:
**P15** requires uncertainty to remain visible, **DL-34** already prohibits a reasoning provider from
acting as the sensitivity classifier, and **P16** requires the decision to be explainable.

| Preferred | Over |
|---|---|
| An explicit **privacy marking** carried by the item — for example a calendar item marked *Private* | Interpreting the item's content |
| A **household-configured classification** for a capability, resource, or content class | Inferring sensitivity from words, participants, or topic |
| A **declared** classification supplied by the originating source | Semantic classification performed at decision time |
| An explicit *unclassified* or *unmarked* state, treated under policy | Guessing a classification because none was supplied |

**Why this is architecture and not taste:**

| Benefit | Consequence for the home |
|---|---|
| **Explainability** | *"You marked it private"* is an explanation a resident can verify. *"It looked sensitive"* is not |
| **Predictability** | The same item is classified the same way every time, by every surface |
| **Auditability** | The classification has a source, a version, and a change record — it can be reviewed and corrected |
| **Implementation simplicity** | No content model, no inference engine, and no provider dependency inside a permission decision |

Three constraints apply:

- **An absent marking is not a permissive marking.** Where no classification is supplied, the governing
  policy for unclassified content applies — it is never silently treated as public.
- **A reasoning provider is never the sensitivity classifier**, and inference never becomes the
  authoritative classification (**DL-34**, **OD-67**).
- **Which native fields carry an explicit marking is a platform question**, subject to the ordered
  burden of proof in **DL-30**. **No native classification field is claimed here**, and none may be
  assumed; the principle binds regardless of which source supplies the marking.

Where a household wants an inferred signal, it may be surfaced as a **proposal** under **P26** and the
promotion ladder — **never applied silently as a classification.**

### Access and disclosure are two decisions

This is **P32** applied to the *solicited* case. P32 was stated for outbound communication, where the
audience is chosen by no requester. The same Existence → Participation → Exposure → Authority chain
applies when a resident asks a question aloud in a Room where someone else can hear the answer.

**Access and disclosure are two decisions.** Tom may be authorised to read Tom's email without that
authorising the home to read it aloud in front of David, in front of an Unknown Person, across
several Rooms, onto a shared display, or into a reasoning-provider request.

These outcomes must remain separately representable:

| Outcome | Meaning |
|---|---|
| Access allowed, disclosure allowed | The content may be conveyed on the proposed surface |
| Access allowed, disclosure requires confirmation | The requestor is asked before the content is conveyed |
| Access allowed, disclosure not appropriate | Content is withheld on this surface; a content-free indication may still be permitted |
| Access allowed, private delivery available | A more appropriate surface exists and may be offered |
| Access denied | The requestor may not have the content at all |
| Identity or audience insufficient | The decision cannot be made safely; **the delivery degrades, the governance does not** |

Every disclosure decision considers requestor identity and confidence, content owner, classification
and sensitivity, intended recipient, **audience composition and its uncertainty**, the proposed
delivery surface, Room, time or mode, applicable policy, consent, any required confirmation, and the
safer alternatives available.

**Operational Trust makes this decision.** Identity does not — it supplies assertions. Concierge does
not — it selects a surface *after* permission is established, and offers the alternative.
Communication does not — it is the governed object. **A reasoning provider is never the sensitivity
classifier.** See [communication.md](communication.md) and
[../architecture/principles.md](../architecture/principles.md).

The policy applied when audience composition is uncertain or undetectable is **DL-72** (resolved
**OD-71**), below.

### Audience-uncertainty disclosure policy (DL-72)

**System-Initiated Communication and Person-Requested Response receive different treatment.** A
System-Initiated Communication (a medication reminder, new private Mail, a Calendar reminder, a
Stewardship warning) carries no current explicit request; a Person-Requested Response answers a
Person's current explicit request (*"What is on my Calendar?"*). **An explicit request is evidence of
willingness to receive an authorized response through the current interaction context — never
unrestricted consent** — and remains bounded by every other rule in this document: it does not
authorize disclosure of another Person's information, does not reach a prohibited reconstruction
(**DL-35**), and is void wherever requester authority, applicability, or safe surface presentation
cannot be established.

**For a System-Initiated Communication where audience composition cannot be safely established, the
accepted default order is**: (1) authorized private delivery to each intended recipient's own
configured destination; (2) content-free Indication, where permitted; (3) a neutral confirmation or
clarification challenge naming no candidate, subject, relationship, or sensitive content; (4)
deferral or refusal, preserving the Communication for retry or escalation. **This is the
privacy-preserving floor and applies even absent household configuration.** See
[communication.md](communication.md) for the full statement and illustrative examples.

**Two Continuity-owned Person Setup preferences are distinct and must not be conflated**: the
existing **Ordinary Delivery Preference** (where Communications normally go) and the new
**Audience-Uncertainty Routing Preference** (where to route when audience composition cannot be
safely established). Operational Trust evaluates both identically — the preference supplies a desired
path; **this model determines whether that path is currently permitted and safe**; Concierge selects
the Delivery Target. A Person preference may select only among already-allowed degradation
behaviours; **it can never weaken the privacy floor or authorize a prohibited disclosure**. Where no
Person-specific preference exists, the household's Global default applies (accepted as "prefer
authorized private delivery").

**Unresolved plurality, Audience unknown, and Audience detection unavailable remain three distinct
composition states (DL-34), and contradictory evidence (evaluated under DL-63) is a fourth** — all
four receive the same default disposition, but the Decision Trace preserves which one actually
applied. A Merged Room's wider Potential Listener and Delivery Surface pool changes the composition
**inputs** evaluated here, never the policy itself.

### Historical Retrieval and Access authorization (resolved — DL-130)

**Access and disclosure remain two decisions for a historical question exactly as for a current one**
(restating the rule above, never reopening it). A historical query reaches Operational Trust through
Assist/Conversation — the sole resident-facing surface, internally classified before any content is
assembled into an ordinary retrieval or a Person/actor reconstruction (**DL-35**, never reachable
through generic Room Help or a general-question capability).

**Subject Authorization is Person-scope and Relationship-scope policy, unchanged from the existing
scope table above.** Where a historical query's Subject is a Person or a Pet, the Subject's own
configured access policy — owned by Operational Trust under the existing **Person-level authority**
and **Privacy visibility policy** items — governs who may inquire about them historically. That
policy is expressed using **DL-71**'s five already-accepted Intended Audience Specification forms
(Named Person, Role/Authority Class, Relationship-based, Anyone Present With Authority, Household),
reused unchanged, never a new vocabulary. A **DL-49** `caretaker-of` relationship — typed over Person,
Pet, and Asset subjects alike — supplies a **candidate** only: holding the relationship is never
itself sufficient, restating DL-71/DL-57's "accountability is not access" discipline, now applied to
Historical Retrieval access generally rather than only to Stewardship content. The resulting Access
outcome combines with every other applicable scope (Home, Room, Person, Relationship, Asset,
Action-Risk Class) under the existing **DL-126** most-restrictive-combination algorithm — no new
scope is added.

**Current-location access and historical-movement-reconstruction access are two independently
configurable capabilities, never one setting.** Both classify under **DL-76**'s existing Disclosure
Risk Class HTBW Default (Moderate Identity Band, Verbal Confirmation Strength); a household wanting
stricter treatment for reconstruction-class queries specifically may apply **DL-109**'s existing
object-specific override, restating "the requirement belongs to what is being protected" — neither
is inherited from the other by default, and no new Required Identity Band/Confirmation Strength table
is created.

**Refusal reuses the existing six-outcome disclosure table above unchanged.** An
authorized-to-ask-but-unauthorized-to-receive historical question resolves to "Access denied" or
"Access allowed, disclosure not appropriate" — a resident-safe, content-free refusal that never
confirms or denies the existence or completeness of the underlying evidence. No bespoke historical
refusal taxonomy is introduced.

See [../architecture/explainability.md](../architecture/explainability.md)'s "Historical Retrieval and
Access" section for the full query model, the twelve-step authorization sequence, and the Episode 9
category mapping.

### Explainability Projection and endpoint authority (resolved — DL-140)

**Assist is the canonical household-facing Explainability interaction path.** Companion App,
dashboard/kiosk, and voice are endpoints through which Assist is invoked — never independent
Explainability capabilities, and never independent authorization paths. The endpoint may contribute
requester evidence, Room context, audience context, private/shared classification, and output
modality; **it never grants access, disclosure, or audience authority by itself**:

```
SURFACE VISIBILITY        != ACCESS AUTHORITY
SURFACE AVAILABILITY      != DISCLOSURE AUTHORITY
DEVICE OWNERSHIP          != UNRESTRICTED EXPLAINABILITY AUTHORITY
HA ADMINISTRATOR STATUS   != HTBW GOVERNANCE AUTHORITY
SIGNED-IN USER            != COMPLETE AUDIENCE COMPOSITION
```

**An HA administrator account does not automatically receive unrestricted Explainability access.**
Native administrator status does not replace Identity, does not replace Operational Trust, does not
grant access to private resident information, and does not bypass presentation policy. If an
administrator is also a governed Person with appropriate authority, Operational Trust may authorize
permitted detail for that Person/context — authority comes from HTBW governance, not the HA admin
flag. No user-selectable "detail level" (a request to "show raw trace," "administrator view," or
"full audit") bypasses this evaluation; it triggers another ordinary access/disclosure/presentation
evaluation.

**Access, disclosure, and presentation remain three separable considerations for an Explainability
request**, reusing the existing mechanisms above and `decision-trace.md`'s existing Access decision
and Presentation decision fields — no new recorded-outcome field is created. Presentation additionally
evaluates endpoint/modality eligibility for Explainability specifically: whether the authorized
content may be rendered on this endpoint, through this modality, right now. A projection assembled for
one requester/audience/endpoint is never reused for another without fresh evaluation, and a
surface/endpoint change (for example, from shared voice Assist to private Companion App Assist)
triggers a new evaluation rather than inheriting a prior authorization or refusal.

Full decision:
[../architecture/adr-explainability-presentation-and-assist-interaction-path.md](../architecture/adr-explainability-presentation-and-assist-interaction-path.md)
(**DL-140**, resolving **OD-30**).

### Location disclosure

> **A location answer is a disclosure about a person, whatever its Subject.**

Truth publishes Location Facts about a Home, Room, Merged Room, Person, Pet, Asset, or Device. **Whether
one may be conveyed, to whom, and on which surface is Operational Trust's decision, evaluated against
audience composition (DL-34, P32) — never against who asked.** Access and disclosure remain two
decisions, and the six outcomes above apply unchanged.

#### Device location may disclose Person location

A Device is bound to a Person through an Identity Evidence Association or a native Person-to-tracker
relationship. **Answering where the device is therefore frequently answers where its owner is**, to
everyone who can perceive the surface.

```
Asked   : "Where is Tom's phone?"
Answered: "Tom's phone is in the Den."
Heard as: "Tom is in the Den."
```

| Requirement | Statement |
|---|---|
| **Audience evaluation is mandatory** | A device-location answer is evaluated as a **person-location disclosure** whenever the device is bound to a Person, regardless of how the question was phrased |
| The Subject does not lower the requirement | Classifying the request as *asset or device location rather than engager identification* is correct about **ownership**. **It is not a licence to skip disclosure evaluation** |
| The requestor is not the audience | Tom asking about Tom's phone does not authorise stating Tom's whereabouts aloud in front of David, an Unknown Person, or a shared surface |
| Another Person's device is a disclosure about them | *"Where is David's phone?"* is a disclosure about **David**, and David's disclosure policy governs it \u2014 not the requestor's |
| The honest degradation applies | Where audience composition is uncertain, **the delivery degrades, not the governance**: a content-free indication, a private surface, a confirmation, or a refusal, per **OD-71** |
| Do not over-claim | A device-location Fact **never establishes that the bound Person is with the device**. An answer must not state or imply that it does |

#### Pet location may disclose human movement

A pet-worn tag reports where the tag is observed, continuously, in rooms people occupy. **A dog that
sleeps in the Primary Bedroom reports when the Primary Bedroom is occupied.**

| Requirement | Statement |
|---|---|
| **Consent evaluation is required** | Consent to track a Pet is **not** consent to derive household movement or occupancy patterns from it. Where pet-location evidence is used, or retained, for anything beyond the Pet's own location, the applicable consent must be present. Evidence lacking valid consent is **excluded before weighting**, never down-weighted |
| **Disclosure evaluation is required** | *"Maisey is in the Primary Bedroom"* is evaluated as a **room-occupancy disclosure**, on the same terms as any other |
| Sensitive Rooms are not exempted by the Subject | A bedroom, bathroom, or guest room does not become disclosable because the question named a Pet |
| No person-scoped inference | Pet-location evidence **never** nominates a candidate Person, never enters the Identity Fusion Function, and never creates person-scoped learning |
| A tag is not the Pet | A tag-location Fact states where the **tag** is. Presenting it as the Pet's location where the tag may have been removed or moved is a false claim, and the conflict is preserved rather than hidden |

Both cases are ordinary applications of the existing chain \u2014 Existence \u2192 Participation \u2192 Exposure \u2192
Authority \u2014 and of **DL-34**. **No new access-control object, policy mechanism, or responsibility is
introduced by either.** Every location disclosure decision, **including a refusal and a degradation**, is
recorded in the Decision Trace, with the access outcome and the disclosure outcome recorded **separately**.

See [../models/truth.md](../models/truth.md) and [../architecture/privacy.md](../architecture/privacy.md).

---

## Confirmation

Confirmation resolves the gap between **probabilistic identity evidence** and **a requirement**. It
is already an authority outcome — `permitted_with_confirmation` — and already an identity evidence
source establishing *"the confirmed claim, on the confirmed channel, for a bounded time"* and
explicitly not *"unrelated claims, future interactions, permanent certainty"* (see
[person-and-identity.md](person-and-identity.md)). This section governs that existing concept.
**There is no second confirmation model.**

### Opportunity and requirement are different

| Aspect | Confirmation Opportunity | Confirmation Requirement |
|---|---|---|
| Trigger | Confidence is **below** the requirement | The operation demands it **regardless** of confidence |
| Purpose | Offer a governed alternative to refusal | Ensure a consequential act is deliberate and attributable |
| If declined | The original refusal stands | The action does not proceed |
| Example | *"I think I am speaking with Tom. Can you confirm?"* | *"Before I change permissions, please confirm that you are Tom."* |

**A shortfall in confidence is not automatically a refusal**, and **high confidence is not
automatically sufficient.** Both directions are policy, held by the protected capability or
operation, not by Identity and not by Concierge.

### Confirmed is not certainty

> **A successful confirmation does not make the original Identity Assertion more confident, and does
> not make it complete.**

A confirmation produces a **separate governed confirmation record**. It does not rewrite the provider
match value, the fused confidence, the evidence, the original assertion, earlier actions, or earlier
uncertainty. An assertion made at a moderate band **remains** moderate afterwards, and remains the
historically correct record of what the evidence supported.

**`Confirmed` is a scoped interaction state, not the top of the confidence scale.** It is produced by
a governed process rather than by evidence fusion, and it must never be rendered as a percentage, as
"certain", or as an authenticated session. Where a new assertion is emitted after confirmation, it
**references** the original, names the confirmation method and scope, and never overwrites it.

### Method strength

> **A spoken "yes" is not proof of identity for every operation.**

A verbal confirmation arriving on the same channel as the original request is corroborated by the
same evidence that was already insufficient. It may be adequate for low and moderate consequence. It
is **not** adequate on its own for permission changes, identity enrollment, security configuration,
financially consequential action, highly sensitive disclosure, Preservation Hold release, evidence
deletion, or administrator changes.

**A capability declares the confirmation strength it requires.** A confirmation mechanism never
declares its own sufficiency.

**Required Confirmation Strength** is an ordered class set. It describes **what a confirmation must
be worth**, and says nothing about how it is performed:

```text
None  <  Verbal  <  Authenticated  <  Strong
```

| Class | What it requires |
|---|---|
| **`None`** | No confirmation is required for this operation |
| **Verbal** | An in-interaction acknowledgement from the participant, on the channel already in use |
| **Authenticated** | Confirmation performed through a surface carrying a governed authenticated user context |
| **Strong** | Confirmation carrying a factor **deliberately independent of the evidence that produced the assertion**, and of the channel that carried the request |

Two rules give the ladder its meaning, and both already follow from **DL-32** and **DL-37**:

- **Independence is what separates the classes**, not effort or friction. A verbal *yes* on the same
  channel is corroborated by the evidence that was already insufficient — which is why it is the
  weakest class and why it can never satisfy **Strong**.
- **A class is not a mechanism.** A strength class is satisfied only by a mechanism the deployment has
  **verified** as meeting it. **No mechanism is prescribed, assumed, or required to exist here**, and a
  mechanism is never credited with a class merely because it feels secure.

Where a required class has no verified mechanism available in the deployment, the outcome is the
existing **`Unavailable`**, and the operation is refused or degraded under normal policy. **An
unavailable strength is never silently downgraded to a weaker one.**

Which class each capability, protected operation, and Action-Risk Class requires is **configuration**,
resolved with **DL-76**'s enumeration and defaults. **Verbal** is not adequate on its own for permission changes,
identity enrollment, security configuration, financially consequential action, highly sensitive
disclosure, Preservation Hold release, evidence deletion, or administrator changes (**DL-37**).

### Scope

> **Every confirmation is bounded. An unbounded confirmation is an authenticated session under
> another name, and is prohibited.**

| Axis | The bound |
|---|---|
| Purpose | The claim confirmed, for the assertion purpose it answered |
| Capability and operation | The specific capability and operation. **Calendar access never silently authorises email, permissions, or enrollment** |
| Interaction | The current request, or a bounded interaction where policy permits |
| Channel | The surface on which the confirmation actually occurred |
| Room | The Room context in which it was given, where policy requires |
| Person | The claimed Person only. **Another Person's assertion is untouched** |
| Time | A governed lifetime, after which it is **expired**, not weakened |
| Audience | **None.** Confirming identity or access confirms nothing about disclosure |

The audience row is **DL-34** and is not negotiable. A confirmation that Tom may read his email says
nothing about who else can hear it, and **a confirmation given on an authenticated phone does not
establish that the Room is empty.**

Lifetimes are policy and **no duration is invented here**. Confirmation lifetime is a different
question from Identity Assertion Validity and Current-Interaction Applicability, which are **DL-64**.

### Confirmation is consumed by its operation

> **A confirmation is spent when the operation it was raised for is evaluated.**

| Default architectural behaviour | Statement |
|---|---|
| Consumed | The confirmation applies to the protected operation, or bounded interaction, for which it was requested, and is then spent |
| No presence lifetime | **It does not remain active because presence is still detected**, because the Room is still occupied, or for any occupancy grace period |
| No session | It never becomes a general authenticated session, and never establishes who initiates the next interaction |
| No carry-forward | It does not authorise the next protected operation automatically, even an identical one |
| Band unchanged | **It never changes the Identity confidence band** (**DL-37**) |
| Presentation unaffected | It does not relax Address by Name unless the presentation policy separately and explicitly says so |

Where a household legitimately needs a multi-step protected task to proceed without re-challenging at
every step, **that bound must be stated explicitly by the capability** as a bounded interaction — a
named sequence, with a stated end. It is never an implicit consequence of presence, of time, or of a
previous success.

Worked example. Tom is `known` at **Moderate**. The calendar's Required Identity Band is **Very
High**, with
confirmation permitted as a substitute. Tom confirms by an accepted method, and the calendar
operation proceeds. Then:

- The Identity Assertion **remains Moderate**
- The confirmation applies to **that calendar operation**
- A following email request is **re-evaluated** against the mailbox's own requirement
- A following calendar question is **re-evaluated**
- The next voice interaction produces a **new current-speaker assertion**
- If Tom leaves and David speaks, **nothing of Tom's carries over** — not the confirmation, not the
  band, not the naming eligibility

### Outcomes

| Outcome | Meaning |
|---|---|
| **Confirmed** | The confirmation succeeded, for its governed scope only |
| **Denied** | The participant states that the candidate is wrong |
| **Unclear** | The response cannot be interpreted reliably |
| **Cancelled** | The requestor declines, or abandons the action |
| **Unavailable** | The required confirmation method cannot be completed |
| **Expired** | A prior confirmation is outside its scope or lifetime |

`Unclear`, `Unavailable`, and `Expired` are **never rendered as Confirmed**, and an expired
confirmation is re-evaluated rather than silently carried forward.

On **Denied** — *"No, I'm David"* — the original assertion is preserved, the contradiction is recorded
as governed evidence, and the candidate confirmation fails for that purpose. **A stated name is a
claim, not an identification.** It does not establish David unless a governed process independently
supports it; the next-highest candidate is **never** silently selected; the outcome may correctly
become `ambiguous` or `unknown`; no durable identity association is created; no voice profile is
trained; and no evidence weight changes automatically (**DL-32**).

### A confirmation challenge is itself a Communication

*"I think I am speaking with Tom. Can you confirm?"* announces to everyone within earshot that the
home believes Tom is present. **The challenge is audience-evaluated before it is spoken** (**DL-34**,
**P32**): candidate-name disclosure, the Room audience, identity privacy, the confirmation surface,
and whether a safer private or neutral challenge exists are all inputs.

A neutral challenge that requests confirmation **without naming a candidate** is a legitimate
outcome, as is redirecting the challenge to an authorised private surface. **No wording is prescribed
here.** The policy applied when audience composition is uncertain is **OD-71**.

### Confirmation and an Unknown Person

An Unknown Person may request something that requires known-person identity. Policy may permit
offering identification or confirmation, continuing as Unknown Person for household-neutral activity,
refusing the protected request, or offering a non-sensitive alternative.

**Enrollment is never forced, and no Person is created** (**DL-33**). *"Yes, I am Tom"* from an
unidentified participant is a **self-assertion** carrying only the strength its method and policy
support. Where the capability requires authenticated confirmation, a verbal self-assertion is
insufficient — and it never becomes enrollment, a durable association, or a permanent identity.

---

## Explicit non-responsibilities

Operational Trust does **not**:

- Determine who a person is (Identity)
- Determine what is true (Truth)
- Determine what matters (Stewardship)
- Store preferences or sessions (Continuity)
- Decide what should happen (Concierge)
- Perform actions (Concierge, through governed interfaces)
- Own the explanation surface, though it must supply the reason behind every decision
- Originate, deliver, suppress, retry, or record a Communication (originators and Concierge)
- Own the escalation **ladder**, which is Stewardship's (**OD-22**)

---

## Learned suggestion versus autonomous policy

> **A learned suggestion is not an autonomous policy.**

Observed patterns may be proposed to the household. They become policy only through explicit
household acceptance, recorded with provenance. Silent promotion of a learned pattern into autonomous
behavior is prohibited.

**The full lifecycle is resolved as OD-28 / DL-123.** Operational Trust's own role is unchanged and
restated precisely: it holds the autonomy permission (never the preference, which is Continuity's)
and evaluates acceptance authority exactly as any other protected mutation — the Confirmation
Strength floor is this document's own existing "permission changes" category (at least
**Authenticated**), because accepting a Suggestion always grants an autonomy permission, regardless of
the resulting Adaptive Policy's own Action-Risk Class. Pause is a resumable Operational Trust Change
Record suspending only the permission's active state; revocation is a terminal Operational Trust
Change Record that stops future autonomous authority immediately without rewriting the Decision Traces
that explain actions already taken while the permission was active. Neither pause nor revocation
touches the Continuity preference itself.

---

## Failure behavior

Operational Trust **fails closed**.

| Condition | Behavior |
|---|---|
| Identity unresolved | Apply the least-privileged applicable policy (guest-safe). Never assume the most likely resident for an authority-bearing action. |
| Identity ambiguous | Do not silently select a candidate. Require disambiguation or refuse. |
| A required fact is unknown | Do not treat unknown as permission. Refuse, ask, or select the benign action. |
| A policy source is unavailable | Apply the most restrictive known policy and report the degradation. |
| Policies conflict irreconcilably | Refuse, explain the conflict, and surface it for household resolution. |
| Consent is missing or expired | Refuse. Missing consent is never implied consent. |
| Confidence is below the requirement | Refuse, or offer confirmation where policy permits it. **Never lower the requirement.** |
| A required confirmation method is unavailable | Refuse, and explain the unmet requirement. A weaker method is never substituted silently. |
| A confirmation response is unclear | Treat as not confirmed. **`Unclear` is never rendered as `Confirmed`.** |
| A prior confirmation has expired | Re-evaluate the request. Expired confirmation never persists silently. |

See [../architecture/failure-and-degradation.md](../architecture/failure-and-degradation.md).

---

## Privacy considerations

Operational Trust owns the visibility policy for personal preferences, presence history, session
history, Stewardship content, and Decision Traces. Guest and child-safe treatments are policy
positions here, not ad-hoc filtering elsewhere.

See [../architecture/privacy.md](../architecture/privacy.md).

---

## Explainability requirements

Every authority decision records:

- The action requested and its risk class
- The identity assertion relied upon, with confidence
- **The threshold that applied, and whether it was met**
- **Whether confirmation was offered or required; its method, outcome, scope, and expiry**
- **The audience composition considered, and the disclosure decision separately from the access decision**
- The facts relied upon
- The policies evaluated, including which were restrictive
- The effective autonomy level and the policy that set the ceiling
- The outcome: permitted, prohibited, confirmation required, escalation required
- The human-readable reason

A refusal must be explainable to the resident in household language.

---

## Retention, history, and preservation authority

**Operational Trust owns the history of its own records**, and owns the *policy* governing everyone
else's retention. Foundation defines the shared temporal model; see
[temporal-record.md](temporal-record.md).

### History owned by Operational Trust

- Policy history
- Authorization-decision history
- Privacy-policy history
- Retention-policy history
- Preservation-hold authority history

Policy history is recorded so that a past decision can cite **the policy version that applied at the
time** (**P30**). Changing a policy today must never silently rewrite the explanation of a decision
made under the previous version.

### Retention classification

Operational Trust owns retention classification and privacy classification policy for governed
records. Retention is bounded from **both** directions:

| Constraint | Source |
|---|---|
| Retention **floor** | **P27**, **P28** — the home must be able to account for itself |
| Retention **ceiling** | [../architecture/privacy.md](../architecture/privacy.md) — minimum necessary data |

**Where a floor and a ceiling conflict, privacy governs, and the resulting limitation on
explainability is itself recorded.** **DL-47 makes retention mandatory per governed record class**,
declared inside each lifecycle rather than in a central matrix, with **External History Retention as
the ceiling** and **four structural floors that survive any configured window** — Tombstones,
consent-lifecycle records, held records, and the versions required to keep a held Decision Trace
explainable. **Operational Trust owns no central purge and no retention registry**; each
responsibility enforces retention over its own records. The remaining numeric values are household
configuration — **DL-137** (OD-05, closed) confirms Explainability's own values carry no independent
architectural floor or ceiling beyond this general rule; **OD-26** and **OD-49** remain open.

### Preservation Hold (DL-132)

**Accepted 2026-11-05 (Issue #85, formal acceptance review PASS).** Resolves **OD-39** in full, except
deletion-versus-preservation precedence, explicitly **OD-36**'s own. Full decision:
[../architecture/adr-preservation-hold-governance.md](../architecture/adr-preservation-hold-governance.md).

**Operational Trust authorises Preservation Holds.** It determines who may create, review, and
release a hold; governs hold visibility; governs conflict with deletion; and governs duration and
review. **Operational Trust does not enforce holds centrally.** Each responsibility enforces holds
over its own records. **There is no central preservation-hold enforcer.**

**Placement, review, and release are each an independent, household-configured authorisation**,
expressed through **DL-71**'s existing Named Person / Role-Authority-Class Intended Audience
Specification forms — the same mechanism **DL-109** (above) already confirmed as the accepted way to
configure "a more capable or trusted configuration role," and the same forms **DL-97** already reused
for escalation accountability. **No parallel Preservation Hold identity/role system is invented.**
Placement authority never implies review or release authority; a household may name the same Person/
Role for all three, or different ones. None of the following is, by itself, a sufficient basis for
any of the three: being a resident; being Household; holding an Owner-role Person record; holding the
native Home Assistant administrator flag alone (**DL-109**); controlling the underlying device; being
able to see the underlying data; managing the affected Asset; being the Subject the records describe;
or holding Explainability/Historical-Retrieval access. **Record access never implies hold authority.**

**Placement and release are each Governance-class (DL-76): Required Identity Band Very High, Required
Confirmation Strength Strong.** No new Identity Band or Confirmation Strength is invented for holds.
Where the required band/strength cannot be verified, **DL-40**'s existing `Unavailable` outcome governs
— refused, never silently downgraded. A review that continues or narrows a hold is likewise
Governance-class under the same defaults.

**No HTBW-wide numeric default duration or review interval exists** (restating **DL-97**'s identical
refusal for escalation timing). Every active hold carries an explicit, placer-set review-due time,
status, stated purpose, authorised placer, review history, and release status. **A missed review
fails safe toward preservation**: ACTIVE → REVIEW DUE → OVERDUE → RENEWED/CONTINUED → RELEASED. An
overdue hold remains preserving and is reported through existing governed Communication, remaining
visible/explainable for as long as it is outstanding — never silently released, never silently
permanent. Review reminders reuse the existing Stewardship "incomplete obligation is notification, not
automatic escalation" pattern (`stewardship.md`) without transferring hold ownership to Stewardship.

**Release does not erase hold history** (who placed it, when, stated purpose, scope, review history,
releaser, reason, time — **DL-47** unchanged) **and release is not immediate deletion**; it removes the
retention floor and returns the records to normal retention/**OD-36** governance.

**Hold existence is itself governed information**, evaluated through this section's own existing
disclosure architecture (above), never a separate model. No universal rule is invented that a data
subject must always, or must never, be proactively notified that their records are held — it is
evaluated case by case exactly as any other sensitive fact about them.

A hold must be discoverable, attributable, bounded or periodically reviewed, independent of normal
visibility permissions, and explainable. **A hold does not automatically increase visibility.** A
hold cannot preserve raw biometric internals or raw voice samples, because those were never stored.
**Any purge/truncation/archival-deletion mechanism governing hold-eligible governed records must
discover and consult hold status before discarding a record; a fixed-size bound whose eviction step
cannot evaluate a hold is not an acceptable retention mechanism for such records.** Home Assistant
Recorder offers no native per-record hold exemption; where only ephemeral native history exists with
no corresponding governed record, a hold may be unimplementable for that specific evidence, stated
honestly rather than claimed.

### Deletion versus preservation (DL-133)

**Accepted 2026-11-05 (Issue #82, formal acceptance review PASS).** Resolves **OD-36** in full. Full
decision: [../architecture/adr-deletion-versus-preservation-reconciliation.md](../architecture/adr-deletion-versus-preservation-reconciliation.md).

**Neither "preservation always prevails" nor "deletion always prevails" is adopted.** A collision
between a valid deletion/erasure/consent-withdrawal obligation and a valid Preservation Hold or
retention floor becomes a **governed conflict**, producing exactly one outcome.

**Preservation/Deletion Conflict-Resolution Authority is a fourth, independently configured
authorisation**, alongside Hold placement/review/release (above) — the same **DL-71** Named
Person/Role-Authority-Class mechanism, configured per **DL-109**, evaluated as Governance-class
(**DL-76**: Very High / Strong). **The Person who placed a Hold does not automatically gain authority
to decide that another Person's deletion request loses**; none of the four Hold/conflict
authorisations is inferred from another.

The conflict is resolved at the **lowest practical level** — the record, the governed Subject-record
relationship, or the specific deletion obligation — never globally per record class or uniformly per
Hold. A required **minimization sequence** precedes any full-payload preservation: delete the payload
and keep only Tombstone/consent-lifecycle/Hold-lifecycle metadata where the preservation purpose
survives that; otherwise reduce identifying content where the purpose survives reduction; otherwise a
reduced governed record; only where the actual payload is necessary for the valid Hold's purpose does
it remain (generalising **DL-56**'s accepted biometric/consent pattern, not universalising it beyond
cases where it actually applies).

**Payload retained solely because of the conflict is restricted to the stated preservation purpose** —
restating the already-accepted purpose-bound-never-blanket authorization principle (**DL-93**), never a
new access-control model — and is unavailable for ordinary use, unrelated reasoning (including **Home
Steward**), personalization, Historical Retrieval, training, analytics, broader disclosure,
correlation, or unrelated automation.

A deletion obligation that cannot immediately be fulfilled becomes a **governed pending-cleanup
obligation** (restating **DL-45** unchanged) — never reported deleted while payload remains, never
lost; **Hold release makes it automatically actionable again**, so the Person is never required to
repeat the request. A Hold placed **after** a deletion request may affect it only with explicit
Conflict-Resolution-Authority approval; ordinary Hold-placement authority alone never suffices, and
chronology is recorded. Where deletion prevails, the existing Tombstone requirement (above, and
`temporal-record.md`) applies unchanged; where preservation temporarily prevails, no Tombstone falsely
claims deletion.

Whether a hold may override an authorised deletion request, and reconciliation of deletion and export
obligations with retention floors and holds, is **resolved as DL-133 (OD-36), above.**

### Evidence Package authority (DL-135)

**Accepted 2026-11-05 (Issue #86, formal acceptance review PASS).** Resolves **OD-40** in full. Full
decision: [../architecture/adr-evidence-package-governance.md](../architecture/adr-evidence-package-governance.md).

An Evidence Package begins as an on-demand projection; it becomes durable **Managed Content**
(**DL-44**) only through an explicit, separately authorized materialization request. **Assembly,
materialization, recipient authorization, and transport are four distinct governed operations**,
reusing this model's existing Action-Risk Classes and the **DL-71**/**DL-109** configured-authority
mechanism — no parallel role model is invented:

- **Assembly** (constructing/viewing a projection, no durable artifact) is **Disclosure**-class at the
  existing default (Moderate / Verbal).
- **Materialization** (creating durable Managed Content) is **Disclosure**-class with a **capability-
  specific override** to **Authenticated** confirmation — reusing this model's own already-accepted
  Capability-Default → HTBW-Default → Household-Override tiering, not a new risk class: a materialized
  artifact outlives the moment of disclosure and is retrievable later without re-asking, justifying the
  stronger confirmation tier within the same class.
- **External recipient/export** (the package leaves HTBW governance) is **Governance**-class (Very
  High / Strong) — matching this class's own test most precisely (an evidentiary-adjacent artifact
  permanently leaving governed control), mirroring **DL-132**'s treatment of Hold placement/release.

**Materialization creates no new disclosure authority.** Information not otherwise disclosable to a
recipient does not become disclosable merely because it was placed in a package; recipient-aware
inclusion precedes materialization/export for external recipients rather than assembling a full
household package and relying on a recipient not to view protected portions. **Preservation Hold
authority never implies package authority**, and materializing a package never automatically places a
Hold on its sources. **DL-133** restricted-use status on an included source survives materialization
unchanged. **Media visibility and storage reachability remain non-authorization** (**DL-44**,
unchanged); anonymous public/"share with anyone with a link" transport is never generated absent an
independently accepted equivalent control.

**Governing Parent and lifecycle** are Foundation's and the owning responsibility's, not Operational
Trust's: see `temporal-record.md`'s *Evidence Package* section and
[adr-evidence-package-governance.md](../architecture/adr-evidence-package-governance.md).

### Portability and Erasure authority (DL-136)

**Accepted 2026-11-05 (Issue #78, formal acceptance review PASS).** Resolves **OD-09** in full. Full
decision: [../architecture/adr-data-portability-and-erasure-mechanics.md](../architecture/adr-data-portability-and-erasure-mechanics.md).

**A Portability Export is a disclosure**, evaluated exactly as any other disclosure (**DL-34**), never
merely authenticated. Authority is evaluated at request/assembly time, reusing **DL-71**'s existing
Intended-Audience-Specification forms to determine **who may request**, and **DL-76**'s Action-Risk
Classification plus its Capability-Default → HTBW-Default → Household-Override tiering — the identical
mechanism **DL-135** already established for Evidence Package — to determine **how strongly gated**
each operation is: **Assembly** is Disclosure-class (Moderate/Verbal, default); **Materialization**
(creating a **Transient Export Artifact**) is Disclosure-class with the same capability-specific
Authenticated-confirmation override already established for Evidence Package materialization;
**external recipient/transport** (the export leaves HTBW governance) is Governance-class (Very High/
Strong). **Requester authority ≠ recipient authority ≠ transport authority**, restated verbatim from
**DL-135**. No native Home Assistant administrator flag, by itself, grants portability authority over
another Person's data.

**Erasure remains fully distributed — no central Erasure responsibility, store, or service.** The
**overall orchestrated erasure request** (the household-facing act of asking to remove a Person's or
an Asset's data across every applicable responsibility) is itself a **Governance-class** action (Very
High/Strong), by direct analogy to **DL-132**'s Hold placement/release and **DL-133**'s Conflict-
Resolution Authority — both already Governance-class for the identical reason: an irreversible,
high-consequence governed action. This governs the **orchestrated request itself only**; each
responsibility's own already-accepted internal deletion authority (for example, **DL-56**'s
consent-withdrawal authority) continues unchanged and is never additionally gated by this requirement.
Every retention-floor/Preservation-Hold collision encountered during erasure is resolved exactly as
**DL-133** already requires — not reopened, not reinterpreted.

**A Person-scoped export never widens disclosure beyond this model's existing rules.** Field-level
redaction and withheld-by-policy markers apply exactly as `privacy.md` already states; **"Home" scope
is never a privacy override**; a Person's own contribution to another Person's Decision Trace is
minimized/restricted/Tombstoned exactly as **DL-133** requires, never used to rewrite history.

**Governing Parent, lifecycle, and the Temporal Portability Contract** are Foundation's and the owning
responsibility's, not Operational Trust's: see `temporal-record.md`'s *Portability Export* and
*Erasure* sections and
[adr-data-portability-and-erasure-mechanics.md](../architecture/adr-data-portability-and-erasure-mechanics.md).

### Explainability persistence and retention authority (DL-137)

**Accepted 2026-11-05 (Issue #77, formal acceptance review PASS; amended 2026-11-05, same day, by
targeted Owner clarification).** Resolves **OD-05** in full. Full decision:
[../architecture/adr-explainability-persistence-and-retention.md](../architecture/adr-explainability-persistence-and-retention.md).

**Answering an on-demand Explainability question is a governed evaluation**, authorized under the
existing Historical Retrieval and Access model (**DL-130**, above) — Disclosure-class by **DL-76**
default, no new authority mechanism. Every invocation produces its own new Explainability Record
(`on_demand_decision_trace` origin), never deduplicated against an earlier identical request.

**Retention is Operational Trust policy, fully household-configured — HTBW imposes no independent
numeric architectural floor or ceiling.** Once an Explainability Record is created, its ordinary
lifetime is governed entirely by the household-configured Explainability retention policy, reusing
**DL-122**'s enumerated-presets-plus-custom-override shape at Integration-default/Room-override scope.
**DL-76's Action-Risk Classes classify action consequence, not Explainability retention duration** — no
mapping between the two exists. A household-configured value of zero/disabled is not silently
overridden merely because it is zero, absent independently accepted authority requiring otherwise.
**A Person's consent-lifecycle duration is never inherited as a record's whole retention period** —
**DL-47**'s existing structural-floor separation governs instead.

**Persistence technology (SQLite) and Connected-Storage/Backup-growth boundaries** are Foundation's/
Connected Storage's, not Operational Trust's: see `decision-trace.md`'s *Persistence* section and
[connected-storage.md](../architecture/connected-storage.md).

### Communication retention authority (DL-138)

**Accepted 2026-11-05 (Issue #118, formal acceptance review PASS).** Resolves **OD-49** in full. Full
decision: [../architecture/adr-communication-retention-governance.md](../architecture/adr-communication-retention-governance.md).

**Communication Content and Communication Metadata are two separate, independently
household-configured retention policies** — Operational Trust owns the configuration surface
(**DL-122**'s preset-plus-custom-override shape, Integration-default/Room-override scope) for each,
never a single combined duration. **HTBW imposes no independent numeric architectural floor or
ceiling** on either class, applying the corrected **DL-137** philosophy unchanged. **DL-78** Category
and **DL-77** Urgency remain downstream inputs to disclosure/audience/interruption, never automatic
retention-duration determinants; an optional per-Category override reuses the identical configuration
surface.

**Retained Communication Metadata remains fully subject to existing disclosure/privacy architecture**
(**DL-34**) — never treated as non-private merely because Content has expired or is absent.

**An ordinary or on-demand Explainability reference to a Communication never extends or resets its
retention** — restating **DL-47**'s holding-rule minimization and amended **DL-137**'s always-new-
on-demand-record rule, applied to Communication specifically: only a valid Preservation Hold
(**DL-132**) may preserve Content genuinely required to keep a held Explainability Record explainable,
and only under the Hold's own rules, never as a rewrite of the Communication's own configured
retention.

### Historical visibility

Visibility policy applies to historical records exactly as it applies to current ones. Presence
history, session history, and Decision Trace history remain among the most sensitive household data,
and *withheld by policy* must remain distinguishable from *no longer retained* and from *nothing
happened*.

### Not a legal instrument

**Preservation Hold, Evidence Package, and deletion/preservation conflict resolution are HTBW
architectural terms. They are not claims of legal effect.** See
[../architecture/privacy.md](../architecture/privacy.md).


---

## Representative scenarios

- [../scenarios/nighttime-suppression.md](../scenarios/nighttime-suppression.md)
- [../scenarios/multi-person-conflict.md](../scenarios/multi-person-conflict.md)
- [../scenarios/why-did-this-happen.md](../scenarios/why-did-this-happen.md)

## Open decisions

| ID | Question |
|---|---|
| OD-04 | **Closed — DL-126.** Policy precedence is four operations (Candidate Value/Preference Resolution, Authority/Policy Ceiling Evaluation, Current Explicit Request, Competing-Communication Ordering), never one undifferentiated ladder. Most-restrictive combination across scopes is precise: `prohibited` > `undecidable` > cumulative confirmation/escalation (never substituted for one another) > `permitted`. Mode, capability, and operation are applicability/condition dimensions, never scopes; Person is dual in kind (Policy vs. Preference), never dual in precedence; a Person preference never becomes permission |
| OD-05 | **Closed — DL-137** (amended 2026-11-05, targeted Owner clarification). Explainability Persistence, Origins, and Retention — retention is fully household-configured, no independent architectural floor or ceiling, no DL-76-to-duration mapping; on-demand Explainability requests authorized as Disclosure-class, each invocation its own governed evaluation |
| OD-06 | Consent user experience |
| OD-08 | **Resolved** as **DL-39** and **DL-40**. Four Identity bands, `None` as a Trust requirement, threshold ownership, Address by Name, operation-scoped confirmation, and the **Required Confirmation Strength** class set. Per-class defaults are configuration, resolved as **DL-76** |
| OD-09 | **Closed — DL-136.** Data Portability and Erasure Mechanics — Portability Export authority (Assembly/Materialization/External-transport mapped onto DL-76), orchestrated-erasure-request Governance-class authority by analogy to DL-132/DL-133, each responsibility's own existing deletion authority unchanged |
| OD-28 | **Closed — DL-123.** Learned-Policy Promotion Lifecycle: Concierge formulates and presents the Suggestion (an ordinary Communication); acceptance requires at minimum Authenticated Confirmation Strength (this document's "permission changes" floor) and resolves eligibility through the Suggestion's own DL-71 Audience Specification; pause suspends, revocation terminates, the autonomy permission alone; "forgotten" is replaced by Revocation/Preference deletion/source-evidence expiration |
| OD-33 | **Closed — DL-43, DL-46, DL-47.** Retention is declared inside every governed record and artifact lifecycle; remaining values are **DL-137** (OD-05, closed), **OD-26**, **OD-49** |
| OD-35 | **Closed — DL-130.** Assist/Conversation is the sole historical-retrieval surface, classified before assembly into ordinary retrieval versus Person/actor reconstruction; the nine existing Explainability scopes remain the complete query model; `caretaker-of` (**DL-49**) and **DL-71**'s five Intended Audience Specification forms are reused unchanged for Subject Authorization; current-location and historical-movement access are two independently configurable Disclosure-Risk-Class capabilities, never one setting; refusal and gap semantics reuse existing vocabulary throughout |
| OD-36 | **Closed — DL-133.** Reconciliation of deletion and export obligations with retention floors and Preservation Holds |
| OD-39 | **Closed — DL-132.** Preservation Hold authority, duration, review, release, scope, disclosure, and enforcement. Conflict with deletion is **DL-133** |
| OD-40 | **Closed — DL-135.** Evidence Package assembly, transport, integrity representation, and audience |
| OD-45 | **Resolved as DL-96.** Acknowledgement is an explicit, Communication-specific responsive act by an identified, in-audience Person; attribution reuses this document's existing Required Identity Band machinery (**DL-36**, **DL-39**) unchanged, no new scale; unacknowledged delivery remains `unknown`, never failure |
| OD-46 | **Resolved as DL-77.** Urgency is a fixed, cumulative four-level entitlement ladder, formally independent of Action-Risk Classification (**DL-76**), never overriding audience, privacy, consent, disclosure, identity, authority, or precedence (**OD-04**) |
| OD-66 | **Resolved as DL-118.** Delegation Boundary for External Adaptive Behaviour — External Decision Authority is a new autonomy-model scope, not a new policy type; declaration is explicit only, never inferred; Type-2 (unmediated) delegation is constitutionally capped at Convenience/Disclosure Risk Classes; the delegated act is a Domain Event (**DL-73**), never its own Decision Trace |
| OD-49 | **Closed — DL-138.** Communication Retention Governance — Content/Metadata classified separately, two independent household-configured retention policies, no independent architectural floor/ceiling (corrected DL-137 philosophy), Category/Urgency never automatically dictate duration, Explainability reference never extends/resets retention |
| OD-51 | **Resolved as DL-76.** Action-Risk Class enumeration (Convenience, Disclosure, Financial, Safety, Security, Governance) and per-class Required Identity Band / Confirmation Strength / Address by Name / Presentation Threshold defaults; household and object-specific override model; interruption confirmed as a separate axis (**DL-77**) |
| OD-52 | **Closed — DL-71.** Five Intended Audience Specification forms accepted; relationship-based resolution requires a **DL-57** Delegated Access Grant for actual authorization; Guest fallback and Copy Settings From Person are Person Setup conveniences, not new authority models |
| OD-53 | **Resolved as DL-78.** Communication Category is a closed, seven-value, content-domain enumeration (Stewardship, Security, Care, Environment, Experience, System, Safety), structurally separate from Urgency, Operation Type, and Action-Risk Classification; Operational Trust Category admissibility rejected |
| OD-56 | **Resolved as DL-79.** Non-life-safety acknowledgement (one-time, authenticated-Administrator), certified-device deference, evidence-quality-proportionate conclusions, Investigation Needed, temporal provenance, and the framework-wide evidence chain; no Safety-specific audience, Urgency, or caretaker model |
| OD-57 | **Resolved as DL-94.** Indication, the Room-Delivery Authorization Challenge, and message-scoped Room-Delivery Authorization formally separated; a new Room-Delivery Audience Preference governs Room-delivery eligibility by Urgency level and Household/Individual/Guest audience permission |
| OD-92 | **Resolved as DL-109.** No general configuration-authority tier model; the proposed four-tier model is rejected as redundant with, or conflating, this model's existing Action-Risk Classification, consent, and confirmation-strength architecture; a non-binding, derived resident-facing descriptor is permitted. See "Configuration Authority Composition (DL-109)," above |
| OD-95 | **Resolved as DL-119.** Home Production (HA-Prod) Trust Boundary Definition — Operational Trust owns the admission decision, Foundation types/holds the resource reference; membership is network/host/process-independent and requires an explicit, Foundation-referenced, Operational-Trust-owned admission record. See "Home Production (HA-Prod) Trust-Boundary Admission (DL-119)," above |

## Related documents

- [person-and-identity.md](person-and-identity.md)
- [truth.md](truth.md)
- [decision-trace.md](decision-trace.md)
- [temporal-record.md](temporal-record.md)
- [communication.md](communication.md)
- [../architecture/behavioral-governance.md](../architecture/behavioral-governance.md)
- [../architecture/privacy.md](../architecture/privacy.md)
- [../contracts/operational-trust-contract.md](../contracts/operational-trust-contract.md)
- [../architecture/adr-explainability-presentation-and-assist-interaction-path.md](../architecture/adr-explainability-presentation-and-assist-interaction-path.md)
  (**DL-140**)
- [../architecture/adr-voiceprint-gallery-structure-under-channel-diversity.md](../architecture/adr-voiceprint-gallery-structure-under-channel-diversity.md)
  (**DL-144**)
