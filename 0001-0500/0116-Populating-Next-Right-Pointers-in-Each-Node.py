def createNextPointers(root):
    def dfs(inputNode):
        if inputNode.left != None:
            inputNode.left.next = inputNode.right
            if inputNode.next != None:
                inputNode.right.next = inputNode.next.left
            else:
                inputNode.right.next = None
            
            dfs(inputNode.left)
            dfs(inputNode.right)
    
    if root is None:
        return None
    
    root.next = None
    dfs(root)
    
    return root

class Solution(object):
    def connect(self, root):
        return createNextPointers(root)