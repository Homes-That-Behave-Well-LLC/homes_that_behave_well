# Security policy

> **Document status: Operational.**
> Process document. Creates no architecture authority; see
> [docs/governance/authority-order.md](docs/governance/authority-order.md).

## Supported components

| Component | Distribution | Supported version |
|---|---|---|
| HTBW Integration (`custom_components/htbw`) | Home Assistant Marketplace | The latest version on the default branch, or the latest GitHub release once releases are published |
| BehavesWell Voice Evidence App, formerly HTBW Voice Evidence (`apps/htbw_voice_evidence`) | Home Assistant app repository | The version in `apps/htbw_voice_evidence/config.yaml` on the default branch |

Both components are pre-1.0 and the App is marked `experimental`.

## Reporting a vulnerability

Do not report vulnerabilities in public issues.

Private vulnerability reporting is not yet enabled on this repository. Until it is, open a public
issue that asks the maintainers for a private reporting route **without any vulnerability details**,
and wait for that route before you send them.

A useful report names the affected component and version, the boundary involved (for example, the
App's Supervisor-internal API, Supervisor Discovery provisioning, diagnostics, or Repairs), the
impact, and a sanitized way to reproduce it.

## Sensitive data

Never include any of the following in an issue, discussion, pull request, log, or diagnostics file
that you share publicly:

- voice recordings, Voiceprints, embeddings, or match scores;
- the App's API secret or any Home Assistant token;
- household names, person identifiers, or device identifiers you have not redacted.

HTBW diagnostics redact Room, configuration-entry, native-reference, and person identifiers, and
never contain the App secret or biometric material. Review a diagnostics file before you share it
anyway.

## Security boundaries

- The Voice Evidence App exposes **no host ports**. Its API is reachable only on the Supervisor
  internal network and requires a bearer secret that the App generates and provisions to the
  Integration through Supervisor Discovery.
- The Integration stores no biometric artifact and never logs the App secret.
- Neither component uses a cloud service. The App downloads one pinned, SHA-256-verified model
  artifact; see `apps/htbw_voice_evidence/DOCS.md`.

Architecture authority for these boundaries:
[docs/architecture/privacy.md](docs/architecture/privacy.md) and
[docs/contracts/identity-contract.md](docs/contracts/identity-contract.md).
