class PeekingIterator(object):
    def __init__(self, iterator):
        self.queue = deque()
        while iterator.hasNext():
            self.queue.appendleft(iterator.next())
        
    def peek(self):
        return self.queue[-1]

    def next(self):
        return self.queue.pop()

    def hasNext(self):
        return len(self.queue) > 0
