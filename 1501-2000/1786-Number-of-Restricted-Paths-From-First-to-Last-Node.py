class Solution(object):
    def countRestrictedPaths(self, n, edges):
        p = 10 ** 9 + 7
        
        #Build graph
        neighbors = defaultdict(list)
        
        for u, v, w in edges:
            neighbors[u].append((v, w))
            neighbors[v].append((u, w))
        
        
        # Compute distance to last vertex
        distanceToLast = defaultdict(int)
        distanceToLast[n] = 0
        vertexHeap = [(0, n)]
        
        while vertexHeap:
            dist, u = heappop(vertexHeap)
            if dist == distanceToLast[u]:
                for v, w in neighbors[u]:
                    if distanceToLast.get(v, float('inf')) > dist + w:
                        distanceToLast[v] = dist + w
                        heapq.heappush(vertexHeap, (dist + w, v))
        
        # Function to compute number of restricted paths
        numPaths = defaultdict(int)
        numPaths[n] = 1
        
        def restrictedPathCount(u):
            if u not in numPaths:
                pathCount = 0
                for v, _ in neighbors[u]:
                    if distanceToLast[v] < distanceToLast[u]:
                        pathCount = (pathCount + restrictedPathCount(v)) % p        
                numPaths[u] = pathCount
                
            return numPaths[u]
            
        return restrictedPathCount(1)