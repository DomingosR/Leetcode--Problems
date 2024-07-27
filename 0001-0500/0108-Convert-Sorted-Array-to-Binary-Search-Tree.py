def BSTRootNode(nums):
    def dfs(numArray):
        numsCount = len(numArray)
        midVal = numsCount // 2
        node = TreeNode(numArray[midVal])
        if midVal > 0:
            node.left = dfs(numArray[:midVal])
        if midVal < numsCount - 1:
            node.right = dfs(numArray[midVal+1:])
        return node
    
    return dfs(nums)

class Solution(object):
    def sortedArrayToBST(self, nums):
        return BSTRootNode(nums)