# Home Assistant distribution and quality standard

> **Document status: Operational.**
> The organization-wide engineering standard for publishing Home Assistant components from
> Homes-That-Behave-Well-LLC repositories. **Creates no architecture authority**: it governs how
> components are packaged, validated, documented, and released, not what they do.
> [authority-order.md](authority-order.md) prevails on any conflict. Other repositories reference this
> document rather than copying it. Established 2026-11-08; per-repository evidence for this
> repository: [home-assistant-quality.md](home-assistant-quality.md).
> Supersedes nothing; [hacs-and-platinum-governance-gate.md](hacs-and-platinum-governance-gate.md)
> remains the historical E12 readiness gate.

## 1. Authority for Home Assistant rules

Use **current official** sources, in this order, and record the URL and retrieval date of every rule you
apply:

1. Home Assistant developer documentation (<https://contributors.home-assistant.io/core/>)
2. Home Assistant Marketplace publishing documentation (<https://contributors.home-assistant.io/marketplace/>)
3. The current Integration Quality Scale (<https://contributors.home-assistant.io/core/quality-scale/rules/>)
4. Home Assistant Core source at the targeted release tag
5. Home Assistant App documentation (<https://contributors.home-assistant.io/apps/>)
6. HACS publisher documentation, only where the Marketplace still consumes that mechanism

Blogs, forum posts, and third-party tutorials are not authority. Remembered rule lists are not
authority: re-read the rules when you assess.

**Home Assistant first** (principle **P21**): before building a mechanism, find the official Home
Assistant pattern (config entries, subentries, options, reconfigure, Repairs, diagnostics, discovery,
selectors, translations, registries, exception hierarchy) and a Core integration that uses it.

## 2. Terminology

- From Home Assistant 2026.11 the store for custom integrations, dashboard plugins, themes, and templates
  is the **Home Assistant Marketplace**. Write "Home Assistant Marketplace".
- Do not tell 2026.11+ users to install the HACS custom integration; 2026.11 blocks it. Where older
  versions matter, write "Home Assistant Marketplace on 2026.11+, HACS on 2026.10 and earlier".
- The Marketplace still uses the HACS catalog (`hacs/default`) and `hacs.json`. Keep `hacs.json`; never
  rename it or invent a Marketplace manifest.
- Add-ons are **Apps**, installed under **Settings > Apps** from an **app repository**
  (`repository.yaml`). The Marketplace does not install Apps.

## 3. Which repositories distribute what

Classify every repository before changing it. Only a repository whose distribution is intended
publishes through a channel. A repository that is sunsetting is **not** made installable, revived, or
newly submitted; its history is preserved. Never delete a repository that is in the catalog: request
removal first (see the catalog guide), or archive it, which removes it from the catalog.

| Component | Channel | Repository metadata |
|---|---|---|
| Custom integration | Home Assistant Marketplace | `hacs.json`, `custom_components/<domain>/` |
| App | Supervisor app repository | `repository.yaml`, `<folder>/config.yaml` |
| Both in one repository | Both, independently | Both sets. The Marketplace refuses a repository with `repository.yaml` only when `custom_components/` has no folder. |

A Marketplace repository holds exactly one integration. An integration and an App in one repository
stay separate runtimes with separate versions; never couple them for packaging convenience.

## 4. Required repository contents

| Item | Integration repo | App repo |
|---|---|---|
| Public repository, description, topics, issues enabled | Required | Required |
| `README.md` stating what each channel installs; GitHub-only parts in `ha-marketplace:exclude` markers | Required | Required |
| `hacs.json` with `name`; `homeassistant` only when a newer Core is genuinely required | Required | — |
| `manifest.json`: `domain`, `name`, `version`, `documentation`, `issue_tracker`, `codeowners`, `config_flow`, `integration_type`, `iot_class`; `requirements` only for packages Core does not already provide | Required | — |
| `translations/en.json` shipped (equal to `strings.json` if both exist) | Required | — |
| `custom_components/<domain>/brand/icon.png` (256²), `icon@2x.png` (512²), `dark_` variants as needed; derived only from Owner-approved branding | Required | — |
| Nothing development-only inside `custom_components/<domain>/` (no tests, scripts, audit notes) | Required | — |
| `repository.yaml` with `name` | — | Required |
| `config.yaml`, `Dockerfile`, `README.md`, `DOCS.md`, `CHANGELOG.md`, `translations/en.yaml` per App | — | Required |
| `SECURITY.md`, `CONTRIBUTING.md`, `.github/CODEOWNERS`, issue forms, Dependabot | Required | Required |
| `LICENSE` | Owner decision — never chosen on the Owner's behalf | Owner decision |
| User documentation for a household administrator (section 7) | Required | Required |
| Quality tracking document (section 6) | Required | — |

## 5. Required CI

Every applicable repository protects itself in GitHub Actions. CI does not replace the local governed
process (section 8).

| Check | Applies to | How |
|---|---|---|
| HACS action, `category: integration`, no `ignore` | Integrations | `hacs/action`, pinned to a release tag |
| hassfest | Integrations | `home-assistant/actions/hassfest` |
| Ruff (`check`, `format --check`), mypy | Python code | Repository's pinned toolchain |
| Official Home Assistant pytest harness | Integrations | `pytest-homeassistant` pinned to the same Core release as `homeassistant` |
| Distribution conformance tests | All | Encode the repository-structure rules (for example `tests/test_distribution.py`) |
| App lint | Apps | `frenck/action-addon-linter`, as used by `home-assistant/apps-example` |
| App build for every declared architecture | Apps | Build only; publishing images is a release (section 9) |

Workflow defaults: `permissions: {}` or `contents: read`; `persist-credentials: false` on checkout;
actions pinned to release tags (official Marketplace and App guidance) and kept current by Dependabot.
Pin by commit SHA wherever a repository handles secrets or publishes artifacts.

## 6. Integration Quality Scale target

- **Target: Gold**, as the consequence of correct Home Assistant architecture, reliable lifecycle,
  actionable failures, good documentation, and thorough tests — not as a badge.
- Assess **every** current rule individually as PASS, EXEMPT (with the reason), FAIL, BLOCKED BY
  ARCHITECTURE, BLOCKED BY FUTURE FEATURE, or NEEDS OWNER DECISION, with evidence.
- Implement every applicable Gold rule that does not contradict accepted architecture. Record a rule
  that needs deferred product scope against its governing issue; do not build that scope only to pass
  the rule.
- Report **GOLD** only when every applicable Bronze, Silver, and Gold rule is PASS; otherwise **PARTIAL
  GOLD** (or the highest complete tier).
- Home Assistant awards no tiers to custom integrations. Say "HTBW self-assessed Gold-conformant",
  never "official Home Assistant Gold". Do not add `quality_scale` to a custom integration's manifest.
- When a change adds entities, devices, actions, or platforms, re-assess every rule previously EXEMPT
  because they were absent.

**Platinum is not an objective.** Classify each Platinum rule as already satisfied, low-cost/high-value,
valuable later, not appropriate, or requiring architecture expansion. Adopt only low-cost practices that
improve security, async behavior, typing, diagnostics, resilience, or maintainability.

## 7. Documentation

Write for the household administrator. Cover what the component does; prerequisites; installation
through each channel; every setup field and option; supported functionality and devices; how and how
often data updates; use cases; known limitations; troubleshooting for every Repair; privacy and
security behavior the household needs to know; and removal, including data that remains (for example
in backups). Do not pad documentation to satisfy a rule.

Repairs are for conditions the household or administrator can fix. Do not raise a Repair for a
transient state or an internal fault nobody can act on.

## 8. Validation before every commit

Both gates pass before a commit:

- **Windows** (authoritative source and Git): Ruff, mypy, structural checks.
- **WSL2 Linux** (test host only): the official Home Assistant pytest harness, with its environment
  and artifacts outside the repository.

Then commit, push, and confirm the GitHub checks. Deployment to HA-DEV and household acceptance remain
separate, Owner-governed steps.

## 9. Releases

- Integration: the GitHub release tag equals `manifest.json` `version` (semantic versioning). Publish a
  full GitHub release with notes that put required user action first. Keep old releases. Set
  `homeassistant` in `hacs.json` when a release needs a newer Core.
- App: `config.yaml` `version` is the single source of truth. Push the image for a version before
  changing `version`; never re-push an existing tag; use `breaking_versions` for changes that need user
  attention; update `CHANGELOG.md`.
- Integration and App versions are independent.
- **Owner approval is required** to publish a release, publish container images, submit to the catalog,
  make a repository public, or change a license.

## 10. Supply chain

Pin Python dependencies as Home Assistant conventions require (the test harness fully pinned; App runtime
fully pinned with binary wheels). Pin container base images to a release tag. Download external model
artifacts by pinned revision and verify their digest before use. Update dependencies deliberately,
never blindly.
