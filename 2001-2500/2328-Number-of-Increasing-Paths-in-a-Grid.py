class Solution(object):
    def countPaths(self, grid):
        p = 10 ** 9 + 7
        m = len(grid)
        n = len(grid[0])
        numPaths = [[1] * n for _ in range(m)]
        totalCount = 0
        directions = [1, 0, -1, 0, 1]
        
        for a, i, j in sorted([(grid[i][j], i, j) for i in range(m) for j in range(n)]):
            for k in range(4):
                x, y = i + directions[k], j + directions[k+1]
                if m > x >= 0 <= y < n and grid[x][y] < grid[i][j]:
                    numPaths[i][j] += numPaths[x][y]
            totalCount += (numPaths[i][j] % p)
        
        return (totalCount % p)