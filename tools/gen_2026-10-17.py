import sys
sys.path.insert(0, "/home/claude/java-posts/tools")
from carousel_lib import *

which, OUT = sys.argv[1], sys.argv[2]
D = Deck(OUT)

if which == "enums":
    hook(D, "JAVA BASICS", "Stop using", "strings as", "constants.", "Meet Java enums.")
    d = D.slide(2, "THE PROBLEM")
    heading(d, "Magic strings", "fail silently.")
    code_block(d, 470, [
        [("String ", T), ("s = ", P), ("\"PAID\"", GREEN), (";", P)],
        [("", P)],
        [("if ", K), ("(s.equals(", P), ("\"PAYD\"", RED), (")) {", P)],
        [("  ship();", P)],
        [("}", P)],
    ], size=36, line_h=66, pad_bottom=60)
    muted(d, 1010, ["A typo compiles fine", "and never runs."], size=46, gap=78)
    D.save()
    d = D.slide(3, "THE ENUM")
    heading(d, "One type,", "fixed values.")
    code_block(d, 470, [
        [("enum ", K), ("Status {", P)],
        [("  PENDING, PAID, SHIPPED", P)],
        [("}", P)],
        [("", P)],
        [("Status s = Status.PAID;", P)],
    ], size=36, line_h=66, pad_bottom=60)
    muted(d, 1010, ["Typos become", "compile errors."], size=46, gap=78)
    D.save()
    d = D.slide(4, "FIELDS")
    heading(d, "Enums can", "hold data.")
    code_block(d, 470, [
        [("enum ", K), ("Size {", P)],
        [("  S(36), M(40), L(44);", P)],
        [("", P)],
        [("  private final int ", K), ("cm;", P)],
        [("  Size(", P), ("int ", K), ("cm) {", P)],
        [("    this.cm = cm;", P)],
        [("  }", P)],
        [("}", P)],
    ], size=32, line_h=58, pad_bottom=20)
    muted(d, 1075, ["Constructors are private."], size=44)
    D.save()
    d = D.slide(5, "SWITCH")
    heading(d, "Perfect with", "switch.")
    code_block(d, 470, [
        [("String ", T), ("msg = ", P), ("switch ", K), ("(s) {", P)],
        [("  case ", K), ("PENDING -> ", P), ("\"Waiting\"", GREEN), (";", P)],
        [("  case ", K), ("PAID -> ", P), ("\"Thanks!\"", GREEN), (";", P)],
        [("  case ", K), ("SHIPPED -> ", P), ("\"On the way\"", GREEN), (";", P)],
        [("};", P)],
    ], size=30, line_h=60, pad_bottom=60)
    muted(d, 960, ["No default needed.", "The compiler checks", "every case."], size=44, gap=72)
    D.save()
    d = D.slide(6, "BUILT-IN")
    heading(d, "Free methods", "included.")
    code_block(d, 470, [
        [("Status.values();", P)],
        [("// [PENDING, PAID, SHIPPED]", C)],
        [("", P)],
        [("Status.valueOf(", P), ("\"PAID\"", GREEN), (");", P)],
        [("// Status.PAID", C)],
        [("", P)],
        [("Status.PAID.ordinal();", P)],
        [("// 1", C)],
    ], size=32, line_h=58, pad_bottom=20)
    muted(d, 1075, ["valueOf() throws on bad names."], size=40)
    D.save()
    recap(D, "Enums beat", "strings.", ["A fixed set of values", "Compile-time safety", "Fields and methods", "Great with switch"])

