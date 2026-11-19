"""Global Presence page, native Elementor build (alternative to the HTML-widget build on page 4349).

Everything is standard Elementor widgets except the animated map, which stays one HTML widget.
Copy and images match gp_sections.py so the two builds can be compared like for like.
"""
import json, re, secrets, sys
import gp_sections as g

M = json.load(open("media.json"))
NAVY, DEEP, INK, CTA, SKY, ORANGE, MIST, LINE, MUTED = "#1B216B", "#0A0F3D", "#0E1733", "#005287", "#A8CEFF", "#F47B2E", "#F4F7FD", "#E1E7F2", "#56607A"

def nid(): return secrets.token_hex(4)[:7]
def px(v, u="px"): return {"unit": u, "size": v, "sizes": []}
def box(t, r=None, b=None, l=None, u="px"):
    r = t if r is None else r; b = t if b is None else b; l = r if l is None else l
    return {"unit": u, "top": str(t), "right": str(r), "bottom": str(b), "left": str(l), "isLinked": t == r == b == l}
def gap(v): return {"unit": "px", "size": v, "column": str(v), "row": str(v), "isLinked": True}
def rad(v): return box(v)
def img(k): return {"url": M[k]["url"], "id": M[k]["id"], "size": "", "alt": "", "source": "library"}

def con(s, *kids, inner=True):
    base = {"content_width": "full", "flex_direction": "column", "padding": box(0), "margin": box(0), "flex_gap": gap(0)}
    base.update(s)
    return {"id": nid(), "elType": "container", "isInner": inner, "settings": base, "elements": list(kids)}

def section(s, *kids):
    base = {"content_width": "boxed", "boxed_width": px(1280), "flex_direction": "column",
            "padding": box(128, 40, 128, 40), "padding_tablet": box(96, 30, 96, 30), "padding_mobile": box(72, 20, 72, 20),
            "margin": box(0), "flex_gap": gap(0)}
    base.update(s)
    return {"id": nid(), "elType": "container", "isInner": False, "settings": base, "elements": list(kids)}

def w(kind, s): return {"id": nid(), "elType": "widget", "widgetType": kind, "settings": s, "elements": []}

def typo(prefix, size, weight="400", lh=None, ls=None, m=None, t=None, lh_unit="em"):
    s = {f"{prefix}_typography": "custom", f"{prefix}_font_family": "Inter", f"{prefix}_font_size": px(size), f"{prefix}_font_weight": weight}
    if lh: s[f"{prefix}_line_height"] = px(lh, lh_unit)
    if ls is not None: s[f"{prefix}_letter_spacing"] = px(ls)
    if m: s[f"{prefix}_font_size_mobile"] = px(m)
    if t: s[f"{prefix}_font_size_tablet"] = px(t)
    return s

def heading(text, size, color, tag="h2", weight="700", lh=1.1, ls=None, m=None, t=None, align=None, anim=True):
    s = {"title": text, "header_size": tag, "title_color": color, **typo("typography", size, weight, lh, ls, m, t)}
    if align: s["align"] = align
    if anim: s["_animation"] = "fadeInUp"
    return w("heading", s)

def eyebrow(text, color):
    return heading(f'<span style="color:{ORANGE}">&#9679;</span>&nbsp;&nbsp;{text}', 12, color, tag="p", weight="600", lh=1.4, ls=1.7)

def text(html, color=MUTED, size=17, m=16, align=None):
    s = {"editor": html, "text_color": color, **typo("typography", size, "400", 1.65, None, m)}
    if align: s["align"] = align
    s["_animation"] = "fadeInUp"
    return w("text-editor", s)

def button(label, url, style="solid", external=False):
    colors = {"solid": (CTA, "#FFFFFF", NAVY, "#FFFFFF", None),
              "light": ("#FFFFFF", NAVY, SKY, NAVY, None),
              "ghost": ("rgba(255,255,255,0)", "#FFFFFF", "rgba(255,255,255,0.08)", "#FFFFFF", "rgba(255,255,255,0.35)"),
              "line": ("#FFFFFF", NAVY, "#FFFFFF", NAVY, LINE)}[style]
    bg, fg, hbg, hfg, border = colors
    s = {"text": label, "link": {"url": url, "is_external": "on" if external else "", "nofollow": ""},
         "background_color": bg, "button_text_color": fg, "button_background_hover_color": hbg, "hover_color": hfg,
         "border_radius": rad(6), "text_padding": box(14, 22, 14, 22), **typo("typography", 15, "600", 20, None, 14, lh_unit="px")}
    if border:
        s.update({"border_border": "solid", "border_width": box(1), "border_color": border, "button_hover_border_color": NAVY if style == "line" else "#FFFFFF"})
    return w("button", s)

