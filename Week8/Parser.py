"""Handles the parsing of a single .vm file, and encapsulates access to the
input code. It reads VM commands, parses them, and provides convenient access to
their components. In addition, it removes all white space and comments."""

lines = []    # contains the lines of the input file, no whitespace on left
current = -1  # indicates which command(line) is the curren one

def init(asmfile):
    """Opens the input file/stream and gets ready to parse it."""
    global lines
    fin = open(asmfile, 'r')
    for l in fin:
        if l.find("//") is not -1:
            l = l[:l.find("//")]
        l = l.replace("\t", " ")  # remove tabs
        while l.find("  ") is not -1:
            l = l.replace("  ", " ")   # remove spaces
        l = l.strip()
        l = l.replace("\n", "")  # remove new-lines
        l = l.replace("\r", "")  # remove carriage-returns
        if len(l) == 0:   # skip empty lines
            continue
        lines.append(l)
    fin.close()

def hasMoreCommands():
    """Are there more commands in the input?"""
    return current < len(lines) - 1

def advance():
    """Reads the next command from the input and makes it the current
    command. Should be called only if hasMoreCommands() is true.  Initially
    there is no current command."""
    global current
    current += 1

def commandType():
    """Returns the type of the current VM command.
    C_ARITHMETIC is returned for all the arithmetic
    commands.
    - "C_ARITHMETIC",
    - "C_PUSH",
    - "C_POP",
    - "C_LABEL",
    - "C_GOTO",
    - "C_IF",
    - "C_FUNCTION",
    - "C_RETURN",
    - "C_CALL"
    """
    l = lines[current]
    if l.startswith("push"):
        return "C_PUSH"
    if l.startswith("pop"):
        return "C_POP"
    if l.startswith("label"):
        return "C_LABEL"
    if l.startswith("goto"):
        return "C_GOTO"
    if l.startswith("if-goto"):
        return "C_IF"
    if l.startswith("function"):
        return "C_FUNCTION"
    if l.startswith("return"):
        return "C_RETURN"
    if l.startswith("call"):
        return "C_CALL"
    return "C_ARITHMETIC"

def arg1():
    """Returns the first arg. of the current command.  In the case of
    C_ARITHMETIC, the command itself (add, sub, etc.) is returned. Should not be
    called if the current command is C_RETURN."""
    l = lines[current]
    splits = l.split(" ")
    if len(splits) > 1:
        return splits[1]

def arg2():
    """Returns the second argument of the current command. Should be called only
    if the current command is C_PUSH, C_POP, C_FUNCTION, or C_CALL."""
    l = lines[current]
    splits = l.split(" ")
    if len(splits) > 2:
        return int(splits[2])
