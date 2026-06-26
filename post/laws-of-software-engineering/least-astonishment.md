# Principle of Least Astonishment

**Definition:** Software and interfaces should behave the way users and developers expect — surprise is a design defect.

**Category:** Design

## Takeaways
- Align behavior with the mental model the user already has; counterintuitive behavior erodes trust even when nothing is technically broken.
- Follow platform conventions and domain norms before inventing new ones.
- Names, signatures, and side effects must agree: `isReady` is boolean, `compute` returns a value, `deleteFile` actually deletes.
- Applies everywhere a human touches the system: UIs, APIs, CLIs, configuration, error messages, and code structure.

## Why it matters
Also called the Rule of Least Surprise (Eric Raymond, *The Art of Unix Programming*), the principle traces back to 1967 PL/I documentation. The idea is simple: every surprise is a bug in the interface, whether or not the implementation is "correct."

Surprises compound. A function with a misleading name forces every reader to memorize the gotcha. An API that throws when users expect a return value shows up in production incidents long after the original author has moved on. Over time, astonishment accumulates into the feeling that the system is hostile.

The fix is humility about names and behavior: the intuitive reading of a method is part of its contract, and violating that reading costs more than getting it right the first time.

## Examples
- **API design:** A `parseDate()` function that silently changes a global locale breaks expectations — parsing should be pure. If it must have side effects, the name must say so.
- **User interfaces:** A "Save" button should persist immediately. If it queues the action or requires a second confirmation, users will lose data and trust.

## When to apply
Treat POLA as a first-class concern during API design, CLI design, UX review, and naming debates in code review. When proposing a new method, ask what a reader with no context would *assume* it does, and make the behavior match.

It's especially valuable at module boundaries and public interfaces, where consistency with surrounding conventions matters more than local cleverness.

## Related laws
- [Hyrum's Law](./hyrums-law.md)
- [Law of Demeter](./law-of-demeter.md)
- [KISS (Keep It Simple, Stupid)](./kiss.md)
- [Postel's Law](./postels-law.md)

---
Source: [Principle of Least Astonishment — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/principle-of-least-astonishment/)
