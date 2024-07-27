class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        m, n = len(matrix), len(matrix[0])
        if numSelect == n:
            return m
        
        rowBitCount = [sum(matrix[i]) for i in range(m)]
        
        nums = []
        for i in range(m):
            num = 0
            for j in range(n):
                num |= matrix[i][j]
                if j < n-1:
                    num <<= 1
            nums.append(num)

        maxRows = 0
        for bitMask in range(2 ** n):
            if bitMask.bit_count() <= numSelect:
                numRows = 0
                for i in range(len(nums)):
                    if (bitMask & nums[i]).bit_count() == rowBitCount[i]:
                        numRows += 1
                maxRows = max(maxRows, numRows)
            
        return maxRows