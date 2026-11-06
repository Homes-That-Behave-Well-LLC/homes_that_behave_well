# ADR: Contextual Governed-Acceptance Placement

> **Document status: Canonical ADR.**
> Status: **Accepted** 2026-11-06. Records **DL-148** (issue **#203**, formal acceptance review PASS).
> Resolves **OD-93** in full.
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Terminology: [../models/operational-trust.md](../models/operational-trust.md),
> [../models/communication.md](../models/communication.md),
> [../contracts/concierge-contract.md](../contracts/concierge-contract.md).

---

## 1. Status

**Accepted 2026-11-06.** Resolves every OD-93 acceptance criterion and all five of its remaining
questions. This ADR creates **no new responsibility**, **no new authority tier**, **no new acceptance
record class**, **no centralized acceptance store**, and **no confirmation mechanism**. It does not
reopen **DL-30**, **DL-37**, **DL-40**, **DL-51**, **DL-52**, **DL-56**, **DL-57**, **DL-71**, **DL-75**,
**DL-76**, **DL-79**, **DL-104**, **DL-109**, or **DL-110** — each is consumed unchanged. It does not
redecide **DL-145** or **DL-146**'s own acceptance semantics.

---

## 2. Context — the premise this issue rejects

OD-93 was raised when **DL-109** and **DL-110** independently arrived at the identical residual: a
generic onboarding/acceptance-capture surface, shared by commissioning acceptance (DL-109), legacy
adoption offer/review (DL-110), and — by DL-146's later independent confirmation — identity-artifact-
invalidation re-enrollment acknowledgement. Evidence posted to this issue during the DL-145/DL-146
closures added two further candidate consumers: the Voice Identity Encoder Migration Policy A/B choice
and the Breaking Identity Update administrator acknowledgement (both **DL-145**).

**The premise under evaluation — that sharing an acceptance-record shape implies sharing a user-
interface destination — is rejected.** The Owner directly supplied the resolving principle:

> **Shared governance mechanics ≠ shared user-interface destination.**

HTBW does not create a centralized **Household Acceptances** page, acceptance inbox, approval center,
consent dashboard, or pending-acceptance queue merely because several governed acceptance events share
**DL-109**'s record shape (actor, scope, authority, granted/effective time, version). The record shape
is governance mechanics underneath the experience. **The interaction belongs with the object or action
being configured.**

---

## 3. Decision — contextual placement

**A governed acceptance is presented at the authoritative interaction surface for the object, Person,
capability, configuration, or lifecycle event to which the acceptance applies.**

This is a refinement of the issue's own Option B (separate surfaces per acceptance type), **not**
Option A (one shared surface) and **not** unrefined Option C (a minimal shared "Household Acceptances"
listing surface) — each rejected as the governing model in §5. The refinement guards against Option
B's own risk of inventing unrelated UX per case: placement is **separate**, but it is governed by one
shared rule (this ADR) and reuses **Home Assistant-native interaction patterns** wherever they fit
(§31), so the household does not actually encounter inconsistent, ad hoc experiences.

---

## 4. Shared record shape does not imply shared surface

**This sentence is explicitly canonical:** shared acceptance-record shape does not imply shared
acceptance surface. **DL-109** supplies shared underlying fields — actor, scope, granted/effective
time, version — as **governance mechanics**, never as evidence that every acceptance using that shape
belongs on the same screen. "Same fields" does not imply "same screen." The interaction is placed
according to the scope of the thing being accepted, decided case by case in §§6–12, never inferred
from the record shape alone.

---

## 5. No centralized Household Acceptances surface, store, or responsibility

HTBW does **not** create:

- a centralized **Household Acceptances** page, acceptance inbox, approval center, consent dashboard,
  or pending-acceptance queue;
- a **Household Acceptance** object, a **Pending Acceptance** record class, or any acceptance store
  independent of each acceptance's own owning architecture;
- an **Acceptance**, **Consent**, or **Approval** responsibility.

Existing acceptance records remain authoritative according to their owning architecture (**DL-56**'s
consent record, **DL-109**'s generalized acceptance-record shape, each reused unchanged). If a future
UI needs to display outstanding governed actions, it may only be a **projection** over existing
authoritative state under future accepted projection architecture (§28) — **not decided here**.

---

## 6. Person-scoped acceptance

**Person-specific governed choices belong with Person setup/configuration when the choice configures
that Person.** This includes Voice Identity participation, Voiceprint enrollment, retained-evidence
consent where applicable to the Person (**DL-56**), and other Person-specific capability enablement or
authority. Example flow: **Person → Voice Identity → enable/configure → disclosure and applicable
Person consent → enrollment.** The act of creating the Voiceprint follows the already-accepted Voice
Identity enrollment/consent architecture unchanged. The Person is never redirected to a disconnected
"Household Acceptances → Voice Identity consent" screen.

---

## 7. Person-scoped Operational Trust capability settings

Where a household enables or configures a Person-specific capability governed by Operational Trust, the
flow is: **Person → relevant capability/trust configuration → required disclosure/acknowledgement/
consent → capability setting becomes authoritative.** Person-specific capability consent is never
collected in a disconnected, generic acceptance surface. **Operational Trust remains the authority**
(§26); the contextual surface only presents the already-governed requirement.

---

## 8. Household/Integration-scoped policy — DL-145's A/B choice

**Household/Integration-scoped governed choices belong with HTBW Integration configuration/options.**
The **DL-145** Voice Identity Encoder Migration Policy (Option A — retain enrollment recordings for
potential regeneration; Option B — delete after successful Voiceprint creation/validation) belongs at
**HTBW Integration → Voice Identity Integration settings/options**, consistent with DL-145's own §2
("Initial Integration configuration — required policy choice"). It does **not** belong in Person
Configuration, Room Configuration, or a centralized acceptance queue. **Person consent remains
separately evaluated when a Person actually enrolls** (§6) — the two axes DL-145 already keeps
independent are never collapsed into one screen.

---

## 9. Breaking Identity Update acknowledgement placement

A **DL-145** Breaking Identity Update acknowledgement belongs at the **update/migration lifecycle
event**: Breaking Identity Update detected → household impact calculated (counts of automatic
regeneration versus manual re-enrollment, per DL-145) → administrator presented the migration impact →
review affected Persons → acknowledge-and-continue or cancel/defer → migration proceeds only according
to DL-145. This acknowledgement is never placed permanently in a generic acceptance center — it exists
because a specific breaking update is about to occur, and the lifecycle event is its natural context.
**Existing Home Assistant configuration/update interaction patterns are used wherever they satisfy the
requirement** (§31); no independent HTBW updater, notification center, or confirmation framework is
invented.

---

## 10. Manual Voice Identity re-enrollment placement — DL-146

**DL-146 remains fully authoritative and is not reopened.** A Person classified manual-re-enrollment-
required receives a governed Communication (**DL-142**, Category System). Conceptual flow: Identity
determines manual re-enrollment required → governed Communication → authorized delivery → affected
Person follows the action → Person/Voice Identity enrollment context (§6) → replacement Voiceprint
creation. **The Communication is not itself an acceptance surface** (§15) — it is the governed
mechanism that informs the Person action is required and leads them to the contextual Voice Identity
setup already defined in §6. No "Household Acceptances → Pending re-enrollment" surface is created.

---

## 11. Legacy adoption placement — DL-110

**DL-110 remains fully authoritative and is not reopened.** Legacy adoption is offered and reviewed in
the authoritative management/configuration context of the capability, artifact, or product eligible for
adoption: HTBW detects an adoptable legacy artifact → the relevant management/configuration context
indicates adoption is available → the household reviews the adoption consequences (unit, destination,
provenance, incomplete-history disclosure, artifact-custody outcome, per DL-110 §4) → accept or skip →
the DL-110 lifecycle follows. Not every adoption possibility is routed into a global acceptance queue.
**Skip remains first-class and reofferable** (§19), exactly as DL-110 already states.

---

## 12. Commissioning acceptance placement — DL-109

**DL-109 remains fully authoritative and is not reopened.** Commissioning/governance-boundary
acceptance (the generalized **DL-79** shape) belongs in the commissioning/configuration context of the
capability being commissioned or enabled: configure/commission the capability → acceptance requirement
becomes relevant → contextual review → the authorized actor accepts, declines, or defers as current
semantics permit → the **DL-109** acceptance record is written. Technical setup alone never implies
household acceptance (DL-79, DL-109, unchanged) — but that requirement does not, by itself, justify a
detached central acceptance UI either.

---

## 13. Room-level configuration

Where a governed choice genuinely belongs to **Room Configuration**, it is presented in Room
Configuration. It is never routed to Person or Integration settings merely because it requires
acknowledgement. This ADR establishes contextual placement generally — Person and Integration
placement (§§6–8) are two instances of the general rule, not its entire scope — and Room Configuration's
existing ownership architecture is preserved unchanged.

---

## 14. Lifecycle-event placement, generally

Some governed acceptances exist only because an event occurred — a Breaking Identity Update, an
adoption opportunity discovered, an identity-artifact invalidation, a future migration event. These
belong at the event/action context, potentially entered through a governed Communication (§15) or a
native Home Assistant interaction (§31). An event-specific acceptance with no persistent setting of its
own is never forced to appear as a permanent configuration field.

---

## 15. Communication is not acceptance authority

A Communication may tell a Person that action is required, review is available, or configuration needs
attention. **Communication delivery does not itself constitute acceptance**, unless the governing
decision explicitly maps an authorized action back to the accepted authority. **DL-142 remains:
Communication ≠ acceptance authority.** Example: DL-146's Communication ("Your Voice Identity needs to
be set up again") — viewing or dismissing the notification neither creates the replacement Voiceprint
nor satisfies re-enrollment; only completing the contextual Voice Identity flow (§6, §10) does.

---

## 16. No general onboarding architecture required; first-run is not a governance owner

**OD-93 does not invent a generic HTBW onboarding subsystem.** Initial setup may contain contextual
configuration steps; Person setup may contain Person-specific capability configuration; Integration
setup may contain Integration-level policy; Room setup may contain Room-level configuration; a later
lifecycle event may produce its own contextual interaction. These are never forced into one onboarding
abstraction. **If a first-run/setup experience orchestrates several contextual configuration
activities, that orchestration does not become authority** for consent, Operational Trust, Identity,
Person Configuration, Integration Configuration, adoption, or commissioning — the underlying
responsibility remains authoritative, and the first-run experience is presentation/orchestration only,
exactly as **Concierge** already is (§26).

---

## 17. Detection belongs to the owning capability/lifecycle

**The interaction surface does not independently detect governance events.** The owning capability or
lifecycle supplies the condition that makes the interaction relevant:

| Case | Detection owner |
|---|---|
| Legacy adoption | Asset/capability architecture detects an adoptable legacy artifact (**DL-110**) |
| Voice Identity policy | Initial Integration configuration knows the policy has not yet been established (**DL-145**) |
| Breaking Identity Update | DL-145 compatibility analysis establishes acknowledgement is required |
| Manual re-enrollment | Identity/**DL-146** determines a Person requires action |
| Commissioning | The commissioning/configuration lifecycle determines acceptance is required before the governed action proceeds (**DL-109**) |

OD-93 invents no parallel detection logic.

---

## 18. Detection mechanics are implementation mapping

**OD-93 defines only that the owning lifecycle/capability must provide an authoritative, detectable
condition sufficient to invoke the contextual interaction.** It does not prescribe an event-bus topic,
sensor entity, polling interval, callback, database query, UI trigger, automation, or WebSocket event,
unless existing canonical architecture already requires it. Those remain implementation mapping.

---

## 19. Revisiting a deferred or skipped choice

A skipped or deferred acceptance is revisited from the **same authoritative contextual configuration/
lifecycle surface**, never a central queue:

- DL-110 adoption skipped → the legacy artifact remains unmanaged per DL-110 → the household later
  enters that capability/artifact's management surface → adoption may be offered again (DL-110's own
  "Skip is first-class and reofferable," unchanged).
- DL-145 household policy → Integration Options always shows the current policy → the household may
  intentionally change Option A ↔ Option B.
- A Person capability disabled → Person configuration shows it currently disabled → the household may
  later reconsider it there.

---

## 20. No nagging

A skipped or deferred choice must not produce repeated disruptive prompts merely because it remains
available. Re-offering uses existing Communication and lifecycle semantics, and occurs only when: the
household intentionally revisits the relevant configuration context; the underlying accepted lifecycle
explicitly requires re-presentation; a materially changed condition makes the decision newly
consequential; or current governance otherwise requires notification. **No hourly reminders, restart
prompts, periodic acceptance nudges, or startup blockers are invented.**

---

## 21. Ordinary HTBW operation is never gated

**No acceptance managed by this placement decision becomes a general startup requirement**, unless its
own governing decision already requires the specific capability/action to be gated:

- Person declines Voice Identity → Voice Identity unavailable for that Person → HTBW continues.
- Legacy adoption skipped → legacy state remains per DL-110 → HTBW continues.
- Breaking Identity Update deferred → the current compatible Voice Identity state remains where DL-145
  permits → ordinary HTBW operation continues.

**"Complete all acceptances before Home can start" is never created.** This directly extends **DL-51**'s
"HTBW must never require Asset Intelligence to be installed" to every acceptance this ADR places.

---

## 22. Action-specific gating remains valid

Ordinary HTBW startup/operation (§21) is distinct from a **specific protected action or capability**. A
specific capability may still require its own accepted authorization/consent before it operates — that
does not mean HTBW as a whole is blocked. **Operational Trust/DL-76 remains authoritative for protected
operations**, exactly as before this decision.

---

## 23. Minimum review content

Every contextual acceptance presents enough information for the authorized Person/administrator to
understand: what is being enabled/adopted/changed; scope; material consequence; relevant retention/
privacy consequence where applicable; whether the choice is reversible; what happens if declined/
skipped/deferred; the identity of the governed object/capability where relevant; and the acceptance
version/governance boundary where current acceptance-record architecture requires it. **Exact wording
or visual design is never prescribed here.**

---

## 24. Review content comes from the owning decision

OD-93 invents no review semantics. **DL-145** supplies the A/B consequences, retention implications,
breaking-update impact, and regeneration/manual-re-enrollment consequence. **DL-110** supplies adoption
consequences, skip behavior, and custody/coexistence semantics. **DL-109** supplies commissioning
acceptance requirements. **DL-146** supplies the manual-re-enrollment condition/action. The contextual
surface renders the already-accepted information; it never reinterprets it.

---

## 25. Future aggregated-attention UX

Not prohibited. **If** a future household UX needs to show "things requiring your attention," that
surface may be a projection over existing obligations/Communications/configuration state, under future
accepted architecture. **It must never become a second authority or a new acceptance store.** This ADR
does not decide or implement that future projection.

---

## 26. Concierge role

**Concierge orchestrates. It does not own everything it consumes** — the contract's own existing
statement, reused directly. Concierge may orchestrate/present whatever contextual interaction this ADR
places. Concierge does **not** own acceptance, consent, authorization, Person Configuration, Integration
Configuration, adoption semantics, or commissioning semantics. No central Concierge Acceptance service
is created. If Assist is used to ask about an acceptance, Assist/Concierge may explain the current
governed state and, where supported, direct the Person to the authoritative interaction — **it must not
bypass authorization** (§34).

---

## 27. Operational Trust role

**Operational Trust continues to own authorization, unchanged.** A Person configuring a capability does
not automatically mean authorization is valid — the action must still satisfy the existing Role/
Authority Class (**DL-71**), Action-Risk Classification (**DL-76**), requester identity, scope, and
every other current trust/consent requirement. **OD-93 creates no new confirmation tier.**

---

## 28. Acceptance record

Where an underlying decision requires the **DL-109** acceptance-record shape (actor, scope, granted/
effective time, version, and any other existing required fields), the interaction surface **writes or
initiates creation of that governed record through the authoritative owning capability**. The surface
itself is never the authority, and **no Acceptance Store is created** (§5).

---

## 29. Privacy

Contextual placement itself helps minimize disclosure: Person-specific consent does not appear
unnecessarily in household-wide UI; a Breaking Identity Update review shows only the affected-Person
information the authorized administrator is permitted to see; a Communication to an affected Person
never exposes another Person's state (consistent with DL-146's own unidentified-person-policy
restatement). **OD-93 creates no new privacy policy** — existing Operational Trust/privacy architecture
governs unchanged.

---

## 30. Explainability

Where authorized, the Home can explain: what acceptance/choice applies; what object/capability it
belongs to; who accepted or changed it, where current records permit disclosure; when; the applicable
version; whether it was skipped or deferred; where the authoritative configuration now lives; and what
consequence currently follows. **Acceptance contents are never duplicated into Explainability — governed
references are used** (consistent with `decision-trace.md`'s existing reference-not-copy discipline).

---

## 31. Home Assistant First

Native Home Assistant patterns are evaluated before introducing HTBW-specific interaction
infrastructure, reusing `home-assistant-boundary.md`'s own verified-facilities sweep, which already
names **Config flows and options flows** and **Repairs issues and guided repair flows** as verified
native constructs HTBW may build against. The right native pattern is matched to the right
responsibility, never forced:

| Governed object | Native pattern used |
|---|---|
| Integration-scoped option (**DL-145** A/B policy) | Integration **Options Flow** |
| Person-specific capability (Voice Identity participation, Voiceprint enrollment) | Person/capability management surface |
| Breaking update acknowledgement | Update/migration/**reconfigure**-style interaction |
| Required Person action (manual re-enrollment) | Governed Communication linking to the relevant configuration action (never Config Flow itself) |

**Home Assistant First does not mean "put everything in Config Flow."** `home-assistant-boundary.md`'s
own Repairs-boundary section already establishes that Repairs is a **surface for an administrator-
correctable defect**, never an obligation store and never a Communication — consistent with this ADR's
own rule that a governed acceptance is never confused with a defect-correction surface. If native
facilities prove insufficient for a specific case, that must be documented before HTBW-specific
presentation is defined — not assumed here for any of the eight cases in §32, each of which already has
a documented native-pattern fit.

---

## 32. Required acceptance-placement matrix

| Acceptance / governed choice | Scope | Owning responsibility | Authoritative contextual surface | Detection source | Minimum review contents | Available actions | Authoritative record/state | How revisited | Communication behavior | HA-native pattern | Rationale |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **DL-109** commissioning acceptance | Capability/Governance boundary | Operational Trust (authorization); the owning capability (requirement) | Commissioning/configuration context of the capability | Commissioning lifecycle (§17) | §23 | Accept / decline / defer | DL-109 acceptance record | Re-enter the capability's own commissioning context | None required by default | Config Flow / in-capability setup | §12 |
| **DL-110** legacy adoption offer/review | Artifact/capability/product | Foundation (custody); Operational Trust (authorization) | Management/configuration context of the adoptable artifact | Asset/capability architecture detects adoptable content | §24 (unit, destination, provenance, custody, incomplete-history) | Accept / Skip (first-class, reofferable) / Refuse (unmappable content only) | DL-110 lifecycle record | Re-enter the artifact's own management context | None required by default | In-capability management surface | §11 |
| Person Voice Identity enablement/consent | Person | Identity (evidence); Operational Trust (authorization) | Person/Voice Identity configuration | Person configuration itself | §24 (purpose, scope, revocability) | Enable/disable; consent/withdraw | DL-56 consent record | Return to Person/Voice Identity configuration | None required by default | Person/capability management surface | §6 |
| Voiceprint enrollment | Person | Identity; Voice Identity runtime | Person/Voice Identity configuration | Person configuration itself | §24 | Enroll; decline | DL-56 consent + resulting Voiceprint (DL-144) | Return to Person/Voice Identity configuration | None required by default | Person/capability management surface | §6 |
| Person-scoped Operational Trust/capability enablement | Person | Operational Trust | Person/relevant capability configuration | Person configuration itself | §24 | Enable/disable | Person's own capability setting | Return to Person/capability configuration | None required by default | Person/capability management surface | §7 |
| **DL-145** Voice Identity Encoder Migration Policy (A/B) | Household/Integration | Identity (policy); Foundation (Integration configuration) | HTBW Integration configuration/options | Initial Integration configuration (policy not yet established) | §24 (Option A/B consequence) | Choose A or B; change later | Standing Integration-scoped policy | Integration Options always shows current policy | None required by default | Integration **Options Flow** | §8 |
| **DL-145** Breaking Identity Update acknowledgement | Household (administrator) | Identity (impact calculation); Operational Trust (authorization) | Update/migration lifecycle event | DL-145 compatibility analysis | §24 (affected-Person counts, regen vs. manual) | Acknowledge-and-continue / cancel-defer | DL-109 acceptance record, Update/migration state | Re-enter update/migration context when update is reattempted | Administrator notified of pending update impact | Update/migration/**reconfigure**-style interaction | §9 |
| **DL-146** manual Voice Identity re-enrollment action | Person | Identity (determination); Concierge (delivery) | Governed Communication → Person/Voice Identity configuration (§6) | Identity/DL-146 determination | §24 (why action is required) | Follow action → re-enroll; defer | Replacement Voiceprint (DL-144) or other terminal disposition (DL-146) | Communication persists until actioned (DL-142); Person/Voice Identity configuration always available | Governed Communication (DL-142, Category System); Communication ≠ acceptance (§15) | Communication link to Person/capability management surface | §10 |

No acceptance is invented where current architecture does not actually require one.

---

## 33. Required answers to OD-93

| Question | Answer |
|---|---|
| **Where?** | Contextually, at the authoritative Person, capability, Integration, commissioning, adoption, or lifecycle-event surface. No centralized Household Acceptances surface |
| **One surface or separate?** | Separate contextual surfaces, using common governance mechanics (DL-109's record shape) and native HA interaction patterns. Shared record shape does not imply shared UI (§4) |
| **Detection?** | The owning capability/lifecycle detects the condition requiring interaction (§17). Exact trigger mechanics are implementation mapping (§18) |
| **Revisit/reoffer?** | Return to the authoritative contextual configuration/management surface (§19). Reoffer only when intentionally revisited or when the underlying lifecycle materially changes. No nagging (§20) |
| **Minimum disclosure?** | Enough to understand subject/object, scope, consequence, privacy/retention effect where applicable, reversibility, decline/skip/defer consequence, and applicable governance/version (§23). Exact wording/layout is implementation/UX mapping |

---

## 34. Explicit non-goals

This ADR does **not**: implement any UI; execute legacy adoption, Voice Identity enrollment, Breaking
Identity Update, commissioning, or Person Configuration implementation; create an Acceptance,
Consent, or Approval responsibility; create a Household Acceptance store, inbox, queue, or new record
class; create a new authority tier or confirmation mechanism; decide or implement a future aggregated-
attention projection (§25); redecide DL-109's, DL-110's, DL-145's, or DL-146's own acceptance semantics;
or reopen DL-51, DL-52, DL-56, DL-71, DL-76, or DL-79.

---

## 35. Related decisions

**DL-30** · **DL-37** · **DL-40** · **DL-51** · **DL-52** · **DL-56** · **DL-57** · **DL-71** · **DL-75**
· **DL-76** · **DL-79** · **DL-104** · **DL-109** · **DL-110** · **DL-142** · **DL-144** · **DL-145** ·
**DL-146** — each consumed unchanged, none reopened.

## 36. Related documents

- [../models/operational-trust.md](../models/operational-trust.md)
- [../models/communication.md](../models/communication.md)
- [../contracts/concierge-contract.md](../contracts/concierge-contract.md)
- [../models/person-and-identity.md](../models/person-and-identity.md)
- [../contracts/identity-contract.md](../contracts/identity-contract.md)
- [home-assistant-boundary.md](home-assistant-boundary.md)
- [adr-product-disposition-and-legacy-adoption.md](adr-product-disposition-and-legacy-adoption.md)
  (**DL-110**)
- [adr-voice-identity-enrollment-evidence-retention-and-regeneration.md](adr-voice-identity-enrollment-evidence-retention-and-regeneration.md)
  (**DL-145**)
- [adr-identity-artifact-invalidation-as-a-governed-household-event.md](adr-identity-artifact-invalidation-as-a-governed-household-event.md)
  (**DL-146**)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
