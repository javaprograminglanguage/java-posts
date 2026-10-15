import sys
sys.path.insert(0, "/home/claude/java-posts/tools")
from carousel_lib import *

which, OUT = sys.argv[1], sys.argv[2]
D = Deck(OUT)

def pts(d, y, items, size=40, gap=80):
    for p in items:
        d.ellipse([M, y + 12, M + 20, y + 32], fill=ORANGE)
        d.text((M + 50, y), p, font=inter(size, "SemiBold"), fill=TEXT)
        y += gap

if which == "textblocks":
    hook(D, "JAVA 15+", "Multiline", "strings", "made easy.", "Meet Java Text Blocks.")
    d = D.slide(2, "THE OLD WAY")
    heading(d, "Quotes, \\n and +", "everywhere.")
    code_block(d, 470, [
        [("String json = ", P), ("\"{\\n\"", ORANGE), (" +", P)],
        [("  ", P), ("\"  \\\"name\\\": \\\"Ava\\\"\\n\"", ORANGE), (" +", P)],
        [("  ", P), ("\"}\"", ORANGE), (";", P)],
    ], size=32, line_h=64, pad_bottom=70)
    muted(d, 960, ["Hard to read.", "Easy to break."], size=48, gap=78)
    D.save()
    d = D.slide(3, "THE NEW WAY")
    heading(d, "Just write it", "as it looks.")
    code_block(d, 470, [
        [("String json = ", P), ('"""', ORANGE)],
        [("    {", ORANGE)],
        [('      "name": "Ava"', ORANGE)],
        [("    }", ORANGE)],
        [('    """', ORANGE), (";", P)],
    ], size=38, line_h=70, pad_bottom=70)
    muted(d, 1060, ["No \\n. No escaped quotes."], size=44)
    D.save()
    d = D.slide(4, "THE RULES")
    heading(d, "Two rules", "to remember.")
    cards(d, 480, [
        ("Start with \"\"\" + new line", "Nothing else on that line"),
        ("End with \"\"\"", "Its position sets the indent"),
        ("Java 15 or newer", "Standard, no flags needed"),
    ], h=170, gap=34, title_size=42, sub_size=32)
    D.save()
    d = D.slide(5, "TIP")
    heading(d, "Long line,", "one string.")
    code_block(d, 470, [
        [("String s = ", P), ('"""', ORANGE)],
        [("    Hello ", ORANGE), ("\\", GREEN)],
        [("    World", ORANGE), ('"""', ORANGE), (";", P)],
    ], size=40, line_h=72, pad_bottom=70)
    muted(d, 930, ["A \\ at the end of a line", "removes the line break.", "Result: Hello World"], size=44, gap=76)
    D.save()
    d = D.slide(6, "BONUS")
    heading(d, "Add values", "with formatted().")
    code_block(d, 470, [
        [("String msg = ", P), ('"""', ORANGE)],
        [("    Hi %s!", ORANGE)],
        [('    """', ORANGE), (".formatted(name);", P)],
    ], size=38, line_h=70, pad_bottom=70)
    muted(d, 960, ["Great for JSON, SQL and HTML", "inside Java code."], size=44, gap=76)
    D.save()
    recap(D, "Cleaner strings.", "Cleaner code.", ["Start with \"\"\" and a new line", "No escaped quotes", "Use \\ to join lines", "Add values: formatted()"])

