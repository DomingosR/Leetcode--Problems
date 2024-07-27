class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not (list1 and list2):
            return list1 if list1 else list2
        
        if list1.val > list2.val:
            list1, list2 = list2, list1
        
        currentPointer = list1
        pointer1 = list1.next
        pointer2 = list2

        while pointer1 and pointer2:
            if pointer1.val <= pointer2.val:
                currentPointer.next = pointer1
                pointer1 = pointer1.next
            else:
                currentPointer.next = pointer2
                pointer2 = pointer2.next
            currentPointer = currentPointer.next
        
        if pointer1:
            currentPointer.next = pointer1

        if pointer2:
            currentPointer.next = pointer2
        
        return list1