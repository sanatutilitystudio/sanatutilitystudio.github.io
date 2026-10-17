# SUS editorial publishing workflow

This repository serves the existing app portfolio at its original URLs and adds a GitHub Pages / Jekyll journal.

## Preview locally

Ruby and Bundler are needed for a local Jekyll preview. Run `bundle install`, then `bundle exec jekyll serve` and open `http://127.0.0.1:4000/blog/`. GitHub Pages can build the same source automatically after deployment.

## Prepare an article (not automatic publishing)

1. Draft off the `main` branch; have the developer review claims, sources, screenshots, privacy and wording.
2. When approved, create `_posts/YYYY-MM-DD-short-slug.md` and give it YAML front matter:
   ```yaml
   ---
   title: "A concise descriptive title"
   date: 2026-10-18 19:00:00 +0530
   description: "A helpful 1–2 sentence article summary."
   categories: [inside-sus]
   author: "Sanat Debbarma"
   featured: false
   ---
   ```
3. Choose a single primary category from `inside-sus`, `building-with-ai`, `tech-updates`, `tutorials`, `ai-lab`.
4. Link original sources. Distinguish observed facts, personal interpretation and tools actually tested. Never publish a fabricated experience.
5. Preview the rendered article and check mobile, links, alt text, dates and spelling. Do not expose private contact details in historical screenshots.
6. Publish only after explicit editorial approval and successful checks; merge reviewed changes to `main`.

Posts appear automatically in reverse chronological order, category archives, the homepage feature, feed, search index and XML sitemap. Pagination begins when there are more than six published posts. The search index is generated statically, requiring no database.

## Preservation and rollback

Legacy product pages keep their original `*.html` routes. Existing CSS, JavaScript, Play Store links and legal pages stay untouched in rendered output. `app-ads.txt` must remain at the domain root. If a deployment breaks an existing link, revert the migration commit/PR on `main` to return to the previous version.

## Deployment notes

Native GitHub Pages/Jekyll supports `jekyll-sitemap`, `jekyll-paginate` and `jekyll-feed`. The old manually maintained `sitemap.xml` source is deliberately removed; the plugin generates it at build time. The root `robots.txt` continues referencing that URL.

Do not introduce unapproved posts, GA4 identifiers, AdSense code, invasive trackers or custom paid services during infrastructure implementation. Analytics and policy work belong to Phase 2.

## Validation

`python3 scripts/validate_site.py _site` verifies critical legacy URLs, the app-ads publisher record, blog routes, generated sitemap, and internal links. The pull request build workflow runs these checks on a GitHub Pages-compatible Jekyll build.

## First article published

The October 2026 introductory article lives in _posts. Future content must undergo human review before publication. Archive images are redacted. Do not expose the original contact details or access code. The website requires Jekyll processing; do not browse source index.html directly.
