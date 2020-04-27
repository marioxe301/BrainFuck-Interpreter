from lexer import LEXER
from parser import PARSER
import sys

def main():
    if len(sys.argv)== 2:
       lexer = LEXER(sys.argv[1])
       lexer.tokenizer()
       lexer.print_tokens() 
    elif len(sys.argv) > 2:
        print("Varios argumentos detectados, especifque solo un archivo")
        sys.exit()
    else:
        print("Especifique el archivo")
        sys.exit()
    pass




if __name__ == "__main__":
    main()