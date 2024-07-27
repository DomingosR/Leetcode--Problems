class Solution(object):
    def findMode(self, root):
        valueCount = Counter()
        
        def dfs(node):
            if not node:
                return
            valueCount[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        maxCount = max(valueCount.values())
        
        return [i for i in valueCount.keys() if valueCount[i] == maxCount]