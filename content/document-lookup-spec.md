# Document Lookup Tool — Technical Spec & Migration Notes

Compiled 2026-06-11 from: live testing with Rasan's sample lots, the app's front-end source, the 4/14 Rasan Aycox meeting (Fireflies 01KP6AGNGNH67TKB06CWBA84FR), and the "Innovive.com Document Look-up page" email thread.

## What it is
Customers enter a **lot number** and download the **Certificate of Irradiation (COI)** for their Innovive product. Certificates originate from **NextBeam** (sterilization vendor); Innovive staff manually download them from NextBeam's portal and upload to a Google Drive folder. Built and administered by **Doug Reese (doug@innovive.com)** — Innovive's Google Workspace admin (contractor). Support contact shown to users: coi@innovive.com.

## Architecture (verified live 6/11)
- Wix page /document-lookup embeds an **iframe**: `https://certificates.innovive.com/`
- That app is a small custom web app on **Google Cloud** (App Engine/Cloud Run — "Google Frontend" headers), Material Design Lite + jQuery front end
- **Two endpoints:**
  - `GET /lotSearch?lot=<lot>` → JSON array of `{doc_id, run_id, lot: [covered lots], file}` or the strings `INVALID` / `NOT FOUND`
  - `GET /download?doc_id=<id>` → serves the certificate PDF (verified: 360KB PDF, application/pdf)
- One COI covers an entire irradiation run (~27 lots per doc). Exact lot → 1 result; 5-digit prefix → multiple results.

## Verified test results (Rasan's sample lots, 4/14 email)
| Lot | Result |
|---|---|
| 35337-05 | 1 doc: COI-2026-03-18-5 WONB15553 MVX1.pdf |
| 35337-03 | same doc as above (same run) |
| 34215-10 | 1 doc: COI-2025-09-25-5 WONB13825 MVX1.pdf |
| 34302-04 | same doc as 34215-10 (same run) |
| 35337 (prefix) | 2+ docs (multiple runs) |
| 99999-99 | `INVALID` → UI shows "Lot not found." |

## UX flow (current)
1. Page instructions: enter lot in format `######-#`, submit; multiple entries may return; fallback to first 5 digits; persistent issues → coi@innovive.com
2. Form: single text input + Submit (Enter key also submits)
3. Results: "Found N document(s)" + table rows: [Download link] [filename]
4. Download opens PDF in new tab

## WordPress migration options
1. **Easiest (recommended for launch):** iframe `https://certificates.innovive.com/` into a WP page, same as Wix does. Zero backend work, zero risk; the app is independent of Wix entirely. Just match iframe height/styling + copy the instruction text.
2. Native WP integration (post-launch option): small JS block calling `lotSearch` directly (no iframe) — needs CORS check on the app, ask Doug.
3. Rebuild (Doug floated "maybe a different path... AI"): out of scope for launch.

## Open items / for the Doug call
- Who owns/pays for the Google Cloud project hosting certificates.innovive.com; is it tied to Wix in ANY way (believed: no)
- CORS policy if we want native embed (option 2)
- Internal automation (NextBeam API → Drive) is Innovive's internal wish — not a website launch dependency
- Victoria wants the tool linked in TWO places (footer + ?) — footer slot reserved
- DNS: certificates.innovive.com must be preserved during any DNS changes at launch ⚠️

## Thread status
Rasan delivered sample lots + Doug intro 4/14 (email UNREAD in inbox, "Re: Innovive.com Document Look-up page"). No reply sent; no Doug meeting has occurred. Needs a revival email before launch.
