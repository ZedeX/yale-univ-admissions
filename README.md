# Yale 招生办播客逐字稿与中文纪要

本仓库整理自耶鲁大学本科招生办官方播客 **Inside the Yale Admissions Office** 的官方 transcript 页面：

https://admissions.yale.edu/podcast-transcripts

## 项目内容

- **`yale_podcast_transcripts/`**：共 **52 集**播客逐字稿，每集一份独立 Markdown 文件。
  - `NN_*.md`：英文原文逐字稿（含标题、发布日期、来源链接与完整对话）。
  - `NN_*-CN.md`：基于原文由大模型生成的中文详细内容纪要，统一结构为：
    1. 本期概览
    2. 主要嘉宾与角色
    3. 详细内容纪要（按话题分小节，忠于原文）
    4. 关键要点与建议（给申请者）
    5. 金句摘录（英文原话 + 中文译文）
- **`fetch_yale.py`**：抓取与转换脚本（Python，依赖 `requests` / `beautifulsoup4` / `html2text` / `lxml`）。
- **`episode_urls.txt`**：52 集文章链接清单（抓取输入）。

## 目录结构示例

```
.
├── README.md
├── fetch_yale.py
├── episode_urls.txt
└── yale_podcast_transcripts/
    ├── 01_episode-1-reading.md
    ├── 01_episode-1-reading-CN.md
    ├── ...
    └── 52_what-yale-looks-for-part-1-academic-strength-CN.md
```


## 如何申请耶鲁：基于全部 52 集播客的综合指南

> 以下由 AI 通读《Inside the Yale Admissions Office》全部 52 集官方 transcript 的中文纪要后综合提炼，目的是把分散在各期的内容串成一套可操作的"申请耶鲁"整体认知。细节与原文请点击下方「各集内容概览」中的对应链接。
> 注意：耶鲁部分政策（尤其标化考试、补充文书题目）逐年调整，请以你申请当年官网公布的为准。

### 一、先理解耶鲁怎么招生（招生逻辑）

- **整体评估（Holistic Review）**：耶鲁每年收到的数万份申请（近年已超 5.2 万）都会被真人"从头到尾"完整阅读，不是算法打分，也不按 GPA/排名"加总"。
- **委员会决策**：每份申请先由区域招生官阅读、写工作卡与评分（评分只是内部速记），真正的决定发生在**五人委员会**（区域官、主席、另一招生官、一名教授、一名院长）的讨论与匿名投票中（录取通常需至少 4/5 票）；发榜前还有 Final Review 最后一关。
- **没有"模板"与"配额"**：耶鲁没有理想申请者模板、没有高中/地区/国家配额、没有"每校一人"、不追踪"表现出的兴趣"（demonstrated interest）、录取与助学金均 need‑blind。
- **真正寻找的**：你能为校园社群**贡献什么**、又能在耶鲁**收获什么**（fit）；学术实力是"必要但不充分"条件。

### 二、学术准备：成绩单与标化

- **选课**：在你就读的高中里选**最严谨、可获得**的课程，并贯穿四年持续挑战自我（核心学术课——数学、科学、英语、历史、语言——尽量不中断）。不要为 AP/IB 数量或加权 GPA "刷分"；耶鲁按学校背景整体评估，不横向攀比。一个 B 不会毁掉申请；若遇选课限制或困难，可在 Additional Information / Challenges and Circumstances 栏说明。
- **标化（逐年变化）**：2020–2023 为可选（test‑optional）；2024 为测试灵活（test‑flexible，SAT/ACT/AP/IB 任选其一）；**2026–2027 起恢复必须提交 SAT 或 ACT**（取消 AP/IB 替代）。请以申请当年官网为准。
- **红线**：学术诚信（作弊、抄袭、造假）绝对不可触碰，后果严重。

### 三、文书：用真实声音做"自我连接"

