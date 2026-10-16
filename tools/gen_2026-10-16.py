import sys
sys.path.insert(0, "/home/claude/java-posts/tools")
from carousel_lib import *

which, OUT = sys.argv[1], sys.argv[2]
D = Deck(OUT)

if which == "casting":
    hook(D, "JAVA BASICS", "Type casting", "without", "surprises.", "Widening vs narrowing.")
    d = D.slide(2, "WIDENING")
    heading(d, "Small to big:", "automatic.")
    code_block(d, 470, [
        [("int ", K), ("i = 42;", P)],
        [("long ", K), ("l = i;", P)],
        [("double ", K), ("d = l;", P)],
    ], size=48, line_h=88, pad_bottom=70)
    muted(d, 1010, ["No cast needed.", "No data lost."], size=46, gap=78)
    D.save()
    d = D.slide(3, "NARROWING")
    heading(d, "Big to small:", "you must cast.")
    code_block(d, 470, [
        [("double ", K), ("d = 3.99;", P)],
        [("int ", K), ("i = (", P), ("int", K), (") d;", P)],
        [("// i = 3", C)],
    ], size=48, line_h=88, pad_bottom=70)
    muted(d, 1010, ["Decimals are cut,", "not rounded."], size=46, gap=78)
    D.save()
    d = D.slide(4, "OVERFLOW")
    heading(d, "Too big for", "the type?")
    code_block(d, 470, [
        [("int ", K), ("n = 130;", P)],
        [("byte ", K), ("b = (", P), ("byte", K), (") n;", P)],
        [("// b = -126", RED)],
    ], size=48, line_h=88, pad_bottom=70)
    muted(d, 1010, ["It silently wraps around.", "No error. No warning."], size=44, gap=78)
    D.save()
    d = D.slide(5, "THE TRAP")
    heading(d, "Integer division", "cuts decimals.")
    code_block(d, 470, [
        [("double ", K), ("a = 7 / 2;", P), ("   // 3.0", RED)],
        [("double ", K), ("b = (", P), ("double", K), (") 7 / 2;", P)],
        [("// b = 3.5", GREEN)],
    ], size=36, line_h=76, pad_bottom=70)
    muted(d, 940, ["Cast one side first,", "then divide."], size=46, gap=78)
    D.save()
    d = D.slide(6, "BONUS")
    heading(d, "A char is", "a number too.")
    code_block(d, 470, [
        [("char ", K), ("c = 'A';", P)],
        [("int ", K), ("n = c;", P), ("      // 65", C)],
        [("char ", K), ("e = (", P), ("char", K), (") (c + 1);", P)],
        [("// e = 'B'", C)],
    ], size=36, line_h=70, pad_bottom=70)
    muted(d, 1010, ["Handy for letters and", "simple ciphers."], size=44, gap=76)
    D.save()
    recap(D, "Cast with", "care.", ["Widening is automatic", "Narrowing needs a cast", "Overflow wraps silently", "Cast before you divide"])

elif which == "volatile":
    hook(D, "INTERVIEW QUESTION", "Why won't", "my thread", "stop?", "Java volatile explained.")
    d = D.slide(2, "THE PROBLEM")
    heading(d, "Threads can", "miss updates.")
    cards(d, 480, [
        ("Thread A", "Sets running = false"),
        ("Thread B", "May still see true"),
        ("Result", "The loop may never end"),
    ], h=170, gap=34, title_size=46, sub_size=34)
    D.save()
    d = D.slide(3, "THE CODE")
    heading(d, "A plain flag", "is not safe.")
    code_block(d, 470, [
        [("boolean ", K), ("running = ", P), ("true", K), (";", P)],
        [("", P)],
        [("// Thread B", C)],
        [("while ", K), ("(running) {", P)],
        [("  work();", P)],
        [("}", P)],
    ], size=36, line_h=64, pad_bottom=60)
    muted(d, 1040, ["It may never see the change."], size=44)
    D.save()
    d = D.slide(4, "THE FIX")
    heading(d, "Add one", "keyword.")
    code_block(d, 470, [
        [("volatile ", ORANGE), ("boolean ", K)],
        [("    running = ", P), ("true", K), (";", P)],
    ], size=42, line_h=76, pad_bottom=70)
    muted(d, 860, ["Every write is visible", "to every thread.", "", "Visibility. Not locking."], size=46, gap=76)
    D.save()
    d = D.slide(5, "THE TRAP")
    heading(d, "volatile isn't", "thread-safe.")
    code_block(d, 470, [
        [("volatile int ", K), ("count;", P)],
        [("", P)],
        [("count++;", P)],
        [("// read, add, write", C)],
    ], size=40, line_h=70, pad_bottom=60)
    muted(d, 970, ["Two threads can overlap.", "Updates get lost."], size=46, gap=76)
    D.save()
    d = D.slide(6, "THE REAL FIX")
    heading(d, "Need atomic", "updates?")
    code_block(d, 470, [
        [("AtomicInteger ", T), ("count =", P)],
        [("    new ", K), ("AtomicInteger();", T)],
        [("", P)],
        [("count.incrementAndGet();", P)],
    ], size=34, line_h=66, pad_bottom=60)
    muted(d, 990, ["Or use synchronized.", "volatile alone is not enough."], size=44, gap=76)
    D.save()
    recap(D, "Flags: volatile.", "Counters: Atomic.", ["volatile = visibility", "No mutual exclusion", "count++ is not atomic", "Use AtomicInteger"])

