# ADR: Resident Communication and Delivery Separation

> **Document status: Accepted ADR.**
> Establishes **P31** and **P32**, and accepted decisions **DL-28** and **DL-29**.
> Terminology: [../models/glossary.md](../models/glossary.md).

---

## Status

**Accepted.**

Adopted following the Resident Communication Constitutional Review and the Resident Communication
Architecture Review, Phase 2 — Communication Model.

This ADR creates **no new responsibility**. The seven responsibilities recorded in **DL-01** —
Foundation, Stewardship, Identity, Truth, Continuity, Operational Trust, Concierge — are unchanged.

---

## Context

### The Notification definition gap

[framework.md](framework.md) §1 assigns Foundation ownership of the canonical definition of
**Notification**. No such definition existed. There was no glossary entry, no model, and no contract
section.

A constitutional document assigned ownership of a definition that was never written. Under **P1**
— *every responsibility needs an owner* — this is a defect of the same class as the unowned Fact
history corrected by **P28**.

### The terminology fork

Seven words were circulating for one idea: *Communication*, *Notification*, *Message*,
*Announcement*, *Alert*, *Reminder*, *Advisory*. They appeared across both the canonical and the
Historical tiers with overlapping and inconsistent meanings.

This is the same pattern as the *Composite Room / Operational Space / Interaction Space / Listening
Area* fork that required **DL-12** to reverse across more than fifteen documents. It was still
confined to a small number of sentences and was therefore closed now rather than later.

### The communication ownership gap

Nothing owned the communication as a governed object. Specifically, nothing owned whether a
communication was delivered, received, acknowledged, still outstanding, expired, superseded,
suppressed, or undeliverable.

The two most serious were **suppression** and **non-delivery**. A home that decided to stay quiet
and cannot say so is in the same condition **P27** was written to prevent.

### P27 already presupposed the record

**P27** obliges the home to reconstruct what it observed, believed, knew, and decided, and why.
Answering *"why didn't you tell me?"* therefore already required a governed record of what was
originated, suppressed, attempted, delivered, and never delivered.

**P27 presupposed a communication record. Nothing owned it.** This ADR closes that gap, using the
same discovery method that produced **P28**.

### The embedded-history lesson, applied again

The accepted lesson recorded in
[adr-temporal-record-model.md](adr-temporal-record-model.md) is that history embedded as an array
inside a mutable record is a defect: it forces whole-record rewrites, truncates silently, and leaves
no tombstone.

A Communication carrying an embedded `delivery history` array would reproduce that defect exactly.
It is therefore prohibited by this ADR.

### What Home Assistant had already converged on, and where it stopped

Home Assistant provides mature **delivery** primitives and almost no **governance** primitives. It
has no audience model, no cross-surface communication identity, no suppression record, no
person-attributed acknowledgement, and no delivery record that survives recorder purge. The full
review is recorded below.

This asymmetry is itself the strongest argument for **P31**: the platform is a delivery layer, and a
domain model shaped around it would be a transport model wearing a domain model's name.

---

## Decision

### P31 — Communication is separate from delivery

> A **Communication** is a household interaction. It exists independently of the mechanism used to
> convey it.
>
> The responsibility that **originates** a Communication does not select how it is **delivered**.
> Origination establishes that something must be conveyed, to whom, and about what. Delivery
> establishes through which surface, at what moment, in what form, and whether at all.
>
> A Communication must never be defined as a notification, a push message, an announcement, an
> indicator, or any other transport artifact. Those are delivery outcomes.
>
> This principle governs the **model**, never the **surface**. It selects no delivery technology, no
> surface catalogue, no indicator scheme, and no escalation ladder.

### P32 — Permission to act does not imply permission to announce

> Authority to perform an action does not confer authority to speak about it, display it, or draw
> attention to it in the presence of whoever happens to be there.
>
> Outbound communication is governed by the same **Existence → Participation → Exposure → Authority**
> chain as any other disclosure, evaluated against **who can perceive the delivery surface**, not
> against who requested something.
>
> Where context cannot be established with sufficient confidence to deliver safely, **the delivery
> degrades — the governance does not.**

P32 is placed immediately after **P7** in [principles.md](principles.md). Its placement is part of
its meaning: P5, P6, and P7 govern what the home will reveal or do *when engaged*. P32 governs the
inverted case, in which the home speaks unprompted and the audience is not chosen by any requester.

### Canonical terminology

**Communication** is the canonical term for the object.

| Term | Disposition |
|---|---|
| **Communication** | Canonical — the object |
| **Delivery**, **Delivery Attempt**, **Delivery Surface** | Canonical — distinct, subordinate concepts |
| **Announcement** | Canonical — a delivery *outcome*: a Delivery made audibly to a shared surface. Never an object |
| **Urgency** | Canonical — time-criticality, governed by Operational Trust. Never a category |
| **Reminder**, **Alert** | Canonical — taxonomy **categories** only, never objects |
| **Advisory** | **Retained with its existing Stewardship meaning** — a judgement about what could be improved, distinct from an Alert. See [../patterns/advisory-patterns.md](../patterns/advisory-patterns.md). It is **not** a Communication category |
| **Notification** | **Superseded** as an HTBW domain term. Retained only as Home Assistant platform vocabulary |
| **Message** | **Superseded** as an HTBW domain term. Retained only for external provider content where the provider is the system of record |

