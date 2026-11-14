#!/usr/bin/env python3
"""
Static site generator for nithin's portfolio. Pure Python standard library.

    python _tools/build.py

Regenerates every HTML page, sitemap.xml and robots.txt in the repository root.
You can also edit the generated .html files directly. If you do, don't re-run
this script afterwards, or your manual edits will be overwritten.

The _tools folder is not published by GitHub Pages (Jekyll skips folders starting with "_").
"""
import html
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from content_services import SERVICES  # noqa: E402
from content_cases import CASES        # noqa: E402
from content_blog import POSTS         # noqa: E402

# ==========================================================================
# CONFIG: edit these values
# ==========================================================================
SITE_URL = "https://nithinsingh97.github.io"   # no trailing slash
BASE_PATH = "/"            # "/" for username.github.io; "/repo-name/" for a project site
NAME = "Nithin Singh"
FIRST = "Nithin"
TITLE = "Web Scraping Specialist | Python Data Extraction Expert | Lead Generation Specialist"
SHORT_TITLE = "Web Scraping & Data Extraction Specialist"
FIVERR = "https://www.fiverr.com/s/61zovaR"
SINCE = 2019
YEARS = "6+"
ORDERS = "1,300+"          # public Fiverr gig figure; refresh periodically
REVIEWS = "966"            # Fiverr gig review count; refresh periodically
STATS_NOTE = "Figures shown for the featured Fiverr gig; check Fiverr for live totals."
CONTACT_EMAIL = "nithinsingh1997@gmail.com"   # used by the contact form mailto fallback
GIG_URL = "https://www.fiverr.com/nithinsingh97/do-web-scraping-data-mining-and-data-extraction-from-any-website"
GIG_IMAGE = "https://fiverr-res.cloudinary.com/t_medium7_x2,q_auto,f_auto/gigs/142647533/original/a0cecb996428a58eb15910ebbba5d62bfb887036.png"
GIG_RATING = "4.8/5"
# Optional Google Form. Leave GOOGLE_FORM_ACTION empty to use the mailto fallback.
# Action format: https://docs.google.com/forms/d/e/<FORM_ID>/formResponse
GOOGLE_FORM_ACTION = ""
GOOGLE_FORM_ENTRIES = {    # form field name -> Google Forms entry id
    "name": "", "email": "", "company": "", "description": "",
    "source": "", "records": "", "format": "", "deadline": "",
}
SAME_AS = [FIVERR]         # add your Fiverr profile, LinkedIn, GitHub URLs for stronger identity signals
PUBLISHED = "2026-11-14"
MODIFIED = "2026-11-14"
OG_IMAGE = "assets/images/og-image.png"
# ==========================================================================

esc = html.escape
PERSON_ID = SITE_URL + "/#person"
WEBSITE_ID = SITE_URL + "/#website"


def url(path):
    return SITE_URL + "/" + ("" if path == "index.html" else path)


def fiverr_btn(label=None, cls="btn btn-fiverr", extra=""):
    label = label or f"Hire {FIRST} on Fiverr"
    return (f'<a class="{cls}" href="{FIVERR}" target="_blank" rel="noopener" {extra}>'
            f'<span class="dot" aria-hidden="true"></span>{esc(label)}'
            f'<span class="sr-only"> (opens Fiverr in a new tab)</span></a>')


# --------------------------------------------------------------------------
# Icons (inline SVG, stroke style)
# --------------------------------------------------------------------------
P = {
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    "code": '<path d="m8 8-4 4 4 4M16 8l4 4-4 4M14 4l-4 16"/>',
    "map": '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11Z"/><circle cx="12" cy="10" r="2.5"/>',
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7M18.5 20a6.5 6.5 0 0 0-3-5.5"/>',
    "cart": '<circle cx="9" cy="20" r="1.4"/><circle cx="18" cy="20" r="1.4"/><path d="M2.5 3h2.6l2.4 12.2h11.3L21 7H6.2"/>',
    "home": '<path d="M3 11.5 12 4l9 7.5M5.5 9.8V20h13V9.8M10 20v-5h4v5"/>',
    "book": '<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5zM4 20.5A2.5 2.5 0 0 0 6.5 23H20v-5"/>',
    "file": '<path d="M14 3H6.5A1.5 1.5 0 0 0 5 4.5v15A1.5 1.5 0 0 0 6.5 21h11a1.5 1.5 0 0 0 1.5-1.5V8z"/><path d="M14 3v5h5M8.5 13h7M8.5 17h5"/>',
    "table": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9.5h18M3 15h18M9 4v16"/>',
    "bolt": '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "star": '<path d="m12 3 2.8 5.7 6.2.9-4.5 4.4 1 6.2L12 17.3 6.5 20.2l1-6.2L3 9.6l6.2-.9z"/>',
    "shield": '<path d="M12 3 4.5 6v5.5c0 4.5 3.2 8.4 7.5 9.5 4.3-1.1 7.5-5 7.5-9.5V6z"/><path d="m9 12 2 2 4-4"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "db": '<ellipse cx="12" cy="5.5" rx="8" ry="2.5"/><path d="M4 5.5v13c0 1.4 3.6 2.5 8 2.5s8-1.1 8-2.5v-13M4 12c0 1.4 3.6 2.5 8 2.5s8-1.1 8-2.5"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 7.5v.01"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 6.5 8.5 6.5 8.5-6.5"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "close": '<path d="M6 6l12 12M18 6 6 18"/>',
}


