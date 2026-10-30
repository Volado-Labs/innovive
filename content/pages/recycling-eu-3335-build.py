"""Build the redesigned /recycling-eu/ Elementor data. Copy is the Wix page's, verbatim."""
import json, sys, secrets

S = sys.argv[1]
cur = json.load(open(f"{S}/cur.json"))
old = json.loads(cur["meta"]["_elementor_data"])

NAVY = "#00223D"
BLUE = "#005287"
BODY = "#535862"
TINT = "#F6F9FF"
CONTACT = {"url": "https://innovive.com/contact/", "is_external": "", "nofollow": "", "custom_attributes": ""}

def nid():
    return secrets.token_hex(4)[:7]

def px(v):
    return {"unit": "px", "size": v, "sizes": []}

def box(t, r=None, b=None, l=None):
    r = t if r is None else r; b = t if b is None else b; l = r if l is None else l
    return {"unit": "px", "top": str(t), "right": str(r), "bottom": str(b), "left": str(l), "isLinked": t == r == b == l}

def gap(v):
    return {"column": str(v), "row": str(v), "isLinked": True, "unit": "px", "size": v}

def con(children, **s):
    s.setdefault("padding", box(0))  # Elementor pads nested containers 10px unless told otherwise
    return {"id": nid(), "elType": "container", "isInner": False, "settings": s, "elements": children}

def typo(prefix, size, weight="400", lh=None, ls=None, mobile=None):
    p = f"{prefix}typography_"
    d = {p + "typography": "custom", p + "font_family": "Inter", p + "font_size": px(size), p + "font_weight": weight}
    if lh: d[p + "line_height"] = px(lh)
    if ls is not None: d[p + "letter_spacing"] = px(ls)
    if mobile: d[p + "font_size_mobile"] = px(mobile[0]); d[p + "line_height_mobile"] = px(mobile[1])
    return d

def widget(kind, **s):
    return {"id": nid(), "elType": "widget", "widgetType": kind, "isInner": False, "settings": s, "elements": []}

def heading(text, tag="h2", size=36, lh=44, color=NAVY, align="start", mobile=(28, 36), **extra):
    return widget("heading", title=text, header_size=tag, title_color=color, align=align,
                  _margin=box(0), **typo("", size, "700", lh, -0.6, mobile), **extra)

def text(html, color=BODY, size=17, lh=28, align="start"):
    return widget("text-editor", editor=html, text_color=color, align=align, **typo("", size, "400", lh))

def pill(label, dark=False):
    return widget("button", text=label, align="left", selected_icon={"value": "fas fa-recycle", "library": "fa-solid"},
                  icon_indent=px(8), button_text_color="#FFFFFF" if dark else BLUE,
                  background_color="#FFFFFF1F" if dark else "#E4F1F9", border_radius=box(100),
                  text_padding=box(7, 14), **typo("", 13, "600", 16, 0.4))

def button(label, light=True, align="left"):
    return widget("button", text=label, link=CONTACT, align=align, align_mobile="justify",
                  selected_icon={"value": "fas fa-arrow-right", "library": "fa-solid"}, icon_align="row-reverse",
                  icon_indent=px(10), button_text_color=BLUE if light else "#FFFFFF",
                  background_color="#FFFFFF" if light else BLUE,
                  hover_color=BLUE if light else "#FFFFFF", button_background_hover_color="#E4F1F9" if light else NAVY,
                  border_radius=box(6), text_padding=box(15, 26), **typo("", 16, "600", 20))

def image(url, mid, height, alt, radius=12, height_mobile=None):
    s = dict(image={"url": url, "id": mid, "size": "", "alt": alt, "source": "library"}, image_size="full",
             width={"unit": "%", "size": 100, "sizes": []}, height=px(height), object_fit="cover",
             image_border_radius=box(radius))
    s["object-fit"] = "cover"
    if height_mobile: s["height_mobile"] = px(height_mobile)
    return widget("image", **s)

CARD = dict(content_width="full", flex_direction="column", background_background="classic", background_color="#FFFFFF",
            border_border="solid", border_width=box(1), border_color="#00528726", border_radius=box(12),
            box_shadow_box_shadow_type="yes",
            box_shadow_box_shadow={"horizontal": 0, "vertical": 20, "blur": 40, "spread": 0, "color": "rgba(15,29,40,0.06)"})

def section(children, bg=None, top=96, bottom=96, **extra):
    s = dict(boxed_width=px(1240), flex_direction="column", flex_gap=gap(48), flex_gap_mobile=gap(32),
             padding=box(top, 40, bottom, 40), padding_tablet=box(72, 30, 72, 30), padding_mobile=box(56, 20, 56, 20))
    if bg: s.update(background_background="classic", background_color=bg)
    s.update(extra)
    return con(children, **s)