The Notification definition gap is closed by **supersession, not definition**. Foundation's
definitional ownership in [framework.md](framework.md) §1 now names **Communication**.

### The Communication object

A Communication is a **small, governed record with a mutable Current Projection and a history of
Change Records**. It is never a growing document.

**Required:** Communication ID; Version Identity; Effective Time and Recorded Time; Provenance;
Originator reference; Subject reference; Intended Audience specification; Category; Urgency;
Significance reference; Originating Context Reference; Visibility Classification reference;
Retention Classification; Lifecycle State; Supersedes and Superseded-by references; Expiry
specification reference; minimal rendering projection; explanation references.

**Prohibited:**

| Prohibited field | Reason |
|---|---|
| A stored `context` value | Context is resolved by Truth and Room Context **at delivery time**. A stored context is a frozen snapshot that will silently become wrong. A **Governed Reference** to the Fact versions true at origination is required instead |
| A stored resolved `visibility` value | Visibility is Operational Trust's, re-evaluated at **each** Delivery Attempt. A stored value would survive a policy revocation — the **P30** failure mode |
| An embedded `delivery history` array | The embedded-audit-array defect. Delivery history is **Change Records referencing the Communication by Version Identity** |

### Category and Urgency are orthogonal

**Category** describes what a Communication is *about* and is proposed by the originator.
**Urgency** describes what it is *entitled to interrupt* and is determined by **Operational Trust**.

Merging the two axes would make the taxonomy the permission model, allowing an originator to
escalate its own interruption rights by choosing a category name. That is precisely what P32 exists
to prevent.

### The delivery outcome model is two-level

| Level | States |
|---|---|
| **Communication lifecycle** | Created, Suppressed, Acknowledged, Expired, Superseded, Resolved by origin, Undeliverable |
| **Delivery Attempt outcome** | Attempted, Delivered, Presented, Failed |

A Communication has exactly one current lifecycle state and may have many Delivery Attempts.
Flattening the two levels makes multi-surface delivery unrepresentable.

`Completed` is **rejected** as a state: it conflates *the Communication was dealt with* with *the
underlying condition was resolved*. The latter belongs to the originator. `Resolved by origin`
replaces it.

### Indication and content are separate deliveries

A **content-free indication** — that something is outstanding — discloses nothing and is therefore
permissible where content is not. Modelling indication and content as one act removes the safe
degradation path and forces a choice between silence and disclosure.

This is the architectural basis for *"You have one message waiting"* followed by an identity-gated
retrieval conversation.

### The Household Inbox is a projection

The Household Inbox is a **projection over outstanding Communications**, assembled on demand and
filtered by the viewer's authority at read time. It is not a persisted object, and no responsibility
owns it — in the same manner as **Historical Reconstruction** and **Evidence Package**.

A persisted inbox would survive a policy revocation until something remembered to rewrite it.

### Re-presentation, not following

A Communication has no location, and therefore cannot move, follow, or remain location-bound.
Location-boundness is a property of a **Delivery Attempt**.

Where a person moves and a Communication is still outstanding, Concierge may make a **new Delivery
Attempt** on a newly appropriate surface, re-evaluating P32 against the **new** audience. The
Communication is never duplicated.

### One escalation architecture

| Concept | Definition | Owner |
|---|---|---|
| **Delivery retry** | Repeating delivery **to the same audience** | **Concierge** |
| **Escalation** | Changing **the audience** to a more authoritative or accountable person | **Stewardship** (ladder, **OD-22**) and **Operational Trust** (authority) |

**There is one escalation architecture, and it already exists.** Retry is a delivery concern and is
never called escalation.

### Interruption is a governed action

Interruption is an **Operational Trust** concern, expressed at delivery by Concierge, and treated as
an **action-risk class** — the same mechanism that already governs unlocking a door.

A safety or critical classification is an Operational-Trust-granted **entitlement**, revocable and
explainable. **It is never a bypass.**

### Accepted decisions

| ID | Decision |
|---|---|
| **DL-28** | **Communication is separate from delivery** (P31) |
| **DL-29** | **Permission to act does not imply permission to announce** (P32) |

### Deliberately not decided

This ADR selects no delivery technology, no surface catalogue, no indicator scheme, no urgency
enumeration, no retry interval, no retention duration, and no identifier implementation. Those are
open decisions **OD-42** through **OD-58**.

---

## Responsibility impact

| Responsibility | Impact |
|---|---|
| **Foundation** | Owns the definitions of Communication, Delivery, Delivery Attempt, Delivery Surface, Urgency, and the delivery-outcome states. Replaces its former definitional ownership of *Notification*. Owns no Communication |
| **Stewardship** | Originates Communications about obligations and advisories. Owns the significance referenced by them and the single escalation ladder. **Does not own the resulting Communication** — unchanged from [framework.md](framework.md) §2 |
| **Identity** | Supplies candidate-person assertions for audience resolution and for attributing an acknowledgement. Decides no delivery |
| **Truth** | Supplies contextual person-presence and occupancy Facts that determine **who can perceive a surface**. Decides no delivery |
| **Continuity** | Owns the resident preference governing whether outstanding Communications are re-presented as a person moves, within the existing Follow-Me preference family |
| **Operational Trust** | Owns Urgency entitlement, interruption authority, audience eligibility, visibility classification, and retention classification for Communications |
| **Concierge** | Resolves audience to surfaces, decides delivery, suppression, retry, timing, and wording; **owns the delivery history and every state-transition record** |

