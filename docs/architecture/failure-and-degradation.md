# Failure, Uncertainty, and Degradation

> **Document status: Canonical.**
> Cross-cutting architecture. Every responsibility must satisfy this document.

---

## Principle

**Uncertainty must remain visible. It must not be converted into false certainty.**

**Do not invent certainty.** A missing fact is a fact about the system, and it must be representable,
reportable, and explainable.

The architecture favours **safe and explainable degradation** over confident wrong behavior.

---

## Governed fallback vocabulary

Depending on risk and policy, the fallback may be:

| Fallback | Meaning |
|---|---|
| Refuse | Do not perform the action, and say so |
| Take no action | Intentional non-action, recorded and explainable |
| Perform only a benign action | Do the low-risk part only |
| Ask | Request clarification or confirmation |
| Convey | Inform without acting |
| Convey without content | Indicate that something is outstanding without disclosing what it says |
| Escalate | Raise to a person with authority, or to a higher-priority channel |
| Preserve the current experience | Change nothing that is already running |
| Record an unresolved state | Leave a durable marker that something could not be settled |
| Report unavailable | State that the capability cannot exist in this home, and name the missing dependency |

Every fallback is a **decision** and produces a Decision Trace.

---

## Honest response vocabulary for conversational retrieval and command resolution (DL-69)

Resolves part of **OD-62**. This extends, and never replaces, the governed fallback vocabulary above
for a spoken or conversational interaction.

| Term | Meaning |
|---|---|
| Unknown | The question was evaluated but the answer cannot be determined from eligible evidence |
| Unavailable | A required capability or source could not be used |
| Not understood | No deterministic HTBW Vocabulary interpretation is available |
| Clarification required | More than one authorized, contextual interpretation remains |
| Not authorized | The requester lacks authority — stating this explicitly may itself be a disclosure, so the spoken wording must remain audience-safe |
| Cannot answer here | The answer may require a private or authenticated surface |
| Unsupported | The requested capability is not available through the current conversational surface |

**The spoken wording must be audience-safe.** A shared-space response may need to say *"I can't answer
that here"* rather than name what is being withheld or from whom. **A failed HTBW Vocabulary match
must never silently authorize an unrelated or materially broader native action** — none of the entries
above, and none of the governed fallback types in the table above, is "silently hand off to a system
that may interpret the request differently." See
[../models/contextual-vocabulary.md](../models/contextual-vocabulary.md), *Command resolution and safe
native fallback*.

---

## Capability dependency

> **A capability that cannot exist is not a capability that was denied.**

Every degraded condition in this document assumes the capability exists at all. That assumption is
itself governed.

**Every capability declares its dependencies.** A dependency is a stated precondition without which
the capability cannot exist in this home:

| Dependency kind | Examples |
|---|---|
| **Native Home Assistant capability** | A calendar source, a media player, a notify service, an Assist pipeline |
| **Integration** | An email integration, a calendar integration, a media provider |
| **Provider** | A Voice Identity provider, a reasoning provider (**OD-67**) |
| **Connected Storage** | Asset documents, voiceprints, Preservation Hold enforcement, extended historical retention |
| **Consent** | Voice enrollment, identity evidence association |
| **Configuration** | Room assignment for a voice assistant, a configured vocabulary mapping, a declared archive destination |

Dependencies are declared per capability by the responsibility that owns it. **This creates no
Capability responsibility, no capability registry service, and no dependency broker.** The seven
responsibilities are unchanged; declaring a precondition is a property of a capability, not a new
owner of one.

### How a dependency is satisfied

| Route | Rule |
|---|---|
| **Native Home Assistant capability** | Satisfies the dependency **where it fully represents the requirement**. This is the first route evaluated (**P21**, **DL-30**) |
| **Integration or provider** | Satisfies a non-native dependency **where it is configured, valid, and available**. Presence in the configuration is not sufficient on its own |
| **Connected Storage** | Satisfies an artifact or extended-retention dependency (**DL-42**) |
| **Consent** | An **eligibility** dependency. Consent governs whether the capability may operate for a Person; it never becomes a platform dependency, and its absence is not a platform defect |
| **Configuration** | Satisfies a dependency on a declared setting — a Room assignment, a vocabulary mapping, a storage destination |

