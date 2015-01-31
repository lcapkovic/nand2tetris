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
    # implement me

def WritePushPop(command, segment, index):
    """Writes the assembly code that is the translation of the given command,
    where command is either C_PUSH or C_POP."""
    # implement me

def close():
    """Closes the output file."""
    f.close()