**No new row is added to the History-ownership matrix.** Delivery is a decision, and the existing
row — *"Decision history, through Decision Traces — Concierge"* — already covers it.

---

## No new responsibility

This ADR creates **no** Communication, Messaging, Inbox, Delivery, or Escalation responsibility.

It creates **no** central delivery owner, **no** central inbox owner, and **no** second escalation
ladder.

The superseded "message authority" boundaries in
[adr-provenance-governance.md](adr-provenance-governance.md) and
[adr-household-memory-governance.md](adr-household-memory-governance.md) remain **Historical**.
**Their former ownership boundaries are not revived by this decision.**

---

## Alternatives considered

| | Alternative |
|---|---|
| **A** | Define *Notification* in the glossary and leave the other six terms in circulation |
| **B** | Model a Communication as a delivery instruction, with one object per surface |
| **C** | Adopt the Home Assistant notification object as the HTBW Communication object |
| **D** | Create a Communication responsibility, or a cross-cutting Communication owner with a store |
| **E** | Persist the Household Inbox as a first-class object |
| **F** | Give communications their own escalation ladder, separate from Stewardship's |
| **G** | Merge Category and Urgency into a single ordered taxonomy from Informational to Critical |

## Alternatives rejected, with reasons

| | Rejected because |
|---|---|
| **A** | Leaves six near-synonyms in circulation across both tiers. This is how the Composite Room fork propagated to more than fifteen documents before DL-12 had to reverse it |
| **B** | Makes *"was this conveyed?"* unanswerable across surfaces, and makes supersession and acknowledgement per-surface rather than per-matter. It is the transport leak P31 forbids, restated as a data model |
| **C** | Structurally unsuitable. Home Assistant has no audience model, no cross-surface communication identity, no suppression record, no governed retention, and no tombstone — gaps **G1**, **G2**, **G5**, **G7**, and **G8** below. Adopting it would make P27 unanswerable by construction |
| **D** | Violates **DL-01**. Origination is distributed and delivery is Concierge's; nothing is left unowned once the delivery record is placed. An eighth responsibility is unnecessary |
| **E** | ⚠️ **A persisted inbox survives a policy revocation.** If authority to see a Communication is withdrawn, a stored inbox still contains it until something rewrites it. This is the P30 failure mode applied to visibility. A projection is correct by construction. There is also no single household inbox — there are as many views as there are viewers |
| **F** | Two ladders would disagree about whether an accountable person has been reached, and **P27** could not answer *who was told, in what order, and why* — two histories, two truths. This is the Fact-history defect **P28** corrected, repeated |
| **G** | Makes the taxonomy the permission model. An originator could grant itself interruption rights by naming its own category, and P32 would become decorative |

---

## Privacy consequences

**Outbound communication inverts the initiative.** Every prior exposure rule governs what the home
reveals *when engaged*. An unsolicited delivery is not requested by the person who receives it, and
the audience is whoever can perceive the surface. This is a distinct risk shape and is why P32
exists.

| Consequence | Treatment |
|---|---|
| The right information delivered to the wrong ears | P32; audience evaluated against surface perceptibility, not against the addressee |
| Guests present when a private matter must be conveyed | Guest-presence constrains delivery of every audience. Existing rule in [privacy.md](privacy.md) |
| Sensitive content in a shared space | Content-free **indication** is the required degradation, followed by identity-gated retrieval |
| Uncertain identity or occupancy | The **delivery** degrades, never the governance. Existing guest-safe treatment applies |
| A stored visibility value outliving its policy | Prohibited. Visibility is a reference, re-evaluated per attempt |
| Communication content retained longer than needed | Content and metadata are **classified separately**. The fact that the home tried and failed may need a longer floor than what it tried to say |
| A suppressed communication leaving no trace | Suppression is an **Intentional Non-Action** and is traced under **P16** and **DL-15** |
| Health, medication, and pet-care reminders | Existing rule preserved and now architecturally supported: *reminders must be deliverable without disclosing content to an unintended audience* |

Retention floors for Communications are settled as a governed record class by **DL-47** and are never
stated without their
ceiling. Where a retention floor and a privacy ceiling conflict, **privacy governs the outcome**, and
the resulting limitation is itself recorded and remains explainable.

---

## Legal and regulatory non-claim

**This architecture does not claim to produce legal-grade evidence.**

HTBW does not assert court admissibility, legal chain-of-custody sufficiency, tamper-evidence
certification, forensic certification, regulatory compliance, or compliance with any legal retention
obligation.

Any legal, regulatory, insurance, investigative, or court-admissibility requirement requires separate
assessment outside this architecture.

---

## Life-safety non-claim

**HTBW is not a life-safety system.**

