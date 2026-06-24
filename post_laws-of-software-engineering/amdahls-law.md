# Amdahl's Law

**Definition:** The maximum speedup from parallelizing a system is capped by the portion of work that must remain sequential.

**Category:** Scale

## Takeaways
- The serial fraction of a workload sets a hard ceiling on achievable speedup, no matter how many workers you add.
- Throwing more hardware (or people) at a problem surfaces existing bottlenecks rather than removing them.
- Fix sequential chokepoints first; parallelize second.
- Bottlenecks are not only technical — a single approver, reviewer, or shared service can serialize an entire organization.

## Why it matters
Gene Amdahl published this observation in 1967 while arguing about processor design. The math is stark: if 10% of a task is inherently sequential, the best you can ever do is a 10x speedup, even with infinite processors. Most of the cores you pay for will sit idle waiting on the serial portion.

The idea travels well beyond CPUs. Any system whose critical path flows through a single component — a shared database, an auth service, a release manager — obeys the same ceiling. Adding capacity everywhere else is wasted spend until the serial segment shrinks.

That is why performance work so often starts with profiling to find the one slow step, and why org scaling work starts with finding the one human everything routes through.

## Examples
- **Single-database web app:** Spinning up more application servers barely moves latency when every request funnels through one Postgres primary that is already saturated.
- **Microservices with a shared dependency:** Splitting a monolith into services does not help throughput if each request still serializes through a central billing or authentication service.

## When to apply
Reach for Amdahl's Law whenever you are considering horizontal scaling, adding parallel workers, or evaluating whether more hardware will help. Use it during capacity planning, performance tuning, and any "we'll just add more replicas" conversation. It is also useful when auditing organizational throughput: map the critical path and look for the one step that everything else waits on.

## Related laws
- [Gustafson's Law](./gustafsons-law.md)
- [Metcalfe's Law](./metcalfes-law.md)
- [Brooks's Law](./brooks-law.md)
- [CAP Theorem](./cap-theorem.md)

---
Source: [Amdahl's Law — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/amdahls-law/)
