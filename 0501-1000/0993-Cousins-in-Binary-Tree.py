class Solution(object):
    def isCousins(self, root, x, y):
        foundX, foundY = False, False
        depthX, parentX = -1, -1
        depthY, parentY = -1, -1
        nodeQueue = deque([(root, 0, -1)])
        
        while not (foundX and foundY):
            currentNode, currentDepth, currentParent = nodeQueue.pop()
            if currentNode.val == x:
                foundX = True
                depthX, parentX = currentDepth, currentParent
            if currentNode.val == y:
                foundY = True
                depthY, parentY = currentDepth, currentParent    
                
            if currentNode.left:
                nodeQueue.appendleft((currentNode.left, currentDepth + 1, currentNode.val))
            if currentNode.right:
                nodeQueue.appendleft((currentNode.right, currentDepth + 1, currentNode.val))
                
        return depthX == depthY and parentX != parentY
        