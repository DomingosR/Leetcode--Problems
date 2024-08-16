class Solution(object):
    def modifiedMatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])
        matrixT = list(map(list, zip(*matrix)))
        maxCol = [max(matrixT[i]) for i in range(n)]
        return [[(matrix[i][j] if matrix[i][j] != -1 else maxCol[j]) for j in range(n)] for i in range(m)]