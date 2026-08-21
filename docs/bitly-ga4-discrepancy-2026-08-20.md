# Why Bitly and Google Analytics disagree

Answered 2026-08-20, for Victoria's question on the 8/20 call: *"So is our Google
Analytics not tracking things accurately?... which one is correct?"*

**Short answer: both are correct, and nothing is broken.** They count different
things. Bitly counts redirect hits. Google Analytics counts visits. The gap
between them is automated traffic.

## The two links

| | Bitly hits | GA4 sessions | GA4 users | Engaged |
|---|---|---|---|---|
| Big4Bio San Diego banner | 4,084 | 9 | 6 | 5 |
| Big4Bio SF Bay banner | 6,334 | 15 | 13 | 3 |
| **Total** | **10,418** | **24** | **19** | **8** |

Roughly 430 redirect hits per real visit.

## The reassuring part, first

**The UTM tags arrive in Google Analytics intact.** GA4 records both campaigns
correctly, as `big4bio_sandiego` and `big4bio_sfbay`, medium `email`, campaign
`innoplus_vivarium_solutions`. Nothing is being stripped, mislabeled or lost.

Whatever else is true, Google Analytics is not failing to track these.

## Four pieces of evidence that the extra hits are machines

**1. There is no send-day spike.** A newsletter produces a hard spike on the day
it goes out, then decays. These do not. Clicks arrive at a steady 50 to 70 a day
across 84 to 88 separate days, and the two biggest days together account for only
5 to 6 percent of the total. That is not how people read email.

**2. It is still happening now.** The SF Bay link took 111 hits in the last 24
hours, months after the newsletter went out. Nobody is clicking a June banner ad
today.

**3. The geography does not match the audience.** These are newsletters for San
Diego and the San Francisco Bay Area. Germany accounts for 18 to 20 percent of
hits and Singapore a further 6 percent, with the Netherlands behind them. Those
are the major cloud datacenter regions, not the readership of a Californian life
sciences newsletter.

**4. Almost none of it carries a referrer.** Between 86 and 95 percent of hits
arrive with no referring page at all. The identifiable referrers that do appear
are Big4Bio's Campaign Monitor sending domains (`createsend1`, `cmail19`,
`cmail20`), which account for only 4 to 14 percent, plus a visible tail of email
security scanners: EdgePilot, URLsand and Proofpoint's `emailprotection.link`.

Those named scanners are simply the ones that identify themselves. The unlabeled
majority behaves identically.

## What this means in practice

- **Do not report Bitly clicks as engagement or reach.** For these placements the
  number is inflated by more than two orders of magnitude.
- **Google Analytics sessions are the honest measure of people.** With one
  qualification below.
- **The banner ads produced very little.** 24 sessions and 8 engaged sessions
  across two placements. That is the real result, and it is worth knowing before
  the next media buy rather than after.

## One qualification, stated plainly

The website's cookie banner gates Google Analytics, so GA4 only counts visitors
who accepted analytics cookies. Real human clicks are therefore somewhat higher
than 24, plausibly two or three times that. Nothing about that closes a gap of
10,418 to 24.

## What would settle it beyond doubt

Server logs for the landing page, which would show every request including the
ones GA4 never sees. If that ever matters enough, SiteGround can provide them.
The evidence above is strong enough that it probably does not.
