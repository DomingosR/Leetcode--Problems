class Solution(object):
    def pairSum(self, head):
        # Handle trivial cases, of lists with no more than one element
        if not (head and head.next):
            return True
        
        # Idea: maintain two pointers, node1 (which will cover the first half of the list
        # in reverse order) and node2 (which will eventually cover the second half).
        # As we run through the first half of the list, we reverse it to perform the comparison
        # later
        node1 = head
        node2 = head.next
        prev = None
        
        while node2.next and node2.next.next:
            current = node1
            node1 = node1.next
            current.next = prev
            prev = current
            
            node2 = node2.next.next
        
        # Make sure that node2 points to the beginning of the second
        # half of the list, and node1 points to the previous node
        node2 = node1.next
        node1.next = prev
        
        # Compute maximum twin sum
        maxVal = 0
        while node2:
            maxVal = max(maxVal, node1.val + node2.val)
            node1 = node1.next
            node2 = node2.next
        
        return maxVal