**A capability may declare several dependencies.** All **mandatory** dependencies must be satisfied
before the capability is available. A capability may also declare **optional** dependencies that
improve its quality — better evidence, richer sources, faster resolution — and **an unmet optional
dependency never makes the capability unavailable**. A dependency is one or the other, declared
explicitly; an undeclared dependency that turns out to be load-bearing is a defect.

### A missing dependency disables the capability

**HTBW does not emulate a missing dependency.** It does not substitute an approximation, build a
local stand-in, or quietly reduce the capability to something weaker that shares its name.

| Missing dependency | Result |
|---|---|
| No email integration | The email capability is **unavailable** |
| No calendar source | The calendar capability is **unavailable** |
| No Voice Identity provider | Voice-based identity evidence is **unavailable** |
| No Connected Storage | Asset documents, voiceprints, Preservation Hold enforcement, and extended historical retention are **unavailable** |
| Consent not given | The consent-dependent capability is **unavailable** |
| Required configuration absent | The capability is **unavailable**, and is surfaced as a configuration problem |

Unavailability is stated, never silent. The home says **what** is unavailable and **which dependency
is missing**, in a sentence a resident can act on.

### Capability unavailable is a dependency outcome

**It is not a trust failure, an identity failure, or a permission failure.** Confusing them produces
two distinct harms: a household is told it lacks permission when it actually lacks an integration,
and a genuine refusal is dismissed as a setup problem.

| Not this | But this |
|---|---|
| *"You are not permitted to do that"* | *"There is no email integration configured, so I cannot send email"* |
| *"I could not tell it was you"* | *"Voice Identity has no provider configured"* |
| *"That was denied"* | *"Connected Storage is not configured, so documents cannot be stored"* |

### Three independent questions

| Layer | Question | Answered by |
|---|---|---|
| **Capability dependency** | *Can this happen at all?* | The declared dependencies of the capability |
| **Identity** | *Who is this?* | Identity (**DL-38**, **DL-39**) |
| **Operational Trust** | *May this happen?* | Operational Trust (**DL-36**, **DL-39**, **DL-40**) |

They are evaluated in that order, and **satisfying one never satisfies another**.

**Dependency is evaluated first.** Where a capability is unavailable, **identity is not consulted and
no requirement is evaluated** — there is nothing to permit. An unavailable capability never becomes a
reason to lower a threshold, and a satisfied threshold never conjures a missing dependency.

```text
Required dependency evaluation
    ↓
Capability available, or unavailable
    ↓
Identity evaluation — only where the protected operation requires identity
    ↓
Operational Trust evaluation
    ↓
Concierge orchestration
    ↓
Communication and delivery, where applicable
```

Two constraints on that order:

- **Identity is not evaluated when the capability is already unavailable.**
- **Identity is not evaluated where the protected operation requires none.** A Required Identity Band
  of `None` means the question is not asked, not that it was asked and waived (**DL-39**).

Worked contrast:

| Situation | Capability | Identity | Trust | Outcome |
|---|---|---|---|---|
| No email integration | **Unavailable** | Not consulted | Not evaluated | *"Email is not configured here"* |
| Email integration present; Tom at **Low**; requirement **Very High** | Available | `known`, Low | Requirement unmet | *"I am not confident enough that it is you"* — access denied, confirmation may be offered |

These are **different outcomes with different explanations**, and a Decision Trace must not render
one as the other.

### Five distinct outcomes

**Do not collapse these into one generic failure.** Each has a different cause, a different remedy,
and a different sentence.

| Outcome | Meaning | Remedy lies with |
|---|---|---|
| **Dependency unavailable** | The capability cannot exist in this deployment | Configuration — add the integration, provider, storage, consent, or setting |
| **Identity insufficient** | The capability exists; the required known-Person condition is unmet | Better evidence, or a confirmation where policy permits |
| **Operational Trust denied** | The capability exists and identity may suffice; policy prohibits the action | Policy, or an authorised person |
| **Disclosure not appropriate** | Access is permitted; presenting it through the proposed surface is not | Surface, audience, or timing — **never by relaxing the exposure rule** |
| **Runtime failure** | Capability and dependencies exist; execution failed | The failing system; the failure is reported honestly and never claimed as success |

