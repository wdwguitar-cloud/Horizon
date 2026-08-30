---
layout: default
title: "Horizon Summary: 2026-08-30 (ZH)"
date: 2026-08-30
lang: zh
---

> 从 60 条内容中筛选出 6 条重要资讯。

---

**AI 创作者雷达**
1. [消息称 NocoBase 新增 DeepSeek V4 Flash 支持，尚未证实](#item-ai-creator-1) ⭐️ 5.0/10
2. [Archify：GitHub 趋势仓库，用 AI 智能体生成自包含 HTML 图表](#item-ai-creator-2) ⭐️ 5.0/10

**科技新闻**
1. [腾讯开源 Hy4 预览版 AI 模型](#item-tech-news-1) ⭐️ 8.0/10
2. [罗曼太空望远镜发射在即](#item-tech-news-2) ⭐️ 7.0/10
3. [美国国土安全部借罕见法律工具秘密调取记者等群体通信记录](#item-tech-news-3) ⭐️ 7.0/10
4. [谷歌新方法通过跟踪状态将智能体 token 用量减少 94%](#item-tech-news-4) ⭐️ 7.0/10

---

## AI 创作者雷达

<a id="item-ai-creator-1"></a>
### [消息称 NocoBase 新增 DeepSeek V4 Flash 支持，尚未证实](https://news.google.com/rss/articles/CBMiS0FVX3lxTE9ZWUYtU3h2RkFTSVpNLWR0QUdoVTg3aTZMM1N1a3YxZWJsbHB6UTYwalQzeGl3U2ZUZnBxUWNhclY5djdrZU5qdDV6dw?oc=5) ⭐️ 5.0/10

OSCHINA 发布的一条资讯标题称，开源无代码平台 NocoBase 新增 DeepSeek V4 Flash 支持，并具备推理续调与联网搜索能力。但目前仅有聚合标题，没有原始公告、具体版本号或功能说明可供核实，模型名称和能力描述均存疑。若消息属实，受影响的是在 NocoBase 上集成 AI 模型的开发者。

rss · AI 工具与效率产品 · 8月29日 09:01

**「内容角度」** 可做角度：从“NocoBase 疑似支持 DeepSeek V4 Flash”这一未经证实的消息出发，讨论开源无代码平台接入新模型时，开发者应如何核实官方发布与能力差异。

**标签**: `#DeepSeek V4 Flash`, `#NocoBase`, `#无代码平台`, `#AI 模型集成`, `#开源`

---

<a id="item-ai-creator-2"></a>
### [Archify：GitHub 趋势仓库，用 AI 智能体生成自包含 HTML 图表](https://github.com/tt-a1i/archify) ⭐️ 5.0/10

Archify 是一个正在 GitHub 上受到关注的仓库，提供一种 AI 智能体技能，用于生成架构图、工作流图、时序图、数据流图和生命周期图，输出为自带动效和可导出功能的自包含 HTML 文件。该仓库过去 24 小时新增 34 颗星、3 个 fork，主要语言为 HTML。目前其实际采用程度和技术价值仍未经过验证。

ossinsight · tt-a1i · 8月30日 02:52

**「为何值得注意」** 该仓库出现在 GitHub 趋势榜上，说明它在近期获得了一定关注；但这只是星标数量的小幅增长，尚未有证据表明它已产生广泛影响或形成成熟生态。

**「内容角度」** 可做角度：从“AI 智能体生成可验证图表”这一思路切入，探讨自包含 HTML 输出对技术文档工作流的潜在价值，同时说明目前仅处于早期关注阶段。

**标签**: `#AI diagrams`, `#agent skills`, `#GitHub trending`, `#HTML export`, `#developer tools`

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [腾讯开源 Hy4 预览版 AI 模型](https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/) ⭐️ 8.0/10

腾讯发布并开源了 Hy4 预览版，这是一个新的人工智能模型，发布后在 OpenRouter 上迅速获得大量使用，几天内处理了数万亿个 token。该模型首次参与了自身开发过程的自动化优化，包括训练方法、数据策略、评估框架和底层算子，形成了早期递归自我改进循环。Hy4 预览版相对便宜，缓存成本仅为 5%，而其他模型通常为 10%或 20%，因此对用户更具吸引力。作为预览版，Hy4 并非完全突破，但其技术新颖性和行业影响值得关注。

hackernews · shenli3514 · 8月29日 19:33 · [社区讨论](https://news.ycombinator.com/item?id=49492632)

**「背景」** Tencent Hy4 preview 是腾讯于 2026 年 8 月 28 日发布并开源的新一代大语言模型，总参数为 770B，活跃参数为 49B，上下文窗口超过 100 万 token。该模型已通过腾讯云、OpenRouter、腾讯产品及公开仓库等多个渠道提供，预览版表明其仍处于早期迭代阶段。了解这些基本参数和发布渠道，有助于理解其早期在 OpenRouter 上的高用量以及参与自身开发流程等特性。

**「影响」** Tencent Hy4 preview 已作为开源 MoE 模型在 OpenRouter 上提供，总参数 770B、激活参数 49B、上下文窗口超 1M token，并针对编码代理、复杂工具调用和生产力任务设计，因此开发者和提供此类场景服务的平台应评估其对现有模型选型与成本结构的影响。

**「社区讨论」** 社区开发者对 Hy4 预览版在 OpenRouter 上的惊人流量印象深刻，指出它几天内处理了数万亿个 token，超过 GLM 5.3 一周的使用量，且 5%的缓存成本使其更具性价比。另一些评论关注模型参与自身开发的递归自我改进循环，也有人质疑精简词表提高 token 密度是否会导致语义简化，还有人对发布图表的排序不当表示不满。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/">Tencent Releases and Open - Sources Tencent Hy 4 preview - Tencent</a></li>
<li><a href="https://www.testingcatalog.com/tencent-released-open-source-hy4-preview-model/">Tencent releases open - source Hy 4 preview model</a></li>
<li><a href="https://the-tech-trend.com/reviews/tencent-open-sources-hy4-preview/">Tencent Hy 4 : 770B Open - Source AI Model Launches</a></li>
<li><a href="https://openrouter.ai/tencent/hy4-preview">Hy 4 preview - API Pricing &amp; Providers | OpenRouter</a></li>
<li><a href="https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/">Tencent Releases and Open -Sources Tencent Hy 4 preview - Tencent</a></li>

</ul>
</details>

**标签**: `#AI`, `#open source`, `#language models`, `#Tencent`, `#model release`

---

<a id="item-tech-news-2"></a>
### [罗曼太空望远镜发射在即](https://science.nasa.gov/mission/roman-space-telescope/) ⭐️ 7.0/10

NASA 的南希·格雷斯·罗曼太空望远镜计划于 8 月 30 日搭载猎鹰重型火箭发射。该望远镜基于废弃的间谍卫星平台改造，专为大视场成像设计，其视野远大于哈勃望远镜。它每天将产生高达 1.4TB 的原始压缩数据，并计划在所有观测处理完成后立即完全公开，无任何禁运期。这为大规模数据处理、公民科学以及抢先发现新天体提供了独特机会。

hackernews · JumpCrisscross · 8月29日 15:48 · [社区讨论](https://news.ycombinator.com/item?id=49490870)

**「背景」** 南希·格雷斯·罗曼太空望远镜是 NASA 的一台红外太空望远镜，于 2025 年 11 月完成建造，计划于 2026 年 8 月 30 日发射至日地 L2 拉格朗日点，其主要科学目标是研究暗能量、系外行星和红外天体物理学。其主镜直径为 2.4 米，与哈勃太空望远镜相同，但专为广域巡天设计，视场远大于哈勃，这使其能够高效开展大范围天空调查。理解这些背景有助于把握该望远镜发射在天文观测和数据开放方面的重要意义。

**「影响」** 天文学家和数据爱好者将能免费访问每天 1.4TB 的公开数据，从而可能率先发现新星系或系外天体，并推动大规模数据处理工具的发展。

**「社区讨论」** 评论者普遍对完全开放的数据表示兴奋，认为罗曼望远镜的大视场能力远超哈勃；还有人指出其成本低于预期且进度超前，得益于间谍卫星改造，但有人质疑为何不建造备份望远镜以应对发射失败风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nancy_Grace_Roman_Space_Telescope">Nancy Grace Roman Space Telescope - Wikipedia</a></li>
<li><a href="https://science.nasa.gov/mission/roman-space-telescope/">Nancy Grace Roman Space Telescope - Science@NASA</a></li>
<li><a href="https://science.nasa.gov/mission/roman-space-telescope/introducing-the-roman-space-telescope/">About Roman - Science@NASA</a></li>

</ul>
</details>

**标签**: `#space telescope`, `#open data`, `#astronomy`, `#Falcon Heavy`, `#data science`

---

<a id="item-tech-news-3"></a>
### [美国国土安全部借罕见法律工具秘密调取记者等群体通信记录](https://www.theguardian.com/us-news/2026/aug/29/trump-dhs-1509-summons-records-journalists-nonprofits) ⭐️ 7.0/10

《卫报》2026 年 8 月 29 日报道，美国国土安全部（DHS）正借助一种鲜为人知的“1509 summons”法律工具，秘密调取记者、非营利组织和工会成员的电话及通信记录。报道称，T-Mobile 已配合交出记者 Fort 六个月的通话记录，涵盖超过 1 万通电话和短信；Fort 直到 7 月中旬才被告知，其律师称对此“震惊”。Google 则选择抵制相关传票。DHS 在被挑战后常主动撤回传票，以避免法院对其合法性作出裁决，法律边界因此仍不明确。此事凸显政府在监控和科技公司数据合规方面的权力争议。

hackernews · firefax · 8月29日 18:44 · [社区讨论](https://news.ycombinator.com/item?id=49492219)

**「背景」** 美国国土安全部（DHS）正在援引一项不太知名的海关法条款（19 USC 1509）来获取记者、非营利组织和工会的私人通信记录，该程序无需法官事先批准。此前在 2017 年，Twitter 曾就 DHS 试图利用 1509 传票识别一个批评 DHS 的账号@alt\_uscis 提起诉讼。例如，DHS 曾获取明尼阿波利斯记者 Georgia Fort 六个月的电话记录，包含超过 1 万通电话和短信，而未通知她本人。

**「影响」** 受影响群体的通信记录可能在毫无预警的情况下被政府获取，而科技公司在面对秘密传票时各自为政（T-Mobile 配合、Google 抵制），后续司法裁决将决定这一权力的边界。

**「社区讨论」** 评论者普遍批评 DHS 滥用权力，认为其通过撤诉规避司法审查，并点名 T-Mobile 等企业不配合就能避免执行。也有人将此与威权国家行为类比，建议记者自建去中心化通信工具（如 tmailplus），并质疑 DHS 预算（1000 亿美元）的使用效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/us-news/2026/aug/29/trump-dhs-1509-summons-records-journalists-nonprofits">Trump’s DHS is using an obscure law to secretly snoop on ...</a></li>
<li><a href="https://zeli.app/story/49492219">DHS uses obscure customs law to secretly spy on journalists ...</a></li>

</ul>
</details>

**标签**: `#privacy`, `#surveillance`, `#government policy`, `#law`, `#journalism`

---

<a id="item-tech-news-4"></a>
### [谷歌新方法通过跟踪状态将智能体 token 用量减少 94%](https://www.reddit.com/r/artificial/comments/1w1ynrf/google_paper_cuts_agent_token_usage_by_94_in_long/) ⭐️ 7.0/10

谷歌的一篇论文提出用结构化状态表示替代完整对话历史来驱动 AI 智能体。在 100 步基准测试中，SKILL.state 方法仅使用约 6.5 万 token 就达到 0.94 的准确率，而基于 LangGraph 风格的完整历史基线消耗约 110 万 token，准确率为 0.91，token 使用量降低约 94%。该方法让智能体在推理时把对后续步骤有用的信息写入状态，之后丢弃对话历史，使输入规模在整个会话中保持基本稳定；前提是智能体需预判未来所需信息，否则可能需重新检索。该消息来自 Reddit 摘要，且论文的 arXiv 编号（2608.26263）看起来异常，因此应谨慎看待这些结果。

reddit · r/artificial · /u/hakansan · 8月29日 21:31

**「背景」** 大型语言模型（LLM）在作为自主代理执行复杂、长期任务时，现有运行时通常会将观察结果、动作和中间推理过程不断追加到对话历史中，导致输入长度持续增长、延迟恶化，并可能在长程任务中引发上下文污染。SKILL.state 提出一种替代方案：用显式的结构化执行状态取代完整的历史记录，代理在推理时仅保留当前状态和最新观察，从而避免历史无限膨胀。论文在 100 步基准测试中展示了该方法的效率与准确性表现。

**「影响」** 对构建长会话 AI 智能体的开发者而言，这种方法有望大幅降低 token 成本，同时保持与完整历史基线相近的准确率，但实际效果取决于智能体对后续需求的前瞻能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.26263">[2608.26263] SKILL.state: Scalable Long-Horizon Agent Skills</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#token efficiency`, `#state management`, `#LLM`, `#Google research`

---