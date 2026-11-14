from pathlib import Path
import re,html
p=Path('index.html')
if not p.exists():raise SystemExit('Run from repository root containing index.html')
s=p.read_text(encoding='utf-8')
items=[('118','The World We Could Have Tomorrow If We Stopped Arguing Today','Practical cooperation on homelessness, hunger, education, peace, and the environment.'),('119','Artificial Scarcity in a Bountiful World','How modern abundance, access barriers, and economic systems shape the experience of scarcity.'),('120','The SALUDOS Manifesto','A universal welcome through community centers, shared resources, dignity, and belonging.')]
for n,t,d in items:
    anchor='</ol></div></section><section id="articles">'
    if f'class="article-index-number">#{n}</span>' not in s:
        if anchor not in s:raise SystemExit('Scrollable index marker not found')
        s=s.replace(anchor,f'<li><a href="articles/article-{n}.html"><span class="article-index-number">#{n}</span> {html.escape(t)}</a></li>'+anchor)
    anchor='</div></section><section class="secondary" id="about">'
    if f'class="article-card" href="articles/article-{n}.html"' not in s:
        if anchor not in s:raise SystemExit('Article card marker not found')
        card=f'<a class="article-card" href="articles/article-{n}.html"><img src="assets/article-{n}-original.png" alt="Article #{n} illustration" loading="lazy"><div class="card-body"><span class="eyebrow">Article #{n}</span><h3>{html.escape(t)}</h3><p>{html.escape(d)}</p><span class="read">Read full article →</span></div></a>'
        s=s.replace(anchor,card+anchor)
s=re.sub(r'Article Index — \d+ Articles','Article Index — 120 Articles',s)
p.write_text(s,encoding='utf-8')
print('Updated index.html to include Articles #118–#120')
