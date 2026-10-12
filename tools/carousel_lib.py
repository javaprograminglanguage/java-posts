"""Shared helpers for @javaprograminglanguage carousels (same approved style as make_carousel_template.py)."""
import os
from PIL import Image, ImageDraw, ImageFont

W, H, M = 1080, 1350, 90
BG = (11, 15, 20); CARD = (19, 26, 34); LINE = (40, 50, 62)
TEXT = (230, 237, 243); MUTED = (139, 152, 165)
ORANGE = (248, 152, 32); BLUE = (92, 159, 214); GREEN = (126, 231, 135); RED = (255, 123, 114)
INTER = "/usr/share/fonts/opentype/inter/"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
K, T, P, C = ORANGE, BLUE, TEXT, MUTED


def inter(size, weight="Bold"):
    return ImageFont.truetype(INTER + f"Inter-{weight}.otf", size)


def mono(size, bold=False):
    return ImageFont.truetype(MONO_B if bold else MONO, size)


class Deck:
    def __init__(self, out, total=7):
        self.out, self.total = out, total
        os.makedirs(out, exist_ok=True)

    def slide(self, n, label):
        img = Image.new("RGB", (W, H), BG)
        d = ImageDraw.Draw(img)
        f = inter(26, "SemiBold")
        tw = d.textlength(label, font=f)
        d.rounded_rectangle([M, M, M + tw + 76, M + 56], radius=28, fill=CARD, outline=LINE, width=2)
        d.ellipse([M + 20, M + 21, M + 34, M + 35], fill=ORANGE)
        d.text((M + 46, M + 12), label, font=f, fill=TEXT)
        d.text((M, H - M - 30), "@javaprograminglanguage", font=inter(26, "Medium"), fill=MUTED)
        num = f"{n:02d} / {self.total:02d}"
        f2 = inter(26, "Medium")
        d.text((W - M - d.textlength(num, font=f2), H - M - 30), num, font=f2, fill=MUTED)
        self.img, self.d, self.n = img, d, n
        return d

    def save(self):
        self.img.save(os.path.join(self.out, f"slide_{self.n:02d}.png"), "PNG")


def heading(d, l1, l2, y=230, size=64):
    d.text((M, y), l1, font=inter(size, "ExtraBold"), fill=TEXT)
    d.text((M, y + 85), l2, font=inter(size, "ExtraBold"), fill=ORANGE)


def code_block(d, y, lines, size=30, line_h=None, pad_bottom=110):
    line_h = line_h or int(size * 1.7)
    h = 110 + len(lines) * line_h + pad_bottom - 30
    d.rounded_rectangle([M, y, W - M, y + h], radius=28, fill=CARD, outline=LINE, width=2)
    for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        d.ellipse([M + 32 + i * 38, y + 30, M + 32 + i * 38 + 18, y + 48], fill=c)
    f = mono(size)
    for i, segs in enumerate(lines):
        cx = M + 44
        for text, color in segs:
            d.text((cx, y + 100 + i * line_h), text, font=f, fill=color)
            cx += d.textlength(text, font=f)
    return y + h


def cards(d, y, items, h=130, gap=28, title_size=42, sub_size=30, dot=None):
    for title, sub in items:
        d.rounded_rectangle([M, y, W - M, y + h], radius=24, fill=CARD, outline=LINE, width=2)
        d.text((M + 40, y + 20), title, font=inter(title_size, "Bold"), fill=TEXT)
        d.text((M + 40, y + 20 + title_size + 18), sub, font=inter(sub_size, "Medium"), fill=MUTED)
        y += h + gap
    return y


def muted(d, y, lines, size=42, gap=70):
    for i, t in enumerate(lines):
        d.text((M, y + i * gap), t, font=inter(size, "Medium"), fill=MUTED)


def hook(deck, label, l1, l2, l3, sub):
    d = deck.slide(1, label)
    d.text((M, 430), l1, font=inter(104, "ExtraBold"), fill=TEXT)
    d.text((M, 550), l2, font=inter(104, "ExtraBold"), fill=ORANGE)
    d.text((M, 670), l3, font=inter(104, "ExtraBold"), fill=TEXT)
    d.text((M, 840), sub, font=inter(44, "Medium"), fill=MUTED)
    d.line([M, 960, M + 120, 960], fill=ORANGE, width=6)
    d.text((M, 990), "Swipe  →", font=inter(34, "SemiBold"), fill=TEXT)
    deck.save()


def recap(deck, l1, l2, points):
    d = deck.slide(deck.total, "RECAP")
    d.text((M, 230), l1, font=inter(80, "ExtraBold"), fill=TEXT)
    d.text((M, 325), l2, font=inter(80, "ExtraBold"), fill=ORANGE)
    y = 520
    for p in points:
        d.ellipse([M, y + 12, M + 20, y + 32], fill=ORANGE)
        d.text((M + 50, y), p, font=inter(40, "SemiBold"), fill=TEXT)
        y += 78
    d.line([M, 900, M + 120, 900], fill=ORANGE, width=6)
    d.text((M, 940), "Follow for daily Java & tech tips", font=inter(40, "SemiBold"), fill=TEXT)
    d.text((M, 1010), "@javaprograminglanguage", font=inter(40, "SemiBold"), fill=BLUE)
    d.text((M, 1120), "Save it  •  Share with a Java dev", font=inter(34, "Medium"), fill=MUTED)
    deck.save()
