def ancestor(root, p, q):
    currentNode = root
    pVal, qVal = p.val, q.val
    
    while True:
        currentVal = currentNode.val
        testVal = (currentVal - pVal) * (currentVal - qVal)
        if testVal <= 0:
            return currentNode
        if currentVal > pVal:
            currentNode = currentNode.left
        else:
            currentNode = currentNode.right
        

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        return ancestor(root, p, q)