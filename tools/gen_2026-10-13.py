"""Generates the three carousels for 2026-10-13. Usage: python3 gen_2026-10-13.py <repo_root>"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from carousel_lib import *

root = sys.argv[1] if len(sys.argv) > 1 else ".."

# ======================= POST 1: pass by value =======================
dk = Deck(os.path.join(root, "2026-10-13-java-pass-by-value"))
hook(dk, "JAVA BASICS", "Java is always", "pass by", "value.", "Even for objects. Here's why.")

d = dk.slide(2, "PRIMITIVES")
heading(d, "The method gets", "a copy.")
e = code_block(d, 470, [
    [("void ", K), ("inc(", P), ("int ", T), ("x) {", P)],
    [("  x = x + 1;", P)],
    [("}", P)],
    [("", P)],
    [("int ", T), ("a = 5;", P)],
    [("inc(a);", P), ("  // a is still 5", C)],
], size=30, line_h=64)
muted(d, e + 50, ["Changing x never touches a."], size=38)
dk.save()

d = dk.slide(3, "OBJECTS")
heading(d, "Objects pass", "a copy of the reference.")
cards(d, 480, [
    ("Your variable", "Holds a reference to the object"),
    ("The method gets", "A copy of that reference"),
    ("Both point to", "The same object on the heap"),
], h=180, gap=40, title_size=46, sub_size=32)
dk.save()

d = dk.slide(4, "MUTATE")
heading(d, "Change the object,", "the caller sees it.")
e = code_block(d, 470, [
    [("void ", K), ("rename(", P), ("User ", T), ("u) {", P)],
    [("  u.name = ", P), ('"Bob"', GREEN), (";", P)],
    [("}", P)],
    [("", P)],
    [("rename(user);", P)],
    [("// user.name is now Bob", C)],
], size=30, line_h=64)
muted(d, e + 50, ["Same object, so the change shows."], size=38)
dk.save()

d = dk.slide(5, "REASSIGN")
heading(d, "Reassign the copy,", "the caller won't.")
e = code_block(d, 470, [
    [("void ", K), ("reset(", P), ("User ", T), ("u) {", P)],
    [("  u = ", P), ("new ", K), ("User", T), ("(", P), ('"Zed"', GREEN), (");", P)],
    [("}", P)],
    [("", P)],
    [("reset(user);", P)],
    [("// user is unchanged", C)],
], size=30, line_h=64)
muted(d, e + 50, ["Only the local copy was re-pointed."], size=38)
dk.save()

d = dk.slide(6, "INTERVIEW ANSWER")
heading(d, "Say it", "like this.")
cards(d, 480, [
    ("Always pass by value", "Primitives copy the value"),
    ("References too", "They copy the reference"),
    ("Never by reference", "A method can't re-point your variable"),
], h=180, gap=40, title_size=46, sub_size=32)
dk.save()

recap(dk, "Copies, always.", "Even references.", ["Primitives: value copied", "Objects: reference copied", "Mutate: visible. Reassign: not"])

# ======================= POST 2: stack vs heap =======================
dk = Deck(os.path.join(root, "2026-10-13-jvm-stack-vs-heap"))
hook(dk, "JVM MEMORY", "Where does", "your data", "live?", "Stack vs Heap, in 60 seconds.")

d = dk.slide(2, "THE STACK")
heading(d, "Stack: one per", "thread.")
cards(d, 480, [
    ("Method calls", "Each call gets its own frame"),
    ("Local variables", "Primitives and references live here"),
    ("Fast and automatic", "Frame is freed when the method ends"),
], h=180, gap=40, title_size=46, sub_size=32)
dk.save()

d = dk.slide(3, "THE HEAP")
heading(d, "Heap: shared by", "all threads.")
cards(d, 480, [
    ("All objects", "Created with new"),
    ("Shared", "Every thread can reach them"),
    ("Garbage collected", "Freed when nothing refers to them"),
], h=180, gap=40, title_size=46, sub_size=32)
dk.save()

d = dk.slide(4, "IN CODE")
heading(d, "Who lives", "where?")
e = code_block(d, 470, [
    [("int ", T), ("n = 5;", P)],
    [("// n: on the stack", C)],
    [("User ", T), ("u = ", P), ("new ", K), ("User", T), ("();", P)],
    [("// u: reference, on the stack", C)],
    [("// User object: on the heap", C)],
], size=26, line_h=60, pad_bottom=70)
muted(d, e + 50, ["Stack holds the reference.", "Heap holds the object."], size=38)
dk.save()

d = dk.slide(5, "STACK OVERFLOW")
heading(d, "Stack runs out:", "StackOverflowError.")
e = code_block(d, 470, [
    [("void ", K), ("f() {", P)],
    [("  f();", P)],
    [("}", P)],
    [("// StackOverflowError", C)],
], size=30, line_h=70)
muted(d, e + 60, ["Cause: endless recursion.", "Fix: add a base case."], size=38)
dk.save()

d = dk.slide(6, "HEAP FULL")
heading(d, "Heap runs out:", "OutOfMemoryError.")
cards(d, 480, [
    ("Cause", "Too many objects still referenced"),
    ("Typical culprit", "A cache or list that only grows"),
    ("Fix", "Release references or tune -Xmx"),
], h=180, gap=40, title_size=46, sub_size=32)
dk.save()

recap(dk, "Stack: calls.", "Heap: objects.", ["Stack is per thread", "Heap is shared and GC'd", "Two limits, two errors"])

# ======================= POST 3: constructor injection =======================
dk = Deck(os.path.join(root, "2026-10-13-spring-constructor-injection"))
hook(dk, "SPRING BOOT", "Stop using", "@Autowired", "on fields.", "Use constructor injection.")

d = dk.slide(2, "THE COMMON WAY")
heading(d, "Field injection", "looks short.")
e = code_block(d, 470, [
    [("@Service", K)],
    [("class ", K), ("OrderService ", T), ("{", P)],
    [("  @Autowired", K)],
    [("  OrderRepo ", T), ("repo;", P)],
    [("}", P)],
], size=30, line_h=66)
muted(d, e + 60, ["Short, but it hides problems."], size=38)
dk.save()

d = dk.slide(3, "THE BETTER WAY")
heading(d, "Ask for it in", "the constructor.")
e = code_block(d, 470, [
    [("@Service", K)],
    [("class ", K), ("OrderService ", T), ("{", P)],
    [("  private final ", K), ("OrderRepo ", T), ("repo;", P)],
    [("  OrderService(", T), ("OrderRepo ", T), ("r) {", P)],
    [("    this.repo = r;", P)],
    [("  }", P)],
    [("}", P)],
], size=26, line_h=60, pad_bottom=70)
muted(d, e + 50, ["One constructor? No @Autowired needed."], size=36)
dk.save()

d = dk.slide(4, "WHY #1")
heading(d, "Fields can be", "final.")
cards(d, 480, [
    ("Immutable", "Set once, never reassigned"),
    ("Never half-built", "The object is ready after new"),
    ("Thread-safe publish", "final fields are safely visible"),
], h=180, gap=40, title_size=46, sub_size=32)
dk.save()

d = dk.slide(5, "WHY #2")
heading(d, "Easy to test", "without Spring.")
e = code_block(d, 470, [
    [("var ", K), ("svc = ", P), ("new ", K), ("OrderService", T), ("(", P)],
    [("    mockRepo);", P)],
    [("", P)],
    [("// no Spring context", C)],
    [("// no reflection", C)],
], size=30, line_h=66)
muted(d, e + 60, ["Plain Java. Fast unit tests."], size=38)
dk.save()

d = dk.slide(6, "WHY #3")
heading(d, "Dependencies are", "explicit.")
cards(d, 480, [
    ("Visible", "Read the constructor, see what it needs"),
    ("Fail fast", "Missing bean? App won't start"),
    ("Spot smells", "Ten parameters? Class does too much"),
], h=180, gap=40, title_size=46, sub_size=32)
dk.save()

recap(dk, "Constructor first.", "Fields never.", ["Final, immutable fields", "Tests without Spring", "Dependencies out in the open"])
print("done")
