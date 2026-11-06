"""Builds the Innorack IVC Mouse mockup with a Published research section.
Usage: python3 build-innorack-mockup.py <image_dir> <out.html>
Images are inlined as data URIs so the file renders anywhere (artifacts block remote images)."""
import base64, sys, pathlib
img_dir, out = pathlib.Path(sys.argv[1]), sys.argv[2]
def uri(name):
    p = img_dir / name
    mime = {'.png': 'image/png', '.jpg': 'image/jpeg', '.webp': 'image/webp'}[p.suffix]
    return f"data:{mime};base64,{base64.b64encode(p.read_bytes()).decode()}"

STUDIES = [
    ("JAALAS", "2022", "Validation of Sanitization Practices in Single-use Individually Ventilated Mouse Cages at Standard and Thermoneutral Temperatures",
     "On Innorack 3.5 racks, changing the cage bottom and water every 14 days and the full cage every 28 days met sanitation standards at both standard and warm (thermoneutral) room temperatures.",
     "https://doi.org/10.30802/aalas-jaalas-22-000036"),
    ("JAALAS", "2022", "Using Filter Media and Soiled Bedding in Disposable Individually Ventilated Cages as a Refinement to SPF Mouse Health Monitoring Programs",
     "In disposable IVC with cage-level filters, testing filter media detected infections more reliably than testing sentinel mice directly.",
     "https://doi.org/10.30802/aalas-jaalas-22-000013"),
    ("JAALAS", "2025", "Extended Sanitization Frequency for Bottles: Using Volume as an Alternative to Time-Scheduled Replacements for Mice in Disposable Individually Ventilated Caging Systems",
     "Prefilled Aquavive bottles left on cages until 100 mL remained (13 to 47 days) caused no change in mouse weight, body condition or water intake, and no bacterial growth.",
     "https://doi.org/10.30802/aalas-jaalas-25-116"),
]
STUDIES.sort(key=lambda x: -int(x[1]))
cards = "\n".join(f"""      <article class="study">
        <div class="meta">{j} · {y}</div>
        <h3>{t}</h3>
        <p>{s}</p>
        <a class="more" href="{u}" target="_blank" rel="noopener">Read the study <span aria-hidden="true">→</span></a>
      </article>""" for j, y, t, s, u in STUDIES)

SPECS = [("Max cage positions", "Up to 192"), ("Configurations", "Single- and Double-Sided"), ("Row options", "9, 10, 11, or 12"),
         ("Column options", "6, 7, or 8"), ("Compatible caging", "Innocage® mouse system only"), ("Filtration", "Dual HEPA, supply and exhaust"),
         ("Airflow", "Patented transversal"), ("Pressure modes", "Positive and negative"), ("Ventilation", "Standard on-rack blowers, supply and exhaust"),
         ("Mobility", "Easy glide lockable casters"), ("Cleaning", "Wipe down with approved cleaning agents")]
