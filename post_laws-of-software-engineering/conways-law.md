# Conway's Law

**Definition:** Any system that an organization designs will end up structurally mirroring the communication patterns of the organization itself.

**Category:** Teams

## Takeaways
- Module boundaries in software tend to follow the reporting lines and social boundaries of the team that built it.
- Teams that rarely talk to each other will produce components that rarely integrate cleanly.
- The "Inverse Conway Maneuver" reshapes team topology first to steer the architecture you actually want.
- Early choices about who sits with whom calcify into long-lived technical seams.
- Cross-functional, end-to-end teams tend to yield more cohesive, service-oriented systems.

## Why it matters
Architecture does not emerge purely from technical decisions — it emerges from who is allowed to speak to whom. If a company has three departments with separate managers, goals, and calendars, the software they ship will have three layers with mismatched assumptions at each seam.

This makes org design a technical lever. You cannot refactor your way out of an architecture that is being continually re-created by the communication graph that produced it. Changing the system usually requires changing the organization that owns it.

## Examples
- **Three-tier enterprise split:** A company with distinct frontend, backend, and DBA teams shipped an app where every integration seam was painful because each group optimized locally for its layer instead of the whole product.
- **Two-pizza teams:** Amazon's small, autonomous service teams directly produced a service-oriented architecture with clear API contracts — the org chart was the architecture diagram.

## When to apply
Invoke Conway's Law during org design, re-orgs, and when planning a major platform rewrite. Before you draw a new architecture diagram, draw the team diagram you want to live with for the next three years — because that is what you will actually end up with. It is also useful during incident postmortems: if the same boundary keeps breaking, the fix may be organizational rather than technical.

Use it defensively when splitting a team or merging two: predict which module seams will harden and which will dissolve, and decide whether that matches your architectural intent.

## Related laws
- [Brooks's Law](./brooks-law.md)
- [Dunbar's Number](./dunbars-number.md)
- [Galls Law](./galls-law.md)
- [Hyrum's Law](./hyrums-law.md)

---
Source: [Conway's Law — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/conways-law/)
