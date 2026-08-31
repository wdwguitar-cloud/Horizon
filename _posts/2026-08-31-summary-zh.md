---
layout: default
title: "Horizon Summary: 2026-08-31 (ZH)"
date: 2026-08-31
lang: zh
---

> 从 68 条内容中筛选出 8 条重要资讯。

---

**AI 创作者雷达**
1. [用户发现：未发送的 ChatGPT 图片仍存入图像库](#item-ai-creator-1) ⭐️ 6.0/10
2. [开源新项目 Click：以 Hook 代替 Prompt 强制执行 AI 编程工作流](#item-ai-creator-2) ⭐️ 5.0/10
3. [LLM 用单画笔工具画钟：一次社区演示揭示的空间推理局限](#item-ai-creator-3) ⭐️ 5.0/10
4. [tt-a1i/archify：24 小时获 41 星的自包含 HTML 图表 agent skill](#item-ai-creator-4) ⭐️ 5.0/10

**科技新闻**
1. [QubesOS 发布 QSB-118：copy-to-VM 错误上报路径存在任意代码执行漏洞](#item-tech-news-1) ⭐️ 8.0/10
2. [ChatGPT Work 解析：云与本地两个版本及其核心功能](#item-tech-news-2) ⭐️ 8.0/10
3. [地球上水面和陆地上最长直线路径的算法验证（2018）](#item-tech-news-3) ⭐️ 7.0/10
4. [亚马逊关闭 Mechanical Turk：AI 取代了训练它的人类](#item-tech-news-4) ⭐️ 7.0/10

---

## AI 创作者雷达

<a id="item-ai-creator-1"></a>
### [用户发现：未发送的 ChatGPT 图片仍存入图像库](https://www.reddit.com/r/ChatGPT/comments/1w2xf19/warning_check_your_image_library_often/) ⭐️ 6.0/10

一位自称每天使用 ChatGPT Plus 的用户发帖提醒：在聊天中选择过的图片即使最后未发送，也可能被保存在 ChatGPT 的图像库中；删除聊天记录也不会删除该聊天上传过的图片，需要用户在图像库中手动删除。该说法来自个人经验，尚未获得 OpenAI 官方确认，具体保存逻辑和适用范围不明。

reddit · r/ChatGPT · /u/LiveYourDaydreams · 8月30日 23:54

**「内容角度」** 可做角度：从“删除聊天不等于删除图片”这一用户发现出发，整理 ChatGPT 图像库中图片的保存与删除逻辑，提示用户定期手动检查；需注明这是用户经验分享，未经官方证实。

**标签**: `#ChatGPT`, `#privacy`, `#data management`, `#image library`, `#user tip`

---

<a id="item-ai-creator-2"></a>
### [开源新项目 Click：以 Hook 代替 Prompt 强制执行 AI 编程工作流](https://news.google.com/rss/articles/CBMiakFVX3lxTE5VLTBlWlhnb0hYYklsdGxoeDBfNTFRTDVxdEkwOVVyblV1a21EZkM2ZXVrcTNjX1FpZFowZ0R1SDR5MnZ5NVg1M1B2dWVQMzhwQzRrX1BCMGJ3c1BPQlZ6eW5OdEE5M1lUWEE?oc=5) ⭐️ 5.0/10

据 80aj.com 报道，一个名为 Click 的开源新项目提出以 Hook 代替 Prompt 来强制执行 AI 编程工作流。目前仅有标题与聚合链接，未提供原始仓库、技术细节或实际应用证据，因此无法确认其具体机制、成熟度与影响范围。该信息适合作为待核实的项目线索，而非已成型的结论。

rss · AI 工具与效率产品 · 8月31日 00:11

**「为何此刻值得注意」** 在 AI 编程工具普遍依赖 Prompt 引导的背景下，Click 提出的“Hook 代替 Prompt”思路具有概念上的新鲜感，可能指向更强制、更可控的工作流执行方式。但目前这仅是标题层面的新项目信息，尚无证据表明它已经落地或被社区验证，需谨慎对待。

**「可做内容角度」** 可做角度：先核实 Click 项目是否存在及其实装方式，再围绕“强制 Hook 与自然语言 Prompt 在 AI 编程工作流中的适用边界”展开对比讨论，而不是直接断言哪种方式更优。

**标签**: `#AI编程`, `#开源项目`, `#Hook`, `#Prompt`, `#工作流`

---

<a id="item-ai-creator-3"></a>
### [LLM 用单画笔工具画钟：一次社区演示揭示的空间推理局限](https://www.reddit.com/r/ChatGPT/comments/1w2ixmi/llms_attempting_to_draw_a_clock/) ⭐️ 5.0/10

Reddit 用户 /u/SeesawGullible398 发布了一个演示：让多个 LLM 用一把画笔工具画钟。它们只能设置画笔的大小、颜色和硬度，并通过一次调用把画笔移动到指定位置。帖子以此展示这类模型当前在简单图形绘制上的空间推理局限。该观察来自社区帖子，尚未看到系统评测或更多验证数据。

reddit · r/ChatGPT · /u/SeesawGullible398 · 8月30日 14:23

**「为什么现在值得注意」** 在大模型多模态能力讨论较多的背景下，这类社区演示提供了一个可直接观察的边界案例；但该帖子只是单个演示，不能据此推断模型在真实任务中的整体表现。

**「内容角度」** 可做角度：围绕“单次调用只能把画笔移动到一个位置”这一限制，说明这类演示如何呈现大模型的空间推理短板，并提醒读者这只是单一社区案例，不能等同于严格评测。

**标签**: `#LLM`, `#multimodal`, `#tool use`, `#AI limitations`, `#demo`

---

<a id="item-ai-creator-4"></a>
### [tt-a1i/archify：24 小时获 41 星的自包含 HTML 图表 agent skill](https://github.com/tt-a1i/archify) ⭐️ 5.0/10

GitHub 趋势仓库 tt-a1i/archify 在近 24 小时获得 41 颗星、1 个 fork 和 1 个 pull request，项目语言为 HTML。据仓库介绍，它提供一种 agent skill，用于生成漂亮且可验证的架构、工作流、时序、数据流和生命周期图；输出为自包含 HTML，带有动态效果和干净导出。该仓库定位面向使用 AI agent 生成图表的开发者，但目前缺少发布公告、版本细节和广泛使用证据。

ossinsight · tt-a1i · 8月31日 02:45

**「为什么现在值得注意」** 该仓库出现在 GitHub 趋势榜中，24 小时内星际增量 41，表明它在图表生成或 agent 技能方向获得初步关注。不过这一热度能否转化为实际采用或生态影响，目前没有更多证据支撑。

**「内容角度」** 可做角度：以 archify 为例，观察“agent skill 生成自包含 HTML 图表”这一功能点，讨论它与传统绘图工具/库的差异，以及“自包含 HTML + 可验证”在 AI 生成内容场景中的潜在价值。

**标签**: `#GitHub`, `#diagrams`, `#HTML`, `#agent skill`, `#visualization`

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [QubesOS 发布 QSB-118：copy-to-VM 错误上报路径存在任意代码执行漏洞](https://www.qubes-os.org/news/2026/08/29/qsb-118/) ⭐️ 8.0/10

QubesOS 发布了安全公告 QSB-118，披露了一个位于 copy-to-VM 错误上报回通道中的任意代码执行漏洞。该漏洞影响 Dom0 版本的 qvm-copy-to-vm，因为其错误报告函数使用了 system\(\)，从而可能执行任意代码。VM 版本不受影响，因为该版本的错误报告函数不使用 system\(\)。由于 Dom0 是 QubesOS 中权限最高的域，该漏洞一旦被利用可能危及整个系统。公告提醒用户注意该漏洞仅在从 Dom0 执行 copy-to-VM 操作时触发。

hackernews · vntok · 8月30日 08:51 · [社区讨论](https://news.ycombinator.com/item?id=49496918)

**「背景」** Qubes OS 是一款以安全为核心、通过 Xen 虚拟机将不同任务隔离到独立域的 Linux 发行版，其中 Dom0 是负责管理的可信域，官方建议不要在 Dom0 中进行日常操作。qvm-copy-to-vm 用于向其他虚拟机复制文件；从 Dom0 发起复制时，其错误报告函数使用 system\(\) 调用处理错误信息，导致攻击者可以通过构造特殊错误内容在 Dom0 中执行任意代码。QSB-118 是 Qubes OS 项目针对此漏洞发布的安全公告，说明了该 Dom0 任意代码执行问题的详情与修复方式；从普通虚拟机发起的复制路径不受影响。

**「影响」** 对于从 Dom0 执行 copy-to-VM 操作的用户，该漏洞可能导致攻击者在最高权限域 Dom0 中执行任意代码，从而完全控制系统。

**「社区讨论」** 评论认为该漏洞虽然严重，但实际触发条件是从 Dom0 进行 copy-to-VM，而 VM 变体不受影响；另有讨论将 QubesOS 的安全模型、图形硬件加速限制与 BSD jail 等方案进行比较。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.qubes-os.org/news/2026/08/29/qsb-118/">QSB-118: Dom0 arbitrary code execution in qvm-copy-to-vm error reporting | Qubes OS</a></li>
<li><a href="https://forum.qubes-os.org/t/qubes-users-qsb-118-dom0-arbitrary-code-execution-in-qvm-copy-to-vm-error-reporting/43108">[qubes-users] QSB-118: Dom0 arbitrary code execution in qvm-copy-to-vm error reporting - qubes-users - Qubes OS Forum</a></li>
<li><a href="https://news.ycombinator.com/item?id=49496918">Arbitrary code execution in QubesOS via copy-to-VM error reporting backchannel | Hacker News</a></li>

</ul>
</details>

**标签**: `#security`, `#qubesos`, `#vulnerability`, `#arbitrary-code-execution`, `#operating-systems`

---

<a id="item-tech-news-2"></a>
### [ChatGPT Work 解析：云与本地两个版本及其核心功能](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/) ⭐️ 8.0/10

OpenAI 于 7 月 9 日发布 ChatGPT Work，并在其后持续迭代。Simon Willison 指出它实际上是两个产品：云端版（Work Cloud）与桌面应用版（Work Local，由原 Codex 改名而来）。目前仅面向每月 20 美元及以上订阅者，免费用户和 8 美元 Go 用户无法使用。Work Cloud 提供 GPT-5.6 Sol/Luna/Terra 和 GPT-5.5 模型选择，支持联网代码执行、无头 Chrome 浏览器、持久共享文件系统、发布 ChatGPT Sites、子代理与定时自动化。其中最引人注目的是代码执行环境可访问互联网（默认开放全部域名，也可配置白名单），浏览器工具可让用户代为输入密码和 2FA，且能通过 Playwright 执行 JavaScript。

rss · Simon Willison · 8月30日 23:59

**「背景」** ChatGPT Work 是 OpenAI 在 ChatGPT 基础上推出的面向任务完成的产品，与普通 Chat 问答模式相区别。OpenAI 官方建议在需要明确产出物（如简报、演示文稿、分析、定期更新、工作流或文件）时使用 Work，而日常问答仍用 Chat。此前 Codex 是面向开发者的编程代理，现被重塑为更平易近人的 Work Local。

**「影响」** 对每月 20 美元及以上的订阅者，Work Cloud 首次让 ChatGPT 能端到端执行需要联网的真实任务（如克隆仓库、安装依赖、操作网站），显著扩展了此前 Chat 代码解释器只能访问受限容器代理的能力边界。

**标签**: `#ChatGPT`, `#OpenAI`, `#AI tools`, `#software engineering`, `#product analysis`

---

<a id="item-tech-news-3"></a>
### [地球上水面和陆地上最长直线路径的算法验证（2018）](https://arxiv.org/abs/1804.07389) ⭐️ 7.0/10

这篇 2018 年 arXiv 论文（1804.07389）提出一种结合计算几何与高程数据的算法，用于计算地球水面和陆地上的最长直线路径。研究结果确认并细化了 Reddit 上关于最长水上直线路径的原始说法，同时给出了陆地上的最长路径。算法需要处理球面大圆路径与陆地/海洋掩膜，且对低于海平面的区域有专门设定，这成为后续讨论中的一个争议点。该工作并非颠覆性进展，但为经典地理谜题提供了可复现的计算验证和可视化基础。

hackernews · joebig · 8月30日 08:23 · [社区讨论](https://news.ycombinator.com/item?id=49496782)

**「背景」** 该研究源于一个在 Reddit 上流传的地理谜题：寻找地球上不经过陆地的可航行最长直线路径。研究人员利用全球高程数据，将地球表面离散化为网格，并设计了一种计算几何算法来搜索这条路径，同时还将方法扩展到陆地上的最长直线路径。该论文于 2018 年发布在 arXiv 上（编号 1804.07389），作者为 Rohan Chabukswar 和 Kushal Mukherjee。

**「影响」** 该算法结果已被社区用于制作第一视角渲染等补充可视化，并引发对海平面以下区域处理方式的进一步讨论。

**「社区讨论」** 社区总体上认可论文的算法和结论，但也有评论指出其把低于海平面的区域一律视为水，可能漏掉了从塞内加尔附近到中国、途中经过死海的更长陆地路径；另有用户提供了第一视角渲染等补充可视化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/1804.07389">[1804.07389] Longest Straight Line Paths on Water or Land on the Earth</a></li>
<li><a href="https://arxiv.org/pdf/1804.07389">Longest Straight Line Paths on Water or Land on the Earth</a></li>

</ul>
</details>

**标签**: `#computational-geometry`, `#geospatial`, `#algorithms`, `#earth-science`, `#path-finding`

---

<a id="item-tech-news-4"></a>
### [亚马逊关闭 Mechanical Turk：AI 取代了训练它的人类](https://www.reddit.com/r/artificial/comments/1w2snwd/amazon_is_killing_mechanical_turk_by_the_end_a/) ⭐️ 7.0/10

亚马逊本周宣布，运行 21 年的众包平台 Mechanical Turk 将于 9 月 30 日关闭。巅峰时期有 50 万人从事图片标注、音频转录等任务，每任务仅赚几美分，这些数据训练了 AI 模型，而模型最终学会了这些工作。2023 年 EPFL 的一项研究发现，三分之一到一半的 Mechanical Turk 工人已使用 LLM 完成任务，形成了人类伪装成机器、机器完成工作的讽刺循环。这一关闭既终结了约 50 万人的灵活收入来源，也暴露了 AI 数据生产中人力与自动化边界日益模糊的问题。

reddit · r/artificial · /u/dettol99perc · 8月30日 20:36

**「背景」** Amazon Mechanical Turk（MTurk）是亚马逊于 2005 年推出的众包平台，把计算机难以完成的小任务（如图像标注、音频转录）分发给人类，每个任务报酬仅几美分，贝索斯曾称之为“人工人工智能”。亚马逊已宣布将于 2026 年 9 月 30 日关闭 MTurk，同时关闭 SageMaker Ground Truth 和 Amazon Augmented AI；请求者可在 10 月 30 日前审批工作和发放奖金，交易记录保留至 2027 年 1 月 28 日。EPFL 2023 年的一项研究通过键盘记录和合成文本分类估计，33%至 46%的众包工人在文本生成任务中使用了 ChatGPT 等大语言模型。

**「影响」** 约 50 万名依赖 Mechanical Turk 获得可支配灵活收入的工人将在 9 月 30 日后失去这一平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://briefly.co/anchor/Artificial_intelligence/story/amazon-mechanical-turk-to-shut-down-sept-30-after-21-years">Amazon Mechanical Turk to Shut Down Sept . 30 After 21... - Briefly</a></li>
<li><a href="https://www.whatjobs.com/news/amazon-to-shut-down-mechanical-turk-crowdsourcing-platform-on-sept-30/">Amazon to Shut Down Mechanical Turk ... | WhatJobs News</a></li>
<li><a href="https://claypier.com/en/aws-mechanical-turk-shutdown/">Amazon to Shut Down Mechanical Turk on September 30 ... | claypier</a></li>
<li><a href="https://techcrunch.com/2023/06/14/mechanical-turk-workers-are-using-ai-to-automate-being-human/">Mechanical Turk workers are using AI to automate being human | TechCrunch</a></li>
<li><a href="https://arxiv.org/abs/2306.07899">[2306.07899] Artificial Artificial Artificial Intelligence: Crowd Workers Widely Use Large Language Models for Text Production Tasks</a></li>
<li><a href="https://aiweekly.co/alerts/amazon-sets-sept-30-shutdown-for-bezos-era-mechanical-turk">Amazon Sets Sept. 30 Shutdown for Bezos-Era Mechanical Turk | AI Weekly</a></li>

</ul>
</details>

**标签**: `#Mechanical Turk`, `#AI`, `#LLM`, `#crowdsourcing`, `#Amazon`

---