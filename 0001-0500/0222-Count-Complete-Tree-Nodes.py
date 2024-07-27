class Solution(object):
    def countNodes(self, root):
        def getHeight(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        
        nodeCount = 0
        node = root
        while node:
            leftHeight = getHeight(node.left)
            rightHeight = getHeight(node.right)
            if leftHeight == rightHeight:
                nodeCount += 2**leftHeight
                node = node.right
            else:
                nodeCount += 2**rightHeight
                node = node.left
        
        return nodeCount