elif which == "comparator":
    hook(D, "INTERVIEW QUESTION", "Comparable", "vs", "Comparator?", "Sorting objects in Java.")
    d = D.slide(2, "THE PROBLEM")
    heading(d, "Sort your own", "objects?")
    code_block(d, 470, [
        [("List<User> users = ...;", P)],
        [("", P)],
        [("Collections.sort(users);", P)],
        [("// compile error", RED)],
    ], size=36, line_h=66, pad_bottom=60)
    muted(d, 940, ["Java does not know", "how to order a User."], size=46, gap=78)
    D.save()
    d = D.slide(3, "COMPARABLE")
    heading(d, "One natural order,", "inside the class.", size=58)
    code_block(d, 470, [
        [("class ", K), ("User ", P), ("implements", K)],
        [("    Comparable<User> {", P)],
        [("", P)],
        [("  public int ", K), ("compareTo(User o) {", P)],
        [("    return Integer", P)],
        [("      .compare(age, o.age);", P)],
        [("  }", P)],
        [("}", P)],
    ], size=32, line_h=58, pad_bottom=20)
    muted(d, 1075, ["Now sort(users) just works."], size=44)
    D.save()
    d = D.slide(4, "COMPARATOR")
    heading(d, "Any order you want,", "outside the class.", size=58)
    code_block(d, 470, [
        [("Comparator<User> byName =", P)],
        [("  Comparator.comparing(", P)],
        [("    User::getName);", P)],
        [("", P)],
        [("users.sort(byName);", P)],
    ], size=34, line_h=62, pad_bottom=60)
    muted(d, 960, ["Many orders.", "No changes to User."], size=46, gap=78)
    D.save()
    d = D.slide(5, "CHAINING")
    heading(d, "Sort by two", "fields.")
    code_block(d, 470, [
        [("users.sort(Comparator", P)],
        [("  .comparing(User::getCity)", P)],
        [("  .thenComparing(", P)],
        [("    User::getName));", P)],
    ], size=34, line_h=64, pad_bottom=60)
    muted(d, 920, ["City first, then name.", "", "Add .reversed() to flip it."], size=44, gap=70)
    D.save()
    d = D.slide(6, "THE TRAP")
    heading(d, "Never compare", "by subtracting.")
    code_block(d, 470, [
        [("// risky", C)],
        [("return a - b;", RED)],
        [("", P)],
        [("// safe", C)],
        [("return Integer.compare(a, b);", GREEN)],
    ], size=32, line_h=62, pad_bottom=60)
    muted(d, 960, ["2 billion minus -2 billion", "overflows to a negative."], size=42, gap=72)
    D.save()
    recap(D, "Natural vs", "custom order.", ["Comparable: compareTo()", "Comparator: compare()", "Comparators chain easily", "Never subtract to compare"])

elif which == "profiles":
    hook(D, "SPRING BOOT", "One app.", "Many", "environments.", "Spring Boot profiles.")
    d = D.slide(2, "THE PROBLEM")
    heading(d, "Dev and prod", "are different.")
    cards(d, 480, [
        ("Dev", "Local database, debug logs"),
        ("Test", "Mock services"),
        ("Prod", "Real database, quiet logs"),
    ], h=170, gap=34, title_size=46, sub_size=34)
    D.save()
    d = D.slide(3, "CONFIG FILES")
    heading(d, "One file", "per profile.")
    code_block(d, 470, [
        [("application.properties", P)],
        [("application-dev.properties", ORANGE)],
        [("application-prod.properties", ORANGE)],
    ], size=38, line_h=88, pad_bottom=70)
    muted(d, 960, ["Profile files override", "the base file."], size=46, gap=78)
    D.save()
    d = D.slide(4, "ACTIVATE")
    heading(d, "Pick the", "active profile.")
    code_block(d, 470, [
        [("# in a file", C)],
        [("spring.profiles.active=dev", P)],
        [("", P)],
        [("# or at startup", C)],
        [("java -jar app.jar \\", P)],
        [("  --spring.profiles.active=prod", P)],
    ], size=30, line_h=58, pad_bottom=60)
    muted(d, 1000, ["Or set the environment variable", "SPRING_PROFILES_ACTIVE."], size=38, gap=62)
    D.save()
    d = D.slide(5, "@PROFILE")
    heading(d, "Beans per", "profile.")
    code_block(d, 470, [
        [("@Profile", ORANGE), ("(", P), ("\"dev\"", GREEN), (")", P)],
        [("@Service", ORANGE)],
        [("class ", K), ("FakeMail ", P), ("implements ", K), ("Mail {}", P)],
        [("", P)],
        [("@Profile", ORANGE), ("(", P), ("\"prod\"", GREEN), (")", P)],
        [("@Service", ORANGE)],
        [("class ", K), ("SmtpMail ", P), ("implements ", K), ("Mail {}", P)],
    ], size=30, line_h=58, pad_bottom=60)
    muted(d, 1060, ["Only the active profile's", "bean is created."], size=42, gap=70)
    D.save()
    d = D.slide(6, "SECURITY")
    heading(d, "Never commit", "secrets.")
    code_block(d, 470, [
        [("# application-prod.properties", C)],
        [("spring.datasource.password=", P)],
        [("  ${DB_PASSWORD}", GREEN)],
    ], size=34, line_h=78, pad_bottom=60)
    muted(d, 930, ["Spring reads the value from", "an environment variable.", "", "Keep secrets out of Git."], size=42, gap=68)
    D.save()
    recap(D, "One build.", "Every environment.", ["File per profile", "Activate with one property", "@Profile for beans", "Secrets in env variables"])
