# Robin's Edits (6/12/26) — Actionable Task List

Source: `Robins_Edits_0001.pdf` (10 annotated screenshots + 2 reference slides). Tags:
**[BUILD]** = doable now via REST/Elementor · **[ASSET]** = needs an image/file · **[COPY]** = needs copy text · **[DECIDE]** = needs client/internal confirmation first.

Reference assets Robin provided in the PDF: **pg 3** = company timeline graphic · **pg 9** = distributor partner list.

---

## SITEWIDE

- [x] **[BUILD]** ✅ 6/13 — Top-nav reordered to Robin's order: **1. Company · 2. The Innovive System · 3. Products · 4. Inno+ Vivarium Solutions · 5. Customer Portal** (header menu id 5; all submenus intact). *(Supersedes the 6/11 Products-first sitemap.)*
- [x] **[BUILD]** ✅ 6/13 — Footer rebuilt to Robin's pg-10 structure: brand + **About Us** + **The Innovive System** + **Resources** columns (menus 30/29/33 reconfigured) + legal bar. ⏳ **Latest Blogs** column deferred — needs the blog→WP-posts migration to show real recent posts.

---

## ✅ EDITABILITY REBUILD (from Collin's 6/13 question — "can the client edit copy?")
Six pages were built as raw HTML blobs (not client-editable). Rebuilt all 6 with **native Elementor widgets** so Robin can edit copy in the visual editor. All verified 200 + 0 HTML widgets:
- [x] **FAQ** (3264) → gradient hero + 4 category headings + 23 Q&As as editable **accordion** items
- [x] **Patents** (3265) → hero + 5 regional headings + editable patent lists (US links to USPTO)
- [x] **Events** (3266) → hero + 2 group headings + editable event cards
- [x] **Case Studies** (3267) → hero + 17 editable cards (title/author/summary/source + Download PDF button; PDF links re-pointed by the migration map later)
- [x] **Job Application** (3268) → hero + real native **Elementor Form** (was a dead `onsubmit=return false` placeholder); submits via email, can add HubSpot action later
- [x] **Profile-Detail** (3269) → hero + native two-column profile (bio + photo)

Backups: `content/backups/page-<id>-htmlblob-20260613.json`. **Follow-ups:** ~~Job form submit button~~ ✅ brand-colored 6/13; Profile-Detail should become the **Teams CMS single template** (so every member gets a profile auto), not a one-off page.

## HOME PAGE — `/` (page 38)

- [x] **[BUILD]** ✅ 6/13 — Reordered to Robin's numbered order (Hero → One Partner → Global Impact → What's New → Testimonials → Video → Boxes); moved Testimonials below What's New.
- [x] **[BUILD]** ✅ 6/13 — Hero: flipped photo horizontally (racks now weight right, media 3423) + navy gradient overlay on the left under the header (headline readable).
- [x] **[BUILD]** ✅ 6/13 — Global Impact background replaced with the new photorealistic earth/network globe (Collin-provided, media 3449), full-width cover/center. Confirmed rendering in Collin's browser.
- [ ] **[COPY]** Pull testimonials from the **current Innovive home page** (⑤).
- [x] **[BUILD]** ✅ 6/13 — CTA headline set to *"Let us "Maximize your Science and Minimize your workload""* (was "Let's make your research easier").
- [x] **[BUILD]** ✅ 6/13 — Added the bottom-of-home video (matched by duration to Site Files "306 - Ambient Video V3_Sped up.mp4" → media 3442); placed as a section before the closing CTA band.
- [ ] **[BUILD]** ⑦ Add "the boxes" from the current home page.
- [ ] **[BUILD]** Footer resources list (Ⓓ): Document Lookup, Video Tutorials, Case Studies, … Blog.

## LEADERSHIP / TEAM — `/team/` (page 1405)

- [ ] **[COPY]** ① Add a statement above, from "Our Mission" on the current site — *"…with over 20 years…"*
- [ ] **[BUILD]** ② Link out the rest of the bios — match the current website (full bios linked).
- [ ] **[ASSET/BUILD]** ③ Add the **company timeline** at the bottom (use pg 3 graphic).

## GNOTOBIOTICS — `/gnotobiotics/` (page 130)

