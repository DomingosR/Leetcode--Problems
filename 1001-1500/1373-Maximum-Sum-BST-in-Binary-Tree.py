# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxSumBSSubtree(inputNode):
    currentVal = inputNode.val # Value of current node
    maxSum = 0                 # Maximum sum of nodes in a valid subtree
    totalSum = currentVal      # Total sum of nodes below this one
    maxVal = currentVal        # Maximum node value in subtree
    minVal = currentVal        # Minimum node value in subtree
    isValidSubtree = 1         # Is this a valid Binary Search Tree?

    if inputNode.left != None:
        maxSum_L, totalSum_L, maxVal_L, minVal_L, isValidSubtree_L = maxSumBSSubtree(inputNode.left)
        totalSum += totalSum_L
        if (maxVal_L >= currentVal) or (isValidSubtree_L == 0):
            isValidSubtree = 0
            maxSum = max(maxSum, maxSum_L)
        else:
            minVal = minVal_L
            maxSum = max(maxSum, maxSum_L)

    if inputNode.right != None:
        maxSum_R, totalSum_R, maxVal_R, minVal_R, isValidSubtree_R = maxSumBSSubtree(inputNode.right)
        totalSum += totalSum_R
        if (minVal_R <= currentVal) or (isValidSubtree_R == 0):
            isValidSubtree = 0
            maxSum = max(maxSum, maxSum_R)
        else:
            maxVal = maxVal_R
            maxSum = max(maxSum, maxSum_R)

    if isValidSubtree == 1:
        maxSum = max(maxSum, totalSum)

    return maxSum, totalSum, maxVal, minVal, isValidSubtree

class Solution(object):
    def maxSumBST(self, root):
        return maxSumBSSubtree(root)[0]
