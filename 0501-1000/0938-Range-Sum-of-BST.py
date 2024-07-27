class Solution(object):
    def rangeSumBST(self, root, low, high):
        rangeSum = 0

        def processNode(node):
            nonlocal rangeSum
            if low <= node.val <= high:
                rangeSum += node.val

            if node.val >= low and node.left:
                processNode(node.left)

            if node.val <= high and node.right:
                processNode(node.right)

        processNode(root)
        return rangeSum
