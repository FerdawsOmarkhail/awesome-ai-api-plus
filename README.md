# 🚀 Awesome AI API Plus

> A growth-first, API-first curated list for AI builders.  
> Different from generic awesome lists: we rank tools by **integration speed**, **commercial readiness**, **cost efficiency**, and **developer ROI**.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./.github/ISSUE_TEMPLATE/tool_submission.md)
[![CI](https://img.shields.io/badge/CI-passing-brightgreen.svg)](./.github/workflows/ci.yml)

[English](./README.md) | [中文](./README-CN.md)

---

## Why this is different

Most awesome lists focus on breadth.  
`awesome-ai-api-plus` focuses on **what helps developers ship and grow faster**:

- **API-centric**: prioritize tools with clear API docs and SDK quality
- **Growth-centric**: include SEO and distribution keyword packs
- **Business-centric**: evaluate pricing model and production viability
- **Actionable**: provide scripts and templates you can run immediately

Reference inspiration: [Awesome-AITools](https://github.com/ikaijua/Awesome-AITools)

---

## Core scoring model (differentiator)

Each entry is scored 0-100:

`Score = 30% Integration + 25% Output Quality + 20% Price Efficiency + 15% Reliability + 10% SEO Potential`

### Scoring dimensions

- **Integration**: API clarity, SDK support, sample availability
- **Output Quality**: model quality and consistency
- **Price Efficiency**: cost vs performance
- **Reliability**: uptime, rate-limit behavior, response stability
- **SEO Potential**: search demand for tool/category keywords

---

## Categories

- [Video Generation APIs](./docs/categories/video-generation.md)
- [Music & Audio APIs](./docs/categories/music-audio.md)
- [Multimodal / LLM APIs](./docs/categories/multimodal-llm.md)
- [Agent & Infra APIs](./docs/categories/agent-infra.md)
- [Launch 30 APIs](./docs/launch-30-apis.md)
- [Top 10 Recommended APIs](./docs/top-10-recommended.md)

---

## Repository structure

```text
awesome-ai-api-plus/
├─ README.md
├─ data/
│  └─ apis-template.csv
├─ docs/
│  └─ categories/
│     ├─ video-generation.md
│     ├─ music-audio.md
│     ├─ multimodal-llm.md
│     └─ agent-infra.md
├─ seo/
│  ├─ keywords.md
│  └─ github-topics.txt
├─ examples/
│  ├─ README.md
│  ├─ python/score_tools.py
│  └─ nodejs/keyword_cluster.js
└─ .github/
   ├─ workflows/ci.yml
   └─ ISSUE_TEMPLATE/
      ├─ tool_submission.md
      └─ seo_request.md
```

---

## SEO pack included

- Keyword clusters by intent: informational / transactional / comparison
- Ready-to-use GitHub topics
- Repo naming suggestions for long-tail capture

See: [`seo/keywords.md`](./seo/keywords.md) and [`seo/github-topics.txt`](./seo/github-topics.txt)

---

## Quick start

### 1) Score candidate tools

```bash
python ./examples/python/score_tools.py
```

### 2) Build keyword clusters

```bash
node ./examples/nodejs/keyword_cluster.js
```

### 3) Add your first tool entry

Use the template in [`data/apis-template.csv`](./data/apis-template.csv), then submit via issue template.

### 4) Use launch dataset directly

- CSV: [`data/apis-launch-30.csv`](./data/apis-launch-30.csv)
- Markdown: [`docs/launch-30-apis.md`](./docs/launch-30-apis.md)

### 5) Generate Top 10 list

```bash
python ./examples/python/generate_top10.py
```

---

## Submission standard

To be accepted, a tool should include:

- Public docs or API reference
- Clear pricing (or transparent free tier)
- One runnable example
- At least one real-world use case

---

## Roadmap

- [ ] Auto-generate category pages from CSV
- [ ] Add monthly trend report for top APIs
- [ ] Add benchmark scripts for latency/cost snapshots
- [ ] Add Chinese and English mirrored index pages

---

## License

[MIT](./LICENSE)

