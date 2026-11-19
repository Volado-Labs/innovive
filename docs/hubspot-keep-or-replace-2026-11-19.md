# Should Innovive keep HubSpot?

Volado Labs, November 19, 2026. Internal analysis for the year-end tech-stack review agreed on August 6.

## Recommendation

**Keep HubSpot, stay on Starter, and give it a narrow, written job.** Do not upgrade to Marketing Hub Professional for 2027, and do not replace HubSpot.

HubSpot costs Innovive about $45 a month. For that, it does three things nothing else in the stack does cheaply: it captures every website inquiry, it receives NetSuite's customer, opportunity and order data through a native connector, and it is the record the custom dashboard reads to tie an inquiry to a purchase. Replacing it would save roughly $540 a year and cost weeks of rebuild work, including the NetSuite sync finished on November 18. Upgrading would cost about $10,000 a year for features Innovive has said it will not use.

## What HubSpot does for Innovive today

| Job | How it works now | Could something else do it? |
|---|---|---|
| Website inquiry capture | Contact Us, Inno+ and HR forms are HubSpot embeds. Snippet #37 fires the GA4 `form_submit` conversion from HubSpot's form message. | Yes, but every form, the GA4 conversion and the HR file-upload handling would be rebuilt. |
| Traffic source on each contact | HubSpot tracking code records first source; the "How did you hear about us?" field adds the self-reported answer. | Partly. GA4 has source but not per-person identity. |
| NetSuite mirror | Native connector, one way from NetSuite. Companies (Innovive subsidiary only, with status, record ID, domain, email and inactive flag), opportunities as deals, invoices, and sales orders since January 1, 2026. | Only with custom code against NetSuite, which Rasan would have to support. |
| Customer recognition | Contacts match companies by email domain; the verifier writes NetSuite status to `vl_customer_match` and `vl_customer_evidence`. | Not without HubSpot or a new database. |
| Lead classification | `inquiry_type` separates sales inquiries from support, jobs, vendors and spam. The Marketing Leads view shows only verified non-customers and inactive accounts (22 contacts on November 19). | Yes, in any CRM, but the rules and history live here now. |
| Event contacts | Reviewed trade-show lists are imported with an `Events attended` tag (Kellogg West done; AALAS and My Green Lab pending). | Yes, in any CRM. |
| Reporting source | The Volado dashboard reads HubSpot every 15 minutes and links each record back to it. | Only by repointing every connector. |

What HubSpot does **not** do, by Innovive's choice: send marketing email (Klaviyo does that for about 6,400 customer profiles), run the sales process (sales stays in email and NetSuite), automate follow-up (Starter has no workflows), or report revenue attribution (HubSpot reserves that for Enterprise; the custom dashboard does it instead).

## The three options

### 1. Stay on Starter (recommended)

- **Cost:** about $45 a month for three core seats (Robin, Victoria, Rasan). Roughly $540 a year.
- **Fits the constraints Robin set:** sales does not change its routine, customers stay separate from prospects, and Innovive does not spend "CRM level money."
- **Room to grow:** the account holds about 395 contacts against a 1,000 marketing-contact tier, and non-marketing contacts are unlimited.
- **The gaps are already covered.** Starter lacks workflows, custom reports and attribution. Classification, customer verification and purchase reporting run in the Volado dashboard, which writes its evidence back onto the HubSpot contact.

### 2. Upgrade to Marketing Hub Professional

- **Cost:** HubSpot lists Professional at $800 a month billed annually ($890 monthly) with three core seats, plus a one-time onboarding fee. Call it $10,000 to $13,000 in year one.
- **What it adds:** workflows (automatic routing and follow-up), lead scoring, custom reports, social publishing and campaign reporting.
- **Why not now:**
  - Its main value is automated email nurture, and Innovive sends email from Klaviyo, not HubSpot.
  - Native multi-touch revenue attribution is still not included. It needs Enterprise at $3,600 a month.
  - Inquiry volume is about 50 to 60 form fills a month. Classification by rule plus a weekly human check handles that.
  - The custom dashboard already provides the board-level reporting Professional would sell.

### 3. Replace HubSpot

The realistic replacements are NetSuite's own CRM features (online forms and lead records) or a forms tool feeding Klaviyo and the dashboard directly.

- **Saving:** about $540 a year.
- **What would have to be rebuilt:** the three website forms and their routing; GA4 conversion snippet #37; the NetSuite connection, which in NetSuite's case would mean marketing working inside the ERP that Rasan administers and that sales does not use for leads; the dashboard connectors; the customer-matching logic; and the classification history since August.
- **Risk:** the November 18 NetSuite work (order sync, company scope, five source fields) is the closest Innovive has come to tying marketing to purchases. Replacing HubSpot restarts that clock just as the first orders import.

Replacement only makes sense if Innovive were leaving NetSuite or wanted sales to work leads in a new CRM. Neither is on the table.

## What "keep" should mean in practice

1. **Write down HubSpot's job.** Intake, source capture, customer recognition and the NetSuite mirror. Not email, not sales, not reporting. This stops the recurring question of why HubSpot "doesn't do more."
2. **Protect the 1,000-contact tier.** HubSpot forms can mark every submitter as a marketing contact even though Innovive sends no HubSpot email. Exceeding the tier can trigger an automatic paid upgrade. Audit marketing-contact status by source and set job applicants, support requests and NetSuite-synced records to non-marketing. No changes have been made yet; this needs Victoria's go-ahead.
3. **Check the invoice.** Confirm the actual monthly charge and whether any Data Hub or add-on line appears. HubSpot's documentation ties some custom NetSuite field mappings to a Data Hub subscription; the five mappings saved on November 18 should be confirmed as covered by the current plan.
4. **Keep ownership inside Innovive.** Rasan holds a core seat and should stay the owner of the NetSuite connection, as he recommended in August, so the integration does not depend on Volado.
5. **Be clear about the dependency on Volado.** The purchase reports and customer verifier run on Volado's infrastructure. If the engagement ended, Innovive would keep all HubSpot data and the evidence fields written onto contacts, but not the live reports. That is a reason to keep writing proof back into HubSpot, not a reason to upgrade.

## When to revisit Professional

Reconsider the upgrade if any of these becomes true:

- Innovive decides to run regular prospect nurture (Inno+, trade-show follow-up) from HubSpot instead of Klaviyo.
- Form volume rises well past manual review, roughly 150 or more a month.
- Marketing contacts approach 1,000 after the status cleanup.
- Sales leadership asks to work leads in HubSpot.

Until then, the cheapest tier is doing the job it should do, and the money is better spent on content and the trade-show follow-up program.

## Sources

Vault client page (August 4, August 6, August 24 and November 18 sections); `docs/innovive-netsuite-hubspot-sync-2026-11-18.md`; `docs/klaviyo-recommendation-2026-09-21.md`; HubSpot Marketing Hub pricing page, checked November 19, 2026.
