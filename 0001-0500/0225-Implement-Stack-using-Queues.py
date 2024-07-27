class MyStack(object):
    
    def __init__(self):
        self.numQueue = deque()
        self.numCount = 0    

    def push(self, x):
        self.numQueue.appendleft(x)
        self.numCount += 1

    def pop(self):
        for i in range(self.numCount - 1):
            self.numQueue.appendleft(self.numQueue.pop())
        self.numCount -= 1
        return self.numQueue.pop()
        
    def top(self):
        for i in range(self.numCount - 1):
            self.numQueue.appendleft(self.numQueue.pop())
        topVal = self.numQueue[-1]
        self.numQueue.appendleft(self.numQueue.pop())
        return topVal

    def empty(self):
        return self.numCount == 0