class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return None
        
        nodeCount = 1
        currNode = head
        
        while currNode.next:
            nodeCount += 1
            currNode = currNode.next
        
        lastNode = currNode
        k %= nodeCount
        
        if k == 0:
            return head
        
        currNode = head
        for _ in range(nodeCount - k - 1):
            currNode = currNode.next
            
        lastNode.next = head
        head = currNode.next
        currNode.next = None
        
        return head