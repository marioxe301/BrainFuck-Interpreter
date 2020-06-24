
class STACK(object):
    def __init__(self):
        self.stack = []
    
    def is_Empty(self):
        if len( self.stack ) == 0:
            return True
        return False
    
    def push(self,element):
        self.stack.append(element)
    
    def pop(self):
        if not self.is_Empty():
            self.stack.pop()
    
    def top(self):
        if not self.is_Empty():
            return self.stack[-1]
        