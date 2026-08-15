"""Create a new Markdown post with Pelican metadata."""

from __future__ import annotations

import argparse
import re
import unicodedata
from datetime import date
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
WRITING_DIRECTORY = PROJECT_ROOT / "content" / "writing"


def slugify(title: str) -> str:
    normalized = unicodedata.normalize("NFKD", title)
    ascii_title = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_title.lower()).strip("-")
    return slug or "untitled-post"


def available_path(slug: str) -> Path:
    candidate = WRITING_DIRECTORY / f"{slug}.md"
    number = 2
    while candidate.exists():
        candidate = WRITING_DIRECTORY / f"{slug}-{number}.md"
        number += 1
    return candidate


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a new Pelican blog post.")
    parser.add_argument("title", help="The post title")
    arguments = parser.parse_args()

    title = arguments.title.strip()
    if not title:
        parser.error("title cannot be empty")

    slug = slugify(title)
    destination = available_path(slug)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        "\n".join(
            [
                f"Title: {title}",
                f"Date: {date.today().isoformat()}",
                f"Slug: {destination.stem}",
                "Tags: writing",
                "Summary: One sentence that tells readers what they will find here.",
                "",
                "Start writing here.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(destination.relative_to(PROJECT_ROOT))


if __name__ == "__main__":
    main()
