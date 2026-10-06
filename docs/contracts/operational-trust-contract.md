# Operational Trust Contract

> **Document status: Canonical contract.**
> Responsibility: **Operational Trust**. Model:
> [../models/operational-trust.md](../models/operational-trust.md).

---

## Owning responsibility

**Operational Trust — what is allowed?**

Operational Trust is distinct from **Human Trust**, which is an outcome the household experiences, not
a layer that can be implemented. See
[../architecture/explainability.md](../architecture/explainability.md).

> **Operational Trust determines what is appropriate for this request, in this context.**

**The qualifier is required.** *For this request, in this context* is what makes the sentence true.
**The household defines what *appropriate* means; Operational Trust determines what is appropriate for
a specific request in a specific context and produces a governed decision; Concierge decides what
should happen now; an executor performs it.**

**"Operational Trust enforces what is appropriate" is rejected** — enforcement is execution, and
Operational Trust holds no execution authority. The unqualified form *"determines what is
appropriate"* is likewise rejected, because read alone it suggests Operational Trust authors household
values. See [../models/operational-trust.md](../models/operational-trust.md).

Eight inputs are evaluated before an outcome is produced, and **no single one decides it**: **Identity
confidence**, **audience awareness**, **context**, **consent**, **privacy markings**, **disclosure
requirements**, **household policy**, and **capability requirements**.

### Sufficiency, not trustworthiness

> **Operational Trust does not evaluate whether a person is trustworthy.**

It evaluates whether the **available confidence is sufficient** for the **requested capability**, the
**requested action**, and the **current context**. **The subject of the judgement is the request,
never the person.** The same person, at the same band, may be sufficient for one request and
insufficient for the next — because the requirement belongs to **what is being protected** (**DL-36**).

### Household values are applied, not authored

> **The framework provides governance. The household provides the values.**

The household defines **participation expectations**, **disclosure expectations**, **privacy
expectations**, **confidence requirements**, and **operational preferences**. Operational Trust
guarantees they are applied **consistently**, **respectfully**, and **explainably** — in every Room, on
every surface, for every requester.

**Operational Trust does not decide what the household ought to value**, and it never substitutes its
own judgement for a household decision it finds inconvenient. **A requirement is never lowered to
reach a result.**

---

## What Operational Trust guarantees

- An authority decision for every action considered: `permitted`, `prohibited`,
  `permitted_with_confirmation`, or `permitted_with_escalation`
- The effective autonomy level for the action in its context
- Confirmation and consent requirements
- **The confidence a given presentation, capability, protected resource, or protected operation requires** — Identity never judges the sufficiency of its own result
- **The confirmation strength required**, and the **scope and lifetime** of a successful confirmation
- Suppression and interruption rules
- Visibility rules for privacy-governed content
- The **Urgency entitlement** of a Communication — what it is entitled to interrupt
- **Audience eligibility** — who may receive a Communication, and who may hear it
- The **visibility classification** applied to a Communication, re-evaluated at each Delivery Attempt
- The **retention classification** of a Communication, with content and metadata classified separately
- The reason and the policy reference behind every decision

Ownership includes: authority, permission, restrictions, guest access, child safety, quiet hours,
nighttime restrictions, room-level authority, person-level authority, autonomy level, confirmation
requirements, consent boundaries, safety-critical restrictions, escalation permissions, suppression
policy, interruption policy, privacy visibility policy, policy provenance and precedence, and
communication urgency, audience eligibility, visibility, and retention classification.

---

## The autonomy model and the ceiling rule

| Level | Meaning |
|---|---|
| Explicit | Act only on direct instruction |
| Assisted | Propose, then act on confirmation |
| Autonomous | Act without asking, within policy |

> **The most restrictive applicable policy sets the ceiling.**

Home Autonomous + Room Assisted + Person Autonomous ⇒ effective level **Assisted**. Restriction always
wins over permission, across Home, Room, Person, Asset, Relationship, Experience class, and
Action-risk class.

---

## Identity confidence and action risk

| Action risk | Example | Identity requirement |
|---|---|---|
| Benign | A lamp in an occupied room | May proceed with unknown identity, per policy |
| Personal | "Play my playlist" | Requires a resolved identity |
| Sensitive | Read a calendar or message | Requires a resolved identity above threshold |
| Safety-critical | Unlock a door, open a garage, control a heat source | Requires high confidence and may require confirmation regardless |

Per-class defaults are configuration, resolved as **DL-76** — see **Action-Risk Classes**, below.