elif which == "deadlock":
    hook(D, "INTERVIEW QUESTION", "Two threads.", "Two locks.", "Frozen.", "Java deadlock explained.")
    d = D.slide(2, "WHAT IS IT")
    heading(d, "Everyone waits.", "Nobody moves.")
    cards(d, 480, [
        ("Thread 1", "Holds lock A, wants lock B"),
        ("Thread 2", "Holds lock B, wants lock A"),
        ("Result", "Both wait forever"),
    ], h=170, gap=34, title_size=46, sub_size=34)
    D.save()
    d = D.slide(3, "THE CODE")
    heading(d, "Opposite order", "= trouble.")
    code_block(d, 470, [
        [("// Thread 1", C)],
        [("synchronized ", K), ("(a) {", P)],
        [("  synchronized ", K), ("(b) { }", P)],
        [("}", P)],
        [("// Thread 2", C)],
        [("synchronized ", K), ("(b) {", P)],
        [("  synchronized ", K), ("(a) { }", P)],
        [("}", P)],
    ], size=32, line_h=54, pad_bottom=60)
    D.save()
    d = D.slide(4, "4 CONDITIONS")
    heading(d, "All four must", "happen.")
    cards(d, 450, [
        ("Mutual exclusion", "One thread owns the lock"),
        ("Hold and wait", "Keeps one, asks for another"),
        ("No preemption", "Locks can't be taken away"),
        ("Circular wait", "A waits for B, B waits for A"),
    ], h=135, gap=20, title_size=40, sub_size=30)
    muted(d, 1115, ["Break any one and it's gone."], size=34)
    D.save()
    d = D.slide(5, "FIX 1")
    heading(d, "Same lock", "order. Always.")
    code_block(d, 470, [
        [("// Both threads", C)],
        [("synchronized ", K), ("(a) {", P)],
        [("  synchronized ", K), ("(b) {", P)],
        [("    work();", P)],
        [("  }", P)],
        [("}", P)],
    ], size=36, line_h=64, pad_bottom=60)
    muted(d, 1040, ["No cycle, no deadlock."], size=44)
    D.save()
    d = D.slide(6, "FIX 2")
    heading(d, "Don't wait", "forever.")
    code_block(d, 470, [
        [("if ", K), ("(lock.tryLock(1, TimeUnit.SECONDS)) {", P)],
        [("  try ", K), ("{ work(); }", P)],
        [("  finally ", K), ("{ lock.unlock(); }", P)],
        [("}", P)],
    ], size=30, line_h=60, pad_bottom=60)
    muted(d, 940, ["tryLock with a timeout", "gives up instead of freezing."], size=40)
    D.save()
    recap(D, "Lock in order.", "Add timeouts.", ["Same lock order everywhere", "tryLock with a timeout", "jstack shows deadlocks"])

elif which == "advice":
    hook(D, "SPRING BOOT", "One place", "for all API", "errors.", "Meet @RestControllerAdvice.")
    d = D.slide(2, "THE PROBLEM")
    heading(d, "try/catch in", "every controller?")
    cards(d, 480, [
        ("Repeated code", "Same catch block, again and again"),
        ("Messy responses", "Each endpoint fails differently"),
        ("Hard to change", "Edit ten places for one fix"),
    ], h=170, gap=34, title_size=46, sub_size=32)
    D.save()
    d = D.slide(3, "STEP 1")
    heading(d, "Controllers", "just throw.")
    code_block(d, 470, [
        [("@GetMapping", ORANGE), ("(\"/users/{id}\")", P)],
        [("User get(", P), ("@PathVariable ", ORANGE), ("Long id) {", P)],
        [("  return ", K), ("service.find(id);", P)],
        [("}", P)],
        [("// throws UserNotFoundException", C)],
    ], size=28, line_h=54, pad_bottom=60)
    muted(d, 920, ["No try/catch. Clean code."], size=40)
    D.save()
    d = D.slide(4, "STEP 2")
    heading(d, "Catch it", "in one class.")
    code_block(d, 470, [
        [("@RestControllerAdvice", ORANGE)],
        [("class ", K), ("ApiErrors ", T), ("{", P)],
        [("  @ExceptionHandler", ORANGE), ("(", P)],
        [("    UserNotFoundException.class)", P)],
        [("  ProblemDetail ", T), ("notFound(", P)],
        [("      UserNotFoundException e) {", P)],
        [("    return ", K), ("ProblemDetail", T)],
        [("      .forStatusAndDetail(", P)],
        [("        HttpStatus.NOT_FOUND,", P)],
        [("        e.getMessage());", P)],
        [("  }", P)],
        [("}", P)],
    ], size=26, line_h=46, pad_bottom=50)
    D.save()
    d = D.slide(5, "THE RESPONSE")
    heading(d, "Clean JSON", "for the client.")
    code_block(d, 470, [
        [("HTTP 404", GREEN)],
        [("{", P)],
        [('  "status": 404,', ORANGE)],
        [('  "detail": "User 42 not found",', ORANGE)],
        [('  "instance": "/users/42"', ORANGE)],
        [("}", P)],
    ], size=32, line_h=58, pad_bottom=60)
    muted(d, 1000, ["Add setTitle() or setProperty()", "for more fields."], size=40, gap=64)
    D.save()
    d = D.slide(6, "WHY IT HELPS")
    heading(d, "Why teams", "love it.")
    cards(d, 480, [
        ("One place", "All error handling together"),
        ("Same format", "Every endpoint fails the same way"),
        ("Standard", "ProblemDetail follows RFC 9457"),
    ], h=170, gap=34, title_size=46, sub_size=32)
    D.save()
    recap(D, "Throw in code.", "Handle in one place.", ["Controllers just throw", "@RestControllerAdvice catches", "Return ProblemDetail", "One format for every error"])
print("ok", which)
