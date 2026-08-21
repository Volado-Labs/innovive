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

## What the clicks actually are

They are **email security scanners**, firing on Big4Bio's weekday newsletter
send. The hourly data makes this exact rather than a guess.

Every burst of 50 or more clicks in a single hour, 22 of them across the window,
landed at **exactly 15:00 UTC**. That is 8am Pacific, 11am Eastern. There is not
one exception.

```
2026-08-03  Mon   15:00 UTC    77        2026-08-13  Thu   15:00 UTC   104
2026-08-04  Tue   15:00 UTC    67        2026-08-14  Fri   15:00 UTC    73
2026-08-05  Wed   15:00 UTC    62        2026-08-15  Sat        none
2026-08-06  Thu   15:00 UTC   110        2026-08-16  Sun        none
2026-08-07  Fri   15:00 UTC   146        2026-08-17  Mon   15:00 UTC   160
2026-08-08  Sat        none              2026-08-18  Tue   15:00 UTC   125
2026-08-09  Sun        none              2026-08-19  Wed   15:00 UTC   107
2026-08-10  Mon   15:00 UTC    66        2026-08-20  Thu   15:00 UTC    96
```

**Weekdays only. Zero weekend spikes.** These bursts account for **81% of all
clicks**.

So the mechanism is:

1. Big4Bio sends its newsletter every weekday at 8am Pacific.
2. The Inno Plus banner is in every issue, so the same Bitly link goes out again.
3. Within the hour, sixty to a hundred and sixty corporate email security systems
   fetch that link to sandbox it before letting the message reach an inbox.
4. Bitly counts every one of those fetches as a click.

Everything else follows from that. The geography is datacenters because scanners
run in AWS and Azure regions in Frankfurt, Singapore and the Netherlands. The
missing referrer is because a scanner fetches the URL directly rather than
following it from a rendered page. The named referrers that do appear, EdgePilot,
URLsand and Proofpoint's `emailprotection.link`, are simply the scanners polite
enough to identify themselves.

### Correcting an earlier reading

At daily resolution this looked like steady background traffic with *no* send-day
spike, which pointed away from email scanning. That was an artifact of the
granularity: because the newsletter goes out every weekday, a daily total hides
the burst inside it. The hourly view shows the opposite, and it is decisive. The
conclusion that the traffic is automated was right; the reason was not.

### The remaining 19%

The clicks outside those spikes run at one to ten an hour, spread across the day
and night. That is a mixture of real readers and scanner stragglers. It is the
right order of magnitude to match GA4's 24 sessions once the cookie banner is
accounted for.

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
