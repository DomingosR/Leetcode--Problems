class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        maxDepth = 0
        nodeQueue = deque()
        nodeQueue.appendleft((root, 1))

        while nodeQueue:
            currentNode, currentDepth = nodeQueue.pop()
            maxDepth = max(maxDepth, currentDepth)
            for nextNode in currentNode.children:
                nodeQueue.appendleft((nextNode, currentDepth + 1))
        
        return maxDepth