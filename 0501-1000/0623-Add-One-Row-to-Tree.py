class Solution(object):
    def addOneRow(self, root, val, depth):
        if depth == 1:
            newNode = TreeNode(val)
            newNode.left = root
            return newNode        
        
        nodeQueue = deque()
        nodeQueue.appendleft((root, 1))
        
        while nodeQueue:
            currNode, currLevel = nodeQueue.pop()
            if currLevel < depth - 1:
                if currNode.left:
                    nodeQueue.appendleft((currNode.left, currLevel + 1))
                if currNode.right:
                    nodeQueue.appendleft((currNode.right, currLevel + 1))
                    
            if currLevel == depth - 1:
                newNode = TreeNode(val)
                if currNode.left:    
                    newNode.left = currNode.left
                currNode.left = newNode

                newNode = TreeNode(val)
                if currNode.right:
                    newNode.right = currNode.right
                currNode.right = newNode
                    
        return root