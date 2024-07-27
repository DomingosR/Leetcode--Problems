class Solution(object):
    def closedIsland(self, grid):
        m = len(grid)
        n = len(grid[0])
        directions = [0, 1, 0, -1, 0]
        numIslands = 0
        
        def dfsFloodEdge(i, j):
            if m > i >= 0 <= j < n and grid[i][j] == 0:
                grid[i][j] = 1
                for k in range(4):
                    dfsFloodEdge(i + directions[k], j + directions[k+1])
        
        def dfsCountIslands(i, j):
            for k in range(4):
                nextI, nextJ = i + directions[k], j + directions[k+1]
                if m > nextI >= 0 <= nextJ < n and grid[nextI][nextJ] == 0:
                    grid[nextI][nextJ] = 1
                    dfsCountIslands(nextI, nextJ)
        
        edgeCells = {(i, 0) for i in range(m)} | {(i, n-1) for i in range(m)} | {(0, j) for j in range(1, n-1)} | {(m-1, j) for j in range(1, n-1)}
        
        for i, j in edgeCells:
            dfsFloodEdge(i, j)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    numIslands += 1
                    grid[i][j] = 1
                    dfsCountIslands(i, j)
                    
        return numIslands