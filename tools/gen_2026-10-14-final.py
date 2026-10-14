import sys
sys.path.insert(0, "/home/claude/java-posts/tools")
from carousel_lib import *

OUT = sys.argv[1]
YELLOW = (255, 214, 10)
D = Deck(OUT)

def fit(d, text, maxw, size, weight="ExtraBold"):
    while d.textlength(text, font=inter(size, weight)) > maxw:
        size -= 2
    return size

# 1 bold cover
d = D.slide(1, "INTERVIEW QUESTION")
words = [("final", YELLOW), ("finally", GREEN), ("finalize()", BLUE)]
size = min(fit(d, w, W - 2 * M, 190) for w, _ in words)
y = 330
for w, c in words:
    d.text((M, y), w, font=inter(size, "ExtraBold"), fill=c)
    y += int(size * 1.12)
d.text((M, y + 40), "Sound the same. Aren't.", font=inter(52, "SemiBold"), fill=TEXT)
d.line([M, y + 150, M + 120, y + 150], fill=ORANGE, width=6)
d.text((M, y + 180), "Swipe  →", font=inter(34, "SemiBold"), fill=TEXT)
D.save()

# 2 final = stops change
d = D.slide(2, "FINAL")
heading(d, "final means", "no changes.")
code_block(d, 470, [
    [("final int ", K), ("MAX = 10;", P)],
    [("MAX = 20;", P)],
    [("// compile error", C)],
], size=38, pad_bottom=60)
muted(d, 930, ["Set once. Never reassigned."], size=40)
D.save()

# 3 final in 3 places
d = D.slide(3, "FINAL")
heading(d, "Three places", "you use it.")
cards(d, 480, [
    ("Variable", "Can't be reassigned"),
    ("Method", "Can't be overridden"),
    ("Class", "Can't be extended"),
], h=170, gap=34, title_size=48, sub_size=34)
D.save()

# 4 finally
d = D.slide(4, "FINALLY")
heading(d, "finally always", "runs.")
code_block(d, 470, [
    [("try ", K), ("{", P)],
    [("  riskyWork();", P)],
    [("} ", P), ("catch ", K), ("(Exception e) {", P)],
    [("  handle(e);", P)],
    [("} ", P), ("finally ", K), ("{", P)],
    [("  closeResource();", GREEN)],
    [("}", P)],
], size=32, line_h=54, pad_bottom=70)
muted(d, 1070, ["Exception or not, cleanup happens."], size=36)
D.save()

# 5 finally after return
d = D.slide(5, "FINALLY")
heading(d, "Even after", "return.")
code_block(d, 470, [
    [("try ", K), ("{", P)],
    [("  return ", K), ("\"try\"", ORANGE), (";", P)],
    [("} ", P), ("finally ", K), ("{", P)],
    [("  System.out.println(", P), ("\"cleanup\"", ORANGE), (");", P)],
    [("}", P)],
], size=30, line_h=54, pad_bottom=70)
muted(d, 960, ["Prints cleanup first,", "then returns \"try\"."], size=40)
D.save()

# 6 finalize
d = D.slide(6, "FINALIZE")
heading(d, "finalize()?", "Skip it.")
cards(d, 480, [
    ("Old GC hook", "Runs before an object is removed"),
    ("Deprecated", "Unreliable. Marked for removal"),
    ("Use instead", "try-with-resources"),
], h=170, gap=34, title_size=46, sub_size=32)
D.save()

# 7 recap
d = D.slide(7, "RECAP")
rows = [("final", YELLOW, "= constant"), ("finally", GREEN, "= cleanup"), ("finalize()", BLUE, "= avoid")]
y = 300
for w, c, s in rows:
    d.text((M, y), w, font=inter(84, "ExtraBold"), fill=c)
    d.text((M, y + 100), s, font=inter(44, "Medium"), fill=MUTED)
    y += 215
d.line([M, 980, M + 120, 980], fill=ORANGE, width=6)
d.text((M, 1010), "Follow for daily Java & tech tips", font=inter(40, "SemiBold"), fill=TEXT)
d.text((M, 1075), "@javaprograminglanguage", font=inter(40, "SemiBold"), fill=BLUE)
d.text((M, 1160), "Save it  •  Send to a friend learning Java", font=inter(32, "Medium"), fill=MUTED)
D.save()
print("ok")
