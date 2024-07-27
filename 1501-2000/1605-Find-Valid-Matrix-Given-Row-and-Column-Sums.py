class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        m, n = len(rowSum), len(colSum)
        matrix = [[0] * n for _ in range(m)]
        i, j = 0, 0
        
        while i < m and j < n:
            currentVal = min(rowSum[i], colSum[j])
            matrix[i][j] = currentVal
            rowSum[i] -= currentVal
            colSum[j] -= currentVal
            if rowSum[i] == 0:
                i += 1
            if colSum[j] == 0:
                j += 1
                
        return matrix