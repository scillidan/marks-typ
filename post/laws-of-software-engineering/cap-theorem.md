# CAP Theorem

**Definition:** In a distributed system facing a network partition, you can have consistency or availability — not both — so partition tolerance forces a choice between the other two.

**Category:** Architecture

## Takeaways
- Partitions are a fact of real networks, so every serious distributed system is partition-tolerant by default.
- The real live trade-off during a partition is: return a possibly-stale answer, or refuse to answer at all.
- Different databases land on different sides — e.g. MongoDB leans CP, Cassandra leans AP.
- When the network is healthy, systems can look like they offer all three, which is why the trade-off only bites under failure.
- The theorem is a coarse but useful frame; real designs involve more nuanced consistency levels.

## Why it matters
CAP, proposed by Eric Brewer and formalized by Gilbert and Lynch, names a constraint that every distributed database designer has to take a position on. When a partition splits your cluster, you either stop serving the side that can't verify it has the latest data (favoring consistency), or you keep serving and accept that some clients may see divergent state (favoring availability). You cannot have both at the same time without a connected network.

The value of CAP is not that it dictates an answer but that it forces the question to be asked explicitly. Systems that pretend the trade-off doesn't exist tend to discover it during outages, when behavior is least predictable and stakes are highest.

## Examples
- **DNS (AP):** Resolvers keep answering queries during partitions, serving possibly-stale records rather than going dark — availability wins.
- **MongoDB vs. Cassandra:** MongoDB blocks writes when it can't talk to its primary (CP); Cassandra keeps accepting reads and writes from any replica and reconciles later (AP).

## When to apply
Reach for CAP whenever you're choosing or designing a distributed datastore, a replicated cache, a multi-region system, or any service where two nodes might disagree. It belongs in discussions about leader election, quorum sizing, read/write consistency levels, failover policy, and incident playbooks. It is also useful for setting expectations with product stakeholders about what happens when — not if — the network misbehaves.

## Related laws
- [Fallacies of Distributed Computing](./fallacies-distributed-computing.md)
- [Murphy's Law](./murphys-law.md)
- [Gall's Law](./galls-law.md)

---
Source: [CAP Theorem — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/cap-theorem/)
