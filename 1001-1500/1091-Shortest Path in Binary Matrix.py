class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        if n == 1:
            return 1
        
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        cellQueue = deque()
        cellQueue.appendleft((0, 0, 1))
        grid[0][0] = -1
        
        while cellQueue:
            currI, currJ, numCells = cellQueue.pop()
            for dI, dJ in directions:
                nextI, nextJ = currI + dI, currJ + dJ
                if n > nextI >= 0 <= nextJ < n and grid[nextI][nextJ] == 0:
                    if nextI == n-1 and nextJ == n-1:
                        return numCells + 1
                    cellQueue.appendleft((nextI, nextJ, numCells + 1))
                    grid[nextI][nextJ] = - numCells - 1
        
        return -1