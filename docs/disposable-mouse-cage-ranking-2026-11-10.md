# Why Innovive ranks third for "disposable mouse cages" (2026-11-10)

Prompted by Robin's 11/10 email "Google ranking" (screenshot: Allentown EasyCage #1, Tecniplast E-Lite #2, Innovive /mouse-caging-btm/ #3).

## What the data says

- **The term is small.** About 20 U.S. searches a month (docs/search-demand-2026-10.md). Search Console, Aug 10 to Nov 8: Innovive pages got about 105 appearances and 7 clicks for "disposable mouse cages".
- **Third is one snapshot, not a fixed position.** A live U.S. check on 11/10 returned Tecniplast #1, Innovive /mouse-caging-btm/ #2, Allentown #3. Innovive held 3 of the top 10 results (#2, #5 /how-it-works/, #9 /mouse-caging-m-btm/), and two more (#4 Braintree, #6 NuAire) were partner pages selling Innovive cages. Rankings shift by user, location and day.

## Why we are not #1

1. **The page that ranks never says "disposable" in its visible text.** /mouse-caging-btm/ (page 3627) has "disposable" only in the title tag and meta description. The H1 is "M–BTM". The main content is about 240 words, almost all spec table. Image alt text is "Product Image".
2. **Our own pages compete with each other.** 12 Innovive URLs appeared for this query in 90 days. The two main ones split it: /how-it-works/ (avg position 6.9) and /mouse-caging-btm/ (9.0), plus /mouse-caging-m-btm/ and /mouse-caging-m-btm-xl/ with near-identical titles. Google has no single clear "disposable mouse cage" page from Innovive.
3. **Competitor pages answer buyer questions; ours does not.**
   - Tecniplast E-Lite: ~900 words, "disposable"/"single-use" throughout, 10-question FAQ (chew-outs, water, bedding, filters, recycling, delivery), parts table with part numbers, a $35 five-cage sample pack. That sample pack is where the price and "In stock" line in Google comes from.
   - Allentown EasyCage: feature sections, an ergonomics study stat (96% less force to undock), component dimensions, ~25 FAQs covering cages, racks, water and recycling.
   - Innovive: specs and four badges (BPA-free, Recyclable, Irradiated, 2x bagged). No FAQ, no explanation of why disposable, no product schema.
4. **No supporting content is live.** innovive.com has 11 blog posts in total; the newest is June 18, 2026. The 11 disposable IVC caging articles Volado wrote (Aug to Sep) are still in client review, so nothing on the site links to the cage page with "disposable mouse cage" wording.

## Content volume vs. the two competitors (sitemaps, 2026-11-10)

| | Innovive | Allentown | Tecniplast USA shop |
|---|---|---|---|
| Blog / articles | 11 posts, newest 2026-06-18 | 104 posts on blog.allentowninc.com, steadily since 2018 (13 to 19 a year 2018 to 2023) | 11 articles (plus tecniplast.com sites) |
| Posts on disposable vs. reusable | 0 that link to the cage page | 4 (reusable vs disposable, single-use waste management, single-use housing analysis, real-world challenges needing single-use) | 0 found |
| Site pages (English) | 112 | 132 on the main site | 167 product pages, 38 collections, 10 pages |
| Ranking page depth | ~240 words of main copy, no FAQ | Features, components, ~25 FAQs | ~900 words, 10 FAQs, parts table |

Takeaway: Allentown has roughly ten times Innovive's published articles, including four on exactly this decision. Tecniplast's edge is less about blog volume and more about page depth, a much larger product catalog, and a priced sample. Both beat Innovive on the ranking page itself.

## Fix plan

Mockup of the rebuilt page: content/drafts/ivc-hub/disposable-mouse-cages.html, noindex preview at reports.voladolabs.ai/innovive/disposable-mouse-cages/ (volado-reports 6d614c7).

**Page work (Volado can do this; needs a fact check, not writing, from Innovive):**
1. Make /mouse-caging-btm/ the one page for "disposable mouse cages": H1 like "Disposable Mouse Cages (M-BTM)", a 150 to 250 word intro (what it is, why disposable, research-ready, recycling), descriptive alt text.
2. Add an FAQ (8 to 10 questions) answered with Innovive facts: material (PET, BPA-free), chew resistance, pre-bedded options, irradiation and bagging, static time if unpowered, rack compatibility, recycling (InnoCycle), delivery cadence, samples.
3. Add Product and FAQ structured data.
4. Point the competing pages at it: /how-it-works/ links to it with the words "disposable mouse cages"; retitle /mouse-caging-m-btm/ and -xl so they target the specific model, not the generic term.

**Content (the bottleneck is approval, not writing):** approve and publish the 4 to 5 most-ready disposable IVC articles, each linking to the cage page.

**Optional, Innovive's call:** a sample-pack offer with a listed price would earn the same price/stock line Tecniplast shows.

**Expectation to set:** even at #1 this term brings a handful of clicks a month. The larger gaps are "rodent caging" (~390/mo), "rodent rack" (~170/mo) and "laboratory mouse cages" (~170/mo), where Innovive barely appears.
