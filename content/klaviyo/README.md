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

## Revision 2026-09-24, from Robin's feedback on the weekly call

**Inno+**
- The social-post photo (Victoria and a colleague at an Innorack) now sits under the
  dark header, fading out of the navy at the top and into the white body at the
  bottom. This is the "bleed / soft edges" Robin liked. The fade is baked into the
  JPEG, so it renders the same in every client, Outlook included.
- The four service callouts from her ad are rebuilt as icon tiles. At her request the
  "bellhop" figure on Expert Vivarium Management is replaced, now with a shield.
  The icons are Lucide line icons recoloured to the ad's magenta.
- "Dedicated capacity. No added FTEs. Expert operations." becomes one bold line, so
  the tiles are free for the callouts.
- The hero is clickable (`utm_content=hero-image`) so we can see whether people
  click the image or the button.

**GCC and MENA**
- One or two product shots, as Robin asked: an Innorack IVC rack and an Innocage
  cage, combined into a single image where her copy marked the hero.
- The partnership logo moves from the top to the sign-off, balancing the Innovive
  wordmark at the top. It shows Attentive Science as a real partner, not only a
  distributor.
- The first build left out the end of Robin's copy. It is now restored: Jamie's
  quote, "Let's talk about your vivarium", the sign-off and the footer line.
- Robin is rewriting this copy. The layout is the part up for review.

## Images

`build_assets.py` builds everything in `img/` from `source/`. The templates refer to
`img/...` by relative path so they preview locally. Before loading into Klaviyo,
upload the `img/` files to Klaviyo's image library and replace each `src` with the
hosted URL. Desktop comps for Robin's markup are in `comps/`.

## Open items

- **Original Inno+ photo.** The current hero is cropped from Robin's flattened social
  post, which is why it starts below the ad text. When she sends the original, point
  `INNOPLUS_PHOTO` at it and run the script again.
- **Icons.** Robin said she may send the icons from her social set. If she does, they
  replace `img/icon-*.png` at the same 96px size.
- **GCC copy.** This is Robin's rewrite, due back with her markup.
- **Colour rules.** Per Collin, 2026-09-24: no accent bars along the top or side of a
  block. Blocks are set apart by background fill only.
- **Not yet in Klaviyo.** The API key in Bitwarden (`innovive-klavio-key`) is
  read-only, and `POST /api/templates` returns 403 `permission_denied`. Loading these
  needs either a private key with template write scope, created from the Admin
  seat, or a paste into Klaviyo's code editor. Check the sender name and address
  (`organization.*`) in account settings at the same time.
- **Sending is a separate decision.** The MENA list (51 contacts, static, uploaded
  28 Aug) is cold, and the account has not sent since 14 July, so the list needs
  warming up. Robin owns the question of whether those contacts agreed to be emailed.

## Editable versions in Klaviyo (2026-09-30)

Robin wants to edit the copy inside Klaviyo, so both emails are now also built as
Klaviyo **hybrid** templates (`editor_type: USER_DRAGGABLE`) by `build_hybrid.py`,
output in `hybrid/`. Each band of copy sits in a `data-klaviyo-region` cell as a
`klaviyo-text-block`, which Klaviyo's visual editor opens as a normal text block.

| Template | Klaviyo id |
|---|---|
| Innovive GCC & MENA Intro (editable) 2026-09-30 | `UsVfpD` |
| Inno+ Drip 1 (editable) 2026-09-30 | `RCk3xz` |

- **Editable in the visual editor:** every headline, eyebrow, paragraph, the benefit
  list, the stat bar, the country list, the quote, the four Inno+ tile labels, the
  teal band, both buttons (label and link), the sign-off, the GCC product image and
  the partnership logo, and the footer lines.
- **Fixed layout:** the Innovive logo, the Inno+ hero photo (its fade is part of the
  image, and a Klaviyo image block adds side padding that would break the bleed),
  the tile icons, and the band and box colours.
- Klaviyo wraps each block in 9px/18px padding. `comp()` takes that off the
  surrounding padding so the spacing matches the code-editor versions.
- Images live in Klaviyo's image library (`cdn.klaviyomail.com/company/RcTRJX/...`).
- Unsubscribe uses `{% unsubscribe "Unsubscribe" %}`; `{% unsubscribe_url %}` breaks
  Klaviyo's template-render preview.
- To change them, edit `build_hybrid.py`, run it, then PATCH the two templates. Once
  a template is attached to a campaign, Klaviyo copies it, so later PATCHes to the
  template do not reach the campaign.
- API key: Bitwarden secret `innovive-klavyo-key-full` (full access).

### Draft campaigns (created 2026-09-30, unsent)

| Campaign | id | Audience | Template copy |
|---|---|---|---|
| GCC & MENA Intro (Volado draft, editable) | `01M3SV7W8TGQ62PX6H02HSXKBJ` | MENA (51) | `RLx46A` |
| Inno+ Drip 1 (Volado draft, editable) | `01M3SV7XR0HAK57K80HT1D62YE` | Innovive+ MA, SF, SD prospect lists + Inno+ Boston Happy Hour invitees (~1,000 before dedupe) | `VJw6FZ` |

Sender: Innovive <marketing@innovive.com>. GCC subject is Robin's option 1; the other two
options are listed above. The Inno+ prospect lists date from Feb 2023, so expect bounces,
and check them for people who have since become Inno+ clients.
