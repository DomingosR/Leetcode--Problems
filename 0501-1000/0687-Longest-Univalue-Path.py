class Solution(object):
    def longestUnivaluePath(self, root):
        if not root:
            return 0

        def dfs(node):
            # Returns a pair (maxLenEnding, maxLenNotEnding), where:
            # > maxLenEnding is the length of the longest path in node's subtree that ends in node
            # > maxLenNotEnding is the length of the longest path in node's subtree that does not end in node
            maxLenEnding = 0
            maxLenNotEnding = 0

            if node.left:
                (maxLenEndingLeft, maxLenNotEndingLeft) = dfs(node.left)
                maxLenNotEnding = max(maxLenNotEnding, maxLenNotEndingLeft, maxLenEndingLeft)
                if node.val == node.left.val:
                    maxLenEnding = max(maxLenEnding, maxLenEndingLeft + 1)

            if node.right:
                (maxLenEndingRight, maxLenNotEndingRight) = dfs(node.right)
                maxLenNotEnding = max(maxLenNotEnding, maxLenNotEndingRight, maxLenEndingRight)
                if node.val == node.right.val:
                    maxLenEnding = max(maxLenEnding, maxLenEndingRight + 1)
                
            if node.left and node.right and node.val == node.left.val == node.right.val:
                maxLenNotEnding = max(maxLenNotEnding, maxLenEndingLeft + maxLenEndingRight + 2)
            
            return (maxLenEnding, maxLenNotEnding)
        
        (maxLenEnding, maxLenNotEnding) = dfs(root)
        return max(maxLenEnding, maxLenNotEnding)