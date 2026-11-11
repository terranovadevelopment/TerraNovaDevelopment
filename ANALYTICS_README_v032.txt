Terra Nova Development v032 — Cloudflare Web Analytics integration prepared.

52 HTML pages (homepage + 51 articles) contain a Cloudflare beacon placeholder.
Do NOT deploy as active analytics until the site's OWN Cloudflare token is configured.

1. In Cloudflare, open Web Analytics and add Terra Nova Development's actual public domain/site.
2. Copy the new 32-character token from its JavaScript beacon snippet.
3. Run: python configure_analytics.py YOUR_32_CHARACTER_CLOUDFLARE_TOKEN
4. Upload the updated website files to hosting.
5. Visit the public homepage and a few articles, then check the Cloudflare Web Analytics dashboard.

Do not reuse the Medicare for All token: it would mix reporting across sites.
The existing v031 SEO configuration instructions still apply.
