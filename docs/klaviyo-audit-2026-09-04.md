# Innovive Klaviyo account audit

Read-only audit, 2026-09-04, ahead of Volado taking over email management.
Account `RcTRJX`. Report: https://claude.ai/code/artifact/3c9c9708-8937-4702-b0f0-e6313046ff38

Nothing in the account was changed. Read against the Klaviyo API (revision
`2024-10-15`) with the `innovive-klavio-key` private key, plus public DNS and a
fetch of the live site.

## The finding that outranks the rest

`innovive.com` publishes `v=DMARC1; p=quarantine`. Klaviyo mail sent From
`marketing@innovive.com` aligns with neither SPF nor DKIM, so receivers are being
told to quarantine it.

- **No Klaviyo DKIM.** `kl._domainkey` and `kl2._domainkey` are both absent. The
  only selectors published are `selector1` (legacy Microsoft 365) and `google`.
- **No Klaviyo branded sending subdomain.** Probed `em`, `e`, `mkt`, `marketing`,
  `news`, `go`, `link`, `click`, `t`, `info`, `updates`, `send`, `mail`,
  `klaviyo`, `trk`. None resolve to Klaviyo.
- **SPF omits Klaviyo:**
  `v=spf1 include:_spf.google.com include:mailsenders.netsuite.com include:amazonses.com include:_spf.brightmove.com ~all`

Every campaign this account has ever sent went out that way.

**A GCC send is queued on top of it.** List `MENA` (51 profiles) was created
2026-08-28, two days after the GCC LinkedIn campaign launched, with a matching
draft campaign `Attentive and Innovive_MENA` and a MENA template of the same
date. Hold it until the domain is authenticated.

## Corroboration in the send data

From Klaviyo's own campaign values report, last 12 months. Every full-list send
exceeds Klaviyo's 2% bounce guidance.

| Sent | Recipients | Bounce | Open | Click | Unsub | Spam |
|---|---:|---:|---:|---:|---:|---:|
| 2026-07-14 | 4,732 | 2.75% | 23.25% | 5.32% | 0.13% | 0.00% |
| 2026-06-30 | 4,835 | 4.41% | 24.79% | 9.28% | 0.24% | 0.00% |
| 2026-03-17 | 4,719 | 3.86% | 39.30% | 4.52% | 0.20% | 0.00% |
| 2026-03-04 | 963 | 5.19% | 37.02% | 6.46% | 0.44% | 0.00% |
| 2026-01-15 | 4,662 | 3.58% | 28.79% | 5.16% | 0.11% | 0.00% |
| 2025-12-16 | 4,653 | 3.37% | 35.70% | 5.47% | 0.31% | 0.00% |
| 2025-12-16 | 4,626 | 3.07% | 44.22% | 3.81% | 0.18% | 0.00% |
| 2025-11-25 | 4,666 | 5.10% | 50.34% | 3.57% | 0.18% | 0.00% |
| 2025-10-30 | 4,847 | 8.87% | 32.17% | 4.10% | 0.45% | 0.04% |

Open rate on the main list is trending down: 50.34% (Nov 2025) to 23.25% (Jul 2026).

Spam complaints are effectively zero and unsubscribes run 0.1% to 0.45%, which
rules out a content problem and leaves list decay plus authentication.

The clean sublists prove it from the other side: a 306-profile engaged survey
cohort bounced 0.98% and opened 84.82%, same account, same sender, same
infrastructure.

## What does not exist

- **0 flows.** Every message in four years was sent by hand.
- **0 live segments.** Five were built for past campaigns and deleted; they are
  still fetchable by ID (`XiFKTY`, `V7ECE8`, `WPybbi`, `U5KrJ4`, `TZsFEF`) but
  absent from the index.
- **0 signup forms.** Nothing collects an address into Klaviyo.
- **0 revenue attribution.** No ecommerce integration, no Placed Order metric.
- **No onsite script** on innovive.com. The served HTML has no
  `static.klaviyo.com` and no `RcTRJX`. The `Viewed Product` and `Active on Site`
  metrics in the account are dead history, almost certainly from the old Wix site.

## Lists

22 lists, 9,060 memberships against roughly 5,000 real people.

