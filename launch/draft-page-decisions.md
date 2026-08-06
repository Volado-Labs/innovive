# Draft Page Decisions — Innovive launch (2026-07-06)

14 pages are in **draft** and will be invisible/404 at launch. Below is each one, whether a published version already exists, the recommendation, and how to decide.

## A. Old duplicates of an already-published page → safe to TRASH (confirm first)
For each: open the **published** version in preview; if it's the finished one, trash the draft.

| Draft (id) | Published version (live) | Action |
|---|---|---|
| case-studies (3992) | case-studies-2-2 | **DECIDE — see B** (homepage "Read studies" points to the draft slug) |
| faq-2 (3782) | /faq/ | Trash draft |
| patents-2 (3742) | /patents-2-2/ | Trash draft (also: rename live slug patents-2-2 → patents) |
| regional-distributors-2-2 (1744) | /regional-distributors/ | Trash draft |
| ca-supply-chain (484) | /ca-supply-chain/ | Trash draft |
| tall-rat (786) + tall-rat-02 (2045) | /tall-rat-01/ | Trash both drafts |
| innorack-ivc-rat (3031) | /innorack-rat/ | Trash draft |

## B. "Which one is canonical?" — needs your eyes
- **case-studies (3992, draft) vs case-studies-2-2 (published):** The homepage "Read studies" button points to `/case-studies/` — which is the DRAFT. So right now that button 404s at launch. Decide which page has the real content:
  - If **3992** is the good one → publish it (it keeps the clean `/case-studies/` URL) and trash case-studies-2-2. Nothing else to change.
  - If **case-studies-2-2** is the good one → trash 3992 and tell me; I'll repoint the homepage button to `/case-studies-2-2/`.
  - *How to decide:* I can screenshot both — just ask.

## C. No published equivalent → PUBLISH or REDIRECT (your call)
| Draft (id) | What it is | How to decide |
|---|---|---|
| innovive-water-process (3196) | Water Processing page. Old Wix had `/innovive-water-process` (it's in the redirect map, currently pointing here → would 404 as a draft). | If water processing should be a live page → **publish it**. If not → tell me and I'll redirect the old URL to `/sustainability/` or `/recycling-eu/`. |
| products (2532) + products-3 (43) | Old "Products" landing pages. The old `/products` page had a PHP fatal; the new site navigates via the mega-menu with no products landing page. | Recommend **trash** both. Confirm nothing should live at `/products/`. |

## D. System / template — ignore
- profile-detail (3269), Elementor #3396, Header (10) — Elementor templates/system entries, not real pages. Leave as-is.

## General rule for deciding
1. Is the URL **linked** from the nav or a button? (If yes, it must resolve — publish it or repoint the link.)
2. Which version has the **finished content**? Keep that one, trash the other.
3. Prefer the **cleaner slug** (`/case-studies/` over `/case-studies-2-2/`).
