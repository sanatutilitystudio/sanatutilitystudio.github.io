#!/usr/bin/env python3
"""Validate a generated SUS Jekyll site without external dependencies."""
from html.parser import HTMLParser
import hashlib
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
    "about-developer/index.html", "about-developer.css", "assets/developer-portrait.webp",
    "assets/sanatruma-2010-introduction.webp", "assets/sanatruma-2010-downloads.webp",
    "assets/kd-player-playback-representative.webp",
    "assets/kd-player-playlist-representative.webp",
    "assets/nokia-nth-themes-representative.webp",
    "blog/how-ai-helped-me-build-sanat-utility-studio/index.html",
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
# Guard against accidentally replacing redacted archive images with originals.
approved_images = {
    "assets/sanatruma-2010-introduction.webp": "00b50c1369f02208feb9663168a7c39be639bc87b4c90132d97da703064ab6e8",
    "assets/sanatruma-2010-downloads.webp": "753e5df8f2891af30b214b632c1a2475bd2b02cff7132eec77890110a82332b7",
}
for path, expected_hash in approved_images.items():
    if (site / path).is_file():
        digest = hashlib.sha256((site / path).read_bytes()).hexdigest()
        if digest != expected_hash:
            errors.append(f"Archive image not approved/redacted version: {path}")
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
            "https://sanatutilitystudio.github.io/blog/",
            "https://sanatutilitystudio.github.io/about-developer/",
            "https://sanatutilitystudio.github.io/blog/how-ai-helped-me-build-sanat-utility-studio/"
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
article_page = site / "blog/how-ai-helped-me-build-sanat-utility-studio/index.html"
if article_page.is_file():
    html = article_page.read_text(encoding="utf-8")
    for term in ("From Nokia Themes to Sanat Utility Studio", "Where AI actually became useful", "occasionally overconfident development assistant"):
        if term not in html:
            errors.append("Article content missing: " + term)
    for image in approved_images:
        if 'src="/' + image + '"' not in html:
            errors.append("Article image missing: " + image)
    if "Nokia themes and KD Player skins" not in html:
        errors.append("Missing feature-phone chapter")
    for asset_name in (
        "kd-player-playback-representative.webp",
        "kd-player-playlist-representative.webp",
        "nokia-nth-themes-representative.webp",
    ):
        if f'src="/assets/{asset_name}"' not in html:
            errors.append("Article missing representative image " + asset_name)
    if "They are not surviving screenshots of my original themes or player skins." not in html:
        errors.append("Representative image attribution missing")
    if "Editorial note: This story" in html:
        errors.append("Internal editorial note present in published article")
if (site / "index.html").is_file():
    home = (site / "index.html").read_text(encoding="utf-8")
    if "journal-featured-story" not in home or "From Nokia Themes to Sanat Utility Studio" not in home:
        errors.append("Featured article not visible on homepage")
if errors:
    print("FAILED - site validation:")
    for error in errors:
        print(" -", error)
    sys.exit(1)
print(f"PASS: {len(required)} required outputs, app-ads.txt, sitemap and local HTML links.")
