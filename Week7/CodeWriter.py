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

def init(outputFile):
    """Opens the output file/stream and gets ready to write into it."""
    global f
    f = open(outputFile, "w")

def setFileName(fileName):
    """Informs the code writer that the translation of a new VM file is
    started."""
    # do not implement me

def writeArithmetic(command):
    """Writes the assembly code that is the translation of the given arithmetic
    command."""
    if command == "eq":
        f.write("@0\n")
        f.write("M=M-1\n")
        f.write("A=M\n")
        f.write("D=M\n")
        f.write("@0\n")
        f.write("M=M-1\n")
        f.write("A=M\n")
        f.write("D=D-M\n")
        f.write("@LABEL1\n")
        f.write("D;JEQ\n")
        f.write("@0\n")
        f.write("A=M\n")
        f.write("M=0\n")
        f.write("@LABEL2\n")
        f.write("0;JMP\n")
        f.write("(LABEL1)\n")
        f.write("@0\n")
        f.write("A=M\n")
        f.write("M=-1\n")
        f.write("(LABEL2)\n")
        f.write("@0\n")
        f.write("M=M+1\n")
    elif command == "lt":
        f.write("@0\n")
        f.write("M=M-1\n")
        f.write("A=M\n")
        f.write("D=M\n")
        f.write("@0\n")
        f.write("M=M-1\n")
        f.write("A=M\n")
        f.write("D=D-M\n")
        f.write("@LABEL1\n")
        f.write("D;JGT\n")
        f.write("@0\n")
        f.write("A=M\n")
        f.write("M=0\n")
        f.write("@LABEL2\n")
        f.write("0;JMP\n")
        f.write("(LABEL1)\n")
        f.write("@0\n")
        f.write("A=M\n")
        f.write("M=-1\n")
        f.write("(LABEL2)\n")
        f.write("@0\n")
        f.write("M=M+1\n")     
    elif command == "gt":
        f.write("@0\n")
        f.write("M=M-1\n")
        f.write("A=M\n")
        f.write("D=M\n")
        f.write("@0\n")
        f.write("M=M-1\n")
        f.write("A=M\n")
        f.write("D=D-M\n")
        f.write("@LABEL1\n")
        f.write("D;JLT\n")
        f.write("@0\n")
        f.write("A=M\n")
        f.write("M=0\n")
        f.write("@LABEL2\n")
        f.write("0;JMP\n")
        f.write("(LABEL1)\n")
        f.write("@0\n")
        f.write("A=M\n")
        f.write("M=-1\n")
        f.write("(LABEL2)\n")
        f.write("@0\n")
        f.write("M=M+1\n")
    elif command == "add":
        f.write("@0\n")
        f.write("M=M-1\n")
        f.write("A=M\n")
        f.write("D=M\n")
        f.write("A=A-1\n")
        f.write("M=M+D\n")
    elif command == "sub":
        f.write("@0\n")
        f.write("M=M-1\n")
        f.write("A=M\n")
        f.write("D=M\n")
        f.write("A=A-1\n")
        f.write("M=M-D\n")    
    elif command == "neg":
        f.write("@0\n")
        f.write("A=M-1\n")
        f.write("M=-M\n")
    elif command == "and":
        f.write("@0\n")
        f.write("M=M-1\n")
        f.write("A=M\n")
        f.write("D=M\n")
        f.write("A=A-1\n")
        f.write("M=D&M\n")
    elif command == "or":
        f.write("@0\n")
        f.write("M=M-1\n")
        f.write("A=M\n")
        f.write("D=M\n")
        f.write("A=A-1\n")
        f.write("M=D|M\n")
    elif command == "not":
        f.write("@0\n")
        f.write("A=M-1\n")
        f.write("M=!M\n")

def WritePushPop(command, segment, index):
    """Writes the assembly code that is the translation of the given command,
    where command is either C_PUSH or C_POP."""
    if command == "C_PUSH":
        if segment == "constant":
            f.write("@" + str(index) + "\n")
            f.write("D=A\n")
            f.write("@0\n")
            f.write("A=M\n")
            f.write("M=D\n")
            f.write("@0\n")
            f.write("M=M+1\n")


def close():
    """Closes the output file."""
    f.close()
