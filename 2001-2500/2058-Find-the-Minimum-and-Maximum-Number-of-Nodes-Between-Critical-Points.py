class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        first, last = -1, -1
        minDiff = float('inf')
        i = 1
        currentNode = head

        while currentNode.next and currentNode.next.next:
            val1, val2, val3 = currentNode.val, currentNode.next.val, currentNode.next.next.val
            if (val2 - val1) * (val2 - val3) > 0:
                if first < 0:
                    first = i
                if last > 0:
                    minDiff = min(minDiff,i - last)
                last = i
            i += 1
            currentNode = currentNode.next

        return [minDiff, last - first] if last > first else [-1, -1]