class Solution(object):
    def shortestBridge(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Find the first 1 in the grid
        i = 0
        while not 1 in grid[i]:
            i += 1
        j = grid[i].index(1)

        # Mark cells in this first islands as 2,
        # and adjacent water cells as 3
        seen = [[0] * n for _ in range(m)]
        seen[i][j] = 1
        islandQueue = deque()
        waterQueue = deque()
        islandQueue.appendleft((i, j))
        changes = {(1, 0), (0, 1), (-1, 0), (0, -1)}

        while islandQueue:
            i, j = islandQueue.pop()
            seen[i][j] = 1
            grid[i][j] = 2

            for dI, dJ in changes:
                nextI, nextJ = i + dI, j + dJ
                if m > nextI >= 0 <= nextJ < n:
                    seen[nextI][nextJ] = 1
                    if grid[nextI][nextJ] == 1:
                        grid[nextI][nextJ] = 2
                        islandQueue.appendleft((nextI, nextJ))
                    else:
                        grid[nextI][nextJ] = 3
                        waterQueue.appendleft((nextI, nextJ, 3))

        # Start breadth-first search from water cells
        while waterQueue:
            i, j, level = waterQueue.pop()
            for dI, dJ in changes:
                nextI, nextJ = i + dI, j + dJ
                if m > nextI >= 0 <= nextJ < n and seen[nextI][nextJ] == 0:
                    seen[nextI][nextJ] = 1
                    if grid[nextI][nextJ] == 1:
                        return level - 2
                    if grid[nextI][nextJ] == 0:
                        grid[nextI][nextJ] = 1
                        waterQueue.appendleft((nextI, nextJ, level + 1))

        return -1
