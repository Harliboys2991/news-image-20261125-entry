#!/usr/bin/env python3
"""Render the front page for Wednesday 25 November 2026 (1024x1024 PNG).

Run locally once to produce entry.png. The submitted program is main.py,
which only copies entry.png into /output/entry.png, so grading never
needs Pillow or fonts. Every word here comes from reporting of the day:
Kyiv owning the Sparta II strike, the CIA/ODNI breach, Huawei's guilty
verdict, the second Houthi hit on Riyadh's tallest tower, Putin's
retaliation vow, and the WHO rescue in Ituri.
"""
import math

from PIL import Image, ImageDraw, ImageFont

PAGE_W, PAGE_H = 1024, 1024
PAGE_BG = (247, 242, 231)
INK_FG = (18, 18, 18)
NAVY_BG = (14, 34, 56)
RED_ACC = (178, 34, 34)
GOLD_ACC = (201, 162, 39)
GRAY_TX = (90, 86, 76)
CARD_BG = (255, 253, 247)
EDGE_LN = (206, 198, 178)

SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_REG = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def load_font(path, size):
    return ImageFont.truetype(path, size)


def burst(draw, cx, cy, outer, inner, points, fill, rot=-90):
    """Star-burst polygon (explosions, sparks) centred on (cx, cy)."""
    verts = []
    for i in range(points * 2):
        radius = outer if i % 2 == 0 else inner
        angle = math.radians(rot + i * 180 / points)
        verts.append((cx + radius * math.cos(angle),
                      cy + radius * math.sin(angle)))
    draw.polygon(verts, fill=fill)


