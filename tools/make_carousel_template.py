"""Style template for @javaprograminglanguage carousels (Java Records example, 7 slides, 1080x1350).
Copy this file, keep the helpers/colors/layout, and replace the slide content for a new topic.
Usage: python3 make_carousel_template.py <output_dir>
"""
import os
from PIL import Image, ImageDraw, ImageFont

import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "out"  # output folder for slide PNGs
os.makedirs(OUT, exist_ok=True)

W, H = 1080, 1350
M = 90
TOTAL = 7

BG = (11, 15, 20)
CARD = (19, 26, 34)
TEXT = (230, 237, 243)
MUTED = (139, 152, 165)
ORANGE = (248, 152, 32)
BLUE = (92, 159, 214)
GREEN = (126, 231, 135)

INTER = "/usr/share/fonts/opentype/inter/"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"


def inter(size, weight="Bold"):
    return ImageFont.truetype(INTER + f"Inter-{weight}.otf", size)


def mono(size, bold=False):
    return ImageFont.truetype(MONO_B if bold else MONO, size)


def new_slide(n, label):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # top label pill
    f = inter(26, "SemiBold")
    tw = d.textlength(label, font=f)
    d.rounded_rectangle([M, M, M + tw + 76, M + 56], radius=28, fill=CARD, outline=(40, 50, 62), width=2)
    d.ellipse([M + 20, M + 21, M + 34, M + 35], fill=ORANGE)
    d.text((M + 46, M + 12), label, font=f, fill=TEXT)
    # footer
    d.text((M, H - M - 30), "@javaprograminglanguage", font=inter(26, "Medium"), fill=MUTED)
    num = f"{n:02d} / {TOTAL:02d}"
    f2 = inter(26, "Medium")
    d.text((W - M - d.textlength(num, font=f2), H - M - 30), num, font=f2, fill=MUTED)
    return img, d


def code_card(d, x, y, w, h):
    d.rounded_rectangle([x, y, x + w, y + h], radius=28, fill=CARD, outline=(40, 50, 62), width=2)
    for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        d.ellipse([x + 32 + i * 38, y + 30, x + 32 + i * 38 + 18, y + 48], fill=c)


def draw_code(d, x, y, lines, size, line_h):
    f = mono(size)
    fb = mono(size, True)
    for i, segs in enumerate(lines):
        cx = x
        for text, color in segs:
            d.text((cx, y + i * line_h), text, font=f, fill=color)
            cx += d.textlength(text, font=f)


def save(img, n):
    img.save(os.path.join(OUT, f"slide_{n:02d}.png"), "PNG")


# ---------- Slide 1: hook ----------
img, d = new_slide(1, "JAVA TIP")
d.text((M, 430), "Stop writing", font=inter(104, "ExtraBold"), fill=TEXT)
d.text((M, 550), "boilerplate", font=inter(104, "ExtraBold"), fill=ORANGE)
d.text((M, 670), "in Java.", font=inter(104, "ExtraBold"), fill=TEXT)
d.text((M, 840), "Meet Java Records.", font=inter(44, "Medium"), fill=MUTED)
d.line([M, 960, M + 120, 960], fill=ORANGE, width=6)
d.text((M, 990), "Swipe  →", font=inter(34, "SemiBold"), fill=TEXT)
save(img, 1)

# ---------- Slide 2: old way ----------
img, d = new_slide(2, "THE OLD WAY")
d.text((M, 230), "A simple data class", font=inter(64, "ExtraBold"), fill=TEXT)
d.text((M, 315), "took 30+ lines.", font=inter(64, "ExtraBold"), fill=ORANGE)
code_card(d, M, 470, W - 2 * M, 640)
K, T, P, C = ORANGE, BLUE, TEXT, MUTED
lines = [
    [("public class ", K), ("User ", T), ("{", P)],
    [("  private final ", K), ("String ", T), ("name;", P)],
    [("  private final ", K), ("int ", T), ("age;", P)],
    [("", P)],
    [("  // constructor", C)],
    [("  // getName(), getAge()", C)],
    [("  // equals()", C)],
    [("  // hashCode()", C)],
    [("  // toString()", C)],
    [("}", P)],
]
draw_code(d, M + 40, 540, lines, 36, 56)
save(img, 2)

