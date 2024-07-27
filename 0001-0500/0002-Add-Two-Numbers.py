class Solution(object):
    def addTwoNumbers(self, l1, l2):
        answerHead = ListNode(0)
        currentNode = answerHead

        firstTerm = l1
        secondTerm = l2

        while firstTerm or secondTerm:
            if firstTerm:
                currentNode.val += firstTerm.val
                firstTerm = firstTerm.next
            if secondTerm:
                currentNode.val += secondTerm.val
                secondTerm = secondTerm.next
            
            if currentNode.val >= 10:
                currentNode.val -= 10
                currentNode.next = ListNode(1)
                currentNode = currentNode.next
            else:
                if firstTerm or secondTerm:
                    currentNode.next = ListNode(0)
                    currentNode = currentNode.next
        
        return answerHead