class Solution(object):
    def longestZigZag(self, root):
        def dfs(node):
            maxBelow = 0
            if node.left:
                _, val2, val3 = dfs(node.left)
                leftLen = 1 + val2
                maxBelow = max(maxBelow, leftLen, val3)
            else:
                leftLen = 0
            
            if node.right:
                val1, _, val3 = dfs(node.right)
                rightLen = 1 + val1
                maxBelow = max(maxBelow, rightLen, val3)                
            else:
                rightLen = 0
            
            
            return [leftLen, rightLen, maxBelow]
        
        return max(dfs(root))