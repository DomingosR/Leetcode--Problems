class Solution(object):
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        firstRowZeroed = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i == 0:
                        firstRowZeroed = 1
                    else:
                        matrix[i][0] = 0              
        
        for i in range(m-1, -1, -1):
            if i == 0:
                if firstRowZeroed:
                    for j in range(n-1, -1, -1):
                        matrix[i][j] = 0
            else:
                for j in range(n-1, -1, -1):
                    matrix[i][j] = (0 if matrix[i][0] * matrix[0][j] == 0 else matrix[i][j])
                    
        return matrix