# Troubleshooting

## The terminal mentions `/favicon.ico`

Browsers ask every website for a tiny tab icon named `favicon.ico`. This starter does not include one yet, so Pelican prints that request. The message does not break the page or publishing.

## `uv` is not found

You only need `uv` for local preview. Follow the **Optional: preview the site before publishing** section in [the setup guide](SETUP.md), then run `uv sync` again.

## The new post is missing

Check all three things:

1. The file ends in `.md`.
2. It lives in `content/writing/`.
3. The first lines contain `Title:`, `Date:`, and `Slug:`.

Run `make check` for a clearer build error.

## Port 8090 is already in use

Another local server is already running. Return to the terminal where it started and press `Ctrl + C`. Then run `make dev` again.

## The published site has not changed

Make sure the commit is on the `main` branch. Then open the repository’s **Actions** tab and wait for the deployment workflow to finish. Refresh the site with `Cmd + Shift + R`.
