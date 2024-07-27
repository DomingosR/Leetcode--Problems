class Solution(object):
    def buildTree(self, inorder, postorder):
        inOrderLocations = {}

        for i, val in enumerate(inorder):
            inOrderLocations[val] = i

        def recursion(lowVal, highVal):
            if lowVal > highVal:
                return None
            
            currentNode = TreeNode(postorder.pop())
            midVal = inOrderLocations[currentNode.val]
            currentNode.right = recursion(midVal + 1, highVal)
            currentNode.left = recursion(lowVal, midVal - 1)
            return currentNode
        
        return recursion(0, len(inorder) - 1)