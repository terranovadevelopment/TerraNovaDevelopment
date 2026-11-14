#!/usr/bin/env python3
"""Apply articles 100-102 to an EXISTING Terra Nova Development website root."""
from pathlib import Path
from shutil import copy2
root=Path(__file__).resolve().parent
idx=root/'index.html'
if not idx.exists():
    raise SystemExit('index.html not found. Place/extract this package into the existing website root, then run this script.')
s=idx.read_text(encoding='utf8')
marker='</div></section><section class="secondary" id="about">'
revision='<section id="revisions"><h2>Revision History</h2>'
if marker not in s or revision not in s:
    raise SystemExit('Expected article/revision markers are missing. Existing index.html left unchanged.')
original=s
for n in ('100','101','102'):
    if f'href="articles/article-{n}.html"' not in s:
        panel=(root/f'article-{n}-index-panel.html').read_text(encoding='utf8')
        s=s.replace(marker,panel+marker,1)
rev='Published Articles #100–#102'
if rev not in s:
    s=s.replace(revision,revision+'<p><strong>November 2026:</strong> Published Articles #100–#102: The True Cost of the Current U.S. Healthcare System; The Benefits of Medicare for All; and Give &amp; Take Community Centers: A Pathway to Economic Freedom for Every American, with original illustrations and downloadable Word documents.</p>',1)
if s!=original:
    backup=idx.with_name('index.backup-before-100-102.html')
    if not backup.exists(): copy2(idx,backup)
    idx.write_text(s,encoding='utf8')
print('Article panels #100–#102 verified in index.html.')
