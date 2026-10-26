import sys
sys.path.insert(0, "/home/claude/java-posts/tools")
from carousel_lib import *

which, OUT = sys.argv[1], sys.argv[2]
D = Deck(OUT)

if which == "labeled":
    hook(D, "JAVA BASICS", "Break out of", "two loops", "at once.", "Labeled break & continue.")
    d = D.slide(2, "THE PROBLEM")
    heading(d, "break only exits", "one loop.")
    cards(d, 480, [
        ("break", "Leaves the innermost loop only"),
        ("continue", "Skips to the next inner iteration"),
        ("Nested loops?", "The outer loop keeps running"),
    ], h=170, gap=34, title_size=42, sub_size=30)
    D.save()
    d = D.slide(3, "LABELED BREAK")
    heading(d, "Name the loop,", "then break it.")
    code_block(d, 470, [
        [("outer:", ORANGE)],
        [("for ", K), ("(", P), ("int", K), ("[] row : grid) {", P)],
        [("  ", P), ("for ", K), ("(", P), ("int", K), (" n : row) {", P)],
        [("    ", P), ("if ", K), ("(n == 3)", P)],
        [("      ", P), ("break ", K), ("outer;", ORANGE)],
        [("  }", P)],
        [("}", P)],
    ], size=30, line_h=58, pad_bottom=50)
    muted(d, 1040, ["Exits both loops", "as soon as n is 3."], size=42, gap=70)
    D.save()
    d = D.slide(4, "LABELED CONTINUE")
    heading(d, "Skip to the next", "outer round.")
    code_block(d, 470, [
        [("outer:", ORANGE)],
        [("for ", K), ("(", P), ("int ", K), ("i = 0; i < 3; i++)", P)],
        [("  ", P), ("for ", K), ("(", P), ("int ", K), ("j = 0; j < 3; j++) {", P)],
        [("    ", P), ("if ", K), ("(j == 1)", P)],
        [("      ", P), ("continue ", K), ("outer;", ORANGE)],
        [("    print(i + ", P), ("\",\"", GREEN), (" + j);", P)],
        [("  }", P)],
    ], size=30, line_h=58, pad_bottom=50)
    muted(d, 1040, ["Prints 0,0  1,0  2,0", "j never reaches 1."], size=42, gap=70)
    D.save()
    d = D.slide(5, "GOOD TO KNOW")
    heading(d, "Labels work", "on loops only.")
    cards(d, 480, [
        ("Naming style", "Lowercase or UPPERCASE, e.g. outer:"),
        ("Allowed with", "for, while and do-while loops"),
        ("No goto in Java", "A label is not a jump target"),
    ], h=170, gap=34, title_size=42, sub_size=30)
    D.save()
    d = D.slide(6, "USE WITH CARE")
    heading(d, "Often a method", "is cleaner.")
    code_block(d, 470, [
        [("static boolean has(int[][] g,", P)],
        [("                   ", P), ("int ", K), ("t) {", P)],
        [("  ", P), ("for ", K), ("(", P), ("int", K), ("[] r : g)", P)],
        [("    ", P), ("for ", K), ("(", P), ("int", K), (" n : r)", P)],
        [("      ", P), ("if ", K), ("(n == t) ", P), ("return true", GREEN), (";", P)],
        [("  ", P), ("return false", RED), (";", P)],
        [("}", P)],
    ], size=30, line_h=58, pad_bottom=50)
    muted(d, 1090, ["Same result, no label needed."], size=42, gap=70)
    D.save()
    recap(D, "Labeled loops", "in a nutshell.", ["break exits one loop only", "break label exits the named loop", "continue label skips outer round", "Extract a method if it reads better"])

