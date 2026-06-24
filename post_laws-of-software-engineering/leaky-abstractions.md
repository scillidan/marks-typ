# The Law of Leaky Abstractions

**Definition:** Every non-trivial abstraction leaks — sooner or later, details of the layer underneath show through and you have to know what's really going on.

**Category:** Architecture

## Takeaways
- Abstractions reduce complexity most of the time but fail predictably at edge cases.
- Using a high-level tool well eventually requires understanding the layer below it.
- Performance problems, bugs, and odd behaviors are the usual leak points.
- When building an abstraction, aim to minimize and document where it leaks.
- Don't treat leakage as a design failure — treat it as a design reality to plan for.

## Why it matters
Joel Spolsky's observation is that abstractions are both necessary and inherently imperfect. They let us work at a higher level by hiding the mess below, but the mess is still there, and it resurfaces in specific, often painful situations: a slow query, a weird network timeout, a subtle ordering bug. At that moment, the abstraction stops helping and you need the mental model of what it was hiding.

This is not an argument against abstractions — without them, modern software would be impossible. It is an argument for honesty: engineers who rely only on the happy path of an abstraction will be stuck when it leaks, while engineers who understand at least one layer below it can diagnose and work around the leak quickly.

## Examples
- **Managed memory:** Garbage-collected languages hide allocation, but once you hit memory leaks from retained references or GC pauses in production, you need to understand collector behavior.
- **ORMs:** Treating rows as objects is convenient until an innocent-looking traversal produces N+1 queries or a lock storm, forcing you to read the generated SQL and the database's execution plan.

## When to apply
Keep this law in mind whenever you pick a framework, ORM, serverless runtime, managed database, or any "it just works" layer — and whenever you design one yourself. Use it to decide how deep your team needs to understand the layer below, what observability to expose at the boundary, and where to document known limits. It is especially relevant during performance investigations, incident reviews, and technology selection.

## Related laws
- [Hyrum's Law](./hyrums-law.md)
- [Gall's Law](./galls-law.md)
- [Tesler's Law](./teslers-law.md)

---
Source: [The Law of Leaky Abstractions — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/law-of-leaky-abstractions/)
