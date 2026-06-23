# Questions for Robin & Victoria

Running list of open questions for the client. Add date when asked; move to Answered when resolved.

## Open

### 1. Which form should the CTAs use? (added 6/11)
Context: On the current Wix site, every CTA (Get Started, Contact Us, header Contact) funnels to **one native Wix form** on /contact-us with fields: First name, Last name, Email, Phone, Company, Country (dropdown), City (US only), State (US only), Reason for Inquiry (dropdown), Message. **HubSpot is installed on the site and its "collected forms" feature is capturing those Wix form submissions** (confirmed via runtime fingerprint; portal ID not visible in page source).

Questions:
- For the new WordPress site, do you want the same single-form approach, or the regional-routing form with role-based fields we scoped in the content assessment?
- Should we embed a native HubSpot form (cleanest lead flow, keeps your scoring/workflows) or build a WP form (Gravity/WPForms/Fluent) and pipe it to HubSpot?
- Who manages your HubSpot account, and can we get the tracking code / portal ID for the new site before launch?
- Same form for the Inno+ secondary contact page, or Inno+-specific fields?

### 2. Footer contents — Jamie's confirmation (added 6/11)
Robin owes a check-in with Jamie on the footer ("I'll broach it again with her"). We rebuilt it minimal per the meeting: brand + flat Resources list (Blog & News, Document Lookup; Video Training/FAQ/Case Studies/Events/Patents as built) + legal links. Confirm Jamie approves this scope — the old Products/Services/Company column menus are preserved and can be re-attached if she wants them.

### 3. "Request a Demo" CTA destination (added 6/11)
The homepage "Request a Demo" button currently points to /contact/ as an interim. Do you want a dedicated demo-request form/page (could be the Reason-for-Inquiry dropdown pre-selected, or a separate Inno+ demo flow)?

### 4. PDF / datasheet hosting strategy (added 6/13)
Context: 17 "Download PDF →" links on the new site currently point to the OLD www.innovive.com file paths — they'll break at launch (and break again on any file revision). We need a portable, host-agnostic home for downloadable datasheets/spec sheets. Recommended approach: store the PDFs in the WP **Media Library** and serve them through **stable redirect URLs** so links never break when a file is revised. Everything kept inside WordPress (media in wp-content, redirect rules in the DB) so it migrates cleanly to whatever production host is chosen — no SiteGround-specific config.

Decisions needed from Robin/Victoria:
- **Tool choice:** **Download Monitor** (free core — gives permanent /download/ URLs, version history, download counts, and optional HubSpot lead-gating) vs. a lean **Redirection** plugin map (durable links only, no analytics/gating). Recommend Download Monitor given HubSpot is already installed and this is B2B.
- **Gating:** Leave routine spec sheets as ungated direct downloads (gating adds friction), or gate a few high-value assets behind a HubSpot form for lead capture? If gating, which assets?
- **Indexing:** Keep datasheet PDFs indexable in Google (they can pull search traffic) or noindex them?
- **Keep separate from Document Lookup** (certificates.innovive.com tool) — that's lot-specific COAs/COCs from a different system; this is static product collateral.
- Approval to install/activate the chosen plugin on staging, and to pull the 17 PDFs from the current site to migrate them.

### 5. HubSpot form notifications — shared inboxes must be added as users (added 6/18)
We have a private-app token and inspected the portal. The two native forms (Contact-Us, Inno+) already exist but currently notify **only the outside consultant (Maddison McKinley, hello@insightimize.co) — nothing reaches Innovive**. That's the "missing submissions" problem. To fix it, HubSpot requires notification recipients to be **users**, and the target inboxes are not:

- **Add `info@innovive.com` and `innoplus@innovive.com` as HubSpot users** (free/view-only seat is fine for receiving notifications): Settings → Users & Teams → Create user. Each gets an invite that someone with mailbox access must **accept**.
  - `info@` invite **created 6/18** (Collin): https://app-na2.hubspot.com/invite-user/27wnvt4esbqnVHhK?lang=en&via=link — pending acceptance. Sent to Robin/Victoria via draft "HubSpot: quick step to route your website form submissions."
  - `innoplus@` invite **created 6/18** (Collin): https://app-na2.hubspot.com/invite-user/6CE3ojSQ6XNSVaa5?lang=en&via=link — pending acceptance. (Form already renamed to "…innoplus@innovive.com — June 2026".) Still confirm the mailbox is live/deliverable.
