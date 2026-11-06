# Auto-watering page: draft, ask list and research

Draft built 2026-11-06 after the 11/6 weekly sync. **Draft only, nothing published.**

- Mockup: `auto-watering.html` (open in a browser; the button at bottom right hides the review notes)
- Proposed URL: `/auto-watering/`
- Style matches `content/drafts/ivc-hub/` (live kit palette, Inter, no orange)
- Images: only existing Innovive media (MVX5 lid photo, grommet video thumbnail, media 3467). Everything else is a labelled placeholder box.

## What we found (it is not a blank slate)

The 11/6 call said "nothing on the site mentions auto watering except the MVX 5 page". The live site actually has scattered references:

| Where | What it says |
|---|---|
| /mouse-lids/ comparison table | MVX5 = "Autowatering", 2 Reemay filters, no water bottle cavity, **bottom required: M-BTM-A**, rack: Innorack IVC Mouse, best for "Autowatering Set-Up" |
| /mouse-lids/ MVX5 tab | "IVC mouse lid for use in Innorack. It uses two Reemay® filters covering exhaust and supply ports. The MVX5 lid is used with autowatering systems only." |
| /video-training/ | "Innocage® Autowatering: Grommet Insertion" video, YouTube `K_Q9iXQwlPw`, thumbnail media 3467 |
| /rat-caging/ | "The autowatering option comes in a standard rat configuration and requires an Innorack IVC Rat, R-BTM-H-A bottom, RVX5 lid, R-FEED-U feeder." |
| /rat-lid/ | RVX5 = "Dual filter IVC. Autowatering." Two Reemay filters, two ventilation grates, best for "Autowatering Set-Up" |
| /rat-racks/ | "*Autowatering option is available" |

So the page covers mouse (from the call) and rat (from the site), with rat marked CONFIRM.

### Inconsistencies on the live site to fix when the page goes up
1. **Mouse bottom pages list MVX5 as a compatible lid for M-BTM** (/mouse-caging-btm/, /mouse-caging-m-btm/). The lid table says MVX5 needs **M-BTM-A**. One of them is wrong.
2. **Rat bottom SKU is written two ways:** `R-BTM-H-A` on /rat-caging/, `R-BTM-A-H` in our IVC rack guide draft.
3. **MVX5 advantage bullet** reads "Accommodates research that requires rodent housing with dual filtration", which looks copied from the MVX2 tab.
4. Neither M-BTM-A nor R-BTM-H-A has its own product page or a WooCommerce product (store search returns nothing).

## Ask list for Robin and Victoria