def row(*kids, g_=12, wrap=True, extra=None):
    s = {"flex_direction": "row", "flex_wrap": "wrap" if wrap else "nowrap", "flex_gap": gap(g_), "flex_align_items": "center"}
    s.update(extra or {})
    return con(s, *kids)

# ---------- map: the one HTML widget ----------
css = g.CSS
top_level = css.split("@media")[0]  # rules inside @media blocks must not leak out as global rules
map_css = "\n".join(l for l in top_level.splitlines() if l.startswith((".gp-map", "@keyframes gp")))
map_css += "\n@media (prefers-reduced-motion:reduce){.gp-map .arc,.gp-map .pulse{animation:none}}\n@media (max-width:767px){.gp-map .lbl,.gp-map .lbl-bg{display:none}}"
map_css = map_css.replace("var(--sky)", SKY).replace("var(--orange)", ORANGE)
map_css += "\n.gp-map .lbl{font:600 11.5px Inter,system-ui,sans-serif;fill:#FFFFFF;letter-spacing:.01em}.gp-map .lbl-bg{fill:rgba(27,33,107,.92);stroke:rgba(168,206,255,.55)}"
# Refit each label pill to the measured text width (after web fonts load) so labels stay centred.
FIT_JS = ("<script>(function(){function fit(){document.querySelectorAll('.gp-map .lblg').forEach(function(g){"
          "var t=g.querySelector('text'),r=g.querySelector('rect');if(!t||!r)return;var p=+g.dataset.pad,px=+g.dataset.px,"
          "w=t.getBBox().width+2*p,lx=g.dataset.side==='r'?px+12:px-12-w;r.setAttribute('x',lx);r.setAttribute('width',w);t.setAttribute('x',lx+w/2);});}"
          "if(document.fonts&&document.fonts.ready){document.fonts.ready.then(fit);}"
          "if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',fit);}else{fit();}})();</script>")
map_html = (f"<style>{map_css}\n.gp-map{{margin:0!important;padding:0!important}}.gp-map svg{{width:100%;height:auto;aspect-ratio:1200/446.7}}</style>"
            f"<div class=\"gp-map\">{g.map_svg(cw=6.9, ph=24, pad=11, center=True)}</div>" + FIT_JS)

# ---------- 1. hero ----------
H1 = f'Global reach. Local expertise.<br><span style="color:{SKY}">One Innovive Standard.</span>'
stat_border = "rgba(168,206,255,0.18)"
def stat(big, label, first=False):
    s = {"width": px(25, "%"), "width_tablet": px(50, "%"), "width_mobile": px(50, "%"),
         "padding": box(34, 28, 44, 0 if first else 28), "padding_mobile": box(24, 12, 28, 12), "flex_gap": gap(12)}
    if not first:
        s.update({"border_border": "solid", "border_width": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "1", "isLinked": False},
                  "border_color": stat_border, "border_width_mobile": box(0)})
    return con(s, heading(big, 44, "#FFFFFF", tag="p", lh=1, ls=-1.3, m=34),
               w("text-editor", {"editor": f"<p>{label}</p>", "text_color": "#AFC0E6", **typo("typography", 14, "400", 1.5)}))

