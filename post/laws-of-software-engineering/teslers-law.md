# Tesler's Law (Conservation of Complexity)

**Definition:** Every application has a floor of inherent complexity that cannot be removed, only moved — the design question is who has to deal with it.

**Category:** Architecture

## Takeaways
- Complexity is conserved: if the UI gets simpler, something behind it got harder.
- Good design absorbs complexity into the system so users don't have to.
- A UI full of toggles and configuration is a sign complexity was pushed the wrong way.
- "Simple" and "easy" aren't the same — easy for the user often means hard for the developer.
- The real design question is placement, not elimination.

## Why it matters
Larry Tesler's observation reframes simplicity as an allocation problem. A task has some irreducible amount of decision-making and state management attached to it. You can move that burden around — onto the user, the UI layer, the backend, an algorithm, a default, or a heuristic — but you cannot make it vanish. Pretending otherwise usually means quietly shoving it onto users and calling their confusion a training problem.

The design discipline this implies is deliberate: decide where complexity should live, and then pay the cost of keeping it there well. Products that feel effortless almost always have complicated internals doing the work that users aren't seeing.

## Examples
- **Scheduling meetings:** Email threads push the complexity of finding overlapping availability onto humans; Calendly absorbs that complexity internally and exposes a one-click booking flow.
- **Business logic placement:** Putting rules in stored procedures vs. application code doesn't make them simpler — it just relocates the complexity between the database and the app, each with different trade-offs.

## When to apply
Use Tesler's Law whenever you're designing APIs, user flows, configuration surfaces, or onboarding. When a proposal "simplifies" something, ask where the displaced complexity went and who pays for it. It is especially useful for critiquing designs that offload decisions onto users (too many settings, too many required inputs) and for justifying investment in smart defaults, automation, and richer backends.

## Related laws
- [The Law of Leaky Abstractions](./leaky-abstractions.md)
- [Hyrum's Law](./hyrums-law.md)
- [KISS](./kiss.md)
- [Occam's Razor](./occams-razor.md)

---
Source: [Tesler's Law — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/teslers-law/)
