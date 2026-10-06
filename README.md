# isr413.github.io

Personal website, digital business card, and blog for **Ian Riley**, Instructional Assistant Professor of Computer Science at the Tandy School of Computer Science, University of Tulsa.

🌐 **Live site:** https://isr413.github.io

---

## Purpose

Visitors usually arrive by scanning a QR code on a business card, slide, poster, or office door, often on a phone. They should be able to:

1. See who I am and what I work on within seconds.
2. Email me or save my details to their phone in one tap.
3. Find my blog posts, interactive apps, and slide decks.

## Tech stack

- **Jekyll 3.10**, built and deployed automatically by GitHub Pages from `main`
- Plain HTML + CSS, with a few lines of vanilla JS for the Share button
- Plugins (all supported by GitHub Pages): `jekyll-seo-tag` (Open Graph / Twitter cards), `jekyll-feed` (RSS at `/blog/feed.xml`), `jekyll-sitemap`
- Visual style: the **Slate & Gold** palette from the slide-deck engine, with light and dark modes. The slide-deck builder skill lives locally in `.claude/skills/` and is git-ignored, so it is never committed or published.

## Repository structure

```
.
├── _config.yml           # Site identity, contact details, social links, nav
├── _data/
│   ├── apps.yml          # Listing for /apps/  (title, url, description, tags)
│   └── decks.yml         # Listing for /decks/ (title, url, course, description, tags)
├── _includes/            # head, icons, listing card
├── _layouts/             # default, page, post
├── _posts/               # Blog posts (YYYY-MM-DD-slug.md)
├── index.html            # Home / business card page with QR code
├── blog/index.html       # Post list
├── apps/                 # Single-file HTML apps, copied as-is + index.html listing
├── decks/                # Single-file HTML decks, copied as-is + index.html listing
├── qr.html               # Printable QR page
├── contact.vcf           # vCard, generated from _config.yml
├── 404.html
├── assets/
│   ├── css/style.css
│   ├── img/              # profile.jpg, favicon.svg, apple-touch-icon.png
│   └── qr/               # site-qr.svg (print) and site-qr.png (slides)
├── scripts/generate_qr.py
└── Gemfile
```

## Common tasks

**Write a blog post.** Add `_posts/YYYY-MM-DD-title.md`:

```markdown
---
title: My post title
description: One-line summary shown in post lists and link previews.
---

Post body in Markdown.
```

**Add an interactive app or slide deck.** Copy the single HTML file into `apps/` or `decks/` *without adding front matter*, so Jekyll publishes it byte-for-byte. Then add an entry to `_data/apps.yml` or `_data/decks.yml`. Use lowercase, hyphenated filenames, for example `decks/graph-traversal.html`.

**Update contact details or social links.** Edit `person:` and `social:` in `_config.yml`. The home page and `contact.vcf` both read from these settings.

**Regenerate the QR code.** This is only needed if the site URL changes.

```bash
pip install segno
python scripts/generate_qr.py
```

## Local development

```bash
bundle install                # once
bundle exec jekyll serve      # http://localhost:4000, rebuilds on save
```

The Gemfile pins the Jekyll version and plugins that GitHub Pages uses, plus a few gems that newer Rubies no longer bundle. It does not use the `github-pages` gem, because that gem does not install on Ruby 4.

## Deployment

Pushing to `main` deploys automatically. In the repository's **Settings → Pages**, set the source to **Deploy from a branch → `main` / root**. You can follow the build in the **Actions** tab.

## License

Content © Ian Riley. Code is available under the MIT License.