hero = section({
    "padding": box(284, 40, 0, 40), "padding_tablet": box(280, 30, 0, 30), "padding_mobile": box(200, 20, 0, 20),
    # Pull the hero up under the header so the header floats over it, matching /how-it-works/ (page 3254, hero 85ec5fe).
    "margin": box(-214, 0, 0, 0), "margin_mobile": box(-176, 0, 0, 0),
    "background_background": "gradient", "background_color": "#1E2A86", "background_color_stop": px(0, "%"),
    "background_color_b": DEEP, "background_color_b_stop": px(55, "%"),
    "background_gradient_type": "radial", "background_gradient_position": "top right", "_title": "Hero"},
    row(
        con({"width": px(58, "%"), "width_tablet": px(100, "%"), "flex_gap": gap(22)},
            eyebrow("INNOVIVE WORLDWIDE", SKY),
            heading(H1, 64, "#FFFFFF", tag="h1", lh=1.04, ls=-2.2, t=52, m=38)),
        con({"width": px(38, "%"), "width_tablet": px(100, "%"), "flex_gap": gap(28)},
            text("<p>Innovive supports scientific organizations across more than 43 countries with integrated vivarium solutions "
                 "designed to deliver consistent performance, operational efficiency and dependable support to enable transformative research.</p>",
                 color="#C8D3F0", size=18),
            row(button("Find your region", "#your-region", "light"), button("Contact Innovive", "/contact/", "ghost"))),
        g_=48, extra={"flex_align_items": "flex-end", "flex_justify_content": "space-between"}),
    con({"margin": box(56, 0, 0, 0), "margin_mobile": box(36, 0, 0, 0), "_title": "Map (HTML)"}, w("html", {"html": map_html, "_animation": "fadeIn", "_element_width": "inherit"})),
    con({"flex_direction": "row", "flex_wrap": "wrap", "margin": box(-8, 0, 0, 0),
         "border_border": "solid", "border_width": {"unit": "px", "top": "1", "right": "0", "bottom": "0", "left": "0", "isLinked": False},
         "border_color": stat_border, "_title": "Stats"},
        stat("500+", "Research organizations served", True), stat("43", "Countries with Innovive customers"),
        stat("Direct", "Innovive sales throughout the U.S. and Europe"),
        stat("4", "Regions of expertise: the Americas, Europe, Asia-Pacific and the Middle East")),
)

# ---------- 2. how we work ----------
photo = con({"width": px(48, "%"), "width_tablet": px(100, "%"), "min_height": px(640), "min_height_tablet": px(460), "min_height_mobile": px(340),
             "background_background": "classic", "background_image": img("cart"), "background_position": "initial", "background_xpos": px(34, "%"), "background_ypos": px(50, "%"), "background_size": "cover",
             "border_radius": rad(20), "overflow": "hidden", "flex_justify_content": "flex-end", "padding": box(20), "animation": "fadeInUp", "_title": "Photo"},
    con({"flex_direction": "row", "flex_direction_mobile": "row", "flex_wrap": "nowrap", "flex_align_items": "center", "flex_gap": gap(12), "padding": box(14, 16, 14, 16),
         "background_background": "classic", "background_color": "rgba(255,255,255,0.92)", "border_radius": rad(12)},
        w("icon", {"selected_icon": {"value": "fas fa-globe", "library": "fa-solid"}, "view": "stacked", "shape": "circle",
                   "primary_color": NAVY, "secondary_color": "#FFFFFF", "size": px(16), "icon_padding": px(10), "_element_width": "auto", "_flex_size": "none"}),
        w("text-editor", {"editor": "<p><strong>One network</strong><br>Direct teams and authorized partners</p>", "text_color": INK,
                          **typo("typography", 13, "400", 1.4)})))
checks = w("icon-list", {
    "icon_list": [{"_id": nid(), "text": t, "selected_icon": {"value": "far fa-check-circle", "library": "fa-regular"}}
                  for t in ("Same product quality", "Same technical expertise", "Same customer experience")],
    "divider": "yes", "divider_color": LINE, "divider_weight": px(1), "space_between": px(36),
    "icon_color": "#3765F8", "icon_size": px(20), "text_indent": px(14), "text_color": INK,
    **typo("icon_typography", 17, "600", 1.4), "_margin": box(20, 0, 0, 0), "_animation": "fadeInUp"})
network = section({"background_background": "classic", "background_color": "#FFFFFF", "_title": "How we work"},
    row(photo,
        con({"width": px(44, "%"), "width_tablet": px(100, "%"), "flex_gap": gap(18)},
            eyebrow("HOW WE WORK", CTA),
            heading("Direct teams and authorized partners, working as one.", 44, NAVY, lh=1.1, ls=-1.3, t=38, m=32),
            text("<p>Our customers engage with Innovive through direct regional teams and carefully selected local partners. Every relationship "
                 "is backed by Innovive's product expertise, quality standards and commitment to research success.</p>"
                 "<p>Wherever your research is conducted, Innovive is committed to providing the same product quality, technical expertise and "
                 "customer experience. Our direct teams and authorized partners work as one network to help customers confidently implement "
                 "and operate the Innovive system.</p>"),
            checks),
        g_=80, extra={"flex_justify_content": "space-between", "flex_gap_tablet": gap(40)}))

