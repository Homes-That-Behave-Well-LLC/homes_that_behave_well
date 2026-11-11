# ADR: BehavesWell Voice Evidence Product Identity

> **Document status: Canonical ADR.**
> Status: **Accepted** 2026-11-10. Records **DL-154** (issue **#216**; Owner decision). Extends
> **DL-153** ([adr-behaveswell-framework-foundation-core-edition-and-context-identity.md](adr-behaveswell-framework-foundation-core-edition-and-context-identity.md)),
> which renamed BehavesWell Core and explicitly kept *HTBW Voice Evidence*.
> Canonical authority: [../contracts/identity-contract.md](../contracts/identity-contract.md) (Voice
> Evidence App boundary) and [../models/glossary.md](../models/glossary.md).

---

## Decision

**The public identity of the existing product HTBW Voice Evidence becomes BehavesWell Voice
Evidence.** Where the Home Assistant App packaging or Apps surface must be explicit, it is the
**BehavesWell Voice Evidence App**. This is **one product renamed**: not a new product, fork, or
replacement runtime, and not a change to Voiceprint, Identity, or storage architecture.

| Name | Status |
|---|---|
| **BehavesWell Voice Evidence** | Current canonical public product name |
| **BehavesWell Voice Evidence App** | The Home Assistant App packaging of that product |
| **BehavesWell © Voice Evidence** | Formal branded notation only (DL-153 §10 rules apply) |
| **HTBW Voice Evidence** (App) | Former public name. Historical and transitional only |

**Why.** The former name implied a product belonging to Homes That Behave Well or to the residential
implementation. Its bounded function is environment-neutral; nothing in it requires a Home, one Core
Edition, or one environmental context.

## Product boundary — unchanged

The boundary is the accepted **Voice Evidence App boundary** in
[../contracts/identity-contract.md](../contracts/identity-contract.md) (DL-50, DL-120, DL-144, DL-145,
DL-146, DL-147, #161). It is restated here, not changed:

- **The App produces biometric comparison evidence. BehavesWell Core produces decisions.** The App
  creates and stores one Voiceprint per Person after receiving the ten enrollment recordings with the
  stable `person_id`. It reads the governed retention choice, retains or disposes of recordings,
  rebuilds where retained recordings permit, and deletes before re-enrollment. At runtime it encodes
  the utterance, compares it against **every** eligible Voiceprint without stopping at the first
  apparent match, and returns the complete result set as ordinal **Voiceprint Match Levels**. Raw
  scores never cross.
- It **never** resolves a Person or decides who is speaking. It never fuses contextual, BLE, device,
  Room, or Place evidence, disambiguates, or decides between competing evidence. It never makes
  Operational Trust decisions, authorizes actions, controls Home Assistant, or orchestrates Concierge,
  and it is not Home Intelligence or General Reasoning. **Identity** in BehavesWell Core maps
  Voiceprints to People, combines evidence, disambiguates, and resolves the Person.

## Relationships

| With | Relationship |
|---|---|
| **BehavesWell Core** | An independent product that may supply governed voice-comparison evidence to BehavesWell Core **Identity** through an explicit contract (Contracts A–D). Not bundled into Core by definition, not required for Core to operate (a DL-41 optional dependency), not a Core Edition, not Layer 0, and not a Framework stage |
| **BehavesWell Core, Home Assistant Edition** | The current and only consumer. The App is installed through the Home Assistant Apps repository and discovered through Supervisor discovery `htbw` |
| **Identity** (Framework stage 2) | A provider *to* Identity, never Identity itself, and never a second identity authority |
| **Homes That Behave Well** | May be used in the Reference Home through the Home Assistant Edition. That does not make the product residential |
| **BehavesWell Extended Intelligence** | A separate product; no relationship is created |
| Future consumers | Another governed Core Edition or eligible consumer would require its own separately accepted contract and placement review. **None exists or is authorized.** **DL-120 HA-Prod-local** placement continues to bind every current relationship |

## Stable identifiers — unchanged, byte-for-byte

App slug `htbw_voice_evidence`; distribution `htbw-voice-evidence`; Python package, module, and logger
names; every `HTBW_VE_*` environment variable; `_PERSON_KEY_DOMAIN = b"htbw-voice-evidence/person-id/v1\x00"`
and every cryptographic domain separator; the storage root `/data` and every storage path; Voiceprint,
Person-key, and enrollment-recording identifiers and relationships; Contract A paths; Supervisor
discovery `htbw`; the Core domain `htbw`; the repository and organization names; released URLs and
anchors.

**No data migration, compatibility alias, or second slug** is created. None is necessary, because
nothing technical is renamed.

**Delivery.** App version **0.1.1** is a **metadata-only** update (Owner-selected), so installed Apps
receive the new name and description. Supervisor stores an installed App's metadata at install and
update time. There is no runtime, storage, slug, key-derivation, or behavior change.

## Historical references

*HTBW Voice Evidence* in accepted ledger rows, closed issues, commits, and the 0.1.0 CHANGELOG entry is
historical and is not rewritten. *Voice Identity* names the earlier standalone product (DL-05, DL-51
sunset), and survives in established feature and policy terms (the Voice Identity consent gate; Voice
Identity Encoder Migration Policy, DL-145). It is **not** renamed to BehavesWell Voice Evidence.
DL-153's statement that "the App keeps the name HTBW Voice Evidence" is annotated, not rewritten.

## Visual identity

No mark is created or approved; the design is tracked in **#202**. The mark must:

- be environment-neutral;
- be visually separate from the Identity stage icon, BehavesWell Core, Homes That Behave Well, and
  BehavesWell Extended Intelligence;
- work at App and App Info sizes, in light, dark, and monochrome, and without a house container.

Earlier Voice Identity visual work (central voice form, bilateral waveform, bounded comparison field,
restrained comparison arcs) may serve as design evidence. The mark must **not** use:

- a house container or an Identity block;
- a fingerprint or microphone as its sole metaphor;
- a person or profile;
- generic security imagery, a robot, a chat bubble, or AI sparkles;
- any imagery claiming that Person identity is resolved.

It communicates *bounded voice-evidence comparison*.

## What is not changed

No responsibility, contract, invariant, retention rule, Match Level, encoder, or data. **DL-50**,
**DL-120**, **DL-144**, **DL-145**, **DL-146**, **DL-147**, and **DL-153** are consumed unchanged.

## Related documents

- [../contracts/identity-contract.md](../contracts/identity-contract.md)
- [adr-behaveswell-framework-foundation-core-edition-and-context-identity.md](adr-behaveswell-framework-foundation-core-edition-and-context-identity.md)
- [adr-wyoming-compatible-voice-evidence-runtime.md](adr-wyoming-compatible-voice-evidence-runtime.md)
- [../governance/decision-ledger.md](../governance/decision-ledger.md)
