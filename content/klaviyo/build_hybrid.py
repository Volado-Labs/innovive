"""Build the Klaviyo *hybrid* versions of the two emails.

A hybrid template is our HTML with `data-klaviyo-region` cells. Klaviyo turns
each `klaviyo-block` inside a region into a normal drag-and-drop block, so Robin
can edit the copy in Klaviyo's visual editor without touching code. Anything
outside a region (band colours, the tile grid, the logo) stays fixed layout.

Copy is Robin's, as in the code-editor versions (gcc-mena-intro.html,
inno-plus-drip-1.html). Images point at Klaviyo's CDN (uploaded 2026-09-30).

    python3 build_hybrid.py   ->  hybrid/gcc-mena-intro.html, hybrid/inno-plus-drip-1.html
"""
from pathlib import Path

CDN = "https://cdn.klaviyomail.com/company/RcTRJX/images/"
IMG = {
    "logo": CDN + "11e61cfa-8c67-49e3-a321-41e8666821e5.png",
    "partner": CDN + "e8a5b565-96a5-44be-95cd-232f219f554d.png",
    "gcc": CDN + "e0efed5a-0ad6-477f-ba18-a051e6e0422a.jpeg",
    "hero": CDN + "bc32d7a9-a044-49a6-aee1-d502d2eef66c.jpeg",
    "husbandry": CDN + "265e3a24-e917-49e0-9e66-bb55e22f806d.png",
    "health": CDN + "e459bf12-da3e-4935-b212-56fe1b1c61c8.png",
    "management": CDN + "17662f4f-780b-437e-a694-05cddf9a0e2a.png",
    "research": CDN + "527ab145-d1dd-4f22-881d-bd3f4c76fb8f.png",
    # Robin's final Inno+ Vivarium Solutions logo, white version (10/9), 360px for 2x.
    "innoplus_logo": CDN + "277223df-cd27-4463-a90a-2af349386531.png",
}

FONT = "Inter,'Helvetica Neue',Helvetica,Arial,sans-serif"
TEXT = "#242d28"
MUTED = "#5a6472"


def utm(url, campaign, content=None):
    sep = "&amp;" if "?" in url else "?"
    q = f"utm_source=klaviyo&amp;utm_medium=email&amp;utm_campaign={campaign}"
    if content:
        q += f"&amp;utm_content={content}"
    return f"{url}{sep}{q}"


def p(text, size=16, lh=26, color=TEXT, mb=16, extra=""):
    return (f'<p style="margin:0 0 {mb}px 0; font-family:{FONT}; font-size:{size}px; '
            f'line-height:{lh}px; color:{color};{extra}">{text}</p>')


def h(text, tag="h2", size=20, lh=28, color="#1b216b", mb=8):
    return (f'<{tag} style="margin:0 0 {mb}px 0; font-family:{FONT}; font-size:{size}px; '
            f'line-height:{lh}px; color:{color}; font-weight:700;">{text}</{tag}>')


def button(label, href, bg):
    return (f'<p style="margin:0; text-align:center;"><a href="{href}" style="display:inline-block; '
            f'padding:15px 36px; background-color:{bg}; border-radius:4px; font-family:{FONT}; '
            f'font-size:16px; line-height:20px; font-weight:700; color:#ffffff; text-decoration:none;">'
            f'{label}</a></p>')


def fixed_button(label, href, bg, pad):
    """A button row outside any editable region, so the visual editor cannot restyle it."""
    return f'''
  <tr>
    <td class="px" align="center" style="padding:{pad}; background-color:#ffffff;">
      {button(label, href, bg)}
    </td>
  </tr>'''


def text_block(html):
    return f'<div class="klaviyo-block klaviyo-text-block">{html}</div>'


def image_block(src, alt, width, href=None):
    img = (f'<img src="{src}" alt="{alt}" width="{width}" '
           f'style="display:block; width:100%; max-width:{width}px; height:auto; border:0;">')
    if href:
        img = f'<a href="{href}">{img}</a>'
    return f'<div class="klaviyo-block klaviyo-image-block">{img}</div>'


# Klaviyo wraps every block in 9px (top/bottom) and 18px (left/right) of padding.
# Callers give the spacing they want to SEE; comp() takes the block padding off.
BLOCK_V, BLOCK_H = 9, 18


def comp(pad):
    v = [int(x.replace("px", "")) for x in pad.split()]
    t, r, b, l = {1: v * 4, 2: [v[0], v[1], v[0], v[1]], 4: v}[len(v)]
    t, b = max(t - BLOCK_V, 0), max(b - BLOCK_V, 0)
    r, l = max(r - BLOCK_H, 0), max(l - BLOCK_H, 0)
    return f"{t}px {r}px {b}px {l}px"