# ---------- Slide 3: new way ----------
img, d = new_slide(3, "THE NEW WAY")
d.text((M, 230), "Now it's", font=inter(64, "ExtraBold"), fill=TEXT)
d.text((M, 315), "one line.", font=inter(64, "ExtraBold"), fill=ORANGE)
code_card(d, M, 520, W - 2 * M, 230)
lines = [
    [("public record ", K), ("User", T), ("(", P), ("String ", T), ("name, ", P), ("int ", T), ("age", P), (") {}", P)],
]
# one-line record at a size that fits the card width
draw_code(d, M + 36, 625, lines, 30, 44)
d.text((M, 840), "Same job. Zero boilerplate.", font=inter(40, "Medium"), fill=MUTED)
d.text((M, 905), "Available since Java 16.", font=inter(40, "Medium"), fill=MUTED)
save(img, 3)

# ---------- Slide 4: free stuff ----------
img, d = new_slide(4, "WHAT YOU GET")
d.text((M, 230), "Java writes the", font=inter(64, "ExtraBold"), fill=TEXT)
d.text((M, 315), "rest for you.", font=inter(64, "ExtraBold"), fill=ORANGE)
items = [
    ("Constructor", "new User(\"Ava\", 25)"),
    ("Accessors", "user.name()  user.age()"),
    ("equals()", "compares by values"),
    ("hashCode()", "consistent with equals"),
    ("toString()", "User[name=Ava, age=25]"),
]
y = 500
for title, sub in items:
    d.ellipse([M, y + 14, M + 22, y + 36], fill=ORANGE)
    d.text((M + 54, y), title, font=inter(44, "Bold"), fill=TEXT)
    d.text((M + 54, y + 58), sub, font=mono(28), fill=MUTED)
    y += 135
save(img, 4)

# ---------- Slide 5: compact constructor ----------
img, d = new_slide(5, "VALIDATION")
d.text((M, 230), "Need checks?", font=inter(64, "ExtraBold"), fill=TEXT)
d.text((M, 315), "Compact constructor.", font=inter(64, "ExtraBold"), fill=ORANGE)
code_card(d, M, 470, W - 2 * M, 470)
lines = [
    [("record ", K), ("User", T), ("(", P), ("String ", T), ("name, ", P), ("int ", T), ("age", P), (") {", P)],
    [("  User {", P)],
    [("    if ", K), ("(age < 0)", P)],
    [("      throw new ", K), ("IllegalArgumentException", T), ("();", P)],
    [("  }", P)],
    [("}", P)],
]
draw_code(d, M + 40, 560, lines, 28, 60)
d.text((M, 1000), "No parameter list. Runs on every creation.", font=inter(32, "Medium"), fill=MUTED)
save(img, 5)

# ---------- Slide 6: rules ----------
img, d = new_slide(6, "GOOD TO KNOW")
d.text((M, 230), "Records have", font=inter(64, "ExtraBold"), fill=TEXT)
d.text((M, 315), "a few rules.", font=inter(64, "ExtraBold"), fill=ORANGE)
rules = [
    ("Immutable", "Fields are final"),
    ("No inheritance", "Can't extend a class"),
    ("Interfaces OK", "Can implement them"),
    ("Methods OK", "Add your own"),
]
y = 480
for title, sub in rules:
    d.rounded_rectangle([M, y, W - M, y + 130], radius=24, fill=CARD, outline=(40, 50, 62), width=2)
    d.text((M + 40, y + 20), title, font=inter(42, "Bold"), fill=TEXT)
    d.text((M + 40, y + 78), sub, font=inter(30, "Medium"), fill=MUTED)
    y += 158
save(img, 6)

# ---------- Slide 7: CTA ----------
img, d = new_slide(7, "RECAP")
d.text((M, 400), "Less boilerplate.", font=inter(88, "ExtraBold"), fill=TEXT)
d.text((M, 510), "More clarity.", font=inter(88, "ExtraBold"), fill=ORANGE)
d.line([M, 690, M + 120, 690], fill=ORANGE, width=6)
d.text((M, 730), "Follow for daily Java & tech tips", font=inter(40, "SemiBold"), fill=TEXT)
d.text((M, 800), "@javaprograminglanguage", font=inter(40, "SemiBold"), fill=BLUE)
d.text((M, 920), "Save it  •  Share with a Java dev", font=inter(34, "Medium"), fill=MUTED)
save(img, 7)

print("done", sorted(os.listdir(OUT)))
