# ADR: Communication Object Persistence and Home Assistant Representation

> **Document status: Canonical ADR.**
> Status: **Accepted** 2026-11-05. Records **DL-142** (issue **#112**, formal acceptance review PASS).
> Resolves **OD-42** in full.
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Terminology: [../models/glossary.md](../models/glossary.md),
> [../models/communication.md](../models/communication.md),
> [adr-resident-communication-and-delivery-separation.md](adr-resident-communication-and-delivery-separation.md).

---

## Status

**Accepted 2026-11-05.** Resolves every OD-42 acceptance criterion. This ADR creates **no Communication,
Messaging, Inbox, or Delivery responsibility**, **no second Recorder**, **no persisted Household Inbox**,
**no notification shadow store**, and **no endpoint-specific Communication store**. It does not reopen
**DL-28**, **DL-31**, **DL-42**, **DL-46**, **DL-47**, **DL-53**, **DL-77**, **DL-78**, **DL-88**,
**DL-90**, **DL-92**, **DL-94**, **DL-95**, **DL-96**, **DL-98**, **DL-99**, **DL-104**, **DL-113**,
**DL-114**, **DL-136**, amended **DL-137**, **DL-138**, **DL-140**, or **DL-141** — each is consumed
unchanged.

---

## Context

OD-42's own Status table named its single genuine blocker as **OD-01** ("the persistence-mechanism
residual is owned there alone"). OD-01 is resolved as **DL-31**/**DL-92**. The issue's remaining
questions (whether a Communication persists before delivery, which fields survive, whether it has a
native Home Assistant representation, how an outstanding Communication survives a restart without an
Inbox store, and whether it follows DL-92 or needs an exception) are answered by applying already-
accepted architecture directly — `communication.md`'s own text already describes the Communication
object as **"a small governed record with a mutable Current Projection and a history of Change
Records"**, which is precisely the record shape DL-92 already governs.

**Owner direction governing this closure:** a Communication is the authoritative governed HTBW record;
the Household Inbox, Home Assistant Notifications, and delivery artifacts are never the Communication
store; durability follows lifecycle, not a blanket always/never rule; and for delivery into Home
Assistant-native notification experiences, HTBW uses native Home Assistant Notifications mechanisms
unless a governed requirement proves them insufficient.

---

## Decision

### 1. Communication is the authoritative governed record

Restating **DL-28** unchanged: a Communication exists independently of transport, notification
technology, presentation surface, or the Household Inbox. It is never defined as a notification, push
message, announcement, indicator, email, or spoken phrase. **Delivery is a separate concern.** This
decision adds only *how* the authoritative record is made durable — it does not redefine what a
Communication is.

### 2. Durability follows Communication lifecycle

Resolving Remaining Question 1 precisely, rejecting both extremes recorded in the issue's own Option
table: **neither** does every instantiated Communication require immediate durable persistence
regardless of outcome, **nor** may a Communication remain in-memory-only until some later event.

**Canonical rule: a Communication must be durably committed before HTBW relies upon future handling of
that Communication.** A Communication whose entire required governed lifecycle completes within the
creating transaction (no outstanding delivery, no deferred delivery, no pending retry, no pending
presentation, no pending acknowledgement) is governed exactly as any other such record under its own
already-accepted retention classification (**DL-47**) — this decision does not force an artificial
durability step where none is required. A Communication whose lifecycle **extends beyond the creating
transaction** — outstanding delivery, deferred delivery, retry pending, presentation pending where
current semantics require future handling, acknowledgement pending, or any other unresolved lifecycle
state — **must** be durably committed first. HTBW never presents a future-handling guarantee (a pending
retry, a promised future delivery) that rests only on volatile in-memory state.

**A completed transaction never creates an additional Inbox/pending artifact merely to prove an Inbox
existed.** The authoritative Communication record follows its own already-accepted lifecycle/history/
retention; no second persisted object is created solely for the Household Inbox, which remains a
projection (**DL-141**, unchanged).

### 3. Persisted Content and Metadata, consuming DL-138 unchanged

Persistence preserves the Content/Metadata classification **DL-138** already established — this is a
logical-governance distinction that physical persistence technology must not collapse merely because
both may be represented in the same underlying file or table. **Communication Content** is the
substantive content HTBW intended to convey (the Minimal rendering projection, DL-138's own anchor).
**Communication Metadata** is the governed lifecycle/context information `communication.md`'s "Required"
field table already enumerates (identity, Version Identity, Effective/Recorded Time, provenance,
originator reference, subject reference, Intended Audience, Category, Urgency, Significance reference,
Originating Context Reference, Visibility Classification reference, Retention Classification, Lifecycle
State, Supersedes/Superseded-by, expiry specification reference, Minimal rendering projection,
Explanation references) plus the delivery/acknowledgement history `communication.md`'s "Communication
history" table already enumerates. **No duplicate field is invented** — this decision persists exactly
the fields already canonical, nothing more.

**Example, restated from the Owner's own illustration:** a 42-page HVAC inspection report produces the
Communication *"The HVAC system is due for annual maintenance next month"* — only that household-facing
sentence (and its governed reference back to the report) persists as Content; the report itself remains
the originating responsibility's own record, referenced, never copied (§4, below).

### 4. Source material is referenced, never copied

Consuming **P30** and the existing governed-reference model unchanged: a Communication may originate
from an Asset document, a Stewardship obligation, a Truth Fact, a calendar, an email, Home Steward
reasoning, an Explainability Record, Continuity state, or another governed source. **The source remains
separately owned by its own responsibility.** The Communication's own `communication.md`-required
**Originator reference**, **Subject reference**, and **Originating Context Reference** fields already
supply sufficient provenance (which responsibility, through which evidence, at what confidence, which
Fact versions were true at origination) to explain what informed the Communication and why — **no
complete source payload is ever copied into the Communication for convenience.**

### 5. Persistence mechanism consumes DL-92 directly, no exception

Resolving Remaining Question 5: **Communication follows DL-92's already-accepted governed-record
persistence architecture unchanged — no Communication-specific exception is created.** Communication is
already a Category 3 "Governed HTBW record" with a Current Projection and Change Record history
(`home-assistant-boundary.md`'s own representation-strategy table), the exact record shape DL-92
governs by default via the Home Assistant Storage helper. **No exception is justified merely because
some Communications are short-lived** — a Communication whose entire lifecycle completes within the
creating transaction still follows the same mechanism; it simply carries a shorter configured
retention, never a different persistence technology. Connected Storage remains available, exactly as
DL-92 already states, strictly as the **already-accepted External History Retention extension
(DL-42)** where a household configures Communication Metadata or Content retention longer than is
practical to keep natively — never a parallel authority, and never required for baseline operation.

### 6. #207 retains broader physical-placement scope, not preempted

**This decision does not preempt #207.** #207 exists to decide repository-wide physical-technology
placement (SQLite vs. YAML vs. Config Entries vs. Connected Storage vs. other mechanisms) where not
already settled. **Communication's placement is already settled by DL-92** (Storage helper, default),
exactly as Explainability's was independently settled by **DL-137** (SQLite) ahead of #207 resolving the
remaining record classes. OD-42 does not need to wait for #207, and #207 is not executed by this
decision.

### 7. Native Home Assistant representation is a projection, never authority

Consuming **DL-31** unchanged: if a Communication is represented in Home Assistant (for example, as a
`persistent_notification` or a `notify` delivery target's own entity state), **that representation is
a projection** — never the authoritative Communication record, never a second persistence store, never
the Household Inbox, never lifecycle authority. Native state/history behavior attached to that
representation does not transfer authority away from the HTBW Communication record.
`home-assistant-boundary.md`'s own Category 3 table entry for Communication is restated, not altered.

### 8. Home Assistant Notifications are the default HA-native delivery mechanism

**For delivery into Home Assistant-native notification experiences, HTBW uses Home Assistant's native
Notifications infrastructure unless a governed requirement proves it insufficient** — restating
**P21** Home Assistant First, applied to Communication delivery specifically. No parallel HTBW push-
notification subsystem, second Home Assistant notification center, or HTBW-invented mobile-notification
transport is created. `adr-resident-communication-and-delivery-separation.md`'s own verified capability
review (`notify`, `persistent_notification`, `assist_satellite`, `tts`, actionable notifications) is
consumed unchanged as the delivery-mechanism evidence base for §9's matrix.

### 9. Delivery-mechanism matrix

| Target / Context | Preferred Mechanism | Authoritative Record | Delivery Artifact | Evidence Available | Acknowledgement Semantics | Privacy/Audience Notes | Fallback/Failure | Rationale |
|---|---|---|---|---|---|---|---|---|
| **Companion App / mobile push** | Home Assistant `notify` → Companion App (`notify.send_message`, notify groups) | HTBW Communication | OS-level push notification | `notify` entity state (last-sent time) only; `mobile_app_notification_action`/`mobile_app_notification_cleared` where actionable | Explicit governed action only (§13); dismissal alone is never acknowledgement | Private device may support stronger requester evidence; another Person holding the device never inherits authority (DL-139) | DL-98 Delivery Retry (household-configured, no HTBW default); DL-41 unavailable-dependency reporting | Verified native capability (G1–G11 reconciled); avoids a parallel push subsystem |
| **HA frontend/web notification** | `persistent_notification.create`/`dismiss` where appropriate | HTBW Communication | Persistent Notification entry | Lifecycle triggers (`added`/`removed`/`updated`/`current`) | Dismissal ≠ acknowledgement (§13) | Never treated as the Household Inbox (DL-141) | Same as above | Native capability verified; `persistent_notification` ≠ Inbox store |
| **Dashboard/kiosk native notification presentation** | Native HA notification presentation where suitable and permitted | HTBW Communication | Rendered native notification | Same as frontend row; endpoint contributes audience/shared-surface context (DL-140) | Dismissal ≠ acknowledgement | Shared-surface audience governance applies (DL-34/DL-72); distinct from an Assist-mediated Inbox query on the same kiosk (§11) | Degrade to content-free Indication or omit per DL-94 | Dashboard visibility semantics were **not independently verified** (`adr-resident-communication-and-delivery-separation.md`); treated conservatively |
| **Spoken Room announcement** | Existing Concierge voice/announcement path (`assist_satellite.announce`, `tts`), reusing `voice_input`/`spoken_response_output` (DL-90) | HTBW Communication | Spoken rendering | Delivery Attempt outcome per DL-95; Presentation Outcome per DL-54 | Explicit governed action only | Audience evaluated for everyone who may hear (DL-34/DL-140); content-free Indication where required | DL-98 retry; degrade to private surface where available | Not forced through `notify` merely for uniformity; reuses existing Concierge entry points |
| **Email** | Appropriate governed email transport (native HA `notify` integration where suitable) | HTBW Communication | Delivered email | Transport-dependent; generally fire-and-forget (G3) | Explicit governed action only | DL-136 external-copy boundary applies once delivered | DL-98 retry; `Failed`/`Unknown` per DL-95 | External transport; HTBW does not control downstream mailbox copies |
| **SMS** | Appropriate governed SMS transport | HTBW Communication | Delivered SMS | Transport-dependent | Explicit governed action only | DL-136 external-copy boundary applies | DL-98 retry; `Failed`/`Unknown` per DL-95 | External transport; same boundary as email |
| **Other configured HA Notify target** | Native HA `notify` integration for that target | HTBW Communication | Target-specific delivery artifact | Per-target, evaluated under DL-30's burden of proof | Explicit governed action only | Same disclosure rules apply regardless of transport | DL-98 retry | Home Assistant First; no bespoke per-target subsystem |
| **Assist Household Inbox retrieval** | Assist (DL-140) → DL-141 projection | HTBW Communication (current authoritative state) | Non-persisted Explainability-sibling projection | Current Communication Current Projection, read fresh | Viewing ≠ acknowledgement; may be a Presentation event (DL-95/DL-96) | Per-requester, read-time Operational Trust filtering (DL-141) | Capability unavailable + dependency named if storage unavailable (DL-41) | No store; this is the conversational retrieval path, distinct from proactive delivery above |

### 10. Companion App delivery detail

Conceptual path: **HTBW Communication → Concierge delivery governance → Home Assistant Notify →
Companion App/mobile endpoint → OS notification presentation.** The mobile notification is a delivery/
presentation artifact, never the Communication itself. It is never authoritative for Communication
lifecycle, Content retention, Metadata retention, acknowledgement, or Household Inbox membership — the
authoritative Communication remains separately governed, exactly as §7 states generally.

### 11. HA frontend, dashboard/kiosk: conversational query vs. proactive presentation, never conflated

Two distinct cases, restated explicitly so they are never merged: **(A) conversational Inbox/
Communication query** ("What messages are waiting?") routes through Assist to the **DL-141** Household
Inbox projection; **(B) proactive/persistent notification presentation** (a Communication deliberately
delivered into a Home Assistant-native UI endpoint) uses current native HA notification/presentation
capability where appropriate. A kiosk dashboard displaying an Assist response is a different event from
Home Assistant proactively presenting a native notification artifact on the same physical screen — both
remain independently subject to current Operational Trust/audience governance, and neither becomes the
other.

### 12. Voice, email, SMS retain their own appropriate transports

Voice delivery is never forced through Home Assistant Notify merely for uniformity — it uses the
already-accepted Concierge voice/announcement architecture (Room input/output relationships per
**DL-90**, reused unchanged; no ad hoc microphone/speaker remapping; no Communication-specific voice
routing; no second voice transport installed). Email and SMS remain distinct external delivery
transports; where Home Assistant provides a suitable native `notify` integration for the channel, Home
Assistant First may justify using it as the transport, but the architectural distinction remains:
transport artifact ≠ Communication authority.

### 13. Transport selection, dismissal, and acknowledgement

**The same authoritative Communication may be attempted over more than one permitted delivery mechanism
without creating two authoritative Communications** — a voice attempt followed by a mobile-notification
attempt for the same Communication produces one Communication with two recorded Delivery Attempts
(**DL-95**), never a duplicate. **Dismissing a Home Assistant notification does not automatically
acknowledge the authoritative HTBW Communication** — notification UI lifecycle ≠ Communication
acknowledgement lifecycle. Where an explicit notification action/button is mapped through a governed
HTBW action to `Acknowledged`, that mapping is permitted **only** when the action is explicit, requester/
authorization context is sufficient, current **DL-96** acknowledgement semantics are satisfied, and the
result is written back to the authoritative Communication lifecycle — never inferred from dismissal
alone. **A native notify entity's "sent" state is not the complete delivery truth**: HTBW continues to
record delivery/presentation/acknowledgement outcome using the existing canonical vocabulary
(`Attempted`/`Delivered`/`Presented`/`Failed`/`Unknown`, DL-95) rather than overclaiming native transport
evidence. Where a native notification mechanism exposes an identifier useful for update, dismissal,
replacement, or callback/action correlation, HTBW may retain it as governed delivery metadata (a
correlation reference) — **it never becomes the Communication's own Record Identity** (DL-104), which
remains separately assigned and governed.

### 14. Recorder and `todo` boundaries restated, not altered

Consuming **DL-114** and the existing `todo` boundary unchanged: **Home Assistant Recorder is not
Communication persistence.** Native notification/entity/event information Recorder retains is a native
retention consequence only; HTBW never relies on Recorder history as the authoritative Communication
lifecycle and never copies Recorder history to build a second communication archive. **`todo` remains
an outstanding-obligation/action surface and is never repurposed as Communication persistence** —
Communication and Obligation remain two distinct models; **DL-141**'s Assist composition may present
both together without merging them.

### 15. Household Inbox restart behavior

Consuming **DL-141** unchanged: the Household Inbox does not survive restart because there is nothing
Inbox-specific to survive. After a restart, Concierge reassembles a fresh Household Inbox Projection
from the current authoritative (now-durable, per §2) Communication records, filtered by Operational
Trust at read time. **No persisted Inbox state is restored, because none exists.** A Communication
that remained outstanding for a Person before restart remains an authoritative unresolved Communication
after restart, discoverable through the same Assist/DL-141 path — never silently lost, never
reconstructed from a notification artifact, never served from a stale cache.

### 16. Transactional durability and failure behavior

**The durability invariant is architectural; the exact database transaction mechanism remains
implementation mapping** (restating DL-92's own encoding-is-implementation-mapping non-goal). If the
system considers an asynchronous/deferred/outstanding Communication successfully created, the
authoritative record must already be durable enough to survive the runtime failure/restart conditions
current persistence architecture (DL-92) is designed to tolerate — HTBW never claims successful,
durable future handling while only volatile in-memory state exists. **Where a Communication requiring
durability cannot be committed**, HTBW does not proceed as though durable future delivery is guaranteed:
current failure/degradation semantics apply (creation failure reported, future delivery marked
unavailable, the originating capability informed, per **DL-41**) — never a silent retention-only-in-
memory state presented as durably scheduled. **Where authoritative durable persistence (storage) is
itself unavailable**, current Connected Storage/governed-persistence outage rules apply unchanged; no
Communication-specific availability semantics are invented, and no secret fallback Inbox store or
native-notification-as-substitute-for-persistence is created.

### 17. Retention after delivery, and after Content expiry

Consuming **DL-138** unchanged: delivery, presentation, or acknowledgement does not itself determine
Communication Content or Metadata retention — both continue to follow their own independently
household-configured policies after any delivery outcome. **If Content expires while Metadata remains**,
the authoritative Communication lifecycle may still honestly answer whether a Communication was created,
whether delivery was attempted, when, to which governed audience, and whether it was presented/
acknowledged — it must never reconstruct expired Content from Metadata, and a native downstream
notification artifact must never become a hidden copy that defeats HTBW-controlled Content retention.

### 18. External copies

Once delivered to a mobile OS, email service, SMS provider, or other external notification service,
**HTBW does not control all downstream copies or their retention**, and states this honestly. Deleting
the authoritative HTBW Communication does not automatically mean the email is deleted from a mailbox,
the SMS is deleted from a phone, the push notification is cleared from the OS notification center, or a
provider's own copy is erased — unless the relevant transport explicitly supports and current governance
(**DL-136**) authorizes that operation.

### 19. Privacy and Explainability

Communication persistence does not increase disclosure for operational convenience: Content, recipient
identity, Category, Urgency (where sensitive), audience specification, delivery metadata,
acknowledgement, and source provenance remain protected exactly as `privacy.md` already requires.
**The authoritative persistence store is never exposed directly through a UI** — household-facing access
remains through governed capabilities (DL-141 Inbox/Assist). Explainability references the Communication
by Governed Reference (identity/version, per **DL-104**) rather than duplicating its full content,
consuming the existing Decision Trace model unchanged.

---

## Explicit non-goals

- **No Communication, Messaging, Inbox, or Delivery responsibility is created.**
- **No second Recorder, persisted Household Inbox, notification shadow store, or endpoint-specific
  Communication store is created.**
- **No physical persistence technology is invented** beyond DL-92's already-accepted Storage-helper
  default and DL-42's already-accepted Connected Storage extension; **#207 is not executed or
  preempted** beyond confirming Communication's placement is already settled by DL-92.
- **No parallel HTBW notification/push subsystem is created.**
- **DL-28, DL-31, DL-42, DL-46, DL-47, DL-53, DL-77, DL-78, DL-88, DL-90, DL-92, DL-94, DL-95, DL-96,
  DL-98, DL-99, DL-104, DL-113, DL-114, DL-136, amended DL-137, DL-138, DL-140, and DL-141 are not
  reopened.**
- **No unrelated Owner policy is invented.**

---

## Related documents

- [../models/communication.md](../models/communication.md)
- [adr-resident-communication-and-delivery-separation.md](adr-resident-communication-and-delivery-separation.md)
- [adr-communication-retention-governance.md](adr-communication-retention-governance.md) (**DL-138**)
- [adr-household-inbox-projection-semantics.md](adr-household-inbox-projection-semantics.md) (**DL-141**)
- [adr-explainability-presentation-and-assist-interaction-path.md](adr-explainability-presentation-and-assist-interaction-path.md)
  (**DL-140**)
- [adr-governed-record-persistence-mechanism.md](adr-governed-record-persistence-mechanism.md)
  (**DL-92**)
- [home-assistant-boundary.md](home-assistant-boundary.md) — Communication capability review,
  representation-strategy table
- [connected-storage.md](connected-storage.md)
- [../contracts/concierge-contract.md](../contracts/concierge-contract.md)
- [../models/glossary.md](../models/glossary.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
