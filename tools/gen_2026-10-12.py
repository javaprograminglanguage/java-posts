"""Generates the three carousels for 2026-10-12. Usage: python3 gen_2026-10-12.py <repo_root>"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from carousel_lib import *

root = sys.argv[1] if len(sys.argv) > 1 else ".."

# ======================= POST 1: var =======================
dk = Deck(os.path.join(root, "2026-10-12-java-var-keyword"))
hook(dk, "JAVA TIP", "Stop typing", "the type", "twice.", "Meet var (Java 10+).")

d = dk.slide(2, "THE OLD WAY")
heading(d, "The same type,", "written twice.")
e = code_block(d, 470, [
    [("Map", T), ("<String, List<Integer>> scores =", P)],
    [("    new ", K), ("HashMap", T), ("<String, List<Integer>>();", P)],
], size=26, line_h=72)
muted(d, e + 60, ["Long. Noisy. Easy to skim past."])
dk.save()

d = dk.slide(3, "THE NEW WAY")
heading(d, "Let the compiler", "infer it.")
e = code_block(d, 470, [
    [("var ", K), ("scores =", P)],
    [("    new ", K), ("HashMap", T), ("<String, List<Integer>>();", P)],
], size=26, line_h=72)
muted(d, e + 60, ["Same type. Less noise.", "Available since Java 10."])
dk.save()

d = dk.slide(4, "STILL TYPED")
heading(d, "var is not", "dynamic typing.")
e = code_block(d, 470, [
    [("var ", K), ("n = 10;", P), ("   // int", C)],
    [("n = ", P), ('"hi"', GREEN), (";", P), ("   // error", RED)],
], size=30, line_h=76)
muted(d, e + 60, ["The type is fixed at compile time.", "It is just not written by you."])
dk.save()

d = dk.slide(5, "WHERE IT WORKS")
heading(d, "Local variables", "only.")
y = cards(d, 480, [
    ("Allowed", "Local variables, for loops, try-with-resources"),
    ("Not allowed", "Fields, parameters, return types"),
], h=160, gap=30, title_size=44, sub_size=30)
code_block(d, y + 30, [
    [("for ", K), ("(", P), ("var ", K), ("e : map.entrySet()) {", P)],
    [("  ...", C)],
    [("}", P)],
], size=28, line_h=56, pad_bottom=40)
dk.save()

d = dk.slide(6, "GOOD TO KNOW")
heading(d, "A few", "ground rules.")
cards(d, 480, [
    ("Needs a value", "var x;  will not compile"),
    ("No null", "var y = null;  will not compile"),
    ("Keep names clear", "var data = load();  say what it is"),
], h=180, gap=40, title_size=46, sub_size=32)
dk.save()

recap(dk, "Less noise.", "Same safety.", ["var infers the type", "Local variables only", "Still static typing"])

# ======================= POST 2: checked vs unchecked =======================
dk = Deck(os.path.join(root, "2026-10-12-checked-vs-unchecked-exceptions"))
hook(dk, "INTERVIEW QUESTION", "Checked or", "unchecked?", "Know why.", "Most Java interviews ask this.")

d = dk.slide(2, "THE FAMILY")
heading(d, "Every exception", "starts here.")
y = 480
rows = [("Throwable", "The root of all of them", 0, TEXT),
        ("Error", "JVM problems. Don't catch.", 1, MUTED),
        ("Exception", "Checked: must be handled", 1, ORANGE),
        ("RuntimeException", "Unchecked: your bugs", 2, BLUE)]
for t, s, lvl, col in rows:
    x = M + lvl * 70
    d.rounded_rectangle([x, y, W - M, y + 130], radius=24, fill=CARD, outline=LINE, width=2)
    d.text((x + 36, y + 18), t, font=inter(40, "Bold"), fill=col)
    d.text((x + 36, y + 78), s, font=inter(30, "Medium"), fill=MUTED)
    y += 176
dk.save()

d = dk.slide(3, "CHECKED")
heading(d, "The compiler", "makes you deal with it.")
e = code_block(d, 470, [
    [("void ", K), ("load", P), ("(", P), ("Path ", T), ("p)", P)],
    [("    throws ", K), ("IOException", T), (" {", P)],
    [("  Files", T), (".readString(p);", P)],
    [("}", P)],
], size=30, line_h=72)
muted(d, e + 60, ["Handle it, or declare it.", "Examples: IOException, SQLException"], size=38)
dk.save()

d = dk.slide(4, "UNCHECKED")
heading(d, "The compiler", "lets it slide.")
e = code_block(d, 470, [
    [("String ", T), ("s = ", P), ("null", K), (";", P)],
    [("s.length();", P)],
    [("// NullPointerException", C)],
], size=30, line_h=72)
muted(d, e + 60, ["Compiles fine. Fails at runtime.", "Examples: NPE, IllegalArgumentException"], size=38)
dk.save()

d = dk.slide(5, "RULE OF THUMB")
heading(d, "Which one", "should you use?")
cards(d, 480, [
    ("Checked", "The caller can recover. File missing? Retry."),
    ("Unchecked", "A programming bug. Fix the code."),
], h=250, gap=44, title_size=54, sub_size=34)
dk.save()

d = dk.slide(6, "YOUR OWN")
heading(d, "Your custom", "exceptions too.")
e = code_block(d, 470, [
    [("class ", K), ("AppEx ", T), ("extends ", K), ("Exception", T)],
    [("  // checked", C)],
    [("", P)],
    [("class ", K), ("BadInput ", T), ("extends ", K), ("RuntimeException", T)],
    [("  // unchecked", C)],
], size=26, line_h=66)
muted(d, e + 60, ["Your parent class decides the type."], size=36)
dk.save()

recap(dk, "Checked: handle it.", "Unchecked: fix it.", ["Checked = compiler enforces", "Unchecked = RuntimeException", "Error = leave it alone"])

# ======================= POST 3: virtual threads =======================
dk = Deck(os.path.join(root, "2026-10-12-java-virtual-threads"))
hook(dk, "JAVA 21", "10,000", "threads?", "Easy.", "Meet virtual threads.")

d = dk.slide(2, "THE PROBLEM")
heading(d, "Normal threads", "are expensive.")
cards(d, 480, [
    ("Platform thread", "Maps to one OS thread"),
    ("Heavy", "Costly in memory, so you pool them"),
    ("Blocked = wasted", "Waiting on I/O holds the OS thread"),
], h=180, gap=40, title_size=46, sub_size=32)
dk.save()

d = dk.slide(3, "THE FIX")
heading(d, "Cheap threads,", "managed by the JVM.")
e = code_block(d, 470, [
    [("Thread", T), (".ofVirtual().start(() -> {", P)],
    [("  System", T), (".out.println(", P), ('"hi"', GREEN), (");", P)],
    [("});", P)],
], size=28, line_h=72)
muted(d, e + 60, ["Final in Java 21.", "Same Thread API you know."], size=38)
dk.save()

d = dk.slide(4, "IN PRACTICE")
heading(d, "One thread", "per task.")
e = code_block(d, 470, [
    [("try ", K), ("(", P), ("var ", K), ("ex = ", P), ("Executors", T)],
    [("    .newVirtualThreadPerTaskExecutor()) {", P)],
    [("  ex.submit(() -> fetch());", P)],
    [("}", P)],
], size=26, line_h=72)
muted(d, e + 60, ["Closing it waits for all tasks."], size=38)
dk.save()

d = dk.slide(5, "BEST FOR")
heading(d, "Great at", "waiting.")
cards(d, 480, [
    ("Blocking I/O", "HTTP calls, database queries"),
    ("Many requests", "Thousands of tasks at once"),
    ("Not CPU-bound", "Heavy math gets no speed-up"),
], h=180, gap=40, title_size=46, sub_size=32)
dk.save()

d = dk.slide(6, "DON'T DO THIS")
heading(d, "Don't pool", "virtual threads.")
cards(d, 480, [
    ("Create one per task", "They are cheap. Let them go."),
    ("Need a limit?", "Use a Semaphore instead of a pool."),
    ("More scale, not speed", "Throughput up. Code is not faster."),
], h=180, gap=40, title_size=46, sub_size=32)
dk.save()

recap(dk, "Write simple", "blocking code.", ["Virtual threads: Java 21", "One per task, no pools", "Best for I/O-heavy apps"])
print("done")
