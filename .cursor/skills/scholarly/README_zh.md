# Scholarly - 学术论文写作助手

> 一个 AI Agent 技能，通过引导式问答帮助你逐步完成学术论文/学位论文的所有章节。

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-OpenClaw%20%7C%20Claude%20Code%20%7C%20Cursor%20%7C%20通用Agent-blue)](README.md)

## 什么是 Scholarly？

Scholarly 是一个 AI 驱动的学术写作助手，通过引导式对话帮助研究者、研究生和学者构建完整的学术论文。

不再面对空白文档，Scholarly 通过一系列针对性问题逐步引导你完成论文的每个部分——从摘要到引言、文献综述、方法、结果、讨论和结论。

## 核心功能

### 📝 逐章节引导开发
- 从标题和摘要开始
- 通过渐进式情境构建引言
- 进行系统的文献综述与 Gap 识别
- 详细描述方法以确保可复现性
- 使用规范的统计格式报告结果
- 与理论和实践意义对话讨论
- 用清晰的要点总结结论

### 📚 全面的写作指导
- 各章节的结构和模板
- 需要避免的常见错误
- 统计报告格式（APA 风格）
- 句式开头和过渡短语
- 学科特定注意事项

### 📖 涵盖的 11 个核心章节

| 章节 | 内容要点 |
|------|----------|
| Title | 关键词、简洁性、变量命名 |
| Abstract | 250词结构、过去/现在时态 |
| Introduction | 四层结构（背景→文献→Gap→目标） |
| Literature Review | 主题/时间/方法三种组织方式 |
| Methods | 参与者、设计、材料、程序、分析 |
| Results | 统计报告、表格vs图形选择 |
| Discussion | 解读、对话文献、局限、未来方向 |
| Conclusion | 核心takeaway、避免重复 |
| References | APA 7th 格式速查 |
| 学位论文 | 本科/硕士/博士要求 |

## 安装

### OpenClaw / WorkBuddy
```bash
cp -r scholarly ~/.workbuddy/skills/
```

### Claude Code
```bash
cp -r scholarly ~/.claude/skills/
```

### Cursor
```bash
cp -r scholarly ~/.cursor/skills/
```

## 使用方法

### 对话示例

> "我要写一篇心理学本科论文，研究社交媒体使用与焦虑的关系。"

> "帮我写一个关于机器学习在教育中应用的文献综述大纲。"

> "我在准备一个混合方法博士论文的方法部分，研究 ESL 学习者。"

## 支持的论文类型

| 类型 | 说明 |
|------|------|
| 课程论文 | 本科/研究生课程论文 |
| 期刊文章 | 同行评审发表 |
| 会议论文 | 学术会议投稿 |
| 本科论文 | 荣誉学位论文 |
| 硕士论文 | 研究生学位论文 |
| 博士论文 | 博士毕业论文 |
| 文献综述 | 独立综述文章 |

## 支持的研究设计

- **量化研究**：实验、调查、相关研究
- **质性研究**：访谈、民族志、案例研究
- **混合方法**：结合量化和质性方法
- **系统综述**：PRISMA 风格综合综述

## 文件结构

```
scholarly/
├── README.md                              # 本文件
├── README_en.md                           # 英文说明
├── SKILL.md                               # 技能定义
└── references/
    └── academic_paper_templates.md         # 各章节详细模板
```

## 引用格式

- APA 7th Edition
- MLA
- Chicago
- Harvard
- IEEE
- Vancouver

## 参考资源

基于以下最佳实践：
- APA Publication Manual (7th Edition)
- Purdue OWL (Online Writing Lab)
- UNC Writing Center
- UCSD Psychology Writing Resources

## 贡献

欢迎贡献！请自由：
- 添加学科特定模板（如化学、法律、医学）
- 改进章节模板
- 添加语言特定指南
- 报告问题或建议

## License

MIT License - 免费使用、修改和分发。

---

*Scholarly——让研究成型。*
