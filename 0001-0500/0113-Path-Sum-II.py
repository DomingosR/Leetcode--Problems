class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        allPaths = []
        currentPath = []
        
        def processNode(node, currentSum):
            currentPath.append(node.val)
            currentSum += node.val
            
            if not (node.left or node.right):
                if currentSum == targetSum:
                    presentPath = currentPath.copy()
                    allPaths.append(presentPath)
            else:
                if node.left:
                    processNode(node.left, currentSum)
                if node.right: 
                    processNode(node.right, currentSum)
            currentPath.pop()
            
        processNode(root, 0)
        return allPaths