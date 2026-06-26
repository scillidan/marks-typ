# Broken Windows Theory

**Definition:** Small unrepaired defects signal that quality does not matter, inviting further decay.

**Category:** Quality

## Takeaways
- Visible neglect - failing tests, ignored warnings, stale TODOs - normalizes cutting corners.
- Clean codebases pull contributors up to the existing standard; messy ones drag them down.
- Fixing small issues promptly prevents compounding entropy and slows software decay.
- Quality is a self-reinforcing feedback loop: discipline begets discipline.

## Why it matters
Borrowed from urban criminology by *The Pragmatic Programmer*, the theory holds that an unrepaired window invites more broken windows. In software, the "windows" are failing CI checks nobody fixes, lint errors silenced with overrides, copy-pasted hacks labeled `// temporary`, and dead code no one dares remove. Each tolerated defect lowers the cost of the next one.

Conversely, a codebase where maintainers promptly repair small cracks sends a clear signal: this place has standards. New contributors mirror what they see, so the prevailing level of polish tends to persist in both directions. Preventing decay is dramatically cheaper than reversing it.

## Examples
- **Rotting-by-TODO:** A repo littered with months-old `TODO: fix this hack` comments teaches newcomers that shortcuts are acceptable, and more hacks get added.
- **Aggressive maintenance:** A project whose maintainers fix style nits and simplify code sets an implicit standard; outside contributions arrive closer to that bar.

## When to apply
Apply the theory during code review (don't let small issues slide "just this once"), when onboarding to a codebase (first impressions calibrate new contributors), and after incidents where a small ignored signal turned out to matter. It is especially important on long-lived systems, where compound entropy is the dominant risk.

## Related laws
- [Technical Debt](./technical-debt.md)
- [Boy Scout Rule](./boy-scout-rule.md)
- [Galls Law](./galls-law.md)

---
Source: [Broken Windows Theory - lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/broken-windows-theory/)
