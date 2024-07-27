class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def processNode(node):
            if node.left:
                (leftCount, leftSum, leftNum) = processNode(node.left)
            else:
                leftCount, leftSum, leftNum = 0, 0, 0
            
            if node.right:
                (rightCount, rightSum, rightNum) = processNode(node.right)
            else:
                rightCount, rightSum, rightNum = 0, 0, 0
                
            currentSum = leftSum + rightSum + node.val
            currentCount = leftCount + rightCount + 1
            currentNum = leftNum + rightNum + (1 if node.val == currentSum // currentCount else 0)
            
            return (currentCount, currentSum, currentNum)
            
        return processNode(root)[2]