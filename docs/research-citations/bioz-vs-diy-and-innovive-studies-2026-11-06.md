# Published research on Innovive product pages: Bioz or do it ourselves?

Prepared by Volado Labs for Innovive, 2026-11-06. Follows the 11/6 sync, where Robin said product-specific studies matter more to PIs and vets than datasheets.

Full citation list: `docs/research-citations/innovive-published-studies-2026-11-06.csv` (657 rows, 22 hand-checked and summarised).

## The short answer

Do it ourselves first. More than 600 published papers name Innovive products in their methods, so the raw material is there. A hand-picked "Published research" section on two pages (Innorack and the M-DIVIDER2 cage divider) costs nothing extra, lets Innovive choose every study shown, and, unlike Bioz, Google can read it. Revisit Bioz only if the trial pages show visitors actually use the studies and Innovive wants the lead data Bioz sells.

## A. What Bioz is

**What it shows.** A badge on the product page ("94/100 | 16 Citations, Powered by Bioz") that opens a panel of papers mentioning the product, with an AI summary, key author and Nobel flags, and star ratings. Higher tiers add figures, filters, full-text search, a map and a page listing every paper for every product. Vendors also get a dashboard of researcher behaviour and citation trends. Bioz pitches it as building trust and finding leads.

**Where the data comes from.** Bioz says it reads all PubMed journals, open-access and subscription, plus preprints, patents and grants, about 35 million articles, updated daily. It matches product names in the text. It does not say how it gets subscription full text. Matching is loose: on Shepherd's Alpha-Dri Plus widget, one of the 16 "citations" is a cystic fibrosis bacteria paper where the bedding is only a methods detail.

**How the score works.** Stars run from 75 to 100 across 15 inputs: number of mentions, recency, journal impact, and also traffic on bioz.com itself (page visits and clicks). The weights are secret. Because paid badges send visitors to bioz.com, paying could nudge a product's score up, even though Bioz says payment does not affect scores.

**Price.** Not published. Prices come from a sales call "according to our rate-cards". The roughly $900 a month Innovive was quoted is about $10,800 a year. Bioz reportedly had $5.7M in annual revenue in 2024.

**Choosing which studies show.** We found no public detail on the vendor portal for excluding studies, and nothing on the widget tells readers the list was filtered. Robin saw the exclusion feature in the demo, so it exists; it just is not documented publicly.

**Does it help SEO? No.** The widget loads from bioz.com inside an embedded frame, and bioz.com's robots.txt tells all search engines not to read the widget pages. Study links point to bioz.com, not to the journals, and can be marked nofollow. So the citation text is invisible to Google on innovive.com, and any link value goes to Bioz. Bioz's claim that it improves "SEO and domain authority" does not hold up for the vendor's own pages.

## How much of this we can build ourselves

| Bioz feature | Do it ourselves | Effort |
|---|---|---|
| List of studies per product | Yes. This report already has it, tagged by product. | Done |
| Choose which studies show | Yes, fully. Innovive approves every study. | None |
| Plain summary of each study | Yes, one hand-checked line per study (better than an AI summary of loosely matched papers). | Done for 22 |
| Links to each study | Yes, straight to the journal or PubMed, which readers trust more than a third-party site. | Small |
| Citation count | Yes, as a plain line: "Innovive caging appears in the methods of more than 600 published studies." | Small |
| Readable by Google | Yes. Ours is normal page text, so it helps innovive.com rank. Bioz's does not. | Built in |
| New studies found automatically | Partly. A saved Europe PMC search for "Innovive" plus a quarterly check by us (about an hour). | Small, ongoing |
| Star score out of 100 | No, and we would not try. It is Bioz's own formula. | Skip |
| Key-author flags | Could do by hand for the few that matter. | Skip for now |
| Visitor behaviour and lead data | No. This is the one real thing Bioz adds. GA4 can still show clicks on study links. | Skip |