# --- 1. Hero: keep the outer wrapper (it carries the header offset), new split panel inside it.
outer = old[0]
hero_text = con([
    pill("EU Recycling", dark=True),
    heading("Our solution removes used product and targets zero waste.", tag="h1", size=52, lh=60,
            color="#FFFFFF", mobile=(34, 42)),
    button("Ask About Availability"),
], content_width="full", flex_direction="column", flex_gap=gap(28), flex_gap_mobile=gap(20),
   width={"unit": "%", "size": 52, "sizes": []}, width_tablet={"unit": "%", "size": 100, "sizes": []},
   flex_align_items="flex-start", flex_justify_content="center")
hero_img = con([
    image("https://innovive.com/wp-content/uploads/2026/06/Container-1.png", 0, 420,
          "Recycled PET plastic flakes", height_mobile=240),
], content_width="full", width={"unit": "%", "size": 48, "sizes": []},
   width_tablet={"unit": "%", "size": 100, "sizes": []})
hero_panel = con([hero_text, hero_img], content_width="full", flex_direction="row", flex_direction_tablet="column",
                 flex_align_items="center", flex_gap=gap(56), flex_gap_mobile=gap(32),
                 padding=box(64, 64, 64, 64), padding_tablet=box(48, 40, 48, 40), padding_mobile=box(32, 22, 22, 22),
                 background_background="gradient", background_color=NAVY, background_color_b="#0B5E96",
                 background_gradient_angle={"unit": "deg", "size": 125, "sizes": []},
                 background_color_stop={"unit": "%", "size": 35, "sizes": []},
                 border_radius=box(16))
outer["elements"] = [hero_panel]
outer["settings"]["padding"] = box(180, 40, 24, 40)
outer["settings"]["padding_mobile"] = box(200, 20, 8, 20)

# --- 2. "Join us" strip: three benefit cards.
def benefit(icon, line):
    return con([
        widget("icon", selected_icon={"value": icon, "library": "fa-solid"}, view="stacked", shape="square",
               primary_color="#E4F1F9", secondary_color=BLUE, size=px(22), icon_padding=px(15),
               border_radius=box(10), align="left"),
        text(line, color=NAVY, size=18, lh=28),
    ], **CARD, flex_gap=gap(20), padding=box(32, 28, 32, 28), padding_mobile=box(24, 22, 24, 22))

strip = section([
    heading("Join us for a greener solution!", align="center", size=36, lh=44),
    con([
        benefit("fas fa-handshake", "We work with partner networks across the EU"),
        benefit("fas fa-recycle", "Innovive recycles all plastic materials, so it is never incinerated or reaches a landfill."),
        benefit("fas fa-tags", "We offer customized pricing tailored to your needs"),
    ], content_width="full", container_type="grid",
       grid_columns_grid={"unit": "fr", "size": 3, "sizes": []}, grid_rows_grid={"unit": "fr", "size": 1, "sizes": []},
       grid_columns_grid_tablet={"unit": "fr", "size": 1, "sizes": []}, grid_rows_grid_tablet={"unit": "fr", "size": 3, "sizes": []},
       grid_columns_grid_mobile={"unit": "fr", "size": 1, "sizes": []}, grid_rows_grid_mobile={"unit": "fr", "size": 3, "sizes": []},
       grid_gaps=gap(24), grid_align_items="stretch"),
], top=72, bottom=96)

# --- 3. Process: two numbered steps with photos.
def step(n, title, body, url, alt):
    return con([
        image(url, 0, 300, alt, radius=8, height_mobile=220),
        con([
            widget("heading", title=f"Step {n}", header_size="div", title_color=BLUE, **typo("", 14, "700", 20, 1.2),
                   _margin=box(0)),
            heading(title, tag="h3", size=24, lh=32, mobile=(21, 28)),
            text(body),
        ], content_width="full", flex_direction="column", flex_gap=gap(12), padding=box(8, 12, 12, 12)),
    ], **CARD, flex_gap=gap(20), padding=box(16), padding_mobile=box(12))

