import Parser
import Code
import SymbolTable

Parser.init("Pong.asm")

symAddress = 16

def toBinary(decNum):
	num = int(decNum)
	ans = ""
	while(num > 0):
		ans = str(num % 2) + ans
		num = num / 2

	return ans

while Parser.hasMoreCommands():
	Parser.advance()
	if Parser.commandType() is "L_COMMAND":
		SymbolTable.addEntry(Parser.symbol(),Parser.current)
		Parser.lines.pop(Parser.current)
		Parser.current-=1

Parser.current = -1

while Parser.hasMoreCommands():
    Parser.advance()
    if Parser.commandType() is "A_COMMAND":
        if Parser.symbol().isdigit():
        	bin = toBinary(Parser.symbol())
        	print "0" * (16-len(bin)) + bin
        else:
        	if SymbolTable.contains(Parser.symbol()):
        		bin = toBinary(SymbolTable.getAddress(Parser.symbol()))
        		print "0" * (16-len(bin)) + bin
        	else:
        		SymbolTable.addEntry(Parser.symbol(),symAddress)
        		bin = toBinary(symAddress)
        		print "0" * (16-len(bin)) + bin
        		symAddress+=1
        		
    elif Parser.commandType() is "C_COMMAND":
        print "111" + Code.comp(Parser.comp()) + Code.dest(Parser.dest()) + Code.jump(Parser.jump())
  

