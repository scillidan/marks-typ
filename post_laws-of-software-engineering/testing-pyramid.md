# Testing Pyramid

**Definition:** A healthy test suite has many fast unit tests, fewer integration tests, and a thin top layer of end-to-end tests.

**Category:** Quality

## Takeaways
- Unit tests are the foundation: fast, isolated, cheap to run, and plentiful.
- Integration tests verify module boundaries; keep them fewer than unit tests.
- End-to-end tests cover critical user journeys but are slow and brittle - use sparingly.
- The pyramid shape gives fast feedback and catches most bugs at the cheapest layer.
- An inverted pyramid (mostly UI tests) produces slow CI, flakiness, and weak diagnostics.

## Why it matters
Tests differ wildly in cost. A unit test runs in milliseconds, pinpoints a failure to a function, and rarely flakes. An end-to-end test can take minutes, depend on browsers and networks, and fail for dozens of unrelated reasons. Putting most of your testing budget at the cheap layer keeps feedback fast and causes clear.

When teams invert the pyramid - often because unit testing feels less "real" - CI slows, flakes pile up, and distinguishing real regressions from noise becomes a daily tax. Restoring the pyramid tends to be one of the highest-leverage changes a struggling test suite can make.

## Examples
- **Healthy e-commerce suite:** Hundreds of unit tests for pricing and validation, dozens of integration tests for order workflows, a handful of end-to-end tests for checkout and login. CI finishes in minutes.
- **Inverted anti-pattern:** A team with sparse unit coverage runs 50 nightly Selenium tests. Failures arrive a day late, and half of them turn out to be flakes, not bugs.

## When to apply
Apply the pyramid when designing a new test strategy, auditing an existing slow CI pipeline, scoping a testing investment for leadership, or diagnosing why production regressions keep escaping review. It's especially valuable on teams where CI time has become a drag on delivery.

## Related laws
- [Pesticide Paradox](./pesticide-paradox.md)
- [Lehman's Laws of Software Evolution](./lehmans-laws.md)
- [Murphy's Law](./murphys-law.md)

---
Source: [Testing Pyramid - lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/testing-pyramid/)
