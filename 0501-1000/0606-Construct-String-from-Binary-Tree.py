class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        finalStr = ""

        def processNode(node):
            nonlocal finalStr
            finalStr += str(node.val)
            if node.left:
                finalStr += "("
                processNode(node.left)
                finalStr += ")"
            if node.right:
                if not node.left:
                    finalStr += "()"
                finalStr += "("
                processNode(node.right)
                finalStr += ")"    

        processNode(root)
        return finalStr          