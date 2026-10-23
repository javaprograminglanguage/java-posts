import sys
sys.path.insert(0, "/home/claude/java-posts/tools")
from carousel_lib import *

which, OUT = sys.argv[1], sys.argv[2]
D = Deck(OUT)

if which == "incr":
    hook(D, "JAVA BASICS", "i++", "vs", "++i", "What is the difference?")
    d = D.slide(2, "THE BASICS")
    heading(d, "Both add 1", "to the variable.")
    code_block(d, 470, [
        [("int ", K), ("a = 5;", P)],
        [("a++;", P), ("   // a is 6", C)],
        [("++a;", P), ("   // a is 7", C)],
    ], size=30, line_h=64, pad_bottom=60)
    muted(d, 860, ["The difference shows up", "when you use the result."], size=44, gap=72)
    D.save()
    d = D.slide(3, "POST-INCREMENT")
    heading(d, "i++ returns", "the old value.")
    code_block(d, 470, [
        [("int ", K), ("i = 5;", P)],
        [("int ", K), ("x = i++;", P)],
        [("", P)],
        [("// x = 5", GREEN)],
        [("// i = 6", GREEN)],
    ], size=30, line_h=60, pad_bottom=50)
    muted(d, 1000, ["Use the value first,", "then add 1."], size=44, gap=72)
    D.save()
    d = D.slide(4, "PRE-INCREMENT")
    heading(d, "++i returns", "the new value.")
    code_block(d, 470, [
        [("int ", K), ("i = 5;", P)],
        [("int ", K), ("y = ++i;", P)],
        [("", P)],
        [("// y = 6", GREEN)],
        [("// i = 6", GREEN)],
    ], size=30, line_h=60, pad_bottom=50)
    muted(d, 1000, ["Add 1 first,", "then use the value."], size=44, gap=72)
    D.save()
    d = D.slide(5, "THE TRAP")
    heading(d, "Never write", "i = i++.")
    code_block(d, 470, [
        [("int ", K), ("i = 5;", P)],
        [("i = i++;", RED)],
        [("", P)],
        [("// i is still 5", RED)],
    ], size=30, line_h=62, pad_bottom=60)
    muted(d, 920, ["The old value (5) is assigned", "back, so the +1 is lost."], size=42, gap=70)
    D.save()
    d = D.slide(6, "IN LOOPS")
    heading(d, "In a for loop,", "no difference.")
    code_block(d, 470, [
        [("for ", K), ("(", P), ("int ", K), ("i = 0; i < 3; i++)", P)],
        [("for ", K), ("(", P), ("int ", K), ("i = 0; i < 3; ++i)", P)],
        [("", P)],
        [("// both run for i = 0, 1, 2", GREEN)],
    ], size=26, line_h=58, pad_bottom=60)
    muted(d, 880, ["The result is unused there,", "so both behave the same."], size=42, gap=70)
    D.save()
    recap(D, "i++ vs ++i", "in a nutshell.", ["i++ returns the old value", "++i returns the new value", "Both add 1 to the variable", "Avoid i = i++"])

