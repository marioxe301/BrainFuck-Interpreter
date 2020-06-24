from lexer import LEXER

lex = None
class INTERPRETER(object):
    def __init__(self,filename):
        global lex
        lex = LEXER(filename)
        self.token_pointer = -1

        self.token_list = lex.tokenizer()
        self.memory = [0]
        self.memory_pointer = 0

        self.loop_pointer_stack = []
    
    def get_token(self):
        self.token_pointer+=1
        if self.token_pointer < len( self.token_list ):
            return [True,self.token_list[self.token_pointer]]
        else:
            return [False,[]]
    
    def execute(self):
        while True:
            token = self.get_token()
            if not token[0]:
                break
            else:
                self.dispatch_action(token[1].tag)

    def dispatch_action(self,token):
        if token == 'ADD':
            self.add()
        elif token == 'SUB':
            self.substract()
        elif token == 'INC':
            self.move_memory_increment()
        elif token == 'DEC':
            self.move_memory_decrement()
        elif token == 'IN':
            self.memory[self.memory_pointer] = ord(input())
        elif token == 'OUT':
            print(chr( self.memory[self.memory_pointer]))
    
    def move_memory_decrement(self):
        if self.memory_pointer != 0:
            self.memory_pointer-=1

    def move_memory_increment(self):
        if self.memory_pointer + 1 < (len( self.memory ) - 1):
            self.memory_pointer+=1
        else:
            self.memory.append(0)
            self.memory_pointer+=1
        
    def substract(self):
        if self.memory[self.memory_pointer] !=0:
            self.memory[self.memory_pointer]-=1

    def add(self):
        if self.memory[self.memory_pointer] < 256:
            self.memory[self.memory_pointer]+=1