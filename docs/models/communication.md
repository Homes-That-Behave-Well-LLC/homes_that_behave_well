# Communication

> **Document status: Active — Canonical model.**
> Owning responsibility: **Foundation** (definitional).
> Governed by **P31** and **P32**. Established by
> [../architecture/adr-resident-communication-and-delivery-separation.md](../architecture/adr-resident-communication-and-delivery-separation.md).
> Terminology: [glossary.md](glossary.md).

---

## Purpose

This model defines what a **Communication** is, how it differs from the act of delivering it, and how
its history is recorded.

Foundation defines this model. **Foundation does not own any Communication.** Any responsibility may
originate one; **Concierge** decides and records delivery.

**This model creates no new responsibility.** There is no Communication responsibility, no Messaging
responsibility, no Inbox responsibility, no central delivery owner, no central inbox owner, and no
second escalation ladder.

**This model creates no new temporal record kind.** Communication history is recorded using the
Change Records, Governed References, and Version Identity already defined in
[temporal-record.md](temporal-record.md).

---

## Question answered

> *What does the home need to convey, to whom, about what — and what happened when it tried?*

---

## The central separation

> **A Communication is a household interaction. A Delivery is an act of conveying it.**

| Concept | Meaning |
|---|---|
| **Communication** | The governed object. What must be conveyed, to whom, about what |
| **Delivery** | The act of conveying a Communication through a surface |
| **Delivery Attempt** | One bounded act of delivery to one surface, with its own outcome |
| **Delivery Surface** | A governed abstraction of a place through which delivery may occur |
| **Announcement** | A Delivery made **audibly to a shared surface**. An outcome, never an object |

A Communication may have zero, one, or many Delivery Attempts. It is not defined by any of them.

**A Communication is never a notification, a push message, an announcement, an indicator, an email,
or a spoken phrase.** Those are delivery outcomes. See **P31**.

---

## The Communication object

A Communication is a **small governed record with a mutable Current Projection and a history of
Change Records**. It is never a growing document.

### Required

| Field | Purpose |
|---|---|
| **Communication ID** | Without identity it cannot be referenced, superseded, held, or tombstoned |
| **Version Identity** | Required of every governed record by **P29** and **P30** |
| **Effective Time** | When the Communication became relevant |
| **Recorded Time** | When the home recorded it |
| **Provenance** | Which responsibility, through which evidence, at what confidence |
| **Originator reference** | A **Governed Reference** to the responsibility and to the exact version of the record that caused it |
| **Subject reference** | A **Governed Reference** to what it is about — an Asset, Room, Person, Obligation, or Fact version |
| **Intended Audience** | An audience **specification** — never a device or surface list |
| **Category** | What it is about. Proposed by the originator |
| **Urgency** | What it is entitled to interrupt. Determined by **Operational Trust** |
| **Significance reference** | A reference to Stewardship's significance, never a copied value |
| **Originating Context Reference** | A **Governed Reference** to the Fact versions that were true at origination |
| **Visibility Classification reference** | A reference to the Operational Trust classification, re-evaluated at each attempt |
| **Retention Classification** | Carries the retention **floor and ceiling** onto the record |
| **Lifecycle State** | The Current Projection — what state it is in now |
| **Supersedes / Superseded-by** | Governed References. Supersession is never inferred from ordering |
| **Expiry specification reference** | A reference to the governing policy, never a copied duration |
| **Minimal rendering projection** | The immutable human-readable form. Permitted by **P30**; must not become a wholesale copy |
| **Explanation references** | Governed References to the Decision Traces that created or suppressed it |

### Prohibited

> **These three fields must never exist on a Communication.**

| Prohibited | Reason |
|---|---|
| A stored **context** value | Context is resolved by Truth and Room Context **at delivery time**. A stored context is a frozen snapshot that will silently become wrong. Use the Originating Context Reference |
| A stored resolved **visibility** value | Visibility is Operational Trust's and is re-evaluated at **each** Delivery Attempt. A stored value would survive a policy revocation — the **P30** failure mode |
| An embedded **delivery history** array | The embedded-audit-array defect recorded in [../architecture/adr-temporal-record-model.md](../architecture/adr-temporal-record-model.md). Delivery history is Change Records referencing the Communication by Version Identity |

---

## Category and Urgency

**These are orthogonal axes and must never be merged.**

### Category — what it is about

Proposed by the originator. Representative categories:

| Category | Representative subject |
|---|---|
| Informational | A package was delivered; a weather change |
| Obligation | Medication due; collection day; filter replacement |
| Stewardship | Humidity is outside the safe range for a sensitive asset; service is due |
| Condition | A door is unlocked; the garage is open |
| Safety | Water, smoke, or carbon monoxide detected |
| Interaction | The home needs an answer before it can proceed |
| Governance | An action was refused; consent is required; a limitation is being reported |

The exact enumeration is open decision **OD-53**.

### Urgency — what it may interrupt (DL-77)

**Urgency is the maximum interruption entitlement Operational Trust grants to a Communication, never a
property the originator asserts.** The originator may propose an Urgency level; Operational Trust
determines and grants it.

> **A category must never function as a bypass.** If a category could grant interruption rights by
> virtue of its name, an originator could authorise itself, and **P32** would be decorative.

#### The canonical ladder

Exactly four levels, fixed and **cumulative**. Each is a **maximum permitted interruption, never a
mandatory delivery behaviour** — Concierge may always choose less.

| Level | Entitlement adds |
|---|---|
| **No Interruption** | Retained; presented when context permits; may not interrupt a current activity, active Mode, protected time, or a sleeping person |
| **Interrupt Current Activity** | May interrupt a current activity or active Mode when other governance permits; may not override protected time or wake/disturb merely by this level |
| **Override Protected Time** | May override quiet hours or another governed protected-time condition when other governance permits; may not wake/disturb merely by this level |
| **Wake or Disturb** | May wake or deliberately disturb the intended audience when all other governance permits |

#### Six distinct values, never collapsed into one field

