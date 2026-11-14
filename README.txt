TERRA NOVA DEVELOPMENT — ARTICLES 109–111 WEBSITE PACKAGE

Contents:
- articles/article-109.html through article-111.html
- assets/article-109-original.png through article-111-original.png
- assets/article-109-social.jpg through article-111-social.jpg (1200x630)
- documents/*.docx — three illustrated Word documents
- update_existing_index.py — idempotent updater for a local copy of the existing website

The GitHub repository index.html has ALSO been updated directly to include all 111 scrollable index entries and all three homepage panels. Do not replace your current index.html with an older copy.

Extract files into your existing TerraNovaDevelopment repository root, preserving the articles/assets/documents directories. Commit and push in GitHub Desktop. The direct index update is already committed on GitHub.

Run python update_existing_index.py only if your local index.html does not yet include the three entries. This updater preserves all older content.

Sharing metadata is included separately in every HTML page: Open Graph and Twitter summary_large_image cards reference the corresponding 1200x630 social card via HTTPS on Render.
