import sys
sys.path.insert(0, "/home/claude/java-posts/tools")
from carousel_lib import *

which, OUT = sys.argv[1], sys.argv[2]
D = Deck(OUT)

if which == "overflow":
    hook(D, "JAVA BASICS", "Max int", "+ 1 =", "negative?", "Integer overflow in Java.")
    d = D.slide(2, "THE SURPRISE")
    heading(d, "No error.", "Just wrong.")
    code_block(d, 470, [
        [("int ", K), ("max = Integer.MAX_VALUE;", P)],
        [("", P)],
        [("System.out.println(max + 1);", P)],
        [("// -2147483648", RED)],
    ], size=30, line_h=62, pad_bottom=60)
    muted(d, 940, ["Java does not warn you.", "The number just wraps around."], size=44, gap=72)
    D.save()
    d = D.slide(3, "WHY")
    heading(d, "int has 32 bits.", "It wraps around.")
    cards(d, 480, [
        ("The range", "-2,147,483,648 to 2,147,483,647"),
        ("Past the max", "It wraps to the minimum"),
        ("No exception", "Java stays silent"),
    ], h=170, gap=34, title_size=42, sub_size=32)
    D.save()
    d = D.slide(4, "THE SNEAKY ONE")
    heading(d, "long does not", "save you.")
    code_block(d, 470, [
        [("long ", K), ("a = 1_000_000 * 1_000_000;", P)],
        [("// -727379968", RED)],
        [("", P)],
        [("long ", K), ("b = 1_000_000L * 1_000_000;", P)],
        [("// 1000000000000", C)],
    ], size=28, line_h=62, pad_bottom=60)
    muted(d, 960, ["Math runs as int first,", "then widens to long."], size=44, gap=72)
    D.save()
    d = D.slide(5, "FIX 1")
    heading(d, "Use the Math", "exact methods.")
    code_block(d, 470, [
        [("int ", K), ("r = Math.addExact(max, 1);", P)],
        [("", P)],
        [("// ArithmeticException:", C)],
        [("// integer overflow", RED)],
    ], size=30, line_h=62, pad_bottom=60)
    muted(d, 940, ["Also: subtractExact(),", "multiplyExact(), toIntExact()."], size=42, gap=70)
    D.save()
    d = D.slide(6, "FIX 2")
    heading(d, "Or pick a", "bigger type.")
    cards(d, 480, [
        ("Use long", "Mark one operand with L"),
        ("Use BigInteger", "No fixed size limit"),
        ("Math.abs(MIN_VALUE)", "Still negative. Watch out"),
    ], h=170, gap=34, title_size=42, sub_size=32)
    D.save()
    recap(D, "Integer overflow", "in a nutshell.", ["int wraps, never throws", "Mixed math starts as int", "Use Math.addExact()", "Use long or BigInteger"])

