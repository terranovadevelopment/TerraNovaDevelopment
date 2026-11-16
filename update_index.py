"""Run: python update_index.py /path/to/your/site/index.html"""
import sys,re,pathlib
p=pathlib.Path(sys.argv[1]);s=p.read_text(encoding="utf-8");cards=pathlib.Path(__file__).with_name("article_cards.html").read_text(encoding="utf-8")
for n in (151,152,153):
 s=re.sub(r'<a\b[^>]*class="[^"]*article-card[^"]*"[^>]*href="articles/article-'+str(n)+r'\.html".*?</a>','',s,flags=re.S)
if '<div class="cards">' not in s:raise SystemExit("Could not locate article card container; original index not modified")
s=s.replace('<div class="cards">','<div class="cards">'+cards,1)
if 'id="revisions"' in s:s=s.replace('id="revisions"','id="revisions"',1).replace('<h2>Revision History</h2>','<h2>Revision History</h2><p>November 16, 2026: Added Articles #151–#153.</p>',1)
p.write_text(s,encoding="utf-8");print('Updated',p)
