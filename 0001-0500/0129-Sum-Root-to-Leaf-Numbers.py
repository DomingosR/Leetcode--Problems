class Solution(object):
    def sumNumbers(self, root):
        totalSum = 0
        nodeQueue = deque()
        nodeQueue.appendleft((root, root.val))
        
        while nodeQueue:
            currNode, currVal = nodeQueue.pop()
            
            if not (currNode.left or currNode.right):
                totalSum += currVal
            else:
                if currNode.left:
                    nodeQueue.appendleft((currNode.left, 10 * currVal + currNode.left.val))
                if currNode.right:
                    nodeQueue.appendleft((currNode.right, 10 * currVal + currNode.right.val))
        
        return totalSum