class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return None
        
        current = head
        
        while current:
            subsequent = current.next
            while subsequent and subsequent.val == current.val:
                subsequent = subsequent.next
            current.next = subsequent
            current = subsequent
            
        return head
        