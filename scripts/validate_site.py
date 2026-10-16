#!/usr/bin/env python3
"""Validate a generated SUS Jekyll site without external dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys
import xml.etree.ElementTree as ET

site = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
required = [
    "index.html", "styles.css", "script.js", "app-ads.txt", "robots.txt",
    "sitemap.xml", "kcallog.html", "formal-letter-maker.html", "kilopic.html",
    "audioprep-studio.html", "april-music.html", "sanat-relay.html",
    "tb-restore-studio.html", "tripura-paycalc.html",
    "tripura-paycalc/privacy-policy/index.html",
    "tripura-paycalc/terms/index.html",
    "tripura-paycalc/data-deletion/index.html",
    "blog/index.html", "blog/search/index.html", "search.json",
    "journal.css", "journal-search.js", "feed.xml",
]
required += [
    f"blog/categories/{category}/index.html" for category in [
        "inside-sus", "building-with-ai", "tech-updates", "tutorials", "ai-lab"
    ]
]
errors = []
for path in required:
    if not (site / path).is_file():
        errors.append(f"Missing required output: /{path}")
expected_ads = "google.com, pub-6758691642754158, DIRECT, f08c47fec0942fa0"
if (site / "app-ads.txt").exists():
    if (site / "app-ads.txt").read_text(encoding="utf-8").strip() != expected_ads:
        errors.append("app-ads.txt contents changed unexpectedly")
if (site / "robots.txt").exists() and "https://sanatutilitystudio.github.io/sitemap.xml" not in (site / "robots.txt").read_text(encoding="utf-8"):
    errors.append("robots.txt lost the sitemap reference")
if (site / "sitemap.xml").exists():
    try:
        sitemap = ET.parse(site / "sitemap.xml")
        urls = {item.text for item in sitemap.findall(".//{*}loc")}
        for url in [
            "https://sanatutilitystudio.github.io/",
            "https://sanatutilitystudio.github.io/kcallog.html",
            "https://sanatutilitystudio.github.io/tripura-paycalc/privacy-policy/",
            "https://sanatutilitystudio.github.io/blog/"
        ]:
            if url not in urls:
                errors.append("Sitemap missing important URL: " + url)
    except ET.ParseError as exc:
        errors.append("Invalid XML sitemap: " + str(exc))

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []
    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if value and ((name == "href" and tag in ("a", "link")) or (name == "src" and tag in ("img", "script"))):
                self.references.append(value)

for page in site.rglob("*.html"):
    parser = Links()
    parser.feed(page.read_text(encoding="utf-8"))
    for ref in parser.references:
        url = urlsplit(ref)
        if url.scheme or url.netloc or not url.path:
            continue
        target_path = unquote(url.path)
        if target_path.startswith("/"):
            target = site / target_path.lstrip("/")
        else:
            target = page.parent / target_path
        # Normalized paths cannot escape the build directory.
        target = target.resolve()
        if not target.is_relative_to(site):
            errors.append(f"Escaping local path in {page.relative_to(site)}: {ref}")
            continue
        if target.is_dir():
            target = target / "index.html"
        if not target.exists():
            errors.append(f"Broken local link in {page.relative_to(site)}: {ref}")
if errors:
    print("FAILED - site validation:")
    for error in errors:
        print(" -", error)
    sys.exit(1)
print(f"PASS: {len(required)} required outputs, app-ads.txt, sitemap and local HTML links.")