| Value | Meaning |
|---|---|
| **Originator Proposal** | The optional level the originator proposes. Advisory only; its absence is itself recorded |
| **Canonical HTBW Recommendation** | The current baseline recommendation for the governed scenario or scope |
| **Learned Household Recommendation** | A Suggestion-stage proposal (existing **P26**/**DL-21** ladder, **OD-28**) derived from repeated accepted overrides — never silently applied |
| **Configured Value** | The value currently accepted for the applicable scope |
| **Household Override State** | Whether the configured value differs from the recommendation, with provenance |
| **Granted Runtime Entitlement** | What Operational Trust actually grants, after evaluating policy and current facts |

#### Relationship to Action-Risk Classification (DL-76)

Urgency and Action-Risk Classification are **independent models**. Operational Trust consumes the
applicable Risk Class, thresholds, and configuration as one input among several — **there is no
required one-to-one mapping**, and two circumstances sharing a Risk Class may receive different
Urgency because current facts, context, audience, or configuration differ.

#### Urgency may be reevaluated

Operational Trust reevaluates the granted entitlement when material inputs change. **A reevaluation is
a new Operational Trust determination — never automatically retry, and never automatically
escalation.** Where the entitlement decreases, pending delivery immediately respects the new
entitlement, completed delivery remains historical fact, and any queued delivery or retry requiring
the former entitlement is cancelled or replanned.

#### Precedence remains OD-04's

Urgency grants interruption **eligibility**; it does not order Communications that are otherwise
eligible. **OD-04 owns relative precedence**, including Communications that share one Urgency level.

Urgency classification is resolved as **DL-77**. Its relationship to action-risk classification is
**DL-76**.

### Why the axes are separate

*Package delivered* and *weather update* are about different things and interrupt identically.
*Alert* and *critical alert* are about the same kind of thing and differ only in interruption
entitlement. Merging the axes makes the taxonomy the permission model.

### Advisory

**Advisory is a Stewardship judgement**, not a Communication category. An Advisory suggests what
could be improved; an Alert indicates that something is wrong. See
[../patterns/advisory-patterns.md](../patterns/advisory-patterns.md). The Communication conveying an
advisory carries the **stewardship** category.

---

## Intended Audience

An audience is expressed as a **specification**, resolved to surfaces only at delivery.

**Five specification forms are accepted (DL-71, resolved OD-52).** Each carries a canonical name, an
owner, a resolution source, an Assertion Purpose where the form is evidence-based, a resolution time,
an uncertainty outcome, a no-recipient outcome, a too-broad outcome, mandatory Operational Trust
evaluation, and Decision Trace evidence.

| Form | Meaning | Resolution source | Assertion Purpose |
|---|---|---|---|
| **Named Person** | One identified Person | Direct reference to the Person object | None — identifying the object is not evidence-based |
| **Role / Authority Class** | A named position or stated authority, unscoped to any subject — resident, owner, child, guest, service provider | Operational Trust, against currently eligible Persons holding it | None (a configuration/authority lookup) |
| **Relationship-based** | A predicate scoped to a specific Subject — a Person, Pet, or Asset — for example "Caretaker of Maisey" | Stewardship's current relationship assignment records (`caretaker-of`), never presence or identity evidence | None — a governed configuration lookup, cross-checked against a **DL-57** Delegated Access Grant for actual authorization |
| **Anyone Present With Authority** | The first suitably authorised Person contextually present — including the plain "whoever is home" case | Truth (Room or Household Presence) crossed with Operational Trust's current authority evaluation | Household or Room Presence |
| **Household** | All residents | Foundation's Person roster | None |

> **"Household" never means "everyone in earshot."** Audience is a specification of who the
> Communication is *for*. Who can *perceive* a surface is a separate question, answered by Truth and
> governed by **P32**.

**"Role" and "Relationship-based" are not the same mechanism, even where they share a word.** "Adult"
or "child" is a bare Role — a household-wide authority classification, unscoped to any subject.
"Caretaker of Maisey" is Relationship-based — scoped to a specific Subject, resolved through a
governed relationship record, never through generic authority classification. The existing glossary
**Caretaker** entry already carries both meanings; this table makes the distinction explicit rather
than leaving it ambiguous.

**Guests are never an audience by default**, and guest presence constrains delivery to every
audience. See [../architecture/privacy.md](../architecture/privacy.md).

### Resolution timing (DL-71)

**The original specification is fixed at origination and is never rewritten.** The *resolved
recipient set* is re-evaluated at each Delivery Attempt for a dynamic form (Relationship-based,
Anyone Present With Authority) — extending the existing principle that visibility is never stored
resolved (see *Multi-person communication*, below) from audience composition to specification
resolution. A Named Person or Household specification needs no re-resolution of *who* it names, but
Operational Trust's authorization is still evaluated fresh at every attempt, unchanged. **A prior
Delivery Attempt record is never rewritten by a later relationship change.** Escalation (**OD-22**)
creates or records a new specification; it never silently mutates the original.

### Resolved to nobody, or too broadly (DL-71)

Where a specification resolves to **no current Person**, the Communication is never silently
discarded, never redirected to a convenient Person, and is never sent broadly by default. Stewardship
records the missing accountable relationship as an accountability gap exactly as already accepted
(see [stewardship.md](stewardship.md)); a Repairs projection follows only where **DL-65**'s own
configuration-invariant test is independently satisfied.

Where a specification resolves to **more Persons than expected** — several current caretakers, several
Persons "present with authority" — this is **not itself an error**. Operational Trust evaluates content
sensitivity, current identity confidence, audience composition, Authorized Recipient status, and
Delivery Surface capability exactly as already accepted (**DL-34**, **DL-53**); where the audience
cannot be safely determined, delivery degrades, the Communication is preserved, and disclosure is
never broadened.

The audience specification model is resolved — **DL-71**, closing **OD-52**.

---

## Audience composition

**Intended Audience says who a Communication is *for*. Audience composition says who may be able to
*perceive* it.** They are different questions, and conflating them is precisely what **P32** forbids.

Audience composition answers: *who may be able to perceive this content through the proposed delivery
surface?* It is a governed **input to disclosure**, evaluated by Operational Trust. It applies to a
solicited answer just as it applies to an unprompted announcement.

| Term | The question it answers |
|---|---|
| **Requestor** | Whose request is this? An Interaction Initiator assertion, for a Person or an Unknown Person |
| **Speaker** | Who uttered it? A Speaker Attribution assertion, for a Person or an Unknown Person |
| **Present Person** | Who is likely physically here? A Room Presence assertion |
| **Potential Listener** | Who may perceive the proposed delivery? |
| **Authorized Recipient** | Whom does Operational Trust permit to receive this content? |
| **Delivery Target** | Which surface, device, application, Room, or endpoint was selected? |

**These must never be collapsed into a single audience field.** A requestor may be authorised while
another potential listener is not. A speaker may not be the authenticated application user. A present
Person may not be a listener when delivery is private. A Delivery Target may be a phone rather than
the Room the request arrived in.

### Composition states

| State | Meaning |
|---|---|
| Known Person present | A known Person, with a purpose-specific confidence |
| Known non-resident Person present | A specifically configured non-resident |
| Unknown Person likely present | Someone is supported; nobody is identified |
| Multiple known Persons | More than one identified potential listener |
| Unresolved plurality | One or more unidentified people; the count is not established |
| No additional listener supported | No evidence of anyone else — **not proof of solitude** |
| Audience unknown | Composition could not be established |
| Audience detection unavailable | The evidence needed to evaluate composition could not be obtained |

> **Audience composition must retain its uncertainty.** It is not required — and not permitted — to
> identify every listener in order to be useful.

Four inferences are prohibited:

- **Room occupancy count is not audience identity.** Occupancy says how many, never who.
- **A detected phone is not proof that its owner can hear the response.** A device is not an ear.
- **Absence of detected evidence is not proof that nobody else is present.** *No additional listener
  supported* and *nobody else is here* are different statements, and the second is not available.
- **Audience composition identifies nobody.** It consumes accepted identity assertions and presence
  Facts. **It is not a second identity-fusion process**, and it produces no assertion of its own.

Composition carries forward, unaltered, the assertion purpose, the known or unknown state, the
confidence band, freshness, Room context, the supporting evidence references, the residual
uncertainty, and whether detection was available at all.

### Private delivery

Where content should not be conveyed aloud, Concierge may offer an authorised alternative: a resident
application surface on an associated device, an Inbox projection restricted to the authorised
audience, a private dashboard, a content-free indication, or a confirmation asking whether audible
delivery is still wanted.

> **A surface is not private because it is a phone.**

Operational Trust evaluates target association, authenticated user, governed device binding, delivery
capability, audience restriction, content classification, and applicable policy before any surface is
treated as private. **Extended, not replaced (DL-72):** the surface must also have sufficient
Potential Perceptibility evidence for the attempted delivery (**DL-53**), be currently available, be
**not known to be shared**, be **not merely nearby** to the intended Person, carry a currently
governed device-Person association, and support the required Presentation Outcome (**DL-54**); the
selection must be explainable. **No platform capability to detect lock-screen state, current physical
possession, or shared-device status is claimed** — where the platform cannot establish privacy, the
uncertainty is retained and the next degradation step applies (**DL-29**); this remains an **OD-43**
implementation-time verification item. A Person-associated mobile application, wearable, or
authenticated personal dashboard is only *potentially* private and must pass the full test; a shared
household tablet, shared phone, television, Room display, kitchen dashboard, or Room speaker is
**never** automatically private. Surface capability and perceptibility are **OD-43**; the audience
specification model is **DL-71** (resolved **OD-52**); the policy applied when composition is
uncertain is **DL-72** (resolved **OD-71**), immediately below.

Communication remains the object. Delivery remains separate. **Concierge orchestrates the outcome and
owns none of the authority.** See [operational-trust.md](operational-trust.md).

### System-Initiated Communication versus Person-Requested Response (DL-72)

**A System-Initiated Communication** is one HTBW originates without a current explicit request — a
medication reminder, new private Mail, a Calendar reminder, a Stewardship warning, a financial or
security notice. **A Person-Requested Response** answers a Person's current explicit request — *"What
is on my Calendar?"*, *"Read my Mail,"* *"Tell me about the Piano,"* *"Send that to my phone."* The
two are not treated identically.

**An explicit request is evidence of willingness to receive an authorized response through the
current interaction context. It is never unrestricted consent.** The presumption of willingness is
void where: the Person requests private delivery instead; a higher content, privacy, or Operational
Trust rule requires private delivery; the response would disclose another Person's information; the
response would reach a prohibited reconstruction (**DL-35**); requester authority or applicability
cannot be sufficiently established; or the current Delivery Surface cannot safely present the
response.

*"Read that here"* is evidence of willingness for the current interaction only — it is never
permission to disclose another Person's private content. *"Send that to my phone"* resolves the
**requestor's own** authorized private destination, never a convenient or nearby device.

### Default degradation order under audience uncertainty (DL-72, resolved OD-71)

For a **System-Initiated** Communication where audience composition cannot be safely established, the
accepted order — evaluated in sequence, not as a mandatory checklist of every step — is:

1. **Authorized private delivery** to each intended recipient's own configured destination, where
   available and qualified as private (above).
2. **Content-free Indication**, where its own audience evaluation and **OD-57**'s eventual
   mandatory-threshold rule permit it.
3. **A neutral confirmation or clarification challenge** that names no candidate, subject,
   relationship, or sensitive content, where a genuinely neutral form exists (**DL-37**).
4. **Deferral or refusal** of audible delivery, preserving the Communication for retry (**OD-54**) or
   escalation (**OD-22**).

**This is the privacy-preserving floor and applies even where no household configuration exists.** A
missing configuration must never result in audible private disclosure.

### A confirmation challenge is a Communication

When the home asks *"I think I am speaking with Tom. Can you confirm?"*, it is not merely running a
process — it is **conveying to everyone within earshot that it believes Tom is present**.

> **The question is a disclosure. It is audience-evaluated before it is asked.**

A confirmation challenge therefore carries an Intended Audience, an audience composition, a Delivery
Surface, and a disclosure decision like any other Communication (**DL-34**, **P32**). Naming a
candidate aloud, choosing a neutral challenge that names nobody, and redirecting the challenge to an
authorised private surface are **three different disclosure outcomes**, and the choice is Operational
Trust's.

**No wording is prescribed here.** The requirement is that the challenge is governed, not that it is
phrased in a particular way. Confirmation requirements, strength, scope, and outcomes belong to
[operational-trust.md](operational-trust.md); the policy applied when audience composition is
uncertain is **DL-72** (resolved **OD-71**).

**A neutral challenge is bounded by information class, not by prescribed wording (DL-72).** Under
audience uncertainty, it must never name a candidate Person, a private subject or resource, a
caretaker or other relationship, the sensitive action or content, or protected history. *"Would you
like that sent privately?"* and *"where would you like the response?"* illustrate a permitted form;
*"Tom, is that you?"*, *"should I send your medication reminder to your phone?"*, and *"are you
Maisey's caretaker?"* each illustrate a prohibited one.

### Content-free Indication discloses nothing about content (DL-72)

An Indication must never reveal the intended recipient's identity, the subject, the content, a
private relationship, a sensitive content class (medical, financial, security, Mail, Calendar), or
that a concealed Asset or Person-specific resource exists. *"There is a private notification
available"* illustrates a safe form; *"Tom, you have a medication reminder,"* *"someone has a medical
notice,"* and *"the caretaker of Maisey has a reminder"* each illustrate an unsafe one — each discloses
more than existence alone. The Indication itself remains a Communication and is audience-evaluated
before it is delivered. **Whether Indication is mandatory rather than merely available at a given
threshold remains OD-57's own question.**

### Named and neutral presentation

Speaking a Person's name is a disclosure, so **whether a response is named or neutral is an
Operational Trust outcome that Communication carries and Concierge renders**. The **Address by Name**
setting and its required current Identity band are Operational Trust's; Communication never sets
them, and never names a candidate on its own initiative.

| Condition | Presentation |
|---|---|
| The **current** assertion meets the required band **and** the audience permits the name | Named |
| The current assertion is below the required band | **Neutral** |
| Address by Name is disabled | **Neutral**, regardless of band |
| The assertion is `ambiguous`, `unknown`, `unavailable`, or `not required` | **Neutral**. No candidate is named |
| The name would disclose identity to an audience not authorised to receive it | **Neutral**, or a private surface is offered (**DL-34**) |

> **A neutral response is a correct response, not a degraded one.** It is never an apology, and it is
> never a refusal of the action.

The naming decision is made from the assertion current **at the time the response is generated**. A
name used in an earlier response confers no eligibility on the next one, and continuing Room occupancy
supplies none. See [person-and-identity.md](person-and-identity.md).

---

## Delivery

### Delivery Surface

A Delivery Surface is a **capability abstraction**, not a device and not a product.

A surface declares what it can convey, **to whom it is perceptible**, and whether it can attest that
something was presented. Perceptibility is the property **P32** depends on; format is not.

> **This model contains no surface catalogue.** Enumerating surfaces would re-couple the domain to
> transport, which is what **P31** forbids.

#### Capability dimensions (DL-53)

A Delivery Surface declares:

| Dimension | Answers |
|---|---|
| **Supported Modalities** | Audio, visual, text, and extensible future modalities |
| **Content Constraints** | Supported content forms and technical limits on successful delivery |
| **Interactivity Capability** | One-way, interactive, or conversational, and what response forms are supported |
| **Persistence Behavior** | Ephemeral, time-limited, persistent, or governed retrieval |
| **Recipient Acknowledgement Capability** | Whether the recipient can explicitly acknowledge, kept distinct from presentation attestation |
| **Presentation Attestation Capability** | Whether the surface can supply evidence that presentation occurred. Defaults to **Unsupported** |
| **Recipient Attribution Capability** | The degree to which the surface can supply evidence about who received, perceived, acknowledged, or interacted with a delivery |

The dimension set is **extensible** and is never a closed list of Home Assistant entity types,
domains, device classes, integration names, or physical devices.

#### Potential Perceptibility is declared, never privacy

A Delivery Surface declares **Potential Perceptibility** — who could potentially hear, see, read, or
otherwise perceive delivery through it (Room occupants, nearby people, an interacting person, an
authenticated session's person, remote viewers, or unknown/unresolved observers, where the canonical
model supports each). **A Delivery Surface never declares itself private.** Device type, integration
type, authentication, media-browser visibility, and a dashboard view's per-user `visible` setting are
each **evidence-insufficient claims of privacy** — the latter two are verified Home Assistant UI-tab
display toggles, not authorization or security controls (**DL-44**; `dashboards/views` `visible`
documentation, verified: *"this is only for the display of the tabs; the URL path is still
accessible"*). A portable surface receives **no automatic privacy classification** merely because it
moves.

Three questions stay separate and are never collapsed:

| Question | Answered by |
|---|---|
| **Potential Perceptibility** — who could perceive the delivery? | The Delivery Surface declaration plus current Truth evidence |
| **Recipient Attribution** — who does available evidence indicate is receiving it? | Truth, Identity, and the surface's declared Recipient Attribution Capability |
| **Disclosure Appropriateness** — is delivery here appropriate for this content and audience? | Operational Trust |

Authentication may supply strong recipient-attribution evidence. **Authentication does not make a
surface private.**

#### Split ownership (DL-53)

| Responsibility | Owns | Does not own |
|---|---|---|
| **Foundation** | The Delivery Surface capability model and declaration schema | Delivery decisions |
| **Integration** | Stable, verified technical characteristics and capabilities it actually exposes | Household values, perceptibility conclusions, privacy, or disclosure appropriateness |
| **Household** | Contextual perceptibility declarations and configuration a platform cannot authoritatively determine; may configure which evidence combinations satisfy a **Required Confirmation Strength** class (**DL-40**) within platform constraints | Canonical meanings of confirmation-strength classes |
| **Truth** | Current facts bearing on perceptibility and context (Room Context, occupancy, presence, authentication state, and other authoritative facts) | Delivery decisions; declaring a surface private |
| **Identity** | Identity evidence and confidence contributing to recipient attribution | Disclosure appropriateness |
| **Operational Trust** | Whether delivery is appropriate given audience, content sensitivity, perceptibility, attribution evidence, policy, and current evidence — the disclosure-risk determination | The Delivery Surface model |
| **Concierge** | Delivery Target selection and the governed delivery attempt | Perceptibility truth, identity determination, or the Delivery Surface model |

#### Fixed and portable surfaces (DL-53; coordinated with OD-73)

Fixed and portable surfaces both declare capabilities and Potential Perceptibility characteristics.
Current context is evaluated at delivery time against available governed evidence (Room Context,
occupancy, person presence, BLE association, authenticated person-scoped sessions, voice identity,
interaction continuity, household declarations, and other authoritative Truth evidence). Mobility may
be a characteristic relevant to that evaluation; it never turns dynamic Truth into static Delivery
Surface configuration.

**What DL-53 decides:** the capability model, its Potential Perceptibility declaration, and that a
portable surface receives no automatic privacy classification. **What remains OD-73's alone:** the
exact mechanism by which Room Context is resolved for an interaction originating from a surface that
is not bound to a Room. DL-53 consumes whatever OD-73 eventually accepts as one input among the Truth
evidence a portable surface's perceptibility evaluation draws on, and preempts none of OD-73's
alternatives.

#### Presentation attestation defaults (DL-53; enumeration remains OD-55)

**Presentation Attestation Capability defaults to Unsupported.** Where attestation is unsupported, or
where attestation evidence is absent, `Presented` is recorded as **unknown** — never inferred from
`Delivered`, and never decayed into *not presented*. Delivery attempted, technical delivery accepted,
content presented, content perceived, recipient acknowledged, and recipient attributed remain **six
distinct states**, and none is inferred from another without authoritative evidence. Which surface
classes can attest presentation, and on what evidence, remains **OD-55**.

#### Strict DL-41 dependency behaviour

Where a capability declares a dependency and that dependency is unavailable, the capability is
**unavailable**, the missing dependency is **named**, and no approximation or unsupported evidence is
substituted (**DL-41**). Where Recipient Attribution Capability depends on a named identity-evidence
source that is unavailable, the Decision Trace states that the capability or evidence is unavailable
**because that named dependency is unavailable** — never as a low-confidence result. An independently
declared alternative evidence source may still be evaluated on its own terms.

#### Delivery Surface suitability

Delivery Surface selection is a **communication-appropriateness decision constrained by disclosure
risk**, never a search for the apparently safest device. It weighs intended audience, content
sensitivity, communication outcome, supported modalities, content constraints, interactivity,
persistence, acknowledgement and presentation-attestation requirements, Recipient Attribution
requirements, Potential Perceptibility, current Truth, household preference and policy, and disclosure
risk. Broad perceptibility can be the **correct** choice for shared content — a television may be more
suitable than a phone for a household news item because it best matches the intended shared audience,
not because the television is public. **No fixed content-to-surface mapping is created.**

#### Disclosure-risk hierarchy and confirmation (DL-53; reuses DL-37, DL-40)

Where Operational Trust finds audience certainty, recipient attribution, or disclosure appropriateness
insufficient, the governed order is: confirm at the **Required Confirmation Strength** the protected
content or action requires (**DL-40**); if the current interaction cannot support that strength, move
confirmation to a surface or channel that can; if compliant confirmation is obtained, continue only
within its authorized scope; if confirmation is declined, unavailable, expired, or insufficient,
degrade to a compliant delivery or indication path; if none exists, fail safely and name the reason.

**A confirmation must meet or exceed the Required Confirmation Strength of what it protects** — this
restates **DL-40** and **DL-37** for the delivery-surface case rather than creating a second scale.
Evidence that only reaches `Verbal` can never authorize what requires `Authenticated` or `Strong`
(**DL-40**), exactly as a spoken *yes* remains inadequate for the operation classes **DL-37** already
names. Which mechanism satisfies which class remains deployment-verified configuration under **OD-51**;
Recipient Attribution Capability declares what evidence a surface **can** contribute toward satisfying
a class, never a class of its own.

### Indication and content are separate deliveries

A **content-free indication** asserts only that something is outstanding. It discloses nothing, and
is therefore permissible where content is not.

| Delivery | Discloses | Governed by |
|---|---|---|
| Indication | That something is outstanding | Permitted broadly; still subject to interruption authority |
| Content | What it says | Full **P32** evaluation against surface perceptibility |
| Retrieval | What it says, on request | Resident-initiated; returns to the ordinary exposure chain with identity asserted at retrieval |

> **Modelling indication and content as one act removes the safe degradation path and forces a
> choice between silence and disclosure.**

On a shared surface the indication is **aggregate and content-free**. A shared surface must never
enumerate whose Communications are waiting. Separation policy is open decision **OD-57**.

### Re-presentation

**A Communication has no location.** It cannot move, follow, or remain location-bound.
Location-boundness is a property of a Delivery Attempt.

Where a person moves and a Communication remains outstanding, Concierge may make a **new Delivery
Attempt** on a newly appropriate surface, re-evaluating **P32** against the **new** audience. Each
attempt is separately recorded.

**The Communication is never duplicated.** One object, many attempts.

Whether a resident wants this is a **Continuity** preference within the existing Follow-Me family.
Whether it is permitted is **Operational Trust**. Whether and where to attempt it is **Concierge**.
See **OD-48**.

### Retry is not escalation

| Concept | Definition | Owner |
|---|---|---|
| **Delivery retry** | Repeating delivery **to the same audience**, on the same or another surface | **Concierge** |
| **Escalation** | Changing **the audience** to a more authoritative or accountable person | **Stewardship** ladder (**OD-22**), **Operational Trust** authority |

> **There is one escalation architecture, and it already exists.** Retry is a delivery concern and is
> never called escalation. Retry policy is open decision **OD-54**.

---

## Delivery outcome model

**Two levels. They must never be flattened.**

### Communication lifecycle states

| State | Meaning |
|---|---|
| **Created** | The Communication exists and is outstanding |
| **Suppressed** | Withheld by decision. **Produces a Decision Trace** — suppression is an Intentional Non-Action |
| **Acknowledged** | An **identified person** acknowledged it. Anonymous dismissal is not acknowledgement |
| **Expired** | Its relevance window closed without a terminal outcome |
| **Superseded** | Replaced by a later Communication, by explicit Governed Reference |
| **Resolved by origin** | The originator withdrew it because the underlying condition cleared. The resident may never have seen it |
| **Undeliverable** | No permitted surface could convey it. **Must be reported, never silent** |

### Delivery Attempt outcomes

| Outcome | Meaning |
|---|---|
| **Attempted** | An attempt was made to a specific surface |
| **Delivered** | The surface accepted it |
| **Presented** | See **Presentation Outcome**, below — a `Delivered` attempt's presentation status |
| **Failed** | The attempt did not succeed at the delivery level (the surface never accepted it) |

### Presentation Outcome (DL-54)

Presentation means an artifact or information payload associated with a Delivery Attempt was
rendered, displayed, shown, spoken, played, or otherwise made available through the selected surface,
using the modality and capability actually invoked. **Presentation is a technical claim only.**

> A Room-defined outcome spanning several participating endpoints (for example a merged-room
> "Speaker" resolving to two physical speakers) carries its own **room-level** Presentation Outcome,
> a narrow projection over these endpoint-level outcomes rather than a replacement for them — see
> [../architecture/failure-and-degradation.md](../architecture/failure-and-degradation.md) and
> **DL-55**.

**Preserve these distinctions, none inferring another:**

Delivery is not automatically Presentation. Presentation is not Perception. Perception is not
Acknowledgement. Acknowledgement is not Outcome Satisfaction. Presentation does not mean correct,
does not mean the household's request was satisfied, and does not mean the right artifact was
selected — those are matters for **OD-45** (acknowledgement) and the originating capability's own
outcome tracking, never for this determination.

A `Delivered` attempt's Presentation Outcome takes exactly one of four values:

| Outcome | Meaning | Example |
|---|---|---|
| **Presented** | Authoritative evidence exists that the artifact was technically made available through the surface, using the relevant modality | An observed `media_player` state transition to `playing` after the specific request, or an `assist_satellite` transition to `responding` |
| **Failed** | Authoritative evidence exists that presentation did not occur because the presentation attempt itself failed | A documented render error; a definitive playback failure; the surface returned an error for this specific presentation |
| **Unknown** | Available evidence is insufficient to determine whether presentation occurred, on a surface that can sometimes attest it | Evidence did not arrive; the outcome is inconclusive; providers conflict and the conflict cannot be resolved |
| **Attestation Unavailable** | The selected surface or modality does not support verified Presentation Attestation at all — a capability limitation, never an attempt failure and never transient uncertainty | Mobile notification "displayed" state, dashboard/kiosk render confirmation, `persistent_notification` render confirmation — none is natively evidenced (see the Home Assistant First review below) |

**Required invariants**, all restating and sharpening **DL-53**'s existing rule:

- `Unknown` is not `Failed`, is not "not presented", and is not a falsy boolean.
- `Attestation Unavailable` is not `Unknown` — the first is a **capability** fact known in advance;
  the second is a **per-attempt** evidentiary gap.
- `Presented` does not mean perceived, acknowledged, correct, or that the household's request was
  satisfied.
- A structural mechanism (schema, enum, or model invariant — never inferred at read time) must
  prevent `Unknown` or `Attestation Unavailable` from decaying into `Failed` or "not presented".

> **A successful service call alone is never evidence of `Presented`.** Command or route acceptance
> without independent state confirmation yields `Unknown` (if the surface can sometimes attest) or
> `Attestation Unavailable` (if it never can) — never `Presented`.

### Empty-room audio

When authoritative technical evidence confirms an audio artifact was played through the selected
surface, the Presentation Outcome may be **Presented** even if the Room was empty. The corresponding
human **Perception** remains **Unknown** unless separate authoritative evidence establishes otherwise.
Empty-room playback is never equated with perception, and Presentation is never forced to `Unknown`
merely because Perception is `Unknown` — they are different questions answered by different evidence.

### Presentation is evaluated by modality and evidence, not device class

Presentation Attestation is evaluated against the **modality actually used**, the **capability
actually invoked**, and the **evidence actually returned** — never merely by physical device type,
vendor, product category, integration name, or Home Assistant entity domain or device class. A single
`media_player` entity may represent a speaker, a television, a receiver, or a camera-associated
speaker, and a single physical endpoint may expose more than one presentation modality (a television
may present audio and visually; a phone may present audio, visual, image, document, and notification).
**None of these is architecturally interchangeable, and none may be hard-coded into this model.**

### Behaviour after Failed

A known presentation failure enters the graceful degradation already governed by
[../architecture/failure-and-degradation.md](../architecture/failure-and-degradation.md). Concierge
may attempt another capable surface, endpoint, endpoint group, modality, or personal fallback only
where the alternative is permitted by the expected household outcome, current context, Operational
Trust, audience and disclosure policy, and capability requirements. Where a compliant alternative
succeeds, the original failure and the fallback result are **both** preserved in the Decision Trace.
Where none exists, the failure is preserved, explained, and the workflow fails safely — **success is
never manufactured**.

### Behaviour after Unknown

`Unknown` is valid metadata, not a trigger. It does **not** automatically cause failure, retry,
escalation, suppression, success, or "not presented" — the next behaviour is workflow- and
policy-dependent, and is not decided here. Where a workflow requires acknowledgement, `Unknown`
passes forward **unrewritten**: the Presentation Outcome remains `Unknown` and the Acknowledgement
Outcome (**OD-45**) is recorded separately. A later acknowledgement may supply stronger evidence about
receipt or interaction; it is **additive** evidence and never retroactively rewrites the historical
Presentation Outcome.

### The honesty rule for Presented

> **Most surfaces cannot attest presentation.** Where a surface's Presentation Attestation Capability
> is Unsupported, the Presentation Outcome is **Attestation Unavailable**; where it is supported but
> the specific attempt's evidence is inconclusive, the outcome is **Unknown**. Neither is **never**
> inferred from `Delivered`.

A home that reports something as seen when it only knows it was sent has converted uncertainty into
false certainty. See **P15** and
[../architecture/failure-and-degradation.md](../architecture/failure-and-degradation.md). Which
surface classes can attest, and on what specific evidence, remains open decision **OD-55**'s residual
per-integration enumeration; the outcome model itself is accepted as **DL-54**.

### Why two levels

A Communication has exactly one current lifecycle state and may have many Delivery Attempts.
Flattening the levels makes multi-surface delivery unrepresentable — the most likely modelling error
in this area.

### Rejected state

**Completed** is not a state. It conflates *the Communication was dealt with* with *the underlying
condition was resolved*. The latter belongs to the originator and outlives every Communication about
it. `Resolved by origin` covers the legitimate case.

---

## Communication history

Communication history uses the shared temporal model **unchanged**.

| Historical record | Record kind | Owner |
|---|---|---|
| Communication created | **Change Record** with no prior version | Concierge |
| Communication suppressed | **Change Record** and a **Decision Trace** | Concierge |
| Delivery attempted, delivered, presented | **Change Record** per attempt | Concierge |
| Delivery failed | **Change Record**, plus a diagnosable failure report | Concierge |
| Communication acknowledged | **Domain Event** *and* **Change Record** | Concierge |
| Communication expired | **Change Record** | Concierge |
| Communication superseded | **Change Record** carrying a Governed Reference | Concierge |
| Communication redacted, purged, or truncated | **Tombstone** | Concierge |

### Acknowledgement is both kinds of record

A resident acknowledging a Communication is **something that happened in the household** — a Domain
Event — *and* **something that happened to a governed record** — a Change Record. Both are recorded.

**Do not collapse them.** See the distinction in [temporal-record.md](temporal-record.md).

### Ownership

**Concierge owns communication delivery history**, because delivery is a decision and Concierge
already owns decision history. **No new row is added to the History-ownership matrix** in
[../architecture/framework.md](../architecture/framework.md).

The **originator** continues to own the history of the underlying matter. An Obligation's history is
Stewardship's; it is not delivery history and is not duplicated here.

> **No consumer may maintain a competing or re-derived communication history.**

### Retention

Settled by **DL-47** as a governed record class; the separate classification of content and metadata
remains **OD-49**. A floor is never stated without its ceiling.

**Content and metadata are classified separately.** The fact that the home tried to convey something
and failed may require a longer floor than the content of what it tried to convey.

---

## Household Inbox

> **The Household Inbox is a projection over outstanding Communications. It is not a persisted
> object.**

| Property | Statement |
|---|---|
| Assembled | On demand, from governed records |
| Filtered | By the viewer's authority, **evaluated at read time** |
| Owned | By no responsibility. Concierge produces it; Operational Trust filters it |
| Never | A store, a source of truth, or a shared household-wide list |

**Why it must not be persisted.** If authority to see a Communication is withdrawn, a stored inbox
still contains it until something remembers to rewrite it. A projection is correct by construction.
This is the **P30** failure mode applied to visibility.

**There is no single household inbox.** There are as many projections as there are viewers.

This is the same treatment given to **Historical Reconstruction** and **Evidence Package** in
[temporal-record.md](temporal-record.md). Projection scope and refresh semantics are open decision
**OD-47**.

---

## Explaining communication

The home must be able to answer *"why didn't you tell me?"*:

| Question | Records |
|---|---|
| Did you know? | Truth Fact history (**P28**) |
| Did you decide to tell me? | The creation Change Record |
| Did you decide **not** to? | The suppression Change Record **and its Decision Trace** |
| Did you try? | Delivery Attempt Change Records |
| Did it arrive? | Delivered and Presented, or an honest `unknown` |
| Did I acknowledge it? | The acknowledgement Domain Event, with identity attribution |
| Is it still outstanding? | The Current Projection |
| Do you still hold the record? | The record, or its **Tombstone** |

**Communication** is a Historical Explainability retrieval scope. See
[../architecture/explainability.md](../architecture/explainability.md).

---

## Multi-person communication

| Step | Responsibility | Output |
|---|---|---|
| 1 | **Originator** | This must be conveyed, to this audience, about this subject |
| 2 | **Operational Trust** | Who may receive it; the granted Urgency (interruption) entitlement; visibility classification |
| 3 | **Identity** | Candidate person assertions with confidence — never presence |
| 4 | **Truth** | Contextual person-presence and occupancy — **who else can perceive the surface** |
| 5 | **Continuity** | Re-presentation preference and personal surface defaults |
| 6 | **Concierge** | Resolve audience to surfaces, apply **P32**, decide, deliver or suppress, record, explain |

The ordering is already constitutional: *context before intent, identity before authorization, truth
before decision, trace always.* See
[../architecture/runtime-sequence.md](../architecture/runtime-sequence.md).

---

## Privacy considerations

- **Outbound communication inverts the initiative.** The audience is whoever can perceive the
  surface, not whoever asked. This is why **P32** exists.
- Guest presence constrains delivery to every audience.
- Health, medication, and pet-care Communications must be **deliverable without disclosing content
  to an unintended audience**. Content-free indication is the mechanism.
- Where identity or occupancy is uncertain, **the delivery degrades — the governance does not.**
- Visibility is never stored resolved; it is re-evaluated per attempt.
- Content and metadata are classified separately for retention.
- A suppressed Communication is recorded and explainable. **Silence is never unrecorded.**
- Redaction, purge, or truncation of a Communication leaves a **Tombstone**.

---

## Life-safety non-claim

**HTBW is not a life-safety system.**

A safety-category Communication does not constitute smoke detection, carbon-monoxide detection,
water-leak protection, medical alerting, security monitoring, or emergency notification, and must
never be represented as a substitute for certified alarms, monitored services, or emergency services.

Delivery is **best-effort** and may fail at the platform boundary. Whether HTBW may originate
safety-category Communications at all is open decision **OD-56**.

---

## Explicit non-responsibilities

This model does **not**:

- Create a Communication, Messaging, Inbox, Delivery, or Escalation responsibility
- Create a central delivery owner, a central inbox owner, or a preservation authority
- Create a second escalation ladder
- Create a new temporal record kind or a parallel history mechanism
- Own any Communication, audience, policy, obligation, or Fact
- Select a delivery technology, surface catalogue, indicator scheme, urgency scale, retry interval,
  retention duration, or identifier implementation
- Revive the superseded "message authority" boundaries of the Historical provenance and household
  memory ADRs

---

## Failure behavior

| Condition | Required behavior |
|---|---|
| No permitted surface exists for the audience | Record **Undeliverable** and report it. Never fail silently |
| A Delivery Attempt fails at the platform boundary | Record **Failed** with a diagnosable reason. Never claim success |
| A surface cannot attest presentation | Record `Presented` as **unknown**. Never infer it from Delivered |
| An acknowledgement event never arrives | Remain **unknown**. Never decay into *not acknowledged* |
| Identity is `unknown` or `ambiguous` | Degrade to content-free indication and guest-safe treatment. Never disclose content to resolve ambiguity |
| Occupancy is `unknown` | Do not announce to a shared surface. Choose the benign delivery or defer |
| Operational Trust is unavailable | Fail closed. Do not deliver |
| A Communication Change Record cannot be written | The failure is itself reportable; a silently unrecorded delivery outcome is a defect |
| A Communication is suppressed | Record the suppression **and** its Decision Trace |
| A Governed Reference on a Communication cannot be resolved | Report the reference as unavailable, with the reason where known |
| Communication history was purged | Report the gap and its reason classification. Never interpolate |

> **Silent non-delivery is prohibited.**

---

## Representative scenarios

- Stewardship determines an obligation is unmet; Operational Trust permits interruption but not
  audible announcement because guests are present; Concierge delivers to a personal surface,
  suppresses the shared announcement, and records both.
- A resident hears *"you have one message waiting"*, asks *"what is my message?"*, and identity is
  asserted at retrieval rather than at indication.
- A Communication remains outstanding as a resident moves rooms; a new Delivery Attempt is made and
  separately recorded; the Communication is not duplicated.
- A resident asks *"why didn't you tell me the garage was open?"* and the home reconstructs
  knowledge, decision, suppression, attempts, and outcomes.

See [../scenarios/why-did-this-happen.md](../scenarios/why-did-this-happen.md).

---

## Open decisions

| ID | Question |
|---|---|
| OD-22 | Escalation ladder semantics and defaults — the single ladder, serving communications |
| OD-33 | **Closed — DL-43, DL-46, DL-47.** Communication records follow the governed-record retention model; the content-versus-metadata classification remains **OD-49** |
| OD-34 | **Closed — DL-42, DL-44, DL-46, DL-47.** The temporal-persistence model is complete; Communication object persistence remains **OD-42**, subordinate to **OD-01** |
| OD-38 | Version identity, correlation, and causation identifier strategy |
| OD-42 | Communication object persistence and Home Assistant representation |
| OD-43 | **Closed — DL-53.** Delivery Surface capability model, including perceptibility and attestation; portable-surface Room Context mechanism remains **OD-73** |
| OD-44 | Delivery outcome semantics across the two levels |
| OD-45 | Acknowledgement semantics and acknowledger identification |
| OD-46 | **Closed — DL-77.** Urgency is a fixed, cumulative four-level entitlement ladder, formally independent of Action-Risk Classification (**DL-76**), never overriding audience, privacy, consent, disclosure, identity, authority, or precedence (**OD-04**) |
| OD-47 | Household Inbox projection scope and refresh semantics |
| OD-48 | Re-presentation preference and its relation to the Follow-Me preference family |
| OD-49 | Communication retention floor and ceiling |
| OD-50 | Escalation ladder semantics for communications, resolved into OD-22 |
| OD-51 | Interruption action-risk class enumeration and defaults |
| OD-52 | **Closed — DL-71.** Five audience specification forms accepted; relationship-based resolution, re-resolution timing, resolved-to-nobody/too-broadly behaviour, and Notice/completion boundary are stated |
| OD-53 | Communication category enumeration |
| OD-54 | Delivery retry policy |
| OD-55 | **Closed — DL-54.** Presentation Outcome model (Presented / Failed / Unknown / Attestation Unavailable); per-surface enumeration evidence recorded in the ADR |
| OD-56 | Safety-category scope |
| OD-57 | Indication versus content separation |
| OD-58 | Terminology supersession scope for *Notification* and *Message* |

---

## Related documents

- [../architecture/adr-resident-communication-and-delivery-separation.md](../architecture/adr-resident-communication-and-delivery-separation.md)
- [../architecture/principles.md](../architecture/principles.md)
- [../architecture/framework.md](../architecture/framework.md)
- [../architecture/privacy.md](../architecture/privacy.md)
- [../architecture/explainability.md](../architecture/explainability.md)
- [../architecture/failure-and-degradation.md](../architecture/failure-and-degradation.md)
- [../architecture/home-assistant-boundary.md](../architecture/home-assistant-boundary.md)
- [../architecture/runtime-sequence.md](../architecture/runtime-sequence.md)
- [temporal-record.md](temporal-record.md)
- [decision-trace.md](decision-trace.md)
- [operational-trust.md](operational-trust.md)
- [stewardship.md](stewardship.md)
- [continuity.md](continuity.md)
- [glossary.md](glossary.md)
- [../contracts/concierge-contract.md](../contracts/concierge-contract.md)
- [../contracts/operational-trust-contract.md](../contracts/operational-trust-contract.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
