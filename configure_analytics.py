"""Configure Terra Nova Development Cloudflare Web Analytics on every HTML page."""
from pathlib import Path
import re,sys
if len(sys.argv)!=2 or not re.fullmatch(r'[0-9a-fA-F]{32}',sys.argv[1]):
    raise SystemExit('Usage: python configure_analytics.py YOUR_32_CHARACTER_CLOUDFLARE_TOKEN')
root=Path(__file__).resolve().parent
count=0
for page in root.rglob('*.html'):
    content=page.read_text(encoding='utf-8')
    if 'TND_CLOUDFLARE_TOKEN' in content:
        page.write_text(content.replace('TND_CLOUDFLARE_TOKEN',sys.argv[1]),encoding='utf-8')
        count+=1
print(f'Cloudflare analytics configured on {count} pages.')
