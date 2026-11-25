#!/usr/bin/env python3
"""Draw the 25 November 2026 world-news front page (1024x1024 PNG).

Run once, locally, to produce entry.png. The entry program itself is
main.py, which only copies entry.png to /output/entry.png, so the grader
never needs PIL or fonts. All text is rendered here, from real reporting
of Wednesday 25 November 2026 (Ukraine confirms the Sparta II strike in
the Gulf of Finland; CIA/ODNI breach; Huawei guilty on 10 of 12 counts;
Houthis hit Riyadh's tallest tower; Putin vows retaliation; WHO evacuates
its Ebola team in Ituri).
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 231)
INK = (18, 18, 18)
NAVY = (14, 34, 56)
NAVY2 = (22, 48, 79)
RED = (178, 34, 34)
GOLD = (201, 162, 39)
GRAY = (90, 86, 76)
CARD = (255, 253, 247)
BORDER = (206, 198, 178)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def star(d, cx, cy, r_out, r_in, points, fill, rot=-90):
    pts = []
    for i in range(points * 2):
        r = r_out if i % 2 == 0 else r_in
        a = math.radians(rot + i * 180 / points)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    d.polygon(pts, fill=fill)


def wrap(d, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = f"{cur} {w}".strip()
        if d.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(d, x, y, text, fnt, max_w, fill, leading=1.18):
    lines = wrap(d, text, fnt, max_w)
    for ln in lines:
        d.text((x, y), ln, font=fnt, fill=fill)
        y += int(fnt.size * leading)
    return y


# ---------------------------------------------------------------- canvas
img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- masthead -----------------------------------------------------------
d.rectangle([0, 0, W, 96], fill=NAVY)
d.rectangle([0, 96, W, 100], fill=GOLD)
title = "THE WORLD TODAY"
tf = font(SERIF_B, 58)
d.text(((W - d.textlength(title, font=tf)) / 2, 14), title, font=tf, fill=(255, 255, 255))
tag = "ONE DAY  •  EVERY CONTINENT  •  IN ONE PICTURE"
tg = font(SANS_B, 15)
d.text(((W - d.textlength(tag, font=tg)) / 2, 74), tag, font=tg, fill=GOLD)

# ---- date bar -----------------------------------------------------------
date = "WEDNESDAY, 25 NOVEMBER 2026"
df = font(SERIF_B, 46)
dw = d.textlength(date, font=df)
d.text(((W - dw) / 2, 112), date, font=df, fill=INK)
d.line([26, 136, (W - dw) / 2 - 18, 136], fill=RED, width=3)
d.line([(W + dw) / 2 + 18, 136, W - 26, 136], fill=RED, width=3)
sub = "The day's world news, as reported on Wednesday 25 November 2026"
sf = font(SANS, 19)
d.text(((W - d.textlength(sub, font=sf)) / 2, 164), sub, font=sf, fill=GRAY)

# ---- lead card: Sparta II, Gulf of Finland ------------------------------
LX, LY, LW, LH = 26, 196, 972, 272
d.rectangle([LX, LY, LX + LW, LY + LH], fill=CARD, outline=BORDER, width=2)
# illustration: night sea, burning cargo ship, drone, left half
IX, IY, IW, IH = LX + 2, LY + 2, 452, LH - 4
d.rectangle([IX, IY, IX + IW, IY + IH], fill=(12, 30, 52))
# stars
for sx, sy in ((30, 18), (90, 34), (160, 14), (240, 26), (330, 16), (410, 30),
               (60, 60), (380, 56), (200, 44)):
    d.ellipse([IX + sx - 1, IY + sy - 1, IX + sx + 1, IY + sy + 1],
              fill=(255, 255, 255))
# moon, top-left, clear of the smoke at top-right
d.ellipse([IX + 18, IY + 12, IX + 58, IY + 52], fill=(240, 230, 190))
d.ellipse([IX + 26, IY + 16, IX + 58, IY + 48], fill=(12, 30, 52))
# sea
d.rectangle([IX, IY + 150, IX + IW, IY + IH], fill=(8, 22, 40))
for wx in range(IX + 6, IX + IW - 20, 44):
    d.arc([wx, IY + IH - 66, wx + 34, IY + IH - 48], 180, 360,
          fill=(90, 150, 190), width=2)
    d.arc([wx + 20, IY + IH - 34, wx + 54, IY + IH - 16], 180, 360,
          fill=(70, 120, 160), width=2)
# cargo ship Sparta II, centre
hx, hy = IX + 70, IY + 128
# containers
d.rectangle([hx + 20, hy - 46, hx + 90, hy - 22], fill=(178, 90, 34))
d.rectangle([hx + 96, hy - 46, hx + 166, hy - 22], fill=(60, 120, 90))
d.rectangle([hx + 58, hy - 70, hx + 128, hy - 46], fill=(140, 60, 60))
d.rectangle([hx + 172, hy - 46, hx + 242, hy - 22], fill=(90, 100, 140))
# bridge tower
d.rectangle([hx + 250, hy - 66, hx + 292, hy - 22], fill=(220, 220, 210))
for wy in (hy - 60, hy - 48, hy - 36):
    d.rectangle([hx + 256, wy, hx + 286, wy + 8], fill=(255, 200, 90))
d.rectangle([hx + 268, hy - 84, hx + 274, hy - 66], fill=(220, 220, 210))
# hull
d.polygon([(hx, hy - 22), (hx + 320, hy - 22), (hx + 300, hy + 16),
           (hx + 18, hy + 16)], fill=(28, 32, 38))
d.rectangle([hx, hy - 22, hx + 320, hy - 16], fill=(60, 64, 70))
# fire at the stern (bow of the blast, starboard side)
star(d, hx + 310, hy - 30, 26, 10, 8, (255, 160, 40))
star(d, hx + 310, hy - 30, 14, 6, 8, (255, 230, 150))
star(d, hx + 282, hy - 52, 14, 6, 8, (255, 120, 30))
# smoke
d.ellipse([hx + 286, hy - 96, hx + 330, hy - 62], fill=(90, 88, 84))
d.ellipse([hx + 306, hy - 116, hx + 346, hy - 84], fill=(120, 116, 110))
d.ellipse([hx + 326, hy - 132, hx + 360, hy - 104], fill=(150, 146, 140))
# naval drone skimming in from the left
d.line([IX + 14, IY + 96, hx - 30, hy - 18], fill=(255, 220, 120), width=3)
d.ellipse([IX + 8, IY + 90, IX + 28, IY + 102], fill=(20, 20, 20))
d.line([IX + 6, IY + 88, IX + 30, IY + 88], fill=(200, 200, 200), width=2)
d.line([IX + 6, IY + 104, IX + 30, IY + 104], fill=(200, 200, 200), width=2)
# ship-name ribbon across the bottom of the art
ry = IY + IH - 44
d.rectangle([IX + 34, ry, IX + IW - 34, ry + 32], fill=RED)
rb = "SPARTA II  •  GULF OF FINLAND"
rf = font(SANS_B, 21)
d.text(((IW - d.textlength(rb, font=rf)) / 2 + IX, ry + 4), rb, font=rf,
       fill=(255, 255, 255))
# lead text, right half
TX = IX + IW + 24
TW = LX + LW - TX - 22
d.text((TX, LY + 22), "WAR  •  GULF OF FINLAND", font=font(SANS_B, 21), fill=RED)
y = text_block(d, TX, LY + 52, "ZELENSKIY: WE HIT THE SPARTA II",
               font(SERIF_B, 38), TW, INK, 1.12)
y += 8
d.line([TX, y, TX + 120, y], fill=RED, width=3)
y += 12
text_block(d, TX, y, "Kyiv confirms Saturday's drone strike on the Russian "
           "cargo ship \u2014 Norway urges caution.",
           font(SANS, 20), TW, GRAY, 1.25)

# ---- middle row ---------------------------------------------------------
MY, MH = 482, 224
MW = (972 - 14) // 2


def mid_card(x, kicker, headline, subline, draw_art):
    d.rectangle([x, MY, x + MW, MY + MH], fill=CARD, outline=BORDER, width=2)
    ax, ay, aw, ah = x + 2, MY + 2, MW - 4, 104
    draw_art(ax, ay, aw, ah)
    tx, tw = x + 18, MW - 36
    d.text((tx, MY + 116), kicker, font=font(SANS_B, 19), fill=RED)
    y = text_block(d, tx, MY + 140, headline, font(SERIF_B, 26), tw, INK, 1.1)
    text_block(d, tx, y + 4, subline, font(SANS, 18), tw, GRAY, 1.2)


def art_breach(ax, ay, aw, ah):
    # dark terminal, broken padlock, red BREACH stamp
    d.rectangle([ax, ay, ax + aw, ay + ah], fill=(10, 16, 24))
    # code lines
    for i, ly in enumerate(range(ay + 14, ay + ah - 12, 14)):
        wdt = 150 if i % 3 == 0 else (220 if i % 3 == 1 else 120)
        d.rectangle([ax + 16, ly, ax + 16 + wdt, ly + 5],
                    fill=(40, 120, 80) if i % 2 else (30, 90, 110))
    # cursor block
    d.rectangle([ax + 16, ay + ah - 22, ax + 30, ay + ah - 12],
                fill=(120, 230, 140))
    # padlock, right side, shackle broken open
    px, py = ax + aw - 130, ay + 22
    d.rounded_rectangle([px, py + 22, px + 76, py + 66], radius=8,
                        fill=(200, 170, 60))
    d.ellipse([px + 30, py + 36, px + 46, py + 52], fill=(10, 16, 24))
    d.rectangle([px + 36, py + 48, px + 40, py + 58], fill=(10, 16, 24))
    # broken shackle: left half up, right half swung open
    d.arc([px + 12, py - 6, px + 64, py + 34], 180, 270,
          fill=(200, 170, 60), width=7)
    d.line([px + 64, py + 2, px + 84, py - 12], fill=(200, 170, 60), width=7)
    # red crack marks beside the broken shackle
    d.line([px + 88, py + 6, px + 98, py + 16], fill=(255, 80, 80), width=3)
    d.line([px + 92, py - 2, px + 104, py + 4], fill=(255, 80, 80), width=3)


def art_verdict(ax, ay, aw, ah):
    # courtroom blue, verdict board "10 OF 12", gavel
    d.rectangle([ax, ay, ax + aw, ay + ah], fill=(20, 32, 58))
    # verdict board
    d.rectangle([ax + 20, ay + 14, ax + 250, ay + ah - 14], fill=(240, 238, 228))
    vf = font(SANS_B, 34)
    d.text((ax + 44, ay + 22), "10 OF 12", font=vf, fill=RED)
    gf = font(SANS_B, 20)
    d.text((ax + 44, ay + 62), "GUILTY", font=gf, fill=(18, 18, 18))
    # gavel, right side, handle diagonal so it reads as a gavel
    gx, gy = ax + 300, ay + 26
    d.rectangle([gx, gy, gx + 96, gy + 24], fill=(150, 100, 50))
    d.rectangle([gx - 6, gy - 4, gx + 6, gy + 28], fill=(120, 80, 40))
    d.line([gx + 48, gy + 24, gx + 78, gy + 76], fill=(120, 80, 40), width=12)
    d.rectangle([gx + 40, gy + 76, gx + 116, gy + 86], fill=(100, 70, 40))
    # sound lines near the head's right end
    for i, sy in enumerate((gy - 6, gy + 6, gy + 18)):
        d.line([gx + 110, sy, gx + 126, sy], fill=(255, 220, 90), width=3)


mid_card(26, "CYBER  •  WASHINGTON",
         "CIA AND ODNI BREACHED",
         "Unclassified spy-intel system hit; no secrets lost.",
         art_breach)
mid_card(26 + MW + 14, "COURTS  •  NEW YORK",
         "HUAWEI GUILTY ON 10 OF 12 COUNTS",
         "Acquitted on racketeering.", art_verdict)

# ---- bottom row ---------------------------------------------------------
BY, BH = 720, 184
BW = (972 - 28) // 3


def small_card(x, kicker, headline, subline, draw_art):
    d.rectangle([x, BY, x + BW, BY + BH], fill=CARD, outline=BORDER, width=2)
    ax, ay, aw, ah = x + 2, BY + 2, BW - 4, 74
    draw_art(ax, ay, aw, ah)
    tx, tw = x + 14, BW - 28
    d.text((tx, BY + 86), kicker, font=font(SANS_B, 16), fill=RED)
    y = text_block(d, tx, BY + 106, headline, font(SERIF_B, 23), tw, INK, 1.08)
    text_block(d, tx, y + 3, subline, font(SANS, 17), tw, GRAY, 1.18)


def art_tower(ax, ay, aw, ah):
    # dusk sky, Riyadh's tallest tower with smoke at its crown
    d.rectangle([ax, ay, ax + aw, ay + ah], fill=(44, 30, 60))
    d.rectangle([ax, ay + 44, ax + aw, ay + ah], fill=(30, 22, 44))
    # setting sun
    d.ellipse([ax + 24, ay + 10, ax + 56, ay + 42], fill=(255, 170, 80))
    # skyline
    for bx, bh in ((8, 26), (44, 18), (240, 22), (272, 30)):
        d.rectangle([ax + bx, ay + ah - bh, ax + bx + 28, ay + ah],
                    fill=(20, 16, 32))
    # the tower: tapering, lit windows
    tx0 = ax + aw // 2
    d.polygon([(tx0 - 26, ay + ah), (tx0 - 16, ay + 6), (tx0 + 16, ay + 6),
               (tx0 + 26, ay + ah)], fill=(200, 190, 170))
    d.polygon([(tx0 - 16, ay + 6), (tx0 - 8, ay - 2), (tx0 + 8, ay - 2),
               (tx0 + 16, ay + 6)], fill=(160, 150, 130))
    for wy in range(ay + 16, ay + ah - 8, 12):
        d.rectangle([tx0 - 10, wy, tx0 + 10, wy + 4], fill=(255, 220, 120))
    # smoke + sparks at the crown
    d.ellipse([tx0 + 6, ay - 2, tx0 + 40, ay + 22], fill=(120, 116, 110))
    d.ellipse([tx0 + 22, ay - 12, tx0 + 50, ay + 8], fill=(150, 146, 140))
    star(d, tx0 + 2, ay + 10, 9, 4, 8, (255, 160, 40))
    # drone
    d.ellipse([ax + aw - 52, ay + 14, ax + aw - 36, ay + 24], fill=(20, 20, 20))
    d.line([ax + aw - 56, ay + 12, ax + aw - 32, ay + 12],
           fill=(200, 200, 200), width=2)


def art_refinery(ax, ay, aw, ah):
    # night refinery, flames, -45% output tag
    d.rectangle([ax, ay, ax + aw, ay + ah], fill=(16, 20, 28))
    # distillation towers
    for tx in (ax + 30, ax + 80, ax + 130):
        d.rectangle([tx, ay + 18, tx + 22, ay + ah - 10], fill=(90, 90, 100))
        d.ellipse([tx - 2, ay + 10, tx + 24, ay + 24], fill=(110, 110, 120))
        d.line([tx + 11, ay + 2, tx + 11, ay + 12], fill=(150, 150, 150), width=2)
    # ground line + pipes
    d.rectangle([ax, ay + ah - 10, ax + aw, ay + ah], fill=(8, 10, 14))
    d.line([ax + 52, ay + 40, ax + 80, ay + 40], fill=(150, 150, 150), width=3)
    d.line([ax + 102, ay + 52, ax + 130, ay + 52], fill=(150, 150, 150), width=3)
    # flames on two towers
    star(d, ax + 41, ay + 12, 10, 4, 8, (255, 160, 40))
    star(d, ax + 141, ay + 14, 8, 3, 8, (255, 120, 30))
    # -45% tag (subline below the card spells out "output")
    d.rectangle([ax + 178, ay + 16, ax + aw - 16, ay + 58], fill=RED)
    pf = font(SANS_B, 26)
    d.text((ax + 192, ay + 20), "-45%", font=pf, fill=(255, 255, 255))


def art_rescue(ax, ay, aw, ah):
    # teal field, white medical cross, tent, "3 DAYS" tag
    d.rectangle([ax, ay, ax + aw, ay + ah], fill=(14, 70, 66))
    # cross badge
    cx, cy = ax + 62, ay + 37
    d.ellipse([cx - 28, cy - 28, cx + 28, cy + 28], fill=(255, 255, 255))
    d.rectangle([cx - 6, cy - 18, cx + 6, cy + 18], fill=(178, 34, 34))
    d.rectangle([cx - 18, cy - 6, cx + 18, cy + 6], fill=(178, 34, 34))
    # tent
    tx = ax + 150
    d.polygon([(tx, ay + 62), (tx + 30, ay + 30), (tx + 60, ay + 62)],
              fill=(240, 240, 230))
    d.rectangle([tx + 28, ay + 26, tx + 32, ay + 34], fill=(178, 34, 34))
    d.rectangle([tx + 32, ay + 22, tx + 44, ay + 28], fill=(178, 34, 34))
    # ground
    d.rectangle([ax, ay + 62, ax + aw, ay + ah], fill=(10, 50, 48))
    # 3 DAYS tag, sized to fit the text inside the art area
    d.rectangle([ax + 212, ay + 14, ax + aw - 10, ay + 48], fill=(255, 255, 255))
    df3 = font(SANS_B, 18)
    d.text((ax + 220, ay + 18), "3 DAYS", font=df3, fill=(14, 70, 66))


small_card(26, "WAR  •  RIYADH", "HOUTHIS HIT RIYADH'S TALLEST TOWER",
           "11 wounded; 2nd hit in a week.", art_tower)
small_card(26 + BW + 14, "WAR  •  MOSCOW", "PUTIN VOWS RETALIATION",
           "Refinery output down 45% since late Oct.", art_refinery)
small_card(26 + 2 * (BW + 14), "HEALTH  •  ITURI",
           "EBOLA TEAM RESCUED AFTER 3 DAYS",
           "Freed from Akwe hospital siege.", art_rescue)

# ---- also-today ticker --------------------------------------------------
TY = 918
d.rectangle([26, TY, 998, TY + 66], fill=NAVY)
d.text((42, TY + 8), "ALSO TODAY", font=font(SANS_B, 19), fill=GOLD)
t1 = ("Sarkozy & Bruni face trial  •  Trump to unveil new tariffs  •  "
      "Giuliani gets Medal of Freedom")
t2 = ("NATO sends AWACS to Poland  •  Houthis 60 km from Aden  •  "
      "England thrash Australia by 8 wickets")
tf2 = font(SANS, 17)
assert d.textlength(t1, font=tf2) <= 940, d.textlength(t1, font=tf2)
assert d.textlength(t2, font=tf2) <= 940, d.textlength(t2, font=tf2)
d.text((42, TY + 30), t1, font=tf2, fill=(255, 255, 255))
d.text((42, TY + 50), t2, font=tf2, fill=(255, 255, 255))

# ---- footer -------------------------------------------------------------
ft = "Drawn from reporting of Wednesday 25 November 2026  •  make.fun news-image-20261125"
ff = font(SANS, 14)
d.text(((W - d.textlength(ft, font=ff)) / 2, 994), ft, font=ff, fill=GRAY)

img.save("entry.png", optimize=True)
print("saved entry.png")