**Operational Trust owns the Required Identity Band.** Every protected capability and protected
operation carries one of five requirement values — **`None`, Low, Moderate, High, Very High**.
**`None` is a Trust requirement, not an Identity output**, and means *no known-Person identity is
required for this operation*. Identity produces four bands and never produces `None`. A requirement of
`None` is satisfied without consulting identity at all, and the outcome is recorded as *known-Person
identity was not required* — **never** as a band "exceeding" `None`.

**Operational Trust owns every threshold**, including **Address by Name**, the Identity Presentation

---

## Action-Risk Classes (DL-76)

Six constitutional, consequence-based classes — **Convenience**, **Disclosure**, **Financial**,
**Safety**, **Security**, **Governance** — structurally separate from **Operation Type** (Read, Write,
Delete, Govern; **DL-36** unchanged). Risk Classification answers *"what happens if this is wrong?"*;
Operation Type answers *"what kind of action is occurring?"*. No matrix is required.

| Risk Class | Required Identity Band | Required Confirmation Strength | Address by Name | Presentation Threshold |
|---|---|---|---|---|
| Convenience | `None` | `None` | Low | `None` |
| Disclosure | Moderate | Verbal | Moderate | Moderate |
| Financial | High | Authenticated | High | High |
| Safety | High | Authenticated | High | High |
| Security | High | Authenticated | High | High |
| Governance | Very High | Strong | Very High | Very High |

**These are HTBW Default Configuration, never Fixed Configuration**, and are not a claim that a
verified confirmation mechanism exists — Issue #146 item 10 remains `VERIFIED_NOT_SUPPORTED` for every
mechanism above Verbal, and **DL-40**'s `Unavailable` outcome governs unchanged.

**Override model:** Capability Default (the capability declares its Risk Class) → HTBW Default (the
table above) → Household Override (governed configuration). **Object-specific overrides** are
explicitly supported, restating **DL-36**: a Safe Lock and a Closet Lock may carry different
requirements despite sharing one capability.
Threshold, Capability Access Thresholds, personalization requirements, confirmation requirements and
acceptable method strength, disclosure appropriateness, Unknown Person eligibility, and the required
behaviour when identity is insufficient. **The configuration surface never changes ownership** — a
setting shown in Room, Person, capability, or Concierge configuration remains Operational Trust's if
it determines permission or identity sufficiency.

**There is no universal threshold.** One purpose-specific Identity Assertion is consumed by four
distinct evaluations — the **Identity Presentation Threshold**, the **Capability Access Threshold**,
**disclosure evaluation**, and **confirmation** — and satisfying one never satisfies another. The
requirement belongs to what is being protected, never to the person, the evidence source, or
Identity. Requirements may be stated per capability, per protected resource, and **per protected
operation**: read, write, delete, and governance operations are never collapsed into one threshold.
*No identity required* is a legitimate requirement and is **not** an absence of governance.

**Confirmation is bounded.** A confirmation is scoped by purpose, capability and operation,
interaction, channel, Room, Person, and time — and **never by audience**. It produces a separate
record and **never rewrites the original Identity Assertion or its confidence**. `Confirmed` is a
scoped interaction state, not the top of the confidence scale, and a spoken "yes" is not adequate for
every operation. **A confirmation is consumed by the operation that required it**: it does not persist
because presence continues, has **no occupancy grace period**, establishes no authenticated session,
does not carry into the next protected operation by default, and **never changes the Identity band**.
A bounded multi-step task must state its bound explicitly. See
[../models/operational-trust.md](../models/operational-trust.md).

**Required Confirmation Strength is an ordered class set** — **`None` < Verbal < Authenticated <
Strong** (**DL-40**) — configured per protected operation, alongside and independent of the Required
Identity Band. The classes are separated by **independence from the evidence and the channel that
produced the assertion**, never by friction. **A strength class is a classification, not a
mechanism**: it is satisfied only by a mechanism the deployment has **verified** as meeting it, no
mechanism is prescribed or assumed, and where no verified mechanism is available the confirmation
outcome is `Unavailable`. **A required strength is never silently downgraded.**

**Every evaluation uses the current assertion.** A requirement is applied against a current,
purpose-appropriate Identity Assertion. Continuous Room occupancy is **not** continuous
authentication, and a prior assertion, band, access grant, or confirmation is never revived because
presence remained active or because an **OD-15** validity window has not elapsed. **Validity is not
current-interaction applicability.** Sensor debouncing belongs to evidence freshness under **DL-38**
and never becomes an authorisation lifetime.

