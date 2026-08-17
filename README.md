# Personal site template

A small personal website that turns Markdown into a live site with Pelican and GitHub Pages.

## New writer? Start here

You do not need Python or a terminal to write and publish. Use Obsidian to edit the `content/` folder and GitHub Desktop to commit and push the change. GitHub builds the website for you. Follow [the handoff guide](docs/HANDOFF.md) for the first setup.

## Write and publish

1. Without local tools: duplicate `content/POST_TEMPLATE.md` in Obsidian and move the copy to `content/writing/`.
2. With local tools: run `make post TITLE="My first note"`.
3. Replace the metadata and write in Markdown.
4. Optionally run `make check`.
5. Commit the file to `main`. GitHub Actions builds and publishes the site.

For an unpublished draft, use `content/private-notes/`. Git ignores this local folder, so private writing never enters the public repository.

To write in Obsidian, open the `content/` folder as a vault. See [the Obsidian guide](docs/OBSIDIAN.md).

To understand where the site’s name, folders, URLs, theme, and publishing behavior are configured, read [the configuration guide](docs/CONFIGURATION.md).

## Work locally

```bash
uv sync
make dev
```

Then open http://localhost:8090. `make dev` rebuilds after each saved change.

Use `make build` to generate the site once, and `make check` before publishing.

## Before the first deployment

Follow [the GitHub Pages setup guide](docs/SETUP_GITHUB_PAGES.md). It explains the one-time Pages setting and how to add a custom domain.

For likely local-writing problems, start with [troubleshooting](docs/TROUBLESHOOTING.md).

## Give this site to its owner

See [the handoff guide](docs/HANDOFF.md). The recipient should own the GitHub repository, domain registrar account, and two-factor authentication recovery codes.
