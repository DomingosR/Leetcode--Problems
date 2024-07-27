class Solution(object):
    def isPalindrome(self, head):
        # Handle trivial cases, of lists with no more than one element
        if not (head and head.next):
            return True
        
        # Idea: maintain two pointers, node1 (which will cover the first half of the list)
        # and node2 (which will eventually cover the second half).  As we run through the
        # first half of the list, we reverse the first half of the list for comparison
        node1 = head
        node2 = head.next
        prev = None
        
        while node2.next and node2.next.next:
            # *** Still have to reverse the direction of nodes in the first half here ***
            current = node1
            node1 = node1.next
            current.next = prev
            prev = current
            
            node2 = node2.next.next
            
        # If at this stage node2 has a successor, the list has an odd number of elements
        if node2.next:
            node2 = node1.next.next
        else:
            node2 = node1.next
        
        # Make sure that node1 now points to the previous node
        node1.next = prev
        
        # Check the two halves of the list
        while node2:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
        
        return True