"""Build Elementor _elementor_data for the Innovive Global Presence page.

Copy source: Robin Gaffney, "Global Presence page - suggested changes and copy", 2026-09-22.
Styles mirror live pages: Inno+ hero (1364), regional-distributors (4055).
"""
import json, secrets, sys

U = "https://innovive.com/wp-content/uploads/2026/07/"
EARTH = {"url": U + "global-impact-earth-dark.webp", "id": 4254, "size": "", "alt": "", "source": "library"}

def nid():
    return secrets.token_hex(4)[:7]

def px(v):
    return {"unit": "px", "size": v, "sizes": []}

def box(t, r, b, l):
    return {"unit": "px", "top": str(t), "right": str(r), "bottom": str(b), "left": str(l), "isLinked": False}

def con(settings, *children):
    return {"id": nid(), "elType": "container", "settings": settings, "elements": list(children), "isInner": False}

def wid(kind, settings):
    return {"id": nid(), "elType": "widget", "widgetType": kind, "settings": settings, "elements": []}

def heading(text, size=40, color="#00223D", tag="h2", align="center", weight="700", lh=48, mobile=30, width=None):
    s = {"title": text, "header_size": tag, "align": align,
         "typography_typography": "custom", "typography_font_family": "Inter",
         "typography_font_size": px(size), "typography_font_weight": weight,
         "typography_line_height": px(lh), "typography_letter_spacing": px(-1.2 if size >= 36 else 0),
         "typography_font_size_mobile": px(mobile), "typography_line_height_mobile": {"unit": "em", "size": 1.2, "sizes": []},
         "title_color": color, "_margin": box(0, 0, 0, 0), "_padding": box(0, 0, 0, 0)}
    if width:
        s["_element_width"] = "initial"; s["_element_custom_width"] = px(width)
    return wid("heading", s)

def text(html, color="#4A5561", size=17, align="center", width=None):
    s = {"editor": html, "align": align,
         "typography_typography": "custom", "typography_font_family": "Inter",
         "typography_font_size": px(size), "typography_font_weight": "400",
         "typography_line_height": {"unit": "em", "size": 1.6, "sizes": []},
         "typography_font_size_mobile": px(16), "text_color": color,
         "_margin": box(0, 0, 0, 0), "_padding": box(0, 0, 0, 0)}
    if width:
        s["_element_width"] = "initial"; s["_element_custom_width"] = px(width)
        s["_element_width_mobile"] = "inherit"
    return wid("text-editor", s)

def button(label, url, align="center", external=False):
    return wid("button", {
        "text": label, "link": {"url": url, "is_external": "on" if external else "", "nofollow": ""},
        "align": align, "typography_typography": "custom", "typography_font_family": "Inter",
        "typography_font_size": px(16), "typography_font_weight": "600", "typography_line_height": px(20),
        "typography_font_size_mobile": px(14), "background_color": "#005287", "button_text_color": "#FCFBF8",
        "button_background_hover_color": "#00223D", "hover_color": "#FFFFFF",
        "border_radius": {"unit": "px", "top": "6", "right": "6", "bottom": "6", "left": "6", "isLinked": True},
        "text_padding": box(14, 22, 14, 22)})

# ---------- 1. Hero (Inno+ pattern, earth photo, no country lists) ----------
hero = con({
    "flex_direction": "column", "boxed_width": px(1400), "min_height": px(560), "min_height_mobile": px(0),
    "flex_justify_content": "flex-start", "flex_align_items": "center", "flex_gap": {"unit": "px", "size": 20, "column": "20", "row": "20"},
    "background_background": "classic", "background_color": "#0B1320", "background_image": EARTH,
    "background_position": "bottom center", "background_size": "cover",
    "padding": box(220, 40, 200, 40), "padding_tablet": box(200, 30, 160, 30), "padding_mobile": box(170, 20, 120, 20)},
    heading("INNOVIVE WORLDWIDE", size=14, color="#A8CEFF", tag="p", weight="600", lh=20, mobile=13),
    heading("Global reach. Local expertise. One Innovive Standard.", size=48, color="#FFFFFF", tag="h1", lh=58, mobile=32, width=900),
    button("Find your region", "#your-region"),
)

# ---------- 2. Intro ----------
intro_html = (
    "<p>Innovive supports scientific organizations across more than 43 countries with integrated vivarium solutions "
    "designed to deliver consistent performance, operational efficiency and dependable support to enable transformative research.</p>"
    "<p>Our customers engage with Innovive through direct regional teams and carefully selected local partners. Every relationship "
    "is backed by Innovive's product expertise, quality standards and commitment to research success.</p>"
    "<p>Wherever your research is conducted, Innovive is committed to providing the same product quality, technical expertise and "
    "customer experience. Our direct teams and authorized partners work as one network to help customers confidently implement "
    "and operate the Innovive system.</p>")
intro = con({
    "flex_direction": "column", "boxed_width": px(1400), "flex_align_items": "center",
    "background_background": "classic", "background_color": "#FFFFFF",
    "padding": box(80, 40, 40, 40), "padding_mobile": box(48, 20, 24, 20)},
    text(intro_html, width=820),
)

