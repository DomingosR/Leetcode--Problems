class Solution(object):
    def countHighestScoreNodes(self, parents):
        class TreeNode:
            def __init__(self, val):
                self.val = val
                self.left = None
                self.right = None
        
        n = len(parents)
        treeNodes = [TreeNode(i+1) for i in range(n)]
        root = treeNodes[0]

        for i in range(1, n):
            parent = parents[i]
            if treeNodes[parent].left:
                treeNodes[parent].right = treeNodes[i]
            else:
                treeNodes[parent].left = treeNodes[i]
        
        scoreCount = defaultdict(int)
                       
        def processNode(node):
            if not node:
                return 0
            
            leftVal = processNode(node.left)
            rightVal = processNode(node.right)
            remainingVal = max(n - 1 - leftVal - rightVal, 1)
            score = max(leftVal, 1) * max(rightVal, 1) * remainingVal
            scoreCount[score] += 1
                       
            return leftVal + rightVal + 1
            
        processNode(root)
        
        return scoreCount[max(scoreCount.keys())]