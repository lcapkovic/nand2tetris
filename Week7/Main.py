import Parser
import CodeWriter

Parser.init("Prog.vm")
CodeWriter.init("Prog.asm")

while Parser.hasMoreCommands():
    Parser.advance()
    cmd = Parser.commandType()
    if cmd is "C_ARITHMETIC":
        CodeWriter.writeArithmetic(Parser.lines[Parser.current])
    else:
        CodeWriter.WritePushPop(cmd, Parser.arg1(), Parser.arg2())

CodeWriter.close()
