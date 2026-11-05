# ADR: Communication Retention Governance

> **Document status: Canonical ADR.**
> Status: **Accepted** 2026-11-05. Records **DL-138** (issue **#118**, formal acceptance review PASS).
> Resolves **OD-49** in full.
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Terminology: [../models/glossary.md](../models/glossary.md), [../models/communication.md](../models/communication.md),
> [adr-explainability-persistence-and-retention.md](adr-explainability-persistence-and-retention.md).

---

## Status

**Accepted 2026-11-05.** Resolves every OD-49 Remaining Question. This ADR creates **no Communication
History, Messaging Archive, or retention responsibility**, **no second Home Assistant Recorder**, **no
duplicate Communication store**, and **no retention-specific shadow content store**. It does not reopen
**DL-34**, **DL-43**, **DL-45**, **DL-46**, **DL-47**, **DL-56**, **DL-71**, **DL-76**, **DL-77**,
**DL-78**, **DL-104**, **DL-109**, **DL-122**, **DL-129**, **DL-130**, **DL-132**, **DL-133**,
**DL-136**, or the amended **DL-137** — each is consumed unchanged.

---

## Context

**DL-47 already settled the rule**: Communication records follow the governed-record retention model,
"with content and metadata classified separately." What remained open was the classification itself
(what exactly is Content, what exactly is Metadata) and the retention values for each. **This decision
also corrects stale dependency evidence on Issue #118** that described the pre-amendment DL-137 model
(a DL-76-proportional, non-zero-floor-existence retention scheme) — that model was superseded by
DL-137's own same-day targeted Owner clarification, and this decision is built on the **corrected**
DL-137 philosophy throughout: **the architecture provides the governance mechanism; the household
provides the retention value.**

---

## Decision

### 1. Stale dependency evidence on #118 is corrected, not carried forward

A prior dependency-evidence comment on Issue #118 described DL-137 as establishing "retention
proportionality expressed as an ordering constraint over DL-76's existing Action-Risk Classes" and "a
non-zero floor-existence configuration-validation requirement." **Both were superseded by DL-137's own
same-day targeted Owner clarification** (see `decision-ledger.md`'s DL-137 Notes, "Amendment
2026-11-05"). This decision does not reuse, extend, or build upon that superseded model for
Communication retention. **DL-137 is not reopened** — this is a correction of what was previously
(incorrectly) cited as its holding, not a revision of DL-137 itself.

### 2. Communication Content and Communication Metadata — canonical boundary

**Communication Content** is the substance actually conveyed, or intended to be conveyed, to the
recipient — the household-facing statement itself: spoken/TTS message text, notification body,
rendered message body, conversational response content, announcement wording, or other semantically
equivalent delivered content. Reusing `communication.md`'s own already-accepted **Minimal rendering
projection** field ("the immutable human-readable form... must not become a wholesale copy") as the
canonical anchor for what Content is.

**Referenced source material is not automatically Communication Content.** Where a Communication is
generated from an Asset document, email, calendar, Truth Fact, Stewardship obligation, Home Steward
reasoning, an Explainability Record, or another governed source, that source retains its own owning
responsibility and lifecycle. The Communication carries a Governed Reference to it (already required:
`communication.md`'s **Originator reference** and **Subject reference** fields) — **never a second
copy of the source payload merely because it informed a Communication.**

**Communication Metadata** is the minimum governed information necessary to describe the Communication
event and lifecycle without retaining Content. Reusing `communication.md`'s already-required fields:
Communication ID, Version Identity, Effective Time, Recorded Time, Provenance, Originator reference,
Subject reference, Intended Audience, Category (**DL-78**), Urgency (**DL-77**), Significance
reference, Originating Context Reference, Visibility Classification reference, Retention
Classification, Lifecycle State, Supersedes/Superseded-by, Expiry specification reference, and
Explanation references — plus the delivery/acknowledgement history already defined in
`communication.md`'s "Communication history" table (delivery attempted/delivered/presented/failed,
acknowledged, suppressed, superseded, Tombstoned). **No duplicate fields are invented.**

### 3. Metadata must not become disguised Content

**Communication Metadata must never contain enough substantive information to reconstruct expired or
deleted Communication Content.** A `description`, `summary`, or similar field must never carry full
message text, a substantial paraphrase, or an excerpt sufficient to recover what was conveyed, merely
to let the Home answer a question after Content retention expires. Where Content has expired, Metadata
may honestly state: that a Communication occurred; its Category; its audience/recipient where
authorized; when it occurred; delivery result; acknowledgement result; and that Content is no longer
retained. **It must never regenerate the expired message.**

### 4. Two independent, household-configured retention classes

**Communication Content retention and Communication Metadata retention are two separate, independently
household-configured policies** — restating **DL-47**'s already-accepted classification split, now
given values. Reusing **DL-122**'s already-accepted retention-duration-choice shape (enumerated,
human-understandable presets plus a custom numeric override), configured at Integration-default/
Room-override scope, consistent with the identical configuration pattern **DL-137** already applies to
Explainability. **These are never collapsed into a single Communication retention duration.**

**Consistent with the corrected DL-137 philosophy, HTBW imposes no independent numeric architectural
floor or ceiling on either class merely because the record class is Communication Content or
Communication Metadata.** The architecture provides the governance mechanism — classification,
configuration surface, validation, lifecycle behaviour, Preservation Hold interaction (§8), and
erasure/conflict interaction (§9–§10) — and **the household provides the value**, independently for
each class. **No arbitrary numeric duration (for example, "Content = 7 days," "Metadata = 30 days," or
any other specific number) is invented by this decision** for any class or Category.

**A household-configured value of zero, disabled, or immediate-expiry is not rejected or silently
overridden merely because it is zero**, absent independently accepted authority requiring otherwise
(none is identified for ordinary Communication Content or Metadata). Where a household configures
effectively no historical Communication Content retention, HTBW explains the consequence honestly
(the Home will not be able to recount what was said after expiry) without overriding the household's
configured value. Communication Metadata may be configured to a longer interval independently, so the
Home can still answer *"did you tell me?"* without retaining *what* was said.

### 5. Communication Category does not automatically dictate retention duration

**DL-78** already establishes Category as a closed, seven-value, content-domain enumeration
(Stewardship, Security, Care, Environment, Experience, System, Safety) that is a **downstream-input
only** to OD-49's own retention ownership — restated, not reopened. **Category does not automatically
impose a shorter or longer retention duration**: a Care-category Communication is not assumed to
require shorter retention than a Stewardship-category one, and a Safety-category Communication is not
assumed to require longer retention, merely because of its Category. Category's own accepted
governance purposes (disclosure, audience, interruption-adjacency) are unaffected and unchanged.
**Optional household-configurable per-Category retention override is supported where the household
wants it** — reusing the identical Integration-default/Room-override/custom-value configuration
surface (§4) applied per Category rather than globally — but **per-Category configuration is never
required merely because Categories exist**, and no Category receives an HTBW-assigned default duration
different from any other.

### 6. Urgency creates no retention class

**DL-77** already establishes that Urgency adds no new retainable record class; restated, not
reopened. Urgency remains ordinary Metadata/context under its existing accepted semantics. **No
"Urgent Communication Content Retention" or "Urgent Communication Metadata Retention" class is created**,
and Urgency does not itself lengthen or shorten either configured retention policy.

### 7. Content expiry, Metadata survival, and honest status reporting

When Communication Content reaches its own configured expiration, it is removed; Communication
Metadata continues under its own, independently configured retention. The Home remains able to answer,
for example: *"A Communication in the [actual Category] category was delivered to [authorized
recipient] at [time] and acknowledged at [time]. The Communication Content is no longer retained."*
**The Home never reconstructs the expired message, and never implies the Communication never
occurred.**

