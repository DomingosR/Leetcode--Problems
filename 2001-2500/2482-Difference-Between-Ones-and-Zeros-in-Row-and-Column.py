class Solution(object):
    def onesMinusZeros(self, grid):
        m, n = len(grid), len(grid[0])
        gridT = list(map(list, zip(*grid)))
        rowDiff, colDiff = [0] * m, [0] * n
        diffMat = [[0] * n for _ in range(m)]

        for i in range(m):
            rowDiff[i] = 2 * sum(grid[i]) - n

        for j in range(n):
            colDiff[j] = 2 * sum(gridT[j]) - m

        for i, j in product(range(m), range(n)):
            diffMat[i][j] = rowDiff[i] + colDiff[j]

        return diffMat