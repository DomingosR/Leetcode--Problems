class Solution(object):
    def oddEvenList(self, head):
        if not head:
            return None

        if not head.next:
            return head

        oddHead = head
        evenHead = head.next
        currentOdd = oddHead
        currentEven = evenHead

        currentNode = head.next
        isNextOdd = 0

        while currentNode.next:
            currentNode = currentNode.next
            isNextOdd = 1 - isNextOdd
            if isNextOdd == 1:
                currentOdd.next = currentNode
                currentOdd = currentOdd.next
            else:
                currentEven.next = currentNode
                currentEven = currentEven.next

        currentOdd.next = evenHead
        currentEven.next = None
        return oddHead
