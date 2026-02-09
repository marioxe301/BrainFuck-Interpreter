from interpreter import INTERPRETER
from parser import PARSER


def build_input_provider(input_text):
    iterator = iter(input_text)

    def provider():
        try:
            return next(iterator)
        except StopIteration:
            return "\x00"

    return provider


def validate_code(code_text):
    parser = PARSER(text=code_text)
    return parser.parse_check()


def run_code(code_text, input_text=""):
    if not validate_code(code_text):
        return {"success": False, "error": "Invalid Brainfuck syntax"}

    output_buffer = []
    interpreter = INTERPRETER(
        text=code_text,
        input_provider=build_input_provider(input_text),
        output_writer=output_buffer.append,
    )
    interpreter.execute()
    return {"success": True, "output": "".join(output_buffer)}
