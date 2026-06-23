# Innovive Website Build — Claude Code Context

## Staging Site
- URL: https://inno.myvoladolabs.com
- WP Admin: https://inno.myvoladolabs.com/wp-admin/
- Username: voladoadmin
- App Password: vJRp lt3o WzSZ hkX7 Eha2 5Bq9
- Admin Password: l0R#B!my0sHWo7pT

## REST API Auth
All WP edits go through the REST API using HTTP Basic Auth.
Username: voladoadmin
App password (spaces stripped): vJRplt3oWzSZhkX7Eha25Bq9
Base64 token: dm9sYWRvYWRtaW46dkpScGx0M29XelNaaGtYN0VoYTI1QnE5

Example curl:
```
curl -s -H "Authorization: Basic dm9sYWRvYWRtaW46dkpScGx0M29XelNaaGtYN0VoYTI1QnE5" \
  "https://inno.myvoladolabs.com/wp-json/wp/v2/pages?per_page=100&_fields=id,slug,title,status"
```

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
- Elementor data is stored in _elementor_data post meta — large JSON blobs, handle carefully
- When editing pages via REST API, always use --data @/tmp/file.json for payloads, never inline JSON
- SiteGround has two cache layers: Elementor CSS cache (flush in WP Admin > Elementor > Tools) and SiteGround Dynamic Cache (flush via Site Tools)
- Draft pages return 404 to unauthenticated visitors
- The /products/ page has a PHP fatal error — investigate before touching
