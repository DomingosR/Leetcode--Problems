class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        
        def processNode(node, traversalOrder):
            if node.left:
                traversalOrder = processNode(node.left, traversalOrder)
            traversalOrder += [node.val]
            if node.right:
                traversalOrder = processNode(node.right, traversalOrder)
            return traversalOrder
        
        return processNode(root, [])