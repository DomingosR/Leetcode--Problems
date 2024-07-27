class Solution(object):
    def doubleIt(self, head):
        if head.val >= 5:
            head = ListNode(0, head)

        currentNode = head
        while currentNode:
            currentNode.val = (2 * currentNode.val % 10)
            if currentNode.next and currentNode.next.val >= 5:
                currentNode.val += 1
            currentNode = currentNode.next

        return head
