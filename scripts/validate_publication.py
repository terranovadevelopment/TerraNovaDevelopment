#!/usr/bin/env python3
"""Validate a Terra Nova article before it is announced as published."""
import argparse
import re
import sys
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]

class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.downloads = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "img" and a.get("src"):
            self.images.append(a["src"])
        if tag == "a" and a.get("href", "").lower().endswith(".docx"):
            self.downloads.append(a["href"])

def validate(number):
    slug = f"{number:03d}"
    page = ROOT / "articles" / f"article-{slug}.html"
    home = ROOT / "index.html"
    errors = []
    if not page.is_file():
        errors.append(f"Missing article page: {page.relative_to(ROOT)}")
        return errors
    if not home.is_file():
        errors.append("Missing index.html")
        return errors
    html = page.read_text(encoding="utf-8")
    index = home.read_text(encoding="utf-8")
    if f"Article #{slug}" not in html:
        errors.append(f"Article page missing Article #{slug} identifier")
    if f"articles/article-{slug}.html" not in index:
        errors.append(f"Homepage missing Article #{slug} link")
    refs = References()
    refs.feed(html)
    homepage = References()
    homepage.feed(index)
    article_images = [s for s in refs.images if not s.startswith(("http:", "https:", "data:"))]
    home_images = [s for s in homepage.images if f"article-{slug}" in s]
    if not article_images:
        errors.append("Article has no local image")
    if not home_images:
        errors.append("Homepage card has no article-specific image")
    for src in article_images + home_images + refs.downloads:
        if src.startswith(("http:", "https:", "data:")):
            continue
        base = page.parent if src in article_images or src in refs.downloads else ROOT
        target = (base / src.split("?", 1)[0].split("#", 1)[0]).resolve()
        if not target.is_relative_to(ROOT.resolve()) or not target.is_file():
            errors.append(f"Missing or invalid referenced asset: {src}")
    return errors

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("article_number", type=int)
    args = p.parse_args()
    problems = validate(args.article_number)
    if problems:
        for problem in problems:
            print("ERROR:", problem, file=sys.stderr)
        sys.exit(1)
    print(f"Article #{args.article_number:03d}: homepage, article and referenced assets verified.")
