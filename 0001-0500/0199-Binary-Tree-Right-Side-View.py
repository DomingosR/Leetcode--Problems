class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        
        rightSideView = []
        nodeQueue = deque()
        nodeQueue.appendleft((root, 0))
        
        while nodeQueue:
            currentNode, level = nodeQueue.pop()
            
            if not nodeQueue or (nodeQueue[-1][1] != level):
                rightSideView.append(currentNode.val)
            
            if currentNode.left:
                nodeQueue.appendleft((currentNode.left, level + 1))
                
            if currentNode.right:
                nodeQueue.appendleft((currentNode.right, level + 1)) 
                
        return rightSideView