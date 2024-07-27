class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        ptr1 = list1
        for _ in range(a - 1):
            ptr1 = ptr1.next
            
        ptr2 = ptr1
        for _ in range(b - a + 2):
            ptr2 = ptr2.next
            
        ptr1.next = list2
        current = list2
        
        while current.next:
            current = current.next
        
        current.next = ptr2
        
        return list1