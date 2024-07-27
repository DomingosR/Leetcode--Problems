class Solution(object):
    def minStoneSum(self, piles, k):
        auxPiles = [-piles[i] for i in range(len(piles))]
        heapq.heapify(auxPiles)

        for i in range(k):
            nextNum = -heapq.heappop(auxPiles)
            if nextNum == 0:
                return 0
            
            heapq.heappush(auxPiles, - nextNum + (nextNum // 2))

        return -sum(auxPiles)