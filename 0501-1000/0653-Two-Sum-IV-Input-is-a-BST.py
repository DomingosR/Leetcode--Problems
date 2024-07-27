class Solution(object):
    def findTarget(self, root, k):
        if not root: 
            return False
        
        nodeQueue = deque()
        nodeQueue.appendleft(root)
        values = set()

        while nodeQueue:
            currentNode = nodeQueue.pop()
            if k - currentNode.val in values:
                return True
            
            values.add(currentNode.val)

            if currentNode.left:
                nodeQueue.appendleft(currentNode.left)
            if currentNode.right:
                nodeQueue.appendleft(currentNode.right)
        
        return False
