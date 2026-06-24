# Bus Factor

**Definition:** The smallest number of people who would need to disappear for a project to grind to a halt — a measure of how concentrated critical knowledge is.

**Category:** Teams

## Takeaways
- A bus factor of 1 is a red flag: one person's absence stops the work.
- Higher numbers (4, 5+) indicate knowledge is genuinely distributed, not just nominally shared.
- Documentation, pairing, code review, and rotation are the main tools for raising bus factor.
- Low bus factor correlates with brittle deployment, legacy subsystems, and "tribal" processes.
- The "Dead Sea Effect" — skilled people leaving first — concentrates knowledge in the least equipped to carry it.

## Why it matters
Every long-running project accumulates implicit knowledge: why this retry is here, which config is load-bearing, what breaks if you touch this job at 3 AM. When that knowledge lives in one person's head, the project is one illness, one resignation, or one vacation away from a crisis.

Bus factor makes this risk visible and measurable. It reframes knowledge sharing from a "nice to have" into a resilience metric, and it gives teams a concrete number they can try to raise over time.

## Examples
- **Solo DB expert:** A startup's one database specialist owns backups, schema, and tuning. They take a two-week vacation and three separate incidents pile up because nobody else can triage them.
- **left-pad:** A single maintainer unpublished an eleven-line npm package and broke builds across the JavaScript ecosystem — a dependency with bus factor 1 propagating up the supply chain.

## When to apply
Raise bus factor during onboarding, before key people go on leave, during retrospectives after an incident traced to one person's unavailability, and whenever you inventory your systems. For each critical subsystem, name the people who could realistically operate and modify it. If the list has one name, that's your next investment.

It's also worth applying during hiring and retention decisions — losing a "square-root" contributor (see Price's Law) from a bus-factor-1 system is the worst combination, and it should shape how you plan backfill.

## Related laws
- [Conway's Law](./conways-law.md)
- [Brooks's Law](./brooks-law.md)
- [Dunbar's Number](./dunbars-number.md)
- [Price's Law](./prices-law.md)

---
Source: [Bus Factor — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/bus-factor/)
