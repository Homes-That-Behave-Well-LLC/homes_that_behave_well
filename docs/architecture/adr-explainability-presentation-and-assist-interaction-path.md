# ADR: Explainability Presentation — Assist as the Canonical Household-Facing Interaction Path

> **Document status: Canonical ADR.**
> Status: **Accepted** 2026-11-05. Records **DL-140** (issue **#80**, formal acceptance review PASS).
> Resolves **OD-30** in full.
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Terminology: [../models/glossary.md](../models/glossary.md),
> [../models/decision-trace.md](../models/decision-trace.md),
> [explainability.md](explainability.md).

---

## Status

**Accepted 2026-11-05.** Resolves every OD-30 acceptance criterion. This ADR creates **no second
Explainability store**, **no raw Decision Trace viewer**, **no administrator bypass**, **no audit-log
bypass**, **no unrestricted dashboard exposure**, **no passive Explainability feed**, **no generic Room
Help access to protected reconstructions**, and **no second Historical Retrieval system**. It does not
reopen **DL-15**, **DL-33**, **DL-34**, **DL-35**, **DL-36**, **DL-39**, **DL-41**, **DL-46**, **DL-69**,
**DL-72**, **DL-88**, **DL-90**, **DL-104**, **DL-113**, **DL-114**, **DL-126**, **DL-129**, **DL-130**,
or the amended **DL-137** — each is consumed unchanged.

---

## Context

OD-30's historical wording asked "which surfaces expose Decision Traces, and to whom." Current accepted
architecture (**DL-137**) requires more precise terminology before that question can even be answered:
**Decision Trace** is the governed reasoning/evaluation process; **Explainability Record** is the
persisted result of that process. OD-30's real, residual question is therefore: **how an Explainability
Record may be retrieved and presented to a household participant.**

**Most of this question is already answered.** Between this issue's opening (2026-08-26) and today, four
of its own cited dependencies closed and substantially narrowed its scope:

- **DL-69** (OD-62) confirmed Conversation as one pre-answer-filtered retrieval/answer surface for
  Decision-Trace-derived content.
- **DL-72** (OD-71) settled the default degradation order under audience uncertainty and the Decision
  Trace fields required to explain it.
- **DL-129** (OD-29) settled Explainability persistence, structure, and write-time assembly.
- **DL-130** (OD-35) settled **Assist/Conversation as the sole resident-facing historical-retrieval
  interaction surface**, a twelve-step authorization sequence, and the full Episode 9 query-category
  mapping — **this is the single largest consumption for this decision**, and this ADR does not
  reopen, duplicate, or compete with it.

**What DL-130 did not decide, and what remains this issue's own residual**: the specific **endpoint
categories** (Companion App, dashboard/kiosk, voice) through which Assist/Conversation is invoked, and
whether/how they differ in what context they contribute; the explicit rejection of a two-persisted-
rendering model and of an administrator bypass; Unknown Person and affected-guest presentation behavior
specifically for Explainability requests; and the explicit statement that surface/endpoint visibility is
never itself authority. This ADR resolves exactly that residual, consuming DL-130 as its own retrieval
and authorization engine rather than inventing a parallel one.

**Owner direction governing this closure:** **Assist is the canonical household-facing Explainability
interaction path.** Companion App, dashboard/kiosk, and voice are endpoints through which Assist is
invoked — not independent Explainability capabilities and not independent authorization paths.

---

## Decision

### 1. Terminology corrected: Explainability Projection

Three terms, precisely distinguished, consuming **DL-137** unchanged:

| Term | Meaning |
|---|---|
| **Decision Trace** | The governed reasoning/evaluation process that produces an explanation (**DL-137**, unchanged) |
| **Explainability Record** | The persisted, durable result of that process (**DL-137**, unchanged) |
| **Explainability Projection** | **New.** The non-persisted, audience-governed rendering assembled from an Explainability Record for the current requester, audience, endpoint, and context |

**There is one authoritative Explainability Record.** Every household-facing response is a governed
projection assembled at read/presentation time. No separate persisted resident, guest, administrator,
technical, or redacted rendering is created — this rejects Option B outright (see §13).

### 2. Assist is the canonical household-facing Explainability interaction path

Restating and extending **DL-130** (not reopening it): **Assist/Conversation is the canonical
household-facing path through which an Explainability question is asked and an Explainability
Projection is delivered.** An Explainability request may enter Assist through:

- typed Assist in the Home Assistant Companion App;
- typed Assist presented through an authorized dashboard or kiosk;
- spoken Assist through a voice-assistant/voice endpoint;
- another future governed Assist endpoint satisfying the same requester/Room/audience/authorization/
  presentation contract.

**These are endpoints through which Assist is invoked. They are not independent Explainability
capabilities, and they are not independent authorization paths.** The canonical flow:

```
INTERACTION ENDPOINT
  -> ASSIST
  -> CONCIERGE / EXPLAINABILITY CAPABILITY
  -> OPERATIONAL TRUST ACCESS AND DISCLOSURE EVALUATION
  -> AUDIENCE-GOVERNED EXPLAINABILITY PROJECTION
  -> ASSIST
  -> INTERACTION ENDPOINT
```

This is **DL-130**'s own twelve-step authorization sequence (classification → requester resolution →
capability gate → Subject Authorization → Operational Trust Access decision → refusal or retrieval →
gap preservation → audience/disclosure → presentation → Decision Trace recording), restated here with
the endpoint explicitly named as the entry/exit point, never as a second authority.

