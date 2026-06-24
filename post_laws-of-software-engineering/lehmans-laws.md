# Lehman's Laws of Software Evolution

**Definition:** Software embedded in the real world must continuously evolve, and that evolution follows predictable patterns of growth, complexity, and constraint.

**Category:** Quality

## Takeaways
- Useful long-lived software must keep changing; standing still means becoming obsolete.
- Every change adds complexity unless effort is spent keeping the system simple.
- Teams face hard delivery-rate limits set by knowledge, coordination, and process.
- Perceived quality erodes as expectations rise and minor issues accumulate.
- The eight laws together describe how change, complexity, and organization interact over time.

## Why it matters
Manny Lehman studied large, long-lived systems and found that their dynamics aren't ad hoc - they follow recurring patterns. Business software, operating systems, and platforms must adapt to shifting environments, so change is not optional. But each change subtly increases disorder, and disorder that is not actively paid down compounds.

The practical upshot is that a mature system needs a budget not just for features but for refactoring, documentation, and structural cleanup. Organizations also hit ceilings on how fast they can absorb change - adding people rarely lifts those ceilings and often lowers them (see Brooks's Law).

## Examples
- **Long-lived ERP:** A 2000-era enterprise system still running in 2025 has absorbed a quarter-century of rule changes, integrations, and UI updates. New features take much longer to ship than they did twenty years ago as complexity accumulates.
- **Linux kernel:** Continuous adaptation to new hardware and requirements has required hierarchical subsystem maintainership and deliberate pacing; stop evolving and it would be irrelevant in a few years.

## When to apply
Apply Lehman's Laws when planning the long-term roadmap of a mature system, justifying refactoring and tech-debt budgets, sizing teams for legacy platforms, and setting realistic expectations with leadership about velocity on old codebases. They're especially clarifying when "why is this slower than it used to be?" becomes the recurring question.

## Related laws
- [Brooks's Law](./brooks-law.md)
- [Conway's Law](./conways-law.md)
- [Technical Debt](./technical-debt.md)

---
Source: [Lehman's Laws - lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/lehmans-laws/)
