# Inversion

**Definition:** Instead of only asking "how do we make this succeed?", ask "how would this fail?" — and design to avoid those failure modes.

**Category:** Decisions

## Takeaways
- Flip the question: what would guarantee the project misses its goal?
- Pre-mortems imagine the disaster ahead of time and surface the risks optimistic planning hides.
- Designing for failure (outages, attacks, bad input) yields systems that stay up when reality misbehaves.
- Adversarial thinking — "how would I break this?" — finds edge cases and security holes you otherwise miss.

## Why it matters
Optimistic planning tends to produce fragile plans. Everyone imagines the happy path, agrees it looks good, and ships it — then reality supplies the edge cases no one wanted to think about. Inversion fixes this by deliberately spending time on the unhappy side of the problem.

The technique is associated with Charlie Munger and the mathematician Jacobi ("invert, always invert"), but the software version is concrete: before you build, enumerate the ways the system could fail. Use that list to drive retries, timeouts, validation, circuit breakers, tests, and rollback plans. You end up with something much harder to knock over.

## Examples
- **Chaos Monkey:** Netflix deliberately kills production instances to force the system to survive failure. Instead of hoping nothing breaks, they make breakage routine and build for it.
- **TDD:** Test-driven development starts with a failing test — forcing you to specify what "broken" looks like before writing code that's "working."

## When to apply
Use inversion during architecture reviews, security design, SRE planning, test design, and project kickoffs. Pre-mortems ("imagine it's six months later and this project failed — why?") are a clean, low-cost way to bring it into planning.

It's also useful personally: before making a big technical or career decision, list what would make you regret it. That list is often more honest than the list of reasons it'll work.

## Related laws
- [First Principles Thinking](./first-principles.md)
- [Murphy's Law](./murphys-law.md)
- [Premature Optimization](./premature-optimization.md)
- [Confirmation Bias](./confirmation-bias.md)

---
Source: [Inversion — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/inversion/)
