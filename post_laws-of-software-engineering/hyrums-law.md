# Hyrum's Law

**Definition:** Once an API has enough users, every observable behavior of your system — documented or not — will become something someone depends on.

**Category:** Architecture

## Takeaways
- The implementation effectively becomes the interface once adoption is large enough.
- Quirks, bug side effects, timing characteristics, and error message text can all turn into de facto contracts.
- Any change, even one that respects the formal spec, can break real consumers.
- Informal UI conventions count too — users build habits around observable behavior.
- Maintainers have less freedom to refactor than the written contract suggests.

## Why it matters
The spec on paper is not the spec in practice. Given enough users, someone, somewhere, has written code that relies on a behavior the API owner never intended to guarantee — a specific ordering, an exact error string, a lucky side effect. That behavior is now load-bearing for them, and changing it is a breaking change whether the documentation admits it or not.

This blurs the boundary between "public contract" and "implementation detail" until the distinction barely exists. Teams that want to preserve freedom to evolve must anticipate this effect early, before a large dependent ecosystem calcifies around accidental behaviors.

## Examples
- **Windows backward compatibility:** Microsoft has repeatedly preserved undocumented quirks because third-party applications relied on them; fixing the bugs would break the apps.
- **"Unordered" iteration:** A library that documents results as unordered but happens to return them sorted will have callers depending on the sorting, so actually randomizing order later is a breaking change.

## When to apply
Think about Hyrum's Law whenever you ship or evolve an API, SDK, CLI flag, wire format, or public UI affordance. It should shape decisions about what to document as guaranteed vs. unspecified, whether to deliberately randomize or fuzz non-guaranteed outputs, and how much change-budget you reserve for future refactors. It is especially relevant at versioning boundaries, deprecations, and when choosing default behaviors that will be observed by many consumers.

## Related laws
- [The Law of Leaky Abstractions](./leaky-abstractions.md)
- [Law of Unintended Consequences](./unintended-consequences.md)
- [Gall's Law](./galls-law.md)

---
Source: [Hyrum's Law — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/hyrums-law/)
