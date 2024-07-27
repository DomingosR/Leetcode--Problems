class Solution(object):
    def maxTrailingZeros(self, grid):
        m, n = len(grid), len(grid[0])
        
        def numFactors(num):
            num1 = num
            count2 = 0
            while num1 % 2 == 0:
                count2 += 1
                num1 //= 2
                
            num2 = num
            count5 = 0
            while num2 % 5 == 0:
                count5 += 1
                num2 //= 5
                
            return [count2, count5]
        
        def maxZeros(i, j):
            above, below, left, right = [0, 0], [0, 0], [0, 0], [0, 0]
            
            above[0] = cumCol[i][j+1][0]        
            above[1] = cumCol[i][j+1][1] 
            
            below[0] = cumCol[-1][j+1][0] - cumCol[i+1][j+1][0]
            below[1] = cumCol[-1][j+1][1] - cumCol[i+1][j+1][1]
            
            left[0] = cumRow[i+1][j+1][0]
            left[1] = cumRow[i+1][j+1][1]
            
            right[0] = cumRow[i+1][-1][0] - cumRow[i+1][j][0]
            right[1] = cumRow[i+1][-1][1] - cumRow[i+1][j][1]
            
            zerosTopLeft = min(above[0] + left[0], above[1] + left[1])
            zerosTopRight = min(above[0] + right[0], above[1] + right[1])
            zerosBottomLeft = min(below[0] + left[0], below[1] + left[1])
            zerosBottomRight = min(below[0] + right[0], below[1] + right[1])
            zerosRow = min(cumRow[i+1][-1])
            zerosCol = min(cumCol[-1][j+1])
            
            return max(zerosTopLeft, zerosTopRight, zerosBottomLeft, zerosBottomRight, zerosRow, zerosCol)
            
        cumRow = [[[0, 0]] * (n+1) for _ in range(m+1)]
        cumCol = [[[0, 0]] * (n+1) for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                count2, count5 = numFactors(grid[i][j])
                cumRow[i+1][j+1] = [cumRow[i+1][j][0] + count2, cumRow[i+1][j][1] + count5]
                cumCol[i+1][j+1] = [cumCol[i][j+1][0] + count2, cumCol[i][j+1][1] + count5]
        
        return max([maxZeros(i, j) for i in range(m) for j in range(n)])