class Solution(object):
    def minCostConnectPoints(self, points):
        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(points)
        distances = collections.defaultdict(list)

        for i in range(n):
            for j in range(i+1, n):
                dist = distance(points[i], points[j])
                distances[i].append((dist, j))
                distances[j].append((dist, i))

        visitedCount = 1
        totalDist = 0
        visited = [0] * n
        auxHeap = distances[0]

        visited[0] = 1
        heapq.heapify(auxHeap)

        while auxHeap and visitedCount < n:
            currentDist, j = heapq.heappop(auxHeap)
            if not visited[j]:
                visited[j] = 1
                visitedCount += 1
                totalDist += currentDist
                for nextPoint in distances[j]: 
                    visited[nextPoint[1]] == 0 and heapq.heappush(auxHeap, nextPoint)
        
        return totalDist