**Metadata represents, using existing canonical lifecycle/status vocabulary, whether the corresponding
Content is**: currently retained/available; expired under retention; deleted/erased; withheld by
policy; preserved under governed restriction (Preservation Hold); or unavailable due to a storage/
provider condition. **No new parallel status taxonomy is invented** — this reuses `communication.md`'s
existing Lifecycle State and the Tombstone/structural-record vocabulary already accepted elsewhere
(**DL-43**, **DL-45**, **DL-133**, **DL-136**). The distinction that must always be preserved: *"no
Content was ever recorded"* versus *"Content existed but is no longer retained."*

**On removal of Content, a Tombstone is required**, distinguishing content-removed from
content-never-existed, exactly as `communication.md`'s own "Communication history" table already
requires ("Communication redacted, purged, or truncated → Tombstone"). **Retained Metadata never
itself carries the deleted Content.** Where Metadata later reaches its own independently configured
expiration, it follows its own accepted deletion/Tombstone lifecycle — **Metadata is never made
permanent by default.**

### 8. Ordinary Explainability reference does not extend Communication retention

**An ordinary Explainability Record (`outcome_generated` or `on_demand_decision_trace`, DL-137) that
references a Communication does not automatically extend that Communication's own Content or Metadata
retention.** Otherwise Communication retention would be meaningless — any Communication ever mentioned
in an Explainability Record would become permanently retained by the mere fact of being referenced.
Where a Communication's Content expires with no Preservation Hold applicable, the Communication
expires normally; the referencing Explainability Record retains its own Governed Reference (**DL-27**,
**P30**); and a later explanation honestly reports the referenced Content as no longer retained,
exactly as `decision-trace.md`'s existing "referenced version cannot be resolved" failure behaviour
already requires. **No Communication Content is copied into an Explainability Record merely to
preserve it against the Communication's own expiry.**