# ---------- 3. regions (native nested tabs) ----------
def chip(label, direct=False):
    return w("heading", {"title": label, "header_size": "span", "title_color": "#B4531A" if direct else CTA,
                         **typo("typography", 12, "600", 1.2, 0.4),
                         "_background_background": "classic", "_background_color": "#FEF0E6" if direct else "#EAF1FF",
                         "_padding": box(6, 12, 6, 12), "_border_radius": rad(999), "_element_width": "auto"})

def panel_body(*kids):
    return con({"width": px(48, "%"), "width_mobile": px(100, "%"), "padding": box(44, 44, 40, 44), "padding_mobile": box(28, 22, 28, 22),
                "flex_gap": gap(16), "flex_align_items": "flex-start"}, *kids)

def panel(photo_con, body):
    return con({"flex_direction": "row", "flex_direction_mobile": "column", "flex_gap": gap(0), "flex_align_items": "stretch",
                "background_background": "classic", "background_color": "#FFFFFF",
                "border_border": "solid", "border_width": box(1), "border_color": LINE, "border_radius": rad(16), "overflow": "hidden"},
               photo_con, body)

def bgphoto(key, h=440, hm=240):
    return con({"background_background": "classic", "background_image": img(key), "background_position": "center center",
                "background_size": "cover", "min_height": px(h), "min_height_mobile": px(hm), "_flex_size": "grow"})

tabs, panels = [], []
tabs.append({"_id": nid(), "tab_title": "U.S. and Europe"})
panels.append(con({"_title": "U.S. and Europe"}, panel(
    con({"width": px(52, "%"), "width_mobile": px(100, "%"), "flex_gap": gap(2)},
        bgphoto("north-america", 219, 150), bgphoto("europe", 219, 150)),
    panel_body(chip("Direct from Innovive", True),
               heading("U.S. and Europe", 30, NAVY, tag="h3", lh=1.15, ls=-0.6, m=24, anim=False),
               w("text-editor", {"editor": "<p>Customers across North America and Europe work directly with Innovive for product selection, implementation and ongoing support.</p>",
                                 "text_color": MUTED, **typo("typography", 16, "400", 1.65)}),
               row(button("Contact info@innovive.com", "mailto:info@innovive.com"), button("Contact form", "/contact/", "line"), g_=10,
                   extra={"margin": box(12, 0, 0, 0)})))))
for tid, tlabel, head, cov, name, logo, url, ik in g.PARTNERS:
    tabs.append({"_id": nid(), "tab_title": tlabel.replace("&amp;", "&")})
    logo_img = w("image", {"image": {"url": g.U + logo, "id": "", "size": "", "alt": f"{name} logo", "source": "library"},
                           "image_size": "full", "width": px(150), "height": px(56), "object-fit": "contain"})
    partner_box = con({"flex_direction": "row", "flex_align_items": "center", "flex_gap": gap(18), "padding": box(16),
                       "border_border": "solid", "border_width": box(1), "border_color": LINE, "border_radius": rad(12),
                       "margin": box(10, 0, 0, 0), "width": px(100, "%")},
                      logo_img, w("text-editor", {"editor": f"<p><span style=\"font-size:12px;color:{MUTED}\">Authorized partner</span><br><strong>{name}</strong></p>",
                                                  "text_color": INK, **typo("typography", 15, "400", 1.4)}))
    panels.append(con({"_title": head.replace("&amp;", "&")}, panel(
        con({"width": px(52, "%"), "width_mobile": px(100, "%"), "min_height_mobile": px(240)}, bgphoto(ik)),
        panel_body(chip("Authorized partner"),
                   heading(head, 30, NAVY, tag="h3", lh=1.15, ls=-0.6, m=24, anim=False),
                   w("text-editor", {"editor": f"<p>Innovive customers in {cov} are supported by {name}, our authorized regional partner, backed by Innovive's product expertise and quality standards.</p>",
                                     "text_color": MUTED, **typo("typography", 16, "400", 1.65)}),
                   partner_box,
                   con({"margin": box(12, 0, 0, 0)}, button(f"Visit {name}", url, external=True)),
                   w("text-editor", {"editor": 'Prefer to speak with Innovive directly? <a href="mailto:info@innovive.com"><strong>info@innovive.com</strong></a>',
                                     "text_color": MUTED, "link_color": CTA, **typo("typography", 13, "400", 1.5)})))))