def icon(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{P[name]}</svg>')


# --------------------------------------------------------------------------
# Structured data
# --------------------------------------------------------------------------
KNOWS = ["Web scraping", "Data extraction", "Python", "Selenium", "Playwright", "BeautifulSoup",
         "Scrapy", "Pandas", "Lead generation", "Data research", "Google Maps data extraction",
         "E-commerce product data", "PDF data extraction", "Excel automation", "Web automation"]


def person_schema():
    return {
        "@type": "Person", "@id": PERSON_ID, "name": NAME, "url": SITE_URL + "/",
        "jobTitle": TITLE,
        "description": (f"{NAME} is a freelance web scraping and Python data extraction specialist and "
                        f"Fiverr Top Rated Seller, freelancing since {SINCE}. He builds custom scrapers, "
                        "lead generation datasets and data automation for businesses worldwide."),
        "image": SITE_URL + "/" + OG_IMAGE,
        "knowsAbout": KNOWS,
        "hasOccupation": {"@type": "Occupation", "name": "Web Scraping Specialist",
                          "skills": ", ".join(KNOWS[:10])},
        "sameAs": SAME_AS,
    }


def website_schema():
    return {"@type": "WebSite", "@id": WEBSITE_ID, "url": SITE_URL + "/",
            "name": f"{NAME}: {SHORT_TITLE}", "publisher": {"@id": PERSON_ID}, "inLanguage": "en"}


def crumbs_schema(crumbs):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": url(p)} for i, (n, p) in enumerate(crumbs)]}


def faq_schema(faqs):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}


def jsonld(nodes):
    data = {"@context": "https://schema.org", "@graph": nodes}
    s = json.dumps(data, ensure_ascii=False, indent=1).replace("</", "<\\/")
    return f'<script type="application/ld+json">\n{s}\n</script>'


# --------------------------------------------------------------------------
# Layout
# --------------------------------------------------------------------------
NAV = [("Home", "index.html"), ("About", "about.html"), ("Services", "services.html"),
       ("Portfolio", "portfolio.html"), ("Blog", "blog.html"), ("Contact", "contact.html")]


def section_of(path):
    if path.startswith("services/"):
        return "services.html"
    if path.startswith("case-studies/"):
        return "portfolio.html"
    if path.startswith("blog/"):
        return "blog.html"
    return path


def header(root, path):
    active = section_of(path)

    def links():
        out = []
        for label, href in NAV:
            cur = ' aria-current="page"' if href == active else ""
            out.append(f'<li><a href="{root}{href}"{cur}>{label}</a></li>')
        return "".join(out)

    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="{root}index.html" aria-label="{NAME}, home">
      <span class="brand-mark" aria-hidden="true">NS</span>
      <span class="brand-text"><span class="brand-name">{NAME}</span><span class="brand-sub">Web Scraping &amp; Data Extraction</span></span>
    </a>
    <nav class="nav" aria-label="Main"><ul>{links()}</ul></nav>
    <div class="header-cta">
      <a class="btn btn-ghost btn-sm" href="mailto:{CONTACT_EMAIL}">Email</a>
      <a class="btn btn-ghost btn-sm" href="{root}contact.html">Get a Quote</a>
      {fiverr_btn(cls="btn btn-fiverr btn-sm")}
    </div>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="Open menu">
      {icon("menu", "i-menu")}{icon("close", "i-close")}
    </button>
  </div>
  <div class="mobile-nav" id="mobile-nav">
    <nav aria-label="Mobile"><ul>{links()}</ul></nav>
    {fiverr_btn()}
    <a class="btn btn-ghost" href="{root}contact.html">Request a Project Quote</a>
  </div>
</header>'''


def footer(root):
    svc = "".join(f'<li><a href="{root}services/{s["slug"]}.html">{esc(s["title"])}</a></li>' for s in SERVICES[:6])
    posts = "".join(f'<li><a href="{root}blog/{p["slug"]}.html">{esc(p["title"].split(":")[0])}</a></li>' for p in POSTS[:5])
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="brand" href="{root}index.html"><span class="brand-mark" aria-hidden="true">NS</span><span class="brand-text"><span class="brand-name">{NAME}</span><span class="brand-sub">{SHORT_TITLE}</span></span></a>
        <p>Custom web scraping, Python data extraction and lead generation for businesses worldwide. Freelancing since {SINCE}. Fiverr Top Rated Seller.</p>
        <div class="btn-row">{fiverr_btn(cls="btn btn-primary btn-sm")}</div>
      </div>
      <div><h2>Services</h2><ul>{svc}<li><a href="{root}services.html">All services</a></li></ul></div>
      <div><h2>Guides</h2><ul>{posts}<li><a href="{root}blog.html">All articles</a></li></ul></div>
      <div><h2>Site</h2><ul>
        <li><a href="{root}about.html">About {FIRST}</a></li>
        <li><a href="{root}portfolio.html">Case studies</a></li>
        <li><a href="{root}contact.html">Request a quote</a></li>
        <li><a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></li>
        <li><a href="{FIVERR}" target="_blank" rel="noopener">Fiverr Gig</a></li>
        <li><a href="{root}sitemap.xml">Sitemap</a></li>
      </ul></div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year>{PUBLISHED[:4]}</span> {NAME}. All rights reserved.</span>
      <span>No tracking cookies. No third-party scripts.</span>
    </div>
  </div>
</footer>'''


def breadcrumbs_html(root, crumbs):
    items = []
    for i, (n, p) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            items.append(f'<li><span aria-current="page">{esc(n)}</span></li>')
        else:
            items.append(f'<li><a href="{root}{p}">{esc(n)}</a></li>')
    return f'<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'


PAGES = {}   # path -> {title, desc}


def page(path, title, desc, body, schema=None, og_type="website", crumbs=None, noindex=False, root_override=None):
    depth = path.count("/")
    root = root_override if root_override is not None else "../" * depth
    nodes = [person_schema()]
    if path == "index.html":
        nodes.append(website_schema())
    if crumbs:
        nodes.append(crumbs_schema(crumbs))
    nodes += schema or []
    canonical = url(path)
    img = SITE_URL + "/" + OG_IMAGE
    robots = '<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large">'
    assert len(desc) <= 175, (path, len(desc))
    PAGES[path] = {"title": title, "desc": desc, "noindex": noindex}
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="author" content="{NAME}">
{robots}
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{NAME}: Web Scraping, Python Data Extraction and Lead Generation">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{img}">
<meta name="theme-color" content="#1f5eff">
<link rel="icon" href="{root}assets/images/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{root}assets/images/apple-touch-icon.png">
<link rel="stylesheet" href="{root}assets/css/style.css?v=20261114-2">
{jsonld(nodes)}
</head>
<body>
{header(root, path)}
<main id="main">
{body}
</main>
{footer(root)}
<script src="{root}assets/js/main.js" defer></script>
</body>
</html>
'''
    out = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)


def page_hero(root, crumbs, eyebrow, h1, lead, extra=""):
    return f'''<section class="page-hero">
  <div class="container">
    {breadcrumbs_html(root, crumbs)}
    <span class="eyebrow">{esc(eyebrow)}</span>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    {extra}
  </div>
