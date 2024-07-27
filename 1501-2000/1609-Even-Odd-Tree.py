class Solution(object):
    def isEvenOddTree(self, root):
        def sign(num):
            if num == 0:
                return 0
            return 1 if num > 0 else -1
        
        prevLevel, prevVal = -1, 0
        nodeQueue = deque()
        nodeQueue.appendleft((root, 0))
        
        while nodeQueue:
            currNode, currLevel = nodeQueue.pop()
            if (currNode.val - currLevel) % 2 == 0:
                return False
            if currLevel == prevLevel:
                if (currNode.val - prevVal) * (1 if currLevel % 2 == 0 else -1) <= 0:
                    return False
            prevLevel, prevVal = currLevel, currNode.val
            if currNode.left:
                nodeQueue.appendleft((currNode.left, currLevel + 1))
            if currNode.right:
                nodeQueue.appendleft((currNode.right, currLevel + 1))
            
        return True