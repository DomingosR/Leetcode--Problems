class Solution(object):
    def lastStoneWeight(self, stones):
        stonesAux = [-stone for stone in stones]
        heapq.heapify(stonesAux)

        while len(stonesAux) >= 2:
            stone1 = heapq.heappop(stonesAux)
            stone2 = heapq.heappop(stonesAux)

            if stone1 != stone2:
                heapq.heappush(stonesAux, stone1 - stone2)

        if len(stonesAux) == 1:
            return -stonesAux[0]
        else:
            return 0
