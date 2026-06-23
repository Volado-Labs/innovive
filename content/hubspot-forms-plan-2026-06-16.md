# HubSpot Forms — Action Plan (from 6/16 Innovive website check-in)

Source: "Innovive website check in," 6/16 (Victoria + Robin + Collin + Clayton). We now **have HubSpot access**.

## What was decided
- The old **Wix forms were imported into HubSpot** as non-native ("collected") forms. **Don't use those — rebuild as native HubSpot forms** and embed them on the new site.
- There are **two forms in scope** (Victoria), and the core problem is **email routing is broken** — submissions aren't all being received.
- Innovive's team doesn't know the workflow internals; an outside person (sister-company employee) is helping with **HubSpot + analytics (SuperMetrics / Data Studio)** — but that's analytics, **forms/routing are ours to set**. Don't break any existing workflow without checking.

## The two forms + correct routing
| Form | Used on | Should route to | Current problem |
|---|---|---|---|
| **Contact Us** (general) | site-wide Contact CTAs / Contact page | **info@innovive.com** | not receiving all emails |
| **Inno+** | the dedicated Inno+ contact page | **noplus@innovive.com** | a HubSpot form (created **May 8**) is misrouting these to **orders@innovive.com**; it's not used anywhere yet, so safe to fix/replace |

*(Email addresses are from a speech-to-text transcript — Victoria is emailing the exact addresses; confirm spelling before wiring.)*

## HubSpot to-do
1. **Build native HubSpot forms** (ignore the imported Wix ones):
   - **Contact Us** — comprehensive field set we already defined (region, "describe you" incl. Purchasing, first/last, email, phone, company, open-text Reason for Inquiry, message).
   - **Inno+** — for the new dedicated Inno+ contact page.
2. **Fix routing / notifications:**
   - Contact Us → **info@innovive.com**
   - Inno+ → **noplus@innovive.com** (correct the May-8 form that points to orders@, or rebuild it)
   - **Test each end-to-end** — the whole reason this came up is the Wix forms were silently dropping emails.
3. **Check existing workflows first** so we don't break anything the Innovive/analytics person set up; only then adjust form notifications/workflow routing.
4. **Embed the native HubSpot forms on the new WP site**, replacing the interim Elementor forms:
   - Contact page → Contact Us form
   - Inno+ second page → Inno+ form
5. **Analytics (adjacent, Collin committed):** set up **GA4 in HubSpot** so Innovive sees traffic reports inside HubSpot; coordinate with their analytics resource.

