from __future__ import annotations

import os
import runpy
from pathlib import Path

_base_settings = runpy.run_path(
    Path(__file__).with_name("pelicanconf.py")
)
for _setting_name, _setting_value in _base_settings.items():
    if _setting_name.isupper():
        globals()[_setting_name] = _setting_value

# GitHub Actions supplies the project-site URL automatically. When the owner
# connects a custom domain, they set the public SITE_URL repository variable.
_repository = os.environ.get("GITHUB_REPOSITORY", "")
_owner, _, _repository_name = _repository.partition("/")
_fallback_url = (
    f"https://{_owner}.github.io/{_repository_name}"
    if _owner and _repository_name
    else ""
)
# GitHub Actions defines SITE_URL as an empty string until the repository owner
# creates the optional variable. Treat that as absent so project Pages sites use
# their default https://owner.github.io/repository-name base path.
SITEURL = (os.environ.get("SITE_URL") or _fallback_url).rstrip("/")
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

# These require an absolute public URL, so they are generated only for the
# published site rather than during local previews.
PLUGINS = ["sitemap"]
FEED_ALL_RSS = "feeds/all.rss.xml"
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.7, "pages": 0.5, "indexes": 0.5},
    "changefreqs": {"articles": "monthly", "pages": "monthly", "indexes": "weekly"},
}