A safety-category Communication does not constitute smoke detection, carbon-monoxide detection,
water-leak protection, medical alerting, security monitoring, or emergency notification, and must
never be represented as a substitute for certified alarms, monitored services, or emergency services.

Delivery of a safety-category Communication is **best-effort**, is subject to the same suppression,
authority, and surface-availability constraints as any other Communication, and may fail silently at
the platform boundary.

**Safety is accepted as the seventh canonical Communication Category (DL-78).** Whether HTBW must defer
entirely to native alarms and certified devices for specific claims, and the disclaimer content and
survival across surfaces, remain open decision **OD-56**, narrowed but not closed by **DL-78**.

---

## Home Assistant First review

Conducted under **P21**. Documentation version **2026.8.2**.

### Documentation reviewed

| Capability | Documentation | Verified |
|---|---|---|
| Notifications (`notify`) | `https://www.home-assistant.io/integrations/notify/` | Yes |
| Persistent Notification | `https://www.home-assistant.io/integrations/persistent_notification/` | Yes |
| Assist Satellite | `https://www.home-assistant.io/integrations/assist_satellite/` | Yes |
| Text-to-speech | `https://www.home-assistant.io/integrations/tts/` | Yes |
| To-do list | `https://www.home-assistant.io/integrations/todo/` | Yes |
| Alert | `https://www.home-assistant.io/integrations/alert/` | Yes |
| Companion app notifications | `https://companion.home-assistant.io/docs/notifications/notifications-basic` | Yes |
| Actionable notifications | `https://companion.home-assistant.io/docs/notifications/actionable-notifications` | Yes |
| Repairs platform | `https://developers.home-assistant.io/docs/core/platform/repairs/` | Yes |
| Repairs | `https://www.home-assistant.io/integrations/repairs/` | Yes |
| Built-in intents, including `HassBroadcast` | `https://developers.home-assistant.io/docs/intent_builtin/` | Yes |

> **Not verified during this review:** dashboard visibility semantics, `media_player` delivery
> semantics, and voice-satellite indicator behaviour. **No links are recorded for them, and none are
> fabricated.** Open decisions that depend on those areas must not be closed on assumed behaviour.

### Capabilities found

| Capability | Evidence |
|---|---|
| Notify entities as delivery targets | `notify.send_message` targets notify entities; entity state is the date and time a message was last sent |
| Notify groups | Multiple devices addressed as one target |
| Persistent notifications with identity and replacement | `persistent_notification.create` / `dismiss` / `dismiss_all`; `notification_id` overwrites an existing notification with the same ID |
| Persistent-notification lifecycle triggers | `added`, `removed`, `updated`, `current` |
| Repeating alerts with acknowledgement | `alert` states `idle` / `on` / `off`, where `off` means the condition is true but was acknowledged; `repeat` accepts a list of intervals; `can_acknowledge`; `skip_first`; `done_message` |
| Outstanding-item tracking | `todo` entity state is the number of incomplete items, with triggers and conditions for completion |
| Audible announcement to a voice satellite | `assist_satellite.announce` |
| Ask a question and receive the response | `assist_satellite.ask_question` |
| Start a conversation from the satellite | `assist_satellite.start_conversation` |
| Satellite state observability | Triggers and conditions for idle, listening, processing, responding |
| Speech to a media player | `tts.speak`, `tts.say` |
| Supersession by tag | Companion `tag`; subsequent notifications take the place of one with the same tag |
| Withdrawal | `clear_notification` with a `tag` |
| Expiration | `timeout`, in seconds |
| Interruption ladder | iOS `interruption-level`: `passive`, `active`, `time-sensitive`, `critical`, with an explicit Focus-override column |
| Importance ladder | Android channel `importance`: `min`, `low`, `default`, `high`, `max` |
| Lock-screen sensitivity | `visibility`: `public`, `private`, `secret` |
| Actionable notifications with response events | `mobile_app_notification_action` fires with `action`, optional `reply_text`, and a `context` containing `id`, `parent_id`, and `user_id` |
| Notification dismissal event | `mobile_app_notification_cleared` |
| Step-up on an action | `authenticationRequired` — the device must be unlocked to use the action |
| Administrator-facing problem surface | Repairs issues carrying `severity`, `is_fixable`, `is_persistent`, `issue_domain`, `learn_more_url`, and translation placeholders |
| Guided correction | A repair flow, which walks the user through fixing a fixable issue |
| Issue dismissal | An ignored issue stays ignored across restarts, regardless of `is_persistent`, until it is explicitly deleted — by the integration, or by the user completing its repair flow — and then created again |
| Broadcast to satellites | The built-in `HassBroadcast` intent, which announces a message on other satellites, provided by `assist_satellite` |

### Repairs, evaluated and bounded

Repairs was evaluated under the **DL-30** burden of proof as a candidate communication surface. **It
is adopted for HTBW configuration defects and rejected as a communication mechanism.**

