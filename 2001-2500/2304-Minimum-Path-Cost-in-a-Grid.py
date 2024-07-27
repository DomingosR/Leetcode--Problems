class Solution(object):
    def minPathCost(self, grid, moveCost):
        m = len(grid)
        n = len(grid[0])
        
        currentCost = grid[0]
        
        for i in range(m-1):
            nextCost = [100 * m + 1] * n
            for j in range(n):
                currentVal = grid[i][j]
                for k in range(n):
                    altCost = currentCost[j] + moveCost[currentVal][k] + grid[i+1][k]
                    nextCost[k] = min(nextCost[k], altCost)
            currentCost = nextCost
        
        return min(currentCost)