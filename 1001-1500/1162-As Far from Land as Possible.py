class Solution(object):
    def maxDistance(self, grid):
        m = len(grid)
        n = len(grid[0])
        cellQueue = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cellQueue.appendleft((i, j, 0))

        if len(cellQueue) in set([0, m*n]):
            return -1

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while cellQueue:
            queueLen = len(cellQueue)
            for _ in range(queueLen):
                i, j, currentSteps = cellQueue.pop()
                for DeltaI, DeltaJ in directions:
                    nextI = i + DeltaI
                    nextJ = j + DeltaJ
                    if m > nextI >= 0 <= nextJ < n and grid[nextI][nextJ] == 0:
                        grid[nextI][nextJ] = 1
                        cellQueue.appendleft((nextI, nextJ, currentSteps + 1))

        return currentSteps