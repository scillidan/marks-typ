# Metcalfe's Law

**Definition:** The value of a network grows roughly with the square of its number of connected users.

**Category:** Scale

## Takeaways
- Doubling the user base can roughly quadruple the number of possible pairwise connections, producing non-linear value growth.
- Each new participant raises utility for everyone already on the network, creating a self-reinforcing flywheel.
- Once a network passes a critical mass, winner-takes-most dynamics tend to lock in the leader.
- The curve runs both ways: when users leave, perceived value can collapse faster than it grew, producing a death spiral.

## Why it matters
Robert Metcalfe's observation was originally about Ethernet cards, but the pattern generalizes to any system where the point is connecting people or nodes. With 5 members a network has 10 possible pairwise links; with 12 members it has 66. Early on, each new user adds little, which is why new platforms feel empty. Past the tipping point, each new user unlocks many new interactions at once, which is why growth can suddenly look exponential.

The law is a simplification — not every pair of users actually interacts, and marginal value does eventually flatten — but it captures why communication platforms, marketplaces, and social products are so sensitive to early adoption and why the second-place network often cannot catch up.

## Examples
- **Messaging platforms:** WhatsApp and WeChat are near-useless with 50 users and near-essential once they saturate a country; the value comes from coverage, not features.
- **Platform decline:** As users abandon a social network, remaining users see fewer posts and replies, which accelerates more departures — the square law in reverse.

## When to apply
Invoke Metcalfe's Law when designing or evaluating any product whose core value is connecting participants: chat, social, marketplaces, developer platforms, federated protocols, internal collaboration tools. It should shape how you think about launch strategy (seeding dense pockets of users beats broad thin adoption), pricing (subsidize early users because they create value for later ones), and risk (watch for the inflection point where churn starts compounding).

## Related laws
- [Amdahl's Law](./amdahls-law.md)
- [Gustafson's Law](./gustafsons-law.md)
- [Conway's Law](./conways-law.md)
- [Reed's contribution via Dunbar's Number](./dunbars-number.md)

---
Source: [Metcalfe's Law — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/metcalfes-law/)
