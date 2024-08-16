class Solution(object):
    def matrixReshape(self, mat, r, c):
        m, n = len(mat), len(mat[0])
        
        if m * n != r * c:
            return mat
        
        newMat = [[0] * c for _ in range(r)]
        i, j, i1, j1 = 0, 0, 0, 0
        
        while i < m:
            newMat[i1][j1] = mat[i][j]
            
            if j == n-1:
                i += 1
                j = 0
            else:
                j += 1
                
            if j1 == c-1:
                i1 += 1
                j1 = 0
            else:
                j1 += 1
        
        return newMat