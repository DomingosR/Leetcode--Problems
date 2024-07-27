class Solution(object):
    def balanceBST(self, root):
        inOrderTraversal = []
        
        def processNode(node):
            if node.left:
                processNode(node.left)
            inOrderTraversal.append(node.val)
            if node.right:
                processNode(node.right)
                
        processNode(root)
        
        n = len(inOrderTraversal)
        
        def buildTree(leftIndex, rightIndex):
            if rightIndex < leftIndex:
                return None
            
            midIndex = leftIndex + (rightIndex - leftIndex) // 2
            newNode = TreeNode(inOrderTraversal[midIndex])
            newNode.left = buildTree(leftIndex, midIndex - 1)
            newNode.right = buildTree(midIndex + 1, rightIndex)
            
            return newNode
        
        return buildTree(0, n-1)