</section>'''


def faq_html(faqs, heading="Frequently asked questions", hid="faq"):
    items = "".join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in faqs)
    return f'<h2 id="{hid}">{heading}</h2><div class="faq">{items}</div>'


def cta_band(root, title="Have a data project in mind?", text=None):
    text = text or "Share the website, the fields you need and a rough record count. You'll get a clear plan, a quote and a sample before the full run."
    return f'''<section class="section"><div class="container"><div class="cta-band reveal">
  <h2>{title}</h2><p>{text}</p>
  <div class="btn-row">{fiverr_btn()}<a class="btn btn-ghost" href="{root}contact.html">Request a Project Quote</a></div>
</div></div></section>'''


SVC = {s["slug"]: s for s in SERVICES}
CASE = {c["slug"]: c for c in CASES}
POST = {p["slug"]: p for p in POSTS}


def svc_card(root, s, i=None):
    num = f'<span class="card-num">{i:02d}</span>' if i else ""
    return f'''<article class="card reveal">{num}<div class="icon-box">{icon(s["icon"])}</div>
  <h3><a href="{root}services/{s["slug"]}.html">{esc(s["title"])}</a></h3><p>{esc(s["short"])}</p>
  <span class="more">Learn more {icon("arrow")}</span></article>'''


def case_card(root, c):
    badge = '<span class="sample">Sample</span>' if c["sample"] else ""
    return f'''<article class="card case-card reveal">{badge}<span class="kicker">{esc(c["category"])}</span>
  <h3><a href="{root}case-studies/{c["slug"]}.html">{esc(c["title"])}</a></h3><p>{esc(c["short"])}</p>
  <span class="more">Read case study {icon("arrow")}</span></article>'''


def post_card(root, p):
    return f'''<article class="card post-card reveal"><div class="post-meta"><span class="cat">{esc(p["category"])}</span><span>{p["read"]} min read</span></div>
  <h3><a href="{root}blog/{p["slug"]}.html">{esc(p["title"])}</a></h3><p>{esc(p["meta"][:150].rsplit(" ", 1)[0])}…</p>
  <span class="more">Read article {icon("arrow")}</span></article>'''


TECH = [
    ("py", "Python", "Primary language for every scraper, pipeline and automation."),
    ("sel", "Selenium", "WebDriver browser automation, with proven QA-grade explicit waits."),
    ("pw", "Playwright", "Modern dynamic sites, auto-waiting and network capture."),
    ("bs4", "BeautifulSoup", "Fast, precise HTML parsing for static pages."),
    ("scrapy", "Scrapy", "High-volume crawling with concurrency and pipelines."),
    ("pd", "Pandas", "Cleaning, deduplication, merging and export."),
    ("http", "Requests", "Lightweight HTTP for pages, APIs and endpoints."),
    ("json", "APIs & JSON", "Extracting clean data from APIs and embedded JSON."),
    ("xlsx", "Excel automation", "openpyxl and XlsxWriter for formatted, repeatable reports."),
    ("pdf", "PDF extraction", "pdfplumber, PyMuPDF and OCR for tables and text."),
]


def tech_grid():
    return '<div class="tech-grid">' + "".join(
        f'<div class="tech reveal"><span class="t-ic">{t}</span><strong>{n}</strong><span>{d}</span></div>' for t, n, d in TECH) + "</div>"


HOME_FAQ = [
    ("What does a web scraping specialist do?", f"A web scraping specialist builds programs that collect information from websites and turn it into structured data such as Excel, CSV or JSON. {NAME} writes custom Python scrapers, cleans and validates the results, and delivers data in the exact format a business needs."),
    ("How do I start a project with Nithin Singh?", "Send the website URL, the fields you need, an estimated record count, your preferred output format and your deadline, either through the project quote form on this site or by messaging on Fiverr. You'll receive a plan and, for most projects, a sample before the full run."),
    ("Which countries do you work with?", "Clients from anywhere. Work is delivered remotely, and communication is in English. The site is aimed at businesses in the USA, UK, Canada, Australia and Europe, among others."),
    ("Do you offer a sample before the full dataset?", "Yes. For most projects a small sample is delivered first so you can confirm fields, format and quality."),
    ("Which output formats do you deliver?", "Excel (.xlsx), CSV, JSON, Google Sheets, and CRM-ready files for tools like HubSpot or Salesforce, with your preferred column order."),
    ("Do you scrape any kind of data?", "No. Only publicly accessible data, collected responsibly. Requests to bypass logins, paywalls or security measures, or that would breach data protection law, are declined."),
]


# --------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------
def build_home():
    body = f"""
<section class="premium-hero">
 <div class="container premium-grid">
  <div class="premium-copy">
   <span class="premium-eyebrow"><span class="live-dot"></span> Fiverr Top Rated Seller · {YEARS} years of experience</span>
   <h1>Need data from the web?<br><span>I'll extract it for you.</span></h1>
   <p class="premium-lead">Custom web scraping, Python automation and lead generation. Get clean, structured data without the manual work.</p>
   <div class="premium-actions">{fiverr_btn("Hire me on Fiverr", "btn btn-primary")}<a class="btn btn-ghost" href="mailto:{CONTACT_EMAIL}">Email me</a><a class="premium-text-link" href="portfolio.html">View work →</a></div>
   <div class="premium-proof"><div><strong>{ORDERS}</strong><span>orders completed</span></div><div><strong>{GIG_RATING}</strong><span>Fiverr gig rating</span></div><div><strong>{REVIEWS}</strong><span>gig reviews</span></div></div>
   <p class="premium-note">Figures shown for this gig; <a href="{FIVERR}" target="_blank" rel="noopener">see my live Fiverr profile</a>.</p>
  </div>
  <a class="gig-feature" href="{GIG_URL}" target="_blank" rel="noopener" aria-label="View my web scraping Fiverr gig">
   <div class="gig-feature-top"><span>MY FEATURED FIVERR GIG</span><span class="gig-rating">★ {GIG_RATING}</span></div>
   <img src="{GIG_IMAGE}" alt="{NAME}'s primary Fiverr gig thumbnail for web scraping, data extraction and Python automation" fetchpriority="high">
   <div class="gig-feature-bottom"><div><strong>Web Scraping &amp; Data Extraction</strong><span>Python · Automation · Lead Generation</span></div><span class="gig-open">View gig ↗</span></div>
  </a>
 </div>
</section>
<section class="premium-trust"><div class="container premium-trust-inner"><span>✓ Fiverr Top Rated Seller</span><span>✓ {ORDERS} completed orders</span><span>✓ {GIG_RATING} gig rating</span><span>✓ Worldwide clients</span></div></section>
<section class="section premium-services"><div class="container">
 <div class="premium-section-head"><span class="eyebrow">WHAT I DO</span><h2>Get the data you need.<br><span>Skip the manual work.</span></h2><p>Practical data services for research, sales, operations and analysis.</p></div>
 <div class="grid grid-3">
  <a class="premium-service-card" href="services/website-web-scraping.html"><span class="service-icon">⌘</span><strong>Website scraping</strong><span>Extract structured data from websites and directories.</span><em>Explore service →</em></a>
  <a class="premium-service-card" href="services/google-maps-data-extraction.html"><span class="service-icon">⌖</span><strong>Google Maps data</strong><span>Business listings, locations and available contact details.</span><em>Explore service →</em></a>
  <a class="premium-service-card" href="services/b2b-lead-generation.html"><span class="service-icon">◎</span><strong>B2B lead generation</strong><span>Targeted company and prospect lists for your sales team.</span><em>Explore service →</em></a>
  <a class="premium-service-card" href="services/ecommerce-product-scraping.html"><span class="service-icon">▤</span><strong>E-commerce scraping</strong><span>Products, prices, SKUs, variants and catalogue data.</span><em>Explore service →</em></a>
  <a class="premium-service-card" href="services/real-estate-data-extraction.html"><span class="service-icon">⌂</span><strong>Real estate data</strong><span>Property listings, prices, features and agent details.</span><em>Explore service →</em></a>
  <a class="premium-service-card" href="services/pdf-data-extraction.html"><span class="service-icon">▧</span><strong>PDF to Excel</strong><span>Turn tables and document information into usable files.</span><em>Explore service →</em></a>
 </div>
 <div class="premium-center"><a class="btn btn-ghost" href="services.html">See all 10 services →</a></div>
</div></section>
<section class="premium-process"><div class="container premium-process-grid">
 <div><span class="eyebrow">SIMPLE PROCESS</span><h2>From website to<br><span>ready-to-use data.</span></h2><p>No complicated process. Just tell me what you need.</p></div>
 <div class="process-mini"><div><b>01</b><section><strong>Share your requirements</strong><p>Send the source URL, fields and estimated records.</p></section></div><div><b>02</b><section><strong>Review a sample</strong><p>Check the data structure and quality before the full run.</p></section></div><div><b>03</b><section><strong>Receive clean data</strong><p>Get your finished Excel, CSV, JSON or Google Sheet.</p></section></div></div>
</div></section>
<section class="premium-cta"><div class="container premium-cta-inner">
 <div><span class="eyebrow">LET'S WORK TOGETHER</span><h2>Have a data project?<br>Let's make it happen.</h2><p>Tell me what you need. I'll review it and get back to you.</p></div>
 <div class="premium-actions">{fiverr_btn("Start on Fiverr", "btn btn-primary")}<a class="btn btn-ghost" href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></div>
</div></section>
"""
    page("index.html",
         f"{NAME} | Web Scraping Specialist & Python Data Extraction Expert",
         "Nithin Singh, web scraping specialist and Fiverr Top Rated Seller: custom Python data extraction, Google Maps scraping and B2B lead generation worldwide.",
         body, schema=[{"@type": "ProfilePage", "@id": SITE_URL + "/#profile", "url": SITE_URL + "/",
                        "mainEntity": {"@id": PERSON_ID}, "isPartOf": {"@id": WEBSITE_ID}}])


def build_about():
    r = ""
    crumbs = [("Home", "index.html"), ("About", "about.html")]
    body = page_hero(r, crumbs, "About", f"About {NAME}",
                     f"Web scraping specialist, Python developer and Fiverr Top Rated Seller. Turning web data into business data since {SINCE}.",
                     f'<div class="btn-row">{fiverr_btn()}<a class="btn btn-ghost" href="contact.html">Request a Project Quote</a></div>') + f'''
