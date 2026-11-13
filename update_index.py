from pathlib import Path
from bs4 import BeautifulSoup
CARD_HTML = {94: '<a class="article-card" href="articles/article-094.html"><img alt="Article #094 illustration" decoding="async" loading="lazy" src="assets/article-094-thumbnail.png"/><div class="card-body"><span class="eyebrow">Article #094 · November 13, 2026</span><h3>The Full Case for Medicare for All: A Structural, Economic, and Moral Transformation</h3><p>The structural, economic, and moral case for universal healthcare.</p><span class="read">Read full article →</span></div></a>', 95: '<a class="article-card" href="articles/article-095.html"><img alt="Article #095 illustration" decoding="async" loading="lazy" src="assets/article-095-thumbnail.png"/><div class="card-body"><span class="eyebrow">Article #095 · November 13, 2026</span><h3>Medicare for All — The Hidden Consensus</h3><p>Why broader understanding of Medicare for All could change public opinion.</p><span class="read">Read full article →</span></div></a>', 96: '<a class="article-card" href="articles/article-096.html"><img alt="Article #096 illustration" decoding="async" loading="lazy" src="assets/article-096-thumbnail.png"/><div class="card-body"><span class="eyebrow">Article #096 · November 13, 2026</span><h3>The Great Contrast: Medicare for All Compared to Our Current System</h3><p>Comparing the complexity of American healthcare with a proposed single-payer system.</p><span class="read">Read full article →</span></div></a>'}
root=Path(__file__).resolve().parent
p=root/'index.html'
if not p.exists():
 raise SystemExit('Place this update package into the root of the TerraNovaDevelopment website repository first.')
soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
cards=soup.select_one('#articles .cards')
if cards is None: raise SystemExit('Could not find article cards section; index not modified.')
for n in (94,95,96):
 if cards.select_one(f'a[href="articles/article-{n:03d}.html"]'): continue
 snippet=BeautifulSoup(CARD_HTML[n], 'html.parser')
 cards.append(snippet)
rev=soup.select_one('#revisions')
if rev and not rev.find(string=lambda s:s and 'Articles #094–#096' in s):
 pnew=soup.new_tag('p')
 pnew.append(BeautifulSoup('<strong>November 13, 2026:</strong> Added Articles #094–#096 on Medicare for All: The Full Case, The Hidden Consensus, and The Great Contrast.', 'html.parser'))
 h=rev.find('h2');h.insert_after(pnew)
p.write_text(str(soup),encoding='utf-8')
print('Updated index.html with Articles #094–#096')
