#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetch Yale 'Inside the Yale Admissions Office' podcast transcripts and
convert each episode into a standalone Markdown file."""
import os
import re
import sys
import time
import html
from datetime import datetime
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
import html2text

BASE = "https://admissions.yale.edu"
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(ROOT, "yale_podcast_transcripts")
URLS_FILE = os.path.join(ROOT, "episode_urls.txt")

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

h2t = html2text.HTML2Text()
h2t.body_width = 0          # do not wrap lines
h2t.ignore_images = True
h2t.ignore_emphasis = False
h2t.ignore_links = False
h2t.unicode_snob = True
h2t.baseurl = BASE


def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "episode"


def fetch(url):
    r = requests.get(url, headers={"User-Agent": UA}, timeout=40)
    r.raise_for_status()
    # Yale serves UTF-8
    r.encoding = "utf-8"
    return r.text


def parse_episode(html_text, url):
    soup = BeautifulSoup(html_text, "lxml")

    # Title
    h1 = soup.select_one("h1.page-title__heading") or soup.select_one("h1")
    title = h1.get_text(" ", strip=True) if h1 else "Untitled"

    # Date
    date_str = ""
    dt = soup.select_one("time.date-time")
    if dt:
        date_str = dt.get_text(" ", strip=True)
        iso = dt.get("datetime", "")
    else:
        iso = ""
    # fallback: try any <time>
    if not date_str:
        t = soup.select_one("time")
        if t:
            date_str = t.get_text(" ", strip=True)
            iso = t.get("datetime", "")

    # Main body: prefer the onecol layout region (last one is the article body)
    regions = soup.select("div.layout__region--content")
    body_region = regions[-1] if regions else soup

    # Collect all .text blocks inside the body region and convert them
    text_blocks = body_region.select("div.text")
    if not text_blocks:
        # fallback: whole region
        text_blocks = [body_region]

    md_parts = []
    for blk in text_blocks:
        inner = "".join(str(c) for c in blk.children)
        md = h2t.handle(inner).strip()
        if md:
            md_parts.append(md)

    transcript = "\n\n".join(md_parts).strip()

    # Parse sort key
    sort_key = None
    if iso:
        try:
            sort_key = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        except Exception:
            sort_key = None
    if sort_key is None and date_str:
        for fmt in ("%B %d, %Y", "%A, %B %d, %Y", "%b %d, %Y", "%Y-%m-%d"):
            try:
                sort_key = datetime.strptime(date_str, fmt)
                break
            except Exception:
                continue

    return {
        "title": title,
        "date": date_str,
        "iso": iso,
        "url": url,
        "transcript": transcript,
        "sort_key": sort_key or datetime.max,
    }


def main():
    with open(URLS_FILE, encoding="utf-8") as f:
        urls = [urljoin(BASE, line.strip()) for line in f if line.strip()]

    print(f"Loaded {len(urls)} episode URLs")
    records = []
    failures = []
    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}] fetching {url}")
        try:
            html_text = fetch(url)
            rec = parse_episode(html_text, url)
            rec["_seq"] = i
            records.append(rec)
            print(f"    -> '{rec['title']}'  ({rec['date']})  "
                  f"transcript {len(rec['transcript'])} chars")
        except Exception as e:
            print(f"    !! ERROR: {e}", file=sys.stderr)
            failures.append((url, str(e)))
        time.sleep(0.4)  # be polite

    # Sort chronologically
    records.sort(key=lambda r: (r["sort_key"], r["_seq"]))

    os.makedirs(OUT_DIR, exist_ok=True)
    written = 0
    for idx, rec in enumerate(records, 1):
        slug = slugify(rec["title"])
        fname = f"{idx:02d}_{slug}.md"
        path = os.path.join(OUT_DIR, fname)
        # avoid collisions
        n = 1
        while os.path.exists(path):
            fname = f"{idx:02d}_{slug}-{n}.md"
            path = os.path.join(OUT_DIR, fname)
            n += 1
        meta = [
            f"# {rec['title']}",
            "",
            f"**Date:** {rec['date']}" if rec["date"] else "",
            f"**Source:** {rec['url']}",
            "",
            "---",
            "",
            rec["transcript"],
        ]
        meta = [m for m in meta if m != ""]
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(meta) + "\n")
        written += 1
        print(f"written {fname}")

    print(f"\nDONE: {written} files written to {OUT_DIR}")
    if failures:
        print(f"\nFAILURES ({len(failures)}):")
        for u, e in failures:
            print(f"  {u} -> {e}")


if __name__ == "__main__":
    main()
