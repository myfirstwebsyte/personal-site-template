# Give this website to its owner

The intended end state is simple: Pratyusha owns the GitHub repository and `pratyushasangwan.com`. You can remain a collaborator if she wants help, but she should not depend on your account to publish, renew the domain, or recover access.

## Before you transfer anything

Pratyusha needs:

1. A personal GitHub account with two-factor authentication enabled.
2. Access to the domain registrar account for `pratyushasangwan.com`, including its renewal payment method.
3. An installed copy of Obsidian if she wants to write there.

Do not put passwords, recovery codes, or private drafts in this repository. A public GitHub repository makes every committed file public.

## Give her the repository

Transferring the repository is better than asking her to clone it: a clone gives her a copy, while a transfer makes her the actual owner.

1. On GitHub, open this repository’s **Settings**.
2. At the bottom of **General**, find **Danger Zone** and choose **Transfer**.
3. Enter Pratyusha’s GitHub username and confirm the repository name.
4. She accepts GitHub’s transfer invitation within 24 hours.
5. After she accepts, she opens **Settings → Pages** and confirms that the source is **GitHub Actions**.

GitHub automatically keeps you as a collaborator after a personal-account transfer. Remove yourself later if she prefers complete independence.

## Her first local setup

After she accepts the transfer:

1. On the repository page, click **Code**, copy the HTTPS address, and clone it to her computer.
2. In a terminal inside the cloned folder, run:

   ```bash
   uv sync
   make dev
   ```

3. Open `http://localhost:8090/` to see the site.
4. In Obsidian, choose **Open folder as vault** and select the repository’s `content/` folder.
5. Read these three short guides:
   - [write in Obsidian](OBSIDIAN.md);
   - [configure the site](CONFIGURATION.md); and
   - [common local problems](TROUBLESHOOTING.md).

To publish a new post, she creates a Markdown file in `content/writing/`, runs `make check`, then commits and pushes to `main`.

## Add `pratyushasangwan.com`

Do this **after** the repository transfer, so the domain is secured to Pratyusha’s GitHub account.

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

For GitHub’s current screens and provider-specific details, see [transferring a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository) and [managing a GitHub Pages custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).
