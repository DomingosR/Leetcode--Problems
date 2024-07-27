class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False

        slowPointer, fastPointer = head, head
        
        while fastPointer.next and fastPointer.next.next:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
            if slowPointer == fastPointer:
                return True
        
        return False