# Pesticide Paradox

**Definition:** Repeatedly running the same tests finds fewer and fewer new bugs over time.

**Category:** Quality

## Takeaways
- A static test suite grows less effective as the software it guards evolves.
- Passing tests prove the code still works against old hypotheses, not against new risks.
- Finding new defects requires new tests: altered inputs, new features covered, fresh scenarios.
- Exploratory testing complements regression testing by probing where scripted tests can't reach.
- Audit your test suite after each release and fill the gaps revealed.

## Why it matters
The name borrows from agriculture: keep spraying the same pesticide and pests evolve resistance. A test suite's "resistance" builds the same way - once a scenario has been fixed, rerunning that exact test yields nothing new. Meanwhile the codebase grows in directions the old suite never covered.

This does not make regression testing useless; catching regressions is the point. But counting on "all green" to mean "no bugs" is a mistake. Healthy quality practice treats the test suite as a living artifact that must grow alongside the product, and pairs it with exploratory testing to probe the unknown.

## Examples
- **Stale coverage:** A mobile team's suite covers login and profile. Messaging ships, inherits no new tests, and bugs reach users despite a green CI - the untested region was invisible.
- **Cycle repeats:** After adding messaging tests, defects drop there - until the next feature ships. Each new area needs its own wave of fresh tests.

## When to apply
Apply this lens when "all tests pass but bugs still escape," when designing test strategy for a rapidly growing product, when planning exploratory testing sessions, and during retrospectives on incidents that slipped past a green build. Pair it with coverage analysis to spot undertested regions.

## Related laws
- [Testing Pyramid](./testing-pyramid.md)
- [Lehman's Laws of Software Evolution](./lehmans-laws.md)
- [Goodhart's Law](./goodharts-law.md)

---
Source: [Pesticide Paradox - lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/pesticide-paradox/)
