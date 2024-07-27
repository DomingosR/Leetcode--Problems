class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return None
        
        priorNode = ListNode(head.val - 1)
        priorNode.next = head
        
        currentNode = priorNode
        
        while currentNode.next:
            if (not currentNode.next.next) or (currentNode.next.next.val != currentNode.next.val):
                currentNode = currentNode.next
            else:
                findNode, findVal = currentNode.next, currentNode.next.val
                while findNode and findNode.val == findVal:
                    findNode = findNode.next
                currentNode.next = findNode
                
        return priorNode.next
                