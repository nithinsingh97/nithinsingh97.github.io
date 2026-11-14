# Nithin Singh: Web Scraping & Data Extraction Specialist

Personal brand website built with plain **HTML5, CSS3 and vanilla JavaScript**. There is no framework, no Node.js, no build step needed to deploy, and no tracking. It is hosted free on **GitHub Pages**.

## What's included

| Path | Contents |
|---|---|
| `index.html` | Homepage: hero, credentials, services, process, tech, case studies, why hire me, FAQ, guides, CTA |
| `about.html` | Freelancing journey, expertise, approach, values |
| `services.html` + `services/` | Services overview + 10 individual service pages |
| `portfolio.html` + `case-studies/` | Case study index + 7 case study pages (**placeholders marked; see below**) |
| `blog.html` + `blog/` | Blog index + 10 full articles with author info and FAQs |
| `contact.html` | Project enquiry form (mailto fallback or Google Forms) + Fiverr CTA |
| `404.html` | Custom not-found page (noindex) |
| `robots.txt`, `sitemap.xml` | Crawl rules (incl. OAI-SearchBot) and sitemap |
| `assets/css/style.css` | The single stylesheet |
| `assets/js/main.js` | Mobile menu, scroll effects, contact form (≈5 KB, no dependencies) |
| `assets/images/` | Favicon, Open Graph image, diagram |
| `_tools/` | Optional Python generator and checker (not published by GitHub Pages) |

**SEO/GEO built in:** unique title and description on every page, canonical URLs, Open Graph and Twitter cards, breadcrumbs, semantic HTML, JSON-LD (`Person`, `WebSite`, `ProfilePage`, `Service`, `BlogPosting`, `Article`, `FAQPage`, `BreadcrumbList`, `ItemList`) with one consistent author identity, "quick answer" boxes and FAQ sections written as direct answers.

---

## 1. Before you deploy: replace 2 placeholders

### A. Your site URL
Every page contains `https://nithinsingh97.github.io` (canonical tags, Open Graph, schema, sitemap, robots.txt).

**Easiest:** in VS Code press `Ctrl+Shift+H` (Replace in Files), search `nithinsingh97`, replace it with your GitHub username, then **Replace All**.

### B. Your contact email
Search for `your-email@example.com` and replace it with your business email. Until you do, the contact form shows visitors an honest message and points them to Fiverr instead of pretending to send.

> If you use the Python generator (section 4), make these changes in `_tools/build.py` → `CONFIG` instead and rebuild.

---

## 2. Deploy to GitHub Pages

1. **Create the repository.** On GitHub, create a new **public** repo named exactly **`YOUR-USERNAME.github.io`** (for example `nithinsingh.github.io`). This gives you the clean root URL `https://YOUR-USERNAME.github.io/`.
2. **Upload the files.** Either:
   - **Web:** open the repo → *Add file → Upload files* → drag in **the contents** of this folder (not the folder itself) → *Commit changes*; or
   - **Git:**
     ```bash
     cd path/to/this/folder
     git init
     git add .
     git commit -m "Initial site"
     git branch -M main
     git remote add origin https://github.com/YOUR-USERNAME/YOUR-USERNAME.github.io.git
     git push -u origin main
     ```
3. **Turn on Pages.** Repo → *Settings → Pages* → *Source: Deploy from a branch* → Branch `main`, folder `/ (root)` → *Save*.
4. Wait 1–2 minutes, then open `https://YOUR-USERNAME.github.io/`.

