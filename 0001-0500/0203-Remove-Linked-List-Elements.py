class Solution(object):
    def removeElements(self, head, val):
        while head and head.val == val:
            head = head.next
            
        if not head:
            return None
            
        current = head
        while current:
            subsequent = current.next
            while subsequent and subsequent.val == val:
                subsequent = subsequent.next
            current.next = subsequent
            current = subsequent
            
        return head