**Preservation Hold is the one accepted exception, and it minimizes first.** Where a valid
Preservation Hold applies and the specific Communication Content is actually required to keep a held
Explainability Record explainable, **DL-47**'s existing holding rule and **DL-132**'s Hold model govern
— the required source version may be preserved under the Hold's own rules. This is **Preservation
governance, not ordinary Communication retention**, and it never rewrites the Communication's own
configured retention policy globally. **DL-47's holding rule preserves only what is required to keep
the held record explainable** — where Metadata, a reference, or provenance already suffices, Content
is not additionally retained; only where the actual Content is genuinely necessary is it preserved,
and only under the Hold. When the Hold ends, ordinary lifecycle and **DL-133** conflict rules resume.

### 9. On-demand Explainability does not reset Communication retention

Consuming the amended **DL-137**: where an on-demand Decision Trace evaluates a Communication (for
example, a Person asking *"did you tell me about the appointment?"*), HTBW may consult the currently
available Communication and produces a new Explainability Record under DL-137's own always-new-record
rule. **This on-demand request does not restart, pause, or extend the Communication's own retention
clock.** The Communication's Content continues to expire according to its own independently configured
Communication Content retention, regardless of how many on-demand Explainability requests have
consulted it. The new Explainability Record does not copy the Communication Content merely to defeat
that expiration (§8).

**Communication Content retention, Communication Metadata retention, and Explainability retention are
three independent policies, never conflated.** References remain resolvable only while the referenced
record remains available, unless a Preservation Hold or another accepted structural rule requires
preservation; a dangling or expired reference is reported honestly, never silently rendered as though
it never existed.

### 10. Consent withdrawal and erasure

Restated from **DL-56**, **DL-133**, and **DL-136**, unchanged — no new conflict precedence is
invented. Where a deletion or erasure obligation applies to Communication Content or Metadata, current
minimization, deletion, redaction, Tombstone, pending-cleanup, and preservation-conflict semantics
apply exactly as already accepted. **Communication Metadata is not automatically exempt from erasure
merely because it is useful for answering "did you tell me?"** — only independently governed
structural lifecycle records (Tombstones, consent-lifecycle proof, held records, and versions required
to keep a held trace explainable — **DL-47**'s four structural floors) are preserved as already
accepted elsewhere; ordinary Metadata is subject to the same erasure request as Content.

### 11. Person-scoped privacy of retained Metadata

**Retained Communication Metadata may itself be sensitive** — recipient identity, audience, Category
(including Care-category content), acknowledgement, delivery outcome, and timing are all potentially
disclosure-sensitive. **Metadata is never treated as non-private merely because Content is absent.**
Operational Trust's existing disclosure/audience/privacy architecture (**DL-34**, `privacy.md`) applies
to retained Metadata exactly as it would to any other governed record.

### 12. Care-category Communications

Care-category Communications (the closed-enumeration Category nearest the brief's "health/care"
concern, **DL-78**) may be particularly sensitive, affecting disclosure, audience, authorization, and
possibly interruption-adjacent governance under already-accepted architecture. **This sensitivity does
not automatically convert into a shorter or longer retention duration** (§5): a household may
deliberately configure Care-category Metadata or Content retention longer, shorter, or equal to any
other Category's, using the same optional per-Category override surface (§5). Absent a specific
accepted rule linking Care-category content to a particular retention value, retention remains fully
household-configured.

### 13. External delivery channels

Where a Communication is delivered through an external system (SMS, email, push provider, external
device), **HTBW's retention policy governs only HTBW-owned Communication records.** HTBW does not
claim control over, and does not promise deletion of, a recipient's or provider's own externally
retained copy, unless current connector architecture explicitly supports such control. This restates
**DL-136**'s external-delivery-boundary discipline (requester authority ≠ recipient authority ≠
transport authority; HTBW cannot guarantee downstream deletion after transfer) applied to Communication
specifically.