def region(blocks, width, bg="#ffffff", pad="0 32px"):
    """A band of the email whose contents Robin can edit in Klaviyo."""
    pad, width = comp(pad), width + 2 * BLOCK_H
    return f'''
  <tr>
    <td class="px" style="padding:{pad}; background-color:{bg};">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
        <tr>
          <td align="left" data-klaviyo-region="true" data-klaviyo-region-width-pixels="{width}">
            {"".join(blocks)}
          </td>
        </tr>
      </table>
    </td>
  </tr>'''


def boxed(blocks, width, box_bg, pad="0 32px", inner_pad="18px 24px", align="left"):
    """A tinted box (stat bar, quote, country list) whose text stays editable."""
    inner_pad, width = comp(inner_pad), width + 2 * BLOCK_H
    return f'''
  <tr>
    <td class="px" style="padding:{pad}; background-color:#ffffff;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{box_bg}; border-radius:6px;">
        <tr>
          <td align="{align}" style="padding:{inner_pad};" data-klaviyo-region="true" data-klaviyo-region-width-pixels="{width}">
            {"".join(blocks)}
          </td>
        </tr>
      </table>
    </td>
  </tr>'''


def logo(width):
    return f'''
  <tr>
    <td class="px" align="left" style="padding:26px 32px 18px 32px; background-color:#ffffff;">
      <img src="{IMG["logo"]}" width="{width}" alt="Innovive" style="display:block; width:{width}px; max-width:{width}px; height:auto; border:0;">
    </td>
  </tr>'''


def footer(extra_line=""):
    lines = []
    if extra_line:
        lines.append(p(extra_line, 12, 19, MUTED, 8))
    lines.append(p("{{ organization.name }}<br>{{ organization.full_address }}", 12, 19, MUTED, 8))
    return lines


def shell(title, preheader, rows):
    pad = "&#847;&zwnj;&nbsp;" * 12
    return f'''<!DOCTYPE html>
<html lang="en" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="x-apple-disable-message-reformatting">
<title>{title}</title>
<!--[if mso]>
<xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml>
<![endif]-->
<style>
  @media only screen and (max-width:620px) {{
    .wrap {{ width:100% !important; }}
    .px {{ padding-left:22px !important; padding-right:22px !important; }}
    .col {{ display:block !important; width:100% !important; padding:0 0 10px 0 !important; }}
  }}
</style>
</head>
<body style="margin:0; padding:0; background-color:#eef2f7;">
<div style="display:none; max-height:0; overflow:hidden; mso-hide:all; font-size:1px; line-height:1px; color:#eef2f7;">{preheader} {pad}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#eef2f7;">
<tr><td align="center" style="padding:24px 12px;">
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px; max-width:600px; background-color:#ffffff; border-radius:6px; overflow:hidden;">
{"".join(rows)}
</table>
</td></tr>
</table>
</body>
</html>
'''


def strong(t):
    return f'<strong style="color:#1b216b;">{t}</strong>'


