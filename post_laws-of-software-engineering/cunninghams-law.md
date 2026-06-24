# Cunningham's Law

**Definition:** The fastest way to get a correct answer online isn't to ask a question — it's to post a confidently wrong one and let people correct you.

**Category:** Decisions

## Takeaways
- People are more motivated to fix a wrong claim than to help with an open question.
- A concrete proposal — even an imperfect one — attracts more useful feedback than an abstract ask.
- Turning a question into an assertion converts passive readers into active participants.
- Works on Stack Overflow, mailing lists, PRs, design docs, and team chat.

## Why it matters
"How should I do this?" often gets silence. "I solved it like this" gets ten people telling you why you're wrong — which is exactly the information you wanted. The asymmetry is real: correcting feels satisfying, helping feels like work.

In practice, this means proposing a concrete (if tentative) direction pulls better engagement than asking for guidance from scratch. Draft PRs, strawman design docs, and "I think we should do X — thoughts?" messages harness this. The willingness to be visibly wrong is the price of fast feedback.

## Examples
- **Open-source forum:** Someone stuck on a config issue posts "I solved it by setting ConfigMode=False." A maintainer shows up within minutes to correct them with the real fix — faster than the original question would have been answered.
- **Draft PR:** A junior opens a PR with an attempt at the feature rather than asking abstractly how to build it. Reviewers give specific, actionable feedback on the actual code, and the right solution emerges quickly.

## When to apply
Use this when you're stuck and abstract questions aren't getting traction — in public forums, internal chat, design reviews, and code reviews. Draft a best guess, publish it, and invite correction. Pair it with a clear "I'm not sure this is right, tell me what I'm missing" framing to keep the interaction collaborative.

Teams can also institutionalize the pattern: design docs with a proposed answer, draft PRs early, RFCs that take a position rather than enumerating options.

## Related laws
- [Linus's Law](./linus-law.md)
- [Broken Windows Theory](./broken-windows.md)
- [Hanlon's Razor](./hanlons-razor.md)

---
Source: [Cunningham's Law — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/cunninghams-law/)