**Access and presentation are evaluated independently**, from the same assertion, and may reach
different outcomes. A presentation threshold that is not met produces neutral wording; **it never
denies the action**.

**Interrupting is a governed action, on its own axis.** Interruption is **not** a Risk Class;
Risk and Interruption are formally separate, independent axes (**DL-76**). **OD-51/DL-76 owns Action
Risk; OD-46 owns Interruption Classification.** A safety or critical classification is a granted,
revocable, explainable entitlement and **never a bypass**.

**Urgency is granted, not asserted.** An originator may propose an urgency; Operational Trust
determines it. Urgency is orthogonal to Category and the two axes must never be merged. See
[../models/communication.md](../models/communication.md).

---

## Consent, participation, and available evidence

**Participation is optional, and participation requires consent.** Voice identity evidence, wearable
evidence, device evidence, and person-scoped preference participation are each **opt-in**. **Voice
identity evidence is available only for a consenting, enrolled participant.**

Operational Trust guarantees:

| Guarantee | Statement |
|---|---|
| Declining is neutral | Fewer eligible families produce a **lower ceiling, never a penalty**. *Missing evidence is not contradicting evidence* |
| Declining is not exclusion | A person who has not consented must still be able to use the home in a **guest-safe** way |
| Consent is scoped | Consenting to voice identity is **not** consent to calendar access |
| Consent gates eligibility, not weight | Evidence lacking valid consent is **excluded before weighting, never down-weighted** |
| Consistency runs both ways | A permitted source is used; **a declined source is never used "just this once"** because the outcome would be convenient |
| Missing consent is never implied consent | Refusal is the governed response |

The governing chain, with each link owned by a different responsibility:

```text
CONSENT  →  AVAILABLE EVIDENCE  →  IDENTITY  →  OPERATIONAL TRUST
```

> **Consent determines what evidence may be used. Operational Trust ensures those choices are applied
> consistently and respectfully.**

Ownership is unchanged: **Foundation** holds the consent record, **Identity** owns the consent
lifecycle, **Operational Trust** owns consent policy and enforcement. Consent user experience is
**OD-06**.

---

## Knowledge, disclosure, and audience

### Disclosure is separate from knowledge

> **The question is not *"can the home know?"* It is *"should the home share?"***

Knowledge acquisition and disclosure are **separate responsibilities evaluated at separate points**.
**The home may legitimately know something it will not say** — that is the privacy model working. The
inverse also binds: **a disclosure requirement never reaches back to authorise collection.**

### Audience awareness is a first-class input

> **Operational Trust evaluates who is asking *and* who is listening.**

**Identity confidence may remain entirely unchanged while the outcome varies** — alone, with a known
participant present, with a guest present, or with an unidentified person present. **The room changed,
not the person.**

Audience composition **identifies nobody**, is **never a second identity fusion**, and **retains its
uncertainty** (**DL-34**). **Absence of evidence is never proof of solitude.** Where composition cannot
be established, **OD-71** governs and **the delivery degrades — the governance does not**.

### Explicit metadata is preferred over inferred sensitivity

> **Where content carries an explicit classification, Operational Trust uses it rather than
> interpreting the content.**

An explicit privacy marking, a household-configured classification, or a declared classification from
the originating source is preferred over content interpretation, sensitivity inference, or semantic
classification at decision time — for **explainability**, **predictability**, **auditability**, and
**implementation simplicity**.

**An absent marking is not a permissive marking**; the governing policy for unclassified content
applies. **A reasoning provider is never the sensitivity classifier** (**DL-34**, **OD-67**). **Which
native fields carry an explicit marking is a platform question under DL-30, and none is claimed here.**

---

## "Not now" is a valid outcome

> **Knowing the answer does not always mean the home should provide it.**

Six outcome shapes describe what the household experiences. **They introduce no new enumeration and
move no ownership** — each is produced by existing constructs.

| Shape | Produced by |
|---|---|
| **Allow** | `permitted` |
| **Require Confirmation** | `permitted_with_confirmation` |
| **Defer** | Operational Trust supplies the suppression or interruption constraint; **Concierge** expresses the deferral |
| **Redirect** | Disclosure outcome *access allowed, private delivery available*; **Concierge** selects the surface |
| **Abstain** | `undecidable`, or *identity or audience insufficient*, degrading under **OD-71** |
| **Deny** | `prohibited` |

