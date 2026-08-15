from __future__ import annotations

AUTHOR = "Pratyusha Sangwan"
SITENAME = "Muffin Logic"
SITESUBTITLE = "My corner of the internet."
# This configuration is for local previewing. GitHub Actions supplies the
# public URL from the optional SITE_URL repository variable during publishing.
SITEURL = ""
TIMEZONE = "Asia/Kolkata"
DEFAULT_LANG = "en"

PORT = 8090
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

FEED_ALL_RSS = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Keep local preview quiet and fast. Production settings enable the sitemap
# plugin and RSS feed, both of which need the public SITEURL.
PLUGINS = []

SOCIAL = []
MENUITEMS = []
