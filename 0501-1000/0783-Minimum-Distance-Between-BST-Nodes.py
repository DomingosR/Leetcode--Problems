class Solution(object):
    def minDiffInBST(self, root):
        values = []

        def getVal(node):
            values.append(node.val)
            if node.left:
                getVal(node.left)
            if node.right:
                getVal(node.right)
            return

        getVal(root)
        values.sort()

        return min([values[i+1] - values[i] for i in range(len(values)-1)])
