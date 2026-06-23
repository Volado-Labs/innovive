# Innovive Staging — Internal Link Integrity Audit
**Date:** 2026-06-12  ·  **Crawler:** authenticated + cache-busted BFS of the live front-end
**Scope:** 55 published pages crawled · 7,184 link instances · 45 unique internal targets · 76-URL inventory (pages/posts/teams/products)

## ✅ Headline: structural integrity is clean
- **0 broken internal links** — every internal `<a href>` target returns 200 when authenticated.
- **0 links to draft/private pages** — nothing public points at a page the public would see as 404.
- **0 unexpected redirects** on internal link targets.

The issues below are **placeholder `#` links** (CTAs/cross-links not yet wired) and a few **cleanup items** — not broken links per se, but they go nowhere when clicked.

## 1. Footer "Resources" links are dead `#` — but the pages now EXIST (wire these)
Each appears on all 54 pages (sitewide footer). Pages are built and published:

| Footer label | Target page (exists) | Currently |
|---|---|---|
| FAQ | /faq/ | `#` |
| Case Studies | /case-studies/ | `#` |
| Events | /events/ | `#` |
| Patents | /patents/ | `#` |
| Video Training | *(no page yet)* | `#` — OK to leave until built |

## 2. Dead `#` CTAs & cross-links by page (154 instances across 37 pages)
These are buttons/links with `href="#"` — they render but do nothing. Excludes the legitimate sitewide nav dropdown toggles (Products/Mouse/Rat/Mouse & Rat/The Innovive System/Company) and the footer items above.

