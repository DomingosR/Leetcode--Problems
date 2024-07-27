class Solution(object):
    def detectCycle(self, head):
        if head == None:
            return None

        slowPointer, fastPointer, auxPointer = head, head, head
        cycleFound = False
        
        while fastPointer.next and fastPointer.next.next:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
            if slowPointer == fastPointer:
                cycleFound = True
                break
        
        if cycleFound:
            while auxPointer != slowPointer:
                auxPointer = auxPointer.next
                slowPointer = slowPointer.next
            return auxPointer
        
        return None