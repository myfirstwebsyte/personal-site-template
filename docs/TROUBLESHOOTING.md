# Troubleshooting

## The local site has no styling

If the terminal says it cannot find a path like this:

```text
/pratyushasangwan.com/theme/css/site.css
```

open `pelicanconf.py` and make sure this line is blank:

```python
SITEURL = ""
```

Then stop the local server with `Ctrl + C` and start it again with `make dev`.

`pelicanconf.py` is for local previewing. The public address belongs in the GitHub repository variable named `SITE_URL`, including `https://`, after the custom domain is connected.

## The terminal mentions `/favicon.ico`

Browsers ask every website for a tiny tab icon named `favicon.ico`. This starter does not include one yet, so Pelican prints that request. The message does not break the page or publishing.

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
