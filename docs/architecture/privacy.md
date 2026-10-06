# Privacy and Data Minimization

> **Document status: Canonical.**
> Cross-cutting architecture. Every responsibility must satisfy this document.
> Unresolved items are marked and recorded in
> [../governance/decision-ledger.md](../governance/decision-ledger.md).

---

## Position

Privacy is an architecture requirement, not a configuration afterthought. Operational Trust owns
privacy **policy**; every responsibility owns privacy **behavior** for the data it holds.

**Privacy before convenience.** Where the two conflict, privacy wins unless a person with authority
has explicitly and knowingly chosen otherwise.

---

## Requirements

### Consent

- Ownership is divided: **Foundation** holds the consent record on the Person, **Identity** owns the
  consent lifecycle, and **Operational Trust** owns consent policy and enforcement. See
  [../models/operational-trust.md](../models/operational-trust.md).
- Identity evidence collection requires explicit consent from the person it describes.
- Consent is recorded, attributable, and revocable.
- Consent is scoped: consenting to voice identity is not consent to calendar access.
- A person who has not consented must still be able to use the home in a guest-safe way.
- **The full scope model, canonical record, self/proxy consent, withdrawal, retention resolution, and
  state distinctions are accepted as DL-56** — see
  [../models/person-and-identity.md](../models/person-and-identity.md#consent-dl-56). **Consent is
  required for person association, never for environmental observation by itself**; correlation
  capability is never itself authorization.

### Participation is optional

> **No person is required to participate in any identity-evidence source, and declining costs them
> nothing they are entitled to.**

- **Every participation class is opt-in**: voice identity evidence, wearable evidence, device
  evidence, and person-scoped preference participation.
- **Voice identity evidence is available only for a consenting, enrolled participant.**
- **Declining is neutral, not degraded.** Fewer eligible evidence families produce a **lower ceiling,
  never a penalty** — *missing evidence is not contradicting evidence*.
- **A declined source is never used "just this once"** because the outcome would have been convenient.
- Declining is not exclusion: guest-safe use of the home remains fully available.

### Consent governs the evidence that exists at all

```text
CONSENT  →  AVAILABLE EVIDENCE  →  IDENTITY  →  OPERATIONAL TRUST
```

**Consent gates eligibility, not weight.** Evidence lacking valid consent is **excluded before
weighting**, never down-weighted, so an assertion is produced as though the source did not exist.
**A withdrawn consent is not a reduced weight.**

> **Consent determines what evidence may be used. Operational Trust ensures those choices are applied
> consistently and respectfully.**

### Knowledge and disclosure are separate

> **The question is not *"can the home know?"* It is *"should the home share?"***

Knowledge acquisition and disclosure are evaluated at **different points, by different
responsibilities**, against **different inputs**. **The home may legitimately know something it will
not say** — that is this document working, not failing. Equally, **a disclosure requirement never
reaches back to authorise collection**: usefulness is not a consent substitute. See
[../models/operational-trust.md](../models/operational-trust.md).

### Enrollment

- Enrollment is an explicit act, never a silent by-product of ordinary use.
- Enrollment artifacts (raw samples, recordings, captures) are **temporary** by default.
- Derived profiles (voiceprints, device associations) are durable and separately governed.
- Enrollment state and quality must be inspectable by the enrolled person.

### Revocation

- Revocation removes the derived profile and its associations, not merely its use.
- Revocation is available to the person described and to a person with household authority.
- Revocation must produce a defined outcome for connected-storage records and Decision Traces.

### Guest treatment

- Guests are unidentified or minimally identified by default.
- Guest-safe behavior is the default when identity is unresolved.
- Guests must not gain visibility of residents' preferences, presence history, calendars, messages,
  or Stewardship information.

### Child-safe treatment

- A person in a child role has a restricted authority ceiling.
- Child-safe restrictions are policy, evaluated by Operational Trust, not hard-coded behavior.

### Local versus cloud processing

- Every capability must **declare** whether it processes locally, remotely, or both.
- Local-first is preferred.
- A capability that requires remote processing must state what leaves the home, and consent must be
  obtainable per capability.

### Minimum necessary data

- Collect only what a stated responsibility requires.
- Retain only as long as the stated purpose requires.
- Derive and discard rather than store raw where a derived form is sufficient.

### Raw voice-sample retention

- Raw samples default to **zero retention** beyond the processing window.
- Any retention is explicit, consented, time-bounded, and inspectable.

### Derived voiceprint treatment

- Biometric internals — vectors, embeddings, fingerprint payloads, artifact internals, storage
  paths — are **never exposed** through diagnostics, services, logs, telemetry, or explanations.
- Safe metadata only: state, quality summary, confidence band, reason code.

### Safe fusion explanation

An identity explanation may state which **evidence families** supported or contradicted a candidate,
that correlated observations were treated as one, that an observation was stale or ineligible, the
**confidence band**, the reason codes, and the **Fusion Policy version**.

It must not expose voiceprint vectors, embeddings, raw biometric payloads, artifact internals, storage
paths, provider secrets, unnecessary device identifiers, or evidence the requester is not authorised
to see. **A fusion explanation must remain redactable without becoming false** — removing a device
identifier must not turn *corroborated by an independent family* into a claim the record does not
support.

A numeric confidence value is disclosed **only where policy governs it and the audience permits**, and
**never described as a probability, likelihood, or measured accuracy**.

### BLE-device and assigned-device associations

- An association between a person and a device is identity evidence and is governed as such.
- Presence history derived from device associations is subject to visibility policy.

### Personal calendar and email associations

- Access is person-scoped and permission-gated.
- Content must not appear in a shared surface unless policy permits it for the current audience.
- A briefing delivered in an occupied Room must respect who can hear it.

### Decision Trace privacy

- Traces may contain identity assertions, presence facts, preferences, and obligations.
- Trace visibility is an Operational Trust policy decision, per audience and per content class.
- A human-readable explanation must be redactable without becoming false.

### Decision Trace retention

- Traces are retained long enough to answer "why did this happen?" for a household-meaningful
  period, and no longer.
- Retention is bounded from **both** directions: **P27** establishes a floor, this document
  establishes the ceiling. See [Historical retention — floors and ceilings](#historical-retention--floors-and-ceilings).
- The retention rule is settled by **DL-47** — a Decision Trace follows External History Retention
  unless an accepted floor or a Preservation Hold applies. The exact floor and ceiling values are
  **not decided here**. Open decision **OD-05**.

### Visibility of personal preferences

- A person's preferences are visible to that person and to household authority as configured.
- They are not visible to guests.

### Visibility of presence history

- Presence history is among the most sensitive household data.
- Default visibility is the person described, plus explicitly authorized roles.

### Visibility of location

**Location is presence data reached by a different question, and it carries the same sensitivity.**
Truth publishes Location Facts about a Home, Room, Merged Room, Person, Pet, Asset, or Device; the
**Subject of the Fact does not determine the sensitivity of the answer.** Access and disclosure remain
two separate Operational Trust decisions (**DL-34**), evaluated against **audience composition** rather
than against who asked.

#### Device location may disclose Person location

- A Device bound to a Person is, for disclosure purposes, **a proxy for that Person**. *"Tom's phone is
  in the Den"* is heard as *"Tom is in the Den."*
- **Audience evaluation is mandatory** for a device-location answer whenever the Device is bound to a
  Person, however the question was phrased.
- Asking about **another Person's** device is a disclosure about **that Person**, governed by their
  policy — not the requestor's.
- A device-location Fact **never establishes that the bound Person is with the device**, and an answer
  must not imply that it does.
- Where audience composition is uncertain, **the delivery degrades, not the governance** — content-free
  indication, a private surface, confirmation, or refusal (**DL-72**, resolved **OD-71**).

#### Pet location may disclose human movement

- A pet-worn tag reports, continuously, where the tag is — in rooms people occupy. **Pet location is
  therefore a source of household occupancy and movement patterns.**
- **Consent to track a Pet is not consent to derive household movement patterns.** Where pet-location
  evidence is used or retained beyond the Pet's own location, the applicable consent must be present;
  evidence lacking valid consent is **excluded, not down-weighted**.
- *"Maisey is in the Primary Bedroom"* is evaluated as a **room-occupancy disclosure**. A sensitive Room
  is not exempted because the question named a Pet.
- Pet-location evidence **never** nominates a candidate Person, never enters identity fusion, and never
  creates person-scoped learning.

#### Location history

- Location history is **presence history** and inherits its default visibility: the person described,
  plus explicitly authorized roles.
- **HTBW retains no duplicate native location history.** Native state history has one owner; HTBW
  retains the governed Fact — Subject, Statement, confidence at the time, provenance, coverage,
  freshness, and lifecycle transitions — and never a copy of the rows behind it (**DL-42**, **DL-46**).
- Retention is bounded from both directions: **P27** sets the floor, this document sets the ceiling, and
  a redacted Historical Fact **remains a record that the Fact existed**.
- Access to movement histories and reconstructions is governed by Operational Trust and **must not be
  reachable through generic Room Help or a general-question capability** (**DL-35**, **OD-35**).

### Visibility of Stewardship information

- Obligations may reveal health, medication, absence patterns, or asset value.
- Stewardship visibility is policy-gated by content class, not uniformly public within the household.

### Health, medication, and pet-care data

- Treated as a distinct sensitive class.
- Access requires explicit authority, not merely household membership.
- Reminders must be deliverable without disclosing content to an unintended audience. The mechanism
  is **content-free indication** followed by identity-gated retrieval. See
  [../models/communication.md](../models/communication.md).

### Deletion and export

- A person must be able to obtain what the home holds about them.
- A person must be able to have it deleted, subject to household authority and safety obligations.
- Deletion must reach connected storage, not only the primary record.
- Reconciliation of deletion and export obligations with retention floors and Preservation Holds is
  **not decided here**. Open decision **OD-36**.

---

## Outbound communication

**Outbound communication inverts the initiative.** Every rule above governs what the home reveals
*when engaged*. An unsolicited delivery is not requested by the person who receives it, and the
audience is **whoever can perceive the delivery surface** — not whoever asked.

This is a distinct risk shape, and it is governed by **P32**: *permission to act does not imply
permission to announce*. See
[adr-resident-communication-and-delivery-separation.md](adr-resident-communication-and-delivery-separation.md)
and [../models/communication.md](../models/communication.md).

### Audience is evaluated against the surface

- Exposure for an outbound delivery is evaluated against **who can perceive the surface**, not
  against the intended recipient.
- The Existence → Participation → Exposure → Authority chain applies unchanged.
- Guests are **never an audience by default**, and guest presence constrains delivery to every
  audience.

### Indication and content are separate disclosures

- A **content-free indication** asserts only that something is outstanding. It discloses nothing and
  is permissible where content is not.
- **Content** requires full evaluation against surface perceptibility.
- **Retrieval** is resident-initiated and returns to the ordinary exposure chain, with identity
  asserted at retrieval rather than at indication.
- A shared surface must never enumerate **whose** communications are waiting.

### Degradation

- Where identity, occupancy, or context cannot be established with sufficient confidence,
  **the delivery degrades — the governance does not.**
- Degrading means choosing a benign surface, reducing to indication, or deferring. It never means
  relaxing an exposure rule to get a message through.

### Visibility is never stored resolved

- A Communication carries a **reference** to its visibility classification, re-evaluated at each
  delivery attempt.
- A stored resolved visibility value would survive a policy revocation. This is prohibited.

### Silence is recorded

- A withheld communication is a **suppression**, recorded as a governed change with a Decision Trace
  under **P16** and **DL-15**.
- **Silent non-delivery is prohibited.** A home that decided to stay quiet must be able to say so.

### Retention of communications

- Communication **content** and communication **metadata** are classified separately. The fact that
  the home tried to convey something may need a longer floor than what it tried to say.
- Floors follow the governed-record retention rule in **DL-47**; communication-specific floors,
  ceilings, and the separate classification of content and metadata are **OD-49**.
- Redaction, purge, or truncation of a Communication leaves a **Tombstone**.

---

## Historical retention — floors and ceilings

**P27 Historical Explainability** and **P28 Historical Truth** establish how *little* may be
retained. This document establishes how *much* and how *long*. **Both bind.**

| Constraint | Source | Direction |
|---|---|---|
| Retention **floor** | P27, P28 | The home must be able to account for itself |
| Retention **ceiling** | This document | The home must not hold more, or longer, than the purpose requires |

**Where a floor and a ceiling conflict, privacy governs the outcome, and the resulting limitation on
explainability is itself recorded.** The home must be able to say *"I no longer hold that record"*
rather than fall silent.

What is retained historically is the **governed conclusion and its attribution**. Long-term retention
of raw payloads is **not** required by any retention floor, and **P30 Reference Over Copy** exists
partly for this reason: sensitive content lives in one governed place where it can be redacted once,
rather than in every record that consumed it.

### Never retained through this architecture

- Raw voice samples, by default
- Biometric vectors
- Embeddings
- Fingerprint payloads
- Biometric artifact internals
- Biometric storage paths
- Complete raw sensor streams
- Complete source payloads copied into Decision Traces

### Retained instead, where policy permits

Evidence references, evidence classes, contributor identity, reason codes, confidence bands,
coverage, provenance, and lifecycle transitions.

### Unidentified people

Observations of people the home cannot identify are among its most sensitive data, and they are
**more** sensitive for being unidentified: the subject cannot be asked, cannot consent, and cannot
request their own erasure.

- **Indefinite retention of unknown-person observation is not a default.** It applies only where
  accepted policy explicitly requires it, for a stated reason, for a bounded period.
- **Observing an unknown evidence source creates no durable identity record**, and no profile that
  accumulates across visits.
- A **biometric no-match** result is retained as a reason code and a confidence band. **The sample is
  not retained in order to explain the non-match**, and the zero-retention default for raw voice is
  unchanged.
- Unknown evidence identifiers and external video references are retained as **references**, under
  the retention of the systems that own them, and are subject to the same redaction and tombstone
  rules as any other reference.
- **Actor reconstructions and movement histories are access-governed by Operational Trust**, are not
  reachable through generic Room Help or a general-question capability, and are not exported merely
  because they can be assembled.
- A **later association** with a known Person is additive. It does not retroactively reclassify the
  earlier records, and it does not extend their retention by itself.
- **An Unknown Actor Reference's Primary Hypothesis Label and Criteria Satisfaction Record (DL-74)
  change nothing above.** Naming a hypothesis — Probably One Actor, Probably Multiple Actors, or
  Unresolved Plurality — is not a characterisation of the actor, grants no retroactive permission,
  and remains bound by every rule already stated in this section.

Ordinary operational retention, extended retention, and incident-related preservation remain three
different things, classified under the floors and ceilings above and under **DL-47**, **OD-36**, and
**OD-39**.

---

## Field-level redaction

**Change Record values are privacy-classified separately from Change Record metadata.** Values may be
redacted without destroying the record of change.

Where policy requires redaction, the record retains at least:

- That a change occurred
- Subject
- Field class
- Actor or initiating process
- Effective Time
- Recorded Time
- Removal authority
- Record identity

> **A redacted record remains a record.** Redaction must not silently convert *"something changed but
> the value is no longer retained"* into *"no change occurred."*

---

## Artifact exposure

Where an artifact is stored outside Home Assistant, **the way a platform happens to display it is not
an authorisation decision.**

Home Assistant's documented behaviour makes storage attached with a **Media** usage visible in the
media browser and protects media directories with **Home Assistant authentication**. That
documentation establishes authentication; it establishes **neither per-person authorisation nor that
an unlisted file type is unreachable by every path**, and the same directories are reachable through
file-access apps.

| Rule | Statement |
|---|---|
| Visibility, not security | Keeping an artifact out of the media browser **reduces incidental exposure**. It is an additional **visibility boundary**, never the sole security or authorisation control |
| Governance is the boundary | Access remains governed by HTBW, **Operational Trust**, privacy, and consent |
| No convenience exposure | **HTBW must not expose sensitive internal artifacts as resident media for convenience.** Voiceprints, temporary enrollment samples, and governed history are internal runtime artifacts, not media |
| Capability-mediated retrieval | Documents intended for residents are opened **through the owning capability**, without requiring general storage browsing |
| Paths stay private | **Physical storage paths are not exposed** through ordinary UI, diagnostics, Repairs, or service responses where a governed artifact identifier is sufficient |

See [connected-storage.md](connected-storage.md).

---

## Tombstones

When a governed record is deleted, purged, or truncated, a **Tombstone** remains where the
architecture requires one.

A Tombstone may retain: record identity, subject, record class, removal timestamp, removal authority,
removal reason classification, and correlation linkage where permitted.

These states must always be distinguishable:

| State | Meaning |
|---|---|
| No event occurred | Nothing happened |
| No record was created | Something happened but produced no governed record |
| A record existed but was purged | Removed by retention policy |
| A record existed but was deleted | Removed by an authorised deletion request |
| A record existed but was redacted | Retained, with values removed |
| A record is unavailable | Cannot currently be reached |
| A record is withheld by policy | Exists and is retained, but is not disclosable to this audience |

> **Do not silently truncate history.**

### Snapshots must not defeat redaction

A Snapshot taken before a field is later redacted would otherwise reinstate removed content on
reconstruction. Snapshots must honour subsequent redaction and deletion, and **must never reintroduce
content removed under privacy policy**. See [../models/temporal-record.md](../models/temporal-record.md).

---

## Preservation Hold

A Preservation Hold protects applicable records from normal purge, truncation, archival deletion, or
retention-driven deletion.

| Aspect | Owner |
|---|---|
| Authorisation; who may create, review, and release; visibility; conflict with deletion; duration and review | **Operational Trust** |
| Enforcement over its own records; prevention of applicable purge or truncation; preservation of required references | **Each owning responsibility** |

A hold must be **discoverable**, **attributable**, **bounded or periodically reviewed**, **independent
of normal visibility permissions**, and **explainable**.

- **A hold does not automatically increase visibility.** Preserving a record is not disclosing it.
- A hold does not retain content that was never permitted to be retained. **A hold cannot preserve
  raw biometric internals or raw voice samples, because those were never stored.**
- An indefinite, unreviewed hold defeats minimisation and is prohibited.

Whether a hold may override an authorised deletion request is **not decided here**. Open decision
**OD-39**.

### Transitive hold integrity

Because Decision Traces reference exact versions rather than copying payloads, **holding a Decision
Trace must also preserve the exact governed source versions required to keep the trace explainable**,
subject to privacy and legal constraints.

Dependencies may include Facts, Identity Assertions, policies, obligations, preferences, sessions,
Room Configuration, vocabulary mappings, and explicit human requests.

> **A held trace whose required references have been silently purged is a preservation failure.**

**Do not duplicate referenced payloads merely to satisfy a hold.** Protect the referenced records
according to their canonical owners.

---

## Evidence Package

An Evidence Package is a projection over governed records, assembled on demand for a stated scope —
a date and time range, an incident retrieval scope, a Room, a Merged Room, an Asset, a Person, a
responsibility, a correlation identifier, or a causation chain.

Every package records its assembly time, requesting authority, scope, applied filters, included and
excluded record classes, redactions, missing-record markers, purged-record markers,
withheld-by-policy markers, known historical gaps, and relevant provenance references.

An Evidence Package creates **no** alternative historical source of truth, does **not** replace or
become authoritative over the underlying records, **may legitimately differ** when assembled at
different times because retention and redaction advance, and **must never claim completeness when
gaps exist**.

Assembly, transport, integrity representation, and permitted audience are **not decided here**. Open
decision **OD-40**.

---

## Legal and regulatory non-claim

**This architecture does not claim to produce legal-grade evidence.**

HTBW does not assert court admissibility, legal chain-of-custody sufficiency, tamper-evidence
certification, forensic certification, regulatory compliance, or compliance with any legal retention
regime.

Any legal, regulatory, insurance, investigative, or court-admissibility requirement requires separate
professional and technical validation.

**Preservation Hold and Evidence Package are HTBW architectural terms. They are not claims of legal
effect.**

---

## Explanation and privacy

An explanation must not become a disclosure channel. It may state that a policy prevented an action
without naming a protected fact. See [explainability.md](explainability.md).

---

## Deliberately undecided

The following are recorded as open decisions and must **not** be resolved inside a contract or model:

| ID | Open decision |
|---|---|
| OD-05 | Decision Trace retention floor and ceiling |
| OD-06 | **Resolved as DL-56.** Consent user experience and its Home Assistant-native surface |
| OD-07 | Local versus cloud voice implementation |
| OD-08 | **Resolved** as **DL-39** and **DL-40** |
| OD-09 | Export and deletion mechanics across connected storage |
| OD-33 | **Closed — DL-43, DL-46, DL-47.** Retention is declared inside every governed record and artifact lifecycle; the remaining values are **OD-05**, **OD-26**, **OD-49** |
| OD-36 | Reconciliation of deletion and export obligations with retention floors and Preservation Holds |
| OD-39 | Preservation Hold authority, duration, review, release, and conflict with deletion |
| OD-40 | Evidence Package assembly, transport, integrity representation, and audience |
| OD-49 | Communication retention floor and ceiling, with content and metadata classified separately |
| OD-52 | **Closed — DL-71.** Audience specification model, including resolution of *anyone present with authority* |
| OD-57 | Indication versus content separation, and when content-free indication becomes mandatory |

See [../governance/decision-ledger.md](../governance/decision-ledger.md).

---

## Related documents

- [../models/person-and-identity.md](../models/person-and-identity.md)
- [../models/operational-trust.md](../models/operational-trust.md)
- [../models/temporal-record.md](../models/temporal-record.md)
- [../models/communication.md](../models/communication.md)
- [connected-storage.md](connected-storage.md)
- [failure-and-degradation.md](failure-and-degradation.md)
- [adr-historical-explainability-and-historical-truth.md](adr-historical-explainability-and-historical-truth.md)
- [adr-temporal-record-model.md](adr-temporal-record-model.md)
- [adr-resident-communication-and-delivery-separation.md](adr-resident-communication-and-delivery-separation.md)
