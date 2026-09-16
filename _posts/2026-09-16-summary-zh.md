---
layout: default
title: "Horizon Summary: 2026-09-16 (ZH)"
date: 2026-09-16
lang: zh
---

> 从 75 条内容中筛选出 6 条重要资讯。

---

**AI 创作者雷达**
1. [学而思 AI 课程从 1 节升级为 10 节，称已进入 56 所中小学](#item-ai-creator-1) ⭐️ 5.0/10

**科技新闻**
1. [TypeSafe.ai 推出 System One Models 与 Jev](#item-tech-news-1) ⭐️ 7.0/10
2. [电子墨水相框识别鸟鸣并绘制成 19 世纪风格插画](#item-tech-news-2) ⭐️ 7.0/10
3. [Internet Archive 就 Wayback Machine 访问发布更新](#item-tech-news-3) ⭐️ 7.0/10
4. [Google 发布 Gemini 3.8 Live 与 3.8 Live Extended Thinking](#item-tech-news-4) ⭐️ 7.0/10
5. [Simon Willison 发布 Gemini Live 语音试用网页界面](#item-tech-news-5) ⭐️ 7.0/10

---

## AI 创作者雷达

<a id="item-ai-creator-1"></a>
### [学而思 AI 课程从 1 节升级为 10 节，称已进入 56 所中小学](https://news.google.com/rss/articles/CBMickFVX3lxTE9NeURpV0hBVWNQV21sOE9HemdwRldCbVNZUDR2QjM4LUVTTHJoR0wyZU1Mc0RDay1YUlhpX290cmNPWXJhdW5laWxMeEFfanRHbDZxX002SlNsVmJtZEpXZGxBNHlrTlA5aHI5RGlmNGNHdw?oc=5) ⭐️ 5.0/10

据标题信息，学而思将其“一节 AI 课”升级为 10 节课程，并称相关课程已走进 56 所中小学。可验证的细节目前仅限课程节数变化和学校数量，原文未提供课程内容、上线时间、覆盖地区及教学效果等信息。受影响人群可能包括使用该课程的中小学师生，但具体落地方式和合作模式尚不明确。该表述带有宣传属性，需以官方原文或后续披露为准。

rss · AI 内容商业化与自动化 · 9月15日 03:55

**「内容角度」** 可做角度：把“1 节 AI 课变 10 节”当作 AI 教育产品化的观察切口，追问课程从单次体验到体系化课程时，学校采购、教师使用和课时安排可能发生哪些具体变化；但需先找到原文或官方说明，避免把宣传口径直接当作事实。

**标签**: `#AI教育`, `#学而思`, `#中小学`, `#课程升级`, `#教育落地`

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [TypeSafe.ai 推出 System One Models 与 Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) ⭐️ 7.0/10

TypeSafe.ai 在一篇博客文章中推出 System One Models 和 Jev，后者被描述为一种结构化/类型化推理方法。与通用生成模型不同，Jev 专注于生成结构化输出，因此社区评论认为它适合分类、问答等任务，而不是替代能输出任意代码的通用模型。有评论质疑其速度对比可能具有误导性，因为通用生成模型能通过图灵完备语言输出代码来完成任何计算机可完成的任务；也有评论认为其商业价值在于从最新 LLM 中蒸馏高频任务并以更低成本、更快速度提供服务。讨论中提到的其他细节包括 Home Assistant 演示、与设计契约/SymbolicAI 结合的可能性，以及毫秒级延迟和每百万 token 0.042 美元的成本说法，这些均来自社区评论，未在源内容中独立验证。

hackernews · albelfio · 9月15日 19:25 · [社区讨论](https://news.ycombinator.com/item?id=49717558)

**「背景」** TypeSafe AI 是一家构建面向自动化的机器原生智能基础设施的 AI 实验室，目标是让模型在软件内部直接做出决策。System One 模型是一类专为快速、结构化决策而设计的模型：它们评估状态并返回带类型的答案和概率。Jev 是 TypeSafe 的旗舰模型，也是首个 System One 模型，目前处于早期访问阶段。

**「影响」** 对需要把非结构化输入快速映射为类型化决策的开发者，Jev 提供的是“非结构化状态输入、类型化概率化决策输出”的函数式能力，可用于分类、抽取等窄场景，但因其放弃字符串生成而无法替代通用生成模型。其“零幻觉”应被理解为类型安全层面的狭义主张，而非对输出正确性或适用范围的普遍保证。

**「社区讨论」** 社区普遍认为 Jev 新颖且实用，尤其适合结构化分类/问答等任务；主要争议在于速度对比是否公平，因为 Jev 牺牲了通用生成能力。也有评论指出，其价值可能来自对前沿 LLM 常见任务的高效蒸馏，从而以更快、更便宜的方式服务特定用例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.typesafe.ai/concepts/system-one">System One - TypeSafe AI</a></li>
<li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev">Introducing System One Models &amp; Jev - TypeSafe AI Blog</a></li>
<li><a href="https://kingy.ai/blog/typesafe-jev-review-the-ai-model-that-doesnt-generate-text/">TypeSafe Jev Review: The AI Model That Doesn’t Generate... - Kingy AI</a></li>
<li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev">Introducing System One Models &amp; Jev - TypeSafe AI Blog</a></li>

</ul>
</details>

**标签**: `#AI models`, `#structured output`, `#LLM inference`, `#type safety`, `#developer tools`

---

<a id="item-tech-news-2"></a>
### [电子墨水相框识别鸟鸣并绘制成 19 世纪风格插画](https://github.com/arnegiacomo/fugleramme) ⭐️ 7.0/10

开发者 arnemunthekaas 在 Hacker News 的 Show HN 板块发布了一个名为 fugleramme 的开源项目（托管于 GitHub 的 arnegiacomo/fugleramme）：一台电子墨水相框能够识别周围的鸟鸣声，并把识别出的鸟绘制成 19 世纪风格的插画。帖子获得了约 1350 点与 183 条评论，社区普遍认为这是边缘机器学习与电子墨水硬件的一次有趣结合，也被形容为“有魔力”的创作。评论者指出，项目底层的鸟类声音分类器是 BirdNET——一个传统神经网络而非大语言模型，其依据是 2021 年发表于《Ecological Informatics》的论文。帖子还关联到此前一个同类项目“Avian Visitors”（20 条评论），显示近期围绕鸟类识别出现了多个相关项目。项目以开源硬件与计算艺术的形式呈现，具体识别精度、硬件清单与插画生成方式等细节需以仓库说明为准。

hackernews · arnemunthekaas · 9月15日 12:31 · [社区讨论](https://news.ycombinator.com/item?id=49711544)

**「背景」** Fugleramme 是一个面向树莓派的开源电子墨水屏项目：麦克风采集环境声音后交给本地运行的 BirdNET-Go 进行识别，再把对应物种画成 19 世纪手绘风格的鸟类插画，检测配置也由 BirdNET-Go 统一管理，整个流程完全在本地完成。其核心分类器 BirdNET 并非大语言模型，而是 2021 年发表于《Ecological Informatics》第 61 卷（编号 101236）的深度神经网络，用于鸟类多样性监测，可自动识别鸟鸣并支持声学事件检测与分类。

**「影响」** 对业余硬件与观鸟爱好者而言，该项目的价值在于把现成的 BirdNET 音频分类、电子墨水屏与低功耗板卡组合成可复用的方案；但这仍是一个个人开源项目，其识别准确率与实际部署条件尚未由项目方给出可验证的数据。

**「社区讨论」** 评论整体以赞赏为主：jadbox 称其为近期 HN 上最酷的作品，divbzero 则澄清底层分类器 BirdNET 是传统神经网络而非 LLM。joshstrange 分享了自用经验——家中四块电子墨水屏通过 KOReader 显示书摘，并称新装的 BTLE 电子墨水驱动在 2000mAh 电池下即使每天多次刷新也能用上数年；theturtletalks 则注意到近期鸟类项目扎堆，归因于 birdnet-go 等项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://connormwood.com/wp-content/uploads/2021/02/kahl.etal-2021-birdnet-a-deep-learning-solution-for-avian-diversity-monitoring.pdf">Ecological Informatics 61 (2021) 101236 Available online 27 January 2021</a></li>
<li><a href="https://github.com/arnegiacomo/fugleramme">GitHub - arnegiacomo / fugleramme : E - ink bird frame for Raspberry...</a></li>
<li><a href="https://arnegiacomo.dev/fugleramme/">E - ink bird frame for Raspberry Pi</a></li>

</ul>
</details>

**标签**: `#e-ink`, `#BirdNET`, `#edge machine learning`, `#open-source hardware`, `#computational art`

---

<a id="item-tech-news-3"></a>
### [Internet Archive 就 Wayback Machine 访问发布更新](https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/) ⭐️ 7.0/10

Internet Archive 发布了关于 Wayback Machine 访问情况的更新，称该服务遭遇多波高流量自动化流量，并已部署保护措施以维持服务运行。该机构认为，这些流量很可能来自抓取者，它们试图绕过对原始网站的访问限制，转而访问 Wayback Machine 上的存档副本。Internet Archive 表示，此类行为给这一关键的非营利互联网基础设施增加了负载，而且已经有一些网站选择退出存档。

hackernews · ChrisArchitect · 9月15日 17:52 · [社区讨论](https://news.ycombinator.com/item?id=49716176)

**「背景」** 互联网档案馆（Internet Archive）是位于美国旧金山的非营利数字图书馆，由 Brewster Kahle 于 1996 年创立，其使命是“提供对一切知识的普遍访问”。该机构运营的 Wayback Machine 于 2001 年向公众开放，允许用户“回到过去”查看网站昔日的样貌，因而成为网络历史存档与开放访问的重要基础设施。此次更新提到，Wayback Machine 遭到大规模自动化流量的连续冲击，被拦截的请求会返回 HTTP 429 错误码，官方推出的防护措施正是在这一背景下出台的。

**「影响」** 随着防护措施上线，Wayback Machine 的普通用户可能遭遇限流（社区中已有人报告持续的 429 错误）和访问不稳定，而部分站点因抓取压力选择退出存档，则会直接缩小这一收录数百亿网页、缺乏同规模替代品的公共档案的可检索范围。互联网档案馆尚未公开限流的具体阈值与适用范围，因此实际影响程度仍有不确定性。

**「社区讨论」** 评论者普遍谴责抓取者对 Internet Archive 造成的负担，并赞赏其仍维持开放访问，包括有用户表示可以从 Tor 匿名访问而无需经过 Cloudflare 等中心化网关。也有人提出实际访问中的困惑，例如在工作电脑上持续遇到 429 错误而手机正常；讨论中还有要求 AI 公司支付高额费用，以及通过监管和高额罚款来应对 AI 抓取滥用的呼声。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wayback_Machine">Wayback Machine - Wikipedia</a></li>
<li><a href="https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/">An Update on Wayback Machine Access | Internet Archive Blogs</a></li>
<li><a href="https://waybackmachine.app/">Wayback Machine - Explore Internet History</a></li>
<li><a href="https://technology.inquirer.net/147235/ai-scraping-is-unintentionally-hurting-the-wayback-machine">AI scraping is unintentionally hurting the Wayback Machine</a></li>

</ul>
</details>

**标签**: `#Internet Archive`, `#Wayback Machine`, `#AI scraping`, `#web archiving`, `#open access`

---

<a id="item-tech-news-4"></a>
### [Google 发布 Gemini 3.8 Live 与 3.8 Live Extended Thinking](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/) ⭐️ 7.0/10

Google 在其官方博客发布了 Gemini 3.8 Live 与 Gemini 3.8 Live Extended Thinking，这是 Gemini 模型家族面向实时/语音场景的一次更新。该消息在 Hacker News 上引发活跃讨论（322 分、198 条评论），用户反馈集中在实时语音表现、口音适应、延迟以及模型定位上。有用户报告说能够在工作区（workspace）账号中使用该模型，而此前多个近期发布版本在这类账号上处于受限状态。目前公开信息中尚未提供基准测试数据，因此这次更新带来的实际能力提升幅度仍不明确。

hackernews · leumon · 9月15日 17:38 · [社区讨论](https://news.ycombinator.com/item?id=49715947)

**「背景」** Gemini Live 是 Google 提供的近实时语音对话能力，此次发布的是支撑该能力的新一代模型：Gemini 3.8 Live 与 Gemini 3.8 Live Extended Thinking。Google 将这两款模型称为其迄今最先进的实时对话模型，面向自然交谈与近实时语音代理场景，其中 Live 与 Live Extended Thinking 的区分对应实时响应与需要更多思考时间的两种模式。据 9to5Google 报道，Gemini 3.8 Live Extended Thinking 还将驱动 Gemini Live、Gmail 等产品中的相关体验。

**「影响」** 对实时语音交互用户和受工作区账号限制的开发者来说，最具体的后果是该模型可在工作区账号上使用，并且早期体验反馈称其延迟较低、对浓重口音处理良好；这些属于使用者主观体验，尚未有基准数据支撑。

**「社区讨论」** 评论者中有人高度称赞 Gemini 在小众语言（如南非荷兰语）对话和即兴语法教学上的语音表现，并称其口音适应好、延迟低、声音悦耳；也有用户批评官方演示视频中模型在国际象棋最常见的将杀模式上失手，并质疑 Google 虽握有数据、TPU 硬件与广告资金优势却仍在竞争中落后。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/">Gemini 3 . 8 Live &amp; Gemini 3 . 8 Live Extended Thinking</a></li>
<li><a href="https://zerohour.day/item/78ec933d8f3c9110a6b74409b1a00980245e1cd9">Gemini 3 . 8 Live and 3 . 8 Live Extended Thinking · ZeroHour</a></li>
<li><a href="https://9to5google.com/2026/09/15/gemini-3-8-live-announced/">Gemini 3 . 8 Live Extended Thinking powers Gemini Live , Gmail</a></li>

</ul>
</details>

**标签**: `#Gemini`, `#LLM`, `#Generative AI`, `#Voice AI`, `#Google`

---

<a id="item-tech-news-5"></a>
### [Simon Willison 发布 Gemini Live 语音试用网页界面](https://simonwillison.net/2026/Sep/15/gemini-live/) ⭐️ 7.0/10

Google 发布了 Gemini 3.8 Live 与 Gemini 3.8 Live Extended Thinking 两款语音到语音模型，形态与 OpenAI 的 GPT-Live 系列相似（源文发表时间为 2026 年 9 月 15 日）。Simon Willison 让 GPT-6 Astra Extra High 阅读官方文档后，生成了一个用于试用这两个新模型的网页 UI。该界面支持选择模型与音色预设、填写可选的系统提示词，并可在浏览器中直接进行语音对话，还允许在模型说话时打断它。实现不使用任何库，直接连接 wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContent 的 WebSocket 端点，并用 Web Audio API 的 AudioContext 完成音频采集与播放；界面提供开始/结束会话、麦克风静音、麦克风音量表、计时器以及可下载的对话转录。源文提示应使用耳机以减少回声，发送文字消息会打断当前回复，转录中可能包含尚未播放就被打断的语音；文中未提供基准测试、架构细节或独立评测。

rss · Simon Willison · 9月15日 22:47

**「背景」** 语音到语音（speech-to-speech）模型直接接收并生成音频，不像传统语音助手那样把语音识别、语言模型推理和文本转语音串成多段流水线，因而延迟更低，也更利于保留语气和情感。Google 此次推出 Gemini 3.8 Live 与 3.8 Live Extended Thinking，称其目标是让语音交互更自然、流畅和智能，其中标准版侧重规模与成本效率，Extended Thinking 版则强化复杂推理、实时视觉上下文和后台任务执行等能力。开发者可通过 Gemini Live API 的 WebSocket 端点进行双向流式音频交互，Simon Willison 的工具正是基于该接口构建。

**「影响」** 对构建实时语音代理的开发者而言，Google 声称 Gemini 3.8 Live Extended Thinking 以 82.6 分位居 Artificial Analysis 语音对语音质量指数首位，并在 τ-Voice 上取得 68.6%、在银行客服类任务上以 35.1% 领先 GPT-Live-1 Astra 的 32.0% 与 xAI-Realtime 的 16.5%，这可能使其成为新的默认候选模型。不过上述成绩来自 Google 官方博客及媒体转述的厂商自报数据，目前尚无独立基准验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/">Introducing Gemini 3.8 Live and 3.8 Live Extended Thinking</a></li>
<li><a href="https://www.thurrott.com/a-i/google-gemini-a-i/341685/google-announces-gemini-3-8-live-and-3-8-live-extended-thinking">Google Announces Gemini 3.8 Live and 3.8 Live Extended Thinking - Thurrott.com</a></li>
<li><a href="https://officechai.com/ai/google-releases-gemini-3-8-live-extended-conversational-model-claims-better-performance-than-gpt-live-1-astra-and-grok-voice-think-fast-2-0-at-lower-price/">Google Releases Gemini 3.8 Live-Extended Conversational Model, Claims Better Performance Than Rivals At Lower Price</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/">Introducing Gemini 3.8 Live and 3.8 Live Extended Thinking</a></li>
<li><a href="https://officechai.com/ai/google-releases-gemini-3-8-live-extended-conversational-model-claims-better-performance-than-gpt-live-1-astra-and-grok-voice-think-fast-2-0-at-lower-price/">Google Releases Gemini 3.8 Live-Extended Conversational Model, Claims Better Performance Than Rivals At Lower Price</a></li>

</ul>
</details>

**标签**: `#Gemini Live`, `#speech-to-speech models`, `#AI voice interfaces`, `#developer tools`, `#Google Gemini`

---