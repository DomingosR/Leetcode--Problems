def constructTree(inorder, preorder):
    def dfs(inArray):
        if not inArray:
            return None

        rootIndex = inArray.index(preorder.pop(0))
        root = TreeNode(inArray[rootIndex])
        root.left = dfs(inArray[:rootIndex])
        root.right = dfs(inArray[rootIndex + 1:])

        return root

    return dfs(inorder)

class Solution(object):
    def buildTree(self, preorder, inorder):
        return constructTree(inorder, preorder)