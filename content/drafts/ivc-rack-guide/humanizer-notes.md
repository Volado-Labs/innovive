# Humanizer pass notes: IVC Rack Configuration Guide

This was a separate editorial pass on the full first draft (kept at the scratchpad as draft-v1), followed by a length trim. The final copy is at `ivc-rack-configuration-guide.md`.

## Read-aloud and rhythm

- Opening. The draft defined IVC in a separate second paragraph, after "IVC rack" had already been used twice. I moved the definition into the opening so the term is defined the first time it appears, and changed "This guide walks through that method" (a signposting line) to "Here is the method."
- I broke up even sentence lengths in Steps 1, 4 and 6, so short lines ("Rows also set the height of the top row." "Then decide where exhaust goes.") now sit next to longer ones.
- Step 6 had one 45-word sentence about bagging, gaylords and InnoCycle. It is now two sentences.
- Two fragments that read like labels ("Filter and blower service intervals:" and "Airflow figures for the Innorack:") became full sentences or were folded into the paragraph before them.

## Patterns removed

- Triples. "a wall, an outlet and an aisle" became "another wall and aisle." The Step 4 feature run-on was regrouped so it no longer reads as one even list. In the cost list I merged two bullets ("Autoclavable construction and optional HVAC connectors") so the bullets don't all share one shape.
- Tailing negations and "not only / not just" shapes. "on the route the rack will travel, not only in the room" and the follow-up "not just the room" were both rewritten as "Measure the route as well as the room."
- Hype and claims with nothing behind them. I cut "in holding rooms of every size" from the closing, because no source supports it. "leave few places for dirt to sit" became the live-page wording, "designed for easy cleaning." "Bottles are the default on Innoracks" became "Innocage cages take water bottles, empty or pre-filled," which the rat rack page supports.
- Over-reach found in the fact check:
  - "so you can switch modes without changing hardware" went, because no source says it.
  - "look at filter status" on the controller went, because no source says the controller shows filter status.
  - The draft said emptying soiled cages was "the task with the highest exposure." The study names cage changing and emptying soiled cages together, so the copy now says both.
  - "hold twice the cages on the same footprint" became "for the same rows and columns," because double-sided depth is unknown.

## Voice added

- Plain stated opinion (Step 6): "In our view this is where most rack plans go wrong, and it has little to do with the rack."
- Honest limitation (Step 6): "That last row is the honest trade-off: disposable caging swaps capital and wash labor for a cost on every cage you open... We would rather run that math with you than assert it." Further limits stated plainly in the text: Innorack is designed for Innocage caging (FAQ), the *Guide* figures are minimums (Steps 1 and 2), rat wire bars still need washing (Step 6 table), there is no margin for rats over 500 g in an R-BTM-H (worked example 2), and "Ask any vendor, us included, whether its cages count as sealed."
- Practitioner details that a competitor's generic guide would not have: the shoulder-height top row, measuring door widths on the route in, the two-mothers-with-litters oxygen example, and putting the MVX3 gnotobiotic rack on backup power because its planning window is 6 hours.

## Length trim

The first full draft came to about 3,400 words including tables. The outline sets "about 2,000 to 2,500 words plus tables", so I cut repetition rather than content:
- The Tall rack matrix table is now one line.
- I dropped the floor-space column from the rack table, since Step 2 already covers it.
- Pre-bedded bedding volumes came out.
- The FAQ answers were shortened.
- Duplicate HEPA and exhaust sentences in Step 5 were merged.

Final count: prose about 2,080 words plus about 780 words of tables (2,859 combined). That excludes the TOC, the [CONFIRM]/[IMAGE]/[LINK] placeholders, Sources and the editorial fields.

## Rules sweep (final file)

