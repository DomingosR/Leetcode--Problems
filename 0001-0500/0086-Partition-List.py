class Solution(object):
    def partition(self, head, x):
        if head == None:
            return None

        startBefore = None
        startAfter = None
        currentNode = head
        i = 0

        while currentNode:
            if currentNode.val < x:
                if startBefore  == None:
                    startBefore = currentNode
                else:
                    currentBefore.next = currentNode
                currentBefore = currentNode
            else:
                if startAfter == None:
                    startAfter = currentNode
                else:
                    currentAfter.next = currentNode
                currentAfter = currentNode

            currentNode = currentNode.next

        if startAfter == None:
            currentBefore.next = None
            return startBefore

        if startBefore == None:
            currentAfter.next = None
            return startAfter

        currentBefore.next = startAfter
        currentAfter.next = None
        return startBefore
