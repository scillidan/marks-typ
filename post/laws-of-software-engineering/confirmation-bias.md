# Confirmation Bias

**Definition:** The unconscious tendency to notice and weight information that supports what you already believe, while discounting evidence that doesn't.

**Category:** Decisions

## Takeaways
- Once you form a hypothesis, you'll start seeing evidence for it everywhere — including where it isn't.
- Ask "what would I expect to see if I'm wrong?" before deciding you're right.
- In group decisions, assign someone to argue the opposing case; silence is not agreement.
- Ground calls in objective signals (tests, metrics, A/B results) rather than gut preference.

## Why it matters
In debugging, confirmation bias is a time-sink: once you're sure the bug lives in module A, you read module A's code carefully and glance at module B — so if the bug actually lives in B, you'll miss it for hours. The same dynamic shows up in code review, architecture debates, and postmortems.

The antidote isn't pure skepticism — it's deliberate disconfirmation. Before acting on a belief, state what evidence would falsify it, and go look for that evidence specifically. Teams that do this catch bad hypotheses early, before they harden into consensus.

## Examples
- **Biased code review:** Reviewing a trusted colleague's PR, you skim and approve. Reviewing a junior's PR with the same patterns, you nitpick. The code didn't change — your expectations did.
- **Happy-path testing:** Developers write tests that exercise the scenarios they already expect to work. The bugs live in the cases they didn't think to test — which is exactly why adversarial or "try to break it" test writing finds more issues.

## When to apply
Use this during debugging (especially when stuck), design reviews, postmortems, hiring decisions, and any "should we adopt X?" discussion. Whenever you notice you're only citing evidence that supports one side, deliberately go search for the other side.

Particularly important in incident analysis: the first plausible cause is often not the real cause, and confirmation bias will tempt you to stop investigating once you find something that "explains it."

## Related laws
- [Dunning-Kruger Effect](./dunning-kruger.md)
- [Hanlon's Razor](./hanlons-razor.md)
- [Inversion](./inversion.md)
- [Goodhart's Law](./goodharts-law.md)

---
Source: [Confirmation Bias — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/confirmation-bias/)
