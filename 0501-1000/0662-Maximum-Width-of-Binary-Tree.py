class Solution(object):
    def widthOfBinaryTree(self, root):
        maxWidth = 1
        nodeQueue = deque()
        nodeQueue.appendleft((root, 1))
        
        while nodeQueue:
            n = len(nodeQueue)
            leftVal = nodeQueue[-1][1]
            for i in range(n):
                currNode, currIndex = nodeQueue.pop()
                if currNode.left:
                    nodeQueue.appendleft((currNode.left, 2 * currIndex))
                if currNode.right:
                    nodeQueue.appendleft((currNode.right, 2 * currIndex + 1))
            rightVal = currIndex
            maxWidth = max(maxWidth, rightVal - leftVal + 1)
        
        return maxWidth