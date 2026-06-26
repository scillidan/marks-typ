# Goodhart's Law

**Definition:** Once a measurement is turned into a target, it stops being a reliable measurement.

**Category:** Planning

## Takeaways
- Optimizing directly for a metric usually erodes the underlying outcome the metric was meant to reflect.
- Metrics are best treated as signals for inquiry, not as goals to hit.
- Balancing several complementary metrics makes any single one harder to game.
- Quantitative numbers need qualitative context to stay meaningful.
- Badly designed incentives can actively make behavior worse (the Cobra Effect).

## Why it matters
Metrics in software often stand in for things we actually care about - quality, reliability, user happiness - because those are hard to measure directly. As soon as a proxy becomes the thing people are graded or rewarded on, behavior shifts to move the proxy, not the underlying reality. The number improves while the outcome quietly degrades.

This is why goal-setting around engineering metrics is so tricky: story points, lines of code, tickets closed, coverage percentages, and velocity are all useful as diagnostic signals and dangerous as performance targets. A good measurement culture keeps metrics visible, balances them against each other, and couples them with human judgment about what the numbers mean.

## Examples
- **Lines of code as a target:** When teams are rewarded for volume, terse and elegant solutions get replaced by verbose or duplicated code that inflates the metric while making the system harder to maintain.
- **Test counts as a target:** QA measured on tests executed shifts toward many cheap, shallow tests, hitting the number while missing the integration bugs that actually matter.

## When to apply
Use Goodhart's Law whenever you're designing KPIs, OKRs, dashboards, bonus structures, or performance reviews. Before you lock a metric to a target, ask how someone could move the number without improving the outcome - and assume somebody will.

It also applies during retros when a metric looks "too good." Investigate whether the underlying behavior really improved or whether the team has simply learned the measurement. Pair it with Gilb's Law: measure, but keep metrics plural and interpreted.

## Related laws
- [Gilb's Law](./gilbs-law.md)
- [Parkinson's Law](./parkinsons-law.md)
- [Dilbert Principle](./dilbert-principle.md)
- [Unintended Consequences](./unintended-consequences.md)

---
Source: [Goodhart's Law - lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/goodharts-law/)
