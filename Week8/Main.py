import Parser
import CodeWriter

Parser.init("Prog.vm")
CodeWriter.init("Prog.asm")

while Parser.hasMoreCommands():
    Parser.advance()
    cmd = Parser.commandType()
    if cmd is "C_ARITHMETIC":
        CodeWriter.writeArithmetic(Parser.lines[Parser.current])
    elif cmd is "C_LABEL":
    	CodeWriter.writeLabel(Parser.arg1())
    elif cmd is "C_GOTO":
    	CodeWriter.writeGoto(Parser.arg1())
    elif cmd is "C_IF":
    	CodeWriter.writeIf(Parser.arg1())
    elif cmd is "C_FUNCTION":
    	CodeWriter.writeFunction(Parser.arg1(),Parser.arg2())
    elif cmd is "C_RETURN":
    	CodeWriter.writeReturn()
    elif cmd is "C_CALL":
    	CodeWriter.writeCall(Paser.arg1(),Parser.arg2())
    else:
        CodeWriter.WritePushPop(cmd, Parser.arg1(), Parser.arg2())

CodeWriter.close()
