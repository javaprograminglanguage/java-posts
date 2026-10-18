import sys
sys.path.insert(0, "/home/claude/java-posts/tools")
from carousel_lib import *

which, OUT = sys.argv[1], sys.argv[2]
D = Deck(OUT)

if which == "varargs":
    hook(D, "JAVA BASICS", "One method.", "Any number", "of arguments.", "Java varargs.")
    d = D.slide(2, "THE PROBLEM")
    heading(d, "Too many", "overloads.")
    code_block(d, 470, [
        [("int ", K), ("sum(", P), ("int ", K), ("a, ", P), ("int ", K), ("b)", P)],
        [("int ", K), ("sum(", P), ("int ", K), ("a, ", P), ("int ", K), ("b,", P)],
        [("        ", P), ("int ", K), ("c)", P)],
        [("int ", K), ("sum(", P), ("int ", K), ("a, ", P), ("int ", K), ("b,", P)],
        [("        ", P), ("int ", K), ("c, ", P), ("int ", K), ("d)", P)],
    ], size=32, line_h=60, pad_bottom=60)
    muted(d, 980, ["And what about five?", "Or ten?"], size=46, gap=78)
    D.save()
    d = D.slide(3, "THE SYNTAX")
    heading(d, "Three dots.", "That's it.")
    code_block(d, 470, [
        [("static int ", K), ("sum(", P), ("int", K), ("... nums) {", P)],
        [("  int ", K), ("t = 0;", P)],
        [("  for ", K), ("(", P), ("int ", K), ("n : nums)", P)],
        [("    t += n;", P)],
        [("  return ", K), ("t;", P)],
        [("}", P)],
    ], size=30, line_h=58, pad_bottom=40)
    muted(d, 1010, ["sum()  sum(1, 2)", "sum(1, 2, 3, 4)  all work."], size=40, gap=64)
    D.save()
    d = D.slide(4, "UNDER THE HOOD")
    heading(d, "It is just", "an array.")
    code_block(d, 470, [
        [("int", K), ("... nums", P)],
        [("// same as", C)],
        [("int", K), ("[] nums", P)],
        [("", P)],
        [("int", K), ("[] arr = {1, 2, 3};", P)],
        [("sum(arr);  ", P), ("// 6", C)],
    ], size=34, line_h=62, pad_bottom=50)
    muted(d, 1010, ["Inside the method, use", "nums.length and nums[i]."], size=42, gap=70)
    D.save()
    d = D.slide(5, "THE RULES")
    heading(d, "One only.", "Always last.")
    code_block(d, 470, [
        [("// OK", C)],
        [("void ", K), ("log(String msg,", P)],
        [("         Object... args)", P)],
        [("", P)],
        [("// compile error", C)],
        [("void ", K), ("bad(", P), ("int", RED), ("... a, String s)", RED)],
    ], size=32, line_h=60, pad_bottom=50)
    muted(d, 990, ["printf() and String.format()", "use exactly this pattern."], size=42, gap=70)
    D.save()
    d = D.slide(6, "GOOD TO KNOW")
    heading(d, "Fixed arity", "wins.")
    code_block(d, 470, [
        [("void ", K), ("p(", P), ("int ", K), ("a, ", P), ("int ", K), ("b)", P)],
        [("  { print(", P), ("\"fixed\"", GREEN), ("); }", P)],
        [("void ", K), ("p(", P), ("int", K), ("... a)", P)],
        [("  { print(", P), ("\"varargs\"", GREEN), ("); }", P)],
        [("", P)],
        [("p(1, 2);     ", P), ("// fixed", C)],
        [("p(1, 2, 3);  ", P), ("// varargs", C)],
    ], size=30, line_h=58, pad_bottom=40)
    muted(d, 1040, ["No args gives an empty", "array, never null."], size=42, gap=70)
    D.save()
    recap(D, "Varargs", "in a nutshell.", ["Type... name", "Becomes an array", "One per method, last", "Fixed arity wins"])

