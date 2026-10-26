# ADR: Stable Endpoint Identity and Network-Boundary Independence

> **Document status: Active — subordinate to the HTBW canonical architecture.**
> Canonical authority: [framework.md](framework.md) and [../models/glossary.md](../models/glossary.md).
> Where this document conflicts with canonical authority, canonical authority prevails.
> Drafts decisions **DL-87**, **DL-88**, and **DL-89**, recorded pending formal acceptance review at
> **Issue #195**.
> **Not yet authoritative. Creates no new responsibility.**
> Terminology: [../models/glossary.md](../models/glossary.md).

---

## Status

**Recorded, pending formal acceptance review (Issue #195). Not yet authoritative.**

Drafted by the 2026-10 Reference Home Network Segmentation and Stable Endpoint Identity Architecture
Review, following completion of Reference Home's VLAN, firewall, mDNS, addressing, and cold-start
commissioning work. Consistent with this repository's established practice that a drafted decision is
recorded first and separately undergoes formal acceptance review before being treated as binding (see
*Notes on the 2026-10 AI, Natural Interaction, and Household Knowledge Architecture Review (DL-80–DL-83)*
and *Notes on the 2026-10 Home Identity and Home Intelligence Architecture Review (DL-84–DL-86)* in
[../governance/decision-ledger.md](../governance/decision-ledger.md)).

**This ADR is not authorization to implement VLAN management, firewall management, DHCP, DNS
infrastructure, mDNS proxying, wireless configuration, switch configuration, or UniFi administration
inside HTBW**, and it authorizes no runtime endpoint-resolution implementation. It is architecture and
governance only.

This ADR creates **no new responsibility**. The seven responsibilities recorded in **DL-01** —
Foundation, Stewardship, Identity, Truth, Continuity, Operational Trust, Concierge — are unchanged.

---

## Context

The Reference Home completed a migration to one physical network divided into eight responsibility-
based trust environments (Trusted, Services, Security, Automation, IoT, Interface, Management, Guest).
**This is one implementation's outcome, not a universal prescription** — nothing in this ADR requires
any HTBW installation to use eight VLANs, or any VLANs at all. The governing distinction observed is
**responsibility**, not manufacturer, transport, or product category: device responsibility determines
logical placement; Ethernet and Wi-Fi are attachment methods, not architectural responsibility; one
physical network may carry multiple virtual trust environments; wireless SSID, device role, virtual-
network placement, discovery permission, and communication permission are separate concerns; and
segmentation is not isolation for its own sake — required household experiences must remain functional
across appropriate boundaries.

The migration exposed topology embedded in household behavior as technical debt: kiosk actions and
dashboard-launch configuration referenced literal endpoint addresses that became stale once Home
Assistant and the kiosks moved; Good Morning and Goodnight failed after the move; locally served media
failed because Home Assistant published an obsolete address; and security devices attempted to reach an
obsolete recorder address. This repository's own Reference Home evidence already records an instance of
this pattern: `docs/reference-home/production-behavior-preservation/production-gaps-and-owner-review.md`
§4 flags hard-coded kiosk device IP addresses (alongside a plaintext credential finding) and asks the
owner whether they warrant the same remediation treatment. **Not every literal address is incorrect** —
some upstream integrations provide no supported alternative — but a durable identity that was available
and deferred in favor of a literal address is technical debt.

### Existing authority reused, not reopened

- **Validation is not discovery.** Configured membership establishes the target set; runtime checking
  may disqualify a configured target that is missing or unavailable; it may never discover an unrelated
  replacement ([failure-and-degradation.md](failure-and-degradation.md), "Operational refinements
  observed in legacy implementations"). This already states the discovery-versus-communication
  distinction this review would otherwise have had to invent, and it is restated, not re-decided, below.
- **Concierge must not runtime-search devices to satisfy a vocabulary term; resolution is explicit and
  configured** ([../contracts/concierge-contract.md](../contracts/concierge-contract.md) §5, Hard
  prohibition #3). This already substantially covers "Concierge must not own hard-coded endpoint maps";
  **DL-88** below restates it and makes its application to network endpoints explicit.
- **Endpoint identity across software providers is the Asset model's concern** where more than one
  technical provider represents one physical endpoint — "a single physical object may be an Asset and be
  represented by several Devices and many Entities" ([../models/asset.md](../models/asset.md); **DL-55**,
  closing **OD-88**/#182). **This is a different layer from this ADR's scope.** DL-55 resolves identity
  *across software providers* for one physical thing (for example, a speaker seen through more than one
  integration). This ADR resolves identity *across network changes* (IP, DNS, subnet) for a configured
  endpoint. Neither narrows the other, and **DL-55/OD-88 is not reopened**.
- **Room Configuration participation already requires an explicit native reference** — "no name/room/IP/
  vendor matching is required or permitted" ([../models/room-configuration.md](../models/room-configuration.md)).
- **Home Assistant First** (**DL-18**) and the greenfield mandate's evidence-preservation practice
  ([greenfield-mandate.md](greenfield-mandate.md)) already govern preferring native capability and
  preserving discovered production behavior generally.

### Genuine gaps closed by this ADR

No existing document states the stable-identity resolution order, the network-boundary-independence
invariant, the requirement that a room's interaction capabilities be independently placeable, a
technical-debt recording convention for literal endpoint addresses, or a placeholder convention for
network examples in this repository. These are drafted below as **DL-87** through **DL-89**.

---

## Decision 1 — Stable Identity Hierarchy and Network-Boundary Independence (DL-87)

**Network location is not Home identity.** A device's subnet, VLAN, or IP address describes where it is
attached today; it is never the identifier by which HTBW recognizes it.

**Where a dependency must resolve to a network endpoint, HTBW should resolve it in this order:**

1. a Home Assistant entity, device, area, config-entry, or other supported native identity;
2. an HTBW Foundation identity or governed relationship;
3. a stable local DNS name, where a network endpoint is genuinely required and supported;
4. a centrally reserved DHCP address, as underlying infrastructure;
5. a literal IP address, only where the upstream platform provides no supported alternative.

This restates and makes explicit what **DL-18** (Home Assistant First) and Room Configuration's existing
explicit-reference rule already imply, and it creates **no duplicate HTBW registry for native Home
Assistant objects** — rank 1 is satisfied by referencing the native object, not by copying its address.

**Network-boundary independence.** Moving a supported endpoint between subnets must not, by itself,
require changing: its HTBW identity; its Place relationship; its capability relationship; its Person
preference relationships; Concierge behavior; behavioral scripts; or experience configuration. A network
move may require valid infrastructure reconfiguration — DNS, reservations, firewall policy, discovery
policy, integration reauthentication, or endpoint recommissioning — and those infrastructure consequences
are explicitly distinguished from HTBW's behavioral identity, which does not change because of them.

**Discovery versus communication (restated, not newly decided).** Service discovery is not authorization;
routing is not authorization; firewall permission is not device identity. A lack of discovery must not
erase a configured identity — this is the same prohibition
[failure-and-degradation.md](failure-and-degradation.md) already records as "validation is not
discovery," applied here explicitly to the network layer. Discovery mechanisms may assist commissioning
and availability reporting; they must never become the sole authoritative Home relationship where a
durable configuration already exists.

**Failures degrade observably.** A network-layer failure (an endpoint unreachable at its configured
address) is reported and named, per [failure-and-degradation.md](failure-and-degradation.md)'s existing
"silent degradation is prohibited" rule. It must never silently trigger an unconfigured replacement
identity.

---

## Decision 2 — Foundation and Concierge Responsibility Split for Endpoint and Room-Interaction-Capability Relationships (DL-88)

**Foundation owns stable relationships** among: Home; Place/room; capability; device or native Home
Assistant identity; interaction input (voice/microphone); audio output; visual/manual interface; and
other governed room capabilities. **Foundation owns these relationships, not endpoint IP addresses.**
This is consistent with, and does not alter, Foundation's existing ownership of Room Configuration
(`adr-room-configuration-ownership.md`) and the object/relationship ownership already recorded in
[../contracts/foundation-contract.md](../contracts/foundation-contract.md).

**Room Configuration must be able to represent separate room-interaction-capability relationships**,
each independently configurable:

- voice_input or microphone endpoint;
- spoken_response_output or media-player endpoint (named `audio_output` in this ADR's original draft;
  refined to `spoken_response_output` by
  [adr-decoupled-voice-interaction-capability-architecture.md](adr-decoupled-voice-interaction-capability-architecture.md)
  (**DL-90**, accepted) before this ADR's own acceptance review, to avoid colliding with
  music/media `audio_output` capability semantics);
- interface or kiosk endpoint;
- physical remote or other interaction surface, where applicable.

**A room's microphone is not required to be the device that plays the response.** The microphone,
speaker, kiosk, and Home Assistant host may reside on different network segments without changing any
of their HTBW identities, their Place relationship, or their capability relationship. This is a narrow,
genuinely new extension of Room Configuration's existing "which experience endpoints exist (music,
video, announcement, conversation)" vocabulary
([../contracts/room-configuration-contract.md](../contracts/room-configuration-contract.md)) to state
explicitly that these experience endpoints are independently placeable and independently identified —
it does not change how participation, exposure, or exclusion already work for any of them.

**Concierge consumes Foundation relationships and Home Assistant identities. Concierge must not own
hard-coded maps**, including but not limited to:

- microphone address → speaker address;
- room → kiosk IP;
- room → Sonos IP;
- room → dashboard URL;
- security endpoint → recorder IP.

This extends Hard Prohibition #3 ("Concierge must not runtime-search devices to satisfy a vocabulary
term. Resolution is explicit and configured.") explicitly to network-endpoint maps; it does not add a
new prohibition class, and it does not change Concierge's existing resolution path. **Concierge resolves:
interaction input → Place → configured capability → governed output or action**, using Foundation's
configured relationships — the same resolution shape the Concierge Contract already requires for every
other vocabulary resolution, applied here explicitly to network-attached endpoints.

---

## Decision 3 — Commissioning, Native Fallback, and Technical-Debt Recording Convention (DL-89)

**Commissioning mode versus permanent architecture.** Some vendor applications require a commissioning
device to be temporarily placed on the same network as the target device. This is recorded as a
commissioning concern, not a permanent-architecture concern: **a same-network commissioning requirement
must not automatically dictate an endpoint's permanent trust placement, and must not require weakening
ordinary cross-boundary policy** once commissioning is complete.

**Native fallback.** Approved native control paths may remain available where they provide legitimate
household resilience or usability — for example, native audio/video control, platform applications,
direct security operation, or supported vendor commissioning applications, described generically here.
**No vendor-specific fallback path is created as a universal HTBW requirement.** This restates, for the
network-boundary case specifically, the existing practice already evidenced in the greenfield mandate
and in Home Assistant First (**DL-18**) of preferring native capability without foreclosing a working
native alternative.

**Technical-debt recording convention (narrow and proportionate).** Where a literal endpoint address is
temporarily accepted to deliver value quickly, and a durable identity was available but deferred, record:

- why the shortcut is necessary;
- where it exists (exact repository path or production location);
- the responsible owner;
- the upstream limitation, if any;
- the intended durable identity;
- the remediation trigger;
- the acceptance test required before replacement;
- security and failure implications.

**This convention applies proportionately to production-relevant and durable examples, not to every
benign test fixture or local development value.** It does not create a general Technical Debt framework
or a new HTBW responsibility — "Technical Debt" as a published framework concept with no repository
representation remains the unticketed residual of **Issue #181** (Episode 11), which this ADR does not
decide, narrow, or substitute for. The convention above is a recording discipline for one specific class
of shortcut (literal network endpoint addresses), applied by the separate **Hard-Coded Topology Audit and
Remediation** issue (**#197**).

**Sensitive-information and placeholder convention.** Operational network details are deployment secrets
or restricted operational documentation, not public architecture. Repository examples must use
placeholders such as `ha.example.internal`, `kiosk-primary.example.internal`, "a reserved private
address," "Management network," or "Security network" — never an actual Reference Home or any
household's operational value (IP address, MAC address, SSID, PPSK, password, internal DNS name,
firewall-log record, physical-infrastructure location, administration URL, or local-user credential).
Applying this convention, two pre-existing literal values discovered in this repository's Reference Home
evidence during this review — a real production REST-endpoint address and a real internal UNC host
address — were redacted to placeholders as part of this review; see **#197** for the full disposition.

**Migration invariant.** HTBW migration must preserve every intentional, beneficial production behavior
unless that behavior has been explicitly reviewed and approved for retirement or replacement. No
production automation, script, helper, scene, endpoint relationship, or fallback path may be removed
merely because an HTBW implementation appears to supersede it.

---

## Commissioning and acceptance criteria

The following are recorded as required acceptance outcomes for a future HTBW Integration implementation
to validate against. **None is implemented by this ADR.** Acceptance must test household outcomes after
cold starts and network-state reconstruction, not only while pre-existing sessions remain active:

- a Home Assistant full restart does not require any configured endpoint relationship to be re-entered;
- an HTBW Integration reload preserves every configured endpoint relationship unchanged;
- a Concierge reload preserves every configured endpoint relationship unchanged;
- an endpoint's IP address changes while its durable identity (native reference, Foundation
  relationship, or stable DNS name) remains stable, and no HTBW behavior requires reconfiguration;
- a kiosk moves to another subnet without requiring its Place or capability relationship to change;
- a room's microphone and its audio output are on separate network segments, and both continue to
  resolve correctly;
- a configured identity is retained when discovery is temporarily unavailable — it is never erased by
  the absence of a discovery signal;
- a required native fallback path remains available after a network change;
- an obsolete address is not retried indefinitely once successful reconfiguration has occurred;
- a network failure is observable (reported and named) and never silently changes a configured
  identity.

---

## Relationship to existing decisions, issues, and reviews

| Item | Relationship to this ADR |
|---|---|
| **DL-55** / **OD-88** (#182, closed) | **Not reopened.** A different layer — cross-software-provider identity for one physical endpoint, not network/IP/DNS stability. Cited as precedent for the Asset model's existing identity-anchoring role. |
| [failure-and-degradation.md](failure-and-degradation.md) "validation is not discovery" | **Reused, not re-decided.** Restated explicitly for the network layer in DL-87. |
| [../contracts/concierge-contract.md](../contracts/concierge-contract.md) Hard prohibition #3 | **Reused, extended.** DL-88 names network-endpoint maps as an explicit instance of the existing prohibition; the prohibition itself is unchanged. |
| [../models/room-configuration.md](../models/room-configuration.md) | **Reused.** The existing explicit-participation and no-IP-matching rule is unchanged; DL-88 adds that room-interaction capabilities are separately representable. |
| **DL-18** (Home Assistant First) | **Reused.** DL-87's resolution order and DL-89's native-fallback statement both restate DL-18 for this specific case. |
| **Issue #181** (Episode 11, Technical Debt as an ungoverned framework concept) | **Unaffected, not decided here.** DL-89's recording convention is narrow and instance-specific; it does not create the general Technical Debt responsibility #181 still owns. |
| **Issue #146** (Home Assistant native capability verification backlog) | **Unaffected.** This ADR's stable-DNS and native-identity mechanics are routed to **#196**, not to #146, and do not add an item to #146. |
| **#196** (Foundation and Concierge mechanics, Implementation Research) | Residual of DL-87/DL-88. Schema, DNS mechanism, and enforcement mechanics are not decided here. |
| **#197** (Hard-Coded Topology Audit and Remediation) | Applies DL-89's recording convention and classification scheme to existing repository references; not a decision issue. |

---

## Explicit non-goals

- No UniFi integration behavior, VLAN management, network-subnet management, wireless SSID/PPSK
  management, switch-port management, firewall-rule management, mDNS proxying, or DHCP/DNS
  infrastructure management is authorized.
- No parallel network controller is created, and HTBW is not made dependent on UniFi or any other
  specific network vendor.
- No installation is required to use exactly eight virtual networks, or any specific number of VLANs.
- No Reference Home operational network map, IP address, MAC address, SSID, or physical-infrastructure
  location is exposed by this ADR.
- No new runtime endpoint-resolution implementation is authorized by this ADR; mechanics are routed to
  **#196**.
- No production Home Assistant instance is modified, and nothing is deployed to HA-DEV.
- No new responsibility is created; Foundation and Concierge's existing ownership boundaries are
  restated and extended to network endpoints, not changed.
- **DL-55**/**OD-88**, Concierge Contract Hard prohibition #3, Room Configuration's existing
  participation rule, and Issue **#181** are each referenced above and are each unaffected — none is
  narrowed, resolved, or reopened by this ADR.
- **This entry is drafted content, not yet a closed decision; it must not be cited as equivalent to
  DL-01–DL-86 until #195's formal acceptance review records a result.**

---

## Related documents

- [failure-and-degradation.md](failure-and-degradation.md)
- [home-assistant-boundary.md](home-assistant-boundary.md)
- [greenfield-mandate.md](greenfield-mandate.md)
- [../contracts/concierge-contract.md](../contracts/concierge-contract.md)
- [../contracts/foundation-contract.md](../contracts/foundation-contract.md)
- [../contracts/room-configuration-contract.md](../contracts/room-configuration-contract.md)
- [../models/room-configuration.md](../models/room-configuration.md)
- [../models/asset.md](../models/asset.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
- [../governance/open-decision-issue-index.md](../governance/open-decision-issue-index.md)
- [../reference-home/discovery/07-network-and-infrastructure-inventory.md](../reference-home/discovery/07-network-and-infrastructure-inventory.md)
- [../reference-home/production-behavior-preservation/production-gaps-and-owner-review.md](../reference-home/production-behavior-preservation/production-gaps-and-owner-review.md)
- [adr-decoupled-voice-interaction-capability-architecture.md](adr-decoupled-voice-interaction-capability-architecture.md) — refines DL-88's generic `audio_output` term to `spoken_response_output` (**DL-90**, accepted)