class Solution(object):
    def pathSum(self, root, targetSum):
        if not root:
            return 0

        prevPathSums = defaultdict(int)
        prevPathSums[0] = 1
        totalNumPaths = [0]

        def processNode(node, prevPathSum):
            currPathSum = prevPathSum + node.val
            totalNumPaths[0] += prevPathSums[currPathSum - targetSum]
            prevPathSums[currPathSum] += 1

            if node.left:
                processNode(node.left, currPathSum)
            if node.right:
                processNode(node.right, currPathSum)

            prevPathSums[currPathSum] -= 1

        processNode(root, 0)
        return totalNumPaths[0]
