# Zawinski's Law

**Definition:** Every program keeps accreting features until it can read mail — software tends inexorably toward bloat.

**Category:** Architecture

## Takeaways
- Feature creep is the default trajectory, not an exception.
- Successful apps attract pressure to become platforms — once users live inside them, every adjacent capability gets proposed.
- Each new feature dilutes the core value proposition and raises maintenance cost.
- Saying "no" is a first-class product skill; without it, focus erodes silently.
- A focused competitor can win purely by not expanding.

## Why it matters
Jamie Zawinski's quip captures an observed gravity in software: once a program is useful enough that people spend time in it, there's constant pressure — from users, from PMs, from adjacent teams — to add "just one more" capability. Individually each request is reasonable; collectively they transform a sharp tool into a sprawling suite. The original users who loved the focus often leave for whatever new, smaller thing does their one job well.

This is an architectural concern as much as a product one. Every added capability touches the data model, the build, the test surface, the security footprint, and the mental model new users have to acquire. The cost compounds, and the moment a focused alternative appears, the bloated incumbent is exposed.

## Examples
- **Netscape to Communicator:** A lean browser grew to bundle mail, news, and composer, becoming slow and complicated — opening the door for Firefox, which won on focus and speed.
- **Slack:** Started as team messaging, then absorbed voice, video, file sharing, bots, workflow automation, and integrations, in pursuit of being the everything-app for work.

## When to apply
Keep Zawinski's Law in mind during roadmap planning, feature prioritization, and architecture reviews for any successful product. It's especially relevant when proposals start with "while we're in there, we could also…" or when stakeholders want your product to absorb a neighboring one. Use it to defend scope, justify deprecations, and push back on platformization that doesn't serve the core use case.

## Related laws
- [Second-System Effect](./second-system-effect.md)
- [YAGNI](./yagni.md)
- [KISS](./kiss.md)
- [Gall's Law](./galls-law.md)

---
Source: [Zawinski's Law — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/zawinskis-law/)
