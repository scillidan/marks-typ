# SOLID Principles

**定义：** 五条面向对象设计准则——单一职责、开闭、里氏替换、接口隔离、依赖倒置——共同推动代码走向可维护性和可扩展性。

**分类：** 设计

## 要点
- **S**单一职责：每个类应该只有一个变更理由。
- **O**开闭：模块应对扩展开放、对修改关闭。
- **L**里氏替换：子类型必须能在其基类型期望的任何地方使用，且无意外。
- **I**接口隔离：宁愿几个小的、聚焦的接口，而非一个迫使客户端依赖它们不使用的方法的胖接口。
- **D**依赖倒置：依赖抽象而非具体实现，使高层策略不与低层细节耦合。

## 为何重要
一起应用时，SOLID产生变更保持局部的系统。强封装和松耦合意味着你可以重构、交换实现和添加功能，而无需担心破坏你没有看的代码。

这些原则是准则而非自然法则。机械地在到处应用所有五条会产生过度抽象的架构，充满单方法接口和间接层，不为任何真实调用者服务。目标是在正确位置放置接缝，而非最大仪式。

它们也使测试显著更容易：有单一工作且依赖表达为接口的类，微不足道地单独演练。

## 示例
- **单一职责：** 将一个臃肿的`UserManager`拆分成`UserValidator`、`UserRepository`、`EmailService`和一个协调它们的瘦`UserRegistrationService`。每块有自己的变更理由。
- **依赖倒置：** 一个通知服务依赖`INotificationChannel`接口。Email、SMS和伪造测试通道都实现它；服务代码永远不需要了解新的具体类型。

## 何时应用
在模块设计、类提取和重构期间调用SOLID——尤其是当一个类长得太大、一个地方的变更持续破坏另一个地方、或单元测试需要精心设置才能运行时。

在抢先应用它们时要克制。当你有第二个实现或测试痛点的证据时引入接口和接缝，而非在可能出现的概率上。

## 相关定律
- [Law of Demeter](./law-of-demeter.md)
- [Hyrum's Law](./hyrums-law.md)
- [DRY (Don't Repeat Yourself)](./dry.md)
- [KISS (Keep It Simple, Stupid)](./kiss.md)
- [YAGNI (You Aren't Gonna Need It)](./yagni.md)

---
来源：[SOLID Principles — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/solid-principles/)