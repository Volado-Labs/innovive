# Klaviyo email templates

Built 2026-09-24 from Robin's copy (emails of 2026-09-22). Copy is hers, used verbatim;
the HTML, structure and styling are ours.

| File | Campaign | Robin's source |
|---|---|---|
| `gcc-mena-intro.html` | GCC and MENA introduction, cold list | `Innovive-GCC-MENA-Intro-Email.docx` |
| `inno-plus-drip-1.html` | Inno+ drip, email 1 | `Innoplus Klayvio email.docx` plus the Inno+ ad as design reference |

## Subject lines and preview text

**GCC and MENA.** Robin gave three subject options; she picks.

1. Innovive is now in the GCC & MENA
2. Wash-free vivariums arrive in the Middle East
3. Innovive + Attentive Science: research-ready caging, now local

Preview text: *Single-use, wash-free IVC systems now available across the UAE, Saudi Arabia, Qatar, Bahrain, Oman, Kuwait, Egypt and Jordan.*

**Inno+ email 1.** Subject: *Outgrown your shared vivarium space?*
Preheader: *Get dedicated capacity and vivarium expertise, without adding FTEs.*

## How these are built

- Table-based, 600px, inline styles, with a `<style>` block only for the mobile
  overrides. Nothing depends on CSS a mail client might strip.
- Inter with Helvetica and Arial fallbacks, matching the site.
- Brand colours: navy `#1b216b`, blue `#3765f8`, orange `#f47b2e` for the GCC call
  to action, body text `#242d28`. The Inno+ email uses the darker navy `#081831`
  and the aqua `#46d6cd` sampled from Robin's ad, since that sub-brand has its own
  palette.
- Klaviyo tags: `{{ first_name|default:'Colleague' }}`, `{{ organization.name }}`,
  `{{ organization.full_address }}` and `{% unsubscribe %}`. The address block comes
  from account settings rather than being hardcoded.
- Links carry `utm_source=klaviyo` with a per-campaign `utm_campaign`, so the
  dashboard can attribute clicks.

## Open items

- **Hero image, GCC.** Robin's copy calls for a hero of the Innorack IVC caging
  system. Not chosen yet, so the partnership badge stands in for now, at 240px.
- **Photos, Inno+.** Robin asked for photos of Innovive ACTs advising researchers.
  There is a marked placeholder in the HTML where the chosen image drops in.
- **Not yet in Klaviyo.** The API key in Bitwarden (`innovive-klavio-key`) is
  read-only: `POST /api/templates` returns 403 `permission_denied`. Loading these
  needs either a private key with template write scope, created from the Admin
  seat, or a paste into Klaviyo's code editor.
- **Sending is a separate decision.** The GCC list is cold and the account has not
  sent since 14 July, so a warm-up matters. Nobody has confirmed where the 51 MENA
  contacts came from or whether they agreed to be emailed.
