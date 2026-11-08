# Issue Execution Review Checklist

> **Document status: Operational.**
> Non-architectural process/checklist document. Canonical architecture:
> [../architecture/framework.md](../architecture/framework.md). Terminology:
> [../models/glossary.md](../models/glossary.md).

## 1. Purpose

Define the purpose of the Issue Execution Review Checklist.

This document establishes the authoritative E15-G3 execution-review governance baseline used to evaluate issue execution against authoritative sources before issue closure.

This document operationalizes E15-G1 and E15-G2.

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
- Concierge #177
- E15-G1
- E15-G2

Reviewed associated authority surfaces:

- HTBW ADR collection
- HTBW contracts
- HTBW models
- existing implementation authorities
- execution governance artifacts

## 3. Review Governance Validation

Validation scope:

- review governance authority
- execution governance authority
- review ownership

Result: PASS

Review governance authority is established by E15-G1 and operationalized by E15-G2 and E15-G3.

Execution governance authority remains authority-order constrained.

Review ownership remains governance-bound and traceability-driven.

## 4. Authority Order Validation

Authority order:

1. ADR
2. Contract
3. Model
4. Existing Implementation
5. GitHub Issue

Result: PASS

## 5. Architecture Alignment Category Definition

Architecture alignment purpose:

- validate execution against ADR-level architecture authority.

Architecture validation expectations:

- confirm no divergence from architecture-of-record decisions.

Review requirements:

- include explicit ADR evidence and findings.

Result: PASS

## 6. Contract Alignment Category Definition

Contract alignment purpose:

- validate execution against contract boundaries and responsibilities.

Contract validation expectations:

- confirm no contract-boundary violations.

Review requirements:

- include explicit contract evidence and findings.

Result: PASS

## 7. Model Alignment Category Definition

Model alignment purpose:

- validate execution against canonical model semantics.

Model validation expectations:

- confirm no semantic drift against canonical models.

Review requirements:

- include explicit model evidence and findings.

Result: PASS

## 8. Ownership Alignment Category Definition

Ownership alignment purpose:

- validate ownership boundaries across architecture, contracts, models, and implementation.

Ownership validation expectations:

- confirm no ownership reassignment or ownership drift.

Review requirements:

- include explicit ownership-boundary evidence and findings.

Result: PASS

## 9. Existing Implementation Alignment Category Definition

Implementation alignment purpose:

- validate execution against authoritative existing implementation behavior interpretation.

Implementation validation expectations:

- confirm implementation changes do not contradict authoritative behavior where upstream authority has not changed.

Review requirements:

- include explicit implementation evidence and findings.

Result: PASS

## 10. Review Completion Rules

Mandatory categories:

- Architecture Alignment
- Contract Alignment
- Model Alignment
- Ownership Alignment
- Existing Implementation Alignment

Completion requirements:

- all five categories must be reviewed and documented.

Review signoff requirements:

- signoff requires full category completion, conflict status, and traceability evidence.

Result: PASS

## 11. Review Failure Rules

Failure conditions:

- any mandatory category missing
- unresolved authority conflict
- missing traceability evidence

Incomplete review conditions:

- partial category coverage
- undocumented validation outcomes

Escalation conditions:

- authority conflicts or unresolved ownership/semantic boundary issues.

Result: PASS

## 12. Conflict Detection Workflow

Workflow:

1. detect conflict
2. compare against authority order
3. document conflict and impact
4. escalate with correction recommendation

Result: PASS

## 13. ADR Conflict Workflow

When issue conflicts with ADR:

- stop execution immediately
- document ADR conflict with citation
- document impact
- recommend correction aligned to ADR
- do not implement conflicting behavior

Result: PASS

## 14. Contract Conflict Workflow

When issue conflicts with Contract:

- stop execution immediately
- document Contract conflict with citation
- document boundary impact
- recommend correction aligned to Contract
- do not implement conflicting behavior

Result: PASS

## 15. Model Conflict Workflow

When issue conflicts with Model:

- stop execution immediately
- document Model conflict with citation
- document semantic impact
- recommend correction aligned to Model
- do not implement conflicting behavior

Result: PASS

## 16. Existing Implementation Conflict Workflow

When issue conflicts with Existing Implementation:

- stop execution immediately
- document implementation conflict with citation
- document behavioral impact
- recommend correction aligned to authoritative implementation and upstream authority
- do not implement conflicting behavior

Result: PASS

## 17. Review Execution Workflow

Review sequence:

1. Architecture Alignment
2. Contract Alignment
3. Model Alignment
4. Ownership Alignment
5. Existing Implementation Alignment