- 没有必胜主题或公式；文书不是作文考试，而是让招生官认识"真实的你"的窗户。
- **有效**：展示而非讲述（show, don't tell）、真诚反思、保留真实声音、简洁自然；借"改变想法、人际关系、热情、归属感、脆弱经历"等体现成长。
- **失灵（错失机会，而非雷区）**：第三人称反转、为煽情而煽情、只叙不议、停留过去、写成求职信、祖辈离世套路、刻意标新、堆砌辞藻。
- **耶鲁补充题**：`Why Yale` 要写"你被耶鲁吸引的故事"（先向内反思，而非罗列官网事实）；学术兴趣题展示好奇心与开放；短答题（short answers / short takes）大胆创意、真诚具体；长文书三选一都重在 *reflect*（反思）。
- **AI 红线**：用生成式 AI 代写违反诚信声明，可被撤销录取；文书灵魂在自我反思，AI 写出的内容"顺滑却无魂"。
- **附加信息栏**：只写必要的背景澄清（如成绩下滑、家庭变故），2025–2026 起限 300 词，**别写成第二封长文书**；多数申请者留白即可。

### 四、课外活动、推荐信与补充材料

- **活动**：核心是"真实"——做你真正喜欢且投入的事，**深度 > 数量**；按"对你最重要、投入最多"排序，家庭责任、打工、本地小项目同样有分量。不必创办 NGO、不必打造单一"尖峰"（spike）；耶鲁重视多元真实的兴趣全貌与对社区的实质贡献。
- **推荐信**：两封**核心学科教师**信（真正了解你、能写具体事例）+ 一封升学顾问信；补充推荐信几乎无影响，绝不代写。
- **补充材料**（艺术 / 研究等）：非必需；只有当该特长已是申请"核心"才提交，由专业教师盲审；它**不能弥补核心材料不足**。

### 五、申请流程与时机

- **平台**：Common App / Coalition / QuestBridge 任选，耶鲁补充题一致。
- **轮次**：SCEA（11/1，非绑定、单选提前行动）与 RD（1 月）。**关键澄清**：耶鲁 SCEA **不提供录取优势**，早申录取率更高只是因为申请池质量更高；只有当耶鲁是你明确首选且材料已就绪时才早申。被延期（defer）≠ 有缺陷。
- **面试**：非必需，通常 30–45 分钟轻松对话，起"锦上添花"与印证作用；无需盛装或带简历。
- **截止后**：老师/顾问材料晚到不会被拒；极端情况（灾害、技术故障）错过截止会被包容，但仍尽量提前数天提交以避开服务器高峰。

### 六、助学金与国际 / 特殊通道

- **助学金**：need‑blind（录取不受支付能力影响）+ need‑based（按需）+ 满足 100% 验证需求、**无贷款**；国际生同样适用（无需 FAFSA，需 CSS Profile + 税表）。先用"净价计算器"估算自付额。
- **国际生**：审核与国内申请**完全一致**，无国家配额；最后两年非英语教学者需提交英语能力测试；无升学顾问可让校方直送成绩单、找校内能写英文的成人代写 counselor 信。
- **转学 / Eli Whitney（非传统学生，学业中断 5 年以上）/ QuestBridge**：规模小但同样高选拔，审核逻辑一致；通过何种途径申请，录取与助学金流程都相同。
- **平权法案后**：学生仍可在文书中写种族相关经历，耶鲁价值观不变，无需为此改变申请策略。

### 七、心态与面对结果

- 录取决定**不定义**你的价值、潜力或努力；被拒多因名额有限而非你不够好；耶鲁无申诉流程，重申几乎不会改变结果（可考虑转学路径）。
- 候补（wait list）不排名，放下焦虑、专注已确定的选择。
- 别把申请当成"人生剧本"或分数游戏：耶鲁录取的是"成功的高中生"，不是"会写申请的人"。保持睡眠、学会求助、做你所爱。

### 八、给不同年级的行动清单

- **高二（Junior）**：开始探索选校、向内认识自己（列出"不可妥协项"）；选最具挑战的课程；真实投入活动；答案从招生官/升学顾问等可靠来源获取，别轻信网络谣言。
- **高三（Senior）**：申请只是收尾，每天固定少量时间处理即可；提前数天从容提交；在材料中真实呈现自己。
- **通用**：把申请当作认识自己、梳理价值的契机——这或许比"最终去哪一所"更重要。

### 九、最重要的一条

**做真实的自己（Be yourself）。** 耶鲁在 52 期里反复强调：没有模板、无需表演、无需"尖峰"或"完美人生剧本"；用真实的声音、诚恳的反思，以及对社群的关切，让自己在材料中"被认识"。所有关于"技巧"的建议，最终都不如真诚与自省更有力量。

---

## 各集内容概览（Episode Guide）

下表按发布时间顺序列出全部 52 集，包含中文标题、英文原标题、由大模型基于原文概括的内容梗概，以及英文原文与中文纪要的双语文件链接。

