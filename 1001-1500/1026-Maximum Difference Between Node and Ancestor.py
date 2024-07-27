class Solution(object):
    def maxAncestorDiff(self, root):
        def dfs(node):
            minBelow = node.val
            maxBelow = node.val
            maxDiff = 0

            if node.left:
                [minLeft, maxLeft, diffLeft] = dfs(node.left)
                minBelow = min(minBelow, minLeft)
                maxBelow = max(maxBelow, maxLeft)
                maxDiff = max(maxDiff, diffLeft, abs(node.val - minBelow), abs(node.val - maxBelow))

            if node.right: 
                [minRight, maxRight, diffRight] = dfs(node.right)
                minBelow = min(minBelow, minRight)
                maxBelow = max(maxBelow, maxRight)
                maxDiff = max(maxDiff, diffRight, abs(node.val - minBelow), abs(node.val - maxBelow))

            return [minBelow, maxBelow, maxDiff]

        return dfs(root)[2]                