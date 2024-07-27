class Solution(object):
    def maximumSafenessFactor(self, grid):
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0

        n = len(grid)
        cellQueue = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    cellQueue.appendleft((i, j, 1))

        while cellQueue:
            i, j, currDist = cellQueue.pop()
            for dI, dJ in directions:
                nextI, nextJ = i + dI, j + dJ
                if n > nextI >= 0 <= nextJ < n and grid[nextI][nextJ] == 0:
                    grid[nextI][nextJ] = currDist + 1
                    cellQueue.appendleft((nextI, nextJ, currDist + 1))

        cellHeap = []
        heappush(cellHeap, (-grid[0][0], 0, 0))
        grid[0][0] *= -1

        while cellHeap:
            currDist, i, j = heappop(cellHeap)
            currDist *= -1
            if i == j == n-1:
                return currDist - 1
            for dI, dJ in directions:
                nextI, nextJ = i + dI, j + dJ
                if n > nextI >= 0 <= nextJ < n and grid[nextI][nextJ] > 0:
                    nextDist = min(grid[nextI][nextJ], currDist)
                    heappush(cellHeap, (-nextDist, nextI, nextJ))
                    grid[nextI][nextJ] *= -1
