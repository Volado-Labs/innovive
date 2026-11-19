"""Build live Elementor payloads for the 2026-11-19 publish.

1. /mouse-caging-btm/ (3627): replaced with the approved preview (Robin's 11/19 markup,
   volado-reports 11eb7ef), as one scoped HTML widget, with the published-research
   section in the Nov 6 rail design.
2. Innorack IVC Mouse (2677), Aquavive (2472), M-DIVIDER2 (1818), Metabolic cage kit (3140):
   a "Published Research" rail section appended as the last top-level container.

Usage: python3 studies-and-mouse-cage-build.py <dir with page-<id>.json> <preview index.html>
Writes payload-<id>.json in the same dir. Read-only otherwise.
"""
import json, re, sys, secrets

D, PREVIEW = sys.argv[1], sys.argv[2]

def nid():
    return secrets.token_hex(4)[:7]

STUDIES = {
    "validation": ("JAALAS · 2022",
        "Validation of Sanitization Practices in Single-use Individually Ventilated Mouse Cages at Standard and Thermoneutral Temperatures",
        "On Innorack 3.5 racks, changing the cage bottom and water every 14 days and the full cage every 28 days met sanitation standards at both standard and warm (thermoneutral) room temperatures.",
        "https://doi.org/10.30802/aalas-jaalas-22-000036"),
    "aquavive": ("JAALAS · 2025",
        "Extended Sanitization Frequency for Bottles: Using Volume as an Alternative to Time-Scheduled Replacements for Mice in Disposable Individually Ventilated Caging Systems",
        "Prefilled Aquavive bottles left on cages until 100 mL remained (13 to 47 days) caused no change in mouse weight, body condition or water intake, and no bacterial growth.",
        "https://doi.org/10.30802/aalas-jaalas-25-116"),
    "divider": ("JAALAS · 2026 (AALAS National Meeting abstract)",
        "Evaluating a Cage Divider System as an Alternative to Singly Housing Mice and its Effect on Animal Well-Being",
        "A feeder-mounted divider with a lid giving each side its own water let male mice live as divided pairs instead of alone, with no aggression, no change in weight or body condition, and better nests.",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC13641234/"),
    "metabolic": ("Cancer Research Communications · 2026",
        "Mechanisms Underlying Cedazuridine-Mediated Enhancement of Oral Decitabine Bioavailability",
        "Mice were housed in the Innovive metabolic cage for up to 23 hours so researchers could collect urine and feces separately during a cancer drug study.",
        "https://doi.org/10.1158/2767-9764.crc-25-0764"),
}

# Nov 6 approved design (volado-reports e08b3ae), minus the dropped 500+ stat.
RES_CSS = """
.ivres{background:#fff;padding:72px 0;font-family:Inter,system-ui,sans-serif;color:#00223D}
.ivres *{box-sizing:border-box}
.ivres .ivres-wrap{max-width:1200px;margin:0 auto;padding:0 24px}
.ivres .ivres-center{text-align:center}
.ivres h2.ivres-h{font-family:Inter,sans-serif;font-size:clamp(26px,3vw,36px);font-weight:700;letter-spacing:-.01em;line-height:1.2;color:#00223D;margin:0 0 12px}
.ivres .ivres-sub{font-size:17px;line-height:1.6;color:#666666;max-width:720px;margin:0 auto}
.ivres .ivres-railwrap{position:relative;max-width:980px;margin:32px auto 0}
.ivres .ivres-rail{display:grid;grid-auto-flow:column;grid-auto-columns:calc((100% - 16px)/2);gap:16px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-behavior:smooth;scrollbar-width:none;padding:2px}
.ivres .ivres-rail::-webkit-scrollbar{display:none}
.ivres .ivres-study{scroll-snap-align:start;border:1px solid #DAEBF8;border-radius:10px;padding:16px 18px;display:flex;flex-direction:column;background:#fff;text-align:left}
.ivres .ivres-meta{font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#005287;margin-bottom:6px;line-height:1.4}
.ivres h3.ivres-title{font-family:Inter,sans-serif;font-size:14.5px;font-weight:700;line-height:1.35;margin:0 0 6px;color:#00223D}
.ivres .ivres-study p{font-size:13.5px;line-height:1.5;margin:0 0 8px;flex:1;color:#666666}
.ivres a.ivres-more{font-weight:600;font-size:13.5px;color:#005287;text-decoration:none}
.ivres a.ivres-more:hover{text-decoration:underline}
.ivres .ivres-nav{display:flex;justify-content:center;align-items:center;gap:14px;margin-top:16px;font-size:13px;color:#666666}
.ivres .ivres-nav button{width:34px;height:34px;border-radius:50%;border:1px solid #DAEBF8;background:#fff;color:#005287;font-size:16px;cursor:pointer;line-height:1;padding:0}
.ivres .ivres-nav button:disabled{opacity:.35;cursor:default}
.ivres .ivres-disclose{margin:14px 0 0;font-size:12px;line-height:1.5;color:#666666;text-align:center}
@media(max-width:700px){.ivres .ivres-rail{grid-auto-columns:88%}}
"""

RES_JS = """(function(){var root=document.getElementById('published-research');if(!root)return;
var r=root.querySelector('.ivres-rail'),nav=root.querySelector('.ivres-nav'),p=nav.children[0],c=nav.children[1],n=nav.children[2];
var cards=r.children,total=cards.length;
function per(){return window.innerWidth<=700?1:2}
function upd(){var k=per();if(total<=k){nav.style.display='none';r.style.justifyContent='center';return}nav.style.display='';r.style.justifyContent='';
var w=cards[0].getBoundingClientRect().width+16,i=Math.round(r.scrollLeft/w);
c.textContent=(i+1)+'\\u2013'+Math.min(i+k,total)+' of '+total+' studies';p.disabled=i<=0;n.disabled=i+k>=total;}
function go(d){var w=cards[0].getBoundingClientRect().width+16;r.scrollBy({left:d*w*per(),behavior:'smooth'})}
p.onclick=function(){go(-1)};n.onclick=function(){go(1)};r.addEventListener('scroll',function(){window.requestAnimationFrame(upd)});window.addEventListener('resize',upd);upd();})();"""


def research_html(keys, sub, with_css=True):
    cards = "".join(
        f'<article class="ivres-study"><div class="ivres-meta">{m}</div><h3 class="ivres-title">{t}</h3>'
        f'<p>{s}</p><a class="ivres-more" href="{u}" target="_blank" rel="noopener">Read the study <span aria-hidden="true">&rarr;</span></a></article>'
        for m, t, s, u in (STUDIES[k] for k in keys))
    css = f"<style>{RES_CSS}</style>" if with_css else ""
    return (f'{css}<section class="ivres" id="published-research"><div class="ivres-wrap">'
            f'<div class="ivres-center"><h2 class="ivres-h">Published Research</h2><p class="ivres-sub">{sub}</p></div>'
            f'<div class="ivres-railwrap"><div class="ivres-rail">{cards}</div>'
            f'<div class="ivres-nav"><button type="button" aria-label="Previous studies">&larr;</button><span></span>'
            f'<button type="button" aria-label="More studies">&rarr;</button></div></div>'
            f'<p class="ivres-disclose">Independent studies that used Innovive products, selected by Innovive. Summaries are our own; see each paper for full methods and results.</p>'
            f'</div></section><script>{RES_JS}</script>')


def html_container(html):
    return {"id": nid(), "elType": "container", "isInner": False,
            "settings": {"content_width": "full", "flex_gap": {"column": "0", "row": "0", "isLinked": True, "unit": "px", "size": 0},
                         "padding": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True},
                         "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}},
            "elements": [{"id": nid(), "elType": "widget", "widgetType": "html", "isInner": False,
                          "settings": {"html": html}, "elements": []}]}


# ---------- mouse cage page from the preview ----------
def scope_css(css, scope):
    out = []
    def pref(sel):
        sel = sel.strip()
        if sel in ("body", "html"):
            return scope
        return f"{scope} {sel}"
    def rules(block):
        res = []
        for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", block):
            sels, body = m.group(1), m.group(2)
            res.append(",".join(pref(s) for s in sels.split(",")) + "{" + body + "}")
        return "".join(res)
    i = 0
    while i < len(css):
        if css.startswith("@media", i):
            start = css.index("{", i)
            depth, j = 1, start + 1
            while depth:
                depth += {"{": 1, "}": -1}.get(css[j], 0); j += 1
            out.append(css[i:start] + "{" + rules(css[start + 1:j - 1]) + "}")
            i = j
        else:
            nxt = css.find("@media", i)
            nxt = len(css) if nxt < 0 else nxt
            out.append(rules(css[i:nxt]))
            i = nxt
    return "".join(out)


src = open(PREVIEW).read()
css = re.search(r"<style>(.*?)</style>", src, re.S).group(1)
css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
keep = []
for m in re.finditer(r"(@media[^{]*\{(?:[^{}]*\{[^{}]*\})*[^{}]*\}|[^{}@]+\{[^{}]*\})", css):
    rule = m.group(0).strip()
    head = rule.split("{")[0]
    if re.search(r"\.review|\.confirm|\.toggle|header\.site|nav\.main|\.notes|footer|\.pubres|^\*|html\{|^html", head.strip()):
        continue
    if head.strip() == ":root":
        rule = rule.replace(":root", "body")  # vars land on the scope element
    keep.append(rule)
mc_css = scope_css("".join(keep), ".ivmc")
mc_css = mc_css.replace(".ivmc *{", ".ivmc *{")
# Extra guards against Elementor kit / theme styles.
mc_css += (".ivmc{font-family:Inter,system-ui,sans-serif;color:var(--text);line-height:1.6;font-size:16px}"
           ".ivmc *{box-sizing:border-box}.ivmc img{height:auto}"
           ".ivmc a.btn-primary,.ivmc a.btn-primary:hover{color:#fff}"
           ".ivmc h1,.ivmc h2,.ivmc h3{font-family:Inter,sans-serif}"
           ".ivmc .tabs button:focus{outline:2px solid var(--accent);outline-offset:2px}")

body = src.split("<body>", 1)[1]
start = body.index('<section class="hero">')
end = body.index("<footer>")
main = body[start:end]
main = re.sub(r'<section class="pubres".*?</section>\s*', "@@RESEARCH@@", main, flags=re.S)
main = main.replace('<a href="/innovive/ivc-systems/">IVC Systems</a> / ', "")
main = main.replace('<div class="crumbs">Home / Products / ', '<div class="crumbs"><a href="https://innovive.com/">Home</a> / Products / ')
assert "/innovive/" not in main and "reports.voladolabs" not in main, "preview-only link left in page"
assert 'class="confirm"' not in main and 'class="review"' not in main
main = main.replace('id="mbtm"', 'id="specs-mbtm"').replace('id="mbtmxl"', 'id="specs-mbtmxl"')
research = research_html(["validation"], "Selected peer-reviewed studies that housed mice in Innocage&reg; cages.")
main = main.replace("@@RESEARCH@@", research)

ld = re.search(r'<script type="application/ld\+json">(.*?)</script>', src, re.S).group(1)
ldj = json.loads(ld)
for g in ldj["@graph"]:
    if g["@type"] == "BreadcrumbList":
        g["itemListElement"] = [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://innovive.com/"},
            {"@type": "ListItem", "position": 2, "name": "Mouse Cages", "item": "https://innovive.com/mouse-caging-btm/"}]

tab_js = """(function(){var bs=document.querySelectorAll('.ivmc .tabs button');
function show(t){bs.forEach(function(x){x.setAttribute('aria-selected',x.dataset.t===t?'true':'false');});
document.getElementById('specs-mbtm').hidden=t!=='mbtm';document.getElementById('specs-mbtmxl').hidden=t!=='mbtmxl';}
bs.forEach(function(b){b.addEventListener('click',function(){show(b.dataset.t);});});
var q=(new URLSearchParams(location.search).get('tab')||'').toUpperCase();if(q==='M-BTM-XL'||location.hash==='#specs-mbtmxl')show('mbtmxl');})();"""

mc_html = (f'<style>{mc_css}</style>'
           f'<script type="application/ld+json">{json.dumps(ldj, ensure_ascii=False)}</script>'
           f'<div class="ivmc">{main}</div><script>{tab_js}</script>')

# research section CSS must also be present on 3627 (it is inside research_html).
payloads = {3627: [html_container(mc_html)]}

ADD = {
    2677: (["validation"], "Selected peer-reviewed studies on the Innorack system and its components."),
    2472: (["aquavive"], "Selected peer-reviewed studies on Aquavive&reg; water for mice."),
    1818: (["divider"], "Selected peer-reviewed research on divided housing for mice."),
    3140: (["metabolic"], "Selected peer-reviewed studies that used the Innovive metabolic cage."),
}
for pid, (keys, sub) in ADD.items():
    page = json.load(open(f"{D}/page-{pid}.json"))
    data = json.loads(page["meta"]["_elementor_data"])
    assert 'id="published-research"' not in json.dumps(data), f"{pid} already has a research section"
    sec = html_container(research_html(keys, sub))
    # Keep the closing sales band last: insert above it when the page ends with one.
    if "Ready to order" in json.dumps(data[-1]):
        data.insert(len(data) - 1, sec)
    else:
        data.append(sec)
    payloads[pid] = data

for pid, data in payloads.items():
    json.dump({"meta": {"_elementor_data": json.dumps(data, ensure_ascii=False)}}, open(f"{D}/payload-{pid}.json", "w"), ensure_ascii=False)
    print(pid, len(json.dumps(data)))