# ---------- 3. Proof points (stat tiles) ----------
def stat(big, label):
    return con({
        "content_width": "full", "flex_direction": "column", "flex_gap": {"unit": "px", "size": 10, "column": "10", "row": "10"},
        "width": {"unit": "%", "size": 25}, "width_tablet": {"unit": "%", "size": 50}, "width_mobile": {"unit": "%", "size": 100},
        "flex_grow": 1, "padding": box(28, 24, 28, 24), "padding_mobile": box(22, 18, 22, 18),
        "background_background": "classic", "background_color": "#FFFFFF1A",
        "border_border": "solid", "border_width": {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": True},
        "border_color": "#FFFFFF33", "border_radius": {"unit": "px", "top": "8", "right": "8", "bottom": "8", "left": "8", "isLinked": True}},
        heading(big, size=44, color="#FFFFFF", tag="p", align="left", lh=50, mobile=36),
        text(label, color="#E3EEFF", size=16, align="left"),
    )

stats_row = con({"content_width": "full", "flex_direction": "row", "flex_wrap": "wrap",
                 "flex_gap": {"unit": "px", "size": 20, "column": "20", "row": "20"}},
    stat("500+", "research organizations served"),
    stat("43", "countries with Innovive customers"),
    stat("Direct", "Innovive sales throughout the U.S. and Europe"),
    stat("4", "regions of expertise: the Americas, Europe, Asia-Pacific and the Middle East"),
)
proof = con({"flex_direction": "column", "boxed_width": px(1400), "background_background": "classic", "background_color": "#FFFFFF",
             "padding": box(40, 40, 40, 40), "padding_mobile": box(24, 20, 24, 20)},
    con({"content_width": "full", "flex_direction": "column", "flex_gap": {"unit": "px", "size": 28, "column": "28", "row": "28"},
         "background_background": "gradient", "background_color": "#00223D", "background_color_b": "#005287",
         "background_gradient_angle": {"unit": "deg", "size": 120, "sizes": []},
         "border_radius": {"unit": "px", "top": "8", "right": "8", "bottom": "8", "left": "8", "isLinked": True},
         "padding": box(56, 56, 56, 56), "padding_tablet": box(40, 30, 40, 30), "padding_mobile": box(32, 20, 32, 20)},
        heading("Innovive by the numbers", size=32, color="#FFFFFF", tag="h2", align="left", weight="600", lh=40, mobile=26),
        stats_row,
    ),
)

# ---------- 4. Innovive in Your Region (dropdowns) ----------
MAIL = '<a href="mailto:info@innovive.com">info@innovive.com</a>'
PARTNERS = [
    ("Latin America", "South &amp; Latin America", "EAD Scientific", "ead-scientific-logo-uniform.png", "https://www.eadscience.com/"),
    ("United Kingdom &amp; Ireland", "United Kingdom &amp; Ireland", "Datesand Group", "datesand-group-logo-uniform.png", "https://www.datesand.com/"),
    ("Middle East &amp; GCC", "GCC &amp; Middle East", "Attentive Science", "attentive-science-logo-uniform.png", "https://www.attentivescience.com/"),
    ("Japan", "Japan", "Oriental Giken", "oriental-logo-uniform.png", "https://en.orientalgiken.co.jp/"),
    ("South Korea", "South Korea", "LK Lab Korea", "lk-lab-korea-logo-uniform.png", "https://www.lklab.com/"),
    ("Australia &amp; New Zealand", "Australia &amp; New Zealand", "Able Scientific", "able-scientific-logo-uniform.png", "https://ablescientific.com.au/"),
]

CSS = """<style>
.gp-regions{max-width:900px;margin:0 auto;font-family:Inter,sans-serif}
.gp-regions details{background:#fff;border:1px solid #00528733;border-radius:8px;margin:0 0 12px;box-shadow:0 20px 40px rgba(15,29,40,.06)}
.gp-regions summary{list-style:none;cursor:pointer;display:flex;align-items:center;justify-content:space-between;gap:16px;padding:20px 24px;font-size:18px;font-weight:600;line-height:1.4;color:#00223D}
.gp-regions summary::-webkit-details-marker{display:none}
.gp-regions summary:focus-visible{outline:2px solid #3765F8;outline-offset:2px;border-radius:8px}
.gp-regions summary .gp-tag{font-size:13px;font-weight:500;color:#005287;background:#EAF2FF;border-radius:999px;padding:4px 12px;white-space:nowrap;margin-left:auto}
.gp-regions summary:after{content:"";flex:0 0 10px;height:10px;border-right:2px solid #005287;border-bottom:2px solid #005287;transform:rotate(45deg);margin:-4px 4px 0 4px;transition:transform .2s}
.gp-regions details[open] summary:after{transform:rotate(-135deg);margin-top:4px}
.gp-regions .gp-body{padding:0 24px 24px;display:flex;gap:24px;align-items:center;flex-wrap:wrap;color:#4A5561;font-size:16px;line-height:1.6}
.gp-regions .gp-body p{margin:0 0 8px}
.gp-regions .gp-logo{flex:0 0 180px;background:#fff;border:1px solid #E6ECF3;border-radius:6px;padding:10px;display:flex;align-items:center;justify-content:center}
.gp-regions .gp-logo img{max-width:100%;height:auto;display:block}
.gp-regions .gp-info{flex:1 1 280px}
.gp-regions .gp-actions{display:flex;flex-wrap:wrap;gap:12px 20px;align-items:center;margin-top:12px}
.gp-regions .gp-btn{display:inline-block;background:#005287;color:#FCFBF8 !important;font-weight:600;font-size:15px;line-height:20px;padding:12px 18px;border-radius:6px;text-decoration:none}
.gp-regions .gp-btn:hover{background:#00223D}
.gp-regions .gp-body a:not(.gp-btn){color:#005287;font-weight:600}
.gp-regions .gp-group{font-size:13px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#005287;margin:32px 0 12px}
@media(max-width:600px){.gp-regions summary{padding:16px 18px;font-size:16px}.gp-regions summary .gp-tag{display:none}.gp-regions .gp-body{padding:0 18px 18px}.gp-regions .gp-logo{flex-basis:100%}}
</style>"""

def partner_item(region, coverage, name, logo, url):
    return (
        f'<details><summary><span>{region}</span><span class="gp-tag">Authorized partner</span></summary>'
        f'<div class="gp-body"><div class="gp-logo"><img src="{U}{logo}" alt="{name} logo" width="180" loading="lazy"></div>'
        f'<div class="gp-info"><p><strong>{name}</strong> is Innovive\'s authorized partner for {coverage}.</p>'
        f'<div class="gp-actions"><a class="gp-btn" href="{url}" target="_blank" rel="noopener">Visit {name}</a>'
        f'<span>or contact Innovive at {MAIL}</span></div></div></div></details>')

direct_item = (
    '<details open><summary><span>U.S. and Europe: Direct from Innovive</span><span class="gp-tag">Direct</span></summary>'
    '<div class="gp-body"><div class="gp-info"><p>Customers across North America and Europe work directly with Innovive '
    'for product selection, implementation and ongoing support.</p>'
    '<div class="gp-actions"><a class="gp-btn" href="mailto:info@innovive.com">Contact info@innovive.com</a></div></div></div></details>')

regions_html = (CSS + '<div class="gp-regions">' + direct_item + '<p class="gp-group">Partner-supported regions</p>'
                + "".join(partner_item(*p) for p in PARTNERS) + "</div>")

regions = con({
    "flex_direction": "column", "boxed_width": px(1400), "flex_align_items": "center",
    "flex_gap": {"unit": "px", "size": 20, "column": "20", "row": "20"},
    "background_background": "classic", "background_color": "#F6F9FF",
    "padding": box(80, 40, 80, 40), "padding_mobile": box(48, 20, 48, 20), "_element_id": "your-region"},
    heading("Innovive in Your Region"),
    text("<p>Innovive serves customers around the world through a combination of direct operations and authorized regional partners. "
         "This approach gives research teams access to local market knowledge while maintaining a consistent Innovive experience.</p>"
         "<p><strong>Select your region to connect with the right Innovive representative.</strong></p>", width=760),
    con({"content_width": "full", "margin": box(20, 0, 0, 0)}, wid("html", {"html": regions_html})),
)

# ---------- 5. Closing CTA band (existing gradient style) ----------
cta = con({"flex_direction": "column", "boxed_width": px(1400), "background_background": "classic", "background_color": "#FFFFFF",
           "padding": box(40, 40, 80, 40), "padding_mobile": box(20, 20, 48, 20)},
    con({"content_width": "full", "flex_direction": "row", "flex_wrap": "wrap", "flex_justify_content": "space-between",
         "flex_align_items": "center", "flex_gap": {"unit": "px", "size": 24, "column": "24", "row": "24"},
         "background_background": "gradient", "background_color": "#005287", "background_color_b": "#72CAC4",
         "background_gradient_angle": {"unit": "deg", "size": 90, "sizes": []},
         "border_radius": {"unit": "px", "top": "8", "right": "8", "bottom": "8", "left": "8", "isLinked": True},
         "padding": box(48, 56, 48, 56), "padding_mobile": box(28, 20, 28, 20)},
        con({"content_width": "full", "flex_direction": "column", "width": {"unit": "%", "size": 65}, "width_mobile": {"unit": "%", "size": 100},
             "flex_gap": {"unit": "px", "size": 8, "column": "8", "row": "8"}},
            heading("Not sure who to contact?", size=32, color="#FFFFFF", align="left", weight="600", lh=40, mobile=26),
            text("<p>Tell us where your research is based and we will connect you with the right Innovive team or partner.</p>",
                 color="#FFFFFF", size=17, align="left")),
        wid("button", {**button("Contact Innovive", "/contact/")["settings"], "align": "right", "align_mobile": "left",
                       "background_color": "#FFFFFF", "button_text_color": "#00223D"}),
    ),
)

data = [hero, intro, proof, regions, cta]
json.dump(data, open(sys.argv[1], "w"), separators=(",", ":"), ensure_ascii=True)
print("ok", len(json.dumps(data)))
