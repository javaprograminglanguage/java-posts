import sys
sys.path.insert(0, "/home/claude/java-posts/tools")
from carousel_lib import *

which, OUT = sys.argv[1], sys.argv[2]
D = Deck(OUT)

if which == "stringbuilder":
    hook(D, "JAVA BASICS", "Slow loop?", "Blame the", "+ operator.", "String vs StringBuilder.")
    d = D.slide(2, "THE CAUSE")
    heading(d, "Strings never", "change.")
    cards(d, 480, [
        ("String is immutable", "It can never be modified"),
        ("Every + makes a new one", "The old text gets copied"),
        ("Inside a loop", "Lots of throwaway objects"),
    ], h=170, gap=34, title_size=42, sub_size=30)
    D.save()
    d = D.slide(3, "THE PROBLEM")
    heading(d, "Concatenating", "in a loop.")
    code_block(d, 470, [
        [("String s = ", P), ("\"\"", GREEN), (";", P)],
        [("for ", K), ("(", P), ("int ", K), ("i = 0; i < n; i++) {", P)],
        [("  s += i;", RED)],
        [("}", P)],
    ], size=30, line_h=62, pad_bottom=50)
    muted(d, 910, ["Each pass copies the old text", "into a brand new String."], size=42, gap=70)
    D.save()
    d = D.slide(4, "THE FIX")
    heading(d, "Use a", "StringBuilder.")
    code_block(d, 470, [
        [("StringBuilder sb =", P)],
        [("   ", P), ("new ", K), ("StringBuilder();", P)],
        [("for ", K), ("(", P), ("int ", K), ("i = 0; i < n; i++) {", P)],
        [("  sb.append(i);", GREEN)],
        [("}", P)],
        [("String s = sb.toString();", P)],
    ], size=30, line_h=58, pad_bottom=50)
    muted(d, 1010, ["One mutable buffer,", "no repeated copying."], size=42, gap=70)
    D.save()
    d = D.slide(5, "USEFUL METHODS")
    heading(d, "More than", "append().")
    code_block(d, 470, [
        [("sb.append(", P), ("\"abc\"", GREEN), (");", P)],
        [("sb.insert(0, ", P), ("\"x\"", GREEN), (");", P)],
        [("sb.reverse();", P)],
        [("sb.deleteCharAt(0);", P)],
        [("sb.setLength(0);", P), ("  // clear", C)],
    ], size=30, line_h=60, pad_bottom=50)
    muted(d, 1000, ["All of them change", "the same object."], size=42, gap=70)
    D.save()
    d = D.slide(6, "WHICH ONE")
    heading(d, "Pick the right", "tool.")
    cards(d, 480, [
        ("Simple a + b", "Plain + is perfectly fine"),
        ("Building in a loop", "Use StringBuilder"),
        ("StringBuffer", "Thread-safe, but slower. Rarely needed"),
    ], h=170, gap=34, title_size=42, sub_size=30)
    D.save()
    recap(D, "StringBuilder", "in a nutshell.", ["String is immutable", "+ in a loop copies again and again", "StringBuilder edits one buffer", "Plain + is fine outside loops"])