tabs_widget = {"id": nid(), "elType": "widget", "widgetType": "nested-tabs", "elements": panels, "settings": {
    "tabs": tabs, "tabs_direction": "inline-start", "tabs_width": px(300), "tabs_justify_vertical": "start",
    "title_alignment": "start", "breakpoint_selector": "mobile",
    "tabs_title_space_between": px(6), "tabs_title_spacing": px(24),
    "tabs_title_background_color_background": "classic", "tabs_title_background_color_color": "#FFFFFF",
    "tabs_title_background_color_hover_background": "classic", "tabs_title_background_color_hover_color": "#EAF1FF",
    "tabs_title_background_color_active_background": "classic", "tabs_title_background_color_active_color": NAVY,
    "tabs_title_border_border": "solid", "tabs_title_border_width": box(1), "tabs_title_border_color": LINE,
    "tabs_title_border_active_border": "solid", "tabs_title_border_active_width": box(1), "tabs_title_border_active_color": NAVY,
    "tabs_title_border_radius": rad(10), "padding": box(14, 18, 14, 18),
    **typo("title_typography", 15, "600", 1.3),
    "title_text_color": INK, "title_text_color_hover": NAVY, "title_text_color_active": "#FFFFFF",
    "box_background_color_background": "", "box_border_border": "none", "box_padding": box(0),
    "_animation": "fadeInUp"}}

regions = section({"background_background": "classic", "background_color": MIST, "_element_id": "your-region", "_title": "Innovive in Your Region"},
    con({"flex_gap": gap(18), "margin": box(0, 0, 48, 0), "flex_align_items": "flex-start"},
        eyebrow("REGIONAL CONTACTS", CTA),
        heading("Innovive in Your Region", 44, NAVY, lh=1.1, ls=-1.3, t=38, m=32),
        con({"width": px(760), "width_tablet": px(100, "%"), "flex_gap": gap(10), "margin": box(4, 0, 0, 0)},
            text("<p>Innovive serves customers around the world through a combination of direct operations and authorized regional partners. "
                 "This approach gives research teams access to local market knowledge while maintaining a consistent Innovive experience.</p>"),
            text("<p><strong>Select your region to connect with the right Innovive representative.</strong></p>", color=INK))),
    tabs_widget)

# ---------- 4. CTA ----------
cta = section({"padding": box(0, 40, 128, 40), "padding_tablet": box(0, 30, 96, 30), "padding_mobile": box(0, 20, 72, 20),
               "background_background": "classic", "background_color": "#FFFFFF", "_title": "Contact CTA"},
    con({"flex_direction": "row", "flex_direction_tablet": "column", "flex_align_items": "center", "flex_align_items_tablet": "flex-start",
         "flex_justify_content": "space-between", "flex_gap": gap(32),
         "padding": box(64), "padding_mobile": box(36, 24, 36, 24), "border_radius": rad(20),
         "background_background": "gradient", "background_color": NAVY, "background_color_b": "#0B1146",
         "background_gradient_angle": px(120, "deg"), "animation": "fadeInUp"},
        con({"width": px(58, "%"), "width_tablet": px(100, "%"), "flex_gap": gap(14)},
            heading("Not sure who to contact?", 40, "#FFFFFF", lh=1.1, ls=-1.2, m=30, anim=False),
            w("text-editor", {"editor": "<p>Tell us where your research is based and we will connect you with the right Innovive team or partner.</p>",
                              "text_color": "#C8D3F0", **typo("typography", 17, "400", 1.6, None, 16)})),
        row(button("Contact Innovive", "/contact/", "light"), button("info@innovive.com", "mailto:info@innovive.com", "ghost"),
            extra={"flex_justify_content": "flex-end", "flex_justify_content_tablet": "flex-start"})))

data = [hero, network, regions, cta]

# No entrance animations: Elementor keeps animated elements hidden (elementor-invisible) until they
# scroll into view, so full-page captures, slow connections and some previews showed blank columns.
def strip_anim(n):
    for k in ("_animation", "animation", "_animation_delay", "animation_duration"):
        n.get("settings", {}).pop(k, None)
    for c in n.get("elements", []):
        strip_anim(c)
for n in data:
    strip_anim(n)
raw = json.dumps(data, separators=(",", ":"), ensure_ascii=True)
open(sys.argv[1], "w").write(raw)
widgets = re.findall(r'"widgetType":"([a-z-]+)"', raw)
print("bytes", len(raw), {k: widgets.count(k) for k in sorted(set(widgets))})
