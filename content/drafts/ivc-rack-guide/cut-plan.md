# Copy edit: cut the IVC rack guide by 25%

Current: 3,258 words (2,390 prose + 868 tables, same counting as before: excludes Contents, placeholders, Sources, editorial fields).
Target: **2,445 or fewer** on that same count. Hard ceiling, not a guideline.

The diagnosis: the guide states most facts two or three times (rack capacities, rat headroom, change intervals, wire bars, power-failure hours, autowatering, pressure rule, cost factors). Every fact keeps exactly ONE home. Second and third mentions go. After that, cut throat-clearing sentences that restate what the next sentence says.

## Must survive untouched

- Every number in the *Guide* Table 3.2 table, the Innocage bottom table, the main rack table, both configuration matrices, the power-failure lid table, the washable vs disposable table, the three worked-example tables.
- Every [CONFIRM] item (move it with its fact if the fact moves; do not drop any; the editorial list must still match).
- Every endnote marker that still has a claim attached, and the Sources list.
- All 10 internal links, each once. If the paragraph holding a link is cut, move the link to the fact's surviving home.
- Keywords: "IVC rack" in H1 and first 100 words; "rat rack system" in the H3 and once in body; "IVC cage system" once in body and in the FAQ question.
- All 9 FAQ questions (they are search targets), and every H2/H3 heading except where noted below.
- The honest trade-off sentence in Step 6 and the one stated opinion ("In our view this is where most rack plans go wrong").

## Line-by-line cuts

1. **Delete the "At a glance" H2 and its table.** It duplicates the Contents list and the Quick answer. Remove it from Contents too.
2. **Intro paragraph:** cut to two sentences. Keep the IVC definition and "Here is the method, with real numbers and worked examples on our Innorack IVC racks." The middle sentence repeats the Quick answer.
3. **Step 1:** merge the two sentences after the *Guide* table into one ("These are minimums; your IACUC or AAALAC program may set stricter ones [1][2]."). Keep the mouse/rat/both paragraph but cut it to two sentences.
4. **Step 2:** keep. Trim the breeding paragraph to two sentences.
5. **Step 3:** cut "Set it from your own history." and fold quarantine/spares into the first buffer sentence.
6. **Step 4:**
   - Cut the ergonomics paragraph to one sentence.
   - Feature paragraph: keep as the ONE place the shared rack features live (three sentences max).
   - Add a "Best for" column to the main rack table (Standard mice / Standard rats up to 500 g, plus M-BTM-XL mouse breeding / Rats needing more than 7" headroom / Large rats, including past 500 g). Then **delete the separate rat decision table**, because headroom, floor space and cages per rack are already in the main table.
   - Delete the inline Tall IVC Rat and Tall XL position line under the matrices. Max positions are in the rack table, and the arithmetic rule is stated above the matrices.
   - Keep "Measure the route as well as the room" (it is the best sentence in the section). Cut it to one sentence.
7. **"Choosing a rat rack system" H3:** cut to about 60 words. One framing sentence with "rat rack system", a sentence on when to step up (headroom, then floor space), and the [rat rack comparison](https://innovive.com/rat-racks/) link, moved here from Step 8. Delete the setup paragraph and the autowatering sentence, since each fact already lives in Step 6, Step 7 or Step 9. Keep [CONFIRM: rat strain guidance by rack] here.
8. **Step 5:**
   - Fold "HEPA on supply protects the animals, and HEPA on exhaust protects the room. Every Innorack filters both." into a single sentence after the pressure table.
   - Tighten the allergen paragraph to three sentences with the same two citations and the sealed-lid CONFIRM.
   - Keep the exhaust and outlet content but cut its sentence count by about half.
9. **Step 6:** keep the change intervals here (their one home). Washable loop paragraph down to two sentences. Disposable paragraph down to three. Trade-off paragraph down to two (drop "We would rather run that math with you than assert it" only if needed to hit the target).
10. **Step 7:** keep autowatering here (its one home). Cut "Each bottle carries a printed fill date, so check use-by windows against it" to just the CONFIRM.
11. **Step 8:** delete the tall-rat paragraph (now covered in the rat H3). Metabolic and gnotobiotic paragraphs one or two sentences each.
12. **Step 9:** prose around the lid table down to two sentences in total, plus the 6-hour single-filter-lid rule.
13. **Worked examples:**
    - Cut the reasoning sentence in example 1 ("One 192-position rack would not hold 202 cages, and two 9-row racks keep the top row lower.") to its shortest form.
    - Cut the 500 g note in example 2 to one sentence.
    - Keep every result line and every CONFIRM.
14. **Cost H2:** keep the bullets. Cut the closing sentence to one short line.
15. **FAQ answers:** one to two sentences each, because the body now carries the detail.
    - "How many cages fit": capacities only.
    - "Positive or negative": one sentence plus "Every Innorack runs both."
    - "How much does it cost": one sentence pointing to sized quotes.
    - "How do I choose an IVC cage system": two sentences.
    - "What size rat rack system": two sentences.
16. **Closing:** two sentences plus the CTA link and the hub placeholder.

## After cutting

- Count the words the same way. If you are over 2,445, keep cutting prose, never tables or facts.
- Run the Humanizer on the result. Cutting creates choppy, same-length sentences, so vary rhythm without adding words back.
- Run deslop.py --allow-proof until it scores 5/5.
- Update Contents, the editorial CONFIRM list and the schema note (FAQ is still 9).
- Save a copy of the pre-cut version as ivc-rack-configuration-guide-v2-precut.md first.