**/** — 3
  - `Explore` · `View All News` · `Read More`
**/about/** — 6
  - `Globally Trusted partner` · `Explore Solutions` · `our mission and vision` · `Leadership` · `LEADERSHIP` · `Explore More`
**/aquavive-mouse-water/** — 2
  - `Mouse Water` · `Contact sales`
**/aquavive-rat-water/** — 1
  - `Rat Water`
**/blog-news/** — 5
  - `Latest blogs` · `Read More` · `View All` · `Latest News` · `View All News Articles`
**/ca-supply-chain/** — 1
  - `Supply chain`
**/career/** — 4
  - `Globally Trusted partner` · `View Open Position` · `Life At Innovive` · `Innovive life`
**/contact/** — 1
  - `CONTACT US`
**/gnotobiotics/** — 8
  - `gnotobiotics` · `Explore` · `IVC System` · `Benefits` · `Contact Us` · `THREE PILLARS` · `video` · `Testimonials`
**/inno/** — 6
  - `Start now` · `Services` · `Testimonials` · `Partner` · `Explore Services` · `Request a Demo`
**/innorack-ivc-rat/** — 4
  - `Contact Sales` · `COMPATIBLE CAGING` · `View Caging` · `Contact sales`
**/innorack-mouse/** — 5
  - `Contact Sales` · `Download data sheet` · `COMPATIBLE CAGING` · `View Caging` · `Contact sales`
**/innorack-rat/** — 4
  - `Contact Sales` · `COMPATIBLE CAGING` · `View Caging` · `Contact sales`
**/innovive-water-process/** — 7
  - `Water Processing` · `Order Aquavive Water` · `In-House Water Prep Actually Costs` · `How Aquavive Water Is Made` · `What Arrives at Your Facility` · `Request a Sample` · `Contact Our Team`
**/metabolic-cage-kit/** — 2
  - `View Cage Components` · `Download PDF for Info`
**/mouse-caging-m-btm-xl/** — 1
  - `Talk to sales`
**/mouse-feeders/** — 1
  - `Mouse Feeder`
**/mouse-lids/** — 2
  - `MOUSE LID` · `MOUSE ENRICHMENT`
**/mouse-rat-bedding/** — 2
  - `Bedding Options` · `Contact sales`
**/mouse-transportation-cart/** — 1
  - `Innocart`
**/privacy-policy/** — 1
  - `Legal`
**/products/** — 1
  - `Globally Trusted Partner`
**/products/enrichment/** — 2
  - `MOUSE & RAT ENRICHMENT` · `Talk to an Expert`
**/rat-caging/** — 2
  - `Rat Caging` · `Contact Innovive`
**/rat-feeders/** — 3
  - `Rat Feeder` · `RELATED` · `Contact sales`
**/rat-lid/** — 2
  - `Rat Cage Lids` · `Request sample`
**/rat-racks/** — 2
  - `Innorack IVC Rat System` · `Contact sales`
**/recycling-eu/** — 7
  - `Recycling` · `Ask About Availability` · `The Problem` · `How EU Recycling Program Works` · `Why This Matters for Your Facility` · `Ask About EU Recycling Availability` · `Contact Our Sustainability Team`
**/regional-distributors/** — 4
  - `Globally distributor` · `GLOBAL` · `DISTRIBUTORS` · `Visit Website`
**/research-ready/** — 7
  - `Research Ready` · `Explore` · `Research Ready Products` · `Explore Innovive IVC Systems` · `A Research Ready TEAM From the Start` · `Learn about Inno+ Vivarium Solutions` · `Learn more about our sustainability efforts`
**/supply-chain-logistics/** — 3
  - `Supply Chain & Logistics` · `Explore Our Operations` · `View Logistics Network`
**/sustainability/** — 7
  - `Sustainability` · `Learn About InnoCycle` · `Environmental Case for Disposable IVC` · `How We Design` · `Closed-Loop Recycling Through InnoCycle` · `Contact Us About Recycling` · `Learn More About InnoCycle`
**/system-benefits/** — 7
  - `System Benefits` · `Get Started` · `Animal Welfare` · `Ergonomics` · `Biosecurity` · `Scalability` · `Contact Us`
**/tall-rat-01/** — 4
  - `Contact Sales` · `COMPATIBLE CAGING` · `View Caging` · `Contact sales`
**/tall-rat-xl/** — 5
  - `Innorack Tall IVC Rat XL` · `Contact Sales` · `COMPATIBLE CAGING` · `View Caging` · `Contact sales`
**/team/** — 1
  - `LEADERSHIP`
**/terms-and-conditions/** — 1
  - `Terms & conditions`

## 3. External links — review

| Domain | Count | What | Verdict |
|---|---|---|---|
| shop.innovive.com | 216 | "Customer Portal" nav (NetSuite/shop) | ✅ expected |
| pdfpiw.uspto.gov | 18 | Patent PDF links on /patents/ | ✅ legit external |
| www.innovive.com | 17 | "Download PDF →" datasheets pointing to the OLD live site | ⚠️ REVIEW — migrate assets to new site or confirm they stay hosted on innovive.com (will 404 if old site is decommissioned at launch) |

Pages with old-domain PDF links:
  - /case-studies/ — `Download PDF →` → https://www.innovive.com/_files/ugd/a212fc_4c311cfde64d4f26876707b248f6ba33.pdf
  - /case-studies/ — `Download PDF →` → https://www.innovive.com/_files/ugd/a212fc_6e387f43da504b3f8730dc53cd6cef8d.pdf
  - /case-studies/ — `Download PDF →` → https://www.innovive.com/_files/ugd/a212fc_70d2a29f0a12475e85c1e48a2cf88c80.pdf
  - /case-studies/ — `Download PDF →` → https://www.innovive.com/_files/ugd/a212fc_e3bf19eee47c43ffa57ddd136b666703.pdf
  - /case-studies/ — `Download PDF →` → https://www.innovive.com/_files/ugd/ddd952_004509b726464908bbb500fbaddd34d8.pdf
  - /case-studies/ — `Download PDF →` → https://www.innovive.com/_files/ugd/ddd952_0bbc2a0336a5476c86a869d28ef93cf0.pdf
  - /case-studies/ — `Download PDF →` → https://www.innovive.com/_files/ugd/ddd952_0d0885ed605244089ae8a39b5c46ee41.pdf
  - /case-studies/ — `Download PDF →` → https://www.innovive.com/_files/ugd/ddd952_15a2b3add264475e892427ebb167cd9d.pdf
  - /case-studies/ — `Download PDF →` → https://www.innovive.com/_files/ugd/ddd952_2c3dce671603444ca6857c54f4545c63.pdf
  - /case-studies/ — `Download PDF →` → https://www.innovive.com/_files/ugd/ddd952_311299efa6be49dc892262614b82033c.pdf
  - /case-studies/ — `Download PDF →` → https://www.innovive.com/_files/ugd/ddd952_35c2b0ec0fd64f7ca971ded830e257d9.pdf
  - /case-studies/ — `Download PDF →` → https://www.innovive.com/_files/ugd/ddd952_4153b926b5ad4b369deb6dd36bafc78a.pdf
  - /case-studies/ — `Download PDF →` → https://www.innovive.com/_files/ugd/ddd952_4d19e7d4e1444a4da777ec63ee7d08c8.pdf
  - /case-studies/ — `Download PDF →` → https://www.innovive.com/_files/ugd/ddd952_6bf53efc551746b1bcae2b86b535c215.pdf
  - /case-studies/ — `Download PDF →` → https://www.innovive.com/_files/ugd/ddd952_9222fa6714f9477cae1475480a9c1a9a.pdf
  - /case-studies/ — `Download PDF →` → https://www.innovive.com/_files/ugd/ddd952_cbfe66a33f8b42efa0d1e7033c6287c6.pdf
  - /case-studies/ — `Download PDF →` → https://www.innovive.com/_files/ugd/ddd952_ea7b9ec2d8ef498a8046fbdc659860f5.pdf

## 4. Cleanup items (broken/duplicate/junk pages)
- **/products-3/ → HTTP 500** (PHP fatal) and orphaned. The working Products page is **/products/** (nav points here, returns 200). Recommend deleting /products-3/ (likely the old broken duplicate noted in CLAUDE.md).
- **Duplicate "Innorack IVC Rat" pages:** /innorack-ivc-rat/ **and** /innorack-rat/ — same title, both published, both orphaned. Dedupe to one canonical slug before launch.
- **/hello-world/** — default WordPress sample post; trash it.
- **/elementor-10/** (title "Header") — Elementor template artifact exposed as a public page; should be a template part, not a page.

## 5. Orphaned pages (published, no inbound internal link)
*Note: /how-it-works/, /system-benefits/, /innovive-water-process/, /recycling-eu/ were orphans in this crawl but I wired them into The Innovive System nav on 6/12 — no longer orphaned. /faq/, /case-studies/, /events/, /patents/ become linked once the footer (§1) is wired.*

Remaining true orphans to address:
  - /case-studies/  ('Case Studies') — resolves when footer wired (§1)
  - /elementor-10/  ('Header') — junk/template (§4)
  - /events/  ('Events') — resolves when footer wired (§1)
  - /faq/  ('FAQ') — resolves when footer wired (§1)
  - /hello-world/  ('Hello world!') — junk/template (§4)
  - /innorack-ivc-rat/  ('Innorack IVC Rat') — duplicate (§4)
  - /innorack-rat/  ('Innorack IVC Rat') — duplicate (§4)
  - /job-application/  ('Job Application') — link from /career/
  - /metabolic-cage-kit/  ('Metabolic Cage Kit') — product/sub page: reach via Products menu, category page, or breadcrumbs (per sitemap)
  - /mouse-caging-m-btm-xl/  ('Mouse Caging Bottom XL') — product/sub page: reach via Products menu, category page, or breadcrumbs (per sitemap)
  - /mouse-rat-bedding/  ('Bedding') — product/sub page: reach via Products menu, category page, or breadcrumbs (per sitemap)
  - /mouse-transportation-cart/  ('Mouse Transportation Cart') — product/sub page: reach via Products menu, category page, or breadcrumbs (per sitemap)
  - /patents/  ('Patents') — resolves when footer wired (§1)
  - /products-3/  ('Products') — DELETE (500, §4)
  - /products/enrichment/crd-hld-h-3/  ('CRD-HLD-H') — product/sub page: reach via Products menu, category page, or breadcrumbs (per sitemap)
  - /profile-detail/  ('Profile &#8211; Detail') — junk/template (§4)
  - /rat-racks/  ('Rat Racks') — product/sub page: reach via Products menu, category page, or breadcrumbs (per sitemap)
  - /sustainability/  ('Sustainability') — product/sub page: reach via Products menu, category page, or breadcrumbs (per sitemap)

## Methodology
- Enumerated all pages/posts/teams/products via WP REST (all statuses, authenticated).
- BFS-crawled every published page's rendered HTML with `?nocache=` (bypasses SiteGround Dynamic Cache) and Basic Auth (so drafts render).
- Extracted every `<a href>`; resolved each unique internal target twice — authenticated (does it exist?) and anonymous (does the public see it?).
- Classified: broken, draft-only, redirect, placeholder `#`, external, orphan.
---

# FIXES APPLIED — 2026-06-12 (same day)

## ✅ Completed
1. **Footer "Resources" wired** — FAQ→/faq/, Case Studies→/case-studies/, Events→/events/, Patents→/patents/ (menu 33). Video Training left `#` (no page yet). De-orphans those 4 pages.
2. **"The Innovive System" nav** — added System Benefits, How It Works, Water Process, Closed Loop Recycling under it (was Research Ready only). [done earlier 6/12]
3. **42 dead CTA/cross-link buttons wired** across 24 pages (verified live). All contact/sales/demo CTAs → /contact/; product & section cross-links → their pages; "View Open Position" → /job-application/ (de-orphans it). Self-referential labels were intentionally skipped. Backup: content/backups/cta-fix-eldata-backup-20260612.json. Full change list in session log.
4. **Junk/broken pages set to draft** (reversible): /products-3/ (was 500, old broken Products dup — live one is /products/), /elementor-10/ ("Header" artifact), /hello-world/ (WP sample post).
5. **Duplicate Innorack page** — /innorack-ivc-rat/ drafted; kept /innorack-rat/ as canonical (mirrors /innorack-mouse/). FLAG: confirm slug preference.

**After-state crawl:** 0 broken internal links · 0 links to draft pages · 0 crawl failures (500 gone) · placeholder `#` instances 1,774 → 1,253.

## ⏳ Remaining `#` links — need content/design decisions (NOT auto-fixable)
*~109 instances (excluding legit sitewide nav toggles & footer). None are "links to the wrong page" — they are non-navigational labels or items blocked on content/assets/design:*

- **Self-referential section labels (~32)** — e.g. "Mouse Water" on /aquavive-mouse-water/, "Sustainability" on /sustainability/. These are hero/section badges naming their own page; likely should be plain text or in-page scroll anchors, not links. **Action: design decision** (make non-link, or add on-page anchor).
- **In-page section jumps (15)** — "Animal Welfare", "Three Pillars", "The Problem", "How EU Recycling Program Works", etc. Meant to scroll to a section on the same page. **Action: add anchor IDs to target sections + point these to #section-id.**
- **Vague CTAs (39)** — "Explore", "View Caging", "COMPATIBLE CAGING" (×6 product pages), "Visit Website" (×6 distributors), "Testimonials", "Partner", "Services", "View Logistics Network". **Action: confirm intended destination per button.**
- **Blog/News (21)** — "Read More" (×16) and "View All News"/"Latest News". Blog is hardcoded static widgets, not real WP posts (per CLAUDE.md). **Action: migrate /blog-news/ to real posts; until then "View All" can point to /blog-news/.**
- **Download assets (2)** — "Download data sheet" (/innorack-mouse/), "Download PDF for Info" (/metabolic-cage-kit/). **Action: upload the PDFs to the media library and link.**

## ⚠️ External links to review (unchanged)
- **17 "Download PDF →" links → old www.innovive.com.** After launch the new site *becomes* innovive.com; these PDF paths will 404 unless the assets are migrated to the new media library. **Action: migrate the datasheet PDFs (requires the files) or confirm they stay hosted.**

## ℹ️ Orphaned product sub-pages (by design)
Several product/sub pages (metabolic-cage-kit, mouse-caging-m-btm-xl, rat-racks, mouse-transportation-cart, products/enrichment/crd-hld-h-3, etc.) have no inbound links yet — per the sitemap they're reached via the Products menu, category pages, and breadcrumbs (breadcrumbs still in progress). Not broken; pending the category-page/breadcrumb build.
