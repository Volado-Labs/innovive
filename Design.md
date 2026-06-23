# Innovive — Website Design Reference

**Project:** innovive.com rebuild ($24K, Volado Labs) · **Staging:** https://inno.myvoladolabs.com
**Builder:** Elementor Pro on WordPress (SiteGround) · **Launch:** week of June 15, 2026 (June 12 = internal page-complete deadline)
**Design source of truth:** Figma board (versions saved side-by-side, never overwritten) + Design Direction doc v1.2 (https://docs.google.com/document/d/1ZxmhQc7eSLZgFZ1C7xSz09q32Jr0iJvdfVbADrAMPoA/edit)

This document consolidates every approved design decision from the Apr–Jun 2026 client syncs (Robin Gaffney, Victoria Zimmerman, CEO Jamie) so any page built or revised on staging matches the approved direction.

---

## 1. Brand Foundation

- **Company:** Innovive — B2B life sciences, San Diego. Vivarium products (IVC racks, disposable recyclable caging) and services (Inno+ vivarium staffing/management), plus gnotobiotic solutions.
- **Tagline:** "Less Washing, More Science"
- **Core differentiator:** the cage-wash-free vivarium — disposable IVC caging arrives irradiated, pre-bedded, research-ready; recycled after use. Eliminates the cage wash room (CapEx, space, labor, ergonomic strain).
- **Positioning goal:** global leader in preclinical vivarium solutions — not just a manufacturer.
- **Audience:** vivarium directors, animal facility managers, institutional procurement at pharma, biotech, CROs, and academic institutions.
- **Aspirational layer (May 1 feedback):** the homepage must carry the "why" — enabling research that cures diseases — woven into copy and imagery, not just nuts-and-bolts product description.

### Sub-brands
| Brand | Role | Treatment |
|---|---|---|
| **Innovive** | Master brand | Wordmark in the global header on every page (media id 1716 on staging) |
| **Inno+** | Vivarium services line | Distinct sub-brand with its own logo/accent color — appears **only inside Inno+ pages**, never in the global header |
| **Innocycle** | Closed-loop recycling program | Logo lockup available; Closed Loop Recycling page links out to the Innocycle site |

Logo assets: `content/brand/` (Innovive RGB/CMYK/white + tagline variants, Inno+ full-color, Innocycle lockup). Full brand kit (brand guide, Pantone, photography): client Dropbox — https://www.dropbox.com/scl/fo/lqqwm8mndl4bktyzm7g4f/AJx5q_jyqdHQfBN2Pg4aakQ

---

## 2. Color System

### Staging palette (implemented)
| Token | Hex | Use |
|---|---|---|
| Navy | `#1b216b` | Primary anchor — heroes, dark sections, homepage pillar boxes. Always navy, **never black** |
| Blue | `#3765f8` | Primary action/brand blue |
| Light Blue | `#a8ceff` | Secondary accents elsewhere on the page |
| Orange | `#f47b2e` | Warm accent |
| Text | `#242d28` | Body copy |

### Usage rules (decided in client meetings — these override any older Figma versions)
- **Dark navy is the anchor tone**, not black. Hero image fades/gradients go to navy.
- **Homepage pillar boxes are uniform dark navy** (May 15 decision). The earlier per-pillar multi-color approach is dead.
- **Purple: removed entirely** (May 15).
- **Green: reserved exclusively for the Sustainability section** — nowhere else.
- **Inno+ accent (magenta in the brand kit):** small accent only — never as a background. Robin finds it "not as pleasing" than the rest of the palette, so usage trends down, not up. Hex still needs verification against the Figma/brand kit before using it in new builds.
- Photo overlays and gradients are used selectively for text readability.

---

## 3. Typography

- **Font:** Manrope, sitewide.
- **Line-height: minimum 1.5 on all body copy.** The original 14px/20px (1.43) was rejected by the client.
- Implemented sitewide via **Elementor kit #9 custom CSS** which sets text-editor body copy to **1.6**. ⚠️ This covers *text-editor widgets only* — headings, buttons, and any widget with a hard-coded line-height are NOT covered. Never hard-code tight values (the `line-height: 1px` and `20px` bugs on Home/Inno+ came from this).
- Blog/news card titles must not truncate mid-sentence without an ellipsis — set template character limits generously.

---

## 4. Layout & Shape Language

Approved direction (Apr 22/24): **modern, clean, bold.**

- **Geometric shapes** for visual interest; bold navy tones.
- **Rounded corners** — medium radius. Not square, not fully rounded (pill).
- **Heavy use of white space.**
- **Static heroes only — no sliders/carousels** (Robin's explicit call). Homepage hero is full-viewport.
- The three pillar sections must read as **one cohesive design language** — the original concepts felt like three different sites, which the client rejected.
- Interior/product page headers must be **visually distinct from the homepage hero** — identical headers across pages was a launch-blocking complaint.
- Site is fully responsive (single build — unlike the old Wix site's separate mobile/desktop). Watch line breaks on mobile during QA.

---

## 5. Homepage Structure (final, per May 15 + May 19 decisions)

1. **Hero** — full viewport, static image, fade to dark navy on the left. H1: "Research Ready from Day One." Aspirational "why" copy, not spec-sheet copy.
2. **Pillar block — asymmetric layout** (client-selected over three equal columns): one **large Products box** (racking & caging — the dominant visual), with **Inno+** and **Sustainability** as two smaller boxes beside/below. All boxes uniform dark navy. Copy: **one main point per box** — Victoria pared this down deliberately.
   - "Enrichment" does NOT appear on the homepage — it lives on the caging/product subpages.
3. **Global presence signal** — compact: small globe visual (or globe as background texture), 2–3 key stats, short text, plus a **"Find your local rep"** CTA linking to the global representation page. The big world map lives on the Global Presence page, never the homepage.
4. **News/events blocks** and **testimonials**.

**Testimonials:** short and bite-size (2–3 sentences). Client-logo scroll is a goal but **blocked on Robin confirming contract permissions** — don't add client logos until cleared. "Trusted by" testimonial blocks appear on Home + Inno+ only.

---

## 6. Product Detail Page Template

Required components of the template (May 15):
- **Comparison tables** — required components / compatible accessories (pattern: consolidated lids pages with tabbed selectors, e.g. /mouse-lids/ — 8 lids × 7 specs).
- **Required Cage Components block** — bottom + feeder + lid + water bottle, framed as a *hard system dependency*, not a soft cross-sell. Appears at the bottom of all four component page types. Section is titled "Required Cage Components" (not "More Components Like this"), ordered bottom → lid → feeder → water.
- **Multiple CTA buttons.** Sample-request CTA is worded **"Request more information"** and routes through sales for vetting — never a blanket free-sample offer.
- **Optional video popup** per product, only where a video exists. (No site video at launch — Innovive films after June 8; video sections ship post-launch. Never leave Elementor demo video URLs in place.)
- Cage-component sections link to product pages with **simple icons/shapes, not large product photos**.
- Each product gets its own photo — don't reuse one image across variants (MVX5/MVX12 bug).
- Section badges (e.g. "MOUSE ENRICHMENT") appear **once per page maximum** — headings carry the hierarchy. And the badge must match the species on the page.

---

## 7. Imagery Rules

- **Never stretch images.** Containers must preserve native aspect ratio (`object-fit: cover` on fixed-height widgets).
- Heroes: photography with selective navy-fade overlays for text legibility.
- Globe imagery: texture/background element only — never a dominant hero.
- Product photography: full uncut product/rack images on product pages (Tall Rat pattern: H1 product name + full rack image).
- Interior page heroes must differ from the homepage hero image (the /research-ready/ page reusing the homepage background was flagged).
- Image sources: Dropbox brand kit, Victoria's website-image Drive folder, and full-res Wix exports. Store image URLs as `https://`, not `http://`.

---

## 8. Voice & Tone (on-page copy)

- Experienced vivarium professional talking to a peer — accessible, practical, direct. Not white-paper dense.
- Lead with operational impact and outcomes, not specs. Simplify complexity.
- **Never link to competitors.** Source stats only from authoritative bodies (NIH, USDA, AAALAC, peer-reviewed journals), current within 1–2 years.
- Aspirational framing where it fits: products enable research that cures diseases.
- Footer: CEO (a lawyer) wants it minimal. Compromise in place — keep current footer links for launch, pare down if he pushes post-launch.

---

## 9. Navigation (June 10 meeting — final structure)

1. **Products** → products category page. Granular sub-nav (per Victoria): Mouse Rack, Mouse Caging, Lids, Water, Enrichment, **Gnotobiotics** (moved from services — "really a mouse application"). Label is "Enrichment", never "Innorichment" (that's a product name only).
2. **The Innovive System** (new top level): Research Ready, System Benefits, How It Works, Water Process, Closed Loop Recycling.
3. **Inno+ Vivarium Solutions** → /inno/ (single nav button; fallback label "Vivarium Solutions" if too long).
4. **Company**: About Us, Leadership/Team, Supply Chain & Logistics, etc.
5. **"Order Products"** NetSuite e-commerce link belongs in the global header (client request — still outstanding).

Accessory pages stay out of nav, reached via category pages + breadcrumbs (breadcrumbs in progress). Full detail: [sitemap-proposal-2026-06-11.md](content/sitemap-proposal-2026-06-11.md).

---

## 10. Implementation Notes (Elementor/staging)

- Page builder: **Elementor Pro**; global styles live in **kit #9** (custom CSS holds the sitewide line-height rule). Global header is **template 88**.
- Elementor data lives in `_elementor_data` post meta — back up before editing (backups in `content/backups/`), edit via REST with `--data @file.json`.
- **After every template/page edit, flush both caches**: Elementor CSS cache (`DELETE /wp-json/elementor/v1/cache`) and SiteGround Dynamic Cache — or the front end serves stale styles.
- Figma versioning: new versions go **beside** prior ones, never overwriting.
- Design freeze discipline: once content is migrated into WordPress, design changes slow dramatically — lock layout in Figma first.
- Known launch blockers tracked in [build-status-report-2026-06-10.md](content/build-status-report-2026-06-10.md) (site title "My WordPress", footer links all "#", /products/ HTTP 500, missing H1s, etc.).

---

## 11. Quick Do / Don't

**Do**
- Navy anchor, white space, geometric shapes, medium-rounded corners
- One badge per section; one main point per homepage box
- Comparison tables + "Required Cage Components" on product pages
- Static full-viewport heroes with navy fades
- Body line-height ≥ 1.5 (kit handles text-editor widgets at 1.6)
- Distinct hero per interior page

**Don't**
- Black backgrounds or black fades (always navy)
- Purple anywhere; green outside Sustainability; magenta/Inno+ accent as background
- Inno+ logo in the global header or on non-Inno+ pages
- Sliders/carousels in heroes
- Stretched images or fixed boxes that distort aspect ratio
- Hard-coded tight line-heights (1px/20px bugs)
- "Free sample" CTAs ("Request more information" instead)
- Competitor links; unverified or stale statistics
- Client logos in testimonials until Robin clears contract permissions
