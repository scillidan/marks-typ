# Fallacies of Distributed Computing

**Definition:** A canonical list of eight false assumptions — starting with "the network is reliable" — that engineers unconsciously carry from local programming into distributed systems, where they cause failures.

**Category:** Architecture

## Takeaways
- Networks drop packets, add latency, have limited bandwidth, and aren't secure by default — code as if all of that is true.
- Treating a remote call like a local one produces chatty designs that collapse at scale.
- Defensive architecture means timeouts, retries with backoff, caching, redundancy, and graceful degradation.
- The fallacies work as a checklist: walk through each one during design review and ask how the system handles it.
- Topology and transport are not homogeneous — don't assume the network all looks the same.

## Why it matters
Originally articulated at Sun Microsystems in the mid-1990s (seven by L. Peter Deutsch, an eighth added by James Gosling), the Fallacies name the mental model mismatch that breaks distributed systems. Local function calls are fast, deterministic, in-process, and trusted. Remote calls are none of those things, yet engineers routinely write them as if they were.

The result is a predictable family of failures: chatty APIs that melt under real-world latency, retry storms that turn blips into outages, unencrypted internal traffic that becomes tomorrow's breach, configuration that silently assumes a single data center. Keeping the fallacies explicit forces these assumptions to be named and addressed instead of absorbed silently into the design.

## Examples
- **Zero-latency caching:** A service does a remote lookup per cache miss assuming the network is effectively free; in production the cache thrashes and tail latency explodes.
- **"The network is secure":** Internal microservices ship tokens and PII over unencrypted links on the assumption the LAN is trusted; a single compromise exposes everything in transit.

## When to apply
Bring the Fallacies into any design involving multiple services, regions, clusters, or clients over a network: RPC boundaries, message queues, replication, mobile sync, multi-cloud deployments, and integrations with third parties. They are especially useful during architecture review, incident postmortems (to name which fallacy bit), and when onboarding engineers who have only worked in-process.

## Related laws
- [CAP Theorem](./cap-theorem.md)
- [Murphy's Law](./murphys-law.md)
- [Law of Unintended Consequences](./unintended-consequences.md)

---
Source: [Fallacies of Distributed Computing — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/fallacies-of-distributed-computing/)
