TERRA NOVA DEVELOPMENT — ARTICLES 145, 146, 147 WEBSITE UPDATE

CONTENTS
  articles/article-145.html, article-146.html, article-147.html
  assets/article-145.jpg.png, article-146.jpg, article-147.jpg
  downloads/article-145-terra-nova-university.docx
  downloads/article-146.docx, article-147.docx
  update_index.py

HOW TO APPLY TO YOUR EXISTING REPOSITORY
1. Download or clone the EXISTING TerraNovaDevelopment repository on Windows.
2. Extract this ZIP over the ROOT of that repository. Merge the articles,
   assets, and downloads folders; do not delete existing files.
3. Open Command Prompt in the repository folder and run:
      py update_index.py
   The script modifies your existing index.html, adding articles 145–147 to
   both the scrollable article index and clickable cards, and updates the
   displayed article count to 147. It is safe to run again.
4. Commit and push the updated files to the main branch in GitHub Desktop.
5. Check the published GitHub Pages website, including images and downloads.

IMPORTANT
The ZIP is an ADDITIVE PATCH, not a replacement for your full website.
It does not contain the previous 144 articles or your original index.html.
DO NOT upload this ZIP alone as a new website. Do not replace your existing
homepage with a blank index. Run update_index.py on the EXISTING homepage.
No live GitHub files have been changed by this ZIP creation.
