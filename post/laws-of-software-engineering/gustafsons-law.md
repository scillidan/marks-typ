# Gustafson's Law

**Definition:** With more parallel resources, we typically tackle bigger problems in the same time rather than finishing the same problem faster, so speedup scales with workload rather than being capped by the serial fraction.

**Category:** Scale

## Takeaways
- Extra compute usually gets spent on larger or richer problems, not on shaving time off the original one.
- It reframes Amdahl's pessimism: if the parallel portion of the workload grows with resources, speedup can remain close to linear.
- Favors "scale out" designs where work expands to fill the cluster.
- Explains why practitioners keep finding value in bigger hardware even when fixed-size benchmarks plateau.

## Why it matters
John Gustafson's 1988 rebuttal to Amdahl pointed out that real users rarely freeze the problem size. Give a scientist a bigger cluster and they run a higher-resolution simulation; give an analytics team more nodes and they ingest more data. The serial work stays roughly constant while the parallel work grows, so aggregate speedup keeps climbing.

This matters because a lot of modern infrastructure — MapReduce, Spark, GPU training, distributed rendering — is built on the implicit assumption that scope grows with capacity. Under that assumption, more machines genuinely translate into more useful output, which is exactly the bet cloud economics makes.

## Examples
- **Climate simulation:** Given a larger supercomputer, researchers do not rerun last year's model in less time; they increase grid resolution or ensemble size and produce a more accurate forecast in the same window.
- **Distributed analytics:** A 10-node cluster is typically pointed at 10x more data for the same hour-long batch, not the original dataset finished in six minutes.

## When to apply
Use Gustafson's framing when planning batch systems, data pipelines, training workloads, or any environment where problem scope is a dial the team can turn. It is the right mental model whenever you are arguing for horizontal scale-out and the expected payoff is "we can handle a bigger problem," not "we finish the current one faster." Pair it with Amdahl's Law to keep both ceilings — fixed-size and scaled — in view.

## Related laws
- [Amdahl's Law](./amdahls-law.md)
- [Metcalfe's Law](./metcalfes-law.md)
- [CAP Theorem](./cap-theorem.md)
- [Fallacies of Distributed Computing](./fallacies-distributed-computing.md)

---
Source: [Gustafson's Law — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/gustafsons-law/)
