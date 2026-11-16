#!/usr/bin/env python3
"""Update the EXISTING Terra Nova Development homepage index and article cards."""
from pathlib import Path
import re, sys
from html import escape
root=Path(__file__).resolve().parent
index=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else root/'index.html'
if not index.exists():sys.exit(f'ERROR: {index} not found. Copy the existing repository index.html into this folder first, or supply its path.')
s=index.read_text(encoding='utf-8')
articles=[
(145,'Terra Nova University: Lifelong Learning for Everyone, Anywhere','A tuition-free global university concept offering units, courses, degrees, and AI-assisted lifelong learning.','assets/article-145.jpg.png'),
(146,'Digital Governments: A Framework for Transparent, Accountable, and Participatory Governance','Open budgets, secure civic participation, AI-assisted public administration, and accountability.','assets/article-146.jpg'),
(147,'Flashing Green Before Yellow: A Proposal for Safer, Less Stressful Intersections','An advance-warning signal concept and proposed DFW safety pilot.','assets/article-147.jpg'),
]
for n,title,desc,img in articles:
    href=f'articles/article-{n:03d}.html'
    indexentry=f'<li><a href="{href}"><span class="article-index-number">#{n:03d}</span> {escape(title)}</a></li>'
    if href not in s:
        marker='</ol></div></section><section id="articles">'
        if marker not in s:sys.exit('ERROR: Could not locate article index insertion point; no changes saved.')
        s=s.replace(marker,indexentry+'</ol></div></section><section id="articles">',1)
    card=f'<a aria-label="Read Article {n:03d}: {escape(title,quote=True)}" class="article-card" href="{href}"><img alt="{escape(title,quote=True)}" decoding="async" loading="lazy" src="{img}"/><div class="card-body"><span class="eyebrow">Article #{n:03d} · November 2026</span><h3>{escape(title)}</h3><p>{escape(desc)}</p><span class="read">Read full article →</span></div></a>'
    if f'class="article-card" href="{href}"' not in s:
        anchor='</div></section><section'
        start=s.find('<section id="articles">')
        if start<0:sys.exit('ERROR: Could not locate articles card section; no changes saved.')
        pos=s.find(anchor,start)
        if pos<0:sys.exit('ERROR: Could not locate end of article cards; no changes saved.')
        s=s[:pos]+card+s[pos:]
s=re.sub(r'Article Index — \d+ Articles','Article Index — 147 Articles',s,count=1)
index.write_text(s,encoding='utf-8')
print(f'Updated {index}: index entries, article cards, and count to 147.')
