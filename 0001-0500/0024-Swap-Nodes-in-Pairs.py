class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        currentNode = head
        nextNode = head.next
        followingNode = nextNode.next
        returnNode = nextNode

        nextNode.next = currentNode
        currentNode.next = followingNode

        while followingNode and followingNode.next:
            previousNode = currentNode
            currentNode = followingNode
            nextNode = currentNode.next
            followingNode = nextNode.next

            previousNode.next = nextNode
            nextNode.next = currentNode
            currentNode.next = followingNode

        return returnNode
