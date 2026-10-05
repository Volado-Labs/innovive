"""Build the raster assets the Klaviyo templates reference, into img/.

Email clients cannot do CSS masks or gradients over images reliably, so the
soft-edge bleed Robin liked in the Inno+ social post is baked into the JPEG:
the top fades out of the header navy and the bottom fades into the white body.

    python3 build_assets.py

Inputs live in source/. When Robin sends the original Inno+ photo, drop it in
source/ and point INNOPLUS_PHOTO (and INNOPLUS_CROP) at it; the current crop
comes from her flattened social post, which is why it starts below the text.
"""
import subprocess
from pathlib import Path

from PIL import Image, ImageFilter

HERE = Path(__file__).parent
SRC = HERE / "source"
OUT = HERE / "img"

NAVY_INNOPLUS = (8, 24, 49)      # #081831, header band of the Inno+ email
WHITE = (255, 255, 255)
MAGENTA = "#d12e86"              # sampled from the icons in Robin's ad

INNOPLUS_PHOTO = SRC / "innoplus-social-post-2026-09-22.png"
INNOPLUS_TOP = 352        # first photo row below the ad copy
INNOPLUS_BOTTOM = 816     # last row above the ad's tiles
INNOPLUS_FADE_END = 383   # source row just above the heads: the navy gradient is clear by here
# Revision 2026-10-05 (Robin): more headroom above the subjects BEFORE the gradient
# starts. The flattened post has only ~30px of rack above the heads (the ad's ghosted
# text sits above that), so the extra height is the rack band just above the heads,
# mirrored upward and heavily blurred. It only ever shows through the navy gradient,
# which now finishes before the heads instead of over them. Replace with a straight
# crop when Robin sends the original photo.
INNOPLUS_EXTENSION = 120  # px of blurred rack added above the photo, at 1200px wide
INNOPLUS_HEADROOM = 20    # px of solid navy above that

ICONS = {
    # file stem in img/   : Lucide icon in source/
    "icon-husbandry": "rat",
    "icon-health": "stethoscope",
    "icon-management": "shield-check",   # replaces the "bellhop" figure Robin disliked
    "icon-research": "microscope",
}


def smoothstep(t):
    t = min(max(t, 0), 1)
    return t * t * (3 - 2 * t)


def innoplus_hero():
    src = Image.open(INNOPLUS_PHOTO).convert("RGB")
    sc = 1200 / src.width
    photo = src.crop((0, INNOPLUS_TOP, src.width, INNOPLUS_BOTTOM))
    photo = photo.resize((1200, round(photo.height * sc)), Image.LANCZOS)

    band = src.crop((0, INNOPLUS_TOP, src.width, INNOPLUS_TOP + 40))
    band = band.resize((1200, round(40 * sc)), Image.LANCZOS)
    ext, pad = INNOPLUS_EXTENSION, INNOPLUS_HEADROOM
    e = Image.new("RGB", (1200, ext))
    y, flip = ext, True
    while y > 0:
        y -= band.height
        e.paste(band.transpose(Image.FLIP_TOP_BOTTOM) if flip else band, (0, y))
        flip = not flip
    e = e.filter(ImageFilter.GaussianBlur(14))

    H = pad + ext + photo.height
    im = Image.new("RGB", (1200, H), NAVY_INNOPLUS)
    im.paste(e, (0, pad))
    im.paste(photo, (0, pad + ext))

    def mask(fn):
        m = Image.new("L", (1, H))
        for yy in range(H):
            m.putpixel((0, yy), int(255 * fn(yy)))
        return m.resize((1200, H))

    join, seam = pad + ext, 28   # ease the blurred extension into the sharp photo
    im = Image.composite(im.filter(ImageFilter.GaussianBlur(10)), im,
                         mask(lambda yy: 1 - smoothstep((yy - (join - seam // 2)) / seam)))
    fade_end = join + round((INNOPLUS_FADE_END - INNOPLUS_TOP) * sc)
    im = Image.composite(Image.new("RGB", (1200, H), NAVY_INNOPLUS), im,
                         mask(lambda yy: 1 - smoothstep((yy - pad) / (fade_end - pad))))
    b = int(H * 0.18)
    im = Image.composite(Image.new("RGB", (1200, H), WHITE), im,
                         mask(lambda yy: (max(yy - (H - b), 0) / b) ** 2))
    im.save(OUT / "innoplus-hero.jpg", quality=82, optimize=True, progressive=True)


def icons():
    for stem, lucide in ICONS.items():
        svg = (SRC / f"{lucide}.svg").read_text()
        svg = svg.replace('stroke="currentColor"', f'stroke="{MAGENTA}"')
        svg = svg.replace('stroke-width="2"', 'stroke-width="1.6"')
        subprocess.run(
            ["rsvg-convert", "-w", "96", "-h", "96", "-o", str(OUT / f"{stem}.png")],
            input=svg.encode(), check=True,
        )


def gcc_products():
    """One image for both product shots: fewer images is kinder to deliverability."""
    W, H, gap = 1200, 560, 16
    canvas = Image.new("RGB", (W, H), WHITE)

    rack = Image.open(SRC / "hiw-innorack.jpg").convert("RGB")
    lw = 520
    scale = H / rack.height
    rack = rack.resize((round(rack.width * scale), H), Image.LANCZOS)
    x0 = (rack.width - lw) // 2
    canvas.paste(rack.crop((x0, 0, x0 + lw, H)), (0, 0))

    cage = Image.open(SRC / "mouse-cage-full.jpg").convert("RGB")
    # the render sits left of a wide white margin; trim to the product itself
    ink = Image.eval(cage.convert("L"), lambda v: 255 if v < 238 else 0).getbbox()
    cage = cage.crop(ink)
    rw = W - lw - gap
    cage.thumbnail((rw - 60, H - 60), Image.LANCZOS)
    panel = Image.new("RGB", (rw, H), WHITE)
    panel.paste(cage, ((rw - cage.width) // 2, (H - cage.height) // 2))
    canvas.paste(panel, (lw + gap, 0))

    canvas.save(OUT / "gcc-products.jpg", quality=82, optimize=True, progressive=True)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    innoplus_hero()
    icons()
    gcc_products()
    for f in sorted(OUT.iterdir()):
        print(f"{f.stat().st_size // 1024:>5} KB  {f.name}")
