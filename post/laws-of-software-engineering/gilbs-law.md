# Gilb's Law

**Definition:** Anything worth quantifying can be measured in some way that is better than not measuring it at all.

**Category:** Planning

## Takeaways
- Partial, imperfect data about something that matters is almost always more useful than no data.
- It complements Goodhart's Law: don't abandon measurement, just don't turn measurements into blunt targets.
- Start with simple, cheap proxies and refine them over time - the act of measuring itself sharpens thinking.
- Approximate or indirect indicators still provide direction and feedback that intuition alone cannot.
- Combining several imperfect proxies usually beats chasing a single perfect one.

## Why it matters
Gilb's Law is the antidote to the paralysis that Goodhart's Law can cause. It is tempting to conclude that because every metric can be gamed, nothing should be measured - but that hands decision-making back to gut feel and office politics. Measurement, even rough measurement, creates a shared reality that teams can argue about honestly.

"Unmeasurable" qualities like code quality, developer productivity, or technical debt can be approached through layered proxies: cyclomatic complexity, lint counts, defect rates, change lead time, incident frequency, and developer surveys. None is the truth, but together they expose patterns that invisible knowledge cannot. The goal is to measure enough to see movement, with enough humility to know the numbers are indicators, not verdicts.

## Examples
- **Developer productivity:** It resists direct measurement, but DORA metrics like deployment frequency and change lead time act as actionable proxies that reveal pipeline friction.
- **Technical debt:** No perfect gauge exists, but a combination of complexity scores, incident rates, and periodic developer surveys turns an opaque problem into a trackable one.

## When to apply
Reach for Gilb's Law when someone argues a concern can't be tracked, or when decisions keep being made on vibes. Use it when designing dashboards, planning engineering health reviews, or evaluating team practices: pick the simplest available proxy, start recording it, and improve the instrument as you learn.

Pair it with Goodhart's Law during KPI and OKR design. Measure to learn and to guide discussion, not to mechanically reward - and carry more than one metric so no single one becomes the whole game.

## Related laws
- [Goodhart's Law](./goodharts-law.md)
- [Parkinson's Law](./parkinsons-law.md)
- [Hofstadter's Law](./hofstadters-law.md)

---
Source: [Gilb's Law - lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/gilbs-law/)
