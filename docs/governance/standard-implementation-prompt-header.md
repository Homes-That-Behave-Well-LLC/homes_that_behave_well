# Standard Implementation Prompt Header

> **Document status: Active — subordinate to the HTBW canonical architecture.**
> Canonical authority: [authority-order.md](authority-order.md),
> [../architecture/framework.md](../architecture/framework.md), and
> [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Where this document names **Voice Identity** or **Asset Intelligence** as an ownership domain, it
> refers to the separately released **repository**, not to an HTBW Core layer. HTBW Core has no Voice
> Identity layer: the responsibility is **Identity**, and voice is one evidence source. See
> [../models/glossary.md](../models/glossary.md) section "Products versus responsibilities".

## 1. Purpose

Define the purpose of the Standard Implementation Prompt Header.

This document establishes the authoritative E15-G2 reusable implementation prompt-header baseline that operationalizes E15-G1 execution governance before any implementation work begins.

This document is architecture and governance only.

This document does not define runtime implementation behavior, platform capabilities, integrations, automation behavior, new architecture, or redefinition of existing architecture.

## 2. Scope Reviewed

Documented review of:

- HTBW #14
- HTBW #16
- HTBW #17
- HTBW #18
- HTBW #20
- HTBW #23
- HTBW #31
- HTBW #39
- HTBW #47
- HTBW #50
- Concierge #176
- E15-G1

Reviewed associated authority surfaces:

- HTBW ADR collection
- HTBW contracts
- HTBW models
- existing implementation authorities
- execution governance artifacts

## 3. Prompt Governance Validation

Validation scope:

- prompt governance authority
- execution governance authority
- review authority

Result: PASS

Prompt governance authority is established by E15-G1 and consumed by this reusable header standard.

Execution governance authority remains grounded in authority-order enforcement.

Review authority remains governance-bound and traceability-driven.

## 4. Authority Order Validation

Authority order:

1. ADR
2. Contract
3. Model
4. Existing Implementation
5. GitHub Issue

Result: PASS

## 5. Implementation Grounding Sequence Validation

Required grounding sequence:

1. Read ADRs
2. Read Contracts
3. Read Models
4. Read Existing Implementation
5. Read GitHub Issue

Only after all five steps may implementation begin.

Result: PASS

## 6. GitHub Issue Authority Review

Issue purpose:

- execution planning, sequencing, and closure criteria.

Issue limitations:

- GitHub Issue is not architecture authority.

Issue authority boundaries:

- GitHub Issue is subordinate to ADR, Contract, Model, and Existing Implementation authority.

Result: PASS

## 7. Conflict Detection Review

Conflict identification:

- identify contradictions between issue instructions and higher authority artifacts.

Conflict validation:

- validate conflicts in authority-order sequence from ADR through Existing Implementation.

Escalation workflow:

- document conflict, impact, and correction recommendation for authority alignment.

Result: PASS

## 8. Stop Condition Review

Mandatory stop conditions:

- issue conflicts with ADR
- issue conflicts with Contract
- issue conflicts with Model
- issue conflicts with Existing Implementation authority interpretation
- authority order cannot be validated
- conflict handling cannot be completed

Result: PASS

## 9. ADR Conflict Workflow

When issue conflicts with ADR:

- stop execution immediately
- document conflict with ADR citation
- document expected impact
- recommend correction aligned to ADR
- do not implement conflicting behavior

Result: PASS

## 10. Contract Conflict Workflow

When issue conflicts with Contract:

- stop execution immediately
- document conflict with Contract citation
- document expected boundary impact
- recommend correction aligned to Contract
- do not implement conflicting behavior

Result: PASS

## 11. Model Conflict Workflow

When issue conflicts with Model:

- stop execution immediately
- document conflict with Model citation
- document expected semantic impact
- recommend correction aligned to Model
- do not implement conflicting behavior

Result: PASS

## 12. Existing Implementation Conflict Workflow

When issue conflicts with Existing Implementation:

- stop execution immediately
- document conflict with implementation citation
- document expected behavioral impact
- recommend correction aligned to authoritative implementation and upstream authority
- do not implement conflicting behavior

Result: PASS

## 13. Prompt Header Structure Review

Required prompt-header structure:

1. repository and issue context
2. governance task declaration
3. authority-order declaration
4. mandatory grounding sequence declaration
5. conflict and stop-condition declaration
6. required source review declaration
7. execution constraints declaration
8. output and closure requirements declaration

Result: PASS

## 14. Mandatory Header Section Review

Every implementation prompt header must contain:

- execution governance principle
- authority order
- implementation grounding sequence
- special acceptance direction for conflicts
- mandatory authority review inputs
- required outputs and closure steps
- validation gates
- final determination requirements

Result: PASS

## 15. Prompt Execution Workflow Review

Workflow after grounding review:

1. validate authority order completion
2. validate grounding sequence completion
3. validate conflict checks
4. execute only authority-aligned work
5. document governance traceability

Result: PASS

## 16. Prompt Validation Workflow Review

Validation workflow:

1. validate required header sections
2. validate authority-order statements
3. validate grounding sequence statements
4. validate stop-condition statements
5. validate traceability expectations

Result: PASS

## 17. Repository Applicability Review

Applicability scope:

- HTBW
- Concierge
- Voice Identity
- Asset Intelligence
- Future repositories

This prompt-header standard is applicable across all HTBW-governed repositories.

Result: PASS

## 18. Copilot Usage Review

Copilot execution expectations:

- treat GitHub Issues as execution inputs, not architecture authority.

Grounding expectations:

- complete ADR, Contract, Model, Existing Implementation, then GitHub Issue review before implementation.

Authority validation expectations:

- validate authority order and conflicts before execution.

Result: PASS

## 19. Implementation Review Expectations

Implementation review requirements:

- review authority alignment before implementation scope is accepted.

Authority review requirements:

- verify ADR/Contract/Model/Existing Implementation/GitHub Issue sequence completion.

Validation requirements:

- verify conflict checks, stop conditions, and traceability documentation.

Result: PASS

## 20. Standard Prompt Header Definition

Authoritative reusable prompt-header template:

```text
HTBW EXECUTION GROUNDING STANDARD

You are working on the Homes That Behave Well platform.

This is an architecture/governance-grounded implementation task.

Authority order:
1. ADR
2. Contract
3. Model
4. Existing Implementation
5. GitHub Issue

GitHub Issues are execution plans.
GitHub Issues are NOT architecture authority.

Before implementation begins, complete grounding in this exact sequence:
1. Read referenced ADRs.
2. Read referenced Contracts.
3. Read referenced Models.
4. Read Existing Implementation.
5. Read the GitHub Issue.

If issue guidance conflicts with ADR, Contract, Model, or Existing Implementation:
STOP.
Document conflict.
Recommend correction.
Do not implement conflicting behavior.

Required execution constraints:
- Do not redefine architecture authority.
- Do not bypass grounding sequence.
- Do not treat GitHub Issue as architecture authority.

Required outputs:
- governance-traceable implementation changes
- documented authority references
- conflict status
- closure evidence aligned to issue requirements

For any change to a Home Assistant integration or App, also apply the
Home Assistant Gold Quality Gate (home-assistant-distribution-and-quality-standard.md,
section 6.1) before, during, and after implementation.
```

Result: PASS

## 21. Prompt Example Review

Example implementation prompt using the standard:

```text
HTBW EXECUTION GROUNDING STANDARD

Task executes: <issue-id and title>
Repository: <owner/repo>

Before coding:
1. Read ADR references: <list>
2. Read Contract references: <list>
3. Read Model references: <list>
4. Read Existing Implementation references: <list>
5. Read GitHub Issue: <issue-url>

Authority order:
1. ADR
2. Contract
3. Model
4. Existing Implementation
5. GitHub Issue

If conflict exists:
STOP.
Document conflict.
Recommend correction.
Do not implement conflicting behavior.

Execution output requirements:
- implement only authority-aligned scope
- document authority traceability
- provide validation and closure evidence
```

Result: PASS

## 22. Governance Traceability Review

Prompt traceability requirements:

- ADR references must be explicitly listed.
- Contract references must be explicitly listed.
- Model references must be explicitly listed.
- Existing Implementation references must be explicitly listed.
- GitHub Issue reference must be explicitly listed and treated as lowest authority.

Result: PASS

## 23. Governance Traceability Matrix

| Authority Surface | Prompt Requirement | Traceability Expectation |
|---|---|---|
| ADR | include ADR references first | highest authority evidence documented |
| Contract | include contract references second | boundary evidence documented |
| Model | include model references third | semantic evidence documented |
| Existing Implementation | include implementation references fourth | behavior evidence documented |
| GitHub Issue | include issue reference last | execution-only input evidence documented |

Result: PASS

## 24. Prompt Validation Checklist

Checklist for validating implementation prompts:

- verify standard prompt header used
- verify ADR review required
- verify Contract review required
- verify Model review required
- verify Existing Implementation review required
- verify GitHub Issue review required and listed last
- verify authority order documented
- verify conflict workflow documented
- verify stop conditions documented
- verify governance traceability documented

Result: PASS

## 25. Ownership Preservation Review

Validation scope:

- architecture ownership
- contract ownership
- model ownership
- implementation ownership

Result: PASS

Ownership is preserved through authority-order enforcement and mandatory conflict-stop behavior.

## 26. Drift Prevention Review

Drift prevention requirements:

- authority drift prevention through explicit hierarchy and stop conditions
- prompt drift prevention through mandatory reusable header structure
- implementation drift prevention through grounded pre-implementation validation

Result: PASS

## 27. E15 Foundation Consumption Review

Validation scope:

- alignment with E15-G1 execution-governance baseline

Result: PASS

E15-G2 consumes and operationalizes E15-G1 without redefining authority order or conflict governance.

## 28. Roadmap Applicability Review

Standard prompt headers support roadmap execution and closure by enforcing repeatable authority validation, conflict handling, and governance traceability before implementation begins.

Result: PASS

## 29. Final Governance Assessment

Governance assessment:

- implementation prompt authority is explicitly constrained by architecture authority order.
- execution control is enforced through grounding sequence and mandatory stop conditions.
- governance traceability is explicit and reusable across repositories.

Result: PASS

## 30. Final Determination

E15-G2 STANDARD IMPLEMENTATION PROMPT HEADER

APPROVED AS THE AUTHORITATIVE BASELINE

FOR IMPLEMENTATION EXECUTION PROMPTS
