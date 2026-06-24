# YAGNI (You Aren't Gonna Need It)

**Definition:** Don't build functionality until a real requirement demands it.

**Category:** Design

## Takeaways
- Solve today's problem with today's code; defer hypothetical needs until they become real.
- Speculative features inflate complexity, maintenance cost, and onboarding time without proven value.
- YAGNI depends on the ability to refactor cheaply later, which in turn depends on good tests and CI.
- Prefer iterative delivery of minimal solutions over premature generalization or configurability.

## Why it matters
Guessing at future requirements is mostly wrong. The feature you pre-built either never arrives, arrives in a different shape, or arrives after the assumptions behind your scaffolding have shifted. Either way, you paid an up-front cost in complexity and got nothing back.

Every extra abstraction layer, option, or hook increases the surface that future engineers must read and reason about. YAGNI keeps that surface small by pushing design decisions to the moment when real information is available.

## Examples
- **Configuration flags:** You're about to add a toggle "in case someone wants the old behavior." If no one has asked, ship the concrete behavior and add the toggle the day a real user needs it.
- **Export formats:** A product needs JSON export. Skip the pluggable serialization framework with XML and YAML adapters; write the JSON writer.

## When to apply
Reach for YAGNI during design discussions, code review, and refactoring whenever someone justifies a change with "we might need..." or "later we could...". It's especially useful when negotiating scope on a story, drawing module boundaries, or deciding whether to introduce a new abstraction.

If you can't point to a current user, caller, or ticket that needs the code, treat it as speculative and defer it.

## Related laws
- [KISS (Keep It Simple, Stupid)](./kiss.md)
- [DRY (Don't Repeat Yourself)](./dry.md)
- [Premature Optimization](./premature-optimization.md)

---
Source: [YAGNI — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/yagni/)
