class Solution(object):
    def searchBST(self, root, val):
        currentNode = root
        
        while currentNode:
            if currentNode.val == val:
                return currentNode
            if currentNode.val > val:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
            
        return None