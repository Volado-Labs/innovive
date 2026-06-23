# Innovive Build Status Report — June 10, 2026

Sources: client tracker (Tracker tab, 25 issue rows), internal tracker (All URLs / Pages / Blog Posts / Team / News tabs), live crawl of 44 staging URLs + WP REST inventory (51 pages, 12 Woo products, 8 team CPT entries, 4 menus).

**Note: the June 8 launch target has passed.**

## Scorecard

| Area | Status |
|---|---|
| Core pages (home, about, contact, team, career, legal) | Built, in client review |
| Service pages (Inno+, gnotobiotics, research-ready, supply-chain) | Built; Inno+ & regional-distributors have revisions requested |
| Product pages | ~28 built / consolidated; ~25 source URLs not yet covered |
| Blog & News migration | **Not started** — 0 of 13 posts + 6 news items in WP; /blog-news/ still hardcoded |
| WooCommerce / Order Products | 12 placeholder dummy products; "Order Products" NetSuite link not in header |
| Footer menus | Exist but **every link is "#"** |
| Site title | Still **"My WordPress"** in every browser tab / SERP |
| /products/ page | Still **HTTP 500** (known Elementor loop-grid fatal) |

## 1. Verified done (client tracker "Resolved" rows hold up on staging)

- Global: Innovive wordmark logo in header ✓; "Trusted by" testimonials only on Home + Inno+ ✓; "Talk to an Expert" removed from nav (still exists as body CTAs on home/inno/enrichment — assumed intentional)
- Homepage: hero "Research Ready from Day One" ✓ (BUT rendered H1 reads "Research Ready from **DayOne**" — missing space)
- /enrichment/ combined mouse+rat page live ✓ (old /mouse-enrichment/ now 404s — fine on staging, but make sure no internal links point there)
- /mouse-lid/ → /mouse-lids/ redirect ✓ (client-requested URL)
- /innorack-mouse/ exists at requested URL ✓ (H1 "Innorack IVC Mouse 3.5")
- /rat-feeders/ rebuilt with wirebar info, 541 words ✓
- /rat-lid/ rebuilt with comparison content, 734 words ✓ (no H1 though)
- /tall-rat-01/ "Innorack Tall IVC Rat" ✓; /tall-rat-xl/ built ✓
- Team: all 8 members now in teams CPT ✓ (sheet's earlier 1-of-3 render bug presumably fixed — verify visually)
- Legal: privacy-policy, terms-and-conditions, ca-supply-chain all published ✓

## 2. Open client feedback ("In review" on client tracker)

- **Gnotobiotics**: header updated ✓ but renders "Research- Ready" (bad hyphen/space). Client also wants MVX3 lid image in Key Benefits, distinct secondary-page hero, copy refresh (Victoria input). Video section was on default Elementor demo URLs as of round-2 audit.
- **Breadcrumb/navigation question** on 8 accessory pages (/m-climb/, /m-divider2/, /innodome-innowheel/, /innotube/, /m-innorichment/, /crd-hld-h/, /r-innorichment/, /r-loft-t/) — client asked how users navigate from these; suggested breadcrumbs. Not yet addressed; none have H1s either.
- **/aquavive-mouse-water/ & /aquavive-rat-water/**: header language still missing (both have NO H1 — confirms client's note); cage-component order fix (bottom→lid→feeder→water) and "More Components Like this"→"Required Cage Components" rename not verified.
- **/mouse-rack/ URL**: now redirects to **/product/mouse-racks/ which is a Woo placeholder** ("Great things are on the horizon") — worse than before; should point to /innorack-mouse/.

## 3. Revisions requested (internal sheet)

- **/inno/** — see client spreadsheet notes + email copy in Slack
- **/regional-distributors/** — screenshot feedback in sheet

## 4. In progress (internal sheet)

- /career/, /supply-chain-logistics/, /blog-news/

## 5. Not built yet (no staging URL in internal sheet, confirmed absent from WP)

Services: sustainability, water-processing, how-it-works*, system-benefits*, recycling-eu (*recommended merge — decision pending with Innovive)
Core: events, case-studies, FAQ, document-lookup, video-training, patents, job-application-form
Products: mouse-products & rat-products index pages*, mouse-caging (+ bottoms M-BTM / M-BTM-XL comparison), metabolic-cage-kit, mouse-transport-cart, mouse & rat bedding combined page (corn cob / alpha-dri / alpha-dri+ / biofresh), rat-racks, innorack-rat, rat-caging-btm, tall-rat-caging-btm, tall-xl-rat-caging-btm
(*may be superseded by /products-category-page/)
Content migration: 13 blog posts, 6 news items, with 301 redirects from Wix URLs

## 6. New sitewide issues found in this crawl

1. **Site title "My WordPress"** — every page title tag. Settings > General fix + consider SEO plugin for per-page titles.
2. **Footer menus all "#"** — Products/Services/Company footer links are placeholders.
3. **/products/ HTTP 500** — known loop-grid fatal, still live and linked nowhere in nav but crawlable.
4. **Missing H1s** on: about, aquavive ×2, blog-news, career, contact, team, rat-lid, regional-distributors, tall-rat (old), all 8 accessory pages.
5. **Homepage H1 typo** "DayOne".
6. **Research-ready H1 run-on** persists ("We've been Research Ready Since Day One What it means for your lab and…").
7. **Stale duplicates still published**: /tall-rat/ (old, superseded by /tall-rat-01/), /tall-rat-02/, /about-3/ (old stub), /services/ & /resources/ stubs (services is a nav parent — OK-ish), /sample-page/, Hello world! post. Need unpublish/redirect plan before launch.
8. **WooCommerce placeholders**: 12 dummy products live ("Mouse Product", "Rat Product", etc.), /shop/ shows "Great things are on the horizon". Decide: hide shop until NetSuite link strategy lands, or populate.
9. **"Order Products" NetSuite link** (client global request) not yet in header.

## 7. ADDENDUM — June 10 client meeting (Robin, Victoria, Collin) — supersedes items above

### Timeline (corrects report header)
- Real target was Friday June 12; **all agreed NOT to launch Friday** — go-live now "next week" (week of June 15). Jamie: "done well over done rushed."
- Dev commitment: **every page on the internal sheet complete by Friday June 12**; team works the weekend on client revisions.
- Robin & Victoria travel to North Sioux City Sunday but will review remotely; Robin must show major pages to the exec team pre-launch.
- Client gets staging edit access **after Friday** to tweak copy on Resolved pages only (no layout changes).

### NEW workstream: top-nav restructure (agreed in meeting)
Final structure dictated at 46:23–50:30:
- **Products** → products category page. Sub-nav: Mouse Rack, Mouse Caging, Lids, Water, Enrichment (combined mouse+rat), **+ Gnotobiotics moves here** (out of services — it's a mouse application). Label is "Enrichment" not "Innorichment" (Innorichment = product name only).
- **The Innovive System** (new top-level): System Benefits, How It Works, Water Process, Closed Loop Recycling — 4 pages.
- **Inno+ Vivarium Solutions** (or "Vivarium Solutions" if too long): single button → Inno+ page only. Research Ready's nav placement was NOT discussed — confirm.
- **Company**: About/Mission, Leadership/Team (Team leaves top level), Supply Chain, Global Representation, **Sustainability (moved here)**, News, Careers.
- **Customer Portal** (renamed from "Order") → NetSuite login link.
- **Contact Us** button CTA — consolidate "Contact" + "Get Started" (currently duplicate destinations).
- **Footer**: Events + Resources (blog, video training, document lookup) move to footer; document lookup gets its own footer slot. Jamie wants footer minimal — Robin re-confirming.

### Decisions that resolve report §5 open questions
- **How It Works & System Benefits**: keep as standalone pages (merge recommendation rejected); live under The Innovive System. How It Works belongs under Products… Robin later put it under Innovive System — final recap says Innovive System.
- **Sustainability**: content transfers AS-IS from current site (already vetted by Jeremy Jensen/Innocycle); new design, under Company. No rewrite needed.
- **Recycling**: becomes a brief **Closed Loop Recycling** page under The Innovive System linking out to the Innocycle site (competitive response to Tecniplast). OK to land post-launch.
- **Water Process**: page under The Innovive System; **content blocked on Innovive update** ("waiting on update pertaining to water").
- **Bedding**: confirmed ONE aggregate page with lids-style tab format + Victoria's bedding-to-configuration chart. The two missing Wix pages (pre-bedded corn cob rat / pre-bedded biofresh rat) are covered by it — no extra pages needed.
- **Enrichment accessory pages**: KEEP individual pages AND the aggregate page; breadcrumbs are the agreed navigation fix (Collin said in progress). Victoria also wants the aggregate enrichment page brought up to lids-page standard (tabs + at-a-glance grid).

### Inno+ scope expanded (was "revisions requested")
- Must feel like **its own business unit** — bigger, broader; hero image now OK (reverses small-thumbnail approach).
- Shrink "Trusted by" section (few Inno+ testimonials exist); expand the services section — services are what's being sold.
- "Partner with us" wide section should speak to Inno+ specifically.
- **Build a second Inno+ page with the contact form** (SEO + per original plan). Doesn't exist yet.
- "Explore Services" / "Request a Demo" buttons currently go nowhere — wire them up.
- Robin rewriting some copy; she flagged "customised"→"customized" earlier (verify fixed).

### Homepage / design feedback
- **New font approved — roll out sitewide** (currently homepage only).
- **Remove decorative section tags/badges on homepage** (e.g. "GLOBAL" above "Global Impact"). Keep functional product-page tags (BPA-free, 100% PET).
- Hero image: Robin wants a multi-rack vivarium image eventually — client to supply; shading/gradient OK. Verify gradient is a WP layer (Collin promised to confirm).
- Designer must not make unrequested changes — all changes flow through Collin's explicit instructions.
- Mobile parity is a CEO-level expectation — add a mobile QA pass before launch.

### Client to deliver
- Testimonials + approved customer logos (Robin auditing contracts)
- Supply chain page copy (Robin)
- Water process content update
- Continued product-page review (Victoria), major-page review (Robin)

### Workflow change
- The client spreadsheet is now the official go-between: Collin adds ready-for-review pages to the bottom with date-in; client flips Resolved→Open with notes when they find issues. (Dashboard formulas still broken.)

## 8. Tracker hygiene notes

- Client tracker Dashboard tab formulas are broken (ranges shifted; "Resolved" row counts "Open").
- Internal sheet "Pages" tab: /about/ maps to old stub in one row; /tall-rat-01/# vs /tall-rat-01/ duplicated rows; some "Combined with row 76" notes reference re-sorted rows.
