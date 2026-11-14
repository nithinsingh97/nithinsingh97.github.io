# Blog articles. Each becomes /blog/<slug>.html
# "sections" is a list of (anchor-id, heading, html). Internal links use the
# placeholder {root}, which the build script replaces with the right relative path.

POSTS = [
# --------------------------------------------------------------------------
{
"slug": "what-is-web-scraping",
"title": "What Is Web Scraping? A Complete Business Guide",
"meta": "What web scraping is, how it works, what businesses use it for, what it costs and how to keep it legal and ethical. A practical business guide.",
"category": "Fundamentals",
"read": 9,
"answer": "Web scraping is the automated extraction of information from web pages into a structured format such as a spreadsheet or database. A program loads pages, finds the data you care about (names, prices, addresses, descriptions) and saves it in consistent rows and columns, so you can analyse or use it without copying it by hand.",
"sections": [
("how-it-works", "How web scraping works", """
<p>Every scraper, however complex, follows the same four steps:</p>
<ol>
<li><strong>Fetch.</strong> Request a page, much as a browser does. For simple sites this is a plain HTTP request. For JavaScript-heavy sites, a headless browser such as Playwright loads and renders the page.</li>
<li><strong>Parse.</strong> Locate the data in the page's HTML using CSS selectors or XPath, or read it from embedded JSON.</li>
<li><strong>Navigate.</strong> Follow pagination, categories and detail-page links until every item is covered.</li>
<li><strong>Store.</strong> Clean the values and write them to Excel, CSV, JSON or a database.</li>
</ol>
<p>The hard part is rarely the first page. It is making the process complete and reliable across thousands of pages that don't all behave the same way.</p>
"""),
("business-uses", "What businesses use web scraping for", """
<ul>
<li><strong>Lead generation:</strong> building lists of companies and contacts from directories, maps and websites. See <a href="{root}services/b2b-lead-generation.html">B2B lead generation</a>.</li>
<li><strong>Price and product monitoring:</strong> tracking competitor prices, stock and new products. See <a href="{root}services/ecommerce-product-scraping.html">e-commerce product scraping</a>.</li>
<li><strong>Market research:</strong> counting and profiling businesses, listings or products in a market.</li>
<li><strong>Real estate analysis:</strong> comparable listings, price trends and agent data.</li>
<li><strong>Content and catalog migration:</strong> moving structured content from one system to another.</li>
<li><strong>Data for analytics and AI:</strong> building training and evaluation datasets.</li>
</ul>
"""),
("tools", "Common web scraping tools", """
<table>
<thead><tr><th>Tool</th><th>Best for</th></tr></thead>
<tbody>
<tr><td>Requests + BeautifulSoup</td><td>Static pages where the data is in the HTML. Fast and simple.</td></tr>
<tr><td>Scrapy</td><td>Large crawls with many pages, built-in concurrency and pipelines.</td></tr>
<tr><td>Playwright</td><td>Modern JavaScript sites, infinite scroll and interactive flows.</td></tr>
<tr><td>Selenium</td><td>Browser automation, especially where existing Selenium setups exist.</td></tr>
<tr><td>Pandas</td><td>Cleaning, deduplicating and exporting the results.</td></tr>
</tbody>
</table>
<p>For a deeper comparison of the browser tools, read <a href="{root}blog/python-vs-selenium-vs-playwright.html">Python vs Selenium vs Playwright</a>.</p>
"""),
("legal-ethical", "Is web scraping legal?", """
<p>The short, honest answer: it depends on what you collect, how you collect it and how you use it. This is general information, not legal advice. In general:</p>
<ul>
<li>Collecting <strong>publicly available</strong> information is treated very differently from bypassing logins, paywalls or technical access controls.</li>
<li><strong>Personal data</strong> (names, emails and phone numbers of individuals) is regulated in many places, for example by GDPR in the EU and UK. You need a lawful basis for using it.</li>
<li>Website <strong>terms of service</strong> and <strong>copyright</strong> can restrict what you may collect and republish.</li>
<li>Responsible scrapers <strong>don't overload servers</strong>: they pace requests and run at sensible times.</li>
</ul>
<p>A professional scraper will ask about your use case before starting and will decline requests that cross clear lines.</p>
"""),
("cost", "What does web scraping cost?", """
<p>Cost depends on four things: how difficult the site is (static HTML or heavy JavaScript and anti-bot protection), how many pages are involved, how many fields are needed and how much cleaning the output needs. A one-off extraction from a simple directory is a small project. A multi-site pipeline that runs weekly with change tracking is a larger one. The fastest way to an accurate quote is to share the target URL, the fields you need and an estimate of the number of records.</p>
"""),
("diy-or-hire", "Build it yourself or hire a specialist?", """
<p>If you have Python skills and a simple, static site, building a scraper yourself is a good learning project. Hiring a specialist makes sense when the site is dynamic or protected, when you need thousands of pages processed reliably, when the data needs cleaning and validation, or when your time is better spent using the data than collecting it. Our guide on <a href="{root}blog/how-to-choose-web-scraping-freelancer.html">choosing a web scraping freelancer</a> covers what to look for.</p>
"""),
],
"faqs": [
("What is the difference between web scraping and web crawling?", "Crawling discovers pages by following links. Scraping extracts specific data from those pages. Most scraping projects include a small crawler to find the pages to scrape."),
("Can web scraping be done without coding?", "Point-and-click tools exist and work for simple sites. Complex, dynamic or large-scale extraction usually needs custom code to be complete and reliable."),
],
"services": ["website-web-scraping", "python-data-extraction"],
},
# --------------------------------------------------------------------------
{
"slug": "python-vs-selenium-vs-playwright",
"title": "Python vs Selenium vs Playwright: Which to Use for Web Scraping",
"meta": "Requests and BeautifulSoup, Selenium or Playwright? A practical comparison of speed, reliability and use cases for web scraping with Python.",
"category": "Tools",
"read": 8,
"answer": "This is not really Python versus the others: Selenium and Playwright are browser automation libraries you use from Python. Use plain Python HTTP tools (Requests, httpx with BeautifulSoup) when the data is in the page HTML or a JSON endpoint, because they are fastest. Use Playwright for JavaScript-heavy sites in new projects, and Selenium when you have existing Selenium infrastructure or need its particular browser support.",
"sections": [
("three-approaches", "Three approaches, not three languages", """
<p>All three options here are usually driven from Python:</p>
<ul>
<li><strong>HTTP libraries</strong> (Requests, httpx) download the raw HTML or JSON. Nothing is rendered and no JavaScript runs.</li>
<li><strong>Selenium</strong> drives a real browser through the WebDriver protocol.</li>
<li><strong>Playwright</strong> drives Chromium, Firefox and WebKit through its own protocol, with modern conveniences built in.</li>
</ul>
"""),
("comparison", "Side-by-side comparison", """
<table>
<thead><tr><th></th><th>Requests + BeautifulSoup</th><th>Selenium</th><th>Playwright</th></tr></thead>
<tbody>
<tr><td>Runs JavaScript</td><td>No</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Relative speed</td><td>Fastest</td><td>Slowest</td><td>Faster than Selenium in most cases</td></tr>
<tr><td>Waiting for elements</td><td>Not applicable</td><td>Explicit waits you write yourself</td><td>Auto-waiting built into actions</td></tr>
<tr><td>Network interception</td><td>Not applicable</td><td>Limited without extra tools</td><td>Built in: read and block requests</td></tr>
<tr><td>Resource use</td><td>Very low</td><td>High</td><td>High, though browser contexts are lightweight</td></tr>
<tr><td>Best for</td><td>Static pages, APIs, large crawls</td><td>Legacy suites, broad ecosystem</td><td>Modern dynamic sites, new projects</td></tr>
</tbody>
</table>
"""),
("when-requests", "When to use Requests and BeautifulSoup", """
<p>Always check this first. Open the browser's developer tools, look at the Network tab and reload the page. If the data appears in the initial HTML, or in a JSON response the page fetches, you can usually get it with plain HTTP requests. This is often ten or more times faster than a browser and much cheaper to run at scale.</p>
<pre><code>import requests
from bs4 import BeautifulSoup

html = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"}).text
soup = BeautifulSoup(html, "html.parser")
titles = [h.get_text(strip=True) for h in soup.select("h2.product-title")]</code></pre>
"""),
("when-playwright", "When to use Playwright", """
<p>Choose Playwright when content only appears after JavaScript runs, when you need to scroll, click or fill forms, or when the page loads data through background requests you want to capture. Its auto-waiting removes a whole class of flaky timing bugs, and its ability to listen to network responses often lets you collect clean JSON instead of parsing the rendered page. See <a href="{root}blog/handling-dynamic-websites-playwright.html">Handling dynamic websites using Playwright</a>.</p>
"""),
("when-selenium", "When Selenium still makes sense", """
<p>Selenium is mature and widely used. It is a sensible choice if your organisation already has Selenium infrastructure, such as Selenium Grid or existing test suites, or if a project needs a browser or language binding where Selenium has the edge. From my QA automation work, a well-written Selenium script with proper explicit waits is perfectly reliable. It just takes more code to get there.</p>
"""),
("rule-of-thumb", "A practical rule of thumb", """
<ol>
<li>Look for an API or JSON endpoint. If one exists, use HTTP requests.</li>
<li>If the data is in the HTML, use Requests and BeautifulSoup, or Scrapy for large crawls.</li>
<li>If JavaScript rendering or interaction is required, use Playwright.</li>
<li>If you are constrained by existing tooling, use Selenium.</li>
</ol>
<p>Many production scrapers mix approaches: a browser to get past a dynamic search page, then fast HTTP requests for the detail pages.</p>
"""),
],
"faqs": [
("Is Playwright better than Selenium for scraping?", "For most new scraping projects, yes, because of auto-waiting, network interception and speed. Selenium remains a solid choice where it is already established."),
("Is BeautifulSoup enough for web scraping?", "BeautifulSoup parses HTML. It is enough when the data is present in the HTML you download. It cannot run JavaScript, so dynamic sites need a browser tool."),
],
"services": ["python-data-extraction", "custom-web-automation"],
},
# --------------------------------------------------------------------------
{
"slug": "extract-data-from-thousands-of-websites",
"title": "How to Extract Data From Thousands of Websites",
"meta": "How to design one scraping pipeline that extracts the same fields from thousands of different websites: input cleaning, concurrency, retries and reporting.",
"category": "Scale",
"read": 8,
"answer": "To extract data from thousands of different websites, you build one pipeline that doesn't depend on any single layout. Clean the URL list first, use generic extraction rules (structured data, meta tags, contact pages and pattern matching), run requests concurrently with per-domain limits and retries, fall back to a headless browser only when needed, and log a status for every site.",
"sections": [
("different-problem", "Why this is a different problem", """
<p>Scraping one website means writing selectors for one layout. Scraping five thousand websites means you can't write five thousand sets of selectors. The pipeline has to find the data wherever it lives, accept that some sites will fail, and tell you exactly which ones did and why.</p>
"""),
("step-1", "Step 1: Clean the input list", """
<ul>
<li>Normalise URLs: add the scheme, lower-case the domain and strip tracking parameters.</li>
<li>Deduplicate by domain, since the same company is often listed with and without <code>www</code>.</li>
<li>Pre-check DNS and HTTP status to remove dead domains before the main run.</li>
</ul>
"""),
("step-2", "Step 2: Use layout-independent extraction", """
<p>Look for data in places that are consistent across sites:</p>
<ul>
<li><strong>Structured data:</strong> JSON-LD such as <code>Organization</code> or <code>LocalBusiness</code> schema often holds names, addresses and phone numbers.</li>
<li><strong>Meta tags:</strong> titles, descriptions and Open Graph data.</li>
<li><strong>Likely pages:</strong> follow links containing words like <em>contact</em>, <em>about</em> or <em>impressum</em>, using local-language equivalents too.</li>
<li><strong>Patterns:</strong> regular expressions for emails, phone numbers and social profile URLs, with validation to reject false positives.</li>
</ul>
"""),
("step-3", "Step 3: Run concurrently, but politely", """
<p>With thousands of different domains, you can make many requests in parallel without overloading any single server. An async HTTP client (for example <code>httpx</code> with <code>asyncio</code>) or Scrapy handles this well. Set a timeout on every request, a small per-domain limit and a retry policy with back-off for transient errors.</p>
<pre><code>sem = asyncio.Semaphore(50)   # global concurrency
async def fetch(client, url):
    async with sem:
        for attempt in range(3):
            try:
                r = await client.get(url, timeout=20, follow_redirects=True)
                return r.status_code, str(r.url), r.text
            except httpx.TransportError:
                await asyncio.sleep(2 ** attempt)
    return None, url, ""</code></pre>
"""),
("step-4", "Step 4: Fall back to a browser only when needed", """
<p>Headless browsers are slow and resource-hungry. Use the fast HTTP path first, and send a site to Playwright only when the HTML comes back nearly empty or the expected fields are missing. In a typical mixed list, only a minority of sites need the browser.</p>
"""),
("step-5", "Step 5: Checkpoint and report everything", """
<ul>
<li><strong>Checkpointing:</strong> write results as you go so a crash doesn't restart the job.</li>
<li><strong>Status per site:</strong> success, no data found, blocked, timeout or invalid domain.</li>
<li><strong>Source evidence:</strong> record the URL where each value was found.</li>
</ul>
<p>A transparent status column is what separates a professional deliverable from a spreadsheet with mysterious gaps. Once the data is collected, <a href="{root}blog/clean-scraped-data-python-pandas.html">clean it with Pandas</a>.</p>
"""),
],
"faqs": [
("How long does it take to scrape thousands of websites?", "It depends on how many pages per site are visited, how many need a browser, and the rate limits used. A pipeline for a few thousand homepages and contact pages typically runs in hours, not days."),
("Why do some websites return no data?", "Common reasons are dead domains, blocking, content loaded only by JavaScript, or the data simply not being published. A good pipeline labels each case."),
],
"services": ["website-web-scraping", "python-data-extraction"],
},
# --------------------------------------------------------------------------
{
"slug": "google-maps-data-extraction-guide",
"title": "Google Maps Data Extraction Guide",
"meta": "How to extract business data from Google Maps: available fields, search planning for full coverage, deduplication, emails, the Places API and compliance.",
"category": "Lead Generation",
"read": 8,
"answer": "Google Maps data extraction collects public business listing details, such as name, category, address, phone, website, rating and review count, for a category and location. Complete coverage depends on splitting large areas into many smaller searches and deduplicating the merged results. Emails are not usually on Maps and are collected from business websites instead.",
"sections": [
("fields", "What data is available", """
<p>A typical Google Maps listing can show:</p>
<ul>
<li>Business name and primary category</li>
<li>Full address and map coordinates</li>
<li>Phone number and website</li>
<li>Rating and review count</li>
<li>Opening hours</li>
<li>The listing's Maps URL, which is useful as a unique identifier</li>
</ul>
<p>Not every business fills in every field, so expect some blanks. That is the source, not an extraction error.</p>
"""),
("coverage", "The coverage problem", """
<p>A search on Google Maps shows a limited number of results, however many businesses exist. A search for <em>plumbers in California</em> returns only a fraction of the plumbers in California. Full coverage comes from planning:</p>
<ol>
<li>List every city, or every postcode, in the target region.</li>
<li>For dense cities, split further into neighbourhoods or map grid points.</li>
<li>Run each keyword in each area, plus close synonyms (for example <em>plumber</em>, <em>plumbing service</em>, <em>emergency plumber</em>).</li>
<li>Merge everything and deduplicate.</li>
</ol>
"""),
("dedup", "Deduplication done properly", """
<p>Overlapping searches return the same business many times. Deduplicate on the Maps listing URL or place ID first, then on normalised phone numbers, then on a normalised name and address combination, to catch the same business listed twice.</p>
"""),
("emails", "Getting email addresses", """
<p>Email addresses are rarely shown on Maps listings. The standard approach is enrichment: visit each listed website and look for publicly published emails on the homepage, contact page and footer. Expect a portion of businesses to have no public email at all. Read more in <a href="{root}blog/build-b2b-lead-generation-dataset.html">How to build a B2B lead generation dataset</a>.</p>
"""),
("api", "Scraping vs the Places API", """
<p>Google offers the official Places API, which returns structured place data under Google's terms and pricing. For some projects, especially ongoing integrations inside a product, the API is the right choice. For one-off research lists, browser-based extraction of public listings is commonly used. A good freelancer should tell you which suits your case.</p>
"""),
("compliance", "Compliance considerations", """
<p>Collecting business information that is shown publicly is different from collecting private data. Platform terms still apply, and so do data protection laws (GDPR, UK GDPR, CAN-SPAM and others) when you use the data for outreach. Keep outreach relevant, honour opt-outs and check your obligations in your region. This is general information, not legal advice.</p>
"""),
],
"faqs": [
("How many results can you get from Google Maps?", "As many as exist for your category and area, provided the search is split into enough small areas. A single search is capped; planned searches are not."),
("Does Google Maps data include emails?", "Usually not. Emails are found by visiting each business's own website and collecting publicly published addresses."),
],
"services": ["google-maps-data-extraction", "b2b-lead-generation"],
},
# --------------------------------------------------------------------------
{
"slug": "scrape-ecommerce-product-data",
"title": "How to Scrape E-commerce Product Data",
"meta": "How to scrape e-commerce product data reliably: category mapping, JSON-LD and product JSON, variants, images, prices and import-ready delivery.",
"category": "E-commerce",
"read": 8,
"answer": "To scrape e-commerce product data reliably, map the store's category and listing pages to collect every product URL, then extract each product from embedded structured data (JSON-LD or the store's product JSON) where available, falling back to HTML parsing. Expand variants into rows, collect image URLs, normalise prices and validate before delivery.",
"sections": [
("map", "Map the store first", """
<p>Start by understanding how the store is organised: the category tree, how listing pages paginate (page numbers, <em>load more</em> buttons or infinite scroll) and how product URLs look. Building a complete, deduplicated list of product URLs is half the job. Sitemaps (<code>/sitemap.xml</code>) often list every product and are a good cross-check.</p>
"""),
("structured", "Look for structured data before parsing HTML", """
<p>Most modern stores embed machine-readable product data:</p>
<ul>
<li><strong>JSON-LD</strong> <code>Product</code> schema with name, SKU, brand, price, currency and availability, added for search engines.</li>
<li><strong>Platform JSON:</strong> many store platforms expose product data as JSON, and many themes embed it in the page.</li>
<li><strong>Background API calls</strong> visible in the browser's Network tab.</li>
</ul>
<pre><code>import json
from bs4 import BeautifulSoup

for tag in soup.select('script[type="application/ld+json"]'):
    data = json.loads(tag.string or "{}")
    if isinstance(data, dict) and data.get("@type") == "Product":
        offer = data.get("offers", {})
        print(data.get("name"), data.get("sku"), offer.get("price"))</code></pre>
<p>Structured data is more accurate than visible text and survives redesigns better.</p>
"""),
("variants", "Handle variants deliberately", """
<p>Decide early whether you need one row per product or one row per variant. Import tools usually want one row per variant, with a shared parent ID, a variant SKU, option values such as size and colour, and a variant price. Agree this format before extraction to avoid reshaping later.</p>
"""),
("prices", "Prices, currencies and stock", """
<ul>
<li>Store prices as numbers, not text. Strip currency symbols and thousands separators, and keep a separate currency column.</li>
<li>Capture both regular and sale price where shown.</li>
<li>Be aware that prices and availability can vary by region, cookies or logged-in state.</li>
</ul>
"""),
("images", "Images", """
<p>Collect full-resolution image URLs rather than thumbnails. Many stores serve resized images through URL parameters. If you need the files, download them into folders named by SKU, and keep the original URL in your spreadsheet.</p>
"""),
("validate", "Validate before you deliver", """
<p>Check for products with missing prices, duplicate SKUs, empty titles and broken image links. Compare the product count against the store's category counts or sitemap. For JavaScript-heavy stores, see <a href="{root}blog/handling-dynamic-websites-playwright.html">Handling dynamic websites using Playwright</a>.</p>
"""),
],
"faqs": [
("Can you scrape Shopify stores?", "Many Shopify stores expose product data in a structured form, which makes extraction efficient. Each store is checked individually."),
("How do I monitor competitor prices?", "Run the same scraper on a schedule, store each run with a date, and compare runs to flag price and stock changes."),
],
"services": ["ecommerce-product-scraping", "data-cleaning-excel-automation"],
},
# --------------------------------------------------------------------------
{
"slug": "build-b2b-lead-generation-dataset",
"title": "How to Build a B2B Lead Generation Dataset",
"meta": "A step-by-step method for building a B2B lead dataset: define your ICP, choose public sources, extract, enrich, deduplicate, verify and export to your CRM.",
"category": "Lead Generation",
"read": 9,
"answer": "To build a B2B lead generation dataset, define your ideal customer profile, choose public sources that list those companies, extract a base list, enrich each company with website, contact and segmentation data, deduplicate and verify the records, then export in your CRM's import format.",
"sections": [
("icp", "1. Define your ideal customer profile", """
<p>Start with the target, not the tool. Write down:</p>
<ul>
<li>Industries and sub-industries</li>
<li>Countries, regions or cities</li>
<li>Size signals such as employee count, number of locations or presence of a careers page</li>
<li>Target job titles and seniority</li>
<li>Exclusions such as existing customers, competitors or franchises</li>
</ul>
<p>Every later decision, including sources, fields and filters, follows from this.</p>
"""),
("sources", "2. Choose the right public sources", """
<table>
<thead><tr><th>Source</th><th>Good for</th></tr></thead>
<tbody>
<tr><td>Google Maps</td><td>Local and SMB businesses by category and area</td></tr>
<tr><td>Business directories and Yellow Pages</td><td>Trades and professions by location</td></tr>
<tr><td>Industry associations</td><td>Verified members of a specific industry</td></tr>
<tr><td>Event and exhibitor lists</td><td>Companies active in a market right now</td></tr>
<tr><td>Company websites</td><td>Emails, phones, team pages and enrichment</td></tr>
</tbody>
</table>
"""),
("extract", "3. Extract a base list", """
<p>Collect company name, website, location and category from your primary source. Keep the source URL for every record. See the <a href="{root}blog/google-maps-data-extraction-guide.html">Google Maps data extraction guide</a> for one of the most common starting points.</p>
"""),
("enrich", "4. Enrich", """
<ul>
<li>Visit each website for publicly listed emails, phone numbers and social links.</li>
<li>Find decision-makers from team pages and public professional profiles.</li>
<li>Add segmentation columns that match your ICP.</li>
</ul>
"""),
("clean", "5. Deduplicate and verify", """
<p>Deduplicate on website domain first. It is the most reliable company key. Then standardise phone formats, fix capitalisation and remove obviously invalid emails. Before sending any campaign, run emails through a dedicated verification service. No lead list should claim a guaranteed deliverability rate. The <a href="{root}blog/clean-scraped-data-python-pandas.html">Pandas cleaning guide</a> covers the techniques.</p>
"""),
("deliver", "6. Deliver in CRM format", """
<p>Match your CRM's import template column for column: HubSpot, Salesforce, Pipedrive or custom. Separate company and contact records if your CRM uses associations.</p>
"""),
("compliance", "A note on compliance", """
<p>B2B outreach is still regulated. GDPR and UK GDPR apply to personal data such as names and work emails, and rules like CAN-SPAM govern commercial email. Use data for relevant outreach, include opt-outs and keep records of your sources. This is general information, not legal advice.</p>
"""),
],
"faqs": [
("How many leads should a B2B list have?", "Enough to match your outreach capacity and test properly. A smaller, accurately targeted list usually outperforms a large generic one."),
("Should I buy a lead list or build one?", "Bought lists are often outdated and shared with competitors. A custom-built list matches your ICP and comes from current public sources."),
],
"services": ["b2b-lead-generation", "business-directory-scraping"],
},
# --------------------------------------------------------------------------
{
"slug": "handling-dynamic-websites-playwright",
"title": "Handling Dynamic Websites Using Playwright",
"meta": "How to scrape JavaScript-heavy websites with Playwright and Python: auto-waiting, infinite scroll, capturing JSON responses and faster, reliable runs.",
"category": "Tools",
"read": 9,
"answer": "To scrape a dynamic website with Playwright, load the page in a headless browser, let Playwright's auto-waiting or explicit locators wait for the content, scroll or click to trigger loading, and, where possible, capture the JSON responses the page fetches instead of parsing the rendered HTML. Block images and fonts to speed things up.",
"sections": [
("why-dynamic", "Why dynamic sites break simple scrapers", """
<p>On a dynamic site, the HTML you download is often an empty shell. The content arrives afterwards through JavaScript and background requests. Requests and BeautifulSoup see the shell; a real browser sees the content. Playwright gives you that browser, controlled from Python.</p>
"""),
("basics", "The basics", """
<pre><code>from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://example.com/listings", wait_until="domcontentloaded")
    cards = page.locator(".listing-card")
    cards.first.wait_for()                # wait until content exists
    for i in range(cards.count()):
        print(cards.nth(i).locator("h2").inner_text())
    browser.close()</code></pre>
<p>Locators in Playwright wait automatically for elements to be ready before acting, which removes most timing problems. Avoid fixed <code>sleep()</code> calls. Wait for the thing you need.</p>
"""),
("network", "Capture the JSON, not the HTML", """
<p>The most useful Playwright technique for scraping is listening to network responses. If the page fetches its listings from an internal API, you can capture that clean JSON directly:</p>
<pre><code>results = []
def on_response(resp):
    if "/api/search" in resp.url and resp.ok:
        results.extend(resp.json().get("items", []))
page.on("response", on_response)
page.goto(url)</code></pre>
<p>This is faster and more accurate than reading visible text, and it often includes fields the page never displays.</p>
"""),
("scroll", "Infinite scroll and load-more buttons", """
<p>Scroll in a loop until no new items appear, or click <em>load more</em> until the button disappears. Always set a maximum number of iterations and stop when the item count stops growing.</p>
<pre><code>prev = -1
while True:
    count = page.locator(".item").count()
    if count == prev: break
    prev = count
    page.mouse.wheel(0, 4000)
    page.wait_for_timeout(800)</code></pre>
"""),
("speed", "Make it faster", """
<ul>
<li><strong>Block heavy resources:</strong> route images, fonts and media to abort when you don't need them.</li>
<li><strong>Reuse browser contexts:</strong> contexts are lightweight compared with launching new browsers.</li>
<li><strong>Use the browser only where needed:</strong> once you know the API endpoint or detail-page pattern, plain HTTP is faster.</li>
</ul>
"""),
("reliability", "Make it reliable", """
<ul>
<li>Wrap each page in try/except, retry transient failures and save a screenshot on error.</li>
<li>Write results incrementally so a long run can resume.</li>
<li>Pace requests and run at sensible volumes. Respect the site.</li>
</ul>
<p>For when to choose Playwright over alternatives, see <a href="{root}blog/python-vs-selenium-vs-playwright.html">Python vs Selenium vs Playwright</a>.</p>
"""),
],
"faqs": [
("Is Playwright good for web scraping?", "Yes. It is one of the best tools for JavaScript-heavy sites, thanks to auto-waiting, multi-browser support and network interception."),
("Can Playwright run headless?", "Yes. Headless mode is the default for automated runs. Headed mode is useful for debugging."),
],
"services": ["custom-web-automation", "website-web-scraping"],
},
# --------------------------------------------------------------------------
{
"slug": "clean-scraped-data-python-pandas",
"title": "How to Clean Scraped Data Using Python Pandas",
"meta": "Pandas techniques for cleaning scraped data: whitespace, types, prices, phones, emails, deduplication, fuzzy matching and formatted Excel export.",
"category": "Data Cleaning",
"read": 9,
"answer": "To clean scraped data with Pandas, load it into a DataFrame, strip whitespace and stray HTML, convert columns to proper types (numbers, dates), standardise formats such as phone numbers and URLs, validate emails, deduplicate on reliable keys like domain or listing URL, then export to a formatted Excel or CSV.",
"sections": [
("load", "Load and inspect", """
<pre><code>import pandas as pd
df = pd.read_csv("raw.csv", dtype=str)
print(df.shape)
print(df.isna().mean().sort_values(ascending=False))  # share of blanks per column</code></pre>
<p>Load everything as text first (<code>dtype=str</code>) so nothing is silently converted, such as phone numbers losing leading zeros.</p>
"""),
("text", "Clean text", """
<pre><code>text_cols = df.columns
df[text_cols] = df[text_cols].apply(lambda s: s.str.replace(r"\\s+", " ", regex=True).str.strip())
df = df.replace({"": pd.NA, "N/A": pd.NA, "-": pd.NA})</code></pre>
<p>Collapse repeated whitespace and line breaks, and turn placeholder values into real blanks.</p>
"""),
("numbers", "Prices and numbers", """
<pre><code>df["price"] = (df["price"].str.replace(r"[^0-9.,]", "", regex=True)
                           .str.replace(",", "", regex=False)
                           .astype(float))</code></pre>
<p>Watch for regional formats: <code>1.299,00</code> in many European countries means 1299.00. Handle these per source rather than with one global rule.</p>
"""),
("phones-emails", "Phone numbers, emails and URLs", """
<ul>
<li><strong>Phones:</strong> keep digits and a leading <code>+</code>. For international data, the <code>phonenumbers</code> library formats numbers to E.164 reliably.</li>
<li><strong>Emails:</strong> lower-case them, strip <code>mailto:</code>, and reject anything that fails a basic pattern or ends in image extensions (a common scraping false positive, such as <code>logo@2x.png</code>).</li>
<li><strong>URLs:</strong> add missing schemes and extract the domain into its own column. It is the best company key.</li>
</ul>
<pre><code>df["email"] = df["email"].str.lower().str.replace("mailto:", "", regex=False)
ok = df["email"].str.match(r"^[\\w.+-]+@[\\w-]+\\.[\\w.-]+$", na=False) & ~df["email"].str.contains(r"\\.(png|jpg|gif|webp)$", na=False)
df.loc[~ok, "email"] = pd.NA
df["domain"] = df["website"].str.extract(r"https?://(?:www\\.)?([^/]+)", expand=False).str.lower()</code></pre>
"""),
("dedup", "Deduplicate", """
<pre><code>df = df.sort_values("filled", ascending=False) if "filled" in df else df
df = df.drop_duplicates(subset=["domain"], keep="first")</code></pre>
<p>Choose keys in order of reliability: listing URL or ID, then domain, then normalised phone, then normalised name plus city. For names that differ slightly (<em>Acme Ltd</em> vs <em>ACME Limited</em>), normalise legal suffixes and consider fuzzy matching with a library such as <code>rapidfuzz</code>, reviewing matches below a confidence threshold.</p>
"""),
("export", "Export a professional Excel file", """
<pre><code>with pd.ExcelWriter("clean.xlsx", engine="xlsxwriter") as xw:
    df.to_excel(xw, index=False, sheet_name="Data")
    ws = xw.sheets["Data"]
    ws.freeze_panes(1, 0)
    ws.autofilter(0, 0, len(df), len(df.columns) - 1)</code></pre>
<p>Frozen headers, filters and sensible column widths make a dataset feel finished. Keep a short summary of what you changed, such as rows removed and fields corrected. It builds trust in the data.</p>
"""),
],
"faqs": [
("Why load scraped data as strings?", "So Pandas doesn't guess types and damage values, for example by dropping leading zeros from phone numbers or postcodes. Convert columns deliberately afterwards."),
("What is the best key for deduplicating companies?", "The website domain is usually the most reliable single key, followed by phone number and a normalised name plus location."),
],
"services": ["data-cleaning-excel-automation", "python-data-extraction"],
},
# --------------------------------------------------------------------------
{
"slug": "web-scraping-for-real-estate",
"title": "Web Scraping for Real Estate Businesses",
"meta": "How real estate investors, agencies and proptech teams use web scraping: listing data, comparables, price tracking, agent lists and responsible use.",
"category": "Real Estate",
"read": 7,
"answer": "Real estate businesses use web scraping to collect public property listing data, such as prices, locations, features, listing dates and agent details, from portals and agency websites. They use it for comparables, market tracking, investment screening and agent outreach, normalising units and property types so different sources can be compared.",
"sections": [
("who", "Who uses real estate data, and why", """
<ul>
<li><strong>Investors:</strong> screen deals and compare asking prices, rents and yields across areas.</li>
<li><strong>Agencies:</strong> track competitor listings, pricing and time on market.</li>
<li><strong>Proptech and analytics teams:</strong> feed dashboards and valuation models.</li>
<li><strong>Service providers:</strong> mortgage brokers, movers, stagers and photographers building agent and agency lists.</li>
</ul>
"""),
("fields", "Typical data fields", """
<table>
<thead><tr><th>Group</th><th>Fields</th></tr></thead>
<tbody>
<tr><td>Listing</td><td>URL, ID, title, status, listed or updated date</td></tr>
<tr><td>Price</td><td>Asking price or rent, currency, price per unit area</td></tr>
<tr><td>Property</td><td>Type, bedrooms, bathrooms, area, lot size, year built, features</td></tr>
<tr><td>Location</td><td>Address, city, postcode, coordinates</td></tr>
<tr><td>Agent</td><td>Agent name, agency, public phone and email</td></tr>
</tbody>
</table>
"""),
("normalise", "Normalise or you can't compare", """
<p>Every portal labels things differently: <em>flat</em>, <em>apartment</em> and <em>condo</em>; square feet and square metres; <em>POA</em> instead of a price. Before analysis, map property types to one list, convert areas to one unit, store prices as numbers with a currency column, and flag listings without a public price instead of dropping them.</p>
"""),
("tracking", "Tracking change over time", """
<p>Real estate data is most valuable as a time series. Scheduled runs, for example weekly, with each run stored and compared to the last, reveal new listings, removed listings (often sold or let) and price reductions. These are signals a single snapshot can't show.</p>
"""),
("technical", "Technical notes", """
<p>Property portals are often dynamic, with map-based search, infinite scroll and filters, and many use bot protection. Playwright handles dynamic search pages well, and many portals load results from internal JSON endpoints that are cleaner to capture. See <a href="{root}blog/handling-dynamic-websites-playwright.html">Handling dynamic websites using Playwright</a>.</p>
"""),
("responsible", "Responsible use", """
<p>Listing photos and descriptions are usually copyrighted, so analyse them rather than republish them. Agent contact details are personal data in many regions. Respect portal terms and data protection rules for your market. This is general information, not legal advice.</p>
"""),
],
"faqs": [
("Can I scrape property portals for price tracking?", "Price tracking from public listings is a common use case. Check the portal's terms and your local rules, and pace data collection responsibly."),
("How often should real estate data be collected?", "Weekly runs suit most market tracking. Fast-moving rental markets may justify more frequent runs."),
],
"services": ["real-estate-data-extraction", "data-cleaning-excel-automation"],
},
# --------------------------------------------------------------------------
{
"slug": "how-to-choose-web-scraping-freelancer",
"title": "How to Choose a Professional Web Scraping Freelancer",
"meta": "What to look for when hiring a web scraping freelancer: questions to ask, sample data, data quality, compliance, red flags and how to write a clear brief.",
"category": "Hiring",
"read": 7,
"answer": "Choose a web scraping freelancer who asks clarifying questions about your fields and use case, offers a sample before the full run, explains how they will handle pagination, dynamic content and duplicates, delivers in your exact format, talks openly about compliance, and has a verifiable track record of similar projects.",
"sections": [
("brief", "Start with a clear brief", """
<p>You will get better quotes, and spot better freelancers, if your brief includes:</p>
<ul>
<li>The target URL or URLs, and an example page</li>
<li>The exact fields you need, ideally as column headers</li>
<li>An estimate of the number of records</li>
<li>Output format: Excel, CSV, JSON, Google Sheets or a CRM template</li>
<li>One-off or recurring, and your deadline</li>
</ul>
<p>The <a href="{root}contact.html">project enquiry form</a> on this site asks for exactly these details.</p>
"""),
("questions", "Questions a good freelancer will ask you", """
<ul>
<li>What will you use the data for? This affects sources, fields and compliance.</li>
<li>Do you need one row per item or per variant, location or contact?</li>
<li>Should blanks be left blank, or the record excluded?</li>
<li>How should duplicates be handled?</li>
</ul>
<p>If a freelancer quotes instantly without asking anything, they may not have looked at the site.</p>
"""),
("signals", "Signals of real expertise", """
<ul>
<li><strong>A sample first:</strong> a small sample lets you check columns and quality before paying for scale.</li>
<li><strong>Technical clarity:</strong> they can explain, in plain terms, whether the site needs a browser, how they'll cover pagination and search caps, and how they'll validate results.</li>
<li><strong>Traceability:</strong> source URLs in the output.</li>
<li><strong>Honest limits:</strong> they say what can't be collected, rather than over-promising.</li>
<li><strong>Track record:</strong> verifiable reviews and similar past projects.</li>
</ul>
"""),
("red-flags", "Red flags", """
<ul>
<li>Guaranteed email deliverability percentages or guaranteed sales results</li>
<li>Willingness to bypass logins, paywalls or security without discussion</li>
<li>No sample, no questions, and a price that seems too good to be true</li>
<li>Vague answers about where the data comes from</li>
</ul>
"""),
("compliance", "Compliance should come up early", """
<p>A professional should raise compliance before you have to: public versus personal data, terms of service and how you plan to use the data. That isn't bureaucracy. It protects your business.</p>
"""),
("next", "Next steps", """
<p>If you have a project in mind, see the <a href="{root}services.html">services</a> I offer, browse <a href="{root}portfolio.html">case studies</a>, or <a href="{root}contact.html">request a quote</a>.</p>
"""),
],
"faqs": [
("Should I hire a freelancer or use a scraping tool?", "Tools work for simple, small jobs. A freelancer is better for complex sites, large volumes, custom cleaning or when you need a guaranteed format."),
("What should a web scraping quote include?", "The fields, record estimate, output format, delivery time, whether a sample is included, and whether the script or future re-runs are part of the price."),
],
"services": ["website-web-scraping", "b2b-lead-generation"],
},
]
