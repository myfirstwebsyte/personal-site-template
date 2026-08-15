# Personal site template

A small personal website that turns Markdown into a live site with Pelican and GitHub Pages.

## Write and publish

1. Copy `docs/POST_TEMPLATE.md` to a new file, such as `content/writing/my-first-note.md`.
2. Replace its metadata and write in Markdown.
3. Commit the file to `main`. GitHub Actions builds and publishes the site.

For an unpublished draft, keep the file outside this public repository or work on a branch until it is ready to merge into `main`.

## Work locally

```bash
uv sync
uv run pelican content
uv run pelican --listen
```

Then open http://localhost:8000.

## Before the first deployment

Follow [the GitHub Pages setup guide](docs/SETUP_GITHUB_PAGES.md). It explains the one-time Pages setting and how to add a custom domain.

## Give this site to its owner

See [the handoff guide](docs/HANDOFF.md). The recipient should own the GitHub repository, domain registrar account, and two-factor authentication recovery codes.
