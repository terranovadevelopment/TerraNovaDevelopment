from pathlib import Path
import re,html
p=Path('index.html')
if not p.exists():raise SystemExit('Run in your TerraNovaDevelopment repository root, next to index.html')
s=p.read_text(encoding='utf-8')
data=[
('115','The World Will Only Know Peace When Truth, Justice, and Love Become the Only Real Commodities of Value','How truth, justice and love can underpin lasting peace.'),
('116','The Bounty and the Barrier','Why humanity experiences scarcity amid abundance.'),
('117','The Age of Unlimited Energy: How Abundance Breaks the Logic of Scarcity','How abundant clean energy could unlock new opportunities.')]
for n,title,description in data:
    marker='</ol></div></section><section id="articles">'
    if f'class="article-index-number">#{n}</span>' not in s:
        row=f'<li><a href="articles/article-{n}.html"><span class="article-index-number">#{n}</span> {html.escape(title)}</a></li>'
        if marker not in s:raise SystemExit('Cannot locate scroll index')
        s=s.replace(marker,row+marker)
    marker='</div></section><section class="secondary" id="about">'
    if f'class="article-card" href="articles/article-{n}.html"' not in s:
        card=f'<a class="article-card" href="articles/article-{n}.html"><img src="assets/article-{n}-original.png" alt="Article #{n} illustration" loading="lazy"><div class="card-body"><span class="eyebrow">Article #{n}</span><h3>{html.escape(title)}</h3><p>{html.escape(description)}</p><span class="read">Read full article →</span></div></a>'
        if marker not in s:raise SystemExit('Cannot locate article grid')
        s=s.replace(marker,card+marker)
s=re.sub(r'Article Index — \d+ Articles','Article Index — 117 Articles',s)
p.write_text(s,encoding='utf-8')
print('Updated index.html with Articles 115–117')