The exact wording is not prescribed. The **distinction** is.

### Dependency health is not dependency presence

A capability's availability depends on a dependency being **usable**, not merely **named in the
configuration**, wherever the architecture can determine the difference:

| State | Capability |
|---|---|
| Not configured | **Unavailable** |
| Configured but invalid | **Unavailable**, reported as a configuration defect rather than an absence |
| Configured but currently unavailable | **Unavailable**, reported as a transient condition where that is known |
| Configured and healthy | Available |
| Degraded but usable | Available, **with the degradation recorded and explainable** — never silently |
| Required dependency removed | **Unavailable**, and existing governed references are reported as broken rather than rewritten |

Truth may establish current Facts about dependency health where that is accepted, and Repairs may
surface a configuration or availability defect. **Neither becomes the owner of the capability or of
its dependency declaration.**

**No runtime health protocol is defined here.** Detection mechanics, polling, and reconciliation
timing are implementation matters and are not settled by this document.

---

## Required behaviors

| Condition | Owner of the condition | Required behavior |
|---|---|---|
| Identity is unresolved | Identity | Apply the unidentified-person policy. Guest-safe behavior by default. Never assume the most likely resident for an authority-bearing action. |
| Two identities are plausible | Identity | Report ambiguity with both candidates and confidences. Do not silently pick the higher score for authority-bearing actions. |
| Evidence sources disagree | Truth | Qualify the evidence per **DL-63** before treating it as conflict; if genuine, resolve to reduced confidence, publish an unresolved fact, or publish `unknown` under the applicable Conflict Policy. Never average, never silently choose. |
| A conflict persists | Truth | Record via the existing Domain Event mechanism (**DL-63**); evaluate against **DL-65**'s Repairs criteria separately from the runtime outcome. Ordinary transient disagreement is not automatically Repairs-eligible. |
| Evidence is stale | Truth | Mark the fact as stale and reduce confidence, or withdraw the fact. Never present a stale value as current. |
| Truth cannot establish a fact | Truth | Publish "unknown" rather than a default. Downstream must treat unknown as unknown. |
| A Primary Authority is unavailable | Truth | The Authority-Derived Fact becomes `unknown` or unavailable (**DL-59**); never silently switched to another candidate sensor, and never treated as an evidence conflict (**DL-62**). |
| A voice assistant has no Room assignment | Room Configuration | Ask which Room, or refuse. Never guess a Room from device naming. Surface it as a configuration problem. |
| A vocabulary term has no mapping | Room Configuration | Say the term is not configured here. Never fall back to a runtime device search. |
| A vocabulary term maps ambiguously | Room Configuration | Ask which target was meant. Offer only exposed options. |
| A target device is unavailable | Truth / execution | Report partial or failed execution honestly. Do not claim success. |
| A configured speaker group is partially unavailable | Continuity / Concierge | Apply the configured partial-availability policy: proceed with available members, ask, or refuse. Record which members were unavailable. |
| A Room-defined presentation outcome spans multiple participating endpoints with mixed results | Concierge | Record the **room-level Presentation Outcome** as `Presented` where at least one participating endpoint achieved `Presented` (**DL-54**), carrying a **Degraded** quality label when any participating endpoint did not. Endpoint-level outcomes remain individually visible. **Never average, score, or replace them with a single room-health value** (**DL-55**). |
| Home Assistant restarts during an active session | Continuity | Do not fabricate a session. Re-establish only what can be verified. Offer resume where eligible. |
| A room transition is missed | Truth / Continuity | Do not retroactively invent a transfer. Treat the newly observed Room as current and explain the gap. |
| A third-party calendar or email service is disconnected | Truth / experience source | Report the source as unavailable. Do not present stale data as current. Do not degrade privacy to compensate. |
| Two policies have equal priority | Operational Trust | Do not choose arbitrarily. Apply the configured tie-breaking policy; if none exists, refuse or ask, and record the tie. |
| Concierge cannot safely resolve a conflict | Concierge | Preserve the current experience, take no action, and record an unresolved state. |
| A historical reconstruction spans purged, deleted, or redacted records | The owning responsibility | Report the gap and its reason classification where known. Never fabricate the missing state and never silently close the gap. **A reconstruction containing an unreported gap is a defect.** |
| A Governed Reference cannot be resolved | The referring responsibility | Report the reference as unavailable with the reason where known. Never render it as though the source record never existed. |
| A referenced native Home Assistant record has been purged | The referring responsibility | Resolve to *"no longer retained"*, never *"never existed"*. |
| A governed record was removed by retention or deletion | The owning responsibility | Leave a Tombstone where required. **Never allow removal to become indistinguishable from absence.** |
| A Change Record value was redacted | The owning responsibility | Report that a change occurred with its value no longer retained. **Never report that no change occurred.** |
| A Change Record cannot be written | The owning responsibility | The failure is itself reportable. A silently unrecorded governed change is a defect. |
| Effective Time cannot be determined for a change | The owning responsibility | Record Effective Time as unknown and state so. Never substitute Recorded Time silently. |
| A held record's required references were removed | Operational Trust / the owning responsibility | Report a preservation failure. |
| A Snapshot would reinstate content removed under privacy policy | The owning responsibility | Redact or re-derive the Snapshot. **Never reintroduce removed content.** |
| No permitted Delivery Surface exists for a Communication's audience | Concierge | Record **Undeliverable** and report it. **Silent non-delivery is prohibited.** |
| A Delivery Attempt fails at the platform boundary | Concierge | Record **Failed** with a diagnosable reason. Never claim success. |
| A surface cannot attest that a Communication was presented | Concierge | Record `Presented` as **unknown**. **Never infer `Presented` from `Delivered`.** |
| An acknowledgement event never arrives | Concierge | Remain **unknown**. Never allow unknown to decay into *not acknowledged*. |
| A Communication is withheld | Concierge | Record the **suppression** as a governed change **and** produce a Decision Trace. A decision to stay quiet that cannot be stated is a defect. |
| Occupancy or identity is unknown and the only available surface is shared | Concierge / Truth / Identity | Degrade the **delivery**: reduce to content-free indication, choose a personal surface, or defer. **Never relax an exposure rule to get a message through.** |
| A Communication Change Record cannot be written | Concierge | The failure is itself reportable. A silently unrecorded delivery outcome is a defect. |
| A declared dependency is missing | The responsibility owning the capability | Report the capability as **unavailable** and name the missing dependency. **Never emulate it, never substitute an approximation, and never render it as a permission or identity failure.** |
| Connected Storage is unavailable or unconfigured | The responsibility owning the artifact | The dependent capability is **unavailable**. **Never fall back to an unmanaged local store**, and never write a governed artifact to a location with no declared lifecycle. |
| A stored artifact's declared retention or deletion strategy is absent | The owning responsibility | The artifact must not be created. **An artifact with no documented lifecycle is a defect, not a default.** |
| A governing parent object is removed | The responsibility owning the artifact | Dependent artifacts and references are cleaned up, holds and retention floors are evaluated first, and empty capability-owned structures are removed. **The default is cleanup; continued existence requires an accepted reason.** |
| Parent-object cleanup is triggered while Connected Storage is unavailable | The responsibility owning the artifact | **Do not claim deletion succeeded.** Retain a governed pending-cleanup state, keep the reference, do not recreate the artifact elsewhere, surface the condition, and reconcile once storage returns. |
| Cleanup cannot complete for an artifact under a Preservation Hold or retention floor | Operational Trust, with the owning responsibility | The artifact remains, **governed and explained**. Cleanup never silently overrides a hold or a floor. |

