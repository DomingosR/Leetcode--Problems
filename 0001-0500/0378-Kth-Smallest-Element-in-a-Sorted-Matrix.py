import heapq

def getKthSmallest(matrix, k):
    valuesHeap = []
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            currentVal = - matrix[i][j]
            if len(valuesHeap) < k:
                heapq.heappush(valuesHeap, currentVal)
            elif currentVal > valuesHeap[0]:
                heapq.heappushpop(valuesHeap, currentVal)

    return - valuesHeap[0]

class Solution(object):
    def kthSmallest(self, matrix, k):
        return getKthSmallest(matrix, k)
