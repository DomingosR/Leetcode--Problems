class Solution(object):
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        lowIndex, highIndex = 0, m * n - 1

        while lowIndex < highIndex:
            midIndex = (lowIndex + highIndex) // 2
            currVal = matrix[midIndex // n][midIndex % n]

            if currVal < target:
                lowIndex = midIndex + 1
            else:
                highIndex = midIndex

        return matrix[lowIndex // n][lowIndex % n] == target
