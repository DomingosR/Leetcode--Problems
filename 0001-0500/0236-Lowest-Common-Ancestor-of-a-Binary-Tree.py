def commonAncestor(initialNode, p, q):
    if initialNode in (None, p, q): return initialNode
    left = commonAncestor(initialNode.left, p, q)
    right = commonAncestor(initialNode.right, p, q)    
    if left and right:
        return initialNode
    else:
        return left or right

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        return commonAncestor(root, p, q)