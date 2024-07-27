class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))
        
    def pop(self):
        return self.stack.pop()[0]
        
    def top(self):
        return self.stack[-1][0]
        
    def getMin(self):
        return self.stack[-1][1]