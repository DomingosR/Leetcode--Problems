class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        if fast.next:
            slow = slow.next

        secondPart = slow.next
        slow.next = None

        prev, curr = None, secondPart

        while curr:
            foll = curr.next
            curr.next = prev
            prev = curr
            curr = foll

        secondPart = prev
        firstPart = head
        
        while secondPart:
            foll1, foll2 = firstPart.next, secondPart.next
            firstPart.next = secondPart
            secondPart.next = foll1
            firstPart = foll1
            secondPart = foll2