#!/usr/bin/env python3
"""Idempotently update the existing Terra Nova index.html, preserving all original content."""
from pathlib import Path
import re
root=Path(__file__).resolve().parent
index=root/'index.html'
if not index.exists():
    raise SystemExit('Missing existing website index.html. Copy update package into the website root and rerun.')
s=index.read_text(encoding='utf-8')
parts=(root/'index-panels-103-105.html').read_text(encoding='utf-8')
marker='</div></section><section class="secondary" id="about">'
if marker not in s:raise SystemExit('Cannot identify articles section. No files modified.')
if all(f'href="articles/article-{n}.html"' in s for n in ('103','104','105')):
    print('Cards already indexed.')
else:
    # Build from individual cards and add only missing ones.
    cards=re.findall(r'(<a class="article-card" href="articles/article-(\d{3})\.html">.*?</a>)',parts,re.S)
    new=''.join(card for card,n in cards if f'href="articles/article-{n}.html"' not in s)
    s=s.replace(marker,new+marker)
revision='<section id="revisions"><h2>Revision History</h2>'
notice='<p><strong>November 14, 2026:</strong> Added Articles #103–#105 with their illustrations, Word downloads, and Facebook, LinkedIn, and X sharing previews.</p>'
if revision in s and notice not in s:s=s.replace(revision,revision+notice)
index.write_text(s,encoding='utf-8')
print('Updated', index)