> **Silent non-delivery is prohibited.** *"Nothing was sent"* and *"we decided not to send"* are
> different facts, and the home must be able to tell them apart. See
> [../models/communication.md](../models/communication.md).

---

## Degradation across time

The rules above apply to the historical record exactly as they apply to the present.

**A gap in history is a fact about the system, and must be representable, reportable, and
explainable.** These states must always remain distinguishable:

| State | Meaning |
|---|---|
| No event occurred | Nothing happened |
| No record was created | Something happened but produced no governed record |
| A record existed but was purged | Removed by retention policy |
| A record existed but was deleted | Removed by an authorised deletion request |
| A record existed but was redacted | Retained, with values removed |
| A record is unavailable | Cannot currently be reached |
| A record is withheld by policy | Exists and is retained, but is not disclosable to this audience |

Collapsing any of these into *"nothing happened"* is the temporal form of inventing certainty. See
[../models/temporal-record.md](../models/temporal-record.md) and [privacy.md](privacy.md).

---

## Fail-closed defaults

Where no policy is configured, the default is the **safer** option:

- Unresolved identity → guest-safe treatment.
- Unknown fact → do not act autonomously.
- Missing permission → refuse.
- Ambiguous target → ask.
- Conflicting priority → preserve the existing experience.

A household may configure a more permissive behavior explicitly, subject to the autonomy ceiling.
It may never be produced implicitly by an absent configuration.

