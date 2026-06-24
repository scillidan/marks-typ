# Hanlon's Razor

**Definition:** Don't attribute to malice what is sufficiently explained by ignorance, carelessness, or honest mistakes.

**Category:** Decisions

## Takeaways
- When something goes wrong, assume human error before assuming bad intent.
- Favor simple explanations (typos, misconfigurations, missed cases) over conspiracy theories.
- Approach surprising code with curiosity; people usually had a reason, even a wrong one.
- Save "malicious actor" as a hypothesis for genuine security contexts, not everyday bugs.
- Blameless culture in incident response depends on this mindset.

## Why it matters
Most "WTF" moments in a codebase or incident turn out to be boring: someone was tired, someone didn't know, someone pasted the wrong value. Teams that jump straight to blame burn trust and miss the real root cause, because they stop investigating once they've found a villain.

Hanlon's Razor keeps investigation honest. It doesn't say malice never happens — it says the probability mass sits firmly on "oops." Incident reviews that assume good faith tend to surface systemic gaps (missing guardrails, unclear docs) that finger-pointing obscures.

## Examples
- **"They deleted my data":** A customer is convinced someone inside the company wiped their account. The real cause is a delete path that misbehaves when a name field is empty — pure bug, no villain.
- **Traffic spike:** Before declaring a DDoS, check whether a misconfigured client is retrying in a tight loop. Most "attacks" are actually friendly fire.

## When to apply
Use this during incident response, production debugging, postmortems, and code review. Whenever you catch yourself narrating "who did this to us," pause and list the mundane explanations first — config drift, stale cache, a silent deploy, an untested edge case.

It also applies to reading other people's code. Before rewriting something that looks "obviously wrong," ask what constraint the original author might have been solving for.

## Related laws
- [Occam's Razor](./occams-razor.md)
- [Confirmation Bias](./confirmation-bias.md)
- [Dunning-Kruger Effect](./dunning-kruger.md)

---
Source: [Hanlon's Razor — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/hanlons-razor/)