def gcc():
    c = "gcc-mena-intro"
    bullets = [
        ("No washroom required.", "Cages arrive pre-bedded and irradiated, with pre-filled water, ready to use. There&rsquo;s no cage-wash infrastructure to build or staff."),
        ("Lower capital, space and labor costs.", "Free up capital, square meters, utilities and staff hours compared with conventional reusable caging."),
        ("Scales with your research.", "The same system works for early-stage biotechs, pharma, CROs and academic institutions."),
        ("Inno+ vivarium services.", "Our trained technicians can support your in vivo team inside your facility, and Attentive Science is working with us to bring this service to the region."),
        ("Closed-loop recycling.", "Used cages are recycled through our InnoCycle program, which can support your sustainability goals."),
    ]
    bullet_html = "".join(
        p(f"{strong(b)} {t}", mb=14 if i < len(bullets) - 1 else 0,
          extra=" padding-bottom:14px; border-bottom:1px solid #e6ebf2;" if i < len(bullets) - 1 else "")
        for i, (b, t) in enumerate(bullets))
    stat = lambda big, small: f'<strong style="color:#1b216b;">{big}</strong> <span style="color:{MUTED};">{small}</span>'
    rows = [
        logo(150),
        region([text_block(
            p("Now serving the Middle East", 12, 16, "#f47b2e", 10,
              " letter-spacing:1.4px; text-transform:uppercase; font-weight:700;")
            + h("Research-ready vivariums, now local to the GCC &amp; MENA", "h1", 30, 38, mb=14)
            + p("Dear {{ first_name|default:'Colleague' }},")
            + p("Innovive&rsquo;s single-use, wash-free IVC systems are now available across the region. We&rsquo;ve signed a distribution and co-marketing agreement with Attentive Science Ltd., a life-science solutions provider headquartered in Masdar City, Abu Dhabi. The goal is simple: give research institutions here the same caging and vivarium support that more than 500 facilities around the world already rely on.", mb=8)
        )], 536),
        region([image_block(IMG["gcc"], "An Innorack IVC rack filled with Innocage single-use cages, and an Innocage cage shown in parts", 536, utm("https://innovive.com/", c, "product-image"))], 536, pad="8px 32px 0 32px"),
        boxed([text_block(p(
            f"{stat('20+ years', 'since 2004')} &nbsp;&middot;&nbsp; {stat('500+ clients', 'worldwide')} &nbsp;&middot;&nbsp; {stat('8 countries', 'in the region')}",
            14, 22, TEXT, 0, " text-align:center;"))], 488, "#f4f7fc", pad="18px 32px 6px 32px", inner_pad="14px 24px", align="center"),
        region([text_block(
            h("What Innovive brings to your facility")
            + p("Our patented system is built to take cage washing out of the vivarium, so your team spends its time on the science.", mb=18)
            + bullet_html
        )], 536, pad="26px 32px 0 32px"),
        region([text_block(
            h("Local supply and support")
            + p("Attentive Science distributes Innovive&rsquo;s full portfolio of caging systems, racks and consumables in:", mb=0)
        )], 536, pad="26px 32px 14px 32px"),
        boxed([text_block(p("United Arab Emirates &middot; Saudi Arabia &middot; Qatar &middot; Bahrain<br>Oman &middot; Kuwait &middot; Egypt &middot; Jordan",
                            15, 24, "#ffffff", 0, " text-align:center; font-weight:600;"))],
              500, "#1b216b", inner_pad="16px 18px", align="center"),
        region([text_block(p("Attentive Science&rsquo;s vivarium in Masdar City is our demonstration site for the region, where you can see the system working before you commit.", mb=0))],
               536, pad="14px 32px 0 32px"),
        boxed([text_block(
            p("&ldquo;This partnership represents a major milestone in Innovive&rsquo;s international growth strategy. Attentive Science brings deep regional expertise, regulatory knowledge, and a state-of-the-art vivarium facility that will serve as a premier demonstration site for our technology in the Middle East.&rdquo;",
              color="#1b216b", mb=12, extra=" font-style:italic;")
            + p(f"{strong('Jamie Blose, Pharm.D., MBA, JD')}<br>Chief Executive Officer, Innovive", 13, 20, MUTED, 0)
        )], 488, "#f4f7fc", pad="28px 32px 0 32px", inner_pad="22px 24px"),
        region([text_block(
            h("Let&rsquo;s talk about your vivarium")
            + p("Whether you&rsquo;re planning a new facility, expanding capacity or rethinking cage wash, our team can help. You can also arrange a visit to the Masdar City demonstration site or request a quote.", mb=24)
            + button("Contact us", utm("https://innovive.com/contact/", c, "cta-button"), "#f47b2e")
            + p(f'<a href="mailto:info@innovive.com" style="color:#3765f8;">info@innovive.com</a> &nbsp;&middot;&nbsp; or visit <a href="{utm("https://innovive.com/", c, "text-link")}" style="color:#3765f8;">innovive.com</a>',
                15, 24, MUTED, 0, " margin-top:14px; text-align:center;")
        )], 536, pad="28px 32px 0 32px"),
        region([text_block(
            p("We look forward to supporting the region&rsquo;s growing research community.")
            + p(f"Warm regards,<br>{strong('The Innovive Team')}", mb=0)
        ), image_block(IMG["partner"], "Innovive and Attentive Science", 150)], 536, pad="30px 32px 32px 32px"),
        region([text_block("".join(footer("Innovive, San Diego, CA &middot; In partnership with Attentive Science Ltd., Masdar City, Abu Dhabi &middot; info@innovive.com"))
                           + p('You are receiving this because you expressed interest in Innovive or Attentive Science. {% unsubscribe "Unsubscribe" %}', 12, 19, MUTED, 0))],
               536, bg="#f4f7fc", pad="22px 32px 26px 32px"),
    ]
    return shell("Innovive is now in the GCC &amp; MENA",
                 "Single-use, wash-free IVC systems now available across the UAE, Saudi Arabia, Qatar, Bahrain, Oman, Kuwait, Egypt and Jordan.",
                 rows)


