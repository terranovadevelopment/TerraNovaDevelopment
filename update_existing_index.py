#!/usr/bin/env python3
from pathlib import Path
import re,html,sys
p=Path(__file__).resolve().parent/'index.html'
if not p.exists():
 print('index.html missing. Extract these files into the existing website repository root first.');sys.exit(1)
s=p.read_text(encoding='utf-8')
entries=[
('112','The Jubilee Manifesto','A call for debt relief, renewed justice, and a sustainable economic order.'),
('113','How Humanity Can Outgrow the Broken Systems We See Everywhere','Ten principles for better public systems and stronger communities.'),
('114','A Financial and Moral Reset: How Government Could Be Funded Without Confiscation','A proposed alternative to tax-based government funding.')]
for n,title,desc in entries:
 if f'class="article-index-number">#{n}</span>' not in s:
  marker='</ol></div></section><section id="articles">'
  if marker not in s:raise ValueError('Scrollable index marker missing')
  s=s.replace(marker,f'<li><a href="articles/article-{n}.html"><span class="article-index-number">#{n}</span> {html.escape(title)}</a></li>'+marker)
 if f'class="article-card" href="articles/article-{n}.html"' not in s:
  marker='</div></section><section class="secondary" id="about">'
  if marker not in s:raise ValueError('Card grid marker missing')
  card=f'<a class="article-card" href="articles/article-{n}.html"><img src="assets/article-{n}-original.png" alt="Article #{n} illustration" loading="lazy" decoding="async"/><div class="card-body"><span class="eyebrow">Article #{n}</span><h3>{html.escape(title)}</h3><p>{html.escape(desc)}</p><span class="read">Read full article →</span></div></a>'
  s=s.replace(marker,card+marker)
s=re.sub(r'Article Index — \d+ Articles','Article Index — 114 Articles',s,count=1)
p.write_text(s,encoding='utf-8')
print('Index updated for articles 112–114')
