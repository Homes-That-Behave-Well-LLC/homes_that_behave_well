# Contributing

> **Document status: Operational.**
> Process document. Creates no architecture authority; see
> [docs/governance/authority-order.md](docs/governance/authority-order.md).

This repository holds the HTBW architecture **and** two separately versioned runtimes: the HTBW
Integration (`custom_components/htbw`) and the HTBW Voice Evidence App
(`apps/htbw_voice_evidence`). A pull request, example, or implementation does not change accepted
architecture; [docs/governance/authority-order.md](docs/governance/authority-order.md) decides.

## Before you change anything

1. Read [docs/governance/home-assistant-distribution-and-quality-standard.md](docs/governance/home-assistant-distribution-and-quality-standard.md)
   for distribution, quality, and CI expectations.
2. Keep the Integration and the App separate: they talk only through the governed contracts in
   [docs/contracts/identity-contract.md](docs/contracts/identity-contract.md), and neither version is
   derived from the other.
3. Use synthetic data only. Never submit recordings, Voiceprints, secrets, or household identifiers.
4. Update [docs/governance/document-register.md](docs/governance/document-register.md) when you add,
   move, or reclassify a Markdown document, and give every Markdown file a status banner.

## Validation

Both local gates must pass before a commit, exactly as described in the README section
"Local integration development":

- **Windows:** Ruff (`check` and `format --check`) and strict mypy for `custom_components/htbw`.
- **WSL2:** the official Home Assistant pytest harness for `tests/`, with every artifact outside
  the repository.
- **App:** the App's own pytest and Ruff checks, from `apps/htbw_voice_evidence` (see its README).

GitHub Actions repeat these checks and add the Marketplace (HACS action), hassfest, and App lint and
build checks. CI does not replace the local gates.

## Licensing

This repository has no license file yet. Do not assume that a contribution grants or implies
license terms; ask the repository Owner first.
