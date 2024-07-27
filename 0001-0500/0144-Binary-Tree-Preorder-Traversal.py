class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []

        traversal = []

        def dfs(node):
            if not node:
                return
            traversal.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return traversal