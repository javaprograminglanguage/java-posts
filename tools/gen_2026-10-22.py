import sys
sys.path.insert(0, "/home/claude/java-posts/tools")
from carousel_lib import *

which, OUT = sys.argv[1], sys.argv[2]
D = Deck(OUT)

if which == "boxing":
    hook(D, "JAVA BASICS", "Integer", "is not", "int.", "Autoboxing and unboxing.")
    d = D.slide(2, "THE BASICS")
    heading(d, "Java converts", "for you.")
    code_block(d, 470, [
        [("int ", K), ("a = 5;", P)],
        [("Integer b = a;", P), ("  // boxing", C)],
        [("int ", K), ("c = b;", P), ("      // unboxing", C)],
    ], size=30, line_h=64, pad_bottom=60)
    muted(d, 860, ["Primitive  ↔  wrapper object.", "Done automatically by the compiler."], size=42, gap=70)
    D.save()
    d = D.slide(3, "WHY IT EXISTS")
    heading(d, "Collections need", "objects.")
    code_block(d, 470, [
        [("List<Integer> list =", P)],
        [("    new ", K), ("ArrayList<>();", P)],
        [("", P)],
        [("list.add(5);", P), ("  // boxes", C)],
        [("int ", K), ("x = list.get(0);", P)],
        [("// unboxes", C)],
    ], size=30, line_h=58, pad_bottom=50)
    muted(d, 1040, ["List<int> does not compile."], size=44, gap=72)
    D.save()
    d = D.slide(4, "TRAP 1")
    heading(d, "Unboxing null", "crashes.")
    code_block(d, 470, [
        [("Integer n = ", P), ("null", K), (";", P)],
        [("int ", K), ("x = n;", P)],
        [("// NullPointerException", RED)],
    ], size=30, line_h=64, pad_bottom=60)
    muted(d, 860, ["Unboxing calls n.intValue().", "Calling it on null throws."], size=44, gap=72)
    D.save()
    d = D.slide(5, "TRAP 2")
    heading(d, "Hidden objects", "in loops.")
    code_block(d, 470, [
        [("Long sum = 0L;", RED)],
        [("for ", K), ("(", P), ("long ", K), ("i = 0; i < n; i++)", P)],
        [("    sum += i;", P)],
        [("", P)],
        [("long sum = 0;", GREEN), ("  // better", C)],
    ], size=30, line_h=60, pad_bottom=50)
    muted(d, 1000, ["Boxed Long: a new object", "for many iterations."], size=44, gap=72)
    D.save()
    d = D.slide(6, "RULES OF THUMB")
    heading(d, "Use the", "right type.")
    cards(d, 480, [
        ("Prefer primitives", "Faster and never null"),
        ("Wrappers for generics", "Collections, Optional, maps"),
        ("Check before unboxing", "Avoid surprise NPEs"),
    ], h=170, gap=34, title_size=42, sub_size=32)
    D.save()
    recap(D, "Autoboxing", "in a nutshell.", ["Boxing: int → Integer", "Unboxing: Integer → int", "Unboxing null throws NPE", "Prefer primitives in loops"])

