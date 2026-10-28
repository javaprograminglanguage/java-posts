import sys
sys.path.insert(0, "/home/claude/java-posts/tools")
from carousel_lib import *

which, OUT = sys.argv[1], sys.argv[2]
D = Deck(OUT)

LAST = [0]
def cd(d, lines, size=30, y=470):
    LAST[0] = code_block(d, y, lines, size=size, line_h=58, pad_bottom=50)
    return LAST[0]

_muted = muted
def muted(d, y, lines, size=42, gap=70):
    _muted(d, max(y, LAST[0] + 60), lines, size=size, gap=gap)

if which == "arrays":
    hook(D, "JAVA BASICS", "Printing an", "array gives", "garbage.", "Java array gotchas.")
    d = D.slide(2, "THE SURPRISE")
    heading(d, "Arrays don't", "print nicely.")
    cd(d, [
        [("int[] ", K), ("a = {1, 2, 3};", P)],
        [("", P)],
        [("System.out.println(a);", P)],
        [("// ", C), ("[I@6d06d69c", RED)],
    ])
    muted(d, 900, ["That is type and hash code.", "Not the contents."], size=42, gap=70)
    D.save()
    d = D.slide(3, "THE FIX")
    heading(d, "Use the", "Arrays helpers.")
    cd(d, [
        [("Arrays.toString(a)", P)],
        [("// ", C), ("[1, 2, 3]", GREEN)],
        [("", P)],
        [("Arrays.deepToString(grid)", P)],
        [("// ", C), ("[[1, 2], [3, 4]]", GREEN)],
    ], size=28)
    muted(d, 960, ["deepToString is for nested arrays."], size=42, gap=70)
    D.save()
    d = D.slide(4, "COMPARING")
    heading(d, "== and equals()", "both disappoint.")
    cd(d, [
        [("int[] ", K), ("p = {1, 2};", P)],
        [("int[] ", K), ("q = {1, 2};", P)],
        [("", P)],
        [("p == q             ", P), ("// ", C), ("false", RED)],
        [("p.equals(q)        ", P), ("// ", C), ("false", RED)],
        [("Arrays.equals(p,q) ", P), ("// ", C), ("true", GREEN)],
    ], size=28)
    muted(d, 1000, ["equals() on arrays is identity."], size=42, gap=70)
    D.save()
    d = D.slide(5, "DEFAULTS")
    heading(d, "New arrays are", "pre-filled.")
    cards(d, 480, [
        ("int[]", "Every element is 0"),
        ("boolean[]", "Every element is false"),
        ("String[]", "Every element is null"),
    ], h=170, gap=34, title_size=42, sub_size=28)
    D.save()
    d = D.slide(6, "COPYING")
    heading(d, "b = a does", "not copy.")
    cd(d, [
        [("int[] ", K), ("b = a;", P)],
        [("b[0] = 99;", P)],
        [("// ", C), ("a[0] is 99 too", RED)],
        [("", P)],
        [("int[] ", K), ("c = Arrays.copyOf(", P)],
        [("    a, a.length);", P)],
    ], size=30)
    muted(d, 1010, ["copyOf makes a real copy."], size=42, gap=70)
    D.save()
    recap(D, "Java arrays", "in a nutshell.", ["Print with Arrays.toString", "Compare with Arrays.equals", "Defaults are 0, false, null", "Copy with Arrays.copyOf"])

