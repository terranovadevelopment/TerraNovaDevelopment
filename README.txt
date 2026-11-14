Terra Nova Development — Articles #100, #101, #102 Website Update

This is a SAFE WEBSITE PATCH, not a replacement for your entire website.

Contents:
 - articles/article-100.html, article-101.html, article-102.html
 - assets/article-100-original.png, article-101-original.png, article-102-original.png
 - documents/*.docx: three illustrated Word files
 - article-100-index-panel.html, article-101-index-panel.html, article-102-index-panel.html
 - update_index.py: inserts clickable homepage panels and revision history into your existing index.html

IMPORTANT: There is intentionally NO replacement index.html in the ZIP because your live website already has Articles #001-099. Overwriting it with an old copy would be destructive.

HOW TO USE:
1. On your computer, open the local folder containing the existing Terra Nova website index.html.
2. Extract the ZIP INTO that folder, preserving articles/, assets/, and documents/ subfolders.
3. Run: python update_index.py (or double-click apply_update.bat on Windows).
4. Confirm article #100, #101 and #102 appear in index.html, then commit/push changed files through GitHub Desktop.
5. Render will redeploy from the GitHub repository.

No images are hotlinked. All three HTML pages use bundled local image files, as do the homepage cards. Every DOCX embeds its image.
If copying manually, NEVER replace index.html with a new blank index or delete older assets and pages.