**Operational Trust owns the constraint; Concierge owns the expression.** Every shape produces a
Decision Trace: *Defer*, *Redirect*, and *Abstain* are **Intentional Non-Actions** under **P16** and
**DL-15**. **A degraded outcome is correct behaviour, not a failure**, and **no shape is a silent one**.

---

## What Operational Trust will never do

- Determine who a person is (Identity)
- Determine what is true (Truth)
- Determine what matters (Stewardship)
- Store preferences or sessions (Continuity)
- Decide what should happen (Concierge)
- Perform actions
- Originate, deliver, suppress, retry, or record a Communication (originators and Concierge)
- Own the escalation **ladder**, which is Stewardship's (**OD-22**)

**Operational Trust does not determine who a person is.** It consumes an identity assertion, applies a
threshold appropriate to the action class, and decides what that assertion is sufficient to authorize.

---

## What consumers may rely upon

| Consumer | May rely upon |
|---|---|
| Concierge | The authority decision, the effective autonomy level, and the reason |
| Concierge | The Urgency entitlement, audience eligibility, visibility classification, and retention classification of a Communication |
| Continuity | Whether a transfer, resume, or displacement is permitted |
| Stewardship | Whether an escalation is permitted, and to whom |
| Every responsibility | Visibility rules for privacy-governed content |

## What consumers must never assume

- That absence of a prohibition is permission
- That a previously granted authority remains valid for a new context or a later moment
- That an autonomous ceiling at one scope overrides a restriction at another
- That confirmation may be skipped because the action is convenient
- That a successful confirmation raised the original identity confidence, or made it certain
- That a confirmation granted for one capability, operation, channel, Room, or moment covers another
- That confirming identity or access also authorised disclosure to the current audience (**DL-34**)
- That a verbal confirmation is sufficient for every operation
- That meeting a presentation threshold granted access, or that access granted personalization
- **That `None` is an Identity band, or that a band "exceeds" `None`**
- **That continuous Room occupancy preserves a prior speaker's identity, band, access, or confirmation**
- That a presentation threshold not being met is a reason to refuse an action
- That an Unknown Person satisfies `Low`, or is assigned any band
- That a confirmation **strength class** implies that a mechanism meeting it exists in this deployment
- **That an unavailable capability was denied, refused, or blocked by a permission or identity outcome**
- **That satisfying a requirement makes a missing dependency available**
- That a learned pattern has become policy
- That permission to act implies permission to announce (**P32**)
- That a visibility classification resolved for one Delivery Attempt remains valid for the next
- **That Operational Trust judged the requester's trustworthiness** — it judged the sufficiency of a confidence for a request
- **That Operational Trust authored a household value** — it applied one
- **That a person who declined a participation class is penalised, excluded, or degraded**
- **That a requirement may be lowered because confidence fell short**
- **That being able to establish something authorises conveying it**
- **That an unmarked or unclassified item is a public item**
- **That refusal is the only alternative to compliance** — *Defer*, *Redirect*, and *Abstain* are governed outcomes

---

## Learned suggestion versus autonomous policy

> **A learned suggestion is not an autonomous policy.**

Observed patterns may be proposed to the household. They become policy only through explicit household
acceptance, recorded with provenance. Silent promotion is prohibited.

---

## Uncertainty and unknown representation

| Outcome | Meaning |
|---|---|
| `permitted` | The action may proceed at the stated autonomy level |
| `prohibited` | The action must not proceed |
| `permitted_with_confirmation` | The action requires explicit human confirmation |
| `permitted_with_escalation` | The action requires escalation to an authorised person |
| `undecidable` | A required input is unknown; the action must not proceed |

`undecidable` is never rendered as `permitted`.

A confirmation outcome is one of `Confirmed`, `Denied`, `Unclear`, `Cancelled`, `Unavailable`, or
`Expired`. **`Unclear`, `Unavailable`, and `Expired` are never rendered as `Confirmed`**, and
`Confirmed` applies only within its governed scope.

---

## Failure and degradation behavior

Operational Trust **fails closed**.

| Condition | Behavior |
|---|---|
| Identity unresolved | Apply the least-privileged applicable policy (guest-safe). Never assume the most likely resident for an authority-bearing action. |
| Identity ambiguous | Require disambiguation or refuse; never silently select a candidate |
| A required fact is unknown | Unknown is never permission. Refuse, ask, or choose the benign action. |
| A policy source is unavailable | Apply the most restrictive known policy and report the degradation |
| Policies conflict irreconcilably | Refuse, explain the conflict, and surface it for household resolution |
| Consent missing or expired | Refuse. Missing consent is never implied consent. |

