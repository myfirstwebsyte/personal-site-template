# Set up your personal website

Use this guide when setting up a new copy of this website for its owner. It covers the one-time work: who owns the accounts, how to publish without a terminal, optional local preview, and connecting a custom domain through Porkbun.

Before you begin, identify these two values:

| Value | Example |
| --- | --- |
| GitHub username that owns the repository | `myfirstwebsyte` |
| Custom domain | `pratyushasangwan.com` |

In the steps below, replace `<github-username>` and `<your-domain>` with the values for the new site.

## One-time ownership and access

The website owner should:

1. Own the GitHub repository, or at least have admin access to it.
2. Keep two-factor authentication and recovery codes for their GitHub account.
3. Control the domain registrar account for `<your-domain>`, including its renewal payment method.
4. Confirm **Settings → Pages** uses **GitHub Actions** as the publishing source.
5. Install Obsidian if they want to write there.

Do not put passwords, recovery codes, or private drafts in this repository. A public GitHub repository makes every committed file public.

## First publishing setup — no terminal required

The owner can write and publish before installing any programming tools.

1. Install [GitHub Desktop](https://desktop.github.com/) and sign in with their GitHub account.
2. In GitHub Desktop, choose **File → Clone repository**, select the website repository, and choose a location on their computer.
3. Install [Obsidian](https://obsidian.md/). In Obsidian, choose **Open folder as vault** and select the cloned repository’s `content/` folder.
4. In Obsidian, duplicate `POST_TEMPLATE.md`, move the copy into `writing/`, rename it, and write the post.
5. Return to GitHub Desktop. Under **Changes**, add a short summary, click **Commit to main**, then **Push origin**.
6. GitHub Actions publishes the site automatically. They can open the website from the repository’s **Settings → Pages** screen.

The `content/` folder is the owner’s writing desk. GitHub Desktop carries saved changes from that desk to GitHub; GitHub then rebuilds the public website.

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

## Connect a custom domain through Porkbun

Use `<your-domain>` as the main address. `www.<your-domain>` will redirect to it. You need access to the GitHub account that owns the repository and the Porkbun account that owns the domain.

### 1. Verify that the GitHub account owns the domain

Verification is a security step. It prevents another GitHub account from attaching this domain to a Pages site.

1. On GitHub, sign in as `<github-username>`, click the profile picture, then choose **Settings**.
2. In the left sidebar, under **Code, planning, and automation**, choose **Pages**.
3. In **Verified domains**, click **Add a domain**.
4. Enter `<your-domain>`, then click **Add domain**.
5. GitHub will display a DNS `TXT` record. Leave this tab open; Porkbun needs the exact host and value that GitHub shows.

### 2. Add the verification record in Porkbun

1. Sign in to Porkbun. Choose **Account → Domain Management**.
2. Find `<your-domain>`, click **Details**, then find **DNS Records** and select its edit icon.
3. Add the GitHub-provided record:

   | Porkbun field | Value |
   | --- | --- |
   | Type | `TXT` |
   | Host | The host GitHub supplied, without `.<your-domain>` at the end |
   | Answer | Paste the GitHub-provided value exactly |
   | TTL | Keep the default |

4. Click **Add**.
5. Return to GitHub and click **Verify**. If it is not ready yet, wait 10–15 minutes and use **Continue verifying** from the verified-domains screen.

Keep the TXT record after verification. It is part of the domain’s security.

### 3. Connect the repository to the domain

Do this before pointing the website DNS records at GitHub.

1. Open the new website repository on GitHub.
2. Choose **Settings → Pages**.
3. Confirm that **Source** is **GitHub Actions**.
4. Under **Custom domain**, enter `<your-domain>` and click **Save**.

### 4. Point Porkbun at GitHub Pages

For a new personal domain without email hosting, Porkbun’s **Quick DNS Config** is the simplest option.

1. Return to Porkbun’s **Manage DNS Records** window for `<your-domain>`.
2. Scroll to **Quick DNS Config**.
3. Click **Github**, then confirm with **OK** when Porkbun asks whether to reconfigure the website DNS records.
4. In the **Additional DNS Requirements** window, add the `www` record:

   | Field | Value |
   | --- | --- |
   | Host | `www` |
   | Answer | `<github-username>.github.io` |

5. Click **Submit**. Porkbun should show a success message and list the new GitHub Pages records under **Current Records**.

Do not use Quick DNS Config if this domain already has email hosting or other DNS services you need to keep. In that case, preserve its mail records and add these website records manually instead:

| Type | Host | Answer |
| --- | --- | --- |
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `<github-username>.github.io` |

Remove only conflicting website records such as an old `@` A record, an old `www` CNAME, a `www` URL-forwarding rule, or Porkbun’s parking record. Do not remove mail `MX` records or unrelated `TXT` records. Do not create wildcard records such as `*.<your-domain>`.

### 5. Publish the site at its real address

1. In the repository, go to **Settings → Secrets and variables → Actions → Variables**.
2. Create this repository variable:

   ```text
   Name: SITE_URL
   Value: https://<your-domain>
   ```

3. Go to the **Actions** tab.
4. Open **Build and deploy personal site**, choose **Run workflow**, then choose **Run workflow** again.

This tells Pelican to generate its sitemap, feed, and page links using the custom domain.

### 6. Check the result and enable HTTPS

1. Return to **Settings → Pages**.
2. Use **Check again** if GitHub still reports a DNS warning. A successful main-domain check can appear before the `www` check finishes; wait 15–30 minutes before changing records again.
3. Once available, select **Enforce HTTPS**.
4. Visit both `https://<your-domain>` and `https://www.<your-domain>`. The `www` address should redirect to the main address.

DNS can take up to 24 hours to propagate, although it often completes much sooner. GitHub may take a little longer to finish the HTTPS certificate.

This project publishes through a GitHub Actions workflow, so it does not need a `CNAME` file in the repository.

For the latest reference material, see [Porkbun’s GitHub Pages guide](https://kb.porkbun.com/article/64-how-to-connect-your-domain-to-github-pages), [GitHub’s custom-domain guide](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), and [GitHub’s domain-verification guide](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages).
