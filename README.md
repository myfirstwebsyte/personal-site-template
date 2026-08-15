# Personal site template

A small personal website that turns Markdown into a live site with Pelican and GitHub Pages.

## Write and publish

1. Create a post with `make post TITLE="My first note"`, or copy `docs/POST_TEMPLATE.md` to `content/writing/`.
2. Replace the metadata and write in Markdown.
3. Run `make check`.
4. Commit the file to `main`. GitHub Actions builds and publishes the site.

For an unpublished draft, use `content/private-notes/`. Git ignores this local folder, so private writing never enters the public repository.

To write in Obsidian, open the `content/` folder as a vault. See [the Obsidian guide](docs/OBSIDIAN.md).

## Work locally

```bash
uv sync
make dev
```

Then open http://localhost:8090. `make dev` rebuilds after each saved change.

Use `make build` to generate the site once, and `make check` before publishing.

## Before the first deployment

Follow [the GitHub Pages setup guide](docs/SETUP_GITHUB_PAGES.md). It explains the one-time Pages setting and how to add a custom domain.

If a local preview looks unstyled or prints an error, start with [troubleshooting](docs/TROUBLESHOOTING.md).

## Give this site to its owner

See [the handoff guide](docs/HANDOFF.md). The recipient should own the GitHub repository, domain registrar account, and two-factor authentication recovery codes.