def innoplus():
    c = "innoplus-drip-1"
    navy = "#081831"

    def tile(icon, label):
        return f'''<td class="col" width="50%" valign="top" style="padding:0 5px 10px 5px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{navy}; border-radius:6px;">
              <tr>
                <td width="44" valign="middle" style="padding:14px 0 14px 16px;"><img src="{IMG[icon]}" width="44" height="44" alt="" style="display:block; width:44px; height:44px; border:0;"></td>
                <td valign="middle" style="padding:0 0 0 0;" data-klaviyo-region="true" data-klaviyo-region-width-pixels="200">
                  {text_block(p(label, 15, 20, "#ffffff", 0, " font-weight:700;"))}
                </td>
              </tr>
            </table>
          </td>'''

    tiles = f'''
  <tr>
    <td class="px" style="padding:0 27px 22px 27px; background-color:#ffffff;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
        <tr>{tile("husbandry", "Daily Husbandry &amp; Animal Care")}{tile("health", "Health Monitoring &amp; Reporting")}</tr>
        <tr>{tile("management", "Expert Vivarium Management")}{tile("research", "Research Technical Services")}</tr>
      </table>
    </td>
  </tr>'''

    hero = f'''
  <tr>
    <td style="padding:0; background-color:{navy}; line-height:0; font-size:0;">
      <a href="{utm("https://innovive.com/inno-plus/", c, "hero-image")}"><img src="{IMG["hero"]}" alt="Two Innovive vivarium technicians checking a cage together on an Innorack" width="600" style="display:block; width:100%; max-width:600px; height:auto; border:0;"></a>
    </td>
  </tr>'''

    rows = [
        logo(140),
        # The Inno+ logo replaces the "Inno+ Services" eyebrow (Robin, 10/5). Fixed
        # layout, like the Innovive logo, so it cannot be dragged out of place.
        f'''
  <tr>
    <td class="px" align="left" style="padding:30px 32px 0 32px; background-color:{navy};">
      <img src="{IMG["innoplus_logo"]}" width="180" alt="Inno+ Vivarium Solutions" style="display:block; width:180px; max-width:180px; height:auto; border:0;">
    </td>
  </tr>''',
        region([text_block(
            h("Your research has grown. Your vivarium space should, too.", "h1", 29, 37, "#ffffff", 10)
            + p("Your vivarium. Our care experts.", 15, 24, "#c9d6e6", 0)
        )], 536, bg=navy, pad="22px 32px 4px 32px"),
        hero,
        region([text_block(
            p("Shared vivarium space can get you started. But as your research grows, limited availability, variable care, and competing priorities can become barriers to scale.")
            + p("Inno+ gives you dedicated vivarium capacity in your facility&mdash;without the need to build out an internal vivarium team.", mb=22)
            + p(f'Dedicated capacity. <span style="color:#0f7d78;">No added FTEs.</span> Expert operations.', 17, 26, navy, 22, " font-weight:700;")
            + p("Our vivarium professionals work directly in your facility to manage daily operations, care, compliance, and oversight&mdash;so your scientists can stay focused on discovery.", mb=0)
        )], 536, pad="28px 32px 22px 32px"),
        tiles,
        boxed([text_block(p("Your space. Our vivarium expertise.<br>More room for science.", 19, 28, navy, 0, " text-align:center; font-weight:700;"))],
              496, "#46d6cd", pad="0 32px 6px 32px", inner_pad="22px 20px", align="center"),
        region([text_block(
            p("Scale your animal research program while keeping overhead lean and operations consistent.", mb=0)
        )], 536, pad="22px 32px 0 32px"),
        # The button sits outside any editable region. Editing its label in Klaviyo's
        # visual editor (2026-10-02) turned it into highlighted text with half the
        # label outside the link, so it is fixed layout now. Label per Robin's edit.
        fixed_button("Discover Inno+", utm("https://innovive.com/inno-plus/", c), "#1b216b", pad="17px 32px 0 32px"),
        region([text_block(
            p('or contact <a href="mailto:innoplus@innovive.com" style="color:#3765f8;">innoplus@innovive.com</a>', 15, 24, MUTED, 0, " text-align:center;")
        )], 536, pad="14px 32px 28px 32px"),
        region([text_block("".join(footer()) + p('{% unsubscribe "Unsubscribe" %}', 12, 19, MUTED, 0))],
               536, bg="#f4f7fc", pad="22px 32px 26px 32px"),
    ]
    return shell("Outgrown your shared vivarium space?",
                 "Get dedicated capacity and vivarium expertise, without adding FTEs.", rows)


if __name__ == "__main__":
    out = Path(__file__).parent / "hybrid"
    out.mkdir(exist_ok=True)
    (out / "gcc-mena-intro.html").write_text(gcc())
    (out / "inno-plus-drip-1.html").write_text(innoplus())
    print("wrote", *sorted(p.name for p in out.iterdir()))
