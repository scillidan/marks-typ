# Gall's Law

**Definition:** Every complex system that works got there by evolving from a simpler system that also worked — you can't successfully design the complex one from scratch.

**Category:** Architecture

## Takeaways
- Start with the smallest thing that actually works end-to-end, then grow it.
- Big-bang designs routinely fail because too many assumptions are untested at once.
- Incremental evolution lets each addition get battle-tested before the next one lands.
- This is the structural argument for MVPs, monoliths-first, and iterative architecture.
- Working simple systems adapt to surprises; elaborate paper designs usually don't.

## Why it matters
John Gall observed that successful complex systems almost always have a simpler working ancestor. The reason is epistemic: when you try to design every subsystem, interface, and interaction up front, you are making countless guesses about behaviors you haven't observed yet. The first contact with reality tends to invalidate many of them at once, and the project collapses under accumulated mistakes.

A minimal working core, by contrast, gives you a feedback loop. Each new capability gets added to a system that is already alive, so problems surface one at a time and can be absorbed. Over time this compounds into a complex system that actually works — not because it was designed in one stroke, but because every step along the way was real.

## Examples
- **Facebook:** Launched as a campus-only profile directory with narrow scope; the global platform was grown on top of that working core, not designed in 2004.
- **Monolith-first microservices:** Modern guidance is to start with a single deployable, learn the real seams from running it, and only then extract services with well-understood boundaries.

## When to apply
Invoke Gall's Law at the start of any non-trivial system: greenfield products, platform rewrites, architecture proposals, and anywhere someone sketches a diagram with many boxes and no running code. It is the counterweight to "let's design the whole thing first." Use it to justify cutting scope to a walking skeleton, deferring infrastructure generality, and keeping the initial architecture embarrassingly small so it can actually ship and learn.

## Related laws
- [Second-System Effect](./second-system-effect.md)
- [YAGNI](./yagni.md)
- [KISS](./kiss.md)
- [Conway's Law](./conways-law.md)

---
Source: [Gall's Law — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/galls-law/)