<section class="section">
  <div class="container content-grid">
    <div class="prose">
      <div class="answer-box"><strong class="lbl">In short</strong><p>{NAME} is a freelance web scraping and Python data extraction specialist who has been freelancing since {SINCE}. He is a Fiverr Top Rated Seller with {ORDERS} completed orders (historical figure) and works with international clients on web scraping, data research and lead generation.</p></div>

      <h2 id="journey">My freelancing journey</h2>
      <p>I started freelancing in {SINCE}, focusing on one problem businesses kept running into: the data they needed was on the web, but not in a form they could use. Over the years since, that focus has grown into a full practice covering web scraping, data extraction, data research and lead generation.</p>
      <p>Most of that work has been delivered through Fiverr, where I reached Top Rated Seller status and completed {ORDERS} orders with {REVIEWS} Gig reviews (historical figures). This website is where I set out how I work, independently of any single platform.</p>

      <img src="assets/images/data-pipeline.svg" width="760" height="300" loading="lazy" decoding="async" alt="Diagram of a data extraction pipeline: website sources flow through a Python scraper, then cleaning and validation, into Excel, CSV and JSON outputs">

      <h2 id="expertise">Technical expertise</h2>
      <p>I work primarily in Python. For static pages and APIs I use Requests, httpx and BeautifulSoup. For large crawls I use Scrapy, and for JavaScript-heavy sites and browser workflows I use Playwright and Selenium. Pandas handles cleaning, deduplication and export, and I use openpyxl for formatted Excel reports and pdfplumber, PyMuPDF and OCR for PDFs.</p>
      <p>My background includes QA test automation with Selenium, Playwright and Pytest. That shapes how I build scrapers: explicit waits instead of guesswork, logging and screenshots on failure, and code structured so it's easy to maintain. When a client's team doesn't use Python, I package tools as Windows executables.</p>

      <h2 id="international">Working with international clients</h2>
      <p>I work remotely with clients across different countries and time zones, and I'm used to sources in multiple languages and local formats: addresses, phone numbers, currencies and units. Communication is written and clear, with progress updates on longer projects.</p>

      <h2 id="approach">My approach to data extraction</h2>
      <ol>
        <li><strong>Understand the goal.</strong> What decision or workflow the data feeds decides the fields, sources and format.</li>
        <li><strong>Inspect the source.</strong> Check for APIs, embedded JSON and rendering method before writing code.</li>
        <li><strong>Sample first.</strong> Agree on columns and quality with a small sample.</li>
        <li><strong>Extract completely.</strong> Plan pagination, search caps and segmentation so nothing is silently missed.</li>
        <li><strong>Validate and deliver.</strong> Deduplicate, normalise, keep source URLs, and report anything that couldn't be collected.</li>
      </ol>

      <h2 id="values">Professional values</h2>
      <ul class="checklist">
        <li><strong>Accuracy over volume.</strong> A smaller correct dataset beats a large unreliable one.</li>
        <li><strong>Transparency.</strong> Clear scope, honest limits and no inflated promises.</li>
        <li><strong>Responsibility.</strong> Public data only, polite request rates and respect for privacy law.</li>
        <li><strong>Confidentiality.</strong> Your project details and data stay private.</li>
        <li><strong>Reliability.</strong> Deadlines agreed realistically and met.</li>
      </ul>
    </div>
    <aside class="sidebar">
      <div class="side-card dark"><h2>Work with {FIRST}</h2><p>Order directly through Fiverr, or send a project brief for a custom quote.</p>{fiverr_btn(cls="btn btn-primary")}<a class="btn btn-ghost" href="contact.html">Request a Quote</a></div>
      <div class="side-card"><h2>On this page</h2><ul class="toc">
        <li><a href="#journey">Freelancing journey</a></li><li><a href="#expertise">Technical expertise</a></li>
        <li><a href="#international">International clients</a></li><li><a href="#approach">Approach</a></li><li><a href="#values">Values</a></li></ul></div>
    </aside>
  </div>
