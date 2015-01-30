"""Encapsulates access to the input code. Reads an assembly language
command, parses it, and provides convenient access to the command's
components (fields and symbols). In addition, removes all white space and
comments."""

lines = []    # contains the lines of the input file, no whitespace on left
current = -1  # indicates which command(line) is the curren one

def init(asmfile):
    """Opens the input file/stream and gets ready to parse it."""
    global lines
    fin = open(asmfile, 'r')
    for l in fin:
        if l.find("//") is not -1:
            l=l[:l.find("//")]
        l = l.replace(" ", "")   # remove spaces
        l = l.replace("\t", "")  # remove tabs
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
    """Returns the type of the current command:
    - "A_COMMAND" for @Xxx where Xxx is either a symbol or a decimal number
    - "C_COMMAND" for dest=comp;jump
    - "L_COMMAND" (actually, pseudo-command) for (Xxx) where Xxx is a
    symbol."""

    if lines[current].startswith('@'):
        return "A_COMMAND"
    if lines[current].startswith('('):
        return "L_COMMAND"
    return "C_COMMAND"

def symbol():
    """Returns the symbol or decimal Xxx of the current command @Xxx or
    (Xxx). Should be called only when commandType() is A_COMMAND or
    L_COMMAND."""

    if commandType() == "A_COMMAND":
        return lines[current][1:]
    if commandType() == "L_COMMAND":
        return lines[current][1:-1]

def dest():
    """Returns the dest mnemonic in the current C-command (8
    possibilities).Should be called only when commandType() is
    C_COMMAND."""

    if '=' in lines[current]:
        return lines[current].split("=")[0]
    return "null"

def comp():
    """Returns the comp mnemonic in the current C-command (28
    possibilities). Should be called only when commandType() is
    C_COMMAND."""

    if dest() == "null":
        return lines[current].split(';')[0]
    return lines[current].split(';')[0].split('=')[1]

def jump():
    """Returns the jump mnemonic in the current C-command (8
    possibilities). Should be called only when commandType() is
    C_COMMAND."""

    if commandType() == "C_COMMAND" and ';' in lines[current]:
        return lines[current].split(';')[-1]
    return "null"