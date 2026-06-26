# The Boy Scout Rule

**Definition:** Always leave code in a cleaner state than you found it.

**Category:** Quality

## Takeaways
- Improve code quality through small, incremental polishes rather than risky grand rewrites.
- Tiny cleanups during normal work compound into major codebase improvements over years.
- A shared "leave it better" ethic spreads ownership and accountability across the team.
- Constant light attention prevents the slow slide into unmaintainable legacy code.

## Why it matters
Sweeping refactors are rarely scheduled, and when they are, they tend to slip. The Boy Scout Rule sidesteps that problem by distributing quality work across every single change. A developer touching a file to fix a bug can also rename a confusing variable, delete a dead branch, or add a missing test, paying for those improvements in minutes rather than sprints.

Over thousands of small edits, the codebase trends upward instead of decaying. The rule also reshapes culture: when everyone cleans as they go, nobody treats messiness as someone else's problem.

## Examples
- **Touching a legacy module:** A developer adding a feature to a 200-line function also splits it into named helpers and removes dead code, at little extra cost but large readability gain.
- **"If you touch it, you own it":** Teams like Google's encourage engineers to fix small issues they encounter on unrelated tasks, heading off architectural rot before it becomes expensive.

## When to apply
Apply the rule on every pull request, especially in legacy code, during code review when a small polish would help the next reader, and when fixing bugs where the surrounding code made the bug easy to write. It is particularly valuable when you lack the budget for a dedicated refactor but still need the codebase to improve.

## Related laws
- [Broken Windows Theory](./broken-windows.md)
- [Technical Debt](./technical-debt.md)
- [YAGNI](./yagni.md)

---
Source: [The Boy Scout Rule - lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/boy-scout-rule/)
