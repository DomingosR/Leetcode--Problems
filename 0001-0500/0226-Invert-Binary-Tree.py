class Solution(object):
    def invertTree(self, root):
        def invertNodes(node):
            if node:
                node.left, node.right = node.right, node.left
                if node.left:
                    invertNodes(node.left)
                if node.right:
                    invertNodes(node.right)
        
        invertNodes(root)
        return root