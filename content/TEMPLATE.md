# Content frontmatter reference

Not a real page — build.py only scans files under content/en/ and content/kr/,
so this file (living directly under content/) is never picked up or built.
Copy the relevant section below when starting a new file.

All frontmatter fields marked (optional) may be omitted entirely.

---

## Simple page
content/{lang}/{page}.md, where page is one of:
index, memoir, books, courses, resources, aphorism, misc

```
---
title: Page Title
---

Body markdown.
```

## Essay
content/{lang}/essays/YYYY-MM-DD.md

```
---
title: "Essay Title"
date: 2026-01-01
description:                        (optional — shown in the essays.html listing)
translation_disclaimer: english     (optional — "english" or "korean"; omit if not a translation)
other_disclaimer: "Free-form text, [markdown links](https://example.com) work."  (optional)
first_published: 2026-01-01         (optional)
last_edited: 2026-01-01             (optional)
---

Body markdown. Footnotes work: a claim[^1].

[^1]: The footnote text.
```

## Paper
content/{lang}/research/YYYY-MM-DD.md
Same fields as an essay, plus:

```
arxiv: https://arxiv.org/abs/...        (optional — shown as a link on the Research listing)
openreview: https://openreview.net/...  (optional — shown as a link on the Research listing)
```
(No Korean toggle is rendered for papers regardless of language.)

## Life entry
content/{lang}/life/YYYY-MM.md — filename and `start` must both be "YYYY-MM"

```
---
title: "MM.YYYY - MM.YYYY: Movie/quote line"     (English — date_range and movie_line are split on ": ")
title: "MM.YYYY - MM.YYYY"                       (Korean — no movie_line needed)
start: "YYYY-MM"
translation_disclaimer: english     (optional — "english" or "korean")
other_disclaimer: "Free-form text, [markdown links](https://example.com) work."  (optional)
first_published: 2026-01-01         (optional)
last_edited: 2026-01-01             (optional)
---

> "Epigraph quote."
> — Attribution, *Source title*

Body markdown.
```
The epigraph blockquote is a body convention, not a frontmatter field — first two
lines of the body, `>`-prefixed, quote then em-dash attribution (trailing two
spaces after the quote line force a line break before the attribution).

---

## translation_disclaimer / other_disclaimer / first_published / last_edited

These four work identically on any content type read via read_md() (essays,
papers, life entries, simple pages) — see build_meta_html() in build.py.

- `translation_disclaimer: english` or `translation_disclaimer: korean` renders
  the matching fixed disclaimer text (edit the wording in the DISCLAIMERS dict
  in build.py — one edit updates every post using it).
- `other_disclaimer: "..."` renders free-form text of your choice in the same
  disclaimer box style. Markdown links (`[text](url)`) inside it are rendered
  as real links; other block-level markdown is not processed. Quote the value
  if it contains a colon (e.g. from a URL like `https://...`).
- `translation_disclaimer` and `other_disclaimer` can both be set at once —
  each renders as its own stacked box, translation disclaimer first.
- `first_published` / `last_edited` render as a small-caps metadata line,
  labeled "First Published"/"Last Edited" for content/en/, "최초 작성"/"최종 수정"
  for content/kr/ (inferred from the file's path).
- All of the above render as styled blocks (`.disclaimer`, `.post-meta` in
  designs/academic.css) inserted right after a leading epigraph blockquote if
  present, otherwise at the top of the body.
