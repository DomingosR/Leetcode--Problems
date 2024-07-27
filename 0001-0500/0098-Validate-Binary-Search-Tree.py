def checkBSTIsValid(root):
    def dfs(node, minVal, maxVal):
        if node.val > maxVal or node.val < minVal:
            return False

        validLeft, validRight = True, True
        if node.left != None:
            validLeft = dfs(node.left, minVal, node.val)
        if validLeft and node.right != None:
            validRight = dfs(node.right, node.val, maxVal)

        if not (validLeft and validRight):
            return False
        return minVal < node.val < maxVal

    return dfs(root, float('-inf'), float('inf'))

class Solution(object):
    def isValidBST(self, root):
        return checkBSTIsValid(root)
