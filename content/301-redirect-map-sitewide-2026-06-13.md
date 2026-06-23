# Innovive — Site-wide 301 Redirect Map (Wix → WordPress)

**Prepared 2026-06-13 (DRAFT).** Source = current innovive.com (Wix) sitemap (110 URLs). Target = new staging slugs.

## Can we prepare this now? Yes — with two caveats
- **Old URLs:** final (pulled from the live Wix sitemap today).
- **New URLs:** the staging slugs, stable but not frozen — re-verify any slug that changes before launch (e.g. `/tall-rat-01/` was flagged for renaming).
- **Activation:** the redirects can only *take effect* once innovive.com cuts over to the new host. Author them in a **WP redirect plugin** (DB-stored) on staging now so they migrate with the site — do NOT put them in host config (won't survive the move).
- Domain is unchanged (innovive.com → innovive.com); only the path/platform changes, so these are path→path redirects.

## Coverage
- 110 old URLs mapped · 42 direct · 8 team members · 41 product variants → category · 18 blog & news articles · 1 needs a decision

## Direct (exact / rename)  (42)

| Old (Wix) | New | Flag | Note |
|---|---|---|---|
| `/about-us` | `/about/` | RENAME? | staging has BOTH /about/ (in nav) and /about-us/ — confirm which is canonical; recommend → /about/ |
| `/aquavive-mouse-water` | `/aquavive-mouse-water/` | EXACT |  |
| `/aquavive-rat-water` | `/aquavive-rat-water/` | EXACT |  |
| `/blog` | `/blog-news/` | RENAME |  |
| `/careers` | `/career/` | RENAME |  |
| `/case-studies` | `/case-studies/` | EXACT |  |
| `/casupplychaintransparancyact` | `/ca-supply-chain/` | RENAME |  |
| `/contact-us` | `/contact/` | RENAME |  |
| `/document-lookup` | `/document-lookup/` | EXACT |  |
| `/events` | `/events/` | EXACT |  |
| `/faq` | `/faq/` | EXACT |  |
| `/global-representation` | `/regional-distributors/` | RENAME |  |
| `/gnotobiotics` | `/gnotobiotics/` | EXACT |  |
| `/how-it-works` | `/how-it-works/` | EXACT |  |
| `/inno-plus` | `/inno/` | RENAME |  |
| `/innorack-mouse` | `/innorack-mouse/` | EXACT |  |
| `/innorack-rat` | `/innorack-rat/` | EXACT |  |
| `/innovive-water-process` | `/innovive-water-process/` | EXACT |  |
| `/job-application-form` | `/job-application/` | RENAME |  |
| `/metabolic-cage-kit` | `/metabolic-cage-kit/` | EXACT |  |
| `/mouse-caging` | `/products/` | RENAME |  |
| `/mouse-caging-m-btm-xl` | `/mouse-caging-m-btm-xl/` | EXACT |  |
| `/mouse-caging-products` | `/products/` | RENAME |  |
| `/mouse-lids` | `/mouse-lids/` | EXACT |  |
| `/mouse-products` | `/products/` | RENAME |  |
| `/mouse-racks` | `/innorack-mouse/` | RENAME |  |
| `/mouse-transport-cart` | `/mouse-transportation-cart/` | RENAME |  |
| `/news` | `/blog-news/` | RENAME |  |
| `/patents` | `/patents/` | EXACT |  |
| `/privacy-policy` | `/privacy-policy/` | EXACT |  |
| `/rat-caging` | `/rat-caging/` | EXACT |  |
| `/rat-caging-btm` | `/rat-caging/` | RENAME |  |
| `/rat-lids` | `/rat-lid/` | RENAME |  |
| `/rat-products` | `/products/` | RENAME |  |
| `/rat-racks` | `/rat-racks/` | EXACT |  |
| `/recycling-eu` | `/recycling-eu/` | EXACT |  |
| `/sustainability` | `/sustainability/` | EXACT |  |
| `/system-benefits` | `/system-benefits/` | EXACT |  |
| `/tall-rat-loft` | `/tall-rat-01/` | RENAME |  |
| `/tall-rat-rack` | `/tall-rat-01/` | RENAME |  |
| `/tall-xl-rat-rack` | `/tall-rat-xl/` | RENAME |  |
| `/terms-conditions` | `/terms-and-conditions/` | RENAME |  |

## Team members  (8)

| Old (Wix) | New | Flag | Note |
|---|---|---|---|
| `/team/ann-mason%2C-rlatg` | `/teams/ann-mason/` | FUZZY 0.74 | team member — URL prefix changed /team/ → /teams/ |
| `/team/dee-conger` | `/teams/dee-conger/` | FUZZY 0.97 | team member — URL prefix changed /team/ → /teams/ |
| `/team/emmanuel-ferton` | `/teams/emmanuel-ferton/` | FUZZY 0.98 | team member — URL prefix changed /team/ → /teams/ |
| `/team/francesca-mcguffie` | `/teams/francesca-mcguffie/` | FUZZY 0.98 | team member — URL prefix changed /team/ → /teams/ |
| `/team/jamie-s-blose` | `/teams/jamie-s-blose/` | FUZZY 0.97 | team member — URL prefix changed /team/ → /teams/ |
| `/team/robin-gaffney` | `/teams/robin-gaffney/` | FUZZY 0.97 | team member — URL prefix changed /team/ → /teams/ |
| `/team/sarah-anderson-jenkins` | `/teams/sarah-anderson-jenkins/` | FUZZY 0.98 | team member — URL prefix changed /team/ → /teams/ |
| `/team/todd-knapp` | `/teams/todd-knapp/` | FUZZY 0.97 | team member — URL prefix changed /team/ → /teams/ |

## Product variants → category (consolidated)  (41)

| Old (Wix) | New | Flag | Note |
|---|---|---|---|
| `/alpha-dri-rat` | `/mouse-rat-bedding/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/biofresh-rat` | `/mouse-rat-bedding/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/corn-cob-rat` | `/mouse-rat-bedding/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/mouse-alpha-dri` | `/mouse-rat-bedding/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/mouse-alpha-dri-plus` | `/mouse-rat-bedding/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/mouse-biofresh` | `/mouse-rat-bedding/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/mouse-caging-card-holder` | `/products/enrichment/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/mouse-caging-innotube` | `/products/enrichment/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/mouse-caging-innowheel` | `/products/enrichment/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/mouse-caging-m-btm` | `/products/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/mouse-caging-m-climb` | `/products/enrichment/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/mouse-caging-m-divider2` | `/products/enrichment/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/mouse-caging-m-feed` | `/mouse-feeders/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/mouse-caging-m-feed-p` | `/mouse-feeders/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/mouse-caging-m-feed-ss` | `/mouse-feeders/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/mouse-caging-msx2` | `/mouse-lids/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/mouse-caging-msx4` | `/mouse-lids/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/mouse-caging-mvx1` | `/mouse-lids/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/mouse-caging-mvx2` | `/mouse-lids/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/mouse-caging-mvx3` | `/mouse-lids/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/mouse-caging-mvx5` | `/mouse-lids/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/mouse-caging-mvx6` | `/mouse-lids/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/mouse-caging-nesting-sheets` | `/mouse-rat-bedding/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/mouse-corn-cob` | `/mouse-rat-bedding/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/r-feed-u` | `/rat-feeders/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/r-wbp` | `/rat-feeders/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/r-wire-hb` | `/rat-feeders/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/r-wire-td` | `/rat-feeders/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/rat-caging-lid-rvx6` | `/rat-lid/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/rat-card-holder` | `/products/enrichment/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/rat-lids-rsx1` | `/rat-lid/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/rat-lids-rvx5` | `/rat-lid/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/rat-lids-rvx62` | `/rat-lid/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/rat-nesting-sheets` | `/mouse-rat-bedding/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/tall-rat-caging-btm` | `/rat-caging/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/tall-rat-caging-lid-rvx7` | `/rat-lid/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/tall-rat-caging-lid-rvx8` | `/rat-lid/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/tall-xl-rat-caging-btm` | `/rat-caging/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/tall-xl-rat-caging-lid-rvx7-xl` | `/rat-lid/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/tall-xl-rat-caging-r-wire-td` | `/rat-lid/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |
| `/tall-xl-rat-caging-r-wire-xl` | `/rat-lid/` | CONSOLIDATE | product variant consolidated into category page — verify target is the best landing page |

## Blog & News articles  (18)

| Old (Wix) | New | Flag | Note |
|---|---|---|---|
| `/news/innovive-expands-global-reach-through-strategic-partnership-with-attentive-science-to-accelerate-scientific-research-across-gcc-and-mena-regions` | `/blog-news/` | BLOG→listing | point to /blog-news/ now; remap to the specific post once blog is migrated to WP posts |
| `/news/innovive-expands-into-latin-america-and-caribbean` | `/blog-news/` | BLOG→listing | point to /blog-news/ now; remap to the specific post once blog is migrated to WP posts |
| `/news/major-environmental-milestones` | `/blog-news/` | BLOG→listing | point to /blog-news/ now; remap to the specific post once blog is migrated to WP posts |
| `/news/new-chief-executive-officer` | `/blog-news/` | BLOG→listing | point to /blog-news/ now; remap to the specific post once blog is migrated to WP posts |
| `/news/pet-rodent-cage-processor-recycled` | `/blog-news/` | BLOG→listing | point to /blog-news/ now; remap to the specific post once blog is migrated to WP posts |
| `/news/product-support-services-and-vivarium-management-solutions` | `/blog-news/` | BLOG→listing | point to /blog-news/ now; remap to the specific post once blog is migrated to WP posts |
| `/news/strategic-partnership-with-dr-marcel-perret-gentil` | `/blog-news/` | BLOG→listing | point to /blog-news/ now; remap to the specific post once blog is migrated to WP posts |
| `/post/building-a-career-in-life-sciences-celebrating-women-and-girls-in-science` | `/blog-news/` | BLOG→listing | point to /blog-news/ now; remap to the specific post once blog is migrated to WP posts |
| `/post/contamination-control-and-its-impact-on-data-integrity-protecting-your-research-investment` | `/blog-news/` | BLOG→listing | point to /blog-news/ now; remap to the specific post once blog is migrated to WP posts |
| `/post/contingency-planning-in-animal-care-facilities-building-resilience-beyond-compliance` | `/blog-news/` | BLOG→listing | point to /blog-news/ now; remap to the specific post once blog is migrated to WP posts |
| `/post/evaluating-vivarium-staffing-models-a-decision-framework-for-research-facilities` | `/blog-news/` | BLOG→listing | point to /blog-news/ now; remap to the specific post once blog is migrated to WP posts |
| `/post/holiday-and-leave-coverage-maintaining-vivarium-care-without-burning-out-your-team` | `/blog-news/` | BLOG→listing | point to /blog-news/ now; remap to the specific post once blog is migrated to WP posts |
| `/post/meeting-facility-esg-goals-with-a-more-sustainable-vivarium-solution` | `/blog-news/` | BLOG→listing | point to /blog-news/ now; remap to the specific post once blog is migrated to WP posts |
| `/post/rethinking-vivarium-water-why-eliminating-on-site-processing-is-your-next-strategic-move` | `/blog-news/` | BLOG→listing | point to /blog-news/ now; remap to the specific post once blog is migrated to WP posts |
| `/post/the-cage-wash-free-vivarium-a-facility-planning-checklist-to-reduce-cage-wash-infrastructure-and-ca` | `/blog-news/` | BLOG→listing | point to /blog-news/ now; remap to the specific post once blog is migrated to WP posts |
| `/post/the-optimized-vivarium-achieving-sustainability-and-strengthened-biosecurity` | `/blog-news/` | BLOG→listing | point to /blog-news/ now; remap to the specific post once blog is migrated to WP posts |
| `/post/the-unseen-weight-a-leader-s-guide-to-compassion-fatigue-in-the-vivarium` | `/blog-news/` | BLOG→listing | point to /blog-news/ now; remap to the specific post once blog is migrated to WP posts |
| `/post/wash-driven-to-research-driven-the-evolution-of-vivarium-infrastructure-and-invention-of-single-use` | `/blog-news/` | BLOG→listing | point to /blog-news/ now; remap to the specific post once blog is migrated to WP posts |

## Needs a decision  (1)

| Old (Wix) | New | Flag | Note |
|---|---|---|---|
| `/video-training` | **? decide** | DECIDE | no Video Training page built yet — redirect to /blog-news/ or homepage, or hold until built |

## To finalize before launch
1. Confirm the handful of flagged targets (about-us canonical, video-training, product-variant category landings).
2. Once the blog is migrated to real WP posts, remap the 18 `/news/` & `/post/` rows from `/blog-news/` to each specific post URL.
3. Re-verify any new slug that changes between now and launch.
4. Load all rows into a WP redirect plugin (e.g. Redirection) on staging; export/confirm they travel with the migration.
5. After production cutover: spot-check a sample with `curl -I` for `301` → correct `Location`.

_Also see: `301-redirect-map-2026-06-13.md` (the 17 legacy case-study PDFs, a subset of this migration)._
## Added 2026-06-18 — bottom-page split
| OLD (staging, internal-only) | NEW | Note |
|---|---|---|
| /mouse-rat-btm/ | /mouse-caging-btm/ | Combined bottom page split into mouse + rat (Victoria 6/16). mouse-rat-btm now 404s. **Add this 301 in Rank Math > Redirections** — could not be created via REST (app-password 403, needs admin nonce). Staging-only slug, no external links, so low-priority but should exist before launch. |

## Added 2026-06-18 — blog migration (Wix /post/<slug> -> WP /<slug>)
| OLD (Wix) | NEW (WP) |
|---|---|
| https://www.innovive.com/post/contingency-planning-in-animal-care-facilities-building-resilience-beyond-compliance | /contingency-planning-in-animal-care-facilities-a-guide-to-resilience/ |
| https://www.innovive.com/post/building-a-career-in-life-sciences-celebrating-women-and-girls-in-science | /building-a-career-in-life-sciences-celebrating-women-and-girls-in-science-with-innovives-ceo-jamie-blose-pharmd-mba-jd/ |
| https://www.innovive.com/post/meeting-facility-esg-goals-with-a-more-sustainable-vivarium-solution | /how-can-a-disposable-ivc-solution-make-your-acfs-operations-more-sustainable/ |
| https://www.innovive.com/post/holiday-and-leave-coverage-maintaining-vivarium-care-without-burning-out-your-team | /strategic-leave-coverage-in-vivarium-management/ |
| https://www.innovive.com/post/the-unseen-weight-a-leader-s-guide-to-compassion-fatigue-in-the-vivarium | /the-unseen-weight-a-leaders-guide-to-compassion-fatigue-in-the-vivarium/ |
| https://www.innovive.com/post/the-cage-wash-free-vivarium-a-facility-planning-checklist-to-reduce-cage-wash-infrastructure-and-ca | /the-cage-wash-free-vivarium-a-facility-planning-checklist-to-reduce-cage-wash-infrastructure-and-capex/ |
| https://www.innovive.com/post/wash-driven-to-research-driven-the-evolution-of-vivarium-infrastructure-and-invention-of-single-use | /wash-driven-to-research-driven-the-evolution-of-vivarium-infrastructure-and-invention-of-single-use-disposable-ivc-system/ |
