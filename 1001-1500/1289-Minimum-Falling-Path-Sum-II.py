class Solution(object):
    def minFallingPathSum(self, grid):
        n = len(grid)

        if n == 1:
            return grid[0][0]

        for i in range(1, n):
            minVal1, minVal2 = heapq.nsmallest(2, grid[i-1])
            for j in range(n):
                grid[i][j] += minVal2 if grid[i-1][j] == minVal1 else minVal1

        return min(grid[n-1])
