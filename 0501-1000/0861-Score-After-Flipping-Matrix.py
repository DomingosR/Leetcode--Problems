class Solution(object):
    def matrixScore(self, grid):
        m, n = len(grid), len(grid[0])
        totalSum = (1 << n-1) * m
        
        for j in range(1, n):
            numOnes = sum([grid[i][j] == grid[i][0] for i in range(m)])
            totalSum += (1 << n-1-j) * max(numOnes, m - numOnes)
            
        return totalSum