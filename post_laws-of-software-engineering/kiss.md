# KISS (Keep It Simple, Stupid)

**Definition:** Designs and systems should be as simple as the requirements allow — no simpler, and definitely no more elaborate.

**Category:** Design

## Takeaways
- Simpler designs are faster to understand, easier to debug, and cheaper to change.
- Every extra line of code is another place where bugs can hide, so brevity has real value.
- "Clever" solutions that optimize for hypothetical future problems usually hurt present clarity.
- When two designs both meet the requirements, choose the shorter, duller one.

## Why it matters
Software is written for humans at least as much as for machines. If a teammate can't read a module and predict what it does, the module is a liability — no matter how impressive its architecture. KISS treats cognitive load as a first-class cost.

Simple code also localizes failure. When something breaks, straightforward control flow shortens the path from symptom to root cause. Clever abstractions do the opposite: they scatter behavior across indirections and force debuggers to reconstruct the author's mental model before making any progress.

## Examples
- **Reporting script:** For a small CSV export, query the database and write rows with a standard library. Don't invent a plugin-based report engine to serve one report.
- **File parser:** A straightforward sequential reader with explicit error handling beats a generic parser-combinator framework when the input format is fixed and small.

## When to apply
Invoke KISS at design time, during code review, and whenever you catch yourself building for "what if." It's particularly relevant when choosing between architectures, deciding how many layers a feature needs, or spotting gold-plating in a pull request.

A good prompt: "Is the simplest thing that could possibly work sufficient here?" If yes, ship that, and add complexity only when a real constraint forces it.

## Related laws
- [YAGNI (You Aren't Gonna Need It)](./yagni.md)
- [Principle of Least Astonishment](./least-astonishment.md)
- [Gall's Law](./galls-law.md)
- [DRY (Don't Repeat Yourself)](./dry.md)

---
Source: [KISS — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/kiss-principle/)
