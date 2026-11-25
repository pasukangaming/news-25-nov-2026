#!/usr/bin/env python3
"""Draw a newspaper front page summing up Wednesday 25 November 2026.

Run:  python3 draw_image.py
Writes entry.png (1024x1024) next to this file.
Only Pillow and the standard library are used; fonts are DejaVu from the
system font directory. No network, no external images.
"""
import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1024, 1024

PAPER = (247, 243, 234)
INK = (18, 18, 18)
NAVY = (16, 38, 74)
NAVY_LIGHT = (31, 64, 110)
RED = (158, 24, 24)
GOLD = (201, 162, 39)
GREY = (90, 86, 78)
RULE = (120, 112, 96)
BOX_BG = (255, 255, 255)
CYAN = (86, 190, 214)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_MAST = font("DejaVuSerif-Bold.ttf", 76)
F_DATE = font("DejaVuSans.ttf", 21)
F_KICK = font("DejaVuSans-Bold.ttf", 20)
F_HEAD = font("DejaVuSerif-Bold.ttf", 58)
F_STAND = font("DejaVuSerif.ttf", 22)
F_BOX_KICK = font("DejaVuSans-Bold.ttf", 16)
F_BOX_HEAD = font("DejaVuSerif-Bold.ttf", 22)
F_BOX_BODY = font("DejaVuSans.ttf", 16)
F_FOOT = font("DejaVuSans.ttf", 16)


def wrap(draw, text, fnt, width):
    """Wrap text to pixel width, returning a list of lines."""
    lines = []
    for para in text.split("\n"):
        words = para.split()
        cur = ""
        for word in words:
            trial = (cur + " " + word).strip()
            if draw.textlength(trial, font=fnt) <= width:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = word
        if cur:
            lines.append(cur)
    return lines