**What we would build.** A "Published research" section in Elementor on each trial page: three to five cards, each with the study title, journal and year, a one-line plain takeaway, and a link to the paper. A heading such as "Selected studies using Innorack" makes it honest that the list is chosen. One shared Elementor template means adding a study later is a quick edit. No plugin, no monthly fee. Optional extra: mark each study up as structured data so search engines recognise it as a citation.

**Honest trade-offs.**
- We lose the live badge, the score, and Bioz's lead and behaviour data.
- New studies will not appear on their own; someone has to check quarterly.
- Our count will look lower than Bioz-style counts, because we only show studies we have checked.
- We win on control (Innovive picks every study), on search value, on cost, and on accuracy.

## B. The studies

Method: we searched the full text of every paper in Europe PMC (which mirrors PubMed Central) for Innovive, Innocage, Innorack, Aquavive, Innowheel and Innodome, then read the exact sentence that names Innovive in each paper we could open. We also read the 2026 AALAS meeting abstracts and checked the main JAALAS husbandry papers one by one. Result: 657 papers, 631 with the Innovive mention confirmed in the text. Most name Innovive only in the methods, which still proves real labs use the product. The 22 below are the ones worth putting on a product page, or worth knowing about. Each is in the CSV with its link.

### Innorack IVC racks (sales priority): best trial page

Use on the page:
1. **Validation of Sanitization Practices in Single-use IVC Mouse Cages at Standard and Thermoneutral Temperatures.** JAALAS, 2022. doi.org/10.30802/aalas-jaalas-22-000036. Names Innorack 3.5 and MVX-6 lids. Backs changing the cage bottom and water every 14 days and the full cage every 28 days, even at warm temperatures. The strongest rack study we found.
2. **Using Filter Media and Soiled Bedding in Disposable IVC as a Refinement to SPF Mouse Health Monitoring.** JAALAS, 2022. doi.org/10.30802/aalas-jaalas-22-000013. Cage-level filter testing found infections more reliably than testing sentinel mice. Also names Allentown.
3. **Reproductive performance of mice in disposable and standard IVC.** JAALAS, 2013. PMC3690442. Mice bred just as well in disposable cages as in reusable ones (776 pups over 3 cycles).
4. **Effects of a 28-day cage-change interval on intracage ammonia, nasal histology and perceived welfare of CD1 mice.** JAALAS, 2011. PMC3228923. A single mouse can go 28 days; groups of 3 need changing every 2 weeks, 5 or breeders weekly. Mixed but useful.

