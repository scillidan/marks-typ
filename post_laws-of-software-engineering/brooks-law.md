# Brooks's Law

**Definition:** Throwing more people at a software project that is already behind schedule will tend to push it further behind, not pull it forward.

**Category:** Teams

## Takeaways
- Ramp-up cost for new hires is paid out of the existing team's productivity budget.
- Communication paths grow roughly quadratically with team size, so coordination tax scales fast.
- Scope cuts and timeline negotiations usually beat staffing up as a response to slippage.
- Some work — deep debugging, architectural decisions — simply cannot be parallelized.
- "Man-months" is a misleading unit because human effort on knowledge work is not fungible.

## Why it matters
Fred Brooks noticed on IBM's OS/360 project that the intuitive manager move — add bodies when a project is late — often made things worse. New engineers need context, pair time, and code review attention, all of which come from the very people who are already behind.

On top of that, each new person adds new communication edges to the team graph. A team of three has three pairwise channels; a team of ten has forty-five. Past a point, the coordination load dwarfs the marginal output any new hire can provide.

## Examples
- **Late-stage reinforcements:** A 5-person team is a month late; management adds 3 more. The originals spend weeks onboarding them, merge conflicts multiply, and the project slips to two months late instead of recovering.
- **Solo-debuggable bug:** A gnarly production bug requires deep knowledge of a subsystem that only one engineer understands. Adding three more debuggers just generates noise — the bottleneck is irreducible.

## When to apply
Reach for Brooks's Law whenever someone proposes adding headcount to rescue a slipping deadline. Use it to push the conversation toward the alternatives: cutting scope, shipping in phases, freezing requirements, or accepting the slip. Also invoke it during hiring planning — a team that has doubled in six months is often less productive than it was at half the size.

In postmortems, check whether schedule pressure drove a mid-project staffing decision that made things worse; that pattern is worth naming explicitly so the org stops repeating it.

## Related laws
- [Conway's Law](./conways-law.md)
- [Second-System Effect](./second-system-effect.md)
- [Unintended Consequences](./unintended-consequences.md)
- [Ringelmann Effect](./ringelmann-effect.md)

---
Source: [Brooks's Law — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/brooks-law/)
