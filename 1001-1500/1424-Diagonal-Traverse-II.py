class Solution(object):
    def findDiagonalOrder(self, nums):
        auxNums = []
        for i, row in enumerate(nums):
            for j, indNum in enumerate(row):
                if i+j >= len(auxNums):
                    auxNums.append([])
                auxNums[i+j].append(indNum)
        
        return [num for i in range(len(auxNums)) for num in reversed(auxNums[i])]