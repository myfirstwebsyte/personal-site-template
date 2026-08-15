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

1. Move or create the finished note in `writing/`.
2. Put the metadata at the very top of the file. Use `../docs/POST_TEMPLATE.md` as the model.
3. Save the note.
4. Run `make dev` to preview it, then `make check` before committing.

## Links

Use standard Markdown links in anything you plan to publish:

```md
[Read the About page](/about/)
```

Obsidian links such as `[[About]]` are useful inside a private vault, but Pelican does not turn them into website links in this starter.

## Privacy rule

A public GitHub repository makes every committed file public, even a file marked `Status: draft`. Keep personal drafts in `private-notes/` until they are ready to publish.
