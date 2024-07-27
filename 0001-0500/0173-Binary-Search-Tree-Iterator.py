class BSTIterator(object):

    def __init__(self, root):
        self.queue = deque()
        
        def processNode(node):
            if node.left:
                processNode(node.left)
            
            self.queue.appendleft(node.val)
            
            if node.right:
                processNode(node.right)
                
        processNode(root)

    def next(self):
        return self.queue.pop()
        

    def hasNext(self):
        return len(self.queue) > 0