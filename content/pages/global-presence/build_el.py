import json, secrets, gp_sections as g
media = json.load(open('media.json'))
secs = g.render(lambda k: media[k]['url'])
nid = lambda: secrets.token_hex(4)[:7]
zero = {"unit":"px","top":"0","right":"0","bottom":"0","left":"0","isLinked":True}
data = [{"id": nid(), "elType": "container", "isInner": False,
         "settings": {"content_width": "full", "flex_direction": "column", "padding": zero, "margin": zero,
                      "flex_gap": {"unit":"px","size":0,"column":"0","row":"0"}, "_title": f"Global Presence: {k}"},
         "elements": [{"id": nid(), "elType": "widget", "widgetType": "html", "settings": {"html": h}, "elements": []}]} for k, h in secs]
raw = json.dumps(data, separators=(",",":"), ensure_ascii=True)
json.dump({"meta": {"_elementor_data": raw, "_elementor_edit_mode": "builder"}}, open('update.json','w'))
open('gp_v3_data.json','w').write(raw)
