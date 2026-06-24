# Broken Windows Theory

**定义：** 小的不修复缺陷信号质量不重要，邀请进一步衰败。

**分类：** 质量

## 要点
- 可见的忽视——失败的测试、被忽略的警告、陈旧的TODO——使偷工减料正常化。
- 干净的代码库将贡献者拉向现有标准；混乱的代码库将他们拉下来。
- 及时修复小问题防止复合熵并减缓软件衰败。
- 质量是一个自我强化的反馈循环：纪律孕育纪律。

## 为何重要
由*The Pragmatic Programmer*从城市犯罪学借用，该理论认为一扇未修复的窗户会招致更多破窗。在软件中，"窗户"是没人修复的失败CI检查、用覆盖静音的lint错误、标记为`// temporary`的复制粘贴hack，以及没人敢删除的死代码。每个被容忍的缺陷降低下一个的成本。

相反，维护者及时修复小裂缝的代码库发送一个清晰信号：这里有标准。新贡献者镜像他们看到的东西，所以现有的精致水平往往在两个方向持续。防止衰败比逆转它便宜得多。

## 示例
- **用TODO腐烂：** 一个散落数月旧`TODO: fix this hack`评论的仓库教新人捷径是可接受的，更多hack被添加。
- **积极维护：** 一个维护者修复风格瑕疵并简化代码的项目设定了一个隐式标准；外部贡献到达时更接近那个标准。

## 何时应用
在代码审查期间应用此理论（不要让小问题"就这一次"滑过）、当入职代码库时（第一印象校准新贡献者）以及在事件后发现一个被忽略的小信号居然很重要时。在长期存在的系统上特别重要，那里复合熵是主导风险。

## 相关定律
- [Technical Debt](./technical-debt.md)
- [Boy Scout Rule](./boy-scout-rule.md)
- [Galls Law](./galls-law.md)

---
来源：[Broken Windows Theory - lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com/laws/broken-windows-theory/)