**The system**
1. Is the rat version (Innorack IVC Rat + R-BTM-H-A + RVX5 + R-FEED-U) still offered? Should it be on this page?
2. Correct rat bottom SKU: R-BTM-H-A or R-BTM-A-H?
3. Does MVX5 work only with M-BTM-A, or also with the standard M-BTM? (Bottom pages and lid page disagree.)
4. Is M-BTM-A the same size as M-BTM (81 in² floor, 5" headroom, 14.7 x 9.2 x 5.5 in, up to 5 mice)? Sold empty, pre-bedded, or both?
5. Do all three feeders (M-FEED, M-FEED-P, M-FEED-SS) fit with MVX5?
6. Any autowatering option for Mouse XL, Tall Rat or Tall Rat XL? (Page currently says no.)

**The rack**
7. Rack name and part number for the autowatering Innorack IVC Mouse. Factory build, retrofit kit for existing racks, or both?
8. How many cage positions on the autowatering rack (standard holds up to 192)? Single- and double-sided?
9. Drinking valve: type, supplier, and where it sits (through the grommet into the cage?).
10. How the rack connects to the facility supply: fitting type and size.
11. Operating water pressure range. Is a pressure regulator or flushing station needed, and who supplies it?
12. Can bottle cages and autowatering cages share one rack?

**Water, safety, cleaning**
13. Water types supported: acidified, chlorinated, RO/ultrapure?
14. How leaks or a flooded cage are prevented (valve design, grommet seal, any leak detection)?
15. Flushing and sanitation of the water lines: how often, and can lines be autoclaved, VHP-treated or chemically sanitized?
16. Grommet: material, and is it reused across cages or thrown away at cage change? How is it cleaned?
17. Are M-BTM-A and MVX5 delivered irradiated and double-bagged like the rest of the line?

**Fit with other systems**
18. Do Innocage A-bottoms work on any third-party autowatering racks (Allentown, Tecniplast, Avidity)? Fine to say "Innorack only".

**Positioning**
19. Who is this for? Draft says: facilities already plumbed for autowatering, studies where a bottle change is a disturbance, teams cutting bottle handling. Anything to add from the UCSF conversation?
20. OK to use the URL `/auto-watering/`, and to link it from the MVX5, RVX5, rat-caging and Innorack pages?

**Photos needed** (page can launch without them; placeholders are labelled)
- Hero: Innorack IVC Mouse fitted for autowatering, cages docked
- M-BTM-A bottom showing the grommet hole (and grommet fitted)
- Close-up of the rack water line and drinking valve at one cage position
- Optional: rat autowatering setup (R-BTM-H-A + RVX5 on an Innorack IVC Rat)
- Existing and reused: MVX5 lid photo, grommet video thumbnail

## Research sources

**Live innovive.com (read-only, fetched 2026-11-06):** /mouse-lids/, /video-training/, /rat-caging/, /rat-lid/, /rat-racks/, /mouse-caging-btm/, /mouse-caging-m-btm/, /innorack-mouse/, /innorack-rat/, /faq/, /how-it-works/, /aquavive-mouse-water/. REST search (`/wp-json/wp/v2/search`) for auto water, autowatering, grommet, MVX5, M-BTM-A; WooCommerce Store API search for M-BTM-A, R-BTM-H-A, RVX5, MVX5 (no products). Media 3467.

**Repo:** `content/press-releases-recovered/` (21 releases, 2011 to 2026): no autowatering mentions. `content/from-wix/copy.md`: none. `content/drafts/ivc-rack-guide/` mentions R-BTM-A-H with a CONFIRM.

**Wayback Machine:** archive.org was offline ("Temporarily Offline") on 2026-11-06, so old innovive.com captures were not checked. Worth a retry.

**Patents:** US9265229B2 / US7954455B2, "Cage cover with filter, shield and nozzle receptacle" (assignee Innovive Inc), https://patents.google.com/patent/US9265229. US8316802B2, "Reusable water line grommet and disposable cage box" (Thoren, not Innovive), https://patents.google.com/patent/US8316802. It notes disposable boxes were rarely used with automatic watering because the grommet added cost. Background only; nothing from patents is presented as a product fact on the page.

**Competitor pages (what buyers expect answered):**
- Allentown EasyCage MAX, https://www.allentowninc.com/rodent-housing/easycage-max/ (autowatering version of a disposable cage needs a reusable grommet)
- Allentown NexGen MAX, https://www.allentowninc.com/rodent-housing/nexgen-max/
- Allentown blog, "An easy solution", https://blog.allentowninc.com/an-easy-solution/ (optional grommet to connect EasyCage to an existing autowatering system)
- Allentown Equinox washer, https://www.allentowninc.com/washing/washing-solutions/equinox/ (IVC manifold washing)
- Tecniplast IVC brochure, https://www.tecniplast.it/usermedia/uk/brochures/IVC_UK.pdf (Leak Detection System for flooding from valve failure)
- Distributor listing: Reuzeit used Innorack IVC Rat 3.5 systems, https://us.reuzeit.com/product/3373681

Common questions on those pages, and where the draft answers them: which cages and racks support it (Components, Compatibility); how the cage connects (How it works, grommet video); valve type and position, pressure, flushing, water types (Specs, as placeholders); leak and flood protection, sanitation, retrofit, mixing with bottles (FAQ, as placeholders).
