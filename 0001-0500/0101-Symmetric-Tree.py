class Solution(object):
    def isSymmetric(self, root):
        def compareTrees(node1, node2):
            if node1 and node2:
                if node1.val == node2.val:
                    return compareTrees(node1.left, node2.right) and compareTrees(node2.left, node1.right)
                else:
                    return False
            elif node1 or node2:
                return False
            return True
        
        return compareTrees(root, root)