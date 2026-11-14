from pathlib import Path
import sys
index=Path(__file__).parent/'index.html'
if not index.exists():
    print('index.html missing. Put this package in the website root first.');sys.exit(1)
h=index.read_text(encoding='utf-8')
marker='</div></section><section class="secondary" id="about">'
if marker not in h:
    print('Unexpected index structure; no changes made.');sys.exit(1)
new=new='<a class="article-card" href="articles/article-106.html"><img src="assets/article-106-original.png" alt="Article #106 illustration" loading="lazy" decoding="async"/><div class="card-body"><span class="eyebrow">Article #106</span><h3>The Manifesto of the National Public Bank</h3><p>A proposal for universal nonprofit public banking, zero-interest loans, and transparent automated financial services.</p><span class="read">Read full article →</span></div></a><a class="article-card" href="articles/article-107.html"><img src="assets/article-107-original.png" alt="Article #107 illustration" loading="lazy" decoding="async"/><div class="card-body"><span class="eyebrow">Article #107</span><h3>America’s First Solar-Over-Canal Project in Arizona</h3><p>The Gila River Indian Community’s solar-over-canal pilot combines renewable electricity with water conservation.</p><span class="read">Read full article →</span></div></a><a class="article-card" href="articles/article-108.html"><img src="assets/article-108-original.png" alt="Article #108 illustration" loading="lazy" decoding="async"/><div class="card-body"><span class="eyebrow">Article #108</span><h3>China’s Dual-Use Solar Farms</h3><p>How agrivoltaic farms combine renewable electricity, livestock grazing, and more efficient agricultural land use.</p><span class="read">Read full article →</span></div></a>'
if 'href="articles/article-106.html"' not in h:
    h=h.replace(marker,new+marker,1)
rev='<section id="revisions"><h2>Revision History</h2>'
entry='<p><strong>November 14, 2026:</strong> Added Articles #106–#108 with images, Word downloads, and Facebook, LinkedIn and X social previews.</p>'
if entry not in h and rev in h:h=h.replace(rev,rev+entry,1)
index.write_text(h,encoding='utf-8')
print('index.html updated for articles 106, 107, 108')
