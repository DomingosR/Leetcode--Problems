class Solution(object):
    def diagonalSum(self, mat):
        n = len(mat)
        diagonalSum = 0

        for i in range(n):
            diagonalSum += mat[i][i] + mat[n-1-i][i]

        if n % 2 == 1:
            diagonalSum -= mat[n//2][n//2]
        
        return diagonalSum