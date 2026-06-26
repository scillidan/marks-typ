# Murphy's Law / Sod's Law

**定义：** 任何可能出错的事情都会出错——往往在最糟糕的时刻。

**分类：** 质量

## 要点
- 边缘情况和故障模式最终在生产中发生；从一开始就为它们规划。
- 验证输入、处理异常、检查null，并优雅降级而非崩溃。
- 构建冗余、监控、回滚和值班，使故障是可存活的而非灾难性的。
- 测试"不可能"的场景——在规模上它们变成常规。

## 为何重要
软件以这样的规模和持续时间运行，罕见事件变得不可避免。百万分之一输入在足够大的系统中每天到达一千次，最糟糕的故障与发布、假期和演示相关——恰好是人类响应最少可用的时刻。

将Murphy's Law作为设计输入将努力转向防御性编程和运维韧性：输入验证、幂等性、断路器、带退避重试和深思熟虑的错误表面。目标不是防止每个故障而是确保故障是受限的、可观察的和可恢复的。

## 示例
- **无限制输入：** 一个没有字符限制的文本字段最终收到一个10,000字符的奇怪Unicodepayload，使后端崩溃。
- **最糟糕时刻故障：** 一个著名的Windows 98现场演示蓝屏——提醒关键系统在峰值可见度下失败除非加固。

## 何时应用
在设计审查期间（当每个依赖失败时会发生什么？）、事件复盘期间（什么无保护假设破裂了？）和测试策略期间（注入故障、模糊输入、演练超时）应用Murphy's Law。在发布、迁移和任何触及生产影响半径的变更前也至关重要。

## 相关定律
- [Hyrum's Law](./hyrums-law.md)
- [Fallacies of Distributed Computing](./fallacies-distributed-computing.md)
- [Confirmation Bias](./confirmation-bias.md)

---
来源：[Murphy's Law - lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/murphys-law/)