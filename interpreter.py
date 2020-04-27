import sys
class Interpreter(object):
    def __init__(self,tokens):
        self.token_list = tokens
        self.token_pointer = 0
        self.loop_pointer = []

        #variable para el interprete
        self.pointer = 0
        self.memory = [0]
    
    def verify_loop(self):
        if self.memory[self.pointer] == 0:
            return False
        else:
            return True

    def move_memory(self,token):
        if token == 'INC':
            #incrementar el puntero
            self.pointer+=1
            # si el puntero mayor al tamaño del arreglo se le agrega memoria ( memoria dinamica )
            if self.pointer >= len( self.token_list):
                self.memory.append(0)
            else:
                pass
        elif token == 'DEC':
            #decrementar el puntero
            self.pointer-=1
            if self.pointer <= -1:
                print("Error al acceder a memoria")
                sys.exit()
            else:
                pass
        else:
            pass

    def dispatch_action(self,token):
        if token == 'ADD':
            self.memory[self.pointer]+=1
        elif token == 'SUB':
            self.memory[self.pointer]-=1
        elif token == 'INC':
            self.move_memory(token)
        elif token == 'DEC':
            self.move_memory(token)
        elif token == 'OUT':
            print(chr(self.memory[self.pointer]))
        elif token == 'IN':
            try:
                self.memory[self.pointer] = ord(input())
            except:
                print('Input invalido, solo se acepta input de tamaño 1')
                sys.exit()
        elif token == 'SL':
            pass
        elif token == 'EL':
            pass
        else:
            pass

    def get_token(self):
        pass

    