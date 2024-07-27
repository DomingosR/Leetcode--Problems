class Solution(object):
    def generateTrees(self, n):
        def newTree(rootVal, leftNode, rightNode):
            newNode = TreeNode(rootVal)
            newNode.left = leftNode
            newNode.right = rightNode
            return newNode

        def allTrees(lowVal, highVal):
            if lowVal > highVal:
                return [None]

            return [newTree(i, leftNode, rightNode) \
                    for i in range(lowVal, highVal + 1) \
                    for leftNode in allTrees(lowVal, i-1) \
                    for rightNode in allTrees(i+1, highVal) ]

        return allTrees(1, n)
        
