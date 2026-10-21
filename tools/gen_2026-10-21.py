import sys
sys.path.insert(0, "/home/claude/java-posts/tools")
from carousel_lib import *

which, OUT = sys.argv[1], sys.argv[2]
D = Deck(OUT)

if which == "float":
    hook(D, "JAVA BASICS", "0.1 + 0.2", "is not", "0.3.", "Floating-point in Java.")
    d = D.slide(2, "THE SURPRISE")
    heading(d, "Simple math,", "wrong answer.")
    code_block(d, 470, [
        [("System.out.println(", P)],
        [("    0.1 + 0.2);", P)],
        [("// 0.30000000000000004", RED)],
        [("", P)],
        [("System.out.println(", P)],
        [("    0.1 + 0.2 == 0.3);", P)],
        [("// false", RED)],
    ], size=30, line_h=56, pad_bottom=40)
    muted(d, 1070, ["Not a Java bug."], size=44, gap=72)
    D.save()
    d = D.slide(3, "WHY")
    heading(d, "double uses", "binary.")
    cards(d, 480, [
        ("Binary can't store 0.1", "Like 1/3 in decimal"),
        ("It stores a close value", "Tiny error, hidden by print"),
        ("Errors add up", "Especially in loops"),
    ], h=170, gap=34, title_size=42, sub_size=32)
    D.save()
    d = D.slide(4, "COMPARING")
    heading(d, "Never use ==", "on doubles.")
    code_block(d, 470, [
        [("double ", K), ("sum = 0.1 + 0.2;", P)],
        [("", P)],
        [("boolean ", K), ("same = Math.abs(", P)],
        [("    sum - 0.3) < 1e-9;", P)],
        [("// true", C)],
    ], size=30, line_h=62, pad_bottom=60)
    muted(d, 960, ["Compare with a small", "tolerance (epsilon)."], size=44, gap=72)
    D.save()
    d = D.slide(5, "MONEY")
    heading(d, "For money,", "use BigDecimal.")
    code_block(d, 470, [
        [("BigDecimal ", T), ("a =", P)],
        [("    new ", K), ("BigDecimal(", P), ("\"0.1\"", GREEN), (");", P)],
        [("BigDecimal ", T), ("b =", P)],
        [("    new ", K), ("BigDecimal(", P), ("\"0.2\"", GREEN), (");", P)],
        [("", P)],
        [("a.add(b); ", P), ("// 0.3", C)],
    ], size=30, line_h=58, pad_bottom=40)
    muted(d, 1040, ["Always build it from a String."], size=44, gap=72)
    D.save()
    d = D.slide(6, "WATCH OUT")
    heading(d, "BigDecimal", "gotchas.")
    cards(d, 480, [
        ("new BigDecimal(0.1)", "Copies the double's error"),
        ("equals() checks scale", "2.0 and 2.00 are not equal"),
        ("Use compareTo()", "Returns 0 when values match"),
    ], h=170, gap=34, title_size=42, sub_size=32)
    D.save()
    recap(D, "Floating-point", "in a nutshell.", ["double is approximate", "Never compare with ==", "Use an epsilon for doubles", "BigDecimal(String) for money"])

