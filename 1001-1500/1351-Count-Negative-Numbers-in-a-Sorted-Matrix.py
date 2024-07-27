class Solution(object):
    def countNegatives(self, grid):
        m, n = len(grid), len(grid[0])
        i, j = 0, n-1
        negativeCount = 0
        
        while i < m:
            if grid[i][j] >= 0:
                negativeCount += n-j-1
            else:
                while j > 0 and grid[i][j-1] < 0:
                    j -= 1
                negativeCount += n-j
            i+= 1
    
        return negativeCount