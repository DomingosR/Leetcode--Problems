class Solution(object):
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        if n == 1:
            return matrix[0][0]

        prevRow, currRow = matrix[0], matrix[1]

        for i in range(n-1):
            for j in range(n):
                currRow[j] += min(prevRow[max(j-1,0):min(j+2,n)])
            if i < n-2:
                prevRow, currRow = currRow, matrix[i+2]

        return min(currRow)
