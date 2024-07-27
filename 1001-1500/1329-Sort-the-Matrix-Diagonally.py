def sortMatrixDiagonally(inputMat):
    m = len(inputMat)
    n = len(inputMat[0])
    
    # First, sort diagonals that start in the leftmost column
    for i in range(m):
        upperLimit = min(n, m-i)
        tempMat = [0] * upperLimit
        for k in range(upperLimit):
            tempMat[k] = inputMat[i+k][k]
        tempMat.sort()
        for k in range(upperLimit):
            inputMat[i+k][k] = tempMat[k]
            
    # Next, sort diagonals that start in the first row
    for j in range(1, n):
        upperLimit = min(m, n-j)
        tempMat = [0] * upperLimit
        for k in range(upperLimit):
            tempMat[k] = inputMat[k][j+k]
        tempMat.sort()
        for k in range(upperLimit):
            inputMat[k][j+k] = tempMat[k]            
      
    return inputMat

class Solution(object):
    def diagonalSort(self, mat):
        return sortMatrixDiagonally(mat)