</section>
{cta_band(r)}'''
    page("about.html", f"About {NAME} | Web Scraping & Python Data Extraction Specialist",
         f"About Nithin Singh: freelancing since {SINCE}, Fiverr Top Rated Seller and Python web scraping specialist. His journey, technical expertise, approach and values.",
         body, crumbs=crumbs, og_type="profile",
         schema=[{"@type": "AboutPage", "url": url("about.html"), "name": f"About {NAME}", "mainEntity": {"@id": PERSON_ID}}])


def build_services_index():
    r = ""
    crumbs = [("Home", "index.html"), ("Services", "services.html")]
    rows = []
    for i, s in enumerate(SERVICES, 1):
        rows.append(f'''<article class="svc-row" id="{s["slug"]}">
  <div class="num">{i:02d}</div>
  <div><h2><a href="services/{s["slug"]}.html">{esc(s["title"])}</a></h2><p>{esc(s["answer"])}</p>
    <div class="btn-row"><a class="btn btn-dark btn-sm" href="services/{s["slug"]}.html">Service details</a>{fiverr_btn(cls="btn btn-fiverr btn-sm")}</div></div>
  <div class="mini"><h3>Use cases</h3><ul>{"".join(f"<li>{esc(u)}</li>" for u in s["use_cases"][:3])}</ul>
    <h3>Technologies</h3><ul class="tags">{"".join(f"<li>{esc(t)}</li>" for t in s["tech"][:5])}</ul></div>
</article>''')
    body = page_hero(r, crumbs, "Services", "Web Scraping and Data Extraction Services",
                     "Ten specialised services, one standard: complete, validated data in the exact format you need.",
                     f'<div class="btn-row">{fiverr_btn()}<a class="btn btn-ghost" href="contact.html">Request a Project Quote</a></div>') + f'''
<section class="section"><div class="container">{"".join(rows)}</div></section>
{cta_band(r, "Not sure which service fits?", "Describe the data you need and where it lives. I'll recommend the right approach and quote it.")}'''
    items = [{"@type": "ListItem", "position": i + 1, "item": {"@type": "Service", "name": s["title"], "url": url(f"services/{s['slug']}.html"),
              "description": s["short"], "provider": {"@id": PERSON_ID}}} for i, s in enumerate(SERVICES)]
    page("services.html", f"Web Scraping & Data Extraction Services | {NAME}",
         "Web scraping, Python data extraction, Google Maps, B2B leads, e-commerce, real estate, directory and PDF extraction, data cleaning and web automation.",
         body, crumbs=crumbs, schema=[{"@type": "ItemList", "name": "Services", "itemListElement": items}])


def build_service(s):
    r = "../"
    path = f"services/{s['slug']}.html"
    crumbs = [("Home", "index.html"), ("Services", "services.html"), (s["title"], path)]
    others = "".join(f'<li><a href="{r}services/{o["slug"]}.html">{esc(o["title"])}</a></li>' for o in SERVICES if o is not s)
    case = CASE[s["related_case"]]
    posts = "".join(f'<li><a href="{r}blog/{k}.html">{esc(POST[k]["title"])}</a></li>' for k in s["related_posts"])
    body = page_hero(r, crumbs, "Service", esc(s["h1"]), esc(s["short"]),
                     f'<div class="btn-row">{fiverr_btn()}<a class="btn btn-ghost" href="{r}contact.html">Request a Project Quote</a></div>') + f'''
