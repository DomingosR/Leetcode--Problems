class Solution(object):
    def removeZeroSumSublists(self, head):
        priorNode = ListNode(0)
        priorNode.next = head
        currentNode, currentSum = head, 0
        sumLocation = {0: priorNode}
        
        while currentNode:
            currentSum += currentNode.val
            sumLocation[currentSum] = currentNode
            currentNode = currentNode.next
            
        currentNode, currentSum = priorNode, 0
        while currentNode:
            currentSum += currentNode.val
            currentNode.next = sumLocation[currentSum].next
            currentNode = currentNode.next
            
        return priorNode.next