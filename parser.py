from lexer import LEXER

lex = 0

class PARSER(object):
    def __init__(self,filename):
        global lex
        lex = LEXER(filename)
        self.token_list = lex.tokenizer()
        self.token_pointer = -1
        
        #contar si hay la misma cantidad de token de loop
        self.open_loop_counter = 0
        self.close_loop_counter = 0

    def get_next_token(self):
        self.token_pointer+=1
        if self.token_pointer < len( self.token_list ):
            return [True,self.token_list[self.token_pointer]]
        else:
            return [False,[]]
    
    def seek_token(self):
        temp = self.token_pointer+1
        if temp < len( self.token_list ):
            return [True,self.token_list[temp]]
        else:
            return[False,[]]
    
    def parse_check(self):
        if self.program():
            return True
        else:
            return False
    
    def program(self):
        seek = self.seek_token()
        if seek[0]:
            while True:
                seek = self.seek_token()
                if seek[0] and seek[1].token == '[':
                    self.open_loop()
                elif seek[0] and seek[1].token == ']':
                    self.close_loop()
                elif seek[0]:
                    if not self.operator():
                        return False
                else:
                    break
            # despues verifica que coincidan los numeros de loop
            if self.open_loop_counter == self.close_loop_counter:
                return True
            else:
                return False
        else:
            return True

    def operator(self):
        token = self.get_next_token()
        if token[1].token == '+':
            return True
        elif token[1].token == '-':
            return True
        elif token[1].token == '<':
            return True
        elif token[1].token == '>':
            return True
        elif token[1].token == '.':
            return True
        elif token[1].token == ',':
            return True
        else:
            return False
    
    def open_loop(self):
        self.get_next_token()
        self.open_loop_counter+=1
        return True
    
    def close_loop(self):
        self.get_next_token()
        self.close_loop_counter+=1
        return True
