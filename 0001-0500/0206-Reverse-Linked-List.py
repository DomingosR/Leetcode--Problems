class Solution(object):
    def reverseList(self, head):
        if not head:
            return None
        
        previousNode = None
        currentNode = head
        
        while currentNode.next:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
        
        currentNode.next = previousNode
        
        return currentNode