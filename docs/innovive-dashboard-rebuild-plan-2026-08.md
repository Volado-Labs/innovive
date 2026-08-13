# Innovive Marketing Dashboard: Audit and Rebuild Plan

Date: 2026-08-13
Owner: Collin Wood
Status: Draft for review, not yet started

## 1. Why this exists

On the Aug 13 weekly sync, Robin asked for something the current Looker Studio report doesn't have at all: an executive summary that shows where leads come from and where the push efforts are underperforming, in one view, ahead of the Innovive board meeting (likely October). Victoria shared the current report during the call. Collin agreed to take a first pass at rebuilding it.

Report audited: "Innovive — DataStudio Report (April 2026)", `https://datastudio.google.com/reporting/97c23de3-6c12-47af-bcd1-3cb9ef2d636b`. Last touched by Madison (Nextbeam) in April 2026.

## 2. Audit: current report, page by page

| Page | Data source | Status | Notes |
|---|---|---|---|
| Website Performance | GA4 (native) | Working, thin | Only a world heatmap + country table (27,647 sessions, 104 countries). No trend line, no KPI summary tiles. |
| Trade Media | GA4 (native) + Bitly campaign links | Working, questionable numbers | GA4 shows 17 and 6 sessions for the two live banner campaigns (San Francisco / San Diego Big4Bio). Victoria says Bitly reports far more clicks. Needs a real diagnosis (bot clicks / UTM stripping / redirect chain) before assuming it's broken. |
| Organic Search Performance | Search Console (native) | Working | Real landing-page click/impression/CTR/position data. |
| LinkedIn Performance | Supermetrics | Broken | All charts empty. Matches what Victoria hit live on the call. |
| Instagram Organic | Supermetrics | Partially working | Top chart empty, but scorecards below have real numbers (4,039 views, 90 likes, 46 media). Date range selector is also misconfigured (says "year to date," footnote says "last 28 days"). |
| X Organic | Supermetrics | Broken | Completely empty, nothing renders anywhere on the page. |
| Email Performance | Klaviyo (direct connector, not Supermetrics) | Broken | All 4 charts empty. Looks like an expired or revoked Klaviyo connection, not a Supermetrics problem. |
| Conference Performance | Static Google Sheet ("from Victoria," 4/20/26) | Stale | 7 records, nothing added since March 2026. Known bug noted on the page itself: region filter doesn't work with this data. |
| Form Submission Performance | Static Google Sheet, literally a Wix export from Robin (4/27/26), Jan-Apr 2026 only | Dead | Predates the WordPress + HubSpot migration entirely. This is the exact page Victoria pointed to as "where we'd connect HubSpot" on the call, confirming HubSpot lead data has never reached this dashboard. Same broken region filter. |
| NOT IN USE - SurveyMonkey Performance | Old survey export | Dead, explicitly labeled unused | Drop entirely, don't migrate. |

**Scorecard:** 3 of 10 pages are live and healthy, all on native connectors (GA4 x2, GSC). 3 pages depend on Supermetrics, ranging from fully broken to partially working. 1 direct integration (Klaviyo) is broken. 2 pages run on manual Google Sheets nobody has touched in months, one of which predates the current form-routing and HubSpot setup entirely. 1 page is dead weight. No page anywhere summarizes across sources, which is the specific gap Robin flagged.

### GA4 property mismatch (needs a decision)

This report's GA4 numbers almost certainly come from Innovive's **original client-owned GA4 property**, not the new Volado-owned `innovive.com` property (544618753, under the voladolabs.ai GA account) stood up in July after the broken-tag incident. Reasoning: the report's default date range runs back to April 2025, well before the new property existed (created 2026-07-08), and via the GA4 MCP connection Volado currently only has API access to the new property, not the client's original one. Search Console access is clean by comparison: `sc-domain:innovive.com` is already verified as site-owner.

