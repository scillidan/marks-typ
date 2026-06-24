# Law of Demeter

**定义：** 一个对象应该只与它的直接协作者交谈——永远不要穿过它们操作陌生人。

**分类：** 设计

## 要点
- 一个方法应该调用自己、自己的字段、自己的参数或它刚创建的对象上的方法——不更深。
- 像`a.getB().getC().doSomething()`这样的长点链是违反的可见症状。
- 委托方法（"告诉，别问"）保持内部结构隐藏，保护调用者免受重构影响。
- 遵循这条定律缩小每个类的公共表面并减少内部变更时的涟漪效应。

## 为何重要
由Ian Holland和同事于1987年左右在东北大学提出，Law of Demeter是"最少知识原则"：每个对象应该尽可能少地了解其他对象的形状。

当`OrderProcessor`深入`order.getCustomer().getAddress().getZipCode()`时，它不仅与`Order`耦合，也与`Customer`和`Address`耦合。重构`Customer`以持有多个地址会破坏`OrderProcessor`——即使它从未有意依赖Customer的内部。

通过像`order.getShippingZip()`这样的委托方法路由调用，内部导航留在`Order`内部，那里它属于。调用者通过结构变更继续工作；封装完成其工作。

## 示例
- **UI呈现器：** 不用`view.getTextField().setText("Hello")`，暴露`view.setUserMessage("Hello")`。稍后将`TextField`换成`Label`，无需呈现器代码变更。
- **电商订单：** 用`order.getShippingCountry()`替换`order.getCustomer().getAddress().getCountry()`。地址逻辑保持封装，调用者稳定。

## 何时应用
在代码审查、API设计和任何触及对象关系的重构期间标记Law of Demeter违规。跨越模块边界的点链是一个强烈气味——每个额外的点是一个新耦合。

在类设计时也有用：在暴露getter之前，问调用者是否真的需要嵌套对象，或父类上的委托方法是否更好地服务它们。

## 相关定律
- [SOLID Principles](./solid-principles.md)
- [Law of Leaky Abstractions](./leaky-abstractions.md)
- [Hyrum's Law](./hyrums-law.md)
- [KISS (Keep It Simple, Stupid)](./kiss.md)

---
来源：[Law of Demeter — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/law-of-demeter/)