---

## Uncertainty must survive the whole pipeline

An uncertain input must not become a certain output.

```
evidence (weak)  →  assertion (identity_confidence_band: Low)  →  fact (unknown / truth_confidence_band: Low)
                 →  decision (ask, or no action)  →  explanation states the uncertainty
```

Any step that discards confidence without recording it is a defect.

**Presentation Attestation is a concrete instance of this rule** (**DL-54**): a Delivery Attempt's
Presentation Outcome is `Presented`, `Failed`, `Unknown`, or `Attestation Unavailable`, and `Unknown`
is structurally prevented from decaying into `Failed` or "not presented" on its way to the resident.
See [../models/communication.md](../models/communication.md).

---

## Diagnosability

Every degraded condition above must be:

- representable in the model,
- visible in diagnostics,
- present in the Decision Trace when it affected an outcome,
- present in a historical reconstruction when it affected the period being reconstructed,
- and expressible in a human sentence.

Silent degradation is prohibited. **Silent truncation of history is prohibited.**

---

## Operational refinements observed in legacy implementations

**Non-normative.** These are working renderings of the requirements already stated above,
harvested from the Concierge and Voice Identity documentation sets during the legacy
knowledge harvest and recorded here as evidence of what conformance looks like in
practice. They are rank-four implementation evidence. They add no requirement, and no
value or vocabulary below is canonical.

**Validation is not discovery.** One implementation states the boundary precisely:
configured membership establishes the target set, runtime checking may **disqualify** a
configured target that is missing or unavailable, and runtime checking may **never**
discover an unrelated replacement. Where every configured target is disqualified the
outcome is a deterministic refusal, not a substitution. This is the same prohibition
recorded in the Concierge contract, expressed as a runtime rule.

**A refusal carries its category, not only its reason.** The same implementation groups
refusal reasons into a small set of categories that separate *no authority for this
scope*, *not configured*, *dependency unavailable*, and *policy denied*, and requires the
explanatory fields to be present on every outcome — with the refusal-specific fields empty
on success rather than absent. Carrying the category alongside the reason is what keeps
the distinction in this document legible to a household after the fact.

**Retry eligibility belongs to the reason, not to the caller.** A second implementation
attaches retry eligibility to each individual failure reason: some conditions are
retryable as-is, some become retryable only after a corrective act such as re-enrollment,
and some are never retryable. A caller that retries uniformly cannot express any of that.

**A machine-safe reason code is not a household sentence.** That implementation
deliberately emits only governed reason codes and assigns the translation into household
language to the orchestrator. The separation is useful: it keeps the diagnostic vocabulary
stable while the sentence remains free to be phrased for the moment and the audience.

**Silence is an outcome, and must not be used to hide one.** An implementation that
classifies every result as *acted*, *answered*, *refused*, or *silently completed* records
the governing constraint plainly: silence is legitimate only where an action genuinely
succeeded and no refusal condition exists, and silence must never stand in for a refusal
or a denial. This is the operational form of the requirement that a resident must always
be able to learn why something did not happen.

---

## Related documents

- [../models/truth.md](../models/truth.md)
- [../models/decision-trace.md](../models/decision-trace.md)
- [../models/temporal-record.md](../models/temporal-record.md)
- [behavioral-governance.md](behavioral-governance.md)
- [explainability.md](explainability.md)
- [privacy.md](privacy.md)
- [adr-stable-endpoint-identity-and-network-boundary-independence.md](adr-stable-endpoint-identity-and-network-boundary-independence.md) — restates "validation is not discovery" explicitly for the network layer (**DL-87**, accepted at **#195**)
