class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        
        nodeQueue = deque()
        nodeQueue.appendleft(root)
        currentLevel = 1

        while nodeQueue:
            for _ in range(len(nodeQueue)):
                nextNode = nodeQueue.pop()
                if not (nextNode.left or nextNode.right):
                    return currentLevel
                if nextNode.left:
                    nodeQueue.appendleft(nextNode.left)
                if nextNode.right:
                    nodeQueue.appendleft(nextNode.right)

            currentLevel += 1