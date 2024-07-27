class Solution(object):
    def isBalanced(self, root):
        def heightNode(node):
            if not node:
                return 0
            return max(heightNode(node.left), heightNode(node.right)) + 1
        
        def isBalanced(node):
            if not node:
                return True
            if not (isBalanced(node.left) and isBalanced(node.right)):
                return False
            return abs(heightNode(node.left) - heightNode(node.right)) <= 1
        
        return isBalanced(root)