Validation sequence:

1. validate category evidence
2. validate conflict status
3. validate traceability completeness

Approval sequence:

1. confirm all categories complete
2. confirm no unresolved conflicts
3. confirm closure evidence documented

Result: PASS

## 18. Review Evidence Requirements

Required evidence:

- authoritative source citations for each category

Validation evidence:

- PASS/FAIL outcomes for each category and rule

Traceability evidence:

- explicit mapping from execution to ADR/Contract/Model/Implementation/Issue inputs.

Result: PASS

## 19. Review Documentation Standards

Review documentation expectations:

- structured category-by-category review outputs

Review output expectations:

- explicit findings, conflict status, and resolution or escalation status

Issue closure documentation expectations:

- closure includes completed review evidence and governance traceability proof.

Result: PASS

## 20. Mandatory Review Checklist Definition

Authoritative reusable review checklist:

```text
Issue Execution Review Checklist

Mandatory Categories:
1. Architecture Alignment
2. Contract Alignment
3. Model Alignment
4. Ownership Alignment
5. Existing Implementation Alignment

For each category:
- list authoritative references reviewed
- record alignment findings
- record PASS/FAIL

Conflict Review:
- document detected conflicts
- document authority-order comparison
- document escalation and correction recommendation

Completion Gate:
- fail review if any category is skipped
- fail review if unresolved conflicts remain
- fail review if traceability evidence is incomplete

Closure Gate:
- approve only when all five categories PASS and evidence is complete
- for a Home Assistant integration or App change, also require the
  Home Assistant Gold Quality Gate acceptance evidence
  (home-assistant-distribution-and-quality-standard.md, section 6.1)
```

Result: PASS

## 21. Review Checklist Example

Example issue review using the checklist:

```text
Issue: <id/title>

Architecture Alignment: PASS
Evidence: <ADR references>

Contract Alignment: PASS
Evidence: <contract references>

Model Alignment: PASS
Evidence: <model references>

Ownership Alignment: PASS
Evidence: <ownership-boundary references>

Existing Implementation Alignment: PASS
Evidence: <implementation references>

Conflict Status: No conflicts identified.

Traceability: complete.

Review Result: PASS
```

Result: PASS

## 22. Copilot Review Expectations

Copilot review requirements:

- complete all five mandatory review categories before closure.

Grounding verification requirements:

- verify authoritative sources were reviewed in order.

Authority verification requirements:

- verify issue guidance did not supersede ADR/Contract/Model/Existing Implementation authority.

Result: PASS

## 23. Governance Traceability Review

Traceability requirements:

- ADR traceability
- Contract traceability
- Model traceability
- Existing Implementation traceability
- GitHub Issue traceability as execution input only

Result: PASS

## 24. Governance Traceability Matrix

| Authority Surface | Review Requirement | Traceability Expectation |
|---|---|---|
| ADR | Architecture Alignment evidence required | architecture-of-record conformance documented |
| Contract | Contract Alignment evidence required | boundary conformance documented |
| Model | Model Alignment evidence required | semantic conformance documented |
| Existing Implementation | Implementation Alignment evidence required | behavior interpretation conformance documented |
| GitHub Issue | Issue input evidence required | execution guidance treated as lowest authority |

Result: PASS

## 25. Ownership Preservation Review

Validation scope:

- architecture ownership
- contract ownership
- model ownership
- implementation ownership

Result: PASS

Ownership remains preserved through mandatory alignment categories and conflict-stop workflows.

## 26. Drift Prevention Review

Drift prevention requirements:

- architecture drift prevention through mandatory Architecture Alignment review
- governance drift prevention through category completion and conflict escalation
- ownership drift prevention through explicit Ownership Alignment review
- implementation drift prevention through Existing Implementation Alignment review

Result: PASS

## 27. Review Completion Validation

Validation scope:

- all five categories required
- no categories optional
- review fails if category omitted

Result: PASS

## 28. Roadmap Applicability Review

Execution reviews support roadmap governance and closure by enforcing authority validation, category completeness, conflict handling, and traceable closure evidence on every issue.

Result: PASS

## 29. Final Governance Assessment

Governance assessment:

- review quality is controlled through mandatory category coverage.
- authority validation is controlled through explicit authority-order enforcement.
- execution oversight is controlled through completion gates, failure rules, and conflict escalation workflow.

Result: PASS

## 30. Final Determination

E15-G3 ISSUE EXECUTION REVIEW CHECKLIST

APPROVED AS THE AUTHORITATIVE BASELINE

FOR EXECUTION REVIEW GOVERNANCE