elif which == "executor":
    hook(D, "CONCURRENCY", "Stop using", "new Thread()", "everywhere.", "Meet ExecutorService.")
    d = D.slide(2, "WHY")
    heading(d, "Threads are", "not free.")
    cards(d, 480, [
        ("Creating is costly", "One thread per task adds up"),
        ("No upper limit", "Too many threads hurt the app"),
        ("A pool reuses them", "A few workers, many tasks"),
    ], h=170, gap=34, title_size=42, sub_size=32)
    D.save()
    d = D.slide(3, "CREATE A POOL")
    heading(d, "Submit tasks,", "not threads.")
    code_block(d, 470, [
        [("ExecutorService pool =", P)],
        [("  Executors", P)],
        [("   .newFixedThreadPool(4);", P)],
        [("", P)],
        [("pool.submit(() ->", P)],
        [("   System.out.println(", P), ("\"hi\"", GREEN), ("));", P)],
    ], size=28, line_h=56, pad_bottom=50)
    muted(d, 1010, ["4 workers handle all tasks."], size=44, gap=72)
    D.save()
    d = D.slide(4, "GET A RESULT")
    heading(d, "submit() returns", "a Future.")
    code_block(d, 470, [
        [("Future<Integer> f =", P)],
        [("   pool.submit(() -> ", P), ("42", GREEN), (");", P)],
        [("", P)],
        [("int ", K), ("r = f.get();", P)],
    ], size=30, line_h=62, pad_bottom=60)
    muted(d, 880, ["get() blocks until the", "task is finished."], size=44, gap=72)
    D.save()
    d = D.slide(5, "SHUT DOWN")
    heading(d, "Always shut", "the pool down.")
    code_block(d, 470, [
        [("pool.shutdown();", P)],
        [("// no new tasks accepted", C)],
        [("// running tasks finish", C)],
    ], size=30, line_h=64, pad_bottom=60)
    muted(d, 860, ["Without it, worker threads", "can keep the JVM alive."], size=44, gap=72)
    D.save()
    d = D.slide(6, "CHOOSING")
    heading(d, "Pick the", "right pool.")
    cards(d, 480, [
        ("newFixedThreadPool(n)", "Exactly n worker threads"),
        ("newCachedThreadPool()", "Grows as tasks arrive"),
        ("newVirtualThreadPerTaskExecutor()", "One virtual thread per task, Java 21+"),
    ], h=170, gap=34, title_size=36, sub_size=30)
    D.save()
    recap(D, "ExecutorService", "in a nutshell.", ["Reuse threads with a pool", "submit() returns a Future", "future.get() blocks", "Always call shutdown()"])

elif which == "validation":
    hook(D, "SPRING BOOT", "Never trust", "user", "input.", "Bean Validation in Spring Boot.")
    d = D.slide(2, "SETUP")
    heading(d, "One starter", "to add.")
    code_block(d, 470, [
        [("<artifactId>", P)],
        [("  spring-boot-starter-validation", GREEN)],
        [("</artifactId>", P)],
    ], size=28, line_h=64, pad_bottom=60)
    muted(d, 870, ["Add it to your pom.xml.", "Annotations do the checking."], size=44, gap=72)
    D.save()
    d = D.slide(3, "CONSTRAINTS")
    heading(d, "Annotate your", "request class.")
    code_block(d, 470, [
        [("record ", K), ("SignupRequest(", P)],
        [("  @NotBlank ", ORANGE), ("String name,", P)],
        [("  @Email ", ORANGE), ("String email,", P)],
        [("  @Min(18) ", ORANGE), ("int age", P)],
        [(") {}", P)],
    ], size=30, line_h=60, pad_bottom=50)
    muted(d, 1000, ["Rules live next to the data."], size=44, gap=72)
    D.save()
    d = D.slide(4, "TRIGGER IT")
    heading(d, "Add @Valid", "to the body.")
    code_block(d, 470, [
        [("@PostMapping(", P), ("\"/signup\"", GREEN), (")", P)],
        [("void ", K), ("signup(", P)],
        [("  @Valid ", ORANGE), ("@RequestBody", P)],
        [("  SignupRequest req) {", P)],
        [("  // runs only if valid", C)],
        [("}", P)],
    ], size=28, line_h=56, pad_bottom=50)
    muted(d, 1010, ["Without @Valid, nothing", "is checked."], size=42, gap=70)
    D.save()
    d = D.slide(5, "WHAT HAPPENS")
    heading(d, "Invalid input", "is rejected.")
    cards(d, 480, [
        ("400 Bad Request", "Sent automatically to the client"),
        ("Your method never runs", "Validation fails first"),
        ("Customize the response", "Handle the exception globally"),
    ], h=170, gap=34, title_size=42, sub_size=32)
    D.save()
    d = D.slide(6, "PICK THE RIGHT ONE")
    heading(d, "Know your", "constraints.")
    cards(d, 480, [
        ("@NotNull", "Rejects null only"),
        ("@NotBlank", "Strings: not null, not blank"),
        ("@Size(min, max)", "Limits length or size"),
    ], h=170, gap=34, title_size=42, sub_size=32)
    D.save()
    recap(D, "Validation", "in a nutshell.", ["Add the validation starter", "Annotate your fields", "Use @Valid on @RequestBody", "Invalid input returns 400"])
