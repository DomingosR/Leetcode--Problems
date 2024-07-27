class Solution(object):
    def kthSmallest(self, root, k):
        countLeft = [k]
        returnVal = [-1]     
        
        def processNode(node):
            if countLeft[0] == 0:
                return
            
            if node.left:
                processNode(node.left)
             
            if countLeft[0] == 0:
                return
            
            if countLeft[0] == 1:
                returnVal[0] = node.val
                countLeft[0] -= 1
                return
            
            countLeft[0] -= 1
            if node.right:
                processNode(node.right)
        
        processNode(root)
        
        return returnVal[0]