> **Document status: Operational — discovery artifact.** Not architecture-of-record.

# Owner Input Required

Narrative, historical, and preference-based facts that discovery **cannot** establish from production or repository evidence. Nothing in this file is presented elsewhere as observed fact.

## Known owner-provided context (recorded as OWNER PROVIDED, not independently verified against production)

1. The owner has used the technology lineage that became Insteon since the X10 era in 1997.
2. Leviton lighting and shade capabilities would have been preferred if the home's wiring plan could have been adjusted.
3. Construction and wiring constraints contributed to the selected retrofit approach.
4. The series should emphasize that households can grow into the architecture while planning infrastructure ahead of installation.
5. Home Assistant is intentionally positioned as the controller, hub, and home operating platform of choice.
6. The HTBW Integration for Home Assistant will be addressed in the closing article.

## Additional narrative gaps discovery could not fill

- **Why Home Assistant specifically**, beyond the stated intent (article 5) — what else was evaluated, and why it lost.
- **Construction/renovation history** of the home itself — age, scope of retrofit vs. new construction, timeline.
- **The front-gate doorbell gap** (confirmed missing entities) — what happened, whether it's a known/pending fix.
- **The vanished PowerView scene** (`Close Downstairs Shades`, confirmed `unknown` by Watchman) — same.
- **The two stale soil-moisture sensors** (Bamboo 05/06) — hardware failure, battery, or decommissioned zone?
- **`openclaw` and `vaca` custom-component purposes** — names alone do not reveal function.
- **The household's actual division of logic between native Home Assistant automations and Node-RED** (`nodered` is installed; its role relative to the 84 native automations is unclear).
- **Network hardware specifics** (router/switch/AP models, count, placement, VLAN design) — see `07-network-and-infrastructure-inventory.md`.
- **Backup destination, schedule, and retention policy.**
- **Whether and how the household uses Home Assistant Cloud for remote access versus another method.**
- **What "would be done differently today"** across every capability area — inherently narrative, owner-only knowledge.
- **The intended meaning and structure of the closing "HTBW Integration for Home Assistant" article** beyond the stated theme — specifically, which household-native patterns (the "Concierge"/"VA:" automation family) the owner wants explicitly reframed under HTBW's seven responsibilities, and which should remain presented as "what Home Assistant and clever automation already achieve on their own."
- **Resident count and relationships** — 7 `person` profiles exist; which are residents, long-term household members, versus occasional guests is not determinable from registry data alone (redacted as "Resident 1 (Primary)" / "Resident 2" plus 5 additional profiles, pending owner clarification of roles for safe publication).

## Why these were not inferred

Per the governing instruction, discovery must never convert an inference into an observed fact, and must never invent personal stories, product preferences, construction history, or selection rationale. Every item above requires a direct owner interview or explicit written confirmation before it can move from this file into any publication-facing article content.
