# Innovive Marketing Dashboard: Custom Build Plan

Date: 2026-08-13
Owner: Collin Wood
Status: Draft for review, not yet started
Supersedes: `innovive-dashboard-rebuild-plan-2026-08.md` (Looker Studio rebuild option, decided against)

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

Also unresolved: the old report's GA4 numbers likely come from Innovive's original
client-owned GA4 property, not the new Volado-owned `innovive.com` property (544618753)
created 2026-07-08 after a broken-tag incident. This decision has to be made before the
GA4 integration is built, since it determines whether trend history exists at all.

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

## 6. Open decisions before build starts

- GA4 property: old client-owned vs. new Volado-owned (Section 1).
- Confirm Innovive's Instagram account is a Business/Creator account tied to a Facebook
  Page (required for the Graph API path); if not, that's a one-time setup step.
- LinkedIn and X: confirm manual-export cadence and who owns doing it (likely Victoria,
  matching her existing Conference-sheet role) versus paying to automate either.
- Confirm the board meeting date (Robin said October, flagged it might be November) to
  set the real deadline for the executive summary view.
- Who gets Cloudflare Access (Robin, Victoria, confirm whether Jamie/CEO wants direct
  access or just the board-deck export).

## 7. Sequencing

1. Resolve the GA4 property decision and the Instagram Business-account check.
2. Stand up the new repo, Cloudflare Pages project, and dedicated Supabase project.
3. Build the data model (metrics table with source/date/value/quality_state, plus the
   events table for Conference data).
4. Wire GA4, GSC, and Klaviyo first (native/clean APIs, no external blockers).
5. Wire HubSpot leads, gated on the lead-vs-service classification work landing.
6. Wire Instagram via Graph API; set up LinkedIn/X manual-import intake.
7. Build the executive summary view.
8. Set up Cloudflare Access with the confirmed email list.
9. Cancel Supermetrics once LinkedIn/Instagram/X are resolved one way or another.
