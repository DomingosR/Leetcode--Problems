class Solution(object):
    def minimumTotal(self, triangle):
        numRows = len(triangle)
        
        for i in range(1, numRows):
            for j in range(i + 1):
                if j == 0:
                    triangle[i][0] += triangle[i-1][0]
                elif j == i:
                    triangle[i][i] += triangle[i-1][i-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
                    
        return min(triangle[-1])