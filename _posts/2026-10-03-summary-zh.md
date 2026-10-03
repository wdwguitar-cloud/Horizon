---
layout: default
title: "Horizon Summary: 2026-10-03 (ZH)"
date: 2026-10-03
lang: zh
---

> 从 61 条内容中筛选出 4 条重要资讯。

---

**科技新闻**
1. [AI 首次击败顶尖 Stratego 人类选手，学习效率远超 DeepNash](#item-tech-news-1) ⭐️ 9.0/10
2. [Chalmers 团队构建闭环 AI，可自主提出并执行酵母实验](#item-tech-news-2) ⭐️ 8.0/10
3. [Google Research 公布 Cogentic 多智能体数学证明系统](#item-tech-news-3) ⭐️ 8.0/10
4. [The Forgetful CPU：Linux 在 Apple M4 上](#item-tech-news-4) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [AI 首次击败顶尖 Stratego 人类选手，学习效率远超 DeepNash](https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/) ⭐️ 9.0/10

一个 AI 系统据报成为首个击败顶尖人类 Stratego 选手的系统；Stratego 是一款大部分棋子信息对对手隐藏的棋盘游戏。该系统采用的方法比 DeepNash 少玩了约 34 倍的对局，却最终达到更强的棋力，显示隐藏信息博弈中的学习效率有大幅提升。相关成果已发表在《Nature》上，并有 arXiv 预印本。此前 DeepMind 在 2022 年提出的 DeepNash 曾被称为“掌握”Stratego，但社区评论认为那一次并未真正达到超越人类顶尖玩家的水平。

hackernews · PaulHoule · 10月2日 14:11 · [社区讨论](https://news.ycombinator.com/item?id=49933740)

**「背景」** Stratego（战略棋）是一款双人棋盘游戏，对局中双方的棋子种类和数值都向对手隐藏，因此属于典型的不完全信息博弈：一步棋的好坏往往取决于自己无法确知的信息，这使得前瞻搜索变得困难。2022 年 DeepMind 曾发布 DeepNash，采用无模型多智能体强化学习并结合正则化纳什动力学，在 Stratego 上达到接近顶尖人类的水平。此次引发讨论的新系统名为 Ataraxos，它在与人类顶尖选手的对局中取得压倒性战绩，而训练所用的算力与自对弈局数都远低于 DeepNash。

**「影响」** 对隐藏信息博弈的 AI 研究者而言，Ataraxos 以约 1.63 亿局自博弈（比 DeepNash 少约 34 倍）达到并超过顶尖人类玩家水平，意味着后续研究可更侧重样本效率而非单纯扩大训练规模。

**「社区讨论」** HN 评论者普遍认为，约 34 倍的对局效率提升是这项工作的关键，因为隐藏信息使前瞻搜索异常困难，最佳着法取决于无法获知的信息；也有人把 2022 年 DeepNash 的“掌握”放在这一新结果下重新审视，认为四年后的方法才真正强于人类。另有评论分享童年玩 Stratego 时对手在棋子上做记号的趣事，以及自己曾计划开发首个获胜 bot 的调侃。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/">With most information hidden, the game Stratego had... - Ars Technica</a></li>
<li><a href="https://www.zmescience.com/science/ai-beats-humans-stratego/">This AI Finally Beat the Best Humans at One of the Last Board...</a></li>
<li><a href="https://www.youtube.com/watch?v=3vO45gcEbRs">AI beats us at another game : STRATEGO | DeepNash paper explained</a></li>
<li><a href="https://games.slashdot.org/story/26/10/02/2129251/ai-has-finally-learned-to-play-stratego">AI Has Finally Learned To Play Stratego - Slashdot</a></li>
<li><a href="https://arxiv.org/abs/2206.15378">[2206.15378] Mastering the Game of Stratego with Model-Free...</a></li>

</ul>
</details>

**标签**: `#AI`, `#hidden-information games`, `#Stratego`, `#game AI`, `#DeepNash`

---

<a id="item-tech-news-2"></a>
### [Chalmers 团队构建闭环 AI，可自主提出并执行酵母实验](https://www.reddit.com/r/artificial/comments/1ww5ozf/scientists_build_an_ai_that_can_propose/) ⭐️ 8.0/10

瑞典查尔姆斯理工大学的研究人员开发了一套闭环 AI 系统，能够自主生成生物学假设、决定如何测试、把计划转成机器可读指令、分析实验结果，并据此改进后续问题。实验室机器人承担了大部分物理操作。该系统在酿酒与烘焙常用的酿酒酵母（Saccharomyces cerevisiae）上进行了测试，即便这种模式生物已被广泛研究，其遗传、代谢和生理信息仍远超人工系统逐一探索的能力。研究发表在《Journal of the Royal Society Interface》，将大语言模型与形式逻辑、生物数据库、机器学习、自动化细胞培养和质谱分析结合起来。

reddit · r/artificial · /u/Brighter-Side-News · 10月2日 21:26

**「背景」** 闭环自主实验指的是由 AI 自行生成假设、决定如何验证、把方案转成机器可读指令并执行，再用实验结果修正后续问题，从而让探索循环无需人工逐步介入；此前多数系统只做到分析数据和提出设想。该研究把大语言模型与形式逻辑、生物学数据库、机器学习、自动化细胞培养和质谱分析结合起来，并在酿酒酵母（Saccharomyces cerevisiae）上验证——这是酿造与烘焙所用、也是生物学中研究得最透彻的模式生物之一，但其遗传、代谢与生理信息量仍远超人工系统化探索的范围。相关论文《Agentic AI integrated with scientific knowledge: laboratory validation in systems biology》发表在 Journal of the Royal Society Interface 上。

**「影响」** 对 AI 驱动科学发现和实验室自动化的研究者而言，这项工作提供了一个把大语言模型、形式逻辑、生物数据库、机器学习与机器人实验串成闭环并用于酵母的公开案例，但其效率、可迁移性和通用性仍需更多同行验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.chalmers.se/en/current/news/ai-scientist-autonomously-generates-and-validates-new-biological-discoveries/">AI scientist autonomously generates and validates new... | Chalmers</a></li>
<li><a href="https://www.thebrighterside.news/post/scientists-build-an-ai-that-can-propose-experiments-run-them-and-learn-from-the-results/">Scientists build an AI that can propose experiments , run them and...</a></li>
<li><a href="https://cryptobriefing.com/swedish-ai-scientist-automates-experiments/">Swedish researchers build an AI scientist that runs its own experiments</a></li>

</ul>
</details>

**标签**: `#AI for science`, `#autonomous experimentation`, `#LLM agents`, `#lab automation`, `#closed-loop systems`

---

<a id="item-tech-news-3"></a>
### [Google Research 公布 Cogentic 多智能体数学证明系统](https://arxiv.org/abs/2609.40324v1) ⭐️ 8.0/10

Google Research 公布了一项名为 Cogentic 的研究，提出一套用于自动发现数学证明的多智能体系统，相关论文发布在 arXiv 上。该系统以 Gemini 为基础模型，采用“证明—验证”循环：多个独立证明器分头探索不同证明方向，并由专门组件进行对抗式验证，已确认的结果则存入可持续使用的验证账本。据该公布，Cogentic 在在线学习、拍卖理论和机制设计三个领域的 5 个开放问题上产出了新结果，这些结果均由领域专家独立验证，并在配套论文中展开说明。目前该消息仅来自一条简短的 Telegram 通报，技术细节有限，也没有独立第三方确认，因此应视为有待进一步核实的初步研究进展。

telegram · zaihuapd · 10月2日 12:04

**「背景」** 大语言模型用于数学证明时，常见做法是让模型一次性给出完整证明，但对于需要同时探索多个相互竞争猜想、跨越细微技术障碍并长期保留中间进展的开放问题，单次生成往往不足。Cogentic 因而把证明搜索组织为多轮、可验证的流程：编排器将不同探索方向分配给相互独立的证明器，专门验证器对草稿提出对抗性质疑，被确认的引理则写入可复用的持久验证账本。该研究属于 AI for mathematics 与多智能体系统的交叉方向，由 Google Research 提出，基础模型为 Gemini。

**「影响」** 若这些结果成立，在线学习、拍卖理论与机制设计方向的研究者将多出一条由多智能体「证明—验证」循环产出的研究路径，其他数学与理论计算机科学团队也可能直接借用该编排框架来攻关研究级问题。不过目前成果仅依据论文自述的领域专家验证，尚缺乏独立第三方的复现确认。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.40324">[2609.40324] Cogentic: Multi-Agent Orchestration for ...</a></li>
<li><a href="https://www.aimodels.fyi/papers/arxiv/cogentic-multi-agent-orchestration-automated-proof-discovery">Cogentic: Multi-Agent Orchestration for Automated Proof Discovery</a></li>
<li><a href="https://arxivsignals.io/papers/2609.40324">Cogentic: Multi-Agent Orchestration for Automated Proof ...</a></li>
<li><a href="https://arxiv.org/html/2609.40324">Cogentic: Multi - Agent Orchestration for Automated Proof Discovery</a></li>

</ul>
</details>

**标签**: `#multi-agent systems`, `#AI for mathematics`, `#theorem proving`, `#LLM research`, `#Google Research`

---

<a id="item-tech-news-4"></a>
### [The Forgetful CPU：Linux 在 Apple M4 上](https://yuka.dev/blog-2026-10-02-linux-m4.html) ⭐️ 7.0/10

这篇题为 The Forgetful CPU 的博客文章讨论在 Apple M4 硬件上运行 Linux。由于来源未提供正文，目前无法确认其涉及的具体内核版本、移植补丁、驱动支持、性能数据或兼容性限制。该条目在 Hacker News 获得 132 分和 58 条评论，表明系统、硬件与开源读者对该话题有一定关注。根据现有元数据，文章被视作面向这些受众的技术写作，但没有证据显示它是重大突破。

hackernews · signa11 · 10月2日 14:22 · [社区讨论](https://news.ycombinator.com/item?id=49933869)

**「背景」** Asahi Linux 是一个旨在让 Linux 在 Apple Silicon Mac 上运行的开源项目，其此前对 M1 至 M3 机型的支持为 M4 移植提供了参照。M4 芯片引入了 SPTM 等安全加固，导致该项目过去用于 bring-up 的 MMIO 跟踪方法失效，开发者不得不改用 println 式调试、设备树修改和寄存器级排查。因此，这篇技术文章记录的是在 M4 Mac mini 上启动主线 Linux 所经历的底层逆向工程过程。

**「社区讨论」** Hacker News 评论多为平台层面的感叹而非具体技术辩论：有人希望苹果更拥抱开放硬件，并称 macOS 臃肿但硬件优于其他选择；也有人质疑为何要从对开放生态敌意的公司购买设备来运行开源系统；还有评论提出能否借助 AI 完成相关工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://yuka.dev/blog-2026-10-02-linux-m4.html">The forgetful CPU (Linux on M4) - Blog - Yureka Lilian - yuka.dev</a></li>
<li><a href="https://www.youtube.com/watch?v=GCG5xr3JRfk">The Forgetful CPU (Linux on M4) - YouTube The forgetful CPU (Linux on M4) - daily.dev The Forgetful CPU (Linux on M4) | Hacker News The Forgetful CPU (Linux on M4) | h4cker The Forgetful CPU (Linux on M4) \ stacker news The forgetful CPU (Linux on M4) | Lobsters</a></li>
<li><a href="https://daily.dev/posts/the-forgetful-cpu-linux-on-m4--igqauax00">The forgetful CPU (Linux on M4) - daily.dev</a></li>

</ul>
</details>

**标签**: `#Linux`, `#Apple Silicon`, `#CPU Architecture`, `#Open Source`, `#Hardware`

---