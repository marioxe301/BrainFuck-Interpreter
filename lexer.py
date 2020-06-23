from pyparsing import ( 
White, Literal, ZeroOrMore, OneOrMore
,Suppress,printables, Combine, Word, alphanums, Forward)
import sys
from tokens import TOKENS

#Constants
ADD = Literal('+') # increment (increase by one) the byte at the data pointer. 
SUB = Literal('-') # decrement (decrease by one) the byte at the data pointer. 
INCP = Literal('>')# increment the data pointer (to point to the next cell to the right). 
DECP = Literal('<')# decrement the data pointer (to point to the next cell to the left). 
INPUT = Literal(',')# accept one byte of input, storing its value in the byte at the data pointer. 
OUTPUT = Literal('.')# output the byte at the data pointer. 
OPEN_LOOP = Literal('[') # if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command.
CLOSE_LOOP = Literal(']') # if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command.
COMMENTS = Combine(Word(printables) + White(ws='\n') | Word(printables))

program = ZeroOrMore( ADD | SUB | INCP | DECP | INPUT | OUTPUT | OPEN_LOOP | CLOSE_LOOP | Suppress(COMMENTS))

class LEXER(object):
    def __init__(self,file):
        self.path = file
        self.token_list = []

    def tokenize_file(self):
        try:
            
            return program.parseFile(self.path)
        except:
            print("AN ERROR HAS OCCURRED")    
            sys.exit()
    
    def tag_token(self,token):
        if token == '+':
            return 'ADD'
        elif token=='-':
            return 'SUB'
        elif token=='>':
            return 'INC'
        elif token=='<':
            return 'DEC'
        elif token=='.':
            return 'OUT'
        elif token==',':
            return 'IN'
        elif token=='[':
            return 'SL'
        elif token==']':
            return 'EL'
        else:
            return

    def tokenizer(self):
        token_list = self.tokenize_file()
        for token in token_list:
            tag = self.tag_token(token)
            self.token_list.append(TOKENS(tag,token))
        return self.token_list
    
    def print_tokens(self):
        for token in self.token_list:
            print("TAG:",token.tag," ","TOKEN:",token.token,"\n")