- **Confirm `innoplus@innovive.com` is a real, deliverable mailbox** (the Inno+ form was named for a future address — it must exist before leads route there).
- **Confirm it's OK to remove the consultant** (insightimize.co) from form notifications. Collin's call is to remove her; flag to Innovive in case she needs submissions for her analytics/reporting.

Once those users exist we set Contact → info@, Inno+ → innoplus@ and embed both forms on the site. (Note: HubSpot blocks API edits to these V4 forms, so the recipient change is a UI step on their side.)

### 6. Inno+ form — "Facility Type" dropdown options (added 6/18)
We want to add a **"Facility Type"** question to the Inno+ form to segment leads. Robin & Victoria to decide the option list. Proposed starter set (sent in the invite email for their approval/edit): Academic/University · Pharmaceutical · Biotechnology · Contract Research Organization (CRO) · Government/Federal lab · Hospital/Medical center · Other. Field not yet on the form; will be added in the HubSpot UI once options are confirmed (API edits to the V4 form are blocked).

### 7. Patents page — all 18 patent links are dead (added 6/18)
Every "View patent" link on the Patents page (3265 /patents-2-2/; also dup 3742 /patents-2/) points to the **retired USPTO `pdfpiw.uspto.gov` "PatImg" system** (USPTO shut it down; the domain now times out). Carried over from the old Wix site. The patent *numbers* are intact in the URLs, so we can repoint each to a working page automatically.

**What we can do on our side (no client input needed):** repoint all 18 to stable **Google Patents** deep links (e.g. US 7,527,020 → https://patents.google.com/patent/US7527020). Google Patents is the practical choice — USPTO's new Patent Public Search uses session-based search with no clean per-patent permalink.

**What to confirm with the client:**
- OK to repoint the links to Google Patents (vs. linking to USPTO, vs. just listing patent numbers with no link)?
- Is the patent list **current and complete** — any expired ones to drop, any new ones to add?

The 18 patents currently listed (decoded from the Docids): US 7,527,020 · 7,661,392 · 7,665,419 · 7,734,381 · 7,739,984 · 7,874,268 · 7,913,650 · 7,954,455 · 7,970,495 · 8,082,885 · 8,156,899 · 8,171,887 · 8,739,737 · 9,066,494 · 9,155,283 · 9,265,229 · 9,516,857 · 9,516,858.

(Also flag: there are **two** Patents pages — 3265 and 3742 — confirm which is canonical / delete the duplicate.)

## Content / assets needed from Innovive

- Testimonials + approved customer logos — Robin auditing contracts (6/10 meeting)
- Supply Chain & Logistics page copy — Robin (6/10 meeting)
- Updated water-process content — blocks the Water Process page under The Innovive System (6/10 meeting)
- Current/upcoming events list — blocks the Events page content (site map)
- Homepage hero photo selection — Robin w/ Victoria (multi-rack vivarium image, 6/10 meeting + tracker row 9)
- HubSpot tracking code / portal ID — ✅ have portal access (246069906) as of 6/18; remaining HubSpot asks moved to question 5

## Answered

### Research Ready placement — ANSWERED 6/11
Under The Innovive System. (Implemented in nav same day.)

### Events & Patents placement — ANSWERED 6/11
Both in the footer.

### Products dropdown shape — ANSWERED 6/11
Option B: Mouse / Rat / Mouse & Rat nested flyouts, plain dropdown, no mega menu. (Implemented.)

### 1. Form platform — ANSWERED (per 5/28 Innovive ⟷ Volado SEO sync)
**HubSpot.** Forms on the new site should be **embedded HubSpot forms** for submission tracking into HubSpot CRM. Meeting action items: Volado requested **HubSpot Manager** access (Innovive to accept), then review/optimize the **existing HubSpot forms** and embed them. Implication: the Contact form, the Inno+ 2nd-page form, and the Job Application form should be HubSpot embeds — the Elementor forms currently built are interim. DEPENDENCY: confirm Volado now has HubSpot Manager access + portal ID to embed.