elif which == "immutable":
    hook(D, "COLLECTIONS", "Is this List", "really", "immutable?", "List.of vs Arrays.asList.")
    d = D.slide(2, "THREE WAYS")
    heading(d, "Three lists,", "three behaviours.")
    cards(d, 480, [
        ("List.of(...)", "Truly immutable, no nulls"),
        ("Arrays.asList(...)", "Fixed size, but set() works"),
        ("unmodifiableList(list)", "A read-only view"),
    ], h=170, gap=34, title_size=42, sub_size=30)
    D.save()
    d = D.slide(3, "LIST.OF")
    heading(d, "Fully", "immutable.")
    code_block(d, 470, [
        [("List<String> a =", P)],
        [("  List.of(", P), ("\"a\"", GREEN), (", ", P), ("\"b\"", GREEN), (");", P)],
        [("", P)],
        [("a.add(", P), ("\"c\"", GREEN), (");", P), ("    // throws", RED)],
        [("a.set(0, ", P), ("\"z\"", GREEN), (");", P), ("  // throws", RED)],
    ], size=30, line_h=60, pad_bottom=50)
    muted(d, 1000, ["Null elements are rejected", "with a NullPointerException."], size=42, gap=70)
    D.save()
    d = D.slide(4, "ARRAYS.ASLIST")
    heading(d, "Fixed size,", "not immutable.")
    code_block(d, 470, [
        [("List<String> b =", P)],
        [("  Arrays.asList(", P), ("\"a\"", GREEN), (", ", P), ("\"b\"", GREEN), (");", P)],
        [("", P)],
        [("b.set(0, ", P), ("\"z\"", GREEN), (");", P), ("  // works", GREEN)],
        [("b.add(", P), ("\"c\"", GREEN), (");", P), ("     // throws", RED)],
    ], size=30, line_h=60, pad_bottom=50)
    muted(d, 1000, ["You can replace elements,", "but never resize it."], size=42, gap=70)
    D.save()
    d = D.slide(5, "THE TRAP")
    heading(d, "A view is not", "a copy.")
    code_block(d, 470, [
        [("List<String> src =", P)],
        [("  ", P), ("new ", K), ("ArrayList<>(List.of(", P), ("\"a\"", GREEN), ("));", P)],
        [("var v = Collections", P)],
        [("   .unmodifiableList(src);", P)],
        [("src.add(", P), ("\"b\"", GREEN), (");", P)],
        [("// v is now [a, b]", RED)],
    ], size=30, line_h=58, pad_bottom=50)
    muted(d, 1010, ["Changes to the source", "show up in the view."], size=42, gap=70)
    D.save()
    d = D.slide(6, "WHICH ONE")
    heading(d, "Pick the right", "one.")
    cards(d, 480, [
        ("Constant data", "List.of(...)"),
        ("Wrap an existing array", "Arrays.asList(...)"),
        ("Safe snapshot (Java 10+)", "List.copyOf(list)"),
    ], h=170, gap=34, title_size=42, sub_size=30)
    D.save()
    recap(D, "Immutable lists", "in a nutshell.", ["List.of: fully immutable", "Arrays.asList: fixed size", "unmodifiableList: read-only view", "List.copyOf: a real snapshot"])

elif which == "slf4j":
    hook(D, "TOOLING", "Stop using", "System.out", "in apps.", "Logging with SLF4J.")
    d = D.slide(2, "WHY A LOGGER")
    heading(d, "println is not", "logging.")
    cards(d, 480, [
        ("Log levels", "ERROR, WARN, INFO, DEBUG, TRACE"),
        ("Configurable", "Change the output without code"),
        ("Richer output", "Timestamp, thread and class name"),
    ], h=170, gap=34, title_size=42, sub_size=30)
    D.save()
    d = D.slide(3, "GET A LOGGER")
    heading(d, "One logger", "per class.")
    code_block(d, 470, [
        [("private static final ", K), ("Logger log =", P)],
        [("  LoggerFactory.getLogger(", P)],
        [("    OrderService.", P), ("class", K), (");", P)],
        [("", P)],
        [("log.info(", P), ("\"Order placed\"", GREEN), (");", P)],
    ], size=30, line_h=60, pad_bottom=50)
    muted(d, 1000, ["Lombok's @Slf4j can", "generate this line for you."], size=42, gap=70)
    D.save()
    d = D.slide(4, "PLACEHOLDERS")
    heading(d, "Use {} instead", "of +.")
    code_block(d, 470, [
        [("// avoid", C)],
        [("log.debug(", P), ("\"User \"", GREEN), (" + name);", RED)],
        [("", P)],
        [("// better", C)],
        [("log.debug(", P), ("\"User {}\"", GREEN), (", name);", GREEN)],
    ], size=30, line_h=60, pad_bottom=50)
    muted(d, 1000, ["The message is only built", "when that level is enabled."], size=42, gap=70)
    D.save()
    d = D.slide(5, "EXCEPTIONS")
    heading(d, "Keep the", "stack trace.")
    code_block(d, 470, [
        [("// loses the trace", C)],
        [("log.error(e.getMessage());", RED)],
        [("", P)],
        [("// keeps the trace", C)],
        [("log.error(", P), ("\"Pay failed\"", GREEN), (", e);", GREEN)],
    ], size=30, line_h=60, pad_bottom=50)
    muted(d, 1000, ["Pass the exception as", "the last argument."], size=42, gap=70)
    D.save()
    d = D.slide(6, "LEVELS")
    heading(d, "Pick the right", "level.")
    cards(d, 470, [
        ("ERROR", "Something failed"),
        ("WARN", "Unexpected, but the app goes on"),
        ("INFO", "Key business events"),
        ("DEBUG", "Details for developers"),
    ], h=130, gap=26, title_size=40, sub_size=28)
    D.save()
    recap(D, "Logging", "in a nutshell.", ["Use a logger, not println", "Use {} placeholders", "Pass the exception last", "Pick the right level"])
