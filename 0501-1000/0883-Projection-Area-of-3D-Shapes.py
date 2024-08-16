class Solution(object):
    def projectionArea(self, grid):
        n = len(grid)
        countGrid = [len([1 for j in range(n) if grid[i][j] > 0]) for i in range(n)]
        maxGrid = [max(grid[i]) for i in range(n)]
        gridT = list(map(list, zip(*grid))) 
        maxGridT = [max(gridT[i]) for i in range(n)]
        return sum(countGrid) + sum(maxGrid) + sum(maxGridT)