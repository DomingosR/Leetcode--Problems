class Solution(object):
    def getRow(self, rowIndex):
        pascalRow = [1]

        for i in range(1, rowIndex + 1):
            nextNum = (pascalRow[-1] * (rowIndex + 1 - i)) // i
            pascalRow.append(nextNum)
        
        return pascalRow