import sys
sys.path.insert(0, "/home/claude/java-posts/tools")
from carousel_lib import *

which, OUT = sys.argv[1], sys.argv[2]
D = Deck(OUT)

if which == "ternary":
    hook(D, "JAVA BASICS", "The ternary", "operator", "? :", "A one-line if-else.")
    d = D.slide(2, "SYNTAX")
    heading(d, "One line", "instead of five.")
    code_block(d, 470, [
        [("int ", K), ("age = 20;", P)],
        [("String s = age >= 18", P)],
        [("   ? ", K), ("\"adult\"", GREEN), (" : ", K), ("\"minor\"", GREEN), (";", P)],
    ], size=30, line_h=64, pad_bottom=60)
    muted(d, 860, ["condition ? ifTrue : ifFalse"], size=44, gap=72)
    D.save()
    d = D.slide(3, "GOOD USE")
    heading(d, "Great for simple", "choices.")
    code_block(d, 470, [
        [("int ", K), ("max = (a > b) ? a : b;", P)],
        [("", P)],
        [("String msg = ok", P)],
        [("   ? ", K), ("\"Saved\"", GREEN), (" : ", K), ("\"Failed\"", GREEN), (";", P)],
    ], size=30, line_h=62, pad_bottom=50)
    muted(d, 920, ["It is an expression,", "so it returns a value."], size=44, gap=72)
    D.save()
    d = D.slide(4, "NESTING")
    heading(d, "Nesting gets", "hard to read.")
    code_block(d, 470, [
        [("String g = s >= 90 ? ", P), ("\"A\"", GREEN)],
        [("   : s >= 60 ? ", P), ("\"B\"", GREEN), (" : ", P), ("\"C\"", GREEN), (";", P)],
    ], size=30, line_h=64, pad_bottom=60)
    muted(d, 790, ["It works, but for 3 or more", "branches prefer if-else."], size=44, gap=72)
    D.save()
    d = D.slide(5, "TRAP 1")
    heading(d, "Mixed types get", "promoted.")
    code_block(d, 470, [
        [("System.out.println(", P)],
        [("   ", P), ("true", K), (" ? ", P), ("1", GREEN), (" : ", P), ("2.0", GREEN), (");", P)],
        [("", P)],
        [("// prints 1.0, not 1", RED)],
    ], size=30, line_h=62, pad_bottom=50)
    muted(d, 920, ["Both branches become", "double, so 1 turns into 1.0."], size=44, gap=72)
    D.save()
    d = D.slide(6, "TRAP 2")
    heading(d, "Unboxing can", "throw an NPE.")
    code_block(d, 470, [
        [("Integer n = ", P), ("null", K), (";", P)],
        [("int ", K), ("r = flag ? n : 0;", P)],
        [("", P)],
        [("// NullPointerException", RED)],
    ], size=30, line_h=62, pad_bottom=50)
    muted(d, 920, ["The result type is int,", "so n gets unboxed."], size=44, gap=72)
    D.save()
    recap(D, "Ternary", "in a nutshell.", ["Short if-else that returns a value", "Great for simple choices", "Avoid deep nesting", "Watch mixed types and null"])

