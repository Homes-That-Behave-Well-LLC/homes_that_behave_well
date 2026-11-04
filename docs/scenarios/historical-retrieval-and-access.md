# Scenario — Historical Retrieval and Access

> **Document status: Canonical scenario.**
> Terminology: [../models/glossary.md](../models/glossary.md).
> Demonstrates: **DL-130** (resolved **OD-35**) — the retrieval surface, query classification,
> Subject Authorization reusing `caretaker-of` and **DL-71**, the Category-7 split, the gap model, and
> the refusal/disclosure discipline. Compare with
> [where-is-tom.md](where-is-tom.md), [where-is-maisey.md](where-is-maisey.md),
> [where-is-my-phone.md](where-is-my-phone.md), and
> [why-did-this-happen.md](why-did-this-happen.md), which this scenario extends to historical and
> reconstruction-risk questions without altering any of their current-location rules.

---

## Why this scenario exists

Current-location questions were already governed. **This scenario demonstrates that a historical or
reconstruction-risk question reaches the identical surface, and an identical Access-then-Disclosure
discipline, through classification rather than through a second authority model.**

---

## Scenario 1 — Ordinary historical decision explanation

Tom asks the Den assistant: *"Why did the Den shades close last night?"*

| Step | Outcome |
|---|---|
| Classification | Ordinary retrieval; Subject = Decision; Reconstruction-Required = false |
| Source | A retained **DL-129** Decision Trace exists |
| Result | The trace is retrieved and explained. No reconstruction is attempted |
| Surface | Assist, audience-evaluated per **DL-34** |

---

## Scenario 2 — Historical device state, not a Decision

Tom asks: *"When did the Den shades last close?"*

| Step | Outcome |
|---|---|
| Classification | Ordinary retrieval; Subject = Asset/Room; Record Class = Truth Fact history |
| Source | Truth's Fact history (**P28**) |
| Result | The last Fact is reported. **No Decision Trace is manufactured** — the question concerns a Fact, not a decision |

---

## Scenario 3 — Category 7, HTBW decided not to act

A Person authorized to control the Den shades asks: *"Why didn't the shades close?"*

| Step | Outcome |
|---|---|
| Classification | Inaction/non-event explanation (category 7) |
| Branch resolved | A Decision Trace exists — HTBW evaluated and decided not to act (**DL-15**) |
| Result | The trace is retrieved and explained, stated as the governed-decision branch |

## Scenario 3a — Category 7, HTBW made no decision

Identical question, different history: no HTBW evaluation occurred.

| Step | Outcome |
|---|---|
| Branch resolved | No Decision Trace exists — HTBW made no decision |
| Result | A diagnostic reconstruction from native condition-entity history (**DL-73**, **DL-111**), explicitly labelled diagnostic, carrying its own confidence, **never borrowed from the Decision Trace branch** |

---

## Scenario 4 — Authorized Person history (Subject Authorization)

Tom asks: *"Where was David yesterday afternoon?"*

| Step | Outcome |
|---|---|
| Classification | Person scope; Record Class = Identity Assertion/Truth Fact history; Reconstruction-Required = true |
| Capability gate | Allow General Questions/Allow Home Steward are **not** evaluated — they never authorize Person/movement retrieval |
| Subject Authorization | Operational Trust evaluates **David's** configured access policy (Person-scope, expressed via **DL-71**'s specification forms). If the policy names a Relationship-based form ("Caretaker of David"), Tom's `caretaker-of` relationship (**DL-49**) supplies a **candidate** only |
| Access decision | Confirmed or denied by Operational Trust's own Person/Relationship-scope evaluation (**DL-126**) — the relationship alone is never sufficient |
| If permitted | Retained Explainability evidence is retrieved; reconstruction is used only where necessary; gaps are stated explicitly |
| Disclosure | Evaluated separately, against the current audience (**DL-34**), after Access |

---

## Scenario 5 — Unauthorized Person history

A houseguest asks: *"Where was David yesterday?"*

