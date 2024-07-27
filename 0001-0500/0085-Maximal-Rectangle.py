class Solution(object):
    def maximalRectangle(self, matrix):
        if not (matrix and matrix[0]):
            return 0
        
        n = len(matrix[0])
        currHeight = [0] * (n + 1)
        maxArea = 0
        
        for row in matrix:
            for i in range(n):
                currHeight[i] = (currHeight[i] + 1) if row[i] == "1" else 0
                
            # Compute maximal area of rectangle ending in this row
            auxStack = [-1]
            for i in range(n + 1):
                while currHeight[i] < currHeight[auxStack[-1]]:
                    currH = currHeight[auxStack.pop()]
                    currW = i - 1 - auxStack[-1]
                    maxArea = max(maxArea, currH * currW)
                auxStack.append(i)
                
        return maxArea