class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        distances = [[float("inf")] * n for _ in range(n)]
        
        for u in range(n):
            distances[u][u] = 0
        
        for u, v, dist in edges:
            distances[u][v] = dist
            distances[v][u] = dist
            
        for w in range(n):
            for u in range(n):
                for v in range(n):
                    distances[u][v] = min(distances[u][v], distances[u][w] + distances[w][v])
                        
        rowCount = [sum([1 for v in range(n) if distances[u][v] <= distanceThreshold]) for u in range(n)]
        minCount = min(rowCount)
        minIndices = [u for u in range(n) if rowCount[u] == minCount]
        return max(minIndices)