# Configure the site

`pelicanconf.py` is the site’s control panel. It is a small Python file that Pelican reads while building the website.

Visitors never download or run this file. Pelican uses it to decide which Markdown files become pages, which theme to use, where links should point, and what site-wide text to insert.

```text
content/ + pelicanconf.py + theme/
                 |
                 v
          Pelican builds HTML
                 |
                 v
        GitHub Pages serves the site
```

For example, `SITENAME = "Muffin Logic"` becomes visible because the templates contain `{{ SITENAME }}`. When Pelican builds the site, it replaces that placeholder with the configured name.

## The two configuration files

| File | When it is used | What it controls |
| --- | --- | --- |
| `pelicanconf.py` | `make dev` and normal local builds | The site’s everyday settings and local preview. |
| `publishconf.py` | GitHub Actions during publishing | The published version: its public address, RSS feed, and sitemap. |

`publishconf.py` begins by loading `pelicanconf.py`, then changes only the settings that must be different on the public internet. This keeps local preview simple while keeping the published links correct.

## Settings you can safely personalize

These are the normal first edits in `pelicanconf.py`:

```python
AUTHOR = "Pratyusha Sangwan"
SITENAME = "Muffin Logic"
SITESUBTITLE = "My corner of the internet."
TIMEZONE = "Asia/Kolkata"
PORT = 8090
```

| Setting | What changes |
| --- | --- |
| `AUTHOR` | The default author information for posts. The current theme does not print it, but Pelican retains it as post metadata. |
| `SITENAME` | The name in the browser tab, navigation, homepage, RSS feed, and sharing metadata. |
| `SITESUBTITLE` | The short description on the homepage and in sharing metadata. |
| `TIMEZONE` | How Pelican interprets dates and times in posts. |
| `PORT` | The local preview address. `PORT = 8090` means `http://localhost:8090/`. |

Text values need quotation marks. Numbers such as `8090` do not.

All Pelican setting names use uppercase letters. In this project, `publishconf.py` also copies only uppercase names from `pelicanconf.py` into the production build.

## How content becomes a website

These settings map folders to jobs:

```python
PATH = "content"
ARTICLE_PATHS = ["writing"]
PAGE_PATHS = ["pages"]
STATIC_PATHS = ["images", "extra"]
```

| Folder | Pelican treats its files as |
| --- | --- |
| `content/writing/` | Blog posts. |
| `content/pages/` | Permanent pages such as About and Now. |
| `content/images/` | Files to copy to the public site without changing them. |
| `content/extra/` | Other public site files, such as `robots.txt`. |

This is also the Obsidian vault structure. Writing a Markdown file in `writing/` makes it a candidate post; moving the same file into `pages/` makes it a permanent page instead.

## How links are formed

Each post has a `Slug` in its metadata. With these settings:

```python
ARTICLE_URL = "writing/{slug}/"
ARTICLE_SAVE_AS = "writing/{slug}/index.html"
```

a post with:

```md
Slug: a-small-idea
```

appears to readers at:

```text
/writing/a-small-idea/
```

`ARTICLE_URL` is the address readers use. `ARTICLE_SAVE_AS` is the generated file location that makes that address work. Keep the two settings aligned; changing one without the other can create broken links.

`PAGE_URL` and `PAGE_SAVE_AS` do the same job for permanent pages. A page with `Slug: about` appears at `/about/`.

## The homepage, archive, and theme

```python
THEME = "theme"
DIRECT_TEMPLATES = ["index", "archives", "404"]
ARCHIVES_SAVE_AS = "archive/index.html"
```

`THEME = "theme"` tells Pelican to use the project’s `theme/` folder.

| If you want to change… | Edit… |
| --- | --- |
| Homepage layout or text around the post list | `theme/templates/index.html` |
| Shared navigation and footer | `theme/templates/base.html` |
| The layout of an individual post | `theme/templates/article.html` |
| Colours, fonts, spacing, and visual style | `theme/static/css/site.css` |
| Archive page | `theme/templates/archives.html` |

`DIRECT_TEMPLATES` names the templates Pelican should generate even though they do not come from one Markdown file. Here, those are the homepage, archive, and 404 page.

## Production-only settings

Leave this local setting alone:

```python
SITEURL = ""
```

When GitHub Actions publishes the site, `publishconf.py` reads the `SITE_URL` repository variable and uses it as the real public address. For a custom domain, set that GitHub variable to a complete URL such as:

```text
https://pratyushasangwan.com
```

The production configuration also enables:

- `FEED_ALL_RSS`, which creates the RSS feed;
- `PLUGINS = ["sitemap"]`, which enables the sitemap generator; and
- `SITEMAP`, which controls the sitemap’s update hints for search engines.

These settings need the public URL, so they belong in `publishconf.py`, not the local configuration.

## A safe change routine

1. Change one setting.
2. Run `make dev` and open `http://localhost:8090/`.
3. Check the visible result.
4. Run `make check` before committing.
5. Commit to `main` to publish.

Avoid editing `output/`: it is generated from the real source files every time Pelican builds the site.

For every Pelican option beyond this guide, see the [official settings reference](https://docs.getpelican.com/en/stable/settings.html).
