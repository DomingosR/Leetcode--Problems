class Solution(object):
    def getMinimumDifference(self, root):        
        lastVal = [-1]
        minDiff = [10**5 + 1]
        
        def getVal(node):
            if node.left: getVal(node.left)
            if lastVal[0] >= 0:
                minDiff[0] = min(minDiff[0], node.val - lastVal[0])
                lastVal[0] = node.val
            else:
                lastVal[0] = node.val
            if node.right: getVal(node.right)
        
        getVal(root) 
        return minDiff[0]