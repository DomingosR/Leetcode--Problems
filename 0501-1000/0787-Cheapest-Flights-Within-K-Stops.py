class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0
        
        flightCost = defaultdict(dict)
        for u, v, cost in flights:
            flightCost[u][v] = cost
            
        costHeap = [(0, src, k+1)]                 # Entries are the form totalCost, location, numFlights left
        visited = [0] * n                          # Flights left when vertex visited
        
        while costHeap:
            cost, u, k = heapq.heappop(costHeap)
            if u == dst:
                return cost
            if visited[u] >= k:
                continue
            visited[u] = k
            if k > 0:
                for v, cost_v in flightCost[u].items():
                    heapq.heappush(costHeap, (cost + cost_v, v, k-1))
            
        return -1 