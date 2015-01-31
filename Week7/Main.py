import Parser
import CodeWriter

Parser.init("Prog.vm")
CodeWriter.init("Prog.asm")

CodeWriter.WritePushPop("push","constant","1")

while Parser.hasMoreCommands():
    Parser.advance()

    ##print Parser.lines[Parser.current] + " = " + Parser.commandType(), Parser.arg1(), Parser.arg2()

    cmd = Parser.commandType()
    if cmd is "C_ARITHMETIC":
        CodeWriter.writeArithmetic(Parser.lines[Parser.current])
    else:
        CodeWriter.WritePushPop(cmd, Parser.arg1(), Parser.arg2())

CodeWriter.close()
