class Solution(object):
    def longestIncreasingPath(self, grid):
        m = len(grid)
        n = len(grid[0])
        longestPaths = [[1] * n for _ in range(m)]
        overallLongest = 1
        directions = [1, 0, -1, 0, 1]
        
        for a, i, j in sorted([(grid[i][j], i, j) for i in range(m) for j in range(n)]):
            for k in range(4):
                newI, newJ = i + directions[k], j + directions[k+1]
                if m > newI >= 0 <= newJ < n and grid[newI][newJ] < grid[i][j]:
                    longestPaths[i][j] = max(longestPaths[i][j], longestPaths[newI][newJ]+1)
            overallLongest = max(overallLongest, longestPaths[i][j])
        
        return overallLongest