### 3. Endpoint categories

Foundation already owns the relationships that ground each category — this decision assigns no new
ownership, it classifies existing endpoint relationships as Assist entry points:

| Category | Governing relationship, already accepted |
|---|---|
| **Companion App Assist** | A private, typically non-Room-bound surface. Where not bound to a Room, Room Context resolves through **DL-113**'s existing composed order (explicit supply → declared surface default → `unresolved`), never guessed from the app's owner |
| **Dashboard/Kiosk Assist** | The `interface`/kiosk Room-Interaction-Capability relationship Foundation already owns (**DL-88**) |
| **Voice Assist** | The `voice_input`/`spoken_response_output` Room Interaction Function Assignments Foundation already owns (**DL-90**), never a hard-coded microphone-to-speaker mapping |
| **Future governed Assist endpoint** | Must satisfy the same requester/Room/audience/authorization/presentation contract as the three above; no new contract is invented per endpoint |

**None of these four categories are three (or four) different Explainability systems.** They are
endpoint contexts for one governed Assist interaction.

### 4. Endpoint contributes context, never authority

The endpoint may contribute: device/resource identity; associated Person evidence; requester evidence;
Room context; audience context; private/shared classification; signed-in user context; voice identity
evidence; output modality; whether content will be spoken aloud; whether visual output may remain
visible; current presentation limitations.

**The endpoint itself never grants Explainability authority.** Stated explicitly as four non-equations:

```
SURFACE VISIBILITY        != ACCESS AUTHORITY
SURFACE AVAILABILITY      != DISCLOSURE AUTHORITY
DEVICE OWNERSHIP          != UNRESTRICTED EXPLAINABILITY AUTHORITY
HA ADMINISTRATOR STATUS   != HTBW GOVERNANCE AUTHORITY
SIGNED-IN USER            != COMPLETE AUDIENCE COMPOSITION
```

A private Companion App endpoint may support stronger requester evidence and a private presentation
channel, but device ownership alone does not bypass Identity, authenticated device context does not
bypass Operational Trust, and private-surface status does not automatically authorize all protected
detail — another Person using the phone must not automatically inherit the owner's Explainability
authority. A shared wall kiosk provides Room context, an endpoint identity, and visual presentation,
but it is a shared surface where the requester may be uncertain and the audience may be mixed — a
signed-in kiosk session does not erase audience risk (Scenario 18). A voice endpoint provides input
context, Room context, requester and audience evidence, and output modality, but spoken content may be
overheard — output is evaluated for everyone who may hear it, never for the speaker alone.

### 5. Access, Disclosure, and Presentation remain three separable considerations

Consuming, not replacing, existing architecture — **no new recorded-outcome field is created**:

| Consideration | Already-accepted mechanism this decision reuses |
|---|---|
| **Access** | Decision Trace's existing **Access decision** field (`decision-trace.md`); whether the governed capability may retrieve/use the Explainability Record at all, including DL-130's Subject Authorization where the record concerns a Person/Pet |
| **Disclosure** | Operational Trust's existing **"Access and disclosure are two decisions"** six-outcome table (`operational-trust.md`); whether the resulting content may be disclosed to this requester/audience at all |
| **Presentation** | Decision Trace's existing **Presentation decision** field (Address by Name, named/neutral, audience/disclosure constraint); **this decision adds the specificity, new to Explainability requests, that Presentation also evaluates endpoint/modality eligibility** — whether the authorized content may be rendered on this endpoint, through this modality, right now |

A possible outcome: access allowed; disclosure partially allowed; private presentation not available on
the current endpoint. **These are never collapsed into one boolean.** Record them as the existing fields
already allow, never as a new field.

