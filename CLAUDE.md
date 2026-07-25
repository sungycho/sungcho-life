# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A static personal website (sungcho.life) built with a small custom Python generator (`build.py`) — Markdown + YAML frontmatter content, rendered through Jinja2 templates. No JS framework, no build tool beyond the Python script, no test suite, no linter.

## Commands

```bash
pip install -r requirements.txt   # deps: markdown, pyyaml, jinja2
python3 build.py                  # regenerate all HTML from content/ + templates/
./switch_design.sh <name>         # swap static/style.css and rebuild in one step
```

`switch_design.sh` accepts `academic` (default), `original`, `brutalist`, `terminal`, or `swiss` — it copies `designs/<name>.css` over `static/style.css` (backing up the previous one to `static/style.css.backup` the first time) and then runs `python3 build.py`.

There is no dev server script; since output is plain static HTML, open the generated files directly or serve the repo root with any static file server.

## Architecture

**The generated HTML is committed to the repo, not gitignored.** `build.py` writes output directly into the repo root (`index.html`, `essays.html`, `essays/*.html`, `aphorism/*.html`, `papers/*.html`, `life/*.html`) and into `kr/` for the Korean site. GitHub Pages serves straight from the repo (custom domain via `CNAME` = `sungcho.life`), so after editing content or templates you must rerun `build.py` and commit the resulting HTML alongside the source changes — there is no CI build step.

**Bilingual content layout**: source lives in `content/en/` and `content/kr/`. English output goes to the repo root; Korean output goes to `kr/`. In practice only life, essay, and aphorism content is ever built for Korean — see the build-ordering note below. Every generated page that supports it carries a language-toggle link (simple pages and papers have `show_lang_toggle=False` regardless of language).

**Content types and their build path** (all logic in `build.py`):
- **Simple pages** — `index`, `about`, `notes`, `books`, `courses`, `misc`: one `.md` file each at `content/{lang}/{page}.md` → `simple.html` template → `{page}.html` (or `index.html`).
- **Essays** — `content/{lang}/essays/*.md` → `essay.html` template → `essays/{slug}.html`, plus a year-grouped listing at `essays.html` (`scan_entries` + `group_by_year`). Frontmatter: `title`, `date: YYYY-MM-DD`, optional `description`.
- **Aphorisms** — identical pattern to essays, under `aphorism/`.
- **Papers** — identical pattern under `papers/`, but `show_lang_toggle=False` (no Korean toggle).
- **Life timeline** — `content/{lang}/life/*.md`, one file per life period, filename and `start` frontmatter both `"YYYY-MM"`. `title` frontmatter is formatted `"<date range>: <quote/movie line>"` (e.g. `"09.2002 - 02.2009: Great men are not born great, they grow great"`); `scan_life_entries` splits on `": "` into `date_range` / `movie_line`. Entries render via `essay.html` under `life/{slug}.html` and are also appended as a linked list to the bottom of the About page by `build_life_timeline_html`.

**Template hierarchy**: `templates/base.html` (nav menu, single `static/style.css` link, optional MathJax via `include_mathjax`, optional accordion JS via `include_accordion`, optional inline `custom_styles`) is extended by `essay.html`, `list.html`, and `simple.html`. None of these flags are currently turned on anywhere in `build.py` — they exist as template hooks for content that hasn't been added yet.

**Non-obvious build ordering in `main()`**: it calls `build_lang('en')` and then `build_kr_essays()` — **`build_lang('kr')` is defined but never called.** This means Korean output is limited to whatever `build_kr_essays()` covers: `kr/life/*.html`, `kr/essays/*.html`, `kr/aphorism/*.html`, plus the `kr/essays.html` and `kr/aphorism.html` listings (with Korean date formatting, `%Y년 %-m월 %-d일`). There is currently **no Korean build for simple pages or papers** — no `kr/index.html`, `kr/about.html`, `kr/notes.html`, `kr/books.html`, `kr/courses.html`, `kr/misc.html`, or `kr/papers.html` are ever generated, even though `content/kr/about.md` and `content/kr/papers/` exist as source. If Korean papers or simple pages are ever wanted, `build_lang('kr')` would need to be invoked from `main()` (and its essay/aphorism date formatting fixed to match `build_kr_essays()`, since `build_lang()` always uses the English `strftime` pattern `%B %-d, %Y` regardless of `lang`).

**Design system**: `designs/*.css` holds five complete alternate stylesheets (academic, original, brutalist, terminal, swiss); only one is ever active, copied into `static/style.css` by `switch_design.sh`. `static/life/` holds images referenced from life entries (convention documented inline in each life `.md` file's HTML comment).

**`.personal/`** is a local-only, gitignored directory — not part of the built site.
