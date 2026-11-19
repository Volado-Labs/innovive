# Innovive press releases: recovery inventory

Compiled 2026-09-23. Research only. Nothing was written to WordPress and the live site was not modified.

## What this is

Innovive's press releases were never migrated to the WordPress rebuild. This inventory accounts for every press
release that has ever lived on an Innovive website, recovers the full text of each one, and marks what is missing.

**Twenty-one press releases are missing from innovive.com. None are live on the new site.** They fall into two
generations:

- **Tier 1, the Wix generation (7 releases, 2023-02-06 to 2026-04-28).** These are the ones the client means. They
  were live on innovive.com until the June 2026 cutover and are still served today by the orphaned Wix mirror.
  Recovered from the live mirror at full fidelity, including images that are still hosted and reachable.
- **Tier 2, the legacy pre-Wix generation (14 releases, 2011-04-14 to 2020-05-29).** These lived at
  `innovive.com/company/news.html` on the pre-2024 HTML site. They were already gone before the Wix site existed,
  so they are almost certainly outside the scope of the client's request, but they are genuine Innovive press
  releases and they are recoverable, so they are catalogued here for a decision.

### Correction to the vault: the old site is not ytechservices.com

The task brief and the 2026-07-16 meeting notes both name **ytechservices.com** as the live old site. That is wrong,
and the vault already records the correction at `wiki/clients/innovive.md` (2026-08-04 entry). The real mirror is
**wytecproductionservices.com**. Verified this session:

| Domain | Result |
|---|---|
| `ytechservices.com` | HTTP 406, unrelated GoDaddy-parked domain, no Innovive content |
| `wytecproductionservices.com` | HTTP 200, serving a complete mirror of the old Innovive Wix site |

The mirror still carries the Innovive branding, the HubSpot tracking code, and a working `/news/` collection. That is
the source used for Tier 1 here, and it is also the reason contact forms from that domain keep landing in HubSpot.

## What is on the new site right now

- `https://innovive.com/wp-json/wp/v2/posts` returns **11 posts**, all dated 2026-06-14 or 2026-06-18, all in
  category `Uncategorized` (id 1). All 11 are blog articles. **Zero press releases.**
- `https://innovive.com/blog-news/` renders those same 11 blog cards and nothing else. The nav item labelled "News"
  points at `/blog-news/`, so the site has a News label with no news behind it.
- The categories `International` (4), `Regional Shows` (3) and `US` (5) exist with non-zero counts but hold no posts
  in the `posts` endpoint. They appear to belong to an events/tradeshow taxonomy, not to press releases.
- `https://innovive.com/news/<any-old-slug>` **301-redirects to `/blog-news/`**. So all 7 Tier 1 URLs currently
  resolve to a page that does not contain the article. The redirect preserves the traffic but loses the content.
- `https://innovive.com/press-releases` returns **404**. That URL was a real page on the Wix site as recently as
  2024-09-09 and has no redirect.

## Blog posts vs press releases

The old site kept these cleanly separated in two different Wix collections, and so does this inventory:

- `/post/<slug>` was the **Blog** collection, 11 items. All 11 were migrated to WordPress. Verified by comparing the
  old `blog-posts-sitemap.xml` against the 11 live posts: the counts match and the titles correspond one to one.
- `/news/<slug>` was the **News** collection, 7 items. **None were migrated.** These are the press releases.

One blog title drifted during migration and is worth a glance, though it is not a press release and not in scope:
old `/post/meeting-facility-esg-goals-with-a-more-sustainable-vivarium-solution` has no exact counterpart, while the
new site has `how-can-a-disposable-ivc-solution-make-your-acfs-operations-more-sustainable`. Same subject, different
title. Most likely a deliberate retitle, flagged as uncertain rather than treated as a loss.

## Inventory

### Tier 1: Wix-era press releases (the migration gap)

| # | Date | Title | Original URL | Status |
|---|---|---|---|---|
| 1 | 2026-04-28 | Innovive Expands Global Reach Through Strategic Partnership with Attentive Science to Accelerate Scientific Research Across GCC and MENA Regions | `https://www.innovive.com/news/innovive-expands-global-reach-through-strategic-partnership-with-attentive-science-to-accelerate-scientific-research-across-gcc-and-mena-regions` | **MISSING** |
| 2 | 2025-04-16 | Innovive Expands into Latin America & Caribbean Through a New Distribution Partnership with EAD Scientific | `https://www.innovive.com/news/innovive-expands-into-latin-america-and-caribbean` | **MISSING** |
| 3 | 2024-10-31 | Innovive, LLC Appoints Jamie S. Blose, Pharm.D, MBA, JD as Chief Executive Officer | `https://www.innovive.com/news/new-chief-executive-officer` | **MISSING** |
| 4 | 2024-08-12 | Innovive Announces Strategic Partnership With Dr. Marcel Perret-Gentil of PLAVS to Enhance and Expand Innovive+ Vivarium Services in the US, Globally | `https://www.innovive.com/news/strategic-partnership-with-dr-marcel-perret-gentil` | **MISSING** |
| 5 | 2024-02-01 | PET rodent cage processor recycled 1.2M pounds in 2023 | `https://www.innovive.com/news/pet-rodent-cage-processor-recycled` | **MISSING** |
| 6 | 2024-01-30 | Celebrating Innocycle’s Environmental Milestones: Closed-Loop Recycling Service Makes Significant Impact | `https://www.innovive.com/news/major-environmental-milestones` | **MISSING** |
| 7 | 2023-02-06 | Innovive Consolidating Product Support Services and Vivarium Management Solutions Under Innovive+ | `https://www.innovive.com/news/product-support-services-and-vivarium-management-solutions` | **MISSING** |

All 7 recovered at full fidelity from the live mirror, including the featured image for each. All 7 featured images
return HTTP 200 from `static.wixstatic.com` and can be downloaded and re-uploaded to the WordPress media library.

### Tier 2: legacy pre-Wix press releases (lost at the earlier rebuild)

| # | Date | Title | Original URL | Status |
|---|---|---|---|---|
| 1 | 2020-05-29 | Innovive Announces Expansion into South Dakota | `http://www.innovive.com/company/news.html#siouxcity` | **MISSING** |
| 2 | 2018-06-27 | Innovive Moves East Coast Facility to Billerica, Massachusetts | `http://www.innovive.com/company/news.html#billerica` | **MISSING** |
| 3 | 2018-04-17 | Innovive Grants Limited License for Allentown Disposable Caging | `http://www.innovive.com/company/news.html#allentown-disposable-cages` | **MISSING** |
| 4 | 2017-09-14 | Innovive and Lou Ristic are Recognized for Excellence | `http://www.innovive.com/company/news.html#excellence-award` | **MISSING** |
| 5 | 2017-08-03 | Innovive Doubles Pre-Bedded Caging Throughput | `http://www.innovive.com/company/news.html#doubling-bedding-line` | **MISSING** |
| 6 | 2017-07-07 | Emmanuel Ferton Joins Innovive as Director of Manufacturing Operations | `http://www.innovive.com/company/news.html#ferton-hiring` | **MISSING** |
| 7 | 2015-12-17 | Innovive Purchases New Corporate Headquarters in San Diego, CA | `http://www.innovive.com/company/news.html#headquarters-2015-move` | **MISSING** |
| 8 | 2015-08-25 | Pfizer’s Stephen Baker Joins Innovive | `http://www.innovive.com/company/news.html#pfizer-baker-joins-innovive` | **MISSING** |
| 9 | 2013-07-10 | Innovive Opens East Coast Corporate Office and Distribution Center in New Hampshire | `http://www.innovive.com/company/news.html#hudson-open` | **MISSING** |
| 10 | 2013-05-30 | Innovive Strengthens Nationwide Recycling Program with New Bay Area Recycling Facility | `http://www.innovive.com/company/news.html#bayarea` | **MISSING** |
| 11 | 2011-12-29 | Innovive Named Winner of the Waste Reduction Awards Program (WRAP) by the California Department of Resources Recycling and Recovery | `http://www.innovive.com/company/news.html#wrap` | **MISSING** |
| 12 | 2011-04-21 | Innovive Receives 2011 Recycler of the Year Award by San Diego 19th Waste Reduction and Recycling Program | `http://www.innovive.com/company/news.html#recycler` | **MISSING** |
| 13 | 2011-04-15 | Innovive Congratulates The Jackson Laboratory - Winner of The 2011 Turnkey Facility of the Year Award | `http://www.innovive.com/company/news.html#jackson` | **MISSING** |
| 14 | 2011-04-14 | Introducing New AIA Continuing Education Credit Course - "Implementing Disposable Caging in New and Existing Facilities" | `http://www.innovive.com/company/news.html#aia` | **MISSING** |

