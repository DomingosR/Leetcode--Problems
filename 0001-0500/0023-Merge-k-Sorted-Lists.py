class Solution(object):
    def mergeKLists(self, lists):
        k = len(lists)
        currentNodes = [lists[i] for i in range(k)]
        valueHeap = []

        for i in range(k):
            if currentNodes[i]:
                heappush(valueHeap, (currentNodes[i].val, i))
        
        if not valueHeap:
            return None

        currentVal, currentList = heappop(valueHeap)
        head = currentNodes[currentList]
        currentNode = head

        currentNodes[currentList] = currentNodes[currentList].next
        if currentNodes[currentList]:
            heappush(valueHeap, (currentNodes[currentList].val, currentList))
                
        while valueHeap:
            currentVal, currentList = heappop(valueHeap)
            currentNode.next = currentNodes[currentList]

            currentNodes[currentList] = currentNodes[currentList].next
            if currentNodes[currentList]:
                heappush(valueHeap, (currentNodes[currentList].val, currentList))

            currentNode = currentNode.next

        return head