elif which == "nested":
    hook(D, "INTERVIEW", "Nested class", "or inner", "class?", "Spot the difference.")
    d = D.slide(2, "TWO KINDS")
    heading(d, "A class inside", "a class.")
    cards(d, 480, [
        ("Static nested", "No link to an outer object"),
        ("Inner (non-static)", "Holds a hidden Outer reference"),
        ("Rule of thumb", "Prefer static nested"),
    ], h=170, gap=34, title_size=42, sub_size=28)
    D.save()
    d = D.slide(3, "STATIC NESTED")
    heading(d, "No Outer", "object needed.")
    cd(d, [
        [("class ", K), ("Outer {", P)],
        [("  static class ", K), ("Nested { }", P)],
        [("}", P)],
        [("", P)],
        [("new ", K), ("Outer.Nested();", P)],
    ])
    muted(d, 900, ["Behaves like a top-level class,", "just grouped inside Outer."], size=42, gap=70)
    D.save()
    d = D.slide(4, "INNER CLASS")
    heading(d, "An Outer object", "comes first.")
    cd(d, [
        [("class ", K), ("Outer {", P)],
        [("  class ", K), ("Inner { }", P)],
        [("}", P)],
        [("", P)],
        [("Outer o = ", P), ("new ", K), ("Outer();", P)],
        [("Outer.Inner i = o.", P), ("new ", K), ("Inner();", P)],
    ], size=28)
    muted(d, 1000, ["Every Inner belongs to one Outer."], size=42, gap=70)
    D.save()
    d = D.slide(5, "ACCESS")
    heading(d, "What can they", "reach?")
    cards(d, 480, [
        ("Both", "Can read Outer's private fields"),
        ("Inner class", "Also uses Outer's instance fields"),
        ("Static nested", "Only Outer's static members"),
    ], h=170, gap=34, title_size=42, sub_size=28)
    D.save()
    d = D.slide(6, "WATCH OUT")
    heading(d, "Inner classes", "can hold on.")
    cards(d, 480, [
        ("Hidden reference", "Inner may keep its Outer alive"),
        ("Long-lived inner", "A cached callback can pin Outer"),
        ("Safer choice", "Make it static if Outer is unused"),
    ], h=170, gap=34, title_size=42, sub_size=28)
    D.save()
    recap(D, "Nested classes", "in a nutshell.", ["Static nested: no Outer needed", "Inner: tied to an Outer object", "Both reach Outer's privates", "Prefer static when you can"])

elif which == "scheduled":
    hook(D, "SPRING BOOT", "Run code", "on a", "timer.", "Spring @Scheduled.")
    d = D.slide(2, "SETUP")
    heading(d, "Switch it on", "first.")
    cd(d, [
        [("@SpringBootApplication", T)],
        [("@EnableScheduling", T)],
        [("public class ", K), ("App { }", P)],
    ])
    muted(d, 790, ["Without @EnableScheduling,", "@Scheduled is ignored."], size=42, gap=70)
    D.save()
    d = D.slide(3, "THE JOB")
    heading(d, "Annotate a", "method.")
    cd(d, [
        [("@Scheduled", T), ("(fixedRate = 5000)", P)],
        [("void ", K), ("sync() {", P)],
        [("  // runs every 5 seconds", C)],
        [("}", P)],
    ])
    muted(d, 850, ["The method takes no arguments.", "The bean must be a Spring bean."], size=42, gap=70)
    D.save()
    d = D.slide(4, "TIMING")
    heading(d, "Rate or", "delay?")
    cards(d, 480, [
        ("fixedRate", "Start to start, every N ms"),
        ("fixedDelay", "Waits N ms after each run ends"),
        ("initialDelay", "Waits before the first run"),
    ], h=170, gap=34, title_size=42, sub_size=28)
    D.save()
    d = D.slide(5, "CRON")
    heading(d, "Cron has", "six fields.")
    cd(d, [
        [("@Scheduled", T), ("(cron =", P)],
        [("  ", P), ("\"0 0 9 * * MON-FRI\"", GREEN), (")", P)],
        [("// ", C), ("weekdays at 9:00", C)],
    ], size=28)
    muted(d, 740, ["Order: second, minute, hour,", "day, month, weekday.", "Seconds come first."], size=42, gap=70)
    D.save()
    d = D.slide(6, "WATCH OUT")
    heading(d, "Two common", "surprises.")
    cards(d, 480, [
        ("One thread by default", "A slow job delays the others"),
        ("Bigger pool", "spring.task.scheduling.pool.size"),
        ("Many instances", "Every instance runs the job"),
    ], h=170, gap=34, title_size=42, sub_size=28)
    D.save()
    recap(D, "@Scheduled", "in a nutshell.", ["Add @EnableScheduling", "fixedRate or fixedDelay", "Cron starts with seconds", "Scale out? Jobs run on each node"])
