# Dunning-Kruger Effect

**Definition:** People with limited knowledge in a domain tend to overestimate their competence, while experts, aware of the domain's complexity, often underestimate theirs.

**Category:** Decisions

## Takeaways
- Loud confidence from someone new to an area often reflects a lack of context, not mastery.
- Learning tends to lower confidence before raising it as the learner discovers what they didn't know.
- Seasoned engineers hedge with ranges and trade-offs; novices give crisp, certain answers to messy questions.
- Impostor syndrome is the flip side: skilled people discount themselves because they see the complexity clearly.

## Why it matters
In software, overconfidence is expensive. A developer who has only touched a system for a week can earnestly promise a "quick fix" that turns into a multi-week incident, because they haven't yet discovered the failure modes experienced teammates already know.

Healthy teams counteract this by grounding decisions in evidence — code review, measurement, and peer challenge — instead of whoever sounds most sure. Self-assessment alone is unreliable; the very skills needed to judge work well are usually the ones being judged.

## Examples
- **Estimation gap:** A junior engineer confidently estimates two days for a migration; the senior who has done it before answers "it depends" and lists five things that could blow the timeline up.
- **Shiny tech:** The strongest advocates for adopting a brand-new framework are often the people who've used it least; practitioners who've shipped on it are more measured about its rough edges.

## When to apply
Reach for this during estimation, technology evaluation, architecture debates, and hiring loops — any moment where stated certainty is driving a decision. When someone (including you) feels totally sure, ask what evidence would change the view and whether the confidence is backed by scar tissue or just exposure.

It's also useful during postmortems: bad calls are frequently traceable to confident-but-uninformed voices being trusted over quieter, better-informed ones.

## Related laws
- [Hanlon's Razor](./hanlons-razor.md)
- [Confirmation Bias](./confirmation-bias.md)
- [First Principles Thinking](./first-principles.md)

---
Source: [Dunning-Kruger Effect — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/dunning-kruger-effect/)