All 14 recovered in full from the Wayback Machine snapshot of 2020-06-21. Body text is complete, not truncated.

### Already live on the new site

None. No press release from either generation exists anywhere on innovive.com.

## Ambiguities, discrepancies and caveats

1. **Two dates disagree between old site versions.** The Wix CMS record dates (used throughout this inventory, and
   matching what the live mirror displays today) differ from what the archived `/press-releases` index page showed on
   2024-09-09 for two items:

   | Release | Wix record date, and current display | 2024 `/press-releases` index showed |
   |---|---|---|
   | Strategic Partnership with Dr. Marcel Perret-Gentil | Aug 12, 2024 | August 13, 2024 |
   | Consolidating Product Support Services under Innovive+ | Feb 6, 2023 | February 09, 2023 |

   The record date is the better source and is what these files use, but someone should confirm the intended public
   date before republishing, especially for the Perret-Gentil release.

2. **Timezone edge on stored dates.** Wix stores dates as UTC timestamps at odd hours (for example the Innovive+
   release is `2023-02-06T21:00:00Z`, which is Feb 6 in UTC but would render Feb 6 in US Pacific too). The dates
   used here match what the mirror actually renders, so they are safe, but they are not authored dates.

3. **Tier 2 scope is a judgment call, not a finding.** The client asked for "the missing press releases from the
   prior site". If "prior site" means the Wix site, the answer is 7. Tier 2 is offered because it was found in the
   same sweep and is recoverable; it should not be republished without asking. Several Tier 2 items are also stale in
   ways that matter (personnel announcements for people who may have left, a Hudson NH office that later moved to
   Billerica, "Innovive Inc" rather than "Innovive, LLC").

4. **Tier 2 images survive only in the archive.** Three legacy releases reference images that now 404 on
   innovive.com. All three are retrievable from the Wayback Machine (verified HTTP 200 via `web.archive.org/web/2019id_/...`).
   If Tier 2 is republished, those images have to be pulled from the archive, not the live host.

5. **The mirror is the only live copy of Tier 1, and it is slated for removal.** wytecproductionservices.com is the
   domain the team has been discussing archiving or redirecting. Once it goes, the live source for these 7 releases
   goes with it. Wayback has them too, so nothing is at risk now that they are captured in this directory, but the
   capture should be treated as the authoritative copy from here on.

6. **No PDFs.** No press release in either tier links to a PDF. The "technical papers with intact backend links"
   item in the vault action list is a separate migration task and is not covered by this inventory.

7. **Outbound links inside the bodies need checking before republishing.** Several point at the old domain or at
   third parties:

   - `http://innovive.com/contact` (LatAm release): the new site uses `/contact-us/`.
   - `http://innovive.com` and `http://www.innovive.com` boilerplate links in four releases: harmless but should be https.
   - `http://www.eadscience.com` (LatAm release), third party.
   - `https://www.linkedin.com/company/innovive/?viewAsMember=true` in two releases: the `viewAsMember` parameter
     should be stripped.
   - `https://www.businesswire.com/news/home/20240130564780/...` and a `resource-recycling.com` article in the PET
     release, both third party.
   - `http://www.alnmag.com/article/2011/04/turnkey-award-winners-announced` in the 2011 Jackson Laboratory release,
     third party and likely dead.

8. **Nothing was retrievable only in part.** Every one of the 21 items listed was recovered with complete body text.
   There are no known press releases that could not be recovered.

## Files in this directory

Each release is also saved as its own file, named `<date>-<slug>.md`, with YAML front matter carrying the title,
date, original URL, source, image URLs and status.

- `2026-04-28-innovive-expands-global-reach-through-strategic-partnership-with-atten.md`
- `2025-04-16-innovive-expands-into-latin-america-and-caribbean.md`
- `2024-10-31-new-chief-executive-officer.md`
- `2024-08-12-strategic-partnership-with-dr-marcel-perret-gentil.md`
- `2024-02-01-pet-rodent-cage-processor-recycled.md`
- `2024-01-30-major-environmental-milestones.md`
- `2023-02-06-product-support-services-and-vivarium-management-solutions.md`
- `2020-05-29-innovive-announces-expansion-into-south-dakota.md` (legacy)
- `2018-06-27-innovive-moves-east-coast-facility-to-billerica-massachusetts.md` (legacy)
- `2018-04-17-innovive-grants-limited-license-for-allentown-disposable-caging.md` (legacy)
- `2017-09-14-innovive-and-lou-ristic-are-recognized-for-excellence.md` (legacy)
- `2017-08-03-innovive-doubles-pre-bedded-caging-throughput.md` (legacy)
- `2017-07-07-emmanuel-ferton-joins-innovive-as-director-of-manufacturing-operations.md` (legacy)
- `2015-12-17-innovive-purchases-new-corporate-headquarters-in-san-diego-ca.md` (legacy)
- `2015-08-25-pfizer-s-stephen-baker-joins-innovive.md` (legacy)
- `2013-07-10-innovive-opens-east-coast-corporate-office-and-distribution-center-in.md` (legacy)
- `2013-05-30-innovive-strengthens-nationwide-recycling-program-with-new-bay-area-re.md` (legacy)
- `2011-12-29-innovive-named-winner-of-the-waste-reduction-awards-program-wrap-by-th.md` (legacy)
- `2011-04-21-innovive-receives-2011-recycler-of-the-year-award-by-san-diego-19th-wa.md` (legacy)
- `2011-04-15-innovive-congratulates-the-jackson-laboratory-winner-of-the-2011-turnk.md` (legacy)
- `2011-04-14-introducing-new-aia-continuing-education-credit-course-implementing-di.md` (legacy)

---

# Full text: Tier 1, Wix-era press releases

Seven releases, newest first. Source: the live mirror at wytecproductionservices.com, extracted from the Wix CMS
record rather than scraped from rendered HTML, so the text is the authored copy with no navigation chrome.

## Innovive Expands Global Reach Through Strategic Partnership with Attentive Science to Accelerate Scientific Research Across GCC and MENA Regions

- **Date:** 2026-04-28
- **Original URL:** `https://www.innovive.com/news/innovive-expands-global-reach-through-strategic-partnership-with-attentive-science-to-accelerate-scientific-research-across-gcc-and-mena-regions`
- **Live mirror:** `https://www.wytecproductionservices.com/news/innovive-expands-global-reach-through-strategic-partnership-with-attentive-science-to-accelerate-scientific-research-across-gcc-and-mena-regions`
- **Wix record created / updated:** 2026-04-28 / 2026-04-28
- **Status:** MISSING from innovive.com
- **Featured image:** `https://static.wixstatic.com/media/9709ce_b911630ba96d4baf9a6af835e7184ff0~mv2.png` (1264x848)

**Innovive, LLC, a first-in-class innovator in single use, wash-free IVC systems and preclinical vivarium solutions, today announced the signing of a distribution and co-marketing agreement with Attentive Science Ltd., a leading life-science solutions provider headquartered in Masdar City.**

Attentive Science will serve as Innovive’s distributor and co-marketing partner throughout the GCC and broader MENA regions, including the United Arab Emirates, Saudi Arabia, Qatar, Bahrain, Oman, Kuwait, Egypt, and Jordan.

Under the agreement, Attentive Science will distribute Innovive’s full portfolio of wash-free recyclable caging systems, racks, and consumables, while also collaborating on the regional expansion of Innovive’s Inno+ vivarium services platform.

Innovive’s recyclable, disposable, IVC system eliminates the need for washrooms in laboratories, reduces capital investment, space requirements, and labor costs while enabling rapid scalability. The agreement with Attentive Science underscores Innovive’s vision of fostering global scientific advancement through strategic partnerships. As it strengthens its presence in the GCC and other international markets, Innovive remains committed to driving innovation and sustainability in research operations worldwide.