### 6. Per-request, per-audience, per-endpoint projection at read time

Selecting the core of Option A (rejecting B and the pure-gating reading of C — see §13): **Explainability
is filtered/projected at read/presentation time**, considering requester, resolved Person, audience
composition, audience uncertainty (**DL-72**), endpoint, Room, output modality, information
classification, affected Person, protected content, current purpose, and current Operational Trust
policy. **A projection generated for a prior requester is never reused for a different requester or
audience.** A resident-authorized rendering is never cached and replayed to a different audience without
fresh evaluation. No audience-specific copy is persisted as a second authority — only the one
Explainability Record persists; every projection is assembled, never stored.

**Surface/endpoint change requires fresh evaluation.** A requester who begins on shared voice Assist and
continues on private Companion App Assist triggers a new endpoint/audience evaluation; no assumption is
made that prior authorization (or refusal) automatically transfers (Scenario 17).

### 7. Governed capability gating, without artificial burden

Consuming the useful control from Option C: Explainability is reachable only through the governed
Assist/Concierge/Operational Trust path — the endpoint cannot directly query raw Explainability
persistence. **This does not mean ordinary "why?" questions must feel artificially gated.** Operational
Trust may authorize ordinary Explainability according to current capability/Identity bands exactly as it
authorizes any other capability (**DL-39**). A surface may never bypass capability classification,
Identity resolution, access, disclosure, audience, or presentation evaluation merely to make a response
feel faster.

### 8. No persisted audience-specific renderings; no administrator bypass

**Option B is rejected as a persistence model.** No resident-safe persisted trace, administrator
persisted trace, technical persisted trace, or raw-plus-redacted-clone pair is created. There is one
authoritative Explainability Record; the read-time projection supplies the appropriate presentation.

