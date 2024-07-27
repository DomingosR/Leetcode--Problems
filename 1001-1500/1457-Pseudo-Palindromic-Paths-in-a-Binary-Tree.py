class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def processNode(node, currentMask):
            if not node:
                return 0
            
            updatedMask = currentMask ^ (1 << (node.val - 1))
            if not (node.left or node.right):
                return 1 if updatedMask & (updatedMask - 1) == 0 else 0
            return processNode(node.left, updatedMask) + processNode(node.right, updatedMask)
        
        return processNode(root, 0)