elif which == "cf":
    hook(D, "JAVA CONCURRENCY", "Don't block.", "Chain", "it.", "CompletableFuture.")
    d = D.slide(2, "THE PROBLEM")
    heading(d, "Future.get()", "blocks.")
    code_block(d, 470, [
        [("Future<String> f =", P)],
        [("  pool.submit(task);", P)],
        [("", P)],
        [("String s = f.get();", P)],
        [("// thread waits here", RED)],
    ], size=34, line_h=64, pad_bottom=50)
    muted(d, 960, ["No chaining.", "No callbacks."], size=46, gap=78)
    D.save()
    d = D.slide(3, "RUN ASYNC")
    heading(d, "Start work", "in background.")
    code_block(d, 470, [
        [("CompletableFuture<String> f =", P)],
        [("  CompletableFuture", P)],
        [("   .supplyAsync(() ->", P)],
        [("     loadUser());", P)],
    ], size=32, line_h=62, pad_bottom=60)
    muted(d, 940, ["Runs on the common", "ForkJoinPool by default.", "Your thread keeps going."], size=42, gap=70)
    D.save()
    d = D.slide(4, "CHAIN")
    heading(d, "Transform", "the result.")
    code_block(d, 470, [
        [("supplyAsync(() -> ", P), ("\"ayush\"", GREEN), (")", P)],
        [("  .thenApply(", P)],
        [("    String::toUpperCase)", P)],
        [("  .thenAccept(", P)],
        [("    System.out::println);", P)],
        [("// AYUSH", C)],
    ], size=32, line_h=60, pad_bottom=40)
    muted(d, 1010, ["thenApply maps a value.", "thenAccept consumes it."], size=42, gap=70)
    D.save()
    d = D.slide(5, "COMBINE")
    heading(d, "Merge two", "tasks.")
    code_block(d, 470, [
        [("var ", K), ("a = supplyAsync(() -> 10);", P)],
        [("var ", K), ("b = supplyAsync(() -> 20);", P)],
        [("", P)],
        [("a.thenCombine(b, Integer::sum)", P)],
        [("  .join();", P), ("  // 30", C)],
    ], size=28, line_h=62, pad_bottom=60)
    muted(d, 960, ["Both run in parallel.", "Combine when both finish."], size=44, gap=72)
    D.save()
    d = D.slide(6, "ERRORS")
    heading(d, "Handle failure", "in the chain.", size=62)
    code_block(d, 470, [
        [("supplyAsync(() -> 1 / 0)", P)],
        [("  .exceptionally(", P)],
        [("    ex -> -1)", P)],
        [("  .join();", P), ("  // -1", C)],
    ], size=34, line_h=66, pad_bottom=60)
    muted(d, 940, ["No try/catch around get().", "The fallback value takes over."], size=42, gap=70)
    D.save()
    recap(D, "Async,", "without blocking.", ["supplyAsync starts work", "thenApply transforms", "thenCombine joins two", "exceptionally recovers"])

elif which == "git":
    hook(D, "GIT & TOOLING", "Merge", "or", "rebase?", "Two ways to update a branch.")
    d = D.slide(2, "THE SETUP")
    heading(d, "main moved", "while you worked.")
    code_block(d, 470, [
        [("main:     A - B - C", P)],
        [("               \\", P)],
        [("feature:        D - E", ORANGE)],
    ], size=36, line_h=70, pad_bottom=70)
    muted(d, 900, ["Your branch is behind.", "How do you catch up?"], size=46, gap=78)
    D.save()
    d = D.slide(3, "MERGE")
    heading(d, "Join the", "histories.")
    code_block(d, 470, [
        [("git switch feature", P)],
        [("git merge main", P)],
        [("", P)],
        [("A - B - C ---- M", P)],
        [("     \\       /", P)],
        [("      D --- E", ORANGE)],
    ], size=34, line_h=62, pad_bottom=40)
    muted(d, 1000, ["Adds one merge commit M.", "History stays as it happened."], size=40, gap=64)
    D.save()
    d = D.slide(4, "REBASE")
    heading(d, "Replay on", "top of main.")
    code_block(d, 470, [
        [("git switch feature", P)],
        [("git rebase main", P)],
        [("", P)],
        [("A - B - C - D' - E'", ORANGE)],
    ], size=34, line_h=64, pad_bottom=60)
    muted(d, 920, ["One straight line.", "D and E are rewritten", "as new commits."], size=44, gap=72)
    D.save()
    d = D.slide(5, "THE GOLDEN RULE")
    heading(d, "Never rebase", "shared branches.")
    cards(d, 480, [
        ("Rebase rewrites history", "New commit hashes"),
        ("Teammates get conflicts", "Their copy no longer matches"),
        ("Needs a force push", "Use --force-with-lease"),
    ], h=170, gap=34, title_size=42, sub_size=32)
    D.save()
    d = D.slide(6, "WHEN TO USE")
    heading(d, "Pick the", "right tool.")
    cards(d, 480, [
        ("Rebase", "Your own branch, before the PR"),
        ("Merge", "Shared branches like main"),
        ("Team rule", "Follow your project's policy"),
    ], h=170, gap=34, title_size=46, sub_size=34)
    D.save()
    recap(D, "Clean line or", "true history.", ["Merge: safe and honest", "Rebase: clean and linear", "Never rebase shared work", "Squash is a third option"])