| Step | Outcome |
|---|---|
| Capability gate | A configured general-question capability, if any, does not reach this path |
| Subject Authorization | The houseguest holds no configured access to David's history |
| Result | **Access denied.** The refusal is content-free: *"I can't share that history."* It does not confirm or deny that evidence exists (existing six-outcome disclosure table, no new wording) |

---

## Scenario 6 — Maisey, a trackable Pet subject

An authorized Person asks: *"Where was Maisey yesterday afternoon?"*

| Step | Outcome |
|---|---|
| Subject | Maisey is a Foundation **Pet** object, never a Person (`where-is-maisey.md`) |
| Subject Authorization | The identical mechanism as Scenario 4 — `caretaker-of` (**DL-49**, typed over Person/Pet/Asset) supplies a candidate; Operational Trust confirms access |
| Result | Truth-only Pet-location history is retrieved, subject to the same consent rule as current-location questions: pet-location evidence is never used to derive human movement without separate consent |

---

## Scenario 7 — Group/Role-based authorization

A requester's access is configured as a Role/Authority Class (for example, "Resident") rather than a
Named Person.

| Step | Outcome |
|---|---|
| Resolution | **DL-71**'s existing Role/Authority Class specification form resolves the requester's eligibility; no shadow roster is created |

---

## Scenario 8 — Voice, with guests present

Tom is authorized to receive David's historical location. Tom asks aloud in a Room containing guests.

| Step | Outcome |
|---|---|
| Access | Granted to Tom (Scenario 4) |
| Disclosure | Evaluated separately against the **current audience** (**DL-34**, **DL-72**) — Tom's own access never authorizes broadcasting to everyone present |
| Result | Private redirect, content-free indication, confirmation, or refusal — whichever the existing **OD-71** default order selects. Access itself is unaffected |

---

## Scenario 9 — Multi-Room macro retrieval

*"What was everything impacted by my 'turn off all downstairs lights' command last night?"*

| Step | Outcome |
|---|---|
| Source | Correlated, Room-normalized **DL-129** Decision Traces, aggregated via their shared **DL-104** correlation identifier |
| Partial retention | Available traces are returned; a Room whose trace has expired is reported as a stated gap, never fabricated |

---

## Scenario 10 — Native long-term-statistics gap

*"What was the highest temperature in the Kitchen last month?"*

| Step | Outcome |
|---|---|
| Source | Native long-term statistics |
| Gap handling | Native statistics performs no gap detection of its own (Issue #146, VERIFIED_SUPPORTED). **HTBW's own assembly step detects and reports the missing interval** — this decision's one new structural obligation |
| Result | The available maximum is reported, with the gap stated, never presented as continuous complete coverage |

---

## Scenario 11 — Actor reconstruction

*"Who was moving through the house Tuesday afternoon?"*

| Step | Outcome |
|---|---|
| Classification | Reconstruction-Required = true |
| Routing | Reaches Assist, but is routed into the dedicated governed Historical Reconstruction path — never answered by generic Room Help or a general-question capability |
| Result | An Unknown Actor Reference reconstruction (**DL-35**, **DL-74**): alternatives and gaps preserved, no identity, role, or criminality asserted |

---

## Scenario 12 — General Questions does not grant movement access

A Person authorized for General Questions asks a question that would require historical Person
movement reconstruction.

| Step | Outcome |
|---|---|
| Capability gate | Allow General Questions (**DL-93**) is evaluated and may be YES — it is a **top-level eligibility gate only** |
| Subject Authorization | Evaluated independently; General Questions authorization does not satisfy it |
| Result | Protected historical household data is never sent to a Reasoning provider on the strength of General Questions authorization alone |

---

## Related documents

- [../governance/decision-ledger.md](../governance/decision-ledger.md) — **DL-130**
- [../architecture/adr-governed-historical-retrieval-and-access.md](../architecture/adr-governed-historical-retrieval-and-access.md)
- [../architecture/explainability.md](../architecture/explainability.md)
- [../models/operational-trust.md](../models/operational-trust.md)
- [../models/temporal-record.md](../models/temporal-record.md)
- [why-did-this-happen.md](why-did-this-happen.md)
