# HTBW in Home Assistant: install, set up, use, and remove

> **Document status: Operational — household administrator documentation.**
> Describes the shipped HTBW Integration and HTBW Voice Evidence App. Creates no architecture
> authority; where it differs from canon, [../governance/authority-order.md](../governance/authority-order.md)
> decides. Distribution and quality tracking:
> [../governance/home-assistant-quality.md](../governance/home-assistant-quality.md).

This guide is for the person who administers Home Assistant for a household.

## What HTBW is

Homes That Behave Well (HTBW) is a framework for a home that is calm, predictable, and able to explain
itself. In Home Assistant it ships as two separate components:

| Component | What it does | How you install it |
|---|---|---|
| **HTBW Integration** (`htbw`, shown as **HTBW Core**) | Holds your household's HTBW configuration and its **Rooms**. Each Room records which Home Assistant entities and devices act as its voice input, spoken response output, interface, and physical remote. | **Home Assistant Marketplace** |
| **HTBW Voice Evidence App** | Optional. A local voice-evidence runtime that will create and compare Voiceprints. Version 0.1.0 is a foundation: it installs, secures itself, connects to the Integration, and verifies its speaker model. Enrollment and voice comparison are not available yet. | **Settings > Apps**, as an app repository |

The Integration works without the App. The two are versioned and updated independently. Installing
one never installs the other.

## Prerequisites

- **Home Assistant 2026.11.0 or newer.** HTBW uses configuration-form features introduced in
  2026.11 and does not load on earlier versions.
- For the App only: a Home Assistant installation with the Supervisor (Home Assistant OS or
  Supervised), on an **amd64** or **aarch64** system, and internet access once to download the pinned
  speaker model (about 25 MB).
- At least one Home Assistant **Area** for each Room you want to configure.

## Install the Integration

HTBW is not in the Marketplace catalog yet, so add the repository from its link:

