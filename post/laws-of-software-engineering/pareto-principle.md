# Pareto Principle (80/20 Rule)

**Definition:** Roughly 80% of effects come from about 20% of the causes — so a small, well-chosen subset of work usually drives most of the outcome.

**Category:** Decisions

## Takeaways
- Find the 20% that matters — the features, bugs, code paths, or customers responsible for most of the impact — and concentrate effort there.
- Equal effort across everything is almost never optimal; hotspots deserve more attention than cold paths.
- The ratio isn't literally 80/20; profiling and data tell you where the actual imbalance lives.
- Applies to prioritization, optimization, and personal productivity alike.

## Why it matters
Engineering resources are finite; the Pareto Principle says the returns on those resources are lumpy. A handful of queries dominate database load. A handful of endpoints serve most traffic. A handful of bugs cause most of the crashes. If you treat every line of code as equally worthy of optimization, you spread effort thin and get marginal gains.

Measuring first and acting second is the practical discipline. Profile before optimizing, look at usage before prioritizing, and look at crash reports before rewriting. The data usually points to a small number of places where fixes pay off out of proportion to their size.

## Examples
- **Microsoft crash data:** Analysis showed that ~20% of bugs caused ~80% of crashes, and ~1% caused roughly half. Targeting those specific bugs produced huge stability wins.
- **Feature usage:** Teams analyzing product analytics often find that 5-10 features out of 50 drive 80%+ of actual usage, which clarifies what to invest in and what to sunset.

## When to apply
Use the 80/20 lens in performance tuning, bug triage, roadmap prioritization, MVP scoping, and customer support — anywhere effort and impact can diverge. Before you start optimizing, instrument. Before you plan features, measure what people use.

Also useful for personal work: which of the tasks on your list actually move the needle? The rest can wait, be delegated, or be dropped.

## Related laws
- [Premature Optimization](./premature-optimization.md)
- [KISS](./kiss.md)
- [YAGNI](./yagni.md)
- [Tesler's Law](./teslers-law.md)

---
Source: [Pareto Principle (80/20 Rule) — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/pareto-principle/)
