class Solution(object):
    def maximalSquare(self, matrix):
        matrix = [[0] * len(matrix[0])] + matrix
        for i in range(len(matrix)):
            matrix[i] = [0] + [int(matrix[i][j]) for j in range(len(matrix[i]))]
        
        m, n = len(matrix), len(matrix[0])
        maxLen = 0
        
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] += (matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1])
                
                k = min(i, j)
                while k > maxLen:
                    if matrix[i][j] - matrix[i-k][j] - matrix[i][j-k] + matrix[i-k][j-k] == k ** 2:
                        maxLen = k
                        break
                    k -= 1
        
        return maxLen ** 2