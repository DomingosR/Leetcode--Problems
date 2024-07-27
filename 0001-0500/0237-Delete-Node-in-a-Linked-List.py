class Solution(object):
    def deleteNode(self, node):
        currentNode = node
        
        while currentNode.next:
            currentNode.val = currentNode.next.val
            if currentNode.next.next:
                currentNode = currentNode.next
            else:
                currentNode.next = None