- No em dashes, en dashes, arrows, curly quotes, emojis or `---` dividers. The only double hyphens are markdown table separator rows.
- No ban-list words.
- Headings use sentence case except the H1 the brief fixed.
- Bold is limited to the Quick answer label, the formula, the mini-example label and the matrix table labels.
- There are 8 internal links, each on first mention only, plus one [LINK] placeholder for the hub.
- No dates or "as of" years in the body. Publication years appear only in the Sources list.

## QA revision round (SlopMonster 3/5 to 5/5, shelf-life placeholders)

- At a glance Pressure row: the "whether you are X or Y" opener became "Positive protects the animals; negative protects people and the room."
- Step 3 buffer: the four-item list became two examples plus a separate sentence about quarantine and change-day spares.
- Step 4 features: the long list was split into two sentences, filtration and airflow first, then standard equipment.
- Step 5 table: "Allergen control, biohazard and infectious studies" became "Allergen control, and biohazard or infectious studies."
- Step 9: "animal numbers, size and room conditions" became a colon sentence about what is in each cage, plus "Room conditions matter too."
- Step 6 table: the caging shelf life is now [CONFIRM: caging shelf life, correction pending from Innovive]. Step 7: the Aquavive windows are now [CONFIRM: Aquavive shelf life], with a pointer to the printed fill date. Both are added to the editorial list.
- "Targeting zero landfill" is unchanged. Final deslop score: 5/5 CLEAN.

## Consolidation round (rat rack system and IVC cage system folded in)

- I saved the pre-change version as ivc-rack-configuration-guide-v1.md.
- Step 1: I added three sentences on choosing a mouse IVC cage system, a rat system or both. I kept them as short declaratives and named the one overlap (M-BTM-XL on the IVC Rat 3.5), so the point is specific rather than generic.
- New H3 under Step 4, "Choosing a rat rack system":
  - a framing sentence that names the real choice (the cage)
  - a five-row decision table
  - a strain CONFIRM, because no source gives strain guidance
  - one setup paragraph covering change interval, wire bars and lid power-failure hours
- In that setup paragraph I avoided a three-item lid list: the RSX1 is set against the RVX6 and RVX7 pair, and the sentence lengths vary.
- I left out the XL lid code. The source says "RV7XL" but the client's corrections list says "RVX7XL", so I did not name it.
- Two new FAQs, "How do I choose an IVC cage system?" and "What size rat rack system do I need?". In the rat answer I broke the three-rack capacity run with a question ("Need 9"?").
- "ivc caging" is not targeted. It appears only in the existing pointers to the hub.
- Added about 390 words (about 300 prose, 90 table). deslop --allow-proof: 5/5 CLEAN.

## 25% cut round (cut-plan.md applied)

- I saved the pre-cut version as ivc-rack-configuration-guide-v2-precut.md.
- Applied all 16 cut-plan items. Each fact now has one home:
  - Change intervals and wire bars live in Step 6.
  - Autowatering lives in Step 7.
  - Lid power-failure hours live in Step 9.
  - Rat headroom, floor space and capacity live in the main rack table, which has a new "Best for" column.
- Removed:
  - the At a glance table
  - the rat decision table
  - the Tall/XL inline position line
  - the Step 8 tall-rat paragraph (its rat-racks link moved to the rat H3)
  - the rat setup paragraph
- Shortened the FAQ answers to one or two sentences.
- I needed about 175 more words beyond the plan to get under 2,445. They came only from prose, by shortening sentences and removing repeats, for example:
  - the second "floor under enrichment doesn't count" (Step 7; the Step 2 instance stays)
  - the worksheet's list of steps
  - the pressure-mode paragraph, folded into one colon sentence, since the table carries "Protects"
- Rhythm pass: I let short declaratives sit next to longer colon sentences rather than leaving a run of same-length lines, and recast "Daily, read..." as a plain imperative. No words were added back.
- Count: 1,734 prose + 706 tables = 2,440. deslop --allow-proof: 5/5. I rewrote the cost-section triple ("racks, caging and running costs") to clear it.
