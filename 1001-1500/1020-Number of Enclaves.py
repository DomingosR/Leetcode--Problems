class Solution(object):
    def numEnclaves(self, grid):
        m = len(grid)
        n = len(grid[0])
        directions = [0, 1, 0, -1, 0]
        
        def dfs(i, j):
            if m > i >= 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = 0
                for k in range(4):
                    dfs(i + directions[k], j + directions[k+1])
        
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
            
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)
        
        return sum([sum(grid[i]) for i in range(m)])