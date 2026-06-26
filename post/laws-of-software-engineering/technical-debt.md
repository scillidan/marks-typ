# Technical Debt

**Definition:** Shortcuts and deferred cleanup in code behave like financial debt, accruing interest paid as slower future work.

**Category:** Quality

## Takeaways
- Shortcuts offer speed now in exchange for obligations later - the "principal" plus compounding "interest."
- Every workaround, hack, and missing test silently taxes future changes.
- Debt is fine when taken deliberately with a repayment plan; toxic when invisible and ignored.
- Paying it down requires refactoring, test coverage, and sometimes architectural rework.

## Why it matters
The metaphor makes a hard trade-off legible to both engineers and business leaders. Shipping fast by skipping tests, hardcoding values, or duplicating logic trades future velocity for present velocity. That trade can be smart - especially when learning faster matters more than elegance - but only if the cost is tracked.

When debt goes unmanaged, it compounds. Teams slow down, bugs multiply, and morale sags as every change fights the codebase. When managed, debt is a tool: taken on consciously to hit a window, then repaid in a planned cleanup before the interest dominates delivery.

## Examples
- **Skipped testing:** A deadline-driven team ships without automated tests. Early wins mask rising risk; soon every change breaks something, and they must stop to add tests before they can move again.
- **Prototype debt:** A startup hardcodes values to win a first customer. The gamble works, and they schedule a "rehab sprint" to pay down the worst debt before scaling features.

## When to apply
Reference technical debt when negotiating scope or deadlines, during postmortems where "we rushed this" shows up repeatedly, when planning refactors, and when making the case to leadership for cleanup work. It's also a useful lens in code review to name a specific cost rather than vague "this feels bad."

## Related laws
- [Broken Windows Theory](./broken-windows.md)
- [Hofstadter's Law](./hofstadters-law.md)
- [Boy Scout Rule](./boy-scout-rule.md)

---
Source: [Technical Debt - lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/technical-debt/)
