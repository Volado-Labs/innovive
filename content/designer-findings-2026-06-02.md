# Innovive Site — Findings for Designer (2026-06-02)

These are issues found on **your recently-built pages** during a QA audit against Robin/Victoria's feedback. Volado (Collin/Claude) did **not** edit these pages — they're yours. Element IDs are the Elementor widget IDs (visible in the editor's Navigator).

Context: Volado has been fixing the older product/utility pages (tall-rat, rat-feeders, mouse-enrichment, blog-news) + sitewide items (logo, line-height, image object-fit) and a round of typos. We're staying off your new-slug builds (about-us, contact-us, team-2, inno, mouse-lid) to avoid collisions.

---

## About Us (/about-us/, page 1444)
1. **Duplicate belief-card copy (P1).** In the "Four beliefs…" section (container `eca2177`), cards 3 & 4 share the identical sentence: widgets `a732512` ("Aseptic Setup") and `8fa2407` ("Efficiency & Scalability") both read *"Two decades of refinement, iterated alongside the world's leading research institutions."* Looks like placeholder leftover. Also the 4 card descriptions don't clearly match their headings — recommend a full copy pass on that section.
2. **Two CTAs both labeled "our mission and vision"** — buttons `94ce316` (Our Mission section) and `48869f0` (Four beliefs section). Confirm if intended or differentiate.
3. Minor: comma splice in careers copy (`9538348`); two images stored as `http://` URLs that 301-redirect (`83fc5d7`, bg `0e84275`) — normalize to https.
- ✅ Hero distinct from homepage, header logo correct, line-heights fine, no broken/stretched images.

## Inno+ (/inno/, page 1364)
1. **Empty heading `bf26c35`** in the testimonial attribution block — should hold the testimonial author's name (currently blank, renders an empty heading above "Pfizer / Top US Biotech Company").
2. **Placeholder stat label** — the `500+` proof-point (`c0095df`) is labeled *"Washing or Setup Global Client"*, which reads like an unfinished fragment vs. its clean siblings ("HVAC Reduction", "Lower Carbon Footprint", "Years of Experience").
3. **`line-height: 1px` bug** on text-editor `c31915b` (the testimonial company line) — collapses the line; set to a normal value.
4. Body text/buttons hard-code `line-height: 20px` (1.43 ratio, below the 1.5 sitewide minimum) on `1139942`, `141b19c`, `13e74b7`, `c0095df`, `58ee284`, buttons `bd0f5da`/`cbf8732`/`20ebb49`. The sitewide kit line-height fix (1.6) only covers body text-editor copy, not these per-widget overrides.
- ✅ Header logo correct (in-body Inno+ logo is fine), hero distinct & on-brief, no broken images.

## Mouse Lid (/mouse-lid/, page 1501) — strongest page
1. **Placeholder/draft heading** `0eb54f6`: *"you need this to complete the system"* — lowercase, unstyled, in the cage-components section. Needs real, styled heading copy.
2. MVX5 and MVX12 use the **same product image** (`ec8d2679…`) in the tab selector — consider a distinct photo for MVX12.
- (Volado already fixed the "Remay®"→"Reemay®" spec-table typo and "lit"→"lid" here, per Collin's go-ahead on typos.)
- ✅ Comparison table fully delivered (8 lids × 7 specs + tab selector), logo, line-height, hero distinct, no broken images.

## Team (/team-2/, page 1405)
1. **Loop-grid renders only 1 of 3 published team members** — only Dee Conger shows; Todd Knapp and Jamie S. Blose are missing from the page. The loop-grid query is likely capped (posts-per-page) or filtered. Highest priority on this page.
2. Page heading "Trusted By Leading Research Companies" reads more like a testimonials/logos header than a Team header — confirm intent.

## Contact Us (/contact-us/, page 1671)
- Functional (form present) but **thin** (single section, ~164 chars). Confirm whether address/phone/map/hours are expected before launch.

---

## Sitewide notes (Volado-owned, FYI)
- Global header logo swapped to the Innovive wordmark (media id 1716). Inno+ logo only belongs inside Inno+ pages.
- Kit (#9) custom CSS raises body **text-editor** line-height to 1.6. Headings/buttons with hard-coded tight values are NOT covered — if you hard-code line-heights, keep body copy ≥1.5.
- After any Elementor edit, the site needs an Elementor CSS cache flush or the front-end serves stale styles.
