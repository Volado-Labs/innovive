# Innovive Marketing Dashboard: Custom Build Plan

Date: 2026-08-13 · Built 2026-08-19
Owner: Collin Wood
Status: **BUILT AND LIVE.** See Section 0 for as-built detail and what remains blocked.
Supersedes: `innovive-dashboard-rebuild-plan-2026-08.md` (Looker Studio rebuild option, decided against)

---

## 0. As-built (2026-08-19)

Live at **https://innovive-dashboard.pages.dev**, behind Cloudflare Access.
Code: `~/Projects/innovive-dashboard` (its own repo).

| Piece | As built |
|---|---|
| Hosting | Cloudflare Pages project `innovive-dashboard` |
| Data access | Cloudflare Pages Functions only. No provider credential reaches the browser, and the Functions themselves hold none — they only read the store. |
| Database | Supabase project `innovive-dashboard` / `gdszfjekgolpaoquwndh`, dedicated, **$10/month** |
| Auth | Cloudflare Access, one-time PIN, allowlist: Collin, Robin, Victoria. Verified server-side on every API call, plus a second env-var allowlist that fails closed. |
| Refresh | Supabase Edge Function `nightly-sync` on pg_cron, 02:00 Pacific, sharing one code path with the CLI sync |
| Tests | 50, covering period maths, missing-vs-zero, Access verification (forged/expired/wrong-audience/non-allowlisted), HubSpot lead refusal, CSV import |

### Source status as built

| Source | State | What it needs |
|---|---|---|
| GA4 website performance | **Live** | — |
| Search Console | Blocked | Grant the sync service account access (one click, see below) |
| HubSpot leads | Blocked | A token for portal 246069906 **and** the lead-vs-service classification |
| Klaviyo email | Blocked | A fresh private API key |
| Bitly trade media | Blocked | A token, plus the click-vs-session diagnosis |
| Conferences | **Live** | Entered in the dashboard; the Google Sheet is retired |
| LinkedIn / X | Manual by design | Decide the owner and cadence for the monthly CSV |
| Instagram | Planned | Confirm it is a Business/Creator account |
| SurveyMonkey | Dropped | — |

Full detail, and exactly what unblocks each one, is in
`~/Projects/innovive-dashboard/docs/unblocking.md`.

### Three findings from building it

1. **There is no GA4 history before 2026-07-08.** The old client-owned property
   is not reachable by any Volado credential — it does not appear in the account
   at all. So the property question in Section 1 is settled by access, not by
   preference. The earliest *complete* GA4 month is **August 2026**; July covers
   24 of 31 days and is labelled partial everywhere it appears. Year-over-year
   website comparison is not possible this year. Search Console, once unblocked,
   is the only source that can carry a long trend.

2. **No meaningful conversion is configured in GA4.** The property's only key
   event is the auto-created `purchase`, which cannot fire on a site that sells
   capital equipment through sales conversations. Only four events exist at all.
   The dashboard reports key events as "Not measured" rather than zero, because
   "zero conversions" and "no conversion is defined" are different statements and
   only the second is true. Until a real key event exists, GA4 cannot answer
   "which channel produced leads" — only HubSpot can.

3. **The HubSpot lead count is deliberately withheld.** One Contact-Us form
   handles sales inquiries, service requests, job applications and general
   questions, all recorded at lifecycle stage `Lead`. The connector reports
   submissions honestly and refuses to call them leads until the classification
   property exists. This is the single most likely way the dashboard could have
   embarrassed someone in a board meeting.

## 1. Decision

Collin decided against rebuilding inside Looker Studio. Innovive gets a custom-built
dashboard instead: a small, always-on web app Robin and Victoria log into, not a
periodically-regenerated report. The audit of the current Looker Studio report (done
2026-08-13, full detail in the superseded plan doc) is still the source of truth for
what data this needs to cover and what state each source is actually in. Summary:

| Data need | Current source | Status |
|---|---|---|
| Website performance | GA4 (native) | Working, but no trend/KPI view |
| Trade media (Bitly banner campaigns) | GA4 + Bitly links | Working, but GA4 session counts look far lower than Bitly's click counts, needs diagnosis |
| Organic search | Search Console (native) | Working |
| LinkedIn organic | Supermetrics | Broken |
| Instagram organic | Supermetrics | Partially working, misconfigured date range |
| X organic | Supermetrics | Broken |
| Email performance | Klaviyo (direct connector) | Broken, likely expired auth |
| Conference/event attendance | Manual Google Sheet (Victoria) | Stale since March 2026 |
| Form submissions / leads | Manual Google Sheet, a pre-migration Wix export | Dead, HubSpot data never reached it |
| SurveyMonkey | Old survey export | Explicitly unused, drop |