| Statement | Consequence |
|---|---|
| **A Repairs issue is not a Communication.** It has no audience, no Urgency entitlement, no delivery attempt, and no presentation outcome | Repairs cannot satisfy P31 or P32 |
| **Ignoring a Repairs issue is not a person-attributed acknowledgement.** Ignoring identifies nobody | Repairs cannot satisfy **OD-45**. Recorded there |
| **`IssueSeverity` is not resident-facing Urgency.** `CRITICAL`, `ERROR`, and `WARNING` are a developer-facing platform ladder, not a household entitlement governed by Operational Trust | Confirms **G9**. Resolved as **DL-77** |
| **Repairs is not an obligation store.** A household obligation is Stewardship-owned, carries significance and accountability, and uses the single escalation ladder | Repairs must not become a fourth list surface |
| **A broadcast targets surfaces, not an audience.** `HassBroadcast` and `assist_satellite.announce` address satellites; neither resolves who may perceive the announcement | Confirms **G1**. Recorded in **OD-52** |

**Neither Repairs nor broadcast replaces the Communication Model.** Repairs is adopted as the
preferred surface for HTBW integration configuration defects and administrator-correctable platform
problems only; the boundary is recorded in
[home-assistant-boundary.md](home-assistant-boundary.md) and its adoption scope is resolved as **DL-65**.

### Gaps

| # | Gap | Consequence |
|---|---|---|
| **G1** | **No audience model.** Targets are entities and devices, never people, roles, or authority classes | P32 has no native anchor |
| **G2** | **No cross-surface communication identity.** A phone notification, a satellite announcement, and a persistent notification about one matter are three unrelated objects | *"Was this conveyed?"* is natively unanswerable |
| **G3** | **Delivery is fire-and-forget.** Notify entity state records only when a message was last sent | `Delivered` and `Presented` are natively unattestable for most surfaces |
| **G4** | **Acknowledgement is not person-attributed at the domain level.** `alert` acknowledgement is an entity state change; dismissing a persistent notification identifies no one | `Acknowledged` requires HTBW-side identity binding. `context.user_id` on `mobile_app_notification_action` is the one native attribution path, and exists only for actionable notifications |
| **G5** | **No suppression record.** A notification not sent leaves no trace | Directly defeats P27 |
| **G6** | **Acknowledgement is not guaranteed to arrive.** The action event does not fire when the app is closed or crashes | Unknown must be representable and must never decay into *not acknowledged* |
| **G7** | **No governed retention.** Notification history is subject to recorder purge; persistent notifications are not governed records | Retention floors cannot be honoured natively |
| **G8** | **No tombstone.** Dismissal, clearing, and purge are indistinguishable from *nothing ever happened* | Violates the existing tombstone requirement |
| **G9** | **Urgency is per-platform and non-portable.** iOS interruption levels and Android channel importance are different ladders with different semantics, neither governed by household policy | Urgency must be an HTBW concept mapped downward, never adopted upward |
| **G10** | **Escalation is retry only.** `alert.repeat` changes timing, never audience | Confirms that retry and escalation are distinct |
| **G11** | **`alert` is condition-driven, not communication-driven.** It watches an entity state | Cannot represent a Communication whose subject is an Obligation rather than an entity |

### Conclusion

**Home Assistant is used for delivery and not for governance.** Every capability above is a
Delivery Surface implementation. `assist_satellite.start_conversation` is the natural implementation
of the retrieval conversation and `announce` of content-free indication. `notification_id` and `tag`
are candidate supersession mechanisms; `context.id`, `parent_id`, and `user_id` are candidate
correlation, causation, and acknowledger anchors already under **OD-38**.

`todo` is an outstanding-**obligation** surface, not a communication inbox, and must not be
conflated with one. `alert` is a useful **retry** implementation and must not be adopted as an
escalation model.

---

## Connected-storage implications

Narrow. Governed Communication records and their Change Records may justify connected storage **only
where a retention floor exceeds what native Home Assistant retention preserves**, on the basis of
gaps **G5**, **G7**, and **G8**.

This creates no general licence to store communication content outside Home Assistant, and no
communication content is stored in connected storage merely because it is convenient. See
[connected-storage.md](connected-storage.md).

---

## Delivery Surface Capability Model (DL-53)

**Accepted 2026-09-15**, resolving **OD-43**. Full capability model, ownership table, and worked
detail are recorded in [../models/communication.md](../models/communication.md) under *Delivery
Surface*; this section is the formal decision record.

### Decision

A Delivery Surface declares seven capability dimensions — Supported Modalities, Content Constraints,
Interactivity Capability, Persistence Behavior, Recipient Acknowledgement Capability, Presentation
Attestation Capability, and Recipient Attribution Capability — plus a **Potential Perceptibility**
declaration. The dimension set is extensible and is never a closed device, domain, or integration
list. **A Delivery Surface never declares itself private**, and no device type, integration type,
authentication state, media-browser visibility (**DL-44**), or dashboard-view `visible` setting is
sufficient evidence of privacy on its own.

### Home Assistant First review (P21, DL-30)

Conducted for this decision, extending the review already recorded above.

