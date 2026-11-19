"""Dot-matrix world map from Natural Earth (world-atlas topojson). Pure Python."""
import json, math
T = json.load(open('land.json'))
sc, tr = T['transform']['scale'], T['transform']['translate']
arcs = []
for a in T['arcs']:
    x = y = 0; pts = []
    for dx, dy in a:
        x += dx; y += dy
        pts.append((x*sc[0]+tr[0], y*sc[1]+tr[1]))
    arcs.append(pts)
def ring(idx):
    out = []
    for i in idx:
        p = arcs[i] if i >= 0 else arcs[~i][::-1]
        out.extend(p if not out else p[1:])
    return out
polys = []
geom = T['objects']['land']
for g in geom['geometries'] if geom['type']=='GeometryCollection' else [geom]:
    for poly in (g['arcs'] if g['type']=='MultiPolygon' else [g['arcs']]):
        rings = [ring(r) for r in poly]
        bb = [min(p[0] for p in rings[0]), min(p[1] for p in rings[0]), max(p[0] for p in rings[0]), max(p[1] for p in rings[0])]
        polys.append((bb, rings))
def inring(x, y, r):
    c = False; j = len(r)-1
    for i in range(len(r)):
        xi, yi = r[i]; xj, yj = r[j]
        if (yi > y) != (yj > y) and x < (xj-xi)*(y-yi)/(yj-yi)+xi: c = not c
        j = i
    return c
def land(lon, lat):
    for bb, rings in polys:
        if bb[0] <= lon <= bb[2] and bb[1] <= lat <= bb[3]:
            if inring(lon, lat, rings[0]) and not any(inring(lon, lat, h) for h in rings[1:]):
                return True
    return False
# equirectangular, cropped
LON0, LON1, LAT0, LAT1 = -170, 190, -56, 78
W = 1200; STEP = 1.55  # degrees between dots
H = W*(LAT1-LAT0)/(LON1-LON0)
def proj(lon, lat):
    return ((lon-LON0)/(LON1-LON0)*W, (LAT1-lat)/(LAT1-LAT0)*H)
d = []; n = 0
lat = LAT1 - STEP/2
while lat > LAT0:
    lon = LON0 + STEP/2
    while lon < LON1:
        L = lon - 360 if lon > 180 else lon
        if land(L, lat):
            x, y = proj(lon, lat); d.append(f"M{x:.1f} {y:.1f}h0"); n += 1
        lon += STEP
    lat -= STEP
json.dump({"W": W, "H": round(H, 1), "d": "".join(d), "n": n, "bounds": [LON0, LON1, LAT0, LAT1]}, open('dotmap.json', 'w'))
print(n, "dots", len("".join(d)), "bytes", "H", round(H,1))
