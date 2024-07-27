class Solution(object):
    def bstToGst(self, root):
        def processNode(node, addedValue):
            sumRight = processNode(node.right, addedValue) if node.right else 0
            sumLeft = processNode(node.left, addedValue + sumRight + node.val) if node.left else 0
            totalSum = node.val + sumRight + sumLeft
            node.val += (addedValue + sumRight)
            return totalSum
        
        processNode(root, 0)
        return root