| Capability | Documentation | Verified | Finding |
|---|---|---|---|
| Dashboard view visibility | `https://www.home-assistant.io/dashboards/views/` | **Yes** | The `visible` property is a per-user **display toggle for the view tab only** — *"this is only for the display of the tabs; the URL path is still accessible"* regardless of setting. **Confirms it is not an authorization or privacy control** |
| `media_player` delivery semantics | `https://www.home-assistant.io/integrations/media_player/` | **Yes** | States (`playing`, `paused`, `idle`, …) and triggers (`started_playing`, `stopped_playing`, …) evidence that a surface **accepted and began rendering** media. **No acknowledgement, no per-listener evidence, and no presentation-attestation capability exists** |
| Voice-satellite indicator behaviour | `https://www.home-assistant.io/integrations/assist_satellite/` | **No** | The entity models command-processing lifecycle (`idle`, `listening`, `processing`, `responding`) and `announce` / `ask_question` / `start_conversation` actions. **No physical indicator (light/LED) behaviour is documented at this reference, and none is fabricated** |

This discharges the burden the ledger recorded against closing **OD-43**, **OD-55**, and **OD-57** on
assumed behaviour: dashboard visibility and `media_player` delivery semantics are now **located,
reviewed, and verified**. **OD-55** and **OD-57** still require their own closure, and the
voice-satellite indicator gap remains open evidence for whichever of them needs it.

### What this decision does not resolve

- **OD-52** — the audience *specification* model.
- **OD-55** — which surface classes can attest presentation, and on what evidence.
- **OD-57** — when content-free indication becomes mandatory.
- **OD-71** — the policy applied under audience uncertainty.
- **OD-73** — the mechanism by which Room Context is resolved for a non-room-bound surface. DL-53
  depends on whatever OD-73 accepts as one Truth input to a portable surface's perceptibility
  evaluation, and preempts none of its alternatives.

### Contradiction identified and resolved

The originating decision set proposed a fourth named scale — **Recipient-Attribution Assurance
Levels: `None` / `Low` / `Moderate` / `High`** — governing whether a confirmation or attribution
result is strong enough to authorize disclosure. **This duplicates an already accepted decision.**
**DL-40** already accepts an ordered, evidence-derived, mechanism-verified class set for exactly this
purpose — **Required Confirmation Strength: `None` < Verbal < Authenticated < Strong** — and **DL-37**
states plainly that **no second confirmation model exists**. Minting a second scale for the same
governance question would violate both. **Resolution: Recipient Attribution Capability is a declared
surface property** (what evidence a surface can supply), and **the strength gating a confirmation or
disclosure decision remains DL-40's Required Confirmation Strength; no new assurance scale is
created.** This is a correction to the supplied decision set, not an open question.

---

## Presentation Attestation Model (DL-54)

**Accepted 2026-09-15**, resolving **OD-55**. Full outcome model, invariants, and worked behaviour are
recorded in [../models/communication.md](../models/communication.md) under *Presentation Outcome*;
this section is the formal decision record and the Home Assistant First review.

### Decision

Presentation is a **technical claim only** — that an artifact was rendered, displayed, shown, spoken,
played, or otherwise made available through a Delivery Surface, using the modality and capability
actually invoked. It is distinct from Delivery, Perception, Acknowledgement, correctness, and
household-outcome satisfaction, none inferring another. A `Delivered` attempt's presentation status is
exactly one of four values: **Presented**, **Failed**, **Unknown**, **Attestation Unavailable** —
where `Attestation Unavailable` is a capability fact (the surface cannot attest at all) and `Unknown`
is a per-attempt evidentiary gap on a surface that sometimes can. Neither decays into "not presented".
Evaluation is by **modality and evidence actually returned**, never by device type, vendor, product
class, integration name, or Home Assistant entity domain.

### Home Assistant First review (P21, DL-30)

Conducted for this decision. **No undocumented capability is credited, and a successful service call
alone is never treated as presentation evidence** — only an independently observed state transition,
confirmed by the platform itself rather than by the calling side, is admitted as evidence.

