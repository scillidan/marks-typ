# The Map Is Not the Territory

**Definition:** Models, diagrams, and documents are abstractions of reality — useful guides, but never the real system running in production.

**Category:** Decisions

## Takeaways
- Architecture diagrams and specs describe intent; the running system is what actually behaves.
- Every model leaves things out — "all models are wrong, but some are useful."
- Expect surprises during implementation; your plan didn't know about them.
- When evidence from the real system contradicts the model, trust the system and update the model.
- Agile's short feedback loops are a direct response to this gap.

## Why it matters
Engineers love clean diagrams, and a pristine architecture doc can feel like the system is already real. It isn't. Latency assumptions break, queue backpressure shows up where no one drew it, a "reliable" network drops packets, data distributions don't match expectations. These aren't model failures in principle — they're the inevitable gap between representation and reality.

Teams get in trouble when they trust the map over the territory. The cure is continuous contact with the real system: measurement, profiling, staged rollouts, chaos testing, and a willingness to revise the diagram when production disagrees with it.

## Examples
- **Microservices on paper:** A clean diagram shows Service A calling B and C over Kafka, "low latency, reliable." In production you need retries, idempotency keys, schema evolution, and timeouts — all invisible on the whiteboard.
- **Benchmark vs. reality:** A database spec promises 10k QPS. Under real workload it delivers 5k because the access patterns and hotspots don't match the benchmark's assumptions.

## When to apply
Use this lens during architecture reviews, capacity planning, migrations, and incident debriefs. Whenever someone says "the design says X," ask what the production data says. When a diagram and reality disagree, the diagram is wrong.

It's especially useful before committing to a big bet based on an untested model — prefer a small real-world probe over an elaborate plan.

## Related laws
- [Leaky Abstractions](./leaky-abstractions.md)
- [Gall's Law](./galls-law.md)
- [Goodhart's Law](./goodharts-law.md)
- [Hofstadter's Law](./hofstadters-law.md)

---
Source: [The Map Is Not the Territory — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/map-is-not-the-territory/)
