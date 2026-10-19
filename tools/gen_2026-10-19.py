import sys
sys.path.insert(0, "/home/claude/java-posts/tools")
from carousel_lib import *

which, OUT = sys.argv[1], sys.argv[2]
D = Deck(OUT)

if which == "shortcircuit":
    hook(D, "JAVA BASICS", "Two ANDs.", "One is", "lazy.", "&& vs & in Java.")
    d = D.slide(2, "THE SETUP")
    heading(d, "A method with", "a side effect.")
    code_block(d, 470, [
        [("static boolean ", K), ("check() {", P)],
        [("  System.out.println(", P), ("\"check\"", GREEN), (");", P)],
        [("  return true;", P)],
        [("}", P)],
    ], size=32, line_h=62, pad_bottom=60)
    muted(d, 940, ["It prints every time", "it runs. Watch when it runs."], size=44, gap=72)
    D.save()
    d = D.slide(3, "AND")
    heading(d, "&& stops", "early.")
    code_block(d, 470, [
        [("false && check()", P)],
        [("// prints nothing", C)],
        [("", P)],
        [("false & check()", P)],
        [("// prints check", RED)],
    ], size=36, line_h=66, pad_bottom=60)
    muted(d, 960, ["Left side is false, so the", "result can only be false."], size=42, gap=70)
    D.save()
    d = D.slide(4, "OR")
    heading(d, "|| skips", "too.")
    code_block(d, 470, [
        [("true || check()", P)],
        [("// prints nothing", C)],
        [("", P)],
        [("true | check()", P)],
        [("// prints check", RED)],
    ], size=36, line_h=66, pad_bottom=60)
    muted(d, 960, ["Left side is true, so the", "result can only be true."], size=42, gap=70)
    D.save()
    d = D.slide(5, "WHY IT MATTERS")
    heading(d, "Safe null", "checks.")
    code_block(d, 470, [
        [("String s = ", P), ("null", K), (";", P)],
        [("", P)],
        [("s != ", P), ("null", K), (" && s.length() > 3", P)],
        [("// false, safe", C)],
        [("", P)],
        [("s != ", P), ("null", K), (" & s.length() > 3", RED)],
        [("// NullPointerException", RED)],
    ], size=30, line_h=58, pad_bottom=40)
    muted(d, 1040, ["The left side guards the right."], size=42, gap=70)
    D.save()
    d = D.slide(6, "ON INTEGERS")
    heading(d, "& and | are", "also bitwise.")
    code_block(d, 470, [
        [("6     = 110", P)],
        [("3     = 011", P)],
        [("6 & 3 = 010", P), ("  // 2", C)],
        [("6 | 3 = 111", P), ("  // 7", C)],
    ], size=38, line_h=70, pad_bottom=60)
    muted(d, 1000, ["AND keeps shared bits.", "OR keeps any bit."], size=44, gap=72)
    D.save()
    recap(D, "Short-circuit", "in a nutshell.", ["&& and || skip the right", "& and | always run both", "Use && for null guards", "On ints, & and | are bitwise"])

