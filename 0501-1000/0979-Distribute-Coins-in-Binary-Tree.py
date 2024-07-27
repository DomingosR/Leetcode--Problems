class Solution(object):
    def distributeCoins(self, root):
        totalMoves = [0]
        
        def processNode(node):
            if not node:
                return 0
            leftVal, rightVal = processNode(node.left), processNode(node.right)
            totalMoves[0] += abs(leftVal) + abs(rightVal)
            return leftVal + rightVal + node.val - 1
            
        processNode(root)
        return totalMoves[0]