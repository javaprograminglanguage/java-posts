"""Generates the three carousels for 2026-10-14. Usage: python3 gen_2026-10-14.py <repo_root>"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from carousel_lib import *
from PIL import ImageDraw

_orig = ImageDraw.ImageDraw.text
def _chk(self, xy, text, *a, **k):
    f = k.get("font")
    if f and text and xy[1] < H - M - 40:
        r = xy[0] + self.textlength(text, font=f)
        if r > W - M + 4:
            print("OVERFLOW", round(r), repr(text))
    return _orig(self, xy, text, *a, **k)
ImageDraw.ImageDraw.text = _chk

import carousel_lib
_cb = code_block
def code_block(d, y, lines, **k):
    k.setdefault('pad_bottom', 45)
    return _cb(d, y, lines, **k)

root = sys.argv[1] if len(sys.argv) > 1 else ".."

# ================= POST 1: static keyword =================
dk = Deck(os.path.join(root, "2026-10-14-java-static-keyword"))
hook(dk, "JAVA BASICS", "What does", "static", "really mean?", "It belongs to the class, not the object.")

d = dk.slide(2, "STATIC VARIABLE")
heading(d, "One copy,", "shared by all.")
e = code_block(d, 470, [
    [("class ", K), ("Counter ", T), ("{", P)],
    [("  static int ", K), ("count = 0;", P)],
    [("  Counter() { count++; }", P)],
    [("}", P)],
    [("", P)],
    [("new ", K), ("Counter();", P)],
    [("new ", K), ("Counter();", P)],
    [("// Counter.count is 2", C)],
], size=30, line_h=60)
muted(d, e + 40, ["Stored once per class."], size=38)
dk.save()

d = dk.slide(3, "STATIC METHOD")
heading(d, "Call it without", "an object.")
e = code_block(d, 470, [
    [("class ", K), ("MathUtil ", T), ("{", P)],
    [("  static int ", K), ("twice(", P), ("int ", T), ("n) {", P)],
    [("    return ", K), ("n * 2;", P)],
    [("  }", P)],
    [("}", P)],
    [("", P)],
    [("int ", T), ("r = MathUtil.twice(4);", P)],
    [("// r is 8", C)],
], size=30, line_h=60)
muted(d, e + 40, ["No new MathUtil() needed."], size=38)
dk.save()

d = dk.slide(4, "THE RULE")
heading(d, "Static can't see", "instance members.")
e = code_block(d, 470, [
    [("class ", K), ("User ", T), ("{", P)],
    [("  String ", T), ("name = ", P), ('"Ava"', GREEN), (";", P)],
    [("", P)],
    [("  static void ", K), ("hi() {", P)],
    [("    name.length();", P)],
    [("    // compile error", RED)],
    [("  }", P)],
    [("}", P)],
], size=30, line_h=60)
muted(d, e + 40, ["Static code has no 'this'."], size=38)
dk.save()

d = dk.slide(5, "WHERE YOU SEE IT")
heading(d, "You already", "use it daily.")
cards(d, 480, [
    ("public static void main", "The JVM calls it with no object"),
    ("Math.max(a, b)", "Utility methods on a class"),
    ("static final int MAX = 10", "Constants shared everywhere"),
], h=180, gap=40, title_size=40, sub_size=32)
dk.save()

d = dk.slide(6, "WATCH OUT")
heading(d, "Static has", "a cost.")
cards(d, 480, [
    ("Shared mutable state", "Every object and thread sees it"),
    ("Harder to test", "Global state leaks between tests"),
    ("Hidden, not overridden", "Static methods don't override"),
], h=180, gap=40, title_size=44, sub_size=32)
dk.save()

recap(dk, "One class.", "Shared by all.", ["Static belongs to the class", "No object needed to call it", "Can't touch instance fields"])

# ================= POST 2: generics wildcards =================
dk = Deck(os.path.join(root, "2026-10-14-java-generics-wildcards"))
hook(dk, "JAVA GENERICS", "Why isn't", "List<Integer>", "a List<Number>?", "Wildcards and PECS, explained.")

d = dk.slide(2, "THE PROBLEM")
heading(d, "Generics are", "invariant.")
e = code_block(d, 470, [
    [("List", T), ("<", P), ("Integer", T), ("> ints =", P)],
    [("    List.of(1, 2);", P)],
    [("", P)],
    [("List", T), ("<", P), ("Number", T), ("> nums = ints;", P)],
    [("// compile error", RED)],
], size=30, line_h=64)
muted(d, e + 40, ["Integer is a Number.", "But the two lists are unrelated."], size=38, gap=62)
dk.save()

d = dk.slide(3, "WHY")
heading(d, "Otherwise this", "would break.")
e = code_block(d, 470, [
    [("// if it were allowed:", C)],
    [("nums.add(", P), ("3.14", GREEN), (");", P)],
    [("", P)],
    [("Integer ", T), ("x = ints.get(0);", P)],
    [("// a Double in an Integer list", RED)],
], size=30, line_h=64)
muted(d, e + 40, ["The compiler stops it early."], size=38)
dk.save()

d = dk.slide(4, "? EXTENDS")
heading(d, "Reading? Use", "? extends.")
e = code_block(d, 470, [
    [("static double ", K), ("sum(", P)],
    [("    List", T), ("<? extends ", K), ("Number", T), ("> l) {", P)],
    [("  double ", T), ("s = 0;", P)],
    [("  for ", K), ("(", P), ("Number ", T), ("n : l)", P)],
    [("    s += n.doubleValue();", P)],
    [("  return ", K), ("s;", P)],
    [("}", P)],
], size=28, line_h=58)
muted(d, e + 40, ["Accepts List<Integer>, List<Double>...", "You can read, but not add."], size=34, gap=56)
dk.save()

d = dk.slide(5, "? SUPER")
heading(d, "Writing? Use", "? super.")
e = code_block(d, 470, [
    [("static void ", K), ("fill(", P)],
    [("    List", T), ("<? super ", K), ("Integer", T), ("> l) {", P)],
    [("  l.add(1);", P)],
    [("  l.add(2);", P)],
    [("}", P)],
    [("", P)],
    [("fill(", P), ("new ", K), ("ArrayList", T), ("<Number>());", P)],
], size=28, line_h=58)
muted(d, e + 40, ["Accepts List<Integer>, List<Number>,", "or List<Object>."], size=34, gap=56)
dk.save()

d = dk.slide(6, "PECS")
heading(d, "Remember", "PECS.")
cards(d, 480, [
    ("Producer Extends", "It gives you values: read it"),
    ("Consumer Super", "It takes your values: write to it"),
    ("Both read and write?", "Skip the wildcard, use T"),
], h=180, gap=40, title_size=46, sub_size=32)
dk.save()

recap(dk, "Read: extends.", "Write: super.", ["List<Integer> is not List<Number>", "? extends T: producer", "? super T: consumer"])

# ================= POST 3: JPA N+1 =================
dk = Deck(os.path.join(root, "2026-10-14-jpa-n-plus-one"))
hook(dk, "SPRING + JPA", "1 query", "became", "101.", "The JPA N+1 problem.")

d = dk.slide(2, "THE SETUP")
heading(d, "Authors have", "many books.")
e = code_block(d, 470, [
    [("@Entity", K)],
    [("class ", K), ("Author ", T), ("{", P)],
    [("  @Id ", K), ("Long ", T), ("id;", P)],
    [("  String ", T), ("name;", P)],
    [("  @OneToMany", K), ("(mappedBy = ", P), ('"author"', GREEN), (")", P)],
    [("  List", T), ("<Book> ", P), ("books;", P)],
    [("}", P)],
], size=28, line_h=58)
muted(d, e + 40, ["@OneToMany is lazy by default."], size=38)
dk.save()

d = dk.slide(3, "THE TRAP")
heading(d, "Innocent code,", "hidden queries.")
e = code_block(d, 470, [
    [("var ", K), ("authors = repo.findAll();", P)],
    [("", P)],
    [("for ", K), ("(", P), ("Author ", T), ("a : authors) {", P)],
    [("  int ", T), ("n = a.getBooks().size();", P)],
    [("}", P)],
], size=28, line_h=62)
muted(d, e + 40, ["Each getBooks() hits the database."], size=38)
dk.save()

d = dk.slide(4, "THE MATH")
heading(d, "100 authors.", "101 queries.")
cards(d, 480, [
    ("1 query", "Load all 100 authors"),
    ("+ 100 queries", "One per author's books"),
    ("= 101 queries", "Slow once real data arrives"),
], h=180, gap=40, title_size=46, sub_size=32)
dk.save()

d = dk.slide(5, "FIX 1")
heading(d, "Fetch it in", "one query.")
e = code_block(d, 470, [
    [('@Query', K), ('("""', GREEN)],
    [('  select distinct a', GREEN)],
    [('  from Author a', GREEN)],
    [('  join fetch a.books""")', GREEN)],
    [("List", T), ("<Author> findAllWithBooks();", P)],
], size=28, line_h=62)
muted(d, e + 40, ["One JOIN loads authors and books."], size=38)
dk.save()

d = dk.slide(6, "FIX 2")
heading(d, "Or use an", "entity graph.")
e = code_block(d, 470, [
    [("@EntityGraph", K), ("(", P)],
    [("    attributePaths = ", P), ('"books"', GREEN), (")", P)],
    [("List", T), ("<Author> findAll();", P)],
], size=28, line_h=64)
muted(d, e + 40, ["Same single query, no JPQL needed.", "Add it to the repository method."], size=36, gap=58)
dk.save()

recap(dk, "Count your", "queries.", ["Lazy loops cost N extra queries", "Fix: join fetch or EntityGraph", "Read the SQL log in dev"])
