import sys
sys.path.insert(0, "/home/claude/java-posts/tools")
from carousel_lib import *

which, OUT = sys.argv[1], sys.argv[2]
D = Deck(OUT)

def cd(d, lines, size=30, y=470):
    return code_block(d, y, lines, size=size, line_h=58, pad_bottom=50)

if which == "char":
    hook(D, "JAVA BASICS", "char + 1", "is not a", "char.", "Java char arithmetic.")
    d = D.slide(2, "THE SURPRISE")
    heading(d, "char math", "gives an int.")
    cd(d, [
        [("char ", K), ("c = ", P), ("'a'", GREEN), (";", P)],
        [("", P)],
        [("System.out.println(c + 1);", P)],
        [("// ", C), ("98", RED)],
    ])
    muted(d, 900, ["Arithmetic promotes char to int.", "'a' is stored as 97."], size=42, gap=70)
    D.save()
    d = D.slide(3, "THE FIX")
    heading(d, "Cast it back", "to get a char.")
    cd(d, [
        [("char ", K), ("c = ", P), ("'a'", GREEN), (";", P)],
        [("", P)],
        [("(", P), ("char", K), (")(c + 1)  ", P), ("// ", C), ("b", GREEN)],
        [("c++;       ", P), ("// ", C), ("b", GREEN)],
        [("c += 1;    ", P), ("// ", C), ("c", GREEN)],
    ])
    muted(d, 920, ["++ and += cast for you.", "c = c + 1 would not compile."], size=42, gap=70)
    D.save()
    d = D.slide(4, "STRING TRAP")
    heading(d, "Order decides", "the output.")
    cd(d, [
        [("\"\"", GREEN), (" + ", P), ("'a'", GREEN), (" + ", P), ("'b'", GREEN), ("   ", P), ("// ", C), ("ab", GREEN)],
        [("", P)],
        [("'a'", GREEN), (" + ", P), ("'b'", GREEN), (" + ", P), ("\"\"", GREEN), ("   ", P), ("// ", C), ("195", RED)],
    ])
    muted(d, 790, ["Left to right: two chars add up", "as ints before the String."], size=42, gap=70)
    D.save()
    d = D.slide(5, "DIGIT TRICK")
    heading(d, "Char to number,", "the easy way.")
    cd(d, [
        [("'7'", GREEN), (" - ", P), ("'0'", GREEN), ("                   ", P), ("// ", C), ("7", GREEN)],
        [("Character.getNumericValue(", P)],
        [("    ", P), ("'7'", GREEN), (")      ", P), ("// ", C), ("7", GREEN)],
    ], size=28)
    muted(d, 790, ["Digits sit in order in Unicode,", "so subtracting '0' works."], size=42, gap=70)
    D.save()
    d = D.slide(6, "COMPARING")
    heading(d, "Chars compare", "by their codes.")
    cards(d, 480, [
        ("'a' < 'b'", "true, because 97 < 98"),
        ("'A' < 'a'", "true, because 65 < 97"),
        ("Loop a to z", "for (char c = 'a'; c <= 'z'; c++)"),
    ], h=170, gap=34, title_size=42, sub_size=28)
    D.save()
    recap(D, "char math", "in a nutshell.", ["char + int gives an int", "Cast back to get a char", "++ and += cast for you", "Concat order changes the result"])

