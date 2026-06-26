# Occam's Razor

**Definition:** When multiple explanations or designs fit the facts, the simplest one is usually correct — or at least the best starting point.

**Category:** Decisions

## Takeaways
- Simple code has fewer moving parts, which means fewer places to break and fewer things to understand later.
- When debugging, check the boring explanations (typo, wrong env, missing flag) before reaching for exotic theories.
- Every extra service, dependency, or abstraction should justify its own weight.
- "As simple as possible, but no simpler" — don't over-prune essential complexity either.

## Why it matters
Software has a gravitational pull toward complexity: layers get added, edge cases sprout special-case handling, architectures fragment. Occam's Razor is a counter-weight — a prompt to ask whether the next layer is earning its keep, or just making the system feel sophisticated.

In debugging, the principle saves hours. The first hypothesis should be the mundane one. Compiler bugs and cosmic rays are possible, but the odds say you forgot to save the file, deployed the wrong branch, or pointed at staging.

## Examples
- **Debugging a broken build:** It's tempting to blame a dependency upgrade or a flaky CI runner. Nine times out of ten, the cause is a trailing comma, an env var that wasn't set, or a merge conflict someone resolved wrong.
- **Architecture:** A team splits a working monolith into six microservices "for scale." The new distributed system has its own failure modes, coordination overhead, and deploy complexity — all without any real load problem to justify it.

## When to apply
Reach for Occam's Razor during debugging, architecture reviews, tech selection, and design discussions. Whenever a proposal involves adding something — a service, a queue, a framework, an abstraction — ask what breaks if you don't add it. If the answer is "nothing yet," that's a signal.

It's also useful in incident triage: start with the simplest hypothesis consistent with the symptoms and only escalate to complex theories once the simple ones are ruled out.

## Related laws
- [KISS](./kiss.md)
- [YAGNI](./yagni.md)
- [Gall's Law](./galls-law.md)
- [Hanlon's Razor](./hanlons-razor.md)

---
Source: [Occam's Razor — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/occams-razor/)
