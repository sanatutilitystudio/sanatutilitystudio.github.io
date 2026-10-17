# Phase 2B — Editorial review and release checklist

**Status: HOLD — NOT APPROVED FOR PUBLICATION**  
**Reviewed source:** `_drafts/how-ai-helped-me-build-sanat-utility-studio.md`  
**Target:** Sanat Utility Studio journal (future approved release only)

## Narrative review

- [ ] Confirm the medical-school and early web-development chronology.
- [ ] Verify the September 24, 2010 Wayback snapshot date.
- [ ] Verify the claims concerning HTML, Java, Python, Java/Symbian websites and free hosting.
- [ ] Review the three app-development examples for factual precision (KCalLog, KiloPic, AudioPrep Studio).
- [ ] Check all first-person wording against the developer's actual experience.
- [ ] Check the distinction between tested tools, recollections, facts and opinions.
- [ ] Remove exaggeration, guaranteed-outcome wording, hype and unsupported claims.
- [ ] Confirm the article title, SEO description, date and author attribution.

## Historical assets — prepared locally, not in GitHub yet

Two authentic Wayback screenshots have been cropped and redacted, excluding the original historic phone number, email and sharing code. The redacted assets are in the separately prepared editorial review ZIP (not in the public repository).

| Planned repository location | Size | SHA256 |
| --- | --- | --- |
| `assets/sanatruma-2010-introduction.webp` | 600 × 1030 | `00b50c1369f02208feb9663168a7c39be639bc87b4c90132d97da703064ab6e8` |
| `assets/sanatruma-2010-downloads.webp` | 600 × 1017 | `753e5df8f2891af30b214b632c1a2475bd2b02cff7132eec77890110a82332b7` |

- [ ] Upload only these approved, redacted image files to the development branch.
- [ ] Inspect the actual uploaded bytes and hashes to confirm no unredacted originals were substituted.
- [ ] Verify the screenshots' alternate descriptions and captions.
- [ ] Render the draft using Jekyll `--drafts` and confirm **both images load**.
- [ ] Review desktop and mobile presentation, heading structure and readability.
- [ ] Rebuild with standard Jekyll settings and verify the draft is absent from the site, feed, sitemap and search.

## Release gate

- [ ] Build succeeds and internal links resolve.
- [ ] Existing Google Play, legal-policy and product URLs are unchanged.
- [ ] Root `app-ads.txt` retains the original seller line.
- [ ] The developer approves the exact final article wording, imagery and layout.
- [ ] Only **after** explicit production approval: move the draft to `_posts/`, review the PR and merge into `main`.

**Important:** The GitHub repository itself is public, so draft *source files* in the feature branch are viewable on GitHub. They are not served as articles by the live website. Do not interpret a passing default-site build as a successful preview of this draft; the normal Jekyll build ignores `_drafts`.