elif which == "threadlocal":
    hook(D, "CONCURRENCY", "Each thread", "gets its", "own copy.", "ThreadLocal in Java.")
    d = D.slide(2, "THE IDEA")
    heading(d, "One variable,", "many copies.")
    cards(d, 480, [
        ("A normal field", "All threads share one value"),
        ("A ThreadLocal", "Each thread has its own value"),
        ("No locks needed", "Threads never see each other's copy"),
    ], h=170, gap=34, title_size=42, sub_size=30)
    D.save()
    d = D.slide(3, "CREATE ONE")
    heading(d, "Set it,", "then get it.")
    code_block(d, 470, [
        [("ThreadLocal<String> user =", P)],
        [("  ThreadLocal.withInitial(", P)],
        [("    () -> ", P), ("\"none\"", GREEN), (");", P)],
        [("", P)],
        [("user.set(", P), ("\"alice\"", GREEN), (");", P)],
    ], size=30, line_h=60, pad_bottom=50)
    muted(d, 1000, ["The initial value is a default."], size=44, gap=72)
    D.save()
    d = D.slide(4, "PER THREAD")
    heading(d, "Other threads see", "their own value.")
    code_block(d, 470, [
        [("// in the main thread", C)],
        [("user.get();", P), ("   // \"alice\"", GREEN)],
        [("", P)],
        [("// in a new thread", C)],
        [("user.get();", P), ("   // \"none\"", GREEN)],
    ], size=30, line_h=60, pad_bottom=50)
    muted(d, 1000, ["The main thread's value", "stays untouched."], size=44, gap=72)
    D.save()
    d = D.slide(5, "WHERE IT IS USED")
    heading(d, "Real-world", "uses.")
    cards(d, 480, [
        ("Per-request data", "For example a user or trace id"),
        ("Non-thread-safe objects", "For example SimpleDateFormat"),
        ("Frameworks", "Spring Security's context holder"),
    ], h=170, gap=34, title_size=42, sub_size=30)
    D.save()
    d = D.slide(6, "THE TRAP")
    heading(d, "Thread pools", "reuse threads.")
    code_block(d, 470, [
        [("try ", K), ("{", P)],
        [("  user.set(", P), ("\"alice\"", GREEN), (");", P)],
        [("  handle();", P)],
        [("} ", P), ("finally ", K), ("{", P)],
        [("  user.remove();", GREEN)],
        [("}", P)],
    ], size=30, line_h=58, pad_bottom=50)
    muted(d, 1020, ["Always remove(), or stale data", "leaks into the next task."], size=40, gap=66)
    D.save()
    recap(D, "ThreadLocal", "in a nutshell.", ["One copy of a value per thread", "set(), get() and remove()", "Great for per-request context", "Always clean up in finally"])

elif which == "cacheable":
    hook(D, "SPRING BOOT", "Stop hitting", "the database", "twice.", "@Cacheable in Spring Boot.")
    d = D.slide(2, "SETUP")
    heading(d, "Turn caching", "on once.")
    code_block(d, 470, [
        [("@SpringBootApplication", ORANGE)],
        [("@EnableCaching", ORANGE)],
        [("public class ", K), ("App {}", P)],
    ], size=30, line_h=64, pad_bottom=60)
    muted(d, 860, ["Add spring-boot-starter-cache", "to your project."], size=42, gap=70)
    D.save()
    d = D.slide(3, "CACHE A METHOD")
    heading(d, "Annotate the", "slow method.")
    code_block(d, 470, [
        [("@Cacheable(", ORANGE), ("\"products\"", GREEN), (")", ORANGE)],
        [("Product find(", P), ("long ", K), ("id) {", P)],
        [("  return ", K), ("repo.load(id);", P)],
        [("}", P)],
    ], size=30, line_h=62, pad_bottom=50)
    muted(d, 910, ["The first call runs the method.", "Repeat calls skip it."], size=42, gap=70)
    D.save()
    d = D.slide(4, "THE KEY")
    heading(d, "The argument", "is the key.")
    cards(d, 480, [
        ("find(1)", "Runs the method, stores the result"),
        ("find(1) again", "Returns the cached value"),
        ("find(2)", "New key, so the method runs"),
    ], h=170, gap=34, title_size=42, sub_size=30)
    D.save()
    d = D.slide(5, "EVICTION")
    heading(d, "Keep your data", "fresh.")
    code_block(d, 470, [
        [("@CacheEvict(", ORANGE), ("\"products\"", GREEN), (")", ORANGE)],
        [("void ", K), ("delete(", P), ("long ", K), ("id) {", P)],
        [("  repo.delete(id);", P)],
        [("}", P)],
    ], size=30, line_h=62, pad_bottom=50)
    muted(d, 910, ["Removes the cached entry", "for that id."], size=42, gap=70)
    D.save()
    d = D.slide(6, "THE TRAP")
    heading(d, "Calls inside the", "same class skip it.")
    code_block(d, 470, [
        [("void ", K), ("report() {", P)],
        [("  find(1);", RED)],
        [("}", P)],
        [("", P)],
        [("// no caching here", RED)],
    ], size=30, line_h=60, pad_bottom=50)
    muted(d, 1000, ["Caching works through a proxy.", "Call it from another bean."], size=40, gap=66)
    D.save()
    recap(D, "@Cacheable", "in a nutshell.", ["@EnableCaching turns it on", "@Cacheable stores results", "@CacheEvict removes entries", "Same-class calls skip the cache"])
