# Postel's Law

**定义：** 在发送上要严格，在接收上要宽容。

**分类：** 质量

## 要点
- 发出紧密遵循规范的输出，让消费者可以依赖它。
- 宽容接受输入，在安全的情况下容忍无害偏差。
- 平衡宽容与安全：宽容不得成为畸形或恶意数据的向量。
- 过度宽容的解析器可能掩盖上游bug并将坏行为固化为事实协议。
- 坚健原则帮助早期互联网跨多样化实现互操作。

## 为何重要
Postel's Law，来自Jon Postel的1980 TCP规范，是异构系统实际能对话的原因。如果每个实现都拒绝所有稍微偏离规范的东西，互联网早就碎片化了。通过严格产出和宽松消费，每个组件吸收小的兼容性问题而非传播它们。

现代警告是无限制宽容有成本。当接收者总是修复生产者的错误时，生产者从不学习——而且"真实"协议漂移到任何被接受的东西（见Hyrum's Law）。安全顾虑进一步收紧平衡，因为畸形输入是常见的攻击面。

## 示例
- **Web浏览器：** HTML解析器积极修复畸形标记；严格解析会破坏大部分web。
- **邮件客户端：** 邮件阅读器渲染稍微不符合规范的消息而非拒绝它们，尽管发送者粗糙仍保持可用性。

## 何时应用
在设计多个独立方将实现的API、协议和文件格式时调用Postel's Law。在设计安全边界、你希望从一开始严格的新绿地协议、或歧义已导致利用的格式时更保守。

## 相关定律
- [Hyrum's Law](./hyrums-law.md)
- [Leaky Abstractions](./leaky-abstractions.md)
- [Fallacies of Distributed Computing](./fallacies-distributed-computing.md)

---
来源：[Postel's Law - lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/postels-law/)