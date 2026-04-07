#!/usr/bin/env python3
"""
Build script to generate HTML files from markdown content + Jinja2 templates.
Supports bilingual output: English at root, Korean at /kr/.
"""

import os
import markdown
import yaml
from pathlib import Path
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from collections import defaultdict

base_dir = Path(__file__).parent
template_dir = base_dir / 'templates'
env = Environment(loader=FileSystemLoader(template_dir))


def read_md(filepath):
    """Parse YAML frontmatter + markdown body → (meta dict, html string)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        raw = f.read()

    meta = {}
    body = raw

    if raw.startswith('---'):
        parts = raw.split('---', 2)
        if len(parts) >= 3:
            meta = yaml.safe_load(parts[1]) or {}
            body = parts[2].strip()

    html = markdown.markdown(body, extensions=['tables', 'fenced_code'])
    return meta, html


def render(template_name, output_path, **kwargs):
    """Render a template and write to output_path."""
    template = env.get_template(template_name)
    html = template.render(**kwargs)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {output_path}")


def scan_entries(content_subdir, url_prefix, lang):
    """Scan a directory of markdown files and return sorted entry list."""
    entries = []
    d = Path(content_subdir)
    if not d.exists():
        return entries

    for md_file in sorted(d.glob('*.md')):
        meta, _ = read_md(md_file)
        slug = md_file.stem
        entry = {
            'slug': slug,
            'title': meta.get('title', slug),
            'date': str(meta.get('date', '2026-01-01')),
            'description': meta.get('description', ''),
            'url': f"{url_prefix}{slug}.html",
        }
        entries.append(entry)

    entries.sort(key=lambda e: e['date'], reverse=True)
    return entries


def group_by_year(entries):
    """Group entries by year, returning list of (year, items) sorted descending."""
    by_year = defaultdict(list)
    for e in entries:
        year = e['date'][:4]
        by_year[year].append(e)
    return sorted(by_year.items(), reverse=True)


def scan_life_entries(content_dir):
    """Scan life/ subpages, return list sorted by start date."""
    entries = []
    d = Path(content_dir) / 'life'
    if not d.exists():
        return entries
    for md_file in sorted(d.glob('*.md')):
        meta, _ = read_md(md_file)
        full_title = meta.get('title', md_file.stem)
        if ': ' in full_title:
            date_range, movie_line = full_title.split(': ', 1)
        else:
            date_range, movie_line = full_title, None
        entries.append({
            'slug': md_file.stem,
            'title': full_title,
            'date_range': date_range,
            'movie_line': movie_line,
            'start': meta.get('start', md_file.stem),
        })
    entries.sort(key=lambda e: e['start'])
    return entries


def build_life_timeline_html(entries, lang):
    """Generate HTML list of life period links for the about page."""
    prefix = '/kr/life/' if lang == 'kr' else '/life/'
    items = ''.join(
        f'<li><a href="{prefix}{e["slug"]}.html">{e["title"]}</a></li>\n'
        for e in entries
    )
    return f'<ul>\n{items}</ul>'


def build_lang(lang):
    """Build all pages for a given language ('en' or 'kr')."""
    content_dir = base_dir / 'content' / lang
    out_root = base_dir if lang == 'en' else base_dir / 'kr'

    nav_lang = lang

    # ── Life subpages ─────────────────────────────────────────────────────────
    life_entries = scan_life_entries(content_dir)

    for entry in life_entries:
        md_path = content_dir / 'life' / f"{entry['slug']}.md"
        meta, html_body = read_md(md_path)
        out_file = out_root / 'life' / f"{entry['slug']}.html"
        render('essay.html', out_file,
               title=entry['date_range'],
               essay_title=entry['date_range'],
               content=html_body,
               lang=nav_lang,
               page_slug=f"life/{entry['slug']}.html",
               show_lang_toggle=True,
               include_mathjax=False,
               include_accordion=False,
               custom_styles=None)

    # ── Simple pages ──────────────────────────────────────────────────────────
    simple_pages = ['index', 'about', 'notes', 'books', 'courses', 'misc']
    for page in simple_pages:
        md_path = content_dir / f'{page}.md'
        if not md_path.exists():
            print(f"Warning: {md_path} not found, skipping")
            continue

        meta, html_body = read_md(md_path)
        title = meta.get('title', page.capitalize())

        # Append life timeline to about page
        if page == 'about' and life_entries:
            html_body += build_life_timeline_html(life_entries, lang)

        out_file = out_root / 'index.html' if page == 'index' else out_root / f'{page}.html'
        page_slug = 'index.html' if page == 'index' else f'{page}.html'

        render('simple.html', out_file,
               title=title,
               content=html_body,
               lang=nav_lang,
               page_slug=page_slug,
               show_lang_toggle=False,
               include_mathjax=False,
               include_accordion=False,
               custom_styles=None)

    # ── Essay pages ───────────────────────────────────────────────────────────
    essay_url_prefix = '/essays/' if lang == 'en' else '/kr/essays/'
    essays = scan_entries(content_dir / 'essays', essay_url_prefix, lang)

    for essay in essays:
        md_path = content_dir / 'essays' / f"{essay['slug']}.md"
        meta, html_body = read_md(md_path)
        out_file = out_root / 'essays' / f"{essay['slug']}.html"
        page_slug = f"essays/{essay['slug']}.html"
        essay_date = datetime.strptime(essay['date'], '%Y-%m-%d').strftime('%B %-d, %Y') if essay.get('date') else ''

        render('essay.html', out_file,
               title=essay['title'],
               essay_title=essay['title'],
               essay_date=essay_date,
               content=html_body,
               lang=nav_lang,
               page_slug=page_slug,
               show_lang_toggle=True,
               include_mathjax=False,
               include_accordion=False,
               custom_styles=None)

    # ── Paper pages ───────────────────────────────────────────────────────────
    paper_url_prefix = '/papers/' if lang == 'en' else '/kr/papers/'
    papers = scan_entries(content_dir / 'papers', paper_url_prefix, lang)

    for paper in papers:
        md_path = content_dir / 'papers' / f"{paper['slug']}.md"
        meta, html_body = read_md(md_path)
        out_file = out_root / 'papers' / f"{paper['slug']}.html"
        page_slug = f"papers/{paper['slug']}.html"
        essay_date = datetime.strptime(paper['date'], '%Y-%m-%d').strftime('%B %-d, %Y') if paper.get('date') else ''

        render('essay.html', out_file,
               title=paper['title'],
               essay_title=paper['title'],
               essay_date=essay_date,
               content=html_body,
               lang=nav_lang,
               page_slug=page_slug,
               show_lang_toggle=False,
               include_mathjax=False,
               include_accordion=False,
               custom_styles=None)

    # ── Listing pages ─────────────────────────────────────────────────────────
    render('list.html', out_root / 'essays.html',
           title='Essays',
           entries_by_year=group_by_year(essays),
           lang=nav_lang,
           page_slug='essays.html',
           show_lang_toggle=True,
           include_mathjax=False,
           include_accordion=False,
           custom_styles=None)

    render('list.html', out_root / 'papers.html',
           title='Research',
           entries_by_year=group_by_year(papers),
           lang=nav_lang,
           page_slug='papers.html',
           show_lang_toggle=False,
           include_mathjax=False,
           include_accordion=False,
           custom_styles=None)


def build_kr_essays():
    """Build Korean essay pages, essays listing, and about page."""
    content_dir = base_dir / 'content' / 'kr'
    out_root = base_dir / 'kr'

    # ── Korean life pages ─────────────────────────────────────────────────────
    life_entries = scan_life_entries(content_dir)
    for entry in life_entries:
        md_path = content_dir / 'life' / f"{entry['slug']}.md"
        meta, html_body = read_md(md_path)
        render('essay.html', out_root / 'life' / f"{entry['slug']}.html",
               title=entry['date_range'],
               essay_title=entry['date_range'],
               content=html_body,
               lang='kr',
               page_slug=f"life/{entry['slug']}.html",
               show_lang_toggle=True,
               include_mathjax=False,
               include_accordion=False,
               custom_styles=None)

    essay_url_prefix = '/kr/essays/'
    essays = scan_entries(content_dir / 'essays', essay_url_prefix, 'kr')

    for essay in essays:
        md_path = content_dir / 'essays' / f"{essay['slug']}.md"
        meta, html_body = read_md(md_path)
        out_file = out_root / 'essays' / f"{essay['slug']}.html"
        essay_date = datetime.strptime(essay['date'], '%Y-%m-%d').strftime('%Y년 %-m월 %-d일') if essay.get('date') else ''
        render('essay.html', out_file,
               title=essay['title'],
               essay_title=essay['title'],
               essay_date=essay_date,
               content=html_body,
               lang='kr',
               page_slug=f"essays/{essay['slug']}.html",
               show_lang_toggle=True,
               include_mathjax=False,
               include_accordion=False,
               custom_styles=None)

    render('list.html', out_root / 'essays.html',
           title='글',
           entries_by_year=group_by_year(essays),
           lang='kr',
           page_slug='essays.html',
           show_lang_toggle=True,
           include_mathjax=False,
           include_accordion=False,
           custom_styles=None)


def main():
    print("Building English pages...")
    build_lang('en')
    print("\nBuilding Korean essay pages...")
    build_kr_essays()
    print("\nBuild complete!")


if __name__ == '__main__':
    main()
