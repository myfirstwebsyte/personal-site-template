from __future__ import annotations

AUTHOR = "Your name"
SITENAME = "Your name"
SITESUBTITLE = "A small corner of the internet."
SITEURL = ""
TIMEZONE = "Asia/Kolkata"
DEFAULT_LANG = "en"

PATH = "content"
ARTICLE_PATHS = ["writing"]
PAGE_PATHS = ["pages"]
STATIC_PATHS = ["images", "extra"]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
}
THEME = "theme"

ARTICLE_URL = "writing/{slug}/"
ARTICLE_SAVE_AS = "writing/{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

DIRECT_TEMPLATES = ["index", "archives", "404"]
ARCHIVES_SAVE_AS = "archive/index.html"
ARCHIVES_URL = "archive/"
DEFAULT_PAGINATION = 10

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SOCIAL = []
MENUITEMS = []
