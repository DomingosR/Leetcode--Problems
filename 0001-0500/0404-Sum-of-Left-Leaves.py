class Solution(object):
    def sumOfLeftLeaves(self, root):
        sumLeftLeaves = 0
        nodeQueue = deque()
        nodeQueue.appendleft(root)
        
        while nodeQueue:
            currNode = nodeQueue.pop()
            if currNode.left:
                if not (currNode.left.left or currNode.left.right):
                    sumLeftLeaves += currNode.left.val
                nodeQueue.appendleft(currNode.left)
            if currNode.right:
                nodeQueue.appendleft(currNode.right)
                
        return sumLeftLeaves