~~Also unresolved: the GA4 property question.~~ **Resolved 2026-08-19 by access.**
The old client-owned property is not present in any Volado-accessible GA4 account, so
there was never a choice to make: property **544618753** is the only source of truth
available, and it begins on 2026-07-08. There is no earlier history to inherit. This is
recorded in the dashboard itself rather than glossed over — every period before
2026-07-08 reads "Not measured", and July 2026 is labelled partial.

## 2. Why custom, and why not copy either existing precedent wholesale

Two live Volado dashboard builds were researched before this decision: Adherent's KPI
dashboard (a static, server-generated HTML report, Vercel-hosted, no live database, no
real auth) and Biscuits Cafe's Kyle dashboard (a real live web app — Cloudflare Pages +
Pages Functions, its own dedicated Supabase project, Supabase Auth with per-user
entitlement rows, RLS, a written threat model, built for a client managing many
locations with a roster of external team logins).

Innovive doesn't fit either precedent cleanly. It needs to be live and explorable
(ruling out Adherent's static-report shape), but its audience is small and fixed: Robin,
Victoria, occasionally Jamie (CEO) for the board deck. There's no multi-location
roster, no external client base beyond Innovive itself, and no self-serve signup need.
Copying Biscuits' full multi-tenant auth/entitlement machinery would be solving a
problem Innovive doesn't have. The right shape is closer to what Biscuits itself
started with before Kyle's requirements pushed it further: a small, gated internal-style
tool, not a multi-tenant product.

## 3. Architecture

- **Hosting:** Cloudflare Pages, its own dedicated project (new repo, e.g.
  `innovive-dashboard`), isolated from both the Biscuits Cafe portal and the internal
  ops dashboard.
- **Data access:** Cloudflare Pages Functions only. No third-party API credential (GA4
  service account, GSC, HubSpot private-app token, Klaviyo key, Meta Graph token, Bitly
  token) is ever shipped to the browser. This is a hard rule, not a preference: a prior
  Volado project shipped a live API key in client-side JS and had to fix it before
  launch. Every credential lives server-side, in Pages Functions environment variables.
- **Database:** a new, dedicated Supabase Postgres project, never shared with Biscuits'
  project or the internal ops-dashboard's project. Needed because the executive summary
  view requires normalized, time-series metrics across sources (trend vs. prior period,
  leads by source), which a stateless API-passthrough can't give cleanly.
- **Auth:** Cloudflare Access, gating the whole Pages site to a named email allowlist
  (Robin, Victoria, Jamie if wanted, plus Collin/Clayton). No signup flow, no
  entitlement table, no RLS policy complexity: because this database holds only
  Innovive's data and every authenticated person is entitled to see all of it, Biscuits'
  per-client entitlement model doesn't apply here and shouldn't be copied. This is
  meaningfully simpler than Biscuits' auth model by design, not by omission.
- **Frontend:** buildless vanilla JS/HTML/CSS with inline SVG charts, matching Biscuits'
  approach, to avoid build-tooling overhead for a project this size.
- **Refresh:** scheduled Supabase Edge Functions (or Cloudflare cron triggers calling
  Pages Functions) per data source, writing normalized rows into Postgres. The frontend
  never calls a third-party API directly, only Supabase through the server-side layer.

### Data model discipline (carried over from both prior builds)

- A metric's absence is stored as absent, never coerced to zero. Follow Biscuits'
  pattern: a `quality_state` field plus a nullable value column.
- Every metric row carries its own source and as-of date. There is no single
  dashboard-wide "last updated" stamp, since GA4/GSC/HubSpot/Klaviyo/social all refresh
  on different schedules.
- No causal claims from correlated data (for example, "this email drove these sales")
  without real attribution. Estimates are labeled as estimates.
- Manually-entered data (see Conference/events below) must never be silently
  overwritten or duplicated by an automated sync.

## 4. Per-source integration plan

| Source | Approach |
|---|---|
| Website performance | GA4 Data API, server-side scheduled pull. Blocked on the property decision (Section 1). |
| Trade media | Same GA4 pull, plus the Bitly API to pull actual click totals and reconcile against GA4 sessions before deciding whether the gap is bot clicks, UTM stripping, or a real tracking bug. |
| Organic search | Search Console API, direct pull. Already clean (`sc-domain:innovive.com` verified). |
| LinkedIn organic | LinkedIn's own organic-page API access is tightly gated (Marketing Developer Platform approval, unlikely to be worth pursuing at this scale). Recommend manual CSV export from LinkedIn's native analytics as the durable path, not a new Supermetrics-style dependency. |
| Instagram organic | Meta Graph API (Instagram Business/Creator account linked to a Facebook Page) can pull this directly with a long-lived token. Real automation opportunity, no manual fallback needed if Innovive's account is already a Business account. |
| X organic | X's API now gates meaningful analytics behind a paid tier. Recommend manual export unless the paid tier is already justified for other reasons. |
| Email performance | Klaviyo has a clean REST API. Reconnect with a fresh server-side API key; this is an auth fix, not an architecture problem. |
| Conference/event attendance | Replace the fragile Google Sheet with a simple form inside the dashboard itself that writes directly to Supabase. Removes the "stale since March" failure mode entirely, since there's no separate sheet to forget about. |
| Form submissions / leads | HubSpot CRM API v3, direct pull, filtered by the lead-vs-service classification work already in progress (`docs/innovive-hubspot-plan-2026-08.md`). This is the actual fix for the dead Wix-export page. |
| SurveyMonkey | Drop. Not migrated. |

## 5. Executive summary view

The specific thing Robin asked for on the 8/13 call and the old report never had:
leads by source, top and bottom performing channels, trend versus prior period. This is
the reason a normalized Supabase layer is needed at all rather than a thin API
passthrough — it's the one view that has to blend every source cleanly.

## 6. Open decisions

Resolved during the build:

- ~~GA4 property~~ — settled by access (Section 0/1). Only 544618753 exists for us.
- ~~Auth model~~ — Cloudflare Access with one-time PIN, no passwords, no signup flow.
- ~~LinkedIn / X automation~~ — manual CSV confirmed as the durable path; importer,
  templates and validation are built.

Still open, and all of them are decisions rather than work:
- **Whether to define a real GA4 key event** (a form-submission conversion). Without
  one, channels can be ranked by sessions but not by outcome. This is the highest-value
  fix on the list and takes minutes.
- Confirm Innovive's Instagram account is a Business/Creator account tied to a Facebook
  Page (required for the Graph API path); if not, that's a one-time setup step.
- LinkedIn and X: who owns the monthly export (likely Victoria, matching her existing
  conference-sheet role) and on what cadence.
- Confirm the board meeting date (Robin said October, flagged it might be November).
- Whether Jamie (CEO) wants direct access or just the board-deck export. Adding someone
  is deliberately two changes: the Access policy **and** `DASHBOARD_ALLOWED_EMAILS`.
- When to cancel Supermetrics. It now covers nothing this dashboard needs, but confirm
  Innovive is not using it elsewhere first.

## 7. Sequencing

Done 2026-08-19:

1. ~~Resolve the GA4 property decision~~ — settled by access.
2. ~~Stand up the repo, Cloudflare Pages project, and dedicated Supabase project.~~
3. ~~Build the data model~~ — metric store with quality_state, partial-period flags,
   per-row provenance, plus the events table.
4. ~~Wire GA4~~ (live) ~~, GSC and Klaviyo~~ — both written and deployed; they report
   their blocked state with the reason until credentials exist.
5. ~~Wire HubSpot~~ — written, including the deliberate lead-count refusal.
6. ~~LinkedIn/X manual-import intake~~ — importer, templates and validation built.
7. ~~Build the executive summary view.~~
8. ~~Set up Cloudflare Access.~~

Remaining, in the order that adds the most before October:

9. Grant the service account Search Console access (one click) — unlocks the only
   real long-term trend the board can be shown.
10. Define a real GA4 key event so channel performance can be measured by outcome.
11. Provision the HubSpot token, then land the lead-vs-service classification. Only
    then does "leads by source" become a number instead of an explanation.
12. Reconnect Klaviyo; provision Bitly and diagnose the click-vs-session gap.
13. Confirm the Instagram account type; set the LinkedIn/X export owner and cadence.
14. Cancel Supermetrics.
