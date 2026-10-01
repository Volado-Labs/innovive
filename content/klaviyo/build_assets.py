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

from PIL import Image

HERE = Path(__file__).parent
SRC = HERE / "source"
OUT = HERE / "img"

NAVY_INNOPLUS = (8, 24, 49)      # #081831, header band of the Inno+ email
WHITE = (255, 255, 255)
MAGENTA = "#d12e86"              # sampled from the icons in Robin's ad

INNOPLUS_PHOTO = SRC / "innoplus-social-post-2026-09-22.png"
INNOPLUS_CROP = (0, 378, 1254, 816)   # photo only: below the ad copy, above its tiles

ICONS = {
    # file stem in img/   : Lucide icon in source/
    "icon-husbandry": "rat",
    "icon-health": "stethoscope",
    "icon-management": "shield-check",   # replaces the "bellhop" figure Robin disliked
    "icon-research": "microscope",
}


def fade(im, color, top_frac, bottom_frac, bottom_color):
    """Blend the top band into `color` and the bottom band into `bottom_color`."""
    w, h = im.size
    top = Image.new("RGB", (w, h), color)
    bottom = Image.new("RGB", (w, h), bottom_color)
    mask_top = Image.new("L", (1, h))
    mask_bottom = Image.new("L", (1, h))
    t, b = int(h * top_frac), int(h * bottom_frac)
    for y in range(h):
        # ease-out so the photo emerges gently rather than along a visible line
        mask_top.putpixel((0, y), int(255 * (1 - min(y / t, 1)) ** 1.4) if t else 0)
        d = y - (h - b)
        mask_bottom.putpixel((0, y), int(255 * (max(d, 0) / b) ** 2) if b else 0)
    im = Image.composite(top, im, mask_top.resize((w, h)))
    return Image.composite(bottom, im, mask_bottom.resize((w, h)))


def innoplus_hero():
    im = Image.open(INNOPLUS_PHOTO).convert("RGB").crop(INNOPLUS_CROP)
    im = im.resize((1200, round(1200 * im.height / im.width)), Image.LANCZOS)
    im = fade(im, NAVY_INNOPLUS, 0.5, 0.22, WHITE)
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