elif which == "junit":
    hook(D, "JUNIT 5", "One test.", "Many inputs.", "No copy-paste.", "Parameterized tests.")
    d = D.slide(2, "THE PROBLEM")
    heading(d, "Same test,", "copied again?")
    code_block(d, 470, [
        [("@Test ", ORANGE), ("void a() { f(2); }", P)],
        [("@Test ", ORANGE), ("void b() { f(4); }", P)],
        [("@Test ", ORANGE), ("void c() { f(6); }", P)],
    ], size=34, line_h=70, pad_bottom=70)
    muted(d, 950, ["Boring to write.", "Painful to maintain."], size=46, gap=78)
    D.save()
    d = D.slide(3, "SETUP")
    heading(d, "Swap one", "annotation.")
    cards(d, 480, [
        ("@Test", "becomes @ParameterizedTest"),
        ("Add a source", "Where the inputs come from"),
        ("Dependency", "junit-jupiter includes params"),
    ], h=170, gap=34, title_size=46, sub_size=34)
    D.save()
    d = D.slide(4, "@VALUESOURCE")
    heading(d, "One input", "per run.")
    code_block(d, 470, [
        [("@ParameterizedTest", ORANGE)],
        [("@ValueSource", ORANGE), ("(ints = {2, 4, 6})", P)],
        [("void ", K), ("isEven(", P), ("int ", K), ("n) {", P)],
        [("  assertTrue(n % 2 == 0);", P)],
        [("}", P)],
    ], size=32, line_h=62, pad_bottom=60)
    muted(d, 1000, ["Runs 3 times:", "2, then 4, then 6."], size=44, gap=76)
    D.save()
    d = D.slide(5, "@CSVSOURCE")
    heading(d, "Many inputs", "per run.")
    code_block(d, 470, [
        [("@ParameterizedTest", ORANGE)],
        [("@CsvSource", ORANGE), ("({\"1,2,3\", \"4,5,9\"})", P)],
        [("void ", K), ("add(", P), ("int ", K), ("a, ", P), ("int ", K), ("b, ", P), ("int ", K), ("sum) {", P)],
        [("  assertEquals(sum, a + b);", P)],
        [("}", P)],
    ], size=29, line_h=60, pad_bottom=60)
    muted(d, 1000, ["Each row is one test."], size=44)
    D.save()
    d = D.slide(6, "TIP")
    heading(d, "Readable", "test names.")
    code_block(d, 470, [
        [("@ParameterizedTest", ORANGE), ("(", P)],
        [("  name = ", P), ("\"{0} + {1} = {2}\"", ORANGE), (")", P)],
    ], size=34, line_h=66, pad_bottom=70)
    muted(d, 815, ["Test report shows:", "1 + 2 = 3", "4 + 5 = 9", "", "More: @MethodSource, @EnumSource"], size=42, gap=66)
    D.save()
    recap(D, "Write once.", "Test many.", ["Use @ParameterizedTest", "Pick a source annotation", "@CsvSource for rows", "Name the cases clearly"])
