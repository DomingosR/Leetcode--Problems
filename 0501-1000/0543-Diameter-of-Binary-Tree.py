class Solution(object):
    def diameterOfBinaryTree(self, root):
        def maxLen(node):
            maxPathCurrent = 0
            maxLenCurrent = 0
            
            if node.left:
                maxLenLeft, maxPathLeft = maxLen(node.left)
                maxPathCurrent += maxLenLeft + 1
                maxLenCurrent = max(maxLenCurrent, maxLenLeft + 1)
            else:
                maxLenLeft, maxPathLeft = 0, 0
                
            if node.right:
                maxLenRight, maxPathRight = maxLen(node.right)
                maxPathCurrent += maxLenRight + 1
                maxLenCurrent = max(maxLenCurrent, maxLenRight + 1)
            else:
                maxLenRight, maxPathRight = 0, 0
             
            maxPathCurrent = max(maxPathLeft, maxPathRight, maxPathCurrent)
            return (maxLenCurrent, maxPathCurrent)
        
        return maxLen(root)[1]