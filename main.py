from lexer import LEXER
from parser import PARSER
from interpreter import INTERPRETER
import sys

def main():
    if len(sys.argv)== 2:
       parser = PARSER(sys.argv[1])
       if parser.parse_check():
            code = INTERPRETER(sys.argv[1])
            code.execute()
       else:
            print("Verifique la gramatica")
    elif len(sys.argv) > 2:
        print("Varios argumentos detectados, especifque solo un archivo")
        sys.exit()
    else:
        print("Especifique el archivo")
        sys.exit()

if __name__ == "__main__":
    main()