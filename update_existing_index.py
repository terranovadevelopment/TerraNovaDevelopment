#!/usr/bin/env python3
"""Safely update an existing Terra Nova index.html with articles 109–111."""
import re, html, pathlib, sys
site=pathlib.Path(__file__).resolve().parent
idx=site/'index.html'
if not idx.exists():
 print('ERROR: index.html is missing. Copy this package into the existing website repository folder first.');sys.exit(1)
s=idx.read_text(encoding='utf-8')
items=[('109','Elon Musk’s World Ten Years from Now','A possible future shaped by AI, robotics and abundant production.'),('110','The Transition to Abundance','A Terra Nova vision for eliminating artificial scarcity.'),('111','The Future of Fusion Energy: Promise, Challenges, and Global Impact','The breakthroughs and challenges surrounding fusion energy.')]
for n,t,d in items:
 if not re.search(r'class="article-index-number">#'+n+r'</span>',s):
  anchor='</ol></div></section><section id="articles">'
  if anchor not in s:raise ValueError('Could not locate scrollable index')
  s=s.replace(anchor,f'<li><a href="articles/article-{n}.html"><span class="article-index-number">#{n}</span> {html.escape(t)}</a></li>'+anchor)
 if not re.search(r'class="article-card" href="articles/article-'+n+r'.html"',s):
  card=f'<a class="article-card" href="articles/article-{n}.html"><img src="assets/article-{n}-original.png" alt="Article #{n} illustration" loading="lazy" decoding="async"/><div class="card-body"><span class="eyebrow">Article #{n}</span><h3>{html.escape(t)}</h3><p>{html.escape(d)}</p><span class="read">Read full article →</span></div></a>'
  anchor='</div></section><section class="secondary" id="about">'
  if anchor not in s:raise ValueError('Could not locate article card grid')
  s=s.replace(anchor,card+anchor)
s=re.sub(r'(Article Index — )\d+( Articles)',r'\g<1>111\2',s,count=1)
idx.write_text(s,encoding='utf-8')
print('Updated index.html: articles 109–111 added to both scrollable list and image cards.')
