class Solution(object):
    def findBottomLeftValue(self, root):
        nodeQueue = deque()
        nodeQueue.appendleft((root, 0))
        level, leftVal = -1, 0

        while nodeQueue:
            currNode, currLevel = nodeQueue.pop()
            if currLevel != level:
                level = currLevel
                leftVal = currNode.val
            if currNode.left:
                nodeQueue.appendleft((currNode.left, currLevel + 1))
            if currNode.right:
                nodeQueue.appendleft((currNode.right, currLevel + 1))

        return leftVal
