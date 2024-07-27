class Solution(object):
    def maxProduct(self, root):
        sumDict = set()

        def dfs(node):
            nodeSum = node.val
            if node.left:
                nodeSum += dfs(node.left)
            if node.right:
                nodeSum += dfs(node.right)
            
            if node != root:
                sumDict.add(nodeSum)
            
            return nodeSum
        
        totalSum = dfs(root)
        targetVal = totalSum / 2.0
        
        sum1 = min(sumDict, key = lambda x: abs(x - targetVal))
        sum2 = totalSum - sum1

        return (sum1 * sum2) % (10**9+7)