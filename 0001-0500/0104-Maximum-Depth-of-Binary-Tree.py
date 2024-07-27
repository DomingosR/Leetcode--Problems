class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        
        nodeQueue = deque()
        nodeQueue.appendleft((root, 1))
        maxLevel = 1
        
        while nodeQueue:
            currentNode, currentLevel = nodeQueue.pop()
            maxLevel = max(currentLevel, maxLevel)
            if currentNode.left:
                nodeQueue.appendleft((currentNode.left, currentLevel + 1))
            if currentNode.right:
                nodeQueue.appendleft((currentNode.right, currentLevel + 1))  
                
        return maxLevel