| Profiles | Created | List |
|---:|---|---|
| 4,985 | 2022-02-10 | Innovive Customer Contacts |
| 906 | 2026-03-03 | eCommerce Survey Respondent List (US) |
| 833 | 2023-07-19 | List of MA and ME Customers Only |
| 627 | 2023-02-10 | Innovive+ Potential Customer Contact List MA Only |
| 352 | 2025-09-25 | Innovive Cust Contacts AALAS 2025 Invite List |
| 239 | 2026-04-30 | Rat Bottom Pallet Quantity Customer List |
| 206 | 2022-02-10 | Innovive Employees |
| 162 | 2023-02-15 | Innovive+ Potential Customer Contact List San Francisco |
| 158 | 2025-12-19 | Innovive Gift Baskets Customer Contacts, US Only |
| 138 | 2024-11-14 | AALAS 2024 Innovive Booth Attendees |
| 118 | 2025-06-06 | FELASA 2025 Innovive Booth Attendees (Leads) |
| 108 | 2023-02-22 | Innovive+ Potential Customer Contacts San Diego |
| 101 | 2025-04-25 | Inno+ Boston Happy Hour Invitees |
| 51 | 2026-08-28 | MENA |
| 31 | 2025-06-27 | Disposable Water Bottle For Competitors Customer Contacts |
| 26 | 2025-09-22 | AALAS 2025 Innovive Team Attendees |
| 12 | 2025-12-22 | Innovive Gift Baskets Customer Contacts, US Only (LR) |
| 5 | 2025-10-30 | NetSuite SB1 Innovive Customer Contacts Test List |
| 1 | 2022-02-02 | Preview List (Klaviyo default) |
| 1 | 2022-02-02 | Newsletter (Klaviyo default) |
| 0 | 2025-11-04 | SMS List |
| 0 | 2024-12-05 | Innocycle Customer Contacts |

Three Inno+ **prospect** lists sit inside the customer account, so the
customer-versus-prospect separation Robin insists on is already broken in
practice.

## Other findings

- **Timezone is US/Eastern.** Innovive operates from San Diego. Every send time
  and daily rollup is displaced three hours, and disagrees with GA4.
- **Cadence declining:** 28 sends in 2023, 19 in 2024, 15 in 2025, 9 through July
  2026. Nothing in 52 days. 15 drafts unsent, several abandoned mid-build.
- Content is almost entirely operational (ECO notices, product changes, holiday
  hours). It is a customer-service channel in a marketing tool.
- 8 of 18 templates are Klaviyo's factory `Newsletter #1` to `#8` boilerplate
  from 2022-02-02.
- Account `website_url` is recorded as `http://innovive.com`, which now 301s.

## Priority order

1. Authenticate the sending domain in Klaviyo, publish the three CNAMEs, confirm
   `kl._domainkey.innovive.com` resolves. Hold the MENA send until it does.
2. Suppress hard bounces and 12-month non-openers on the main list.
3. Consolidate 22 lists into one list plus segments; delete the two Klaviyo
   defaults, the NetSuite test list and the two empty lists.
4. Add a signup form and the onsite script to innovive.com, behind CookieYes.
5. Build one flow (welcome / new customer) before building five.
6. Settle the Klaviyo versus HubSpot boundary in writing before AALAS 2026.

## Access notes

- The key is `innovive-klavio-key` in Bitwarden Secrets Manager (note the
  spelling; `docs/access-checklist.md` in the dashboard repo names it
  `innovive-klaviyo-api-key`, which does not exist).
- Reach it with `~/.local/bin/bwsx`, not the `bw` password-manager CLI, which is
  unauthenticated on this Mac and is not the path.
- The key is **broad read-only**: `accounts`, `lists`, `segments`, `flows`,
  `metrics`, `campaigns`, `templates`, `forms`, `tags` all return 200;
  `webhooks` returns 403. Managing sends will need a user seat, not this key.

## Not covered

- Klaviyo's own sending-domain screen. The DNS evidence is conclusive that no
  Klaviyo DKIM is published, but the UI is authoritative for the configured
  state and a read-only key cannot see it.
- Profile-level consent provenance for the 4,985 profiles. Matters for MENA.
- SMS (channel empty, never used).
