class Solution(object):
    def maxIncreasingCells(self, mat):
        m = len(mat)
        n = len(mat[0])
        cellsForVal = defaultdict(list)

        for i in range(m):
            for j in range(n):
                cellsForVal[mat[i][j]].append((i, j))
        
        maxLen = [[0] * n for _ in range(m)]
        maxForRow = [0] * m
        maxForCol = [0] * n
        overallMax = 0
        
        for val in sorted(cellsForVal):
            for i, j in cellsForVal[val]:
                maxLen[i][j] = max(maxForRow[i], maxForCol[j]) + 1
                overallMax = max(overallMax, maxLen[i][j])
            for i, j in cellsForVal[val]:
                maxForRow[i] = max(maxForRow[i], maxLen[i][j])
                maxForCol[j] = max(maxForCol[j], maxLen[i][j])

        return overallMax