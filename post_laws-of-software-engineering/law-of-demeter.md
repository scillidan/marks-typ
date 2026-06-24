# Law of Demeter

**Definition:** An object should talk only to its immediate collaborators — never reach through them to operate on strangers.

**Category:** Design

## Takeaways
- A method should call methods on itself, its fields, its parameters, or objects it just created — nothing deeper.
- Long dotted chains like `a.getB().getC().doSomething()` are a visible symptom of the violation.
- Delegating methods ("tell, don't ask") keep internal structure hidden and callers insulated from refactors.
- Following the law shrinks each class's public surface and reduces ripple effects when internals change.

## Why it matters
Formulated by Ian Holland and colleagues at Northeastern around 1987, the Law of Demeter is the "principle of least knowledge": each object should know as little as possible about the shape of other objects.

When `OrderProcessor` digs through `order.getCustomer().getAddress().getZipCode()`, it's coupled not just to `Order` but to `Customer` and `Address` too. Refactor `Customer` to hold multiple addresses and `OrderProcessor` breaks — even though it never knowingly depended on Customer's internals.

By routing the call through a delegating method like `order.getShippingZip()`, the internal navigation stays inside `Order`, where it belongs. Callers keep working through structural changes; encapsulation does its job.

## Examples
- **UI presenter:** Instead of `view.getTextField().setText("Hello")`, expose `view.setUserMessage("Hello")`. Swap the `TextField` for a `Label` later and no presenter code changes.
- **E-commerce order:** Replace `order.getCustomer().getAddress().getCountry()` with `order.getShippingCountry()`. Address logic stays encapsulated and the caller is stable.

## When to apply
Flag Law of Demeter violations during code review, API design, and any refactor touching object relationships. Dotted chains crossing module boundaries are a strong smell — each extra dot is a new coupling.

It's also useful at class-design time: before exposing a getter, ask whether callers really need the nested object, or whether a delegating method on the parent would serve them better.

## Related laws
- [SOLID Principles](./solid-principles.md)
- [Law of Leaky Abstractions](./leaky-abstractions.md)
- [Hyrum's Law](./hyrums-law.md)
- [KISS (Keep It Simple, Stupid)](./kiss.md)

---
Source: [Law of Demeter — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/law-of-demeter/)
