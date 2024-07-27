class Solution(object):
    def swapNodes(self, head, k):
        currentNode = head
        for _ in range(k-1):
            currentNode = currentNode.next
            
        node1 = currentNode
        node2 = head
        
        while currentNode.next:
            node2 = node2.next
            currentNode = currentNode.next
        
        node1.val, node2.val = node2.val, node1.val
        
        return head