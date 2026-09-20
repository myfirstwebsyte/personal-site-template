# Write in Obsidian

This site’s `content/` folder is also an Obsidian vault. Open that folder in Obsidian:

1. Choose **Open folder as vault**.
2. Select the `content` folder inside this repository.
3. Write posts in `writing/` and permanent pages in `pages/`.

## Folder map

| Obsidian folder | What happens when you publish |
| --- | --- |
| `writing/` | Every Markdown file becomes a blog post. |
| `pages/` | Every Markdown file becomes a permanent page, such as About. |
| `images/` | Images for the site. |
| `private-notes/` | Local writing only. Git ignores it and Pelican does not publish it. |
| `extra/` | Site files such as `robots.txt`. Leave these alone for now. |

## Publish a note

1. Duplicate `POST_TEMPLATE.md` from the top level of the vault.
2. Move the copy into `writing/` and give it a clear filename, such as `my-first-note.md`.
3. Replace the title, date, slug, summary, and body text.
4. Save the note.
5. In GitHub Desktop, commit the change to `main` and push it. GitHub publishes the site automatically.

Local preview with `make dev` is optional. Follow the **Optional: preview the site before publishing** section in [the setup guide](SETUP.md) when you want it.

## Links

Use standard Markdown links in anything you plan to publish:

```md
[Read the About page](/about/)
```

Obsidian links such as `[[About]]` are useful inside a private vault, but Pelican does not turn them into website links in this starter.

## Privacy rule

A public GitHub repository makes every committed file public, even a file marked `Status: draft`. Keep personal drafts in `private-notes/` until they are ready to publish.