Know about, do not feature:
- **CO2, O2 and ammonia in mouse and rat disposable IVC removed from ventilation.** JAALAS, 2022. doi.org/10.30802/aalas-jaalas-22-000028. Sealed cages taken off the rack should not stay off more than 1 to 2 hours for group mice. Good operating guidance for a FAQ, poor headline.
- **CO2 and O2 levels in disposable IVC after removal from ventilation.** JAALAS, 2012. PMC3314517. Same point, framed as a risk. Names Allentown.
- **Rack design and exhaust-debris pathogen detection.** JAALAS, 2016. PMC5113880. Exhaust-air testing works poorly on racks with a filter between cage and exhaust (Innovive's design). Names Tecniplast and Green Line.
- **Influence of housing systems on aging DBA/2 mice.** Animals, 2020. doi.org/10.3390/ani10040746. Innorack mice differed from chamber-housed mice in weight and temperature; neither better nor worse.
- **2026 AALAS abstract P341 (Stanford).** Filters inside Innovive cages caught more pathogens than filters on Innovive lids. Mildly unfavourable for lid filters.

### M-DIVIDER2 cage divider: second trial page

1. **Partially divided caging reduces overall aggression and anxiety in group-housed male C57BL/6J mice.** BMC Veterinary Research, 2024. doi.org/10.1186/s12917-024-03918-y. University of Arizona. Less anxiety, fewer bite wounds and less aggression in Innocage cages with a partial divider. Caveat: the lab hand-made its divider from Innovive pallet sheets; it is not the M-DIVIDER2. The authors say it was made for the Innovive mouse cage. Open access, no competitor caging named.
2. **2026 AALAS abstract P135, Evaluating a Cage Divider System as an Alternative to Singly Housing Mice.** JAALAS 65(5), 2026 meeting abstracts, PMC13641234. Eisai (Cambridge, MA). A prototype feeder-mounted divider, with a lid giving each side its own water, let male mice live as divided pairs instead of alone: no aggression, no weight change, better nests. **This is very likely the AALAS study Robin meant, but the abstract does not name Innovive.** The same Eisai team wrote the Aquavive bottle paper below. Innovive should confirm it is their prototype and ask the authors to credit Innovive in the full paper (that is also the backlink check).
3. **Partial cage division significantly reduces aggressive behavior in male laboratory mice.** Laboratory Animals, 2018. doi.org/10.1177/0023677217753464. The same Arizona lab's pilot. Paywalled, so we could not confirm it names Innovive.

### Aquavive water: easy third page if wanted

- **Extended Sanitization Frequency for Bottles: Using Volume as an Alternative to Time-Scheduled Replacements.** JAALAS, 2025. doi.org/10.30802/aalas-jaalas-25-116. Eisai. Names the Aquavive bottle. Leaving prefilled bottles on until 100 mL remained (13 to 47 days) caused no health changes and no bacterial growth. Strong and favourable. More than 100 other papers name Aquavive or Innovive prefilled water in their methods.

### Metabolic cage kit: too thin for now

- **Mechanisms Underlying Cedazuridine-Mediated Enhancement of Oral Decitabine Bioavailability.** Cancer Research Communications, 2026. doi.org/10.1158/2767-9764.crc-25-0764. Names the Innovive Metabolic Cage Kit for 23-hour urine and feces collection. Only one confirmed paper, methods mention only. Not enough for a section yet.

### Rat caging

- **Effect of 2 Bedding Materials on Ammonia Levels in IVC.** JAALAS, 2016. PMC4747007. Rats in disposable IVC on corncob lasted 14 to 21 days before ammonia rose. Neutral to favourable.
- **Enlarged housing and social play in rats.** Animals, 2025. doi.org/10.3390/ani15182757. Mentions the Innovive Tall and Tall XL only as market examples next to Tecniplast; the cage tested is not Innovive. Do not use.
- About 35 more papers name Innovive rat caging in their methods.

### Enrichment (Innodome, Innowheel)

- **Effects of Enrichment and Litter Parity on Reproductive Performance in BALB/c and 129/Sv Mice.** JAALAS, 2016. PMC4943608. A dome with wheel improved some breeding measures. Mostly favourable; names Tecniplast and Ancare.
- **Unfavourable, do not feature:** a 2026 PLoS One study (doi.org/10.1371/journal.pone.0353843) found an Innodome plus Innowheel reduced social interest in female mice, and a 2017 JAALAS case study (PMC5361047) found running wheels triggered circling in one mouse line.

### Innocage mouse caging, general

About 290 papers name Innocage or Innovive mouse cages in their methods. These support a sitewide line like "used in more than 600 published studies" rather than individual cards.

## Studies that name competitors

About 100 papers also name Tecniplast, Allentown, Ancare, Thoren, Lab Products or Green Line. Most are harmless (for example, Ancare nesting material). The ones that compare systems are flagged above and in the CSV column `competitors_named`.

## Recommendation

1. Trial a "Published research" section on the **Innorack IVC Mouse** page (studies 1 to 4 above) and the **M-DIVIDER2** page (the 2024 Arizona study, plus the Eisai abstract once Innovive confirms it is their divider).
2. Add the line "Innovive caging appears in the methods of more than 600 published studies" to both pages.
3. Track clicks on the study links in GA4 for two to three months.
4. Robin's call with Renee at Shepherd: worth asking whether Bioz brought Shepherd any leads, and whether they could pick which studies show.
5. Decide on Bioz after the trial. If the sections get used and Innovive wants visitor and lead data, Bioz is the only way to get that. If not, we have saved about $10,800 a year.

**Needs from Innovive:** confirm the Eisai P135 divider is theirs; approve the four rack studies and the divider study for the pages; say whether to include the cautionary ventilation studies in a FAQ.

Nothing on the live site was changed for this report.