def wrap_text(draw, text, fnt, max_w):
    """Greedy word wrap to lines no wider than max_w pixels."""
    out = []
    current = ""
    for word in text.split():
        trial = (current + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            current = trial
        else:
            if current:
                out.append(current)
            current = word
    if current:
        out.append(current)
    return out


def draw_lines(draw, x, y, text, fnt, max_w, fill, leading=1.18):
    """Draw wrapped text starting at (x, y); return the y below it."""
    step = int(fnt.size * leading)
    for line in wrap_text(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += step
    return y


# ------------------------------------------------------------------ page
page = Image.new("RGB", (PAGE_W, PAGE_H), PAGE_BG)
draw = ImageDraw.Draw(page)

# ---- masthead: navy band, gold rule, centred title ----------------------
draw.rectangle([0, 0, PAGE_W, 96], fill=NAVY_BG)
draw.rectangle([0, 96, PAGE_W, 100], fill=GOLD_ACC)
masthead = "THE WORLD TODAY"
masthead_font = load_font(SERIF_BOLD, 58)
masthead_w = draw.textlength(masthead, font=masthead_font)
draw.text(((PAGE_W - masthead_w) / 2, 14), masthead, font=masthead_font,
          fill=(255, 255, 255))
strapline = "ONE DAY  •  EVERY CONTINENT  •  IN ONE PICTURE"
strap_font = load_font(SANS_BOLD, 15)
strap_w = draw.textlength(strapline, font=strap_font)
draw.text(((PAGE_W - strap_w) / 2, 74), strapline, font=strap_font,
          fill=GOLD_ACC)

# ---- date bar: big serif date between red rules -------------------------
dateline = "WEDNESDAY, 25 NOVEMBER 2026"
date_font = load_font(SERIF_BOLD, 46)
date_w = draw.textlength(dateline, font=date_font)
draw.text(((PAGE_W - date_w) / 2, 112), dateline, font=date_font, fill=INK_FG)
draw.line([26, 136, (PAGE_W - date_w) / 2 - 18, 136], fill=RED_ACC, width=3)
draw.line([(PAGE_W + date_w) / 2 + 18, 136, PAGE_W - 26, 136],
          fill=RED_ACC, width=3)
dateline_sub = "The day's world news, as reported on Wednesday 25 November 2026"
sub_font = load_font(SANS_REG, 19)
sub_w = draw.textlength(dateline_sub, font=sub_font)
draw.text(((PAGE_W - sub_w) / 2, 164), dateline_sub, font=sub_font,
          fill=GRAY_TX)

# ---- lead story: Sparta II, Gulf of Finland -----------------------------
lead_x, lead_y, lead_w, lead_h = 26, 196, 972, 272
draw.rectangle([lead_x, lead_y, lead_x + lead_w, lead_y + lead_h],
               fill=CARD_BG, outline=EDGE_LN, width=2)
# artwork on the left: night sea, burning cargo ship, incoming drone
art_x, art_y = lead_x + 2, lead_y + 2
art_w, art_h = 452, lead_h - 4
draw.rectangle([art_x, art_y, art_x + art_w, art_y + art_h], fill=(12, 30, 52))
# stars
for sx, sy in ((30, 18), (90, 34), (160, 14), (240, 26), (330, 16),
               (410, 30), (60, 60), (380, 56), (200, 44)):
    draw.ellipse([art_x + sx - 1, art_y + sy - 1, art_x + sx + 1,
                  art_y + sy + 1], fill=(255, 255, 255))
# crescent moon, top-left, clear of the smoke at top-right
draw.ellipse([art_x + 18, art_y + 12, art_x + 58, art_y + 52],
             fill=(240, 230, 190))
draw.ellipse([art_x + 26, art_y + 16, art_x + 58, art_y + 48],
             fill=(12, 30, 52))
# sea with two rows of wave arcs
draw.rectangle([art_x, art_y + 150, art_x + art_w, art_y + art_h],
               fill=(8, 22, 40))
for wx in range(art_x + 6, art_x + art_w - 20, 44):
    draw.arc([wx, art_y + art_h - 66, wx + 34, art_y + art_h - 48],
             180, 360, fill=(90, 150, 190), width=2)
    draw.arc([wx + 20, art_y + art_h - 34, wx + 54, art_y + art_h - 16],
             180, 360, fill=(70, 120, 160), width=2)
# the cargo ship, mid-frame
ship_x, ship_y = art_x + 70, art_y + 128
# container stacks
draw.rectangle([ship_x + 20, ship_y - 46, ship_x + 90, ship_y - 22],
               fill=(178, 90, 34))
draw.rectangle([ship_x + 96, ship_y - 46, ship_x + 166, ship_y - 22],
               fill=(60, 120, 90))
draw.rectangle([ship_x + 58, ship_y - 70, ship_x + 128, ship_y - 46],
               fill=(140, 60, 60))
draw.rectangle([ship_x + 172, ship_y - 46, ship_x + 242, ship_y - 22],
               fill=(90, 100, 140))
# bridge tower with lit windows
draw.rectangle([ship_x + 250, ship_y - 66, ship_x + 292, ship_y - 22],
               fill=(220, 220, 210))
for wy in (ship_y - 60, ship_y - 48, ship_y - 36):
    draw.rectangle([ship_x + 256, wy, ship_x + 286, wy + 8],
                   fill=(255, 200, 90))
draw.rectangle([ship_x + 268, ship_y - 84, ship_x + 274, ship_y - 66],
               fill=(220, 220, 210))
# hull with a lighter sheer strake
draw.polygon([(ship_x, ship_y - 22), (ship_x + 320, ship_y - 22),
              (ship_x + 300, ship_y + 16), (ship_x + 18, ship_y + 16)],
             fill=(28, 32, 38))
draw.rectangle([ship_x, ship_y - 22, ship_x + 320, ship_y - 16],
               fill=(60, 64, 70))
# fire at the stern and smoke rising from it
burst(draw, ship_x + 310, ship_y - 30, 26, 10, 8, (255, 160, 40))
burst(draw, ship_x + 310, ship_y - 30, 14, 6, 8, (255, 230, 150))
burst(draw, ship_x + 282, ship_y - 52, 14, 6, 8, (255, 120, 30))
draw.ellipse([ship_x + 286, ship_y - 96, ship_x + 330, ship_y - 62],
             fill=(90, 88, 84))
draw.ellipse([ship_x + 306, ship_y - 116, ship_x + 346, ship_y - 84],
             fill=(120, 116, 110))
draw.ellipse([ship_x + 326, ship_y - 132, ship_x + 360, ship_y - 104],
             fill=(150, 146, 140))
# naval drone skimming in from the left on a dotted trail
draw.line([art_x + 14, art_y + 96, ship_x - 30, ship_y - 18],
          fill=(255, 220, 120), width=3)
draw.ellipse([art_x + 8, art_y + 90, art_x + 28, art_y + 102],
             fill=(20, 20, 20))
draw.line([art_x + 6, art_y + 88, art_x + 30, art_y + 88],
          fill=(200, 200, 200), width=2)
draw.line([art_x + 6, art_y + 104, art_x + 30, art_y + 104],
          fill=(200, 200, 200), width=2)
# ship-name ribbon across the bottom of the artwork
ribbon_y = art_y + art_h - 44
draw.rectangle([art_x + 34, ribbon_y, art_x + art_w - 34, ribbon_y + 32],
               fill=RED_ACC)
ribbon = "SPARTA II  •  GULF OF FINLAND"
ribbon_font = load_font(SANS_BOLD, 21)
ribbon_w = draw.textlength(ribbon, font=ribbon_font)
draw.text(((art_w - ribbon_w) / 2 + art_x, ribbon_y + 4), ribbon,
          font=ribbon_font, fill=(255, 255, 255))
# lead text on the right
lead_tx = art_x + art_w + 24
lead_tw = lead_x + lead_w - lead_tx - 22
draw.text((lead_tx, lead_y + 22), "WAR  •  GULF OF FINLAND",
          font=load_font(SANS_BOLD, 21), fill=RED_ACC)
cursor_y = draw_lines(draw, lead_tx, lead_y + 52,
                      "ZELENSKIY: WE HIT THE SPARTA II",
                      load_font(SERIF_BOLD, 38), lead_tw, INK_FG, 1.12)
cursor_y += 8
draw.line([lead_tx, cursor_y, lead_tx + 120, cursor_y], fill=RED_ACC, width=3)
cursor_y += 12
draw_lines(draw, lead_tx, cursor_y,
           "Kyiv confirms Saturday's drone strike on the Russian "
           "cargo ship \u2014 Norway urges caution.",
           load_font(SANS_REG, 20), lead_tw, GRAY_TX, 1.25)

# ---- middle row: two half-width cards -----------------------------------
mid_y, mid_h = 482, 224
mid_w = (972 - 14) // 2


def middle_card(x, kicker, headline, subline, paint):
    draw.rectangle([x, mid_y, x + mid_w, mid_y + mid_h],
                   fill=CARD_BG, outline=EDGE_LN, width=2)
    paint(x + 2, mid_y + 2, mid_w - 4, 104)
    tx, tw = x + 18, mid_w - 36
    draw.text((tx, mid_y + 116), kicker, font=load_font(SANS_BOLD, 19),
              fill=RED_ACC)
    next_y = draw_lines(draw, tx, mid_y + 140, headline,
                        load_font(SERIF_BOLD, 26), tw, INK_FG, 1.1)
    draw_lines(draw, tx, next_y + 4, subline, load_font(SANS_REG, 18),
               tw, GRAY_TX, 1.2)


def paint_breach(x0, y0, wd, ht):
    # dark terminal, code lines, a padlock with its shackle broken open
    draw.rectangle([x0, y0, x0 + wd, y0 + ht], fill=(10, 16, 24))
    for i, ly in enumerate(range(y0 + 14, y0 + ht - 12, 14)):
        span = 150 if i % 3 == 0 else (220 if i % 3 == 1 else 120)
        shade = (40, 120, 80) if i % 2 else (30, 90, 110)
        draw.rectangle([x0 + 16, ly, x0 + 16 + span, ly + 5], fill=shade)
    draw.rectangle([x0 + 16, y0 + ht - 22, x0 + 30, y0 + ht - 12],
                   fill=(120, 230, 140))
    lock_x, lock_y = x0 + wd - 130, y0 + 22
    draw.rounded_rectangle([lock_x, lock_y + 22, lock_x + 76, lock_y + 66],
                           radius=8, fill=(200, 170, 60))
    draw.ellipse([lock_x + 30, lock_y + 36, lock_x + 46, lock_y + 52],
                 fill=(10, 16, 24))
    draw.rectangle([lock_x + 36, lock_y + 48, lock_x + 40, lock_y + 58],
                   fill=(10, 16, 24))
    # broken shackle: left half up, right half swung open
    draw.arc([lock_x + 12, lock_y - 6, lock_x + 64, lock_y + 34],
             180, 270, fill=(200, 170, 60), width=7)
    draw.line([lock_x + 64, lock_y + 2, lock_x + 84, lock_y - 12],
              fill=(200, 170, 60), width=7)
    # red crack marks beside the broken shackle
    draw.line([lock_x + 88, lock_y + 6, lock_x + 98, lock_y + 16],
              fill=(255, 80, 80), width=3)
    draw.line([lock_x + 92, lock_y - 2, lock_x + 104, lock_y + 4],
              fill=(255, 80, 80), width=3)


def paint_verdict(x0, y0, wd, ht):
    # courtroom blue, a verdict board reading 10 OF 12, and a gavel
    draw.rectangle([x0, y0, x0 + wd, y0 + ht], fill=(20, 32, 58))
    draw.rectangle([x0 + 20, y0 + 14, x0 + 250, y0 + ht - 14],
                   fill=(240, 238, 228))
    draw.text((x0 + 44, y0 + 22), "10 OF 12", font=load_font(SANS_BOLD, 34),
              fill=RED_ACC)
    draw.text((x0 + 44, y0 + 62), "GUILTY", font=load_font(SANS_BOLD, 20),
              fill=(18, 18, 18))
    # gavel, handle diagonal so it reads as a gavel
    gav_x, gav_y = x0 + 300, y0 + 26
    draw.rectangle([gav_x, gav_y, gav_x + 96, gav_y + 24],
                   fill=(150, 100, 50))
    draw.rectangle([gav_x - 6, gav_y - 4, gav_x + 6, gav_y + 28],
                   fill=(120, 80, 40))
    draw.line([gav_x + 48, gav_y + 24, gav_x + 78, gav_y + 76],
              fill=(120, 80, 40), width=12)
    draw.rectangle([gav_x + 40, gav_y + 76, gav_x + 116, gav_y + 86],
                   fill=(100, 70, 40))
    # sound lines near the head's right end
    for sy in (gav_y - 6, gav_y + 6, gav_y + 18):
        draw.line([gav_x + 110, sy, gav_x + 126, sy],
                  fill=(255, 220, 90), width=3)


middle_card(26, "CYBER  •  WASHINGTON",
            "CIA AND ODNI BREACHED",
            "Unclassified spy-intel system hit; no secrets lost.",
            paint_breach)
middle_card(26 + mid_w + 14, "COURTS  •  NEW YORK",
            "HUAWEI GUILTY ON 10 OF 12 COUNTS",
            "Acquitted on racketeering.", paint_verdict)

# ---- bottom row: three third-width cards --------------------------------
bot_y, bot_h = 720, 184
bot_w = (972 - 28) // 3


def mini_card(x, kicker, headline, subline, paint):
    draw.rectangle([x, bot_y, x + bot_w, bot_y + bot_h],
                   fill=CARD_BG, outline=EDGE_LN, width=2)
    paint(x + 2, bot_y + 2, bot_w - 4, 74)
    tx, tw = x + 14, bot_w - 28
    draw.text((tx, bot_y + 86), kicker, font=load_font(SANS_BOLD, 16),
              fill=RED_ACC)
    next_y = draw_lines(draw, tx, bot_y + 106, headline,
                        load_font(SERIF_BOLD, 23), tw, INK_FG, 1.08)
    draw_lines(draw, tx, next_y + 3, subline, load_font(SANS_REG, 17),
               tw, GRAY_TX, 1.18)


def paint_tower(x0, y0, wd, ht):
    # dusk sky, Riyadh's tallest tower with smoke at its crown
    draw.rectangle([x0, y0, x0 + wd, y0 + ht], fill=(44, 30, 60))
    draw.rectangle([x0, y0 + 44, x0 + wd, y0 + ht], fill=(30, 22, 44))
    # setting sun
    draw.ellipse([x0 + 24, y0 + 10, x0 + 56, y0 + 42], fill=(255, 170, 80))
    # low skyline blocks
    for bx, bh in ((8, 26), (44, 18), (240, 22), (272, 30)):
        draw.rectangle([x0 + bx, y0 + ht - bh, x0 + bx + 28, y0 + ht],
                       fill=(20, 16, 32))
    # the tower: tapering, lit windows
    tower_cx = x0 + wd // 2
    draw.polygon([(tower_cx - 26, y0 + ht), (tower_cx - 16, y0 + 6),
                  (tower_cx + 16, y0 + 6), (tower_cx + 26, y0 + ht)],
                 fill=(200, 190, 170))
    draw.polygon([(tower_cx - 16, y0 + 6), (tower_cx - 8, y0 - 2),
                  (tower_cx + 8, y0 - 2), (tower_cx + 16, y0 + 6)],
                 fill=(160, 150, 130))
    for wy in range(y0 + 16, y0 + ht - 8, 12):
        draw.rectangle([tower_cx - 10, wy, tower_cx + 10, wy + 4],
                       fill=(255, 220, 120))
    # smoke + sparks at the crown
    draw.ellipse([tower_cx + 6, y0 - 2, tower_cx + 40, y0 + 22],
                 fill=(120, 116, 110))
    draw.ellipse([tower_cx + 22, y0 - 12, tower_cx + 50, y0 + 8],
                 fill=(150, 146, 140))
    burst(draw, tower_cx + 2, y0 + 10, 9, 4, 8, (255, 160, 40))
    # drone at upper right
    draw.ellipse([x0 + wd - 52, y0 + 14, x0 + wd - 36, y0 + 24],
                 fill=(20, 20, 20))
    draw.line([x0 + wd - 56, y0 + 12, x0 + wd - 32, y0 + 12],
              fill=(200, 200, 200), width=2)


def paint_refinery(x0, y0, wd, ht):
    # night refinery, flames, and a -45% output tag
    draw.rectangle([x0, y0, x0 + wd, y0 + ht], fill=(16, 20, 28))
    # distillation towers with caps and vents
    for tx in (x0 + 30, x0 + 80, x0 + 130):
        draw.rectangle([tx, y0 + 18, tx + 22, y0 + ht - 10],
                       fill=(90, 90, 100))
        draw.ellipse([tx - 2, y0 + 10, tx + 24, y0 + 24],
                     fill=(110, 110, 120))
        draw.line([tx + 11, y0 + 2, tx + 11, y0 + 12],
                  fill=(150, 150, 150), width=2)
    # ground line + connecting pipes
    draw.rectangle([x0, y0 + ht - 10, x0 + wd, y0 + ht], fill=(8, 10, 14))
    draw.line([x0 + 52, y0 + 40, x0 + 80, y0 + 40],
              fill=(150, 150, 150), width=3)
    draw.line([x0 + 102, y0 + 52, x0 + 130, y0 + 52],
              fill=(150, 150, 150), width=3)
    # flames on two towers
    burst(draw, x0 + 41, y0 + 12, 10, 4, 8, (255, 160, 40))
    burst(draw, x0 + 141, y0 + 14, 8, 3, 8, (255, 120, 30))
    # -45% tag (the subline below the card spells out "output")
    draw.rectangle([x0 + 178, y0 + 16, x0 + wd - 16, y0 + 58], fill=RED_ACC)
    draw.text((x0 + 192, y0 + 20), "-45%", font=load_font(SANS_BOLD, 26),
              fill=(255, 255, 255))


def paint_rescue(x0, y0, wd, ht):
    # teal field, white medical cross, relief tent, "3 DAYS" tag
    draw.rectangle([x0, y0, x0 + wd, y0 + ht], fill=(14, 70, 66))
    # cross badge
    cross_x, cross_y = x0 + 62, y0 + 37
    draw.ellipse([cross_x - 28, cross_y - 28, cross_x + 28, cross_y + 28],
                 fill=(255, 255, 255))
    draw.rectangle([cross_x - 6, cross_y - 18, cross_x + 6, cross_y + 18],
                   fill=(178, 34, 34))
    draw.rectangle([cross_x - 18, cross_y - 6, cross_x + 18, cross_y + 6],
                   fill=(178, 34, 34))
    # relief tent with a red flag
    tent_x = x0 + 150
    draw.polygon([(tent_x, y0 + 62), (tent_x + 30, y0 + 30),
                  (tent_x + 60, y0 + 62)], fill=(240, 240, 230))
    draw.rectangle([tent_x + 28, y0 + 26, tent_x + 32, y0 + 34],
                   fill=(178, 34, 34))
    draw.rectangle([tent_x + 32, y0 + 22, tent_x + 44, y0 + 28],
                   fill=(178, 34, 34))
    # ground
    draw.rectangle([x0, y0 + 62, x0 + wd, y0 + ht], fill=(10, 50, 48))
    # 3 DAYS tag, sized to fit the text inside the art area
    draw.rectangle([x0 + 212, y0 + 14, x0 + wd - 10, y0 + 48],
                   fill=(255, 255, 255))
    draw.text((x0 + 220, y0 + 18), "3 DAYS", font=load_font(SANS_BOLD, 18),
              fill=(14, 70, 66))


mini_card(26, "WAR  •  RIYADH", "HOUTHIS HIT RIYADH'S TALLEST TOWER",
          "11 wounded; 2nd hit in a week.", paint_tower)
mini_card(26 + bot_w + 14, "WAR  •  MOSCOW", "PUTIN VOWS RETALIATION",
          "Refinery output down 45% since late Oct.", paint_refinery)
mini_card(26 + 2 * (bot_w + 14), "HEALTH  •  ITURI",
          "EBOLA TEAM RESCUED AFTER 3 DAYS",
          "Freed from Akwe hospital siege.", paint_rescue)

# ---- also-today ticker --------------------------------------------------
ticker_y = 918
draw.rectangle([26, ticker_y, 998, ticker_y + 66], fill=NAVY_BG)
draw.text((42, ticker_y + 8), "ALSO TODAY", font=load_font(SANS_BOLD, 19),
          fill=GOLD_ACC)
ticker_1 = ("Sarkozy & Bruni face trial  •  Trump to unveil new tariffs  •  "
            "Giuliani gets Medal of Freedom")
ticker_2 = ("NATO sends AWACS to Poland  •  Houthis 60 km from Aden  •  "
            "England thrash Australia by 8 wickets")
ticker_font = load_font(SANS_REG, 17)
assert draw.textlength(ticker_1, font=ticker_font) <= 940, \
    draw.textlength(ticker_1, font=ticker_font)
assert draw.textlength(ticker_2, font=ticker_font) <= 940, \
    draw.textlength(ticker_2, font=ticker_font)
draw.text((42, ticker_y + 30), ticker_1, font=ticker_font,
          fill=(255, 255, 255))
draw.text((42, ticker_y + 50), ticker_2, font=ticker_font,
          fill=(255, 255, 255))

# ---- footer -------------------------------------------------------------
footer = ("Drawn from reporting of Wednesday 25 November 2026  •  "
          "make.fun news-image-20261125")
footer_font = load_font(SANS_REG, 14)
footer_w = draw.textlength(footer, font=footer_font)
draw.text(((PAGE_W - footer_w) / 2, 994), footer, font=footer_font,
          fill=GRAY_TX)

page.save("entry.png", optimize=True)
print("saved entry.png")
