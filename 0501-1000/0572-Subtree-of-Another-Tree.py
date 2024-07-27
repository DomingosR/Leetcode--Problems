class Solution(object):
    def isSubtree(self, root, subRoot):
        subRootVal = subRoot.val
        
        def checkTrees(root1, root2):
            if root1 == root2 == None:
                return True
            if root1 == None or root2 == None:
                return False
            if root1.val == root2.val:
                return checkTrees(root1.left, root2.left) and checkTrees(root1.right, root2.right)
            
        nodeQueue = deque()
        nodeQueue.appendleft(root)
        
        while nodeQueue:
            currNode = nodeQueue.pop()
            if currNode.val == subRootVal and checkTrees(currNode, subRoot):
                return True
            if currNode.left:
                nodeQueue.appendleft(currNode.left)
            if currNode.right:
                nodeQueue.appendleft(currNode.right)
            
        return False