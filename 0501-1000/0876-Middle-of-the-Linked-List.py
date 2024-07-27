class Solution(object):
    def middleNode(self, head):
        if not head.next:
            return head

        slow, fast = head, head.next

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow.next
        
