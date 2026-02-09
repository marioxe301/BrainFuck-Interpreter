from lexer import LEXER
from parser import PARSER
from interpreter import INTERPRETER
import sys


def main():
    if len(sys.argv) == 2:
        parser = PARSER(sys.argv[1])
        if parser.parse_check():
            code = INTERPRETER(sys.argv[1])
            code.execute()
        else:
            print("Invalid Brainfuck syntax")
    elif len(sys.argv) > 2:
        print("Too many arguments. Provide a single file.")
        sys.exit()
    else:
        print("Please provide a Brainfuck file.")
        sys.exit()


if __name__ == "__main__":
    main()
