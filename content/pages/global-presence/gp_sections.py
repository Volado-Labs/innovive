"""Global Presence page, v2 design. Single source for the local prototype and the Elementor build.

Copy: Robin Gaffney, "Global Presence page - suggested changes and copy", 2026-09-22.
render(img) -> list of (section_key, html). `img(name)` returns the URL for an image key.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
DOTS = open(os.path.join(HERE, "dotpath.txt")).read()

# Map projection (matches dotmap.py): equirectangular, lon -170..190, lat -56..78, 1200 x 446.7
W, H = 1200, 446.7
def proj(lat, lon):
    return round((lon + 170) / 360 * W, 1), round((78 - lat) / 134 * H, 1)

HQ = proj(32.9, -117.2)  # 10019 Waples Court, San Diego
HUBS = [  # key, label, lat, lon, kind, label side
    ("latam", "Latin America", -23.5, -46.6, "partner", "r"),
    ("europe", "Europe", 49.5, 8.5, "direct", "r"),
    ("uk", "UK & Ireland", 53.0, -2.0, "partner", "l"),
    ("gcc", "Middle East & GCC", 25.2, 55.3, "partner", "r"),
    ("korea", "South Korea", 37.6, 127.0, "partner", "l"),
    ("japan", "Japan", 35.7, 139.7, "partner", "r"),
    ("anz", "Australia & NZ", -33.9, 151.2, "partner", "l"),
]

CSS = r"""
.gp{--navy:#1B216B;--deep:#0A0F3D;--ink:#0E1733;--blue:#3765F8;--cta:#005287;--sky:#A8CEFF;--orange:#F47B2E;--mist:#F4F7FD;--line:#E1E7F2;--muted:#56607A;
font-family:Inter,system-ui,sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased;line-height:1.6}
.gp *,.gp *:before,.gp *:after{box-sizing:border-box}
.gp h1,.gp h2,.gp h3,.gp p{margin:0;font-family:Inter,system-ui,sans-serif}
.gp .wrap{max-width:1280px;margin:0 auto;padding:0 40px}
.gp .eyebrow{display:inline-flex;align-items:center;gap:10px;font-size:12px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--cta)}
.gp .eyebrow i{width:6px;height:6px;border-radius:50%;background:var(--orange);display:block}
.gp .btn{display:inline-flex;align-items:center;gap:10px;font-size:15px;font-weight:600;line-height:20px;padding:14px 22px;border-radius:6px;text-decoration:none!important;transition:background-color .35s cubic-bezier(.2,.7,.2,1),color .35s cubic-bezier(.2,.7,.2,1),border-color .35s cubic-bezier(.2,.7,.2,1),transform .35s cubic-bezier(.2,.7,.2,1)}
.gp .btn:active{transform:scale(.98)}
.gp .btn svg{width:16px;height:16px;transition:transform .35s cubic-bezier(.2,.7,.2,1)}
.gp .btn:hover svg{transform:translateX(3px)}
.gp .btn-solid{background:var(--cta);color:#fff!important}
.gp .btn-solid:hover{background:var(--navy)}
.gp .btn-light{background:#fff;color:var(--navy)!important}
.gp .btn-light:hover{background:var(--sky)}
.gp .btn-ghost{border:1px solid rgba(255,255,255,.35);color:#fff!important}
.gp .btn-ghost:hover{border-color:#fff;background:rgba(255,255,255,.06)}
.gp .btn-line{border:1px solid var(--line);color:var(--navy)!important;background:#fff}
.gp .btn-line:hover{border-color:var(--navy)}
.gp .btn:focus-visible,.gp .tab:focus-visible{outline:2px solid var(--blue);outline-offset:3px}

/* hero */
.gp-hero{position:relative;overflow:hidden;background:radial-gradient(1200px 600px at 78% 8%,#26318F 0%,rgba(38,49,143,0) 60%),linear-gradient(180deg,#0B1146 0%,var(--deep) 100%);color:#fff;padding:190px 0 0}
.gp-hero .top{display:grid;grid-template-columns:7fr 5fr;gap:64px;align-items:end}
.gp-hero .eyebrow{color:var(--sky)}
.gp-hero h1{font-size:64px;line-height:1.04;font-weight:700;letter-spacing:-.035em;color:#fff;margin-top:22px}
.gp-hero h1 span{display:block;color:var(--sky)}
.gp-hero .lede{font-size:18px;line-height:1.65;color:#C8D3F0}
.gp-hero .ctas{display:flex;flex-wrap:wrap;gap:12px;margin-top:28px}
.gp-map{position:relative;margin:56px auto 0;max-width:1280px;padding:0 20px}
.gp-map svg{display:block;width:100%;height:auto;overflow:visible}
.gp-map .dots{stroke:#6A86DA;stroke-opacity:.62;stroke-width:2.4;stroke-linecap:round;fill:none}
.gp-map .arc{fill:none;stroke:url(#gpArc);stroke-width:1.2;stroke-dasharray:4 6;animation:gpflow 1.6s linear infinite}
.gp-map .pin{fill:var(--sky)}
.gp-map .pin.direct{fill:#fff}
.gp-map .halo{fill:var(--sky);opacity:.18}
.gp-map .hq{fill:var(--orange)}
.gp-map .pulse{fill:none;stroke:var(--orange);stroke-width:1.5;transform-box:fill-box;transform-origin:center;animation:gppulse 2.4s cubic-bezier(.2,.7,.2,1) infinite}
.gp-map .lbl{font:600 11px Inter,system-ui,sans-serif;fill:#DCE6FF;letter-spacing:.02em}
.gp-map .lbl.hql{fill:#fff}
.gp-map .lbl-bg{fill:rgba(10,15,61,.72);stroke:rgba(168,206,255,.28);stroke-width:1}
@keyframes gpflow{to{stroke-dashoffset:-20}}
@keyframes gppulse{0%{transform:scale(.6);opacity:.9}100%{transform:scale(2.6);opacity:0}}
.gp-stats{position:relative;display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid rgba(168,206,255,.18);margin-top:-8px}
.gp-stats div{padding:34px 28px 44px;border-left:1px solid rgba(168,206,255,.18)}
.gp-stats div:first-child{border-left:0;padding-left:0}
.gp-stats b{display:block;font-size:44px;line-height:1;font-weight:700;letter-spacing:-.03em;color:#fff}
.gp-stats span{display:block;margin-top:12px;font-size:14px;line-height:1.5;color:#AFC0E6;max-width:230px}

/* network */
.gp-net{background:#fff;padding:128px 0}
.gp-net .grid{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center}
.gp-net figure{margin:0;position:relative;border-radius:20px;overflow:hidden;aspect-ratio:4/5;background:var(--mist)}
.gp-net figure img{width:100%;height:100%;object-fit:cover;display:block}
.gp-net figure figcaption{position:absolute;left:20px;bottom:20px;right:20px;display:flex;align-items:center;gap:12px;background:rgba(255,255,255,.92);border-radius:12px;padding:14px 16px;font-size:13px;line-height:1.4;color:var(--ink)}
.gp-net figure figcaption b{display:block;font-size:14px}
.gp-net figure figcaption i{flex:0 0 36px;height:36px;border-radius:50%;background:var(--navy);display:flex;align-items:center;justify-content:center}
.gp-net h2{font-size:44px;line-height:1.1;letter-spacing:-.03em;font-weight:700;color:var(--navy);margin:18px 0 24px}
.gp-net p{font-size:17px;color:var(--muted);margin-bottom:16px}
.gp-net ul{list-style:none;margin:32px 0 0;padding:0;border-top:1px solid var(--line)}
.gp-net li{display:flex;align-items:center;gap:16px;padding:18px 0;border-bottom:1px solid var(--line);font-size:17px;font-weight:600;color:var(--ink)}
.gp-net li svg{flex:0 0 22px;color:var(--blue)}
.gp-net li small{margin-left:auto;font-size:13px;font-weight:500;color:var(--muted)}

/* regions */
.gp-reg{background:var(--mist);padding:128px 0}
.gp-reg .head{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:end;margin-bottom:56px}
.gp-reg h2{font-size:44px;line-height:1.1;letter-spacing:-.03em;font-weight:700;color:var(--navy);margin-top:18px}
.gp-reg .head p{font-size:17px;color:var(--muted)}
.gp-reg .head p+p{margin-top:12px;color:var(--ink);font-weight:600}
.gp-sel{display:grid;grid-template-columns:320px 1fr;gap:24px;align-items:start}
.gp-tabs{background:#fff;border:1px solid var(--line);border-radius:16px;padding:10px}
.gp-tabs .grp{font-size:11px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);padding:14px 14px 8px}
.gp .tab{all:unset;box-sizing:border-box;display:flex;width:100%;align-items:center;gap:12px;padding:13px 14px;border-radius:10px;font-size:15px;font-weight:600;color:var(--ink);cursor:pointer;transition:background-color .3s cubic-bezier(.2,.7,.2,1),color .3s cubic-bezier(.2,.7,.2,1)}
.gp .tab i{width:8px;height:8px;border-radius:50%;background:var(--sky);flex:0 0 8px}
.gp .tab.direct i{background:var(--orange)}
.gp .tab svg{margin-left:auto;width:16px;height:16px;opacity:0;transform:translateX(-4px);transition:all .3s cubic-bezier(.2,.7,.2,1)}
.gp .tab:hover{background:var(--mist)}
.gp .tab[aria-selected=true]{background:var(--navy);color:#fff}
.gp .tab[aria-selected=true] svg{opacity:1;transform:none}
.gp-panel{background:#fff;border:1px solid var(--line);border-radius:16px;overflow:hidden;display:grid;grid-template-columns:1.05fr 1fr}
.gp-panel[hidden]{display:none}
.gp-panel .ph{position:relative;min-height:440px;background:var(--mist)}
.gp-panel .ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.gp-panel .ph.duo img{height:calc(50% - 1px)}
.gp-panel .ph.duo img+img{top:auto;bottom:0}
.gp-panel .bd{padding:44px 44px 40px;display:flex;flex-direction:column}
.gp-panel .chip{align-self:flex-start;font-size:12px;font-weight:600;letter-spacing:.04em;padding:6px 12px;border-radius:999px;background:#EAF1FF;color:var(--cta)}
.gp-panel .chip.direct{background:#FEF0E6;color:#B4531A}
.gp-panel h3{font-size:30px;line-height:1.15;letter-spacing:-.02em;font-weight:700;color:var(--navy);margin:18px 0 14px}
.gp-panel p{font-size:16px;color:var(--muted)}
.gp-panel .partner{display:flex;align-items:center;gap:18px;margin-top:26px;padding:16px;border:1px solid var(--line);border-radius:12px}
.gp-panel .partner img{width:150px;height:56px;object-fit:contain;flex:0 0 150px}
.gp-panel .partner small{display:block;font-size:12px;color:var(--muted)}
.gp-panel .partner b{display:block;font-size:15px;color:var(--ink)}
.gp-panel .acts{display:flex;flex-wrap:wrap;gap:10px;margin-top:auto;padding-top:28px}
.gp-panel .note{font-size:13px;color:var(--muted);margin-top:14px}
.gp-panel .note a{color:var(--cta);font-weight:600}
.gp-js .gp-panel:not(.on){display:none}

/* cta */
.gp-cta{background:#fff;padding:0 0 128px}
.gp-cta .card{position:relative;overflow:hidden;border-radius:20px;background:linear-gradient(120deg,var(--navy) 0%,#0B1146 100%);padding:64px;display:grid;grid-template-columns:1.4fr 1fr;gap:48px;align-items:center;color:#fff}
.gp-cta .card:after{content:"";position:absolute;right:-120px;top:-160px;width:520px;height:520px;border-radius:50%;background:radial-gradient(closest-side,rgba(55,101,248,.45),rgba(55,101,248,0));pointer-events:none}
.gp-cta h2{font-size:40px;line-height:1.1;letter-spacing:-.03em;font-weight:700;color:#fff}
.gp-cta p{font-size:17px;color:#C8D3F0;margin-top:14px;max-width:520px}
.gp-cta .acts{position:relative;z-index:1;display:flex;flex-wrap:wrap;gap:12px;justify-content:flex-end}

/* reveal */
.gp-js .rv{opacity:0;transform:translateY(28px);transition:opacity .9s cubic-bezier(.2,.7,.2,1),transform .9s cubic-bezier(.2,.7,.2,1)}
.gp-js .rv.in{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){.gp-map .arc,.gp-map .pulse{animation:none}.gp-js .rv{opacity:1;transform:none;transition:none}}

@media (max-width:1024px){
.gp .wrap{padding:0 30px}
.gp-hero h1{font-size:52px}
.gp-hero .top,.gp-net .grid,.gp-reg .head,.gp-cta .card{grid-template-columns:1fr;gap:32px}
.gp-stats{grid-template-columns:repeat(2,1fr)}
.gp-stats div:nth-child(3){border-left:0;padding-left:0}
.gp-stats div:nth-child(n+3){border-top:1px solid rgba(168,206,255,.18)}
.gp-sel{grid-template-columns:1fr}
.gp-tabs{display:flex;overflow-x:auto;gap:6px;scrollbar-width:none}
.gp-tabs::-webkit-scrollbar{display:none}
.gp-tabs .grp{display:none}
.gp .tab{width:auto;white-space:nowrap;flex:0 0 auto}
.gp .tab svg{display:none}
.gp-net figure{aspect-ratio:16/10}
.gp-cta .acts{justify-content:flex-start}
}
@media (max-width:767px){
.gp .wrap{padding:0 20px}
.gp-hero{padding-top:150px}
.gp-hero h1{font-size:38px}
.gp-hero .lede{font-size:16px}
.gp-map{margin-top:36px;padding:0}
.gp-map .lbl,.gp-map .lbl-bg{display:none}
.gp-stats b{font-size:34px}
.gp-stats div{padding:24px 16px 28px}
.gp-stats div:nth-child(odd){padding-left:0;border-left:0}
.gp-net,.gp-reg{padding:80px 0}
.gp-net h2,.gp-reg h2{font-size:32px}
.gp-panel{grid-template-columns:1fr}
.gp-panel .ph{min-height:220px}
.gp-panel .bd{padding:28px 22px}
.gp-panel h3{font-size:24px}
.gp-panel .partner img{width:110px;flex-basis:110px}
.gp-cta{padding-bottom:80px}
.gp-cta .card{padding:36px 24px}
.gp-cta h2{font-size:30px}
}
"""

ARROW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'
EXT = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 3h7v7M13 3 4 12"/></svg>'
CHECK = '<svg viewBox="0 0 22 22" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="9.5"/><path d="m7 11.3 2.7 2.7L15.2 8.5"/></svg>'
MAIL = "mailto:info@innovive.com"


def map_svg(cw=6.4, ph=22, pad=9, center=False):
    """cw: approx width per character of label text; ph: pill height; pad: pill side padding."""
    hx, hy = HQ
    arcs, pins, labels = [], [], []
    for key, label, lat, lon, kind, side in HUBS:
        x, y = proj(lat, lon)
        mx, my = (hx + x) / 2, min(hy, y) - abs(x - hx) * 0.18 - 20
        arcs.append(f'<path class="arc" d="M{hx} {hy}Q{mx:.1f} {my:.1f} {x} {y}"/>')
        pins.append(f'<circle class="halo" cx="{x}" cy="{y}" r="9"/><circle class="pin {kind}" cx="{x}" cy="{y}" r="3.6"/>')
        tw = len(label.replace("&amp;", "&")) * cw + 2 * pad
        lx = x + 12 if side == "r" else x - 12 - tw
        if center:  # text centred in the pill; the page script refits pill widths to the measured text
            labels.append(f'<g class="lblg" data-side="{side}" data-px="{x}" data-pad="{pad}">'
                          f'<rect class="lbl-bg" x="{lx:.1f}" y="{y-ph/2:.1f}" width="{tw:.1f}" height="{ph}" rx="{ph/2:g}"/>'
                          f'<text class="lbl" x="{lx+tw/2:.1f}" y="{y:.1f}" text-anchor="middle" dominant-baseline="central">{label}</text></g>')
        else:
            labels.append(f'<rect class="lbl-bg" x="{lx:.1f}" y="{y-ph/2:.1f}" width="{tw:.1f}" height="{ph}" rx="{ph/2:g}"/>'
                          f'<text class="lbl" x="{lx+pad:.1f}" y="{y+ph/2-7:.1f}">{label}</text>')
    hq_label = "San Diego · Headquarters"
    tw = len(hq_label) * cw + 2 * pad
    if center:
        labels.append(f'<g class="lblg" data-side="l" data-px="{hx}" data-pad="{pad}">'
                      f'<rect class="lbl-bg" x="{hx-tw-12:.1f}" y="{hy-ph/2:.1f}" width="{tw:.1f}" height="{ph}" rx="{ph/2:g}"/>'
                      f'<text class="lbl hql" x="{hx-12-tw/2:.1f}" y="{hy:.1f}" text-anchor="middle" dominant-baseline="central">{hq_label}</text></g>')
    else:
        labels.append(f'<rect class="lbl-bg" x="{hx-tw-12:.1f}" y="{hy-ph/2:.1f}" width="{tw:.1f}" height="{ph}" rx="{ph/2:g}"/>'
                      f'<text class="lbl hql" x="{hx-tw-12+pad:.1f}" y="{hy+ph/2-7:.1f}">{hq_label}</text>')
    hq = (f'<circle class="pulse" cx="{hx}" cy="{hy}" r="8"/><circle class="halo" cx="{hx}" cy="{hy}" r="11" style="fill:#F47B2E;opacity:.22"/>'
          f'<circle class="hq" cx="{hx}" cy="{hy}" r="5"/>')
    return (f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Map of Innovive\'s headquarters in San Diego and the regions it serves: '
            f'the United States, Europe, Latin America, the United Kingdom and Ireland, the Middle East and GCC, Japan, South Korea, and Australia and New Zealand.">'
            '<defs><linearGradient id="gpArc" x1="0" x2="1"><stop offset="0" stop-color="#F47B2E" stop-opacity=".9"/>'
            '<stop offset="1" stop-color="#A8CEFF" stop-opacity=".8"/></linearGradient></defs>'
            f'<path class="dots" d="{DOTS}"/>' + "".join(arcs) + "".join(pins) + hq + "".join(labels) + "</svg>")


def hero():
    return f"""<section class="gp gp-hero" aria-labelledby="gp-h1"><div class="wrap"><div class="top">
<div class="rv"><span class="eyebrow"><i></i>Innovive Worldwide</span>
<h1 id="gp-h1">Global reach. Local expertise. <span>One Innovive Standard.</span></h1></div>
<div class="rv"><p class="lede">Innovive supports scientific organizations across more than 43 countries with integrated vivarium solutions designed to deliver consistent performance, operational efficiency and dependable support to enable transformative research.</p>
<div class="ctas"><a class="btn btn-light" href="#your-region">Find your region {ARROW}</a><a class="btn btn-ghost" href="/contact/">Contact Innovive</a></div></div>
</div></div>
<div class="gp-map rv">{map_svg()}</div>
<div class="wrap"><div class="gp-stats">
<div><b>500+</b><span>Research organizations served</span></div>
<div><b>43</b><span>Countries with Innovive customers</span></div>
<div><b>Direct</b><span>Innovive sales throughout the U.S. and Europe</span></div>
<div><b>4</b><span>Regions of expertise: the Americas, Europe, Asia-Pacific and the Middle East</span></div>
</div></div></section>"""


def network(img):
    items = "".join(f"<li>{CHECK}{t}</li>" for t in ("Same product quality", "Same technical expertise", "Same customer experience"))
    return f"""<section class="gp gp-net"><div class="wrap grid">
<figure class="rv"><img src="{img('cart')}" alt="Innovive team member with an Innovive shipment on a cart in a vivarium" loading="lazy" width="2560" height="1707" style="object-position:72% 50%">
<figcaption><i><svg width="18" height="18" viewBox="0 0 22 22" fill="none" stroke="#fff" stroke-width="1.5" aria-hidden="true"><circle cx="11" cy="11" r="9"/><path d="M2 11h18M11 2c2.5 2.6 3.7 5.6 3.7 9s-1.2 6.4-3.7 9c-2.5-2.6-3.7-5.6-3.7-9S8.5 4.6 11 2Z"/></svg></i>
<span><b>One network</b>Direct teams and authorized partners</span></figcaption></figure>
<div class="rv"><span class="eyebrow"><i></i>How we work</span>
<h2>Direct teams and authorized partners, working as one.</h2>
<p>Our customers engage with Innovive through direct regional teams and carefully selected local partners. Every relationship is backed by Innovive's product expertise, quality standards and commitment to research success.</p>
<p>Wherever your research is conducted, Innovive is committed to providing the same product quality, technical expertise and customer experience. Our direct teams and authorized partners work as one network to help customers confidently implement and operate the Innovive system.</p>
<ul>{items}</ul></div>
</div></section>"""


U = "https://innovive.com/wp-content/uploads/2026/07/"
PARTNERS = [  # tab id, tab label, heading, coverage phrase, partner, logo, url, image key
    ("latam", "Latin America", "Latin America", "South and Latin America", "EAD Scientific", "ead-scientific-logo-uniform.png", "https://www.eadscience.com/", "latin-america"),
    ("uk", "United Kingdom &amp; Ireland", "United Kingdom &amp; Ireland", "the United Kingdom and Ireland", "Datesand Group", "datesand-group-logo-uniform.png", "https://www.datesand.com/", "uk-ireland"),
    ("gcc", "Middle East &amp; GCC", "Middle East &amp; GCC", "the GCC and the Middle East", "Attentive Science", "attentive-science-logo-uniform.png", "https://www.attentivescience.com/", "middle-east"),
    ("japan", "Japan", "Japan", "Japan", "Oriental Giken", "oriental-logo-uniform.png", "https://en.orientalgiken.co.jp/", "japan"),
    ("korea", "South Korea", "South Korea", "South Korea", "LK Lab Korea", "lk-lab-korea-logo-uniform.png", "https://www.lklab.com/", "korea"),
    ("anz", "Australia &amp; New Zealand", "Australia &amp; New Zealand", "Australia and New Zealand", "Able Scientific", "able-scientific-logo-uniform.png", "https://ablescientific.com.au/", "australia"),
]


def regions(img):
    tabs = [f'<div class="grp">Direct from Innovive</div>'
            f'<button class="tab direct" role="tab" id="gpt-direct" aria-controls="gpp-direct" aria-selected="true"><i></i>U.S. and Europe{ARROW}</button>'
            f'<div class="grp">Authorized partners</div>']
    panels = [f"""<div class="gp-panel on" role="tabpanel" id="gpp-direct" aria-labelledby="gpt-direct">
<div class="ph duo"><img src="{img('north-america')}" alt="San Diego skyline and the Coronado Bridge" loading="lazy"><img src="{img('europe')}" alt="The Eiffel Tower above the Seine in Paris" loading="lazy"></div>
<div class="bd"><span class="chip direct">Direct from Innovive</span><h3>U.S. and Europe</h3>
<p>Customers across North America and Europe work directly with Innovive for product selection, implementation and ongoing support.</p>
<div class="acts"><a class="btn btn-solid" href="{MAIL}">Contact info@innovive.com {ARROW}</a><a class="btn btn-line" href="/contact/">Contact form</a></div></div></div>"""]
    for tid, tlabel, head, cov, name, logo, url, ik in PARTNERS:
        tabs.append(f'<button class="tab" role="tab" id="gpt-{tid}" aria-controls="gpp-{tid}" aria-selected="false" tabindex="-1"><i></i>{tlabel}{ARROW}</button>')
        panels.append(f"""<div class="gp-panel" role="tabpanel" id="gpp-{tid}" aria-labelledby="gpt-{tid}">
<div class="ph"><img src="{img(ik)}" alt="" loading="lazy"></div>
<div class="bd"><span class="chip">Authorized partner</span><h3>{head}</h3>
<p>Innovive customers in {cov} are supported by {name}, our authorized regional partner, backed by Innovive's product expertise and quality standards.</p>
<div class="partner"><img src="{U}{logo}" alt="{name} logo" loading="lazy"><div><small>Authorized partner</small><b>{name}</b></div></div>
<div class="acts"><a class="btn btn-solid" href="{url}" target="_blank" rel="noopener">Visit {name} {EXT}</a></div>
<p class="note">Prefer to speak with Innovive directly? <a href="{MAIL}">info@innovive.com</a></p></div></div>""")
    return f"""<section class="gp gp-reg" id="your-region"><div class="wrap">
<div class="head rv"><div><span class="eyebrow"><i></i>Regional contacts</span><h2>Innovive in Your Region</h2></div>
<div><p>Innovive serves customers around the world through a combination of direct operations and authorized regional partners. This approach gives research teams access to local market knowledge while maintaining a consistent Innovive experience.</p>
<p>Select your region to connect with the right Innovive representative.</p></div></div>
<div class="gp-sel rv"><div class="gp-tabs" role="tablist" aria-label="Regions">{''.join(tabs)}</div>
<div>{''.join(panels)}</div></div>
</div></section>"""


def cta():
    return f"""<section class="gp gp-cta"><div class="wrap"><div class="card rv">
<div><h2>Not sure who to contact?</h2><p>Tell us where your research is based and we will connect you with the right Innovive team or partner.</p></div>
<div class="acts"><a class="btn btn-light" href="/contact/">Contact Innovive {ARROW}</a><a class="btn btn-ghost" href="{MAIL}">info@innovive.com</a></div>
</div></div></section>"""


JS = r"""<script>(function(){if(window.__gpInit)return;window.__gpInit=1;
function init(){var root=document.documentElement;root.classList.add('gp-js');
var tabs=[].slice.call(document.querySelectorAll('.gp .tab'));
function sel(t,focus){tabs.forEach(function(x){var on=x===t;x.setAttribute('aria-selected',on);x.tabIndex=on?0:-1;var p=document.getElementById(x.getAttribute('aria-controls'));if(p)p.classList.toggle('on',on);});if(focus)t.focus();
if(window.innerWidth<=1024)t.scrollIntoView({block:'nearest',inline:'center',behavior:'smooth'});}
tabs.forEach(function(t,i){t.addEventListener('click',function(){sel(t)});t.addEventListener('keydown',function(e){var k=e.key,n=null;if(k==='ArrowDown'||k==='ArrowRight')n=tabs[(i+1)%tabs.length];if(k==='ArrowUp'||k==='ArrowLeft')n=tabs[(i-1+tabs.length)%tabs.length];if(k==='Home')n=tabs[0];if(k==='End')n=tabs[tabs.length-1];if(n){e.preventDefault();sel(n,true);}});});
var els=[].slice.call(document.querySelectorAll('.gp .rv'));
if(!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('in')});return;}
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}})},{rootMargin:'0px 0px -8% 0px'});
els.forEach(function(e){io.observe(e)});}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();})();</script>"""


def render(img):
    return [("hero", "<style>" + CSS + "</style>" + hero()), ("network", network(img)),
            ("regions", regions(img)), ("cta", cta() + JS)]
