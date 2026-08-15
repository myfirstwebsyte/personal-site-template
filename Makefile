.PHONY: dev build check post

dev:
	uv run pelican --listen --autoreload

build:
	uv run pelican content --delete-output-directory

check:
	SITE_URL=http://localhost:8090 uv run pelican content -s publishconf.py --fatal warnings

post:
	@test -n "$(TITLE)" || (echo 'Usage: make post TITLE="A title"'; exit 1)
	uv run python scripts/new_post.py "$(TITLE)"