This needs a decision before Phase 1 build work starts: keep reporting off the old property (loses the fixed tag, stays on an account Volado doesn't control) or cut over to the new one (clean tag, full API access, but the trend lines restart from July 2026 with a visible gap before that).

## 3. Precedent: what Volado has actually built before

Collin asked to weigh two other dashboard builds before deciding Innovive's architecture: Adherent and Conexiom (both described as already built), and Biscuits Cafe (in progress). Researched directly against the vault and the underlying repos.

### Adherent (SEO/GEO KPI dashboard)

A static, server-generated HTML report, not a live web app. A Python build script (uv/PEP 723, no venv) pulls DataForSEO AI share-of-voice data, Semrush (rankings, site audit, AI visibility), GA4, Search Console, and WordPress publish counts, and bakes everything into one static `index.html`. Hosted on Vercel at `reports.voladolabs.ai/adherent/kpi-dashboard/`, `noindex/nofollow`, no auth at all beyond obscurity. Nothing calls an API from the browser.

Two details matter for Innovive:
- HubSpot MQLs are **not automated** here either. Adherent's client won't grant an API seat, so it's a manual monthly CSV import, same category of problem Innovive is in right now.
- A weekly refresh cron existed, then Collin removed it on 8/06. The record points to a rebuild having overwritten hand-fixed live HTML from a stale generator source, plus most sources needing manual touch anyway. The handoff doc is explicit: don't recreate the cron without approval.

### Conexiom: no dashboard precedent actually exists

Collin, this is worth flagging directly: there is no Adherent/Biscuits-style dashboard for Conexiom in the vault. What exists is a periodic "Marketing Intelligence" HTML report (Google Ads + GA4 tables with trend lines) that replaced a weekly email in April, and a "new marketing dashboard" that was listed as owed to the incoming interim CMO during the July handoff but never shows up as built anywhere in the churn-transition notes (contract ends 8/17). I checked the full client page for every "dashboard" mention. There's no architecture, auth model, or build plan to borrow from here, only the general discipline of a clean handoff folder when a relationship ends.

### Biscuits Cafe (Kyle's performance portal, in progress)

This one's a real live web app, not a report. Cloudflare Pages hosting a buildless vanilla JS/HTML/CSS frontend, with all data access happening server-side through Cloudflare Pages Functions. Its own dedicated Supabase Postgres project, fully separate from the internal ops-dashboard's database. Auth is Supabase email+password, which Collin deliberately switched to mid-build from the original plan (Cloudflare Access/SSO) once it became clear Kyle needed self-serve daily access across multiple locations for his own team, not SSO-gated internal tooling.

Data sources: Toast (ops/sales via nightly Supabase sync + a documented Standard API path, a full year backfilled), Google Business Profile via Local Falcon's "Falcon Guard" (cross-validated against Kyle's own GBP numbers), Metricool (published posts), Toast Marketing email (no public API, manual import, sales-driven numbers explicitly flagged as unverified estimates, never causal proof), and Google Ads (schema present but inert until tracking is verified).

The access model is genuinely hardened, because it has to be: a `client_dashboard_access` table drives all entitlement server-side, RLS is enabled with zero client-facing policies (all real reads go through `service_role` behind the entitlement check), and a named anti-pattern from the internal ops repo (`client_id` trusted straight from the request body, no auth check) is called out as the exact IDOR failure this portal must never replicate. There's also a "roster vs. managed scope" data model: what Kyle owns versus what Volado actually manages are tracked as separate, effective-dated facts, so an unmanaged location renders as "not managed by Volado" rather than a misleading zero. A 9-threat model was written and reviewed before any UI code.

Current status is genuinely inconsistent across the vault's own documents (three different files disagree with each other and with the repo's own README about what phase it's in), but the most recent status line (2026-08-11) says the real state is: fully built and tested (97/97 tests passing, full data layer live), not yet deployed or invited. Treat "awaiting approval" and "Phase 1 in progress" language elsewhere in the vault as stale bookkeeping. Repo: `Volado-Labs/volado-client-portal`.

### What's actually shared across builds, versus one-off choices

Shared, and worth carrying into Innovive regardless of which architecture gets picked:
- **No provider credentials ever reach the browser.** Both real builds keep every API key server-side. This traces to a named prior failure: the MCA Dashboard project shipped a live Anthropic key in client-side JS, visible via view-source, and had to be fixed before launch. Adherent's own build notes cite this directly as the failure mode it was designed to avoid.
- **Missing data renders as missing, never as zero**, and partial periods are labeled as partial. Biscuits enforces this with a `quality_state` field; Adherent enforces it by leaving gaps blank rather than fabricating.
- **Every metric carries its own freshness/source date**, not one dashboard-wide "last updated" stamp, because GSC lags days, some Semrush metrics are monthly-manual, GA4 is near-live, etc.
- **Manual CSV import is treated as a normal, permanent fallback**, not a stopgap to be automated away, whenever a platform's own access/plan limits block API automation. Both builds discovered this mid-project for at least one source (HubSpot at Adherent, Toast Marketing at Biscuits).
- **Never assert causation from correlated data.** Both builds have an explicit rule against it.

