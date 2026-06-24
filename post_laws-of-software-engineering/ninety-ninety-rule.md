# The Ninety-Ninety Rule

**Definition:** The first 90% of the code takes 90% of the schedule, and the remaining 10% takes the other 90% of the schedule.

**Category:** Planning

## Takeaways
- Late-stage work (edge cases, integration, bug fixes, polish) typically consumes as much time as the initial build.
- "Mostly done" is a misleading state - it often means roughly halfway, in calendar terms.
- Hidden effort hides in integration testing, corner cases, performance tuning, and QA.
- Progress feels fast while building core features and then stalls during finishing work.
- Plans should budget real time for the tail, not treat it as a quick cleanup pass.

## Why it matters
Teams tend to race through the visible, well-understood features and then hit a wall made of everything that was deferred: cross-environment quirks, flaky integrations, accessibility, performance regressions, obscure inputs, and production-readiness work. Each of these is small in isolation and vast in aggregate, which is why the last slice of the project can rival the first in effort.

The rule is really an estimation warning. It pairs naturally with Hofstadter's Law: we consistently underestimate the part of the work we can't fully see yet. Treating "finishing" as a first-class phase, with its own budget and plan, is what prevents the familiar slip from "almost done" to "still going."

## Examples
- **Mobile app launch:** A team ships 90% of features in three months and expects one more month to release. Integration reveals crashes on edge inputs, memory issues, and cross-module bugs - the tail takes another three months.
- **Website rollout:** Core pages and login go live quickly. The remaining work - cross-browser compatibility, responsive behavior, accessibility, tests, and performance tuning - looks minor but consumes effort comparable to the initial build.

## When to apply
Bring this law into estimation and roadmap reviews, especially when stakeholders hear "we're 90% done." Use it during milestone planning to explicitly size hardening, integration, and polish phases rather than absorbing them into a single generic buffer.

It also belongs in any discussion about pushing a deadline forward based on feature completeness. If the visible work is done but integration, edge cases, and QA are still open, assume a long tail and plan accordingly.

## Related laws
- [Hofstadter's Law](./hofstadters-law.md)
- [Parkinson's Law](./parkinsons-law.md)
- [Pareto Principle](./pareto-principle.md)

---
Source: [The Ninety-Ninety Rule - lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/ninety-ninety-rule/)
