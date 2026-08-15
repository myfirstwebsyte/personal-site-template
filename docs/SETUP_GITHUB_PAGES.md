# Deploy this site with GitHub Pages

## First deployment

1. Create a **public** GitHub repository and push this project to its `main` branch.
2. In the repository, open **Settings → Pages** and set **Source** to **GitHub Actions**.
3. Open the **Actions** tab and wait for “Build and deploy personal site” to finish. GitHub will show the temporary `github.io` address.

The workflow installs the locked Python dependencies, runs Pelican, and uploads only the generated `output/` folder. The Markdown source remains in the repository.

## Add a custom domain

1. In **Settings → Pages**, add and verify the custom domain **before changing DNS**.
2. At the domain registrar, configure the root domain and `www` according to GitHub's current instructions. Do not use wildcard DNS records.
3. In **Settings → Secrets and variables → Actions**, add a repository variable named `SITE_URL` with the exact value `https://your-domain.example`.
4. Run the deployment workflow again. This makes Pelican use the custom domain in its canonical links.
5. When GitHub offers it, enable **Enforce HTTPS**.

DNS and certificate changes can take time to propagate. Keep the temporary GitHub Pages URL available until the custom domain is working.
