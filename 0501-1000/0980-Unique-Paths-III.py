class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        result = 0
        m = len(grid)
        n = len(grid[0])
        emptySquareCount = 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    startRow, startCol = (i, j)
                elif grid[i][j] == 0:
                    emptySquareCount += 1

        def dfs(i, j, emptySquareCount):
            nonlocal result
            if not (m > i >= 0 <= j < n and grid[i][j] >= 0): 
                return

            if grid[i][j] == 2:
                result += (emptySquareCount == 0)
                return

            grid[i][j] = -2
            for deltaI, deltaJ in directions:
                dfs(i + deltaI, j + deltaJ, emptySquareCount - 1)
            
            grid[i][j] = 0

        dfs(startRow, startCol, emptySquareCount)

        return result