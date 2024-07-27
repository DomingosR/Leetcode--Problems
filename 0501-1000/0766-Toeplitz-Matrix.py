class Solution(object):
    def isToeplitzMatrix(self, matrix):
        numRows = len(matrix)

        for i in range(numRows-1):
            if matrix[i][:-1] != matrix[i+1][1:]:
                return False

        return True