elif which == "twr":
    hook(D, "JAVA INTERVIEW", "Stop closing", "resources", "by hand.", "try-with-resources.")
    d = D.slide(2, "THE OLD WAY")
    heading(d, "finally gets", "messy.")
    code_block(d, 470, [
        [("BufferedReader r = ", P), ("null", K), (";", P)],
        [("try {", P)],
        [("  r = ", P), ("new ", K), ("BufferedReader(..);", P)],
        [("  r.readLine();", P)],
        [("} ", P), ("finally ", K), ("{", P)],
        [("  if (r != ", P), ("null", K), (") r.close();", P)],
        [("}", P)],
    ], size=30, line_h=56, pad_bottom=40)
    muted(d, 1030, ["And close() can throw too."], size=44, gap=70)
    D.save()
    d = D.slide(3, "THE FIX")
    heading(d, "Declare it in", "the try.")
    code_block(d, 470, [
        [("try (", P), ("var ", K), ("r = ", P), ("new ", K), ("BufferedReader(", P)],
        [("       ", P), ("new ", K), ("FileReader(", P), ("\"a.txt\"", GREEN), (")))  {", P)],
        [("  System.out.println(", P)],
        [("      r.readLine());", P)],
        [("}", P)],
        [("// r is closed automatically", C)],
    ], size=28, line_h=58, pad_bottom=50)
    muted(d, 1010, ["No finally. No null check.", "Closed even if an exception hits."], size=42, gap=70)
    D.save()
    d = D.slide(4, "THE RULE")
    heading(d, "Implement", "AutoCloseable.")
    code_block(d, 470, [
        [("class ", K), ("Conn ", P), ("implements", K)],
        [("        AutoCloseable {", P)],
        [("  ", P), ("public void ", K), ("close() {", P)],
        [("    System.out.println(", P)],
        [("        ", P), ("\"closed\"", GREEN), (");", P)],
        [("  }", P)],
        [("}", P)],
    ], size=28, line_h=56, pad_bottom=40)
    muted(d, 1030, ["Streams, readers, JDBC", "connections all do it."], size=42, gap=70)
    D.save()
    d = D.slide(5, "MANY RESOURCES")
    heading(d, "Closed in", "reverse order.")
    code_block(d, 470, [
        [("try (A x = ", P), ("new ", K), ("A(", P), ("\"a\"", GREEN), (");", P)],
        [("     A y = ", P), ("new ", K), ("A(", P), ("\"b\"", GREEN), (")) {", P)],
        [("  System.out.println(", P), ("\"body\"", GREEN), (");", P)],
        [("}", P)],
        [("", P)],
        [("// body", C)],
        [("// close b", C)],
        [("// close a", C)],
    ], size=30, line_h=56, pad_bottom=40)
    muted(d, 1080, ["Last opened, first closed."], size=40, gap=70)
    D.save()
    d = D.slide(6, "HIDDEN BONUS")
    heading(d, "No lost", "exceptions.")
    cards(d, 480, [
        ("Body throws an error", "That one is the main exception"),
        ("Then close() throws too", "It is attached, not lost"),
        ("Read it back with", "e.getSuppressed()"),
    ], h=170, gap=34, title_size=42, sub_size=32)
    D.save()
    recap(D, "try-with-resources", "in a nutshell.", ["Declare it in the try ( )", "Needs AutoCloseable", "Closed in reverse order", "Suppressed errors kept"])

elif which == "jdbc":
    hook(D, "JDBC & SECURITY", "Never glue", "SQL", "together.", "PreparedStatement vs Statement.")
    d = D.slide(2, "THE TRAP")
    heading(d, "Building SQL", "with +.")
    code_block(d, 470, [
        [("String sql =", P)],
        [("  ", P), ("\"SELECT * FROM users \"", GREEN)],
        [("  + ", P), ("\"WHERE name = '\"", GREEN)],
        [("  + name + ", P), ("\"'\"", GREEN), (";", P)],
    ], size=30, line_h=62, pad_bottom=60)
    muted(d, 940, ["Looks fine.", "Until a user types something odd."], size=44, gap=72)
    D.save()
    d = D.slide(3, "THE ATTACK")
    heading(d, "SQL injection", "in one line.")
    code_block(d, 470, [
        [("name = ", P), ("\"' OR '1'='1\"", RED)],
        [("", P)],
        [("SELECT * FROM users", P)],
        [("WHERE name = ", P), ("'' OR '1'='1'", RED)],
    ], size=32, line_h=62, pad_bottom=60)
    muted(d, 940, ["'1'='1' is always true.", "Every row comes back."], size=44, gap=72)
    D.save()
    d = D.slide(4, "THE FIX")
    heading(d, "Use a", "placeholder.")
    code_block(d, 470, [
        [("String sql = ", P), ("\"SELECT * FROM users \"", GREEN)],
        [("  + ", P), ("\"WHERE name = ?\"", GREEN), (";", P)],
        [("", P)],
        [("try (", P), ("var ", K), ("ps = con", P)],
        [("     .prepareStatement(sql)) {", P)],
        [("  ps.setString(1, name);", P)],
        [("  ps.executeQuery();", P)],
        [("}", P)],
    ], size=26, line_h=54, pad_bottom=30)
    muted(d, 1050, ["? is filled by setString()."], size=42, gap=70)
    D.save()
    d = D.slide(5, "WHY IT WORKS")
    heading(d, "Data stays", "data.")
    cards(d, 480, [
        ("The query shape is fixed", "Only the ? slots take values"),
        ("Values are bound safely", "Quotes stay plain text"),
        ("Input never becomes SQL", "The attack is just a name"),
    ], h=170, gap=34, title_size=42, sub_size=32)
    D.save()
    d = D.slide(6, "WATCH OUT")
    heading(d, "? is for values", "only.")
    cards(d, 480, [
        ("Works for values", "WHERE name = ?"),
        ("Not for names", "Table or column names"),
        ("Whitelist those", "Check against a fixed list"),
    ], h=170, gap=34, title_size=46, sub_size=34)
    D.save()
    recap(D, "Safe SQL", "in a nutshell.", ["Never concatenate input", "Use PreparedStatement", "Bind values with set...()", "Whitelist column names"])