- [x] **[BUILD]** ✅ 6/13 — ① Removed eyebrow tags (gnotobiotics/IVC System/Benefits/THREE PILLARS/Testimonials/video).
- [x] **[BUILD]** ✅ 6/13 — ② Removed the "Explore" button.
- [x] **[BUILD]** ✅ 6/13 — Hero image → vivarium scene (Site Files: Vivarium Services.jpg → media 3446).
- [x] **[BUILD]** ✅ 6/13 — Why-Use image → technician holding mouse over open cage (Holding-mouse-over-cage-close.jpg → media 3447).
- [ ] **[BUILD]** Remove redundant section (Why Use… / Key Benefits marked "redundant").
- [x] **[BUILD]** ✅ 6/13 — Key Benefits (biosecurity) image → MVX3 lid top-down (MVX3 Lid_02_edited.jpg → media 3448).
- [ ] **[BUILD]** ⑥ Use "this background" for that section (the teal/gradient band).
- [x] **[BUILD]** ✅ 6/13 — ⑦ Deleted the unfinished "Unboxing… Coming May 2026" placeholder section.
- [ ] **[BUILD]** ⑧ Add a contact section below. *(Note: a "Get in Touch!" section already exists mid-page.)*
- [x] **[BUILD]** ✅ 6/13 — Removed leftover placeholder demo video section (was on Elementor's default YouTube demo URL).

## INNO+ VIVARIUM SOLUTIONS — `/inno/` (page 1364)

- [ ] **[BUILD]** Fix "inno+" text/color.
- [ ] **[ASSET/BUILD]** ① Make hero image like the homepage; **Ⓐ** make it **bigger — currently way too small**.
- [x] **[BUILD]** ✅ 6/13 — Hero button → "Talk to an Inno+ expert."
- [x] **[BUILD]** ✅ 6/13 — Reordered: "Why Partner with Us" now above the testimonial.
- [ ] **[COPY]** ③ Use testimonial from the current Inno+ page.
- [ ] **[BUILD]** Color the section backgrounds.
- [ ] **[DECIDE/BUILD]** Add a contact form (or put it on a second page).

## ABOUT US — `/about/` (page 1444)

- [x] **[BUILD]** ✅ 6/13 — Hero image swapped to the woman-pushing-cart-with-Innovive-box photo (Site Files: Juliana_Product Box.jpg → media 3441).
- [ ] **[COPY]** "Built on Purpose, Driven by Vision" is generic — change it.
- [ ] **[COPY]** ② Put **our values** here (see current site).
- [ ] **[BUILD]** ③ Move the "this goes on Career page" content to the Career page.
- [ ] **[BUILD]** ④ Remove the leadership-photos section / move up.
- [x] **[BUILD]** ✅ 6/13 — Relabeled "Four beliefs that shape every decision" → **"Our Core Values."**
- [ ] **[ASSET/BUILD]** ⑤ Add the **company timeline** (same as leadership page, pg 3).
- [ ] **[BUILD]** Remove the Sustainability section (crossed out).
- [ ] **[DECIDE]** Top-left note "NM — keep / spec copy on next page" — confirm intent with Robin.

## CONTACT — `/contact/` (page 1671)

- [x] **[BUILD]** ✅ 6/13 — Heading "Get In Touch" → **"Let's Connect."**
- [x] **[BUILD]** ✅ 6/13 — Form has the comprehensive field set (region, describe-you, first/last, email, phone, company, reason, message). *Note: Wix's conditional City/State (US-only) fields not added — flag if wanted.*
- [x] **[BUILD]** ✅ 6/13 — "What best describes you?" → Researcher / Faculty Manager / Distributor / Purchasing / Other.
- [x] **[BUILD]** ✅ 6/13 — "Reason for Inquiry" → open text field.
- [x] **[BUILD]** ✅ 6/13 — Form moved to lead; Office Locations moved below.
- [x] **[BUILD]** ✅ 6/13 — Form now leads (map no longer first). ⚠️ Google-map embed renders as a blank gap — review.
- [ ] **[DECIDE]** (Ties to open question #1 — which form platform / HubSpot.)

## REGIONAL DISTRIBUTORS — `/regional-distributors/` (page 1744)

- [x] **[BUILD]** ✅ 6/13 — Deleted the "PowerPoint" world-map section.
- [x] **[BUILD]** ✅ 6/13 — Deleted "Our Global Distribution Network" section.
- [x] **[BUILD]** ✅ 6/13 — Replaced placeholder distributor cards with the pg-9 list table (6 distributors + regions). Descriptions/links "copy to come" noted on page.

---

## Dependencies / blockers to chase
- **[ASSET]** From current site/Robin: home-page hero photo, home-page video, Global Impact bleed reference, gnotobiotics vivarium + mouse-in-cage + lid images, About "girl pushing cart" image.
- **[COPY]** Current-site testimonials (home + Inno+), "Our Mission"/20-years line, About values, "Our Core Values," distributor descriptions ("copy to come").
- **[DECIDE]** Top-nav order (conflicts with prior), footer scope (vs Jamie's minimal), Inno+ contact form vs 2nd page, form platform.
- **[ASSET — provided]** Company timeline (pg 3), distributor list (pg 9).
