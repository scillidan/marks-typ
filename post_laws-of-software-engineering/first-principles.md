# First Principles Thinking

**Definition:** Solve hard problems by stripping them down to the underlying facts and constraints, then reasoning back up — instead of copying whatever solution is conventional.

**Category:** Decisions

## Takeaways
- Ask "what are we actually trying to do, and what's genuinely required?" before picking a tool or pattern.
- Separate real constraints from inherited assumptions ("we've always done it this way").
- Don't anchor estimates on analogies to prior projects; decompose from scratch.
- This mode is expensive — use it for transformative decisions, not every ticket.

## Why it matters
Most engineering decisions borrow shape from precedent: "we'll do it like Project X," "use the standard framework," "mirror what Big Company wrote about." That's usually efficient, but it quietly inherits whatever constraints the precedent had, even ones that don't apply to you.

First-principles thinking forces a clean slate. You identify what's physically, mathematically, or legally required, then build the simplest thing that satisfies those requirements. This is how genuinely new architectures appear — and how teams discover that the "standard" approach carried a 10x cost they didn't need to pay.

## Examples
- **SpaceX reusable rockets:** Rather than accepting industry pricing, the team compared raw material cost to finished-rocket cost, saw a massive gap, and concluded reusability was worth the engineering bet.
- **Build vs. buy analytics:** A team questioning a six-figure analytics license broke the product into its core capabilities (ingest, aggregate, visualize) and assembled an equivalent stack from open-source parts at a fraction of the cost.

## When to apply
Reach for first-principles thinking at inflection points: new product bets, large architecture choices, build-vs-buy decisions, cost-reduction programs, and moments where a "standard" solution feels too expensive or too constraining. Also useful in estimation when historical analogies are leading you astray.

Don't default to it for routine work — for most tickets, the conventional answer is fine and much cheaper to produce. It pays off when the stakes justify the cognitive cost.

## Related laws
- [Occam's Razor](./occams-razor.md)
- [KISS](./kiss.md)
- [Inversion](./inversion.md)
- [Gall's Law](./galls-law.md)

---
Source: [First Principles Thinking — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/first-principles-thinking/)