elif which == "init":
    hook(D, "INTERVIEW", "Who runs", "first in", "Java?", "Class initialization order.")
    d = D.slide(2, "THE ORDER")
    heading(d, "Static first,", "then instance.")
    cards(d, 480, [
        ("1. Static blocks", "Parent first, then child. Once per class"),
        ("2. Instance blocks", "Run before the constructor body"),
        ("3. Constructor", "Parent constructor, then child"),
    ], h=170, gap=34, title_size=42, sub_size=28)
    D.save()
    d = D.slide(3, "THE CODE")
    heading(d, "Parent and", "child classes.")
    cd(d, [
        [("class ", K), ("A {", P)],
        [("  ", P), ("static ", K), ("{ p(", P), ("\"A static\"", GREEN), ("); }", P)],
        [("  { p(", P), ("\"A instance\"", GREEN), ("); }", P)],
        [("  A() { p(", P), ("\"A ctor\"", GREEN), ("); }", P)],
        [("}", P)],
        [("class ", K), ("B ", P), ("extends ", K), ("A { ", P), ("// ", C), ("same shape", C)],
    ], size=28)
    muted(d, 1040, ["B has the same three blocks.", "Then we run: new B();"], size=42, gap=70)
    D.save()
    d = D.slide(4, "THE OUTPUT")
    heading(d, "What does", "new B() print?")
    cd(d, [
        [("A static", GREEN)],
        [("B static", GREEN)],
        [("A instance", ORANGE)],
        [("A ctor", ORANGE)],
        [("B instance", BLUE)],
        [("B ctor", BLUE)],
    ], size=32)
    D.save()
    d = D.slide(5, "SECOND OBJECT")
    heading(d, "Static runs", "only once.")
    cd(d, [
        [("new ", K), ("B();  ", P), ("// ", C), ("2nd object", C)],
        [("", P)],
        [("A instance", ORANGE)],
        [("A ctor", ORANGE)],
        [("B instance", BLUE)],
        [("B ctor", BLUE)],
    ], size=30)
    muted(d, 1010, ["Static blocks do not run again.", "The class is already loaded."], size=42, gap=70)
    D.save()
    d = D.slide(6, "WATCH OUT")
    heading(d, "Avoid risky", "constructors.")
    cards(d, 480, [
        ("Overridable calls", "A parent constructor may call child code"),
        ("The child state", "Its fields are not set up yet"),
        ("Safer choice", "Call only private or final methods"),
    ], h=170, gap=34, title_size=42, sub_size=28)
    D.save()
    recap(D, "Init order", "in a nutshell.", ["Static blocks run once per class", "Parent runs before child", "Instance block, then constructor", "Do not call overridable methods"])

elif which == "pick":
    hook(D, "GIT", "Take one commit", "from another", "branch.", "git cherry-pick explained.")
    d = D.slide(2, "THE IDEA")
    heading(d, "Copy a commit,", "not the branch.")
    cards(d, 480, [
        ("Merge", "Brings in every commit of a branch"),
        ("Cherry-pick", "Copies just the commit you choose"),
        ("Result", "A new commit with a new hash"),
    ], h=170, gap=34, title_size=42, sub_size=28)
    D.save()
    d = D.slide(3, "BASIC USE")
    heading(d, "Switch, find,", "pick.")
    cd(d, [
        [("$ git switch main", P)],
        [("$ git log feature --oneline", P)],
        [("a1b2c3d fix login bug", GREEN)],
        [("$ git cherry-pick a1b2c3d", P)],
    ], size=30)
    muted(d, 900, ["The fix now lives on main.", "The rest of feature stays behind."], size=42, gap=70)
    D.save()
    d = D.slide(4, "USEFUL FLAGS")
    heading(d, "Three flags", "worth knowing.")
    cards(d, 480, [
        ("-x", "Adds the original hash to the message"),
        ("-n / --no-commit", "Applies changes without committing"),
        ("A..B", "Picks a range, A itself is excluded"),
    ], h=170, gap=34, title_size=42, sub_size=28)
    D.save()
    d = D.slide(5, "CONFLICTS")
    heading(d, "Conflict?", "Resolve, continue.")
    cd(d, [
        [("# fix the files, then:", C)],
        [("$ git add .", P)],
        [("$ git cherry-pick --continue", P)],
        [("", P)],
        [("# or give up:", C)],
        [("$ git cherry-pick --abort", RED)],
    ], size=30)
    D.save()
    d = D.slide(6, "WHEN TO USE")
    heading(d, "Great for", "hotfixes.")
    cards(d, 480, [
        ("Backport a fix", "Copy it to a release branch"),
        ("Wrong branch", "Move a commit you made by mistake"),
        ("Do not overuse", "Duplicate commits can confuse history"),
    ], h=170, gap=34, title_size=42, sub_size=28)
    D.save()
    recap(D, "cherry-pick", "in a nutshell.", ["Copies a single commit", "It gets a new hash", "Use -x to keep the origin", "Conflicts: continue or abort"])
