class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        countGood = 0

        def dfs(currentNode, currentMax):
            nonlocal countGood
            if currentMax <= currentNode.val:
                countGood += 1
            adjustedMax = max(currentMax, currentNode.val)

            if currentNode.left:
                dfs(currentNode.left, adjustedMax)
            if currentNode.right:
                dfs(currentNode.right, adjustedMax)

        dfs(root, root.val)
        return countGood        