# Give this website to its owner

Pratyusha now owns this GitHub repository. She should also control `pratyushasangwan.com`. You can remain a collaborator if she wants help, but she should not depend on your account to publish, renew the domain, or recover access.

## Ownership and access

Pratyusha should:

1. Keep two-factor authentication and recovery codes for her GitHub account.
2. Control the domain registrar account for `pratyushasangwan.com`, including its renewal payment method.
3. Confirm **Settings → Pages** uses **GitHub Actions** as the publishing source.
4. Install Obsidian if she wants to write there.

Do not put passwords, recovery codes, or private drafts in this repository. A public GitHub repository makes every committed file public.

## Her first publishing setup — no terminal required

After she accepts the transfer:

She can write and publish before installing any programming tools.

1. Install [GitHub Desktop](https://desktop.github.com/) and sign in with her GitHub account.
2. In GitHub Desktop, choose **File → Clone repository**, select the transferred repository, and choose a location on her computer.
3. Install [Obsidian](https://obsidian.md/). In Obsidian, choose **Open folder as vault** and select the cloned repository’s `content/` folder.
4. In Obsidian, duplicate `POST_TEMPLATE.md`, move the copy into `writing/`, rename it, and write the post.
5. Return to GitHub Desktop. Under **Changes**, add a short summary, click **Commit to main**, then **Push origin**.
6. GitHub Actions publishes the site automatically. She can open the website from the repository’s **Settings → Pages** screen.

The `content/` folder is her writing desk. GitHub Desktop carries saved changes from that desk to GitHub; GitHub then rebuilds the public website.

Read [write in Obsidian](OBSIDIAN.md) first. The [configuration guide](CONFIGURATION.md) explains the settings she can change later.

## Optional: preview the site before publishing

Local preview is useful, but it is not required for writing or publishing. It adds one tool: `uv`, which downloads the project’s Python tools into an isolated project folder.

1. Install `uv` using one official method:

   - macOS with Homebrew: `brew install uv`
   - macOS without Homebrew: `curl -LsSf https://astral.sh/uv/install.sh | sh`
   - Windows: `winget install --id=astral-sh.uv -e`

2. Close and reopen the terminal, then check the installation:

   ```bash
   uv --version
   ```

3. In GitHub Desktop, choose **Repository → Open in Terminal**. Then run:

   ```bash
   uv sync
   make dev
   ```

4. Open `http://localhost:8090/`. Saved changes in `content/` and `theme/` rebuild automatically.

`uv sync` only needs to run again when the project’s Python dependencies change. Use `make check` before a more involved publishing change; it builds the site once and turns warnings into errors.

## Add `pratyushasangwan.com`

The repository transfer is already complete, so the domain can now be secured to Pratyusha’s GitHub account.

1. In her GitHub **profile Settings → Pages**, choose **Add a domain** and enter `pratyushasangwan.com`.
2. GitHub shows a DNS `TXT` record. Add that exact record at the domain registrar, wait for it to appear, then click **Verify** in GitHub. Keep the TXT record afterwards.
3. In the repository, open **Settings → Pages**. Under **Custom domain**, enter `pratyushasangwan.com` and save it **before** changing the website DNS records.
4. At the domain registrar, add these four `A` records for the root (`@`) domain:

   ```text
   185.199.108.153
   185.199.109.153
   185.199.110.153
   185.199.111.153
   ```

5. Also add a `CNAME` record for `www` that points to:

   ```text
   <pratyusha-github-username>.github.io
   ```

   Use her GitHub username and do not include the repository name.

6. In **Settings → Secrets and variables → Actions → Variables**, add:

   ```text
   SITE_URL = https://pratyushasangwan.com
   ```

7. Run the deployment workflow again. When GitHub offers it, enable **Enforce HTTPS**.

DNS and certificates can take up to 24 hours. Do not use wildcard DNS records such as `*.pratyushasangwan.com`.

This project publishes through a GitHub Actions workflow, so it does not need a `CNAME` file in the repository.

For GitHub’s current screens and provider-specific details, see [managing a GitHub Pages custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).
