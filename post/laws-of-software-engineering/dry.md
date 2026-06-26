# DRY (Don't Repeat Yourself)

**Definition:** Every piece of knowledge in a system should have one single, unambiguous, authoritative representation.

**Category:** Design

## Takeaways
- Duplicated logic is duplicated maintenance; one change in requirements should require one change in code.
- Target duplicated *intent*, not just duplicated *text* — code that looks alike but means different things should stay separate.
- DRY applies beyond source code: schemas, tests, build configs, and documentation all suffer from knowledge duplication.
- Centralize shared rules into functions, modules, or config files so consumers reference one source of truth.

## Why it matters
When the same rule lives in five places, every change becomes a hunt. Miss one site and the system silently disagrees with itself — the kind of bug that ships to production and embarrasses the team months later.

Consolidating knowledge into one place also makes the system easier to reason about. Readers learn a rule once instead of inferring it from repeated-but-subtly-different copies.

The trap is premature consolidation. Two snippets that happen to look alike today may diverge tomorrow because they model different concepts. Merging them creates a brittle abstraction that serves neither caller well.

## Examples
- **Configuration:** Instead of hardcoding the database URL in every service file, put it in one config and import it. Rotating a host becomes a one-line change.
- **Formatting helpers:** When several screens format dates the same way, extract a shared `formatDate()` helper. The format lives in one spot and evolves coherently.

## When to apply
Look for DRY violations during code review, when writing a new feature that echoes an existing one, or when a bug fix requires editing the same logic in multiple files. Those repeated edits are the clearest signal.

Resist applying DRY during the very first appearance of a pattern. Wait for the second or third instance so you can see the real shape of the abstraction before committing to it.

## Related laws
- [SOLID Principles](./solid-principles.md)
- [Law of Demeter](./law-of-demeter.md)
- [KISS (Keep It Simple, Stupid)](./kiss.md)
- [YAGNI (You Aren't Gonna Need It)](./yagni.md)

---
Source: [DRY — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/dry-principle/)