elif which == "singleton":
    hook(D, "INTERVIEW", "One class,", "only one", "instance.", "The Singleton pattern.")
    d = D.slide(2, "THE IDEA")
    heading(d, "Singleton in", "three rules.")
    cards(d, 480, [
        ("Private constructor", "Nobody else can call new"),
        ("One static instance", "Created once, shared everywhere"),
        ("Public access method", "getInstance() returns it"),
    ], h=170, gap=34, title_size=42, sub_size=30)
    D.save()
    d = D.slide(3, "THE TRAP")
    heading(d, "Lazy singleton", "is not thread-safe.")
    code_block(d, 470, [
        [("static Config get() {", P)],
        [("  ", P), ("if ", K), ("(instance == ", P), ("null", K), (")", P)],
        [("    instance = ", RED), ("new ", K), ("Config();", RED)],
        [("  ", P), ("return ", K), ("instance;", P)],
        [("}", P)],
    ], size=30, line_h=60, pad_bottom=50)
    muted(d, 920, ["Two threads can both see null", "and create two instances."], size=42, gap=70)
    D.save()
    d = D.slide(4, "HOLDER IDIOM")
    heading(d, "Lazy and", "thread-safe.")
    code_block(d, 470, [
        [("class ", K), ("Config {", P)],
        [("  ", P), ("private ", K), ("Config() {}", P)],
        [("  ", P), ("private static class ", K), ("Holder {", P)],
        [("    ", P), ("static final ", K), ("Config I = ", P), ("new ", K), ("Config();", P)],
        [("  }", P)],
        [("  ", P), ("static ", K), ("Config get() { ", P), ("return ", K), ("Holder.I; }", GREEN)],
        [("}", P)],
    ], size=28, line_h=58, pad_bottom=50)
    muted(d, 1040, ["Holder loads only on first use,", "and the JVM does it safely."], size=42, gap=70)
    D.save()
    d = D.slide(5, "ENUM SINGLETON")
    heading(d, "The simplest", "safe version.")
    code_block(d, 470, [
        [("enum ", K), ("Config {", P)],
        [("  INSTANCE;", GREEN)],
        [("  ", P), ("void ", K), ("load() { ", P), ("/* ... */", C), (" }", P)],
        [("}", P)],
        [("", P)],
        [("Config.INSTANCE.load();", P)],
    ], size=30, line_h=58, pad_bottom=50)
    muted(d, 1000, ["Safe against reflection and", "serialization tricks too."], size=42, gap=70)
    D.save()
    d = D.slide(6, "WHICH ONE")
    heading(d, "Pick the right", "one.")
    cards(d, 480, [
        ("Enum", "Simple and safest default"),
        ("Holder idiom", "When you need a normal class"),
        ("In Spring Boot", "Beans are singletons already"),
    ], h=170, gap=34, title_size=42, sub_size=30)
    D.save()
    recap(D, "Singleton", "in a nutshell.", ["Private constructor, one instance", "Plain lazy getInstance() is unsafe", "Holder idiom: lazy and safe", "Enum: simplest and safest"])

elif which == "reset":
    hook(D, "GIT", "Undo a commit", "without", "panic.", "git reset: soft, mixed, hard.")
    d = D.slide(2, "THE BASICS")
    heading(d, "reset moves", "your branch back.")
    cards(d, 480, [
        ("git reset <mode> HEAD~1", "Undoes the last commit"),
        ("The mode decides", "What happens to your changes"),
        ("Three modes", "--soft, --mixed (default), --hard"),
    ], h=170, gap=34, title_size=40, sub_size=30)
    D.save()
    d = D.slide(3, "--SOFT")
    heading(d, "Keeps changes", "staged.")
    code_block(d, 470, [
        [("$ git reset --soft HEAD~1", P)],
        [("", P)],
        [("Commit  ", C), ("undone", RED)],
        [("Staging ", C), ("kept", GREEN)],
        [("Files   ", C), ("kept", GREEN)],
    ], size=30, line_h=60, pad_bottom=50)
    muted(d, 950, ["Good for rewording a commit", "or squashing the last few."], size=42, gap=70)
    D.save()
    d = D.slide(4, "--MIXED")
    heading(d, "Keeps changes,", "unstages them.")
    code_block(d, 470, [
        [("$ git reset HEAD~1", P)],
        [("", P)],
        [("Commit  ", C), ("undone", RED)],
        [("Staging ", C), ("cleared", RED)],
        [("Files   ", C), ("kept", GREEN)],
    ], size=30, line_h=60, pad_bottom=50)
    muted(d, 950, ["This is the default mode.", "Re-add what you want."], size=42, gap=70)
    D.save()
    d = D.slide(5, "--HARD")
    heading(d, "Deletes", "your changes.")
    code_block(d, 470, [
        [("$ git reset --hard HEAD~1", P)],
        [("", P)],
        [("Commit  ", C), ("undone", RED)],
        [("Staging ", C), ("cleared", RED)],
        [("Files   ", C), ("reset", RED)],
    ], size=30, line_h=60, pad_bottom=50)
    muted(d, 950, ["Uncommitted work is lost.", "Use it carefully."], size=42, gap=70)
    D.save()
    d = D.slide(6, "SAFETY NET")
    heading(d, "Already pushed?", "Use revert.")
    cards(d, 480, [
        ("git reflog", "Find a commit you reset away"),
        ("Shared branch", "Prefer git revert <commit>"),
        ("Why", "Revert adds a commit, keeps history"),
    ], h=170, gap=34, title_size=42, sub_size=30)
    D.save()
    recap(D, "git reset", "in a nutshell.", ["--soft keeps changes staged", "--mixed keeps them unstaged", "--hard throws them away", "Pushed commits: use git revert"])
