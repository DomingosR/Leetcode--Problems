class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        if upper + lower != sum(colsum):
            return []
        
        i, j, n = 0, 0, len(colsum)
        matrix = [[0] * n for _ in range(2)]
        remainingUpper, remainingLower = upper, lower
        
        for j in range(n):
            if colsum[j] == 2:
                matrix[0][j] = 1
                matrix[1][j] = 1
                remainingUpper -= 1
                remainingLower -= 1
                
                if remainingUpper < 0 or remainingLower < 0:
                    return []
                
        for j in range(n):
            if colsum[j] == 1:
                if remainingUpper:
                    matrix[0][j] = 1
                    remainingUpper -= 1
                else:
                    matrix[1][j] = 1
        
        return matrix