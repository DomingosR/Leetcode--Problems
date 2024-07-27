def reverseGivenNodes(head, left, right):
    if left == right:
        return head

    # First, get a pointer to the node at position left
    # (and, if possible, to the previous node in the list)
    if left == 1:
        startNode = head
        precedingNode = None
    else:
        i = 1
        prevNode = head
        while i < left - 1:
            prevNode = prevNode.next
            i += 1

        precedingNode = prevNode
        startNode = prevNode.next

    # Begin reversing direction of links one at a time
    i = left
    currentNode = startNode
    nextNode = currentNode.next
    while i < right:
        followingNode = nextNode.next
        nextNode.next = currentNode
        currentNode = nextNode
        nextNode = followingNode
        i += 1

    if left == 1:
        head = currentNode
    else:
        precedingNode.next = currentNode

    startNode.next = nextNode
    return head

class Solution(object):
    def reverseBetween(self, head, left, right):
        return reverseGivenNodes(head, left, right)