spec_rows = "\n".join(f"        <tr><th>{a}</th><td>{b}</td></tr>" for a, b in SPECS)
comps = [("Cage bottom", "cage-bottom.jpg"), ("Lid", "lid-img.jpg"), ("Feeder", "feeder.jpg"), ("Water Solution", "water-solution.jpg")]
comp_cards = "\n".join(f'      <div class="comp"><img src="{uri(f)}" alt=""><div><b>{n}</b><a href="#">Explore</a></div></div>' for n, f in comps)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Innorack IVC Mouse with Published research (mockup)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{{--navy:#00223D;--blue:#005287;--para:#666666;--line:#DAEBF8;--tint:#F6F9FF;--grey:#F5F5F5;--teal:#75C6C1;--note:#fff4d6;--note-text:#6b4b00}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:Inter,system-ui,sans-serif;color:var(--navy);background:#fff;line-height:1.6;font-size:16px}}
img{{max-width:100%;display:block}}
a{{color:var(--blue);text-decoration:none}}
.wrap{{max-width:1240px;margin:0 auto;padding:0 24px}}
h1,h2,h3{{margin:0;line-height:1.25}}
p{{margin:0 0 14px;color:var(--para)}}
.btn{{display:inline-block;background:var(--blue);color:#fff;border-radius:8px;padding:10px 18px;font-weight:600;font-size:15px}}
section{{padding:72px 0}}
.center{{text-align:center}}
.sub{{max-width:600px;margin:12px auto 0;color:var(--para)}}
h2{{font-size:34px;font-weight:700;color:var(--navy)}}

/* review layer */
.review{{background:var(--note);color:var(--note-text);font-size:14px;padding:12px 0}}
.review b{{color:#4a3300}}
.tag{{display:inline-block;background:var(--note);color:var(--note-text);font-size:12px;font-weight:600;padding:3px 10px;border-radius:999px;margin-bottom:14px}}
body.clean .review,body.clean .tag{{display:none}}
.toggle{{position:fixed;right:16px;bottom:16px;z-index:50;background:var(--navy);color:#fff;border:0;border-radius:999px;padding:10px 16px;font:600 13px Inter,sans-serif;cursor:pointer;box-shadow:0 4px 14px rgba(0,0,0,.18)}}

/* header */
header{{position:sticky;top:0;z-index:40;background:var(--tint);padding:14px 0}}
.bar{{background:#fff;border-radius:10px;display:flex;align-items:center;justify-content:space-between;padding:10px 20px;box-shadow:0 1px 3px rgba(0,34,61,.06)}}
.bar img{{height:34px;width:auto}}
.bar nav{{display:flex;gap:26px;font-size:14px;font-weight:600}}
.bar nav a{{color:var(--navy)}}
@media(max-width:900px){{.bar nav{{display:none}}}}

/* hero */
.hero{{background:var(--tint);padding:28px 0 64px}}
.hero .wrap{{display:grid;grid-template-columns:420px 1fr;gap:56px;align-items:center}}
.hero .pic{{background:#fff;border-radius:12px;box-shadow:0 2px 12px rgba(0,34,61,.08);padding:28px;display:flex;justify-content:center}}
.hero .pic img{{height:330px;width:auto}}
.hero h1{{font-size:34px;font-weight:600;color:var(--blue);margin-bottom:6px}}
.hero .h2{{font-size:28px;font-weight:700;margin-bottom:18px}}
@media(max-width:860px){{.hero .wrap{{grid-template-columns:1fr}}}}

/* features */
.feats{{display:grid;grid-template-columns:1fr 1fr;gap:34px 64px;margin-top:44px}}
.feat h3{{font-size:18px;display:flex;gap:12px;align-items:center;margin-bottom:8px}}
.chk{{width:24px;height:24px;border-radius:4px;background:var(--blue);display:inline-flex;align-items:center;justify-content:center;flex:none}}
.feat ul{{margin:0;padding-left:52px;color:var(--para);font-size:15px}}
@media(max-width:760px){{.feats{{grid-template-columns:1fr}}}}

/* specs */
.specs{{background:var(--tint)}}
table.spec{{width:100%;max-width:1160px;margin:36px auto 28px;border-collapse:collapse;background:#fff;border-radius:6px;overflow:hidden;box-shadow:0 2px 14px rgba(0,34,61,.06);font-size:14px}}
table.spec th{{text-align:left;color:var(--blue);font-weight:600;padding:14px 22px;width:40%}}
table.spec td{{color:var(--para);padding:14px 22px}}
table.spec tr:nth-child(even){{background:var(--tint)}}

/* NEW: published research */
.research{{background:#fff}}
.research .stat{{display:inline-flex;gap:10px;align-items:center;background:var(--tint);border-radius:999px;padding:8px 18px;margin-top:20px;font-size:15px;color:var(--navy)}}
.research .stat b{{color:var(--blue);font-size:18px}}
.rail-wrap{{position:relative;max-width:980px;margin:32px auto 0}}
.rail{{display:grid;grid-auto-flow:column;grid-auto-columns:calc((100% - 16px)/2);gap:16px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-behavior:smooth;scrollbar-width:none;padding:2px}}
.rail::-webkit-scrollbar{{display:none}}
.study{{scroll-snap-align:start;border:1px solid var(--line);border-radius:10px;padding:16px 18px;display:flex;flex-direction:column;background:#fff}}
.study .meta{{font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--blue);margin-bottom:6px}}
.study h3{{font-size:14.5px;font-weight:700;line-height:1.35;margin-bottom:6px}}
.study p{{font-size:13.5px;line-height:1.5;margin:0 0 8px;flex:1}}
.study .more{{font-weight:600;font-size:13.5px}}
.rail-nav{{display:flex;justify-content:center;align-items:center;gap:14px;margin-top:16px;font-size:13px;color:var(--para)}}
.rail-nav button{{width:34px;height:34px;border-radius:50%;border:1px solid var(--line);background:#fff;color:var(--blue);font-size:16px;cursor:pointer;line-height:1}}
.rail-nav button:disabled{{opacity:.35;cursor:default}}
.disclose{{margin-top:14px;font-size:12px;color:var(--para);text-align:center}}
@media(max-width:700px){{.rail{{grid-auto-columns:88%}}}}

/* compatible + components */
.compat{{display:grid;grid-template-columns:1fr 1fr;gap:20px}}
.compat .card{{border:1px solid var(--line);border-radius:6px;padding:40px 28px;text-align:center}}
.pill{{display:inline-block;background:#e9f5f4;color:var(--blue);font-size:11px;font-weight:700;letter-spacing:.06em;padding:4px 12px;border-radius:4px;margin-bottom:14px}}
.compat h3{{font-size:32px;margin-bottom:12px}}
.comps{{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:34px}}
.comp{{border:1px solid var(--line);border-radius:6px;padding:16px;display:flex;gap:16px;align-items:center}}
.comp img{{width:66px;height:66px;object-fit:cover;border-radius:4px}}
.comp b{{display:block;font-size:17px}}
.comp a{{font-size:14px;font-weight:600}}
@media(max-width:860px){{.compat,.comps{{grid-template-columns:1fr 1fr}}}}
.cta{{background:var(--navy);color:#fff;border-radius:12px;padding:48px;text-align:center}}
.cta h2{{color:#fff}} .cta p{{color:#DAEBF8}}
footer{{background:var(--navy);color:#DAEBF8;font-size:13px;padding:28px 0;margin-top:72px}}
footer .wrap{{display:flex;justify-content:space-between;align-items:center;padding-right:190px}}
footer img{{height:30px;width:auto}}
</style>
</head>
<body>
<div class="review"><div class="wrap"><b>Mockup for review.</b> This is the live Innorack IVC Mouse page with one new section, <b>Published research</b>, added below the specifications. Nothing else on the page changes. Study links open the real papers. Use the button at the bottom right to hide these notes.</div></div>

<header><div class="wrap"><div class="bar">
  <img src="{uri('Innovive-Color-Logo-Dark-1.png')}" alt="Innovive">
  <nav><a href="#">Company ▾</a><a href="#">The Innovive System ▾</a><a href="#">Products ▾</a><a href="#">Vivarium Solutions ▾</a><a href="#">Customer Portal</a></nav>
  <a class="btn" href="#" style="font-size:13px;padding:8px 14px">Contact Us</a>
</div></div></header>

<section class="hero"><div class="wrap">
  <div class="pic"><img src="{uri('Mouse-Rack.png')}" alt="Innorack IVC Mouse 3.5 rack"></div>
  <div>
    <h1>Innorack IVC Mouse 3.5</h1>
    <div class="h2">Mouse IVC rack for up to 192 disposable cages</div>
    <p>It’s portable, ergonomic, and easy to configure top-of-the-line ventilated mouse housing system designed for Innovive disposable IVC cages. The rack is powered by patented transversal airflow and delivers dual HEPA-filtered air into each recyclable cage. Controlled airflow allows positive and negative modes of operation. It comes with a dynamic digital controller and provides a high-quality environment for your animals.</p>
    <a class="btn" href="#">Contact Sales</a>
  </div>
</div></section>

<section><div class="wrap">
  <h2 class="center">Innorack Mouse Racks Features</h2>
  <div class="feats">
    <div class="feat"><h3><span class="chk"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3"><path d="M5 12l5 5 9-10"/></svg></span>Dynamic Digital Controller</h3><ul><li>Dynamically maintains settings on both supply and exhaust blowers.</li><li>Quick-look color display for easy status monitoring.</li></ul></div>
    <div class="feat"><h3><span class="chk"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3"><path d="M5 12l5 5 9-10"/></svg></span>Ergonomic Design</h3><ul><li>Lightweight rack &amp; blowers.</li><li>Full cage visibility.</li></ul></div>
    <div class="feat"><h3><span class="chk"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3"><path d="M5 12l5 5 9-10"/></svg></span>Easy Cleaning and Maintenance</h3><ul><li>Continuous shelf design and smooth beveled surface allow for easy cleaning.</li><li>Quick-disconnect blowers.</li><li>Autoclavable Innorack available upon request.</li></ul></div>
    <div class="feat"><h3><span class="chk"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3"><path d="M5 12l5 5 9-10"/></svg></span>Low-Vibration Rack Operations</h3><ul><li>A low-vibration ventilation system creates a stress-free animal environment, contributing to animal welfare.</li></ul></div>
  </div>
</div></section>

<section class="specs"><div class="wrap center">
  <h2>Product Specifications</h2>
  <p class="sub">Comprehensive specifications including sizing, materials, components, and usage requirements</p>
  <table class="spec">
{spec_rows}
  </table>
  <a class="btn" href="#">Download data sheet</a>
</div></section>

<section class="research" id="published-research"><div class="wrap">
  <div class="center">
    <span class="tag">New section: two studies show at a time; use the arrows or swipe for more</span>
    <h2>Published Research</h2>
    <p class="sub">Selected peer-reviewed studies from the last 10 years on the Innorack system and its components.</p>
    <div class="stat"><b>500+</b> studies published in the last 10 years name Innovive caging in their methods</div>
  </div>
  <div class="rail-wrap">
    <div class="rail" id="rail">
{cards}
    </div>
    <div class="rail-nav"><button id="prev" aria-label="Previous studies">←</button><span id="count"></span><button id="next" aria-label="More studies">→</button></div>
  </div>
  <p class="disclose">Studies selected by Innovive. Summaries are our own; see each paper for full methods and results.</p>
</div></section>

<section style="padding-top:0"><div class="wrap">
  <div class="compat">
    <div class="card"><span class="pill">● COMPATIBLE CAGING</span><h3>Innocage® IVC Mouse</h3><p>Standard mouse housing solution with pre-bedded options.</p><a class="btn" href="#">View Caging</a></div>
    <div class="card"><span class="pill">● COMPATIBLE CAGING</span><h3>Metabolic Cage</h3><p>Industry’s first disposable recyclable metabolic cage that can be used with Innorack IVC Mouse.</p><a class="btn" href="#">View Caging</a></div>
  </div>
</div></section>

<section style="padding-top:0"><div class="wrap">
  <h2 class="center">Required Cage Components</h2>
  <p class="sub center">A complete cage requires the following components. All are designed to work together with the Innorack IVC Mouse.</p>
  <div class="comps">
{comp_cards}
  </div>
</div></section>

<div class="wrap"><div class="cta"><h2>Ready to order your Mouse IVC system?</h2><p>Our team can help you size the rack and caging for your facility and colony.</p><a class="btn" href="#" style="background:#fff;color:var(--blue)">Contact sales</a></div></div>

<footer><div class="wrap"><img src="{uri('Innovive-Grascale-Logo-Light-1.webp')}" alt="Innovive"><span>Mockup only. Not the live site.</span></div></footer>

<script>
(function(){{var r=document.getElementById('rail'),p=document.getElementById('prev'),n=document.getElementById('next'),c=document.getElementById('count');
var cards=r.children,total=cards.length;
function per(){{return window.innerWidth<=700?1:2}}
function upd(){{var w=cards[0].getBoundingClientRect().width+16,i=Math.round(r.scrollLeft/w),k=per();
c.textContent=(i+1)+'–'+Math.min(i+k,total)+' of '+total+' studies';p.disabled=i<=0;n.disabled=i+k>=total;}}
function go(d){{var w=cards[0].getBoundingClientRect().width+16;r.scrollBy({{left:d*w*per(),behavior:'smooth'}})}}
p.onclick=function(){{go(-1)}};n.onclick=function(){{go(1)}};r.addEventListener('scroll',function(){{window.requestAnimationFrame(upd)}});window.addEventListener('resize',upd);upd();}})();
</script>
<button class="toggle" onclick="document.body.classList.toggle('clean');this.textContent=document.body.classList.contains('clean')?'Show review notes':'Hide review notes'">Hide review notes</button>
</body>
</html>
"""
pathlib.Path(out).write_text(html)
print(len(html))