elif which == "sealed":
    hook(D, "JAVA 17+", "Control who", "can extend", "your class.", "Sealed classes in Java.")
    d = D.slide(2, "THE PROBLEM")
    heading(d, "Anyone can", "extend it.")
    code_block(d, 470, [
        [("interface ", K), ("Shape {}", P)],
        [("", P)],
        [("// any file, any package", C)],
        [("class ", K), ("Hack ", P), ("implements ", K), ("Shape {}", P)],
    ], size=32, line_h=62, pad_bottom=60)
    muted(d, 940, ["You can never list", "every valid subtype."], size=44, gap=72)
    D.save()
    d = D.slide(3, "SEALED")
    heading(d, "Seal it with", "permits.")
    code_block(d, 470, [
        [("sealed interface ", K), ("Shape", P)],
        [("    permits ", K), ("Circle, Square {}", P)],
        [("", P)],
        [("record ", K), ("Circle(", P), ("double ", K), ("r)", P)],
        [("    implements ", K), ("Shape {}", P)],
        [("record ", K), ("Square(", P), ("double ", K), ("s)", P)],
        [("    implements ", K), ("Shape {}", P)],
    ], size=30, line_h=56, pad_bottom=40)
    muted(d, 1030, ["Only the listed types", "can implement Shape."], size=42, gap=70)
    D.save()
    d = D.slide(4, "THE RULES")
    heading(d, "Every subtype", "must choose.")
    cards(d, 480, [
        ("final", "No further subclasses"),
        ("sealed", "Restrict its own subclasses"),
        ("non-sealed", "Opens the hierarchy again"),
    ], h=170, gap=34, title_size=44, sub_size=32)
    D.save()
    d = D.slide(5, "JAVA 21+")
    heading(d, "Exhaustive", "switch.")
    code_block(d, 470, [
        [("double ", K), ("area(Shape s) {", P)],
        [("  return switch ", K), ("(s) {", P)],
        [("    case ", K), ("Circle c ->", P)],
        [("      Math.PI * c.r() * c.r();", P)],
        [("    case ", K), ("Square q ->", P)],
        [("      q.s() * q.s();", P)],
        [("  };", P)],
        [("}", P)],
    ], size=28, line_h=54, pad_bottom=30)
    muted(d, 1040, ["No default needed."], size=44, gap=72)
    D.save()
    d = D.slide(6, "BONUS")
    heading(d, "The compiler", "has your back.")
    cards(d, 480, [
        ("Add a Triangle", "To the permits list"),
        ("Forget its case?", "Compile error, not a bug"),
        ("Caught early", "Not at runtime"),
    ], h=170, gap=34, title_size=44, sub_size=32)
    D.save()
    recap(D, "Sealed classes", "in a nutshell.", ["permits lists allowed types", "final, sealed or non-sealed", "Final feature in Java 17", "Switch needs no default"])

elif which == "configprops":
    hook(D, "SPRING BOOT", "Stop using", "@Value", "everywhere.", "Spring Boot config, done right.")
    d = D.slide(2, "@VALUE")
    heading(d, "One field,", "one property.")
    code_block(d, 470, [
        [("@Value", K), ("(", P), ("\"${app.mail.host}\"", GREEN), (")", P)],
        [("String ", T), ("host;", P)],
        [("", P)],
        [("@Value", K), ("(", P), ("\"${app.mail.port}\"", GREEN), (")", P)],
        [("int ", K), ("port;", P)],
    ], size=30, line_h=62, pad_bottom=60)
    muted(d, 960, ["Fine for one or two.", "Messy for ten."], size=44, gap=72)
    D.save()
    d = D.slide(3, "THE BETTER WAY")
    heading(d, "Group them", "in a record.")
    code_block(d, 470, [
        [("@ConfigurationProperties", K), ("(", P)],
        [("    ", P), ("\"app.mail\"", GREEN), (")", P)],
        [("record ", K), ("MailProps(", P)],
        [("    String ", T), ("host,", P)],
        [("    int ", K), ("port", P), (") {}", P)],
    ], size=30, line_h=62, pad_bottom=60)
    muted(d, 960, ["The prefix plus the field", "name finds the property."], size=44, gap=72)
    D.save()
    d = D.slide(4, "REGISTER IT")
    heading(d, "Turn it on", "once.")
    code_block(d, 470, [
        [("@SpringBootApplication", K)],
        [("@ConfigurationPropertiesScan", K)],
        [("class ", K), ("App {}", P)],
    ], size=28, line_h=62, pad_bottom=60)
    muted(d, 880, ["Or list it with", "@EnableConfigurationProperties."], size=42, gap=70)
    D.save()
    d = D.slide(5, "WHY IT WINS")
    heading(d, "More than", "grouping.")
    cards(d, 480, [
        ("Type-safe", "Text becomes int, Duration, List"),
        ("Validation", "Add @Validated and @NotBlank"),
        ("Relaxed binding", "kebab-case and ENV_VARS bind"),
    ], h=170, gap=34, title_size=42, sub_size=32)
    D.save()
    d = D.slide(6, "WHEN TO USE WHAT")
    heading(d, "@Value still", "has a place.")
    cards(d, 480, [
        ("@Value", "One-off simple values"),
        ("@Value also has SpEL", "Expressions like #{2 * 60}"),
        ("Properties class", "Grouped or validated config"),
    ], h=170, gap=34, title_size=42, sub_size=32)
    D.save()
    recap(D, "Spring config", "in a nutshell.", ["@Value for one-offs", "@ConfigurationProperties groups", "Records bind by name", "Validate at startup"])