> “This partnership represents a major milestone in Innovive’s international growth strategy,” said Jamie Blose, Pharm. D, MBA, JD, Chief Executive Officer at Innovive. “Attentive Science brings deep regional expertise, regulatory knowledge, and a state-of-the-art vivarium facility that will serve as a premier demonstration site for our technology in the Middle East.”

Innovive is capturing a pivotal moment in the GCC, where significant biotech and pharmaceutical interest is driving the creation of advanced laboratory facilities and expanded research capacity. With small animal models dominating preclinical drug development, Innovive’s IVC system is engineered specifically to meet the rigorous demands of this critical research phase.

> Tareq Abu-Nadi, CEO & Co-Founder of Attentive Science, commented, “Innovive’s single-use housing technology aligns perfectly with the rapid growth of biomedical research infrastructure in the GCC and MENA region. We are proud to serve as Innovive’s regional partner and to introduce advanced, biosecure, and workflow-optimized solutions to research institutions across the region.”

This partnership strengthens Innovive’s global network while positioning Attentive Science as a key enabler of advanced vivarium infrastructure across one of the world’s fastest-growing life-science markets.

**About Attentive Science Ltd.**

Attentive Science Limited, located in Abu Dhabi’s Masdar City, is a leading life sciences enabler advancing drug development across the Middle East and globally. As the region’s first licensed preclinical contract research organization (CRO), the company delivers high-quality, GLP-compliant studies spanning toxicology, bioanalysis, biodistribution, and translational research. With a strong focus on advanced therapeutics, including cell and gene therapies and nucleic acid–based drugs. In parallel, the company has established a first-of-its-kind wet lab incubator in Masdar City, designed to accelerate the growth of biotech startups and enable rapid market entry into the region.

As part of Attentive Science Global, the Abu Dhabi operation is integrated within a broader international platform with capabilities across the United States and Australia. This multi-site model enables seamless execution of complex, globally coordinated studies while maintaining rigorous scientific and regulatory standards. By combining world-class infrastructure, strategic geographic positioning, and deep scientific expertise, Attentive Science is building a fully integrated ecosystem for drug development—reinforcing Abu Dhabi’s role as a rapidly emerging hub for life sciences innovation and investment.

---

## Innovive Expands into Latin America & Caribbean Through a New Distribution Partnership with EAD Scientific

- **Date:** 2025-04-16
- **Original URL:** `https://www.innovive.com/news/innovive-expands-into-latin-america-and-caribbean`
- **Live mirror:** `https://www.wytecproductionservices.com/news/innovive-expands-into-latin-america-and-caribbean`
- **Wix record created / updated:** 2025-04-16 / 2026-04-28
- **Status:** MISSING from innovive.com
- **Featured image:** `https://static.wixstatic.com/media/9709ce_2f14035bb93a4bcaab658cc7f1071c5a~mv2.jpg` (4290x2406)

Innovive’s recyclable, disposable IVC System eliminates the need for washrooms in laboratories, reduces capital investment, space requirements, and labor costs while enabling rapid scalability.