## Confirmations needed from Innovive
- Exact email addresses: **info@innovive.com** (Contact) and **noplus@innovive.com** (Inno+) — Victoria to email.
- Anything on the May-8 Inno+ HubSpot form/workflow they want preserved (likely not — it's misrouted + unused).

## Note
- The meeting scoped **two** forms (Contact + Inno+). The **Job Application** form (Careers) wasn't discussed here — flag whether it should also become a HubSpot form or stay as the native page form.

---

## DISCOVERED STATE — 2026-06-18 (live API inspection, portal 246069906 / na2)

Got a private-app token; inspected the portal directly. **The forms are NOT missing — they already exist as native HubSpot forms.** This is a routing fix, not a build-from-scratch.

**Two native forms present (both `formType: hubspot`, both "Not Live Yet"):**
- `4207ae0e-805c-44ba-a074-adf07bf26125` — "Contact-Us — info@innovive.com" — fields: firstname, lastname, email, phone, company, country, country_region_code, state, city, message(label "Reason for Inquiry").
- `28d17095-a476-4751-8acb-4f1137b51e76` — "Inno-Plus — orders@innovive.com" — same minus country/country_region_code.

**Zero workflows in the portal** — so routing is handled by form **notification recipients**, not automation. Nothing for the analytics person to "break" on the workflow side.

**The actual misroute (concrete, not the transcript's "orders@"):** BOTH forms have `notifyRecipients: ["51813385"]`. User 51813385 = **Maddison McKinley, hello@insightimize.co** — the outside analytics consultant, NOT an Innovive inbox. So every submission notifies the consultant and **nothing reaches info@ or noplus@**. This is almost certainly the "not receiving all emails" problem.

**Routing blocker:** `info@innovive.com` and `noplus@innovive.com` are **not HubSpot users/owners** (the only owners are Maddison/insightimize, Collin, Robin, Victoria). To notify those addresses they must be added as notification email recipients (and noplus@ spelling is still pending Victoria's email).

**Field gaps vs. our agreed Contact spec:** neither form has the "What best describes you?" dropdown (Researcher / Faculty Manager / Distributor / Purchasing / Other) added to the Contact page; the Inno+ form also lacks the Country field. Proposed, not yet changed.

**Embed (ready once routing is set):** region `na2`, portalId `246069906`, formIds above (V4 embed).

**Decisions (Collin, 6/18):** remove the consultant from notifications; Inno+ recipient = **innoplus@innovive.com**; Contact recipient = **info@innovive.com**.

**API WRITE BLOCKED (confirmed 6/18):** Both forms are `embedType: V4` (built in HubSpot's new form editor). Every write attempt — v3 `PATCH /marketing/v3/forms/{id}` AND legacy v2 `POST /forms/v2/forms/{guid}` — returns `403 BANNED: "The client is not allowlisted to perform an operation to v4 forms."` This is a HubSpot platform restriction on V4 forms, not a scope/token problem. The API can READ them fully but cannot edit them. CREATE (`POST /marketing/v3/forms`) is NOT banned.

**Therefore the recipient fix must be made one of these ways:**
1. **UI edit on the existing two forms (recommended)** — open each form in HubSpot, set submission-notification recipient (Contact→info@, Inno+→innoplus@), remove Maddison. Keeps the consultant's existing forms intact; ~1 min each.
2. **API-build replacement forms** — create two fresh forms via the (non-banned) create endpoint with routing baked in, embed those, archive the old two. Downside: forks the consultant's setup into parallel forms.

**Embed (ready regardless of which path):** HubSpot V4 embed — region `na2`, portalId `246069906`, formId `4207ae0e-805c-44ba-a074-adf07bf26125` (Contact) / `28d17095-a476-4751-8acb-4f1137b51e76` (Inno+).

**Contact form EMBEDDED 6/18** on page 1671 (/contact/), replacing the interim Elementor form (was widget `55a5f9c`, now html widget `fc0a7b1` in column `bd3685c`). Backup: content/backups/page-1671-2026-06-18-pre-edit.json.
- **kses gotcha (important for the Inno+ embed):** a raw `<script src="…external…">` tag in an Elementor HTML widget is **silently rejected by WP's kses on the REST `_elementor_data` write** — the whole meta write becomes a no-op (returns 200, saves nothing). Fix: use an **inline** `<script>` that injects the loader via `document.createElement` (inline scripts + the `hs-form-frame` div survive kses; iframes also survive). That's what's deployed.
- Submissions are captured to HubSpot CRM as soon as the form renders; the notification-recipient fix (info@ acceptance) is independent and still pending.
- **Inno+ embed still pending** the dedicated second Inno+ page being built.

**Site-wide form audit + standardization — 6/18:** Scanned all pages (publish+draft) and all elementor_library templates (header/footer/popup) for form widgets, HubSpot embeds, and shortcode forms (CF7/Gravity/WPForms/Fluent/Ninja). Result — only **two lead forms** existed: /contact/ (already HubSpot Contact, done above) and /job-application/ (Elementor form `a194140`). No forms in templates, no shortcode forms, no stray embeds. **Job Application form replaced 6/18** with the HubSpot **Contact** form (per Collin's instruction) — page 3268, Elementor form `a194140` → html widget `b2f4c81`; backup content/backups/page-3268-2026-06-18-pre-edit.json. So every lead form on the site is now a HubSpot form (Contact). The only remaining non-HubSpot forms are WooCommerce's transactional cart/checkout/account forms (out of scope).
- **Caveat on Job Application:** the general Contact form has no resume-upload or position field — applicants can't attach a CV through it. Flagged in case a job-specific HubSpot form (or a resume-email step) is wanted later.
