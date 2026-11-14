#!/usr/bin/env python3
"""Generates the site's image assets. Optional: the images are already in assets/images.
Requires Pillow:  pip install pillow"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "images")
os.makedirs(IMG, exist_ok=True)

FONT_DIR = "/usr/share/fonts/opentype/inter/"


def font(name, size):
    for p in [FONT_DIR + name, "C:/Windows/Fonts/segoeuib.ttf", "C:/Windows/Fonts/arial.ttf"]:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def gradient(w, h, c1, c2):
    img = Image.new("RGB", (w, h), c1)
    d = ImageDraw.Draw(img)
    for x in range(w):
        t = x / w
        d.line([(x, 0), (x, h)], fill=tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3)))
    return img


# ---- OG image 1200x630 ----
W, H = 1200, 630
og = Image.new("RGB", (W, H), (255, 255, 255))
d = ImageDraw.Draw(og)
for x in range(0, W, 44):
    d.line([(x, 0), (x, H)], fill=(240, 243, 249))
for y in range(0, H, 44):
    d.line([(0, y), (W, y)], fill=(240, 243, 249))
band = gradient(W, 12, (31, 94, 255), (90, 61, 255))
og.paste(band, (0, 0))
mark = gradient(84, 84, (63, 123, 255), (18, 57, 170))
m = Image.new("L", (84, 84), 0)
ImageDraw.Draw(m).rounded_rectangle([0, 0, 83, 83], 22, fill=255)
og.paste(mark, (80, 86), m)
d.text((122, 128), "NS", font=font("Inter-ExtraBold.otf", 34), fill="white", anchor="mm")
d.text((184, 98), "Nithin Singh", font=font("Inter-Bold.otf", 36), fill=(22, 27, 38))
d.text((184, 142), "Fiverr Top Rated Seller  ·  Freelancing since 2019", font=font("Inter-Medium.otf", 22), fill=(93, 102, 118))
d.text((80, 250), "Turn Websites Into", font=font("Inter-ExtraBold.otf", 72), fill=(22, 27, 38))
d.text((80, 334), "Valuable Business Data", font=font("Inter-ExtraBold.otf", 72), fill=(23, 72, 214))
d.text((80, 452), "Web Scraping  ·  Python Data Extraction  ·  Lead Generation", font=font("Inter-SemiBold.otf", 28), fill=(59, 67, 82))
d.rounded_rectangle([80, 518, 470, 568], 12, fill=(234, 240, 255))
d.text((100, 543), "Excel  ·  CSV  ·  JSON  ·  Google Sheets", font=font("Inter-SemiBold.otf", 20), fill=(18, 57, 170), anchor="lm")
og.save(os.path.join(IMG, "og-image.png"), optimize=True)

# ---- Apple touch icon 180 ----
ic = gradient(180, 180, (63, 123, 255), (18, 57, 170))
ImageDraw.Draw(ic).text((90, 92), "NS", font=font("Inter-ExtraBold.otf", 76), fill="white", anchor="mm")
ic.save(os.path.join(IMG, "apple-touch-icon.png"), optimize=True)

# ---- Favicon SVG ----
with open(os.path.join(IMG, "favicon.svg"), "w") as f:
    f.write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3f7bff"/><stop offset="1" stop-color="#1239aa"/></linearGradient></defs><rect width="64" height="64" rx="16" fill="url(#g)"/><text x="32" y="42" font-family="Arial, Helvetica, sans-serif" font-size="27" font-weight="800" fill="#fff" text-anchor="middle">NS</text></svg>''')

# ---- About page pipeline diagram ----
with open(os.path.join(IMG, "data-pipeline.svg"), "w") as f:
    f.write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 300" role="img" aria-labelledby="t d">
<title id="t">Data extraction pipeline</title>
<desc id="d">Website sources flow through a Python scraper, then cleaning and validation, into Excel, CSV and JSON outputs.</desc>
<defs><linearGradient id="b" x1="0" x2="1"><stop offset="0" stop-color="#1f5eff"/><stop offset="1" stop-color="#5a3dff"/></linearGradient>
<marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 10 5 0 10z" fill="#9fb3d9"/></marker></defs>
<rect width="760" height="300" rx="18" fill="#f6f8fc"/>
<g font-family="system-ui, -apple-system, Segoe UI, Arial, sans-serif" font-size="13" fill="#3b4352">
<g><rect x="30" y="50" width="150" height="44" rx="10" fill="#fff" stroke="#e3e8f0"/><text x="105" y="77" text-anchor="middle">Websites</text></g>
<g><rect x="30" y="128" width="150" height="44" rx="10" fill="#fff" stroke="#e3e8f0"/><text x="105" y="155" text-anchor="middle">Directories &amp; Maps</text></g>
<g><rect x="30" y="206" width="150" height="44" rx="10" fill="#fff" stroke="#e3e8f0"/><text x="105" y="233" text-anchor="middle">PDFs &amp; APIs</text></g>
<path d="M182 72 C230 72 230 150 262 150M182 150H262M182 228 C230 228 230 150 262 150" fill="none" stroke="#9fb3d9" stroke-width="2" marker-end="url(#a)"/>
<rect x="266" y="112" width="160" height="76" rx="14" fill="url(#b)"/>
<text x="346" y="146" text-anchor="middle" fill="#fff" font-weight="700" font-size="15">Python scraper</text>
<text x="346" y="166" text-anchor="middle" fill="#dbe5ff" font-size="12">Playwright · Scrapy · Requests</text>
<path d="M428 150H470" stroke="#9fb3d9" stroke-width="2" marker-end="url(#a)"/>
<rect x="474" y="112" width="120" height="76" rx="14" fill="#fff" stroke="#cfdcff"/>
<text x="534" y="146" text-anchor="middle" fill="#161b26" font-weight="700">Clean &amp;</text>
<text x="534" y="164" text-anchor="middle" fill="#161b26" font-weight="700">validate</text>
<path d="M596 150 C620 150 620 72 640 72M596 150H640M596 150 C620 150 620 228 640 228" fill="none" stroke="#9fb3d9" stroke-width="2" marker-end="url(#a)"/>
<g font-weight="700" fill="#1239aa"><rect x="644" y="52" width="90" height="40" rx="10" fill="#eaf0ff"/><text x="689" y="77" text-anchor="middle">Excel</text>
<rect x="644" y="130" width="90" height="40" rx="10" fill="#eaf0ff"/><text x="689" y="155" text-anchor="middle">CSV</text>
<rect x="644" y="208" width="90" height="40" rx="10" fill="#eaf0ff"/><text x="689" y="233" text-anchor="middle">JSON</text></g>
</g></svg>''')
print("images written to", IMG)