def draw_centered(draw, y, text, fnt, fill, x0=0, x1=W):
    w = draw.textlength(text, font=fnt)
    draw.text(((x0 + x1 - w) / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size + 4


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    m = 36  # margin
    inner = W - 2 * m

    # ---- Masthead -------------------------------------------------------
    y = 30
    y = draw_centered(d, y, "THE WORLD TODAY", F_MAST, INK)
    d.line([(m, y + 2), (W - m, y + 2)], fill=INK, width=4)
    d.line([(m, y + 10), (W - m, y + 10)], fill=INK, width=1)
    y += 22
    y = draw_centered(
        d, y,
        "WEDNESDAY 25 NOVEMBER 2026  •  ONE DAY, ONE FRONT PAGE",
        F_DATE, RED)
    d.line([(m, y + 2), (W - m, y + 2)], fill=RULE, width=1)
    y += 18

    # ---- Lead story -----------------------------------------------------
    lead_h = 355
    lead_top = y
    # illustration panel on the right
    ill_x0 = m + 620
    ill_x1 = W - m
    d.rectangle([ill_x0, lead_top, ill_x1, lead_top + lead_h],
                fill=NAVY, outline=INK, width=2)
    # network motif: nodes and links
    import math
    cx, cy = (ill_x0 + ill_x1) // 2, lead_top + 150
    nodes = []
    for i in range(7):
        ang = 2 * math.pi * i / 7
        nx = cx + int(105 * math.cos(ang))
        ny = cy + int(95 * math.sin(ang))
        nodes.append((nx, ny))
        d.line([(cx, cy), (nx, ny)], fill=(70, 110, 160), width=2)
    for i in range(7):
        d.line([nodes[i], nodes[(i + 2) % 7]], fill=(52, 88, 138), width=1)
    for nx, ny in nodes:
        d.ellipse([nx - 9, ny - 9, nx + 9, ny + 9], fill=CYAN,
                  outline=(255, 255, 255), width=2)
    # shield with a keyhole in the centre
    d.polygon([(cx - 52, cy - 42), (cx + 52, cy - 42), (cx + 52, cy + 8),
               (cx, cy + 62), (cx - 52, cy + 8)], fill=GOLD,
              outline=(255, 255, 255), width=3)
    d.ellipse([cx - 11, cy - 22, cx + 11, cy + 0], fill=NAVY)
    d.polygon([(cx - 7, cy - 4), (cx + 7, cy - 4), (cx + 12, cy + 26),
               (cx - 12, cy + 26)], fill=NAVY)
    d.text((ill_x0 + 14, lead_top + lead_h - 52),
           "A system used to sift\nopen-source intelligence",
           font=F_BOX_BODY, fill=(220, 228, 240))

    # lead text on the left
    tx = m
    tw = 600
    d.text((tx, lead_top), "CYBERATTACK  •  WASHINGTON", font=F_KICK,
           fill=RED)
    hy = lead_top + 28
    head = "Spy agencies\nbreached in\ncyberattack"
    for line in head.split("\n"):
        d.text((tx, hy), line, font=F_HEAD, fill=INK)
        hy += 58
    sy = hy + 6
    stand = ("The CIA and the Director of National\n"
             "Intelligence were hit by a cyber-\n"
             "attack, officials say. Classified\n"
             "material may be involved — not\n"
             "linked to the FBI database breach.")
    for line in stand.split("\n"):
        d.text((tx, sy), line, font=F_STAND, fill=(40, 40, 40))
        sy += 27
    d.line([(m, lead_top + lead_h + 14), (W - m, lead_top + lead_h + 14)],
           fill=INK, width=3)

    # ---- Story grid -----------------------------------------------------
    stories = [
        ("HUAWEI", "Guilty on 10 of 12 counts",
         "Convicted in New York after a three-month trial: trade-secret "
         "theft and bank fraud. Huawei rejects it."),
        ("RIYADH", "Drone hits city's tallest tower",
         "A Houthi drone struck Riyadh's tallest tower; Saudi civil "
         "defence says 11 people were wounded."),
        ("UKRAINE", "Drone strike on Russian ship",
         "Zelenskiy confirms a Ukrainian drone hit a Russian cargo ship "
         "in the Gulf of Finland."),
        ("WASHINGTON", "Medal of Freedom for Giuliani",
         "President Trump awards Rudy Giuliani the Medal of Freedom, "
         "the top US civilian honour."),
        ("MARKETS", "Nvidia slides after the surge",
         "Nvidia shares fell about 7%, a day after jumping 31% on "
         "Jensen Huang's return as chief executive."),
        ("DR CONGO", "WHO flees Ebola hospital",
         "WHO evacuates staff from a hospital in Ituri as fighting "
         "rages at the Ebola centre: 5,775 dead of 11,762 cases."),
        ("NATO", "Early-warning jets for Poland",
         "NATO plans to deploy early-warning aircraft in Poland as "
         "it watches Russia's eastern flank."),
        ("MIDDLE EAST", "Tankers mined; Gaza fears grow",
         "Iran says three oil tankers were hit by naval mines in the "
         "Strait of Hormuz. The UN warns over Gaza."),
    ]

    grid_top = lead_top + lead_h + 30
    grid_bottom = H - 46
    rows, cols = 4, 2
    gap = 14
    cw = (inner - gap) // cols
    ch = (grid_bottom - grid_top - (rows - 1) * gap) // rows

    for i, (kick, head, body) in enumerate(stories):
        r, c = divmod(i, cols)
        x0 = m + c * (cw + gap)
        y0 = grid_top + r * (ch + gap)
        d.rectangle([x0, y0, x0 + cw, y0 + ch], fill=BOX_BG,
                    outline=RULE, width=1)
        d.rectangle([x0, y0, x0 + cw, y0 + 5], fill=NAVY)
        px = x0 + 12
        py = y0 + 8
        d.text((px, py), kick, font=F_BOX_KICK, fill=RED)
        py += 20
        for line in wrap(d, head, F_BOX_HEAD, cw - 24):
            d.text((px, py), line, font=F_BOX_HEAD, fill=INK)
            py += 24
        py += 2
        for line in wrap(d, body, F_BOX_BODY, cw - 24)[:2]:
            d.text((px, py), line, font=F_BOX_BODY, fill=(52, 52, 52))
            py += 19

    # ---- Footer ---------------------------------------------------------
    d.line([(m, H - 40), (W - m, H - 40)], fill=RULE, width=1)
    d.text((m, H - 32),
           "THE WORLD TODAY  •  Wednesday 25 November 2026  •  "
           "All stories first reported or unfolding on this day.",
           font=F_FOOT, fill=GREY)

    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, img.size, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
