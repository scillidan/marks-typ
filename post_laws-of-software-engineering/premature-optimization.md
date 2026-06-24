# Premature Optimization (Knuth's Optimization Principle)

**Definition:** Investing effort to optimize code before measuring where the real performance bottlenecks live tends to waste time, add complexity, and hurt readability.

**Category:** Planning

## Takeaways
- The vast majority of code is not performance-critical, so optimizing everywhere buys little while costing a lot.
- Roughly 97% of micro-optimizations should be skipped in favor of clear design and correct behavior.
- Optimization tends to add complexity, so applying it early compounds maintenance cost for minimal gain.
- A safe order of operations: make it work, then make it right, then (if measurements demand it) make it fast.

## Why it matters
Performance and simplicity usually pull in opposite directions. When engineers chase speed before they know where the real cost lives, they typically trade clarity for theoretical gains in code paths that barely run. The well-known 80/20 observation applies: a small fraction of the code accounts for most of the runtime, so effort spent outside that fraction is largely decorative.

Writing for readability first leaves the system easy to profile, easy to change, and easy to reason about. Once profiling reveals actual hot spots, you can invest complexity precisely where it pays back, and nowhere else. That discipline keeps both performance work and long-term maintenance under control.

## Examples
- **Startup-only speedup:** A developer spends two days hand-tuning bit-twiddling in C, only to discover the function executes once at boot and accounts for roughly 0.001% of runtime.
- **Wrong data structure for the job:** Reaching for an elaborate logarithmic data structure for "future scale" when a straightforward linear search would comfortably handle the data sizes actually observed.

## When to apply
Invoke this law during design reviews, code review, and whenever someone proposes rewriting something "for performance." Before approving optimization work, ask for profile data that names the bottleneck and a predicted improvement. During planning and estimation, resist including speculative performance stories that have no measurement behind them.

It is equally useful as a check on yourself: if you are about to introduce cleverness for speed, confirm the hot path is real before you pay the readability tax.

## Related laws
- [YAGNI](./yagni.md)
- [Hofstadter's Law](./hofstadters-law.md)
- [Gall's Law](./galls-law.md)
- [Kernighan's Law](./kernighans-law.md)
- [Amdahl's Law](./amdahls-law.md)

---
Source: [Premature Optimization (Knuth's Optimization Principle) - lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/premature-optimization/)