**An HA administrator account does not automatically receive unrestricted Explainability access.**
Native administrator status does not replace Identity, does not replace Operational Trust, does not
grant access to private resident information, does not allow raw Explainability database browsing
through HTBW, and does not bypass presentation policy (restating **DL-31**'s "native platform status is
not HTBW authority" pattern, applied here to Explainability specifically). If an administrator is also a
governed Person with appropriate authority, Operational Trust may authorize permitted detail for that
Person/context — **authority comes from HTBW governance, not the HA admin flag.**

**No user-selectable "detail level" bypass exists.** A requester asking to "show technical details,"
"show raw trace," "administrator view," "full audit," or "unredacted explanation" triggers another
full access/disclosure/presentation evaluation — never a debug flag that becomes a privacy bypass.
Additional detail is returned only if authorized and suitable for the current endpoint/audience.

### 9. Partial authority is honest

Where the requester/audience may receive some explanation but not protected details: the projection
never exposes protected content, never lies, never silently omits the existence of a governing reason
where acknowledging the boundary is itself permitted, never implies no reason existed, and never implies
the record was incomplete when content was withheld by policy. Preferred form, reusing **DL-69**'s
existing honest-response vocabulary (Unknown / Unavailable / Not understood / Clarification required /
Not authorized / Cannot answer here / Unsupported) and `why-did-this-happen.md` Scenario 8's own worked
pattern:

> *"The action was suppressed because an applicable household policy was active. I can't provide the
> protected details on this surface or to the current audience."*

**Withholding itself may require protection.** Operational Trust determines whether the projection may
state that a protected detail exists, its category, only that the answer cannot be given here, or only a
refusal — a content-free boundary statement must never leak the protected fact itself (restating
`privacy.md`'s "Indication and content are separate disclosures" principle, applied to Explainability).

### 10. Affected guest

A guest directly affected by a Home behavior may receive an honest explanation of the **observable**
behavior to the degree authorized, without the protected cause. Example: a guest asks why an
announcement didn't play; the true reason involves a resident's private health-related policy. A
permissible projection: *"The announcement was suppressed because a household communication policy
applied."* It must never reveal resident health information, medication context, private routine, the
identity of the protected resident, or private policy detail beyond what is authorized. **Being
affected by behavior is not equivalent to no explanation, and it is not equivalent to access to
protected causes.**

### 11. Unknown Person

Consuming **DL-33** unchanged: no blanket rule denies an Unknown Person every explanation. Conservative
disclosure applies instead — an Unknown Person may receive limited information about non-sensitive,
directly observable behavior where doing so does not reveal resident information, Identity evidence,
protected policy, presence/movement, actor reconstruction, Safety/Security circumvention information,
or private household operation. Safe examples: *"That action isn't available here,"* *"The device is
currently unavailable,"* *"I can't provide that explanation without identifying an authorized
requester."* **Declining must never be framed as demeaning exclusion** — restating the
unidentified-person policy's existing posture (`operational-trust.md`) that this is a governed policy
scope, not a withheld profile.

### 12. Safety/Security defeat information

An Explainability response must never coach a requester on how to defeat a Safety or Security
restriction: the exact condition that would bypass a safety interlock, the occupancy threshold that
would defeat a restriction, the Identity confidence threshold needed to impersonate a Person, security
policy detail enabling circumvention, or a private sensor/evidence combination used to authorize access.
The Home may state that a safety rule applied, authorization wasn't sufficient, the action cannot be
performed, and that a more specific explanation cannot be provided — restating `why-did-this-happen.md`
Scenario 7's existing boundary (*"the home must not coach an unidentified person on how to defeat a
safety restriction... the correct answer is simply that it cannot be done"*), extended explicitly to
every requester, not only an unidentified one.

### 13. Actor reconstruction remains excluded

Consuming **DL-35** and **DL-130** unchanged: actor reconstruction, unknown-person reconstruction,
movement history, and Person-location history must never become reachable through an ordinary
Explainability Assist question. *"Why didn't the lights turn on?"* must never become a path to *"who
moved through the room?"* A request classified as actor/Person reconstruction follows its own governed
Historical Retrieval path and authorization (**DL-130**'s own Reconstruction-Required flag,
resolved **before** assembly) — reconstruction is never hidden inside an ordinary Explainability
projection, and generic Room Help/general questions remain excluded from it.

### 14. Passive dashboard cards, direct database access, and other exclusions are not authorized

OD-30 does **not** authorize: passive dashboard cards or Lovelace cards listing Explainability Records;
an unrestricted Explainability timeline; raw Decision Trace browsing; direct SQLite database browsing;
generic Home Assistant History or Media Browser presentation as an Explainability surface; administrator
audit panels; or persistent Room-screen explanation feeds. A dashboard may host an **Assist** interface
(a typed Assist interaction displayed through the dashboard endpoint); it may not passively expose
Explainability Records merely because the dashboard is visible. A Companion App may host Assist; OD-30
does not authorize a standalone Explainability-record browser inside it. A voice endpoint may invoke
Assist; OD-30 does not authorize arbitrary TTS playback of prior Explainability Records without a new
governed interaction. **If a future governed Explainability-history browser is desired, it requires its
own explicit governance decision/capability — it is not created, and not implicitly authorized, here.**

### 15. Existing Explainability Record retrieval does not create a duplicate record

Consuming **DL-137** unchanged: when an existing Explainability Record already answers the question,
Assist retrieves it through the governed path and assembles an audience-governed Explainability
Projection — **no duplicate Explainability Record is created merely because the existing record was
viewed**, and the access/disclosure/presentation event may be recorded according to existing
Explainability architecture. **A record originally created for one audience is not automatically safe
for another audience** — current disclosure is evaluated independently of the disclosure context that
applied at the record's own creation time. Viewing the same record twice produces two governed
presentation/access events, never two Explainability Records.

### 16. On-demand Decision Trace still creates a new record, every time

Where no existing Explainability Record answers the question and current architecture calls for an
on-demand Decision Trace: the governed research/reasoning process runs using evidence authorized for
it; a new Explainability Record is created with origin `on_demand_decision_trace` and current canonical
UTC creation time; requested historical/effective scope is recorded separately (never backdated);
request parameters, gaps, and uncertainty are preserved; an Explainability Projection is then assembled
for the current Assist interaction. **The same historical question asked again creates its own new
Explainability Record each time** — DL-137's "never deduplicated, never backdated" rule, restated for
Assist specifically. The newly created record enters normal household-configured Explainability
retention (amended **DL-137**) unchanged.

### 17. Rendering does not change retention

Viewing or rendering an Explainability Record (through any Assist endpoint) does not restart its
retention, does not extend its retention, does not create a retained projection, does not automatically
place a Preservation Hold, does not create an Evidence Package, and does not create another
Explainability Record merely because it was displayed. Where the interaction itself requires a new
on-demand Decision Trace, that new reasoning invocation creates its own record under **DL-137** — these
two paths remain distinct.

### 18. Withheld, expired, or unavailable source

An Explainability Record may reference source material that is available, expired, purged, deleted,
withheld by policy, unavailable, under restricted preservation, or never recorded. The Explainability
Projection preserves those distinctions where authorized, reusing `decision-trace.md`'s existing
failure-behavior vocabulary (`"no longer retained"`, `"redacted"`) — never reconstructing expired source
content from metadata, and never claiming no source existed when it expired (restating **DL-138**'s
"on Content expiry, Metadata survives... never reconstructing the expired message" rule, applied here to
any expired referenced source, not only Communication Content).

### 19. Explainability request flow

The canonical flow, consuming **DL-69**, **DL-72**, and **DL-130** without inventing a second retrieval
pipeline:

1. Request enters Assist through a governed endpoint.
2. The requested capability is classified as Explainability/Historical Explainability (**DL-130**'s
   existing classification-before-assembly step).
3. Requester identity is resolved to the available confidence band.
4. Room context is resolved where applicable (endpoint-category-specific, §3 above).
5. Audience composition and uncertainty are evaluated (**DL-34**, **DL-72**).
6. Access to the relevant Explainability Record or on-demand reasoning process is evaluated.
7. If an existing Explainability Record answers the question, it is retrieved through the governed
   path (§15).
8. If no existing record answers the question and architecture calls for research, an on-demand
   Decision Trace runs and a new Explainability Record is created (§16).
9. Operational Trust evaluates disclosure and presentation for requester, audience, endpoint, modality,
   protected details, purpose, and surface privacy (§5).
10. An Explainability Projection is assembled.
11. The response is delivered through Assist to the endpoint.
12. The access/disclosure/presentation outcome is recorded according to existing Explainability
    architecture (§5).

### 20. Rejected alternatives

**Option B — two persisted renderings (resident-safe and administrator).** Rejected. Risks the
administrator view becoming an ungoverned bypass; creates a second Explainability model exactly where
**DL-137** established there is one authoritative repository.

**Option C alone — trace retrieval only through a governed capability with its own Required Identity
Band.** Not rejected outright; its useful control (no direct raw-persistence query) is folded into §7,
but adopted as a *component* of Option A rather than the whole model, because pure capability-gating
alone does not address per-audience, per-endpoint projection, which Option A's read-time filtering
supplies and which the Household Inbox precedent (**OD-47**) already establishes as the accepted shape
for per-viewer projection.

**Option A — per-viewer projection filtered at read time.** **Accepted**, as elaborated in §6, combined
with Option C's capability-gating discipline (§7) and explicit administrator/raw-access rejection (§8,
§14).

---

## Explicit non-goals

- **No second Explainability store, raw Decision Trace viewer, or passive Explainability feed is
  created.**
- **No administrator bypass or audit-log bypass is created.** HA administrator status is not HTBW
  governance authority.
- **No unrestricted dashboard exposure is authorized.** A dashboard may host Assist; it may not become
  a passive Explainability record browser.
- **No generic Room Help access to protected reconstructions is created.** Actor reconstruction remains
  excluded (**DL-35**, **DL-130**).
- **No second Historical Retrieval system is created.** **DL-130** remains the sole historical-retrieval
  authorization engine; this decision adds only endpoint-category clarity and explicit
  administrator/passive-surface rejection on top of it.
- **No new responsibility is created.** Concierge continues to compose and present; Operational Trust
  continues to own access/disclosure/presentation; Identity continues to supply assertions.
- **DL-69, DL-72, DL-88, DL-90, DL-113, DL-129, DL-130, and the amended DL-137 are not reopened.**
- **No unrelated Owner policy is invented**, and no HTBW-wide numeric threshold, retry count, or
  cooldown is created by this decision.

---

## Related documents

- [../models/decision-trace.md](../models/decision-trace.md)
- [explainability.md](explainability.md) — "Historical Retrieval and Access (resolved — DL-130)"
- [../models/operational-trust.md](../models/operational-trust.md) — "Access and disclosure are two
  decisions," "Historical Retrieval and Access authorization"
- [../scenarios/why-did-this-happen.md](../scenarios/why-did-this-happen.md) — Scenarios 7, 8
- [privacy.md](privacy.md) — "Decision Trace privacy," "Explanation and privacy"
- [adr-governed-historical-retrieval-and-access.md](adr-governed-historical-retrieval-and-access.md)
  (**DL-130**)
- [adr-explainability-persistence-and-retention.md](adr-explainability-persistence-and-retention.md)
  (**DL-137**)
- [adr-decoupled-voice-interaction-capability-architecture.md](adr-decoupled-voice-interaction-capability-architecture.md)
  (**DL-90**)
- [adr-stable-endpoint-identity-and-network-boundary-independence.md](adr-stable-endpoint-identity-and-network-boundary-independence.md)
  (**DL-88**)
- [../contracts/concierge-contract.md](../contracts/concierge-contract.md)
- [../models/glossary.md](../models/glossary.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