<!-- ha-marketplace:exclude-start -->
[![Open your Home Assistant instance and open this repository in the Marketplace.](https://my.home-assistant.io/badges/marketplace_repository.svg)](https://my.home-assistant.io/redirect/marketplace_repository/?owner=Homes-That-Behave-Well-LLC&repository=homes_that_behave_well&category=integration)
<!-- ha-marketplace:exclude-end -->

1. Open the link above. Home Assistant offers to add the repository to the Marketplace as a custom
   repository of category **Integration**. Accept.
2. Select **Download** to install **HTBW Core**.
3. Continue with [Set up HTBW](#set-up-htbw). No restart is needed for the first install.

Do not install HTBW through the HACS custom integration on Home Assistant 2026.10 or earlier: this
version needs 2026.11.0.

## Install the Voice Evidence App (optional)

<!-- ha-marketplace:exclude-start -->
[![Open your Home Assistant instance and show the add app repository dialog with this repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FHomes-That-Behave-Well-LLC%2Fhomes_that_behave_well)
<!-- ha-marketplace:exclude-end -->

1. Go to **Settings** > **Apps** > **Install app**, open the top-right menu, select
   **Repositories**, and add `https://github.com/Homes-That-Behave-Well-LLC/homes_that_behave_well`.
2. Install **HTBW Voice Evidence** and start it.
3. Home Assistant discovers the App for HTBW. Confirm it under **Settings** > **Devices & services**.

The App is built on your device the first time, which can take several minutes. It is marked
**experimental**. See the App's own **Documentation** tab for its security and privacy details.

## Set up HTBW

### The household entry

Add the **HTBW Core** integration under **Settings** > **Devices & services** > **Add integration**,
or confirm the discovered App. Either way creates the single household HTBW entry. A second household
entry cannot be created.

| Setup field | Meaning |
|---|---|
| **Retain Enrollment Recordings** | Required. **Retain** keeps the ten recordings captured when someone enrolls their voice, so a future speaker-model update may rebuild their Voiceprint automatically (never guaranteed). **Delete** removes them once the Voiceprint is created; a future incompatible model then needs that person to enroll again. This setting never deletes a working Voiceprint. |

You can change **Retain Enrollment Recordings** later with **Configure** on the household entry. HTBW
copies the value into the App; changes made on the App's own Configuration tab are overwritten.

### Rooms

Select **Add Room** on the HTBW entry.

| Field | Meaning |
|---|---|
| **Room (Area)** | Required. The Home Assistant Area this HTBW Room represents. Each Area can be added once. |
| **Voice input** | Optional. Entities that hear spoken requests in this Room, such as an Assist satellite. |
| **Spoken response output** | Optional. Media players that speak responses in this Room. |

To change a Room, select **Reconfigure** on it. The form has four sections — **Voice input**,
**Spoken response output**, **Interface**, and **Physical remote** — each with **Entities** and/or
**Devices** selectors. Multiple selections are independent assignments, never a priority or fallback
order. Clearing a field removes those assignments.

## What HTBW provides

- **Room interaction configuration**: the four interaction functions per Room, stored as native Home
  Assistant configuration subentries and read by HTBW's Foundation responsibility.
- **Repairs** for problems you can fix (see [Troubleshooting](#troubleshooting)).
- **Diagnostics** you can download from the HTBW entry. Room, entry, reference, and person
  identifiers are redacted; secrets and biometric material are never included.
- **Voice Evidence App status**, when the App is installed: whether it is available, unreachable,
  rejecting HTBW's credential, incompatible, or not ready, and whether your retention setting has
  reached it.

HTBW creates **no entities, devices, actions, triggers, or conditions**, so there is nothing to put on a
dashboard or into an automation yet.

## How data is updated

- **Room assignments** change only when you add or reconfigure a Room. HTBW listens for entity and
  device registry changes and for entities appearing or disappearing, and re-checks the affected
  assignments immediately.
- **Voice Evidence App status** is checked when HTBW starts and then every **5 minutes**. Each check is
  limited to **10 seconds**, and Home Assistant never waits for the App during startup.
- **App connection details** arrive through Supervisor Discovery. When the App's address or secret
  changes, HTBW updates its stored connection automatically.

## Use cases

- **Declare how each room is spoken to and answered.** A household with an Assist satellite in the
  kitchen and a speaker in the den records exactly which device listens and which answers in each
  Room, instead of HTBW guessing from names or areas.
- **Notice when a configured device is gone.** If you replace the den speaker and the old entity is
  deleted, HTBW raises a Repair naming the Room and function, and does not quietly substitute another
  device.
- **Prepare for voice identity locally.** Installing the App sets up a local, authenticated
  voice-evidence runtime with your retention choice applied, ready for later enrollment features,
  with no cloud service involved.

## Supported devices

HTBW does not talk to devices directly. Any entity or device already in Home Assistant can be assigned:

- **Voice input**: any entity, or any device.
- **Spoken response output**: `media_player` entities, or any device.
- **Interface**: any device.
- **Physical remote**: `remote`, `event`, or `button` entities, or any device.

The App supports **amd64** and **aarch64** systems only.

## Known limitations

- HTBW creates no entities, actions, or automations yet; it is a configuration and governance
  foundation that later HTBW capabilities build on.
- The App cannot enroll anyone or identify voices yet (version 0.1.0).
- The App is built on your device; prebuilt images are not published yet.
- A stored assignment with a reference type the form cannot edit blocks that Room's reconfigure
  form with an explanation instead of silently dropping it.
- The Integration is not in the Marketplace catalog yet; add it from its link.
- There are no GitHub releases yet, so the Marketplace shows a commit instead of a version number,
  and it cannot hold the Integration back from an older Home Assistant.

## Troubleshooting

Problems you can fix appear under **Settings** > **System** > **Repairs**:

| Repair | What to do |
|---|---|
| **A configured HTBW reference no longer exists** | Reconfigure the named Room and choose a new entity or device, or clear the assignment. An entity that is merely unavailable does not raise this. |
| **An HTBW room could not be moved into the household configuration** | After an upgrade from 0.1.x, two copies of a Room differ. Compare the earlier Room entry with the Room under the household entry, keep the correct one, and delete the other. Nothing was deleted automatically. |
| **Voice evidence is unavailable: the App cannot be reached** | Raised only after three failed checks in a row. Check that the App is installed and running under **Settings** > **Apps**. |
| **… the App rejected HTBW's credential** | Restart the App; it provisions HTBW again through discovery. |
| **… the App version is incompatible** | Update the Integration and the App to versions that match. |
| **… the App is not ready** | Open the App's **Log** tab. The reason (for example `model_downloading` or `model_digest_mismatch`) is explained on the App's **Documentation** tab. |
| **The Retain Enrollment Recordings setting has not reached the App** | Check that the App is installed and running. HTBW keeps retrying. |

If HTBW fails to start with **"HTBW could not start because its stored Room configuration is
invalid"**, nothing has been changed or deleted. Restore a backup taken before the problem, or open a
bug report.

When you report a bug, attach the HTBW diagnostics file after reviewing it. Never attach recordings,
secrets, or unredacted household identifiers.

## Privacy and security

- Everything runs locally. The Integration uses no cloud service. The App downloads only its pinned,
  SHA-256-verified model file and uploads nothing.
- The App's API is reachable only on Home Assistant's internal network and requires a secret that the
  App generates and hands to HTBW through discovery.
- The Integration stores no Voiceprints, embeddings, or recordings. The App stores them only in its
  private data folder, which **Home Assistant backups include**. Treat backups accordingly.

## Remove HTBW

**Integration**

1. Under **Settings** > **Devices & services**, open **HTBW Core** and delete the household entry. This
   removes its Rooms. Your entities, devices, and Areas are untouched.
2. In the Marketplace, open **HTBW Core** and select **Remove**. Restart Home Assistant when the
   Marketplace asks.

**App**

1. Under **Settings** > **Apps**, open **HTBW Voice Evidence** and select **Uninstall**.
2. Optionally remove the repository under **Settings** > **Apps** > **Install app** > menu >
   **Repositories**.
3. Home Assistant backups made while the App was installed still contain its private data, including
   Voiceprints and any kept recordings. Delete those backups if you need that data gone.
