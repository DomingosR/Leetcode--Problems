class Solution(object):
    def getMaximumGold(self, grid):
        m, n = len(grid), len(grid[0])
        maxCoins = [0]
        directions = [1, 0, -1, 0, 1]
        
        def processCell(i, j, currentCoins):
            if m > i >= 0 <= j < n and grid[i][j] > 0:
                currentCoins += grid[i][j]
                grid[i][j] *= -1
                maxCoins[0] = max(maxCoins[0], currentCoins)
                
                for k in range(4):
                    nextI, nextJ = i + directions[k], j + directions[k+1]
                    processCell(nextI, nextJ, currentCoins)
                
                grid[i][j] *= -1
                
        for i in range(m):
            for j in range(n):
                processCell(i, j, 0)
                
        return maxCoins[0]