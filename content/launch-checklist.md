# Innovive Launch Checklist — production cutover (Wix → WordPress)

Staging: inno.myvoladolabs.com (SiteGround). **Production host: TBD** — SiteGround is staging only. The site keeps the domain **innovive.com**; only the platform/host changes.

## Search-engine indexing ⚠️
- [ ] **NOW (staging):** WP Admin → Settings → Reading → enable **"Discourage search engines from indexing this site."** As of 2026-06-13 staging is **fully indexable** (robots.txt allows crawl, `sitemap_index.xml` is published, every page emits `<meta robots> index,follow`). Not yet indexed (`site:` returns 0), but unprotected. `blog_public` is not REST-controllable — must be set in the admin UI.
- [ ] **AT LAUNCH (production):** confirm indexing is turned back **ON** for innovive.com (uncheck "Discourage…") — a migrated DB carries the staging noindex over and will silently de-index the live site if not reverted.
- [ ] Submit the production sitemap to Google Search Console at cutover.

## Migration mechanics
- [ ] Choose production host; provision WordPress.
- [ ] Migrate DB + `wp-content` from staging to production.
- [ ] **Search-replace** `inno.myvoladolabs.com` → `innovive.com` across the DB (use a serialization-safe tool, e.g. WP-CLI `search-replace` or Better Search Replace) so no staging URLs remain hardcoded (incl. Elementor `_elementor_data`).
- [ ] Re-point DNS to the new host; provision SSL.
- [ ] Keep everything host-agnostic — no SiteGround-specific config baked into the build (caching, redirects, CDN). SiteGround Dynamic Cache behavior is a STAGING-only concern.

## 301 redirects (SEO preservation)
- [ ] Load the site-wide redirect map into a **WP redirect plugin** (DB-stored so it migrates) — see `301-redirect-map-sitewide-2026-06-13.md` (110 old Wix URLs mapped). **Google Sheet:** https://docs.google.com/spreadsheets/d/1cz6BCfF01x59BpZMyTzVoviFl-x1F-jzPUjAzv3ctpY/edit
- [ ] Confirm flagged targets: `/about-us` canonical (→ /about/ recommended), `video-training` destination, product-variant category landings.
- [ ] After the blog → WP-posts migration, remap the 18 `/news/` & `/post/` rows from `/blog-news/` to each specific post.
- [ ] Post-cutover: `curl -I` spot-check a sample for `301` → correct `Location`.

## PDFs / downloadable collateral
- [ ] Decide hosting approach (Download Monitor vs. Media Library + Redirection) — client-questions #4.
- [ ] Migrate the 17 legacy case-study PDFs off Wix into the new site; repoint the `/case-studies/` links — see `301-redirect-map-2026-06-13.md`.
- [ ] Wire the 2 "Download data sheet / PDF for Info" buttons (innorack-mouse, metabolic-cage-kit) once assets are hosted.

## Content / build dependencies (also tracked in client-questions.md)
- [ ] HubSpot tracking code / portal ID installed (forms + analytics).
- [ ] Blog migrated from static widgets to real WP posts (fixes "Read More" dead links + enables per-post redirects).
- [ ] Freeze slugs before launch (e.g. `/tall-rat-01/` was flagged for a cleaner slug — if changed, update the redirect map).
- [ ] Resolve remaining placeholder `#` links per `remaining-placeholder-links-2026-06-13.md` (in-page anchors, vague CTAs, distributor "Visit Website" URLs).
- [ ] Updated water-process content (Water Process page is live but content not final).

## Pre-launch QA
- [ ] Re-run the internal-link crawl on production (unique cache-bust token) — confirm 0 broken links.
- [ ] Verify forms submit and route to HubSpot.
- [ ] Confirm Customer Portal (NetSuite) + Document Lookup (certificates.innovive.com) links resolve.
