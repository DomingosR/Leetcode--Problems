class Solution(object):
    def getDirections(self, root, startValue, destValue):
        pathStart, pathEnd = [], []
        
        def findNode(value, node, path):
            if not node:
                return False
            
            if node.val == value:
                return True
            
            if findNode(value, node.left, path):
                path.append("L")
                return True
            
            if findNode(value, node.right, path):
                path.append("R")
                return True
            
            return False
        
        findNode(startValue, root, pathStart)
        findNode(destValue, root, pathEnd)
        
        while pathStart and pathEnd and pathStart[-1] == pathEnd[-1]:
            pathStart.pop()
            pathEnd.pop()
            
        return "U" * len(pathStart) + "".join(pathEnd)[::-1]