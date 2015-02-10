"""Translates VM commands into Hack assembly code."""
SP = 0
LCL = 1
ARG = 2
THIS = 3
THAT = 4
TEMP = 5
GP = 13

STATIC = 16
POINTER = 3

f = None
labelCount = 0
currentFunction = "null"

def init(outputFile):
    """Opens the output file/stream and gets ready to write into it."""
    global f
    f = open(outputFile, "w")

def setFileName(fileName):
    """Informs the code writer that the translation of a new VM file is
    started."""
    # implement me

def writeArithmetic(command):
    """Writes the assembly code that is the translation of the given arithmetic
    command."""
    if command in ["neg", "not"]:
        writeUnary(command)
    if command in ["eq", "gt", "lt"]:
        writeBranch(command)
    if command in ["add", "sub", "and", "or"]:
        writeBinary(command)

def WritePushPop(command, segment, index):
    """Writes the assembly code that is the translation of the given command,
    where command is either C_PUSH or C_POP."""
    if command == "C_PUSH":
        if segment in ["constant", "static", "pointer", "temp"]:
            writeStaticPush(segment, index)
        if segment in ["local", "this", "that", "argument"]:
            writeMemoryPush(segment, index)

    if command == "C_POP":
        if segment in ["static", "pointer", "temp"]:
            writeStaticPop(segment, index)
        if segment in ["local", "this", "that", "argument"]:
            writeMemoryPop(segment, index)

def writeInit():
    """Writes the assembly code that effects the VM initialization, also called
    bootstrap code. This code must be placed at the beginning of the output
    file."""
    # implement me
    f.write("@"+ str(SP)+"\n")
    f.write("M=256\n")
    writeCall("Sys.init")

def writeLabel(label):
    """Writes the assembly code that is the translation of the label command."""
    f.write("(" + currentFunction + "$" + label + ")\n")

def writeGoto(label):
    """Writes the assembly code that is the translation of the goto command."""
    f.write("@"+ currentFunction + "$" + label + ")\n")
    f.write("0;JMP\n")

def writeIf(label):
    """Writes the assembly code that is the translation of the if-goto command."""
    f.write("@" + str(SP) + "\n")
    f.write("M=M-1\n")
    f.write("A=M\n")
    f.write("D=M\n")
    f.write("@"+ currentFunction + "$"+ label+"\n")
    f.write("D;JNE\n")

def writeCall(functionName, numArgs):
    """Writes the assembly code that is the translation of the call command."""


def writeReturn():
    """Writes the assembly code that is the translation of the return
    command."""
    # implement me

def writeFunction(functionName, numLocals):
    """Writes the assembly code is the translation of the given function
    command."""
    # implement me


def close():
    """Closes the output file."""
    f.close()

# Dirty Little Helpers

def nextLabel():
    global labelCount
    res = "__LABEL." + str(labelCount)
    labelCount += 1
    return res

def writeBinary(command):
    f.write("@" + str(SP) + "\n")
    f.write("M = M - 1\n")
    f.write("A = M\n")
    f.write("D = M\n")
    f.write("@" + str(SP) + "\n")
    f.write("M = M - 1\n")
    f.write("A = M\n")
    if command == "add":
        f.write("M = M + D\n")
    if command == "sub":
        f.write("M = M - D\n")
    if command == "and":
        f.write("M = M & D\n")
    if command == "or":
        f.write("M = M | D\n")
    f.write("@" + str(SP) + "\n")
    f.write("M = M + 1\n")

def writeUnary(command):
    f.write("@" + str(SP) + "\n")
    f.write("M = M - 1\n")
    f.write("A = M\n")
    if command == "neg":
        f.write("M = -M\n")
    if command == "not":
        f.write("M = !M\n")
    f.write("@" + str(SP) + "\n")
    f.write("M = M + 1\n")

def writeBranch(command):
    f.write("@" + str(SP) + "\n")
    f.write("M = M - 1\n")
    f.write("A = M\n")
    f.write("D = M\n")
    f.write("@" + str(SP) + "\n")
    f.write("M = M - 1\n")
    f.write("A = M\n")
    f.write("D = M - D\n")
    branchLabel = nextLabel()
    f.write("@" + branchLabel + "\n")
    if command == "eq":
        f.write("D;JEQ\n")
    if command == "gt":
        f.write("D;JGT\n")
    if command == "lt":
        f.write("D;JLT\n")
    f.write("@0\n")
    f.write("D = A\n")
    f.write("@" + str(SP) + "\n")
    f.write("A = M\n")
    f.write("M = D\n")
    f.write("@" + str(LCL) + "\n");
    endLabel = nextLabel()
    f.write("@" + endLabel + "\n")
    f.write("0;JMP\n")
    f.write("(" + branchLabel + ")\n")
    f.write("D = -1\n")
    f.write("@" + str(SP) + "\n")
    f.write("A = M\n")
    f.write("M = D\n")
    f.write("(" + endLabel + ")\n")
    f.write("@" + str(SP) + "\n")
    f.write("M = M + 1\n")

def writeMemoryPush(segment, index):
    if segment == "local":
        f.write("@" + str(LCL) + "\n");
    if segment == "argument":
        f.write("@" + str(ARG) + "\n");
    if segment == "this":
        f.write("@" + str(THIS) + "\n");
    if segment == "that":
        f.write("@" + str(THAT) + "\n");
    f.write("D = M\n")
    f.write("@" + str(index) + "\n");
    f.write("A = D + A\n")
    f.write("D = M\n")
    f.write("@" + str(SP) + "\n")
    f.write("A = M\n")
    f.write("M = D\n")
    f.write("@" + str(SP) + "\n")
    f.write("M = M + 1\n")

def writeMemoryPop(segment, index):
    if segment == "local":
        f.write("@" + str(LCL) + "\n");
    if segment == "argument":
        f.write("@" + str(ARG) + "\n");
    if segment == "this":
        f.write("@" + str(THIS) + "\n");
    if segment == "that":
        f.write("@" + str(THAT) + "\n");
    f.write("D = M\n")
    f.write("@" + str(index) + "\n");
    f.write("D = D + A\n")
    f.write("@" + str(GP) + "\n");
    f.write("M = D\n")
    f.write("@" + str(SP) + "\n")
    f.write("M = M - 1\n")
    f.write("A = M\n")
    f.write("D = M\n")
    f.write("@" + str(GP) + "\n");
    f.write("A = M\n")
    f.write("M = D\n")

def writeStaticPush(segment, index):
    if segment == "constant":
        f.write("@" + str(index) + "\n")
        f.write("D = A\n")
    if segment == "static":
        f.write("@" + str(STATIC + index) + "\n")
        f.write("D = M\n")
    if segment == "pointer":
        f.write("@" + str(POINTER + index) + "\n")
        f.write("D = M\n")
    if segment == "temp":
        f.write("@" + str(TEMP + index) + "\n")
        f.write("D = M\n")
    f.write("@" + str(SP) + "\n")
    f.write("A = M\n")
    f.write("M = D\n")
    f.write("@" + str(SP) + "\n")
    f.write("M = M + 1\n")

def writeStaticPop(segment, index):
    f.write("@" + str(SP) + "\n")
    f.write("M = M - 1\n")
    f.write("A = M\n")
    f.write("D = M\n")
    if segment == "static":
        f.write("@" + str(STATIC + index) + "\n")
    if segment == "pointer":
        f.write("@" + str(POINTER + index) + "\n")
    if segment == "temp":
        f.write("@" + str(TEMP + index) + "\n")
    f.write("M = D\n")
