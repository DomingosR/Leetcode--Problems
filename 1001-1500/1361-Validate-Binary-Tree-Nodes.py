class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        parents = [0] * n

        for left, right in zip(leftChild, rightChild):
            if left  > -1: parents[left]  += 1
            if right > -1: parents[right] += 1
            if parents[left] > 1 or parents[right] > 1: return False
        
        if parents.count(0) != 1: return False

        rootNode = parents.index(0)

        def countDescendants(indNode):
            if indNode == -1: return 0
            return 1 + countDescendants(leftChild[indNode]) + countDescendants(rightChild[indNode])

        return countDescendants(rootNode) == n