| Surface / modality | Integration | Documented evidence | What it proves | What it does not prove | DL-30 result | Classification |
|---|---|---|---|---|---|---|
| Audio / video playback | `media_player` (generic) | `https://www.home-assistant.io/integrations/media_player/` — documented states `playing`/`paused`/`idle`/etc. and triggers `media_player.started_playing` | An independently observed state transition to `playing` after the specific request — the player itself began rendering | Which specific artifact rendered beyond what was commanded; that a person heard or saw it | **Discharged** for the state-transition case only | **Presented** may be claimed from the observed `playing` transition; **never** from service-call success alone |
| Sonos playback | `sonos` | `https://www.home-assistant.io/integrations/sonos/` — `media_player.play_media` with `announce: true`; standard `media_player` states apply | Same as generic `media_player`, plus a documented announce-overlay behaviour | Human perception; older/S1 hardware may not fully support `announce` | **Discharged** for state-transition evidence | **Presented** via observed state, as above |
| Music Assistant playback | `music_assistant` | `https://www.home-assistant.io/integrations/music_assistant/` — creates standard `media_player` entities; `music_assistant.play_announcement` | Same state-transition evidence as generic `media_player` | Same limits as above; a Home-Assistant-imported player appears duplicated in MA | **Discharged** | **Presented** via observed state |
| Camera-associated speaker | `unifiprotect` | `https://www.home-assistant.io/integrations/unifiprotect/` — camera speaker exposed as a `media_player` entity; documented troubleshooting shows failures surface as connectivity errors | Same `media_player` state-transition evidence; failures are diagnosable, not silent | Network presence is not presentation evidence | **Discharged** | **Presented** via observed state; network-online is **not** evidence |
| Voice assistant / Assist Satellite | `assist_satellite` | `https://www.home-assistant.io/integrations/assist_satellite/` — documented `announce`/`ask_question`/`start_conversation` actions and `started_responding` trigger ("triggers after…start playing back a response") | An independently observed transition to `responding` — the satellite itself began playback | Physical LED/light indicator behaviour (**separately, not documented — see below**); human perception | **Discharged** for the state-transition case | **Presented** may be claimed from the observed `responding` transition |
| Television, generic | `media_player` domain | Same generic `media_player` findings apply | Same as generic `media_player` | A `media_player` domain never itself proves visual capability | **Discharged** (state-transition only) | **Presented** via observed state; domain membership alone proves nothing |
| Roku | `roku` | `https://www.home-assistant.io/integrations/roku/` — documented `sensor.active_app`/`active_app_id` reflecting the platform's own report of the active application | Independent confirmation that the targeted application became active | That specific on-screen content within the app rendered; remote-command success (buttons may silently no-op per app) | **Discharged** for active-app confirmation only | **Presented** (app activation) may be claimed from the `active_app` sensor; remote-command completion alone is **not** evidence |
| Apple TV | `apple_tv` | `https://www.home-assistant.io/integrations/apple_tv/` — documented FAQ: *"Is it possible to see if a device is on without interacting with it? No"*; *"the tvOS apps themselves decide what commands they support"* | Very limited independent observability; official FAQ confirms remote-command success does not confirm the app actually acted | Presentation of any specific content | **Not discharged** beyond generic `media_player` state | **Presented** (playback) via observed `media_player` state only; all other claims **Attestation Unavailable** |
| LG webOS TV | `webostv` | `https://www.home-assistant.io/integrations/webostv/` — documented `notify` action displays a message on screen; documented known limitation that some firmware ignores the `icon` parameter without failing the call | A message-display **action exists**; no independently observed confirmation that it rendered | That the message was actually shown — the call can "succeed" while part of the payload is silently dropped, per the documented firmware limitation | **Not discharged** for render confirmation | **Attestation Unavailable** for the `notify` text-display path (service-call success only); **Presented** (playback) via observed generic `media_player` state for video/audio |
| Mobile notification | Companion App (`mobile_app`) | `https://companion.home-assistant.io/docs/notifications/notifications-basic` — full options reviewed (attachments, grouping, replacing, clearing, channels, TTS-on-device, interruption levels, presentation options, live activity); **no "displayed" event is documented anywhere** | Delivery/service acceptance only | Whether the notification was ever shown on the lock screen or in the shade | **Not discharged** | **Attestation Unavailable.** Only `mobile_app_notification_action` (tap) and `mobile_app_notification_cleared` (dismiss) exist, and both are interaction/acknowledgement evidence, never presentation evidence |
| `persistent_notification` | `persistent_notification` | `https://www.home-assistant.io/integrations/persistent_notification/` — documented triggers `added`/`removed`/`updated`/`current` describe the notification's existence in frontend state; `dismiss` requires user action | Existence-lifecycle only | That any person viewed the frontend at all | **Not discharged** | **Attestation Unavailable** |
| Dashboard / kiosk render | Lovelace frontend | `https://www.home-assistant.io/dashboards/views/` — reviewed for **DL-53**; no render-confirmation event is documented for any dashboard view | The `visible` property is a display-tab toggle only | That a view was rendered on any physical screen | **Not discharged** | **Attestation Unavailable** |

This is a genuine extension of the existing platform review recorded above (`Not verified during this
review: dashboard visibility semantics, media_player delivery semantics, and voice-satellite indicator
behaviour`). **Dashboard visibility and `media_player` delivery semantics are now verified** (see the
**DL-53** section and this table). **The physical voice-satellite light/LED indicator specifically
remains not verified and is not required by this decision** — Presented, where claimed for
`assist_satellite`, rests on the documented `responding` **state** transition, not on any indicator
light.

### What this decision does not resolve

- Any per-integration enumeration beyond the surfaces reviewed above; a newly reviewed integration
  follows the same evidentiary rule (independent observed state, never call-success alone).
- **OD-44** (delivery outcome semantics generally), **OD-45** (acknowledgement), **OD-54** (retry) —
  each receives an evidence update, not a closure, from this decision.

---

## Open decisions

