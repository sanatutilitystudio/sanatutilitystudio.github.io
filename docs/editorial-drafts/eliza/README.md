# ELIZA: unpublished editorial draft

Prepared 15 November 2026 for Sanat Utility Studio.

This content lives on the GitHub branch `draft/eliza-editorial-2026-11`, **not on main**. It is unpublished. The article is stored in `_drafts/eliza-remarkable-story.md`, with `published: false` and `sitemap: false`. Jekyll does not render drafts in normal builds. All its images are held in `docs/editorial-drafts/eliza/images`, which the website's `_config.yml` excludes.

- `preview.html` is the review copy with all three images **embedded**, suitable for opening separately without fetching assets.
- `_drafts/eliza-remarkable-story.md` is the full approximately 1,800-word editorial draft with captions and sources, using temporary draft-stage image paths.
- The 1960s lab and transcript graphics are AI-generated editorial interpretations. Neither should be presented as a historical photograph or screenshot. The first features a historically imagined CRT representation; original ELIZA used text terminals and teletypes.
- The Joseph Weizenbaum 2005 portrait was photographed by **Ulrich Hansen**, licensed **CC BY-SA 3.0**, via https://commons.wikimedia.org/wiki/File:Joseph_Weizenbaum.jpg . Keep the author/license linked in the figure caption.
- Original source and restoration citations are included at the end of the article.
- Large PDF scan and additional research originals remain only in the pre-existing local research folder, not committed to GitHub.

## To publish later (not authorized by this change)

Review the article and imagery. Copy all three images into `/assets` and replace their `docs/editorial-drafts` references (including front matter). Set a publication date. Move the draft to `_posts`, change `published: true` and `sitemap: true`, then build, inspect mobile layout and links, and push to main **only with explicit publication approval**.

The GitHub repository is public, so branch source is viewable through GitHub; this does not make the post appear on the SUS website.

## Portrait display fix, 16 November 2026

A credited copy of the 2005 Weizenbaum portrait is hosted at `/assets/eliza/joseph-weizenbaum-ulrich-hansen-2005.jpg` on the main website, including `assets/eliza/PHOTO-CREDITS.txt` with photographer and licence. The unpublished Jekyll draft references that URL. Its standalone preview embeds the JPEG as a data URI so it displays in mobile viewers without a separate asset request. The source image is unmodified, from Wikimedia Commons.

## Editorial image revision — 16 November 2026

The 2005 color portrait is no longer used in this ELIZA draft. The early biography now uses the 1982 RIT black-and-white portrait; a separate documentary-era terminal photograph is positioned near the later history section. Both are embedded in the self-contained HTML preview so mobile file viewers work without external image downloads. Original AI editorial images remain unchanged.

**Rights gate before release:** RIT's portrait is public domain in the US per Wikimedia Commons, but its copyright status outside the US is not universally resolved. The user-supplied terminal photo's photographer, definitive archival identity and reproduction permission are unconfirmed. Do not publish either image to the live SUS site until rights review is complete. The draft branch is a public GitHub branch, not a private repository.

## Illustration replacement | 16 November 2026

Replaced the user-supplied documentary-era photo with `docs/editorial-drafts/eliza/images/weizenbaum-terminal-editorial-illustration.webp` and updated the caption in the draft and self-contained review HTML. The original unlicensed photo file is deleted from the latest draft branch tree. The approved illustration is a very close interpretation of the historical reference, so rights for its source composition still require review before publication. Do not treat the illustration as public-domain archival material.
