def reverseFirstK(inputList, k):
    firstNode = inputList
    currentNode = firstNode
    i = 0

    while (currentNode.next != None) and (i < k-1):
        currentNode = currentNode.next
        i += 1

    if i == k-1:
        currentNode = firstNode
        nextNode = currentNode.next
        i = 0

        while i < k-1:
            followingNode = nextNode.next
            nextNode.next = currentNode
            currentNode = nextNode
            nextNode = followingNode
            i += 1

        firstNode.next = nextNode
        lastNode = firstNode
        firstNode = currentNode
        return firstNode, lastNode

    else:
        return firstNode, None

def reverseKAtATime(inputList, k):
    if k==1:
        return inputList

    currentFirst, currentLast = reverseFirstK(inputList, k)

    while currentLast != None:
        if currentLast.next != None:
            newFirst, newLast = reverseFirstK(currentLast.next, k)
            currentLast.next = newFirst
            currentLast = newLast
        else:
            currentLast = None

    return currentFirst

class Solution(object):
    def reverseKGroup(self, head, k):
        return reverseKAtATime(head, k)