---

## Privacy constraints

Operational Trust owns the visibility policy for personal preferences, presence history, session
history, Stewardship content, and Decision Traces. Guest and child-safe treatments are policy positions
here, never ad-hoc filtering elsewhere.

**Consent ownership.** Operational Trust owns consent **policy and enforcement**: which actions require
consent, what consent is sufficient, and refusal when consent is missing or expired. It does not hold
the consent record (Foundation) and does not run the consent lifecycle (Identity). See
[../models/operational-trust.md](../models/operational-trust.md).

**Historical visibility.** Visibility policy applies to historical records exactly as it applies to
current ones. *Withheld by policy* must remain distinguishable from *no longer retained* and from
*nothing happened*.

---

## Retention and preservation authority

Operational Trust owns retention classification, privacy classification policy, and Preservation Hold
authority.

| Guarantee | Statement |
|---|---|
| Retention is bounded from both directions | **P27** and **P28** set the floor; [../architecture/privacy.md](../architecture/privacy.md) sets the ceiling. Both bind |
| Privacy governs conflicts | Where a floor and a ceiling conflict, privacy governs, and the resulting limitation on explainability is itself recorded |
| Policy history is retained | A past decision can cite the policy version that applied at the time. Changing a policy never rewrites a past explanation |
| Holds are authorised centrally, enforced locally | Operational Trust authorises a Preservation Hold; **each responsibility enforces it over its own records**. There is no central preservation-hold enforcer |
| Holds are governed | Discoverable, attributable, bounded or periodically reviewed, independent of visibility, explainable |
| Holds never widen disclosure | **A hold does not automatically increase visibility.** Preserving a record is not disclosing it |
| Holds cannot resurrect prohibited data | A hold cannot preserve raw biometric internals or raw voice samples, because those were never stored |

**Consumers must never assume** that a record's existence implies permission to see it, or that a
record's absence implies that nothing happened.

**Preservation Hold and Evidence Package are HTBW architectural terms, not claims of legal effect.**

---

## Explainability contributions

Every authority decision records: the action and its risk class; the identity assertion relied upon and
its confidence; the facts relied upon; the policies evaluated, including which were restrictive; the
effective autonomy level and the policy that set the ceiling; the outcome; and the human-readable
reason.

A refusal must be explainable to the resident in household language, and — where safe — must state what
would change the outcome.

---

## Open decisions

| ID | Question |
|---|---|
| OD-04 | Exact global priority order across policy scopes |
| OD-06 | Consent user experience |
| OD-08 | **Resolved** as **DL-39** and **DL-40** |
| OD-28 | How household acceptance of learned suggestions is captured and revoked |
| OD-33 | **Closed — DL-43, DL-46, DL-47.** Retention is declared inside every governed record and artifact lifecycle; the remaining values are **OD-05**, **OD-26**, **OD-49** |
| OD-35 | Historical query surface and access |
| OD-36 | Reconciliation of deletion and export obligations with retention floors and Preservation Holds |
| OD-39 | Preservation Hold authority, duration, review, release, and conflict with deletion |
| OD-40 | Evidence Package assembly, transport, integrity representation, and audience |
| OD-45 | Acknowledgement semantics, and whether unacknowledged delivery is a failure |
| OD-46 | Urgency classification as an Operational Trust entitlement. **Resolved by DL-76 that this is formally independent of Action-Risk Classification** |
| OD-49 | Communication retention floor and ceiling |
| OD-51 | **Resolved as DL-76.** Action-Risk Class enumeration and per-class defaults; household and object-specific override model; interruption confirmed as a separate axis (OD-46) |
| OD-52 | Audience specification model |
| OD-53 | Communication category enumeration |
| OD-56 | Safety-category scope |
| OD-57 | Indication versus content separation |

## Related documents

- [../models/operational-trust.md](../models/operational-trust.md)
- [../models/temporal-record.md](../models/temporal-record.md)
- [../models/communication.md](../models/communication.md)
- [../architecture/behavioral-governance.md](../architecture/behavioral-governance.md)
- [../architecture/privacy.md](../architecture/privacy.md)
- [identity-contract.md](identity-contract.md)
- [concierge-contract.md](concierge-contract.md)