**Using a different repo name** (for example `portfolio`)? Your site will live at `https://YOUR-USERNAME.github.io/portfolio/`. Internal links still work (they're relative), but also: set `SITE_URL` to `https://YOUR-USERNAME.github.io/portfolio` and `BASE_PATH` to `/portfolio/` in `_tools/build.py` and rebuild, or update the 404 page links by hand. Note that `robots.txt` is only read at a domain root, so a user-site repo (step 1) is recommended.

**Custom domain (optional):** *Settings → Pages → Custom domain*, add your domain, follow GitHub's DNS instructions, tick *Enforce HTTPS*, then replace the site URL everywhere as in step 1A.

---

## 3. After launch: get indexed

1. **Google Search Console** (search.google.com/search-console): add your site, verify it (the HTML-tag method works: paste the meta tag into `index.html`'s `<head>`), then submit `sitemap.xml`.
2. **Bing Webmaster Tools** (bing.com/webmasters): import from Search Console or add manually, then submit the sitemap. ChatGPT search relies partly on Bing's index, so this step matters.
3. **Validate structured data:** test a few URLs at validator.schema.org and Google's Rich Results Test.
4. **Strengthen your identity signals:** add your Fiverr *profile* URL, LinkedIn and GitHub to `SAME_AS` in `_tools/build.py` and rebuild (or edit the `"sameAs"` list in the JSON-LD). Link back to this site from those profiles.

Allowing crawlers in `robots.txt` makes the site **eligible** to be found. It does not guarantee rankings or that ChatGPT or any AI assistant will recommend you. Real case studies, consistent profiles and links from other sites are what build visibility over time.

---

## 4. Editing the site

**Option A: edit HTML directly.** Open any `.html` file in VS Code and change the text. Simple and fine for small edits.

**Option B: use the generator (recommended for bigger changes).** All content lives in Python files, and one command rebuilds all 34 pages consistently (headers, footers, schema, sitemap):

```bash
python _tools/build.py        # rebuild every page, sitemap.xml and robots.txt
python _tools/check_site.py   # verify links, anchors, metadata, schema, sitemap
```

| To change… | Edit |
|---|---|
| Name, URLs, email, **order count / review count**, dates | `_tools/build.py` → `CONFIG` block (`ORDERS`, `REVIEWS`, …) |
| Service pages | `_tools/content_services.py` |
| Case studies | `_tools/content_cases.py` |
| Blog articles | `_tools/content_blog.py` |
| Design | `assets/css/style.css` (colours are variables at the top) |

Python 3.8+ is required, using only the standard library. Don't mix the options: rebuilding overwrites manual HTML edits.

**Adding a blog article:** copy an entry in `content_blog.py`, give it a new `slug`, write the content, rebuild. It automatically appears on the blog index, in the sitemap and with full schema.

---

## 5. Case studies: replace the placeholders

The 7 case studies describe the **typical technical approach** for each type of project. Every client-specific detail (industry, volume, timeline, outcome) is a **yellow placeholder**, and each page carries a "Sample case study" notice. Nothing is fabricated.

To publish a real one: in `_tools/content_cases.py`, replace the `ph("…")` values with real, verifiable details (anonymise the client if needed, e.g. "UK property agency"), then set `"sample": False` to remove the notice. Only include results the client has confirmed.

---

## 6. Contact form

The site has no backend, so the form works in one of two honest ways:

- **Default (mailto):** submitting opens the visitor's email app with all fields prefilled, addressed to your email. The visitor still presses *Send*.
- **Google Forms (free, no email app needed):**
  1. Create a Google Form with the 8 fields (Name, Business email, Company website, Project description, Data source URL, Estimated records, Output format, Deadline) as short/long answer questions.
  2. Open the form's preview → right-click → *View page source* → find each field's `entry.123456789` name, and the form ID in the URL.
  3. In `_tools/build.py` set `GOOGLE_FORM_ACTION = "https://docs.google.com/forms/d/e/<FORM_ID>/formResponse"` and fill `GOOGLE_FORM_ENTRIES` with each `entry.xxx`, then rebuild.
  4. Submissions open Google's confirmation page in a new tab and land in your form's Responses (link it to a Google Sheet and enable email notifications).

---

## 7. Pre-deployment testing (already done)

- `_tools/check_site.py`: all internal links and `#anchors` resolve, every image exists and has alt text plus lazy loading, every page has exactly one `<h1>`, unique titles and descriptions (50–160 characters), canonical URLs, OG and Twitter tags, valid JSON-LD with the expected types, a Fiverr CTA on every page, and a sitemap that matches the files exactly.
- Browser tests (Chrome): all 34 pages at 375 px, 768 px and 1440 px, with no console errors, no failed requests and no horizontal overflow; the mobile menu opens and closes (including the Esc key); form validation and the mailto flow work.

Re-run `python _tools/check_site.py` after every change.
