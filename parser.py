
class PARSER(object):
    def __init__(self, tokens):
        self.token_list = tokens
        self.pointer = 0
        self.loop_pointer = 0

    def get_token(self):
        if self.pointer < len(self.token_list):
            token = self.token_list[self.pointer]
            self.pointer+=1
            return token
        else:
            pass
    