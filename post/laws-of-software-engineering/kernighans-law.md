# Kernighan's Law

**Definition:** Debugging is twice as hard as writing code, so code at the edge of your cleverness is code you cannot debug.

**Category:** Quality

## Takeaways
- Diagnosing a failure requires both understanding intent and locating the fault - harder than writing from scratch.
- Code written at the limit of your ability becomes unmaintainable when something breaks.
- Clarity and structure are investments that pay back many times during debugging.
- "Clever" one-liners often cost hours later for microseconds saved now.

## Why it matters
When you write code, the full design lives in your head. When you debug - your own old code or someone else's - that context is gone and must be reconstructed from the artifact alone. If the original code pushed the author's limits, the debugger (often a tired you, six months later) is operating beyond them.

The practical consequence is a bias toward boring, readable solutions. Named helpers, explicit conditionals, and obvious data flow cost a little typing up front and save disproportionately during incidents. Kernighan's advice pairs naturally with KISS and with skepticism toward premature optimization.

## Examples
- **Clever chain:** A single expression with nested ternaries, bitwise tricks, and list comprehensions looks elegant until it misbehaves at 2 a.m. and nobody can step through it.
- **Boring version:** The same logic split into named intermediate variables with plain `if` statements is longer but trivially debuggable.

## When to apply
Apply Kernighan's Law during code review (ask: could a tired teammate debug this?), when tempted to compress logic into a clever one-liner, when optimizing hot paths (measure first), and when hiring or mentoring juniors whose reach may exceed their grasp. Favor readable code everywhere performance is not proven-critical.

## Related laws
- [KISS](./kiss.md)
- [Premature Optimization](./premature-optimization.md)
- [Least Astonishment](./least-astonishment.md)

---
Source: [Kernighan's Law - lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/kernighans-law/)