> ***By addressing local challenges such as limited funding and infrastructure gaps, Innovive, with the support of EAD, aims to empower researchers in the region with scalable and sustainable tools.****** ***[**Share**](https://www.linkedin.com/company/innovive/?viewAsMember=true)

This partnership with EAD Scientific is a key milestone in Innovive’s broader international growth strategy. The LAC region represents a significant opportunity for innovation due to its growing research ecosystem and increasing demand for cost-effective scientific solutions. By addressing local challenges such as limited funding and infrastructure gaps, Innovive, with the support of EAD, aims to empower researchers in the region with scalable and sustainable tools.

Innovive’s collaboration with EAD Scientific underscores its vision of fostering global scientific advancement through strategic partnerships. As it strengthens its presence in LAC and other international markets, Innovive remains committed to driving innovation and sustainability in research operations worldwide.

“We are thrilled to partner with EAD Scientific to expand Innovive’s reach across Latin America and the Caribbean,” said Sarah Anderson-Jenkins, Vice President of Sales at Innovive. “As a partner with strong regional expertise, EAD will help deliver our research-ready solutions to more scientists while reducing capital expenditure, simplifying operations, and accelerating science."

EAD Scientific is a company committed to offering high-quality laboratory products that meet the specific needs of each customer, making it a trusted partner in the scientific industry worldwide.

"

We are very excited about the agreement signed with Innovive. The equipment they manufacture, combined with the favorable recyclable use they offer, aligns well with the market in Latin America and the Caribbean where funding resources are still not very high,” commented Enrique Aguinaga, CEO of EAD Scientific. Aguinaga emphasized that he is always seeking strategic partners who share his passion for innovation and positive impact. "Innovive has proven to be a reliable and visionary ally, and we are excited about the potential of this collaboration to amplify our presence and achieve new goals in the region,” Aguinaga added.

Customers in the region can begin sourcing Innovive products through EAD Scientific immediately. For distributor inquiries or product information in Latin America and the Caribbean, visit [**innovive.com/contact**](http://innovive.com/contact).

**About Innovive**

Founded in 2004, Innovive is recognized as a ground-breaking leader in the development of disposable, recyclable caging for research vivariums. The company provides a comprehensive solution for the global research community, including exceptional vivarium support and management services. Headquartered in San Diego, CA, Innovive’s patented disposable IVC System significantly accelerates the path to scientific discovery by eliminating cage washing and allowing customers to optimize their resources -- saving time, space, capital, and labor. Additionally, the company uses sustainability principles in the manufacturing, distribution, use, and disposal of its products. For more information about Innovive and its products, visit [**www.innovive.com**](http://www.innovive.com).

**About EAD Scientific**

EAD Scientific is a U.S.-based scientific laboratory distribution company with a special focus on Latin America. It is part of A&C Group, a group of companies dedicated to supporting scientists and collaborating to solve complex challenges in biotechnology, pharmaceutical, academic, governmental, industrial, clinical, and environmental research. For more information about EAD Scientific and its distribution services, visit [**www.eadscience.com**](http://www.eadscience.com).

**Links in body:**

- `http://innovive.com/contact`
- `http://www.eadscience.com`
- `http://www.innovive.com`
- `https://www.linkedin.com/company/innovive/?viewAsMember=true`

---

## Innovive, LLC Appoints Jamie S. Blose, Pharm.D, MBA, JD as Chief Executive Officer

- **Date:** 2024-10-31
- **Original URL:** `https://www.innovive.com/news/new-chief-executive-officer`
- **Live mirror:** `https://www.wytecproductionservices.com/news/new-chief-executive-officer`
- **Wix record created / updated:** 2025-04-16 / 2026-04-28
- **Status:** MISSING from innovive.com
- **Featured image:** `https://static.wixstatic.com/media/9709ce_befe7aba60344ebbbff13be03a271ed2~mv2.png` (2684x1257)

**Innovive, LLC, a pioneer and leader in disposable caging and preclinical research solutions, today announced a change in executive leadership with the appointment of Jamie S. Blose, Pharm.D., MBA, JD, as Chief Executive Officer.**

As a life science executive, Dr. Blose has over 30 years of global experience in the biopharmaceutical industry, bringing a wealth of expertise in preclinical and clinical drug and medical device development, commercialization, and strategic acquisitions and partnerships.

“We are thrilled to have Jamie lead Innovive during the company’s next pivotal growth phase,” said Dee Conger, Innovive’s Founder and Chairman of the Board. “Jamie has a proven track record of scaling successful biopharma companies, and her experience and leadership align perfectly with Innovive’s corporate mission. Jamie’s powerful combination of drug and medical device development knowledge, along with her financial and legal acumen, will help drive our innovation and growth to continue serving the research industry.”

Dr. Blose earned her Doctor of Pharmacy degree from the University of Arizona, her international MBA from Thunderbird, her post-doctoral fellowship in drug development at the University of North Carolina, and her Juris Doctor degree from the University of San Diego School of Law. Dr. Blose is both a licensed pharmacist and a licensed attorney.

“Joining Innovive is an exciting opportunity to work with an exceptionally talented team in transforming how preclinical research is done,” commented Dr. Blose. “Together, we will continue to provide comprehensive support for the research community while expanding our global reach.”

In April, Dr. Blose joined Innovive as the Chief Business Officer. Prior to joining Innovive, she served in leadership positions at both public and private companies including Rain Oncology, Genentech, Amylin Pharmaceuticals, NovaQuest, Quintiles and Glaxo Wellcome. She has also served on various advisory boards, steering committees, and as legal counsel and an advisor to entrepreneurs and start-up companies. Her notable career includes extensive international experience and a commitment to driving innovation and optimization at critical junctures in a company’s evolution.

**About Innovive**

Founded in 2004, Innovive is recognized as a ground-breaking leader in the development of disposable, recyclable caging for research vivariums. The company provides a comprehensive solution for the global research community, including exceptional vivarium support and management services. Headquartered in San Diego, CA, Innovive’s patented Research-Ready disposable IVC System significantly accelerates the path to scientific discovery by eliminating cage washing and allowing customers to optimize their resources -- saving time, space, capital, and labor. Additionally, the company uses sustainability principles in the manufacturing, distribution, use, and disposal of its products. To learn more about Innovive’s unique products and breadth of services, visit [**innovive.com**](http://innovive.com).

**Links in body:**

- `http://innovive.com`

---

## Innovive Announces Strategic Partnership With Dr. Marcel Perret-Gentil of PLAVS to Enhance and Expand Innovive+ Vivarium Services in the US, Globally

- **Date:** 2024-08-12
- **Original URL:** `https://www.innovive.com/news/strategic-partnership-with-dr-marcel-perret-gentil`
- **Live mirror:** `https://www.wytecproductionservices.com/news/strategic-partnership-with-dr-marcel-perret-gentil`
- **Wix record created / updated:** 2025-04-16 / 2026-04-28
- **Status:** MISSING from innovive.com
- **Featured image:** `https://static.wixstatic.com/media/829070_b23c8481e66c4d23b1371a9f4ff05951~mv2.jpg` (490x345)

**Innovive, LLC is proud to announce a strategic partnership with Dr. Marcel Perret-Gentil, the founder and President of Perret-Gentil Laboratory Animal Veterinary Services (PLAVS).**

This collaboration will significantly expand and enhance Innovive+ Vivarium Services across the United States, Central America, and South America.

> ***We're thrilled that PLAVS's extensive range of services will greatly enhance the support we offer to our clients worldwide. This collaboration enables us to provide a more integrated and thorough approach to laboratory animal care and facility management.****** ***[**Share**](https://www.linkedin.com/company/innovive/?viewAsMember=true)

"We're excited about our partnership with PLAVS," said Sarah Anderson-Jenkins, Vice President of Sales and Marketing at Innovive. "PLAVS's extensive range of services, including but not limited to facility design, attending veterinarian services, IACUC services, and AAALAC international accreditation preparation, will greatly enhance the support we offer to our clients across the globe. This collaboration enables us to provide a more integrated and thorough approach to laboratory animal care and facility management."

Innovive+ Vivarium Services combine the benefits and convenience of the Innovive IVC racking and disposable caging products with year-round in-facility animal care. Innovive offers tailored support to further clients' scientific discovery, relieving them of the operational burden and allowing researchers to focus on delivering their mission—the science.

"Joining forces with Innovive is a significant step forward for PLAVS," said Dr. Marcel Perret-Gentil. "This partnership allows us to leverage Innovive's cutting-edge technology with PLAVS comprehensive support services, providing our clients unparalleled care and facility management solutions. Together, we are well-positioned to meet the research community's evolving needs and drive scientific advancements."

**About Innovive**

Founded in 2004, Innovive, LLC is an industry leader serving the global laboratory research market by providing innovative animal racking, disposable caging, and support services. Innovive enables accelerated science by eliminating the stress and complexity of a washroom. Innovive’s technology allows for fast scalability of research operations while reducing capital expenditures, space requirements, and labor. Innovive is proud of its superior customer service, reliable and vetted supply chains, and its reduced dependency on third parties by utilizing established partnerships with Innocycle (for recycling) and NextBeam (for sterilization). The company applies sustainability principles in the manufacturing, distribution, use, and disposal of its products. To learn more about the unique products and breadth of services, visit [**innovive.com**](http://innovive.com).

**Links in body:**

- `http://innovive.com`
- `https://www.linkedin.com/company/innovive/?viewAsMember=true`

---

## PET rodent cage processor recycled 1.2M pounds in 2023

- **Date:** 2024-02-01
- **Original URL:** `https://www.innovive.com/news/pet-rodent-cage-processor-recycled`
- **Live mirror:** `https://www.wytecproductionservices.com/news/pet-rodent-cage-processor-recycled`
- **Wix record created / updated:** 2025-04-16 / 2026-04-28
- **Status:** MISSING from innovive.com
- **Featured image:** `https://static.wixstatic.com/media/9709ce_e3772f39d0c04ece978ddb9639618aa0~mv2.jpg` (3300x2550)

**Innovive processed 1.2 million pounds of PET in 2023, up from 1.1 million pounds the prior year.**

Innovive, a U.S. manufacturer of single-use plastic cages for mice and rats in laboratories, has scaled up its recycling operations in recent years, nearly doubling its annual processing capacity since 2020 and building an in-house reclamation center in Sacramento, California.

The San Diego-headquartered company, which launched in 2004, makes rodent cages – known as vivariums or individually ventilated cages (IVCs) more technically – for use by a variety of research operations and similar customers. The cages are made from PET, with the bedding inside made from organic material. Innovive, which has offered recycling for its products since its inception, operates a sister company, Innocycle, that collects and recycles used cages from customer facilities.

Innovive’s recycling efforts have been increasing each year: The company processed 1.2 million pounds of PET in 2023, up from 1.1 million pounds the prior year. The company [announced](https://www.businesswire.com/news/home/20240130564780/en/Celebrating-Innocycle%E2%80%99s-Environmental-Milestones-Closed-Loop-Recycling-Service-Makes-Significant-Impact) the latest numbers on Jan. 30.

Much of the growth has come in the last few years – Innovive nearly doubled its processing volume since 2020 and increased by 48% in one year alone, from 2021 to 2022, when the company opened a dedicated Sacramento reclamation facility. Prior to developing its own reclamation plant, the company operated a smaller prototype processing line and partnered with other companies to scale up its recycling capabilities.

The new facility and expanded processing capacity [received a boost](https://resource-recycling.com/plastics/2021/04/21/california-provides-funding-to-boost-thermoform-recycling/) from grant funds awarded by the California Department of Resources Recycling and Recovery (CalRecycle). In awarding the grant, CalRecycle noted Innovive’s project “will expand existing recycling to 75% of cages sold in California.”

The facility totals 30,000 square feet and has a current capacity to process 8 million pounds of PET per year, a company spokesperson told Plastics Recycling Update. 

Customers participating in the recycling program are asked to stack used cages and aggregate them in their original bags, and an Innocycle truck will come to collect them. The bags are delivered to Innocycle’s reclamation plant.

There, the bedding is separated from the cages, which are then shredded and washed to produce recycled PET flake. The bedding, meanwhile, is sent to an industrial composter.

The facility uses plastics and organics separation equipment from Scott Equipment, flake processing and cleaning machinery from Lindner, and a flake optical sorting system from Tomra.

Nearly all the recycled flake output is sent to a network of vendors who produce Innovive’s products. Innovive uses recycled PET flake from recycled cages at levels of more than 30% recycled content in its new products, and it also uses RPET purchased from other suppliers.

**Links in body:**

- `https://resource-recycling.com/plastics/2021/04/21/california-provides-funding-to-boost-thermoform-recycling/`
- `https://www.businesswire.com/news/home/20240130564780/en/Celebrating-Innocycle%E2%80%99s-Environmental-Milestones-Closed-Loop-Recycling-Service-Makes-Significant-Impact`

---

## Celebrating Innocycle’s Environmental Milestones: Closed-Loop Recycling Service Makes Significant Impact

- **Date:** 2024-01-30
- **Original URL:** `https://www.innovive.com/news/major-environmental-milestones`
- **Live mirror:** `https://www.wytecproductionservices.com/news/major-environmental-milestones`
- **Wix record created / updated:** 2025-04-16 / 2026-04-28
- **Status:** MISSING from innovive.com
- **Featured image:** `https://static.wixstatic.com/media/9709ce_ff543b97074f46c595d3ad22f21c27e4~mv2.jpg` (4032x3024)

**Innovive is proud to announce major environmental milestones achieved by the Closed-Loop Recycling program operated by its sister company, Innocycle.**

From January 2022 through December 2023, the program has made significant contributions to environmental sustainability, including recycling 2.3 million pounds of plastic, diverting 5.7 million pounds of bedding, and reducing 1,720.95 metric tons of CO2 equivalent emissions.

"I am humbled to be part of a company committed to taking the time, effort, and investment necessary to develop a truly circular product," said Jeremy Jenson, Sr. Sustainability and Circularity Manager. "With the support of our customers and an industry committed to reducing its environmental impact, the Closed-Loop Recycling program has achieved remarkable results."

The Closed-Loop Recycling Service allows customers to keep their operations simple, safe, and science-focused. It eliminates the burden and risk of cage dumping and processing at customer facilities. Innovive has maintained a recycling program from its inception. In 2022, Innovive expanded its recycling capacity by opening the Innocycle facility, which is dedicated to producing the highest quality recycled PET flake and focuses on closing the loop.

When the cages arrive, recycling technology separates bedding from the cages, then granulates, washes, and sorts the plastic. This produces a high-quality, clean flake to form new cages. Innovive is the first vivarium manufacturer in the U.S. to implement product-to-product circularity, with more than 30% of the reclaimed PET plastic used to create new cages. Innocycle collects, sorts, and sends all packaging material for additional recycling while sending the bedding to an industrial composting facility, where it is processed into a nitrogen and carbon-rich soil amendment.

"From inception, Innovive has focused on reducing the environmental impact of our products and operations. We apply sustainable practice in everything we do, from the engineering, production, and packaging to delivery of our products to your vivarium," said Dee Conger, CEO of Innovive.

**About Innovive**

Innovive is a recognized leader in disposable rodent housing since 2004. It provides the only simple, full-cycle clean environment for accelerated science without the stress and complexity of a washroom, with more than 500 installations worldwide. Innovive's patented technology allows fast scalability of research operations while freeing capital funding, time, space, labor, utilities, and other valuable resources. Innovive is committed to serving customers, ensuring the highest quality of products through a reliable and vetted supply chain, and applying sustainability principles in the manufacturing, distribution, use, and disposal of plastic material.

---

## Innovive Consolidating Product Support Services and Vivarium Management Solutions Under Innovive+

- **Date:** 2023-02-06
- **Original URL:** `https://www.innovive.com/news/product-support-services-and-vivarium-management-solutions`
- **Live mirror:** `https://www.wytecproductionservices.com/news/product-support-services-and-vivarium-management-solutions`
- **Wix record created / updated:** 2025-04-16 / 2026-04-28
- **Status:** MISSING from innovive.com
- **Featured image:** `https://static.wixstatic.com/media/9709ce_38a0b7922ec748cfb796fc137144f0a4~mv2.jpg` (7680x5120)

**Innovive consolidates product support services and vivarium management solutions under Innovive+.**

Innovive is pleased to announce the consolidation of its current product support services and the expansion of comprehensive vivarium solutions into a single platform - Innovive+.

"We are thrilled to offer Innovive+ to our existing and future clients,” said Dee Conger, CEO of Innovive. “In today's world, scientific research cannot be slowed down by the operational and financial challenges that research facilities increasingly face. When it comes to drug discovery, time is of the essence. Innovive+ is an extension of the Innovive IVC technology and offers tailored solutions that help researchers focus on delivering their mission by taking non-core work off their plate."

Innovive+ combines the benefits and convenience of the standardized Innovive rodent racking and caging products with in-facility animal care. Our industry-leading management team has more than 20 years of experience working hand-in-hand with clients in their facilities. This expansion allows Innovive's customers to further their scientific discovery by maximizing the use of Innovive’s high-performance technology with comprehensive in-facility support. Innovive+ offers inventory management, equipment maintenance, husbandry, vivarium management, and technical and scientific solutions to accommodate clients' research needs allowing them to scale easily as their research grows.

“Our expanded services are a direct response to the need of customers to prioritize their scientific discovery work. It is a natural extension of our internal capabilities and will allow Innovive to shoulder an increasing share of the vivarium burden at our client sites while enabling our customers to focus on their most value-added activity, their science,” said Conger.

**About Innovive**

Innovive LLC is a recognized leader in disposable rodent housing. It provides the only simple, full-cycle clean environment for accelerated science without the stress and complexity of a washroom since 2004, with more than 500 installations worldwide. Innovive's patented technology allows fast scalability of research operations while freeing capital funding, time, space, labor, utilities, and other valuable resources. Innovive is committed to serving customers, ensuring the highest quality of products through a reliable and vetted supply chain, and applying sustainability principles in the manufacturing, distribution, use, and disposal of plastic material. Learn more at [**innovive.com**](http://innovive.com).

**Links in body:**

- `http://innovive.com`

---

# Full text: Tier 2, legacy pre-Wix press releases

Fourteen releases, newest first. Source: Wayback Machine snapshot of `innovive.com/company/news.html` taken
2020-06-21, the last capture before that page disappeared. Full text, not the teaser.

Snapshot URL: `http://web.archive.org/web/20200621104917/http://www.innovive.com/company/news.html`

## Innovive Announces Expansion into South Dakota

- **Date:** 2020-05-29 (dateline: May 29, 2020 | North Sioux City, South Dakota)
- **Original URL:** `http://www.innovive.com/company/news.html#siouxcity`
- **Status:** MISSING from innovive.com, lost at the pre-2024 rebuild
- **Images:** none

Innovive LLC (www.innovive.com), a U.S.-based technology company, and a leader in disposable IVC rodent caging systems, is excited to announce that it will be expanding its manufacturing processes into North Sioux City, South
Dakota, with their recent purchase of a 367,000 SF advanced manufacturing and distribution center.

The building, one of five that comprised the former Gateway Computer Campus, was initially purchased by investor Gerard Keating in 2018 who repositioned the campus and turned it into one of the largest industrial properties in the State of South Dakota.

The reasons that factored into purchasing the center were many, says company founder and CEO Dee Conger, but ultimately it was the ability to access a quality workforce with experience in automation in a production environment.

“Over the course of the next two to three year, we will be looking to hire approximately 150 new employees,” says Conger. “And knowing that the area has experienced workers available, has been a big selling feature.”

 

Other factors that influenced the company’s decision to expand into South Dakota include: the building’s central location within the U.S.; the low cost of energy to run a manufacturing operation; and the overall favourable business climate for manufacturing operations the area offers. The opportunity to purchase a repurposed building also fit well into the company’s overall culture of sustainability and commitment to reducing the environmental impact of their
 products and operations.

 
 About Innovive: Innovive was founded in 2004 with the goal of radically transforming the economics and convenience of working with laboratory animals. 
Using advanced design and manufacturing processes, Innovive creates reliable disposable rodent caging systems to provide research facilities with superior quality, performance, and cost savings. Our products are independently tested and validated to assure trouble-free operation, and our global manufacturing and distribution network provides advantageous pricing and rapid order fulfillment.

---

## Innovive Moves East Coast Facility to Billerica, Massachusetts

- **Date:** 2018-06-27 (dateline: June 27, 2018 | San Diego, CA)
- **Original URL:** `http://www.innovive.com/company/news.html#billerica`
- **Status:** MISSING from innovive.com, lost at the pre-2024 rebuild
- **Image:** `http://www.innovive.com/images/company/contact-us/innovive-east-coast-small.jpg` (404 live, retrievable via `http://web.archive.org/web/2019id_/http://www.innovive.com/images/company/contact-us/innovive-east-coast-small.jpg`)

We are happy to announce that our East Coast facility will be operating from our new location in Billerica, Massachusetts. This newly renovated 68,000 sq. ft. building will serve as our East Coast headquarters going forward.

The prime location along the Route 128 corridor will allow us to deliver and service the Boston and Cambridge regions quicker and more efficiently.

This is an exciting expansion for us and we are looking forward to being in close proximity to Boston's emerging biotech market while continuing to providing the service you have come to expect from Innovive.

About Innovive: Innovive was founded in 2004 with the goal of radically transforming the economics and convenience of working with laboratory animals. 
Using advanced design and manufacturing processes, Innovive creates reliable disposable rodent caging systems to provide research facilities with superior quality, performance, and cost savings. Our products are independently tested and validated to assure trouble-free operation, and our global manufacturing and distribution network provides advantageous pricing and rapid order fulfillment.

---

## Innovive Grants Limited License for Allentown Disposable Caging

- **Date:** 2018-04-17 (dateline: April 17, 2018 | San Diego, CA)
- **Original URL:** `http://www.innovive.com/company/news.html#allentown-disposable-cages`
- **Status:** MISSING from innovive.com, lost at the pre-2024 rebuild
- **Images:** none

Innovive, an innovator in disposable rodent caging, is pleased to announce that it has issued a limited non-exclusive license to Allentown, Inc. This license will allow Allentown to continue development of Allentown disposable caging products for use in their rear-ventilated racks.

“We are pleased that Allentown has chosen to honor our significant intellectual property around disposable rodent caging systems, and secured this license. Disposable caging is the future of our industry, and we view this license as a strong endorsement of this fact,” said Dee Conger, CEO of Innovive.

 Innovive invented, patented, and brought to market the world’s first commercial disposable rodent caging system. Since 2004, Innovive has been issued 31 U.S. and International patents, and is at the forefront of the industry standards for disposable caging. Innovive ships more than one million cages per month to more than 475 companies in 28 countries, enabling customers to focus on science and curing diseases instead of non-value added cage washing.

About Innovive: Innovive was founded in 2004 with the goal of radically transforming the economics and convenience of working with laboratory animals. 
Using advanced design and manufacturing processes, Innovive creates reliable disposable rodent caging systems to provide research facilities with superior quality, performance, and cost savings. Our products are independently tested and validated to assure trouble-free operation, and our global manufacturing and distribution network provides advantageous pricing and rapid order fulfillment.

---

## Innovive and Lou Ristic are Recognized for Excellence

- **Date:** 2017-09-14 (dateline: September 14, 2017 | San Diego, CA)
- **Original URL:** `http://www.innovive.com/company/news.html#excellence-award`
- **Status:** MISSING from innovive.com, lost at the pre-2024 rebuild
- **Image:** `http://www.innovive.com/images/company/news/LouAward.jpg` (404 live, retrievable via `http://web.archive.org/web/2019id_/http://www.innovive.com/images/company/news/LouAward.jpg`)

On Thursday night at the 2017 NEBAALAS Annual Award and Installation Meeting, Innovive and Northeastern Sales Representative Lou Ristic were presented with the "Robert Kydd Vendor Excellence Award for Dedication to The Field of Laboratory Animal Science and Technology." The award was presented by The New England Branch of the American Association for Laboratory Animal Science and is the first ever awarded Vendor Excellence Award in their history. 

 
 Upon receiving the award, Lou Ristic said, “It is with great pride that I accept this great achievement for myself and Innovive.”

 

 
About Innovive: Innovive was founded in 2004 with the goal of radically transforming the economics and convenience of working with laboratory animals. 
Using advanced design and manufacturing processes, Innovive creates reliable disposable rodent caging systems to provide research facilities with superior quality, performance, and cost savings. Our products are independently tested and validated to assure trouble-free operation, and our global manufacturing and distribution network provides advantageous pricing and rapid order fulfillment.

---

## Innovive Doubles Pre-Bedded Caging Throughput

- **Date:** 2017-08-03 (dateline: August 3, 2017 | San Diego, CA)
- **Original URL:** `http://www.innovive.com/company/news.html#doubling-bedding-line`
- **Status:** MISSING from innovive.com, lost at the pre-2024 rebuild
- **Images:** none

Innovive has put the final updates to a new state-of-the-art cage bedding system, located in our headquarter facility in San Diego, CA. This system, along with the addition of the soon-to-be-completed enhanced water bottle filling system, is part of a continuous effort to invest and focus on the premium quality of our optional services for our customers.

“The new bedding filling system we’ve custom-built allows us to effectively double our throughput, and help meet the growing demand that we have for pre-bedded cages,” says Vice President of Engineering, Paul Jackson. “We’ve also added in multiple air filtration systems to evacuate airborne dust and contaminants to not only deliver a better product to our customers, but a cleaner, safer working environment for our staff.”

The bedding filling system now has two individual operating assembly lines, and each one can pre-bed approximately up to 3,000 Innocages® per hour. Each assembly line can also compile up to four separate stacks of 25 pre-bedded Innocages® simultaneously, before they are bagged and sent to be fully irradiated. Automated product packaging, as well as Innorichment™ insertion, are scheduled to be implemented later this year.

The construction of the streamlined water filling system is currently being fine-tuned and is expected to be completed by the end of November 2017.

About Innovive: Innovive was founded in 2004 with the goal of radically transforming the economics and convenience of working with laboratory animals. 
Using advanced design and manufacturing processes, Innovive creates reliable disposable rodent caging systems to provide research facilities with superior quality, performance, and cost savings. Our products are independently tested and validated to assure trouble-free operation, and our global manufacturing and distribution network provides advantageous pricing and rapid order fulfillment.

---

## Emmanuel Ferton Joins Innovive as Director of Manufacturing Operations

- **Date:** 2017-07-07 (dateline: July 7, 2017 | San Diego, CA)
- **Original URL:** `http://www.innovive.com/company/news.html#ferton-hiring`
- **Status:** MISSING from innovive.com, lost at the pre-2024 rebuild
- **Images:** none

Innovive, the leader in disposable IVC rodent caging, today announced that Emmanuel Ferton has joined the company as Director of Manufacturing Operations.

 Ferton will lead the company’s direction, strategy and execution for manufacturing operations of both new and existing products. He will also optimize demand planning, sourcing and purchasing to hold internal product line operations and external vendors to their production plan commitment.

 
 “I am very happy to join Innovive,” said Ferton. “I really value the technology disruption driven by Innovive and I will lead operations towards excellence in quality and in customer experience. Innovive promotes great working values and I am excited to be a part of this talented team.”

 
 Ferton brings with him over 20 years in Supply Chain and Operations Management experience. Ferton has 11 years of experience as a Supply Chain Director at Soitec Solar Industries LLC., leading an international team covering supply planning, services procurement, logistics and transportation management, Customs, and Trade compliance. At Hewlett Packard in his native country France, Ferton held the position of Logistics Operations Manager for 6 years before being promoted to Supply Chain Development Program Manager where he managed the supply chain corporate programs as well as outsourcing and offshoring strategy.

 
“We are excited to have Emmanuel join our team,” said CEO Dee Conger. “He will play an integral role at Innovive, working together with our engineering and manufacturing departments as well as our vendors to ensure that our line of products are of the utmost highest quality. With his vast expertise, we are confident that he will help deliver the best premium experience of our products to our customers.”

 Ferton will be based out of the headquarters of Innovive in San Diego, California.

About Innovive: Innovive was founded in 2004 with the goal of radically transforming the economics and convenience of working with laboratory animals. 
Using advanced design and manufacturing processes, Innovive creates reliable disposable rodent caging systems to provide research facilities with superior quality, performance, and cost savings. Our products are independently tested and validated to assure trouble-free operation, and our global manufacturing and distribution network provides advantageous pricing and rapid order fulfillment.

---

## Innovive Purchases New Corporate Headquarters in San Diego, CA

- **Date:** 2015-12-17 (dateline: December 17, 2015 | San Diego, CA)
- **Original URL:** `http://www.innovive.com/company/news.html#headquarters-2015-move`
- **Status:** MISSING from innovive.com, lost at the pre-2024 rebuild
- **Images:** none

Innovive, the leader in disposable IVC rodent caging serving the biomedical research market, has invested in a new corporate headquarters in San Diego, California. The 50,000 square foot facility contains expanded Manufacturing, Customer Service, Sales, Marketing, and Engineering departments. The site also houses an improved and streamlined distribution and warehouse operation for the Western U.S. and Asian markets as well as a Quality Control laboratory.

Over the next six months, Innovive will make a significant investment in this new location including installation of its proprietary high-throughput water bottling and cage bedding operation which will be housed in an 8,000 square foot addition. Upgraded biosecurity measures will be implemented to ensure that these processes are undertaken in a completely clean environment. In addition, the new facility will also house a state-of-the-art vivarium to allow thorough internal validation of our products before they are released. "We’ve spared no expense in investing in our facility, equipment, and personnel to continue delivering high quality products that our consumers have come to expect from us," says Dee Conger, CEO of Innovive.

About Innovive: Innovive was founded in 2004 with the goal of radically transforming the economics and convenience of working with laboratory animals. 
Using advanced design and manufacturing processes, Innovive creates reliable disposable rodent caging systems to provide research facilities with superior quality, performance, and cost savings. Our products are independently tested and validated to assure trouble-free operation, and our global manufacturing and distribution network provides advantageous pricing and rapid order fulfillment.

---

## Pfizer’s Stephen Baker Joins Innovive

- **Date:** 2015-08-25 (dateline: August 25, 2015 | San Diego, CA)
- **Original URL:** `http://www.innovive.com/company/news.html#pfizer-baker-joins-innovive`
- **Status:** MISSING from innovive.com, lost at the pre-2024 rebuild
- **Images:** none

Innovive, the leader in disposable IVC rodent caging, today announced that Stephen Baker has joined the company as Vice President of Business Development.

Baker joins Innovive from Pfizer Inc where he served as a Senior Manager with the Global Standardization and Business Resources Team for Comparative Medicine. Previous to Pfizer, Baker was employed by Genzyme / Sanofi where he served as the Director of Operations for the Department of Comparative Medicine.

Baker’s new role at Innovive will include supporting customers with best practices for implementing the Innovive Disposable Caging System, as well as helping users to develop the most efficient Standard Operating Procedures and protocols to maximize workflow. He will also partner with clients to ensure new products and services meet expectations, improve animal welfare and support research.

“Innovive is the future of lab animal research – the portability of science,” said Baker. “I truly believe in the product, allowing users to be flexible, sustainable, operate outside-of-the-box and shift away from conventional vivariums. I am thrilled and excited to join Innovive’s team. In this world of constant change, I look forward to offering my knowledge of facility operations coupled with my strong background in facility design and renovation to help implement change in other institutions.”

Baker holds a Bachelor of Science from Boston College and a Masters of Science from Emmanuel College. He has his Project Management Professional (PMP) certification and Accelerating Implementation Methodology (AIM) certification. He is a certified manager of animal resources (CMAR) and a registered laboratory animal technologist (RLATG) through the American Association for Laboratory Animal Science (AALAS). Baker is also a graduate and faculty member of the Institute for Laboratory Animal Management (ILAM). Currently, Baker serves on the Board of Directors for the Laboratory Animal Management Association (LAMA) and is a co-chair for the Continuing Education & Training committee. In addition to his experiences and certifications in the field of laboratory animal science, he is a certified somatic leadership coach and enjoys growing the leaders of tomorrow. 

“We’re thrilled to have Steve join our team. During his tenure at Pfizer he researched and vetted every facet of the Innovive Disposable Caging System to ensure it could achieve Pfizer’s high standards of operation,” said Innovive CEO, Dee L. Conger. “With his vast expertise in the industry and his deep knowledge of our products, we are confident he will be able to help animal research facilities of any size or type successfully implement our caging technology.”

Baker will be based out of the East Coast Corporate Office of Innovive in Hudson, New Hampshire. 

About Innovive: Innovive was founded in 2004 with the goal of radically transforming the economics and convenience of working with laboratory animals. 
Using advanced design and manufacturing processes, Innovive creates reliable disposable rodent caging systems to provide research facilities with superior quality, performance, and cost savings. Our products are independently tested and validated to assure trouble-free operation, and our global manufacturing and distribution network provides advantageous pricing and rapid order fulfillment.

---

## Innovive Opens East Coast Corporate Office and Distribution Center in New Hampshire

- **Date:** 2013-07-10 (dateline: July 10, 2013 | Boston, MA)
- **Original URL:** `http://www.innovive.com/company/news.html#hudson-open`
- **Status:** MISSING from innovive.com, lost at the pre-2024 rebuild
- **Image:** `http://www.innovive.com/EM/2013/06/front-angled-no-sign.jpg` (404 live, retrievable via `http://web.archive.org/web/2019id_/http://www.innovive.com/EM/2013/06/front-angled-no-sign.jpg`)

Innovive, the leader in disposable IVC rodent caging serving the biomedical research market, has opened a new corporate office and distribution center in Hudson, New Hampshire. The 20,000 square foot facility, previously occupied by ThermoFisher Scientific, is located in close proximity to the Greater Boston Area, one of the largest biomedical research centers in the world. The new site will serve as the company's East Coast office for customer service, sales, and supply chain logistics. It will also house the distribution and warehouse operation for the Eastern U.S. and all of Europe. The company's product development efforts will continue to be based in their West Coast headquarters in San Diego, CA, which will also retain customer service, sales, and distribution staff to serve the Western U.S. and Asian markets.

Innovive's COO, Jim Fallon, has relocated to New Hampshire to lead the new office. "Our strong, steady growth and expanding global customer footprint – especially during these uncertain times – are a testimony to our value proposition, our customer relationships and our dedicated staff," says Fallon. "All customers in the Greater Boston Area will benefit from the convenience of Innovive operating in the Eastern Time Zone, the security of local inventory in the new warehouse, and deliveries made by Innovive staff using the company's own fleet of trucks."

Innovive's Director of Customer Service Operations, Jessie Shea, has also relocated to the new location to provide dedicated support to East Coast customers. "We're excited to be focusing our efforts and resources on the Eastern region," says Dee Conger, CEO of Innovive. "Our success has been built not only on bringing new technology to the industry, but also on the closeness of our customer relationships. The added ability for us to provide local, on-demand deliveries and services throughout the East Coast will help to solidify our presence in the region and allow us to better serve our substantial and rapidly growing client base."

About Innovive: Innovive was founded in 2004 with the goal of radically transforming the economics and convenience of working with laboratory animals. 
Using advanced design and manufacturing processes, Innovive creates reliable disposable rodent caging systems to provide research facilities with superior quality, performance, and cost savings. Our products are independently tested and validated to assure trouble-free operation, and our global manufacturing and distribution network provides advantageous pricing and rapid order fulfillment.

---

## Innovive Strengthens Nationwide Recycling Program with New Bay Area Recycling Facility

- **Date:** 2013-05-30 (dateline: May 30, 2013 | San Diego, CA)
- **Original URL:** `http://www.innovive.com/company/news.html#bayarea`
- **Status:** MISSING from innovive.com, lost at the pre-2024 rebuild
- **Images:** none

Innovive, the leader in disposable IVC rodent caging, is pleased to announce the opening of a new cage recycling and processing facility in Newark, California. This expansion will strengthen Innovive’s award-winning, nationwide recycling program by increasing its current recycling capacity to an additional two million cages annually. The new facility will provide customized direct pickup services to research facilities across the San Francisco Bay Area.

Over the next twelve months, Innovive will invest more than $500,000 in this new location for the installation of its proprietary separation and granulation equipment. Using this technology, Innovive is able to process dirty cages that are picked up from facilities so that customers do not have to dump or separate soiled bedding. The resulting PET flake is then cleaned and used by its vendor network to be repurposed in new products. This unique process is the industry’s only closed-loop recycling program.

“We are excited about the expansion of our recycling capabilities,” said COO Jim Fallon. “This new facility doubles our processing capacity and is a direct result of the continued growth of Innovive disposable caging and the demand for our recycling services. We are committed to providing sustainable services to our customers, allowing them to conveniently recycle and compost dirty caging while reducing their environmental impact.”

This new facility is part of Innovive's ongoing expansion plan, which will include the opening of a dedicated processing center in the northeast region in 2014.

About Innovive: Innovive was founded in 2004 with the goal of radically transforming the economics and convenience of working with laboratory animals. 
Using advanced design and manufacturing processes, Innovive creates reliable disposable rodent caging systems to provide research facilities with superior quality, performance, and cost savings. Our products are independently tested and validated to assure trouble-free operation, and our global manufacturing and distribution network provides advantageous pricing and rapid order fulfillment.

---

## Innovive Named Winner of the Waste Reduction Awards Program (WRAP) by the California Department of Resources Recycling and Recovery

- **Date:** 2011-12-29 (dateline: December 29, 2011 | San Diego, CA)
- **Original URL:** `http://www.innovive.com/company/news.html#wrap`
- **Status:** MISSING from innovive.com, lost at the pre-2024 rebuild
- **Images:** none

The California 2011 Waste Reduction Awards Program (WRAP) recognized Innovive for the company's commitment to recycling and waste reduction. WRAP, administered by the California Department of Resources Recycling and Recovery, honors California businesses and non-profit organizations for significant achievements in landfill waste diversion.

The program recognized Innovive's contribution to sustainable business development. In the course of implementing the Material Consumption and Waste Reduction Program, the company redesigned the manufacturing process at the San Diego manufacturing facility. This process optimization resulted in a 50% cutback of used materials and produced waste.

 
Innovive also pioneered a closed-loop recycling service program, assuming full responsibility for its product at every stage of the production cycle. Used disposable caging is collected directly from customer sites and returned to Innovive's San Diego recycling facility for composting and recycling. Since December 2010, 56,800 lbs of plastic have been diverted from landfills and 91,200 lbs of soiled bedding have been composted at the local municipal facility.

About Innovive: Innovive was founded in 2004 with the goal of radically transforming the economics and convenience of working with laboratory animals. 
Using advanced computer-aided design and manufacturing processes, Innovive creates reliable disposable rodent caging systems to provide research facilities with superior quality, performance, and cost savings. Our products are independently tested and validated to assure trouble-free operation, and our global manufacturing and distribution network provides advantageous pricing and rapid order fulfillment.

---

## Innovive Receives 2011 Recycler of the Year Award by San Diego 19th Waste Reduction and Recycling Program

- **Date:** 2011-04-21 (dateline: April 21, 2011 | San Diego, CA)
- **Original URL:** `http://www.innovive.com/company/news.html#recycler`
- **Status:** MISSING from innovive.com, lost at the pre-2024 rebuild
- **Images:** none

Each year, the City of San Diego's Environmental Services Department recognizes the waste reduction and diversion achievements of local businesses with its Waste Reduction and Recycling Awards Program. The awards recognize companies that have committed to reducing the amount of business-produced waste and ensuring that as much waste as possible is recycled or composted as an alternative to landfilling.

Innovive, a San Diego based manufacturer of racking systems and single use plastics to the biomedical research community, is delighted to be recognized with this award for their commitment to waste reduction. Innovive tackled this responsibility on two fronts; first by reducing the amount of packaging waste entering their business, and second by assuming responsibility for their products, post-consumer. The former was achieved by implementing a material consumption and waste reduction program at their manufacturing facility in San Diego. In 2010 they diverted 50% of their in-house waste by using municipal recycling services along with private 3rd party recyclers for material not accepted in the municipal stream. They also implemented a product and packaging design review that will cut the amount of material used in production by an estimated 60% in 2011. Additionally, Innovive encompassed producer responsibility by setting up a program where used products are collected from customers and returned to San Diego for environmentally friendly composting and recycling.

In 2009 Innovive invested in a 10,000sq ft recycling plant featuring a proprietary high capacity plastics separation and granulation line and a dedicated fleet of recycling vehicles. Their recycling line separates plastics from compostable materials and then processes plastics back into clean PET 1 flake. The compostable material is aggregated and sent to the Miramar Greenery compost facility located at the Miramar Landfill. Innovive provides a pick-up service for customers in California including Universities and Biotech Companies. This program diverted over 35,000 pounds of plastic flake and 22,000 pounds of compostable bedding from the landfill at Miramar annually. 

"We take great pride in this award" said Jim Fallon, President and COO of Innovive. "It is exciting to be able to provide innovative solutions to our customers in the Bio-medical industry. Our customers are increasingly interested in dealing with vendors who provide creative, sustainable solutions for the full life cycle of a product. Our substantial investment in our own recycling infrastructure allows us to provide solution to customer's issues and allows us to extend our commitment to waste reduction."

About Innovive: Innovive was founded in 2004 with the goal of radically transforming the economics and convenience of working with laboratory animals. 
Using advanced computer-aided design and manufacturing processes, Innovive creates reliable disposable rodent caging systems to provide research facilities with superior quality, performance, and cost savings. Our products are independently tested and validated to assure trouble-free operation, and our global manufacturing and distribution network provides advantageous pricing and rapid order fulfillment.

---

## Innovive Congratulates The Jackson Laboratory - Winner of The 2011 Turnkey Facility of the Year Award

- **Date:** 2011-04-15 (dateline: April 15, 2011 | San Diego, CA)
- **Original URL:** `http://www.innovive.com/company/news.html#jackson`
- **Status:** MISSING from innovive.com, lost at the pre-2024 rebuild
- **Images:** none

The 2011 Facility of the Year Award was bestowed on The Jackson Laboratory for their new Importation and Isolation facility, a three-story, 22,500-square-foot building, located on the Laboratory's Bar Harbor, Maine campus. The Facility of the Year Award recognizes outstanding achievements in the design/build of a new or renovated laboratory animal facility and is intended to showcase new ideas and accomplishments in facility design, construction and operation.

The Jackson Laboratory (JAX), a nonprofit biomedical research institution, is also the world's leading distributor of mouse models of human diseases. The new Importation facility is a new construction containment facility for receiving, housing and processing "imported" mice of unknown health status that are delivered from other institutions around the world. The building includes a 5,000-pen-capacity vivarium for housing mice. Other facilities housed in the building are an in vitro fertilization lab for harvesting and processing eggs, sperm and embryos; a cryogenic storage facility with 20 large LN2 tank freezers; a cryopreservation sample processing laboratory; and a BSL2cell culture laboratory for importing cell lines. 

The vivarium was designed specifically for Innovive Disposable Caging. The entire project was completed without a supporting cage wash or sterilizing operation. At capacity the facility will house 5,000 cages of mice in Innovive disposable caging that will reside in dual ventilated IVC racks. The design also included an innovative bio-safety cabinet design by The Baker Company of Sanford, Maine. The BSC provides an ergonomic cage change process using disposable caging.

The facility was designed by lead architect RMW Architecture of Sacramento, Calif., and WBRC of Bangor, Maine, for engineering services associated with mechanical, electrical and plumbing design, and Woodard and Curran for site permitting, site design and civil work. 

About The Jackson Laboratory: Founded in 1929, The Jackson Laboratory is an independent, nonprofit biomedical research institution based in Bar Harbor, Maine, with a facility in Sacramento, California. Its mission is to discover the genetic basis for preventing, treating and curing human diseases, and to enable research and education for the global biomedical community. The Jackson Laboratory's JAX(R) Mice & Services division supplies thousands of research mouse models and extensive research services to accelerate basic research and early stage drug discovery worldwide.

 

About Innovive: Innovive was founded in 2004 with the goal of radically transforming the economics and convenience of working with laboratory animals. 
Using advanced computer-aided design and manufacturing processes, Innovive creates reliable disposable rodent caging systems to provide research facilities with superior quality, performance, and cost savings. Our products are independently tested and validated to assure trouble-free operation, and our global manufacturing and distribution network provides advantageous pricing and rapid order fulfillment.

 
Read article on ALN site

---

## Introducing New AIA Continuing Education Credit Course - "Implementing Disposable Caging in New and Existing Facilities"

- **Date:** 2011-04-14 (dateline: April 14, 2011 | San Diego, CA)
- **Original URL:** `http://www.innovive.com/company/news.html#aia`
- **Status:** MISSING from innovive.com, lost at the pre-2024 rebuild
- **Images:** none

Innovive, the innovator and market leader in Disposable Rodent Caging, is proud to announce our American Institute of Architect's Continuing Education program. Our AIA Continuing Education Course qualifies for general education credits and will be of interest to all architects and lab planners that are engaged in animal laboratory facility projects in the US.

The course will provide an overview of designing for a disposable facility and will address the following: 

Strategies for the most efficient facility layout, with a focus on storage space, caging density, one-way materials flow and improved bio-security.
An overview of health and safety considerations including immediate and long-term benefits that accrue from eliminating the washroom, as well as ergonomic reasons for using lighter weight disposable caging.
A detailed computational model that compares the total lifetime cost of a traditional animal facility to one designed and operated with disposable cages.
Environmental assessment of disposable caging, from manufacturing and customer use to disposal.

 

About Innovive: Innovive was founded in 2004 with the goal of radically transforming the economics and convenience of working with laboratory animals. 
Using advanced computer-aided design and manufacturing processes, Innovive creates reliable disposable rodent caging systems to provide research facilities with superior quality, performance, and cost savings. Our products are independently tested and validated to assure trouble-free operation, and our global manufacturing and distribution network provides advantageous pricing and rapid order fulfillment.

---