| ID | Question |
|---|---|
| **OD-42** | Communication object persistence and Home Assistant representation — subordinate to OD-01, which now owns the persistence-mechanism residual alone |
| **OD-43** | **Resolved as DL-53** — Delivery Surface capability model, including perceptibility and presentation attestation |
| **OD-44** | Delivery outcome semantics across the two levels |
| **OD-45** | Acknowledgement semantics, acknowledger identification, and whether unacknowledged delivery is a failure |
| **OD-46** | **Resolved as DL-77.** Urgency is a fixed, cumulative four-level entitlement ladder, formally independent of Action-Risk Classification (**DL-76**) |
| **OD-47** | Household Inbox projection scope and refresh semantics |
| **OD-48** | Re-presentation preference and its relation to the Follow-Me preference family |
| **OD-49** | Communication retention floor and ceiling, with content and metadata classified separately — the retention rule is settled by DL-47; the separate classification and the values remain |
| **OD-50** | Escalation ladder semantics for communications, resolved into OD-22 |
| **OD-51** | Interruption action-risk class enumeration and defaults |
| **OD-52** | Audience specification model, including resolution of *anyone present with authority* |
| **OD-53** | **Resolved as DL-78** — Communication Category is a closed, seven-value, content-domain enumeration (Stewardship, Security, Care, Environment, Experience, System, Safety), structurally separate from Urgency, Operation Type, and Action-Risk Classification |
| **OD-54** | Delivery retry policy — attempts, intervals, surface progression, and give-up semantics |
| **OD-55** | **Resolved as DL-54** — Presentation Outcome model (Presented / Failed / Unknown / Attestation Unavailable), and the representation of unknown |
| **OD-56** | **Narrowed by DL-78** — Safety accepted as the seventh Category; disclaimer content/survival, written reconciliation, audience-bypass confirmation, dependency-missing behaviour, and certified-device deference remain open |
| **OD-57** | Indication versus content separation, and when content-free indication becomes mandatory |
| **OD-58** | Terminology supersession scope for *Notification* and *Message* |

Existing open decisions amended by this ADR: **OD-04** (priority order now explicitly includes
delivery ordering) and **OD-22** (the single escalation ladder now explicitly serves communications).

---

## Consequences

### Positive

- The Notification definition gap is closed, and Foundation's definitional ownership is real.
- The terminology fork is closed at seven terms rather than at fifteen documents.
- *"Why didn't you tell me?"* becomes answerable, completing **P27**.
- Suppression and non-delivery become recorded, explainable events rather than silence.
- Delivery surfaces may be added without changing the domain model, satisfying **P17** and **P25**.
- Communication history reuses the temporal model unchanged; no new record kind exists.

### Costs

- Every Delivery Attempt carries a governance evaluation, not only a transport call.
- `Presented` will frequently be `unknown`, and the home must say so rather than assume.
- Category and Urgency must be carried and reasoned about separately.

### Risks accepted

| Risk | Mitigation |
|---|---|
| The Communication object grows into a document | Prohibited fields stated in this ADR and in the model |
| A surface catalogue enters the canonical model | Delivery Surface is a capability abstraction with no enumeration |
| Category becomes the permission model | Category and Urgency separated, with Urgency granted by Operational Trust |
| A second escalation ladder emerges | Retry and escalation distinguished; OD-50 resolved into OD-22 |
| A persisted inbox survives a revocation | Inbox is a projection, evaluated at read time |
| `Presented` is inferred from `Delivered` | Unknown is representable and required; **P15** applies |
| A communication-specific history mechanism fragments the temporal model | Explicit reuse of Change Records required |
| Safety category implies a life-safety claim | Life-safety non-claim; **OD-56** |

---

## Validation requirements

1. **Terminology consistency** — *Communication* used consistently; *Notification* and *Message*
   recorded as superseded and not used as domain terms in the canonical tier.
2. **No new responsibility** — no Communication, Messaging, Inbox, Delivery, or Escalation
   responsibility; no central delivery owner; no central inbox owner.
3. **Prohibited fields** — no canonical document describes a stored context value, a stored resolved
   visibility value, or an embedded delivery-history array on a Communication.
4. **Category and Urgency separation** — stated and never collapsed.
5. **Single escalation architecture** — retry and escalation distinguished; no second ladder.
6. **Indication versus content separation** — present wherever shared-surface delivery is described.
7. **Suppression is traced** — suppression referenced as an Intentional Non-Action from failure
   behaviour and from the Decision Trace model.
8. **Silent non-delivery prohibited** — stated in failure and degradation behaviour.
9. **Life-safety non-claim** present verbatim in the required documents, and no document asserts
   life-safety, emergency, or monitoring sufficiency.
10. **Legal and regulatory non-claim** unaffected and still present in exactly its four documents,
    plus this ADR.
11. **Scenario walkthrough** — *"Why didn't you tell me the garage was open?"* answerable end to end
    as the joint test of P27, P31, and P32.
12. **Constitutional boundary** — P31 and P32 name no surface, technology, category enumeration,
    urgency scale, retry interval, or identifier scheme.

---

## Related documents

- [principles.md](principles.md)
- [north-star.md](north-star.md)
- [framework.md](framework.md)
- [privacy.md](privacy.md)
- [explainability.md](explainability.md)
- [failure-and-degradation.md](failure-and-degradation.md)
- [home-assistant-boundary.md](home-assistant-boundary.md)
- [connected-storage.md](connected-storage.md)
- [adr-historical-explainability-and-historical-truth.md](adr-historical-explainability-and-historical-truth.md)
- [adr-temporal-record-model.md](adr-temporal-record-model.md)
- [../models/communication.md](../models/communication.md)
- [../models/temporal-record.md](../models/temporal-record.md)
- [../models/decision-trace.md](../models/decision-trace.md)
- [../models/glossary.md](../models/glossary.md)
- [../contracts/concierge-contract.md](../contracts/concierge-contract.md)
- [../contracts/operational-trust-contract.md](../contracts/operational-trust-contract.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
