class Solution(object):
    def findBall(self, grid):
        numRows = len(grid)
        numCols = len(grid[0])
        
        def exitColumn(j):
            for i in range(numRows):
                nextJ = j + grid[i][j]
                if nextJ < 0 or nextJ >= numCols or grid[i][j] != grid[i][nextJ]:
                    return -1
                j = nextJ
            return j
        
        return map(exitColumn, range(numCols))