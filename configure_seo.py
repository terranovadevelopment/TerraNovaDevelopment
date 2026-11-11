from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json,sys
root=Path(__file__).resolve().parent
if len(sys.argv)!=2 or not sys.argv[1].startswith('https://'):
    raise SystemExit('Usage: python configure_seo.py https://your-actual-website-domain.com/')
base=sys.argv[1].rstrip('/')+'/'
paths=[Path('index.html')]+sorted(Path('articles').glob('article-*.html'))
urls=[]
for rel in paths:
    p=root/rel
    s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
    canonical=urljoin(base,str(rel).replace('index.html','') if rel.name=='index.html' else str(rel))
    for old in s.head.find_all('link',rel='canonical'):old.decompose()
    link=s.new_tag('link',rel='canonical',href=canonical);s.head.append(link)
    for key,value in [('og:url',canonical)]:
        t=s.head.find('meta',attrs={'property':key})
        if t:t['content']=value
        else:s.head.append(s.new_tag('meta',attrs={'property':key,'content':value}))
    img=s.select_one('main img') or s.select_one('img')
    if img:
        image=urljoin(canonical,img.get('src',''))
        for key in ['og:image','twitter:image']:
            attr='property' if key=='og:image' else 'name'
            t=s.head.find('meta',attrs={attr:key})
            if t:t['content']=image
            else:s.head.append(s.new_tag('meta',attrs={attr:key,'content':image}))
    for a in s.head.find_all('script',type='application/ld+json'):
        try:
            obj=json.loads(a.string or '{}');obj['mainEntityOfPage']=canonical
            if img:obj['image']=urljoin(canonical,img.get('src',''))
            a.string=json.dumps(obj,ensure_ascii=False)
        except ValueError:pass
    p.write_text(str(s),encoding='utf-8')
    urls.append(canonical)
(root/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('  <url><loc>'+u.replace('&','&amp;')+'</loc></url>\n' for u in urls)+'</urlset>\n',encoding='utf-8')
(root/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+urljoin(base,'sitemap.xml')+'\n',encoding='utf-8')
print('Configured',len(urls),'URLs for',base)
