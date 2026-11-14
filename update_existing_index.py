#!/usr/bin/env python3
"""Synchronize a local index.html with Terra Nova articles 124–126; leaves other content alone."""
import pathlib,html,re,sys
root=pathlib.Path(__file__).resolve().parent
p=root/'index.html'
if not p.exists():
 print('index.html not found. Extract this ZIP to the existing repository root before running.');sys.exit(1)
s=p.read_text(encoding='utf-8')
entries=[('124','The Courage to Stand in What You Claim','Faith, fear, and integrity.'),('125','The Bounty Already Here: How Technology Has Outgrown Scarcity, and Why Money Hasn’t','Technology, abundance, and distribution.'),('126','What Would You Do If You No Longer Had to Earn Money to Survive?','Human time, purpose, and freedom in an age of abundance.')]
for n,t,d in entries:
 if f'class="article-index-number">#{n}</span>' not in s:
  marker='</ol></div></section><section id="articles">'
  if marker not in s:raise RuntimeError('Could not find scrollable index')
  s=s.replace(marker,f'<li><a href="articles/article-{n}.html"><span class="article-index-number">#{n}</span> {html.escape(t)}</a></li>'+marker)
 if f'class="article-card" href="articles/article-{n}.html"' not in s:
  marker='</div></section><section class="secondary" id="about">'
  if marker not in s:raise RuntimeError('Could not find homepage panels')
  card=f'<a class="article-card" href="articles/article-{n}.html"><img src="assets/article-{n}-original.png" alt="Article #{n} illustration" loading="lazy" decoding="async"/><div class="card-body"><span class="eyebrow">Article #{n}</span><h3>{html.escape(t)}</h3><p>{html.escape(d)}</p><span class="read">Read full article →</span></div></a>'
  s=s.replace(marker,card+marker)
s=re.sub(r'Article Index — \d+ Articles','Article Index — 126 Articles',s,count=1)
p.write_text(s,encoding='utf-8')
print('Local index synchronized through #126')
