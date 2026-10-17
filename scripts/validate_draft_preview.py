#!/usr/bin/env python3
"""Validate editorial draft preview rendered via an isolated CI-only build."""
from pathlib import Path
from html.parser import HTMLParser
import hashlib
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else "_draft_site").resolve()
article_path = root / "blog/how-ai-helped-me-build-sanat-utility-studio/index.html"
homepage_path = root / "index.html"
checks = []
for path in (article_path, homepage_path):
    if not path.is_file():
        raise SystemExit(f"FAIL: Preview output missing: {path}")
article = article_path.read_text(encoding="utf-8")
home = homepage_path.read_text(encoding="utf-8")
for marker in (
    "How AI Helped Me Build Sanat Utility Studio",
    "Where AI actually became useful",
    "occasionally overconfident development assistant",
    "colour palette",
    "I would much rather make those visible",
):
    if marker not in article:
        checks.append(f"Missing expected article passage: {marker}")
if "Editorial note: This story is a draft" in article:
    checks.append("Internal editorial note leaked into article content")
if "How AI Helped Me Build Sanat Utility Studio" not in home or "journal-featured-story" not in home:
    checks.append("Homepage featured story is not rendered")
if '<a href="/blog/how-ai-helped-me-build-sanat-utility-studio/">' not in home:
    checks.append("Featured article link is missing")

expected = {
    "sanatruma-2010-introduction.webp": "00b50c1369f02208feb9663168a7c39be639bc87b4c90132d97da703064ab6e8",
    "sanatruma-2010-downloads.webp": "753e5df8f2891af30b214b632c1a2475bd2b02cff7132eec77890110a82332b7",
}
class Images(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
    def handle_starttag(self, tag, attrs):
        if tag == "img":
            self.images.append(dict(attrs))
parsed = Images()
parsed.feed(article)
for name, sha in expected.items():
    path = root / "assets" / name
    if not path.is_file():
        checks.append(f"Missing archive image: {name}")
    elif hashlib.sha256(path.read_bytes()).hexdigest() != sha:
        checks.append(f"Archive image hash mismatch: {name}")
    matching = [i for i in parsed.images if i.get("src") == "/assets/" + name]
    if len(matching) != 1 or not matching[0].get("alt"):
        checks.append(f"Article image or accessible alt text missing: {name}")
if checks:
    for err in checks:
        print("FAIL:", err)
    sys.exit(1)
print("PASS: Featured draft renders with both approved archive images and no internal editorial note.")
