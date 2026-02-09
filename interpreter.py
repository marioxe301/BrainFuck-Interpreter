from lexer import LEXER
import sys
from stack import STACK

lex = None


class INTERPRETER(object):
    def __init__(
        self, filename=None, text=None, input_provider=None, output_writer=None
    ):
        global lex
        lex = LEXER(file=filename, text=text)
        self.token_pointer = -1

        self.token_list = lex.tokenizer()
        self.memory = [0]
        self.memory_pointer = 0

        self.loop_pointer_stack = STACK()
        self.input_provider = input_provider or input
        self.output_writer = output_writer or sys.stdout.write

    def get_token(self):
        self.token_pointer += 1
        if self.token_pointer < len(self.token_list):
            return [True, self.token_list[self.token_pointer]]
        else:
            return [False, []]

    def execute(self):
        while True:
            token = self.get_token()
            if not token[0]:
                break
            else:
                self.dispatch_action(token[1].tag)

    def dispatch_action(self, token):
        if token == "ADD":
            self.add()
        elif token == "SUB":
            self.substract()
        elif token == "INC":
            self.move_memory_increment()
        elif token == "DEC":
            self.move_memory_decrement()
        elif token == "IN":
            self.memory[self.memory_pointer] = self.read_input_char()
        elif token == "OUT":
            self.output_writer(chr(self.memory[self.memory_pointer]))
        elif token == "SL":
            self.loop_pointer_stack.push(self.token_pointer)
            self.execute_loop()

    def read_input_char(self):
        value = self.input_provider()
        if value is None:
            return 0
        if isinstance(value, int):
            return value
        if not isinstance(value, str):
            value = str(value)
        if value == "":
            return 0
        return ord(value[0])

    def move_memory_decrement(self):
        if self.memory_pointer != 0:
            self.memory_pointer -= 1

    def move_memory_increment(self):
        if self.memory_pointer + 1 < (len(self.memory) - 1):
            self.memory_pointer += 1
        else:
            self.memory.append(0)
            self.memory_pointer += 1

    def substract(self):
        if self.memory[self.memory_pointer] != 0:
            self.memory[self.memory_pointer] -= 1

    def add(self):
        if self.memory[self.memory_pointer] < 256:
            self.memory[self.memory_pointer] += 1

    def execute_loop(self):
        while True:
            token = self.get_token()
            if token[1].tag == "EL":
                if self.memory[self.memory_pointer] == 0:
                    self.loop_pointer_stack.pop()
                    if self.loop_pointer_stack.is_Empty():
                        break
                    else:
                        continue
                else:
                    self.jump()
            else:
                self.dispatch_action(token[1].tag)

    def jump(self):
        self.token_pointer = self.loop_pointer_stack.top()
