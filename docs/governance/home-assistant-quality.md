# Home Assistant distribution and quality conformance — HTBW repository

> **Document status: Operational.**
> Evidence record for this repository's Home Assistant Marketplace, app-store, and Integration
> Quality Scale conformance. **Creates no architecture authority** and decides nothing; the rules it
> applies are set by [home-assistant-distribution-and-quality-standard.md](home-assistant-distribution-and-quality-standard.md).
> Assessed 2026-11-08 against Home Assistant Core **2026.11.0**, Integration `htbw` **0.2.0**, App
> `htbw_voice_evidence` **0.1.0**. **Addendum 2026-11-10 (Issue #211, DL-151):** the External
> Storage Foundation rows below are added evidence for that implementation; they do not re-run or
> change the 2026-11-08 baseline for any other row.

## 1. Result

| Component | Channel | Result |
|---|---|---|
| HTBW Integration (`custom_components/htbw`) | Home Assistant Marketplace (link install) | **PASS** — conforms to the repository structure, `hacs.json`, manifest, brand, and validation requirements. Not in the catalog (Owner decision; needs a release). |
| HTBW Voice Evidence App (`apps/htbw_voice_evidence`) | Supervisor app repository | **PASS** for local-build distribution. Prebuilt images are not published (Owner decision). |
| Dual distribution | Both | **PASS** — each channel resolves only its own component (see section 3). |
| Integration Quality Scale | — | **GOLD — HTBW self-assessed.** Every Bronze, Silver, and Gold rule is PASS or exempt with a recorded reason. Home Assistant awards no tier to custom integrations; this is not an official Home Assistant Gold rating. |

## 2. Sources

Retrieved 2026-11-08. Official sources only; HTBW's authority order still governs architecture.

| Source | URL |
|---|---|
| Quality Scale, all rules (54: 20 Bronze, 10 Silver, 21 Gold, 3 Platinum) | <https://contributors.home-assistant.io/core/quality-scale/rules/> |
| Marketplace: publish a custom integration | <https://contributors.home-assistant.io/marketplace/guides/integrations/> |
| Marketplace: repository structure | <https://contributors.home-assistant.io/marketplace/reference/repository-structure/> |
| Marketplace: `hacs.json` | <https://contributors.home-assistant.io/marketplace/reference/hacs-json/> |
| Marketplace: validation checks | <https://contributors.home-assistant.io/marketplace/reference/validation/> |
| Marketplace: releases and updates | <https://contributors.home-assistant.io/marketplace/guides/releases/> |
| Marketplace: get into the catalog | <https://contributors.home-assistant.io/marketplace/guides/catalog/> |
| Integration brands and images | <https://contributors.home-assistant.io/core/integrations/brands/> |
| Integration categories | <https://contributors.home-assistant.io/core/integrations/categories/> |
| Apps: create and share a repository | <https://contributors.home-assistant.io/apps/guides/repository/> |
| Apps: app files | <https://contributors.home-assistant.io/apps/reference/files/> |
| Apps: publish your app | <https://contributors.home-assistant.io/apps/guides/publishing/> |
| Apps: test your app | <https://contributors.home-assistant.io/apps/guides/testing/> |
| Marketplace source, core tag `2026.11.0` | `homeassistant/components/marketplace/repositories/integration.py`, `utils/validate.py` |
| Official example app repository | <https://github.com/home-assistant/apps-example> |

## 3. Dual-distribution verification

The repository is both a Marketplace integration repository and a Supervisor app repository. Each
channel's own rules were checked against the source that applies them:

| Question | Evidence | Result |
|---|---|---|
| Does the Marketplace resolve the integration? | Core 2026.11.0 `IntegrationRepository.resolve_content` takes the first folder under `custom_components/`; `custom_components/htbw` is the only one. | PASS |
| Does `repository.yaml` make the Marketplace refuse the repository? | `AppRepositoryError` is raised **only** when `custom_components/` has no folder **and** a `repository.yaml` exists. Here the folder exists. | PASS — no interference |
| Does the Supervisor find exactly one app? | The Supervisor reads `config.yaml` at any depth except hidden and `rootfs` folders; the only one is `apps/htbw_voice_evidence/config.yaml`. | PASS |
| Does Marketplace metadata affect the app store? | The Supervisor ignores `hacs.json` and `custom_components/`. | PASS |
| Is the download clean? | The Marketplace installs only `custom_components/htbw/`, which holds only `.py`, `.json`, and brand `.png` files. | PASS |
| Are versions unambiguous? | Integration version: `manifest.json` (future release tags). App version: `config.yaml` + `CHANGELOG.md`. Neither derives from the other. | PASS |
| Do the docs say which channel installs what? | README "Use HTBW in Home Assistant" and [../user-guide/htbw-in-home-assistant.md](../user-guide/htbw-in-home-assistant.md). | PASS |

Regression protection: `tests/test_distribution.py` encodes every structural row above;
`.github/workflows/validate.yaml`
runs the HACS action and hassfest; `.github/workflows/app.yaml` lints the App and builds it for both
architectures without pushing.

Not automatable here: an end-to-end install into a live Home Assistant. That remains the Owner
retest on HA-DEV (add both repository links, install, start setup).

## 4. Marketplace conformance (Integration)

| Requirement | Evidence | Result |
|---|---|---|
| Public GitHub repository, description, topics, issues on | GitHub repository settings | PASS |
| `hacs.json` in the root, valid keys and types | `hacs.json`: `name`, `homeassistant: 2026.11.0` | PASS |
| `homeassistant` minimum is genuine | Config flow uses the 2026.11 Probatio form API; harness pinned to 2026.11.0. Only enforced once releases exist. | PASS |
| `custom_components/<domain>/`, domain characters | `custom_components/htbw`, `domain: htbw` | PASS |
| Manifest: `version`, `documentation`, `issue_tracker`, `codeowners`, `name` | `manifest.json` | PASS |
| `config_flow`, `integration_type: hub`, `iot_class` | `manifest.json`. `iot_class` is `local_push`; configuration and Repairs are event-driven, but the optional App status and the optional External Storage health (#211) are each polled every 5 minutes, so `local_polling` is also defensible. Display-only; left unchanged. | PASS (note) |
| `categories` | Absent. Optional for custom integrations; the HACS action only warns. | **Owner decision** (public positioning) |
| Translations shipped in `translations/en.json` | Identical to `strings.json` (test-enforced) | PASS |
| Brand images in `custom_components/htbw/brand/` | `icon.png` 256², `icon@2x.png` 512², `dark_icon.png`, `dark_icon@2x.png`: trimmed, resized crops of the approved `brand/icon_light.png` and `brand/icon_dark.png`. No new artwork. | PASS (Owner may review the crop) |
| HACS action and hassfest in CI | `.github/workflows/validate.yaml` | PASS (see CI run) |
| GitHub releases | None yet. Users get the default-branch commit. | **Owner decision** — required for the catalog and for `homeassistant` enforcement |
| Catalog listing | Not listed | **Owner decision** |
| README Marketplace exclusion markers | GitHub-only badges wrapped in `ha-marketplace:exclude` markers | PASS |

## 5. App conformance (Voice Evidence App)

| Requirement | Evidence | Result |
|---|---|---|
| `repository.yaml` with `name` | `name`, `url`, `maintainer` | PASS |
| `config.yaml` required keys; slug matches folder | `name`, `version`, `slug`, `description`, `arch`; test-enforced | PASS |
| Architectures | `amd64`, `aarch64`; CI builds both (QEMU for aarch64) | PASS |
| Dockerfile on official base image, pinned | `ghcr.io/home-assistant/base-debian:trixie-2026.11.0`; pip `--only-binary`, fully pinned `requirements.txt` | PASS |
| Translations, `DOCS.md`, `README.md`, `CHANGELOG.md` | Present; CHANGELOG top heading equals `version` (test-enforced) | PASS |
| `icon.png` / `logo.png` | Absent (optional) | Gap — optional; reuse approved branding when the Owner chooses |
| Security: no host ports, no privileged access, no config-folder map, bearer secret, discovery provisioning | `config.yaml`, `DOCS.md` | PASS |
| Lifecycle: default `startup` (application) and `boot` (auto), `init: false`, `watchdog` | `config.yaml`; redundant default keys removed per lint | PASS |
| Backups | Private `/data` is included in HA backups; documented in `DOCS.md` and the user guide | PASS |
| Model artifact external, pinned, verified | Revision-pinned download, SHA-256 before activation and on load (`MODEL_LICENSE.md`, `DOCS.md`) | PASS |
| Prebuilt images (`image:`) | Built on device. Official guidance prefers published multi-arch images. | **Owner decision** — production image publication |
| `stage: experimental` | Accurate for 0.1.0 | PASS |
| App lint | `frenck/action-addon-linter` (as used by `home-assistant/apps-example`), run from its pinned release in `.github/workflows/app.yaml`. Its one `watchdog` "obsolete" finding is overridden: the official configuration reference and the Supervisor schema accept `watchdog` without deprecation. Every other finding fails CI. | PASS (see CI run) |

## 6. Integration Quality Scale — rule by rule

Statuses: **PASS**, **EXEMPT** (rule does not apply; reason given), **FAIL**, **BLOCKED**.
`htbw` creates **no entities, devices, platforms, or actions** (`PLATFORMS = []`), which makes the
entity, device, and action rules not applicable.

### Bronze

| Rule | Status | Evidence |
|---|---|---|
| action-setup | EXEMPT | No actions registered. |
| appropriate-polling | PASS | Only the optional App status is pulled: every 300 s, 10 s timeout (`const.py`). No polled entities. |
| brands | PASS | `custom_components/htbw/brand/` |
| common-modules | EXEMPT | No coordinator and no entity base class. |
| config-flow | PASS | UI-only setup; `data_description` on every field; retention in `options`, App connection in `data`. |
| config-flow-test-coverage | PASS | `config_flow.py` 100 %; error-then-recovery (`test_add_room_area_not_found_shows_error`), duplicate abort, invalid discovery, options, discovery reconcile. |
| dependency-transparency | PASS | `requirements: []`; uses Home Assistant's aiohttp session only. |
| docs-actions | EXEMPT | No actions; the user guide states so. |
| docs-conditions | EXEMPT | No conditions; stated. |
| docs-high-level-description | PASS | User guide, "What HTBW is". |
| docs-installation-instructions | PASS | User guide, "Prerequisites", "Install the Integration". |
| docs-removal-instructions | PASS | User guide, "Remove HTBW". |
| docs-triggers | EXEMPT | No triggers; stated. |
| entity-event-setup | EXEMPT | No entities. |
| entity-unique-id | EXEMPT | No entities. |
| has-entity-name | EXEMPT | No entities. |
| runtime-data | PASS | `entry.runtime_data = HTBWRuntimeData(...)` |
| test-before-configure | EXEMPT | Setup connects to nothing: the household entry needs no connection, and the App is an optional DL-41 dependency whose discovery payload is validated (`_discovery_connection`) before use. |
| test-before-setup | PASS | Invalid stored Room data raises a translated `ConfigEntryError`. App absence or failure is deliberately not a setup failure (DL-41). |
| unique-config-entry | PASS | `HOUSEHOLD_UNIQUE_ID`; one Room per Area. |

### Silver

| Rule | Status | Evidence |
|---|---|---|
| action-exceptions | EXEMPT | No actions. |
| config-entry-unloading | PASS | `async_unload_entry`; every listener via `entry.async_on_unload`; `test_setup_and_unload_entry`, reload tests. |
| docs-configuration-parameters | PASS | User guide documents the one option. |
| docs-installation-parameters | PASS | User guide tables for setup and Room fields. |
| entity-unavailable | EXEMPT | No entities. |
| integration-owner | PASS | `codeowners: ["@tom-tagmdl"]`, `.github/CODEOWNERS`. |
| log-when-unavailable | PASS | One info log per App outcome transition (`VoiceEvidenceManager._set`), not per poll. |
| parallel-updates | EXEMPT | No entity platforms. |
| reauthentication-flow | EXEMPT | No user-entered credential. The App secret is generated by the App and re-provisioned by Supervisor Discovery; a Repair tells the user to restart the App. |
| test-coverage | PASS | 100 % of every module (official pytest harness, 2026-11-08; External Storage Foundation module added 2026-11-10, `tests/components/htbw/test_external_storage.py`, including idempotence and sibling-ownership-safety coverage per DL-151 SS2.6). |

### Gold

| Rule | Status | Evidence |
|---|---|---|
| devices | EXEMPT | No devices. HTBW Rooms are configuration, not HA Devices (README "Object distinctions are preserved"). |
| diagnostics | PASS | `diagnostics.py` with `async_redact_data`; secret never read; person IDs redacted (tests). External Storage (#211) reports configured/outcome/root-initialized only — never the configured path (`test_external_storage.py`). |
| discovery | PASS | Supervisor (hassio) discovery of the App: `async_step_hassio`. |
| discovery-update-info | PASS | `_abort_if_unique_id_configured(updates=...)`; `test_repeated_discovery_reconciles_the_one_household_entry`. |
| docs-data-update | PASS | User guide, "How data is updated". |
| docs-examples | EXEMPT | No entities, actions, or triggers to automate; stated in the user guide. |
| docs-known-limitations | PASS | User guide, "Known limitations". |
| docs-supported-devices | PASS | User guide, "Supported devices". |
| docs-supported-functions | PASS | User guide, "What HTBW provides". |
| docs-troubleshooting | PASS | User guide, "Troubleshooting" (every Repair). |
| docs-use-cases | PASS | User guide, "Use cases". |
| dynamic-devices | EXEMPT | No devices. |
| entity-category | EXEMPT | No entities. |
| entity-device-class | EXEMPT | No entities. |
| entity-disabled-by-default | EXEMPT | No entities. |
| entity-translations | EXEMPT | No entities. |
| exception-translations | PASS | `ConfigEntryError(translation_domain=..., translation_key="invalid_room_data")`; flow errors and aborts are translated. |
| icon-translations | EXEMPT | No entities or actions. |
| reconfiguration-flow | PASS | Room subentry `async_step_reconfigure`. The household entry has no user-entered setup data to reconfigure. |
| repair-issues | PASS | Missing reference, migration conflict, App outcomes, retention sync, External Storage outcomes (#211: `path_not_allowed`, `media_path_not_supported`, `unavailable`, `read_only`, `write_failed`, `invalid_root`, each raised only after it persists) — all actionable, none for transient states. |
| stale-devices | EXEMPT | No devices. Stale *references* are surfaced as Repairs instead. |

When HTBW later adds entities, devices, or actions, every rule marked EXEMPT because of their absence
must be re-assessed in that change.

### Platinum (not an HTBW objective)

| Rule | Status | Classification |
|---|---|---|
| async-dependency | PASS | A — already satisfied: no library; uses Home Assistant's aiohttp. |
| inject-websession | PASS | A — already satisfied: `async_get_clientsession(hass)`. |
| strict-typing | PASS | B — adopted (one annotation fix); `pyproject.toml` sets mypy `strict = true`. |

## 7. Repository hygiene

| Item | State |
|---|---|
| LICENSE | **Absent — Owner decision.** No license was chosen on the Owner's behalf. |
| SECURITY.md, CONTRIBUTING.md, CODEOWNERS, issue forms | Present |
| Dependabot | GitHub Actions, weekly |
| Actions permissions | Workflows default to `permissions: {}` or `contents: read`; checkouts do not persist credentials |
| Branch protection | None on `main` (recommend requiring the Validate and CI checks) |
| Private vulnerability reporting, secret scanning | Disabled (recommend enabling both) |
| Releases | None (see section 4) |

## 8. Owner decisions recorded

1. Publish the first GitHub release of the Integration (prerequisite for catalog and version display).
2. Submit to the Marketplace catalog.
3. Publish prebuilt multi-architecture App images to GHCR and add `image:` to `config.yaml`.
4. Choose a license.
5. Choose manifest `categories`.
6. Enable branch protection, private vulnerability reporting, and secret scanning.