elif which == "gc":
    hook(D, "JVM INTERNALS", "Java frees", "memory", "for you.", "How garbage collection works.")
    d = D.slide(2, "THE RULE")
    heading(d, "Unreachable", "means removable.")
    cards(d, 480, [
        ("GC roots", "Locals, static fields, threads"),
        ("Reachable = alive", "A path from a root exists"),
        ("Unreachable = eligible", "The GC may reclaim it"),
    ], h=170, gap=34, title_size=42, sub_size=32)
    D.save()
    d = D.slide(3, "EXAMPLE")
    heading(d, "Lose the", "reference.")
    code_block(d, 470, [
        [("Object o = ", P), ("new ", K), ("Object();", P)],
        [("// reachable via o", C)],
        [("", P)],
        [("o = ", P), ("null", K), (";", P)],
        [("// now unreachable", RED)],
    ], size=30, line_h=62, pad_bottom=60)
    muted(d, 950, ["Eligible for GC.", "Not deleted instantly."], size=44, gap=72)
    D.save()
    d = D.slide(4, "CYCLES")
    heading(d, "Cycles don't", "save objects.")
    code_block(d, 470, [
        [("A a = ", P), ("new ", K), ("A();", P)],
        [("B b = ", P), ("new ", K), ("B();", P)],
        [("a.b = b;  b.a = a;", P)],
        [("", P)],
        [("a = ", P), ("null", K), ("; b = ", P), ("null", K), (";", P)],
        [("// both eligible", GREEN)],
    ], size=30, line_h=58, pad_bottom=50)
    muted(d, 1040, ["Only roots decide, not counts."], size=44, gap=72)
    D.save()
    d = D.slide(5, "System.gc()")
    heading(d, "System.gc() is", "only a hint.")
    code_block(d, 470, [
        [("System.gc();", P)],
        [("// a request, not a command", C)],
    ], size=30, line_h=64, pad_bottom=60)
    cards(d, 760, [
        ("No guarantee", "The JVM decides if and when"),
        ("Rarely needed", "Let the GC do its job"),
    ], h=170, gap=34, title_size=42, sub_size=32)
    D.save()
    d = D.slide(6, "LEAKS")
    heading(d, "Leaks still", "happen.")
    code_block(d, 470, [
        [("static final", K)],
        [("List<Object> CACHE =", P)],
        [("    new ", K), ("ArrayList<>();", P)],
        [("", P)],
        [("CACHE.add(", P), ("new ", K), ("Object());", P)],
        [("// never removed = never freed", RED)],
    ], size=28, line_h=56, pad_bottom=50)
    muted(d, 1000, ["Static references live forever.", "Remove what you no longer need."], size=42, gap=70)
    D.save()
    recap(D, "Garbage collection", "in a nutshell.", ["Unreachable = eligible", "Cycles don't keep objects", "System.gc() is just a hint", "Static refs can leak memory"])

elif which == "actuator":
    hook(D, "SPRING BOOT", "Is your", "app", "healthy?", "Spring Boot Actuator.")
    d = D.slide(2, "WHAT IT DOES")
    heading(d, "Production tools,", "built in.")
    cards(d, 480, [
        ("Health checks", "Is the app up and running?"),
        ("Metrics", "Memory, requests, JVM stats"),
        ("App info", "Version and build details"),
    ], h=170, gap=34, title_size=42, sub_size=32)
    D.save()
    d = D.slide(3, "SETUP")
    heading(d, "One starter", "to add.")
    code_block(d, 470, [
        [("<artifactId>", P)],
        [("  spring-boot-starter-actuator", GREEN)],
        [("</artifactId>", P)],
    ], size=30, line_h=64, pad_bottom=60)
    muted(d, 870, ["Add it to your pom.xml.", "No extra config needed."], size=44, gap=72)
    D.save()
    d = D.slide(4, "HEALTH")
    heading(d, "Check the", "health endpoint.")
    code_block(d, 470, [
        [("GET /actuator/health", P)],
        [("", P)],
        [("{", P)],
        [("  \"status\": ", P), ("\"UP\"", GREEN)],
        [("}", P)],
    ], size=30, line_h=60, pad_bottom=50)
    muted(d, 1000, ["Load balancers and probes", "can call this URL."], size=44, gap=72)
    D.save()
    d = D.slide(5, "EXPOSE MORE")
    heading(d, "Only health", "is exposed.")
    code_block(d, 470, [
        [("management:", P)],
        [("  endpoints:", P)],
        [("    web:", P)],
        [("      exposure:", P)],
        [("        include: ", P), ("health,info", GREEN)],
    ], size=30, line_h=56, pad_bottom=50)
    muted(d, 960, ["Choose endpoints on purpose."], size=44, gap=72)
    D.save()
    d = D.slide(6, "SAFETY")
    heading(d, "Don't expose", "everything.")
    cards(d, 480, [
        ("Avoid include: \"*\"", "Exposes more than you need"),
        ("Secure endpoints", "Use Spring Security"),
        ("Health details", "show-details is never by default"),
    ], h=170, gap=34, title_size=42, sub_size=32)
    D.save()
    recap(D, "Actuator", "in a nutshell.", ["Add the actuator starter", "/actuator/health = app status", "Only health exposed by default", "Secure what you expose"])
