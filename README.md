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
