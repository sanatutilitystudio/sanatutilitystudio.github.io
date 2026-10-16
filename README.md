# Sanat Utility Studio — Website

Production website: https://sanatutilitystudio.github.io/

This repository contains the official app portfolio and the Sanat Utility Studio journal. The original static HTML application and legal pages remain at their existing paths; GitHub Pages / Jekyll builds the new article infrastructure.

## Site structure

- `index.html` — existing homepage with journal preview
- `*.html` — retained standalone app/product pages
- `tripura-paycalc/` — retained public legal-policy routes
- `blog/`, `blog/categories/` — journal and category archives
- `_layouts/`, `_includes/` — reusable Jekyll templates
- `_posts/` — approved Markdown articles (added only after editorial review)
- `search.json`, `journal-search.js` — static article search
- `app-ads.txt`, `robots.txt` — important root resources
- `jekyll-sitemap` — generates `/sitemap.xml` during the build
- `scripts/validate_site.py` — build integrity checks

Read [Publishing and validation](docs/PUBLISHING.md) before adding articles. Keep Google Play and product links, Search Console verification, and `app-ads.txt` functional. Do not commit signing keys, passwords or API credentials.

Publishing is manual, and site changes require review. Phase 1 does **not** add GA4, ads or unapproved content.