| # | 中文标题 | English Title | 内容梗概（AI 概括） | 英文原文 | 中文纪要 |
|---|---|---|---|---|---|
| 01 | 第1期：我们如何阅读申请材料 | Episode 1: Reading | 招生官讲解按地区分配、逐份通读每份申请并做笔记与评分；文件经多轮阅读后交委员会讨论，强调以“整体评估”认识真实的人，而非量化打分。 | [📄 EN](yale_podcast_transcripts/01_episode-1-reading.md) | [📘 中文](yale_podcast_transcripts/01_episode-1-reading-CN.md) |
| 02 | 第2期：招生委员会如何做决定 | Episode 2: Committee | 每宗申请由五人委员会（地区官、主席、另一招生官、一名教授、一名院长）讨论后匿名投票，需五票中四票方录取；决策靠集体商议而非个人决断。 | [📄 EN](yale_podcast_transcripts/02_episode-2-committee.md) | [📘 中文](yale_podcast_transcripts/02_episode-2-committee-CN.md) |
| 03 | 第3期：新冠疫情下的招生应对 | Episode 3: COVID-19 | 疫情下招生办远程完成审阅与委员会；招生主任说明成绩单、活动因疫情变化不会损害录取机会，会结合背景整体评估，并转线上与申请者保持沟通。 | [📄 EN](yale_podcast_transcripts/03_episode-3-covid-19.md) | [📘 中文](yale_podcast_transcripts/03_episode-3-covid-19-CN.md) |
| 04 | 第4期：文书——什么能打动我们 | Episode 4: Essays: What Works | 好文书贵在“展示而非讲述”、真诚反思、保留真实声音、简洁自然；借改变想法、人际关系、热情、归属感或脆弱经历等，让招生官认识真实的你。 | [📄 EN](yale_podcast_transcripts/04_episode-4-essays-what-works.md) | [📘 中文](yale_podcast_transcripts/04_episode-4-essays-what-works-CN.md) |
| 05 | 第5期：文书——什么会失灵 | Episode 5: Essays: What Doesn’t Work | 效果不佳的文书多属“错失机会”：第三人称反转、为煽情而煽情、只叙不议、停留过去、写成求职信、祖辈离世套路、浴室笑话、刻意标新、过度堆砌辞藻。 | [📄 EN](yale_podcast_transcripts/05_episode-5-essays-what-doesn-t-work.md) | [📘 中文](yale_podcast_transcripts/05_episode-5-essays-what-doesn-t-work-CN.md) |
| 06 | 第6期：文书——那些"小问题" | Episode 6: Essays: The Little Stuff | 介绍耶鲁特有短答题（如“为何选耶鲁”、学术兴趣、35词短答、250词短文），题目每年精心打磨，意在让申请者多维度展示自我并体现与学校的契合度。 | [📄 EN](yale_podcast_transcripts/06_episode-6-essays-the-little-stuff.md) | [📘 中文](yale_podcast_transcripts/06_episode-6-essays-the-little-stuff-CN.md) |
| 07 | 第7期：QuestBridge 合作项目 | Episode 7: QuestBridge | 讲解耶鲁与QuestBridge合作：为低收入家庭学生免申请费并匹配全额助学金（家长零分担）；其申请与常规一样整体评估，鼓励真实、完整地讲述自己的故事。 | [📄 EN](yale_podcast_transcripts/07_episode-7-questbridge.md) | [📘 中文](yale_podcast_transcripts/07_episode-7-questbridge-CN.md) |
| 08 | 第8期：校友/在校生于面试 | Episode 8: Interviews | 面试非必需，通常为30–45分钟轻松对话，由校友或在读生进行；报告仅补充、印证其他材料。建议自然交流、展现好奇心与自省，无需盛装或带简历。 | [📄 EN](yale_podcast_transcripts/08_episode-8-interviews.md) | [📘 中文](yale_podcast_transcripts/08_episode-8-interviews-CN.md) |
| 09 | 第10期：补充材料（艺术/STEM 等） | Episode 10: Supplementary Materials | 补充材料（艺术/音乐/舞蹈/电影/STEM研究）非必需，仅当该特长已是你申请核心才有用；由专业教师盲审评级，可锦上添花，却无法弥补核心材料不足。 | [📄 EN](yale_podcast_transcripts/09_episode-10-supplementary-materials.md) | [📘 中文](yale_podcast_transcripts/09_episode-10-supplementary-materials-CN.md) |
| 10 | 推荐信全攻略 | Episode 9: Recommendation Letters | 本集讲解推荐信：耶鲁要求两封核心学科教师信加一封顾问信。选真正了解你、能写具体事例的老师，补充信无益，招生官重真实细节。 | [📄 EN](yale_podcast_transcripts/10_episode-9-recommendation-letters.md) | [📘 中文](yale_podcast_transcripts/10_episode-9-recommendation-letters-CN.md) |
| 11 | 招生谣言粉碎机（第一辑） | Episode 11: Mythbusters | 本集破除六大招生误区：早申并不比常规轮更易录取，耶鲁无高中或地区配额，不追踪“表现兴趣”，暑期项目不加分，网上“测录取概率”不可信。 | [📄 EN](yale_podcast_transcripts/11_episode-11-mythbusters.md) | [📘 中文](yale_podcast_transcripts/11_episode-11-mythbusters-CN.md) |
| 12 | 新冠疫情下的招生工作更新 | Episode 12: COVID-19 Update | 疫情下耶鲁将宣讲与招生委员会转为线上，并临时将SAT/ACT改为可选。招生官强调仍做整体评估，学生活动因疫情中断与否均不被偏好。 | [📄 EN](yale_podcast_transcripts/12_episode-12-covid-19-update.md) | [📘 中文](yale_podcast_transcripts/12_episode-12-covid-19-update-CN.md) |
| 13 | 怎样才算"脱颖而出"？ | Episode 13: What Stands Out | 本集谈“何为突出”：耶鲁看重申请者能为校园增添什么、又能从中收获什么。真正脱颖而出者往往真实做自己、展现学术热情与社区影响力。 | [📄 EN](yale_podcast_transcripts/13_episode-13-what-stands-out.md) | [📘 中文](yale_podcast_transcripts/13_episode-13-what-stands-out-CN.md) |
| 14 | "预录信"（Likely Letters）究竟是什么 | Episode 14: Likely Letters | 耶鲁每年向约200名常规轮申请者发“likely letter”，意在提前争取易被其他名校争抢的学生，与实力无关；九成以上录取者并无此信。 | [📄 EN](yale_podcast_transcripts/14_episode-14-likely-letters.md) | [📘 中文](yale_podcast_transcripts/14_episode-14-likely-letters-CN.md) |
| 15 | 如何面对录取结果：拒绝、录取与候补 | Episode 15: Dealing with Decisions | 本集教如何面对结果：拒信不代表人生成败或能力不足，只因名额有限；候补期间应专注已有录取、不必纠缠；被录者亦勿自大。 | [📄 EN](yale_podcast_transcripts/15_episode-15-dealing-with-decisions.md) | [📘 中文](yale_podcast_transcripts/15_episode-15-dealing-with-decisions-CN.md) |
| 16 | 转学生与非传统学生申请指南 | Episode 16: Transfer and Nontraditional Students | 本集介绍转学及Eli Whitney（学业中断五年以上）项目：规模很小但极看重生活经历多样性。社区学院生与退伍军人皆可申请，按近期学业表现评估。 | [📄 EN](yale_podcast_transcripts/16_episode-16-transfer-and-nontraditional-students.md) | [📘 中文](yale_podcast_transcripts/16_episode-16-transfer-and-nontraditional-students-CN.md) |
| 17 | 申请中的"选择游戏"：哪些做法加分、哪些减分 | Episode 17: The Choices Game | 本集以点赞/踩点评常见申请选择：附加信息堆简历、第三封教师信、诗体文书、刻意煽情宜避免；研究导师推荐信与补充真实背景值得加。 | [📄 EN](yale_podcast_transcripts/17_episode-17-the-choices-game.md) | [📘 中文](yale_podcast_transcripts/17_episode-17-the-choices-game-CN.md) |
| 18 | 招生谣言粉碎机（第二辑） | Episode 18: Mythbusters 2 | 本集再破六误区：耶鲁不以压低录取率为目标，无“完美申请者”模板，不必填满活动栏或刷满AP，不必渲染苦难，国际生无需额外标化考试。 | [📄 EN](yale_podcast_transcripts/18_episode-18-mythbusters-2.md) | [📘 中文](yale_podcast_transcripts/18_episode-18-mythbusters-2-CN.md) |
| 19 | 课外活动板块怎么写 | Episode 19: The Activities Section | 招生官讲解课外活动评审，核心建议是“做你所爱、适度参与”。不必堆砌经历或硬创办组织，重在真实展现兴趣与对社区的贡献，多数申请者活动评分集中在中间值。 | [📄 EN](yale_podcast_transcripts/19_episode-19-the-activities-section.md) | [📘 中文](yale_podcast_transcripts/19_episode-19-the-activities-section-CN.md) |
| 20 | 高三年级常见问题解答 | Episode 20: Senior Year Questions & Answers | 针对高三申请者常见疑问（国籍身份、截止日、推荐信迟到、成绩单差异、双录取等）逐一解答，安抚焦虑并强调突发情况不会损害录取，材料可补交。 | [📄 EN](yale_podcast_transcripts/20_episode-20-senior-year-questions-answers.md) | [📘 中文](yale_podcast_transcripts/20_episode-20-senior-year-questions-answers-CN.md) |
| 21 | 听众来信特辑（Mailbag） | Episode 21: Mailbag | 首期邮件问答：回应宗教等“敏感”文书主题、疫情期活动列表、阅读爱好能否入表、推荐信与是否联系招生官等听众提问，重申真实做自己最关键。 | [📄 EN](yale_podcast_transcripts/21_episode-21-mailbag.md) | [📘 中文](yale_podcast_transcripts/21_episode-21-mailbag-CN.md) |
| 22 | 助学金入门 101 | Episode 22: Financial Aid 101 | 财务援助官讲解耶鲁助学金四原则：need-blind、need-based、整体需求评估、可负担承诺。说明费用构成、FAFSA/CSS材料与助学金无需偿还，提醒勿错过截止日。 | [📄 EN](yale_podcast_transcripts/22_episode-22-financial-aid-101.md) | [📘 中文](yale_podcast_transcripts/22_episode-22-financial-aid-101-CN.md) |
| 23 | 高二年级常见问题解答 | Episode 23: Junior Year Questions & Answers | 面向高二学生的常见问答，涵盖选课、访校、暑期安排、新活动、AP考试、文书准备、成绩回升与招生宣传邮件，鼓励探索自我、从实际出发规划申请。 | [📄 EN](yale_podcast_transcripts/23_episode-23-junior-year-questions-answers.md) | [📘 中文](yale_podcast_transcripts/23_episode-23-junior-year-questions-answers-CN.md) |
| 24 | 招生黑话宾果游戏（Lingo Bingo） | Episode 24: Lingo Bingo! | 以宾果游戏科普招生与助学金常用术语（Common App、FAFSA、CSS、SCEA、QuestBridge、Short Takes、Status Portal、need-blind等），帮申请者读懂流程黑话。 | [📄 EN](yale_podcast_transcripts/24_episode-24-lingo-bingo.md) | [📘 中文](yale_podcast_transcripts/24_episode-24-lingo-bingo-CN.md) |
| 25 | 最终审核（Final Review） | Episode 25: Final Review | 揭秘录取委员会最终审查：因名额有限须在已录取者中取舍，多数结果不变。提醒申请者很多因素超出个人控制，被拒或候补未必代表差距很大。 | [📄 EN](yale_podcast_transcripts/25_episode-25-final-review.md) | [📘 中文](yale_podcast_transcripts/25_episode-25-final-review-CN.md) |
| 26 | 我到底该不该申请？ | Episode 26: Should I Even Apply? | 回应“我该不该申耶鲁”：列出竞争力所需的必要条件（学术实力、英语能力、诚信、契合文理教育等），并澄清换校、非全A、疾病等并非硬性劣势。 | [📄 EN](yale_podcast_transcripts/26_episode-26-should-i-even-apply.md) | [📘 中文](yale_podcast_transcripts/26_episode-26-should-i-even-apply-CN.md) |
| 27 | 2022–2023 申请更新 | Episode 27: 2022-2023 Application Update | 介绍2022-2023申请文书改动：两篇短文书合并为一篇约400词长文书，新增融合“兴奋话题”的AA题、价值观交流/社区贡献长文及“未提及之事”短答题。 | [📄 EN](yale_podcast_transcripts/27_episode-27-2022-2023-application-update.md) | [📘 中文](yale_podcast_transcripts/27_episode-27-2022-2023-application-update-CN.md) |
| 28 | 提前录取全解析 | Episode 28: Early Admissions | 本集讲解耶鲁单选提前行动（SCEA）为非绑定、不提供录取优势；提前申请仅在耶鲁是你明确首选且材料11月1日前就绪时才值得，否则与常规轮无异。 | [📄 EN](yale_podcast_transcripts/28_episode-28-early-admissions.md) | [📘 中文](yale_podcast_transcripts/28_episode-28-early-admissions-CN.md) |
| 29 | 邮件问答第二期 | Episode 29: Mailbag 2 | 本集邮件问答涵盖荣誉栏、双胞胎、 homeschool 申请者、推荐信、补充材料及重申；要点：高三重在做自己，二次申请极少被录取，不必过度包装。 | [📄 EN](yale_podcast_transcripts/29_episode-29-mailbag-2.md) | [📘 中文](yale_podcast_transcripts/29_episode-29-mailbag-2-CN.md) |
| 30 | 重新解读审阅流程 | Episode 30: Reading Reloaded | 本集揭秘耶鲁新增的“初步审阅”环节及招生官写的审阅卡片与评分；录取由委员会讨论决定，而非算法打分，故文书与推荐信的真实呈现最为关键。 | [📄 EN](yale_podcast_transcripts/30_episode-30-reading-reloaded.md) | [📘 中文](yale_podcast_transcripts/30_episode-30-reading-reloaded-CN.md) |
| 31 | 录取确认季 | Episode 31: Yield Season | 本集介绍四月“yield season”：耶鲁努力说服录取者入学，但招生时不考虑就读意向或yield率，纯按实力与契合度录取，申请者无需为此策略化。 | [📄 EN](yale_podcast_transcripts/31_episode-31-yield-season.md) | [📘 中文](yale_podcast_transcripts/31_episode-31-yield-season-CN.md) |
| 32 | 斗牛犬日现场 | Episode 32: Bulldog Days Live! | 本集在录取者开放日现场录制，多名学生分享经验：申请的核心是真实、自我反思与做自己，而非琢磨“如何钻营进名校”，真挚比技巧更重要。 | [📄 EN](yale_podcast_transcripts/32_episode-32-bulldog-days-live.md) | [📘 中文](yale_podcast_transcripts/32_episode-32-bulldog-days-live-CN.md) |
| 33 | 2023–2024 申请季文书更新 | Episode 33: 2023-2024 Application Update | 本集公布2023-24耶鲁补充文书与短答题的新题；建议用现在/过去时写“关于你自己的事”，避免堆砌百科式介绍或空想未来，保持真诚。 | [📄 EN](yale_podcast_transcripts/33_episode-33-2023-2024-application-update.md) | [📘 中文](yale_podcast_transcripts/33_episode-33-2023-2024-application-update-CN.md) |
| 34 | 人工智能与大学文书：问错了问题，也给错了答案 | Episode 34: AI and College Essays: Wrong Question; Wrong Answer | 本集谈AI与申请文书：用ChatGPT代写违背诚信声明且不会加分，招生官看重的是你独有的声音与反思，AI写出的内容“华丽却空洞”，无法替代自我表达。 | [📄 EN](yale_podcast_transcripts/34_episode-34-ai-and-college-essays-wrong-question-wrong-answer.md) | [📘 中文](yale_podcast_transcripts/34_episode-34-ai-and-college-essays-wrong-question-wrong-answer-CN.md) |
| 35 | 辟谣现场 | Episode 35: Mythbusters Live! | 本集直播答疑破除误区：无需“ passion project”、未定专业无碍、耶鲁早申无优势、平权法案裁决后仍可写种族经历；整体审阅依背景因人而异。 | [📄 EN](yale_podcast_transcripts/35_episode-35-mythbusters-live.md) | [📘 中文](yale_podcast_transcripts/35_episode-35-mythbusters-live-CN.md) |
| 36 | 那只最高法院案子到底怎么回事 | Episode 36: What’s the Deal With That Supreme Court Case? | 本集解读最高法院SFFA案：耶鲁审阅中将不再看到申请者自报种族，但学生仍可在文书中写种族相关经历；裁决不应改变你准备申请的方式。 | [📄 EN](yale_podcast_transcripts/36_episode-36-what-s-the-deal-with-that-supreme-court-case.md) | [📘 中文](yale_podcast_transcripts/36_episode-36-what-s-the-deal-with-that-supreme-court-case-CN.md) |
| 37 | 揭秘招生谣言直播（早申截止特别版） | Episode 37: Mythbusters Live – EA Deadline Edition | 本集为EA截止前线上答疑，招生官澄清标化考试“可选”政策、早申不提高录取率、无名额与黑名单等谣言，并讲解活动排序与文书写作要点。 | [📄 EN](yale_podcast_transcripts/37_episode-37-mythbusters-live-ea-deadline-edition.md) | [📘 中文](yale_podcast_transcripts/37_episode-37-mythbusters-live-ea-deadline-edition-CN.md) |
| 38 | 斗牛犬日现场直播 2024 | Episode 42: Bulldog Days Live! 2024 | 招生官在已被录取学生面前分享选校最后阶段建议，并邀请新生讲述如何通过访校、交流来判断“哪所学校真正适合自己”。 | [📄 EN](yale_podcast_transcripts/38_episode-42-bulldog-days-live-2024.md) | [📘 中文](yale_podcast_transcripts/38_episode-42-bulldog-days-live-2024-CN.md) |
| 39 | 申请更新 2024-2025 | Application Update 2024-2025 | 本学年耶鲁附加文书题目与去年完全相同；招生官结合上年度回复，给出如何写好“为何选耶鲁”、短答及三选一长篇文书的建议。 | [📄 EN](yale_podcast_transcripts/39_application-update-2024-2025.md) | [📘 中文](yale_podcast_transcripts/39_application-update-2024-2025-CN.md) |
| 40 | 大学搜索 101：如何提问 | College Search 101: How to Ask Questions | 面向高二高三学生，建议选校前先主动思考，向招生官或在读生提出个性化问题，而非只问排名或泛泛而谈。 | [📄 EN](yale_podcast_transcripts/40_college-search-101-how-to-ask-questions.md) | [📘 中文](yale_podcast_transcripts/40_college-search-101-how-to-ask-questions-CN.md) |
| 41 | 揭秘谣言直播 2024（申请截止特别版） | MythBusters Live 2024 Application Deadline Edition | 招生官在申请截止前答疑，澄清新的“灵活标化”政策、早申不降低录取率、AI不审材料、无需“专长”等误区，并讲解活动与文书。 | [📄 EN](yale_podcast_transcripts/41_mythbusters-live-2024-application-deadline-edition.md) | [📘 中文](yale_podcast_transcripts/41_mythbusters-live-2024-application-deadline-edition-CN.md) |
| 42 | 大学搜索 101：什么对你重要 | College Search 101: What’s Important to You | 面向低年级学生，建议选校前先“认识自己”，列出不可妥协的底线（地点、专业、社群等），并忽略大学排名。 | [📄 EN](yale_podcast_transcripts/42_college-search-101-what-s-important-to-you.md) | [📘 中文](yale_podcast_transcripts/42_college-search-101-what-s-important-to-you-CN.md) |
| 43 | 耶鲁看重什么：特别揭秘版 | What Yale Looks For: Special Mythbusters Edition | 招生官在审材料期间澄清常见误区：耶鲁不看“明确职业规划”“堆砌成就”“突出苦难”或“专长”，而重视真实反思与社区契合。 | [📄 EN](yale_podcast_transcripts/43_what-yale-looks-for-special-mythbusters-edition.md) | [📘 中文](yale_podcast_transcripts/43_what-yale-looks-for-special-mythbusters-edition-CN.md) |
| 44 | 斗牛犬日现场直播 2025 | Bulldog Days Live 2025 | 第三届Bulldog Days现场，招生官介绍这一最大规模录取生活动，并请新生分享如何平衡高中强度、自我成长并享受过程。 | [📄 EN](yale_podcast_transcripts/44_bulldog-days-live-2025.md) | [📘 中文](yale_podcast_transcripts/44_bulldog-days-live-2025-CN.md) |
| 45 | 申请更新 2025-2026 | Application Update 2025-2026 | 本学年耶鲁附加题中“为何选耶鲁”改为“反思你的兴趣、价值观或经历如何吸引你”，并介绍Common App附加信息栏调整。 | [📄 EN](yale_podcast_transcripts/45_application-update-2025-2026.md) | [📘 中文](yale_podcast_transcripts/45_application-update-2025-2026-CN.md) |
| 46 | 选择高中课程 | Selecting High School Courses | 招生官讲解高中选课：看重学术准备与学术积极性，建议选校内最具挑战课程并坚持四年，勿盲目堆AP或过度专攻单一领域；成绩单最关键却非录取唯一决定因素。 | [📄 EN](yale_podcast_transcripts/46_selecting-high-school-courses.md) | [📘 中文](yale_podcast_transcripts/46_selecting-high-school-courses-CN.md) |
| 47 | 访谈 Jimmy Hatch：从海豹突击队到耶鲁课堂 | Interview with Jimmy Hatch | 采访经Eli Whitney非传统学生项目入学的52岁耶鲁毕业生、前海军海豹突击队Jimmy Hatch，分享从军旅到人文教育的转变，强调广泛好奇、跨差异对话与珍惜大学时光。 | [📄 EN](yale_podcast_transcripts/47_interview-with-jimmy-hatch.md) | [📘 中文](yale_podcast_transcripts/47_interview-with-jimmy-hatch-CN.md) |
| 48 | 听众来信第三辑（Mailbag 3） | Mailbag 3 | 邮件问答集：回应选课（敢挑战拿B）、暑期项目、Yale in MOHtion、低年级规划、推荐信及委员会常问问题，强调真实探索与善用资源而非堆砌简历或过早专一。 | [📄 EN](yale_podcast_transcripts/48_mailbag-3.md) | [📘 中文](yale_podcast_transcripts/48_mailbag-3-CN.md) |
| 49 | 国际招生 | International Admissions | 国际招生专题：对所有申请者采用整体评估且need-blind、满足100%资金需求；政策与国内生一致，详解海外课程体系、英语能力测试、签证与不同时间线等安排。 | [📄 EN](yale_podcast_transcripts/49_international-admissions.md) | [📘 中文](yale_podcast_transcripts/49_international-admissions-CN.md) |
| 50 | Bulldog Days 2026 现场特辑 | Bulldog Days Live 2026 | 录取学生分享申请心得的现场集：强调做自己热爱的事、感恩他人支持、活动贵在投入而非堆砌，并破除“必须四年专一”或“需单一热忱”等迷思。 | [📄 EN](yale_podcast_transcripts/50_bulldog-days-live-2026.md) | [📘 中文](yale_podcast_transcripts/50_bulldog-days-live-2026-CN.md) |
| 51 | 2026–2027 申请更新 | Application Update 2026-2027 | 2026-27申请更新：恢复必须提交SAT或ACT（取消AP/IB替代）；取消“为何选耶鲁”题，短答题减为三道，新增反思“大学期间希望成长的一面”的问题。 | [📄 EN](yale_podcast_transcripts/51_application-update-2026-2027.md) | [📘 中文](yale_podcast_transcripts/51_application-update-2026-2027-CN.md) |
| 52 | 耶鲁看重什么（第一部）：学术实力 | What Yale Looks For, Part 1: Academic Strength | 新系列首集讲学术实力：成绩单与标化是录取必要但不充分条件；看重持续挑战自我、广泛文理兴趣与抗挫折力，而非唯分数或堆砌“尖峰”式专攻。 | [📄 EN](yale_podcast_transcripts/52_what-yale-looks-for-part-1-academic-strength.md) | [📘 中文](yale_podcast_transcripts/52_what-yale-looks-for-part-1-academic-strength-CN.md) |

> 梗概由大模型阅读英文 transcript 后自动生成，旨在帮助快速判断每集是否相关；深入细节请点击对应链接阅读完整中文纪要或英文原文。

## 数据说明

- 数据来源为耶鲁大学官方公开页面，按发布时间（2020-05 至 2026-09）排序。
- 官网索引页中 **Episode 38–41 已下架**（直接访问返回 404），因此实际收录 52 集而非 53 集。
- 中文纪要由 AI 基于英文 transcript 生成，仅供学习与参考；如与官方原文有出入，以官方原文为准。

## 重新抓取 / 更新

如需重新抓取最新 transcript，安装依赖后运行：

```bash
pip install requests beautifulsoup4 html2text lxml
python fetch_yale.py
```

脚本会读取 `episode_urls.txt`，逐集抓取并生成英文 md 文件。

## 版权与归属

所有 transcript 文本版权归 **Yale University（耶鲁大学）** 所有。本仓库仅作个人学习、研究与非商业性参考用途整理，不构成对原内容的版权主张。如权利人认为不妥，可联系移除。
