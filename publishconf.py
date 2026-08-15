from __future__ import annotations

import os
import runpy
from pathlib import Path

_base_settings = runpy.run_path(Path(__file__).with_name("pelicanconf.py"))
for _setting_name, _setting_value in _base_settings.items():
    if _setting_name.isupper():
        globals()[_setting_name] = _setting_value

# GitHub Actions supplies the project-site URL automatically. When the owner
# connects a custom domain, they set the public SITE_URL repository variable.
_repository = os.environ.get("GITHUB_REPOSITORY", "")
_owner, _, _repository_name = _repository.partition("/")
_fallback_url = (
    f"https://{_owner}.github.io/{_repository_name}" if _owner and _repository_name else ""
)
SITEURL = os.environ.get("SITE_URL", _fallback_url).rstrip("/")
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True
