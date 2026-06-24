# Linus's Law

**Definition:** Given enough eyeballs, all bugs are shallow - broad review surfaces defects quickly.

**Category:** Quality

## Takeaways
- The more competent reviewers look at code, the faster obscure bugs surface and get fixed.
- Open-source projects benefit most because the pool of potential reviewers is largest.
- Visibility alone is not enough; the community must actually be engaged and empowered.
- Pair programming and internal code review apply the same idea at team scale.
- Heartbleed and the xz backdoor show that "many eyes" can still miss issues without sustained attention.

## Why it matters
Named for Linus Torvalds and popularized by Eric Raymond, the law captures why releasing early and often to a large community works. A bug that confounds one developer is often obvious to another with different domain knowledge or tooling. Distributed attention effectively parallelizes debugging.

The modern counterpoint is that "eyes" must be *engaged* eyes. A published repo with no real reviewers is not reviewed. This is why funded maintenance, paid reviewers for critical infrastructure, and deliberate pairing all matter - they convert theoretical visibility into actual scrutiny.

## Examples
- **Apache HTTP Server:** A massive user and contributor base means vulnerabilities tend to get spotted and patched quickly after disclosure.
- **Closed enterprise product:** A system seen only by one vendor and a handful of customers can harbor subtle bugs for years because almost nobody is looking.

## When to apply
Apply Linus's Law when choosing between open and closed source for non-differentiating components, designing code-review processes, setting up pair or mob programming, and staffing reviewers for security-sensitive code. It also argues for investing in readable code so more eyes can meaningfully engage.

## Related laws
- [Brooks's Law](./brooks-law.md)
- [Sturgeon's Law](./sturgeons-law.md)
- [Bus Factor](./bus-factor.md)

---
Source: [Linus's Law - lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/linuss-law/)
