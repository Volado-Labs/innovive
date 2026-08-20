# Innovive — HubSpot Build & Marketing Operations Plan

**Prepared by:** Volado Labs
**Date:** 2026-08-04
**Portal:** 246069906 (`na2`)
**Target:** Innovive board meeting, first week of October 2026

> **Document status.** Sections 1 through 8 are written to be shareable with Robin and Victoria with light editing. Section 9 (Commercial framing) and Section 10 (Internal notes) are internal to Volado.

---

## 1. Where things stand today

Every figure below was pulled directly from the live HubSpot portal on 2026-08-04, not estimated.

| Measure | Value |
|---|---|
| Contacts | 142 |
| Created by a website form | 140 (the other 2 are HubSpot's built-in sample records) |
| Contacts with an owner assigned | **0** |
| Contacts past lifecycle stage "Lead" | **0** |
| Deals | **0** |
| Import jobs ever run | **0** |
| Sales activity ever logged (calls, emails, meetings) | None. The 2 of each in the portal are HubSpot's samples. |
| Users with a paid seat | 3 (Robin, Victoria, Maddison) |

**Original traffic source of those contacts:** 101 direct, **38 organic search**, 2 offline, 1 referral.

### The finding that matters most

On 2026-08-04 the site received six form submissions. One was a job application, one was a genuine sales lead, and **four were existing customers reporting equipment problems**. Every one of them was written into HubSpot as a new contact at lifecycle stage `Lead`.

This means the current contact count is not a lead count. Submissions arrive at roughly 45 to 50 per month, but the genuine new-business inquiry rate is far lower, plausibly **5 to 10 per month**. Any report built on the raw number will not survive scrutiny in a board meeting.

The cause is structural: **one form on the website is doing four different jobs.** Sales inquiries, customer service requests, job applications, and general questions all submit through the same Contact-Us form and all land in the same shared inbox.

### Everything else follows from that

- Nobody owns any contact, so nothing is followed up on a schedule.
- Service requests and sales leads compete for the same attention, so both are slower than they should be.
- There is no way to answer "how many leads did marketing generate," because the data does not distinguish a lead from a broken cage.
- There is no way to answer "did any of them become revenue," because nothing links back to NetSuite.

---

## 2. What Robin has asked for

Stated on the 2026-07-30 and 2026-08-04 calls:

1. A board-ready view, for the first week of October, of marketing performance across Google Analytics, HubSpot, trade shows, email, and social.
2. Attribution: *"if we spend marketing dollars in this lane, how is it affecting the bottom line?"*
3. Knowing how inquiries found Innovive, including a "How did you hear about us?" question on the forms.
4. **One source of truth**, rather than data spread across Looker Studio, Klaviyo, Hootsuite, and HubSpot.
5. All of it **without changing how the sales team works.** Sales stays in email and NetSuite.

### The constraint that shapes the whole design

Robin scoped HubSpot to **marketing only**. Sales opportunities, accounts, and post-handoff activity remain in NetSuite. Volado agreed to this on the call and this plan is built around it.

Consequences, stated plainly so there are no surprises in October:

- **No deal pipeline is built in HubSpot.** Deal stages would be empty and misleading.
- **Marketing's measurable outcome is the qualified handoff to sales**, not closed revenue.
- **Revenue attribution requires a link back to NetSuite.** Until that exists, "did this lead become a customer" is answered by a monthly manual reconciliation (Section 6), not automatically.

---

## 3. The plan

Eight weeks to the board meeting. Sequenced so the highest-value, lowest-dependency work lands first.

| Phase | Window | Work | Depends on |
|---|---|---|---|
| ~~**1. Separate the funnels**~~ | — | **DROPPED 2026-08-06 at Robin's decision.** No separate support form. `info@` stays the single general route, Sarah keeps routing manually, and the lead/support split moves to classification inside HubSpot. Replaced by Phase 1b. | — |
| **1b. Classify at the record** | Ongoing from Aug 6 | Assess every incoming contact as sales enquiry / service request / job application and set `inquiry_type` + lifecycle accordingly. Manual, ~5-10 real enquiries a month. | Nothing |
| **2. Know who is already a customer** | Aug 11–15 | Import the NetSuite customer list as non-marketing contacts. **Now the primary automatic way to spot an existing customer**, since the form split is gone. | A CSV export from Innovive |
| **3. Fix the data model** | Aug 18–29 | Lifecycle stages, lead status, custom properties, owner assignment, routing. | Robin's approval of proposed stages |
| **4. Turn on attribution** | Aug 25 – Sep 5 | UTM taxonomy agreed and applied across every controlled link, "How did you hear about us?" live, HubSpot source tracking verified. GA4 and Search Console joined in the dashboard, not pushed into HubSpot. See 4.10. | Nothing external. Volado reads GA4 and GSC directly. |
| **5. Trade show program** | From the August show onward | Pre-show outreach, on-site capture, post-show follow-up, list import and tagging. | A list owner at Innovive per show |
| **6. Paid advertising readiness** | Early September | Tracking verified before spend starts. | Ad account access |
| **7. Reporting** | Late September | Monthly report format agreed, board deck assembled. | Phases 1–4 complete |

**On the dropped Phase 1.** It was the highest-value change in the original plan and everything else was sequenced behind it. Robin declined it on 2026-08-06, preferring to keep `info@` as the single route with Sarah routing by hand, on the grounds that the old site had a technical support address and the new one does not, so splitting now would add a route nobody is used to. That is a reasonable call at 5-10 real enquiries a month.

Two consequences to track:

1. **Phase 2 got more important.** The NetSuite customer import is now the only automatic way to tell an existing customer from a new lead. If that stalls, classification stays fully manual indefinitely.
2. **Sarah remains the router**, which is the dependency the original design was trying to remove. Worth revisiting if volume grows or if leads start visibly sitting unactioned. The door was explicitly left open with the client.

---

## 4. HubSpot structure

This is the build specification.

### 4.1 Forms

Three live forms, agreed with the client on 2026-08-06. The proposed Customer Support form was declined; `info@` remains the catch-all.

| Form | Purpose | Routes to | Contact created as |
|---|---|---|---|
| **Contact Us** *(exists)* | Everything except InnoPlus and careers: sales enquiries, quotes, product info, **and customer service requests** | `info@`, Sarah routes | Marketing contact, lifecycle `Lead`, then reclassified by hand |
| **InnoPlus Inquiry** *(exists)* | InnoPlus service line | `innoplus@` | Marketing contact, lifecycle `Lead` |
| **Job Application** *(exists, fixed 2026-08-04)* | Careers, with résumé upload + reCAPTCHA | `hr@` | Non-marketing contact, lifecycle `Other` |
| ~~Customer Support~~ | **Declined 2026-08-06.** Revisit if manual routing becomes a burden. | — | — |
| **Event / Trade Show Capture** *(later)* | Booth capture on tablet | Marketing | Marketing contact, tagged to the event |

**Careers form verified working.** `joshuapace99@gmail.com` first applied 2026-07-26 through the old Contact-Us form with no way to attach a résumé, then re-applied 2026-08-06 07:06 UTC through the corrected HR form **with a résumé**, routed to `hr@`. Same applicant, previously mis-routed, now handled correctly. Robin's virus concern was closed on the call: HubSpot scans uploads.

**The support form is the single highest-value change in this document.** It gives customers an obvious place to go, gets service traffic out of the sales queue, and stops service requests from inflating the lead count. It needs a visible entry point on the site, not just a link buried in the footer.

**Field sets:**

*Sales / Product Inquiry:* First name, Last name, Email, Company/Institution, Country, Institution type, Product interest, Message, **How did you hear about us?**

*Customer Support:* First name, Last name, Email, Company/Institution, Product or part number, Order or PO reference (optional), Nature of issue, Description.

*Job Application:* First name, Last name, Email, Phone, Position applied for. **Open decision on the résumé field, see Section 8.**

### 4.2 Lifecycle stages

Reduced set, because sales lives in NetSuite. Deal stages are deliberately not used.

| Stage | Definition | Set by |
|---|---|---|
| `Subscriber` | On a list, has not inquired | Import or signup |
| `Lead` | Submitted a sales inquiry, not yet assessed | Form submission |
| `Marketing Qualified Lead` | Fits the ICP and shows real buying interest | Scoring or manual review |
| `Sales Qualified Lead` | Handed to sales. **This is marketing's primary KPI.** | Marketing, at handoff |
| `Customer` | Known NetSuite customer | NetSuite import or monthly reconciliation |
| `Other` | Service contacts, job applicants, vendors, students | Form type |

Marketing's reportable outcome is the count of contacts reaching **Sales Qualified Lead**, plus what the monthly reconciliation later says happened to them.

### 4.3 Lead status

Secondary to lifecycle, tracks marketing's working state: `New`, `Attempted contact`, `Working`, `Nurture`, `Unqualified`.

### 4.4 Custom properties to create

| Property | Type | Why |
|---|---|---|
| `how_did_you_hear_about_us` | Dropdown | Robin's explicit request. Values: Google search, LinkedIn, Instagram, X, Trade show or event, Referral, Industry newsletter, Distributor, Other |
| `inquiry_type` | Dropdown | Separates sales from service even when a form is shared. Values: New purchase, Quote request, Product information, Technical support, Repair or replacement, Careers, Other |
| `institution_type` | Dropdown | ICP segmentation. Values: Academic, CRO, Pharma or biotech, Government or national lab, Hospital, Other |
| `trade_show_source` | Dropdown or text | Which event a contact came from |
| `netsuite_customer` | Boolean | Set true on import. Makes "is this an existing customer?" answerable instantly |
| `netsuite_account_id` | Text | Key for the monthly reconciliation |
| `marketing_outcome` | Dropdown | **The ROI field.** Values: Unknown, Became customer, Already a customer, Lost, No response |

`marketing_outcome` is what turns activity reporting into outcome reporting. It is filled in monthly by hand until a NetSuite link exists.

### 4.5 Contact ownership and routing

Today: zero contacts have an owner. Proposed:

- Sales inquiries → **Sarah Anderson**, copy to `info@`
- Service requests → **Lisa**, customer service
- InnoPlus → InnoPlus lead, copy to `innoplus@`
- Careers → **HR**
- Anything unmatched → Victoria, for manual routing

**Dependency to confirm:** a HubSpot contact owner must be a user in the portal. Whether a free view-only seat can be set as an owner needs verifying against their subscription before seat allocation is finalised. If it cannot, seat assignment becomes a real decision rather than a formality.

### 4.6 Marketing vs non-marketing contacts

This is the most important technical decision in the build, and it costs nothing.

HubSpot bills on **marketing contacts**, the ones you can email. **Non-marketing contacts are unlimited and free.**

So:

- Import the **entire NetSuite customer list as non-marketing contacts.**
- Any future form submission from a known address is then instantly identifiable as an existing customer rather than a new lead.
- The lead count becomes true without anyone having to read and classify submissions by hand.
- Zero cost, zero quota impact, no effect on Klaviyo.

Current usage: 140 marketing contacts, 2 non-marketing. The plan's steady state should be closer to the inverse for anything customer-related.

### 4.7 Lists and segmentation

- All prospects (non-customer, marketing contacts)
- Customers (non-marketing, from NetSuite)
- By institution type
- By trade show
- Nurture audience (prospects who have not yet converted)
- Unengaged (for suppression)

Prospects and customers are never merged into one sending audience. This is Robin's explicit requirement and it is also why Klaviyo stays in place (Section 5).

### 4.8 Routing and automation on Starter

**Tier is confirmed: Starter Customer Platform, roughly $45/month across three seats, 1,000 marketing contacts included. Workflows and lead scoring are Professional-only, at roughly $890/month.**

So there is no automation engine. Everything below is achieved by static configuration plus a documented manual routine.

| Need | How it works on Starter | Would be automated at Professional |
|---|---|---|
| Sales inquiry routing | Static notification recipients set on the sales form | Workflow assigns owner and sets lifecycle |
| Service routing | Static notification recipients set on the support form | Workflow sets non-marketing and notifies Lisa |
| Owner assignment | Set manually on the contact record, or by import | Workflow |
| Lead grading | Manual `lead_grade` property, reviewed weekly | Lead scoring |
| Trade show intake | Set on import via CSV columns | Workflow |
| Follow-up nudge | Weekly review of unowned or stale leads | Task-generating workflow |
| Prospect nurture | Sent as a manual campaign to a static list | Sequenced automation |

**Note on routing, superseded 2026-08-06.** The original argument here was that forms must be physically separate, because form notification recipients are static and without workflows nothing can branch on a field value. That remains technically true, but it is now moot: the client chose to keep one general form and route by hand at the inbox. So routing is a human step by design, not a HubSpot limitation. The "What is your inquiry about?" dropdown is still worth adding for reporting, and it would help Sarah triage faster, but it classifies rather than routes.

**Do not propose an upgrade.** At 5 to 10 genuine inquiries a month, automation solves a volume problem Innovive does not have, and Victoria has already offered to handle classification manually. The constraint that will actually bind is the marketing contact allowance, not the feature set. See 4.6.

### 4.9 Integrations

| System | Decision |
|---|---|
| **Google Analytics 4** | **Do not connect to HubSpot.** HubSpot does not ingest GA4 data, and GA4 is aggregate so it cannot attribute an individual lead in the first place. Volado reads the property (`G-V8ZJQ03BE3`, owned by Volado) directly into the dashboard. |
| **Google Search Console** | **Cannot connect on Starter.** HubSpot's GSC integration requires Marketing Hub or CMS Hub Professional. Volado reads GSC directly into the dashboard instead. This is the better option anyway, since it is where the data gets joined with everything else. |
| **Klaviyo** | **Do not integrate.** See Section 5. |
| **NetSuite** | No write access, no disruption to in-flight automations. Phase 2 at the earliest, read-only, and only if IT agrees. Until then, monthly manual reconciliation. |
| **Google Ads** | Connect before September spend begins. |
| **Hootsuite / Supermetrics / Looker Studio** | Candidates for retirement once reporting moves. See Section 7. |

### 4.10 Campaign tracking (UTM)

**This is the mechanism that attributes paid media, email, social and events. It is free, works at any tier, needs no integration, and HubSpot reads it natively into the source drill-down fields on the contact record.**

Without it, everything Innovive does lands in the "direct" bucket. That bucket is currently **101 of 142 contacts, or 71%**, which is high and reflects the fact that nothing has ever been tagged.

**Taxonomy.** Agreed once and then never deviated from, because inconsistent casing or naming fragments the data and makes the reporting worthless.

| Parameter | Rule | Examples |
|---|---|---|
| `utm_source` | The specific property. Lowercase, no spaces. | `linkedin`, `instagram`, `x`, `klaviyo`, `google`, `sfa-newsletter`, `sandiego-newsletter` |
| `utm_medium` | The channel type. Fixed vocabulary. | `organic-social`, `paid-social`, `cpc`, `email`, `newsletter-sponsorship`, `print`, `qr` |
| `utm_campaign` | The initiative. `yyyy-mm-topic` or the event name. | `2026-09-innoplus-launch`, `aalas-2026`, `tradeline-2026-08` |
| `utm_content` | Optional. Distinguishes variants. | `hero-cta`, `footer-link`, `ad-a` |

**Where it gets applied**

| Surface | Owner | Notes |
|---|---|---|
| Paid advertising from September | Volado | Non-negotiable before spend starts. Without it, ad attribution is impossible after the fact. |
| Klaviyo email links | Volado / Victoria | The one place customer-facing sends become measurable |
| LinkedIn, Instagram, X posts (3x/week) | Victoria / Skyler | Needs a link-builder so they are not hand-typed |
| SFA and San Diego newsletter sponsorships | Volado | Already running, currently untracked |
| Trade show collateral, printed URLs, QR codes | Volado | Ties booth traffic to the website |

**Deliverable:** a one-page taxonomy sheet plus a pre-built link builder (a spreadsheet or a simple internal tool) so Victoria and Skyler generate correct links without memorising the convention. Hand-built UTMs are the single most common way this breaks.

**Watch item:** the share of contacts with an unknown or direct source. It should fall materially between August and October, and that movement is itself a reportable result.

---

## 5. Klaviyo: keep it, and here is why

There is **no native Klaviyo–HubSpot integration.** Connecting them requires a third-party connector such as Outfunnel or Stacksync, or custom API work.

More importantly, they should not be connected right now:

- The Klaviyo list is roughly **5,000 customers only**, mailed once or twice a quarter.
- Moving those into HubSpot as marketing contacts would consume the paid contact allowance for an audience that does not need to live there.
- Robin's requirement that customers and prospects stay strictly separate is satisfied cleanly by keeping the two systems apart.

**Recommendation: HubSpot owns prospects and marketing. Klaviyo keeps customers.** Revisit only if HubSpot's tier and contact allowance ever make consolidation cheaper.

*(Correction for the record: on the 2026-08-04 call it was said that Klaviyo was already integrated with HubSpot. It is not, and nothing from Klaviyo has ever entered the portal.)*

---

## 6. Answering "did marketing generate revenue?"

Robin's central question. The honest answer has two versions.

**The version deliverable by October, with no dependencies:**

A monthly reconciliation. Marketing exports the month's qualified leads from HubSpot, checks them against NetSuite for closed business, and records the result in `marketing_outcome`. At current volumes this is under an hour a month. It requires no sales behaviour change, no integration, and no IT involvement.

**The version that needs NetSuite:**

A one-way, read-only NetSuite to HubSpot connection that writes closed-won status back onto the contact. Better, automatic, and entirely dependent on Rasan's team agreeing that it will not disturb the automations they are already building.

**Plan for the first, treat the second as upside.** Do not build an October board commitment on top of a dependency owned by another department.

---

## 7. Reporting

**Monthly (internal):** submissions by type, genuine leads, source breakdown, qualified handoffs, outcomes recorded, trade show contribution.

**Quarterly (board):** leads by channel, cost per lead once paid media is running, qualified handoffs, outcomes, and channel-level recommendations.

**On Looker Studio.** The existing dashboard has not been maintained since the end of April, its Supermetrics connections have expired and were failing live during the 2026-08-04 call, and its HubSpot panel was pulling from the old Wix site rather than HubSpot. It is not currently a reliable source for anything.

Recommendation: rebuild reporting on a single dashboard fed directly from HubSpot, GA4, Search Console, and the social accounts. This is the "one source of truth" Robin asked for, and it removes the Supermetrics dependency and potentially the Hootsuite one as well.

---

## 8. What we need from Innovive

Everything below is on the critical path. Nothing in Phase 1 to 4 can complete without the corresponding item.

### Still open

| # | Need | From | Blocks |
|---|---|---|---|
| 3 | **NetSuite customer export** (CSV: name, email, company, account ID), or better, the read-only connection | Rasan / Victoria | Phase 2, and the whole ROI answer |
| 4 | Approve the lifecycle stages in Section 4.2 | Robin | Phase 3 |
| 5b | Agree the UTM taxonomy in 4.10 and confirm who owns link generation | Robin / Victoria | Phase 4, and all September ad spend |
| 6 | Seat allocation. Maddison's seat can be freed. | Robin | Phase 3 |
| 8 | Name a list owner per show. Victoria is engaged and proposed the September event as the pilot, with two European shows after. She has this year's lists in hand. | Victoria | Phase 5 |
| 10 | **Looker Studio access**, so nothing currently tracked is lost in the rebuild. Robin agreed but does not know how to grant it. Needs chasing. | Robin | Phase 7 |
| 11 | White / reverse InnoPlus and InnoCycle logo files | Robin | Homepage tidy-up |

### Closed 2026-08-06

| # | Was | Outcome |
|---|---|---|
| 1 | Who receives customer service requests | **No separate route.** `info@` stays the catch-all, Sarah routes by hand. Support form declined. |
| 2 | `info@` vs `orders@` | `info@`, confirmed. |
| 5 | HubSpot tier and allowance | Starter Customer Platform, ~$45/mo across 3 seats, 1,000 marketing contacts. |
| 7 | Résumé field: upload or paste | **Upload stays.** Virus concern closed on the call, HubSpot scans uploads. Verified working by a real applicant on 2026-08-06. |
| 9 | Will Sarah accept lead assignment in HubSpot | Moot for now. She continues to receive and route by email; nothing changes for her. |

**Rasan meeting:** Robin meets him 2026-08-07 08:30. A written summary of the read-only NetSuite ask was sent ahead of it so he can assess without Volado in the room. Collin offered to join; Robin may schedule separately.

---

## 9. Commercial framing *(internal)*

This work is delivered **within the existing $3,000/month retainer.** It is not an additional charge, and that should be said explicitly and early, because cost sensitivity was raised twice on the 2026-08-04 call.

The retainer is being **repositioned**, not expanded: away from blog and content production, which stalled because Innovive requires SME-authored material, and toward marketing operations and demand generation, which has no SME dependency and produces measurable output.

Recommended framing to Robin:

> "A HubSpot implementation of this size is normally a five-figure project. It is included in what you already pay us, because without it neither of us can prove what any of the marketing is doing."

**Blog production should be paused and the pause explained**, rather than continuing quietly. It is the deliverable most associated with dissatisfaction, and continuing to send it signals the objection was not heard.

The durable value in this account is not the HubSpot configuration, which finishes. It is the recurring marketing function Innovive does not have: **10+ trade shows a year with no pre-show outreach, no capture process, and no follow-up**, plus paid media starting in September. That is what should carry the relationship past October.

---

## 10. Internal notes

**Platform decision: stay on HubSpot Starter. Do not move them to GoHighLevel.**

The case for a white-labelled GHL build is real: near-zero marginal cost if Volado already runs an agency account, unlimited contacts with no marketing-contact metering, automation included, and strong retention lock-in. It was considered and rejected for four reasons:

1. **NetSuite.** HubSpot has a native NetSuite integration; GHL does not. The hardest problem in this engagement routes through NetSuite, and switching platforms makes it harder.
2. **Political cost.** Innovive bought HubSpot roughly three months ago on a recommendation from the Nextbeam/Innocycle side. Asking Robin to abandon it spends her internal capital on infrastructure rather than on the NetSuite export and Sarah's cooperation, which are what we actually need from her.
3. **Audience fit.** GHL's vocabulary and UI are built for local service businesses and agencies. Innovive sells capital equipment to NIH, Pasteur and Charles River and presents to a board.
4. **Data location.** A white-labelled agency-owned CRM puts the client's customer records in Volado's account. That is the lock-in benefit and the liability in one sentence, and their CEO is a lawyer who handles privacy matters personally. "Where does our data live and what happens if we leave" is a question we would not want to answer.

Revisit only if the marketing contact allowance becomes genuinely expensive, or for a future client whose shape actually fits.

**Risks**

1. ~~Tier collision.~~ **Resolved.** Tier confirmed as Starter. The plan has been rewritten so that nothing in it depends on an upgrade. Section 4.8 now documents the manual equivalents.
2. **The October deadline depends on Innovive.** Six of the nine items in Section 8 are theirs. Track them weekly and escalate early.
3. **Lead volume must be restated carefully.** Do not present 142 as a lead count anywhere. Once service requests and job applicants are stripped, the real number is small, and the honest story is about visibility and process, not volume.
4. **NetSuite may never open.** Design the October deliverable so it does not require it.

**Assets and access already held**

- HubSpot: service key with full read/write scopes on portal 246069906. Missing `workflows-access-public-api` and `crm.objects.leads.read`.
- GA4: Volado-owned property 544618753, `G-V8ZJQ03BE3`.
- WordPress: REST access to innovive.com.
- Ember (Innovive agent profile) has **read-only** HubSpot access and can answer CRM questions conversationally. Verified 2026-08-04: it returns authoritative counts and correctly refuses write requests. This is the mechanism for keeping recurring reporting cheap to deliver.

**Completed 2026-08-04**

- Job application page (`/job-application/`, page 3268) repointed from the Contact-Us form GUID to the HR form GUID. Applicants now route to `hr@` and can attach a résumé. Backup: `content/backups/page-3268-2026-08-04-pre-hrformguid.json`. Revert: `content/backups/revert-3268-formguid.sh`. **Still needs one human confirmation that the form renders correctly**, and the résumé-field decision in item 7.

---

## Appendix: reference

**HubSpot portal:** 246069906, data residency `na2`, UI at `app-na2.hubspot.com`

**Existing forms**

| Form | GUID |
|---|---|
| Contact-Us — info@innovive.com — June 2026 | `4207ae0e-805c-44ba-a074-adf07bf26125` |
| Inno+ — innoplus@innovive.com — June 2026 | `28d17095-a476-4751-8acb-4f1137b51e76` |
| Job Application — hr@innovive.com — July 2026 | `b29ca828-5c74-4531-b8fd-b82386d3b162` |

**Current portal users:** Robin Gaffney, Victoria Zimmerman, Maddison McKinley (`hello@insightimize.co`), Collin Wood (partner admin, unbilled), plus `info@`, `innoplus@` and `hr@` shared mailboxes.

**Key people at Innovive**

| Name | Role | Relevance |
|---|---|---|
| Robin Gaffney | Senior Director, Marketing | Decision maker, owns the board deliverable |
| Victoria Zimmerman | Senior Marketing Manager | HubSpot admin, day-to-day |
| Sarah Anderson | VP of Sales | Receives sales inquiries |
| Lisa | Head of Customer Service | Should receive service requests |
| Rasan Aycox | Digital Transformation Manager (IT / business systems) | Owns NetSuite. `raycox@innovive.com`, direct 858-309-6629. Also badged NextBeam. Transcripts misspell him as "Rahsaan"/"Rahaan". |
| Skyler | Marketing intern | New as of 2026-08-04 |
