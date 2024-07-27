class Solution(object):
    def removeLeafNodes(self, root, target):
        def processNode(node):
            if node.left and processNode(node.left):
                node.left = None
            if node.right and processNode(node.right):
                node.right = None
            if node.left or node.right or node.val != target:
                return False
            return True

        return None if processNode(root) else rootfc