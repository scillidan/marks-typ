# SOLID Principles

**Definition:** Five object-oriented design guidelines — Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion — that together push code toward maintainability and extensibility.

**Category:** Design

## Takeaways
- **S**ingle Responsibility: each class should have one reason to change.
- **O**pen/Closed: modules should be open to extension but closed to modification.
- **L**iskov Substitution: subtypes must be usable anywhere their base type is expected, without surprises.
- **I**nterface Segregation: prefer several small, focused interfaces over one fat one that forces clients to depend on methods they don't use.
- **D**ependency Inversion: depend on abstractions, not concretions, so high-level policy isn't coupled to low-level detail.

## Why it matters
Applied together, SOLID produces systems where changes stay local. Strong encapsulation and loose coupling mean you can refactor, swap implementations, and add features without fear of shattering code you weren't looking at.

The principles are guidelines, not laws of nature. Mechanically applying all five everywhere yields over-abstracted architectures full of one-method interfaces and indirection layers that serve no real caller. The goal is well-placed seams, not maximum ceremony.

They also make testing dramatically easier: classes with one job and dependencies expressed as interfaces are trivial to exercise in isolation.

## Examples
- **Single Responsibility:** Split a bloated `UserManager` into `UserValidator`, `UserRepository`, `EmailService`, and a thin `UserRegistrationService` that coordinates them. Each piece has its own reason to change.
- **Dependency Inversion:** A notification service depends on an `INotificationChannel` interface. Email, SMS, and a fake test channel all implement it; the service code never needs to learn a new concrete type.

## When to apply
Reach for SOLID during module design, class extraction, and refactoring — especially when a class has grown too large, a change in one place keeps breaking another, or a unit test needs an elaborate setup to run.

Be restrained when applying them preemptively. Introduce interfaces and seams when you have evidence of a second implementation or a testing pain point, not on the chance one might appear.

## Related laws
- [Law of Demeter](./law-of-demeter.md)
- [Hyrum's Law](./hyrums-law.md)
- [DRY (Don't Repeat Yourself)](./dry.md)
- [KISS (Keep It Simple, Stupid)](./kiss.md)
- [YAGNI (You Aren't Gonna Need It)](./yagni.md)

---
Source: [SOLID Principles — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/solid-principles/)