process = section([
    heading("What Happens When Used", align="center"),
    con([
        step(1, "What Happens At Your Facility",
             "Dirty disposable cages can be re-stacked with soiled bedding and sealed back in their original bags. Then, they can go straight to the recycling dock of the facility.",
             "https://innovive.com/wp-content/uploads/2026/06/Recycling.png", "Sealed bags of used cages in a recycling container"),
        step(2, "Caging is Picked Up",
             "Used product is sent to specialized plastic recycling facilities that have validated our product. Plastic is mechanically cleaned, sorted and re-used in caging or equivalent products.",
             "https://innovive.com/wp-content/uploads/2026/06/faculty.jpg", "Used caging being collected and processed"),
    ], content_width="full", container_type="grid",
       grid_columns_grid={"unit": "fr", "size": 2, "sizes": []}, grid_rows_grid={"unit": "fr", "size": 1, "sizes": []},
       grid_columns_grid_tablet={"unit": "fr", "size": 1, "sizes": []}, grid_rows_grid_tablet={"unit": "fr", "size": 2, "sizes": []},
       grid_columns_grid_mobile={"unit": "fr", "size": 1, "sizes": []}, grid_rows_grid_mobile={"unit": "fr", "size": 2, "sizes": []},
       grid_gaps=gap(28), grid_align_items="stretch"),
], bg=TINT)

# --- 4. Materials: list on the left, PET note card on the right.
def chip(icon, label):
    return con([
        widget("icon", selected_icon={"value": icon, "library": "fa-solid"}, view="stacked", shape="circle",
               primary_color="#E4F1F9", secondary_color=BLUE, size=px(15), icon_padding=px(11), align="left"),
        text(label, color=NAVY, size=16, lh=24),
    ], content_width="full", flex_direction="row", flex_align_items="center", flex_gap=gap(14),
       padding=box(14, 18, 14, 14), border_border="solid", border_width=box(1), border_color="#00528726",
       border_radius=box(10), background_background="classic", background_color="#FFFFFF",
       flex_wrap="nowrap")

items = [("fas fa-box", "Cage bottoms with or without soiled bedding"), ("fas fa-layer-group", "Cage lids"),
         ("fas fa-tint", "Aquavive® Water Bottles"), ("fas fa-seedling", "Feeders"),
         ("fas fa-id-card", "Cardholders"), ("fas fa-puzzle-piece", "Enrichment plastics")]
materials = section([
    con([
        con([
            heading("Materials We Pick Up"),
            con([chip(i, t) for i, t in items], content_width="full", container_type="grid",
                grid_columns_grid={"unit": "fr", "size": 2, "sizes": []}, grid_rows_grid={"unit": "fr", "size": 3, "sizes": []},
                grid_columns_grid_mobile={"unit": "fr", "size": 1, "sizes": []}, grid_rows_grid_mobile={"unit": "fr", "size": 6, "sizes": []},
                grid_gaps=gap(14), grid_align_items="stretch"),
        ], content_width="full", flex_direction="column", flex_gap=gap(28),
           width={"unit": "%", "size": 60, "sizes": []}, width_tablet={"unit": "%", "size": 100, "sizes": []}),
        con([
            widget("icon", selected_icon={"value": "fas fa-recycle", "library": "fa-solid"}, view="stacked",
                   shape="square", primary_color=BLUE, secondary_color="#FFFFFF", size=px(26), icon_padding=px(16),
                   border_radius=box(12), align="left"),
            text("Innovive IVC caging is made from recyclable PET plastic, RIC 1", color=NAVY, size=24, lh=34),
        ], **{**CARD, "background_color": TINT}, flex_gap=gap(24), padding=box(40, 36, 40, 36),
           padding_mobile=box(28, 24, 28, 24), flex_justify_content="center",
           width={"unit": "%", "size": 40, "sizes": []}, width_tablet={"unit": "%", "size": 100, "sizes": []}),
    ], content_width="full", flex_direction="row", flex_direction_tablet="column", flex_gap=gap(48),
       flex_gap_mobile=gap(32), flex_align_items="center", flex_align_items_tablet="stretch"),
])

# --- 5. Closing call to action.
cta = section([
    con([
        con([
            heading("Ask us about availability of our recycling solution at your EU research facility.",
                    size=32, lh=42, color="#FFFFFF", mobile=(24, 32)),
        ], content_width="full", width={"unit": "%", "size": 68, "sizes": []},
           width_tablet={"unit": "%", "size": 100, "sizes": []}),
        button("Ask About Availability", align="right"),
    ], content_width="full", flex_direction="row", flex_direction_tablet="column", flex_align_items="center",
       flex_align_items_tablet="flex-start", flex_justify_content="space-between", flex_gap=gap(32),
       padding=box(56, 56, 56, 56), padding_mobile=box(32, 24, 32, 24),
       background_background="gradient", background_color=NAVY, background_color_b="#0B5E96",
       background_gradient_angle={"unit": "deg", "size": 125, "sizes": []},
       background_color_stop={"unit": "%", "size": 35, "sizes": []}, border_radius=box(16)),
], top=24, bottom=96)

data = [outer, strip, process, materials, cta]
json.dump({"meta": {"_elementor_data": json.dumps(data, ensure_ascii=False)}},
          open(f"{S}/redesign.json", "w"), ensure_ascii=False)
print("sections", len(data))
