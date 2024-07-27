class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        
        traversal = []
        
        def processNode(node):
            if node.left: 
                processNode(node.left)
            if node.right:
                processNode(node.right)
            traversal.append(node.val)
            
        processNode(root)
        return traversal