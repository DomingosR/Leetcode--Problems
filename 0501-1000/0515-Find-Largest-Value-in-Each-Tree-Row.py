class Solution(object):
    def largestValues(self, root):
        if not root:
            return []

        maxRowVal = []
        nodeQueue = deque()
        nodeQueue.appendleft(root)

        while nodeQueue:
            n = len(nodeQueue)
            maxVal = - 2**31 - 1
            for i in range(n):
                currNode = nodeQueue.pop()
                maxVal = max(maxVal, currNode.val)
                if currNode.left:
                    nodeQueue.appendleft(currNode.left)
                if currNode.right:
                    nodeQueue.appendleft(currNode.right)
            maxRowVal += [maxVal]

        return maxRowVal