<section class="section">
  <div class="container content-grid">
    <article class="prose">
      <div class="answer-box"><strong class="lbl">What is it?</strong><p>{esc(s["answer"])}</p></div>
      <h2 id="overview">Overview</h2>
      {"".join(f"<p>{esc(p)}</p>" for p in s["intro"])}
      <div class="svc-block">
        <div class="box"><h3 id="use-cases">Business use cases</h3><ul>{"".join(f"<li>{esc(u)}</li>" for u in s["use_cases"])}</ul></div>
        <div class="box"><h3 id="deliverables">Example deliverables</h3><ul>{"".join(f"<li>{esc(d)}</li>" for d in s["deliverables"])}</ul></div>
      </div>
      <h2 id="technologies">Technologies used</h2>
      <ul class="tags">{"".join(f"<li>{esc(t)}</li>" for t in s["tech"])}</ul>
      <h2 id="process">How the project works</h2>
      <ol>
        <li><strong>Brief:</strong> share the source, fields, estimated records, output format and deadline.</li>
        <li><strong>Feasibility check:</strong> I inspect the site and confirm approach, timeline and price.</li>
        <li><strong>Sample:</strong> you approve a sample of the output.</li>
        <li><strong>Full extraction:</strong> I run, clean and validate the data.</li>
        <li><strong>Delivery:</strong> you receive the final file, plus the script if agreed.</li>
      </ol>
      <h2 id="example">Related case study</h2>
      <p><a href="{r}case-studies/{case["slug"]}.html">{esc(case["title"])}</a>: {esc(case["short"])}</p>
      {faq_html(s["faqs"])}
      <h2 id="guides">Related guides</h2>
      <ul>{posts}</ul>
      <div class="cta-band mt-2"><h2>Ready to get your data?</h2><p>Order on Fiverr, or send a brief for a custom quote.</p>
        <div class="btn-row">{fiverr_btn()}<a class="btn btn-ghost" href="{r}contact.html">Request a Project Quote</a></div></div>
    </article>
    <aside class="sidebar">
      <div class="side-card dark"><h2>{esc(s["title"])}</h2><p>Top Rated on Fiverr. Sample before the full run. Clean, validated output.</p>{fiverr_btn(cls="btn btn-primary")}<a class="btn btn-ghost" href="{r}contact.html">Get a Quote</a></div>
      <div class="side-card"><h2>Other services</h2><ul>{others}</ul></div>
    </aside>
  </div>
</section>'''
    schema = [{"@type": "Service", "@id": url(path) + "#service", "name": s["title"], "serviceType": s["title"],
               "description": s["answer"], "url": url(path), "provider": {"@id": PERSON_ID},
               "areaServed": "Worldwide", "availableChannel": {"@type": "ServiceChannel", "serviceUrl": FIVERR}},
              faq_schema(s["faqs"])]
    page(path, f"{s['title']} Services | {NAME}", s["meta"], body, crumbs=crumbs, schema=schema)


SAMPLE_NOTE = f'<div class="placeholder-note">{icon("info")}<div><strong>Sample case study.</strong> This page describes the typical technical approach for this type of project. Fields marked <span class="ph">like this</span> are placeholders to be replaced with real, verified project details. No client names, volumes or results are claimed here.</div></div>'


def build_portfolio():
    r = ""
    crumbs = [("Home", "index.html"), ("Portfolio", "portfolio.html")]
    cards = "".join(case_card(r, c) for c in CASES)
    body = page_hero(r, crumbs, "Portfolio", "Portfolio and Technical Case Studies",
                     "How different kinds of data extraction projects are planned, built and validated, from Google Maps lead lists to PDF batches.",
                     f'<div class="btn-row">{fiverr_btn()}<a class="btn btn-ghost" href="contact.html">Request a Project Quote</a></div>') + f'''
<section class="section"><div class="container">
  {SAMPLE_NOTE}
  <div class="grid grid-3">{cards}</div>
</div></section>
{cta_band(r, "Have a similar project?")}'''
    items = [{"@type": "ListItem", "position": i + 1, "url": url(f"case-studies/{c['slug']}.html"), "name": c["title"]} for i, c in enumerate(CASES)]
    page("portfolio.html", f"Portfolio & Web Scraping Case Studies | {NAME}",
         "Case studies: Google Maps extraction, e-commerce scraping, real estate data, business directories, PDF extraction, large-scale scraping and automation.",
         body, crumbs=crumbs, schema=[{"@type": "CollectionPage", "name": "Case studies", "url": url("portfolio.html"),
                                       "mainEntity": {"@type": "ItemList", "itemListElement": items}}])


def build_case(c):
    r = "../"
    path = f"case-studies/{c['slug']}.html"
    crumbs = [("Home", "index.html"), ("Portfolio", "portfolio.html"), (c["title"], path)]
    s = SVC[c["service"]]
    meta = "".join(f"<div><dt>{esc(k)}</dt><dd>{v}</dd></div>" for k, v in c["meta"].items())
    pipe = "".join(f"<div>{esc(n)}<small>Step {i}</small></div>" for i, (n, _) in enumerate(c["approach"], 1))
    steps = "".join(f"<li><strong>{esc(n)}:</strong> {esc(d)}</li>" for n, d in c["approach"])
    others = "".join(f'<li><a href="{r}case-studies/{o["slug"]}.html">{esc(o["title"])}</a></li>' for o in CASES if o is not c)
    body = page_hero(r, crumbs, c["category"], esc(c["title"]), esc(c["short"]),
                     f'<dl class="case-meta">{meta}</dl>') + f'''
