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
- Font: Manrope
- Page builder: Elementor Pro
- Host: SiteGround

## Outstanding Feedback — Must Fix Before Launch

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
