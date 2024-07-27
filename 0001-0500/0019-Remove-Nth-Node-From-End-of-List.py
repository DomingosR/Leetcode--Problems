class Solution(object):
    def removeNthFromEnd(self, head, n):
        firstPtr = head
        for _ in range(n):
            firstPtr = firstPtr.next

        if not firstPtr:
            return head.next

        secondPtr = head
        while firstPtr.next:
            firstPtr = firstPtr.next
            secondPtr = secondPtr.next

        secondPtr.next = secondPtr.next.next
        return head
