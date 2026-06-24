# Principle of Least Astonishment

**定义：** 软件和接口应该以用户和开发者期望的方式表现——惊讶是设计缺陷。

**分类：** 设计

## 要点
- 将行为与用户已经拥有的心智模型对齐；反直觉行为侵蚀信任，即使技术上没有破坏任何东西。
- 在发明新约定之前遵循平台惯例和领域规范。
- 名称、签名和副作用必须一致：`isReady`是布尔值，`compute`返回值，`deleteFile`实际删除。
- 应用于人类触及系统的任何地方：UI、API、CLI、配置、错误消息和代码结构。

## 为何重要
也称为最小惊讶规则（Eric Raymond，*The Art of Unix Programming*），这个原则可追溯到1967年的PL/I文档。想法简单：每个惊讶都是接口中的bug，无论实现是否"正确"。

惊讶会复合。一个具有误导性名称的函数迫使每个读者记住这个陷阱。一个当用户期望返回值时抛出的API在生产事件中显现，早已在原作者离开后。随着时间推移，惊讶累积成系统感觉充满敌意的感觉。

修复在于对名称和行为的谦逊：方法的直觉阅读是其契约的一部分，违反该阅读比第一次就做对的成本更高。

## 示例
- **API设计：** 一个默默改变全局locale的`parseDate()`函数破坏预期——解析应该是纯的。如果它必须有副作用，名称必须说明。
- **用户界面：** 一个"保存"按钮应该立即持久化。如果它排队操作或需要第二次确认，用户将丢失数据和信任。

## 何时应用
在API设计、CLI设计、UX审查和代码审查的命名辩论期间将POLA视为一等关注点。当提议一个新方法时，问一个没有上下文的读者会*假设*它做什么，并使行为匹配。

在模块边界和公共接口处特别有价值，在那里与周围惯例的一致性比局部聪明更重要。

## 相关定律
- [Hyrum's Law](./hyrums-law.md)
- [Law of Demeter](./law-of-demeter.md)
- [KISS (Keep It Simple, Stupid)](./kiss.md)
- [Postel's Law](./postels-law.md)

---
来源：[Principle of Least Astonishment — lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/principle-of-least-astonishment/)