elif which == "chm":
    hook(D, "JAVA CONCURRENCY", "HashMap", "in threads?", "Not safe.", "ConcurrentHashMap explained.")
    d = D.slide(2, "THE PROBLEM")
    heading(d, "HashMap is not", "thread-safe.")
    cards(d, 480, [
        ("Lost updates", "Two threads, one wins"),
        ("Corrupt state", "Unpredictable behavior"),
        ("No exception", "It just breaks quietly"),
    ], h=170, gap=34, title_size=42, sub_size=32)
    D.save()
    d = D.slide(3, "THE FIX")
    heading(d, "Use", "ConcurrentHashMap.")
    code_block(d, 470, [
        [("Map<String, Integer> m =", P)],
        [("    new ", K), ("ConcurrentHashMap<>();", P)],
        [("", P)],
        [("m.merge(", P), ("\"hits\"", GREEN), (", 1,", P)],
        [("    Integer::sum);", P)],
    ], size=30, line_h=62, pad_bottom=60)
    muted(d, 950, ["Safe from many threads.", "No lock on the whole map."], size=44, gap=72)
    D.save()
    d = D.slide(4, "ATOMIC")
    heading(d, "Check-then-put", "is a trap.")
    code_block(d, 470, [
        [("// not atomic", RED)],
        [("if ", K), ("(!m.containsKey(k))", P)],
        [("    m.put(k, v);", P)],
        [("", P)],
        [("// atomic", GREEN)],
        [("m.putIfAbsent(k, v);", P)],
    ], size=30, line_h=60, pad_bottom=50)
    muted(d, 1040, ["Also: compute(), merge()."], size=44, gap=72)
    D.save()
    d = D.slide(5, "NULLS")
    heading(d, "No nulls", "allowed.")
    code_block(d, 470, [
        [("m.put(", P), ("null", K), (", 1);", P)],
        [("// NullPointerException", RED)],
        [("", P)],
        [("m.put(", P), ("\"k\"", GREEN), (", ", P), ("null", K), (");", P)],
        [("// NullPointerException", RED)],
    ], size=30, line_h=62, pad_bottom=60)
    muted(d, 940, ["HashMap allows one null key", "and null values."], size=44, gap=72)
    D.save()
    d = D.slide(6, "WHEN")
    heading(d, "Which one", "to use?")
    cards(d, 480, [
        ("HashMap", "Single thread. Fastest choice"),
        ("ConcurrentHashMap", "Shared across threads"),
        ("Collections.synchronizedMap", "One lock for every call"),
    ], h=170, gap=34, title_size=42, sub_size=32)
    D.save()
    recap(D, "ConcurrentHashMap", "in a nutshell.", ["HashMap is not thread-safe", "Use merge / putIfAbsent", "No null keys or values", "No global lock on reads"])

elif which == "stash":
    hook(D, "GIT TIPS", "Switch branch", "without", "committing.", "Meet git stash.")
    d = D.slide(2, "THE PROBLEM")
    heading(d, "Half-done work.", "Urgent bug.")
    cards(d, 480, [
        ("You have changes", "Not ready to commit"),
        ("Need another branch", "Git blocks the switch"),
        ("Don't commit junk", "Stash it instead"),
    ], h=170, gap=34, title_size=42, sub_size=32)
    D.save()
    d = D.slide(3, "STASH")
    heading(d, "Save it,", "get a clean tree.")
    code_block(d, 470, [
        [("git stash", P)],
        [("# changes saved away", C)],
        [("", P)],
        [("git switch hotfix", P)],
        [("# fix the bug, then back", C)],
        [("git switch feature", P)],
    ], size=32, line_h=62, pad_bottom=50)
    muted(d, 1040, ["Tracked changes are saved."], size=44, gap=72)
    D.save()
    d = D.slide(4, "BRING IT BACK")
    heading(d, "pop or", "apply.")
    cards(d, 480, [
        ("git stash pop", "Restore and delete the stash"),
        ("git stash apply", "Restore and keep the stash"),
        ("git stash list", "See everything you stashed"),
    ], h=170, gap=34, title_size=42, sub_size=32)
    D.save()
    d = D.slide(5, "UNTRACKED")
    heading(d, "New files are", "skipped.")
    code_block(d, 470, [
        [("# include untracked files", C)],
        [("git stash -u", P)],
        [("", P)],
        [("# name your stash", C)],
        [("git stash push -m ", P), ("\"login\"", GREEN)],
    ], size=30, line_h=62, pad_bottom=60)
    muted(d, 950, ["Names help when you", "have several stashes."], size=44, gap=72)
    D.save()
    d = D.slide(6, "GOOD TO KNOW")
    heading(d, "A few", "safety tips.")
    cards(d, 480, [
        ("Conflict on pop?", "The stash is kept"),
        ("git stash drop", "Deletes a stash for good"),
        ("Stashes pile up", "Clean them regularly"),
    ], h=170, gap=34, title_size=42, sub_size=32)
    D.save()
    recap(D, "git stash", "in a nutshell.", ["stash saves unfinished work", "pop restores and deletes", "-u includes new files", "push -m names a stash"])
