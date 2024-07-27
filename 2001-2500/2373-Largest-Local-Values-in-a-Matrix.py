class Solution(object):
    def largestLocal(self, grid):
        n = len(grid)
        localMax = [[0 for j in range(n-2)] for i in range(n-2)]

        for i in range(1, n-1):
            for j in range(1, n-1):
                localMax[i-1][j-1] = max([grid[row][col] for col in range(j-1, j+2) for row in range(i-1, i+2)])
        
        return localMax