<section class="section">
  <div class="container content-grid">
    <article class="prose">
      {SAMPLE_NOTE if c["sample"] else ""}
      <h2 id="challenge">The challenge</h2>
      <p>{esc(c["challenge"])}</p>
      <h2 id="approach">Technical approach</h2>
      <div class="pipeline" aria-hidden="true">{pipe}</div>
      <ol>{steps}</ol>
      <h2 id="fields">Data fields delivered</h2>
      <ul class="tags">{"".join(f"<li>{esc(f)}</li>" for f in c["fields"])}</ul>
      <h2 id="tech">Technology</h2>
      <ul class="tags">{"".join(f"<li>{esc(t)}</li>" for t in c["tech"])}</ul>
      <h2 id="outcome">Outcome</h2>
      <p>{c["outcome"]}</p>
      <h2 id="service">Related service</h2>
      <p><a href="{r}services/{s["slug"]}.html">{esc(s["title"])}</a>: {esc(s["short"])}</p>
      <div class="cta-band mt-2"><h2>Need something similar?</h2><p>Get the same approach applied to your data source.</p>
        <div class="btn-row">{fiverr_btn()}<a class="btn btn-ghost" href="{r}contact.html">Request a Project Quote</a></div></div>
    </article>
    <aside class="sidebar">
      <div class="side-card dark"><h2>Start a project</h2><p>Order on Fiverr or send a brief for a custom quote.</p>{fiverr_btn(cls="btn btn-primary")}<a class="btn btn-ghost" href="{r}contact.html">Get a Quote</a></div>
      <div class="side-card"><h2>More case studies</h2><ul>{others}</ul></div>
    </aside>
  </div>
</section>'''
    desc = f"Case study: {c['short']} Technical approach, tools and data fields by Nithin Singh."
    if len(desc) > 165:
        desc = f"Case study: {c['short']}"
    schema = [{"@type": "Article", "headline": c["title"], "description": c["short"], "url": url(path),
               "author": {"@id": PERSON_ID}, "publisher": {"@id": PERSON_ID}, "datePublished": PUBLISHED,
               "dateModified": MODIFIED, "image": SITE_URL + "/" + OG_IMAGE, "about": c["category"],
               "mainEntityOfPage": url(path)}]
    page(path, f"{c['title']} | Case Study | {NAME}", desc, body, crumbs=crumbs, schema=schema, og_type="article")


def build_blog_index():
    r = ""
    crumbs = [("Home", "index.html"), ("Blog", "blog.html")]
    cards = "".join(post_card(r, p) for p in POSTS)
    body = page_hero(r, crumbs, "Blog", "Web Scraping and Data Extraction Guides",
                     "Practical, technical guides on web scraping, Python data extraction, lead generation and data cleaning, written for business owners and developers.") + f'''
<section class="section"><div class="container"><div class="grid grid-3">{cards}</div></div></section>
{cta_band(r)}'''
    posts = [{"@type": "BlogPosting", "headline": p["title"], "url": url(f"blog/{p['slug']}.html"), "datePublished": PUBLISHED,
              "author": {"@id": PERSON_ID}} for p in POSTS]
    page("blog.html", f"Web Scraping Blog & Guides | {NAME}",
         "Guides on web scraping, Python vs Selenium vs Playwright, Google Maps extraction, e-commerce scraping, B2B lead lists and cleaning data with Pandas.",
         body, crumbs=crumbs, schema=[{"@type": "Blog", "name": f"{NAME} Blog", "url": url("blog.html"), "author": {"@id": PERSON_ID}, "blogPost": posts}])


def build_post(p):
    r = "../"
    path = f"blog/{p['slug']}.html"
    crumbs = [("Home", "index.html"), ("Blog", "blog.html"), (p["title"], path)]
    toc = "".join(f'<li><a href="#{i}">{esc(h)}</a></li>' for i, h, _ in p["sections"]) + '<li><a href="#faq">FAQ</a></li>'
    secs = "".join(f'<h2 id="{i}">{esc(h)}</h2>{c.replace("{root}", r)}' for i, h, c in p["sections"])
    svcs = "".join(f'<li><a href="{r}services/{k}.html">{esc(SVC[k]["title"])}</a></li>' for k in p["services"])
    related = [q for q in POSTS if q is not p][:3]
    rel = "".join(f'<li><a href="{r}blog/{q["slug"]}.html">{esc(q["title"])}</a></li>' for q in related)
    meta = f'''<div class="article-meta"><span class="author-inline"><span class="avatar" aria-hidden="true">NS</span><a href="{r}about.html" rel="author">{NAME}</a></span>
      <span>Published <time datetime="{PUBLISHED}">{PUBLISHED}</time></span><span>{p["read"]} min read</span><span>{esc(p["category"])}</span></div>'''
    body = page_hero(r, crumbs, p["category"], esc(p["title"]), esc(p["meta"]), meta) + f'''
<section class="section">
  <div class="container content-grid">
    <article class="prose">
      <div class="answer-box"><strong class="lbl">Quick answer</strong><p>{esc(p["answer"])}</p></div>
      {secs}
      {faq_html(p["faqs"])}
      <section class="author-box" aria-label="About the author"><span class="avatar" aria-hidden="true">NS</span><div>
        <h2>About the author</h2>
        <p><a href="{r}about.html">{NAME}</a> is a web scraping and Python data extraction specialist, freelancing since {SINCE} and a Fiverr Top Rated Seller. He builds custom scrapers, lead generation datasets and data automation for businesses worldwide.</p>
        <div class="btn-row">{fiverr_btn(cls="btn btn-fiverr btn-sm")}<a class="btn btn-ghost btn-sm" href="{r}contact.html">Request a Quote</a></div></div></section>
    </article>
    <aside class="sidebar">
      <div class="side-card toc"><h2>In this article</h2><ol>{toc}</ol></div>
      <div class="side-card dark"><h2>Need this done for you?</h2><p>Custom scrapers and clean datasets, delivered.</p>{fiverr_btn(cls="btn btn-primary")}<a class="btn btn-ghost" href="{r}contact.html">Get a Quote</a></div>
      <div class="side-card"><h2>Related services</h2><ul>{svcs}</ul></div>
      <div class="side-card"><h2>More guides</h2><ul>{rel}</ul></div>
    </aside>
  </div>
