# Innovive Website Build — Claude Code Context

> **LIVE as of 2026-07-06:** production site is now **https://innovive.com** (migrated to new SiteGround hosting, IP 34.174.250.140, valid SSL). REST edits should target **innovive.com** (same voladoadmin app password works — same DB copy). `inno.myvoladolabs.com` is now a SEPARATE staging install; do NOT edit it for live changes. 301 redirects live via Code Snippets snippet #9. GA4: **G-V8ZJQ03BE3** firing sitewide (NEW Volado-owned property 544618753 / stream 15218892880, under voladolabs.ai GA account 355260418; created 2026-07-08 because client access to their property 534747623 stalled AND its tag G-97PG8MC1MH was broken — gtag.js 404). Tag lives in Code Snippets snippet #7; Realtime verified 2026-07-08; GA4 MCP can read the property directly. Cache tip: reactivating single-use snippet #10 flushes SiteGround dynamic cache over REST. Pending: GSC DNS TXT verify + sitemap.

## Staging Site
- URL: https://inno.myvoladolabs.com
- WP Admin: https://inno.myvoladolabs.com/wp-admin/
- Username: voladoadmin
- App Password: ‹REDACTED — see ~/workspace/credentials.md, WordPress / Innovive section› (issued 2026-07-06, post-incident rotation)
- Admin Password: STALE — rotated during June 2026 security incident; get current from Collin

## REST API Auth
All WP edits go through the REST API using HTTP Basic Auth. The same voladoadmin
app password works against both innovive.com (production) and the staging install.

Username: voladoadmin
App password: ‹REDACTED — see ~/workspace/credentials.md›

**This repo is on GitHub. Never commit the password or its base64 form here.**
Load it into the environment for the session instead:

```
export WP_BASIC="$(printf '%s' 'voladoadmin:<app-password-no-spaces>' | base64)"
```

Example curl (production; swap the host for staging):
```
curl -s -H "Authorization: Basic ${WP_BASIC}" \
  "https://innovive.com/wp-json/wp/v2/pages?per_page=100&_fields=id,slug,title,status"
```

Scripts in `content/backups/` follow the same convention and refuse to run
without `WP_BASIC` set.

## Client
- Company: Innovive — B2B life sciences, vivarium products and services
- Contact: Robin Gaffney (rgaffney@innovive.com) — Senior Director
- Internal: Victoria Zimmerman (vzimmerman@innovive.com) — Senior Marketing Manager
- Launch target: June 8, 2026 (non-negotiable)
- Managed by: Collin Wood, Volado Labs

## Site Structure — Current Page Inventory
| ID | Slug | Status |
|----|------|--------|
| 38 | home | publish |
| 41 | about | publish (empty) |
| 51 | blog-news | publish |
| 52 | contact | publish (empty) |
| 64 | career | publish (empty) |
| 130 | gnotobiotics | publish |
| 161 | shop | publish |
| 162 | cart | publish |
| 163 | checkout | publish |
| 164 | my-account | publish |
| 388 | compare | publish |
| 565 | mouse-enrichment | publish |
| 696 | rat-feeders | publish |
| 786 | tall-rat | publish |
| 1364 | inno+ | publish |
| 1405 | team (v2) | publish |
| 1444 | about-us | publish |
| 1493 | career (v3) | publish |
| 484 | ca-supply-chain-transparency | draft |
| 3 | privacy-policy | draft |
| 165 | refund-and-returns-policy | draft |

## Brand
- Colors: Navy #1b216b, Blue #3765f8, Light Blue #a8ceff, Orange #f47b2e, Text #242d28
- Font: Inter — the ONLY approved font, sitewide (client-approved 6/10; NOT Manrope, NOT Plus Jakarta Sans). All Elementor font_family settings swept to Inter on 6/11; audit via _elementor_data, not generated CSS files.
- Page builder: Elementor Pro
- Host: SiteGround

## Outstanding Feedback — Must Fix Before Launch

