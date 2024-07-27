class Solution(object):
    def luckyNumbers (self, matrix):
        m, n = len(matrix), len(matrix[0])
        matrixT = list(map(list, zip(*matrix)))
        
        minRowVal = [min(matrix[i]) for i in range(m)]
        maxColVal = [max(matrixT[j]) for j in range(n)]
        
        minRowIndices = [[j for j in range(n) if matrix[i][j] == minRowVal[i]] for i in range(m)]
        maxColIndices = [[i for i in range(m) if matrix[i][j] == maxColVal[j]] for j in range(n)]
        
        luckyNumbers = [matrix[i][j] for i in range(m) for j in range(n) \
                                     if i in maxColIndices[j] \
                                     and j in minRowIndices[i]]
        
        return list(set(luckyNumbers))