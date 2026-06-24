# Law of Unintended Consequences

**Definition:** Any change to a complex system will produce effects you didn't predict — some helpful, some harmful, and some that actively worsen the problem you were trying to solve.

**Category:** Architecture

## Takeaways
- Complex systems have dense interdependencies, so changes rarely stay local.
- Outcomes fall into three flavors: unexpected wins, unexpected costs, and perverse results that make the original problem worse.
- In software, fixes and features routinely trigger regressions in unrelated modules.
- Your mental model of the system is always partial — plan for surprises, don't pretend they won't happen.
- Planning and review help, but "unknown unknowns" can't be fully eliminated.

## Why it matters
This law is a reminder that engineers work with incomplete models of the systems they change. A UI simplification quietly doubles backend load. A "small" refactor breaks a downstream consumer. A fix for one bug exposes another that was being masked by it. These aren't failures of diligence — they're a structural feature of complex, interconnected systems.

The practical implication is humility in how changes are shipped. Gradual rollouts, feature flags, canaries, observability, and reversible deployments exist precisely because we know, in advance, that not every consequence was foreseen. The question isn't whether surprises will happen, but how fast you'll notice and how cheaply you can back out.

## Examples
- **Logging that crashes prod:** A new debug-logging feature is added to improve observability; it fills the disk and brings down the service it was meant to help diagnose.
- **Fix breaks dependents:** A module's bug is silently being relied on elsewhere (see Hyrum's Law); fixing it correctly causes a regression in the unrelated module that had adapted to the wrong behavior.

## When to apply
Invoke this law on any change that touches a system with real users or real integrations — migrations, refactors, protocol changes, infra upgrades, policy or rate-limit changes, ML model swaps, UI overhauls. Use it to justify canarying, staged rollout, feature flags, rollback plans, and monitoring for second-order metrics (not just the thing you tried to change). It's also a useful mindset during postmortems to look beyond the triggering change to the interactions it exposed.

## Related laws
- [Hyrum's Law](./hyrums-law.md)
- [Murphy's Law](./murphys-law.md)
- [Gall's Law](./galls-law.md)
- [Goodhart's Law](./goodharts-law.md)

---
Source: [Law of Unintended Consequences — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/law-of-unintended-consequences/)