### 14. Home Assistant Recorder is not the Communication retention policy

Restated from **DL-114**, unchanged: where HTBW publishes Communication-related entity or event state
into Home Assistant, Recorder's retention of that published projection is a separate, native retention
consequence — it does not become the Communication retention policy, and HTBW does not copy Recorder
history into Communication records merely to satisfy retention. **No second Recorder is built.** HTBW
Communication records use their own governed persistence and retention, reusing the already-accepted
**DL-92**/**DL-129** persistence mechanism (Storage helper default, Connected Storage as the **DL-42**
External History Retention extension) — this decision does not alter that mechanism.

### 15. Persistence technology placement is routed to #207, not decided here

**Issue #207** (HTBW Structured Data Persistence Placement Review) owns the repository-wide
SQLite/YAML/Config-Entry/Connected-Storage classification question. **This decision does not make a
new global persistence-technology decision for Communication records** — it states the logical
retention/data-class decision (Content versus Metadata, and their independent configuration) and
routes any unresolved physical persistence placement to #207, which remains unexecuted. Where current
accepted architecture already determines Communication's persistence mechanism (**DL-92**'s Storage
helper default, **DL-129**'s Connected Storage extension pattern), that mechanism is reused unchanged.

### 16. Portability accounts for Content and Metadata independently

Consuming **DL-136** unchanged: a Portability Export's Completeness Manifest reports Communication
Content and Communication Metadata as **independently resolved classes**, each to one of the existing
nine outcome states (included; included by reference; excluded by scope; withheld by policy;
unavailable; no longer retained; deleted/tombstoned; unsupported by native source; no responsive
records) — never a single combined "Communication" status that could silently conflate an expired
Content state with a still-retained Metadata state. **An expired or withheld Content is never
reconstructed from retained Metadata merely to produce a more complete-looking export.**

### 17. Field-by-field classification matrix

| Field / Semantic Element | Current Canonical Name | Class | Authority | Retention Policy | Deletion Behaviour | Privacy Notes |
|---|---|---|---|---|---|---|
| Unique identity | Communication ID | Metadata | Foundation (definitional) | Metadata policy | Tombstoned on removal | Low sensitivity alone |
| Version/identity | Version Identity | Metadata | Foundation | Metadata policy | Retained with record | Low sensitivity |
| Effective Time | Effective Time | Metadata | Foundation | Metadata policy | Retained with record | Low sensitivity |
| Recorded Time | Recorded Time | Metadata | Foundation | Metadata policy | Retained with record | Low sensitivity |
| Source/authority of the Communication | Provenance | Metadata | Originating responsibility | Metadata policy | Retained with record | Low sensitivity |
| Reference to originating record | Originator reference | Governed Reference/Provenance | Originating responsibility | Follows the source's own lifecycle, never copied | Reference resolves to unavailable if source expires | Low, unless the reference itself reveals a protected subject |
| Reference to what it is about | Subject reference | Governed Reference/Provenance | Originating responsibility | As above | As above | May be sensitive (for example, a Person or health-adjacent Asset) |
| Who it is for | Intended Audience | Metadata | Foundation (**DL-71**) | Metadata policy | Tombstoned on removal | Potentially sensitive (reveals recipient) |
| What it is about | Category (**DL-78**) | Metadata | Foundation | Metadata policy | Tombstoned on removal | Potentially sensitive (for example, Care) |
| What it may interrupt | Urgency (**DL-77**) | Metadata | Operational Trust | Metadata policy | Tombstoned on removal | Low sensitivity alone |
| Significance | Significance reference | Governed Reference | Stewardship | Follows Stewardship's own record | N/A (reference) | Low, reference only |
| Facts true at origination | Originating Context Reference | Governed Reference/Provenance | Truth | Follows Truth's own record | N/A (reference) | Inherits source sensitivity |
| Disclosure classification | Visibility Classification reference | Governed Reference | Operational Trust | Re-evaluated at each attempt, never stored resolved | N/A (reference) | Policy-sensitive |
| Retention declaration | Retention Classification | Metadata | Operational Trust (policy), Foundation (record) | Carries this decision's Content/Metadata policy | N/A | Low sensitivity |
| Current state | Lifecycle State | Metadata | Concierge | Metadata policy | Tombstoned on removal | Low sensitivity |
| Supersession | Supersedes/Superseded-by | Governed Reference | Concierge | Metadata policy | Tombstoned on removal | Low sensitivity |
| Expiry governance | Expiry specification reference | Governed Reference | Operational Trust | N/A (reference) | N/A | Low sensitivity |
| **Delivered substance** | Minimal rendering projection | **Content** | Originating responsibility | Content policy (§4) | Deleted/Tombstoned on expiry | **High — this is the substantive message** |
| Why it was created/suppressed | Explanation references | Governed Reference | Concierge | Follows Explainability's own policy (never extended by this reference, §8) | N/A (reference) | Inherits Explainability sensitivity |
| Delivery attempts/outcomes | Change Records per attempt | Metadata | Concierge | Metadata policy | Tombstoned on removal | Potentially sensitive (reveals surface/timing) |
| Acknowledgement | Domain Event + Change Record | Metadata | Concierge | Metadata policy | Tombstoned on removal | Potentially sensitive (reveals who acknowledged) |
| Deletion/removal proof | Tombstone | Structural Lifecycle | Concierge | **DL-47**'s structural floor — survives any configured window | N/A (is the deletion record) | Never reconstructs deleted Content |
| Consent-lifecycle proof (where applicable) | Consent-lifecycle record | Structural Lifecycle | Identity | **DL-47**'s structural floor — survives any configured window | N/A | Never reconstructs withdrawn evidence |

---

## Responsibility impact

| Responsibility | Change |
|---|---|
| **Foundation** | Continues to define the Communication model (definitional only, owns no Communication) |
| **Concierge** | Continues to own Communication delivery history; applies the Content/Metadata classification and retention policies when composing/persisting records |
| **Operational Trust** | Owns the Content and Metadata retention configuration surfaces (Integration-default/Room-override, optional per-Category override); owns disclosure evaluation for retained Metadata |
| **Originating responsibility** | Continues to own the Communication's source material and its own lifecycle, never duplicated into Content |
| **Identity** | Continues to own consent-lifecycle proof unaffected by Communication retention (**DL-56**, unchanged) |

---

## What this decision does not do

- Does not create a Communication History, Messaging Archive, or retention responsibility.
- Does not create a second Home Assistant Recorder or a duplicate Communication store.
- Does not invent an arbitrary numeric retention duration for any class or Category.
- Does not impose an independent architectural retention floor or ceiling on Communication Content or
  Metadata.
- Does not reopen DL-47, DL-56, DL-76, DL-77, DL-78, DL-92, DL-114, DL-122, DL-129, DL-132, DL-133,
  DL-136, or the amended DL-137.
- Does not make a new global SQLite/YAML/Connected-Storage persistence-placement decision (routed to
  #207, unexecuted).
- Does not promise deletion of an externally delivered copy outside HTBW's own governance.

---

## Related documents

- [../governance/decision-ledger.md](../governance/decision-ledger.md) — DL-138
- [../governance/open-decision-issue-index.md](../governance/open-decision-issue-index.md) — OD-49
- [../models/communication.md](../models/communication.md) — Communication history, Retention
- [../architecture/privacy.md](../architecture/privacy.md) — Retention of communications
- [../models/operational-trust.md](../models/operational-trust.md) — Communication retention authority
- [../models/decision-trace.md](../models/decision-trace.md) — Reference/holding discipline
- [adr-explainability-persistence-and-retention.md](adr-explainability-persistence-and-retention.md) — DL-137 (amended)
- [adr-data-portability-and-erasure-mechanics.md](adr-data-portability-and-erasure-mechanics.md) — DL-136
- [adr-deletion-versus-preservation-reconciliation.md](adr-deletion-versus-preservation-reconciliation.md) — DL-133
- [adr-preservation-hold-governance.md](adr-preservation-hold-governance.md) — DL-132
- [../models/glossary.md](../models/glossary.md) — Communication Content, Communication Metadata
