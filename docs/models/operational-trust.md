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
| Room | Nighttime restrictions, child-safe rooms, no-media rooms |
| Person | Child safety, guest limitation, caretaker elevation |
| Asset | Safety-critical devices, irreplaceable assets |
| Relationship | Caretaker-of, owner-of elevation |
| Experience class | Media may be suppressed while care escalations are not |
| Action-risk class | Locks, garage doors, and heat sources require higher confidence |

Precedence within a scope, and the exact global priority order across scopes, is recorded in
[../architecture/behavioral-governance.md](../architecture/behavioral-governance.md) and remains open
decision **OD-04**.

**Threshold resolution introduces no new precedence order.** A presentation threshold, a capability
requirement, and a confirmation requirement are ordinary policy statements evaluated in the scopes
above, under the ceiling rule. A constitutional prohibition is never overridden by any of them; a
narrower scope may restrict but never silently relax a governing ceiling; and whether a Person may
relax a household setting is itself a policy. **A Person preference is never a permission.** **OD-04
is unchanged.**

---

## Identity confidence and action risk

Authority requirements scale with consequence.

| Action risk | Example | Identity requirement |
|---|---|---|
| Benign | Turn on a lamp in an occupied room | May proceed with unknown identity, per policy |
| Personal | Play *my* playlist | Requires a resolved identity |
| Sensitive | Read a calendar or message | Requires a resolved identity above threshold |
| Safety-critical | Unlock a door, open a garage, control a heat source | Requires a high-confidence identity and may require confirmation regardless |

Numerical thresholds are policy, not architecture. Risk-class enumeration and defaults remain
**OD-51**.

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

Defaults per capability and per risk class are **configuration**, resolved with **OD-51**'s risk-class
enumeration. They are not constitutional, and none is prescribed here.

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
  Risk-class enumeration and defaults remain **OD-51**.
- **Households define the requirements; Operational Trust applies them.** A household that wants
  greetings at a low bar and calendars at a high one is expressing a value, not misconfiguring.
- **Requirements are never lowered to reach a result.** Where confidence falls short, the governed
  responses are confirmation where policy offers it, a degraded outcome, or refusal — **never a
  relaxed threshold.**
- **Satisfying one capability's requirement satisfies no other.** The four consumers above are
  evaluated independently, every time.

Action-risk class enumeration and defaults remain **OD-51**. The confidence and confirmation strength
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

### Interrupting is a governed action

**Interruption is treated as an action-risk class**, using the mechanism above rather than a separate
cross-cutting mechanism. Speaking aloud in an occupied room, overriding a quiet hour, and raising a
time-critical Communication are all governed the same way a lock is governed.

> **A category must never function as a bypass.** A safety or critical classification is an
> Operational-Trust-granted **entitlement** — revocable, explainable, and traced. It is never a right
> that an originator confers upon itself by naming its own category.

Risk-class enumeration and defaults for interruption are open decision **OD-51**. Urgency
classification is **OD-46**.

### Urgency is granted, not asserted

An originator may **propose** an urgency. **Operational Trust determines it.** Urgency is orthogonal
to Category: Category describes what a Communication is about, Urgency describes what it may
interrupt. The two axes must never be merged. See
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

**These illustrate the policy's shape. They are not defaults.** Risk-class enumeration and defaults
remain **OD-51**; the Required Identity Band per class is **configuration** under **DL-39**.

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

The provider remains replaceable. Provider strategy is **OD-67**, and is neither closed nor prejudged
here.

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

Which class each capability, protected operation, and action-risk class requires is **configuration**,
resolved with **OD-51**'s enumeration. **Verbal** is not adequate on its own for permission changes,
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
configuration, held by **OD-05**, **OD-26**, and **OD-49**.

### Preservation Hold

**Operational Trust authorises Preservation Holds.** It determines who may create, review, and
release a hold; governs hold visibility; governs conflict with deletion; and governs duration and
review.

**Operational Trust does not enforce holds centrally.** Each responsibility enforces holds over its
own records. **There is no central preservation-hold enforcer.**

A hold must be discoverable, attributable, bounded or periodically reviewed, independent of normal
visibility permissions, and explainable. **A hold does not automatically increase visibility.** A
hold cannot preserve raw biometric internals or raw voice samples, because those were never stored.

Whether a hold may override an authorised deletion request is **OD-39**. Reconciliation of deletion
and export obligations with retention floors and holds is **OD-36**.

### Historical visibility

Visibility policy applies to historical records exactly as it applies to current ones. Presence
history, session history, and Decision Trace history remain among the most sensitive household data,
and *withheld by policy* must remain distinguishable from *no longer retained* and from *nothing
happened*.

### Not a legal instrument

**Preservation Hold and Evidence Package are HTBW architectural terms. They are not claims of legal
effect.** See [../architecture/privacy.md](../architecture/privacy.md).

---

## Representative scenarios

- [../scenarios/nighttime-suppression.md](../scenarios/nighttime-suppression.md)
- [../scenarios/multi-person-conflict.md](../scenarios/multi-person-conflict.md)
- [../scenarios/why-did-this-happen.md](../scenarios/why-did-this-happen.md)

## Open decisions

| ID | Question |
|---|---|
| OD-04 | Exact global priority order across policy scopes |
| OD-06 | Consent user experience |
| OD-08 | **Resolved** as **DL-39** and **DL-40**. Four Identity bands, `None` as a Trust requirement, threshold ownership, Address by Name, operation-scoped confirmation, and the **Required Confirmation Strength** class set. Per-class defaults are configuration, resolved with **OD-51** |
| OD-28 | How household policy acceptance of learned suggestions is captured and revoked |
| OD-33 | **Closed — DL-43, DL-46, DL-47.** Retention is declared inside every governed record and artifact lifecycle; remaining values are **OD-05**, **OD-26**, **OD-49** |
| OD-35 | Historical query surface and access |
| OD-36 | Reconciliation of deletion and export obligations with retention floors and Preservation Holds |
| OD-39 | Preservation Hold authority, duration, review, release, and conflict with deletion |
| OD-40 | Evidence Package assembly, transport, integrity representation, and audience |
| OD-45 | Acknowledgement semantics, and whether unacknowledged delivery is a failure |
| OD-46 | Urgency classification as an Operational Trust entitlement, and mapping to non-portable platform ladders |
| OD-49 | Communication retention floor and ceiling, with content and metadata classified separately |
| OD-51 | Interruption action-risk class enumeration and defaults |
| OD-52 | **Closed — DL-71.** Five Intended Audience Specification forms accepted; relationship-based resolution requires a **DL-57** Delegated Access Grant for actual authorization; Guest fallback and Copy Settings From Person are Person Setup conveniences, not new authority models |
| OD-53 | Communication category enumeration, and confirmation of the Category × Urgency separation |
| OD-56 | Safety-category scope, and whether HTBW may originate safety Communications at all |
| OD-57 | Indication versus content separation |

## Related documents

- [person-and-identity.md](person-and-identity.md)
- [truth.md](truth.md)
- [decision-trace.md](decision-trace.md)
- [temporal-record.md](temporal-record.md)
- [communication.md](communication.md)
- [../architecture/behavioral-governance.md](../architecture/behavioral-governance.md)
- [../architecture/privacy.md](../architecture/privacy.md)
- [../contracts/operational-trust-contract.md](../contracts/operational-trust-contract.md)
