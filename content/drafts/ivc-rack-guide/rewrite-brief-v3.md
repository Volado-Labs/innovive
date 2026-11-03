# Rewrite brief: IVC rack guide v3 (voice and tables)

Collin's feedback on v2: "Right from the beginning, the sentences read awkwardly." His examples were "You size an IVC rack from the animals outward" ("I don't even understand what that means") and "IVC stands for individually ventilated cage" ("way too elementary for readers of Innovive's blog"). He also said the tables are formatted very poorly: a 7-column table ran off the page, and cells wrapped onto three lines.

This is a full voice rewrite, not a polish. Keep the facts, structure and keywords. Rewrite the sentences.

## Read first

1. Voice profile (required): /Users/collinwood/Projects/innovive/content/voice/innovive-voice-profile.md
2. Model posts, in the voice to imitate: /Users/collinwood/Projects/innovive/content/voice/posts/3991-*.md, 3981-*.md, 3986-*.md
3. Stance and terminology rules from the September rework, sections "Banned moves" and "Terminology": /Users/collinwood/Projects/innovive/content/drafts/2026-09-18-ivc-rework/00-shared-brief.md
4. Current draft, saved as v2 before you edit: /Users/collinwood/Projects/innovive/content/drafts/ivc-rack-guide/ivc-rack-configuration-guide.md

Save the current file as ivc-rack-configuration-guide-v2.md, then write v3 to ivc-rack-configuration-guide.md.

## Voice fixes (apply throughout)

- **Opening:** write it fresh. Two short paragraphs that put a facility manager in their situation: planning a holding room, an expansion or a new program, and needing to know how many racks and which ones. Then say how we work it out on a sizing call: census first, then cages, racks, pressure and the cage-change workflow.
  - Do not define IVC.
  - No aphorism.
  - The keyword "IVC rack" goes in the first 100 words naturally.
  - The Quick answer box stays, but reword it so it reads like a person.
- **Reader level:** a peer. Never explain an IVC, the IACUC, a cage wash, autoclaving or what a census is.
- **Stance:** confident from our side. Remove every neutral-vendor or self-undermining line, including:
  - "So ask any vendor, us included, whether its cages count as sealed." Replace it with our own fact, from sources/gnotobiotics.txt: our gnotobiotic setup uses "cage lids that create an airtight seal". Keep [CONFIRM: whether Innocage IVC lids are sealed in the sense used in these studies].
  - The "honest trade-off" paragraph, and "whether you already own a working cage wash". Reframe from our side: the fair comparison is full cost per occupied cage-week, and we will run those numbers with you. No invented prices.
  - The FAQ line "Whoever you buy from, get the interval in writing."
- **Terminology:**
  - Body copy uses "consumable caging" or "consumable IVC caging". "Disposable" may stay once in the first 100 words if natural.
  - Never "sterilize" or "sterile". The washable workflow is washed and autoclaved.
  - Say "used caging", not waste.
- **Power draw:** our live FAQ states "very low power draw, similar to a standard light bulb". You may use it and drop the power-draw CONFIRM. Cite it like the other Innovive FAQ facts.
- **Rhythm:** mostly 12 to 20 word plain sentences, paragraphs of 2 to 4 sentences, and at most two short sentence pairs in the whole piece. Read every sentence aloud. If it needs decoding, rewrite it.

## Tables (hard rules)

Innovive's rule is sparse tables, and Collin flagged the formatting.

- **At most 4 columns** in any table. Cells hold short values only, never sentences.
- **Units:** put them in the column header and give one unit per cell. Use inches in the cells. Put the metric equivalent once in a short note under the table, or give a cm column only where it matters.
- **Keep, but narrow:**
  1. The *Guide* Table 3.2 space table: Animal and weight | Floor area per animal (in²) | Minimum height (in). Put the cm² equivalents in one note line below it. All numbers stay exact.
  2. The Innocage bottoms table: Cage | Floor space (in²) | Headroom (in) | Sized for. Move Euro equivalents, the *Guide* ceiling and "runs on" into one or two sentences of prose under the table.
  3. The main rack table: Rack | Max cages | Rows × columns | Headroom (in). Move "Best for" and cage bottoms into a short sentence per rack or a compact list.
  4. The two configuration matrices. They are already 4 columns. Keep them.
  5. The power-failure lid table (2 columns). Keep it.
- **Convert to prose:**
  - the pressure table
  - the washable versus consumable table (two short paragraphs from our side)
  - the three worked-example tables (each becomes a short paragraph, with the result line kept)
- That leaves 6 tables at most, all numeric.

## Must survive

- Every fact and number currently in the draft, except power draw, which becomes a fact as described above.
- Every [CONFIRM], other than power draw. Update the editorial list to match.
- All 10 internal links, each used once.
- All 9 FAQ questions. Rewrite the answers in voice; "What is an IVC rack?" should answer at peer level in one or two sentences.
- Keywords: "IVC rack" in the H1 and first 100 words; "rat rack system" in its H3 and once in the body; "IVC cage system" in Step 1 and the FAQ.
- The endnotes, and the Sources list.
- Length ceiling: 2,440 words of prose plus tables, counted the same way as before. Shorter is fine.

## Process

Rewrite, then run the Humanizer as a separate pass, then run deslop --allow-proof until it scores 5/5. Report back:
- the word count
- the table count and the largest column count
- the CONFIRM count
- the link count
- the new opening paragraph, quoted
- any fact you could not place