One-off, chosen per project, not "the Volado way":
- **Hosting/deploy shape differs on purpose.** Adherent is a periodically-regenerated static report (no live database). Biscuits is an always-on portal with a real time-series database and role-based access. The right choice depends on whether the audience needs to log in and explore data themselves (Biscuits-style) or just receive a report Volado maintains (Adherent-style).
- **Auth model diverges even within Biscuits' own history** (Cloudflare Access/SSO originally planned, then replaced by Supabase email+password once self-serve, invite-based, multi-user access became the actual requirement). Adherent has no auth at all. Pick based on the actual audience, not habit.

## 4. Recommendation for Innovive

Innovive's audience is small and known: Robin, Victoria, occasionally Jamie (CEO) for the board deck. There's no external client roster, no multi-location/multi-tenant access problem, and no self-serve-signup requirement like Kyle's. That argues against copying Biscuits' full Supabase Auth + RLS + threat-model machinery wholesale. It's also not a pure static report the way Adherent is, since Robin explicitly wants an ongoing, checkable view ahead of a recurring board cadence, not a one-off document.

Proposed staged approach:

**Phase 1: rebuild inside Looker Studio (fast, matches what Collin already told Robin and Victoria he'd do).**
Robin and Victoria already know the tool. Native GA4 and Search Console connectors already work well (3 of the current pages prove this). HubSpot has an official native Looker Studio connector, which directly replaces the dead Wix-export page and is the actual fix for "this is where we'd connect HubSpot." This gets Robin a materially better dashboard within days, not a multi-week build.

Concretely, per page:
- Website Performance: rebuild as the executive summary Robin asked for (KPI scorecards + trend, not just a heatmap), decide the GA4 property question first.
- Trade Media: keep GA4-native, add the Bitly-vs-GA4 discrepancy investigation as a one-time task, not a rebuild.
- Organic Search Performance: keep as-is, it works.
- LinkedIn / X Organic: decide whether to keep paying for Supermetrics at all. Both platforms have thin free organic reach for a B2B life-sciences account this size; before rebuilding these pages, check whether the numbers justify the subscription cost Collin already asked Robin about on the call, versus just linking out to native LinkedIn/X analytics.
- Instagram Organic: fix the date-range misconfiguration, keep if Supermetrics stays.
- Email Performance: this is a Klaviyo auth/reconnect issue, not an architecture issue. Fix the connection directly.
- Conference Performance: keep as a manual Google Sheet for now (matches Victoria's actual workflow), but fix the region filter and put a process in place so it's actually updated when events happen, since it's been stale since March.
- Form Submission Performance: replace entirely with the native HubSpot connector, filtered/segmented by the lead-vs-service classification work already underway in the HubSpot build plan (`docs/innovive-hubspot-plan-2026-08.md`).
- SurveyMonkey: delete the page.
- Add a true first-page executive summary: leads by source, top and bottom performing channels, trend versus prior period. This is the specific thing Robin said is missing.

**Phase 2 (only if Phase 1 turns out not to be enough): a lightweight custom app, Biscuits-pattern but scaled down.**
Two concrete triggers would justify this: (1) Collin's own stated interest in letting Robin ask the dashboard plain-English questions ("what channel is underperforming," mentioned live on the call) isn't something Looker Studio can do; or (2) the HubSpot lead-classification and NetSuite-attribution logic gets complex enough that blending it correctly needs real business logic Looker Studio's blending can't express cleanly. If either of those becomes real, follow Biscuits' pattern for the parts that generalize (server-side-only credentials, per-metric freshness, missing-never-zero) without its multi-tenant auth complexity. Cloudflare Access restricted to named Innovive and Volado emails (the model Biscuits itself started with before Kyle's requirements changed it) fits Innovive's small, known audience better than building a signup system.

## 5. Open decisions needed before Phase 1 starts

- GA4 property: stay on the client's original property, or cut over to the new Volado-owned one and accept the July 2026 data start.
- Supermetrics: cancel now (Robin confirmed on the call it's not used for anything but this dashboard) once a decision is made per-platform on LinkedIn/Instagram/X, or keep it running through the rebuild.
- Board meeting date: Robin said October on the call but flagged she needs to confirm whether it's actually November. The executive summary page's must-have date depends on this.
- Who owns keeping Conference Performance current going forward (Victoria, per the existing workflow) so it doesn't go stale again immediately after the rebuild.

## 6. Next steps

1. Confirm the GA4 property decision with Robin/Victoria.
2. Reconnect Klaviyo (quick, no architecture decision needed).
3. Diagnose the Trade Media Bitly-vs-GA4 gap.
4. Build the executive summary page first, since it's the specific ask.
5. Swap Form Submission Performance to the native HubSpot connector once lead/service classification is live.
6. Decide Supermetrics per-platform and drop or fix LinkedIn/Instagram/X accordingly.
7. Delete the SurveyMonkey page.
