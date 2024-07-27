class Solution(object):
    def allPossibleFBT(self, n):
        if n % 2 == 0:
            return []

        preComputed = {1: [TreeNode(0)]}

        if n not in preComputed:
            returnVal = []
            for i in range(1, n-1, 2):
                for leftTree in self.allPossibleFBT(i):
                    for rightTree in self.allPossibleFBT(n-i-1):
                        root = TreeNode(0, leftTree, rightTree)
                        returnVal += [root]
            preComputed[n] = returnVal

        return preComputed[n]
