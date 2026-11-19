# Klaviyo: Where the Account Stands and What We Recommend

Volado Labs, 2026-09-21. Nothing has been changed in the account. Every number is a read-only measurement taken today.

## The short version

The account is healthy where it is hard to fix and unhealthy where it is easy to fix. The sending domain is authenticated. Content is not the problem: spam complaints are effectively zero and unsubscribes run 0.1% to 0.45%. List hygiene is the problem, and it costs deliverability on every send. The account has also been quiet since 14 July.

We recommend cleaning the lists before the next campaign, then consolidating 22 lists into one list plus segments. Both need your approval first.

## What we measured

22 lists, 9,074 memberships, **6,386 actual people** (30% duplicates). Main list 4,999. Zero flows, zero signup forms, zero saved segments, 17 unsent drafts.

Klaviyo advises keeping bounces under 2%. Every full-list send in the past year:

| Date | Recipients | Bounce | Open |
|---|---|---|---|
| 2025-10-30 | 4,847 | 8.87% | 32.17% |
| 2025-11-25 | 4,666 | 5.10% | 50.34% |
| 2026-01-15 | 4,662 | 3.58% | 28.79% |
| 2026-06-30 | 4,835 | 4.41% | 24.82% |
| 2026-07-14 | 4,732 | 2.75% | 23.25% |

Open rate on the main list fell from 50.34% to 23.25% in ten months.

**The counter-example, same account:** in March, a send to 306 engaged survey respondents bounced **0.98%** and opened **84.82%**, the same week a 963-recipient send bounced 5.19%. The difference was who was on the list. The account can deliver excellently today, as soon as it stops mailing addresses that no longer exist.

## Correction to what we sent on 4 September

Our 4 September email said Klaviyo mail was not authenticated against innovive.com and asked you to publish three DNS records. **That was wrong.** email.innovive.com is Active, delegated to Klaviyo's nameservers, and the DKIM keys resolve. No DNS work is needed and the request to Doug Reese can be dropped.

The rest of the report we sent holds, re-verified today: no automation of any kind, no way to capture an address on the website, three Inno+ prospect lists sitting inside the customer account, the employee list (206) alongside customer lists, account timezone on US/Eastern for a San Diego business, and no revenue attribution.

## Recommendations

1. **Clean before the next send.** Suppress hard bounces and twelve-month non-openers. Klaviyo auto-suppressed 604 hard bounces this year, so the decay is ongoing. Bounce rate should land under 2% and open rates rise immediately.
2. **Consolidate 22 lists into one plus segments.** Event uploads become segments. Retire the four empty or test lists, and keep the employee list (206) out of marketing sends by rule rather than by memory. This is effectively irreversible, so we want it agreed in writing.
3. **Correct the timezone** to US/Pacific so reporting reconciles with GA4. Historical reports shift three hours once.
4. **Automation comes after, not now.** Once the list is clean, the first build is a single welcome flow plus a signup form behind CookieYes. We will bring that proposal separately.

## What we need from you

1. Approval to suppress hard bounces and twelve-month non-openers.
2. Approval of the consolidation plan, and a decision on whether Inno+ prospects belong in Klaviyo or HubSpot.
3. Confirmation that the employee list is excluded from marketing sends.
4. Approval to correct the timezone.

One thing to settle separately: nothing connects Klaviyo to an order or to HubSpot, so it can tell you who opened something but not what it was worth. Worth agreeing what success means for this channel before setting a target.
