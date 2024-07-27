class Solution(object):
    def deleteMiddle(self, head):
        if not head.next:
            return None
        
        pointer1 = head
        pointer2 = head.next

        while pointer2.next != None and pointer2.next.next != None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next

        pointer1.next = pointer1.next.next
        
        return head