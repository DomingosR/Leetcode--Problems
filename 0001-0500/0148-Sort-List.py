class Solution(object):
    def sortList(self, head):
        nodeValues = []
        currentNode = head

        while currentNode:
            nodeValues.append(currentNode.val)
            currentNode = currentNode.next
        
        nodeValues.sort()
        i = 0
        currentNode = head

        while currentNode:
            currentNode.val = nodeValues[i]
            i += 1
            currentNode = currentNode.next
        
        return head