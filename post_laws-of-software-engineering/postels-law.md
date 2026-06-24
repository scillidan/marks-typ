# Postel's Law

**Definition:** Be strict in what you send and lenient in what you accept.

**Category:** Quality

## Takeaways
- Emit output that adheres tightly to the spec so consumers can rely on it.
- Accept input graciously, tolerating harmless deviations where it is safe to do so.
- Balance tolerance against security: leniency must not become a vector for malformed or malicious data.
- Over-forgiving parsers can mask upstream bugs and entrench bad behavior as de facto protocol.
- The robustness principle helped make the early Internet interoperable across diverse implementations.

## Why it matters
Postel's Law, from Jon Postel's 1980 TCP spec, is why heterogeneous systems can actually talk. If every implementation rejected everything slightly off-spec, the Internet would have fragmented long ago. By producing strictly and consuming loosely, each component absorbs small incompatibilities rather than propagating them.

The modern caveat is that unlimited leniency has costs. When receivers always fix producers' mistakes, producers never learn - and the "real" protocol drifts toward whatever gets accepted (see Hyrum's Law). Security concerns tighten the balance further, since malformed input is a common attack surface.

## Examples
- **Web browsers:** HTML parsers aggressively repair malformed markup; strict parsing would break most of the web.
- **Email clients:** Mail readers render slightly non-conforming messages rather than rejecting them, preserving usability despite sloppy senders.

## When to apply
Invoke Postel's Law when designing APIs, protocols, and file formats that multiple independent parties will implement. Be more conservative when designing security boundaries, new greenfield protocols where you want strictness from day one, or formats where ambiguity has caused exploits.

## Related laws
- [Hyrum's Law](./hyrums-law.md)
- [Leaky Abstractions](./leaky-abstractions.md)
- [Fallacies of Distributed Computing](./fallacies-distributed-computing.md)

---
Source: [Postel's Law - lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/postels-law/)
