---
layout: default
title: "Horizon Summary: 2026-08-25 (ZH)"
date: 2026-08-25
lang: zh
---

> 从 69 条内容中筛选出 7 条重要资讯。

---

**AI 创作者雷达**
1. [Anthropic 上线免费 AI 学院，课程覆盖 Claude API、RAG、MCP](#item-ai-creator-1) ⭐️ 7.0/10
2. [OpenAI 被报道举行“AI 上岗”发布会：称可承担股票研究、投行路演](#item-ai-creator-2) ⭐️ 6.0/10

**科技新闻**
1. [画图与照片应用为本地图片添加隐形 GUID 水印](#item-tech-news-1) ⭐️ 8.0/10
2. [整座旧金山被做成网页版游戏化 3D 城市](#item-tech-news-2) ⭐️ 8.0/10
3. [seL4 在 AArch64 上的安全证明完成，形式化验证里程碑](#item-tech-news-3) ⭐️ 8.0/10
4. [阿里云 Wan3.0 上线：30 秒视频生成 API 最低 0.3 元/秒](#item-tech-news-4) ⭐️ 8.0/10
5. [你的可执行文件是 SQLite 数据库](#item-tech-news-5) ⭐️ 7.0/10

---

## AI 创作者雷达

<a id="item-ai-creator-1"></a>
### [Anthropic 上线免费 AI 学院，课程覆盖 Claude API、RAG、MCP](https://news.google.com/rss/articles/CBMijAFBVV95cUxOLWJZTXVDLWMtRlRQdUZKTloxaXhJY0ZUTzlVTkpkcm9fVU1keFhyYktTZS1OOEduT0JIXzVSUmJic2dKeXY0Z3VwazMtR3Y2cVVaTXZwR0xfaTVza2ZmRVdHWEpkdTk4OGRHZjRxMkg1OVYySS1qcmt5QmVZNjlCU1dpTmlnby1ZY0xPSw?oc=5) ⭐️ 7.0/10

据搜狐网转载信息，Anthropic 上线 AI 学院，所有课程免费学，内容从 AI 入门到 Claude API、RAG、MCP 开发，并涉及 Anthropic 员工培训中的 4D AI Fluency 框架。目前可见的关键细节主要来自新闻标题，尚无 Anthropic 官方公告、课程数量、上线日期和访问方式等具体信息。面向人群主要是希望学习 Claude 开发与 AI 基础的开发者和创作者。

rss · AI 内容商业化与自动化 · 8月24日 11:33

**「为什么现在值得注意」** 这一信息出现在 Claude API、RAG、MCP 生态备受关注的阶段，若属实，Anthropic 提供免费课程是面向开发者教育的实质性动作。但需要明确，材料只是转载标题，尚未证实课程实际上线状态，也不应视为官方正式发布。

**「内容角度」** 可做角度：从“Anthropic 免费 AI 学院”切入，整理 Claude API、RAG、MCP 的开发者学习路径，并明确标注哪些信息来自转载传闻、哪些尚待官方确认，避免把未核实细节当作事实。

**标签**: `#Anthropic`, `#AI课程`, `#Claude API`, `#开发者教育`, `#MCP`

---

<a id="item-ai-creator-2"></a>
### [OpenAI 被报道举行“AI 上岗”发布会：称可承担股票研究、投行路演](https://news.google.com/rss/articles/CBMiSEFVX3lxTE84dFE3Mmc3WS1jQVJmNUNBdkZ2UlhJUTAtaHdIZVB5NnNCQ1lmaGg5U0FGSXNGTUFnVG14eDFiYUh0d2ZoVUh4Yw?oc=5) ⭐️ 6.0/10

据财联社报道，OpenAI 举行了一场以“AI 上岗”为主题的发布会，并宣称 AI 能承担股票研究、投行路演等金融领域工作。目前可获取的信息仅有这条标题，尚不包含发布会时间、具体功能演示、能力边界或适用范围等可验证细节。

rss · AI 工具与效率产品 · 8月24日 13:40

**「为何现在值得关注」** 材料本身只提供了标题，尚无法确认发布会时间与具体内容；此事之所以值得注意，是因为它可能体现 AI 从通用对话向金融专业工作流延伸的潜在方向，但这一影响尚未得到证实。

**「内容切入角度」** 可做角度：以“AI 上岗”发布会为引，梳理 AI Agent 在金融场景中可能涉及的典型任务，如股票研究、投行路演材料准备等，并对照现有信息，区分哪些是官方演示、哪些仍只是宣传表述。

**标签**: `#OpenAI`, `#AI Agent`, `#金融`, `#发布会`, `#AI工具`

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [画图与照片应用为本地图片添加隐形 GUID 水印](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

微软 Windows 自带的画图（MS Paint）和照片（Photos）应用会对本地生成的图片静默添加基于 GUID 的不可见水印，即使图片完全在设备本地创建也会如此。该水印与用户或系统唯一标识相关联，用户不会收到任何提示，因此带来明显的隐私与匿名性风险。这一发现来自对应用的逆向分析，提示本地输出内容也可能携带可追踪标识。目前尚不清楚具体适用场景是否涵盖所有 AI 辅助操作，但本地生成的图片也可能受到影响。

hackernews · ComputerGuru · 8月24日 15:28 · [社区讨论](https://news.ycombinator.com/item?id=49421158)

**「背景」** 微软的“画图”与“照片”应用被发现会在使用本地 AI 模型处理图像时，从微软服务器获取 GUID，并将这个 GUID 作为不可见水印嵌入图像像素中；该算法位于 Watermarker.dll，独立于用户可以关闭的可见水印，且无法被禁用。这意味着即使用户完全在本地生成或编辑图像，输出仍带有可追踪的唯一标识符，同时还可能包含 C2PA 内容凭据。需要理解的是，这里的“本地 AI”仅指推理在设备上运行，但水印 GUID 由微软服务器签发，因此并非真正意义上的完全离线处理。

**「影响」** 使用微软画图或照片应用保存图片的用户，其本地生成图片也会携带隐形 GUID 标识，分享图片可能让第三方据此关联到其 Microsoft 账户或设备，构成隐私泄露风险。

**「社区讨论」** 评论普遍认为 AI 只是干扰项，核心问题是图片被静默写入唯一标识符，可能被用于针对微软账号的版权传票或破坏网络匿名性。也有用户指出可见水印可以关闭，但不可见水印无法禁用，并对本地处理仍会上报数据表示担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zeli.app/story/49421158">Microsoft Paint and Photos Embed Server-Issued GUIDs as... | Zeli</a></li>
<li><a href="https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/">Microsoft Paint and Photos Embed Server-Issued GUIDs as...</a></li>
<li><a href="https://byteiota.com/ms-paint-invisible-server-guid-watermark-ai-image/">MS Paint Embeds Invisible Server GUIDs in Every AI Image | byteiota</a></li>

</ul>
</details>

**标签**: `#privacy`, `#watermarking`, `#Microsoft`, `#reverse engineering`, `#surveillance`

---

<a id="item-tech-news-2"></a>
### [整座旧金山被做成网页版游戏化 3D 城市](https://sf.thijs.gg/) ⭐️ 8.0/10

一个名为 sf.thijs.gg 的网页项目将整座旧金山渲染成类似电子游戏的交互式 3D 环境，基于城市空间数据构建。它展示了实时渲染与地理空间数据整合的技术能力，被 Hacker News 用户视为互动地图和城市可视化领域的显著进展。项目内可在虚拟城市中驾车并收集硬币等游戏化元素，但目前没有本地高清版本或多人模式。社区反馈既包括在虚拟街区中唤起个人记忆的情感共鸣，也包含对街道名称、地标、地址传送等功能扩展的建议。

hackernews · centrosphere · 8月24日 17:05 · [社区讨论](https://news.ycombinator.com/item?id=49422784)

**「背景」** 这是一个基于浏览器的交互式 3D 城市模拟页面，将旧金山的建筑、地形等城市数据整合为可探索的游戏化环境。这类项目通常依赖开放的测绘数据与 Web 3D 渲染技术（如 WebGL、Three.js 等），在网页中实时呈现整座城市的全貌。它并非传统意义上的完整游戏，而是提供类似游戏引擎体验的城市可视化工具，让用户能够在网页上漫游、切换视角并查看地标。

**「影响」** 对互动地图与城市可视化开发者而言，该项目证明了仅凭公开城市数据就可在浏览器中构建可自由探索的城市级 3D 环境，可能推动更多类似可视化或游戏化地图项目的出现；不过其现阶段影响仍偏向展示性原型，尚无证据表明会直接转化为正式产品。

**「社区讨论」** 评论区普遍称赞项目的技术完成度与情感冲击力，一位在旧金山居住近 20 年的用户称在虚拟城市中行走让他感到激动。也有用户提出希望加入街道名称、地标、地址传送、本地高清版或多人模式，并指出日本城 Webster 与 Geary 人行天桥下方无法穿过等细节问题；还有人分享了西雅图的 N64 风格类似项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sf.thijs.gg/">San Francisco -- The Game</a></li>
<li><a href="https://progscrape.com/?search=sf.thijs.gg">progscrape: sf . thijs . gg</a></li>
<li><a href="https://news.ycombinator.com/item?id=49422784">The entire city of San Francisco as a video game | Hacker News</a></li>

</ul>
</details>

**标签**: `#3D rendering`, `#San Francisco`, `#geospatial`, `#web development`, `#interactive maps`

---

<a id="item-tech-news-3"></a>
### [seL4 在 AArch64 上的安全证明完成，形式化验证里程碑](https://proofcraft.systems/news-2026/#2026-08-21) ⭐️ 8.0/10

seL4 微内核现已完成针对 AArch64 架构的形式化安全证明，这标志着形式化验证在 64 位安全关键系统上取得重要进展。该证明复盖非 MCS（非混合关键性系统）和单核（unicore）配置，为广泛使用的安全关键微内核在 64 位架构上提供了更强的安全保证。此前 seL4 已经在 32 位架构上完成类似证明，此次扩展至 AArch64 使得更多现代硬件平台能够受益于其经过验证的安全属性。不过，评论指出该结果仍存在局限，且旁信道时序攻击等现实威胁可能削弱其实际安全效果。

hackernews · snvzz · 8月24日 11:32 · [社区讨论](https://news.ycombinator.com/item?id=49418255)

**「背景」** seL4 是一个形式化验证的微内核，以能力机制（capability model）实现隔离，长期用于安全关键系统。此前其安全证明主要覆盖 32 位架构，而本次宣布的里程碑是在 AArch64（64 位 Arm 架构）上完成了对实现代码的正式证明，确保运行在其上的应用程序之间具备安全隔离，但结果依赖特定假设条件。

**「影响」** 这一进展使 seL4 在 64 位 ARM（AArch64）平台上获得了经形式化验证的安全保证，对使用该微内核的系统和安全工程师具有重要意义；但当前证明仅覆盖单核、非 MCS（混合关键性系统）配置，且定时侧信道攻击仍可能削弱实际安全性。

**「社区讨论」** 社区对此次证明反应多样：有人调侃称旁信道时序攻击可能很快使该结果失效；有用户列举了 seL4 的实际使用者，包括 GenodeOS、LionsOS 以及某中国车企将其用作车载虚拟机监控程序，并询问其他部署案例；还有人提醒留意证明的“非 MCS、单核”两处限制，并认为若要真正提升系统安全性，可能需要原生 seL4/Linux 支持，而非仅依赖现有安全启动虚拟化平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lists.sel4.systems/hyperkitty/list/announce@sel4.systems/thread/ZL6HYXH3PKI6XUVKMPTLIPKQMWJW7N7M/">seL 4 security proofs now complete on AArch 64 ... - lists. sel 4 .systems</a></li>

</ul>
</details>

**标签**: `#seL4`, `#formal verification`, `#microkernel`, `#AArch64`, `#security`

---

<a id="item-tech-news-4"></a>
### [阿里云 Wan3.0 上线：30 秒视频生成 API 最低 0.3 元/秒](https://mp.weixin.qq.com/s/peeeU6cBz4AaROvFe1zqQQ) ⭐️ 8.0/10

阿里云今日正式上线视频生成模型 Wan3.0，支持最长 30 秒视频生成，并强调在人物质感、参考精准一致性和非写实风格化方面表现突出。用户可通过阿里云百炼、万相官网和千问 APP 等平台体验。API 按清晰度阶梯定价：480P、720P、1080P 分别为 0.3、0.6、1.2 元/秒；8 月 24 日至 9 月 23 日期间，阿里云百炼和千问 AI 平台提供限时 7 折优惠。该发布为视频生成领域提供了来自阿里云的高性价比商用方案，对 AI/ML 行业具有直接价值。

telegram · zaihuapd · 8月24日 10:14

**「背景」** 此前的 AI 视频生成模型通常只能生成几秒钟的短片，而 Wan3.0 将单次生成长度扩展到 30 秒。此外，Wan3.0 还支持多模态输入，可接受文档（如 DOC、XLS、PPT）等多种素材，并可组合最多 20 个资产进行创作。

**「影响」** 对使用阿里云百炼（Model Studio）的开发者与企业而言，Wan3.0 的 API 定价为 480P 0.05 美元/秒、720P 0.10 美元/秒、1080P 0.20 美元/秒，一条完整 30 秒 1080P 视频约 6 美元，低于 Google Veo 3.1 的 0.40 美元/秒，并已被用于短剧/电影制作、广告营销和旅游推广。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.alibabacloud.com/blog/wan3-0-30-second-ai-video-generation-from-any-input_603452">Wan3.0: 30-Second AI Video Generation from Any Input - Alibaba Cloud Community</a></li>
<li><a href="https://technode.com/2026/08/24/alibaba-launches-wan3-0-video-model-with-30-second-generation-and-document-input/">Alibaba launches Wan3.0 video model with 30-second generation and document input · TechNode</a></li>
<li><a href="https://github.com/AlibabaCloud-Official/Wan3.0">GitHub - AlibabaCloud-Official/Wan3.0: Official repository for Wan 3.0, Alibaba Cloud&#x27;s state-of-the-art AI video generation model. Supports native 30s videos, multi-modal omni-creation (up to 20 assets), cinematic realism, precision video editing, and advanced text rendering. · GitHub</a></li>
<li><a href="https://www.alibabacloud.com/blog/wan3-0-30-second-ai-video-generation-from-any-input_603452">Wan3.0: 30-Second AI Video Generation from Any Input - Alibaba Cloud Community</a></li>
<li><a href="https://aiweekly.co/alerts/alibaba-launches-wan30-video-model-after-10b-share-sale">Alibaba launches Wan3.0 video model after $10B share sale | AI Weekly</a></li>
<li><a href="https://ground.news/article/alibaba-launches-wan30-video-model-with-30-second-generation-and-document-input-technode">Alibaba Launches Wan3.0 AI Video Model After $10 Billion Share Sale</a></li>

</ul>
</details>

**标签**: `#video generation`, `#Alibaba Cloud`, `#AI models`, `#API pricing`

---

<a id="item-tech-news-5"></a>
### [你的可执行文件是 SQLite 数据库](https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/) ⭐️ 7.0/10

Farid Zakaria 展示了一种 Linux 技巧，让 SQLite 数据库文件可以直接作为可执行二进制运行。方法是将 SQLite 文件格式第 68 字节处的 4 字节应用 ID 设为 SELF，代表结构化可执行与可链接格式，并把 ELF 可执行格式的各个组件存放到不同的 SQLite 表中。配套的 self-exec 解释器可以提取并执行必要部分，还可以通过 binfmt\_misc 机制让内核在识别到该二进制模式时自动调用解释器（作者使用 NixOS 演示，非 NixOS 系统可通过向 /proc/sys/fs/binfmt\_misc/register 写入注册行实现）。这目前是一个概念验证，而非广泛影响的技术突破。

rss · Simon Willison · 8月24日 11:38

**「背景」** SQLite 数据库文件有一个 4 字节的应用 ID 字段，通常用于标识文件类型；ELF 是 Linux 可执行文件的标准格式，包含文件头、程序头和节区等组件。binfmt\_misc 是 Linux 内核机制，允许通过自定义模式匹配来注册新的可执行文件格式。这一技巧将数据库文件同时伪装成 ELF 启动所需的模式，并通过额外解释器执行其中存储的 ELF 组件。

**「影响」** 对 Linux 开发者、文件格式爱好者和实验者而言，该方案展示了将 SQLite 作为可执行文件容器的可能性，但它是概念验证，尚不适合生产环境或广泛生态采用。

**标签**: `#sqlite`, `#elf`, `#linux`, `#executable`, `#file-format`

---