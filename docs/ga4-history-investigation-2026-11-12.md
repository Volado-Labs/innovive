# Innovive GA4: what happened to the history, and the traffic decline

Prepared 2026-11-12 after the weekly SEO sync, where Victoria and Robin asked why Google Analytics "stops at July", whether it can be one property, and why traffic reads about 40% down year over year. All numbers are GA4 sessions pulled live from the Innovive, LLC account (89752335) today.

## The properties in Innovive's account

| Property | ID | What it holds |
|---|---|---|
| Innovive.com - GA4 | 308021023 | The Wix site's full history, March 2022 to July 7, 2026. Stops when the Wix site was retired. |
| Innovive website | 534747623 | Created late April 2026, also on the Wix site. Same visits as 308021023 for April to July 2026 (a second tag counting the same people). Its tag G-97PG8MC1MH was never on the new site. |
| innovive.com | 544618753 | The current WordPress site, from July 8, 2026 (tag G-V8ZJQ03BE3). |
| Shop Innovive | 386609373 | The NetSuite shop. Seen by the dashboard session today; not in this export's access list, so not checked here. |

## Why the history "stops at July"

Nothing in the old property broke or was deleted. GA4 records a site only while that property's tag is on the site. Both old tags lived in the Wix site, so when innovive.com moved to WordPress on July 7 to 8, 2026, they stopped receiving visits. The new site was given a new property (544618753) because the June check found the newer old tag returning "not found" from Google. The old long-history property, 308021023, was not identified at that point, so its tag was never added to WordPress.

**Can it be one property?** GA4 cannot merge two properties after the fact. Two practical options:

1. **Dashboard (done today).** The Volado dashboard now joins 308021023 before July 8, 2026 to 544618753 from July 8, so the sessions chart and year-over-year comparisons run back to March 2022.
2. **Re-tag 308021023 on the WordPress site** alongside the current tag. Innovive's own GA would then show one continuous property from July 2026 onward, with a gap from July 8 to the day it is added. This is a production change (Code Snippets #7) and needs Collin's OK. It also needs the measurement ID of 308021023's web stream, which the reporting API does not return.

## The traffic decline

Monthly sessions, old property then new:

| Month | 2024 | 2025 | 2026 |
|---|---|---|---|
| June | 3,378 | 3,218 | 1,365 (old) |
| July | 3,413 | 2,334 | 2,272 (new, from Jul 8) + 140 (old) |
| August | 3,591 | 1,327 | 1,387 |
| September | 3,474 | 1,345 | 1,559 |
| October | 4,293 | 1,713 | 1,285 |
| November (to date) | 3,989 | 1,345 | 574 through Nov 11 |

**The drop happened in July 2025, a year before the new website.** Weekly sessions went from 600 to 800 a week to about 300 a week in the week of July 21, 2025, and stayed there. It hit every channel and every page at once: Organic Search fell from about 2,050 to 914 a month, Direct from about 950 to 305, and the home page, /mouse-caging and /innorack-mouse all roughly halved together.

A real loss of rankings shows up gradually and in some pages first. An overnight halving across every channel and page is the signature of a measurement change on the old Wix site, for example a cookie consent banner or consent mode being switched on, or a duplicate tag being removed. Search Console's earliest available days (from July 20, 2025) show about 50 search clicks on a weekday, in line with the lower GA level rather than the higher one. Search Console data from before July 20, 2025 is no longer available, so the cause cannot be confirmed from Google's side. **Worth asking Innovive:** did anything change on the Wix site around July 21, 2025 (cookie banner, Wix analytics settings, a tag or app removed)?

**Since the new site launched, traffic is roughly level with last year, not 40% down:** August +5%, September +16%, October −25%, with November on pace for about 1,550 (vs 1,345). A 40% to 60% gap appears only when comparing against 2024 or the first half of 2025, before the July 2025 step change. Comparing across that change overstates the decline.

**Caveat on the new site:** innovive.com counts only visitors who accept analytics cookies (CookieYes opt-in), so it undercounts compared with a site with no banner. That is the likely kind of change that hit the Wix site in July 2025.

## Open items

- Ask Innovive what changed on the Wix site around July 21, 2025.
- Collin to decide whether to add 308021023's tag to WordPress (option 2).
- Madison's access: Victoria offered to ask whether she changed anything. Not needed to explain the July 2026 stop; may matter for July 2025.
