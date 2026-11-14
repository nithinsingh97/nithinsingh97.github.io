#!/usr/bin/env python3
"""Static checks for the whole site. Run before every deployment:

    python _tools/check_site.py

Checks: internal links and #anchors resolve, image paths exist and have alt text,
titles and meta descriptions are unique, canonical URLs match file paths, JSON-LD
parses and includes the expected types, and sitemap.xml lists every indexable page.
"""
import json
import os
import re
import sys
from html.parser import HTMLParser
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import SITE_URL, BASE_PATH  # noqa: E402


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.imgs, self.ids, self.jsonld, self.meta = [], [], set(), [], {}
        self.title, self._in_title, self._in_ld, self.canonical, self.h1 = "", False, False, None, 0
        self._buf = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a" and "href" in a:
            self.links.append(a["href"])
        if tag == "link" and a.get("rel") in ("stylesheet", "icon", "apple-touch-icon"):
            self.links.append(a["href"])
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical = a["href"]
        if tag == "script" and a.get("src"):
            self.links.append(a["src"])
        if tag == "img":
            self.imgs.append(a)
        if tag == "meta":
            k = a.get("name") or a.get("property")
            if k:
                self.meta[k] = a.get("content", "")
        if tag == "title":
            self._in_title = True
        if tag == "h1":
            self.h1 += 1
        if tag == "script" and a.get("type") == "application/ld+json":
            self._in_ld, self._buf = True, ""

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag == "script" and self._in_ld:
            self.jsonld.append(self._buf)
            self._in_ld = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_ld:
            self._buf += data


def types_in(obj, acc):
    if isinstance(obj, dict):
        t = obj.get("@type")
        if t:
            acc.add(t)
        for v in obj.values():
            types_in(v, acc)
    elif isinstance(obj, list):
        for v in obj:
            types_in(v, acc)
    return acc


def main():
    errors, pages = [], {}
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if not d.startswith((".", "_"))]
        for f in fn:
            if f.endswith(".html"):
                rel = os.path.relpath(os.path.join(dp, f), ROOT).replace(os.sep, "/")
                p = Page()
                p.feed(open(os.path.join(dp, f), encoding="utf-8").read())
                pages[rel] = p

    titles, descs = {}, {}
    for rel, p in pages.items():
        base = os.path.dirname(rel)
        # links
        for href in p.links:
            u = urlparse(href)
            if u.scheme in ("http", "https", "mailto", "tel"):
                continue
            path, frag = u.path, u.fragment
            if not path:
                target = rel
            elif path.startswith("/"):
                target = path[len(BASE_PATH):] if path.startswith(BASE_PATH) else path.lstrip("/")
            else:
                target = os.path.normpath(os.path.join(base, path)).replace(os.sep, "/")
            if target.endswith("/") or target == "":
                target += "index.html"
            if not os.path.exists(os.path.join(ROOT, target)):
                errors.append(f"{rel}: broken link -> {href}")
            elif frag and target in pages and frag not in pages[target].ids:
                errors.append(f"{rel}: missing anchor #{frag} in {target}")
        # images
        for im in p.imgs:
            src = im.get("src", "")
            if not im.get("alt"):
                errors.append(f"{rel}: <img> without alt ({src})")
            if not src.startswith("http") and not os.path.exists(os.path.normpath(os.path.join(ROOT, base, src))):
                errors.append(f"{rel}: missing image {src}")
            if "loading" not in im:
                errors.append(f"{rel}: <img> without loading attribute ({src})")
        # metadata
        if p.h1 != 1:
            errors.append(f"{rel}: has {p.h1} <h1> elements (expected 1)")
        d = p.meta.get("description", "")
        if not p.title.strip() or not d:
            errors.append(f"{rel}: missing title or description")
        if not (50 <= len(d) <= 160):
            errors.append(f"{rel}: description length {len(d)}")
        titles.setdefault(p.title, []).append(rel)
        descs.setdefault(d, []).append(rel)
        for k in ("og:title", "og:description", "og:image", "og:url", "twitter:card"):
            if k not in p.meta:
                errors.append(f"{rel}: missing {k}")
        expected = SITE_URL + "/" + ("" if rel == "index.html" else rel)
        if p.canonical != expected:
            errors.append(f"{rel}: canonical {p.canonical} != {expected}")
        # json-ld
        found = set()
        for block in p.jsonld:
            try:
                data = json.loads(block)
            except json.JSONDecodeError as e:
                errors.append(f"{rel}: invalid JSON-LD ({e})")
                continue
            if data.get("@context") != "https://schema.org":
                errors.append(f"{rel}: JSON-LD missing @context")
            types_in(data, found)
        if "Person" not in found:
            errors.append(f"{rel}: no Person schema")
        if rel not in ("index.html", "404.html") and "BreadcrumbList" not in found:
            errors.append(f"{rel}: no BreadcrumbList schema")
        if rel.startswith("blog/") and "BlogPosting" not in found:
            errors.append(f"{rel}: no BlogPosting schema")
        if rel.startswith("services/") and "Service" not in found:
            errors.append(f"{rel}: no Service schema")
        if rel.startswith(("blog/", "services/")) and "FAQPage" not in found:
            errors.append(f"{rel}: no FAQPage schema")
        if rel != "404.html" and "fiverr.com" not in "".join(p.links):
            errors.append(f"{rel}: no Fiverr CTA")

    for t, rs in titles.items():
        if len(rs) > 1:
            errors.append(f"duplicate title '{t}': {rs}")
    for t, rs in descs.items():
        if len(rs) > 1:
            errors.append(f"duplicate description: {rs}")

    sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
    locs = re.findall(r"<loc>(.*?)</loc>", sm)
    for loc in locs:
        rel = loc[len(SITE_URL) + 1:] or "index.html"
        if rel not in pages:
            errors.append(f"sitemap: {loc} has no file")
    for rel in pages:
        if rel != "404.html" and (SITE_URL + "/" + ("" if rel == "index.html" else rel)) not in locs:
            errors.append(f"sitemap: missing {rel}")
    robots = open(os.path.join(ROOT, "robots.txt"), encoding="utf-8").read()
    if "Disallow: /\n" in robots:
        errors.append("robots.txt blocks crawlers")
    for bot in ("OAI-SearchBot", "Googlebot", "Bingbot"):
        if f"User-agent: {bot}" not in robots:
            errors.append(f"robots.txt missing {bot}")

    print(f"Checked {len(pages)} pages, {sum(len(p.links) for p in pages.values())} links, {len(locs)} sitemap URLs.")
    if errors:
        print(f"\n{len(errors)} problem(s):")
        for e in errors:
            print(" -", e)
        sys.exit(1)
    print("All checks passed.")


if __name__ == "__main__":
    main()