### ✅ PROGRESS LOG — 2026-06-02 (Collin/Claude session)
Shipped & verified live (REST edits, cache-flushed, backups in content/backups/):
- SITEWIDE #1 logo ✅ — Innovive wordmark (media id 1716) swapped into global header template 88
- SITEWIDE #3 line-height ✅ — kit #9 custom CSS raises text-editor body copy to 1.6 (verified 14px→22.4px)
- SITEWIDE #4 stretched images ✅ (partial) — object-fit:cover on the distorting fixed-height widgets (tall-rat 29f8d13/3c0db31/a2bbe54/d217dfd, rat-feeders 058b293/1c1cf6b/60d85d6/f9d3fda). "Broken images" were NOT reproduced — all return 200; blank boxes were the stretched containers.
- TALL RAT ✅ partial — removed MOUSE ENRICHMENT badge (7a87fcd), large bottom image (col d07b33a), stray "Features:" (icon-list 629473e), fixed "mouse cage"→"rat cage" (f1bead9). STILL TODO (needs assets): hero rack image + H1, rack spec table (Victoria's doc), cage-component icon links.
- RAT FEEDERS ✅ — removed MOUSE ENRICHMENT badge (b1ac918), removed duplicate R-WIRE-HB card (c61d0c2). Broken images not reproduced.
- MOUSE ENRICHMENT ✅ — badges 4→1 (removed e969163/d183456/c1a0e91), removed dup "Talk to an Expert" CTA (fafd967), fixed "Innovice"→"Innocage" typo (04dd9f7).
- BLOG & NEWS ✅ partial — image-first card order (8 cards), gap 272px→132px (f583c69 pad-bottom 100→20, 8f313d6 pad-top 100→40). STILL TODO: 2-3 reworded titles need authoritative copy; page is HARDCODED static widgets not real posts (dead Read More links, wrong dates, Figma blob in b092473) — real fix is migrating to WP posts.

Decisions made: ignore old empty stubs (about/41, contact/52, team/47, services/45, resources/49) — designer is building replacements under NEW slugs (about-us/1444, contact-us/1671, team-2/1405). Those are HERS, do not edit.
Flag to designer: /team-2/ (1405) renders only 1 of 3 published team members — loop-grid query is capped.
/products/ (43) fatal diagnosed: 3 loop-grid widgets set to "current_query" on a static page (Elementor Pro fatal). Not yet fixed; page is being rebuilt per migration plan anyway.

Round-2 audit (Home, Research Ready, Gnotobiotics, Inno+, About-us, Mouse-lid) + typo fixes shipped:
- Typos fixed ✅: Home "programh"→"program" (dcd4d3b); Research-Ready "ReadyTEAM"→"Ready TEAM" (496019b/2fb7f47) + stripped zero-width spaces (8470001/8390732); Gnotobiotics "Oregon Universit"→"University" (9cb4dd4 — VERIFY real institution name); Mouse-lid "Remay®"→"Reemay®" (8ddc829 ×5) + "lit"→"lid" (f8ea1ae).
- NOT fixed, needs owner/designer/content (round-2 findings):
  - Home (mine): empty heading 9a86385; line-height:1px bug on news-row date/button widgets (de4ca65/436c1d3/cd9f2a6/a2a7ccb/61ef991/1c2b88d); "InnoCycle" vs "closed-loop recycling program" naming (Victoria); Home testimonial 1c2b88d "PfizerTop US Biotech Company" run-together (confirm).
  - Research-Ready (mine): hero bg identical to homepage (b07590e = 7a2ec820…webp); 2 stretched images (c451f71 870x340, 7eb4104 340px); run-on H1 6faab6a; THIN page (~141 words) — Robin questioned if it should be standalone.
  - Gnotobiotics (mine): UNFINISHED video section — video widget 3a43f40 still on DEFAULT Elementor demo URLs + stale "Coming May 2026" copy (7d8036d1/25847bab) + placeholder "video" badge a7b789f; empty heading 2196cbb.
  - Inno+ (designer): empty heading bf26c35 (testimonial author); placeholder stat label "Washing or Setup Global Client" (c0095df, the 500+ stat); line-height:1px on c31915b; 20px line-heights on body widgets.
  - About-us (designer): DUPLICATE belief-card copy cards 3&4 (a732512==8fa2407); card copy doesn't match headings; two CTAs both "our mission and vision".
  - Mouse-lid (designer): placeholder heading "you need this to complete the system" (0eb54f6); MVX5 & MVX12 share same image.
- Line-height global fix caveat: kit #9 CSS covers text-editor BODY copy only; headings/buttons with hard-coded tight/1px line-heights are NOT covered (Home news row, Inno+).

### SITEWIDE (all pages)
1. Wrong logo in global header — Inno+ logo ("inno+") is showing on every page. Must be replaced with the Innovive wordmark. Inno+ should only appear on Inno+ service pages.
2. Product page headers are identical to the homepage — interior pages need a visually distinct header treatment.
3. Font line-height too tight — body text is 14px/20px (1.43 ratio). Increase to minimum 1.5 globally.
4. Product images stretched — image containers force all photos into fixed boxes regardless of native aspect ratio. Fix containers to preserve aspect ratios. Also multiple broken images (blank white boxes) on Tall Rat and Rat Feeders.

### TALL RAT (/tall-rat/)
- Remove hero image. Replace with product name as H1 + full uncut rack image (match current innovive.com layout)
- Add rack specification table — Victoria provided this in the Google Doc, it is missing entirely
- "Features" appears 3x on page — remove stray duplicate in the Innocage section
- "MOUSE ENRICHMENT" badge on a rat page — copy-paste error, remove it
- Remove large Innocage bottom image — page should focus on the rack
- Cage component section: replace large product images with simple icon/shape links to product pages (multiple lids exist for this product)
- Copy needs review for correct application attribution

### RAT FEEDERS (/rat-feeders/)
- Multiple broken images not loading
- R-WIRE-HB product card duplicated with identical content — remove one
- "MOUSE ENRICHMENT" badge on a rat page — remove it

### MOUSE ENRICHMENT (/mouse-enrichment/)
- "MOUSE ENRICHMENT" section badge repeating 4-5 times — reduce to once or remove, let headings carry the hierarchy
- Two identical "Talk to An Expert" CTA buttons side by side — remove duplicate

### BLOG & NEWS (/blog-news/)
- 4 of 8 blog titles are cut off mid-sentence with no ellipsis — increase template character/word limit
- 272px blank gap between Featured Articles and Latest News sections — CSS/empty element issue
- Blog card image is below title/excerpt — should be image first, then title, then excerpt
- One blog card has no image — confirm featured images uploaded for all 8 posts

## Pages Still Empty (need content built)
- /about/ (ID 41) — just a heading, no content
- /contact/ (ID 52) — just a heading, no content
- /resources/ (ID 49) — just a heading, no content
- /services/ (ID 45) — just a heading, no content
- /team/ (ID 47) — just a heading, no content

## Notes
- **CSS integrity guard (2026-07-10; v2 2026-07-28):** production runs Code Snippets **#22 "Elementor CSS integrity guard"** — fixes the recurring "containers collapse to display:inline / page renders flush-left" bug (blanket Elementor purges wiped all `_elementor_css` meta; occasional bad lazy regeneration persisted incomplete CSS that SG page cache then froze). The guard: (A) any Elementor cache purge → synchronous regen of ALL post CSS + SG flush (purge takes ~15s now, that's normal); (B) front-end self-heal of poisoned container CSS; (C) REST writes to `_elementor_data` → instant per-page CSS regen + targeted SG purge. **Never deactivate #22.** After REST page edits no manual purging is needed anymore. Diagnostic tell for the TOTAL-poisoning class: page HTML has `e-con` containers but no `elementor-element-XXXX{--display` rules.
  - **v2 (2026-07-28) — partial-incompleteness detection.** v1 only caught TOTAL poisoning (containers present but zero `--display` rules). On 2026-07-28 the home page (id 38) hero rendered blank: all `--display` rules were present but the hero band `elementor-element-fe996ad`'s `background-image`/`background-color` block was dropped during a regen (hero image 4141 had been media-edited to `...-e1782271851818.webp`), so the white hero heading rendered white-on-white and SG froze it. v1's self-heal saw `--display` and skipped it. v2 adds: (B) also parses `_elementor_data` for elements with a **classic background image** and verifies each has a `background-image` rule in the generated CSS (deep check cached per CSS build via `_volado_css_ok_sig` postmeta, so it runs at most once per generation, not per request); (A) and (C) now **regen-and-verify with one retry** and stamp the good signature. Diagnostic tell for the PARTIAL class: an element whose data has `background_background:classic` + `background_image.url` but whose served CSS has no `elementor-element-XXXX{...background-image:url}`. v1 backup: content/backups/snippet-22-2026-07-28-v1-pre-partialguard.json.
  - **v3 (2026-07-28) — hardened per Henry's review.** Three additions: (1) **rate-limit** the front-end self-heal (B) with a per-post cooldown transient `volado_css_heal_{id}` (10 min) so a genuinely un-healable page can NEVER spin into a regen loop on every request — this closes a real risk in v2 (v2 would re-attempt on every hit for a page that stays incomplete); (2) **value-specific `min_height` check** added to the required set (element with non-zero `min_height` in data must have `min-height:{size}{unit}` in its CSS block) — kept value-specific to dodge Elementor's `--min-height:0px` reset rule; (3) **specific logging** — `volado_css_selfheal_log` / `volado_css_regen_log` options now record the exact `element:declaration` that was missing (e.g. `38 healed; was missing [fe996ad:background-image]`). Checked set kept deliberately TIGHT (classic backgrounds + value-specific min-height only); widths/responsive are intentionally NOT asserted because Elementor legitimately omits defaulted/inherited values (asserting them would cause false-positive heal loops). Validated before deploy: on the healthy home page all 18 derived requirements resolve PRESENT (no false positive); a negative control that strips the hero background is correctly detected. PHP linted clean; verified all pages 200 post-deploy.
- **Elementor Element Caching DISABLED (2026-07-10):** `elementor_element_cache_ttl` set to `disable`. It was caching rendered widget HTML for 24h, so REST **content** edits (heading/title/link text) didn't appear on the front end until a full Elementor cache clear — a separate stale-content bug from the CSS one above. With it off + guard #22's per-edit SG purge, REST content edits now show **immediately** (proven with a live test). SG full-page cache is still the primary perf layer. To re-enable for performance, turn it back on in Elementor → Settings → Performance → Element Caching, but then add per-post element-cache invalidation to guard #22's `_elementor_data` hook or content edits will go stale again.
- Elementor data is stored in _elementor_data post meta — large JSON blobs, handle carefully
- When editing pages via REST API, always use --data @/tmp/file.json for payloads, never inline JSON
- SiteGround has two cache layers: Elementor CSS cache (flush in WP Admin > Elementor > Tools) and SiteGround Dynamic Cache (flush via Site Tools)
- Draft pages return 404 to unauthenticated visitors
- The /products/ page has a PHP fatal error — investigate before touching
