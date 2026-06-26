# Murphy's Law / Sod's Law

**Definition:** Anything that can go wrong will go wrong - often at the worst possible moment.

**Category:** Quality

## Takeaways
- Edge cases and failure modes eventually occur in production; plan for them from the start.
- Validate inputs, handle exceptions, check nulls, and degrade gracefully rather than crash.
- Build redundancy, monitoring, rollback, and on-call so failures are survivable, not catastrophic.
- Test the "impossible" scenarios - at scale they become routine.

## Why it matters
Software runs at scales and for durations where rare events become inevitable. A one-in-a-million input arrives a thousand times a day in a big enough system, and the worst outages correlate with launches, holidays, and demos - exactly when humans are least available to respond.

Treating Murphy's Law as a design input shifts effort toward defensive programming and operational resilience: input validation, idempotency, circuit breakers, retries with backoff, and thoughtful error surfaces. The goal is not to prevent every failure but to ensure failures are bounded, observable, and recoverable.

## Examples
- **Unbounded input:** A text field without a character limit eventually receives a 10,000-character payload of weird Unicode that crashes the backend.
- **Worst-time failure:** A live demo of Windows 98 famously blue-screened on stage - a reminder that critical systems fail at peak visibility unless hardened.

## When to apply
Apply Murphy's Law during design reviews (what happens when each dependency fails?), incident postmortems (what unguarded assumption broke?), and test strategy (inject faults, fuzz inputs, exercise timeouts). It is also vital before launches, migrations, and any change that touches production's blast radius.

## Related laws
- [Hyrum's Law](./hyrums-law.md)
- [Fallacies of Distributed Computing](./fallacies-distributed-computing.md)
- [Confirmation Bias](./confirmation-bias.md)

---
Source: [Murphy's Law - lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/murphys-law/)
