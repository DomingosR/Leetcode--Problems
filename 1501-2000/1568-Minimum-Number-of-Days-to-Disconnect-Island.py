class Solution(object):
    def minDays(self, grid):
        # Preliminaries
        m, n = len(grid), len(grid[0])
        neighbors = defaultdict(list)
        
        def cellIndex(i, j):
            return n * i + j
        
        # Build grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    currentCell = cellIndex(i, j)
                    neighbors[currentCell] = []    # This row ensures that currentCell is in neighbors,
					                               # even if it does not have any neighbors
                    if i < m - 1 and grid[i+1][j] == 1:
                        nextCell = cellIndex(i+1, j)
                        neighbors[currentCell].append(nextCell)
                        neighbors[nextCell].append(currentCell)
                    if j < n - 1 and grid[i][j+1] == 1:
                        nextCell = cellIndex(i, j+1)
                        neighbors[currentCell].append(nextCell)
                        neighbors[nextCell].append(currentCell)    
                        
        # Function to count islands
        def countIslands(vertexToExclude):
            UFParent = defaultdict(int)
            for u in neighbors.keys():
                if u != vertexToExclude:
                    UFParent[u] = u
            islandCount = [len(UFParent.keys())]

            def find(u):
                if UFParent[u] != u:
                    UFParent[u] = find(UFParent[u])
                return UFParent[u]

            def union(u, v):
                u, v = find(u), find(v)
                if u != v:
                    UFParent[v] = u
                    islandCount[0] -= 1

            for u in neighbors:
                if u != vertexToExclude:
                    for v in neighbors[u]:
                        if v > u and v != vertexToExclude:
                            union(u, v)
                        
            return islandCount[0]
        
        # Count islands with all vertices, return 0 if there is one
        if countIslands(-1) != 1:
            return 0
        
        # Otherwise, try excluding each vertex individually and check if there is only one island
        for u in neighbors.keys():
            if countIslands(u) != 1:
                return 1
        
        # Otherwise, return 2
        return 2