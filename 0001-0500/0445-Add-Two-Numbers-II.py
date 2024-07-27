class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def listToNum(node):
            num = 0
            currentNode = node
            while currentNode:
                num = 10 * num + currentNode.val
                currentNode = currentNode.next
            return num

        def numToList(num):
            if num == 0:
                currentNode = ListNode(0)
            else:
                currentNode = None
                while num:
                    currentVal = num % 10
                    prevNode = ListNode(currentVal)
                    prevNode.next = currentNode
                    currentNode = prevNode
                    num = num // 10

            return currentNode

        num1 = listToNum(l1)
        num2 = listToNum(l2)
        resultNum = num1 + num2
        return numToList(resultNum)
