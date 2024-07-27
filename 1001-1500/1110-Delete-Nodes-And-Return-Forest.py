class Solution(object):
    def delNodes(self, root, to_delete):
        deleteVals = set(to_delete)
        remainingRoots = []
        
        def processNode(node, isRoot):
            if not node:
                return
            
            if node.val in deleteVals:
                processNode(node.left, True)
                processNode(node.right, True)
                node.left = None
                node.right = None
                
            else:
                processNode(node.left, False)
                processNode(node.right, False)
                if node.left and node.left.val in deleteVals:
                    node.left = None
                if node.right and node.right.val in deleteVals:
                    node.right = None
                if isRoot:
                    remainingRoots.append(node)
                    
        processNode(root, True)
        return remainingRoots