</section>'''
    schema = [{"@type": "BlogPosting", "@id": url(path) + "#article", "headline": p["title"], "description": p["meta"],
               "url": url(path), "mainEntityOfPage": url(path), "datePublished": PUBLISHED, "dateModified": MODIFIED,
               "author": {"@id": PERSON_ID}, "publisher": {"@id": PERSON_ID}, "image": SITE_URL + "/" + OG_IMAGE,
               "articleSection": p["category"], "inLanguage": "en", "timeRequired": f"PT{p['read']}M"},
              faq_schema(p["faqs"])]
    t = p["title"] if len(p["title"]) > 55 else f"{p['title']} | {NAME}"
    page(path, t, p["meta"], body, crumbs=crumbs, schema=schema, og_type="article")


def build_contact():
    r = ""
    crumbs = [("Home", "index.html"), ("Contact", "contact.html")]
    entries = "".join(f' data-entry-{k}="{esc(v)}"' for k, v in GOOGLE_FORM_ENTRIES.items() if v)
    mode = ("Submitting opens Google Forms in a new tab, where Google confirms receipt." if GOOGLE_FORM_ACTION
            else "Submitting opens your email app with the enquiry prefilled. Nothing is sent until you press send there.")
    body = page_hero(r, crumbs, "Contact", "Request a Web Scraping Project Quote",
                     "Tell me what data you need. The more detail you share, the more accurate the quote.") + f'''
<section class="section">
  <div class="container content-grid">
    <div class="form-card">
      <h2 class="mt-0">Project enquiry</h2>
      <p class="muted">Fields marked <span class="req" style="color:#c2410c">*</span> are required. {mode}</p>
      <form id="enquiry-form" class="form" novalidate data-email="{esc(CONTACT_EMAIL)}" data-google-form="{esc(GOOGLE_FORM_ACTION)}"{entries}>
        <div class="row-2">
          <div class="field"><label for="f-name">Name <span class="req">*</span></label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
          <div class="field"><label for="f-email">Business email <span class="req">*</span></label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
        </div>
        <div class="field"><label for="f-company">Company website</label><input id="f-company" name="company" type="url" placeholder="https://" autocomplete="url"></div>
        <div class="field"><label for="f-desc">Project description <span class="req">*</span></label><textarea id="f-desc" name="description" required aria-describedby="h-desc"></textarea><span class="hint" id="h-desc">What data do you need, which fields, and what will you use it for?</span></div>
        <div class="field"><label for="f-source">Data source URL</label><input id="f-source" name="source" type="url" placeholder="https://example.com/listings"></div>
        <div class="row-2">
          <div class="field"><label for="f-records">Estimated records</label><input id="f-records" name="records" type="text" placeholder="e.g. 5,000 businesses"></div>
          <div class="field"><label for="f-format">Required output format</label>
            <select id="f-format" name="format"><option value="">Select…</option><option>Excel (.xlsx)</option><option>CSV</option><option>JSON</option><option>Google Sheets</option><option>CRM import file</option><option>Other / not sure</option></select></div>
        </div>
        <div class="field"><label for="f-deadline">Deadline</label><input id="f-deadline" name="deadline" type="date"></div>
        <div id="form-status" class="form-status" role="status" aria-live="polite"></div>
        <div class="btn-row"><button class="btn btn-primary" type="submit">Send project enquiry {icon("arrow")}</button></div>
      </form>
    </div>
    <aside class="sidebar">
      <div class="side-card dark"><h2>Prefer Fiverr?</h2><p>View my gig, check the reviews or message me directly on Fiverr.</p><a class="btn btn-primary" href="{GIG_URL}" target="_blank" rel="noopener">View my Fiverr Gig ↗</a></div>
      <div class="side-card"><h2>Email me directly</h2><p>For project enquiries and custom requirements.</p><a href="mailto:{CONTACT_EMAIL}"><strong>{CONTACT_EMAIL}</strong></a></div>
      <div class="side-card"><h2>What happens next</h2><ol class="toc">
        <li>I review the source and your requirements.</li><li>You get a plan, timeline and quote.</li>
        <li>A sample is delivered for approval.</li><li>The full dataset is delivered.</li></ol></div>
      <div class="side-card"><h2>Helpful reading</h2><ul>
        <li><a href="blog/how-to-choose-web-scraping-freelancer.html">How to choose a web scraping freelancer</a></li>
        <li><a href="services.html">All services</a></li><li><a href="portfolio.html">Case studies</a></li></ul></div>
    </aside>
  </div>
</section>'''
    page("contact.html", f"Contact & Request a Quote | {NAME}",
         "Request a web scraping or data extraction quote from Nithin Singh. Share the source URL, fields, record count, format and deadline, or hire directly on Fiverr.",
         body, crumbs=crumbs, schema=[{"@type": "ContactPage", "url": url("contact.html"), "name": "Contact", "about": {"@id": PERSON_ID}}])


def build_404():
    r = BASE_PATH   # absolute links: 404 is served from any URL depth
    body = f'''<section class="notfound"><div class="container narrow">
  <p class="code">404</p><h1>Page not found</h1>
  <p class="lead">The page you're looking for doesn't exist or has moved.</p>
  <div class="btn-row"><a class="btn btn-primary" href="{r}index.html">Go to homepage</a><a class="btn btn-ghost" href="{r}services.html">Browse services</a><a class="btn btn-ghost" href="{r}blog.html">Read the blog</a></div>
</div></section>'''
    page("404.html", f"Page Not Found | {NAME}", "The page you requested could not be found. Browse web scraping services, case studies and guides by Nithin Singh.",
         body, noindex=True, root_override=r)


def build_meta_files():
    urls = []
    prio = {"index.html": "1.0", "services.html": "0.9", "contact.html": "0.8", "about.html": "0.8", "portfolio.html": "0.8", "blog.html": "0.8"}
    for path, info in PAGES.items():
        if info["noindex"]:
            continue
        pr = prio.get(path, "0.7" if path.startswith("services/") else "0.6")
        urls.append(f"  <url><loc>{url(path)}</loc><lastmod>{MODIFIED}</lastmod><priority>{pr}</priority></url>")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")
    robots = f"""# robots.txt for {SITE_URL}
# Allowing crawlers makes pages eligible to be indexed; it does not guarantee rankings
# or that any AI assistant will recommend this site.

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)


def main():
    PAGES.clear()
    build_home()
    build_about()
    build_services_index()
    for s in SERVICES:
        build_service(s)
    build_portfolio()
    for c in CASES:
        build_case(c)
    build_blog_index()
    for p in POSTS:
        build_post(p)
    build_contact()
    build_404()
    build_meta_files()
    print(f"Built {len(PAGES)} pages into {ROOT}")


if __name__ == "__main__":
    main()
