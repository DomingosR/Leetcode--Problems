class Solution(object):
    def evaluateTree(self, root):
        def evalNode(node):
            if node.val == 0:
                return False
            if node.val == 1:
                return True
            if node.val == 2:
                return evalNode(node.left) or evalNode(node.right)
            return evalNode(node.left) and evalNode(node.right)
        
        return evalNode(root)