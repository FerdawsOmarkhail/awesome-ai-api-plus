# 🚀 Awesome AI API Plus（中文）

> 面向开发者增长的 AI API 精选清单。  
> 与传统 awesome list 的差异：不只罗列工具，而是按 **接入效率、商业可用性、性价比、稳定性、SEO 潜力** 给出可执行选型框架。

[English](./README.md) | 中文

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./.github/ISSUE_TEMPLATE/tool_submission.md)
[![CI](https://img.shields.io/badge/CI-passing-brightgreen.svg)](./.github/workflows/ci.yml)

---

## 目录

- [项目定位与差异化](#项目定位与差异化)
- [趋势榜单（2026 Q1）](#趋势榜单2026-q1)
- [评分模型](#评分模型)
- [首发 30 条 API 清单](#首发-30-条-api-清单)
- [Top 10 推荐榜](#top-10-推荐榜)
- [分类导航](#分类导航)
- [快速开始](#快速开始)
- [投稿墙与贡献方式](#投稿墙与贡献方式)
- [更新日志](#更新日志)

---

## 项目定位与差异化

`Awesome-AITools` 强在覆盖广度；本项目聚焦“可落地增长”：

- **API 优先**：优先有 API 文档、SDK、可运行样例的项目
- **增长优先**：提供关键词包、GitHub topics、仓库命名建议
- **商业优先**：关注价格模型与生产可用性
- **行动优先**：内置脚本，可快速跑出评分和关键词分组

灵感来源（对标项目）：[Awesome-AITools](https://github.com/ikaijua/Awesome-AITools)

---

## 趋势榜单（2026 Q1）

> 基于开发者讨论热度、搜索趋势和生态活跃度的观察性榜单（非官方统计）。

| 领域 | 趋势关键词 | 代表 API/平台 |
|---|---|---|
| 视频生成 | text-to-video、image-to-video | Sora、KLING、Runway、Dreamina |
| 音乐生成 | text-to-music、ai audio | Suno、Udio、Stable Audio |
| 多模型网关 | openai-compatible、routing | OpenRouter、OmniRoute |
| Agent Infra | observability、benchmark | Helicone、LiveCodeBench、LMSYS Arena |

---

## 评分模型

每个条目按 0-100 评分：

`总分 = 30% 接入效率 + 25% 输出质量 + 20% 性价比 + 15% 稳定性 + 10% SEO 潜力`

### 评分维度定义

- **接入效率**：文档质量、SDK 完整度、示例可运行性
- **输出质量**：模型效果一致性、生成可用度
- **性价比**：成本与性能比
- **稳定性**：可用性、限流表现、接口稳定
- **SEO 潜力**：相关关键词搜索热度与可抢占空间

---

## 首发 30 条 API 清单

- Markdown 清单：[`docs/launch-30-apis.md`](./docs/launch-30-apis.md)
- CSV 数据集：[`data/apis-launch-30.csv`](./data/apis-launch-30.csv)
- 模板文件：[`data/apis-template.csv`](./data/apis-template.csv)

---

## Top 10 推荐榜

- 结果文档：[`docs/top-10-recommended.md`](./docs/top-10-recommended.md)
- 生成脚本：[`examples/python/generate_top10.py`](./examples/python/generate_top10.py)

---

## 分类导航

- [视频生成 API](./docs/categories/video-generation.md)
- [音乐与音频 API](./docs/categories/music-audio.md)
- [多模态与 LLM API](./docs/categories/multimodal-llm.md)
- [Agent 与基础设施 API](./docs/categories/agent-infra.md)

---

## 快速开始

### 1) 跑评分示例

```bash
python ./examples/python/score_tools.py
```

### 2) 跑关键词分组

```bash
node ./examples/nodejs/keyword_cluster.js
```

### 3) 生成 Top 10 榜单

```bash
python ./examples/python/generate_top10.py
```

### 4) 新增条目

编辑 [`data/apis-template.csv`](./data/apis-template.csv)，或按 Issue 模板提交：

- [Tool Submission](./.github/ISSUE_TEMPLATE/tool_submission.md)
- [SEO Request](./.github/ISSUE_TEMPLATE/seo_request.md)

---

## 投稿墙与贡献方式

欢迎提交 API/工具，推荐格式：

- 工具名称 + 主页链接
- 类别（video/music/llm/infra）
- 收费模式（free/free-paid/paid）
- 一句话使用场景
- 文档链接（优先）

你可以通过以下方式参与：

- 提交 Issue：`Tool Submission`
- 提交 PR：直接修改 `data/apis-template.csv` 或分类文档

---

## 更新日志

### 2026-03-21

- 新增中文主文档（`README-CN.md`）
- 新增首发 30 条 API 清单（Markdown + CSV）
- 分类页替换为真实 API 链接
- 新增 Top 10 自动生成脚本与结果文档

---

## License

[MIT](./LICENSE)

