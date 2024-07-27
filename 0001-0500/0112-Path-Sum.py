class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        nodeQueue = deque()
        nodeQueue.appendleft((root, root.val))
        
        while nodeQueue:
            nextNode = nodeQueue.pop()
            currentNode = nextNode[0]
            currentVal = nextNode[1]
            
            if currentNode.left:
                nodeQueue.appendleft((currentNode.left, currentVal + currentNode.left.val))
            if currentNode.right:
                nodeQueue.appendleft((currentNode.right, currentVal + currentNode.right.val))
            if currentNode.left == None and currentNode.right == None:
                if currentVal == targetSum:
                    return True
                
        return False  