class Solution(object):
    def largestSubmatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        maxArea = 0
        
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
                    
        for i in range(m):
            matrix[i].sort(reverse = True)
            for j in range(n):
                maxArea = max(maxArea, matrix[i][j] * (j+1))
                
        return maxArea